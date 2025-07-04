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
from BitUtils import  BitBuffer
from Commands import handle_hotbar_packet, handle_masterclass_packet, handle_research_packet, handle_gear_packet, handle_apply_dyes, handle_rune_packet, handle_change_look, handle_create_gearset, handle_name_gearset, handle_apply_gearset, handle_update_equipment
from constants import EntType, DyeType, Entity, LinkUpdater
from WorldEnter import build_enter_world_packet, Player_Data_Packet
from bitreader import BitReader
from PolicyServer import start_policy_server
from static_server import start_static_server
from entity import Send_Entity_Data
from Entity_Data import load_npc_data_for_level
from level_config import DOOR_MAP, LEVEL_CONFIG

HOST = "127.0.0.1"
PORTS = [8080]#7498 for Developer mode
pending_world = {}  # token → character dict
all_sessions = []    # list of ClientSession for broadcasting updates

PKTTYPE_ENT_POWER_HIT = 0x0A

def send_power_hit(session, npc_id, player_id, power_idx=0):
    """
    Simulates a hit on npc_id by player_id using power index `power_idx`.
    """
    bb = BitBuffer()
    bb.write_method_4(npc_id)       # target entity
    bb.write_method_4(player_id)    # source entity
    bb.write_method_4(power_idx)    # index into class_14.powerTypes
    payload = bb.to_bytes()
    header  = struct.pack(">HH", PKTTYPE_ENT_POWER_HIT, len(payload))
    session.conn.sendall(header + payload)

PKTTYPE_SERVER_ADJUST_HP = 0x3A

def send_hp_adjust(session, npc_id, delta):
    """
    Tells the client to change npc_id's HP by `delta` (negative = damage).
    """
    bb = BitBuffer()
    bb.write_method_4(npc_id)
    bb.write_signed_method_45(delta)
    payload = bb.to_bytes()
    header  = struct.pack(">HH", PKTTYPE_SERVER_ADJUST_HP, len(payload))
    session.conn.sendall(header + payload)

PKTTYPE_ENT_INCREMENTAL_UPDATE = 7

def build_incremental_update(entity_id: int,
                             dx: int = 0,
                             dy: int = 0,
                             dz: int = 0,
                             ent_state: int = Entity.const_6,
                             b_left: bool = False,
                             b_running: bool = False,
                             b_jumping: bool = False,
                             b_dropping: bool = False,
                             b_backpedal: bool = False,
                             y_vel: float = 0.0,
                             target_id: int = 0) -> bytes:
    bb = BitBuffer()
    bb.write_method_4(entity_id)
    bb.write_signed_method_45(dx)
    bb.write_signed_method_45(dy)
    bb.write_signed_method_45(dz)
    bb.write_method_6(ent_state, Entity.const_316)
    # movement flags
    for flag in (b_left, b_running, b_jumping, b_dropping, b_backpedal):
        bb.write_bits(1 if flag else 0, 1)
    # vertical velocity
    if abs(y_vel) > 1e-6:
        bb.write_bits(1, 1)
        bb.write_signed_method_45(int(y_vel * LinkUpdater.VELOCITY_INFLATE))
    else:
        bb.write_bits(0, 1)
    # NEW: write the NPC's target
    bb.write_method_4(target_id)
    payload = bb.to_bytes()
    header  = struct.pack(">HH", PKTTYPE_ENT_INCREMENTAL_UPDATE, len(payload))
    return header + payload

# Broadcaster thread
def broadcast_incremental_updates():
    while True:
        time.sleep(20.05)
        for session in all_sessions:
            if not session.world_loaded:
                continue

            pid = session.clientEntID
            for npc in session.spawned_npcs:
                # 1) Make them ‘hate’ the player
                send_power_hit(session, npc['id'], pid, power_idx=0)

                # 2) (Optional) sync HP so dragon doesn’t appear damaged
                send_hp_adjust(session, npc['id'], 0)

                # 3) Send incremental update to keep AI ticking
                #    (use ent_state=2 for movement, flags as before)
                pkt = build_incremental_update(
                    entity_id=npc['id'],
                    dx=0, dy=0, dz=0,
                    ent_state=0,
                    b_left=True,
                    b_running=True,
                    b_jumping=False,
                    b_dropping=False,
                    b_backpedal=False,
                    y_vel=0.0,
                    target_id=pid
                )
                session.conn.sendall(pkt)

# Start it once, at module load
threading.Thread(target=broadcast_incremental_updates, daemon=True).start()

def build_handshake_response(sid):
    b = sid.to_bytes(2,"big")
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
                # connection closed
                return None
            buf += chunk
        return buf

