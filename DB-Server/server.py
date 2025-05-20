#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, struct, hashlib, sys, time
import json
import os
from Character import (
    make_character_dict_from_tuple,
    build_login_character_list_bitpacked,
    build_paperdoll_packet,
    load_characters,
    save_characters
)
from bitreader import BitReader
characters = load_characters()
from BitUtils import BitBuffer

HOST = '127.0.0.1'
PORT = 443

transfer_token = 1
PKTTYPE_WELCOME = 0x10

# The Flash policy file
policy_response = b"""<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy SYSTEM="http://www.adobe.com/xml/dtds/cross-domain-policy.dtd">
<cross-domain-policy>
  <allow-access-from domain="*" to-ports="443"/>
</cross-domain-policy>\x00"""

def build_handshake_response(session_id):
    session_id_bytes = session_id.to_bytes(2, 'big')
    key = b"815bfb010cd7b1b4e6aa90abc7679028"
    challenge_hash = hashlib.md5(session_id_bytes + key).hexdigest()
    dummy_bytes = bytes.fromhex(challenge_hash[:12])  # first 6 bytes
    payload = session_id_bytes + dummy_bytes
    header = struct.pack(">HH", 0x12, len(payload))
    return header + payload

def build_login_challenge(challenge_str):
    cbytes = challenge_str.encode('utf-8')
    payload = struct.pack(">H", len(cbytes)) + cbytes
    header = struct.pack(">HH", 0x13, len(payload))
    return header + payload

###################################################################

def build_enter_world_packet(
    transfer_token: int,
    old_level_id: int,
    old_swf: str,
    has_old_coord: bool,
    old_x: int,
    old_y: int,
    old_flashvars: str,
    user_id: int,
    new_level_swf: str,
    new_map_lvl: int,
    new_base_lvl: int,
    new_internal: str,
    new_moment: str,
    new_alter: str,
    new_is_inst: bool
) -> bytes:
    buf = BitBuffer()

    # 1) transferToken + oldLevelId
    buf.write_method_4(transfer_token)
    buf.write_method_4(old_level_id)

    # 2) old SWF path
    buf.write_utf_string(old_swf)

    # 3) old coords?
    buf._append_bits(1 if has_old_coord else 0, 1)
    if has_old_coord:
        buf.write_method_4(old_x)
        buf.write_method_4(old_y)

    # 4) old flashVars
    buf.write_utf_string(old_flashvars)

    # 5) userID
    buf.write_method_4(user_id)

    # 6) new SWF path
    buf.write_utf_string(new_level_swf)

    # 7) map/base levels (6 bits each)
    buf.write_method_6(new_map_lvl, 6)
    buf.write_method_6(new_base_lvl, 6)

    # 8) new strings
    buf.write_utf_string(new_internal)
    buf.write_utf_string(new_moment)
    buf.write_utf_string(new_alter)

    # 9) new isInstanced
    buf._append_bits(1 if new_is_inst else 0, 1)
    buf.align_to_byte()

    payload = buf.to_bytes()
    return struct.pack(">HH", 0x21, len(payload)) + payload

clientEntID = 500
clientEntName = "Frosby"
characterLevel = 20
MAX_CHAR_LEVEL_BITS = 1
skinID = 1
currGold = 100
currGems = 100

#TODO.....
     #WELCOME packet
##############################################################
def build_welcome_packet():
    buf = BitBuffer()

    # 1) clientEntID
    buf.write_method_4(clientEntID)

  # 2) clientEntName — writeUTF (2-byte length + UTF-8), then align to the next byte
    buf.write_utf_string(clientEntName)
    buf.align_to_byte()

    # 3) characterLevel
    buf.write_method_6(characterLevel, MAX_CHAR_LEVEL_BITS)

    # 4) skin/class ID
    buf.write_method_4(skinID)

    # 5) currGold
    buf.write_method_4(currGold)

    # 6) currGems
    buf.write_method_4(currGems)

    # 7) **hasOptions flag** (1 bit). 0 = skip all the appearance data
    buf._append_bits(0, 1)
    buf.align_to_byte()

    # … now continue with master‐ranks, world code, bonusLevels, pet list …

    payload = buf.to_bytes()
    header  = struct.pack(">HH", PKTTYPE_WELCOME, len(payload))
    return header + payload

