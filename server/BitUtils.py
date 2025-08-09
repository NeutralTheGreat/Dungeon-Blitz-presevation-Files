# BitUtils.py
import struct
class BitBuffer:
    def __init__(self, debug=True):
        self.bits = []
        self.debug = debug
        self.debug_log = [] if debug else None

    def align_to_byte(self):
        while len(self.bits) % 8 != 0:
            self.bits.append(0)
            if self.debug:
                self.debug_log.append("align_pad=0")

    def write_method_309(self, val: float):
        self.write_float(val)
        if self.debug:
            self.debug_log.append(f"method_309={val}")

    def write_method_24(self, val: int):
        """
        Write a signed integer as a 1-bit sign flag followed by the magnitude via method_9.
        - val: Signed integer to write.
        """
        sign = 1 if val < 0 else 0
        self._append_bits(sign, 1)
        self.write_method_9(abs(val))
        if self.debug:
            self.debug_log.append(f"method_24={val}, sign={sign}")

    def _append_bits(self, value, bit_count):
        if self.debug:
            self.debug_log.append(f"write_bits={value:0{bit_count}b} ({bit_count} bits)")
        for i in reversed(range(bit_count)):
            self.bits.append((value >> i) & 1)

    def write_utf_string(self, text):
        if text is None:
            text = ""
        data = text.encode("utf-8")
        length = len(data)
        self._append_bits((length >> 8) & 0xFF, 8)
        self._append_bits(length & 0xFF, 8)
        if self.debug:
            self.debug_log.append(f"write_string={text}, length={length}")
        for b in data:
            self._append_bits(b, 8)

    def write_method_26(self, val: str):
        """
        Write a UTF-8 encoded string with a 16-bit length prefix, capped at 65535.
        - val: String to write (None or empty string treated as empty).
        """
        if val is None:
            val = ""
        encoded = val.encode('utf-8')
        length = min(len(encoded), 65535)
        self._append_bits(length, 16)
        for byte in encoded[:length]:
            self._append_bits(byte, 8)
        if self.debug:
            self.debug_log.append(f"method_26={val}, length={length}")


    def write_method_4(self, val: int):
        bits_needed = val.bit_length() if val > 0 else 1
        bits_to_use = max(2, (bits_needed + 1) & ~1)
        prefix = (bits_to_use // 2) - 1
        assert 0 <= prefix <= 15, f"Value too large for method_4: {val}"
        self._append_bits(prefix, 4)
        self._append_bits(val, bits_to_use)
        if self.debug:
            self.debug_log.append(f"method_4={val}, prefix={prefix}, bits={bits_to_use}")

    def write_method_45(self, val):  # If this is a float
        b = struct.pack(">f", float(val))
        for byte in b:
            self._append_bits(byte, 8)

    def write_method_739(self, value: int):
        if value < 0:
            self._append_bits(1, 1)
            self.write_method_91(-value)
        else:
            self._append_bits(0, 1)
            self.write_method_91(value)
        if self.debug:
            self.debug_log.append(f"method_739={value}")

    def write_method_393(self, val):
        self._append_bits(val & 0xFF, 8)

    def write_method_6(self, val: int, bit_count: int):
        self._append_bits(val, bit_count)
        if self.debug:
            self.debug_log.append(f"method_6={val}, bits={bit_count}")

    def write_bits(self, value, nbits):
        for i in reversed(range(nbits)):
            self._append_bits((value >> i) & 1, 1)

    def insert_bits(self, value, nbits):
        for i in reversed(range(nbits)):
            self._append_bits((value >> i) & 1, 1)
        if self.debug:
            self.debug_log.append(f"insert_bits={value:0{nbits}b} ({nbits} bits)")

    def write_uint48(self, value: int) -> None:
        if value < 0 or value > 0xFFFFFFFFFFFF:
            raise ValueError(f"Value {value} out of range for 48-bit integer")
        self._append_bits(value, 48)

    def to_bytes(self):
        while len(self.bits) % 8 != 0:
            self.bits.append(0)
            if self.debug:
                self.debug_log.append("pad_to_byte=0")
        out = bytearray()
        for i in range(0, len(self.bits), 8):
            byte = 0
            for bit in self.bits[i:i + 8]:
                byte = (byte << 1) | bit
            out.append(byte)
        return bytes(out)

    def write_method_9(self, val: int):
        bitlen = val.bit_length()
        if bitlen % 2:
            bitlen += 1
        prefix = (bitlen // 2) - 1
        self._append_bits(prefix, 4)
        self._append_bits(val, bitlen)

    def write_int24(self, val: int):
        self._append_bits(1 if val < 0 else 0, 1)
        self.write_method_9(abs(val))

    def write_method_91(self, val: int):
        bits_needed = val.bit_length() if val > 0 else 1
        bits_to_use = max(2, (bits_needed + 1) & ~1)
        n = (bits_to_use // 2) - 1
        self._append_bits(n, 3)
        self._append_bits(val, bits_to_use)
        if self.debug:
            self.debug_log.append(f"method_91={val}, n={n}, bits={bits_to_use}")

    def write_method_13(self, val: str):
        encoded = val.encode('utf-8')
        length = min(len(encoded), 65535)
        self._append_bits(length, 16)
        for byte in encoded[:length]:
            self._append_bits(byte, 8)
        if self.debug:
            self.debug_log.append(f"method_13={val}, length={length}")

    def write_signed_method_45(self, val: int):
        if val < 0:
            self._append_bits(1, 1)
            self.write_method_4(-val)
        else:
            self._append_bits(0, 1)
            self.write_method_4(val)
        if self.debug:
            self.debug_log.append(f"method_45={val}, sign={1 if val < 0 else 0}")

    def write_float(self, val: float):
        b = struct.pack(">f", val)
        for byte in b:
            self._append_bits(byte, 8)

    def get_debug_log(self):
        return self.debug_log if self.debug else []
