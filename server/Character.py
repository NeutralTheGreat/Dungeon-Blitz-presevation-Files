# Character.py

import os
import json
from BitUtils import BitBuffer
from constants import inventory_gears

#Hints Do not delete
"""
"inventoryGears": [
    # {"gearID": 1, "tier": 1, "runes": [1, 2, 3], "colors": [255, 0]},
    # {"gearID": 13, "tier": 2, "runes": [0, 0, 0], "colors": [0, 128]},
    # {"gearID": 30, "tier": 0, "runes": [0, 0, 0], "colors": [0, 0]}
],
"gearSets": [
    {
      "name": "PvP Build",
           (ChestPlate) (Gloves)(Boots) (Hat) (Sword) (Shield)
        "slots": [ 1181,  1180,   1182, 1181,   1177,    1178 ]
    }
  ]
"""


# ──────────────── Default full gear definitions ────────────────
# Each sub-list is [GearID, Rune1, Rune2, Rune3, Color1, Color2]
DEFAULT_GEAR = {
    "paladin": [
        [1, 0, 0, 0, 0, 0], #Shield
        [13, 0, 0, 0, 0, 0], #Sword
        [0, 0, 0, 0, 0, 0], #Gloves
        [0, 0, 0, 0, 0, 0], #Hat
        [0, 0, 0, 0, 0, 0], #Armor
        [0, 0, 0, 0, 0, 0], #Boots
    ],
    "rogue": [
        [39, 0, 0, 0,  0, 0], #Off Hand/Shield
        [27, 0, 0, 0,  0, 0], #Sword
        [0, 0, 0, 0,  0, 0], #Gloves
        [0, 0, 0, 0,  0, 0], #Hat
        [0, 0, 0, 0,  0, 0], #Armor
        [0, 0, 0, 0,  0, 0], #Boots
    ],
    "mage": [
        [53, 0, 0, 0, 0, 0], #Staff
        [65, 0, 0, 0, 0, 0], #Focus/Shield
        [0, 0, 0, 0, 0, 0], #Gloves
        [ 0, 0, 0, 0, 0, 0], #Hat
        [0, 0, 0, 0, 0, 0], #Robe
        [0, 0, 0, 0, 0, 0], #Boots
    ],
}

CHAR_SAVE_DIR = "saves"

def load_characters(user_id: str) -> list[dict]:
    """Load the list of characters for a given user_id."""
    path = os.path.join(CHAR_SAVE_DIR, f"{user_id}.json")
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("characters", [])

def save_characters(user_id: str, char_list: list[dict]):
    """Save the list of characters for a given user_id, preserving other fields."""
    os.makedirs(CHAR_SAVE_DIR, exist_ok=True)
    path = os.path.join(CHAR_SAVE_DIR, f"{user_id}.json")
    # Load existing to preserve email
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"email": None, "characters": []}
    data["characters"] = char_list
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def default_master_for_base(base_cls: str) -> str:
    """Return the default “first” MasterClass name for a given base class."""
    if base_cls == "Paladin":
        return "Sentinel"
    if base_cls == "Rogue":
        return "Executioner"
    if base_cls == "Mage":
        return "Frostwarden"
    return ""

