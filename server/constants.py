# constants.py
import time

NUM_TALENT_SLOTS = 27
CONST_529 = [5,2,3,5,5,3,2,3,2,5,2,3,5,5,3,2,3,2,5,2,3,5,5,3,2,3,2]
CLASS_118_CONST_127 = 6
const_228 = 4
GAME_CONST_209 = 4
ENTITY_CONST_244    = 2
Entity_const_172 = 3
class_9_const_28 = 5
class_1_const_254 = 7
class_64_const_499 = 2
class_64_const_218 = 5
class_111_const_432 = 9
class_10_const_665 = 4
ENT_MAX_SLOTS = 7
GS_BITS = 2
MAX_CHAR_LEVEL_BITS = 6
Game_const_646     = 4
EntType_MAX_SLOTS = 7
class_21_const_763 = 250
class_10_const_83  = 7
class_66_const_409 = 6
class_16_const_167 = 6
class_7_const_19 = 7
quest_val = None
class_9_const_129 = 5
class_66_const_571 = 2
class_7_const_75 = 6

SLOT_BIT_WIDTHS = []
for x in CONST_529:
    if x <= 2:
        SLOT_BIT_WIDTHS.append(1)
    elif x <= 4:
        SLOT_BIT_WIDTHS.append(2)
    elif x <= 5:
        SLOT_BIT_WIDTHS.append(3)
    else:
        SLOT_BIT_WIDTHS.append(0)


class class_119:
    const_228 = const_228

CLASS_NAME_TO_ID = {
    "Paladin": 0,
    "Rogue":   1,
    "Mage":    2,
}

class class_111 :
    const_286 = 1
    const_509 = 0
    const_432 = 9
    const_1101 = 511
    const_264 = 2

class LockboxType:
    ID_BITS = 8

class EntType:
    MAX_SLOTS = 7

class DyeType:
    BITS = 8

class Mission:
    const_72 = 2
    const_58 = 1

class class_118:
    const_43 = 27

class class_64:
    const_101 = 16

class GearType:
    GEARTYPE_BITSTOSEND = 11
    const_348          = 3
    const_176          = 2

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
    MissionDef(var_1775=False, var_908=1, var_134=False),  # mission ID 1
    MissionDef(var_1775=True,  var_908=2,  var_134=False),  # mission ID 2
    MissionDef(var_1775=False, var_908=3,  var_134=True ),  # mission ID 3
MissionDef(var_1775=False, var_908=4,  var_134=True ),  # mission ID 3
MissionDef(var_1775=False, var_908=5,  var_134=True ),  # mission ID 3
    # …and so on for all mission IDs…
]



NEWS_EVENTS = {
    1: ["a_NewsGoldIcon",      "Double Gold Event",     "While this event is in place all gold will be doubled world wide",       "http://www.dungeonblitz.com/", 1387602000],
    2: ["a_NewsGearIcon",      "Double Gear Event",     "While this event is in place all gear drops will be doubled world wide",  "http://www.dungeonblitz.com/", 1387602000],
    3: ["a_NewsMatsIcon",      "Double Material Event", "While this event is in place all material drops will be doubled world wide","http://www.dungeonblitz.com/",1387602000],
    4: ["a_NewsXPIcon",        "Double XP Event",       "While this event is in place all XP gained will be doubled world wide",     "http://www.dungeonblitz.com/",1387602000],
    5: ["a_NewsPetXPIcon",     "Double Pet XP Event",   "While this event is in place all pet XP gained will be doubled world wide", "http://www.dungeonblitz.com/",1387602000],
}

