#!/usr/bin/env python3
import random
import json
import socket, struct, hashlib, sys, time, secrets, threading
from accounts import get_or_create_user_id, load_accounts
from Character import (
    make_character_dict_from_tuple,
    build_login_character_list_bitpacked,
    build_paperdoll_packet,
    load_characters,
    save_characters
)
from BitUtils import BitBuffer
from Commands import handle_hotbar_packet, handle_masterclass_packet, handle_research_packet, handle_gear_packet, \
    handle_apply_dyes, handle_rune_packet, handle_change_look, handle_create_gearset, handle_name_gearset, \
    handle_apply_gearset, handle_update_equipment, magic_forge_packet, collect_forge_charm, start_forge_packet, \
    cancel_forge_packet, allocate_talent_points
from constants import EntType, DyeType, Entity, LinkUpdater
from WorldEnter import build_enter_world_packet, Player_Data_Packet
from bitreader import BitReader
from PolicyServer import start_policy_server
from static_server import start_static_server
from entity import Send_Entity_Data
from Entity_Data import load_npc_data_for_level
from level_config import DOOR_MAP, LEVEL_CONFIG

HOST = "127.0.0.1"
PORTS = [8080]
pending_world = {}
all_sessions = []

def build_handshake_response(sid):
    b = sid.to_bytes(2, "big")
    h = hashlib.md5(b + b"815bfb010cd7b1b4e6aa90abc7679028").hexdigest()
    payload = b + bytes.fromhex(h[:12])
    return struct.pack(">HH", 0x12, len(payload)) + payload

def new_transfer_token():
    while (t := secrets.randbits(16)) in pending_world:
        pass
    return t

class ClientSession:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.user_id = None
        self.char_list = []
        self.active_tokens = set()
        self.authenticated = False
        self.player_data = {}
        self.current_character = None
        self.current_level = None
        self.world_loaded = False
        self.spawned_npcs = []
        self.npc_states = {}
        self.entities = {}
        self.clientEntID = None
        self.running = True

    def attack_entity(self, attacker_id, target_id, damage):
            target_ent = self.entities.get(target_id)
            if not target_ent:
                print(f"[{self.addr}] [PKT0F] Target entity {target_id} not found")
                return
            target_ent["damage_taken"] = target_ent.get("damage_taken", 0) + damage
            target_ent["health_delta"] = -damage
            target_ent["attacker_id"] = attacker_id
            print(
                f"[{self.addr}] [PKT0F] NPC {target_id} attacked by {attacker_id}, damage={damage}, new HP {target_ent.get('hp', 0)}")
            update_packet = Send_Entity_Data(target_ent, is_player=False)
            for other_session in all_sessions:
                if other_session.world_loaded and other_session.current_level == self.current_level:
                    other_session.conn.sendall(struct.pack(">HH", 0x0F, len(update_packet)) + update_packet)
                    print(f"[{self.addr}] [PKT0F] Broadcasted NPC {target_id} update to {other_session.addr}")

    def Send_NPC_Updates(self):
        for ent_id, entity in self.entities.items():
            if not entity.get("is_player", False):
                entity["entState"] = 0
                update_packet = Send_Entity_Data(entity, is_player=False)
                self.conn.sendall(struct.pack(">HH", 0x0F, len(update_packet)) + update_packet)
                #print(f"[{self.addr}] [NPC Update] Sent 0x0F for NPC {ent_id}: state={entity['entState']}, pos=({entity['x']}, {entity['y']})")


    def stop(self):
        self.running = False
        self.cleanup()


    def get_entity(self, entity_id):
        """
        Retrieve an entity from session.entities by its ID.
        Returns the entity dictionary or None if not found.
        """
        return self.entities.get(entity_id)

    def issue_token(self, char):
        tk = new_transfer_token()
        pending_world[tk] = char
        self.active_tokens.add(tk)
        return tk

    def cleanup(self):
        try:
            self.conn.close()
        except:
            pass
        if self in all_sessions:
            all_sessions.remove(self)

def read_exact(conn, n):
    buf = b""
    while len(buf) < n:
        chunk = conn.recv(n - len(buf))
        if not chunk:
            return None
        buf += chunk
    return buf

