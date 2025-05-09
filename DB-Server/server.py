#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, struct, hashlib, sys, time

HOST = '127.0.0.1'
PORT = 443

# Global storage for characters.
# Each entry is a tuple:
# (name, class_name, level, computed, extra1, extra2, extra3, extra4,
#  hair_color, skin_color, shirt_color, pant_color, equipped_gear)
characters = []

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


def build_entity_packet(character, category="Player"):
    (name, class_name, level, computed, extra1, extra2, extra3, extra4,
     hair_color, skin_color, shirt_color, pant_color, equipped_gear) = character

    # Change this: Use the character's name for the key
    parent = f"Player:{name}"

    computed = computed if computed else "Male"
    extra1 = extra1 if extra1 else "Head01"
    extra2 = extra2 if extra2 else "Hair01"
    extra3 = extra3 if extra3 else "Mouth01"
    extra4 = extra4 if extra4 else "Face01"

    xml = f"""<EntType EntName='{name}' parent='{parent}'>
        <Level>{level}</Level>
        <Name>{name}</Name>
        <HairColor>{hair_color}</HairColor>
        <SkinColor>{skin_color}</SkinColor>
        <ShirtColor>{shirt_color}</ShirtColor>
        <PantColor>{pant_color}</PantColor>
        <GenderSet>{computed}</GenderSet>
        <HeadSet>{extra1}</HeadSet>
        <HairSet>{extra2}</HairSet>
        <MouthSet>{extra3}</MouthSet>
        <FaceSet>{extra4}</FaceSet>
        <CustomScale>{0.8 if class_name.lower() == 'mage' else 1.0}</CustomScale>
        <EquippedGear>{equipped_gear if equipped_gear else ""}</EquippedGear>
    </EntType>"""
    return xml.replace('\n', '').replace('    ', '')


#
# ----------------------- BIT-PACKED READING -----------------------
#

class BitReader:
    def __init__(self, data: bytes):
        self.data = data
        self.bit_index = 0

    def read_bits(self, count: int) -> int:
        result = 0
        for _ in range(count):
            byte_index = self.bit_index // 8
            bit_offset = 7 - (self.bit_index % 8)
            if byte_index >= len(self.data):
                raise ValueError("Not enough data to read")
            bit = (self.data[byte_index] >> bit_offset) & 1
            result = (result << 1) | bit
            self.bit_index += 1
        return result

    def align_to_byte(self):
        remainder = self.bit_index % 8
        if remainder != 0:
            self.bit_index += (8 - remainder)

    def read_string(self) -> str:
        self.align_to_byte()
        length = self.read_bits(16)
        result_bytes = bytearray()
        for _ in range(length):
            result_bytes.append(self.read_bits(8))
        try:
            return result_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return result_bytes.decode('latin1')

    def read_method_4(self) -> int:
        n = self.read_bits(4)
        n = (n + 1) << 1
        return self.read_bits(n)

    def read_method_393(self) -> int:
        return self.read_bits(8)

    def read_method_6(self, bit_count: int) -> int:
        return self.read_bits(bit_count)


#
# ----------------------- BIT-PACKED WRITING -----------------------
#

class BitBuffer:
    def __init__(self):
        self.bits = []

    def _append_bits(self, value, bit_count):
        for i in reversed(range(bit_count)):
            bit = (value >> i) & 1
            self.bits.append(bit)

    def write_utf_string(self, text):
        if text is None:
            text = ""
        length = len(text)
        self._append_bits((length >> 8) & 0xFF, 8)
        self._append_bits(length & 0xFF, 8)
        for ch in text:
            self._append_bits(ord(ch) & 0xFF, 8)

    def write_method_4(self, val):
        if val == 0:
            _loc1_ = 0
            _loc2_ = 2
            self._append_bits(_loc1_, 4)
            self._append_bits(val, _loc2_)
            return
        n = val.bit_length()
        if n % 2 != 0:
            n += 1
        _loc1_ = (n >> 1) - 1
        self._append_bits(_loc1_, 4)
        self._append_bits(val, n)

    def write_method_393(self, val):
        self._append_bits(val & 0xFF, 8)

    def write_method_6(self, val, bit_count):
        self._append_bits(val, bit_count)

    def write_method_13_string(self, text):
        length = len(text)
        self.write_method_4(length)
        for ch in text:
            self._append_bits(ord(ch) & 0xFF, 8)

    def to_bytes(self):
        while len(self.bits) % 8 != 0:
            self.bits.append(0)
        out = bytearray()
        for i in range(0, len(self.bits), 8):
            b = 0
            for bit in self.bits[i:i + 8]:
                b = (b << 1) | bit
            out.append(b)
        return bytes(out)

    # this shows all the user characters in the character select list

