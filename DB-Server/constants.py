# constants.py

# ─── Game packet bit-widths ───
GAME_CONST_209 = 4   # number of bits used for the master-class ID

# ─── “Master-class talent tree” constants ───
CLASS_118_CONST_43 = 27
CLASS_118_CONST_529 = [5,2,3,5,5,3,2,3,2,5,2,3,5,5,3,2,3,2,5,2,3,5,5,3,2,3,2]
CLASS_118_CONST_127 = 6

def master_bits_for_slot(slot_index: int) -> int:
    """
    Exactly the same logic as class_118.method_277:
      raw_max = CLASS_118_CONST_529[slot_index]
      if raw_max <= 2: bits = 1
      if raw_max <= 4: bits = 2
      if raw_max <= 5: bits = 3
    """
    raw_max = CLASS_118_CONST_529[slot_index]
    bits = 0
    if raw_max <= 2:
        bits = 1
    if raw_max <= 4:
        bits = 2
    if raw_max <= 5:
        bits = 3
    return bits


ENT_MAX_SLOTS = 7
GS_BITS = 2             # Game.const_813
MAX_CHAR_LEVEL_BITS = 6 # Entity.MAX_CHAR_LEVEL_BITS

# (1) Bit-width for master-class ID
Game_const_209     = 4

# (2) Bit-width for “alert state”
Game_const_646     = 4

EntType_MAX_SLOTS = 7

# (3) Maximum dye index (so we write exactly that many 1-bit flags)
class_21_const_763 = 250

# (4) Bit-width for ability IDs/ranks
class_10_const_83  = 7

# (5) Bit-width for master-class tower data
class_66_const_409 = 6

# (6) Bit-width for pet-ID in egg/pet loops
class_16_const_167 = 6

class class_118:
    const_43 = 27

class GearType:
    GEARTYPE_BITSTOSEND = 11   # (for example—use whatever the AS3 says)
    const_348          = 3   # (for example)
    const_176          = 2   # (for example)

quest_val = None      # or char.get("dungeonProgress", None)

_MASTERCLASS_TO_ID = {
    "frostwarden":   7,
    "flameseer":     8,
    "necromancer":   9,
    "sentinel":      4,
    "justicar":      5,
    "templar":       6,
    "executioner":   1,
    "shadowwalker":  2,
    "soulthief":     3,
}

NEWS_EVENTS = {
    1: [
        "a_NewsGoldIcon",
        "Double Gold Event",
        "While this event is in place all gold will be doubled world wide",
        "http://www.dungeonblitz.com/",
        1387602000,
    ],
    2: [
        "a_NewsGearIcon",
        "Double Gear Event",
        "While this event is in place all gear drops will be doubled world wide",
        "http://www.dungeonblitz.com/",
        1387602000,
    ],
    3: [
        "a_NewsMatsIcon",
        "Double Material Event",
        "While this event is in place all material drops will be doubled world wide",
        "http://www.dungeonblitz.com/",
        1387602000,
    ],
    4: [
        "a_NewsXPIcon",
        "Double XP Event",
        "While this event is in place all XP gained will be doubled world wide",
        "http://www.dungeonblitz.com/",
        1387602000,
    ],
    5: [
        "a_NewsPetXPIcon",
        "Double Pet XP Event",
        "While this event is in place all pet XP gained will be doubled world wide",
        "http://www.dungeonblitz.com/",
        1387602000,
    ],
}