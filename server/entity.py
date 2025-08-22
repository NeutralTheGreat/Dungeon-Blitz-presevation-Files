import json
import os

from BitUtils import BitBuffer
from constants import Entity, class_7, class_20, class_3, Game, class_118, \
    LinkUpdater, EntType, GearType, class_64, class_21, method_277
from typing import Dict, Any

npc_cache = {}

"""
Hints NPCs data 
[
    {
      "id": 3,
      "name": "NPCRuggedVillager02",
      "x": 3317,
      "y": 461,
      "v": 0,
      "team": 3,
      "untargetable": false,
      "render_depth_offset": -15,
      "behavior_speed": 0.0,
      "Linked_Mission": "NR_Mayor01", 
      "DramaAnim": "",
      "SleepAnim": "",
      "NPClevel": 0,
      "power_id": 0,
      "entState": 0,
      "facing_left": true,
      "health_delta": 0,
      "buffs": []
    }
]

======== Intercatible NPCs Tips =====================
- how to make the NPC interactable by the player
- NPC will only become interactable if they have a "Linked_Mission" set and  "team" set to 3 

- look at the "MissionTypes.Json" for these 2 lines on each mission : 

"ContactName": "CaptainFink",
"ReturnName": "NR_Mayor01", 

For example the NPC with the "Linked_Mission": "NR_Mayor01",  will be linked to all the missions that have "ReturnName": "NR_Mayor01",  OR "ContactName": "NR_Mayor01",

- this will also show the NPCs name under his feet "NR_Mayor01" is "Mayor Ristas"


===============


Team Types : 

 const_531:uint = 0; # team type will be automatically chosen  its  used for a entity called "EmberBush" :/ but it will also give any other NPC team 2 (enemies)
      
 GOODGUY:uint = 1; #  players 
      
 BADGUY:uint = 2; # Enemies 
      
 NEUTRAL:uint = 3; # Friendly NPC
 
 
entState : 
 
 0 = Active State
 
 1 = Sleep State
 
 2 = Drama State (used during cutscenes most likely) this will put the entity to sleep also make them untargetable 
 
 3 = Entity Dies when the game loads 
 
 
 
 =============== how to use "DramaAnim" and "SleepAnim" ===============
 
 for "DramaAnim" to activate you have to set the "entState" to 2  
 
 for "SleepAnim" to activate you have to set the "entState" to 1 
 
 you can find which entity uses "DramaAnim" and "SleepAnim" at EntTypes.json some entities have "DramaAnim" or "SleepAnim" defined 
 
 Example : 
      
     # goblin will spawn in the boarding ship animation 
     {
      "name": "IntroGoblinJumper",
      "DramaAnim": "board",
      "SleepAnim": "",
      "entState": 2,
    }
    
    # the eye will spawn closed 
    {
      "name": "NephitCrownEye",
      "DramaAnim": "Sleep",
      "SleepAnim": "",
      "entState": 1,
    }

"""


def load_npc_data_for_level(level_name: str) -> list:
    """
    Args:
        level_name (str): The level identifier (e.g., 'TutorialBoat').

    Returns:
        list: List of dictionaries, each containing NPC data for the given level.
    """
    json_path = os.path.join("NPC_Data", f"{level_name}.json")
    try:
        with open(json_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading NPC data for {level_name}: {e}")
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
    if entity.get("is_player", False):
        bb.write_bits(1, 1)  # send visuals block
        bb.write_method_13(entity.get("class", ""))
        bb.write_method_13(entity.get("gender", ""))
        bb.write_method_13(entity.get("headSet", ""))
        bb.write_method_13(entity.get("hairSet", ""))
        bb.write_method_13(entity.get("mouthSet", ""))
        bb.write_method_13(entity.get("faceSet", ""))
        bb.write_bits(entity.get("hairColor", 0), 24)
        bb.write_bits(entity.get("skinColor", 0), 24)
        bb.write_bits(entity.get("shirtColor", 0), 24)
        bb.write_bits(entity.get("pantColor", 0), 24)
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

    # 4) Position + Velocity
    bb.write_signed_method_45(int(entity['x']))  # x
    bb.write_signed_method_45(int(entity['y']))  # y
    bb.write_signed_method_45(int(entity['v']))  # Velocity
    # 4) team
    bb.write_method_6(entity.get('team', 0), Entity.TEAM_BITS)

    # TODO... im not sure where exactly but this branch is causing the bitstream to break
    #  leading to the player level reading wrong and some other things  if Player branches are off(False) the NPCs spawn properly
    #  (at least i think so...)
    # ── PLAYER VS NPC BRANCH ──
    if entity.get("is_player", False):
        # 5a) Signal “yes, player data follows”
        bb.write_bits(1, 1)

        # 5b) Player level (6 bits on client)
        bb.write_method_6(entity.get('PlayerLevel', 0), Entity.MAX_CHAR_LEVEL_BITS)

        # 5c)
        bb.write_method_6(entity.get('game_mode', 0), Game.const_209)

        # 5d) Talent‐points block
        talents = entity.get('talents', [])  # list of (node_index, points_spent)
        bb.write_bits(1 if talents else 0, 1)
        if talents:
            # client loops over const_43 slots
            for slot_index in range(class_118.NUM_TALENT_SLOTS):
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

    speed = entity.get("behavior_speed", 0)
    if speed > 0:
        bb.write_bits(1, 1)
        bb.write_method_4(int(speed * LinkUpdater.VELOCITY_INFLATE))
    else:
        bb.write_bits(0, 1)


    for key in ("Linked_Mission", "DramaAnim", "SleepAnim"):
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
    value = int(round(entity.get("health_delta", 0)))
    bb.write_signed_method_45(value)

    #this is likely meant to be used when a player has a mount or a pet equipped
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
            bb.write_method_6(pet[0], class_7.const_75)
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

