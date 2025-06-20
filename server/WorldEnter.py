# WorldEnter.py

from BitUtils import BitBuffer
import struct
import time
from constants import (
    GS_BITS,
    MAX_CHAR_LEVEL_BITS,
    Game_const_646,
    class_10_const_83,
    GearType,
    class_21_const_763,
    class_66_const_409,
    class_10_const_665,
    CLASS_NAME_TO_ID,
    ENTITY_CONST_244,
    class_64,
    class_9_const_28,
class_1_const_254,
class_64_const_499,
class_111_const_432,
var_238,
const_228
)


def Player_Data_Packet(char: dict,
                      event_index: int = 2,
                      transfer_token: int = 1,
                      scaling_factor: int = 0,
                      bonus_levels: int = 0) -> bytes:
    buf = BitBuffer()

    # ────────────── (1) Preamble ──────────────
    buf.write_method_4(transfer_token)  # _loc2_
    current_game_time = int(time.time())
    buf.write_method_4(current_game_time)  # _loc3_
    scaling_factor = max(0, min(scaling_factor, 3))  # Clamp to 0–3 (2-bit range)
    buf.write_method_6(scaling_factor, GS_BITS)  # _loc4_
    bonus_levels = max(0, min(bonus_levels, 0xFFFFFFFF))  # Clamp to uint32
    buf.write_method_4(bonus_levels)  # _loc5_

    # ────────────── (2) Customization ──────────────
    buf.write_utf_string(char.get("name", "") or "")
    buf._append_bits(1, 1)  # hasCustomization
    buf.write_utf_string(char.get("class", "") or "")
    buf.write_utf_string(char.get("gender", "") or "")
    buf.write_utf_string(char.get("headSet", "") or "")
    buf.write_utf_string(char.get("hairSet", "") or "")
    buf.write_utf_string(char.get("mouthSet", "") or "")
    buf.write_utf_string(char.get("faceSet", "") or "")
    buf._append_bits(char.get("hairColor", 0), 24)
    buf._append_bits(char.get("skinColor", 0), 24)
    buf._append_bits(char.get("shirtColor", 0), 24)
    buf._append_bits(char.get("pantColor", 0), 24)

    # ────────────── (3) Gear slots ──────────────
    gear_list = char.get("gearList", [[0] * 6] * 6)
    for slot in gear_list:
        gear_id, rune1, rune2, rune3, color1, color2 = slot
        if gear_id:
            buf._append_bits(1, 1)  # presence bit
            buf._append_bits(gear_id, 11)  # Gear ID (11 bits)
            buf._append_bits(0, 2)  # (reserved / flags)
            buf._append_bits(rune1, 16)
            buf._append_bits(rune2, 16)
            buf._append_bits(rune3, 16)
            buf._append_bits(color1, 8)
            buf._append_bits(color2, 8)
        else:
            buf._append_bits(0, 1)  # no item in this slot

    # ────────────── (4) Numeric fields ──────────────
    char_level = char.get("level", 1) or 1
    buf.write_method_6(char_level, MAX_CHAR_LEVEL_BITS)
    buf.write_method_4(char.get("xp", 0))  # xp
    buf.write_method_4(char.get("gold", 0))  # gold
    buf.write_method_4(char.get("Gems", 0))  # Gems
    buf.write_method_4(char.get("DragonOre", 0))  # DragonOre
    buf.write_method_4(char.get("mammothIdols", 0))  # mammoth idols
    buf._append_bits(int(char.get("showHigher", True)), 1)

    # ────────────── (5) Quest-tracker ──────────────
    quest_val = char.get("questTrackerState", None)
    if quest_val is not None:
        buf._append_bits(1, 1)
        buf.write_method_4(quest_val)
    else:
        buf._append_bits(0, 1)

    # ────────────── (6) Position‐presence ──────────────
    buf._append_bits(0, 1)  # no door/teleport update

    # ────────────── (7) Extended‐data‐presence ──────────────
    buf._append_bits(1, 1)  # yes, sending extended data

    # ────────────── (8) Extended data block ──────────────
    # Inventory Gears
    inventory_gears = char.get("inventoryGears", [])
    buf.write_method_6(len(inventory_gears), GearType.GEARTYPE_BITSTOSEND)  # Number of gears (11 bits)
    for gear in inventory_gears:
        gear_id = gear.get("gearID", 0)
        tier = gear.get("tier", 0)
        runes = gear.get("runes", [0, 0, 0])
        colors = gear.get("colors", [0, 0])

        buf._append_bits(gear_id, 11)  # Gear ID (11 bits)
        buf._append_bits(tier, GearType.const_176)  # Tier (2 bits)

        has_modifiers = any(rune != 0 for rune in runes) or any(color != 0 for color in colors)
        buf._append_bits(1 if has_modifiers else 0, 1)  # has_modifiers bit

        if has_modifiers:
            for i in range(3):
                rune = runes[i]
                rune_present = rune != 0
                buf._append_bits(1 if rune_present else 0, 1)
                if rune_present:
                    buf._append_bits(rune, 16)  # Rune ID (16 bits)
            for i in range(2):
                color = colors[i]
                color_present = color != 0
                buf._append_bits(1 if color_present else 0, 1)
                if color_present:
                    buf._append_bits(color, 8)  # Color value (8 bits)

    # Gear Sets
    gear_sets = char.get("gearSets", [])
    buf.write_method_6(len(gear_sets), GearType.const_348)
    for gs in gear_sets:
        buf.write_utf_string(gs.get("name", ""))
        slots = gs.get("slots", [])
        slots = (slots + [0] * 6)[:6]  # pad/truncate to 6
        for gear_id in slots:
            buf._append_bits(gear_id, GearType.GEARTYPE_BITSTOSEND)

    buf._append_bits(0, 1)  # no keybinds

    # Mounts
    mounts = char.get("mounts", [])
    buf.write_method_4(len(mounts))  # Number of mounts
    for mount_id in mounts:
        buf.write_method_4(mount_id)

    # Pets
    pets = char.get("pets", [])
    buf.write_method_4(len(pets))  # Number of pets
    for pet in pets:
        type_id = pet.get("typeID", 0)
        iteration = pet.get("level", 0)
        attr1 = pet.get("xp", 0)
        attr2 = pet.get("attr2", 0)
        type_id = max(0, min(type_id, 127))
        iteration = max(0, min(iteration, 63))
        buf.write_method_6(type_id, 7)  # Type ID (7 bits)
        buf.write_method_6(iteration, 6)  # Iteration (6 bits)
        buf.write_method_4(attr1)  # Attribute 1
        buf.write_method_4(attr2)  # Attribute 2

    # Charms
    charms = char.get("charms", [])
    for charm in charms:
        charm_id = charm.get("charmID", 0)
        count = charm.get("count", 1)
        buf._append_bits(1, 1)
        buf._append_bits(charm_id, class_64.const_101)
        if count != 1:
            buf._append_bits(1, 1)
            buf.write_method_4(count)
        else:
            buf._append_bits(0, 1)
    buf._append_bits(0, 1)  # no more charms

    # Materials
    materials = char.get("materials", [])
    for mat in materials:
        mat_id = mat.get("materialID", 0)
        count = mat.get("count", 1)
        buf._append_bits(1, 1)
        buf.write_method_4(mat_id)
        if count != 1:
            buf._append_bits(1, 1)
            buf.write_method_4(count)
        else:
            buf._append_bits(0, 1)
    buf._append_bits(0, 1)  # no more materials

    # Lockboxes
    lockboxes = char.get("lockboxes", [])
    for box in lockboxes:
        box_id = box.get("lockboxID", 0)
        count = box.get("count", 1)
        buf._append_bits(1, 1)
        buf.write_method_4(box_id)
        buf.write_method_4(count)
    buf._append_bits(0, 1)  # no more lockboxes

    buf.write_method_4(char.get("DragonKeys", 0))  # lockboxKeys
    buf.write_method_4(char.get("SilverSigils", 0))  # royalSigils
    buf.write_method_6(1, Game_const_646)  # alert state = 0
    for _ in range(1, class_21_const_763 + 1):  # dyes
        buf._append_bits(1, 1)
    consumables = char.get("consumables", [])
    for item in consumables:
        cid = item.get("consumableID", 0)
        count = item.get("count", 1)
        buf._append_bits(1, 1)
        buf.write_method_4(cid)
        buf.write_method_4(count)
    buf._append_bits(0, 1)  # no more consumables

    # ────────────── (5) Mission-tracker ──────────────
    #buf.write_method_4(0)
    missions = char.get("missions", {})

    # 1) total number of mission definitions
    total_defs = len(var_238) - 1
    buf.write_method_4(total_defs)

    # 2) for each mission ID, in order
    for mid in range(1, total_defs + 1):
        mdef = var_238[mid]
        mstate = missions.get(mid)

        # outer “do I have any state for this mission?”
        has_state = mstate is not None
        buf._append_bits(1 if has_state else 0, 1)
        if not has_state:
            continue

        # one‐shot missions just stop here
        if mdef.var_1775:
            continue

        # inner boolean #1: ready to turn in vs in-progress
        ready = (mstate.get("state") == 2)  # Mission.const_72 == 2
        buf._append_bits(1 if ready else 0, 1)

        if not ready:
            # in-progress: write currCount if mdef.var_908 > 1
            if mdef.var_908 > 1:
                buf.write_method_4(mstate.get("currCount", 0))
        else:
            # completed: inner boolean #2 → reward claimed?
            claimed = (mstate.get("state") == 1)  # Mission.const_58 == 1
            buf._append_bits(1 if claimed else 0, 1)

            # if timed mission, write the three extra fields
            if mdef.var_134:
                buf._append_bits(mstate.get("var_588", 0), const_228)
                buf.write_method_4(mstate.get("var_1745", 0))
                buf.write_method_4(mstate.get("var_2806", 0))

    # Friends
    friends = char.get("friends", [])
    buf.write_method_4(len(friends))  # count
    for f in friends:
        buf.write_utf_string(f["name"])
        buf._append_bits(1 if f.get("isRequest", False) else 0, 1)
        online = f.get("isOnline", False)
        buf._append_bits(1 if online else 0, 1)
        if online:
            custom_name = f.get("charName", "") != f["name"]
            buf._append_bits(1 if custom_name else 0, 1)
            if custom_name:
                buf.write_utf_string(f["charName"])
            cls_id = CLASS_NAME_TO_ID.get(f.get("className", ""), 0)
            buf._append_bits(cls_id, ENTITY_CONST_244)
            buf._append_bits(f.get("level", 1), MAX_CHAR_LEVEL_BITS)

    # Learned Abilities
    learned_abilities = char.get("learnedAbilities", [])
    buf.write_method_6(len(learned_abilities), class_10_const_83)
    for ability in learned_abilities:
        ability_id = ability.get("abilityID", 0)
        rank = ability.get("rank", 0)
        buf.write_method_6(ability_id, class_10_const_83)
        buf.write_method_6(rank, class_10_const_665)

    active_slots = char.get("activeAbilities", [0, 0, 0])
    while len(active_slots) < 3:
        active_slots.append(0)
    for slot_id in active_slots[:3]:
        buf.write_method_6(slot_id, class_10_const_83)

    buf.write_method_4(0)  # craft talent
    buf.write_method_6(0, class_66_const_409)  # tower A
    buf.write_method_6(0, class_66_const_409)  # tower B
    buf.write_method_6(0, class_66_const_409)  # tower C

    # Magic Forge
    mf = char.get("magicForge", {})
    buf._append_bits(1 if mf.get("stats") else 0, 1)
    if not mf.get("stats"):
        pass
    else:
        for val in mf["stats"]:
            buf._append_bits(val, class_9_const_28)
        if not mf.get("hasSession", False):
            buf._append_bits(0, 1)
        else:
            buf._append_bits(1, 1)
            buf._append_bits(mf.get("primary", 0), class_1_const_254)
            status = mf.get("status", "idle")
            if status == "inProgress":
                buf._append_bits(1, 1)
                buf.write_method_4(mf.get("endTime", 0))
            else:
                buf._append_bits(0, 1)
                mod_id = mf.get("modSlotID", 0)
                buf._append_bits(mod_id, class_64_const_499)
                if mod_id:
                    buf._append_bits(mf.get("modTier", 0), class_64_const_499)
                    buf._append_bits(mf.get("usedList", 0), class_111_const_432)
            buf._append_bits(1 if mf.get("flagA", False) else 0, 1)
            buf._append_bits(1 if mf.get("flagB", False) else 0, 1)
    """
    buf._append_bits(0, 1)  # no ability research
    buf._append_bits(0, 1)  # no building info
    buf._append_bits(0, 1)  # no tower research
    buf._append_bits(0, 1)  # no egg/pet data
    buf.write_method_6(0, class_16_const_167)  # pet count = 0
    buf._append_bits(0, 1)
    buf._append_bits(0, 1)
    buf._append_bits(0, 1)
    buf._append_bits(0, 1)
   
    # ────────────── NEWS ──────────────
    buf.write_method_6(0, 2)
    # Select event: prefer char["active_news_event"] if set, else use event_index
    news_event_id = char.get("active_news_event", event_index)
    # Validate news_event_id (0–5, where 0 means no event)
    news_event_id = news_event_id if news_event_id in NEWS_EVENTS else 0

    if news_event_id in NEWS_EVENTS:
        event = NEWS_EVENTS[news_event_id]
        buf.write_utf_string(event["icon"])       # _loc66_
        buf.write_utf_string(event["url"])        # _loc67_
        buf.write_utf_string(event["title"])      # _loc68_
        buf.write_utf_string(event["description"]) # _loc69_
        buf.write_method_4(event["end_time"])    # _loc70_
    else:
        # No active event
        buf.write_utf_string("")  # _loc66_
        buf.write_utf_string("")  # _loc67_
        buf.write_utf_string("")  # _loc68_
        buf.write_utf_string("")  # _loc69_
        buf.write_method_4(0)    # _loc70_

    # ───────── (X) Specialization (_loc33_) ─────────
    spec_id = _MASTERCLASS_TO_ID.get(char.get("masterClass", ""), 0)
    buf._append_bits(spec_id, GAME_CONST_209)
    has_spec = spec_id != 0
    buf._append_bits(1 if has_spec else 0, 1)
    if has_spec:
        for i in range(CLASS_118_CONST_43):
            has_pt = char.get("specPoints", {}).get(i, False)
            buf._append_bits(1 if has_pt else 0, 1)
            if has_pt:
                buf._append_bits(char["rankIncrements"][i], CLASS_118_CONST_127)
                buf._append_bits(char["currentRanks"][i], master_bits_for_slot(i))

    # ───────── (Y) Equipped gear slots (_loc150_) ─────────
    for slot in range(1, ENT_MAX_SLOTS):
        gid = char.get("gearList", [[0] * 6] * ENT_MAX_SLOTS)[slot - 1][0]
        buf._append_bits(1 if gid else 0, 1)
        if gid:
            buf._append_bits(gid, GearType.GEARTYPE_BITSTOSEND)

    # ───────── (Z) Mount, pet, buff & potion (_loc37_, _loc39_, _loc40_, _loc42_, _loc43_) ─────────
    buf.write_method_4(char.get("equippedMountID", 0))
    buf.write_method_4(char.get("activePetID", 0))
    buf.write_method_4(char.get("activePetIteration", 0))
    buf.write_method_4(char.get("currentBuffTypeID", 0))
    buf.write_method_4(char.get("queuedPotionTypeID", 0))

    # ───────── (A) Friends update (method_933) ─────────
    friends = char.get("friends", [])
    buf._append_bits(1 if friends else 0, 1)
    if friends:
        buf.write_utf_string(char.get("friendHeader", ""))
        buf._append_bits(char.get("friendStateVersion", 0), Entity_const_172)
        buf.write_method_4(len(friends))
        for f in friends:
            buf.write_utf_string(f["name"])
            cls_id = CLASS_NAME_TO_ID.get(f.get("className", ""), 0)
            buf._append_bits(cls_id, ENTITY_CONST_244)
            buf._append_bits(f.get("level", 1), MAX_CHAR_LEVEL_BITS)
            buf._append_bits(f.get("stateVersion", 0), Entity_const_172)

    # Level data (_loc46_)
    levels = char.get("knownLevels", [{"name": "NewbieRoad", "swf": "LevelsNR.swf/a_Level_NewbieRoad"}])
    buf.write_method_4(len(levels))
    for lvl in levels:
        buf.write_utf_string(lvl["name"])
        buf.write_utf_string(lvl["swf"])

    # Room data (_loc47_)
    rooms = char.get("knownRooms", [{"id": 0, "name": "Room_Main", "type": "Main"}])
    buf.write_method_4(len(rooms))
    for room in rooms:
        buf.write_method_4(room["id"])
        buf.write_utf_string(room["name"])
        buf.write_utf_string(room["type"])

    # ────────────── (48) Collision geometry ──────────────
    geom = char.get("geometry", [])
    buf.write_method_4(len(geom))          # segmentCount
    for seg in geom:
        buf.write_method_4(seg["x1"])
        buf.write_method_4(seg["y1"])
        buf.write_method_4(seg["x2"])
        buf.write_method_4(seg["y2"])
        buf.write_method_4(seg["type"])
        buf.write_method_4(seg["flags"])
        tags = seg.get("tags", [])
        buf.write_method_4(len(tags))
        for tag in tags:
            buf.write_utf_string(tag)
        buf._append_bits(seg["roomId"], 4)
        buf.write_method_4(seg.get("extra1", 0))
        buf.write_method_4(seg.get("extra2", 0))

     """
    payload = buf.to_bytes()
    return struct.pack(">HH", 0x10, len(payload)) + payload


