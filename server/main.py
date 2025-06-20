#!/usr/bin/env python3
import random
import socket, struct, hashlib, sys, time, secrets, threading
from accounts import get_or_create_user_id, load_accounts
from Character import (
    make_character_dict_from_tuple,
    build_login_character_list_bitpacked,
    build_paperdoll_packet,
    load_characters,
    save_characters
)
from level_config import DOOR_MAP, LEVEL_CONFIG
from BitUtils import BitBuffer
from constants import EntType, DyeType
from WorldEnter import build_enter_world_packet, Player_Data_Packet
from bitreader import BitReader

from PolicyServer import start_policy_server
from static_server import start_static_server

HOST = "127.0.0.1"
PORTS = [8080]
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
        self.conn = conn; self.addr = addr
        self.user_id = None
        self.char_list = []
        self.active_tokens = set()
        self.authenticated = False
        self.current_char     = None
        self.current_internal = ""
        self.current_swf      = ""
        self.current_map_lvl  = 0
        self.player_x         = 0
        self.player_y         = 0
    def issue_token(self, char):
        tk = new_transfer_token()
        pending_world[tk] = char
        self.active_tokens.add(tk)
        return tk

    def cleanup(self):
        # Don’t pop pending_world here!
        # Just close the socket.
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
                    # Send error popup (0x1B)
                    err = "Account not found".encode("utf-8")
                    err_pl = struct.pack(">H", len(err)) + err
                    conn.sendall(struct.pack(">HH", 0x1B, len(err_pl)) + err_pl)
                    continue
                session.user_id = user_id
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
                    1,                 # level
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
                # send updated list + paperdoll + popup
                conn.sendall(build_login_character_list_bitpacked(session.char_list))
                pd = build_paperdoll_packet(new_char)
                conn.sendall(struct.pack(">HH",0x1A,len(pd))+pd)
                popup = "Character Successfully Created".encode("utf-8")
                pl = struct.pack(">HH",0x1B,len(popup)+2) + struct.pack(">H",len(popup))+popup
                conn.sendall(pl)

            elif pkt == 0x19:
                # paperdoll refresh
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
                        tk = session.issue_token(c)


                        level_swf = "LevelsHome.swf/a_Level_Home"
                        level_internal = "CraftTown"
                        is_inst = False

                        pending_world[tk] = {
                            "char": c,
                            "new_internal": level_internal,
                            "new_swf": level_swf,
                            "new_map_lvl": 1,
                            "new_base_lvl": 1,
                            "is_inst": is_inst,
                            "spawn_x": 0,
                            "spawn_y": 0,
                        }
                        conn.sendall(build_enter_world_packet(
                            transfer_token=tk,
                            old_level_id=0,
                            old_swf="",
                            has_old_coord=False,
                            old_x=0,
                            old_y=0,
                            old_flashvars="",
                            user_id=1,
                            new_level_swf=level_swf,
                            new_map_lvl=1,
                            new_base_lvl=1,
                            new_internal=level_internal,
                            new_moment="",
                            new_alter="",
                            new_is_inst=is_inst
                        ))
                        session.current_char = c
                        session.current_internal = level_internal
                        session.current_swf = level_swf
                        session.current_map_lvl = 1
                        session.player_x = 0
                        session.player_y = 0
                        print("Transfer begin:", name, "tk=", tk)
                        break

            elif pkt == 0x1f:
                if len(data) < 8:
                    print("Malformed 0x1F (too short)")
                    continue
                token = int.from_bytes(data[4:8], 'big')
                info = pending_world.pop(token, None)
                # fallback if exactly one left
                if info is None and len(pending_world) == 1:
                    ft, fi = next(iter(pending_world.items()))
                    pending_world.pop(ft, None)
                    token, info = ft, fi
                session.active_tokens.discard(token)
                if info:
                    c = info["char"]
                    ni = info["new_internal"]
                    sp, ml, bl = info["new_swf"], info["new_map_lvl"], info["new_base_lvl"]
                    inst = info.get("is_inst", False)
                    sx, sy = info.get("spawn_x", 0), info.get("spawn_y", 0)
                    session.current_char = c
                    session.current_internal = ni
                    session.current_swf = sp
                    session.current_map_lvl = ml
                    session.player_x = sx
                    session.player_y = sy
                    conn.sendall(Player_Data_Packet(c, transfer_token=token))
                    print("Welcome:", c["name"], "(used token", token, ")")
                else:
                    print("Unknown token", token)
                """
            elif pkt == 0x2D:
                door_id = BitReader(data[4:]).read_method_4()
                key = (session.current_internal, door_id)
                next_i = DOOR_MAP.get(key)
                if not next_i:
                    print(f"No DOOR_MAP entry for {key!r}; ignoring")
                    return
                swf, ml, bl, inst = LEVEL_CONFIG[next_i]
                token = session.issue_token(session.current_char)
                pending_world[token] = {
                    "char": session.current_char,
                    "new_internal": next_i,
                    "new_swf": swf,
                    "new_map_lvl": ml,
                    "new_base_lvl": bl,
                    "is_inst": inst,
                    "spawn_x": session.player_x,
                    "spawn_y": session.player_y,
                }
                conn.sendall(build_enter_world_packet(
                    transfer_token=token,
                    old_level_id=session.current_map_lvl,
                    old_swf=session.current_swf,
                    has_old_coord=True,
                    old_x=session.player_x,
                    old_y=session.player_y,
                    old_flashvars=session.current_internal,
                    user_id=1,
                    new_level_swf=swf,
                    new_map_lvl=ml,
                    new_base_lvl=bl,
                    new_internal=next_i,
                    new_moment="",
                    new_alter="",
                    new_is_inst=inst
                ))
                session.current_internal = next_i
                session.current_swf = swf
                session.current_map_lvl = ml
                print(f"SENT ENTER_WORLD to {next_i}")
                """

            elif pkt == 0x08:
              # Heartbeat / time‐sync from client
              # The client sends back the timestamp we gave it in 0x10,
              # so just echo it verbatim.
                        conn.sendall(data)

            elif pkt == 0x41:
              # SWF load‐progress notification (1-byte 0–100)
              # We don’t need to do anything—just swallow it.
              pass

            elif pkt == 0xA2:
              # Flash ExternalInterface / JS bridge handshake
              # Also safe to ignore.
              pass

            elif pkt == 0x07:
                # movement: just broadcast it back to the client (or to other clients)
                # so the game’s own client‐side code will animate the player.
                #conn.sendall(data)
                # optionally log the raw hex if you still want to see it:
                #print(f"[{session.addr}] MOVE raw: {data.hex()}")
                pass

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

            elif pkt == 0x09:
                # Melee‐attack *request* (0x09) from client
                #   payload = [ts:4B] + optional [attackIndex:1B]
                _, length = struct.unpack_from(">HH", data, 0)
                payload = data[4:4 + length]
                if len(payload) == 4:
                    # implicit index 0
                    ts = struct.unpack_from(">I", payload, 0)[0]
                    idx = 0
                elif len(payload) >= 5:
                    ts = struct.unpack_from(">I", payload, 0)[0]
                    idx = payload[4]
                else:
                    print(f"[{session.addr}] ATTACK_REQ malformed (<4B): {payload.hex()}")
                    continue
                #print(f"[{session.addr}] ATTACK_REQ (0x09)  ts={ts}  idx={idx}")

            elif pkt == 0x0E:
                # Ranged‐attack / projectile fire from client
                # Format: [0x0E][length:2B][ts:4B][…projectile data…]
                _, length = struct.unpack_from(">HH", data, 0)
                payload = data[4:4+length]
                if len(payload) >= 4:
                    ts = struct.unpack_from(">I", payload, 0)[0]
                    extra = payload[4:]
                    #print(f"[{session.addr}] RANGED_REQ (0x0E)  ts={ts}  data={extra.hex()}")
                else:
                    print(f"[{session.addr}] RANGED_REQ malformed: {payload.hex()}")

            elif pkt == 0x0A:
                # Melee‐attack *response* / hit packet
                # Format: [0x0A][length:2B][ts:4B][…rest varies…]
                _, length = struct.unpack_from(">HH", data, 0)
                payload = data[4:4+length]
                if len(payload) >= 4:
                    ts = struct.unpack_from(">I", payload, 0)[0]
                    rest = payload[4:]
                    #print(f"[{session.addr}] ATTACK_RES (0x0A)  ts={ts}  data={rest.hex()}")
                else:
                    print(f"[{session.addr}] ATTACK_RES malformed: {payload.hex()}")



            elif pkt == 0x31:
                # strip off the 4-byte header, give us the raw payload
                payload = data[4:]
                br = BitReader(payload)
                # 1) match the client’s `method_9` varint for entity ID:
                entity_id = br.read_method_4()
                # 2) read the 3-bit “padded bit-count header”:
                header = br.read_bits(3)
                bit_count = (header + 1) * 2
                # 3) read exactly bit_count bits for the slot:
                slot = br.read_bits(bit_count)
                # 4) finally read the 11-bit gear ID:
                gear_id = br.read_bits(11)
                print(f"Equip request: entity={entity_id}, slot={slot}, gear={gear_id}")
                # …now update your character and send out a paperdoll refresh…
                continue


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
                # …apply & broadcast…
                continue
            elif pkt == 0xBD:
                payload = data[4:]
                if len(payload) < 1:
                    print(f"Malformed 0xBD packet: too short, payload={payload.hex()}")
                    continue
                if payload.hex() == '2640':
                    print(f"0xBD packet: possible hotbar clear or default action, payload={payload.hex()} ")
                    continue
                br = BitReader(payload)
                max_slots = 4
                slot = 0
                ability_id = 0
                for i in range(max_slots):
                    changed = br.read_bits(1)
                    if changed:
                        slot = i + 1
                        ability_id = br.read_bits(7)
                        break
                if slot == 0:
                    print(f"0xBD packet: no slots changed, payload={payload.hex()}")
                    continue
                remaining_bits = br.remaining_bits()
                entity_id = br.read_bits(remaining_bits) if remaining_bits > 0 else 0
                print(f"Ability equip: slot={slot}, ability_id={ability_id}, entity_id={entity_id} ")
                continue

            #TODO... Sigils reward are missing and the commented out rewards currently crash the game
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
                    8: ("Lockbox01Gear", True),  # Gear (will crash if invalid)
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
                # Pick a random index 0–19
                idx, (name, needs_str) = random.choice(list(reward_map.items()))
                # Build the packet
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

            else:
                # Log any packet we haven't explicitly handled
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
            # Start a thread to accept connections for this server
            threading.Thread(target=accept_connections, args=(server, port), daemon=True).start()
    return servers

if __name__ == "__main__":
    # 1) Flash policy server on loopback only:
    start_policy_server(host="127.0.0.1", port=843)

    # 2) Static HTTP server, serving your "p" folder on localhost:80
    start_static_server(host="127.0.0.1", port=80, directory="content/localhost")

    # 3) Start TCP game servers on both ports
    servers = start_servers()
    print("running on : http://localhost/index.html")
    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down servers...")
        for server, port in servers:
            server.close()
        sys.exit(0)