# constants.py
import time
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

ENTITY_CONST_244    = 2
Entity_const_172 = 3

CLASS_NAME_TO_ID = {
    "Paladin": 0,
    "Rogue":   1,
    "Mage":    2,
}
stringPairs1 = [("Reputation","Friendly"), ("DailyQuest","Complete")]  # etc.
stringTriples = [(101, "Title1","Desc1"), (102,"Title2","Desc2")]

class_9_const_28 = 5
class_1_const_254 = 7
class_64_const_499 = 2
class_64_const_218 = 5
class_111_const_432 = 9



class_10_const_665 = 4
ENT_MAX_SLOTS = 7
GS_BITS = 2             # Game.const_813
MAX_CHAR_LEVEL_BITS = 6 # Entity.MAX_CHAR_LEVEL_BITS

# (1) Bit-width for master-class ID
Game_const_209     = 4

# (2) Bit-width for “alert state”
Game_const_646     = 4

EntType_MAX_SLOTS = 7



class LockboxType:
    ID_BITS = 8

class EntType:
    MAX_SLOTS = 7

class DyeType:
    BITS = 8

class Mission:
    const_72 = 2
    const_58 = 1


const_228 = 4


class MissionDef:
    def __init__(self, var_1775: bool, var_908: int, var_134: bool):
        # client fields:
        #   var_1775: one‐shot mission?
        #   var_908:   maximum progress count
        #   var_134:   timed mission?
        self.var_1775 = var_1775
        self.var_908   = var_908
        self.var_134   = var_134

# Index 0 is unused, so we put a dummy placeholder
var_238 = [
    None,
    MissionDef(var_1775=False, var_908=10, var_134=False),  # mission ID 1
    MissionDef(var_1775=True,  var_908=1,  var_134=False),  # mission ID 2
    MissionDef(var_1775=False, var_908=5,  var_134=True ),  # mission ID 3
    # …and so on for all mission IDs…
]

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

class class_64:
    const_101 = 16


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
    1: {
        "icon": "a_NewsGoldIcon",
        "title": "Double Gold Event",
        "description": "While this event is in place all gold will be doubled world wide",
        "url": "http://www.dungeonblitz.com/",
        "end_time": int(time.time()) + 7 * 24 * 3600  # 7 days from now
    },
    2: {
        "icon": "a_NewsGearIcon",
        "title": "Double Gear Event",
        "description": "While this event is in place all gear drops will be doubled world wide",
        "url": "http://www.dungeonblitz.com/",
        "end_time": int(time.time()) + 7 * 24 * 3600
    },
    3: {
        "icon": "a_NewsMatsIcon",
        "title": "Double Material Event",
        "description": "While this event is in place all material drops will be doubled world wide",
        "url": "http://www.dungeonblitz.com/",
        "end_time": int(time.time()) + 7 * 24 * 3600
    },
    4: {
        "icon": "a_NewsXPIcon",
        "title": "Double XP Event",
        "description": "While this event is in place all XP gained will be doubled world wide",
        "url": "http://www.dungeonblitz.com/",
        "end_time": int(time.time()) + 7 * 24 * 3600
    },
    5: {
        "icon": "a_NewsPetXPIcon",
        "title": "Double Pet XP Event",
        "description": "While this event is in place all pet XP gained will be doubled world wide",
        "url": "http://www.dungeonblitz.com/",
        "end_time": int(time.time()) + 7 * 24 * 3600
    }
}

