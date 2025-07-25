import json

from BitUtils import BitBuffer
from constants import Entity, class_7, class_20, class_3, Game, CLASS_NAME_TO_ID, class_118, SLOT_BIT_WIDTHS, \
    LinkUpdater
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

def Send_Entity_Data(entity: Dict[str, Any], is_player: bool = False) -> bytes:
    bb = BitBuffer(debug=False)
    #print("Send_Entity_Data: Starting packet construction")

    # Core Header
    entity_id = entity.get("id", 0)
    bb.write_method_4(entity_id)
    #print(f"Send_Entity_Data: Wrote entity ID: {entity_id}")

    entity_name = entity.get("name", "")
    bb.write_method_13(entity_name)
    #print(f"Send_Entity_Data: Wrote entity name: {entity_name}")

    has_appearance = is_player  # Enable for players
    bb.write_bits(1 if has_appearance else 0, 1)
    if has_appearance:
        bb.write_method_13(entity.get("class", "Paladin"))
        bb.write_method_13(entity.get("headSet", "Head01"))
        bb.write_method_13(entity.get("hairSet", "Hair01"))
        bb.write_method_13(entity.get("mouthSet", "Mouth01"))
        bb.write_method_13(entity.get("faceSet", "Face01"))
        bb.write_method_13("")  # Additional string (placeholder)
        bb.write_bits(entity.get("hairColor", 0), 24)
        bb.write_bits(entity.get("skinColor", 0), 24)
        bb.write_bits(entity.get("shirtColor", 0), 24)
        bb.write_bits(entity.get("pantColor", 0), 24)
        # Gear slots (6 slots)
        equipped_gears = entity.get("equippedGears", [[0, 0, 0, 0, 0, 0]] * 6)
        for slot in range(6):
            gear = equipped_gears[slot] if slot < len(equipped_gears) else [0, 0, 0, 0, 0, 0]
            gear_id = gear[0]
            bb.write_bits(1 if gear_id != 0 else 0, 1)
            if gear_id != 0:
                bb.write_bits(gear_id, 11)  # GearID
                bb.write_bits(gear[1], 8)  # Rune1
                bb.write_bits(gear[2], 8)  # Rune2
                bb.write_bits(gear[3], 8)  # Rune3
                bb.write_bits(gear[4], 8)  # Color1
                bb.write_bits(gear[5], 8)  # Color2

    # Coordinates
    x_scaled, y_scaled, z_scaled = scale_coordinates(
        entity.get("x", 0.0), entity.get("y", 0.0), entity.get("z", 0.0)
    )
    bb.write_signed_method_45(x_scaled)
    #print(f"Send_Entity_Data: Wrote X coordinate: {x_scaled}")
    bb.write_signed_method_45(y_scaled)
    #print(f"Send_Entity_Data: Wrote Y coordinate: {y_scaled}")
    bb.write_signed_method_45(z_scaled)
    #print(f"Send_Entity_Data: Wrote Z coordinate: {z_scaled}")

    # Team Bits
    team = entity.get("team", 0)
    bb.write_method_6(team, Entity.TEAM_BITS)
    #print(f"Send_Entity_Data: Wrote team bits: {team}")

    # Entity Type and Related Data
    if is_player:
        #print("Send_Entity_Data: Entity is a player")
        bb.write_bits(1, 1)  # Player flag
        bb.write_bits(entity.get("flag1", False), 1)
        #print(f"Send_Entity_Data: Wrote player flag1: {entity.get('flag1', False)}")
        bb.write_bits(entity.get("flag2", False), 1)
        #print(f"Send_Entity_Data: Wrote player flag2: {entity.get('flag2', False)}")
        bb.write_method_6(entity.get("player_data1", 0), class_7.const_19)
        #print(f"Send_Entity_Data: Wrote player data1: {entity.get('player_data1', 0)}")
        bb.write_method_6(entity.get("player_data2", 0), class_7.const_75)
        #print(f"Send_Entity_Data: Wrote player data2: {entity.get('player_data2', 0)}")
        bb.write_method_6(entity.get("mount_data", 0), class_20.const_297)
        #print(f"Send_Entity_Data: Wrote mount data: {entity.get('mount_data', 0)}")
        bb.write_method_6(entity.get("additional_data", 0), class_3.const_69)
        #print(f"Send_Entity_Data: Wrote additional data: {entity.get('additional_data', 0)}")

        has_additional = entity.get("has_additional_player_data", False)
        bb.write_bits(1 if has_additional else 0, 1)
        #print(f"Send_Entity_Data: Wrote additional player data flag: {has_additional}")
        if has_additional:
            bb.write_method_6(entity.get("extra_data1", 0), class_7.const_19)
            #print(f"Send_Entity_Data: Wrote extra player data1: {entity.get('extra_data1', 0)}")
            bb.write_method_6(entity.get("extra_data2", 0), class_7.const_75)
            #print(f"Send_Entity_Data: Wrote extra player data2: {entity.get('extra_data2', 0)}")
            bb.write_method_6(entity.get("extra_data3", 0), class_7.const_19)
            #print(f"Send_Entity_Data: Wrote extra player data3: {entity.get('extra_data3', 0)}")
            bb.write_method_6(entity.get("extra_data4", 0), class_7.const_75)
            #print(f"Send_Entity_Data: Wrote extra player data4: {entity.get('extra_data4', 0)}")
            bb.write_method_6(entity.get("extra_data5", 0), class_7.const_19)
            #print(f"Send_Entity_Data: Wrote extra player data5: {entity.get('extra_data5', 0)}")
            bb.write_method_6(entity.get("extra_data6", 0), class_7.const_75)
            #print(f"Send_Entity_Data: Wrote extra player data6: {entity.get('extra_data6', 0)}")
    else:
        #print("Send_Entity_Data: Entity is not a player")
        bb.write_bits(0, 1)  # Not a player
        untargetable = entity.get("untargetable", False)
        bb.write_bits(1 if untargetable else 0, 1)
        #print(f"Send_Entity_Data: Wrote untargetable flag: {untargetable}")
        bb.write_method_739(entity.get("behavior_id", 0))
        #print(f"Send_Entity_Data: Wrote behavior ID: {entity.get('behavior_id', 0)}")
        behavior_speed = entity.get("behavior_speed", 0.0)
        bb.write_bits(1 if behavior_speed > 0 else 0, 1)
        #print(f"Send_Entity_Data: Wrote behavior speed flag: {1 if behavior_speed > 0 else 0}")
        if behavior_speed > 0:
            scaled_speed = int(behavior_speed * LinkUpdater.VELOCITY_INFLATE)
            bb.write_method_4(scaled_speed)
            #print(f"Send_Entity_Data: Wrote scaled behavior speed: {scaled_speed}")

    # Optional Strings
    level_str = entity.get("level_str", "")
    bb.write_bits(1 if level_str else 0, 1)
    #print(f"Send_Entity_Data: Wrote level string flag: {1 if level_str else 0}")
    if level_str:
        bb.write_method_13(level_str)
        #print(f"Send_Entity_Data: Wrote level string: {level_str}")

    var_1958 = entity.get("var_1958", "")
    bb.write_bits(1 if var_1958 else 0, 1)
    #print(f"Send_Entity_Data: Wrote var_1958 flag: {1 if var_1958 else 0}")
    if var_1958:
        bb.write_method_13(var_1958)
        #print(f"Send_Entity_Data: Wrote var_1958: {var_1958}")

    var_1879 = entity.get("var_1879", "")
    bb.write_bits(1 if var_1879 else 0, 1)
    #print(f"Send_Entity_Data: Wrote var_1879 flag: {1 if var_1879 else 0}")
    if var_1879:
        bb.write_method_13(var_1879)
        #print(f"Send_Entity_Data: Wrote var_1879: {var_1879}")

    # Level and Power Type
    level = entity.get("level", 0)
    bb.write_bits(1 if level > 0 else 0, 1)
    #print(f"Send_Entity_Data: Wrote level flag: {1 if level > 0 else 0}")
    if level > 0:
        bb.write_method_4(level)
        #print(f"Send_Entity_Data: Wrote level: {level}")

    power_id = entity.get("power_id", 0)
    bb.write_bits(1 if power_id > 0 else 0, 1)
    #print(f"Send_Entity_Data: Wrote power ID flag: {1 if power_id > 0 else 0}")
    if power_id > 0:
        bb.write_method_4(power_id)
        #print(f"Send_Entity_Data: Wrote power ID: {power_id}")

    # Entity State and Facing
    ent_state = entity.get("entState", Entity.const_6)
    bb.write_method_6(ent_state, Entity.const_316)
    #print(f"Send_Entity_Data: Wrote entity state: {ent_state}")

    facing_left = entity.get("facing_left", False)
    bb.write_bits(1 if facing_left else 0, 1)
    #print(f"Send_Entity_Data: Wrote facing left: {facing_left}")

    # Player-Specific Equipment
    if is_player:
        #print("Send_Entity_Data: Processing player equipment")
        player_level = entity.get("player_level", 0)
        bb.write_method_6(player_level, Entity.MAX_CHAR_LEVEL_BITS)
        #print(f"Send_Entity_Data: Wrote player level: {player_level}")

        game_const = entity.get("game_const", Game.const_526)
        bb.write_method_6(game_const, Game.const_209)
        #print(f"Send_Entity_Data: Wrote game constant: {game_const}")

        has_equipment = entity.get("has_equipment", False)
        bb.write_bits(1 if has_equipment else 0, 1)
        #print(f"Send_Entity_Data: Wrote equipment flag: {has_equipment}")

        if has_equipment:
            #print("Send_Entity_Data: Writing equipment data")
            class_type = entity.get("class_type", "")
            class_id = CLASS_NAME_TO_ID.get(class_type, 0)
            for slot in range(class_118.const_43):
                equipment = entity.get("equipment", {}).get(str(slot), None)
                if equipment:
                    #print(f"Send_Entity_Data: Equipment present in slot {slot}")
                    slot_index = SLOT_BIT_WIDTHS(slot)
                    bb.write_bits(1, 1)
                    #print(f"Send_Entity_Data: Wrote equipment flag for slot {slot}: 1")
                    bb.write_method_6(equipment.get("index", 0), class_118.const_127)
                    #print(f"Send_Entity_Data: Wrote equipment index for slot {slot}: {equipment.get('index', 0)}")
                    value = 1 + equipment.get("value", 0)
                    bb.write_method_6(value, slot_index)
                    #print(f"Send_Entity_Data: Wrote equipment value for slot {slot}: {value}")
                else:
                    bb.write_bits(0, 1)
                    #print(f"Send_Entity_Data: Wrote equipment flag for slot {slot}: 0")

    # Health Adjustment
    health_delta = entity.get("health_delta", 0)
    bb.write_signed_method_45(health_delta)
    #print(f"Send_Entity_Data: Wrote health delta: {health_delta}")

    # Buffs
    buffs = entity.get("buffs", [])
    bb.write_method_4(len(buffs))
    #print(f"Send_Entity_Data: Wrote number of buffs: {len(buffs)}")

    for i, buff in enumerate(buffs):
        #print(f"Send_Entity_Data: Processing buff {i}")
        bb.write_method_4(buff.get("type_id", 0))
        #print(f"Send_Entity_Data: Wrote buff type ID: {buff.get('type_id', 0)}")
        bb.write_method_4(buff.get("param1", 0))
        #print(f"Send_Entity_Data: Wrote buff param1: {buff.get('param1', 0)}")
        bb.write_method_4(buff.get("param2", 0))
        #print(f"Send_Entity_Data: Wrote buff param2: {buff.get('param2', 0)}")
        bb.write_method_4(buff.get("param3", 0))
        #print(f"Send_Entity_Data: Wrote buff param3: {buff.get('param3', 0)}")
        bb.write_method_4(buff.get("param4", 0))
        #print(f"Send_Entity_Data: Wrote buff param4: {buff.get('param4', 0)}")

        extra_data = buff.get("extra_data", [])
        has_extra = len(extra_data) > 0
        bb.write_bits(1 if has_extra else 0, 1)
        #print(f"Send_Entity_Data: Wrote extra data flag for buff {i}: {has_extra}")

        if has_extra:
            bb.write_method_4(len(extra_data))
            #print(f"Send_Entity_Data: Wrote number of extra data entries for buff {i}: {len(extra_data)}")
            for j, data in enumerate(extra_data):
                #print(f"Send_Entity_Data: Processing extra data {j} for buff {i}")
                bb.write_method_4(data.get("id", 0))
                #print(f"Send_Entity_Data: Wrote extra data ID: {data.get('id', 0)}")
                values = data.get("values", [])
                bb.write_method_4(len(values))
                #print(f"Send_Entity_Data: Wrote number of values for extra data {j}: {len(values)}")
                for k, value in enumerate(values):
                    bb.write_float(value)
                    #print(f"Send_Entity_Data: Wrote value {k} for extra data {j}: {value}")

    # Finalize Packet
    payload = bb.to_bytes()
    #print(f"Send_Entity_Data: Finalized payload, length: {len(payload)} bytes")
    #print(f"Send_Entity_Data: Debug log: {bb.get_debug_log()}")
    return payload