def handle_client(conn, addr):
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
                session_id = int(hex_data[8:12], 16) if len(hex_data) >= 12 else 0
                print(f"Got handshake packet (0x11), session ID = {session_id}")
                resp = build_handshake_response(session_id)
                conn.sendall(resp)
                print("Sent handshake response (0x12):", resp.hex())

                challenge_packet = build_login_challenge("CHALLENGE")
                conn.sendall(challenge_packet)
                print("Sent login challenge (0x13):", challenge_packet.hex())

            elif pkt_type in (0x13, 0x14):
                print("Got authentication packet (0x13/0x14). Parsing...")
                pkt = build_login_character_list_bitpacked(characters)
                conn.sendall(pkt)
                print("Sent login character list (0x15):", pkt.hex())

            elif pkt_type == 0x17:
                print("Got character creation packet (0x17). Parsing creation data...")
                payload = data[4:]
                try:
                    br = BitReader(payload)
                    name = br.read_string()
                    class_name = br.read_string()
                    level_dummy = 1  # level is fixed at creation
                    gender = br.read_string()
                    head = br.read_string()
                    hair = br.read_string()
                    mouth = br.read_string()
                    face = br.read_string()
                    hair_color = br.read_bits(24)
                    skin_color = br.read_bits(24)
                    shirt_color = br.read_bits(24)
                    pant_color = br.read_bits(24)
                    # equipped_gear placeholder, will be handled by make_character_dict...
                    equipped_gear = None
                    # Build the raw-character tuple exactly as make_character_dict expects
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

                # Convert tuple → full dict (fills in gearList, defaults, etc.)
                char_dict = make_character_dict_from_tuple(character_tuple)
                # Append + persist
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

                #i just added this so the game will show a pop wich can be removed instead of getting stuck at (creating Character...)
                PopUpError = struct.pack(">HH", 0x1B, 0)
                conn.sendall(PopUpError)
                print("Sent login to game load level (0x1F):", PopUpError.hex())
            ###################################################################################
            elif pkt_type == 0x19:
                name = BitReader(data[4:]).read_string()
                for char in characters:
                    if char["name"] == name:
                        payload = build_paperdoll_packet(char)  # use char, not new_char
                        pkt = struct.pack(">HH", 0x1A, len(payload)) + payload
                        conn.sendall(pkt)
                        print("Sent paper-doll (0x1A), payload len:", len(payload))
                        break
                else:
                    # character not found → still ack so the client doesn't hang
                    conn.sendall(struct.pack(">HH", 0x1A, 0))

            elif pkt_type == 0x16:
                payload = data[4:]
                br = BitReader(payload)
                selected_name = br.read_string()
                for char in characters:
                    if char["name"] == selected_name:
                        # Send ENTER_WORLD (transfer) packet
                        transfer_packet = build_enter_world_packet(
                            transfer_token=1,
                            old_level_id=0,
                            old_swf="",
                            has_old_coord=False,
                            old_x=0,
                            old_y=0,
                            old_flashvars="",
                            user_id=1,
                            new_level_swf="LevelsTut.swf/a_Level_TutorialBoat",
                            new_map_lvl=1,
                            new_base_lvl=1,
                            new_internal="CraftTown",
                            new_moment="Normal",
                            new_alter="",
                            new_is_inst=True
                        )
                        conn.sendall(transfer_packet)
                        print("Sent TRANSFER_BEGIN (0x1C)")
                        # Send WELCOME (0x10) packet (for now this will crash the game )
                        #welcome_pkt = build_welcome_packet()
                        #conn.sendall(welcome_pkt)
                        #print("Sent WELCOME (0x10)")
                        break
                else:
                    print(f"Character {selected_name} not found in list")

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

if __name__ == "__main__":
    start_server()