def handle_client(session: ClientSession):
    conn, addr = session.conn, session.addr
    print("Connected:", addr)
    conn.settimeout(300)
    try:
        while True:
            # 1) read 4-byte header
            hdr = read_exact(conn, 4)
            if not hdr:
                break  # client closed

            pkt_id, length = struct.unpack(">HH", hdr)

            # 2) read exactly 'length' bytes of payload
            payload = read_exact(conn, length)
            if payload is None:
                break

            # now you have the full packet: hdr + payload
            data = hdr + payload

            #hex_data = data.hex()
            #print("Received raw data:", hex_data)

            pkt = int(data.hex()[:4], 16)
            if pkt == 0x11:
                sid = int(data.hex()[8:12],16) if len(data)>=6 else 0
                conn.sendall(build_handshake_response(sid))

            elif pkt == 0x13:
              # New-account registration packet
              # Skip header (4 bytes) + session-id (4 bytes)
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
              session.authenticated = True  # ← grant auth
              conn.sendall(build_login_character_list_bitpacked(session.char_list))

            elif pkt == 0x14:
                # Existing-account login (0x14)
                # Payload starts immediately after the 4-byte header:
                br = BitReader(data[4:])
                # 1) clientFacebookID (ignore)
                _ = br.read_string()
                # 2) clientKongID (ignore)
                _ = br.read_string()
                # 3) email ← this is the real one we want
                email = br.read_string().strip().lower()
                # 4) encrypted payload (ignore)
                _ = br.read_string()
                # 5) some other token/ID (ignore)
                _ = br.read_string()
                accounts = load_accounts()  # dict: email → user_id
                user_id = accounts.get(email)
                if not user_id:
                    print(f"[{session.addr}] Login failed—no account for {email}")
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
                session.authenticated = True  # ← grant auth
                conn.sendall(build_login_character_list_bitpacked(session.char_list))
                print(f"[{session.addr}] Logged in {email} → user_id={user_id}, chars={len(session.char_list)}")

            elif pkt == 0x17:
                if not session.authenticated:
                    msg = "Please log in first".encode("utf-8")
                    pl = struct.pack(">H", len(msg)) + msg
                    conn.sendall(struct.pack(">HH", 0x1B, len(pl)) + pl)
                    continue
                br = BitReader(data[4:])
                tup = (
                    br.read_string(),  # name
                    br.read_string(),  # class
                    50,  # level
                    br.read_string(),  # gender
                    br.read_string(),  # head
                    br.read_string(),  # hair
                    br.read_string(),  # mouth
                    br.read_string(),  # face
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
                        conn.sendall(struct.pack(">HH",0x1A,len(pd))+pd)
                        break
                else:
                    conn.sendall(struct.pack(">HH",0x1A,0))

            elif pkt == 0x16:
                name = BitReader(data[4:]).read_string()
                for c in session.char_list:
                    if c["name"] == name:
                        # Remember which character was selected
                        session.current_character = name
                        # Get the current level from the character's save data, default to "NewbieRoad" if missing
                        current_level = c.get("CurrentLevel", "CraftTown")
                        session.current_level = current_level
                        # Inject the user_id so char carries it forward
                        c["user_id"] = session.user_id
                        tk = session.issue_token(c)
                        # Get level config from LEVEL_CONFIG, fallback if level not found
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
                            new_level_swf=level_config[0],  # SWF from config
                            new_map_lvl=level_config[1],  # Map level from config
                            new_base_lvl=level_config[2],  # Base level from config
                            new_internal=current_level,  # Internal name from save data
                            new_moment="",
                            new_alter="1",
                            new_is_inst=level_config[3]  # Instance flag from config
                        )
                        conn.sendall(pkt_out)
                        print("Transfer begin:", name, "tk=", tk, "level=", current_level)
                        break

            elif pkt == 0x1f:
                if len(data) < 8:
                    #print("Malformed 0x1F (too short)")
                    continue
                token = int.from_bytes(data[4:8], 'big')
                #print("Pending tokens:", list(pending_world.keys()))
                #print("Client asked for token:", token)
                char = pending_world.pop(token, None)
                if char is None and len(pending_world) == 1:
                    fallback_token, fallback_char = next(iter(pending_world.items()))
                    #print(f"Falling back to sole pending token {fallback_token}")
                    char = fallback_char
                    token = fallback_token
                    pending_world.pop(fallback_token, None)
                session.active_tokens.discard(token)
                if char:
                    # Now this returns the right user_id
                    session.user_id = char["user_id"]
                    # Load their save
                    with open(f"saves/{session.user_id}.json", "r") as f:
                        session.player_data = json.load(f)
                    # Set current_character and current_level
                    session.current_character = char["name"]
                    session.current_level = char.get("CurrentLevel",
                                                     "CraftTown")  # Use CurrentLevel, default to NewbieRoad
                    welcome = Player_Data_Packet(char, transfer_token=token)
                    conn.sendall(welcome)
                    session.clientEntID = token
                    print("Welcome:", char["name"], "(used token", token, ") on level", session.current_level)

            elif pkt == 0x7C:
                    # Client crash/error report
                    # Packet format: [0x7C][length:2B][UTF-8 error message]
                    _, length = struct.unpack_from(">HH", data, 0)
                    payload = data[4:4 + length]
                    try:
                        msg = payload.decode("utf-8", errors="replace")
                    except Exception:
                        msg = repr(payload)
                    print(f"[{session.addr}] CLIENT ERROR (0x7C): {msg}")

            elif pkt == 0x41:
                #print(f"[{session.addr}] Handling DOOR_STATE_REQUEST (0x41), raw payload = {data.hex()}")
                # Ensure packet has at least the header (4 bytes: 2 for type, 2 for length)
                if len(data) < 4:
                    #print(f"[{session.addr}] Malformed 0x41 packet: too short ({len(data)} bytes)")
                    continue
                # Extract payload length from bytes 2-4
                payload_length = struct.unpack(">H", data[2:4])[0]
                # Check if total packet length matches expected (header + payload)
                if len(data) != 4 + payload_length:
                    #print(f"[{session.addr}] Malformed 0x41 packet: expected {4 + payload_length} bytes, got {len(data)}")
                    continue
                # Extract payload
                payload = data[4:4 + payload_length]
                try:
                    br = BitReader(payload)
                    door_id = br.read_method_9()
                    #print(f"[{session.addr}] Parsed method_9 doorID = {door_id}")
                except Exception as e:
                    #print(f"[{session.addr}] Failed to parse method_9 doorID: {e}")
                    continue
                # Check DOOR_MAP for destination or state
                door_info = DOOR_MAP.get((session.current_level, door_id))
                bb = BitBuffer()
                bb.write_method_4(door_id)  # doorID (method_4)
                if door_info is None:
                    #print(f"[{session.addr}] Unknown doorID {door_id} for level {session.current_level}, defaulting to open")
                    bb.write_method_91(1)  # doorState = 1 (open)
                    bb.write_method_13("")  # Empty destination
                else:
                    #print(f"[{session.addr}] DoorID {door_id} in level {session.current_level}")
                    if isinstance(door_info, str):
                        # Transition door
                        #print(f"[{session.addr}] Door leads to {door_info}")
                        bb.write_method_91(1)  # doorState = 1 (open)
                        bb.write_method_13(door_info)  # Destination (e.g., TutorialBoat)
                    else:
                        # State door (open/closed)
                        #print(f"[{session.addr}] Door state = {door_info}")
                        bb.write_method_91(door_info)  # doorState
                        bb.write_method_13("")  # No destination
                payload = bb.to_bytes()
                response = struct.pack(">HH", 0x42, len(payload)) + payload
                conn.sendall(response)
                #print(f"[{session.addr}] Sent DOOR_STATE response: doorID={door_id}, state=1, destination={door_info if isinstance(door_info, str) else ''}, packet = {response.hex()}")
                continue

            #TODO...
            elif pkt == 0x2D:
                print(f"[{session.addr}] Handling OPEN_DOOR (0x2D), raw payload = {data.hex()}")
                if len(data) < 6:
                    print(f"[{session.addr}] Malformed 0x2D packet: too short ({len(data)} bytes)")
                    continue
                try:
                    br = BitReader(data[4:])
                    door_id = br.read_method_9()
                    print(f"[{session.addr}] Parsed method_9 doorID = {door_id}")
                except Exception as e:
                    print(f"[{session.addr}] Failed to parse method_9 doorID: {e}")
                    continue
                print(
                    f"[{session.addr}] Session state: level={session.current_level}, character={session.current_character}")

                door_info = DOOR_MAP.get((session.current_level, door_id))
                if door_info is None or not isinstance(door_info, str):
                    print(
                        f"[{session.addr}] No transition for doorID {door_id} in level {session.current_level}, sending open state")
                    bb = BitBuffer()
                    bb.write_method_4(door_id)
                    bb.write_method_91(1)
                    bb.write_method_13("")
                    payload = bb.to_bytes()
                    response = struct.pack(">HH", 0x42, len(payload)) + payload
                    conn.sendall(response)
                    print(
                        f"[{session.addr}] Sent DOOR_STATE response: doorID={door_id}, state=1, destination='', packet = {response.hex()}")
                    continue

                # Transition to the destination level
                target_level = door_info
                print(f"[{session.addr}] Transitioning to {target_level} for doorID={door_id}")
                """
                level_config = LEVEL_CONFIG.get(target_level, ("LevelsTut.swf/a_Level_" + target_level, 1, 1, True))
                pkt_out = build_enter_world_packet(
                    transfer_token=session.active_tokens.pop() if session.active_tokens else new_transfer_token(),
                    old_level_id=2,
                    old_swf="LevelsNR.swf/a_Level_NewbieRoad",
                    has_old_coord=False,
                    old_x=0,
                    old_y=0,
                    host="127.0.0.1",
                    port=8080,
                    new_level_swf=level_config[0],
                    new_map_lvl=level_config[1],
                    new_base_lvl=level_config[2],
                    new_internal=target_level,
                    new_moment="",
                    new_alter="",
                    new_is_inst=level_config[3]
                )
                conn.sendall(pkt_out)
                print(
                    f"[{session.addr}] Sent transition to {target_level} for doorID={door_id}, packet = {pkt_out.hex()}")
                # Update session and save data
                session.current_level = target_level
                for char in session.char_list:
                    if char["name"] == session.current_character:
                        char["CurrentLevel"] = target_level
                        break
                save_characters(session.user_id, session.char_list)
                # Send FULL_UPDATE for NPCs
                try:
                    npcs = load_npc_data_for_level(target_level)
                    for npc in npcs:
                        payload = Send_Entity_Data(npc, is_player=False)
                        conn.sendall(struct.pack(">HH", 0x0F, len(payload)) + payload)
                    print(f"[{session.addr}] Sent FULL_UPDATE for {target_level}")
                except Exception as e:
                    print(f"[{session.addr}] Failed to send FULL_UPDATE for {target_level}: {e}")
                continue
                """
            elif pkt == 0xA2:
                payload = data[4:]
                # skip those too-short ones
                if len(payload) < 9:
                    continue

                # parse what little we need
                br = BitReader(payload)
                client_elapsed = br.read_bits(32)
                drift_flag = bool(br.read_bits(1))
                system_elapsed = br.read_bits(32)

                # build a response packet (you could include server time here if you wish)
                bb = BitBuffer()
                bb.write_bits(client_elapsed, 32)
                bb.write_bits(0, 1)  # no drift on server side
                bb.write_bits(system_elapsed, 32)
                resp = struct.pack(">HH", 0xA2, len(bb.to_bytes())) + bb.to_bytes()
                session.conn.sendall(resp)

                continue

            elif pkt == 0x107:
                CAT_BITS = 3  # class_18.var_1846
                ID_BITS = 6  # class_18.var_1776
                PACK_ID = 1  # Lockbox01's RewardpackID
                # Full 0–19 mapping from your XML:
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
                continue

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
                    print(f"[{session.addr}] World already loaded; skipping NPC spawn.")
                    continue
                try:
                    npcs = load_npc_data_for_level(session.current_level)
                    for npc in npcs:
                        payload = Send_Entity_Data(npc, is_player=False)
                        conn.sendall(struct.pack(">HH", 0x0F, len(payload)) + payload)
                        session.spawned_npcs.append(npc)
                        session.npc_states[npc['id']] = {
                            'last_x': npc['x'],
                            'last_y': npc['y'],
                            'last_z': npc['z']
                        }
                        session.world_loaded = True
                except Exception as e:
                    print(f"[{session.addr}] Error spawning NPCs: {e}")
                continue

            elif pkt_id == 0xDE:
                bb = BitBuffer()
                bb.write_bits(1, 16)  # test-building ID = 1
                bb.write_bits(2, 8)  # test-new level = 2
                bb.write_bits(0, 32)  # end-time = 0 (instant)
                payload = bb.to_bytes()
                conn.sendall(struct.pack(">HH", 0xbf, len(payload)) + payload)
                print(f"[{addr}] TEST: sent BUILDING-UPDATE 0xDA len={len(payload)}")
                continue

            elif pkt == 0xC3:
                handle_masterclass_packet(session, data)
                continue

            elif pkt == 0xDF:
                handle_research_packet(session, data)
                continue

            elif pkt == 0x31:
                handle_gear_packet(session, data)
                continue

            elif pkt == 0x8E:
                handle_change_look(session, data)
                continue

            elif pkt == 0xC7:
                handle_create_gearset(session, data)
                continue

            elif pkt == 0xC8:
                handle_name_gearset(session, data)
                continue

            elif pkt == 0xC6:
                handle_apply_gearset(session, data)
                continue

            elif pkt == 0x30:
                handle_update_equipment(session, data)
                continue

            elif pkt == 0xBD:
                handle_hotbar_packet(session, data)

            elif pkt == 0xCC: #no idea what this does
                pass

            elif pkt == 0xB0:
                handle_rune_packet(session, data)
                continue

            else:
                print(f"[{session.addr}] Unhandled packet type: 0x{pkt:02X}, raw payload = {data.hex()}")

    except Exception as e:
        print("Session error:", e)
    finally:
        print("Disconnect:", addr)
        session.cleanup()

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
    #print("running on : http://localhost/DeveloperMode.html")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down servers...")
        for server, port in servers:
            server.close()
        sys.exit(0)