def make_character_dict_from_tuple(character):
    """
    character is a tuple of:
      (name, class_name, level,
       gender, head, hair, mouth, face,
       hair_color, skin_color, shirt_color, pant_color,
       equipped_gear)
    where equipped_gear can be:
      - None → use DEFAULT_GEAR for that class
      - a list of six 6-element lists → use directly
    """
    (name, class_name, level,
     gender, head, hair, mouth, face,
     hair_color, skin_color, shirt_color, pant_color,
     equipped_gear) = character

    cls = class_name.lower()

    # If provided a full 6×6 structure, validate and use it:
    if (isinstance(equipped_gear, (list, tuple))
        and len(equipped_gear) == 6
        and all(isinstance(slot, (list, tuple)) and len(slot) == 6
                for slot in equipped_gear)):
        gear_list = [list(slot) for slot in equipped_gear]
    else:
        # Otherwise, pull from our per-class defaults
        default = DEFAULT_GEAR.get(cls, [[0]*6]*6)
        gear_list = [list(slot) for slot in default]

    starting_inventory = inventory_gears.get(cls, [])

    # Assemble the character dict
    char_dict = {
        "name":       name,
        "class":      class_name,
        "level":      level,
        "gender":     gender or "Male",
        "headSet":    head or "Head01",
        "hairSet":    hair or "Hair01",
        "mouthSet":   mouth or "Mouth01",
        "faceSet":    face or "Face01",
        "hairColor":  hair_color,
        "skinColor":  skin_color,
        "shirtColor": shirt_color,
        "pantColor":  pant_color,

        # Now each slot is [GearID, Rune1, Rune2, Rune3, Color1, Color2]
        "gearList":   gear_list,

        # ── new persistent fields ───────────────────────────────
        "xp":             10,
        "gold":           100000,
        "Gems":           100000,
        "DragonOre":      100000,
        "mammothIdols":   100000,
        "DragonKeys":     100000,
        "SilverSigils":   100000,
        "showHigher":     True,
        "MasterClass":    default_master_for_base(class_name),
        "inventoryGears":  starting_inventory,
        "mounts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
            71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
            81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
            91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
            101, 102, 103, 104, 105, 106, 107, 108],
        "learnedAbilities": [{"abilityID": 27, "rank": 10}, {"abilityID": 20, "rank": 9}, {"abilityID": 21, "rank": 1},
                             {"abilityID": 81, "rank": 8}, {"abilityID": 22, "rank": 1}, {"abilityID": 23, "rank": 1},
                             {"abilityID": 19, "rank": 1}, {"abilityID": 24, "rank": 1}, {"abilityID": 25, "rank": 1},
                             {"abilityID": 26, "rank": 1}, {"abilityID": 48, "rank": 1}, {"abilityID": 49, "rank": 1},
                             {"abilityID": 50, "rank": 1}, {"abilityID": 51, "rank": 1}, {"abilityID": 52, "rank": 1},
                             {"abilityID": 53, "rank": 1}, {"abilityID": 54, "rank": 1}, {"abilityID": 55, "rank": 1},
                             {"abilityID": 56, "rank": 1}, {"abilityID": 57, "rank": 1}, {"abilityID": 78, "rank": 1},
                             {"abilityID": 79, "rank": 1}, {"abilityID": 80, "rank": 1}, {"abilityID": 82, "rank": 1},
                             {"abilityID": 83, "rank": 1}, {"abilityID": 84, "rank": 1}, {"abilityID": 85, "rank": 1},
                             {"abilityID": 86, "rank": 1}, {"abilityID": 87, "rank": 1}, {"abilityID": 108, "rank": 1},
                             {"abilityID": 109, "rank": 1}, {"abilityID": 110, "rank": 1},
                             {"abilityID": 111, "rank": 1}, {"abilityID": 112, "rank": 1},
                             {"abilityID": 113, "rank": 1}, {"abilityID": 114, "rank": 1},
                             {"abilityID": 115, "rank": 1}, {"abilityID": 116, "rank": 1},
                             {"abilityID": 117, "rank": 1}],
        "activeAbilities": [20, 0, 0],
        "pets":[{"typeID":1,"level":1,"xp":0,"attr2":0},{"typeID":2,"level":1,"xp":0,"attr2":0},{"typeID":3,"level":1,"xp":0,"attr2":0},{"typeID":4,"level":1,"xp":0,"attr2":0},{"typeID":5,"level":1,"xp":0,"attr2":0},{"typeID":6,"level":1,"xp":0,"attr2":0},{"typeID":7,"level":1,"xp":0,"attr2":0},{"typeID":8,"level":1,"xp":0,"attr2":0},{"typeID":9,"level":1,"xp":0,"attr2":0},{"typeID":10,"level":1,"xp":0,"attr2":0},{"typeID":11,"level":1,"xp":0,"attr2":0},{"typeID":12,"level":1,"xp":0,"attr2":0},{"typeID":13,"level":1,"xp":0,"attr2":0},{"typeID":14,"level":1,"xp":0,"attr2":0},{"typeID":15,"level":1,"xp":0,"attr2":0},{"typeID":16,"level":1,"xp":0,"attr2":0},{"typeID":17,"level":1,"xp":0,"attr2":0},{"typeID":18,"level":1,"xp":0,"attr2":0},{"typeID":19,"level":1,"xp":0,"attr2":0},{"typeID":20,"level":1,"xp":0,"attr2":0},{"typeID":21,"level":1,"xp":0,"attr2":0},{"typeID":22,"level":1,"xp":0,"attr2":0},{"typeID":23,"level":1,"xp":0,"attr2":0},{"typeID":24,"level":1,"xp":0,"attr2":0},{"typeID":25,"level":1,"xp":0,"attr2":0},{"typeID":26,"level":1,"xp":0,"attr2":0},{"typeID":27,"level":1,"xp":0,"attr2":0},{"typeID":28,"level":1,"xp":0,"attr2":0},{"typeID":29,"level":1,"xp":0,"attr2":0},{"typeID":30,"level":1,"xp":0,"attr2":0},{"typeID":31,"level":1,"xp":0,"attr2":0},{"typeID":32,"level":1,"xp":0,"attr2":0},{"typeID":33,"level":1,"xp":0,"attr2":0},{"typeID":34,"level":1,"xp":0,"attr2":0},{"typeID":35,"level":1,"xp":0,"attr2":0},{"typeID":36,"level":1,"xp":0,"attr2":0},{"typeID":37,"level":1,"xp":0,"attr2":0},{"typeID":38,"level":1,"xp":0,"attr2":0},{"typeID":39,"level":1,"xp":0,"attr2":0},{"typeID":40,"level":1,"xp":0,"attr2":0},{"typeID":41,"level":1,"xp":0,"attr2":0},{"typeID":42,"level":1,"xp":0,"attr2":0},{"typeID":43,"level":1,"xp":0,"attr2":0},{"typeID":44,"level":1,"xp":0,"attr2":0},{"typeID":45,"level":1,"xp":0,"attr2":0},{"typeID":46,"level":1,"xp":0,"attr2":0},{"typeID":47,"level":1,"xp":0,"attr2":0},{"typeID":48,"level":1,"xp":0,"attr2":0},{"typeID":49,"level":1,"xp":0,"attr2":0},{"typeID":50,"level":1,"xp":0,"attr2":0},{"typeID":51,"level":1,"xp":0,"attr2":0},{"typeID":52,"level":1,"xp":0,"attr2":0},{"typeID":53,"level":1,"xp":0,"attr2":0},{"typeID":54,"level":1,"xp":0,"attr2":0},{"typeID":55,"level":1,"xp":0,"attr2":0},{"typeID":56,"level":1,"xp":0,"attr2":0},{"typeID":57,"level":1,"xp":0,"attr2":0},{"typeID":58,"level":1,"xp":0,"attr2":0},{"typeID":59,"level":1,"xp":0,"attr2":0},{"typeID":60,"level":1,"xp":0,"attr2":0},{"typeID":61,"level":1,"xp":0,"attr2":0},{"typeID":62,"level":1,"xp":0,"attr2":0},{"typeID":63,"level":1,"xp":0,"attr2":0},{"typeID":64,"level":1,"xp":0,"attr2":0},{"typeID":65,"level":1,"xp":0,"attr2":0},{"typeID":66,"level":1,"xp":0,"attr2":0},{"typeID":67,"level":1,"xp":0,"attr2":0},{"typeID":68,"level":1,"xp":0,"attr2":0},{"typeID":69,"level":1,"xp":0,"attr2":0},{"typeID":70,"level":1,"xp":0,"attr2":0}],
        "charms": [
            {"charmID": 1, "count": 10},
            {"charmID": 2, "count": 10},
            {"charmID": 3, "count": 10},
            {"charmID": 4, "count": 10},
            {"charmID": 5, "count": 10},
            {"charmID": 6, "count": 10},
            {"charmID": 7, "count": 10},
            {"charmID": 8, "count": 10},
            {"charmID": 9, "count": 10},
            {"charmID": 10, "count": 10},
            {"charmID": 11, "count": 10},
            {"charmID": 12, "count": 10},
            {"charmID": 13, "count": 10},
            {"charmID": 14, "count": 10},
            {"charmID": 15, "count": 10},
            {"charmID": 16, "count": 10},
            {"charmID": 17, "count": 10},
            {"charmID": 18, "count": 10},
            {"charmID": 19, "count": 10},
            {"charmID": 20, "count": 10},
            {"charmID": 21, "count": 10},
            {"charmID": 22, "count": 10},
            {"charmID": 23, "count": 10},
            {"charmID": 24, "count": 10},
            {"charmID": 25, "count": 10},
            {"charmID": 26, "count": 10},
            {"charmID": 27, "count": 10},
            {"charmID": 28, "count": 10},
            {"charmID": 29, "count": 10},
            {"charmID": 30, "count": 10},
            {"charmID": 31, "count": 10},
            {"charmID": 32, "count": 10},
            {"charmID": 33, "count": 10},
            {"charmID": 34, "count": 10},
            {"charmID": 35, "count": 10},
            {"charmID": 36, "count": 10},
            {"charmID": 37, "count": 10},
            {"charmID": 38, "count": 10},
            {"charmID": 39, "count": 10},
            {"charmID": 40, "count": 10},
            {"charmID": 41, "count": 10},
            {"charmID": 42, "count": 10},
            {"charmID": 43, "count": 10},
            {"charmID": 44, "count": 10},
            {"charmID": 45, "count": 10},
            {"charmID": 46, "count": 10},
            {"charmID": 47, "count": 10},
            {"charmID": 48, "count": 10},
            {"charmID": 49, "count": 10},
            {"charmID": 50, "count": 10},
            {"charmID": 51, "count": 10},
            {"charmID": 52, "count": 10},
            {"charmID": 53, "count": 10},
            {"charmID": 54, "count": 10},
            {"charmID": 55, "count": 10},
            {"charmID": 56, "count": 10},
            {"charmID": 57, "count": 10},
            {"charmID": 58, "count": 10},
            {"charmID": 59, "count": 10},
            {"charmID": 60, "count": 10},
            {"charmID": 61, "count": 10},
            {"charmID": 62, "count": 10},
            {"charmID": 63, "count": 10},
            {"charmID": 64, "count": 10},
            {"charmID": 65, "count": 10},
            {"charmID": 66, "count": 10},
            {"charmID": 67, "count": 10},
            {"charmID": 68, "count": 10},
            {"charmID": 69, "count": 10},
            {"charmID": 70, "count": 10},
            {"charmID": 71, "count": 10},
            {"charmID": 72, "count": 10},
            {"charmID": 73, "count": 10},
            {"charmID": 74, "count": 10},
            {"charmID": 75, "count": 10},
            {"charmID": 76, "count": 10},
            {"charmID": 77, "count": 10},
            {"charmID": 78, "count": 10},
            {"charmID": 79, "count": 10},
            {"charmID": 80, "count": 10},
            {"charmID": 81, "count": 10},
            {"charmID": 82, "count": 10},
            {"charmID": 83, "count": 10},
            {"charmID": 84, "count": 10},
            {"charmID": 85, "count": 10},
            {"charmID": 86, "count": 10},
            {"charmID": 87, "count": 10},
            {"charmID": 88, "count": 10},
            {"charmID": 89, "count": 10},
            {"charmID": 90, "count": 10},
            {"charmID": 91, "count": 10},
            {"charmID": 92, "count": 10},
            {"charmID": 93, "count": 10},
            {"charmID": 94, "count": 10},
            {"charmID": 95, "count": 10},
            {"charmID": 96, "count": 10}
        ],
        "materials": [
            {"materialID": 1, "count": 10},
            {"materialID": 2, "count": 10},
            {"materialID": 3, "count": 10},
            {"materialID": 4, "count": 10},
            {"materialID": 5, "count": 10},
            {"materialID": 6, "count": 10},
            {"materialID": 7, "count": 10},
            {"materialID": 8, "count": 10},
            {"materialID": 9, "count": 10},
            {"materialID": 10, "count": 10},
            {"materialID": 11, "count": 10},
            {"materialID": 12, "count": 10},
            {"materialID": 13, "count": 10},
            {"materialID": 14, "count": 10},
            {"materialID": 15, "count": 10},
            {"materialID": 16, "count": 10},
            {"materialID": 17, "count": 10},
            {"materialID": 18, "count": 10},
            {"materialID": 19, "count": 10},
            {"materialID": 20, "count": 10},
            {"materialID": 21, "count": 10},
            {"materialID": 22, "count": 10},
            {"materialID": 23, "count": 10},
            {"materialID": 24, "count": 10},
            {"materialID": 25, "count": 10},
            {"materialID": 26, "count": 10},
            {"materialID": 27, "count": 10},
            {"materialID": 28, "count": 10},
            {"materialID": 29, "count": 10},
            {"materialID": 30, "count": 10},
            {"materialID": 31, "count": 10},
            {"materialID": 32, "count": 10},
            {"materialID": 33, "count": 10},
            {"materialID": 34, "count": 10},
            {"materialID": 35, "count": 10},
            {"materialID": 36, "count": 10},
            {"materialID": 37, "count": 10},
            {"materialID": 38, "count": 10},
            {"materialID": 39, "count": 10},
            {"materialID": 40, "count": 10},
            {"materialID": 41, "count": 10},
            {"materialID": 42, "count": 10},
            {"materialID": 43, "count": 10},
            {"materialID": 44, "count": 10},
            {"materialID": 45, "count": 10},
            {"materialID": 46, "count": 10},
            {"materialID": 47, "count": 10},
            {"materialID": 48, "count": 10},
            {"materialID": 49, "count": 10},
            {"materialID": 50, "count": 10},
            {"materialID": 51, "count": 10},
            {"materialID": 52, "count": 10},
            {"materialID": 53, "count": 10},
            {"materialID": 54, "count": 10},
            {"materialID": 55, "count": 10},
            {"materialID": 56, "count": 10},
            {"materialID": 57, "count": 10},
            {"materialID": 58, "count": 10},
            {"materialID": 59, "count": 10},
            {"materialID": 60, "count": 10},
            {"materialID": 61, "count": 10},
            {"materialID": 62, "count": 10},
            {"materialID": 63, "count": 10},
            {"materialID": 64, "count": 10},
            {"materialID": 65, "count": 10},
            {"materialID": 66, "count": 10},
            {"materialID": 67, "count": 10},
            {"materialID": 68, "count": 10},
            {"materialID": 69, "count": 10},
            {"materialID": 70, "count": 10},
            {"materialID": 71, "count": 10},
            {"materialID": 72, "count": 10},
            {"materialID": 73, "count": 10},
            {"materialID": 74, "count": 10},
            {"materialID": 75, "count": 10},
            {"materialID": 76, "count": 10},
            {"materialID": 77, "count": 10},
            {"materialID": 78, "count": 10},
            {"materialID": 79, "count": 10},
            {"materialID": 80, "count": 10},
            {"materialID": 81, "count": 10},
            {"materialID": 82, "count": 10},
            {"materialID": 83, "count": 10},
            {"materialID": 84, "count": 10},
            {"materialID": 85, "count": 10},
            {"materialID": 86, "count": 10},
            {"materialID": 87, "count": 10},
            {"materialID": 88, "count": 10},
            {"materialID": 89, "count": 10},
            {"materialID": 90, "count": 10},
            {"materialID": 91, "count": 10},
            {"materialID": 92, "count": 10},
            {"materialID": 93, "count": 10},
            {"materialID": 94, "count": 10},
            {"materialID": 95, "count": 10},
            {"materialID": 96, "count": 10},
            {"materialID": 97, "count": 10},
            {"materialID": 98, "count": 10},
            {"materialID": 99, "count": 10},
            {"materialID": 100, "count": 10},
            {"materialID": 101, "count": 10},
            {"materialID": 102, "count": 10},
            {"materialID": 103, "count": 10},
            {"materialID": 104, "count": 10},
            {"materialID": 105, "count": 10},
            {"materialID": 106, "count": 10},
            {"materialID": 107, "count": 10},
            {"materialID": 108, "count": 10},
            {"materialID": 109, "count": 10},
            {"materialID": 110, "count": 10},
            {"materialID": 111, "count": 10},
            {"materialID": 112, "count": 10},
            {"materialID": 113, "count": 10},
            {"materialID": 114, "count": 10},
            {"materialID": 115, "count": 10},
            {"materialID": 116, "count": 10},
            {"materialID": 117, "count": 10},
            {"materialID": 118, "count": 10},
            {"materialID": 119, "count": 10},
            {"materialID": 120, "count": 10},
            {"materialID": 121, "count": 10},
            {"materialID": 122, "count": 10},
            {"materialID": 123, "count": 10},
            {"materialID": 124, "count": 10},
            {"materialID": 125, "count": 10},
            {"materialID": 126, "count": 10}
        ],
        "lockboxes": [
            {"lockboxID": 1, "count": 10}
        ],
        "consumables": [
            {"consumableID": 1, "count": 10},
            {"consumableID": 2, "count": 10},
            {"consumableID": 3, "count": 10},
            {"consumableID": 4, "count": 10},
            {"consumableID": 5, "count": 10},
            {"consumableID": 6, "count": 10},
            {"consumableID": 7, "count": 10},
            {"consumableID": 8, "count": 10},
            {"consumableID": 9, "count": 10},
            {"consumableID": 10, "count": 10},
            {"consumableID": 11, "count": 10},
            {"consumableID": 12, "count": 10},
            {"consumableID": 13, "count": 10}
        ],
        "friends": [
            {
                "name": "Neutral",
                "className": "Paladin",
                "level": 40,
                "stateVersion": 5
            },
            {
                "name": "Neo",
                "className": "Mage",
                "level": 20,
                "stateVersion": 5
            },
            {
                "name": "Tired",
                "className": "Rogue",
                "level": 23,
                "stateVersion": 5
            },
            {
                "name": "Telahair",
                "className": "Mage",
                "level": 23,
                "stateVersion": 5
            }
        ],
        "magicForge": {
        "stats": [1, 0, 2, 0, 1, 3, 0], #// _loc21_.._loc27_, each class_9.const_28 bits
        "hasSession": True, #// triggers the “ else ” branch
        "primary": 5, #// _loc123_, class_1.const_254 bits
        "status": "ready", #// one of “inProgress”, “ready”, or “idle”
        "endTime": 0, #// only if inProgress
        "modSlotID": 42, #// only if ready
        "modTier": 2, #// class_64.const_218 bits
        "usedList": 1, #// class_111.const_432 bits
        "flagA": True, #// two method_91() booleans
        "flagB": False
        },
        "gearSets": [
            {
                "name": "PvP Build",
                "slots": [1180, 1181, 1182, 1179, 1177, 1178]
            }
        ]
    }


    return char_dict