############################################################################

# we may have to update this since the character paper doll is not showing when login in

def build_login_character_list_bitpacked():
    buf = BitBuffer()
    user_id = 1
    max_chars = 8
    char_count = len(characters)
    # user_id via method_4()
    buf.write_method_4(user_id)
    # max_chars via method_393 (8 bits)
    buf.write_method_393(max_chars)
    # char_count via method_393 (8 bits)
    buf.write_method_393(char_count)
    for char in characters:
        name, class_name, level, *_ = char
        # The client reads these with method_13 => a 16-bit length plus raw bytes
        buf.write_utf_string(name)
        buf.write_utf_string(class_name)
        # The client reads level with method_6(6 bits)
        buf.write_method_6(level, 6)
    payload = buf.to_bytes()
    header = struct.pack(">HH", 0x15, len(payload))
    return header + payload


#############################################################################
def Character_creation(character):
    # Unpack character details
    name, class_name, level, computed, extra1, extra2, extra3, extra4, \
        hair_color, skin_color, shirt_color, pant_color, equipped_gear = character

    buf = BitBuffer()
    # Write the seven strings (order must match what method_1170 reads)
    buf.write_utf_string(name)  # _loc2_
    buf.write_utf_string(class_name)  # _loc3_
    buf.write_utf_string(computed)  # _loc5_
    buf.write_utf_string(extra1)  # _loc6_
    buf.write_utf_string(extra2)  # _loc7_
    buf.write_utf_string(extra3)  # _loc8_
    buf.write_utf_string(extra4)  # _loc9_

    # Write the four color values (each using 24 bits)
    buf.write_method_6(hair_color, 24)  # _loc10_
    buf.write_method_6(skin_color, 24)  # _loc11_
    buf.write_method_6(shirt_color, 24)  # _loc12_
    buf.write_method_6(pant_color, 24)  # _loc13_

    # Write gear bits based on the character class.
    # Each gear value is written using 11 bits.
    class_lower = class_name.lower()
    if class_lower == "rogue":
        # For Rogue: these values are example gear IDs
        buf.write_method_6(484, 11)  # e.g. Shield
        buf.write_method_6(379, 11)  # e.g. Sword
        buf.write_method_6(584, 11)  # e.g. Gloves
        buf.write_method_6(676, 11)  # e.g. Helmet
        buf.write_method_6(668, 11)  # e.g. Armor
        buf.write_method_6(577, 11)  # e.g. Boots
    elif class_lower == "paladin":
        # For Paladin: these values are example gear IDs
        buf.write_method_6(902, 11)  # e.g. Shield
        buf.write_method_6(890, 11)  # e.g. Sword
        buf.write_method_6(912, 11)  # e.g. Gloves
        buf.write_method_6(916, 11)  # e.g. Helmet
        buf.write_method_6(909, 11)  # e.g. Armor
        buf.write_method_6(905, 11)  # e.g. Boots
    elif class_lower == "mage":
        # For Mage: these values are examples – adjust as needed
        buf.write_method_6(63, 11)  # e.g. Staff
        buf.write_method_6(151, 11)  # e.g. Offhand orb
        buf.write_method_6(75, 11)  # e.g. Robe
        buf.write_method_6(68, 11)  # e.g. focus
        buf.write_method_6(77, 11)  # e.g. Gloves
        buf.write_method_6(70, 11)  # e.g. Boots
    else:
        # Default: no gear equipped
        for i in range(6):
            buf.write_method_6(0, 11)

    payload = buf.to_bytes()
    header = struct.pack(">HH", 0x1A, len(payload))
    return header + payload



    # enter world packets testing

###################################################################

 # i think the game expects a (Begin Transfer) transfer before (build_load_level_packet) is send
def build_begin_transfer_packet():
    buf = BitBuffer()
    # Not clear if it needs any payload, but probably zero
    payload = buf.to_bytes()
    header = struct.pack(">HH", 0x1B, len(payload))
    return header + payload


