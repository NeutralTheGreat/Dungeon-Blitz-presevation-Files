#BitUtils.py
class BitBuffer:
    def __init__(self):
        self.bits = []

    def align_to_byte(self):
        while len(self.bits) % 8 != 0:
            self.bits.append(0)

    def _append_bits(self, value, bit_count):
        for i in reversed(range(bit_count)):
            self.bits.append((value >> i) & 1)

    def write_utf_string(self, text):
        if text is None:
            text = ""
        data = text.encode("utf-8")
        length = len(data)
        self._append_bits((length >> 8) & 0xFF, 8)
        self._append_bits(length & 0xFF, 8)
        for b in data:
            self._append_bits(b, 8)

    def write_method_4(self, val):
        if val == 0:
            self._append_bits(0, 4)
            self._append_bits(0, 2)
            return
        n = val.bit_length()
        if n % 2 != 0:
            n += 1
        self._append_bits((n >> 1) - 1, 4)
        self._append_bits(val, n)

    def write_method_393(self, val):
        self._append_bits(val & 0xFF, 8)

    def write_method_6(self, val, bit_count):
        self._append_bits(val, bit_count)

    def write_bits(self, value, nbits):
        for i in reversed(range(nbits)):
            self._append_bits((value >> i) & 1, 1)

    def write_uint48(self, value: int) -> None:
        """Write a 48-bit unsigned integer."""
        if value < 0 or value > 0xFFFFFFFFFFFF:
            raise ValueError(f"Value {value} out of range for 48-bit integer")
        self._append_bits(value, 48)

    def to_bytes(self):
        while len(self.bits) % 8 != 0:
            self.bits.append(0)
        out = bytearray()
        for i in range(0, len(self.bits), 8):
            byte = 0
            for bit in self.bits[i:i + 8]:
                byte = (byte << 1) | bit
            out.append(byte)
        return bytes(out)

    def write_method_9(self, val: int):
        # 1) compute how many bits we need
        bitlen = val.bit_length()
        # round up to next even number
        if bitlen % 2:
            bitlen += 1
        # unary prefix = (bitlen / 2) − 1
        prefix = (bitlen // 2) - 1

        # 2) write 4-bit prefix
        self._append_bits(prefix, 4)
        # 3) write the value in exactly bitlen bits
        self._append_bits(val, bitlen)


    def write_int24(self, val: int):
        # 1) sign‐bit
        self._append_bits(1 if val < 0 else 0, 1)
        # 2) absolute using method_9
        self.write_method_9(abs(val))

    def write_method_91(self, val: int):
        # Determine the smallest n where val < 2^(2*(n+1))
        n = 0
        while (1 << (2 * (n + 1))) <= val:
            n += 1
        # Write n (3 bits)
        self.write_method_6(n, 3)
        # Write val in (2*(n+1)) bits
        bitlen = 2 * (n + 1)
        self.write_method_6(val, bitlen)