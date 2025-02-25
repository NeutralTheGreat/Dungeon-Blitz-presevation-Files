#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, struct, hashlib, sys

HOST = '127.0.0.1'
PORT = 443

# Global storage for characters.
# Each entry will be a tuple:
# (name, class_name, level, extra1, extra2, extra3, extra4, hair_color, skin_color, shirt_color, pant_color)
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
            # Ensure we don't run past the data
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
        # method_1250 writes a 16-bit length first
        length = self.read_bits(16)
        result_bytes = bytearray()
        for _ in range(length):
            result_bytes.append(self.read_bits(8))
        try:
            return result_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return result_bytes.decode('latin1')  # fallback

    def read_method_4(self) -> int:
        # method_4: read 4 bits, then interpret (n+1)<<1 bits for the value.
        n = self.read_bits(4)
        n = (n + 1) << 1
        return self.read_bits(n)

    def read_method_393(self) -> int:
        # Simply read 8 bits (one byte)
        return self.read_bits(8)

    def read_method_6(self, bit_count: int) -> int:
        return self.read_bits(bit_count)

#
# ----------------------- BIT-PACKED WRITING (for char list 0x15) -----------------------
#

class BitBuffer:
    def __init__(self):
        self.bits = []

    def _append_bits(self, value, bit_count):
        for i in reversed(range(bit_count)):
            bit = (value >> i) & 1
            self.bits.append(bit)

    def write_utf_string(self, text):
        """
        Match the client's method_13() usage:
          - 16 bits of length
          - length * 8 bits of character data
        No "method_4" trick here; just a plain 16-bit length.
        """
        if text is None:
            text = ""
        length = len(text)
        # Write 16 bits for length:
        self._append_bits((length >> 8) & 0xFF, 8)  # high byte
        self._append_bits(length & 0xFF, 8)         # low byte
        # Then length * 8 bits of data
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
        # For the character list we use a simpler routine (if needed)
        length = len(text)
        self.write_method_4(length)
        for ch in text:
            self._append_bits(ord(ch) & 0xFF, 8)

    def to_bytes(self):
        # Pad out to multiple of 8 bits
        while len(self.bits) % 8 != 0:
            self.bits.append(0)
        out = bytearray()
        for i in range(0, len(self.bits), 8):
            b = 0
            for bit in self.bits[i:i+8]:
                b = (b << 1) | bit
            out.append(b)
        return bytes(out)

def build_login_character_list_bitpacked():
    buf = BitBuffer()

    user_id = 1
    max_chars = 9
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



#
# ----------------------- SERVER MAIN LOGIC -----------------------
#

def handle_client(conn, addr):
    print("Connection from", addr)
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break

            # Flash policy request
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
                # handshake
                session_id = 0
                if len(hex_data) >= 12:
                    session_id = int(hex_data[8:12], 16)
                print(f"Got handshake packet (0x11), session ID = {session_id}")
                conn.sendall(build_handshake_response(session_id))
                print("Sent handshake response (0x12).")
                challenge_packet = build_login_challenge("CHALLENGE")
                conn.sendall(challenge_packet)
                print("Sent login challenge (0x13).")

            elif pkt_type == 0x13 or pkt_type == 0x14:
                print("Got authentication packet (0x13/0x14). Parsing...")
                # For authentication, just send back the character list.
                pkt = build_login_character_list_bitpacked()
                conn.sendall(pkt)
                print("Sent login character list (0x15).")

            elif pkt_type == 0x17:
                # Character creation packet
                print("Got character creation packet (0x17). Parsing creation data...")
                # The packet header is 4 bytes; payload is the rest.
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
                except Exception as e:
                    print("Error parsing create character packet:", e)
                    continue

                print("Parsed Character Creation Packet:")
                print("  Name:     ", name)
                print("  ClassName:", class_name)
                print("  Extra:    ", [computed, extra1, extra2, extra3, extra4])
                print("  Colors:   ", [hair_color, skin_color, shirt_color, pant_color])

                # For a new character, level is 1.
                new_char = (name, class_name, 1, computed, extra1, extra2, extra3, extra4,
                            hair_color, skin_color, shirt_color, pant_color)
                characters.append(new_char)
                print(f"Created new char: userID=1, name='{name}', class='{class_name}'")
                pkt = build_login_character_list_bitpacked()
                conn.sendall(pkt)
                print("Sent updated login character list (0x15).")

            elif pkt_type == 0x16:
                print("Got character select packet (0x16). Acknowledge.")
                conn.sendall(struct.pack(">HH", 0x16, 0))

            elif pkt_type == 0x19:
                print("Got packet type 0x19. Acknowledge.")
                conn.sendall(struct.pack(">HH", 0x19, 0))

            elif pkt_type == 0x7C:
                # If the client sends a 0x7C packet (e.g. for cue or appearance update), log it.
                print("Received packet type 0x7C. (Appearance/cue update) - currently unhandled.")
                conn.sendall(struct.pack(">HH", 0x7C, 0))

            else:
                print(f"Unhandled packet type: 0x{pkt_type:02X}")

    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
        print("Client disconnected.")

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"Listening on {HOST}:{PORT} (NO SSL)...")
    while True:
        conn, addr = s.accept()
        handle_client(conn, addr)

if __name__ == "__main__":
    start_server()