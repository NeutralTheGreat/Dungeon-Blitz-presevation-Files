#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import signal
import socket
import struct
import hashlib
import subprocess
import sys
import time

from Character import (
    make_character_dict_from_tuple,
    build_login_character_list_bitpacked,
    build_paperdoll_packet,
    load_characters,
    save_characters
)
from WorldEnter import (build_enter_world_packet, Player_Data_Packet)
from bitreader import BitReader

# Watchable extensions (add others if needed)
WATCHED_EXTENSIONS = {".py"}

# -----------------------
# Server logic:
# -----------------------

characters = load_characters()

HOST = '127.0.0.1'
PORT = 1

# When a client selects a character (0x16), we generate a unique token here...
pending_world = {}         # maps transfer_token → character_dict
next_transfer_token = 1    # incrementing integer for each new selection

def parse_movement_payload(payload: bytes):
    if len(payload) < 2:
        print("Too short for movement packet")
        return

    subtype = payload[0]
    flags = payload[1]
    vector = payload[2:]

    print(f"Subtype: {subtype:02x}, Flags: {flags:02x}")
    print(f"Raw Vector Data: {vector.hex()}")

    # Try interpreting bytes in chunks
    if len(vector) >= 6:
        x = int.from_bytes(vector[0:2], byteorder='big', signed=True)
        y = int.from_bytes(vector[2:4], byteorder='big', signed=True)
        z = int.from_bytes(vector[4:6], byteorder='big', signed=True)
        print(f"Interpreted coords: x={x}, y={y}, z={z}")



def build_handshake_response(session_id):
    session_id_bytes = session_id.to_bytes(2, 'big')
    key = b"815bfb010cd7b1b4e6aa90abc7679028"
    challenge_hash = hashlib.md5(session_id_bytes + key).hexdigest()
    dummy_bytes = bytes.fromhex(challenge_hash[:12])  # first 6 bytes
    payload = session_id_bytes + dummy_bytes
    header = struct.pack(">HH", 0x12, len(payload))
    return header + payload


def handle_client(conn, addr):
    global next_transfer_token, pending_world

    print("Connection from", addr)
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break

            hex_data = data.hex()
            print("Received raw data:", hex_data)

            if len(hex_data) < 4:
                continue

            try:
                pkt_type = int(hex_data[:4], 16)
            except ValueError:
                print("Error parsing packet type.")
                continue

            if pkt_type == 0x11:
                # Initial handshake
                session_id = int(hex_data[8:12], 16) if len(hex_data) >= 12 else 0
                print(f"Got handshake packet (0x11), session ID = {session_id}")
                resp = build_handshake_response(session_id)
                conn.sendall(resp)
                print("Sent handshake response (0x12):", resp.hex())

            elif pkt_type in (0x13, 0x14):
                # Auth packet → send character list
                print("Got auth packet (0x14). Sending character list…")
                pkt = build_login_character_list_bitpacked(characters)
                conn.sendall(pkt)
                print("Sent login-character list (0x15):", pkt.hex())

            elif pkt_type == 0x17:
                # Character creation request
                print("Got character creation packet (0x17). Parsing creation data...")
                payload = data[4:]
                try:
                    br = BitReader(payload)
                    name = br.read_string()
                    class_name = br.read_string()
                    level_dummy = 1  # fixed at creation
                    gender = br.read_string()
                    head = br.read_string()
                    hair = br.read_string()
                    mouth = br.read_string()
                    face = br.read_string()
                    hair_color = br.read_bits(24)
                    skin_color = br.read_bits(24)
                    shirt_color = br.read_bits(24)
                    pant_color = br.read_bits(24)
                    equipped_gear = None
                    character_tuple = (
                        name,
                        class_name,
                        level_dummy,
                        gender,
                        head,
                        hair,
                        mouth,
                        face,
                        hair_color,
                        skin_color,
                        shirt_color,
                        pant_color,
                        equipped_gear
                    )
                except Exception as e:
                    print("Error parsing 0x17 packet:", e)
                    # Re-send the list so client doesn’t hang
                    conn.sendall(build_login_character_list_bitpacked(characters))
                    continue

                # Build and store the new character dict
                char_dict = make_character_dict_from_tuple(character_tuple)
                characters.append(char_dict)
                save_characters(characters)
                print(f"Created new char '{name}', class='{class_name}' and saved to JSON.")

                # Send updated character list (0x15)
                list_pkt = build_login_character_list_bitpacked(characters)
                conn.sendall(list_pkt)
                print("Sent updated login-character-list (0x15):", list_pkt.hex())

                # Send initial paper-doll (0x1A)
                pd_payload = build_paperdoll_packet(char_dict)
                pd_pkt = struct.pack(">HH", 0x1A, len(pd_payload)) + pd_payload
                conn.sendall(pd_pkt)
                print("Sent initial paper-doll (0x1A), length:", len(pd_payload))

                # Send “Character Successfully Created” popup (0x1B)
                text_message = "Character Successfully Created"
                text_bytes = text_message.encode('utf-8')
                utf16_length_prefix = struct.pack(">H", len(text_bytes))
                payload2 = utf16_length_prefix + text_bytes
                pkt2 = struct.pack(">HH", 0x1B, len(payload2)) + payload2
                conn.sendall(pkt2)

            elif pkt_type == 0x19:
                # Client requests a paper-doll update for an existing character
                name = BitReader(data[4:]).read_string()
                for char in characters:
                    if char["name"] == name:
                        payload = build_paperdoll_packet(char)
                        pkt = struct.pack(">HH", 0x1A, len(payload)) + payload
                        conn.sendall(pkt)
                        print("Sent paper-doll (0x1A), payload len:", len(payload))
                        break
                else:
                    # char not found → still ack so client doesn’t hang
                    conn.sendall(struct.pack(">HH", 0x1A, 0))


            elif pkt_type == 0x16:
                # Client selected a character and wants to enter the world
                payload = data[4:]
                br = BitReader(payload)
                selected_name = br.read_string()
                for char in characters:
                    if char["name"] == selected_name:
                        # Assign a fresh, unique transfer_token
                        token = next_transfer_token
                        next_transfer_token += 1
                        # Remember which character maps to that token
                        pending_world[token] = char
                        transfer_packet = build_enter_world_packet(
                            transfer_token=token,
                            old_level_id=0,
                            old_swf="",
                            has_old_coord=False,
                            old_x=0,
                            old_y=0,
                            old_flashvars="",
                            user_id=1,
                            new_level_swf="LevelsHome.swf/a_Level_Home",
                            new_map_lvl=1,
                            new_base_lvl=1,
                            new_internal="CraftTown",
                            new_moment="",
                            new_alter="",
                            new_is_inst=False
                        )
                        conn.sendall(transfer_packet)
                        print(f"Sent TRANSFER_BEGIN (0x21) for character {selected_name}, token={token}")
                        break
                else:
                    print(f"Character {selected_name} not found in list")

            elif pkt_type == 0x1f:
                # Client is now asking for “Player data.” 
                br = BitReader(data[4:])
                token = br.read_method_4()
                char = pending_world.pop(token, None)
                if char is None:
                    print(f"Error: 0x1F with unknown transfer_token={token}")
                    continue

                welcome = Player_Data_Packet(char,
                                             transfer_token=token)
                conn.sendall(welcome)
                print(f"Sent  WELCOME (0x10) for character {char['name']} (token={token})")

            elif pkt_type == 0x07:
                print("Got movement/action packet (0x07).")
                payload = data[4:]

                if len(payload) == 0:
                    print("Empty payload.")
                    return

                sub_type = payload[0]
                print(f"Subtype: {sub_type:02x}")

                # You can then branch on sub_type
                if sub_type == 0x04:
                    print("→ Player motion/jump/move packet.")
                    print(f"Payload: {payload.hex()}")

                elif sub_type == 0x05:
                    print("→ Melee attack")

                elif sub_type == 0x08:
                    print("→ Likely jump arc / movement updates")

                else:
                    print(f"→ Unknown subtype for 0x07: {sub_type:02x}")

            elif pkt_type == 0x2D:
                door_id = int.from_bytes(data[4:6], 'big')
                print(f"Received OPEN_DOOR packet for door ID {door_id}")
                # Optionally validate door ID, trigger event, send transfer packet, etc.

            # …any other packet types you support…
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
        print("Client disconnected.")


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on {HOST}:{PORT}...")
    while True:
        conn, addr = s.accept()
        handle_client(conn, addr)


