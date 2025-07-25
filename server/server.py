#!/usr/bin/env python3
import os
import random
import json
import socket, struct, hashlib, sys, time, secrets, threading
from accounts import get_or_create_user_id, load_accounts, _SAVES_DIR, is_character_name_taken, build_popup_packet
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
    cancel_forge_packet, allocate_talent_points, tick_forge_status, use_forge_xp_consumable, handle_private_message, \
    handle_public_chat, handle_group_invite, handle_power_cast, handle_power_hit, \
    handle_projectile_explode, handle_add_buff, handle_remove_buff, handle_entity_full_update, handle_position_sync, \
    handle_entity_incremental_update, handle_packet_0x7C, handle_packet_0x41
from constants import EntType, DyeType, Entity
from WorldEnter import build_enter_world_packet, Player_Data_Packet
from bitreader import BitReader
from PolicyServer import start_policy_server
from static_server import start_static_server
from entity import Send_Entity_Data, load_npc_data_for_level
from level_config import DOOR_MAP, LEVEL_CONFIG, get_spawn_coordinates

HOST = "127.0.0.1"
PORTS = [8080]
pending_world = {}
all_sessions = []
current_characters = {}
used_tokens = {}

def build_handshake_response(sid):
    b = sid.to_bytes(2, "big")
    h = hashlib.md5(b + b"815bfb010cd7b1b4e6aa90abc7679028").hexdigest()
    payload = b + bytes.fromhex(h[:12])
    return struct.pack(">HH", 0x12, len(payload)) + payload

def new_transfer_token():
    while (t := secrets.randbits(16)) in pending_world:
        pass
    return t
                         # For testing purposes
######################################################################################
def broadcast_level_change(session, char_name, new_level):
    """
    Notify all other authenticated clients of a player's level change.
    Sends a 0x2C packet with a custom message: "LEVEL_UPDATE:<char_name>:<new_level>".
    """
    message = f"LEVEL_UPDATE:{char_name}:{new_level}"
    bb = BitBuffer()
    bb.write_method_4(session.clientEntID or 0)  # Use clientEntID or 0 if not set
    bb.write_method_13(message)
    broadcast_payload = bb.to_bytes()
    packet = struct.pack(">HH", 0x2C, len(broadcast_payload)) + broadcast_payload
    for other_session in all_sessions:
        if other_session != session and other_session.authenticated:
            try:
                other_session.conn.sendall(packet)
                print(
                    f"[{session.addr}] Broadcasted level change for {char_name} to {new_level} to {other_session.addr}")
            except Exception as e:
                print(f"[{session.addr}] Error broadcasting level change to {other_session.addr}: {e}")

