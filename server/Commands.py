
import json, struct
import pprint
import random
import secrets
import time

from Character import save_characters, build_paperdoll_packet
from accounts import build_popup_packet
from bitreader import BitReader
from constants import GearType, EntType, class_64, class_1, DyeType, class_118, method_277, GAME_CONST_209, \
    CLASS_118_CONST_127, class_111, class_1_const_254, class_8, class_3, \
    get_ability_info, load_building_data, find_building_data, class_66, LinkUpdater, PowerType, Entity, Game

from BitUtils import BitBuffer
from constants import get_dye_color
from level_config import SPAWN_POINTS, DOOR_MAP, LEVEL_CONFIG
from scheduler import scheduler, _on_research_done_for, schedule_building_upgrade, _on_building_done_for, \
    schedule_forge, _on_talent_done_for, schedule_Talent_point_research

SAVE_PATH_TEMPLATE = "saves/{user_id}.json"

def handle_collect_hatched_egg(conn, char):
    egg_data = char.get("EggHachery", {})
    egg_id = egg_data.get("EggID", 0)

    if egg_id > 0:
        # Add egg as pet
        new_pet = {
            "PetTypeID": egg_id,
            "Rank": 1,
            # any other pet fields you use
        }
        char.setdefault("OwnedPets", []).append(new_pet)

        # Clear hatchery
        char["EggHachery"] = {"EggID": 0, "ReadyTime": 0, "done": False}

        # Send updated hatchery state to client so it stops spamming 0xEA
        buf = BitBuffer()
        buf._append_bits(0, 1)  # no egg data
        payload = buf.to_bytes()
        conn.sendall(struct.pack(">HH", 0xe7, len(payload)) + payload)

def handle_pet_info_packet(session, data, all_sessions):
    """
    Handle packet type 0xB3 for sending pet information to the server.
    Parses the payload to extract pet type IDs and values for active and resting pets.
    """
    if data[:2] != b'\x00\xb3':
        return

    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKT0xB3] Ignored: not authenticated or no character")
        return

    payload = data[4:]  # Skip header (type: 00b3, length: 0007)
    reader = BitReader(payload, debug=True)

    try:
        # Parse four pets: active pet and three resting pets
        pets = []
        for _ in range(4):
            pet_type_id = reader.read_method_6(7)  # 7-bit pet type ID
            value = reader.read_method_4()         # Variable-length value
            pets.append((pet_type_id, value))

        # Extract pet information
        active_pet_type, active_pet_value = pets[0]
        resting_pet1_type, resting_pet1_value = pets[1]
        resting_pet2_type, resting_pet2_value = pets[2]
        resting_pet3_type, resting_pet3_value = pets[3]

        # Print the parsed pet information
        print(f"[{session.addr}] [PKT0xB3] Active pet: type={active_pet_type}, value={active_pet_value}")
        print(f"[{session.addr}] [PKT0xB3] Resting pet 1: type={resting_pet1_type}, value={resting_pet1_value}")
        print(f"[{session.addr}] [PKT0xB3] Resting pet 2: type={resting_pet2_type}, value={resting_pet2_value}")
        print(f"[{session.addr}] [PKT0xB3] Resting pet 3: type={resting_pet3_type}, value={resting_pet3_value}")

    except Exception as e:
        print(f"[{session.addr}] [PKT0xB3] Error parsing packet: {e}")
        for line in reader.get_debug_log():
            print(line)


REWARD_TYPES = ['gear', 'item', 'gold', 'chest', 'xp', 'potion']
GEARTYPE_BITS = GearType.GEARTYPE_BITSTOSEND  # e.g. 5

def build_loot_drop_packet(entity_id: int, x: int, y: int,
                           reward_type: str, value1: int=0, value2: int=0) -> bytes:
    """
    Packet 0x32: one bit per reward in order:
      [gear, item, gold, chest, xp, potion]
    """
    bb = BitBuffer(debug=True)

    # 1) Entity ID
    bb.write_method_4(entity_id)

    # 2) X,Y (signed)
    bb.write_signed_method_45(x)
    bb.write_signed_method_45(y)

    # 3) no-offset flag = 0
    bb._append_bits(1, 1)

    # 4) six-type flags + payload
    for rt in REWARD_TYPES:
        bit = 1 if rt == reward_type else 0
        bb._append_bits(bit, 1)
        if bit:
            if rt == 'gear':
                bb.write_method_6(value1, GEARTYPE_BITS)
                bb.write_method_6(value2, GEARTYPE_BITS)
            else:
                bb.write_method_4(value1)
            break

    payload = bb.to_bytes()
    header  = struct.pack('>HH', 0x32, len(payload))
    return header + payload


def handle_grant_reward(session, data, all_sessions):
    # …header checks…

    payload = data[4:]
    br = BitReader(payload, debug=True)
    try:
        grantor_id    = br.read_method_9()
        target_id     = br.read_method_9()

        flag_showXP   = bool(br.read_bit())
        xp_rate       = br.read_float()

        flag_showGold = bool(br.read_bit())
        gold_rate     = br.read_float()

        flag_showHeal = bool(br.read_bit())
        flag_showMana = bool(br.read_bit())

        code_xpType   = br.read_method_9()
        code_goldType = br.read_method_9()
        code_manaType = br.read_method_9()
        code_healType = br.read_method_9()

        # **NOW** read the drop coordinates:
        drop_x = br.read_method_24()   # signed 24-bit
        drop_y = br.read_method_24()   # signed 24-bit

        has_extra     = bool(br.read_bit())
        extra_id      = br.read_method_9() if has_extra else None

    except Exception as e:
        print("…parsing error…")
        # …
        return

    # log for sanity:
    #print(f"[PKT2A] grantor={grantor_id} target={target_id} coords=({drop_x},{drop_y}) "
          #f"XP?{flag_showXP}@{xp_rate} Gold?{flag_showGold}@{gold_rate} Extra?{extra_id}")

    # now build loot_drops using the true drop_x, drop_y:
    loot_drops = []
    if flag_showXP:
        loot_drops.append(('xp', code_xpType, int(xp_rate)))
    if flag_showGold:
        loot_drops.append(('gold', code_goldType, int(gold_rate)))
    if flag_showHeal:
        loot_drops.append(('healing', code_healType, 0))
    if flag_showMana:
        loot_drops.append(('mana', code_manaType, 0))
    if extra_id:
        # the client expects two fixed‐width values for gear:
        loot_drops.append(('gear', extra_id, extra_id))

    # broadcast one 0x32 per drop:
    for rtype, v1, v2 in loot_drops:
        pkt = build_loot_drop_packet(
            entity_id=target_id,
            x=drop_x,
            y=drop_y,
            reward_type=rtype,
            value1=v1,
            value2=v2
        )
        for other in all_sessions:
            if other.world_loaded and other.current_level == session.current_level:
                other.conn.sendall(pkt)
                #print(f"[PKT2A] → DROP {rtype} @({drop_x},{drop_y}) to {other.addr}")


def handle_change_max_speed(session, data, all_sessions):
    # Extract payload (skip 4-byte header: type and length)
    payload = data[4:]
    br = BitReader(payload, debug=True)

    # Parse entity ID and speed modifier
    try:
        entity_id = br.read_method_4()
        speed_mod_int = br.read_method_4()
    except Exception as e:
        #print(f"[{session.addr}] [PKT0x8A] Error parsing packet: {e}")
        return

    # Find the entity
    entity = session.entities.get(entity_id)
    if not entity:
        #print(f"[{session.addr}] [PKT0x8A] Entity {entity_id} not found")
        return

    # Update the entity's behaviorSpeedMod
    entity['behaviorSpeedMod'] = speed_mod_int * LinkUpdater.VELOCITY_DEFLATE
    #print(f"[{session.addr}] [PKT0x8A] Updated entity {entity_id} behaviorSpeedMod to {entity['behaviorSpeedMod']}")

    # Build the broadcast packet
    bb = BitBuffer()
    bb.write_method_4(entity_id)
    bb.write_method_4(speed_mod_int)  # Send the original integer value
    payload = bb.to_bytes()
    packet = struct.pack(">HH", 0x8A, len(payload)) + payload

    # Broadcast to all clients in the same level
    for other_session in all_sessions:
        if other_session.world_loaded and other_session.current_level == session.current_level:
            other_session.conn.sendall(packet)


def handle_lockbox_reward(session):
    CAT_BITS = 3
    ID_BITS = 6
    PACK_ID = 1

    reward_map = {
        0: ("MountLockbox01L01", True),  # Mount
        1: ("Lockbox01L01", True),  # Pet
        # 2: ("GenericBrown", True),  # Egg
        # 3: ("CommonBrown", True),  # Egg
        # 4: ("OrdinaryBrown", True),  # Egg
        # 5: ("PlainBrown", True),  # Egg
        6: ("RarePetFood", True),  # Consumable
        7: ("PetFood", True),  # Consumable
        # 8: ("Lockbox01Gear", True),  # Gear (will crash if invalid)
        9: ("TripleFind", True),  # Charm
        10: ("DoubleFind1", True),  # Charm
        11: ("DoubleFind2", True),  # Charm
        12: ("DoubleFind3", True),  # Charm
        13: ("MajorLegendaryCatalyst", True),  # Consumable
        14: ("MajorRareCatalyst", True),  # Consumable
        15: ("MinorRareCatalyst", True),  # Consumable
        16: (None, False),  # Gold (3 000 000)
        17: (None, False),  # Gold (1 500 000)
        18: (None, False),  # Gold (750 000)
        19: ("DyePack01Legendary", True),  # Dye‐pack
    }

    idx, (name, needs_str) = random.choice(list(reward_map.items()))
    bb = BitBuffer()
    bb.write_method_6(PACK_ID, CAT_BITS)
    bb.write_method_6(idx, ID_BITS)
    bb.write_bits(1 if needs_str else 0, 1)
    if needs_str:
        bb.write_utf_string(name)

    payload = bb.to_bytes()
    packet = struct.pack(">HH", 0x108, len(payload)) + payload
    session.conn.sendall(packet)

    print(f"Lockbox reward: idx={idx}, name={name}, needs_str={needs_str}")


def send_mastery_packet(session, entity_id):
    # 1) Fetch slots for current MasterClass

    mc = None
    slots = []
    for char in session.char_list:
        if char.get("name") == session.current_character:
            mc      = char.get("MasterClass", 1)
            mastery = char.get("Mastery", {}).get(str(mc), {})
            slots   = mastery.get("slots", [])
            break
    else:
        return
    session.player_data["characters"] = session.char_list

    # Turn into a map 0-based index -> slot data
    slot_map = { s["nodeIdx"] - 1: s for s in slots }

    # 2) Build the exact packet
    bb = BitBuffer()
    bb.write_method_4(entity_id)

    total = class_118.const_43  # 27 slots
    for i in range(total):
        if i in slot_map and slot_map[i].get("filled"):
            slot = slot_map[i]
            bb.write_bits(1, 1)  # has this node
            bb.write_method_6(slot["nodeIdx"], CLASS_118_CONST_127)
            width = method_277(i)  # exactly method_277(i)
            bb.write_bits(slot["points"] - 1, width)
        else:
            bb.write_bits(0, 1)

    payload = bb.to_bytes()
    pkt = struct.pack(">HH", 0xC1, len(payload)) + payload
    session.conn.sendall(pkt)
    #print(f"[Reply 0xC1] Mastery for class {mc}, slot_map keys: {sorted(slot_map.keys())}")

def handle_masterclass_packet(session, raw_data):
    payload = raw_data[4:]
    br = BitReader(payload)
    entity_id       = br.read_method_4()
    master_class_id = br.read_method_6(GAME_CONST_209)
    print(f"[MasterClass] Player {session.user_id} → classID={master_class_id}")

    for char in session.char_list:
        if char.get("name") == session.current_character:
            char["MasterClass"] = master_class_id
            break
    else:
        return

    session.player_data["characters"] = session.char_list
    save_characters(session.user_id, session.char_list)

    bb = BitBuffer()
    bb.write_method_4(entity_id)
    bb.write_method_6(master_class_id, GAME_CONST_209)
    resp = struct.pack(">HH", 0xC3, len(bb.to_bytes())) + bb.to_bytes()
    session.conn.sendall(resp)
    print(f"[Reply 0xC3] entity={entity_id}, class={master_class_id}")

    send_mastery_packet(session, entity_id)

