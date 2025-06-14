# Character.py

import os
import json
from BitUtils import BitBuffer


#Hints Do not delete
"""
"inventoryGears": [
    # {"gearID": 1, "tier": 1, "runes": [1, 2, 3], "colors": [255, 0]},
    # {"gearID": 13, "tier": 2, "runes": [0, 0, 0], "colors": [0, 128]},
    # {"gearID": 30, "tier": 0, "runes": [0, 0, 0], "colors": [0, 0]}
],
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
        "xp":             1,
        "gold":           100000,
        "Gems":           100000,
        "DragonOre":      100000,
        "mammothIdols":   100000,
        "DragonKeys":     100000,
        "SilverSigils":   100000,
        "showHigher":     True,
        "MasterClass":    default_master_for_base(class_name),
        "inventoryGears": [
            {"gearID": 1, "tier": 1, "runes": [1, 2, 3], "colors": [255, 0]},
            {"gearID": 13, "tier": 2, "runes": [0, 0, 0], "colors": [0, 128]},
            {"gearID": 30, "tier": 0, "runes": [0, 0, 0], "colors": [0, 0]}
        ],
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