def build_load_level_packet(map_name, map_level, base_level,
                            internal_name, moment_params,
                            alter_params, is_instanced):
    """
    Construct the 0x1C “load level” packet so the Flash client
    will call Level.method_1853(...) and begin loading the world.
    """
    buf = BitBuffer()
    # write the level name (16-bit length + UTF-8 bytes)
    buf.write_utf_string(map_name)
    # write mapLevel and baseLevel as simple 8-bit values
    buf.write_method_393(map_level)
    buf.write_method_393(base_level)
    # write the internal SWF linkage name
    buf.write_utf_string(internal_name)
    # write the momentParams (e.g. "Normal,Tutorial", or "" for default)
    buf.write_utf_string(moment_params)
    # write the alterParams (e.g. "Hard", or "" for default)
    buf.write_utf_string(alter_params)
    # write instancing flag (0 or 1) as 8-bit
    buf.write_method_393(1 if is_instanced else 0)

    payload = buf.to_bytes()
    # packet-type 0x1C, big-endian length
    return struct.pack(">HH", 0x1C, len(payload)) + payload

###############################################################


def handle_client(conn, addr):
    print("Connection from", addr)
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break

            if b"<policy-file-request/>" in data:
                print("Flash policy request received. Sending policy XML.")
                conn.sendall(policy_response)
                continue

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
                pkt = build_login_character_list_bitpacked()
                conn.sendall(pkt)
                print("Sent login character list (0x15):", pkt.hex())

            elif pkt_type == 0x17:
                print("Got character creation packet (0x17). Parsing creation data...")
                payload = data[4:]
                try:
                    br = BitReader(payload)
                    name = br.read_string()
                    class_name = br.read_string()
                    computed = br.read_string()
                    extra1 = br.read_string()
                    extra2 = br.read_string()
                    extra3 = br.read_string()
                    extra4 = br.read_string()
                    hair_color = br.read_bits(24)
                    skin_color = br.read_bits(24)
                    shirt_color = br.read_bits(24)
                    pant_color = br.read_bits(24)
                    # Set default gear based on class

                    # the default gear is already handled elsewhere at (Character_creation)
                    # the reason im keeping this is because the server crashes without it
                    default_gear = """ """

                    new_char = (
                        name, class_name, 1, computed, extra1, extra2, extra3, extra4,
                        hair_color, skin_color, shirt_color, pant_color, default_gear
                    )
                    print("Parsed Character Creation Packet:")
                    print("  Name:     ", name)
                    print("  ClassName:", class_name)
                    print("  Extra:    ", [computed, extra1, extra2, extra3, extra4])
                    print("  Colors:   ", [hair_color, skin_color, shirt_color, pant_color])
                    print("  Gear:     ", default_gear)
                    characters.append(new_char)
                    print(f"Created new char name='{name}', class='{class_name}'")

                except Exception as e:
                    print("Error parsing create character packet:", e)

                    continue

                # Send updated character list immediately
                # Send updated character list (0x15)
                pkt = build_login_character_list_bitpacked()
                conn.sendall(pkt)
                print("Sent updated login character list (0x15):", pkt.hex())


                # Send enter game character data for method_1170
                enter_packet = Character_creation(new_char)
                conn.sendall(enter_packet)
                print("Sent character data  (0x1A) with full character info:", enter_packet.hex())

                begin_transfer_pkt = build_begin_transfer_packet()
                conn.sendall(begin_transfer_pkt)
                print("Sent begin transfer packet (0x1B)")

                  # NEW: Send load level packet (0x1C) to trigger world loading
                load_level_pkt = build_load_level_packet(
                    map_name="LevelsHome.swf/a_Level_HomeTutorial",  # ← DevSettings.standAloneMapName
                    map_level=1,  # ← DevSettings.standAloneMapLevel
                    base_level=1,  # ← DevSettings.var_1351
                    internal_name="CraftTown",  # ← DevSettings.standAloneMapInternalName
                    moment_params="",  # ← DevSettings.standAloneMomentParams
                    alter_params="",  # ← DevSettings.standAloneAlterParams
                    is_instanced=True  # ← DevSettings.standAloneIsInstanced
                )
                conn.sendall(load_level_pkt)
                print("Sent load level packet (0x1C):", load_level_pkt.hex())
                  # NOW send LOGIN_TO_GAME_LOAD_LEVEL (0x1F) with length=0
                login_to_game_hdr = struct.pack(">HH", 0x1F, 0)
                conn.sendall(login_to_game_hdr)
                print("Sent login to game load level (0x1F):", login_to_game_hdr.hex())

                # i dont think this is needed
                """
                # Finally, send the paperdoll update (0x7C)
                paperdoll_xml = build_entity_packet(new_char, category="Player")
                buf = BitBuffer()
                buf.write_utf_string(paperdoll_xml)
                pd_payload = buf.to_bytes()
                pd_pkt = struct.pack(">HH", 0x7C, len(pd_payload)) + pd_payload
                conn.sendall(pd_pkt)
                print("Sent paperdoll update (0x7C):", pd_pkt.hex())
                time.sleep(0.2)
                """

                

                # i belive this code is to start the world load after a character has been selected or a new character has been created(im not really sure yet... )

            ###################################################################################
            ###################################################################################

            elif pkt_type == 0x16:
                # client selected a character
                payload = data[4:]
                if len(payload) > 0:
                    br = BitReader(payload)
                    selected_name = br.read_string()
                    print("Received character selection (0x16) from client:", selected_name)
                    # find the tuple for that character
                    for char in characters:
                        if char[0] == selected_name:
                            # 1) Begin transfer (0x1B)
                            begin_transfer = struct.pack(">HH", 0x1B, 0)
                            conn.sendall(begin_transfer)
                            print("Sent begin transfer (0x1B):", begin_transfer.hex())
                            # 2) Load level (0x1C)
                            load_level = build_load_level_packet(
                                map_name="LevelsHome.swf/a_Level_Home",
                                map_level=1,
                                base_level=1,
                                internal_name="CraftTown",
                                moment_params="",
                                alter_params="",
                                is_instanced=True
                            )
                            conn.sendall(load_level)
                            print("Sent load level (0x1C):", load_level.hex())
                            # 3) Login‑to‑game ack (0x1F)
                            login_to_game = struct.pack(">HH", 0x1F, 0)
                            conn.sendall(login_to_game)
                            print("Sent login to game (0x1F):", login_to_game.hex())
                            # 4) Paper‑doll update (0x7C)
                            xml = build_entity_packet(char, category="Player")
                            buf = BitBuffer()
                            buf.write_utf_string(xml)
                            pd_payload = buf.to_bytes()
                            pd_pkt = struct.pack(">HH", 0x7C, len(pd_payload)) + pd_payload
                            conn.sendall(pd_pkt)
                            print("Sent paperdoll update (0x7C):", pd_pkt.hex())
                            break
                    else:
                        # character name not found: ack empty
                        ack = struct.pack(">HH", 0x16, 0)
                        conn.sendall(ack)
                        print("Character not found, sent empty 0x16 ack:", ack.hex())
                else:
                    # no payload: resend character list
                    updated = build_login_character_list_bitpacked()
                    conn.sendall(updated)
                    print("Empty select payload; resent char list (0x15):", updated.hex())


               ###################################################################################
               ###################################################################################


            elif pkt_type == 0x19:
                print("Got packet type 0x19. Request for character details.")
                payload = data[4:]  # Skip 4-byte header (type + length)
                br = BitReader(payload)
                try:
                    name = br.read_string()
                    print(f"Requested character: {name}")
                    # Find character by name
                    for char in characters:
                        if char[0] == name:
                            xml = build_entity_packet(char, category="Player")
                            buf = BitBuffer()
                            buf.write_utf_string(xml)
                            pd_payload = buf.to_bytes()
                            pd_pkt = struct.pack(">HH", 0x7C, len(pd_payload)) + pd_payload
                            conn.sendall(pd_pkt)
                            print("Sent paperdoll update (0x7C):", pd_pkt.hex())
                            break
                    else:
                        print(f"Character '{name}' not found.")
                        ack_pkt = struct.pack(">HH", 0x19, 0)
                        conn.sendall(ack_pkt)
                        print("Sent 0x19 ack:", ack_pkt.hex())
                except Exception as e:
                    print("Error parsing 0x19 packet:", e)
                    ack_pkt = struct.pack(">HH", 0x19, 0)
                    conn.sendall(ack_pkt)
                    print("Sent 0x19 ack:", ack_pkt.hex())

            elif pkt_type == 0x7C:
                print("Received packet type 0x7C. (Appearance/cue update)")
                if characters:
                    entity_xml = build_entity_packet(characters[0], category="Player")
                    buf = BitBuffer()
                    buf.write_utf_string(entity_xml)
                    payload = buf.to_bytes()
                    response = struct.pack(">HH", 0x7C, len(payload)) + payload
                    conn.sendall(response)
                    print("Sent entity packet (0x7C):", response.hex())
                else:
                    print("No character data available. Sending empty 0x7C response.")
                    response = struct.pack(">HH", 0x7C, 0)
                    conn.sendall(response)
                    print("Sent 0x7C response:", response.hex())

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
