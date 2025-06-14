#!/usr/bin/env python3
import os, signal, socket, struct, hashlib, subprocess, sys, time, secrets, threading
from accounts import get_or_create_user_id, load_accounts
from Character import (
    make_character_dict_from_tuple,
    build_login_character_list_bitpacked,
    build_paperdoll_packet,
    load_characters,
    save_characters
)
from WorldEnter import build_enter_world_packet, Player_Data_Packet
from bitreader import BitReader

HOST, PORT = "127.0.0.1", 1
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
                # enter world
                name = BitReader(data[4:]).read_string()
                for c in session.char_list:
                    if c["name"] == name:
                        tk = session.issue_token(c)
                        pkt_out = build_enter_world_packet(
                            transfer_token=tk, old_level_id=0, old_swf="", has_old_coord=False,
                            old_x=0, old_y=0, old_flashvars="", user_id=1,
                            new_level_swf="LevelsHome.swf/a_Level_Home",
                            new_map_lvl=1, new_base_lvl=1,
                            new_internal="CraftTown", new_moment="", new_alter="",
                            new_is_inst=False
                        )
                        conn.sendall(pkt_out)
                        print("Transfer begin:", name, "tk=",tk)
                        break

            elif pkt == 0x1f:
                # Client asks for “minimal welcome” with a 32-bit raw token
                if len(data) < 8:
                    print("Malformed 0x1F (too short)")
                    continue
                token = int.from_bytes(data[4:8], 'big')
                print("Pending tokens:", list(pending_world.keys()))
                print("Client asked for token:", token)
                char = pending_world.pop(token, None)
                # FALLBACK: if no exact match, but exactly one pending entry left, use it
                if char is None and len(pending_world) == 1:
                    fallback_token, fallback_char = next(iter(pending_world.items()))
                    print(f"Falling back to sole pending token {fallback_token}")
                    char = fallback_char
                    token = fallback_token
                    pending_world.pop(fallback_token, None)
                session.active_tokens.discard(token)
                if char:
                    welcome = Player_Data_Packet(char, transfer_token=token)
                    conn.sendall(welcome)
                    print("Welcome:", char["name"], "(used token", token, ")")
                else:
                    print("Unknown token", token)


            elif pkt == 0x2D:
                # everything after the 4-byte header is the payload
                payload = data[4:]
                # read a 32-bit transfer_token / doorID
                door_id = BitReader(payload).read_method_4()
                print(f"[{session.addr}] OPEN_DOOR packet received, door_id={door_id}")
            # … other packet types …

    except Exception as e:
        print("Session error:", e)
    finally:
        print("Disconnect:", addr)
        session.cleanup()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print("Server listening on", HOST, PORT)
    while True:
        conn, addr = s.accept()
        session = ClientSession(conn, addr)
        threading.Thread(target=handle_client, args=(session,), daemon=True).start()

if __name__ == "__main__":
    if "--run-server" in sys.argv:
        start_server()
    else:
        start_server()
