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
    GEARTYPE_BITS,
    Mission,
    class_119, class_111,
)
from missions import var_238
def Player_Data_Packet(char: dict,
                      event_index: int = 1,
                      transfer_token: int = 1,
                      scaling_factor: int = 0,
                      bonus_levels: int = 0,
                      target_level: str = None,
                      new_x: int = None,
                      new_y: int = None,
                      new_has_coord: bool = True) -> bytes:
    buf = BitBuffer()

    # ────────────── (1) Preamble ──────────────
    buf.write_method_4(transfer_token)  # _loc2_
    current_game_time = int(time.time())  # seconds
    buf.write_method_4(current_game_time)
    # _loc3_
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
    buf.write_method_4(char.get("craftXP", 0))  # Gems
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
    #buf._append_bits(0, 1)  # no door/teleport update
    if new_has_coord and target_level and new_x is not None and new_y is not None:
        buf._append_bits(1, 1)
        buf.write_signed_method_45(new_x)
        buf.write_signed_method_45(new_y)
    else:
        buf._append_bits(0, 1)
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

    # 1) Stats flag + stats data
    has_stats = bool(mf.get("stats", []))
    buf._append_bits(1 if has_stats else 0, 1)
    if has_stats:
        for val in mf.get("stats", [0] * 7)[:7]:
            buf.write_method_6(val, class_9_const_28)

    # 2) Session flag
    has_session = mf.get("hasSession", False)
    buf._append_bits(1 if has_session else 0, 1)

    if has_session:
        # 2a) Read primary gem ID
        primary = mf.get("primary", 0)
        buf.write_method_6(primary, class_1_const_254)

        # 2b) In-progress or completed?
        status = mf.get("status", class_111.const_509)
        if status == class_111.const_286:  # in progress
            # write “1” then the end-time
            buf._append_bits(1, 1)
            now = int(time.time())
            duration_ms = mf.get("duration", 60000)
            duration_sec = (duration_ms + 999) // 1000
            duration_sec = min(duration_sec, (2 ** 30) - 1)
            end_ts = now + duration_sec
            buf.write_method_4(end_ts)
        else:
            # write “0” then var_8 + secondary + usedlist
            buf._append_bits(0, 1)
            var_8 = mf.get("var_8", 0)
            buf.write_method_6(var_8, class_64_const_499)
            if var_8:
                buf.write_method_6(mf.get("secondary", 0), class_64_const_218)
                buf.write_method_6(mf.get("usedlist", 0), class_111_const_432)

        # 2c) Only when there IS a session do we write these two
        buf.write_method_91(min(mf.get("var_2675", 0), 65535))
        buf.write_method_91(min(mf.get("var_2316", 0), 65535))

    # 3) Final continuation flag (var_2434)
    buf._append_bits(1 if mf.get("var_2434", False) else 0, 1)

    # ── Skill Research ──
    research = char.get("research")
    if research:
        buf._append_bits(1, 1)  # flag: research in progress

        # 1) ability ID
        buf.write_method_6(research["abilityID"], class_10_const_83)

        # 2) build an end timestamp in seconds
        now_sec = int(time.time())  # current time in seconds
        ready_ms = research.get("ReadyTime", 0)  # e.g. 50000 ms
        duration_sec = (ready_ms + 999) // 1000  # round up to seconds

        # 3) cap to method_4’s safe range (~1B)
        max_safe = (2 ** 30) - 1
        duration_sec = min(duration_sec, max_safe)

        # 4) compute absolute end time in seconds
        end_sec = now_sec + duration_sec

        # 5) write end time
        buf.write_method_4(end_sec)

    else:
        buf._append_bits(0, 1)

    # (7) buildingResearch
    bld = char.get("buildingResearch")
    if bld:
        buf._append_bits(1, 1)

        # 1) write the building slot ID
        buf.write_method_6(bld["slotID"], class_9_const_129)

        # 2) calculate end time in seconds
        now_sec = int(time.time())  # current Unix time (s)
        finish_ms = bld.get("finishTime", 0)  # stored as milliseconds
        duration_sec = (finish_ms + 999) // 1000  # round up to seconds

        # 3) cap to method_4’s safe range (~1B)
        max_safe = (2 ** 30) - 1
        duration_sec = min(duration_sec, max_safe)

        # 4) absolute finish time (s)
        finish_sec = now_sec + duration_sec

        # 5) write as a method_4 timestamp
        buf.write_method_4(finish_sec)

    else:
        buf._append_bits(0, 1)

    # (8) towerResearch
    tower = char.get("towerResearch")
    if tower:
        buf._append_bits(1, 1)

        # 1) write the master class ID
        buf.write_method_6(tower["masterClassID"], class_66_const_571)

        # 2) calculate end time in seconds
        now_sec = int(time.time())  # current Unix time (s)
        end_ms = tower.get("endTime", 0)  # stored in milliseconds
        duration_sec = (end_ms + 999) // 1000  # convert & round up to seconds

        # 3) cap to method_4’s safe range (~1B)
        max_safe = (2 ** 30) - 1
        duration_sec = min(duration_sec, max_safe)

        # 4) absolute finish time (s)
        finish_sec = now_sec + duration_sec

        # 5) write as a method_4 timestamp
        buf.write_method_4(finish_sec)

    else:
        buf._append_bits(0, 1)

    # “SetEggData” (egg type + reset timer)
    egg_data = char.get("eggData")
    if egg_data:
        buf._append_bits(1, 1)

        # 1) egg type ID
        buf.write_method_6(egg_data["typeID"], class_16_const_167)

        # 2) calculate end time in seconds
        now_sec = int(time.time())  # current Unix time (s)
        reset_ms = egg_data.get("resetEndTime", 0)  # stored in milliseconds
        duration_sec = (reset_ms + 999) // 1000  # convert & round up to seconds

        # 3) cap to method_4’s safe range (~1B)
        max_safe = (2 ** 30) - 1
        duration_sec = min(duration_sec, max_safe)

        # 4) absolute finish time (s)
        finish_sec = now_sec + duration_sec

        # 5) write as a method_4 timestamp
        buf.write_method_4(finish_sec)

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
        ["", "", "", "", 0]
    )
    buf.write_utf_string(icon)
    buf.write_utf_string(headline)
    buf.write_utf_string(body)
    buf.write_utf_string(tooltip)

    # 1) current time in seconds
    now_sec = int(time.time())

    # 2) event duration (5 days) in milliseconds → seconds
    five_days_ms = 12 * 24 * 60 * 60 * 1000
    duration_sec = (five_days_ms + 999) // 1000  # round up to seconds

    # 3) cap to method_4’s safe range (~1B)
    max_safe = (2 ** 30) - 1
    duration_sec = min(duration_sec, max_safe)

    # 4) compute future end timestamp in seconds
    event_end_sec = now_sec + duration_sec

    # 5) write it as a method_4 value
    buf.write_method_4(event_end_sec)

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

    # Equipped Gears
    equip = char.get("equippedGears", [])
    for slot_id in range(1, 7):  # Slots 1 to 6
        gear = equip[slot_id - 1] if slot_id - 1 < len(equip) else {}
        gear_id = gear.get("gearID", 0)
        if gear_id:
            buf._append_bits(1, 1)
            buf.write_method_6(gear_id, GEARTYPE_BITS)
        else:
            buf._append_bits(0, 1)

    # TODO... the equipped Mounts and Pets are not showing not sure why yet
    mount_id = char.get("equippedMount", 0)
    buf.write_method_4(mount_id)
    pet_type_id = char.get("equippedPetID", 0)
    pet_iteration = char.get("petIteration", 0)
    buf.write_method_4(pet_type_id)
    buf.write_method_4(pet_iteration)
    active_consumable_id = char.get("activeConsumableID", 0)
    queued_consumable_id = char.get("queuedConsumableID", 0)
    buf.write_method_4(active_consumable_id)
    buf.write_method_4(queued_consumable_id)

    # ──── (10) Guild‐panel data (method_933) ────
    guild = char.get("guild", None)
    in_guild = guild is not None
    buf._append_bits(1 if in_guild else 0, 1)

    if in_guild:
        buf.write_utf_string(guild["name"])
        buf.write_method_6(guild.get("rank", 0), 3)

        members = guild.get("onlineMembers", [])
        buf.write_method_4(len(members))
        for m in members:
            buf.write_utf_string(m["name"])
            buf.write_method_6(m["classID"], 2)
            buf.write_method_6(m["level"], 6)
            buf.write_method_6(m["status"], 3)

        # your own entry
        buf.write_utf_string(char["name"])
        buf.write_method_6(CLASS_NAME_TO_ID[char["class"]], 2)
        buf.write_method_6(char["level"], 6)
        buf.write_method_6(guild.get("rank", 0), 3)

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
    new_is_inst: bool,
    new_has_coord: bool = False,
    new_x: int = 0,
    new_y: int = 0,
    char: dict = None,
) -> bytes:
    buf = BitBuffer()

    # 1) transferToken (_loc4_)
    buf.write_method_4(transfer_token)

    # 2) oldLevelId (_loc5_)
    buf.write_method_4(old_level_id)

    # 3) old SWF path (_loc6_)
    buf.write_utf_string(old_swf)

    # 4) old coords? + values (_loc8_, _loc2_, _loc3_)
    buf._append_bits(1 if has_old_coord else 0, 1)
    if has_old_coord:
        buf.write_method_4(old_x)
        buf.write_method_4(old_y)

    # 5) host (_loc9_)
    buf.write_utf_string(host)

    # 6) port (_loc10_)
    buf.write_method_4(port)

    # 7) new SWF path (_loc11_)
    buf.write_utf_string(new_level_swf)

    # 8) new_map_lvl, new_base_lvl (_loc12_, _loc13_, 6 bits each)
    buf.write_method_6(new_map_lvl, MAX_CHAR_LEVEL_BITS)
    buf.write_method_6(new_base_lvl, MAX_CHAR_LEVEL_BITS)

    # 9) new strings (_loc14_, _loc15_, _loc16_)
    buf.write_utf_string(new_internal)
    buf.write_utf_string(new_moment)
    buf.write_utf_string(new_alter)

    # 10) new_is_instanced flag (_loc17_)
    buf._append_bits(1 if new_is_inst else 0, 1)

    # 11) spawn-point flag (_loc18_) + coords (_loc20_, _loc21_)
    buf._append_bits(1 if new_has_coord else 0, 1)
    if new_has_coord:
        buf.write_signed_method_45(new_x)
        buf.write_signed_method_45(new_y)

    # 12) Extended data presence (_loc19_)
    buf._append_bits(1, 1)  # Indicate we are sending building data

    # 13) Buildings data block
    # New level ID (_loc22_, same as transfer_token)
    new_level_id = transfer_token
    buf.write_method_4(new_level_id)

    # Master class ID (_loc25_, 4 bits)
    master_class_id = char.get("MasterClass", 0) if char else 0
    buf.write_method_6(master_class_id, GAME_CONST_209)

    # Building levels from magicForge stats (5 bits each)
    stats = char.get("magicForge", {}).get("stats", [0] * 7) if char else [0] * 7
    forge_level = stats[0]         # _loc26_, e.g., 10
    keep_level = stats[1]          # _loc27_, e.g., 0
    tower_level = stats[2]         # _loc28_, e.g., 10
    tome_level = stats[3]          # _loc29_, e.g., 10
    barn_level = stats[4]          # _loc30_, e.g., 10
    scaffolding_level = stats[5]   # _loc31_, e.g., 10

    buf.write_method_6(forge_level, class_9_const_28)
    buf.write_method_6(keep_level, class_9_const_28)
    buf.write_method_6(tower_level, class_9_const_28)
    buf.write_method_6(tome_level, class_9_const_28)
    buf.write_method_6(barn_level, class_9_const_28)
    buf.write_method_6(scaffolding_level, class_9_const_129)

    # Build final packet
    payload = buf.to_bytes()
    return struct.pack(">HH", 0x21, len(payload)) + payload