# ──────────────── Starting inventory by class ────────────────
inventory_gears = {
    "paladin": [
        {
            "gearID": 1,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 2,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 3,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 4,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 5,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 6,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 7,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 8,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 9,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 10,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 11,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 12,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 13,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 14,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 15,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 16,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 17,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 18,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 19,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 20,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 21,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 22,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 23,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 24,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 25,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 26,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 79,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 80,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 81,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 82,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 83,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 84,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 85,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 86,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 87,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 88,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 89,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 90,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 91,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 92,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 93,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 94,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 95,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 96,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 97,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 98,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 99,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 100,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 101,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 102,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 103,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 104,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 105,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 106,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 107,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 108,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 169,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 170,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 171,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 172,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 173,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 174,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 175,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 176,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 177,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 178,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 179,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 180,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 181,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 182,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 183,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 184,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 185,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 186,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 187,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 188,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 189,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 190,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 191,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 192,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 193,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 194,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 195,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 196,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 197,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 198,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 259,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 260,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 261,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 262,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 263,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 264,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 265,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 266,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 267,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 268,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 269,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 270,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 271,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 272,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 273,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 274,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 275,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 276,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 277,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 278,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 279,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 280,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 281,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 282,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 283,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 284,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 285,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 286,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 287,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 288,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 349,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 350,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 351,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 352,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 353,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 354,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 355,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 356,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 357,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 358,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 359,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 360,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 361,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 362,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 363,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 364,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 365,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 366,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 367,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 368,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 369,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 370,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 371,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 372,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 373,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 374,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 375,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 376,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 377,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 378,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 439,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 440,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 441,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 442,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 443,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 444,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 445,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 446,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 447,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 448,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 449,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 450,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 451,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 452,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 453,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 454,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 455,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 456,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 457,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 458,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 459,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 460,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 461,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 462,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 463,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 464,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 465,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 466,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 467,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 468,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 529,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 530,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 531,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 532,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 533,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 534,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 535,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 536,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 537,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 538,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 539,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 540,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 541,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 542,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 543,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 544,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 545,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 546,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 547,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 548,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 549,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 550,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 551,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 552,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 553,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 554,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 555,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 556,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 557,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 558,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 619,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 620,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 621,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 622,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 623,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 624,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 625,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 626,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 627,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 628,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 629,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 630,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 631,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 632,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 633,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 634,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 635,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 636,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 637,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 638,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 639,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 640,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 641,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 642,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 643,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 644,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 645,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 646,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 647,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 648,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 709,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 710,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 711,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 712,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 713,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 714,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 715,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 716,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 717,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 718,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 719,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 720,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 721,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 722,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 723,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 724,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 725,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 726,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 727,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 728,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 729,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 730,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 731,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 732,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 733,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 734,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 735,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 736,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 737,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 738,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 799,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 800,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 801,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 802,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 803,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 804,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 805,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 806,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 807,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 808,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 809,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 810,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 811,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 812,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 813,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 814,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 815,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 816,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 817,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 818,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 819,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 820,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 821,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 822,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 823,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 824,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 825,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 826,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 827,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 828,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 889,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 890,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 891,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 892,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 893,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 894,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 895,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 896,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 897,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 898,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 899,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 900,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 901,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 902,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 903,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 904,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 905,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 906,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 907,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 908,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 909,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 910,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 911,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 912,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 913,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 914,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 915,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 916,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 917,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 918,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 979,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 980,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 981,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 982,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 983,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 984,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 985,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 986,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 987,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 988,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 989,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 990,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 991,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 992,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 993,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 994,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 995,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 996,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 997,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 998,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 999,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1000,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1001,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1002,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1003,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1004,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1005,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1006,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1007,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1008,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1069,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1070,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1071,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1072,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1073,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1074,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1075,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1076,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1077,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1078,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1079,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1080,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1081,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1082,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1083,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1084,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1085,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1086,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1087,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1088,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1089,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1090,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1091,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1092,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1093,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1094,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1095,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1096,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1097,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1098,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1159,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1162,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1177,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1178,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1179,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1180,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1181,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1182,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        }

    ],
    "rogue": [
        {
            "gearID": 27,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 28,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 29,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 30,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 31,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 32,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 33,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 34,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 35,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 36,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 37,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 38,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 39,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 40,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 41,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 42,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 43,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 44,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 45,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 46,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 47,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 48,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 49,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 50,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 51,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 52,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 109,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 110,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 111,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 112,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 113,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 114,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 115,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 116,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 117,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 118,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 119,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 120,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 121,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 122,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 123,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 124,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 125,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 126,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 127,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 128,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 129,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 130,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 131,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 132,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 133,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 134,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 135,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 136,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 137,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 138,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 199,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 200,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 201,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 202,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 203,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 204,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 205,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 206,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 207,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 208,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 209,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 210,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 211,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 212,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 213,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 214,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 215,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 216,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 217,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 218,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 219,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 220,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 221,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 222,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 223,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 224,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 225,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 226,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 227,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 228,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 289,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 290,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 291,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 292,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 293,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 294,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 295,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 296,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 297,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 298,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 299,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 300,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 301,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 302,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 303,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 304,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 305,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 306,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 307,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 308,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 309,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 310,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 311,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 312,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 313,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 314,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 315,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 316,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 317,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 318,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 379,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 380,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 381,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 382,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 383,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 384,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 385,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 386,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 387,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 388,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 389,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 390,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 391,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 392,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 393,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 394,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 395,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 396,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 397,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 398,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 399,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 400,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 401,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 402,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 403,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 404,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 405,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 406,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 407,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 408,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 469,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 470,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 471,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 472,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 473,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 474,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 475,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 476,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 477,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 478,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 479,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 480,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 481,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 482,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 483,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 484,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 485,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 486,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 487,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 488,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 489,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 490,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 491,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 492,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 493,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 494,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 495,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 496,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 497,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 498,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 559,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 560,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 561,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 562,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 563,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 564,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 565,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 566,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 567,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 568,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 569,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 570,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 571,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 572,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 573,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 574,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 575,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 576,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 577,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 578,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 579,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 580,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 581,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 582,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 583,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 584,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 585,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 586,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 587,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 588,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 649,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 650,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 651,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 652,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 653,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 654,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 655,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 656,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 657,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 658,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 659,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 660,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 661,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 662,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 663,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 664,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 665,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 666,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 667,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 668,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 669,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 670,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 671,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 672,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 673,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 674,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 675,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 676,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 677,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 678,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 739,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 740,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 741,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 742,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 743,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 744,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 745,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 746,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 747,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 748,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 749,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 750,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 751,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 752,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 753,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 754,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 755,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 756,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 757,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 758,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 759,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 760,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 761,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 762,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 763,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 764,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 765,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 766,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 767,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 768,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 829,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 830,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 831,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 832,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 833,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 834,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 835,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 836,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 837,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 838,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 839,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 840,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 841,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 842,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 843,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 844,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 845,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 846,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 847,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 848,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 849,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 850,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 851,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 852,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 853,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 854,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 855,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 856,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 857,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 858,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 919,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 920,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 921,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 922,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 923,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 924,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 925,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 926,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 927,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 928,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 929,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 930,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 931,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 932,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 933,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 934,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 935,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 936,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 937,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 938,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 939,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 940,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 941,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 942,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 943,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 944,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 945,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 946,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 947,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 948,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1009,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1010,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1011,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1012,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1013,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1014,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1015,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1016,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1017,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1018,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1019,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1020,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1021,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1022,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1023,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1024,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1025,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1026,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1027,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1028,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1029,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1030,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1031,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1032,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1033,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1034,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1035,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1036,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1037,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1038,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1099,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1100,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1101,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1102,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1103,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1104,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1105,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1106,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1107,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1108,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1109,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1110,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1111,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1112,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1113,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1114,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1115,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1116,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1117,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1118,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1119,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1120,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1121,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1122,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1123,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1124,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1125,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1126,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1127,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1128,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1161,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1163,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1171,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1172,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1173,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1174,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1175,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1176,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        }
    ],
    "mage": [
        {
            "gearID": 53,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 54,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 55,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 56,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 57,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 58,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 59,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 60,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 61,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 62,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 63,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 64,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 65,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 66,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 67,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 68,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 69,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 70,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 71,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 72,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 73,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 74,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 75,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 76,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 77,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 78,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 139,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 140,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 141,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 142,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 143,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 144,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 145,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 146,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 147,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 148,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 149,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 150,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 151,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 152,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 153,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 154,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 155,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 156,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 157,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 158,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 159,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 160,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 161,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 162,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 163,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 164,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 165,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 166,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 167,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 168,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 229,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 230,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 231,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 232,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 233,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 234,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 235,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 236,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 237,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 238,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 239,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 240,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 241,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 242,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 243,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 244,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 245,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 246,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 247,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 248,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 249,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 250,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 251,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 252,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 253,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 254,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 255,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 256,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 257,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 258,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 319,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 320,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 321,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 322,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 323,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 324,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 325,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 326,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 327,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 328,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 329,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 330,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 331,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 332,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 333,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 334,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 335,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 336,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 337,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 338,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 339,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 340,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 341,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 342,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 343,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 344,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 345,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 346,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 347,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 348,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 409,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 410,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 411,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 412,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 413,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 414,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 415,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 416,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 417,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 418,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 419,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 420,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 421,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 422,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 423,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 424,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 425,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 426,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 427,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 428,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 429,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 430,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 431,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 432,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 433,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 434,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 435,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 436,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 437,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 438,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 499,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 500,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 501,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 502,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 503,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 504,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 505,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 506,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 507,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 508,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 509,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 510,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 511,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 512,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 513,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 514,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 515,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 516,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 517,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 518,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 519,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 520,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 521,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 522,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 523,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 524,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 525,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 526,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 527,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 528,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 589,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 590,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 591,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 592,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 593,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 594,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 595,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 596,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 597,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 598,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 599,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 600,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 601,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 602,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 603,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 604,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 605,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 606,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 607,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 608,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 609,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 610,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 611,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 612,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 613,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 614,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 615,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 616,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 617,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 618,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 679,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 680,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 681,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 682,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 683,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 684,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 685,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 686,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 687,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 688,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 689,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 690,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 691,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 692,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 693,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 694,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 695,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 696,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 697,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 698,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 699,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 700,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 701,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 702,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 703,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 704,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 705,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 706,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 707,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 708,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 769,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 770,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 771,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 772,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 773,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 774,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 775,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 776,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 777,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 778,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 779,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 780,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 781,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 782,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 783,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 784,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 785,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 786,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 787,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 788,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 789,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 790,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 791,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 792,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 793,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 794,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 795,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 796,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 797,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 798,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 859,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 860,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 861,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 862,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 863,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 864,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 865,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 866,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 867,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 868,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 869,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 870,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 871,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 872,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 873,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 874,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 875,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 876,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 877,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 878,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 879,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 880,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 881,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 882,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 883,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 884,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 885,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 886,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 887,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 888,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 949,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 950,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 951,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 952,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 953,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 954,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 955,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 956,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 957,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 958,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 959,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 960,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 961,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 962,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 963,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 964,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 965,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 966,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 967,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 968,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 969,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 970,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 971,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 972,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 973,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 974,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 975,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 976,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 977,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 978,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1039,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1040,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1041,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1042,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1043,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1044,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1045,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1046,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1047,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1048,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1049,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1050,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1051,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1052,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1053,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1054,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1055,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1056,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1057,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1058,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1059,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1060,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1061,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1062,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1063,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1064,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1065,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1066,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1067,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1068,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1129,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1130,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1131,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1132,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1133,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1134,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1135,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1136,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1137,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1138,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1139,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1140,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1141,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1142,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1143,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1144,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1145,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1146,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1147,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1148,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1149,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1150,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1151,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1152,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1153,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1154,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1155,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1156,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1157,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1158,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1160,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1164,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1165,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1166,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1167,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1168,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1169,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        },
        {
            "gearID": 1170,
            "tier": 1,
            "runes": [
                0,
                0,
                0
            ],
            "colors": [
                0,
                0
            ]
        }
    ],
}