def handle_clear_talent_research(session, data):
    """
    Handle 0xDF: client cleared the current talent research.
    Payload: [ header(4) ]  (no body)
    """
    #print(f"[{session.addr}] [0xDF] ClearResearch packet received")

    # 1) Locate the character
    char = next((c for c in session.char_list
                 if c.get("name") == session.current_character), None)
    if not char:
        print(f"[{session.addr}] [0xDF] no character found")
        return

    # 2) Cancel any pending scheduler
    tr = char.get("talentResearch", {})
    sched_id = tr.pop("schedule_id", None)
    if sched_id is not None:
        try:
            scheduler.cancel(sched_id)
            print(f"[{session.addr}] [0xDF] Canceled talent schedule id={sched_id}")
        except Exception as e:
            print(f"[{session.addr}] [0xDF] Failed to cancel schedule: {e}")

    # 3) Clear the research state
    char["talentResearch"] = {
        "classIndex": None,
        "ReadyTime":  0,
        "done":       False,
        "isInstant":  False
    }

    # 4) Persist and mirror
    save_characters(session.user_id, session.char_list)
    mem = next((c for c in session.char_list
                if c.get("name") == session.current_character), None)
    if mem:
        mem["talentResearch"] = char["talentResearch"].copy()

    #print(f"[{session.addr}] [0xDF] talentResearch cleared for {session.current_character}")

def handle_gear_packet(session, raw_data):
    payload = raw_data[4:]
    br = BitReader(payload)

    entity_id  = br.read_method_4()
    prefix     = br.read_bits(3)
    nbits      = 2 * (prefix + 1)
    slot1      = br.read_bits(nbits)
    gear_id    = br.read_method_6(GearType.GEARTYPE_BITSTOSEND)
    slot       = slot1 - 1

    print(f"[Gear] entity={entity_id}, slot={slot}, gear={gear_id}")
    # 1) Locate and update the character in session.char_list
    for char in session.char_list:
        if char.get("name") != session.current_character:
            continue

        inv = char.setdefault("inventoryGears", [])
        eq  = char.setdefault("equippedGears", [])

        # Ensure equipped list has enough slots
        while len(eq) < 6:
            eq.append({"gearID": 0, "tier": 0, "runes": [0, 0, 0], "colors": [0, 0]})

        # 1) Try to find gear in inventory
        for item in inv:
            if item.get("gearID") == gear_id:
                gear_data = item.copy()
                break
        else:
            # fallback default if not found (client will still fail visually, but we'll keep server consistent)
            gear_data = {
                "gearID": gear_id,
                "tier": 0,
                "runes": [0, 0, 0],
                "colors": [0, 0]
            }

        # 2) Set gear in equipped slot
        eq[slot] = gear_data

        # 3) Ensure gear also exists in inventory (add if missing)
        if not any(g.get("gearID") == gear_id for g in inv):
            inv.append(gear_data.copy())  # keep dye/rune info consistent

        break
    # 2) Sync into session.player_data if still used
    session.player_data["characters"] = session.char_list

    # 3) Persist via helper
    save_characters(session.user_id, session.char_list)
    print(f"[Save] slot {slot} updated with gear {gear_id}, inventory count = {len(inv)}")

    # Echo back to client
    bb = BitBuffer()
    bb.write_method_4(entity_id)
    bb.write_bits(prefix, 3)
    bb.write_bits(slot1, nbits)
    bb.write_method_6(gear_id, GearType.GEARTYPE_BITSTOSEND)
    resp = struct.pack(">HH", 0x31, len(bb.to_bytes())) + bb.to_bytes()
    session.conn.sendall(resp)
    print(f"[Reply 0x31] echoed equip update")

def handle_apply_dyes(session, payload):
    br = BitReader(payload)

    try:
        entity_id = br.read_method_4()
        dyes_by_slot = {}
        for slot in range(1, EntType.MAX_SLOTS):
            has_pair = br.read_bits(1)
            if has_pair:
                d1 = br.read_bits(DyeType.BITS)
                d2 = br.read_bits(DyeType.BITS)
                dyes_by_slot[slot - 1] = (d1, d2)

        preview_only = bool(br.read_bits(1))
        primary_dye = br.read_bits(DyeType.BITS) if br.read_bits(1) else None
        secondary_dye = br.read_bits(DyeType.BITS) if br.read_bits(1) else None
    except Exception as e:
        print(f"[Dyes] ERROR parsing dye packet: {e}")
        return

    print(f"[Dyes] entity={entity_id}, dyes={dyes_by_slot}, "
          f"preview={preview_only}, shirt={primary_dye}, pants={secondary_dye}")

    for char in session.char_list:
        if char.get("name") != session.current_character:
            continue

        eq = char.setdefault("equippedGears", [])
        inv = char.setdefault("inventoryGears", [])

        # Apply gear dye colors
        for slot, (d1, d2) in dyes_by_slot.items():
            if slot < len(eq):
                eq[slot]["colors"] = [d1, d2]
                gear_id = eq[slot].get("gearID")

                # Update matching item in inventory
                for g in inv:
                    if g.get("gearID") == gear_id:
                        g["colors"] = [d1, d2]
                        break
                else:
                    # Ensure we insert a full copy so dyes persist
                    inv.append(eq[slot].copy())

        # Handle clothes (shirt/pant) color conversion from dye ID
        if primary_dye is not None:
            color = get_dye_color(primary_dye)
            if color is not None:
                char["shirtColor"] = color
            else:
                print(f"[Warning] Unknown primary dye ID: {primary_dye}")

        if secondary_dye is not None:
            color = get_dye_color(secondary_dye)
            if color is not None:
                char["pantColor"] = color
            else:
                print(f"[Warning] Unknown secondary dye ID: {secondary_dye}")

        break
    else:
        print(f"[Dyes] ERROR: character {session.current_character} not found")
        return

    session.player_data["characters"] = session.char_list
    save_characters(session.user_id, session.char_list)
    print(f"[Save] Dye info applied for {session.current_character} and saved")

    char_data = next(c for c in session.char_list if c.get("name") == session.current_character)
    send_dye_sync_packet(
        session,
        entity_id,
        dyes_by_slot,
        char_data.get("shirtColor"),
        char_data.get("pantColor")
    )


def send_dye_sync_packet(session, entity_id, dyes_by_slot, shirt_color=None, pant_color=None):
        bb = BitBuffer()
        bb.write_method_4(entity_id)

        eq = []
        for char in session.player_data.get("characters", []):
            if char.get("name") == session.current_character:
                eq = char.get("equippedGears", [])
                break

        for slot in range(1, EntType.MAX_SLOTS):
            gear = eq[slot - 1] if slot - 1 < len(eq) else None
            if gear and "colors" in gear:
                d1, d2 = gear["colors"]
                bb.write_bits(1, 1)  # has dye pair
                bb.write_method_6(d1, DyeType.BITS)
                bb.write_method_6(d2, DyeType.BITS)
            else:
                bb.write_bits(0, 1)  # no dye pair

        # Write shirt color
        if shirt_color is not None:
            bb.write_bits(1, 1)
            bb.write_method_6(shirt_color, EntType.CHAR_COLOR_BITSTOSEND)
        else:
            bb.write_bits(0, 1)

        # Write pant color
        if pant_color is not None:
            bb.write_bits(1, 1)
            bb.write_method_6(pant_color, EntType.CHAR_COLOR_BITSTOSEND)
        else:
            bb.write_bits(0, 1)

        payload = bb.to_bytes()
        pkt = struct.pack(">HH", 0x111, len(payload)) + payload
        session.conn.sendall(pkt)
        print(f"[Sync] Sent dye update (0x111) to client for entity {entity_id}")

def handle_rune_packet(session, raw_data):
    payload = raw_data[4:]
    br = BitReader(payload)
    entity_id = br.read_method_4()
    gear_id    = br.read_method_6(GearType.GEARTYPE_BITSTOSEND)
    gear_tier  = br.read_method_6(GearType.const_176)
    rune_id    = br.read_method_6(class_64.const_101)
    rune_slot  = br.read_method_6(class_1.const_765)
    print(f"[Rune] entity={entity_id}, gear={gear_id}, tier={gear_tier}, rune_id={rune_id}, rune_slot={rune_slot}")

    for char in session.char_list:
        if char.get("name") != session.current_character:
            continue

        eq     = char.setdefault("equippedGears", [])
        inv    = char.setdefault("inventoryGears", [])
        charms = char.setdefault("charms", [])

        # Ensure correct slot count
        desired_slots = EntType.MAX_SLOTS - 1
        while len(eq) < desired_slots:
            eq.append({
                "gearID": 0,
                "tier": 0,
                "runes": [0, 0, 0],
                "colors": [0, 0]
            })
        if len(eq) > desired_slots:
            eq[:] = eq[:desired_slots]

        gear_found = False
        for slot in range(len(eq)):
            if eq[slot]["gearID"] == gear_id and eq[slot]["tier"] == gear_tier:
                idx = rune_slot - 1
                if 1 <= rune_slot <= 3:
                    old_rune = eq[slot]["runes"][idx]

                    if rune_id == 96:
                        # 1) Clear the rune slot
                        eq[slot]["runes"][idx] = 0

                        # 2) Return old_rune to charms
                        if old_rune and old_rune != 96:
                            for charm in charms:
                                if charm["charmID"] == old_rune:
                                    charm["count"] += 1
                                    break
                            else:
                                charms.append({"charmID": old_rune, "count": 1})

                        # 3) Decrement remover (ID 96) count
                        for charm in charms:
                            if charm["charmID"] == 96:
                                charm["count"] -= 1
                                if charm["count"] <= 0:
                                    charms.remove(charm)
                                break
                        else:
                            print("[Warning] No rune‑removers found to consume")

                    else:
                        # Equip new rune → set slot & decrement its count
                        eq[slot]["runes"][idx] = rune_id
                        for charm in charms:
                            if charm["charmID"] == rune_id:
                                charm["count"] -= 1
                                if charm["count"] <= 0:
                                    charms.remove(charm)
                                break
                        else:
                            print(f"[Warning] Equipped rune {rune_id} not in charms")

                    gear_found = True

                    # Sync inventoryGears
                    for item in inv:
                        if item["gearID"] == gear_id and item["tier"] == gear_tier:
                            item["runes"][idx] = eq[slot]["runes"][idx]
                            break
                    else:
                        inv.append(eq[slot].copy())
                break

        if not gear_found:
            print(f"[Warning] Gear {gear_id} (tier {gear_tier}) not found for {session.current_character}")
            return

        break
    else:
        print(f"[Warning] Character {session.current_character} not found")
        return

    # Save updated data
    # 2) Sync session.player_data and persist
    session.player_data["characters"] = session.char_list
    save_characters(session.user_id, session.char_list)
    print(f"[Save] Rune {rune_id} applied to slot {rune_slot} for gear {gear_id} (tier {gear_tier})")

    # Echo response to client
    bb = BitBuffer()
    bb.write_method_4(entity_id)
    bb.write_method_6(gear_id, GearType.GEARTYPE_BITSTOSEND)
    bb.write_method_6(gear_tier, GearType.const_176)
    bb.write_method_6(rune_id, class_64.const_101)
    bb.write_method_6(rune_slot, class_1.const_765)
    resp = struct.pack(
        ">HH", 0xB0, len(bb.to_bytes())) + bb.to_bytes()
    session.conn.sendall(resp)
    print(
        f"[Reply 0xB0] Echoed rune update: entity={entity_id}, gear={gear_id}, tier={gear_tier}, rune={rune_id}, slot={rune_slot}")

def send_look_update_packet(session, entity_id, head, hair, mouth, face, gender, hair_color, skin_color):
    """
    Send the look update packet (const_941) to a client session.

    Args:
        session: The client session object with a connection (session.conn).
        entity_id: The ID of the entity being updated (uint).
        head: Head appearance string.
        hair: Hair appearance string.
        mouth: Mouth appearance string.
        face: Face appearance string.
        gender: Gender string.
        shirt_color: Shirt color value (24-bit uint).
        pant_color: Pant color value (24-bit uint).
    """
    # Create a BitBuffer to build the payload
    bb = BitBuffer()

    # Write data according to the packet structure
    bb.write_method_4(entity_id)  # Entity ID (variable-length uint)
    bb.write_method_13(head)  # Head string
    bb.write_method_13(hair)  # Hair string
    bb.write_method_13(mouth)  # Mouth string
    bb.write_method_13(face)  # Face string
    bb.write_method_13(gender)  # Gender string
    bb.write_method_6(hair_color, EntType.CHAR_COLOR_BITSTOSEND)  # Shirt color (24 bits)
    bb.write_method_6(skin_color, EntType.CHAR_COLOR_BITSTOSEND)  # Pant color (24 bits)

    # Convert payload to bytes
    payload = bb.to_bytes()

    # Set packet type (adjust this value based on the actual const_941 value)
    packet_type = 0x8F  # Placeholder; replace with the correct value (e.g., 0x8F, 0x90, etc.)

    # Send packet: header (type, length) + payload
    session.conn.sendall(struct.pack(">HH", packet_type, len(payload)) + payload)

    # Optional logging for debugging
    print(f"[LookUpdate] Sent packet 0x{packet_type:02X} for entity {entity_id}")

