#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, struct, hashlib, sys, time

HOST = '127.0.0.1'
PORT = 443

transfer_token = 1

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

    def debug_bytes(self):
        bytes_data = self.to_bytes()
        print("Packet hex:", bytes_data.hex())

    def align_to_byte(self):
        """Pads the bit buffer with zeros to the next byte boundary."""
        while len(self.bits) % 8 != 0:
            self.bits.append(0)


    def _append_bits(self, value, bit_count):
        for i in reversed(range(bit_count)):
            bit = (value >> i) & 1
            self.bits.append(bit)

    def write_utf_string(self, text):
        """
        Write a length-prefixed UTF-8 string exactly as Flash's ByteArray.readUTF() expects:
          - 2-byte big-endian prefix giving the *byte* length of the UTF-8 data
          - that many raw UTF-8 bytes
        """
        if text is None:
            text = ""
        data = text.encode('utf-8')  # encode to UTF-8 bytes
        length = len(data)  # now length is in *bytes*
        # write the two-byte prefix
        self._append_bits((length >> 8) & 0xFF, 8)
        self._append_bits(length & 0xFF, 8)
        # write each byte of the UTF-8 data
        for b in data:
            self._append_bits(b, 8)

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
            self.bits.append(0)  # Pad to byte boundary
        out = bytearray()
        for i in range(0, len(self.bits), 8):
            byte = 0
            for bit in self.bits[i:i + 8]:
                byte = (byte << 1) | bit
            out.append(byte)
        return bytes(out)

    # this shows all the user characters in the character select list
############################################################################

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

###################################################################

def handle_client(conn, addr):
    print("Connection from", addr)
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break

            #if b"<policy-file-request/>" in data:
                #print("Flash policy request received. Sending policy XML.")
                #conn.sendall(policy_response)
                #continue

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

            ###################################################################################

            elif pkt_type == 0x16:
                payload = data[4:]
                if not payload:
                    continue
                br = BitReader(payload)
                selected_name = br.read_string()
                for char in characters:
                    if char[0] == selected_name:
                        # 1) Send the “enter world” (transfer) packet
                        enter_world = build_enter_world_packet(
                            transfer_token=transfer_token,
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
                        conn.sendall(enter_world)
                        print("Sent TRANSFER_BEGIN+READY:", enter_world.hex())
                        break

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
            """
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

            else:
                # no payload → resend character list
                updated = build_login_character_list_bitpacked()
                conn.sendall(updated)
                print("Sent updated character list (0x15):", updated.hex())
            """

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
