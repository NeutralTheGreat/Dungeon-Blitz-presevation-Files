import json

from BitUtils import BitBuffer
from constants import Entity, class_7, class_20, class_3, Game, CLASS_NAME_TO_ID, class_118, SLOT_BIT_WIDTHS, \
    LinkUpdater, EntType, GearType, class_64, class_21, method_277, method_233
from typing import Dict, Any

def load_npc_data_for_level(level_name: str, json_path: str = r"data/npc_data.json") -> list:
    """
    Args:
        level_name (str): The level identifier (e.g., 'TutorialBoat').
        json_path (str): Path to the JSON file containing NPC data.

    Returns:
        list: List of dictionaries, each containing NPC data for the given level.
    """
    try:
        with open(json_path, 'r') as file:
            npc_data = json.load(file)
        return npc_data.get(level_name, [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading NPC data: {e}")
        return []

def scale_coordinates(x: float, y: float, z: float):
    """Convert floats to integers for method_45."""
    return int(x), int(y), int(z)

def Send_Entity_Data(entity: Dict[str, Any]) -> bytes:
    bb = BitBuffer(debug=True)

    # 1) Entity ID
    bb.write_method_4(entity['id'])

    # 2) Name
    bb.write_method_13(entity['name'])

    # 3) Player Appearance block
    if entity.get("hasCustomization", False):
        bb.write_bits(1, 1)  # send visuals block
        bb.write_method_13(entity.get("class", "Mage"))
        bb.write_method_13(entity.get("gender", ""))
        bb.write_method_13(entity.get("headSet", "basic"))
        bb.write_method_13(entity.get("hairSet", "short"))
        bb.write_method_13(entity.get("mouthSet", "default"))
        bb.write_method_13(entity.get("faceSet", "neutral"))
        bb.write_bits(entity.get("hairColor", 19940), 24)
        bb.write_bits(entity.get("skinColor", 16764057), 24)
        bb.write_bits(entity.get("shirtColor", 15263971), 24)
        bb.write_bits(entity.get("pantColor", 15263971), 24)
        equipped = entity.get('equippedGears', [])
        for slot in range(1, EntType.MAX_SLOTS):
            idx = slot - 1
            if idx < len(equipped) and equipped[idx] is not None:
                gear = equipped[idx]
                bb.write_bits(1, 1)
                bb.write_method_6(gear['gearID'], GearType.GEARTYPE_BITSTOSEND)
                bb.write_method_6(gear['tier'], GearType.const_176)
                runes = gear.get('runes', [0, 0, 0])
                bb.write_method_6(runes[0], class_64.const_101)
                bb.write_method_6(runes[1], class_64.const_101)
                bb.write_method_6(runes[2], class_64.const_101)
                colors = gear.get('colors', [0, 0])
                bb.write_method_6(colors[0], class_21.const_50)
                bb.write_method_6(colors[1], class_21.const_50)
            else:
                bb.write_bits(0, 1)

    else:
        bb.write_bits(0, 1)  # skip entire visuals section

    # 4) Position + rotation
    bb.write_signed_method_45(int(entity['x']))  # x
    bb.write_signed_method_45(int(entity['y']))  # y
    bb.write_signed_method_45(int(entity['z']))  # rotation
    # 4) team
    bb.write_method_6(entity.get('team', 0), Entity.TEAM_BITS)

    # TODO... im not sure where exactly but this branch is causing the bitstream to break
    #  leading to the player level reading wrong and some other things  if Player branches are off(False) the NPCs spawn properly
    #  (at least i think so...)
    # ── PLAYER VS NPC BRANCH ──
    if entity.get('is_player', False):
        # 5a) Signal “yes, player data follows”
        bb.write_bits(1, 1)

        # 5b) Player level (6 bits on client)
        bb.write_method_6(entity.get('PlayerLevel', 1), Entity.MAX_CHAR_LEVEL_BITS)

        # 5c)
        bb.write_method_6(entity.get('game_mode', 0), Game.const_209)

        # 5d) Talent‐points block
        talents = entity.get('talents', [])  # list of (node_index, points_spent)
        bb.write_bits(1 if talents else 0, 1)
        if talents:
            # client loops over const_43 slots
            for slot_index in range(class_118.const_43):
                matching = next((t for t in talents if t[0] == slot_index), None)
                bb.write_bits(1 if matching else 0, 1)
                if matching:
                    node_id, points = matching
                    # write tier modifier (computed client‐side via method_277)
                    tier = method_277(slot_index)
                    bb.write_method_6(tier, class_118.const_127)
                    # write “points minus one” (client adds back 1)
                    bb.write_method_6(points - 1, class_118.const_127)
    else:
        # 5a) NPCs skip the player block
        bb.write_bits(0, 1)

    bb.write_bits(1 if entity.get("untargetable", False) else 0, 1)

    bb.write_method_739(entity.get("render_depth_offset", 0))

    speed = entity.get("behavior_speed", 0.0)
    if speed > 0:
        bb.write_bits(1, 1)
        bb.write_method_4(int(speed * LinkUpdater.VELOCITY_INFLATE))
    else:
        bb.write_bits(0, 1)

    # 6) optional strings
    for key in ("level_str", "var_1958", "var_1879"):
        val = entity.get(key, "")
        bb.write_bits(1 if val else 0, 1)
        if val:
            bb.write_method_13(val)

    # 7) NPC Entity Level
    bb.write_bits(1, 1)
    bb.write_method_4(entity.get("NPClevel", 0))

    # 8) power type
    pid = entity.get("power_id", 0)
    bb.write_bits(1 if pid else 0, 1)
    if pid:
        bb.write_method_4(pid)

    # 9) entity state
    bb.write_method_6(entity.get("entState", 0), Entity.const_316)

    # 10) facing left
    bb.write_bits(1 if entity.get("facing_left", False) else 0, 1)

    # 11) HP delta
    bb.write_signed_method_45(entity.get("health_delta", 0))

    # ── MOUNTS & PETS ──
    # The client only reads mounts/pets if it saw the initial mount flag (Game.const_526)
    if entity.get('has_mount', False):
        bb.write_bits(1, 1)  # signal “mounts/pets follow”
        # mount flags (2 booleans), mount ID (7 bits), mount level (6 bits), mount type (7 bits)
        bb.write_bits(1 if entity.get('is_local_player', False) else 0, 1)
        bb.write_bits(1 if entity.get('uses_vanity_mount', False) else 0, 1)
        bb.write_method_6(entity.get('mount_id', 0), class_7.const_19)
        bb.write_method_6(entity.get('mount_level', 0), class_7.const_75)
        bb.write_method_6(entity.get('mount_type', 0), class_20.const_297)
        # pet-food slot (5 bits)
        bb.write_method_6(entity.get('petfood_slot', 0), class_3.const_69)

        # pets block
        pets = entity.get('pets', [])  # list of up to 3 (pet_id, pet_level)
        bb.write_bits(1 if pets else 0, 1)
        for pet in pets:
            bb.write_method_6(pet[0], class_7.const_19)
            bb.write_method_6(pet[1], class_7.const_75)
    else:
        bb.write_bits(0, 1)  # no mounts/pets

    # 12) buffs
    buffs = entity.get("buffs", [])
    bb.write_method_4(len(buffs))
    for buff in buffs:
        bb.write_method_4(buff.get("type_id", 0))
        bb.write_method_4(buff.get("param1", 0))
        bb.write_method_4(buff.get("param2", 0))
        bb.write_method_4(buff.get("param3", 0))
        bb.write_method_4(buff.get("param4", 0))

        extra = buff.get("extra_data", [])
        bb.write_bits(1 if extra else 0, 1)
        if extra:
            bb.write_method_4(len(extra))
            for ed in extra:
                bb.write_method_4(ed.get("id", 0))
                vals = ed.get("values", [])
                bb.write_method_4(len(vals))
                for v in vals:
                    bb.write_float(v)

    return bb.to_bytes()

