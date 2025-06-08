# Character.py

import os
import json

CHAR_FILE = "characters.json"

def load_characters():
    if not os.path.exists(CHAR_FILE):
        return []
    with open(CHAR_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_characters(char_list):
    with open(CHAR_FILE, "w", encoding="utf-8") as f:
        json.dump(char_list, f, ensure_ascii=False, indent=2)

def default_master_for_base(base_cls: str) -> str:
    """Return the default “first” MasterClass name for a given base class."""
    # these must match the client’s class_150 mappings:
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
    """
    (name, class_name, level,
     gender, head, hair, mouth, face,
     hair_color, skin_color, shirt_color, pant_color,
     equipped_gear) = character

    # build gear_list (either the provided tuple or defaults per class)
    if isinstance(equipped_gear, (list, tuple)) and len(equipped_gear) == 6:
        gear_list = list(equipped_gear)
    else:
        cls = class_name.lower()
        if cls == "paladin":
            gear_list = [902, 890, 912, 916, 909, 905]
        elif cls == "rogue":
            gear_list = [1172, 1171, 1175, 1173, 1174, 1176]
        elif cls == "mage":
            gear_list = [1165, 1166, 1169, 0, 1168, 1170]
        else:
            gear_list = [0] * 6

    # Give every character a “MasterClass” field.  If there is no
    # pre‐existing “MasterClass” in the tuple, default to the first
    # tier (e.g. Sentinel for Paladin, Executioner for Rogue, Frostwarden for Mage).
    default_master = default_master_for_base(class_name)

    return {
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
        "gearList":   gear_list,

        # ── new persistent fields ───────────────────────────────
        "currGold":    0,
        "currGems":    0,
        "mCraftTalentData": 0,
        "mammothIdols":0,
        "extraField":  0,
        "showHigher":  False,
        "MasterClass": default_master
    }

def build_paperdoll_packet(character_dict):
    from BitUtils import BitBuffer
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

    # The client expects exactly six 11‐bit gear IDs in a row.
    for gear in character_dict.get("gearList", []):
        buf.write_bits(gear, 11)

    return buf.to_bytes()

def build_login_character_list_bitpacked(characters):
    from BitUtils import BitBuffer
    buf = BitBuffer()
    user_id = 1
    max_chars = 8
    char_count = len(characters)

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