def handle_client(session: ClientSession):
    def npc_update_loop():
        while session.running and session.world_loaded:
            session.Send_NPC_Updates()
            time.sleep(1)  # Update every 1 second
    conn, addr = session.conn, session.addr
    print("Connected:", addr)
    conn.settimeout(300)
    try:
        # Start NPC update thread
        threading.Thread(target=npc_update_loop, daemon=True).start()
        while True:
            hdr = read_exact(conn, 4)
            if not hdr:
                break
            pkt_id, length = struct.unpack(">HH", hdr)
            payload = read_exact(conn, length)
            if payload is None:
                break
            data = hdr + payload
            pkt = int(data.hex()[:4], 16)

            if pkt == 0x11:
                sid = int(data.hex()[8:12], 16) if len(data) >= 6 else 0
                conn.sendall(build_handshake_response(sid))

            elif pkt == 0x13:
                payload = data[8:]
                br = BitReader(payload)
                email = br.read_string().strip().lower()
                session.user_id = get_or_create_user_id(email)
                session.char_list = load_characters(session.user_id)
                try:
                    with open(f"saves/{session.user_id}.json", "r", encoding="utf-8") as f:
                        session.player_data = json.load(f)
                except FileNotFoundError:
                    session.player_data = {}
                session.authenticated = True
                conn.sendall(build_login_character_list_bitpacked(session.char_list))
            elif pkt == 0x14:
                br = BitReader(data[4:])
                _ = br.read_string()
                _ = br.read_string()
                email = br.read_string().strip().lower()
                _ = br.read_string()
                _ = br.read_string()
                accounts = load_accounts()
                user_id = accounts.get(email)
                if not user_id:
                    #print(f"[{session.addr}] Login failed—no account for {email}")
                    err = "Account not found".encode("utf-8")
                    err_pl = struct.pack(">H", len(err)) + err
                    conn.sendall(struct.pack(">HH", 0x1B, len(err_pl)) + err_pl)
                    continue
                session.user_id = user_id
                try:
                    with open(f"saves/{session.user_id}.json", "r", encoding="utf-8") as f:
                        session.player_data = json.load(f)
                except FileNotFoundError:
                    session.player_data = {}
                session.char_list = load_characters(user_id)
                session.authenticated = True
                conn.sendall(build_login_character_list_bitpacked(session.char_list))
                #print(f"[{session.addr}] Logged in {email} → user_id={user_id}, chars={len(session.char_list)}")

            elif pkt == 0x17:
                if not session.authenticated:
                    msg = "Please log in first".encode("utf-8")
                    pl = struct.pack(">H", len(msg)) + msg
                    conn.sendall(struct.pack(">HH", 0x1B, len(pl)) + pl)
                    continue
                br = BitReader(data[4:])
                tup = (
                    br.read_string(),
                    br.read_string(),
                    50,
                    br.read_string(),
                    br.read_string(),
                    br.read_string(),
                    br.read_string(),
                    br.read_string(),
                    br.read_bits(24),
                    br.read_bits(24),
                    br.read_bits(24),
                    br.read_bits(24),
                    None
                )
                new_char = make_character_dict_from_tuple(tup)
                session.char_list.append(new_char)
                save_characters(session.user_id, session.char_list)
                conn.sendall(build_login_character_list_bitpacked(session.char_list))
                pd = build_paperdoll_packet(new_char)
                conn.sendall(struct.pack(">HH", 0x1A, len(pd)) + pd)
                popup = "Character Successfully Created".encode("utf-8")
                pl = struct.pack(">HH", 0x1B, len(popup) + 2) + struct.pack(">H", len(popup)) + popup
                conn.sendall(pl)
            elif pkt == 0x19:
                name = BitReader(data[4:]).read_string()
                for c in session.char_list:
                    if c["name"] == name:
                        pd = build_paperdoll_packet(c)
                        conn.sendall(struct.pack(">HH", 0x1A, len(pd)) + pd)
                        break
                else:
                    conn.sendall(struct.pack(">HH", 0x1A, 0))

            elif pkt == 0x16:
                name = BitReader(data[4:]).read_string()
                for c in session.char_list:
                    if c["name"] == name:
                        session.current_character = name
                        current_level = c.get("CurrentLevel", "CraftTown")
                        session.current_level = current_level
                        c["user_id"] = session.user_id
                        tk = session.issue_token(c)
                        level_config = LEVEL_CONFIG.get(current_level, ("LevelsNR.swf/a_Level_NewbieRoad", 1, 1, False))
                        pkt_out = build_enter_world_packet(
                            transfer_token=tk,
                            old_level_id=0,
                            old_swf="",
                            has_old_coord=False,
                            old_x=0,
                            old_y=0,
                            host="127.0.0.1",
                            port=8080,
                            new_level_swf=level_config[0],
                            new_map_lvl=level_config[1],
                            new_base_lvl=level_config[2],
                            new_internal=current_level,
                            new_moment="",
                            new_alter="",
                            new_is_inst=level_config[3],
                            # spawn coords
                            new_has_coord=False,
                            new_x=0,
                            new_y=0,
                            # character dict for buildings
                            char=c
                        )
                        conn.sendall(pkt_out)
                        print("Transfer begin:", name, "tk=", tk, "level=", current_level)
                        break

            elif pkt == 0x1f:
                print ("pkt == 0x1f: used again  sending player data again for level transfer ")
                if len(data) < 8:
                    continue
                token = int.from_bytes(data[4:8], 'big')
                char = pending_world.pop(token, None)
                if char is None and len(pending_world) == 1:
                    fallback_token, fallback_char = next(iter(pending_world.items()))
                    char = fallback_char
                    token = fallback_token
                    pending_world.pop(fallback_token, None)
                session.active_tokens.discard(token)
                if char:
                    session.user_id = char["user_id"]
                    with open(f"saves/{session.user_id}.json", "r") as f:
                        session.player_data = json.load(f)
                    session.current_character = char["name"]
                    session.current_char_dict = char
                    session.current_level = char.get("CurrentLevel", "CraftTown")
                    session.entities[token] = {
                        "id": token,
                        "x": 360.0,
                        "y": 1458.99,
                        "z": 0.0,
                        "entState": Entity.const_6,
                        "is_player": True,
                        "name": char["name"],
                        "hp": char.get("hp", 100),
                        "max_hp": char.get("max_hp", 100)
                    }
                    welcome = Player_Data_Packet(char, transfer_token=token)
                    conn.sendall(welcome)
                    session.clientEntID = token
                    print(f"Welcome: {char['name']} (used token {token}) on level {session.current_level}")

            elif pkt == 0x7C:
                _, length = struct.unpack_from(">HH", data, 0)
                payload = data[4:4 + length]
                try:
                    msg = payload.decode("utf-8", errors="replace")
                except Exception:
                    msg = repr(payload)
                print(f"[{session.addr}] CLIENT ERROR (0x7C): {msg}")
            elif pkt == 0x41:
                if len(data) < 4:
                    continue
                payload_length = struct.unpack(">H", data[2:4])[0]
                if len(data) != 4 + payload_length:
                    continue
                payload = data[4:4 + payload_length]
                try:
                    br = BitReader(payload)
                    door_id = br.read_method_9()
                except Exception as e:
                    continue
                door_info = DOOR_MAP.get((session.current_level, door_id))
                bb = BitBuffer()
                bb.write_method_4(door_id)
                if door_info is None:
                    bb.write_method_91(1)
                    bb.write_method_13("")
                else:
                    if isinstance(door_info, str):
                        bb.write_method_91(1)
                        bb.write_method_13(door_info)
                    else:
                        bb.write_method_91(door_info)
                        bb.write_method_13("")
                payload = bb.to_bytes()
                response = struct.pack(">HH", 0x42, len(payload)) + payload
                conn.sendall(response)

            elif pkt == 0xA2:
                payload = data[4:]
                if len(payload) < 9:
                    continue
                br = BitReader(payload)
                client_elapsed = br.read_bits(32)
                drift_flag = bool(br.read_bits(1))
                system_elapsed = br.read_bits(32)
                bb = BitBuffer()
                bb.write_bits(client_elapsed, 32)
                bb.write_bits(0, 1)
                bb.write_bits(system_elapsed, 32)
                resp = struct.pack(">HH", 0xA2, len(bb.to_bytes())) + bb.to_bytes()
                session.conn.sendall(resp)


            elif pkt == 0x107:
                CAT_BITS = 3
                ID_BITS = 6
                PACK_ID = 1
                reward_map = {
                    0: ("MountLockbox01L01", True),  # Mount
                    1: ("Lockbox01L01", True),  # Pet
                    #2: ("GenericBrown", True),  # Egg
                    #3: ("CommonBrown", True),  # Egg
                    #4: ("OrdinaryBrown", True),  # Egg
                    #5: ("PlainBrown", True),  # Egg
                    6: ("RarePetFood", True),  # Consumable
                    7: ("PetFood", True),  # Consumable
                    #8: ("Lockbox01Gear", True),  # Gear (will crash if invalid)
                    9: ("TripleFind", True),  # Charm
                    10: ("DoubleFind1", True),  # Charm
                    11: ("DoubleFind2", True),  # Charm
                    12: ("DoubleFind3", True),  # Charm
                    13: ("MajorLegendaryCatalyst", True),  # Consumable
                    14: ("MajorRareCatalyst", True),  # Consumable
                    15: ("MinorRareCatalyst", True),  # Consumable
                    16: (None, False),  # Gold (3 000 000)
                    17: (None, False),  # Gold (1 500 000)
                    18: (None, False),  # Gold (750 000)
                    19: ("DyePack01Legendary", True),  # Dye‐pack
                }
                idx, (name, needs_str) = random.choice(list(reward_map.items()))
                bb = BitBuffer()
                bb.write_method_6(PACK_ID, CAT_BITS)
                bb.write_method_6(idx, ID_BITS)
                bb.write_bits(1 if needs_str else 0, 1)
                if needs_str:
                    bb.write_utf_string(name)
                payload = bb.to_bytes()
                packet = struct.pack(">HH", 0x108, len(payload)) + payload
                session.conn.sendall(packet)
                print(f"Lockbox reward: idx={idx}, name={name}, needs_str={needs_str}")
            elif pkt == 0xBA:
                payload = data[4:]
                br = BitReader(payload)
                entity_id = br.read_method_4()
                dyes_by_slot = {}
                for slot in range(1, EntType.MAX_SLOTS):
                    has_pair = br.read_bits(1)
                    if has_pair:
                        d1 = br.read_bits(DyeType.BITS)
                        d2 = br.read_bits(DyeType.BITS)
                        dyes_by_slot[slot - 1] = (d1, d2)
                preview_only = bool(br.read_bits(1))
                primary_dye = br.read_bits(DyeType.BITS) if br.read_bits(1) else None
                secondary_dye = br.read_bits(DyeType.BITS) if br.read_bits(1) else None
                print(f"[Dyes] entity={entity_id}, dyes={dyes_by_slot}, "
                      f"preview={preview_only}, shirt={primary_dye}, pants={secondary_dye}")
                handle_apply_dyes(session, entity_id, dyes_by_slot, preview_only, primary_dye, secondary_dye)

            elif pkt == 0x08:
                if session.world_loaded:
                    #print(f"[{session.addr}] World already loaded; skipping NPC spawn.")
                    continue
                try:
                    npcs = load_npc_data_for_level(session.current_level)
                    for npc in npcs:
                        payload = Send_Entity_Data(npc, is_player=False)
                        conn.sendall(struct.pack(">HH", 0x0F, len(payload)) + payload)
                        session.entities[npc["id"]] = npc
                        session.spawned_npcs.append(npc)
                    session.world_loaded = True
                    session.Send_NPC_Updates()  # Send initial NPC updates
                    #print(f"[{session.addr}] Spawned {len(npcs)} NPCs for level {session.current_level}")
                except Exception as e:
                    print(f"[{session.addr}] Error spawning NPCs: {e}")

            elif pkt == 0x07:
                if len(data) < 4:
                    #print(f"[{session.addr}] [PKT07] Invalid packet: too short, raw payload = {data.hex()}")
                    continue
                payload = data[4:]
                if len(payload) * 8 < 20:
                    #print(f"[{session.addr}] [PKT07] Payload too short: {len(payload)} bytes, raw payload = {payload.hex()}")
                    continue
                br = BitReader(payload, debug=False)
                try:
                    ent_id = br.read_method_4()
                    #print(f"[{session.addr}] [PKT07] Entity ID = {ent_id}, raw payload = {payload.hex()}")
                    if ent_id != session.clientEntID:
                        #print(f"[{session.addr}] [PKT07] Entity ID {ent_id} does not match clientEntID {session.clientEntID}")
                        continue
                    if ent_id not in session.entities:
                        session.entities[ent_id] = {
                            "x": 360.0,
                            "y": 1458.99,
                            "z": 0.0,
                            "entState": Entity.const_6,
                            "is_player": True
                        }
                    entity = session.entities[ent_id]
                    if br.remaining_bits() < 3:
                        #print(f"[{session.addr}] [PKT07] Not enough bits for dx: {br.remaining_bits()}")
                        continue
                    dx = br.read_method_45()
                    if br.remaining_bits() < 3:
                        #print(f"[{session.addr}] [PKT07] Not enough bits for dy: {br.remaining_bits()}")
                        continue
                    dy = br.read_method_45()
                    if br.remaining_bits() < 3:
                        #print(f"[{session.addr}] [PKT07] Not enough bits for frame_acc: {br.remaining_bits()}")
                        continue
                    frame_acc = br.read_method_45()
                    #print(f"[{session.addr}] [PKT07] Deltas → X={dx}, Y={dy}, FrameAcc={frame_acc}")
                    entity['x'] = entity.get('x', 360.0) + dx
                    entity['y'] = entity.get('y', 1458.99) + dy
                    entity['frame_acc'] = frame_acc
                    if br.remaining_bits() < 2:
                        #print(f"[{session.addr}] [PKT07] Not enough bits for entState: {br.remaining_bits()}")
                        continue
                    ent_state = br.read_method_6(Entity.const_316)
                    was_idle = entity.get('entState', Entity.const_6) == Entity.const_6 and not entity.get('was_falling', False)
                    was_active = entity.get('entState', Entity.const_6) == Entity.const_78
                    entity['entState'] = ent_state
                    #print(f"[{session.addr}] [PKT07] entState (2 bits) = {ent_state}")
                    if br.remaining_bits() < 5:
                        #print(f"[{session.addr}] [PKT07] Not enough bits for flags: {br.remaining_bits()}")
                        continue
                    flags = {
                        "left": bool(br.read_bit()),
                        "running": bool(br.read_bit()),
                        "jumping": bool(br.read_bit()),
                        "dropping": bool(br.read_bit()),
                        "backpedal": bool(br.read_bit())
                    }
                    entity.update(flags)
                    #print(f"[{session.addr}] [PKT07] Flags = {flags}")
                    if br.remaining_bits() < 1:
                        #print(f"[{session.addr}] [PKT07] Not enough bits for velocity flag: {br.remaining_bits()}")
                        continue
                    has_velocity = br.read_bit()
                    if has_velocity:
                        if br.remaining_bits() < 3:
                            #print(f"[{session.addr}] [PKT07] Not enough bits for velocity: {br.remaining_bits()}")
                            continue
                        raw_vy = br.read_method_45()
                        vy = raw_vy * LinkUpdater.VELOCITY_DEFLATE
                        if ent_state != Entity.const_6:
                            entity['velocity_y'] = vy
                            entity['surface'] = None
                        #print(f"[{session.addr}] [PKT07] Vertical velocity = {vy}")
                    else:
                        #print(f"[{session.addr}] [PKT07] No vertical velocity")
                         pass
                    if ent_state == Entity.const_6 and not was_idle:
                        entity['was_idle'] = True
                        if entity.get('is_player', False):
                            #print(f"[{session.addr}] [PKT07] Player entered idle state")
                             pass
                    if entity.get('was_falling', False):
                        entity['entState'] = Entity.const_6
                        entity['was_falling'] = False
                    if ent_state == Entity.const_78 and not was_active:
                        entity['state'] = 'active'
                    elif ent_state != Entity.const_78 and was_active:
                        entity['state'] = 'sleep'
                    session.entities[ent_id] = entity
                    #print(f"[{session.addr}] [PKT07] Updated entity {ent_id}: {entity}")
                    #print(f"[{session.addr}] [PKT07] Debug log: {br.get_debug_log()}")
                    for other_session in all_sessions:
                        if other_session != session and other_session.world_loaded and other_session.current_level == session.current_level:
                            update_packet = Send_Entity_Data(entity, is_player=True)
                            other_session.conn.sendall(struct.pack(">HH", 0x0F, len(update_packet)) + update_packet)
                            #print(f"[{session.addr}] [PKT07] Broadcasted update for entity {ent_id} to {other_session.addr}")
                except Exception as e:
                    #print(f"[{session.addr}] [PKT07] Parse error: {e}, raw payload = {payload.hex()}")
                    #print(f"[{session.addr}] [PKT07] Remaining bits = {br.remaining_bits()}")
                    #print(f"[{session.addr}] [PKT07] Debug log: {br.get_debug_log()}")
                            pass

            elif pkt == 0x09:
                # Handle PKTTYPE_ENT_POWER_CAST
                payload = data[4:]
                if len(payload) * 8 < 10:
                    #print(f"[{session.addr}] [PKT09] Payload too short: {len(payload)} bytes, raw payload = {payload.hex()}")
                    continue
                br = BitReader(payload, debug=False)
                try:
                    # Read entity ID
                    ent_id = br.read_method_4()
                    #print(f"[{session.addr}] [PKT09] Entity ID = {ent_id}, raw payload = {payload.hex()}")
                    if ent_id != session.clientEntID:
                        #print(f"[{session.addr}] [PKT09] Entity ID {ent_id} does not match clientEntID {session.clientEntID}")
                        continue
                    # Read power type ID
                    if br.remaining_bits() < 2:
                        #print(f"[{session.addr}] [PKT09] Not enough bits for power_type: {br.remaining_bits()}")
                        continue
                    power_type = br.read_method_4()
                    # Read is_charged flag
                    if br.remaining_bits() < 1:
                        #print(f"[{session.addr}] [PKT09] Not enough bits for is_charged: {br.remaining_bits()}")
                        continue
                    is_charged = bool(br.read_bit())
                    # Read optional target point
                    has_target_point = bool(br.read_bit()) if br.remaining_bits() >= 1 else False
                    target_x, target_y = None, None
                    if has_target_point:
                        if br.remaining_bits() < 6:
                            #print(f"[{session.addr}] [PKT09] Not enough bits for target point: {br.remaining_bits()}")
                            continue
                        target_x = br.read_method_45()
                        target_y = br.read_method_45()
                    # Read optional target entity
                    has_target_entity = bool(br.read_bit()) if br.remaining_bits() >= 1 else False
                    target_entity_id = None
                    if has_target_entity:
                        if br.remaining_bits() < 2:
                            #print(f"[{session.addr}] [PKT09] Not enough bits for target_entity_id: {br.remaining_bits()}")
                            continue
                        target_entity_id = br.read_method_4()
                    # Read is_queued flag
                    is_queued = bool(br.read_bit()) if br.remaining_bits() >= 1 else False
                    # Read optional secondary/tertiary entity
                    has_extra_entity = bool(br.read_bit()) if br.remaining_bits() >= 1 else False
                    secondary_entity_id, tertiary_entity_id = None, None
                    if has_extra_entity:
                        if br.remaining_bits() < 1:
                            #print(f"[{session.addr}] [PKT09] Not enough bits for extra entity flag: {br.remaining_bits()}")
                            continue
                        is_secondary = bool(br.read_bit())
                        if br.remaining_bits() < 2:
                            #print(f"[{session.addr}] [PKT09] Not enough bits for extra entity ID: {br.remaining_bits()}")
                            continue
                        if is_secondary:
                            secondary_entity_id = br.read_method_4()
                        else:
                            tertiary_entity_id = br.read_method_4()
                    # Log the power cast
                    #print(f"[{session.addr}] [PKT09] Power cast: power_type={power_type}, is_charged={is_charged}, "
                    #      f"target_point=({target_x},{target_y}), target_entity_id={target_entity_id}, "
                    #      f"is_queued={is_queued}, secondary_entity_id={secondary_entity_id}, "
                    #      f"tertiary_entity_id={tertiary_entity_id}")
                    #print(f"[{session.addr}] [PKT09] Debug log: {br.get_debug_log()}")
                    # Store power state (simplified, no ActivePower logic yet)
                    if ent_id in session.entities:
                        entity = session.entities[ent_id]
                        entity['combat_state'] = entity.get('combat_state', {})
                        entity['combat_state']['active_power'] = {
                            'power_type': power_type,
                            'is_charged': is_charged,
                            'is_queued': is_queued,
                            'target_x': target_x,
                            'target_y': target_y,
                            'target_entity_id': target_entity_id,
                            'secondary_entity_id': secondary_entity_id,
                            'tertiary_entity_id': tertiary_entity_id
                        }
                        session.entities[ent_id] = entity
                        #print(f"[{session.addr}] [PKT09] Updated entity {ent_id} combat_state: {entity['combat_state']}")
                    # Send empty response (assume 0x0A)
                    conn.sendall(struct.pack(">HH", 0x0A, 0))
                    # Broadcast power cast to other clients
                    for other_session in all_sessions:
                        if other_session != session and other_session.world_loaded and other_session.current_level == session.current_level:
                            update_packet = Send_Entity_Data(entity, is_player=True)
                            other_session.conn.sendall(struct.pack(">HH", 0x0F, len(update_packet)) + update_packet)
                            #print(f"[{session.addr}] [PKT09] Broadcasted entity {ent_id} power cast to {other_session.addr}")
                except Exception as e:
                    #print(f"[{session.addr}] [PKT09] Parse error: {e}, raw payload = {payload.hex()}")
                    #print(f"[{session.addr}] [PKT09] Remaining bits = {br.remaining_bits()}")
                    #print(f"[{session.addr}] [PKT09] Debug log: {br.get_debug_log()}")
                           pass
            elif pkt == 0x0A:
                try:
                    br = BitReader(payload)
                    target_id = br.read_method_4()  # Target entity ID
                    source_id = br.read_method_4()  # Source entity ID
                    value = br.read_method_45()  # Damage or effect value
                    power_id = br.read_method_4()  # Power ID
                    has_param5 = br.read_bit()  # Boolean for param5
                    param5 = br.read_method_4() if has_param5 else 0
                    has_param6 = br.read_bit()  # Boolean for param6
                    param6 = br.read_method_4() if has_param6 else 0
                    param7 = br.read_bit()  # Boolean flag (e.g., crit)
                    # Find entities
                    source_ent = session.get_entity(source_id)
                    target_ent = session.get_entity(target_id)
                    if source_ent and target_ent:
                        # Ensure entities have hp and name
                        if 'hp' not in target_ent:
                            target_ent['hp'] = target_ent.get('max_hp', 100)  # Default max HP
                        if 'name' not in source_ent:
                            source_ent['name'] = session.current_character or f"Entity_{source_id}"
                        if 'name' not in target_ent:
                            target_ent['name'] = f"NPC_{target_id}"
                        # Apply damage
                        damage = value
                        target_ent['hp'] = max(0, target_ent['hp'] - damage)
                        print(
                            f"[{addr}] Power hit: {source_ent['name']} hit {target_ent['name']} with power {power_id}, damage {damage}, new HP {target_ent['hp']}")
                        if param7:
                            print(f"[{addr}] Critical hit or special condition triggered")
                        # Broadcast updated entity state to other clients
                        for other_session in all_sessions:
                            if other_session != session and other_session.world_loaded and other_session.current_level == session.current_level:
                                update_packet = Send_Entity_Data(target_ent,
                                                                 is_player=(target_id == session.clientEntID))
                                other_session.conn.sendall(struct.pack(">HH", 0x0F, len(update_packet)) + update_packet)
                                print(f"[{addr}] Broadcasted entity {target_id} update to {other_session.addr}")
                    else:
                        print(f"[{addr}] Invalid entities: source {source_id}, target {target_id}")
                except Exception as e:
                    print(f"[{addr}] Error parsing 0x0A packet: {e}, raw payload = {payload.hex()}")

            elif pkt == 0xDE:
                bb = BitBuffer()
                bb.write_bits(1, 16)
                bb.write_bits(2, 8)
                bb.write_bits(0, 32)
                payload = bb.to_bytes()
                conn.sendall(struct.pack(">HH", 0xBF, len(payload)) + payload)
                print(f"[{addr}] TEST: sent BUILDING-UPDATE 0xBF len={len(payload)}")

            elif pkt == 0x2C:
                # Handle PKTTYPE_CHAT_MESSAGE
                payload = data[4:]
                try:
                    br = BitReader(payload)
                    entity_id = br.read_method_4()
                    message = br.read_method_13()
                    print(f"[{session.addr}] Chat message from entity {entity_id}: {message}")
                    # Broadcast to all clients in the same level
                    for other_session in all_sessions:
                        if other_session != session and other_session.world_loaded and other_session.current_level == session.current_level:
                            bb = BitBuffer()
                            bb.write_method_4(entity_id)
                            bb.write_method_13(message)
                            broadcast_payload = bb.to_bytes()
                            packet = struct.pack(">HH", 0x2C, len(broadcast_payload)) + broadcast_payload
                            other_session.conn.sendall(packet)
                            print(f"[{session.addr}] Broadcasted chat message to {other_session.addr}")
                except Exception as e:
                    print(f"[{session.addr}] Error parsing 0x2C packet: {e}, raw payload = {payload.hex()}")

            elif pkt == 0xC3:
                handle_masterclass_packet(session, data)
            elif pkt == 0xDF:
                handle_research_packet(session, data)
            elif pkt == 0x31:
                handle_gear_packet(session, data)
            elif pkt == 0x8E:
                handle_change_look(session, data,all_sessions)
            elif pkt == 0xC7:
                handle_create_gearset(session, data)
            elif pkt == 0xC8:
                handle_name_gearset(session, data)
            elif pkt == 0xC6:
                handle_apply_gearset(session, data)
            elif pkt == 0x30:
                handle_update_equipment(session, data)
            elif pkt == 0xBD:
                handle_hotbar_packet(session, data)
            elif pkt == 0xE2:
                magic_forge_packet(session, data)
            elif pkt == 0xD0:
                collect_forge_charm(session, data)
            elif pkt == 0xB0:
                handle_rune_packet(session, data)
            elif pkt == 0xB1:
                start_forge_packet(session, data)
            elif pkt == 0xE1:
                cancel_forge_packet(session, data)
            elif pkt == 0xD3:
                allocate_talent_points(session, data)
                continue

            elif pkt == 0xCC:
                pass

            elif pkt == 0x10E:
                pass

            elif pkt == 0x2D:
                print("Sent DOOR_TARGET (0x2E)")
                br = BitReader(data[4:])
                door_id = br.read_method_9()
                level_name = DOOR_MAP.get((session.current_level, door_id))
                if not level_name:
                    continue
                bb = BitBuffer()
                bb.write_method_4(door_id)
                bb.write_method_13(level_name)
                conn.sendall(struct.pack(">HH", 0x2E, len(bb.to_bytes())) + bb.to_bytes())
                print("Sent DOOR_TARGET (0x2E)")
                continue

            elif pkt == 0x1D:
                br = BitReader(data[4:])
                door_id = br.read_method_9()
                level_name = br.read_method_13()
                print(f"TRANSFER_READY for door {door_id} → {level_name}")
                token = session.issue_token(session.player_data)
                pending_world[token] = session.player_data
                swf_path, map_id, base_id, is_inst = LEVEL_CONFIG[level_name]
                pkt21 = build_enter_world_packet(
                    transfer_token=token,
                    old_level_id=0, old_swf="", has_old_coord=False, old_x=0, old_y=0,
                    host="127.0.0.1", port=8080,
                    new_level_swf=swf_path, new_map_lvl=map_id,
                    new_base_lvl=base_id, new_internal=level_name,
                    new_moment="", new_alter="", new_is_inst=is_inst,
                    new_has_coord=True, new_x=1000, new_y=1000,
                    char=session.player_data
                )
                conn.sendall(pkt21)
                print("Sent ENTER_WORLD (0x21)")
                continue

            else:
                print(f"[{session.addr}] Unhandled packet type: 0x{pkt:02X}, raw payload = {data.hex()}")
    except Exception as e:
        print("Session error:", e)
    finally:
        print("Disconnect:", addr)
        session.stop()

def start_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, port))
    except PermissionError:
        print(f"Error: Cannot bind to port {port}. Ports below 1024 require root privileges.")
        return None
    except OSError as e:
        print(f"Error: Cannot bind to port {port}. {e}")
        return None
    s.listen(5)
    print(f"Server listening on {HOST}:{port}")
    return s

def accept_connections(s, port):
    while True:
        conn, addr = s.accept()
        session = ClientSession(conn, addr)
        all_sessions.append(session)
        threading.Thread(target=handle_client, args=(session,), daemon=True).start()

def start_servers():
    servers = []
    for port in PORTS:
        server = start_server(port)
        if server:
            servers.append((server, port))
            threading.Thread(target=accept_connections, args=(server, port), daemon=True).start()
    return servers

if __name__ == "__main__":
    start_policy_server(host="127.0.0.1", port=843)
    start_static_server(host="127.0.0.1", port=80, directory="content/localhost")
    servers = start_servers()
    print("For Browser running on : http://localhost/index.html")
    print("For Flash Projector running on : http://localhost/p/cbv/DungeonBlitz.swf?fv=cbq&gv=cbv")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down servers...")
        for server, port in servers:
            server.close()
        sys.exit(0)