def build_enter_world_packet(
        transfer_token: int,
        old_level_id: int,
        old_swf: str,
        has_old_coord: bool,
        old_x: int,
        old_y: int,
        old_flashvars: str,
        user_id: int,
        new_level_swf: str,
        new_map_lvl: int,
        new_base_lvl: int,
        new_internal: str,
        new_moment: str,
        new_alter: str,
        new_is_inst: bool
) -> bytes:
    buf = BitBuffer()

    # 1) transferToken + oldLevelId
    buf.write_method_4(transfer_token)
    buf.write_method_4(old_level_id)

    # 2) old SWF path
    buf.write_utf_string(old_swf)

    # 3) old coords?
    buf._append_bits(1 if has_old_coord else 0, 1)
    if has_old_coord:
        buf.write_method_4(old_x)
        buf.write_method_4(old_y)

    # 4) old flashVars
    buf.write_utf_string(old_flashvars)

    # 5) userID
    buf.write_method_4(user_id)

    # 6) new SWF path
    buf.write_utf_string(new_level_swf)

    # 7) map/base levels (6 bits each)
    buf.write_method_6(new_map_lvl, 6)
    buf.write_method_6(new_base_lvl, 6)

    # 8) new strings
    buf.write_utf_string(new_internal)
    buf.write_utf_string(new_moment)
    buf.write_utf_string(new_alter)

    # 9) new isInstanced
    buf._append_bits(1 if new_is_inst else 0, 1)

    payload = buf.to_bytes()
    return struct.pack(">HH", 0x21, len(payload)) + payload
