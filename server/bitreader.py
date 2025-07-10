import struct
from typing import List

class BitReader:
    def __init__(self, data: bytes, debug: bool = False):
        self.data = data
        self.bit_index = 0
        self.debug = debug
        self.debug_log: List[str] = [] if debug else []

    def read_bit(self) -> int:
        byte_index = self.bit_index // 8
        bit_offset = 7 - (self.bit_index % 8)
        if byte_index >= len(self.data):
            raise ValueError("Not enough data to read bit")
        bit = (self.data[byte_index] >> bit_offset) & 1
        self.bit_index += 1
        if self.debug:
            self.debug_log.append(f"read_bit={bit} at bit_index={self.bit_index-1}")
        return bit

    def read_bits(self, count: int) -> int:
        if self.bit_index + count > len(self.data) * 8:
            raise ValueError(f"Not enough data to read {count} bits")
        result = 0
        for _ in range(count):
            result = (result << 1) | self.read_bit()
        if self.debug:
            self.debug_log.append(f"read_bits={result:0{count}b} ({count} bits)")
        return result

    def remaining_bits(self) -> int:
        total_bits = len(self.data) * 8
        return max(0, total_bits - self.bit_index)

    def align_to_byte(self):
        remainder = self.bit_index % 8
        if remainder:
            skip_bits = 8 - remainder
            for _ in range(skip_bits):
                self.read_bit()
            if self.debug:
                self.debug_log.append(f"align_to_byte=skipped {skip_bits} bits")

    def read_string(self) -> str:
        self.align_to_byte()
        length = self.read_bits(16)
        if self.bit_index + length * 8 > len(self.data) * 8:
            raise ValueError("Not enough data to read string")
        result_bytes = bytearray()
        for _ in range(length):
            result_bytes.append(self.read_bits(8))
        if self.debug:
            self.debug_log.append(f"read_string={result_bytes.decode('utf-8', errors='replace')}, length={length}")
        try:
            return result_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return result_bytes.decode('latin1')

    def read_float(self) -> float:
        self.align_to_byte()
        if self.bit_index + 32 > len(self.data) * 8:
            raise ValueError("Not enough data to read float")
        byte_index = self.bit_index // 8
        float_bytes = self.data[byte_index:byte_index + 4]
        self.bit_index += 32
        result = struct.unpack('>f', float_bytes)[0]
        if self.debug:
            self.debug_log.append(f"read_float={result}")
        return result

    def read_method_4(self) -> int:
        prefix = self.read_bits(4)
        bits_to_use = (prefix + 1) * 2
        if self.bit_index + bits_to_use > len(self.data) * 8:
            raise ValueError(f"Not enough data to read {bits_to_use} bits for method_4")
        value = self.read_bits(bits_to_use)
        if self.debug:
            self.debug_log.append(f"read_method_4={value}, prefix={prefix}, bits={bits_to_use}")
        return value

    def read_method_6(self, bit_count: int) -> int:
        if self.bit_index + bit_count > len(self.data) * 8:
            raise ValueError(f"Not enough data to read {bit_count} bits for method_6")
        value = self.read_bits(bit_count)
        if self.debug:
            self.debug_log.append(f"read_method_6={value}, bits={bit_count}")
        return value

    def read_method_9(self) -> int:
        prefix = self.read_bits(4)
        n_bits = (prefix + 1) * 2
        if self.bit_index + n_bits > len(self.data) * 8:
            raise ValueError(f"Not enough data to read {n_bits} bits for method_9")
        value = self.read_bits(n_bits)
        if self.debug:
            self.debug_log.append(f"read_method_9={value}, prefix={prefix}, bits={n_bits}")
        return value

    def read_int24(self) -> int:
        sign = self.read_bit()
        magnitude = self.read_method_9()
        value = -magnitude if sign else magnitude
        if self.debug:
            self.debug_log.append(f"read_int24={value}, sign={sign}")
        return value

    def read_method_45(self) -> int:
        # Removed align_to_byte() to match ActionScript method_45
        sign = self.read_bit()
        if self.bit_index + 4 > len(self.data) * 8:  # Need at least 4 bits for prefix
            raise ValueError("Not enough data to read method_4 prefix for method_45")
        magnitude = self.read_method_4()
        value = -magnitude if sign else magnitude
        if self.debug:
            self.debug_log.append(f"read_method_45={value}, sign={sign}, magnitude={magnitude}")
        return value

    def read_method_393(self) -> int:
        value = self.read_bits(8)
        if self.debug:
            self.debug_log.append(f"read_method_393={value}")
        return value

    def read_unsigned_int64(self) -> int:
        L = self.read_bits(5)
        bit_length = (L + 1) << 1
        if self.bit_index + bit_length > len(self.data) * 8:
            raise ValueError(f"Not enough data to read {bit_length} bits for unsigned_int64")
        if bit_length <= 32:
            low = self.read_bits(bit_length)
            high = 0
        else:
            high_bits = bit_length - 32
            high = self.read_bits(high_bits)
            low = self.read_bits(32)
        value = (high << 32) | low
        if self.debug:
            self.debug_log.append(f"read_unsigned_int64={value}, L={L}, bits={bit_length}")
        return value

    def read_int16(self) -> int:
        value = self.read_signed_bits(16)
        if self.debug:
            self.debug_log.append(f"read_int16={value}")
        return value

    def read_uint32(self) -> int:
        value = self.read_bits(32)
        if self.debug:
            self.debug_log.append(f"read_uint32={value}")
        return value

    def read_signed_bits(self, count: int) -> int:
        if self.bit_index + count > len(self.data) * 8:
            raise ValueError(f"Not enough data to read {count} bits for signed_bits")
        val = self.read_bits(count)
        sign_bit = 1 << (count - 1)
        value = (val ^ sign_bit) - sign_bit
        if self.debug:
            self.debug_log.append(f"read_signed_bits={value}, count={count}")
        return value

    # Add this method to the BitReader class
    def read_method_13(self) -> str:
        length = self.read_bits(16)
        if self.bit_index + length * 8 > len(self.data) * 8:
            raise ValueError("Not enough data to read string")
        result_bytes = bytearray()
        for _ in range(length):
            result_bytes.append(self.read_bits(8))
        try:
            return result_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return result_bytes.decode('latin1')



    def get_debug_log(self) -> List[str]:
        return self.debug_log