def build_paperdoll_packet(character_dict):

    buf = BitBuffer()
    buf.write_utf_string(character_dict["name"])
    buf.write_utf_string(character_dict["class"])
    buf.write_utf_string(character_dict["gender"])
    buf.write_utf_string(character_dict["headSet"])
    buf.write_utf_string(character_dict["hairSet"])
    buf.write_utf_string(character_dict["mouthSet"])
    buf.write_utf_string(character_dict["faceSet"])
    buf.write_bits(character_dict["hairColor"], 24)
    buf.write_bits(character_dict["skinColor"], 24)
    buf.write_bits(character_dict["shirtColor"], 24)
    buf.write_bits(character_dict["pantColor"], 24)

    # Write exactly 6 gear slots, using only the GearID (slot[0])
    for slot in character_dict.get("gearList", []):
        gear_id = slot[0]
        buf.write_bits(gear_id, 11)

    return buf.to_bytes()

def build_login_character_list_bitpacked(characters):
    """
    Builds the 0x15 login-character-list packet.
    """
    buf = BitBuffer()
    user_id   = 1       # you’ll overwrite this per-session
    max_chars = 8
    char_count= len(characters)

    buf.write_method_4(user_id)
    buf.write_method_393(max_chars)
    buf.write_method_393(char_count)

    for char in characters:
        buf.write_utf_string(char["name"])
        buf.write_utf_string(char["class"])
        buf.write_method_6(char["level"], 6)

    import struct
    header = struct.pack(">HH", 0x15, len(buf.to_bytes()))
    return header + buf.to_bytes()
