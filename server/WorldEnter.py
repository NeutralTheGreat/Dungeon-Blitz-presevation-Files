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
    class_10_const_665,
    CLASS_NAME_TO_ID,
    ENTITY_CONST_244,
    class_64,
    class_9_const_28,
    class_1_const_254,
    class_64_const_499,
    class_111_const_432,
    class_64_const_218,
class_9_const_129,
class_66_const_571,
class_16_const_167,
class_7_const_19,
NEWS_EVENTS,
GAME_CONST_209,
CLASS_118_CONST_127,
SLOT_BIT_WIDTHS,
NUM_TALENT_SLOTS,
EntType_MAX_SLOTS,
GEARTYPE_BITS,
Mission,
class_119

)
from missions import var_238
def Player_Data_Packet(char: dict,
                      event_index: int = 1,
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

    # ────────────── (3) Gear Slots ──────────────
    gear_list = char.get("equippedGears", [])
    for gear in gear_list:
        gear_id = gear.get("gearID", 0)
        rune1, rune2, rune3 = gear.get("runes", [0, 0, 0])
        color1, color2 = gear.get("colors", [0, 0])

        if gear_id:
            buf._append_bits(1, 1)  # presence bit
            buf._append_bits(gear_id, 11)  # Gear ID (11 bits)
            buf._append_bits(0, 2)  # reserved/flags (still hardcoded to 0)
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
    # ────────────── (5) Mission‐tracker ──────────────
    # ────────────── (5) Mission‐tracker ──────────────
    missions = char.get("missions", {})

    # 1) total number of mission definitions
    total_defs = len(var_238) - 1
    buf.write_method_4(total_defs)

    # 2) for each mission ID, in order
    for mid in range(1, total_defs + 1):
        mdef = var_238[mid]
        mstate = missions.get(str(mid))

        # outer presence bit
        has_state = mstate is not None
        buf._append_bits(1 if has_state else 0, 1)
        if not has_state:
            continue

        # one‐shot missions: write an extra “ready” bit
        if mdef.var_1775:
            ready = (mstate.get("state") == Mission.const_72)  # 2
            buf._append_bits(1 if ready else 0, 1)
            continue

        # multi-step missions:

        # inner bit #1: “ready vs in-progress”
        ready = (mstate.get("state") == Mission.const_72)
        buf._append_bits(1 if ready else 0, 1)

        if not ready:
            # in-progress: currCount if >1
            if mdef.var_908 > 1:
                buf.write_method_4(mstate.get("currCount", 0))
        else:
            # inner bit #2: “reward claimed?”
            claimed = (mstate.get("state") == Mission.const_58)  # 1
            buf._append_bits(1 if claimed else 0, 1)

            # timed-mission extras
            if mdef.var_134:
                buf._append_bits(mstate.get("var_588", 0), class_119.const_228)
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

    craft_talent_points = char.get("craftTalentPoints", [0, 0, 0, 0, 0])  # List of 5 values, each 0-15
    packed_value = 0
    for i in range(5):
        packed_value |= (craft_talent_points[i] & 0xF) << (i * 4)
    buf.write_method_4(packed_value)
    tower_points = char.get("towerPoints", [0, 0, 0])  # List of 3 values, each 0-63
    for tp in tower_points:
        buf.write_method_6(tp, 6)  # class_66_const_409 = 6

    # Magic Forge Section
    mf = char.get("magicForge", {})
    has_stats = bool(mf.get("stats", []))
    buf._append_bits(1 if has_stats else 0, 1)
    if has_stats:
        stats = mf.get("stats", [0] * 7)
        for val in stats[:7]:
            buf.write_method_6(val, class_9_const_28)

    has_session = mf.get("hasSession", False)
    buf._append_bits(1 if has_session else 0, 1)
    if has_session:
        primary = mf.get("primary", 0)
        buf.write_method_6(primary, class_1_const_254)
        status = mf.get("status", 0)
        if status == 1:
            buf._append_bits(1, 1)
            endtime = mf.get("endtime", 0)
            buf.write_method_4(endtime)
        else:
            buf._append_bits(0, 1)
            var_8 = mf.get("var_8", 0)
            buf.write_method_6(var_8, class_64_const_499)
            if var_8 != 0:
                secondary = mf.get("secondary", 0)
                buf.write_method_6(secondary, class_64_const_218)
                usedlist = mf.get("usedlist", 0)
                buf.write_method_6(usedlist, class_111_const_432)
        var_2675 = min(mf.get("var_2675", 0), 65535)
        var_2316 = min(mf.get("var_2316", 0), 65535)
        buf.write_method_91(var_2675)
        buf.write_method_91(var_2316)

    var_2434 = mf.get("var_2434", False)
    buf._append_bits(1 if var_2434 else 0, 1)

   # Skill Research
    research = char.get("research")
    if research:
        buf._append_bits(1, 1)  # the method_11() flag
        buf.write_method_6(research["abilityID"], class_10_const_83)
        buf.write_method_4(research["finishTime"])
    else:
        buf._append_bits(0, 1)

    # (7) buildingResearch
    bld = char.get("buildingResearch")
    if bld:
        buf._append_bits(1, 1)
        buf.write_method_6(bld["slotID"], class_9_const_129)
        buf.write_method_4(bld["finishTime"])
    else:
        buf._append_bits(0, 1)

    # (8) towerResearch
    tower = char.get("towerResearch")
    if tower:
        buf._append_bits(1, 1)
        buf.write_method_6(tower["masterClassID"], class_66_const_571)
        buf.write_method_4(tower["finishTime"])
    else:
        buf._append_bits(0, 1)

    # 1) Optional “SetEggData” (egg type + reset timer)
    egg_data = char.get("eggData")
    if egg_data:
        buf._append_bits(1, 1)
        buf.write_method_6(egg_data["typeID"], class_16_const_167)
        buf.write_method_4(egg_data["resetEndTime"])
    else:
        buf._append_bits(0, 1)

    # 2) Egg-ID list
    eggPetIDs = char.get("eggPetIDs", [])
    buf.write_method_6(len(eggPetIDs), class_16_const_167)
    for eid in eggPetIDs:
        buf.write_method_6(eid, class_16_const_167)

    # 3) Active-egg count
    activeEggCount = char.get("activeEggCount", 0)
    buf.write_method_4(activeEggCount)

   #TODO... _loc119_: null
    # 4) Resting-pet loops (four distinct if-method_11() blocks)
    rest_loops = char.get("restingPets", [])[:4]

    for i in range(4):
        if i < len(rest_loops):
            r = rest_loops[i]
            buf._append_bits(1, 1)
            buf.write_method_6(r["typeID"], class_7_const_19)
            buf.write_method_4(r["level"])
            if i == 3 and "extraValue" in r:
                buf.write_method_4(r["extraValue"])
        else:
            buf._append_bits(0, 1)

    icon, headline, body, tooltip, ts = NEWS_EVENTS.get(
        event_index,
        ["", "", "", "", 0]           # fallback: no news
    )
    buf.write_utf_string(icon)       # _loc66_
    buf.write_utf_string(headline)   # _loc67_
    buf.write_utf_string(body)       # _loc68_
    buf.write_utf_string(tooltip)    # _loc69_
    buf.write_method_4(ts)           # _loc70_

    selected = str(char.get("MasterClass", 0))
    mastery_data = char.get("Mastery", {}).get(selected, {"classID": 0, "slots": []})

    # Write the chosen classID & slots exactly as before:
    buf.write_method_6(mastery_data["classID"], GAME_CONST_209)
    buf._append_bits(1, 1)  # we always send a tree
    for i in range(NUM_TALENT_SLOTS):
        slot = mastery_data["slots"][i] if i < len(mastery_data["slots"]) else {"filled": False}
        if slot["filled"]:
            buf._append_bits(1, 1)  # presence bit

            # === NODE INDEX FIRST ===
            buf.write_method_6(slot["nodeIdx"], CLASS_118_CONST_127)

            # === POINTS-MINUS-ONE SECOND ===
            bits = SLOT_BIT_WIDTHS[i]
            buf.write_method_6(slot["points"] - 1, bits)
        else:
            buf._append_bits(0, 1)

    equip = char.get("equippedGears", [])
    for slot_id in range(EntType_MAX_SLOTS):
        gear = equip[slot_id] if slot_id < len(equip) else {}
        gear_id = gear.get("gearID", 0)

        if gear_id:
            buf._append_bits(1, 1)  # presence bit
            buf.write_method_6(gear_id, GEARTYPE_BITS)
        else:
            buf._append_bits(0, 1)

    # ────────────── (9) Equipped‐mount ID ──────────────
    #equipped_mount = char.get("mountID", 0)
    #buf.write_method_4(equipped_mount)

    payload = buf.to_bytes()
    return struct.pack(">HH", 0x10, len(payload)) + payload

def build_enter_world_packet(
        transfer_token: int,
        old_level_id: int,
        old_swf: str,
        has_old_coord: bool,
        old_x: int,
        old_y: int,
        host: str,
        port: int,
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
    buf.write_utf_string(host)
    # 5) userID
    buf.write_method_4(port)
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


"""def Player_Data_Packet(char: dict,
                      event_index: int = 1,
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

    craft_talent_points = char.get("craftTalentPoints", [0, 0, 0, 0, 0])  # List of 5 values, each 0-15
    packed_value = 0
    for i in range(5):
        packed_value |= (craft_talent_points[i] & 0xF) << (i * 4)
    buf.write_method_4(packed_value)
    tower_points = char.get("towerPoints", [0, 0, 0])  # List of 3 values, each 0-63
    for tp in tower_points:
        buf.write_method_6(tp, 6)  # class_66_const_409 = 6

    # Magic Forge Section
    mf = char.get("magicForge", {})
    has_stats = bool(mf.get("stats", []))
    buf._append_bits(1 if has_stats else 0, 1)
    if has_stats:
        stats = mf.get("stats", [0] * 7)
        for val in stats[:7]:
            buf.write_method_6(val, class_9_const_28)

    has_session = mf.get("hasSession", False)
    buf._append_bits(1 if has_session else 0, 1)
    if has_session:
        primary = mf.get("primary", 0)
        buf.write_method_6(primary, class_1_const_254)
        status = mf.get("status", 0)
        if status == 1:
            buf._append_bits(1, 1)
            endtime = mf.get("endtime", 0)
            buf.write_method_4(endtime)
        else:
            buf._append_bits(0, 1)
            var_8 = mf.get("var_8", 0)
            buf.write_method_6(var_8, class_64_const_499)
            if var_8 != 0:
                secondary = mf.get("secondary", 0)
                buf.write_method_6(secondary, class_64_const_218)
                usedlist = mf.get("usedlist", 0)
                buf.write_method_6(usedlist, class_111_const_432)
        var_2675 = min(mf.get("var_2675", 0), 65535)
        var_2316 = min(mf.get("var_2316", 0), 65535)
        buf.write_method_91(var_2675)
        buf.write_method_91(var_2316)

    var_2434 = mf.get("var_2434", False)
    buf._append_bits(1 if var_2434 else 0, 1)

   # Skill Research
    research = char.get("research")
    if research:
        buf._append_bits(1, 1)  # the method_11() flag
        buf.write_method_6(research["abilityID"], class_10_const_83)
        buf.write_method_4(research["finishTime"])
    else:
        buf._append_bits(0, 1)

    # (7) buildingResearch
    bld = char.get("buildingResearch")
    if bld:
        buf._append_bits(1, 1)
        buf.write_method_6(bld["slotID"], class_9_const_129)
        buf.write_method_4(bld["finishTime"])
    else:
        buf._append_bits(0, 1)

    # (8) towerResearch
    tower = char.get("towerResearch")
    if tower:
        buf._append_bits(1, 1)
        buf.write_method_6(tower["masterClassID"], class_66_const_571)
        buf.write_method_4(tower["finishTime"])
    else:
        buf._append_bits(0, 1)

    # 1) Optional “SetEggData” (egg type + reset timer)
    egg_data = char.get("eggData")
    if egg_data:
        buf._append_bits(1, 1)
        buf.write_method_6(egg_data["typeID"], class_16_const_167)
        buf.write_method_4(egg_data["resetEndTime"])
    else:
        buf._append_bits(0, 1)

    # 2) Egg-ID list
    eggPetIDs = char.get("eggPetIDs", [])
    buf.write_method_6(len(eggPetIDs), class_16_const_167)
    for eid in eggPetIDs:
        buf.write_method_6(eid, class_16_const_167)

    # 3) Active-egg count
    activeEggCount = char.get("activeEggCount", 0)
    buf.write_method_4(activeEggCount)

   #TODO... _loc119_: null
    # 4) Resting-pet loops (four distinct if-method_11() blocks)
    rest_loops = char.get("restingPets", [])[:4]

    for i in range(4):
        if i < len(rest_loops):
            r = rest_loops[i]
            buf._append_bits(1, 1)
            buf.write_method_6(r["typeID"], class_7_const_19)
            buf.write_method_4(r["level"])
            if i == 3 and "extraValue" in r:
                buf.write_method_4(r["extraValue"])
        else:
            buf._append_bits(0, 1)

    icon, headline, body, tooltip, ts = NEWS_EVENTS.get(
        event_index,
        ["", "", "", "", 0]           # fallback: no news
    )
    buf.write_utf_string(icon)       # _loc66_
    buf.write_utf_string(headline)   # _loc67_
    buf.write_utf_string(body)       # _loc68_
    buf.write_utf_string(tooltip)    # _loc69_
    buf.write_method_4(ts)           # _loc70_

    selected = str(char.get("MasterClass", 0))
    mastery_data = char.get("Mastery", {}).get(selected, {"classID": 0, "slots": []})

    # Write the chosen classID & slots exactly as before:
    buf.write_method_6(mastery_data["classID"], GAME_CONST_209)
    buf._append_bits(1, 1)  # we always send a tree
    for i in range(NUM_TALENT_SLOTS):
        slot = mastery_data["slots"][i] if i < len(mastery_data["slots"]) else {"filled": False}
        if slot["filled"]:
            buf._append_bits(1, 1)  # presence bit

            # === NODE INDEX FIRST ===
            buf.write_method_6(slot["nodeIdx"], CLASS_118_CONST_127)

            # === POINTS-MINUS-ONE SECOND ===
            bits = SLOT_BIT_WIDTHS[i]
            buf.write_method_6(slot["points"] - 1, bits)
        else:
            buf._append_bits(0, 1)

    equip = char.get("equipGear", [0] * EntType_MAX_SLOTS)
    for slot_id in range(1, EntType_MAX_SLOTS):
        gear_id = equip[slot_id]
        if gear_id:
            buf._append_bits(1, 1)  # presence
            buf.write_method_6(gear_id, GEARTYPE_BITS)  # GearType.GEARTYPE_BITSTOSEND
        else:
            buf._append_bits(0, 1)

    payload = buf.to_bytes()
    return struct.pack(">HH", 0x10, len(payload)) + payload"""