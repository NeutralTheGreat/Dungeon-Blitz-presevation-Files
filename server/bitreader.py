import struct

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

    def read_bit(self) -> int:
        return self.read_bits(1)

    def remaining_bits(self) -> int:
        total_bits = len(self.data) * 8
        return max(0, total_bits - self.bit_index)

    def read_signed_bits(self, count: int) -> int:
        val = self.read_bits(count)
        sign_bit = 1 << (count - 1)
        return (val ^ sign_bit) - sign_bit

    def align_to_byte(self):
        remainder = self.bit_index % 8
        if remainder:
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

    def read_float(self) -> float:
        """
        Read a 32-bit IEEE 754 float (4 bytes), assuming byte alignment.
        """
        self.align_to_byte()  # Ensure we're at a byte boundary
        if self.bit_index + 32 > len(self.data) * 8:
            raise ValueError("Not enough data to read float")
        byte_index = self.bit_index // 8
        float_bytes = self.data[byte_index:byte_index + 4]
        self.bit_index += 32
        return struct.unpack('>f', float_bytes)[0]

    def read_method_4(self) -> int:
        n = self.read_bits(4)
        n = (n + 1) << 1
        return self.read_bits(n)

    def read_method_393(self) -> int:
        return self.read_bits(8)

    def read_method_6(self, bit_count: int) -> int:
        return self.read_bits(bit_count)

    def read_method_9(self) -> int:
        prefix = self.read_bits(4)
        n_bits = (prefix + 1) * 2
        raw = self.read_bits(n_bits)
        return raw

    def read_int24(self) -> int:
        sign = self.read_bits(1)
        mag = self.read_method_9()
        return -mag if sign else mag

    def read_unsigned_int64(self) -> int:
        """
        Reads an unsigned 64-bit integer encoded as in Flash `ReceiveUnsignedInt64`:
        - 5-bit prefix L
        - if L <= 32: read L bits as low, high=0
        - else: read (L-32) bits as high, then 32 bits as low
        Returns as Python int (high << 32 | low)
        """
        # read 5-bit length prefix
        L = self.read_bits(5)
        # compute total bits count: (L + 1) << 1, then interpret that as bit-length
        bit_length = (L + 1) << 1
        if bit_length <= 32:
            low = self.read_bits(bit_length)
            high = 0
        else:
            high_bits = bit_length - 32
            high = self.read_bits(high_bits)
            low = self.read_bits(32)
        return (high << 32) | low