def handle_change_look(session, raw_data, all_sessions):
    """
    Handle the look change request from the client (e.g., packet 0x8E),
    update both the live entity and the saved character data, persist,
    and broadcast the change.
    """
    # ─── (1) Parse incoming packet ────────────────────────────────────────────────
    payload = raw_data[4:]  # skip type+length
    br = BitReader(payload)

    head       = br.read_string()
    hair       = br.read_string()
    mouth      = br.read_string()
    face       = br.read_string()
    gender     = br.read_string()
    hair_color = br.read_bits(EntType.CHAR_COLOR_BITSTOSEND)
    skin_color = br.read_bits(EntType.CHAR_COLOR_BITSTOSEND)

    entity_id = session.clientEntID

    # ─── (2) In‑memory entity update ─────────────────────────────────────────────
    ent_states = getattr(session, "entity_states", None)
    if ent_states and entity_id in ent_states:
        ent = ent_states[entity_id]
        ent["headSet"]   = head
        ent["hairSet"]   = hair
        ent["mouthSet"]  = mouth
        ent["faceSet"]   = face
        ent["gender"]    = gender
        ent["hairColor"] = hair_color
        ent["skinColor"] = skin_color

    # ─── (3) Update per‑character saved data ────────────────────────────────────
    for char in session.player_data.get("characters", []):
        if char.get("name") == session.current_character:
            char["headSet"]   = head
            char["hairSet"]   = hair
            char["mouthSet"]  = mouth
            char["faceSet"]   = face
            char["gender"]    = gender
            char["hairColor"] = hair_color
            char["skinColor"] = skin_color
            break
    else:
        print(f"[Look] ERROR: character {session.current_character} not found")
        return

    # ─── (4) Persist to disk ─────────────────────────────────────────────────────
    save_characters(session.user_id, session.player_data["characters"])
    print(f"[Save] Look updated for {session.current_character}")

    # ─── (5) Send update back to requester ──────────────────────────────────────
    send_look_update_packet(
        session,
        entity_id,
        head, hair, mouth, face,
        gender, hair_color, skin_color
    )

    # ─── (6) Broadcast to nearby clients ────────────────────────────────────────
    for other in all_sessions:
        if (other is not session and
            other.world_loaded and
            other.current_level == session.current_level):
            send_look_update_packet(
                other,
                entity_id,
                head, hair, mouth, face,
                gender, hair_color, skin_color
            )


def handle_create_gearset(session, raw_data):
    """
    Packet 0xC7: client wants to create a new gear-set slot.
    Payload is a single uint: the new slot index.
    """
    payload = raw_data[4:]
    br = BitReader(payload)
    slot_idx = br.read_bits(GearType.const_348)
    print(f"[GearSet] Creating new slot #{slot_idx} for {session.current_character}")

    # update in-memory save
    pd = session.player_data
    chars = pd.get("characters", [])
    for char in chars:
        if char.get("name") != session.current_character:
            continue
        gs = char.setdefault("gearSets", [])
        # Insert a new gearset object with name and slots
        gearset = {
            "name": f"GearSet {slot_idx + 1}",
            "slots": [0] * (EntType.MAX_SLOTS - 1)  # 6 slots
        }
        if slot_idx < len(gs):
            gs[slot_idx] = gearset
        else:
            gs.append(gearset)
        break
    else:
        print(f"[WARNING] Character not found for create_gearset")
        return

    # persist
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(pd, f, indent=2)
    print(f"[Save] Created gearset slot {slot_idx} in {save_path}")

    # echo back so the client will show the "Enter name" popup
    session.conn.sendall(raw_data)

def handle_name_gearset(session, raw_data):
    """
    Packet 0xC8: client sends the chosen name for a gear-set.
    Payload is (slot_idx:3 bits, name:String with 16-bit length).
    """
    payload = raw_data[4:]
    print(f"[Debug] Payload: {payload.hex()}")
    br = BitReader(payload)
    slot_idx = br.read_bits(3)
    print(f"[Debug] slot_idx: {slot_idx}, bit_index: {br.bit_index}")
    length = br.read_bits(16)
    print(f"[Debug] String length: {length}")
    if length > br.remaining_bits() // 8:
        print(f"[Error] Invalid string length: {length}, remaining bytes: {br.remaining_bits() // 8}")
        return
    result_bytes = bytearray()
    for _ in range(length):
        result_bytes.append(br.read_bits(8))
    try:
        name = result_bytes.decode('utf-8')
    except UnicodeDecodeError:
        name = result_bytes.decode('latin1')
    print(f"[GearSet] Naming slot #{slot_idx} → {name} for {session.current_character}")

    # Update in-memory save
    pd = session.player_data
    chars = pd.get("characters", [])
    for char in chars:
        if char.get("name") != session.current_character:
            continue
        gs = char.setdefault("gearSets", [])
        if slot_idx < len(gs):
            gs[slot_idx]["name"] = name
        else:
            print(f"[Error] Gearset slot {slot_idx} does not exist")
            return
        break
    else:
        print(f"[WARNING] Character not found for name_gearset")
        return

    # Persist
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(pd, f, indent=2)
    print(f"[Save] Renamed gearset slot {slot_idx} to “{name}” in {save_path}")

    # Echo back to client
    session.conn.sendall(raw_data)

def handle_apply_gearset(session, raw_data):
    """
    Packet 0xC6: client assigns currently equipped gears to a gearset slot.
    Payload is a single uint: the gearset slot index (3 bits).
    """
    payload = raw_data[4:]
    br = BitReader(payload)
    slot_idx = br.read_bits(GearType.const_348)
    print(f"[GearSet] Assigning equipped gears to gearset #{slot_idx} for {session.current_character}")

    # Update in-memory save
    pd = session.player_data
    chars = pd.get("characters", [])
    for char in chars:
        if char.get("name") != session.current_character:
            continue
        gs = char.get("gearSets", [])
        if slot_idx >= len(gs):
            print(f"[Error] Gearset slot {slot_idx} does not exist")
            return
        eq = char.get("equippedGears", [])
        if len(eq) != EntType.MAX_SLOTS - 1:
            print(f"[Warning] equippedGears has {len(eq)} slots, expected {EntType.MAX_SLOTS - 1}")
            return
        # Copy gear IDs from equippedGears to gearSets[slot_idx]["slots"]
        gear_ids = [item.get("gearID", 0) for item in eq]
        gs[slot_idx]["slots"] = gear_ids
        print(f"[Debug] Assigned gear IDs to gearset #{slot_idx}: {gear_ids}")
        break
    else:
        print(f"[WARNING] Character not found for apply_gearset")
        return

    # Persist
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(pd, f, indent=2)
    print(f"[Save] Assigned equipped gears to gearset slot {slot_idx} in {save_path}")

    # Echo back to client
    session.conn.sendall(raw_data)

def handle_update_equipment(session, raw_data):
    """
    Packet 0x30: client updates equipped gears for a gearset.
    Payload is (entity_id, followed by 6 slots: 1-bit changed flag, optional gear_id).
    """
    payload = raw_data[4:]
    print(f"[Debug] Payload: {payload.hex()}")
    br = BitReader(payload)
    entity_id = br.read_method_4()
    print(f"[Equipment] Updating for entity={entity_id}, character={session.current_character}")

    # Update in-memory save
    pd = session.player_data
    chars = pd.get("characters", [])
    for char in chars:
        if char.get("name") != session.current_character:
            continue
        eq = char.setdefault("equippedGears", [])
        inv = char.setdefault("inventoryGears", [])
        # Ensure equippedGears has 6 slots
        while len(eq) < EntType.MAX_SLOTS - 1:
            eq.append({"gearID": 0, "tier": 0, "runes": [0, 0, 0], "colors": [0, 0]})
        if len(eq) > EntType.MAX_SLOTS - 1:
            eq[:] = eq[:EntType.MAX_SLOTS - 1]
        # Process 6 slots
        updates = {}
        for slot in range(EntType.MAX_SLOTS - 1):
            if br.remaining_bits() < 1:
                print(f"[Error] Not enough bits to read slot {slot} changed flag")
                return
            changed = br.read_bits(1)
            if changed:
                if br.remaining_bits() < GearType.GEARTYPE_BITSTOSEND:
                    print(f"[Error] Not enough bits to read gear ID for slot {slot}")
                    return
                gear_id = br.read_method_6(GearType.GEARTYPE_BITSTOSEND)
                updates[slot] = gear_id
        # Apply updates
        for slot, gear_id in updates.items():
            for item in inv:
                if item.get("gearID") == gear_id:
                    eq[slot] = item.copy()
                    break
            else:
                print(f"[Warning] Gear ID {gear_id} not found in inventory for slot {slot}")
                eq[slot] = {"gearID": 0, "tier": 0, "runes": [0, 0, 0], "colors": [0, 0]}
        print(f"[Equipment] Updated slots: {updates}")
        break
    else:
        print(f"[WARNING] Character not found for update_equipment")
        return

    # Persist
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(pd, f, indent=2)
    print(f"[Save] Updated equippedGears for {session.current_character} in {save_path}")

    # Echo back to client
    session.conn.sendall(raw_data)

def magic_forge_packet(session, data):
    payload = data[4:]
    br = BitReader(payload)
    idols_to_spend = br.read_method_9()
    print(f"[{session.addr}] Speed‑up request: spend {idols_to_spend} idols")

    chars = session.player_data.get("characters", [])
    char = next((c for c in chars if c.get("name") == session.current_character), None)
    if char is None:
        print(f"[{session.addr}] Character {session.current_character} not found")
        return

    mf        = char.setdefault("magicForge", {})
    available = char.get("mammothIdols", 0)

    # ONLY check hasSession (i.e. an upgrade in progress), not status==1
    if mf.get("hasSession") and available >= idols_to_spend:
        # 1) Deduct idols
        char["mammothIdols"] = available - idols_to_spend

        # 2) Cancel the scheduled completion, if any
        sched_id = mf.get("schedule_id")
        if sched_id is not None:
            try:
                scheduler.cancel(sched_id)
                print(f"[{session.addr}] Canceled scheduled forge completion (id={sched_id})")
            except Exception as e:
                print(f"[{session.addr}] Failed to cancel scheduler id={sched_id}: {e}")
        mf.pop("schedule_id", None)

        # 3) Mark forge as completed via speed‑up
        mf["status"]   = class_111.const_264  # completed via speed‑up
        mf["duration"] = 0
        mf["hasSession"] = False

        # 4) Persist save
        save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(session.player_data, f, indent=2)

        # 5) Build & send the 0xCD “forge update” response
        bb = BitBuffer()
        bb.write_method_6(mf.get("primary", 0), class_1_const_254)
        bb.write_method_91(mf.get("var_2675", 0))
        bb.write_method_91(mf.get("var_2316", 0))
        bb._append_bits(0, 1)  # no secondary/usedlist

        resp_payload = bb.to_bytes()
        resp = struct.pack(">HH", 0xCD, len(resp_payload)) + resp_payload
        session.conn.sendall(resp)
        print(f"[{session.addr}] Sent 0xCD forge‑update (speed‑up applied)")

    else:
        print(f"[{session.addr}] Speed‑up denied: hasSession={mf.get('hasSession')}, idols={available}")

#TODO... for every collect the forge should gain level XP
def collect_forge_charm(session, data):
    """
    Handle 0xD0 "collect charm" from client:
    - Grant the player the charm they just forged (computed full ID)
    - Clear out the forge session
    - Persist save
    - Reply with an empty 0xD0 ack
    """
    chars = session.player_data.get("characters", [])
    char = next((c for c in chars if c.get("name") == session.current_character), None)
    if char is None:
        print(f"[{session.addr}] Character {session.current_character} not found")
        return

    mf = char.get("magicForge", {})
    if not mf.get("hasSession", False):
        print(f"[{session.addr}] No active forge session to collect")
        return

    # Compute full charm ID
    primary = mf.get("primary", 0)
    secondary = mf.get("secondary", 0)
    var_8 = mf.get("var_8", 0)
    charm_id = (primary & 0x1FF) | ((secondary & 0x1F) << 9) | ((var_8 & 0x3) << 14)

    if primary <= 0:
        print(f"[{session.addr}] Invalid primary ID: {primary}")
    else:
        charms = char.setdefault("charms", [])
        for entry in charms:
            if entry.get("charmID") == charm_id:
                entry["count"] = entry.get("count", 0) + 1
                break
        else:
            charms.append({"charmID": charm_id, "count": 1})
        print(f"[{session.addr}] Granted charmID={charm_id}. New charms: {char['charms']}")

    # Clear forge session
    mf.update({
        "hasSession": False,
        "primary": 0,
        "secondary": 0,
        "status": 0,
        "duration": 0,
        "var_8": 0,
        "usedlist": 0,
        "var_2675": 0,
        "var_2316": 0,
        "var_2434": False
    })

    # Save file
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(session.player_data, f, indent=2)
    print(f"[{session.addr}] Forge session cleared and saved")

    # Reply with 0xD0 ACK
    resp = struct.pack(">HH", 0xD0, 0)
    session.conn.sendall(resp)
    print(f"[{session.addr}] Sent 0xD0 collect-ack")
