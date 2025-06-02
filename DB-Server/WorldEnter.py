# WorldEnter.py

from BitUtils import BitBuffer
import struct

GS_BITS = 2             # Game.const_813
MAX_CHAR_LEVEL_BITS = 6 # Entity.MAX_CHAR_LEVEL_BITS


def Player_Data_Packet(char: dict, transfer_token: int = 1) -> bytes:
    """
    Build the 0x10 “WELCOME” packet exactly how the Flash client’s method_1379 (and method_870) expects.
    """

    buf = BitBuffer()

    # ----------------------------------------------------------------------------
    # 1) Preamble (four writes)
    buf.write_method_4(transfer_token)      # 32 bits: transfer_token
    buf.write_method_4(0)                   # 32 bits: zero
    buf.write_method_6(0, GS_BITS)          # 2 bits: zero
    buf.write_method_4(0)                   # 32 bits: zero

    # ----------------------------------------------------------------------------
    # 2) Paper‐doll “has customization” + six UTFs
    buf.write_utf_string(char["name"])
    buf._append_bits(1, 1)                  # 1 bit: “has customization” = 1
    buf.write_utf_string(char["class"])
    buf.write_utf_string(char["gender"])
    buf.write_utf_string(char["headSet"])
    buf.write_utf_string(char["hairSet"])
    buf.write_utf_string(char["mouthSet"])
    buf.write_utf_string(char["faceSet"])

    # ----------------------------------------------------------------------------
    # 3) Four 24‐bit color reads
    buf._append_bits(char.get("hairColor", 0), 24)
    buf._append_bits(char.get("skinColor", 0), 24)
    buf._append_bits(char.get("shirtColor", 0), 24)
    buf._append_bits(char.get("pantColor", 0), 24)

    # ----------------------------------------------------------------------------
    # 4) Six gear‐slot entries, each with 1 "presence" bit.
    #    For i=0..5 (slots 1 through 6):
    #      - Write 1 bit: “slot present?” (1 if gear_id != 0, else 0)
    #      - If present:
    #          * 11 bits  → gearID
    #          *  2 bits  → const_176 (send 0)
    #          * 16 bits  → class_64.const_101 (send 0)
    #          * 16 bits  → class_64.const_101 (send 0)
    #          * 16 bits  → class_64.const_101 (send 0)
    #          *  8 bits  → class_21.const_50 (send 0)
    #          *  8 bits  → class_21.const_50 (send 0)
    #
    #    If absent (gear_id == 0), write exactly 1 bit = 0 and move to next slot.

    gear_list = char.get("gearList", [0] * 6)

    for i in range(6):
        gear_id = gear_list[i] if i < len(gear_list) else 0
        if gear_id:
            buf._append_bits(1, 1)  # 1-bit “present”
            buf._append_bits(gear_id, 11)  # 11-bit “gearID”
            buf._append_bits(0, 2)  # 2-bit “const_176”
            buf._append_bits(0, 16)  # 16-bit “class_64.const_101”
            buf._append_bits(0, 16)  # 16-bit “class_64.const_101”
            buf._append_bits(0, 16)  # 16-bit “class_64.const_101”
            buf._append_bits(1114378, 8)  # 8-bit “class_21.const_50”
            buf._append_bits(1114378, 8)  # 8-bit “class_21.const_50”
        else:
            buf._append_bits(0, 1)  # 1-bit “absent”

    # ----------------------------------------------------------------------------
    # 5) ALIGN before numeric fields
    buf.align_to_byte()
    buf.write_method_6(char.get("level", 1), MAX_CHAR_LEVEL_BITS)  # 6 bits: level
    buf.write_method_4(char.get("currGold", 0))  # 32 bits: currGold
    buf.write_method_4(char.get("currGems", 0))  # 32 bits: currGems
    buf.write_method_4(char.get("bonusLevels", 0))  # 32 bits: bonusLevels
    buf.write_method_4(char.get("mammothIdols", 0))  # 32 bits: mammothIdols
    buf.write_method_4(char.get("extraField", 0))  # 32 bits: extraField

    # ----------------------------------------------------------------------------
    # 6) Numeric fields (exact order; no missing bits!):
    #    a) 6‐bit “level”

    # ----------------------------------------------------------------------------
    # Build final bytes and prepend two‐byte type (0x10) + two‐byte length
    payload = buf.to_bytes()
    return struct.pack(">HH", 0x10, len(payload)) + payload
















transfer_token = 1
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