def broadcast_attack_dialogue(session, player_name, target_entity_id, target_name):
    """
    Broadcast scripted dialogue for a turn-based player-NPC conversation when the player attacks an NPC (e.g., ID 1).
    Sends five 0x2C packets (alternating player and NPC) with a 2-second delay, for a scripted scene.
    """
    print(f"[{session.addr}] Checking dialogue trigger for NPC ID {target_entity_id}")
    if target_entity_id != 999:
        print(f"[{session.addr}] Dialogue skipped: target_entity_id {target_entity_id} is not 1")
        return  # Only trigger for NPC ID 1
    # Check for cooldown (30 seconds)
    if hasattr(session, 'last_dialogue_time') and time.time() - session.last_dialogue_time < 90:
        print(f"[{session.addr}] Dialogue skipped: on cooldown for {player_name}")
        return
    session.last_dialogue_time = time.time()
    # Alternating dialogue: Player, NPC, Player, NPC, Player
    dialogue_sequence = [
        ("player", session.clientEntID, "Nephit! I finally found you."),
        ("NPC", target_entity_id, "So, the flame still flickers in you... intriguing."),
        ("player", session.clientEntID, "You knew this would end with us."),
        ("NPC", target_entity_id, "Many have tried. All have knelt before the void."),
        ("player", session.clientEntID, "I’m not like them. I’m not afraid."),
        ("NPC", target_entity_id, "Then come. Let your courage be your curse."),
        ("player", session.clientEntID, "I’ll tear through your illusions and take back the shard!"),
        ("NPC", target_entity_id, "The shard belongs to the darkness now."),
        ("player", session.clientEntID, "Then I’ll bring light to your darkness."),
        ("NPC", target_entity_id, "Bold... and foolish. Let’s end this.")
    ]
    print(
        f"[{session.addr}] Triggering turn-based dialogue for {player_name} and {target_name} (NPC ID {target_entity_id})")

    def send_dialogue(line, delay, entity_id, entity_type):
        """Helper to send a single dialogue line for player or NPC after a delay."""
        try:
            bb = BitBuffer()
            bb.write_method_4(entity_id or 0)  # Use player or NPC entity ID
            bb.write_method_13(line)  # Raw text for scripted scene
            broadcast_payload = bb.to_bytes()
            packet = struct.pack(">HH", 0x2C, len(broadcast_payload)) + broadcast_payload
            print(
                f"[{session.addr}] Constructed dialogue packet: type=0x2C, payload_len={len(broadcast_payload)}, line='{line}', entity_type={entity_type}")
            # Broadcast to all clients in the same level, including self
            for other_session in all_sessions:
                if other_session.world_loaded and other_session.current_level == session.current_level:
                    try:
                        other_session.conn.sendall(packet)
                        print(
                            f"[{session.addr}] Broadcasted {entity_type} dialogue '{line}' via 0x2C to {other_session.addr} after {delay}s")
                    except Exception as e:
                        print(f"[{session.addr}] Error sending {entity_type} dialogue to {other_session.addr}: {e}")
        except Exception as e:
            print(f"[{session.addr}] Error constructing {entity_type} dialogue packet for '{line}': {e}")

    # Schedule dialogue at 0.1s, 2.1s, 4.1s, 6.1s, 8.1s
    for i, (entity_type, entity_id, line) in enumerate(dialogue_sequence):
        threading.Timer(0.1 + i * 2.0, send_dialogue, args=(line, 0.1 + i * 2.0, entity_id, entity_type)).start()