#TODO... implement the proper system to calculate the runnes  for each craft and the timers
def start_forge_packet(session, data):
    """
    Handle 0xB1: client clicked Craft on the Magic Forge.
    Also deducts materials and consumables from the character’s save,
    updates the session.char_list, and persists the result.
    """
    payload = data[4:]
    br = BitReader(payload)

    # 1) Read primary gem ID
    primary = br.read_bits(class_1_const_254)
    print(f"[{session.addr}] Forge start: primary gemID={primary}")

    # 2) Read materials list
    materials_used = {}
    while br.read_bit():  # method_15(true)
        mat_id = br.read_bits(class_8.const_658)
        count = br.read_bits(class_8.const_731)
        materials_used[mat_id] = count
    print(f"[{session.addr}] Forge materials: {materials_used}")

    # 3) Read consumable flags (4 total)
    consumable_flags = [br.read_bit() for _ in range(4)]
    print(f"[{session.addr}] Forge consumables flags: {consumable_flags}")

    # 4) Locate the character dict in session.char_list
    char = next((c for c in session.char_list
                 if c["name"] == session.current_character), None)
    if not char:
        print(f"[{session.addr}] ERROR: character not found for forge start")
        return

    # 5) Deduct materials
    mats = char.setdefault("materials", [])
    for mat_id, used in materials_used.items():
        for entry in mats:
            if entry["materialID"] == mat_id:
                entry["count"] = max(0, entry["count"] - used)
                break
        else:
            mats.append({"materialID": mat_id, "count": 0})

    # 6) Deduct consumables
    consumable_ids = [
        class_3.var_1415,
        class_3.var_2082,
        class_3.var_1374,
        class_3.var_1462
    ]
    cons = char.setdefault("consumables", [])
    for flag, cid in zip(consumable_flags, consumable_ids):
        if flag:
            for entry in cons:
                if entry["consumableID"] == cid:
                    entry["count"] = max(0, entry["count"] - 1)
                    break
            else:
                cons.append({"consumableID": cid, "count": 0})

    # 7) Decide if the result has a secondary buff
    import random, time
    has_secondary = random.random() < 0.25  # 25%
    secondary    = random.randint(1, 9) if has_secondary else 0
    var_8        = 1 if has_secondary else 0

    # 8) Start the forge session on the character
    mf = char.setdefault("magicForge", {})
    mf.update({
        "hasSession": True,
        "primary": primary,
        "secondary": secondary,
        "status": class_111.const_286,  # in-progress
        "duration": 60000,              # ms
        "_start_time": time.time(),     # timestamp
        "var_8": var_8,
        "usedlist": 0,
        "var_2675": 0,
        "var_2316": 0,
        "var_2434": True
    })

    # 9) Sync and persist initial in‑progress state
    session.player_data["characters"] = session.char_list
    save_characters(session.user_id, session.char_list)
    print(f"[{session.addr}] Forge session started and saved")

    # 10) Schedule completion callback
    now = int(time.time())
    # duration is in ms
    run_at = now + (mf["duration"] // 1000)
    schedule_forge(session.user_id,
                   session.current_character,
                   run_at,
                   primary,
                   secondary)
    print(f"[{session.addr}] Forge completion scheduled at {run_at}")


def cancel_forge_packet(session, data):
    """
    Handle 0xE1: client clicked Cancel on the Magic Forge.
    Clears the session so the UI resets.
    """
    print(f"[{session.addr}] Cancel‑forge request received")

    # 1) Find the character in the save
    chars = session.player_data.get("characters", [])
    char = next((c for c in chars if c["name"] == session.current_character), None)
    if char is None:
        print(f"[{session.addr}] ERROR: character not found for cancel forge")
        return

    # 2) Clear the forge session (no gem, no secondary, no timer)
    mf = char.setdefault("magicForge", {})
    mf["hasSession"] = False
    mf["status"]     = 0
    mf["duration"]   = 0
    mf["primary"]    = 0
    mf["secondary"]  = 0
    mf["var_8"]      = 0
    mf["usedlist"]   = 0
    mf["var_2675"]   = 0
    mf["var_2316"]   = 0
    mf["var_2434"]   = False

    # 3) Persist the change
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(session.player_data, f, indent=2)
    print(f"[{session.addr}] Forge session canceled and save updated")

def allocate_talent_points(session, data):
    """
    Handle 0xD3: client sent new craftTalentPoints.
    Packet payload is one method_9-packed integer containing
    five 4-bit values: [p0, p1, p2, p3, p4].
    """
    payload = data[4:]
    br = BitReader(payload)
    packed = br.read_method_9()
    # Unpack five 4‑bit fields: index i at bits (i*4 .. i*4+3)
    points = [(packed >> (i * 4)) & 0xF for i in range(5)]
    print(f"[{session.addr}] Allocate talent points: {points}")

    # Update save
    chars = session.player_data.setdefault("characters", [])
    char = next((c for c in chars if c["name"] == session.current_character), None)
    if not char:
        print(f"[{session.addr}] ERROR: character not found for talent allocation")
        return

    char["craftTalentPoints"] = points

    # Persist
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(session.player_data, f, indent=2)
    print(f"[{session.addr}] Saved new craftTalentPoints for {char['name']}")

def use_forge_xp_consumable(session, data):
    """
    Handle 0x110: player used a forge‑XP consumable.
    Deduct one consumable and award forge XP (capped at 159,948).
    """
    payload = data[4:]
    br = BitReader(payload)

    # Read consumableID
    cid = br.read_bits(class_3.const_69)
    print(f"[{session.addr}] Forge XP consumable used: consumableID={cid}")

    # Get character
    chars = session.player_data.get("characters", [])
    char = next((c for c in chars if c.get("name") == session.current_character), None)
    if not char:
        print(f"[{session.addr}] ERROR: character not found")
        return

    # Deduct from inventory
    cons = char.setdefault("consumables", [])
    for entry in cons:
        if entry["consumableID"] == cid:
            entry["count"] = max(0, entry["count"] - 1)
            break
    else:
        print(f"[{session.addr}] Warning: consumable {cid} not in inventory")

    # Award XP (capped)
    xp_gain = 4000
    current_xp = char.get("craftXP", 0)
    max_xp = 159_948
    new_xp = min(current_xp + xp_gain, max_xp)
    char["craftXP"] = new_xp

    print(f"[{session.addr}] Forge XP +{xp_gain} (capped), total now = {char['craftXP']}")

    # Save file
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(session.player_data, f, indent=2)
    print(f"[{session.addr}] Save updated with capped forge XP")

def handle_private_message(session, data, all_sessions):
    payload = data[4:]
    try:
        br = BitReader(payload)
        recipient_name = br.read_method_13()
        message = br.read_method_13()
        print(f"[{session.addr}] [PKT46] Private message from {session.current_character} to {recipient_name}: {message}")

        # Find recipient session
        recipient_session = next(
            (s for s in all_sessions
             if s.current_character
             and s.current_character.lower() == recipient_name.lower()
             and s.authenticated),
            None
        )

        # Build 0x47 packet
        bb = BitBuffer()
        bb.write_method_13(session.current_character)  # Sender's name
        bb.write_method_13(message)                   # Raw message
        payload_out = bb.to_bytes()
        pkt = struct.pack(">HH", 0x47, len(payload_out)) + payload_out

        if recipient_session:
            # Send to recipient
            recipient_session.conn.sendall(pkt)
            print(f"[{session.addr}] [PKT47] Sent private message to {recipient_session.addr} ({recipient_session.current_character})")
            # Send to sender
            session.conn.sendall(pkt)
            print(f"[{session.addr}] [PKT47] Sent private message to sender {session.addr} ({session.current_character})")
        else:
            print(f"[{session.addr}] [PKT46] Recipient {recipient_name} not found")
            err = f"Player {recipient_name} not found".encode("utf-8")
            pl = struct.pack(">H", len(err)) + err
            session.conn.sendall(struct.pack(">HH", 0x1B, len(pl)) + pl)

    except Exception as e:
        print(f"[{session.addr}] [PKT46] Parse error: {e}, raw payload = {payload.hex()}")



def Client_Crash_Reports(session, data):
    """
    Read a CLIENT ERROR (0x7C) packet and log it.
    No response is sent back.
    """
    # unpack the two‐byte packet ID and two‐byte length
    _, length = struct.unpack_from(">HH", data, 0)
    # extract exactly `length` bytes of payload
    payload = data[4:4 + length]
    try:
        msg = payload.decode("utf-8", errors="replace")
    except Exception:
        msg = repr(payload)
    print(f"[{session.addr}] CLIENT ERROR (0x7C): {msg}")

def handle_packet_0x41(session, data, conn):
    if len(data) < 4:
        return
    payload_length = struct.unpack(">H", data[2:4])[0]
    if len(data) != 4 + payload_length:
        return
    payload = data[4:4 + payload_length]
    try:
        br = BitReader(payload)
        door_id = br.read_method_9()
    except Exception:
        return
    door_info = DOOR_MAP.get((session.current_level, door_id))
    bb = BitBuffer()
    bb.write_method_4(door_id)
    if door_info is None:
        bb.write_method_91(1)
        bb.write_method_13("")
    else:
        if isinstance(door_info, str):
            bb.write_method_91(1)
            bb.write_method_13(door_info)
        else:
            bb.write_method_91(door_info)
            bb.write_method_13("")
    payload = bb.to_bytes()
    response = struct.pack(">HH", 0x42, len(payload)) + payload
    conn.sendall(response)


def Start_Skill_Research(session, data, conn):
    br = BitReader(data[4:], debug=True)
    try:
        # --- 1) Parse the incoming 0xBE packet ---
        ability_id = br.read_bits(7)
        rank       = br.read_bits(4)
        is_instant = bool(br.read_bit())
        print(f"[{session.addr}] [PKT0xBE] Parsed skill upgrade: "
              f"abilityID={ability_id}, rank={rank}, isInstant={is_instant}")

        # --- 2) Auth & character lookup ---
        if not session.authenticated or not session.current_character:
            raise ValueError("Not authenticated or no character selected")

        char = next((c for c in session.char_list
                     if c.get("name") == session.current_character), None)
        if not char:
            raise ValueError(f"Character {session.current_character} not found")

        # --- 3) Validate ability & rank ---
        ability_data = get_ability_info(ability_id, rank)
        if not ability_data:
            raise LookupError(f"Invalid ability/rank ({ability_id}, {rank})")
        if rank > 10:
            raise ValueError("Rank exceeds maximum (10)")

        # --- 4) Check Tome rank from stats_by_building ---
        mf = char.setdefault("magicForge", {})
        stats_dict = mf.setdefault("stats_by_building", {})
        # BuildingID for Tome is "1" in your mapping
        tome_rank = stats_dict.get("1", 0)
        if rank > tome_rank:
            raise ValueError("Upgrade requires a higher Tome rank")

        # --- 5) Deduct gold if not instant ---
        if not is_instant:
            curr_gold = char.get("gold", 0)
            cost      = int(ability_data["goldCost"])
            if curr_gold < cost:
                raise ValueError("Not enough gold for upgrade")
            char["gold"] = curr_gold - cost

        # --- 6) Schedule the research ---
        ready_ts = int(time.time()) + (0 if is_instant else int(ability_data["upgradeTime"]))
        char["research"] = {
            "abilityID": ability_id,
            "ReadyTime": ready_ts,
            "done": False,
        }
        save_characters(session.user_id, session.char_list)
        print(f"[{session.addr}] Started research for {char['name']} → ReadyTime={ready_ts}")

        # --- 7) Queue completion callback ---
        scheduler.schedule(
            run_at=ready_ts,
            callback=lambda uid=session.user_id, cname=char["name"]:
                         _on_research_done_for(uid, cname)
        )

        # --- 8) Immediate “in progress” reply (0xBF) ---
        bb = BitBuffer()
        bb.insert_bits(1, 16)            # placeholder building ID
        bb.insert_bits(2, 8)             # status = in progress
        bb.insert_bits(ability_id, 7)
        bb.insert_bits(rank, 4)
        payload = bb.to_bytes()
        conn.sendall(struct.pack(">HH", 0xBF, len(payload)) + payload)
        print(f"[{session.addr}] [PKT0xBE] Sent 0xBF confirmation len={len(payload)}")

    except (ValueError, LookupError) as err:
        print(f"[{session.addr}] [PKT0xBE] Error: {err}")
        conn.sendall(build_popup_packet(str(err), disconnect=False))

    except Exception as ex:
        print(f"[{session.addr}] [PKT0xBE] Unexpected error: {ex}")
        conn.sendall(build_popup_packet("Invalid skill upgrade request", disconnect=False))





def handle_research_claim(session):
    """
    Handle packet 0xD1: player claims completed skill research.
    """
    char = next((c for c in session.char_list if c["name"] == session.current_character), None)
    if not char:
        print(f"[{session.addr}] No character found to complete research")
        return

    research = char.get("research")
    if not research or not research.get("done"):
        print(f"[{session.addr}] No completed research to claim")
        return

    ability_id = research["abilityID"]

    # Find or add ability
    learned = char.setdefault("learnedAbilities", [])
    for ab in learned:
        if ab["abilityID"] == ability_id:
            ab["rank"] += 1
            break
    else:
        learned.append({"abilityID": ability_id, "rank": 1})

    print(f"[{session.addr}] Claimed research: abilityID={ability_id}")

    # Instead of deleting, reset the research block to a neutral "done" state
    char["research"] = {
        "abilityID": 0,
        "ReadyTime": 0,
        "done": True
    }

    save_characters(session.user_id, session.char_list)

def Skill_Research_Cancell_Request(session):
    """
    Handles research cancellation (0xDD).
    Resets research state and optionally refunds gold.
    """
    char = next((c for c in session.char_list if c["name"] == session.current_character), None)
    if not char:
        print(f"[{session.addr}] Cannot cancel research: No character found")
        return

    research = char.get("research")
    if not research or research.get("done"):
        print(f"[{session.addr}] No active research to cancel")
        return

    ability_id = research.get("abilityID")
    ready_time = research.get("ReadyTime")
    now = int(time.time())

    # === Configurable gold refund percentage ===
    REFUND_PERCENT = 0.0  # set to 0.5 for 50% refund if needed

    # === Determine current rank of the ability ===
    learned = char.get("learnedAbilities", [])
    current_rank = 0
    for ab in learned:
        if ab["abilityID"] == ability_id:
            current_rank = ab["rank"]
            break

    next_rank = current_rank + 1

    # === Replace this with your actual gold cost function ===
    def calculate_research_cost(ability_id: int, rank: int) -> int:
        # Dummy placeholder logic
        return 1000 * rank + 500

    full_cost = calculate_research_cost(ability_id, next_rank)
    refund_amount = int(full_cost * REFUND_PERCENT)

    # Cancel research and refund
    char["research"] = {
        "abilityID": 0,
        "ReadyTime": 0,
        "done": True
    }

    char["gold"] = char.get("gold", 0) + refund_amount

    print(f"[{session.addr}] Research cancelled: abilityID={ability_id}, refunded {refund_amount}")
    save_characters(session.user_id, session.char_list)

def Skill_SpeedUp(session, data):
    """
    Handles skill research speed-up request (0xDE).
    Deducts idols and completes the research immediately.
    Sends 0xBF confirmation back to the client.
    """
    br = BitReader(data[4:])
    idol_cost = br.read_method_9()

    char = next((c for c in session.char_list if c["name"] == session.current_character), None)
    if not char:
        print(f"[{session.addr}] Cannot speed up research: No character found")
        return

    research = char.get("research")
    if not research or research.get("done"):
        print(f"[{session.addr}] Cannot speed up: No active research or already done")
        return

    if idol_cost > 0:
        current_idols = char.get("mammothIdols", 0)
        if current_idols < idol_cost:
            print(f"[{session.addr}] Not enough idols for speed-up: required={idol_cost}, have={current_idols}")
            return
        char["mammothIdols"] = current_idols - idol_cost

    # Complete the research instantly
    research["ReadyTime"] = 0
    research["done"] = True

    save_characters(session.user_id, session.char_list)

    # Send 0xBF confirmation packet
    bb = BitBuffer()
    bb.insert_bits(research["abilityID"], 7)
    payload = bb.to_bytes()

    session.conn.sendall(struct.pack(">HH", 0xBF, len(payload)) + payload)

    print(f"[{session.addr}] Speed-up complete: abilityID={research['abilityID']}, cost={idol_cost}")

def PaperDoll_Request(session, data, conn):
    """
    Handles paperdoll request (0x19). Reads character name,
    finds the character in session.char_list, and sends back
    a 0x1A response with their paperdoll or empty if not found.
    """
    name = BitReader(data[4:]).read_string()
    print(f"[{session.addr}] [PKT0x19] Request for paperdoll: {name}")

    for c in session.char_list:
        if c["name"] == name:
            pd = build_paperdoll_packet(c)
            conn.sendall(struct.pack(">HH", 0x1A, len(pd)) + pd)
            print(f"[{session.addr}] [PKT0x19] Found and sent paperdoll for '{name}'")
            break
    else:
        # Character not found, send empty packet
        conn.sendall(struct.pack(">HH", 0x1A, 0))
        print(f"[{session.addr}] [PKT0x19] Character '{name}' not found. Sent empty paperdoll.")

def handle_building_upgrade(session, data):
    load_building_data()

    try:
        # --- 1) Parse the incoming 0xD7 packet ---
        payload = data[4:]
        if len(payload) < 2:
            raise ValueError("Malformed 0xD7 payload")

        br = BitReader(payload, debug=True)
        building_id = br.read_bits(5)
        client_rank = br.read_bits(5)
        is_instant  = bool(br.read_bit())

        rank = client_rank + 1

        print(f"[{session.addr}] [PKT0xD7] Upgrade request: "
              f"ID={building_id}, rank={client_rank+1}, isInstant={is_instant}")

        # --- 2) Lookup character & current rank ---
        char = next(c for c in session.char_list
                    if c["name"] == session.current_character)

        # Get current rank from stats_by_building dict (default 0)
        mf = char.setdefault("magicForge", {})
        stats_dict = mf.setdefault("stats_by_building", {})
        current_rank = stats_dict.get(str(building_id), 0)

        # Determine the new rank
        rank = 1 if current_rank == 0 else current_rank + 1

        # --- 3) Cost & time from your data table ---
        bdata        = find_building_data(building_id, rank)
        gold_cost    = int(bdata["GoldCost"])
        upgrade_time = int(bdata["UpgradeTime"])

        # --- 4) Deduct gold if not instant ---
        if not is_instant:
            if char.get("gold", 0) < gold_cost:
                raise ValueError("Not enough gold")
            char["gold"] -= gold_cost

        # --- 5) Compute finish timestamp ---
        now        = int(time.time())
        ready_time = now if is_instant else now + upgrade_time

        # --- 6) Persist the pending upgrade ---
        char["buildingUpgrade"] = {
            "buildingID": building_id,
            "rank": rank,
            "ReadyTime": ready_time,
            "done": False,
            "isInstant": is_instant
        }
        save_characters(session.user_id, session.char_list)

        # --- 7) Fire or schedule completion ---
        if is_instant:
            # Will update stats_by_building & send 0xD8 completion
            _on_building_done_for(session.user_id, session.current_character)
        else:
            schedule_building_upgrade(
                session.user_id,
                session.current_character,
                ready_time
            )

    except Exception as e:
        print(f"[{session.addr}] [PKT0xD7] Error: {e}")



def handle_speedup_request(session, data):
    """
    Handle packet 0xDC (speed‑up using Mammoth Idols).
    Payload is: [ header(4 bytes) | body... ]
    The body is a bit‑packed value written via method_9(cost).
    """
    # --- Parse the incoming packet ---
    payload = data[4:]
    br = BitReader(payload, debug=True)
    try:
        idol_cost = br.read_method_9()
    except Exception as e:
        print(f"[{session.addr}] [PKT0xDC] failed to parse payload: {e}")
        return

    print(f"[{session.addr}] [PKT0xDC] Speed‑up requested with cost={idol_cost}")

    # --- Look up the character ---
    char = next((c for c in session.char_list
                 if c.get("name") == session.current_character), None)
    if not char:
        print(f"[{session.addr}] [PKT0xDC] no current character")
        return

    # --- Verify idol balance ---
    curr_idols = char.get("mammothIdols", 0)
    if curr_idols < idol_cost:
        print(f"[{session.addr}] [PKT0xDC] not enough idols ({curr_idols} < {idol_cost})")
        return
    char["mammothIdols"] = curr_idols - idol_cost

    # --- Get pending upgrade info ---
    bu = char.get("buildingUpgrade", {})
    building_id = bu.get("buildingID")
    new_rank     = bu.get("rank")
    if not building_id or new_rank is None:
        print(f"[{session.addr}] [PKT0xDC] no pending buildingUpgrade to speed‑up")
        save_characters(session.user_id, session.char_list)
        return

    # --- Mark the upgrade done and record the new rank ---
    bu["done"] = True

    # Store stats in a dict keyed by building ID
    stats_dict = char.setdefault("magicForge", {}).setdefault("stats_by_building", {})
    stats_dict[str(building_id)] = new_rank

    # --- Clear the pending upgrade request ---
    bu.update({
        "buildingID": 0,
        "rank": 0,
        "ReadyTime": 0,
        "done": False,
        "isInstant": False
    })

    # --- Persist changes ---
    save_characters(session.user_id, session.char_list)

    # --- Mirror updates in in‑memory list ---
    mem_char = next((c for c in session.char_list
                     if c.get("name") == session.current_character), None)
    if mem_char:
        mem_char["mammothIdols"] = char["mammothIdols"]
        mem_char.setdefault("magicForge", {})["stats_by_building"] = stats_dict.copy()

    # --- Send success response (0xD8) ---
    try:
        status_byte = (1 & 0b11111) << 3  # 1 = completed
        out_payload = bytes([status_byte])
        session.conn.sendall(
            struct.pack(">HH", 0xD8, len(out_payload)) + out_payload
        )
        print(f"[{session.addr}] [PKT0xDC] sped‑up building ID={building_id} to rank={new_rank}")
    except Exception as e:
        print(f"[{session.addr}] [PKT0xDC] failed to send completion: {e}")



def handle_cancel_upgrade(session, data):
    """
    Handle packet 0xDB (CancelUpgrade).
    Resets the 'buildingUpgrade' object to default empty state.
    """
    char = next((c for c in session.char_list
                 if c.get("name") == session.current_character), None)
    if not char:
        return

    # Ensure buildingUpgrade key exists and reset its fields
    char["buildingUpgrade"] = {
        "buildingID": 0,
        "rank": 0,
        "ReadyTime": 0,
        "done": False,
        "isInstant": False
    }

    save_characters(session.user_id, session.char_list)
    print(f"[{session.addr}] [PKT0xDB] Building upgrade canceled and reset")

    # Send back 0xD8 status = 0 to tell client there's no active upgrade
    status_byte = (0 & 0b11111) << 3
    payload = bytes([status_byte])
    session.conn.sendall(struct.pack(">HH", 0xE3, len(payload)) + payload)
    print(f"[{session.addr}] Sent 0xD8 with status=0 after cancel")



def handle_train_talent_point(session, data):
    """
    Handle 0xD4: client started talent‐point research.
    Payload = [ header(4) | 2‐bit classIndex | 1‐bit isInstant ]
    """
    payload = data[4:]
    br = BitReader(payload, debug=True)

    # 1) Read master‐class index (2 bits) and instant flag (1 bit)
    try:
        class_index = br.read_bits(2)
        is_instant  = bool(br.read_bit())
    except Exception as e:
        print(f"[{session.addr}] [PKT0xD4] parse error: {e}")
        return

    print(f"[{session.addr}] [PKT0xD4] Research request: classIndex={class_index}, isInstant={is_instant}")

    # 2) Lookup character
    char = next((c for c in session.char_list
                 if c.get("name") == session.current_character), None)
    if not char:
        print(f"[{session.addr}] [PKT0xD4] no such character")
        return

    # 3) Determine cost & duration
    #    class_index+1 because arrays are 1‐based in client
    idx = class_index + 1
    duration = class_66.RESEARCH_DURATIONS [idx]
    cost     = class_66.RESEARCH_COSTS [idx]

    # 4) Deduct gold if not instant
    if not is_instant:
        if char.get("gold", 0) < cost:
            print(f"[{session.addr}] [PKT0xD4] insufficient gold ({char.get('gold')} < {cost})")
            # Optionally send popup here
            return
        char["gold"] -= cost

    # 5) Compute ready timestamp
    now = int(time.time())
    ready_ts = now if is_instant else now + duration

    # 6) Store pending talent research
    char["talentResearch"] = {
        "classIndex": class_index,
        "ReadyTime":  ready_ts,
        "done":       False,
        "isInstant":  is_instant
    }
    save_characters(session.user_id, session.char_list)
    print(f"[{session.addr}] Talent research stored → ReadyTime={ready_ts}")

    # 7) Schedule or immediate callback
    if is_instant:
        _on_talent_done_for(session.user_id, session.current_character)
    else:
        # use the correctly named helper
        schedule_Talent_point_research(
            session.user_id,
            session.current_character,
            ready_ts
        )

def handle_talent_speedup(session, data):
    """
    Handle 0xE0: client clicked Speed‑up on talent research.
    Payload: [ header(4) | method_9(idolCost) ]
    """
    # 1) Parse cost
    payload = data[4:]
    br = BitReader(payload, debug=True)
    try:
        idol_cost = br.read_method_9()
    except Exception as e:
        print(f"[{session.addr}] [0xE0] parse error: {e}")
        return

    print(f"[{session.addr}] [0xE0] Talent speed‑up requested: cost={idol_cost}")

    # 2) Locate the character
    char = next((c for c in session.char_list
                 if c.get("name") == session.current_character), None)
    if not char:
        print(f"[{session.addr}] [0xE0] no character found")
        return

    # 3) Deduct idols
    curr_idols = char.get("mammothIdols", 0)
    if curr_idols < idol_cost:
        print(f"[{session.addr}] [0xE0] insufficient idols ({curr_idols} < {idol_cost})")
        return
    char["mammothIdols"] = curr_idols - idol_cost

    # 4) Grab pending research
    tr = char.get("talentResearch", {})
    class_idx = tr.get("classIndex")
    if class_idx is None or tr.get("done", False):
        print(f"[{session.addr}] [0xE0] nothing to speed‑up")
        save_characters(session.user_id, session.char_list)
        return

    # 5) Cancel scheduler if stored
    sched_id = tr.pop("schedule_id", None)
    if sched_id is not None:
        try:
            scheduler.cancel(sched_id)
            print(f"[{session.addr}] Canceled talent schedule id={sched_id}")
        except Exception:
            pass

    # 6) Reset research timer so client will send 0xD6 claim
    tr["ReadyTime"] = 0
    tr["isInstant"] = True  # mark as instant

    # 7) Persist & mirror updated data
    save_characters(session.user_id, session.char_list)
    mem = next((c for c in session.char_list
                if c.get("name") == session.current_character), None)
    if mem:
        mem["mammothIdols"] = char["mammothIdols"]
        mem["talentResearch"] = tr.copy()

    # 8) Send the 0xD5 “complete” notification to trigger client claim
    try:
        bb = BitBuffer()
        # format: 2-bit class index, 1-bit flag (ignored by client)
        bb.insert_bits(class_idx, class_66.const_571)
        bb.insert_bits(1, 1)
        payload = bb.to_bytes()
        session.conn.sendall(struct.pack(">HH", 0xD5, len(payload)) + payload)
        print(f"[{session.addr}] [0xE0] sent 0xD5 to complete talent research")
    except Exception as e:
        print(f"[{session.addr}] [0xE0] failed to send 0xD5: {e}")


def handle_talent_claim(session, data):
    """
    Handle 0xD6: client claiming a completed talent research.
    Payload is usually empty (client writes no bits), so we ignore status.
    """
    # Try to read classIndex, but fall back if there's nothing to read
    payload = data[4:]
    br = BitReader(payload, debug=True)
    try:
        class_idx = br.read_bits(class_66.const_571)
    except Exception:
        # No bits in payload: grab from pending research
        char = next((c for c in session.char_list
                     if c.get("name") == session.current_character), None)
        if not char:
            return
        tr = char.get("talentResearch", {})
        class_idx = tr.get("classIndex")
        if class_idx is None:
            return

    print(f"[{session.addr}] [0xD6] Talent claim for classIndex={class_idx}")

    # Lookup the character
    char = next((c for c in session.char_list
                 if c.get("name") == session.current_character), None)
    if not char:
        print(f"[{session.addr}] [0xD6] no character found")
        return

    # Award the point if it's still pending
    tr = char.get("talentResearch", {})
    # Only award if it's not already done
    if not tr.get("done", False):
        pts = char.setdefault("talentPoints", {})
        pts[str(class_idx)] = pts.get(str(class_idx), 0) + 1

        # Mark the research as done & clear it
        char["talentResearch"] = {
            "classIndex": None,
            "ReadyTime":  0,
            "done":       True,
            "isInstant":  False
        }

        # Persist
        save_characters(session.user_id, session.char_list)

        # Mirror in-memory
        mem = next((c for c in session.char_list
                    if c.get("name") == session.current_character), None)
        if mem:
            mem.setdefault("talentPoints", {})[str(class_idx)] = pts[str(class_idx)]
            mem["talentResearch"] = char["talentResearch"].copy()

        print(f"[{session.addr}] [0xD6] Awarded talent point for classIndex={class_idx}")
    else:
        print(f"[{session.addr}] [0xD6] nothing to claim, already done")



def handle_hp_increase_notice(session, data):
    """
    Handle 0xBB: client reports maxHP increase (delta).
    Payload: [header(4) | delta:int16]
    """
    if len(data) < 6:
        print(f"[{session.addr}] [0xBB] malformed packet (len={len(data)})")
        return

    delta = struct.unpack(">h", data[4:6])[0]
    print(f"[{session.addr}] [0xBB] Client reported maxHP increase: ΔHP = {delta}")

def handle_char_regen(session, data):
    """
    Handle 0x78 - PKTTYPE_CHAR_REGEN
    Payload: uint32 (entity ID), int16 (HP delta)
    """
    if len(data) < 10:
        print(f"[{session.addr}] [0x78] Malformed packet (len={len(data)})")
        return

    entity_id = struct.unpack(">I", data[4:8])[0]
    hp_delta = struct.unpack(">h", data[8:10])[0]  # signed short

    print(f"[{session.addr}] [0x78] Character regen: Entity {entity_id} gains {hp_delta} HP")

    # Optional: apply regen to in-memory entity state if you track it
    ent = session.get_entity_by_id(entity_id)
    if ent:
        ent.heal(hp_delta)
    else:
        print(f"[{session.addr}] Entity {entity_id} not found")


def handle_volume_enter(session, data):
     pass

def handle_change_offset_y(session, data):
    payload = data[4:]
    br = BitReader(payload, debug=True)

    try:
        ent_id = br.read_method_9()
        offset_y = br.read_method_706()

        print(f"[PKT125] ent_id={ent_id}, offset_y={offset_y}")

        entity = session.get_entity(ent_id)
        if entity:
            entity.target_offset_y = offset_y
        else:
            print(f"[PKT125] Unknown entity ID: {ent_id}")

    except Exception as e:
        print(f"[{session.addr}] [PKT125] Error parsing packet: {e}")

# Helpers
#############################################

# updates players consumables inventory when a  consumable is used
def send_consumable_update(conn, consumable_id: int, new_count: int):
    bb = BitBuffer()
    bb.write_method_6(consumable_id, class_3.const_69)
    bb.write_method_4(new_count)
    body = bb.to_bytes()
    packet = struct.pack(">HH", 0x10C, len(body)) + body
    conn.sendall(packet)

#handled
#############################################

def handle_mount_equip_packet(session, data, all_sessions):
    """
    Handle packet type 0xB2 for equipping a mount on an entity.
    Parses the payload to extract Entity ID and Mount ID, prints them,
    and updates the character's equipped mount.
    """
    if data[:2] != b'\x00\xb2':
        return
    payload = data[4:]
    reader = BitReader(payload, debug=True)

    try:
        # Read Entity ID (method_4)
        entity_id = reader.read_method_4()
        # Read Mount ID (7 bits, as per class_20.const_297)
        mount_id = reader.read_method_6(7)

        print(f"[{session.addr}] [PKT0xB2] Entity ID: {entity_id}, Mount ID: {mount_id}")

        # Validate and update character's equipped mount
        for char in session.char_list:
            if char.get("name") == session.current_character:
                # Check if the mount is owned
                owned_mounts = char.get("mounts", [])
                if mount_id not in owned_mounts and mount_id != 0:  # 0 might mean unequip
                    print(f"[{session.addr}] [PKT0xB2] Invalid mount ID {mount_id} for {session.current_character}")
                    return
                # Update equipped mount
                char["equippedMount"] = mount_id
                session.player_data["characters"] = session.char_list
                save_characters(session.user_id, session.char_list)
                print(f"[{session.addr}] [PKT0xB2] Equipped mount ID {mount_id} for {session.current_character}")
                break
        else:
            print(f"[{session.addr}] [WARNING] Character {session.current_character} not found for PKT0xB2")

        # Broadcast to other sessions (optional, based on game design)
        for other in all_sessions:
            if other is not session and other.world_loaded and other.current_level == session.current_level:
                other.conn.sendall(data)
                print(f"[{session.addr}] [PKT0xB2] Broadcasted mount update to {other.addr}")

    except Exception as e:
        print(f"[{session.addr}] [PKT0xB2] Error parsing packet: {e}")
        for line in reader.get_debug_log():
            print(line)


def handle_emote_begin(session, data, all_sessions):
    """
    Packet 0x7E: an entity starts an emote.
    Client sends:
      method_9(entityID) -> var-int via write_method_4
      method_26(emoteString)
    Other clients read:
      method_4() for ID, method_13() for the string.
    """
    # 0) Validate header & auth
    if data[:2] != b'\x00\x7e':
        return
    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKT7E] Ignored: not authenticated or no character")
        return

    # 1) Parse the emote packet
    payload = data[4:]
    br = BitReader(payload, debug=False)
    try:
        entity_id = br.read_method_4()
        emote     = br.read_method_13()
    except Exception as e:
        print(f"[{session.addr}] [PKT7E] Parse error: {e}, raw={payload.hex()}")
        return

    print(f"[{session.addr}] [PKT7E] Entity {entity_id} began emote \"{emote}\"")

    # 2) Broadcast unchanged packet to all other clients in the same level
    for other in all_sessions:
        if (other is not session
            and other.world_loaded
            and other.current_level == session.current_level):
            try:
                other.conn.sendall(data)
            except Exception as e:
                print(f"[{session.addr}] [PKT7E] Error forwarding to {other.addr}: {e}")