# -------------------------------
# Embedded “auto-reload” wrapper:
# -------------------------------
try:
    from watchdog.events import FileSystemEventHandler
    from watchdog.observers import Observer
except ImportError:
    print("The 'watchdog' package is required for auto-reload. Install it with:\n\n    pip install watchdog\n")
    sys.exit(1)


class ReloaderHandler(FileSystemEventHandler):
    def __init__(self, proc_holder, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.proc_holder = proc_holder

    def on_any_event(self, event):
        if event.is_directory:
            return

        _, ext = os.path.splitext(event.src_path)
        if ext not in WATCHED_EXTENSIONS:
            return

        print(f"[reload] Detected change in {event.src_path}. Restarting server…")
        if self.proc_holder["proc"] is not None:
            try:
                self.proc_holder["proc"].send_signal(signal.SIGINT)
                self.proc_holder["proc"].wait(timeout=5)
            except Exception:
                self.proc_holder["proc"].kill()
                self.proc_holder["proc"].wait()
        self.proc_holder["proc"] = subprocess.Popen([sys.executable, __file__, "--run-server"])


def watcher_loop():
    holder = {"proc": subprocess.Popen([sys.executable, __file__, "--run-server"])}
    event_handler = ReloaderHandler(proc_holder=holder)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
            if holder["proc"].poll() is not None:
                print("[reload] Server process exited. Restarting…")
                holder["proc"] = subprocess.Popen([sys.executable, __file__, "--run-server"])
    except KeyboardInterrupt:
        print("\n[reload] Stopping watcher and server…")
    finally:
        observer.stop()
        observer.join()
        if holder["proc"].poll() is None:
            try:
                holder["proc"].send_signal(signal.SIGINT)
                holder["proc"].wait(timeout=5)
            except Exception:
                holder["proc"].kill()
                holder["proc"].wait()


if __name__ == "__main__":
    # If "--run-server" argument is provided, just run the socket server.
    if len(sys.argv) > 1 and sys.argv[1] == "--run-server":
        try:
            start_server()
        except KeyboardInterrupt:
            print("\nServer shutting down…")
            sys.exit(0)
    else:
        # Otherwise, run the file-watcher wrapper
        print("Starting in auto-reload mode. Watching for file changes…")
        watcher_loop()
