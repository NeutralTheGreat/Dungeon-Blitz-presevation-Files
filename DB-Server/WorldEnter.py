# WorldEnter.py

from BitUtils import BitBuffer
import struct
import time
import struct
from constants import (
    GS_BITS,
    MAX_CHAR_LEVEL_BITS,
    GAME_CONST_209,
    CLASS_118_CONST_43,
    CLASS_118_CONST_127,
    master_bits_for_slot,
    _MASTERCLASS_TO_ID,
    Game_const_646,
    class_10_const_83,
    GearType,
    class_21_const_763,
    class_66_const_409,
    class_16_const_167,
    ENT_MAX_SLOTS,
    NEWS_EVENTS
)

def Player_Data_Packet(char: dict,
                       event_index: int = 2,
                       transfer_token: int = 1) -> bytes:

    buf = BitBuffer()

    # ────────────── (1) Preamble ──────────────
    buf.write_method_4(transfer_token)                   # _loc2_
    current_game_time = int(time.time())
    buf.write_method_4(current_game_time)                # _loc3_
    buf.write_method_6(0, GS_BITS)                       # _loc4_
    buf.write_method_4(0)                                # _loc5_

    # ────────────── (2) Customization ──────────────
    buf.write_utf_string(char.get("name", "") or "")
    buf._append_bits(1, 1)  # hasCustomization
    buf.write_utf_string(char.get("class", "") or "")
    buf.write_utf_string(char.get("gender", "") or "")
    buf.write_utf_string(char.get("headSet", "") or "")
    buf.write_utf_string(char.get("hairSet", "") or "")
    buf.write_utf_string(char.get("mouthSet", "") or "")
    buf.write_utf_string(char.get("faceSet", "") or "")
    buf._append_bits(char.get("hairColor", 0), 24)
    buf._append_bits(char.get("skinColor", 0), 24)
    buf._append_bits(char.get("shirtColor", 0), 24)
    buf._append_bits(char.get("pantColor", 0), 24)

    # ────────────── (3) Gear slots ──────────────
    # Each slot is [GearID, Rune1, Rune2, Rune3, Color1, Color2]
    gear_list = char.get("gearList", [[0] * 6] * 6)
    for slot in gear_list:
        gear_id, rune1, rune2, rune3, color1, color2 = slot

        if gear_id:
            # presence bit
            buf._append_bits(1, 1)
            # Gear ID (11 bits)
            buf._append_bits(gear_id, 11)
            # (reserved / flags)
            buf._append_bits(0, 2)
            # Runes (3 × 16 bits each)
            buf._append_bits(rune1, 16)
            buf._append_bits(rune2, 16)
            buf._append_bits(rune3, 16)
            # Colors (2 × 8 bits each)
            buf._append_bits(color1, 8)
            buf._append_bits(color2, 8)
        else:
            # no item in this slot
            buf._append_bits(0, 1)

    # ────────────── (4) Numeric fields ──────────────
    char_level = char.get("level", 1) or 1
    buf.write_method_6(char_level, MAX_CHAR_LEVEL_BITS)
    buf.write_method_4(char.get("xp",  0))  # xp
    buf.write_method_4(char.get("gold",  0))  # gold
    buf.write_method_4(char.get("Gems",  0))  # (Gems or something else im not sure what this is)
    buf.write_method_4(char.get("DragonOre",  0))  # something else
    buf.write_method_4(char.get("mammothIdols",  0)) # mammoth idols
    buf._append_bits(int(char.get("showHigher", True)), 1)

    # ────────────── (5) Quest-tracker ──────────────
    quest_val = char.get("questTrackerState", None)
    if quest_val is not None:
        buf._append_bits(1, 1)
        buf.write_method_4(quest_val)
    else:
        buf._append_bits(0, 1)

    # ────────────── (6) Position‐presence ──────────────
    buf._append_bits(0, 1)  # no door/teleport update

    # ────────────── (7) Extended‐data‐presence ──────────────
    buf._append_bits(1, 1)  # yes, we’re sending the big block

    # ────────────── (8) stub out the entire “if (_loc32_)” block ──────────────
    buf.write_method_6(0, GearType.GEARTYPE_BITSTOSEND)  # gear-to-send = 0
    buf.write_method_6(0, GearType.const_348)           # gear-sets = 0
    buf._append_bits(0, 1)                             # no keybinds
    buf.write_method_4(0)                              # mounts = 0
    buf.write_method_4(0)                              # pets = 0
    buf._append_bits(0, 1)                             # no charms
    buf._append_bits(0, 1)                             # no materials
    buf._append_bits(0, 1)                             # no lockboxes
    buf.write_method_4(char.get("DragonKeys",  0))                              # lockboxKeys
    buf.write_method_4(char.get("SilverSigils",  0))                             # royalSigils
    buf.write_method_6(1, Game_const_646)              # alert state = 0
    for _ in range(1, class_21_const_763 + 1):         # dyes
        buf._append_bits(1, 1)
    buf._append_bits(0, 1)                             # no consumables
    buf.write_method_4(0)                              # missions = 0
    buf.write_method_4(0)                              # friends = 0
    buf.write_method_6(0, class_10_const_83)           # learned abilities = 0
    buf.write_method_6(0, class_10_const_83)           # active slot 1
    buf.write_method_6(0, class_10_const_83)           # active slot 2
    buf.write_method_6(0, class_10_const_83)           # active slot 3
    buf.write_method_4(0)                              # craft talent
    buf.write_method_6(0, class_66_const_409)          # tower A
    buf.write_method_6(0, class_66_const_409)          # tower B
    buf.write_method_6(0, class_66_const_409)          # tower C
    buf._append_bits(0, 1)                             # no magic forge
    buf._append_bits(0, 1)                             # no ability research
    buf._append_bits(0, 1)                             # no building info
    buf._append_bits(0, 1)                             # no tower research
    buf._append_bits(0, 1)                             # no egg/pet data
    buf.write_method_6(0, class_16_const_167)          # pet count = 0
    # no resting-pet loops…
    buf._append_bits(0, 1)
    buf._append_bits(0, 1)
    buf._append_bits(0, 1)
    buf._append_bits(0, 1)
    # NEWS (4 empty strings + zero timestamp)
    for _ in range(4):
        buf.write_utf_string("")
    buf.write_method_4(0)




            # ────────────── final packet assembly ──────────────
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


    payload = buf.to_bytes()
    return struct.pack(">HH", 0x21, len(payload)) + payload