def handle_entity_destroy(session, data, all_sessions):
    """
    Packet 0x0D: an entity is destroyed/removed.
    Client sends: method_9(entityID)
    We'll parse, remove from our map, and broadcast to peers.
    """
    # 1) Validate header & auth
    if data[:2] != b'\x00\x0d' or not session.authenticated:
        return

    # 2) Parse payload
    payload = data[4:]
    br = BitReader(payload, debug=False)
    try:
        # Client uses method_9 to write the ID:
        entity_id = br.read_method_9()
        # No boolean is actually written by the client, so we don't consume extra bits.
    except Exception as e:
        print(f"[{session.addr}] [PKT0D] Parse error: {e}, raw={payload.hex()}")
        return

    #print(f"[{session.addr}] [PKT0D] Entity destroy for ID {entity_id}")

    # 3) Remove from this session's entity map
    if entity_id in session.entities:
        del session.entities[entity_id]
        #print(f"[{session.addr}] [PKT0D] Removed entity {entity_id} from server map")

    # If this was the player, clear clientEntID
    if session.clientEntID == entity_id:
        session.clientEntID = None

    # 4) Broadcast to peers
    for other in all_sessions:
        if (other is not session
            and other.world_loaded
            and other.current_level == session.current_level):
            try:
                other.conn.sendall(data)
                print(f"[{session.addr}] [PKT0D] Broadcasted destroy to {other.addr}")
            except Exception as e:
                print(f"[{session.addr}] [PKT0D] Error sending to {other.addr}: {e}")

