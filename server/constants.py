# constants.py
import json
import os
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
GEARTYPE_BITS = 11#
Entity_const_172_bits = 3

SLOT_BIT_WIDTHS = []
for x in CONST_529:
    w = 0
    if x <= 2:
        w = 1
    if x <= 4:
        w = 2
    if x <= 5:
        w = 3
    SLOT_BIT_WIDTHS.append(w)

def method_277(idx: int) -> int:
    x = CONST_529[idx]
    w = 0
    if x <= 2: w = 1
    if x <= 4: w = 2
    if x <= 5: w = 3
    return w

class Mission:
    const_213 = 0
    const_58  = 1
    const_72  = 2

class class_119:
    const_228 = 4

CLASS_NAME_TO_ID = {
    "Paladin": 0,
    "Rogue":   1,
    "Mage":    2,
}
class class_8:
    const_658 = 7
    const_731 = 7
class class_7 :
    const_19 = 7
    const_75 = 6
class class_20 :
    const_297 = 7
class class_3 :
    const_69 = 5
    var_1415 = 1  # ForgeXP
    var_2082 = 2  # RareBoost
    var_1374 = 3  # LegendaryBoost
    var_1462 = 4  # ArtisanBoost


class Entity:
    TEAM_BITS = 2
    const_316 = 2  # Entity state bit count
    const_399 = 1  # Sleep state
    const_467 = 2  # Drama state
    const_6 = 3
    const_526 = 0
    MAX_CHAR_LEVEL_BITS = 6
    VELOCITY_INFLATE = 10000
    const_78 = 0
    PLAYER = 1


class LinkUpdater:
    VELOCITY_DEFLATE = 10000
class Game :
    const_209 = 4
class class_118 :
    const_127 = 6
    const_43 = 27


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
    STATE_IDLE = 6
    STATE_ACTIVE = 78
    CHAR_COLOR_BITSTOSEND = 24

class DyeType:
    BITS = 8

class class_1:
    const_765 = 2

class class_64:
    const_101 = 16

class GearType:
    GEARTYPE_BITSTOSEND = 11
    const_348          = 3
    const_176          = 2

NEWS_EVENTS = {
    1: ["a_NewsGoldIcon",      "Double Gold Event",     "While this event is in place all gold will be doubled world wide",       "http://www.dungeonblitz.com/", 1387602000],
    2: ["a_NewsGearIcon",      "Double Gear Event",     "While this event is in place all gear drops will be doubled world wide",  "http://www.dungeonblitz.com/", 1387602000],
    3: ["a_NewsMatsIcon",      "Double Material Event", "While this event is in place all material drops will be doubled world wide","http://www.dungeonblitz.com/",1387602000],
    4: ["a_NewsXPIcon",        "Double XP Event",       "While this event is in place all XP gained will be doubled world wide",     "http://www.dungeonblitz.com/",1387602000],
    5: ["a_NewsPetXPIcon",     "Double Pet XP Event",   "While this event is in place all pet XP gained will be doubled world wide", "http://www.dungeonblitz.com/",1387602000],
}
               #Loaders
################################################################

# load the JSON file into a dict
with open("data/DyeTypes.json", "r", encoding="utf-8") as f:
    DYE_DATA = json.load(f)

def get_dye_color(dye_id):
    dye = DYE_DATA.get(str(dye_id))
    if dye:
        return dye["color"]
    return None


def load_gear_data(class_name):
    path = os.path.join("data", f"{class_name.lower()}_gears.json")
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load {class_name} gear data: {e}")
        return []

inventory_gears = {
    "paladin": load_gear_data("paladin"),
    "mage": load_gear_data("mage"),
    "rogue": load_gear_data("rogue"),
}

with open("data/MasteryClass.json", "r", encoding="utf-8") as f:
    Mastery_Class = json.load(f)

def get_starting_mastery(cls):
    return Mastery_Class.get(cls, [])