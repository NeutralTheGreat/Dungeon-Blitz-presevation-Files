#!/usr/bin/env python3
import os
import json
import socket, struct, hashlib, sys, time, secrets, threading

from Brain import tick_npc_brains
from accounts import get_or_create_user_id, load_accounts, _SAVES_DIR, is_character_name_taken, build_popup_packet
from Character import (
    make_character_dict_from_tuple,
    build_login_character_list_bitpacked,
    build_paperdoll_packet,
    load_characters,
    save_characters
)
from BitUtils import BitBuffer
from Commands import handle_hotbar_packet, handle_masterclass_packet, handle_gear_packet, \
    handle_apply_dyes, handle_rune_packet, handle_change_look, handle_create_gearset, handle_name_gearset, \
    handle_apply_gearset, handle_update_equipment, magic_forge_packet, collect_forge_charm, start_forge_packet, \
    cancel_forge_packet, allocate_talent_points, use_forge_xp_consumable, handle_private_message, \
    handle_public_chat, handle_group_invite, handle_power_cast, handle_power_hit, \
    handle_projectile_explode, handle_add_buff, handle_remove_buff, handle_entity_full_update, \
    handle_entity_incremental_update, handle_packet_0x41, Start_Skill_Research, \
    handle_research_claim, PaperDoll_Request, Skill_Research_Cancell_Request, Skill_SpeedUp, handle_building_upgrade, \
    handle_speedup_request, handle_cancel_upgrade, handle_train_talent_point, handle_talent_speedup, \
    handle_talent_claim, handle_clear_talent_research, handle_hp_increase_notice, handle_volume_enter, \
    handle_change_offset_y, handle_start_skit, handle_change_max_speed, handle_lockbox_reward, handle_grant_reward, \
    handle_linkupdater, handle_request_respawn, handle_respawn_ack, PKTTYPE_BUFF_TICK_DOT, handle_entity_destroy, \
    handle_emote_begin, Client_Crash_Reports, handle_mount_equip_packet, handle_pet_info_packet, \
    handle_collect_hatched_egg, handle_talk_to_npc, handle_char_regen
from constants import Entity
from WorldEnter import build_enter_world_packet, Player_Data_Packet
from bitreader import BitReader
from PolicyServer import start_policy_server
from static_server import start_static_server
from entity import Send_Entity_Data, load_npc_data_for_level
from level_config import DOOR_MAP, LEVEL_CONFIG, get_spawn_coordinates
from scheduler import set_active_session_resolver, schedule_research

HOST = "127.0.0.1"
PORTS = [8080]# Developer mode Port : 7498
pending_world = {}
all_sessions = []
current_characters = {}
used_tokens = {}

SECRET_HEX = "815bfb010cd7b1b4e6aa90abc7679028"
SECRET      = bytes.fromhex(SECRET_HEX)

def send_login_challenge(conn):
    # 1) pick a random 16-bit sid
    sid = secrets.randbelow(1 << 16)
    sid_bytes = sid.to_bytes(2, "big")
    # 2) compute MD5(sid_bytes || SECRET) → take first 12 hex chars
    digest = hashlib.md5(sid_bytes + SECRET).hexdigest()[:12]
    # 3) build a single ASCII-hex string: 4 hex digits of sid + 12 hex digits of digest
    #    e.g. "1A2B3c4d5e6f7a8b9c0d"
    sid_hex = f"{sid:04x}"
    challenge_str = sid_hex + digest  # total length = 16 chars
    # 4) UTF-encode it with a 2-byte length prefix
    utf_bytes = challenge_str.encode("utf-8")
    payload = struct.pack(">H", len(utf_bytes)) + utf_bytes
    # 5) prepend the 0x12 header
    packet = struct.pack(">HH", 0x12, len(payload)) + payload
    # 6) send to client
    conn.sendall(packet)
    #print(f"→ Sent 0x12 login challenge sid={sid_hex} hash={digest}")

def new_transfer_token():
    while (t := secrets.randbits(16)) in pending_world:
        pass
    return t