def PKTTYPE_BUFF_TICK_DOT(session, data, all_sessions):
    # 0) Quick header/auth check
    if data[:2] != b'\x00\x79' or not session.authenticated:
        return

    # 1) Strip off 0x79 + length, feed to BitReader
    payload = data[4:]
    br = BitReader(payload, debug=False)
    try:
        # ✔️ Make sure to CALL each read_method_*
        target_id     = br.read_method_4()
        source_id     = br.read_method_4()
        power_type_id = br.read_method_4()
        amount        = br.read_method_45()
        flags         = br.read_method_6(Game.const_390)
    except Exception as e:
        print(f"[{session.addr}] [PKT79] Parse error: {e}, raw={payload.hex()}")
        return

    print(f"[{session.addr}] [PKT79] Buff tick: target={target_id}, "
          f"source={source_id}, power={power_type_id}, amount={amount}")

    # 2) Rebroadcast the exact same bytes to peers
    for other in all_sessions:
        if (other is not session
            and other.world_loaded
            and other.current_level == session.current_level):
            try:
                other.conn.sendall(data)
            except Exception as e:
                print(f"[{session.addr}] [PKT79] Forward error to {other.addr}: {e}")

def handle_request_respawn(session, data, all_sessions):
    # 1) Validate header & auth
    if data[:2] != b'\x00\x77' or not session.authenticated:
        return

    # 2) Parse use_potion flag
    br = BitReader(data[4:], debug=False)
    try:
        use_potion = bool(br.read_bit())
    except:
        return

    # 3) Deduct a potion server-side and update client inventory
    if use_potion:
        for char in session.char_list:
            if char['name'] == session.current_character:
                for item in char.get('consumables', []):
                    if item.get('consumableID') == 9:
                        if item['count'] > 0:
                            item['count'] -= 1
                            new_count = item['count']
                            print(f"[{session.addr}] [PKT77] Used potion, new count={new_count}")
                            # 3a) Persist save
                            save_characters(session.user_id, session.char_list)
                            # 3b) Inform client of new count
                            send_consumable_update(session.conn, 9, new_count)
                        # if count was zero, we silently proceed (client will handle empty)
                        break
                break

    # 4) Send RESPAWN_COMPLETE (0x80)
    spawn_pos = 0  # or compute actual spawn X
    bb = BitBuffer()
    bb.write_signed_method_45(spawn_pos)
    bb._append_bits(1 if use_potion else 0, 1)
    body = bb.to_bytes()
    session.conn.sendall(struct.pack(">HH", 0x80, len(body)) + body)

    # 5) Immediately restore health via CHAR_REGEN (0x78)
    heal_amount = 10000
    bb2 = BitBuffer()
    bb2.write_method_9(session.clientEntID or 0)
    bb2.write_method_24(heal_amount)
    body2 = bb2.to_bytes()
    session.conn.sendall(struct.pack(">HH", 0x78, len(body2)) + body2)

    print(f"[{session.addr}] [PKT77] Respawned at {spawn_pos}, potion_used={use_potion}")

