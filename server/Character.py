# Character.py

import os
import json
from BitUtils import BitBuffer
from Items import  Starting_Mounts, Starting_Pets, Starting_Charms, Starting_Materials, Starting_Consumables, Active_master_Class, Starter_Weapons, Active_Abilities
from constants import inventory_gears
from default_abilities import default_learned_abilities
from constants import Mastery_Class
#Hints Do not delete
"""

"research": {
        "abilityID": 113,
        "finishTime": 50
      },
"inventoryGears": [
    # {"gearID": 1, "tier": 1, "runes": [1, 2, 3], "colors": [255, 0]}
], 
  "gearSets": [
    {
      "name": "PvP Build",    
        "slots": [4 1181, (ChestPlate)
                  5 1180, (Gloves)
                  6 1182, (Boots)
                  3 1181, (Hat)
                  1 1177, (Sword)
                  2 1178  (Shield)
        ]
    }
  ]
    "magicForge": {
            (Forge) (Keep) (Tower1)(Tower2)(Tower3)(Tome)(Barn)
    "stats": [    1,    0,       0,      1,     1,     1,    1],
    "hasSession": true, # true if the forge is active : false if the forge is idle or has finished the rune
    "primary": 1, # Rune 1 
    "secondary": 1, # Rune 2 
    "status": 2, # Crafting in progress
    "var_8": 1, # Unknown (i assume this is Likely a gem counter or flag.)
    "usedlist": 2,# Number of gems used (primary + secondary)
    "var_2675": 5000, #Unknown (timers maybe ?)
    "var_2316": 6000, #Unknown (timers maybe ?)
    "var_2434": true
}
  
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
    starting_abilities = default_learned_abilities.get(cls, [])
    starting_talent = Active_master_Class.get(cls, [])
    Starting_Mastery = Mastery_Class.get(cls, [])
    starter_gear = Starter_Weapons.get(cls, [])
    Starting_Active_Abilities = Active_Abilities.get(cls, [])

    char_dict = {
        "CurrentLevel": "CraftTown",
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
        "equippedGears": starter_gear,
        "xp":             10,
        "gold":           100000,
        "Gems":           100000,# this is the XP for the magic forge
        "DragonOre":      100000,
        "mammothIdols":   100000,
        "DragonKeys":     100000,
        "SilverSigils":   100000,
        "showHigher":     True,
        "MasterClass": starting_talent,
        "Mastery" : Starting_Mastery,
        #=================
        "magicForge": {
        "stats": [10, 0, 10, 10, 10, 10, 10],
        "hasSession": False,  # true if the forge is active : false if the forge is idle or has finished the rune
        "primary": 0,  # Rune 1
        "secondary": 0,  # Rune 2
        "status": 0,  # Crafting in progress
        "var_8": 0,  # Unknown (i assume this is Likely a gem counter or flag.)
        "usedlist": 0,  # Number of gems used (primary + secondary)
        "var_2675": 0,  # Unknown (timers maybe ?)
        "var_2316": 0,  # Unknown (timers maybe ?)
        "var_2434": True},
        #===================
        "activeAbilities": Starting_Active_Abilities,
        "craftTalentPoints": [5, 5, 5, 5, 5],# these are the Magic Forge upgrade points Max value is 10 each
        "towerPoints": [50, 50, 50],# Talent upgrade 50 Max each
        "equippedMount": 5,
        "equippedPetID": 1,
        "petIteration": 0,
        "activeConsumableID": 13,
        "queuedConsumableID": 12,
        "research": {
        "abilityID": 0,
        "ReadyTime": 0
        },
        "buildingResearch": {
        "slotID": 0,
        "finishTime": 0
        },
        "towerResearch": {
        "masterClassID": 0,
        "endTime": 0
        },
        "eggData": {
        "typeID": 1,
        "resetEndTime": 5000
        },
        "eggPetIDs": [1, 2, 30, 27, 5,35,20,17],
        "activeEggCount": 8,
        "restingPets": [
            {"typeID": 1, "level": 1, "extraValue": 0},
            {"typeID": 2, "level": 1, "extraValue": 0},
            {"typeID": 30, "level": 1, "extraValue": 0},
            {"typeID": 27, "level": 1, "extraValue": 0}
        ],
        "missions": {
            "1": {
                "state": 2
            },
            "2": {
                "state": 2
            },
            "3": {
                "state": 2
            }
        },
        "learnedAbilities": starting_abilities,
        "inventoryGears":  starting_inventory,
        "lockboxes": [{"lockboxID": 1, "count": 100}],
        "gearSets": [
        ],
        "mounts":Starting_Mounts,
        "pets":Starting_Pets,
        "charms":Starting_Charms,
        "materials":Starting_Materials,
        "consumables":Starting_Consumables,
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
        "guild": {
            "name": "KnightsOfValor",
            "rank": 2,
            "onlineMembers": [
                {
                    "name": "Teggdel",
                    "classID": 0,
                    "level": 45,
                    "status": 1
                },
                {
                    "name": "ProGooner",
                    "classID": 1,
                    "level": 50,
                    "status": 3
                },
                {
                    "name": "Fitler",
                    "classID": 2,
                    "level": 47,
                    "status": 3
                },
                {
                    "name": "DrHouse",
                    "classID": 2,
                    "level": 22,
                    "status": 3
                },
                {
                    "name": "FriendlyNephit",
                    "classID": 1,
                    "level": 43,
                    "status": 3
                },
                {
                    "name": "SneakyMcStab",
                    "classID": 1,
                    "level": 48,
                    "status": 1
                },
                {
                    "name": "HolyTickler",
                    "classID": 0,
                    "level": 42,
                    "status": 1
                },
                {
                    "name": "WizzyMcFizzle",
                    "classID": 2,
                    "level": 46,
                    "status": 0
                },
                {
                    "name": "PwnyThePaladin",
                    "classID": 0,
                    "level": 40,
                    "status": 1
                },
                {
                    "name": "StabbyMcSneak",
                    "classID": 1,
                    "level": 44,
                    "status": 0
                },
                {
                    "name": "SparkleFart",
                    "classID": 2,
                    "level": 39,
                    "status": 1
                },
                {
                    "name": "SirGiggles",
                    "classID": 0,
                    "level": 41,
                    "status": 2
                },
                {
                    "name": "RogueyMcRoguface",
                    "classID": 1,
                    "level": 47,
                    "status": 2
                },
                {
                    "name": "MagicTickler",
                    "classID": 2,
                    "level": 43,
                    "status": 1
                },
                {
                    "name": "ShieldyMcBloop",
                    "classID": 0,
                    "level": 38,
                    "status": 0
                }
            ]
        },

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

    #TODO....
    #for slot in character_dict.get("gearList", []):
        #gear_id = slot[0]
        #buf.write_bits(gear_id, 11)

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