######################################################################################
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
        self.entry_level = None
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
                # print(f"[{self.addr}] [NPC Update] Sent 0x0F for NPC {ent_id}: state={entity['entState']}, pos=({entity['x']}, {entity['y']})")

    def stop(self):
        self.running = False
        self.cleanup()

    def get_entity(self, entity_id):
        """
        Retrieve an entity from session.entities by its ID.
        Returns the entity dictionary or None if not found.
        """
        return self.entities.get(entity_id)

    def issue_token(self, char, target_level, previous_level):
        tk = new_transfer_token()
        # Use session.current_level if previous_level is None
        previous_level = previous_level if previous_level else self.current_level or char.get("PreviousLevel",
                                                                                              "NewbieRoad")
        pending_world[tk] = (char, target_level, previous_level)
        self.active_tokens.add(tk)
        print(f"[{self.addr}] Issued token {tk} for {char['name']} to {target_level}, previous={previous_level}")
        return tk

    def cleanup(self):

        # Close the connection and remove the session
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

    def forge_tick_loop():
        while session.running:
            tick_forge_status(session)
            time.sleep(1)

    conn, addr = session.conn, session.addr
    print("Connected:", addr)
    conn.settimeout(300)
    try:
        # Start NPC update thread
        threading.Thread(target=forge_tick_loop, daemon=True).start()
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
                br = BitReader(data[4:], debug=True)
                try:
                    _ = br.read_string()
                    _ = br.read_string()
                    email = br.read_string().strip().lower()
                    _ = br.read_string()
                    _ = br.read_string()
                except Exception as e:
                    print(f"[{session.addr}] [PKT0x14] Error parsing packet: {e}, raw payload={data[4:].hex()}")
                    continue
                accounts = load_accounts()
                user_id = accounts.get(email)
                if not user_id:
                    print(f"[{session.addr}] [PKT0x14] Login failed—no account for {email}")
                    err_packet = build_popup_packet("Account not found", disconnect=True)
                    conn.sendall(err_packet)
                    continue
                session.user_id = user_id
                try:
                    with open(os.path.join(_SAVES_DIR, f"{session.user_id}.json"), "r", encoding="utf-8") as f:
                        session.player_data = json.load(f)
                except FileNotFoundError:
                    session.player_data = {"email": email, "characters": []}
                session.char_list = session.player_data.get("characters", [])
                session.authenticated = True
                conn.sendall(build_login_character_list_bitpacked(session.char_list))
                print(
                    f"[{session.addr}] [PKT0x14] Logged in {email} → user_id={user_id}, chars={len(session.char_list)}")

            elif pkt == 0x17:
                if not session.authenticated:
                    err_packet = build_popup_packet("Please log in first", disconnect=True)
                    conn.sendall(err_packet)
                    continue
                br = BitReader(data[4:], debug=True)
                try:
                    tup = (
                        br.read_string(),  # name
                        br.read_string(),  # class
                        50,  # level
                        br.read_string(),  # gender
                        br.read_string(),  # head
                        br.read_string(),  # hair
                        br.read_string(),  # mouth
                        br.read_string(),  # face
                        br.read_bits(24),  # hairColor
                        br.read_bits(24),  # skinColor
                        br.read_bits(24),  # shirtColor
                        br.read_bits(24),  # pantColor
                        None  # equipped_gear
                    )
                    print(
                        f"[{session.addr}] [PKT0x17] Parsed character creation: name={tup[0]}, class={tup[1]}, gender={tup[3]}")
                except Exception as e:
                    print(f"[{session.addr}] [PKT0x17] Error parsing packet: {e}, raw payload={data[4:].hex()}")
                    continue
                # Check for duplicate character name
                if is_character_name_taken(tup[0]):
                    print(f"[{session.addr}] [PKT0x17] Character name {tup[0]} is already taken")
                    err_packet = build_popup_packet("Character name is unavailable. Please choose a new name.",
                                                    disconnect=False)
                    conn.sendall(err_packet)
                    continue
                new_char = make_character_dict_from_tuple(tup)
                session.char_list.append(new_char)
                save_characters(session.user_id, session.char_list)
                # Send updated character list (0x15)
                conn.sendall(build_login_character_list_bitpacked(session.char_list))
                print(f"[{session.addr}] [PKT0x17] Sent 0x15 character list update")
                # Send paperdoll packet (0x1A)
                pd = build_paperdoll_packet(new_char)
                conn.sendall(struct.pack(">HH", 0x1A, len(pd)) + pd)
                print(
                    f"[{session.addr}] [PKT0x17] Sent 0x1A paperdoll packet, len={len(pd)},")
                # Send popup message (0x1B)
                popup = build_popup_packet("Character Successfully Created", disconnect=False)
                conn.sendall(popup)
                print(f"[{session.addr}] [PKT0x17] Sent 0x1B popup message")

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
                        current_level = c.get("CurrentLevel", {}).get("name", "CraftTown")
                        session.current_level = current_level
                        c["user_id"] = session.user_id
                        # Set default PreviousLevel if unset
                        prev_name = c.get("PreviousLevel", {}).get("name", "NewbieRoad")
                        tk = session.issue_token(c, target_level=current_level, previous_level=prev_name)
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
                            new_has_coord=False,
                            new_x=0,
                            new_y=0,
                            char=c
                        )
                        session.conn.sendall(pkt_out)
                        # Save updated char_list to ensure PreviousLevel is set
                        session.char_list = load_characters(session.user_id)
                        for i, char in enumerate(session.char_list):
                            if char["name"] == name:
                                session.char_list[i] = c
                                break
                        save_characters(session.user_id, session.char_list)
                        print(f"[{session.addr}] Transfer begin: {name}, tk={tk}, level={current_level}")
                        break

            elif pkt == 0x1f:
                if len(data) < 6:
                    print(f"[{session.addr}] Error: Packet 0x1f too short, len={len(data)}")
                    continue
                token = int.from_bytes(data[4:6], 'big')
                entry = pending_world.pop(token, None)
                if entry is None:
                    if len(pending_world) == 1:
                        token, entry = next(iter(pending_world.items()))
                        pending_world.pop(token)
                    else:
                        print(
                            f"[{session.addr}] Error: No entry found for token {token}, pending_world size={len(pending_world)}")
                        continue
                session.active_tokens.discard(token)
                if len(entry) == 2:
                    char, target_level = entry
                    previous_level = session.current_level or char.get("PreviousLevel", {}).get("name", "NewbieRoad")
                else:
                    char, target_level, previous_level = entry
                    if isinstance(previous_level, dict):
                        previous_level = previous_level.get("name", "NewbieRoad")
                if char is None:
                    print(f"[{session.addr}] Error: Character is None for token {token}")
                    continue
                is_dungeon = LEVEL_CONFIG.get(target_level, (None, None, None, False))[3]
                if is_dungeon:
                    session.entry_level = previous_level if previous_level else char.get("PreviousLevel", "NewbieRoad")
                else:
                    session.entry_level = None
                session.user_id = char["user_id"]
                if not session.user_id:
                    print(f"[{session.addr}] Error: session.user_id is None for token {token}")
                    continue
                session.char_list = load_characters(session.user_id)
                if session.char_list:
                    for i, c in enumerate(session.char_list):
                        if c["name"] == char["name"]:
                            session.char_list[i] = char
                            break
                    else:
                        session.char_list.append(char)
                else:
                    session.char_list = [char]
                save_characters(session.user_id, session.char_list)
                print(
                    f"[{session.addr}] Saved character {char['name']}: CurrentLevel={char['CurrentLevel']}, PreviousLevel={char.get('PreviousLevel')}")

                session.current_level = target_level
                session.current_character = char["name"]
                session.current_char_dict = char
                current_characters[session.user_id] = session.current_character
                session.authenticated = True
                session.entities[token] = {
                    "id": token,
                    "x": 360.0,  # Temporary; will be overridden by Player_Data_Packet
                    "y": 1458.99,
                    "z": 0.0,
                    "entState": Entity.const_6,
                    "is_player": True,
                    "name": char["name"],
                    "hp": char.get("hp", 100),
                    "max_hp": char.get("max_hp", 100)
                }
                used_tokens[token] = (
                    char, target_level, session.current_level or char.get("PreviousLevel", "NewbieRoad"))
                # Calculate coordinates for Player_Data_Packet
                new_x, new_y, new_has_coord = get_spawn_coordinates(char, previous_level, target_level)
                welcome = Player_Data_Packet(
                    char,
                    transfer_token=token,
                    target_level=target_level,
                    new_x=int(round(new_x)),
                    new_y=int(round(new_y)),
                    new_has_coord=new_has_coord,
                )

                conn.sendall(welcome)
                session.clientEntID = token
                print(
                    f"[{session.addr}] Welcome: {char['name']} (token {token}) on level {session.current_level}, pos=({new_x},{new_y})")

            # Level Transfer request
            elif pkt == 0x1D:
                br = BitReader(data[4:])
                try:
                    _old_token = br.read_method_9()
                    level_name = br.read_method_13()
                except Exception as e:
                    print(f"[{session.addr}] ERROR: Failed to parse 0x1D packet: {e}, raw payload = {data[4:].hex()}")
                    continue
                print(f"[{session.addr}] TRANSFER_READY → {level_name}, old_token={_old_token}")
                # 1) Pull the pending entry
                entry = pending_world.pop(_old_token, None) or used_tokens.get(_old_token)
                if not entry:
                    print(f"[{session.addr}] ERROR: No character for token {_old_token}")
                    continue
                # 2) Unpack character and target_level
                char, target_level = entry[:2]
                # 3) Snapshot the level we're leaving (extract name if it’s a dict)
                raw = char.get("CurrentLevel")
                if isinstance(raw, dict):
                    old_level = raw.get("name", session.current_level or "NewbieRoad")
                else:
                    old_level = raw or session.current_level or "NewbieRoad"

                # 4) Clear player’s entity from old level to reflect they’ve left
                if session.clientEntID in session.entities:
                    del session.entities[session.clientEntID]
                    print(f"[{session.addr}] Removed entity {session.clientEntID} from level {old_level}")
                # 5) Bootstrap session with this character
                session.user_id = char.get("user_id")
                if not session.user_id:
                    print(f"[{session.addr}] ERROR: char['user_id'] missing for {char['name']}")
                    continue
                session.char_list = load_characters(session.user_id)
                session.current_character = char["name"]
                session.authenticated = True
                # 6) If the packet's level_name is empty, fallback
                if not level_name:
                    level_name = target_level
                    print(f"[{session.addr}] WARNING: Empty level_name, using target_level={level_name}")
                # 7) Update the character record
                is_dungeon = LEVEL_CONFIG.get(level_name, (None, None, None, False))[3]

                # 7a) Save current level’s coords to PreviousLevel
                prev_rec = char.get("CurrentLevel", {})
                prev_x = prev_rec.get("x", 0.0)
                prev_y = prev_rec.get("y", 0.0)
                char["PreviousLevel"] = {
                    "name": old_level,
                    "x": prev_x,
                    "y": prev_y
                }
                # 7b) Determine coordinates for the new level
                new_x, new_y, new_has_coord = get_spawn_coordinates(char, old_level, level_name)
                # 7c) Update CurrentLevel (skip coords for dungeons unless CraftTown)
                if not is_dungeon or level_name == "CraftTown":
                    char["CurrentLevel"] = {"name": level_name, "x": new_x, "y": new_y}
                save_characters(session.user_id, session.char_list)

                # 8) Write back into session.char_list and save
                for i, c in enumerate(session.char_list):
                    if c["name"] == char["name"]:
                        session.char_list[i] = char
                        break
                else:
                    session.char_list.append(char)
                save_characters(session.user_id, session.char_list)
                print(f"[{session.addr}] Saved character {char['name']}: "
                      f"CurrentLevel={char['CurrentLevel']}, PreviousLevel={char['PreviousLevel']}")
                # 9) Update session.current_level
                session.current_level = level_name
                session.world_loaded = False
                # 10) For testing purposes only; uncomment to broadcast level change, remove after testing
                broadcast_level_change(session, char["name"], level_name)
                # 11) Issue the new transfer token
                new_token = session.issue_token(
                    char,
                    target_level=level_name,
                    previous_level=old_level
                )
                # 12) Build and send the ENTER_WORLD packet
                swf_path, map_id, base_id, is_inst = LEVEL_CONFIG[level_name]
                pkt_out = build_enter_world_packet(
                    transfer_token=new_token,
                    old_level_id=0,
                    old_swf="",
                    has_old_coord=False,
                    old_x=0,
                    old_y=0,
                    host="127.0.0.1",
                    port=8080,
                    new_level_swf=swf_path,
                    new_map_lvl=map_id,
                    new_base_lvl=base_id,
                    new_internal=level_name,
                    new_moment="",
                    new_alter="",
                    new_is_inst=is_inst,
                    new_has_coord=new_has_coord,
                    new_x=int(round(new_x)),
                    new_y=int(round(new_y)),
                    char=char,
                )
                session.conn.sendall(pkt_out)
                print(
                    f"[{session.addr}] Sent ENTER_WORLD with token {new_token} for level {level_name}, pos=({new_x},{new_y})")

            elif pkt == 0x2D:
                br = BitReader(data[4:])
                try:
                    door_id = br.read_method_9()
                except Exception as e:
                    print(f"[{session.addr}] ERROR: Failed to parse 0x2D packet: {e}, raw payload = {data[4:].hex()}")
                    continue
                print(f"[{session.addr}] OpenDoor request: doorID={door_id}, current_level={session.current_level}")
                is_dungeon = LEVEL_CONFIG.get(session.current_level, (None, None, None, False))[3]
                # Determine target level
                target_level = None
                if is_dungeon and door_id in (0, 1, 2):
                    target_level = session.entry_level
                    if not target_level:
                        print(
                            f"[{session.addr}] Error: No entry_level set for door {door_id} in dungeon {session.current_level}")
                        continue
                elif door_id == 999:
                    target_level = "CraftTown"
                else:
                    target_level = DOOR_MAP.get((session.current_level, door_id))
                if target_level:
                    if target_level not in LEVEL_CONFIG:
                        print(f"[{session.addr}] Error: Target level {target_level} not found in LEVEL_CONFIG")
                        continue
                    # Send DOOR_TARGET response
                    bb = BitBuffer()
                    bb.write_method_4(door_id)
                    bb.write_method_13(target_level)
                    payload = bb.to_bytes()
                    resp = struct.pack(">HH", 0x2E, len(payload)) + payload
                    session.conn.sendall(resp)
                    print(f"[{session.addr}] Sent DOOR_TARGET: doorID={door_id}, level='{target_level}'")
                    # Reset world state
                    session.world_loaded = False
                    session.entities.clear()
                else:
                    print(f"[{session.addr}] Error: No target for door {door_id} in level {session.current_level}")

            elif pkt == 0x107:
                CAT_BITS = 3
                ID_BITS = 6
                PACK_ID = 1
                reward_map = {
                    0: ("MountLockbox01L01", True),  # Mount
                    1: ("Lockbox01L01", True),  # Pet
                    # 2: ("GenericBrown", True),  # Egg
                    # 3: ("CommonBrown", True),  # Egg
                    # 4: ("OrdinaryBrown", True),  # Egg
                    # 5: ("PlainBrown", True),  # Egg
                    6: ("RarePetFood", True),  # Consumable
                    7: ("PetFood", True),  # Consumable
                    # 8: ("Lockbox01Gear", True),  # Gear (will crash if invalid)
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

            elif pkt == 0x41:
                handle_packet_0x41(session, data, conn)
            elif pkt == 0x7C:
                handle_packet_0x7C(session, data)
            elif pkt == 0xA2:
                handle_position_sync(session, data, all_sessions)

            #TODO...
            #elif pkt == 0x08:
            #    handle_entity_full_update(session, data, all_sessions)
            #####
            elif pkt == 0x08:
                if session.world_loaded:
                    # print(f"[{session.addr}] World already loaded; skipping NPC spawn.")
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
                    # print(f"[{session.addr}] Spawned {len(npcs)} NPCs for level {session.current_level}")
                except Exception as e:
                    print(f"[{session.addr}] Error spawning NPCs: {e}")

            elif pkt == 0x07:
                handle_entity_incremental_update(session, data, all_sessions)
            elif pkt == 0x09:
                handle_power_cast(session, data, all_sessions)
            elif pkt == 0x0A:
                handle_power_hit(session, data, all_sessions)
            elif pkt == 0x0E:
                handle_projectile_explode(session, data, all_sessions)
            elif pkt == 0x0E:
                handle_projectile_explode(session, data, all_sessions)
            elif pkt == 0x0B:
                handle_add_buff(session, data, all_sessions)
            elif pkt == 0x0C:
                handle_remove_buff(session, data, all_sessions)
            elif pkt == 0xDE:
                bb = BitBuffer()
                bb.write_bits(1, 16)
                bb.write_bits(2, 8)
                bb.write_bits(0, 32)
                payload = bb.to_bytes()
                conn.sendall(struct.pack(">HH", 0xBF, len(payload)) + payload)
                print(f"[{addr}] TEST: sent BUILDING-UPDATE 0xBF len={len(payload)}")
            elif pkt == 0x65:
                handle_group_invite(session, data, all_sessions)
            elif pkt == 0x2C:
                handle_public_chat(session, data, all_sessions)
            elif pkt == 0x46:
                handle_private_message(session, data, all_sessions)
            elif pkt == 0xC3:
                handle_masterclass_packet(session, data)
            elif pkt == 0xDF:
                handle_research_packet(session, data)
            elif pkt == 0x31:
                handle_gear_packet(session, data)
            elif pkt == 0x8E:
                handle_change_look(session, data, all_sessions)
            elif pkt == 0xC7:
                handle_create_gearset(session, data)
            elif pkt == 0xC8:
                handle_name_gearset(session, data)
            elif pkt == 0xC6:
                handle_apply_gearset(session, data)
            elif pkt == 0x30:
                handle_update_equipment(session, data)
            elif pkt == 0xBD:
                handle_hotbar_packet(session, data)  # Active Skills
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
            elif pkt == 0x110:
                use_forge_xp_consumable(session, data)

            elif pkt == 0xCC:
                pass
            elif pkt == 0x10E:
                pass

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