def handle_respawn_ack(session, data, all_sessions):
    # 0x82: client confirms it has respawned
    if data[:2] != b'\x00\x82' or not session.authenticated:
        return

    br = BitReader(data[4:], debug=False)
    try:
        entity_id = br.read_method_9()
        spawn_pos = br.read_method_24()
        used_potion = bool(br.read_bit())
    except Exception as e:
        print(f"[{session.addr}] [PKT82] Parse error: {e}")
        return

    # Update server state: mark entity alive at spawn_pos
    ent = session.entities.get(entity_id)
    if ent is not None:
        ent['pos_x'] = spawn_pos
        ent['pos_y'] = 0    # or default
        ent['is_alive'] = True
        print(f"[{session.addr}] [PKT82] Entity {entity_id} respawned at {spawn_pos}, potion={used_potion}")

        # Optionally broadcast to peers: raw 0x82 or a custom update
        for other in all_sessions:
            if other is not session and other.world_loaded and other.current_level == session.current_level:
                other.conn.sendall(data)
    else:
        print(f"[{session.addr}] [PKT82] Unknown entity {entity_id}")




def _send_error(conn, msg):
    encoded = msg.encode("utf-8")
    payload = struct.pack(">H", len(encoded)) + encoded
    conn.sendall(struct.pack(">HH", 0x102, len(payload)) + payload)


def handle_group_invite(session, data, all_sessions):
    """
    Packet 0x65: /invite <player>
    Only the invitee gets the 0x58 invite packet.
    No confirmation packet is sent back to the inviter.
    """
    # 0) Validate header & auth
    if data[:2] != b'\x00\x65':
        return
    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKT65] Ignored: not authenticated or no character")
        return

    # 1) Parse invitee name
    payload = data[4:]
    try:
        br = BitReader(payload, debug=False)
        invitee_name = br.read_method_13()
    except Exception as e:
        print(f"[{session.addr}] [PKT65] Parse error: {e}, raw={payload.hex()}")
        return

    print(f"[{session.addr}] [PKT65] Group invite from {session.current_character} to {invitee_name}")


    # 2) Find the invitee’s session
    invitee = next((
        s for s in all_sessions
        if s.authenticated
           and s.current_character
           and s.current_character.lower() == invitee_name.lower()
    ), None)

    if not invitee:
        _send_error(session.conn, f"Player {invitee_name} not found")
        print(f"[{session.addr}] [PKT65] Invitee {invitee_name} not found")
        return

    # 3) Ensure inviter has a group_id
    if not getattr(session, 'group_id', None):
        session.group_id = secrets.randbits(16)
        session.group_members = [session]
        print(f"[{session.addr}] [PKT65] Created group {session.group_id}")

    # 4) Reject if invitee already in a group
    if getattr(invitee, 'group_id', None):
        _send_error(session.conn, f"{invitee_name} is already in a group")
        print(f"[{session.addr}] [PKT65] {invitee_name} already in group {invitee.group_id}")
        return

    # 5) Send the invite (0x58) to the invitee only
    bb = BitBuffer()
    inviter_id   = session.clientEntID or 0
    inviter_name = session.current_character
    invite_text  = f"{inviter_name} has invited you to join a party"

    bb.write_method_9(inviter_id)
    bb.write_method_26(inviter_name)
    bb.write_method_26(invite_text)
    body = bb.to_bytes()
    invite_packet = struct.pack(">HH", 0x58, len(body)) + body
    invitee.conn.sendall(invite_packet)
    print(f"[{session.addr}] [PKT65] Sent 0x58 invite to {invitee.current_character}")


def handle_public_chat(session, data, all_sessions):
    """
    Packet 0x2C: global (level-wide) chat.
    Client sends: method_9(entity_id), method_26(message)
    Server rebroadcasts same format.
    """
    # 0) Header check
    if data[:2] != b'\x00\x2c':
        return
    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKT2C] Ignored: not authenticated or no character")
        return

    # 1) Parse incoming packet
    payload = data[4:]
    try:
        br = BitReader(payload, debug=False)
        entity_id = br.read_method_9()    # client used method_9
        message   = br.read_method_13()   # readMethod13 pairs with writer method_26

    except Exception as e:
        print(f"[{session.addr}] [PKT2C] Error parsing chat: {e}, raw={payload.hex()}")
        return

    print(f"[{session.addr}] [PKT2C] Chat from {entity_id} ({session.current_character}): {message}")

    # 2) Build the rebroadcast packet
    bb = BitBuffer()
    bb.write_method_9(entity_id)
    bb.write_method_26(message)
    body = bb.to_bytes()
    header = struct.pack(">HH", 0x2C, len(body))
    packet = header + body

    # 3) Send to everyone else in the same level
    for other in all_sessions:
        if other is session:
            continue
        if not other.world_loaded or other.current_level != session.current_level:
            continue
        try:
            other.conn.sendall(packet)
            print(f"[{session.addr}] [PKT2C] → \"{message}\" to {other.addr} ({other.current_character})")
        except Exception as e:
            print(f"[{session.addr}] [PKT2C] Error sending to {other.addr}: {e}")

def handle_remove_buff(session, data, all_sessions):
    """
    Packet 0x0C: “remove buff” — client telling server to remove a buff.
    Mirrors AS3 method_1837:
      method_9(entity.id),
      method_9(buffTypeID),
      method_9(param2)
    """
    # 0) Validate header & auth
    if data[:2] != b'\x00\x0c':
        return
    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKT0C] Ignored: not authenticated or no character")
        return

    # 1) Strip header
    payload = data[4:]
    br = BitReader(payload, debug=False)

    try:
        # 2) Read all three var‐ints
        entity_id   = br.read_method_9()  # param1.id
        buff_type   = br.read_method_9()  # param2
        instance_id = br.read_method_9()  # param3

        # 3) Log parsed values
        props = {
            'entity_id':   entity_id,
            'buff_type':   buff_type,
            'instance_id': instance_id,
        }
        #print(f"[{session.addr}] [PKT0C] Parsed remove-buff:")
        #pprint.pprint(props, indent=4)

        # 4) Broadcast unchanged packet to peers
        for other in all_sessions:
            if (other is not session
                and other.world_loaded
                and other.current_level == session.current_level):
                other.conn.sendall(data)
                print(f"[{session.addr}] [PKT0C] Broadcasted to {other.addr}")

    except Exception as e:
        print(f"[{session.addr}] [PKT0C] Error parsing remove-buff: {e}, raw={payload.hex()}")
        if br.debug:
            for line in br.get_debug_log():
                print(line)

def handle_add_buff(session, data, all_sessions):
    """
    Packet 0x0B: “add buff” — applies a buff/debuff with optional numeric modifiers.
    Mirrors AS3 method_1262:
      method_9(entity.id),
      method_9(param2),
      method_9(param3),
      method_9(param5),
      method_9(param4),
      method_9(param6),
      method_15(vector!=null),
      [vector length + (powerNodeTypeID, modCount, modValues...)]
    """
    # 0) Validate header & auth
    if data[:2] != b'\x00\x0b':
        return
    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKT0B] Ignored: not authenticated or no character")
        return

    # 1) Strip header
    payload = data[4:]
    br = BitReader(payload, debug=False)

    try:
        # 2) Read the six uints (all via method_9)
        entity_id  = br.read_method_9()
        param2     = br.read_method_9()
        param3     = br.read_method_9()
        param5     = br.read_method_9()   # note: client writes param5 _before_ param4
        param4     = br.read_method_9()
        param6     = br.read_method_9()

        # 3) Optional Vector.<class_140>
        has_vector = bool(br.read_bit())
        vector     = []
        if has_vector:
            length = br.read_method_9()
            for _ in range(length):
                power_node_type_id = br.read_method_9()
                mod_count          = br.read_method_9()
                mods               = [br.read_method_560() for _ in range(mod_count)]
                vector.append({
                    'power_node_type_id': power_node_type_id,
                    'mod_values':         mods
                })

        # 4) Log parsed values
        props = {
            'entity_id': entity_id,
            'param2':     param2,
            'param3':     param3,
            'param4':     param4,
            'param5':     param5,
            'param6':     param6,
            'vector':     vector if has_vector else None
        }
        #print(f"[{session.addr}] [PKT0B] Parsed add-buff:")
        #pprint.pprint(props, indent=4)

        # 5) Broadcast unchanged packet to peers
        for other in all_sessions:
            if (other is not session
                and other.world_loaded
                and other.current_level == session.current_level):
                other.conn.sendall(data)

    except Exception as e:
        print(f"[{session.addr}] [PKT0B] Error parsing add-buff: {e}, raw={payload.hex()}")
        if br.debug:
            for line in br.get_debug_log():
                print(line)


def handle_projectile_explode(session, data, all_sessions):
    """
    Packet 0x0E: “projectile explode” event.
    Mirrors AS3 WriteProjectileExplode:
      method_9(entity.id),
      method_9(remoteMissileID),
      method_24(param3), method_24(param4),
      method_15(flag)
    """
    # 0) Validate header
    if data[:2] != b'\x00\x0e':
        return
    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKT0E] Ignored: not authenticated or no character")
        return

    # 1) Strip packet header
    payload = data[4:]
    br = BitReader(payload, debug=False)

    try:
        # 2) Read projectile owner entity ID and the missile’s remote ID
        entity_id       = br.read_method_9()
        remote_missile  = br.read_method_9()

        # 3) Read explosion position (24-bit var‐int)
        x = br.read_method_24()
        y = br.read_method_24()

        # 4) Read the final flag (e.g. “spawn splatter”)
        flag = bool(br.read_bit())

        # 5) Log for verification
        props = {
            'entity_id':      entity_id,
            'remote_missile': remote_missile,
            'x':              x,
            'y':              y,
            'flag':           flag,
        }
        #print(f"[{session.addr}] [PKT0E] Parsed projectile-explode:")
        #pprint.pprint(props, indent=4)

        # 6) Broadcast raw packet to peers
        for other in all_sessions:
            if (other is not session
                and other.world_loaded
                and other.current_level == session.current_level):
                other.conn.sendall(data)

    except Exception as e:
        print(f"[{session.addr}] [PKT0E] Error parsing projectile explode: {e}, raw={payload.hex()}")
        if br.debug:
            for line in br.get_debug_log():
                print(line)


def handle_power_hit(session, data, all_sessions):
    """
    Packet 0x0A: “power hit” event — source hit target, with optional extra params.
    Mirrors AS3 method_1092 exactly.
    """
    # 0) Validate header
    if data[:2] != b'\x00\x0a':
        return
    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKT0A] Ignored: not authenticated or no character")
        return

    # 1) Strip packet header
    payload = data[4:]
    br = BitReader(payload, debug=False)

    try:
        # 2) Read IDs (both written with method_9 in AS3)
        target_id = br.read_method_9()   # param3.id in client
        source_id = br.read_method_9()   # param1.id in client

        # 3) Read damage/effect value as 24-bit
        value     = br.read_method_24()  # param4

        # 4) Read powerID (var-int)
        power_id  = br.read_method_9()   # param2.powerID

        # 5) Optional param5 (var-int)
        has_p5    = bool(br.read_bit())
        param5    = br.read_method_9() if has_p5 else 0

        # 6) Optional param6 (var-int)
        has_p6    = bool(br.read_bit())
        param6    = br.read_method_9() if has_p6 else 0

        # 7) Final boolean flag (crit? or similar)
        param7    = bool(br.read_bit())

        # 8) Log what we got
        props = {
            'target_id': target_id,
            'source_id': source_id,
            'value':      value,
            'power_id':   power_id,
            'param5':     param5 if has_p5 else None,
            'param6':     param6 if has_p6 else None,
            'flag':       param7,
        }
        #print(f"[{session.addr}] [PKT0A] Parsed power-hit:")
        #pprint.pprint(props, indent=4)

        # 9) Broadcast unchanged packet to other clients
        for other in all_sessions:
            if (other is not session
                and other.world_loaded
                and other.current_level == session.current_level):
                other.conn.sendall(data)

    except Exception as e:
        print(f"[{session.addr}] [PKT0A] Error parsing power-hit: {e}, raw={payload.hex()}")
        if br.debug:
            for line in br.get_debug_log():
                print(line)