default_learned_abilities = {
    "paladin": [
        {
            "abilityID": 27,
            "rank": 10
        },
        {
            "abilityID": 20,
            "rank": 9
        },
        {
            "abilityID": 21,
            "rank": 1
        },
        {
            "abilityID": 81,
            "rank": 8
        },
        {
            "abilityID": 22,
            "rank": 1
        },
        {
            "abilityID": 23,
            "rank": 1
        },
        {
            "abilityID": 19,
            "rank": 1
        },
        {
            "abilityID": 24,
            "rank": 1
        },
        {
            "abilityID": 25,
            "rank": 1
        },
        {
            "abilityID": 26,
            "rank": 1
        },
        {
            "abilityID": 48,
            "rank": 1
        },
        {
            "abilityID": 49,
            "rank": 1
        },
        {
            "abilityID": 50,
            "rank": 1
        },
        {
            "abilityID": 51,
            "rank": 1
        },
        {
            "abilityID": 52,
            "rank": 1
        },
        {
            "abilityID": 53,
            "rank": 1
        },
        {
            "abilityID": 54,
            "rank": 1
        },
        {
            "abilityID": 55,
            "rank": 1
        },
        {
            "abilityID": 56,
            "rank": 1
        },
        {
            "abilityID": 57,
            "rank": 1
        },
        {
            "abilityID": 78,
            "rank": 1
        },
        {
            "abilityID": 79,
            "rank": 1
        },
        {
            "abilityID": 80,
            "rank": 1
        },
        {
            "abilityID": 82,
            "rank": 1
        },
        {
            "abilityID": 83,
            "rank": 1
        },
        {
            "abilityID": 84,
            "rank": 1
        },
        {
            "abilityID": 85,
            "rank": 1
        },
        {
            "abilityID": 86,
            "rank": 1
        },
        {
            "abilityID": 87,
            "rank": 1
        },
        {
            "abilityID": 108,
            "rank": 1
        },
        {
            "abilityID": 109,
            "rank": 1
        },
        {
            "abilityID": 110,
            "rank": 1
        },
        {
            "abilityID": 111,
            "rank": 1
        },
        {
            "abilityID": 112,
            "rank": 1
        },
        {
            "abilityID": 113,
            "rank": 1
        },
        {
            "abilityID": 114,
            "rank": 1
        },
        {
            "abilityID": 115,
            "rank": 1
        },
        {
            "abilityID": 116,
            "rank": 1
        },
        {
            "abilityID": 117,
            "rank": 1
        }
    ],
    "rogue": [

        {
            "abilityID": 1,
            "rank": 10
        },
        {
            "abilityID": 2,
            "rank": 10
        },
        {
            "abilityID": 3,
            "rank": 10
        },
        {
            "abilityID": 4,
            "rank": 10
        },
        {
            "abilityID": 5,
            "rank": 10
        },
        {
            "abilityID": 6,
            "rank": 10
        },
        {
            "abilityID": 7,
            "rank": 10
        },
        {
            "abilityID": 8,
            "rank": 10
        },
        {
            "abilityID": 9,
            "rank": 10
        },
        {
            "abilityID": 38,
            "rank": 10
        },
        {
            "abilityID": 39,
            "rank": 10
        },
        {
            "abilityID": 40,
            "rank": 10
        },
        {
            "abilityID": 41,
            "rank": 10
        },
        {
            "abilityID": 42,
            "rank": 10
        },
        {
            "abilityID": 43,
            "rank": 10
        },
        {
            "abilityID": 44,
            "rank": 10
        },
        {
            "abilityID": 45,
            "rank": 10
        },
        {
            "abilityID": 46,
            "rank": 10
        },
        {
            "abilityID": 47,
            "rank": 10
        },
        {
            "abilityID": 68,
            "rank": 10
        },
        {
            "abilityID": 69,
            "rank": 10
        },
        {
            "abilityID": 70,
            "rank": 10
        },
        {
            "abilityID": 71,
            "rank": 10
        },
        {
            "abilityID": 72,
            "rank": 10
        },
        {
            "abilityID": 73,
            "rank": 10
        },
        {
            "abilityID": 74,
            "rank": 10
        },
        {
            "abilityID": 75,
            "rank": 10
        },
        {
            "abilityID": 76,
            "rank": 10
        },
        {
            "abilityID": 77,
            "rank": 10
        },
        {
            "abilityID": 88,
            "rank": 10
        },
        {
            "abilityID": 89,
            "rank": 10
        },
        {
            "abilityID": 90,
            "rank": 10
        },
        {
            "abilityID": 91,
            "rank": 10
        },
        {
            "abilityID": 92,
            "rank": 10
        },
        {
            "abilityID": 93,
            "rank": 10
        },
        {
            "abilityID": 94,
            "rank": 10
        },
        {
            "abilityID": 95,
            "rank": 10
        },
        {
            "abilityID": 96,
            "rank": 10
        },
        {
            "abilityID": 97,
            "rank": 10
        }
    ],
    "mage": [
        {
            "abilityID": 10,
            "rank": 10
        },
        {
            "abilityID": 11,
            "rank": 10
        },
        {
            "abilityID": 12,
            "rank": 10
        },
        {
            "abilityID": 13,
            "rank": 10
        },
        {
            "abilityID": 14,
            "rank": 10
        },
        {
            "abilityID": 15,
            "rank": 10
        },
        {
            "abilityID": 16,
            "rank": 10
        },
        {
            "abilityID": 17,
            "rank": 10
        },
        {
            "abilityID": 18,
            "rank": 10
        },
        {
            "abilityID": 28,
            "rank": 10
        },
        {
            "abilityID": 29,
            "rank": 10
        },
        {
            "abilityID": 30,
            "rank": 10
        },
        {
            "abilityID": 31,
            "rank": 10
        },
        {
            "abilityID": 32,
            "rank": 10
        },
        {
            "abilityID": 33,
            "rank": 10
        },
        {
            "abilityID": 34,
            "rank": 10
        },
        {
            "abilityID": 35,
            "rank": 10
        },
        {
            "abilityID": 36,
            "rank": 10
        },
        {
            "abilityID": 37,
            "rank": 10
        },
        {
            "abilityID": 58,
            "rank": 10
        },
        {
            "abilityID": 59,
            "rank": 10
        },
        {
            "abilityID": 60,
            "rank": 10
        },
        {
            "abilityID": 61,
            "rank": 10
        },
        {
            "abilityID": 62,
            "rank": 10
        },
        {
            "abilityID": 63,
            "rank": 10
        },
        {
            "abilityID": 64,
            "rank": 10
        },
        {
            "abilityID": 65,
            "rank": 10
        },
        {
            "abilityID": 66,
            "rank": 10
        },
        {
            "abilityID": 67,
            "rank": 10
        },
        {
            "abilityID": 98,
            "rank": 10
        },
        {
            "abilityID": 99,
            "rank": 10
        },
        {
            "abilityID": 100,
            "rank": 10
        },
        {
            "abilityID": 101,
            "rank": 10
        },
        {
            "abilityID": 102,
            "rank": 10
        },
        {
            "abilityID": 103,
            "rank": 10
        },
        {
            "abilityID": 104,
            "rank": 10
        },
        {
            "abilityID": 105,
            "rank": 10
        },
        {
            "abilityID": 106,
            "rank": 10
        },
        {
            "abilityID": 107,
            "rank": 10
        }

    ],
}