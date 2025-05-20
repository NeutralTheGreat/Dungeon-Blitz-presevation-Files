# BitUtils.py

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