def handle_power_cast(session, data, all_sessions):
    if data[:2] != b'\x00\x09': return
    if not session.authenticated or not session.current_character:
        return

    payload = data[4:]
    br = BitReader(payload, debug=False)

    try:
        ent_id   = br.read_method_9()
        power_id = br.read_method_9()

        # ← CORRECTED TARGET‐POINT HANDSHAKE
        _ = br.read_bit()                        # discard hasTargetEntity
        has_target_pos = bool(br.read_bit())     # var_2846: does this power type support coords?
        target_pt = None
        if has_target_pos:
            target_x = br.read_method_24()
            target_y = br.read_method_24()
            target_pt = (target_x, target_y)

        # projectile
        has_proj = bool(br.read_bit())
        proj_id  = br.read_method_9() if has_proj else None

        # charged flag
        is_charged = bool(br.read_bit())

        # melee‐combo / var_674 branch
        has_extra = bool(br.read_bit())
        secondary_id = tertiary_id = None
        if has_extra:
            is_secondary = bool(br.read_bit())
            if is_secondary:
                secondary_id = br.read_method_9()
            else:
                tertiary_id = br.read_method_9()

        # cooldown & mana
        has_flags = bool(br.read_bit())
        cooldown_tick = mana_cost = None
        if has_flags:
            if bool(br.read_bit()):
                cooldown_tick = br.read_method_9()
            if bool(br.read_bit()):
                MANA_BITS = PowerType.const_423
                mana_cost = br.read_method_6(MANA_BITS)

        props = {
            'caster_ent_id': ent_id,
            'power_id':      power_id,
            'target_pt':     target_pt,
            'projectile_id': proj_id,
            'is_charged':    is_charged,
            'secondary_id':  secondary_id,
            'tertiary_id':   tertiary_id,
            'cooldown_tick': cooldown_tick,
            'mana_cost':     mana_cost,
        }
        #print(f"[{session.addr}] [PKT09] Parsed power-cast:")
        #pprint.pprint(props, indent=4)

        # broadcast to peers
        for other in all_sessions:
            if (other is not session
                and other.world_loaded
                and other.current_level == session.current_level):
                other.conn.sendall(data)

    except Exception as e:
        print(f"[{session.addr}] [PKT09] Error parsing power-cast: {e}")
        if br.debug:
            for line in br.get_debug_log():
                print(line)

def handle_linkupdater(session, data, all_sessions):
    # Only handle 0xA2 internally
    if data[:2] != b'\x00\xa2':
        return
    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKTA2] Ignored: not auth or no char")
        return

    payload = data[4:]
    br = BitReader(payload, debug=False)
    try:
        client_time = br.read_method_24()
        is_desync   = bool(br.read_bit())
        server_time = br.read_method_24()

        # Update our session’s clock‐sync info
        session.client_elapsed  = client_time
        session.server_elapsed  = server_time
        session.clock_desynced  = is_desync
        session.clock_offset_ms = server_time - client_time

        #print(f"[{session.addr}] [PKTA2] Sync: client={client_time}ms "
        #      f"server={server_time}ms desync={is_desync} offset={session.clock_offset_ms}ms")

        #TODO...
        # If the client thinks we’re badly out of sync, we can reply here
        # response = build_clock_correction_packet(...)
        # session.conn.sendall(response)

    except Exception as e:
        print(f"[{session.addr}] [PKTA2] Error parsing link-sync: {e}")

def handle_entity_full_update(session, data, all_sessions):
    """
    Handle a full entity spawn/update (packet type 0x08) from a client.
    Parses the entity data, learns the client's own entity ID, maintains a server-side
    entity map, and broadcasts the same packet to other clients in the same level.
    """
    # Only handle 0x08
    if data[:2] != b'\x00\x08':
        return

    # Must be authenticated and have a character
    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKT08] Ignored: not authenticated or no character")
        return

    # Extract payload (skip packet type and length)
    payload = data[4:]
    br = BitReader(payload, debug=True)

    try:
        # Read core fields
        entity_id = br.read_method_9()
        pos_x      = br.read_method_24()
        pos_y      = br.read_method_24()
        velocity_x = br.read_method_24()
        ent_name   = br.read_method_13()
        # Use correct bit width for team (matches client’s Entity.TEAM_BITS)
        TEAM_BITS = Entity.TEAM_BITS # adjust if client uses different value
        team       = br.read_method_6(TEAM_BITS)
        is_player  = bool(br.read_bit())
        # y_offset uses AS3 method_706 → read via signed prefix encoding
        y_offset   = br.read_method_739()

        # Read optional cue data
        has_cue = bool(br.read_bit())
        cue_data = {}
        if has_cue:
            if bool(br.read_bit()):
                cue_data['character_name'] = br.read_method_13()
            if bool(br.read_bit()):
                cue_data['drama_anim'] = br.read_method_13()
            if bool(br.read_bit()):
                cue_data['sleep_anim'] = br.read_method_13()

        # Optional summoner
        has_summoner = bool(br.read_bit())
        summoner_id = br.read_method_9() if has_summoner else None

        # Optional power
        has_power = bool(br.read_bit())
        power_id  = br.read_method_9() if has_power else None

        # State and flags
        # Use correct bit width for entity state (matches client’s Entity.const_316)
        STATE_BITS = Entity.const_316  # adjust to actual number of state bits
        ent_state = br.read_method_6(STATE_BITS)
        b_left    = bool(br.read_bit())
        b_running = bool(br.read_bit())
        b_jumping = bool(br.read_bit())
        b_dropping = bool(br.read_bit())
        b_backpedal = bool(br.read_bit())

        # 1) Learn client's own entity ID
        if is_player and session.clientEntID is None:
            session.clientEntID = entity_id
            print(f"[{session.addr}] [PKT08] Learned clientEntID = {entity_id}")

        # 2) Build properties dict
        props = {
            'pos_x': pos_x,
            'pos_y': pos_y,
            'velocity_x': velocity_x,
            'ent_name': ent_name,
            'team': team,
            'is_player': is_player,
            'y_offset': y_offset,
            'cue_data': cue_data,
            'summoner_id': summoner_id,
            'power_id': power_id,
            'ent_state': ent_state,
            'b_left': b_left,
            'b_running': b_running,
            'b_jumping': b_jumping,
            'b_dropping': b_dropping,
            'b_backpedal': b_backpedal
        }
        # Nicely print parsed entity properties
        #print(f"[{session.addr}] [PKT08] Parsed entity {entity_id}:")
        #pprint.pprint(props, indent=4)

        # 3) Add or update server-side map
        if entity_id in session.entities:
            session.entities[entity_id].update(props)
        else:
            session.entities[entity_id] = props
            #print(f"[{session.addr}] [PKT08] Added new entity {entity_id}")

        # 4) Mark world as loaded once first batch is received
        if not session.world_loaded:
            session.world_loaded = True

        # 5) Broadcast raw packet to peers
        for other in all_sessions:
            if other is not session and other.world_loaded and other.current_level == session.current_level:
                other.conn.sendall(data)
                # Optionally log broadcast:
                #print(f"[{session.addr}] [PKT08] Broadcasted to {other.addr}")

    except Exception as e:
        print(f"[{session.addr}] [PKT08] Error parsing packet: {e}")
        if br.debug:
            for log_line in br.get_debug_log():
                print(log_line)

def handle_entity_incremental_update(session, data, all_sessions):
    # Only handle 0x07
    if data[:2] != b'\x00\x07':
        return

    if not session.authenticated or not session.current_character:
        print(f"[{session.addr}] [PKT07] Ignored: not authenticated or no character")
        return

    payload = data[4:]
    br = BitReader(payload, debug=True)

    try:
        # 1) Read caster/entity ID
        entity_id = br.read_method_4()

        is_self = (entity_id == session.clientEntID)
        if not is_self and entity_id not in session.entities:
            print(f"[{session.addr}] [PKT07] Unknown entity {entity_id} movement dropped")
            return


        # 2) Read deltas
        delta_x  = br.read_method_24()
        delta_y  = br.read_method_24()
        delta_vx = br.read_method_24()

        # 3) Read state & flags
        STATE_BITS = Entity.const_316
        ent_state = br.read_method_6(STATE_BITS)
        flags = {
            'b_left':      bool(br.read_bit()),
            'b_running':   bool(br.read_bit()),
            'b_jumping':   bool(br.read_bit()),
            'b_dropping':  bool(br.read_bit()),
            'b_backpedal': bool(br.read_bit()),
        }

        # 4) Airborne check
        is_airborne = bool(br.read_bit())
        velocity_y = br.read_method_24() if is_airborne else 0

        # ────────────────────────────────────────────────────────────
        # ← NEW: always use last-full-update coords if available
        ent = session.entities.get(entity_id, {})
        old_x = ent.get('pos_x')
        old_y = ent.get('pos_y')

        # Determine spawn/origin based on memory and level type
        current_level = session.current_level
        lvl_cfg = LEVEL_CONFIG.get(current_level, (None,) * 4)
        is_dungeon = lvl_cfg[3]

        if old_x is None or old_y is None:
            # no full-update seen yet, fall back to file or default
            spawn = SPAWN_POINTS.get(session.current_level, {'x': 0, 'y': 0})
            old_x, old_y = spawn['x'], spawn['y']
            # you could still inspect char-list here if you really want extra fallback
        # ────────────────────────────────────────────────────────────

        # 5) Compute new absolute position
        new_x = old_x + delta_x
        new_y = old_y + delta_y

        # 6) Update server-side map
        ent.update({
            'pos_x':      new_x,
            'pos_y':      new_y,
            'velocity_x': ent.get('velocity_x', 0) + delta_vx,
            'velocity_y':  velocity_y,
            'ent_state':   ent_state,
            **flags
        })
        session.entities[entity_id] = ent

        # 7) Persist file only when non-dungeon and truly moving
        if ent.get('is_player') and not is_dungeon:
            for char in session.char_list:
                if char['name'] == session.current_character:
                    char['CurrentLevel'] = {'name': session.current_level, 'x': new_x, 'y': new_y}
                    save_characters(session.user_id, session.char_list)
                    break

        #print(f"[{session.addr}] [PKT07] Player moved to absolute=({new_x},{new_y}), state={ent_state}")

        # 8) Broadcast raw packet to peers
        for other in all_sessions:
            if other is not session and other.world_loaded and other.current_level == session.current_level:
                other.conn.sendall(data)

    except Exception as e:
        print(f"[{session.addr}] [PKT07] Error parsing packet: {e}")
        for line in br.get_debug_log():
            print(line)


def handle_start_skit(session, data, all_sessions):
    """
    Handle packet 0xC5: Client requests to start or stop a skit for an entity.
    - Reads entity ID, boolean flag, and text.
    - Sends PKT_ROOM_THOUGHT (0x76) only if flag is True.
    """
    payload = data[4:]  # Strip 4-byte header
    br = BitReader(payload, debug=True)

    try:
        entity_id = br.read_method_9()
        flag = bool(br.read_bit())
        text = br.read_method_26()
    except Exception as e:
        print(f"[{session.addr}] [PKT0xC5] Error parsing packet: {e}")
        return

    if flag:
        bb = BitBuffer()
        bb.write_method_4(entity_id)
        bb.write_method_13(text)
        payload = bb.to_bytes()
        packet = struct.pack(">HH", 0x76, len(payload)) + payload

        for other_session in all_sessions:
            if other_session.world_loaded and other_session.current_level == session.current_level:
                other_session.conn.sendall(packet)

        print(f"[{session.addr}] [PKT0xC5] Sent skit message from entity {entity_id}: '{text}'")
    else:
        print(f"[{session.addr}] [PKT0xC5] Skit flag is False for entity {entity_id}, message suppressed")



def handle_hotbar_packet(session, raw_data):
    payload = raw_data[4:]
    reader = BitReader(payload)

    slot = 1
    updates = {}   # slot_index (0‑based) -> new skill_id
    while reader.remaining_bits() >= 1:
        changed = reader.read_bits(1)
        if changed:
            skill_id = reader.read_bits(7)
            updates[slot - 1] = skill_id
        slot += 1

    print(f"[Hotbar] Player {session.user_id} updates → {updates}")

    # 2) Locate the right character in the save
    for char in session.char_list:
        if char.get("name") == session.current_character:
            # 3) Fetch existing list, or default to zeros
            active = char.get("activeAbilities", [])
            # ensure it's long enough
            max_idx = max(updates.keys(), default=-1)
            while len(active) <= max_idx:
                active.append(0)

            # 4) Apply updates in‑place
            for idx, skill_id in updates.items():
                active[idx] = skill_id

            # 5) Store back
            char["activeAbilities"] = active
            break
    else:
        print(f"[WARNING] Character {session.current_character} not found in save!")
        return

    # 6) Persist full JSON
    session.player_data["characters"] = session.char_list
    save_characters(session.user_id, session.char_list)
    print(f"[Save] activeAbilities for {session.current_character} = {active} saved (user_id={session.user_id})")
