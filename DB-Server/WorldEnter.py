from BitUtils import  BitBuffer
import struct

transfer_token = 1

class EntType:
    MAX_SLOTS = 6    # slots 1–6 inclusive

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

#TODO.....
     #WELCOME packet
##############################################################

def build_welcome_packet(char, transfer_token=1):
    GS_BITS         = 2    # Game.const_813
    LVL_BITS        = 6    # Entity.MAX_CHAR_LEVEL_BITS
    METHOD4_BITS    = None # write_method_4() is its own variable‐length encoding
    GEAR_COUNT_BITS = 6    # GearType.GEARTYPE_BITSTOSEND
    GEAR_ID_BITS    = 11
    GEAR_TYPE_BITS  = 11
    COORD_BITS      = 16   # coords from method_45()

    buf = BitBuffer()

    # 1) preamble
    buf.write_method_4(transfer_token)  # _loc2_
    buf.write_method_4(0)               # _loc3_
    buf.write_method_6(0, GS_BITS)      # _loc4_
    buf.write_method_4(0)               # _loc5_

    # 2) name + customization
    buf.write_utf_string(char["name"])  # _loc6_
    buf._append_bits(1,1)               # hasCustomization
    for k in ("class","gender","headSet","hairSet","faceSet","mouthSet"):
        buf.write_utf_string(char[k])
    for c in ("hairColor","skinColor","shirtColor","pantColor"):
        buf._append_bits(char[c],24)

    # 3) level + five method_4() placeholders
    buf.write_method_6(char.get("level",1), LVL_BITS)  # _loc8_
    for _ in range(5):
        buf.write_method_4(0)                         # _loc9_–_loc13_

    # 4) door/position flag and optional coords
    buf._append_bits(0,1)      # _loc14_ = false (no door)
    # if it were true, you'd do:
    #    buf._append_bits(x_coord, COORD_BITS)
    #    buf._append_bits(y_coord, COORD_BITS)

    # 5) hasExtended flag
    buf._append_bits(1,1)      # _loc32_ = true

    # 6) gear
    # … after buf._append_bits(1,1) for hasExtended …

    gear = char["gearList"]
    buf.write_method_6(len(gear), 6)  # gear count is 6 bits
    for gid in gear:
        buf._append_bits(1, 1)  # hasGear flag
        buf._append_bits(gid, 11)  # **gear ID is 11 bits**
        buf._append_bits(0, 6)  # gearType (stubbed here, 6 bits)
        # now the rune‐block:
        buf._append_bits(0, 1)  # hasStatRune?
        buf._append_bits(0, 1)  # hasProcRune?
        buf._append_bits(0, 1)  # hasMagicRune?
        buf._append_bits(0, 8)  # runeColor1
        buf._append_bits(0, 8)  # runeColor2

    # for the empty slots:
    for _ in range(len(gear) + 1, EntType.MAX_SLOTS):
        buf._append_bits(0, 1)  # hasGear = false

    # 7) stub out all the “while(method_11())” loops:
    buf.write_method_4(0)  # gearsetCount
    buf.write_method_4(0)  # mountCount
    buf.write_method_4(0)  # petCount
    buf._append_bits(0,1)  # charms
    buf._append_bits(0,1)  # materials
    buf._append_bits(0,1)  # lockboxes
    buf.write_method_4(0)  # lockboxKeys
    buf.write_method_4(0)  # royalSigils
    buf.write_method_6(0,4)# alertState
    buf.write_method_393(250)
    for _ in range(250):
        buf._append_bits(0,1)
    buf._append_bits(0,1)  # consumables
    buf.write_method_4(0)  # missions
    buf.write_method_4(0)  # friends
    buf.write_method_6(0,6)# ability count
    for _ in range(3):
        buf.write_method_6(0,6)  # master‐class ranks
    buf.write_method_6(6,4)     # master class = Sentinel
    buf._append_bits(0,1)       # no master‐tower
    for _ in range(4):
        buf.write_utf_string("")
    buf.write_method_4(0)       # news count

    # 8) finalize
    buf.align_to_byte()
    payload = buf.to_bytes()
    return struct.pack(">HH", 0x10, len(payload)) + payload