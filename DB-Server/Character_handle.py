
import os
import json
import struct
from BitUtils import BitBuffer

CHAR_FILE = "characters.json"

def load_characters():
    if not os.path.exists(CHAR_FILE):
        return []
    with open(CHAR_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_characters(char_list):
    with open(CHAR_FILE, "w", encoding="utf-8") as f:
        json.dump(char_list, f, ensure_ascii=False, indent=2)


def make_character_dict_from_tuple(character):
    (name, class_name, level,
     gender, head, hair, mouth, face,
     hair_color, skin_color, shirt_color, pant_color,
     equipped_gear) = character

    if isinstance(equipped_gear, (list, tuple)) and len(equipped_gear) == 6:
        gear_list = equipped_gear
    else:
        cls = class_name.lower()
        if cls == "paladin":
            gear_list = [902, 890, 912, 916, 909, 905]
        elif cls == "rogue":
            gear_list = [484, 379, 584, 676, 668, 577]
        elif cls == "mage":
            gear_list = [63, 151, 75, 68, 77, 70]
        else:
            gear_list = [0] * 6

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
        "gearList":   gear_list
    }

def build_paperdoll_packet(character_dict):
    from BitUtils import BitBuffer  # if BitBuffer is in another module
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

    for gear in character_dict.get("gearList", []):
        buf.write_bits(gear, 11)

    return buf.to_bytes()

def build_login_character_list_bitpacked(characters):
    from BitUtils import BitBuffer  # if BitBuffer is elsewhere
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

    payload = buf.to_bytes()
    import struct
    header = struct.pack(">HH", 0x15, len(payload))
    return header + payload