def find_active_session(user_id, char_name):
    for s in all_sessions:
        if getattr(s, 'user_id', None) == user_id and getattr(s, 'current_character', None) == char_name and s.authenticated:
            return s
    return None

# register resolver
set_active_session_resolver(find_active_session)

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
        #print(f"[{self.addr}] Issued token {tk} for {char['name']} to {target_level}, previous={previous_level}")
        return tk

    def cleanup(self):
        try: self.conn.close()
        except: pass
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
    conn = session.conn
    addr = session.addr
    print("Connected:", addr)
    conn.settimeout(300)
    tick_npc_brains(all_sessions)
    # On login, reschedule future research
    if session.user_id:
        now = int(time.time())
        for char in session.char_list:
            research = char.get("research")
            if research and not research.get("done", False):
                rt = research.get("ReadyTime", 0)
                if rt > now:
                    schedule_research(session.user_id, char["name"], rt)

    buffer = bytearray()
    try:
        while True:
            chunk = conn.recv(4096)
            if not chunk:
                print(f"[{addr}] Connection closed by client")
                break
            buffer.extend(chunk)

            # Try to extract complete packets
            while len(buffer) >= 4:
                # Peek header
                pkt    = int.from_bytes(buffer[0:2], byteorder='big')
                length = int.from_bytes(buffer[2:4], byteorder='big')
                total  = 4 + length

                # If we don’t yet have the full packet, wait for more data
                if len(buffer) < total:
                    break

                # We have a full packet in buffer[0:total]
                data    = bytes(buffer[:total])
                payload = data[4:]
                # Remove it from buffer
                del buffer[:total]

                # Debug‐print
               # print(f"[{addr}] Framed pkt=0x{pkt:02X} length={length} payload_bytes={len(payload)}")

                # Sanity check
                if len(payload) != length:
                    print(f"[{addr}] ⚠️ Length mismatch: header says {length} but payload is {len(payload)}")
                    # continue

            if pkt == 0x11:# Done
                send_login_challenge(conn)
                continue

            elif pkt == 0x13:  # Done
                br = BitReader(data[8:], debug=True)
                email = br.read_string().strip().lower()
                session.user_id = get_or_create_user_id(email)
                session.char_list = load_characters(session.user_id)
                session.authenticated = True
                # reschedule research again after login
                now = int(time.time())
                for char in session.char_list:
                    research = char.get("research")
                    if research and not research.get("done", False):
                        rt = research.get("ReadyTime", 0)
                        if rt > now:
                            schedule_research(session.user_id, char["name"], rt)
                conn.sendall(build_login_character_list_bitpacked(session.char_list))

            elif pkt == 0x14:  # Done
                br = BitReader(data[4:], debug=True)
                try:
                    _ = br.read_string()  # skip first string
                    _ = br.read_string()  # skip second string
                    email = br.read_string().strip().lower()
                    _ = br.read_string()  # skip next
                    _ = br.read_string()  # skip next
                except Exception as e:
                    print(f"[{session.addr}] [PKT0x14] Error parsing packet: {e}, raw payload={data[4:].hex()}")
                    continue
                accounts = load_accounts()
                user_id = accounts.get(email)
                if not user_id:
                    print(f"[{session.addr}] [PKT0x14] Login failed—no account for {email}")
                    conn.sendall(build_popup_packet("Account not found", disconnect=True))
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

            elif pkt == 0x17:# Done
                if not session.authenticated:
                    err_packet = build_popup_packet("Please log in first", disconnect=True)
                    conn.sendall(err_packet)
                    continue
                br = BitReader(data[4:], debug=True)
                try:
                    tup = (
                        br.read_string(),  # name
                        br.read_string(),  # class
                        20,  # level
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
                    #print(
                       # f"[{session.addr}] [PKT0x17] Parsed character creation: name={tup[0]}, class={tup[1]}, gender={tup[3]}")
                except Exception as e:
                    #print(f"[{session.addr}] [PKT0x17] Error parsing packet: {e}, raw payload={data[4:].hex()}")
                    continue
                # Check for duplicate character name
                if is_character_name_taken(tup[0]):
                    #print(f"[{session.addr}] [PKT0x17] Character name {tup[0]} is already taken")
                    err_packet = build_popup_packet("Character name is unavailable. Please choose a new name.",
                                                    disconnect=False)
                    conn.sendall(err_packet)
                    continue
                new_char = make_character_dict_from_tuple(tup)
                session.char_list.append(new_char)
                save_characters(session.user_id, session.char_list)
                # Send updated character list (0x15)
                conn.sendall(build_login_character_list_bitpacked(session.char_list))
                #print(f"[{session.addr}] [PKT0x17] Sent 0x15 character list update")
                # Send paperdoll packet (0x1A)
                pd = build_paperdoll_packet(new_char)
                conn.sendall(struct.pack(">HH", 0x1A, len(pd)) + pd)
                #print(
                    #f"[{session.addr}] [PKT0x17] Sent 0x1A paperdoll packet, len={len(pd)},")
                # Send popup message (0x1B)
                popup = build_popup_packet("Character Successfully Created", disconnect=False)
                conn.sendall(popup)
                #print(f"[{session.addr}] [PKT0x17] Sent 0x1B popup message")


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

                        # detect hard mode (Dread levels)
                        is_hard = current_level.endswith("Hard")
                        new_moment = "Hard" if is_hard else ""
                        new_alter = "Hard" if is_hard else ""

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
                            new_moment=new_moment,
                            new_alter=new_alter,
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
                        #print(f"[{session.addr}] Transfer begin: {name}, tk={tk}, level={current_level}")
                        break
            #TODO...
            #the 0x1f and 0x1D needs to be rewritten and organised since the code is a mess
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
                #print(
                    #f"[{session.addr}] Saved character {char['name']}: CurrentLevel={char['CurrentLevel']}, PreviousLevel={char.get('PreviousLevel')}")

                session.current_level = target_level
                session.current_character = char["name"]
                session.current_char_dict = char
                current_characters[session.user_id] = session.current_character
                session.authenticated = True
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

                #print(
                    #f"[{session.addr}] Welcome: {char['name']} (token {token}) on level {session.current_level}, pos=({new_x},{new_y})")


            # Level Transfer request
            elif pkt == 0x1D:
                br = BitReader(data[4:])
                try:
                    _old_token = br.read_method_9()
                    level_name = br.read_method_13()
                except Exception as e:
                    print(f"[{session.addr}] ERROR: Failed to parse 0x1D packet: {e}, raw payload = {data[4:].hex()}")
                    continue
                #print(f"[{session.addr}] TRANSFER_READY → {level_name}, old_token={_old_token}")
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
                #print(f"[{session.addr}] Saved character {char['name']}: "
                     # f"CurrentLevel={char['CurrentLevel']}, PreviousLevel={char['PreviousLevel']}")
                # 9) Update session.current_level
                session.current_level = level_name
                session.world_loaded = False
                # 10) For testing purposes only; uncomment to broadcast level change, remove after testing
                #broadcast_level_change(session, char["name"], level_name)
                # 11) Issue the new transfer token
                new_token = session.issue_token(
                    char,
                    target_level=level_name,
                    previous_level=old_level
                )
                # 12) Build and send the ENTER_WORLD packet, including info about the level we just left
                #    old_level     := the name of the level we departed
                #    prev_rec      := char["PreviousLevel"] ⟶ {name, x, y}
                #    old_swf       := its SWF path
                #    old_has_coord := True if we have stored coords
                old_name = old_level
                prev_rec = char.get("PreviousLevel", {})
                prev_x = prev_rec.get("x", 0)
                prev_y = prev_rec.get("y", 0)
                old_swf, _, _, old_is_inst = LEVEL_CONFIG.get(old_name, ("", 0, 0, False))
                old_has_coord = ("x" in prev_rec and "y" in prev_rec)

                swf_path, map_id, base_id, is_inst = LEVEL_CONFIG[level_name]
                is_hard = level_name.endswith("Hard")
                new_moment = "Hard" if is_hard else ""
                new_alter = "Hard" if is_hard else ""

                pkt_out = build_enter_world_packet(
                    transfer_token=new_token,
                    old_level_id=0,
                    # tell the client what we just left
                    old_swf = old_swf,
                    has_old_coord  = old_has_coord,
                    old_x = int(round(prev_x)),
                    old_y = int(round(prev_y)),

                    host="127.0.0.1",
                    port=8080,
                    # New level the player is entering
                    new_level_swf=swf_path,
                    new_map_lvl=map_id,
                    new_base_lvl=base_id,
                    new_internal=level_name,
                    new_moment=new_moment,
                    new_alter=new_alter,
                    new_is_inst=is_inst,
                    new_has_coord=new_has_coord,
                    new_x=int(round(new_x)),
                    new_y=int(round(new_y)),
                    char=char,
                )
                session.conn.sendall(pkt_out)
                #print(
                    #f"[{session.addr}] Sent ENTER_WORLD with token {new_token} for level {level_name}, pos=({new_x},{new_y})")

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

            # Level & Door related packets
            ###################################
            elif pkt == 0x41:
                handle_packet_0x41(session, data, conn)
            elif pkt == 0x7D:
                handle_change_offset_y(session, data)
            ###################################

            #Entity Update Related packets
            ###################################
            elif pkt == 0x07:# Done
                handle_entity_incremental_update(session, data, all_sessions)
            elif pkt == 0xA2:# Done
                handle_linkupdater(session, data, all_sessions)
            elif pkt == 0x09:# Done
                handle_power_cast(session, data, all_sessions)
            elif pkt == 0x08:  # Done
                handle_entity_full_update(session, data, all_sessions)

                # Force NPC load temporarily For testing
                # we will remove this and implement it properly once we are sure Send_Entity_Data is working properly
                try:
                    npcs = load_npc_data_for_level(session.current_level)
                    for npc in npcs:
                        payload = Send_Entity_Data(npc)
                        conn.sendall(struct.pack(">HH", 0x0F, len(payload)) + payload)
                        session.entities[npc["id"]] = npc
                        session.spawned_npcs.append(npc)

                    #print(f"[{session.addr}] NPCs manually triggered after world update")
                except Exception as e:
                    print(f"[{session.addr}] Error spawning NPCs: {e}")
            ###################################


              # Combat Related packets
            ############################################
            elif pkt == 0x0D: # Done
               handle_entity_destroy(session, data, all_sessions)
            elif pkt == 0x79: # Done
               PKTTYPE_BUFF_TICK_DOT(session, data, all_sessions)
            elif pkt == 0x82: # Done
               handle_respawn_ack(session, data, all_sessions)
            elif pkt == 0x77:# Done
                handle_request_respawn(session, data, all_sessions)
            elif pkt == 0x2A:
                handle_grant_reward(session, data, all_sessions)
            elif pkt == 0x0A:# Done
                handle_power_hit(session, data, all_sessions)
            elif pkt == 0x0E:# Done
                handle_projectile_explode(session, data, all_sessions)
            elif pkt == 0x0B:# Done
                handle_add_buff(session, data, all_sessions)
            elif pkt == 0x0C:# Done
                handle_remove_buff(session, data, all_sessions)
            elif pkt == 0x8A:
                handle_change_max_speed(session, data, all_sessions)
            ############################################


            #Login Screen
            ############################################
            elif pkt == 0x19:# Done
                PaperDoll_Request(session, data, conn)
            ############################################


            #Chatting messages NPC talking Emotes etc...
            ############################################
            elif pkt == 0x2C:# Done
                handle_public_chat(session, data, all_sessions)
            elif pkt == 0xC5:# Done
                handle_start_skit(session, data,all_sessions)# i think this is meant to be used during scripted events
            elif pkt == 0x46:# Done
                handle_private_message(session, data, all_sessions)
            elif pkt == 0x7E:# Done
               handle_emote_begin(session, data, all_sessions)
            elif pkt == 0x113:
                #handle_alert_update(session, data)
                pass
            elif pkt == 0x7A:
                handle_talk_to_npc(session, data, all_sessions)
                pass
            ############################################


            # Group Related packets
            ############################################
            elif pkt == 0x65:# Done
                handle_group_invite(session, data, all_sessions)
            ############################################


            # Skill Related packets
            ############################################
            elif pkt == 0xBD:# Done
                handle_hotbar_packet(session, data)  # Equipped skills
            elif pkt == 0xBE:# Done
                Start_Skill_Research(session, data, conn)
            elif pkt == 0xD1:# Done
                handle_research_claim(session) # claim completed upgrade skills
            elif pkt == 0xDD:# Done
                Skill_Research_Cancell_Request(session)
            elif pkt == 0xDE:# Done
                Skill_SpeedUp(session, data)
            ############################################


            # Entity Visuals related packets
            ############################################
            elif pkt == 0x8E:# Done
                handle_change_look(session, data, all_sessions)
            elif pkt == 0xBA:# Done
                payload = data[4:]
                handle_apply_dyes(session, payload)
            ############################################


           # Barn and pets related packets
            ############################################
            elif pkt == 0xB2:# Done
                handle_mount_equip_packet(session, data, all_sessions)
            elif pkt == 0xB3:# Done
                handle_pet_info_packet(session, data, all_sessions)
            elif pkt == 0xEA:
                handle_collect_hatched_egg(session, data)
                pass
            ############################################


            # Gear Set Related Packets
            ############################################
            elif pkt == 0xC8:# Done
                handle_name_gearset(session, data)
            elif pkt == 0xC7:# Done
                handle_create_gearset(session, data)
            elif pkt == 0xC6:# Done
                handle_apply_gearset(session, data)
            ############################################


            # Gear Related packets
            ############################################
            elif pkt == 0xB0:# Done
                handle_rune_packet(session, data) # equips runes on weapon slots
            elif pkt == 0x31:# Done
                handle_gear_packet(session, data)
            elif pkt == 0x30:# Done
                handle_update_equipment(session, data)
            ############################################


            #TODO...
            # Forge related packets
            ############################################
            elif pkt == 0xE2:
                magic_forge_packet(session, data)
            elif pkt == 0xD0:
                collect_forge_charm(session, data)
            elif pkt == 0xB1:
                start_forge_packet(session, data)
            elif pkt == 0xE1:
                cancel_forge_packet(session, data)
            elif pkt == 0x110:
                use_forge_xp_consumable(session, data)
            ############################################


            #TODO...
            # Talent Upgrade related packets
            ############################################
            elif pkt == 0xD6 :
                handle_talent_claim(session, data)
            elif pkt == 0xE0:
                handle_talent_speedup(session, data)
            elif pkt == 0xD4:
                handle_train_talent_point(session, data)
            elif pkt == 0xDF:
                handle_clear_talent_research(session, data)
            elif pkt == 0xD3:
                allocate_talent_points(session, data)
            elif pkt == 0xD9:# the client sends this to acknowledge that the building has finishing upgrading
                 pass
            ############################################


            # LockBox related packets
            ###################################
            elif pkt == 0x107:
                payload = data[4:]
                handle_lockbox_reward(session)
            ###################################


            # Master class related packets
            ############################################
            elif pkt == 0xC3:# Done
                handle_masterclass_packet(session, data)
            ############################################


            # client crash Reports
            ############################################
            elif pkt == 0x7C:
                Client_Crash_Reports(session, data)
            ############################################


            # Buildings Upgrade packets
            ############################################
            elif pkt == 0xDB:
                handle_cancel_upgrade(session, data)
            elif pkt == 0xDC:
                handle_speedup_request(session, data)
            elif pkt == 0xD7:
                handle_building_upgrade(session, data)
            ############################################


            elif pkt == 0xF0:
                handle_volume_enter(session, data)
            elif pkt == 0xBB:
                handle_hp_increase_notice(session, data)
                pass
            elif pkt == 0x78:
                handle_char_regen(session, data)
                pass
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
    #print("For Browser running on : http://localhost/DeveloperMode.html")
    print("For Flash Projector running on : http://localhost/p/cbv/DungeonBlitz.swf?fv=cbq&gv=cbv")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down servers...")
        for server, port in servers:
            server.close()
        sys.exit(0)
