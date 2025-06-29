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
from Commands import handle_hotbar_packet
from BitUtils import BitBuffer
from constants import EntType, DyeType
from WorldEnter import build_enter_world_packet, Player_Data_Packet
from bitreader import BitReader
from PolicyServer import start_policy_server
from static_server import start_static_server

HOST = "127.0.0.1"
PORTS = [8080]#7498 for Developer mode
pending_world = {}  # token → character dict

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
        self.current_character = None   # ← initialize here
        self.current_level = None
        self.world_loaded = False    # ← add this

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

def handle_client(session: ClientSession):
    conn = session.conn; addr = session.addr
    print("Connected:", addr)
    conn.settimeout(300)
    try:
        while True:
            try:
                data = conn.recv(4096)
            except socket.timeout:
                print("Timeout:", addr); break
            if not data:
                break

            hex_data = data.hex()
            print("Received raw data:", hex_data)

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
                    # Not logged in: send error pop-up and skip
                    msg = "Please log in first".encode("utf-8")
                    pl = struct.pack(">H", len(msg)) + msg
                    conn.sendall(struct.pack(">HH", 0x1B, len(pl)) + pl)
                    continue
                br = BitReader(data[4:])
                tup = (
                    br.read_string(),  # name
                    br.read_string(),  # class
                    50,                 # level
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
                conn.sendall(struct.pack(">HH",0x1A,len(pd))+pd)
                popup = "Character Successfully Created".encode("utf-8")
                pl = struct.pack(">HH",0x1B,len(popup)+2) + struct.pack(">H",len(popup))+popup
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
                        session.current_level = "CraftTown"
                        # **Inject the user_id so char carries it forward**
                        c["user_id"] = session.user_id
                        tk = session.issue_token(c)
                        pkt_out = build_enter_world_packet(
                            transfer_token=tk,
                            old_level_id=0,
                            old_swf="",
                            has_old_coord=False,
                            old_x=0,
                            old_y=0,
                            host="127.0.0.1",
                            port=8080,
                            new_level_swf="LevelsHome.swf/a_Level_Home",
                            new_map_lvl=1,
                            new_base_lvl=1,
                            new_internal="CraftTown",
                            new_moment="",
                            new_alter="",
                            new_is_inst=False
                        )
                        conn.sendall(pkt_out)
                        print("Transfer begin:", name, "tk=", tk)
                        break

            elif pkt == 0x1f:
                if len(data) < 8:
                    print("Malformed 0x1F (too short)")
                    continue
                token = int.from_bytes(data[4:8], 'big')
                print("Pending tokens:", list(pending_world.keys()))
                print("Client asked for token:", token)
                char = pending_world.pop(token, None)
                if char is None and len(pending_world) == 1:
                    fallback_token, fallback_char = next(iter(pending_world.items()))
                    print(f"Falling back to sole pending token {fallback_token}")
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
                    # Also set current_character if you haven’t already
                    session.current_character = char["name"]
                     # The server just sent them into `char["knownLevels"][0]`, so:
                    first_level = char.get("knownLevels", [{}])[0].get("name", "NewbieRoad")
                    session.current_level = first_level
                    welcome = Player_Data_Packet(char, transfer_token=token)
                    conn.sendall(welcome)
                    print("Welcome:", char["name"], "(used token", token, ")")

            elif pkt == 0x2D:
                door_id = BitReader(data[4:]).read_method_4()
                print(f"[{session.addr}] OPEN_DOOR packet received, door_id={door_id}")
                # Only send Enter‑World once:
                """"
                if session.world_loaded:
                    print("World already loaded; skipping world‑change on door click.")
                    continue
                current = getattr(session, "current_level", None)
                if current is None:
                    print(f"No current_level; cannot open door {door_id}")
                    continue
                key = (current, door_id)
                if key not in DOOR_MAP:
                    print(f"Unknown door key: {key}")
                    continue
                next_level = DOOR_MAP[key]
                swf_path, map_lvl, base_lvl, is_inst = LEVEL_CONFIG[next_level]
                tk = session.issue_token(session.player_data)
                enter_pkt = build_enter_world_packet(
                    transfer_token=tk,
                    old_level_id=LEVEL_CONFIG[current][1],
                    old_swf=LEVEL_CONFIG[current][0],
                    has_old_coord=True,
                    old_x=session.player_data.get("x", 0),
                    old_y=session.player_data.get("y", 0),
                    host=HOST, port=8080,
                    new_level_swf=swf_path,
                    new_map_lvl=map_lvl,
                    new_base_lvl=base_lvl,
                    new_internal=next_level,
                    new_moment="", new_alter="",
                    new_is_inst=is_inst
                )
                conn.sendall(enter_pkt)
                print(f"Sent level‑change: {current} → {next_level} (token={tk})")
                session.current_level = next_level
                session.world_loaded = True  # ← mark that we've done it
                 """
            elif pkt == 0xBD:
                handle_hotbar_packet(session, data)

            elif pkt == 0xCC: #no idea what this does
                pass

            elif pkt == 0xA2:
                #print(f"[{session.addr}] Received packet 0xA2 (2-byte zero payload).")
                # Optional: parse it
                flag = int.from_bytes(data[4:6], 'big')
                #print(f"  Parsed flag value = {flag}")
                # Do nothing for now

            elif pkt == 0x08:
                print(f"[{session.addr}] Packet 0x08: sync/startup payload ({len(data[4:])} bytes): {data[4:].hex()}")

            elif pkt == 0x41:
                val = int.from_bytes(data[4:6], 'big')
                print(f"[{session.addr}] Packet 0x41: Sync ID or state = {val}")

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

            elif pkt == 0xBA:
                payload = data[4:]
                br = BitReader(payload)
                # 1) clientEntID
                entity_id = br.read_method_4()
                # 2) per‐slot dye pairs
                dyes_by_slot = {}
                for slot in range(1, EntType.MAX_SLOTS):
                    has_pair = br.read_bits(1)
                    if has_pair:
                        d1 = br.read_bits(DyeType.BITS)
                        d2 = br.read_bits(DyeType.BITS)
                        dyes_by_slot[slot] = (d1, d2)
                # 3) “apply permanently?” preview flag
                preview_only = bool(br.read_bits(1))
                # 4) two extra dyes
                primary_dye = None
                if br.read_bits(1):
                    primary_dye = br.read_bits(DyeType.BITS)
                secondary_dye = None
                if br.read_bits(1):
                    secondary_dye = br.read_bits(DyeType.BITS)
                print(f"Dyes: ent={entity_id}, slots={dyes_by_slot}, "
                      f"preview={preview_only}, primary={primary_dye}, secondary={secondary_dye}")

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
        try:
            conn, addr = s.accept()
            session = ClientSession(conn, addr)
            threading.Thread(target=handle_client, args=(session,), daemon=True).start()
        except Exception as e:
            print(f"Error accepting connections on port {port}: {e}")

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
    print("running on : http://localhost/index.html")
    #print("running on : http://localhost/DeveloperMode.html")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down servers...")
        for server, port in servers:
            server.close()
        sys.exit(0)