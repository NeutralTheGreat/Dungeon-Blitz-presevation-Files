import json, struct
import time

from Character import save_characters
from bitreader import BitReader
from constants import GearType, EntType, class_64, class_1, DyeType, class_118, method_277, GAME_CONST_209, \
    CLASS_118_CONST_127, class_111, class_1_const_254, class_8, class_3, class_64_const_218, class_111_const_432, \
    LinkUpdater, Entity
from BitUtils import BitBuffer
from constants import get_dye_color
from entity import Send_Entity_Data

SAVE_PATH_TEMPLATE = "saves/{user_id}.json"

def tick_forge_status(session):
    """
    Called periodically to check if the forge session has finished naturally.
    If duration is expired and session is still marked in-progress,
    convert it to status=2 and send a 0xCD packet to client.
    """
    chars = session.player_data.get("characters", [])
    char = next((c for c in chars if c.get("name") == session.current_character), None)
    if char is None:
        return

    mf = char.get("magicForge", {})

    # If no session or not in-progress, skip
    if not mf.get("hasSession") or mf.get("status") != class_111.const_286:
        return

    duration_ms = mf.get("duration", 0)
    if duration_ms <= 0:
        return

    # Determine when it started
    forge_start = mf.get("_start_time")
    if not forge_start:
        return

    now = time.time()
    if now >= forge_start + (duration_ms / 1000):
        mf["status"] = class_111.const_264  # completed state
        mf["duration"] = 0
        mf["var_8"] = 1 if mf.get("secondary") else 0

        # Save the update
        save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(session.player_data, f, indent=2)

        # Send 0xCD packet to update client
        bb = BitBuffer()
        bb.write_method_6(mf.get("primary", 0), class_1_const_254)
        bb.write_method_91(mf.get("var_2675", 0))
        bb.write_method_91(mf.get("var_2316", 0))
        bb._append_bits(1 if mf.get("var_8") else 0, 1)
        if mf.get("var_8"):
            bb.write_method_6(mf.get("secondary", 0), class_64_const_218)
            bb.write_method_6(mf.get("usedlist", 0), class_111_const_432)

        payload = bb.to_bytes()
        resp = struct.pack(">HH", 0xCD, len(payload)) + payload
        session.conn.sendall(resp)
        print(f"[{session.addr}] Forge auto-finish: 0xCD sent.")

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
    print(f"[Reply 0xC1] Mastery for class {mc}, slot_map keys: {sorted(slot_map.keys())}")

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

def handle_research_packet(session, raw_data):
    pd = session.player_data
    chars = pd.get("characters", pd if isinstance(pd, list) else [])
    for char in chars:
        if char.get("name") == session.current_character:
            char["towerResearch"] = {"masterClassID": 0, "endTime": 0}
            break

    with open(SAVE_PATH_TEMPLATE.format(user_id=session.user_id), "w", encoding="utf-8") as f:
        json.dump(pd, f, indent=2)

    session.conn.sendall(struct.pack(">HH", 0xDF, 0))
    print(f"[Reply 0xDF] Cleared research for {session.current_character}")

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

def handle_apply_dyes(session, entity_id, dyes_by_slot, preview_only, primary_dye, secondary_dye):
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
                char["shirtColor"] = color  # Store actual RGB int
            else:
                print(f"[Warning] Unknown primary dye ID: {primary_dye}")

        if secondary_dye is not None:
            color = get_dye_color(secondary_dye)
            if color is not None:
                char["pantColor"] = color
            else:
                print(f"[Warning] Unknown secondary dye ID: {secondary_dye}")

        break  # Done updating current character
    else:
        print(f"[Dyes] ERROR: character {session.current_character} not found")
        return

    # 2) Sync session.player_data and persist
    session.player_data["characters"] = session.char_list
    save_characters(session.user_id, session.char_list)
    print(f"[Save] Dye info applied for {session.current_character} and saved")

    # 3) Send the sync packet
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
    Handle the look change request from the client (e.g., packet 0x8E) and send back the update.

    Args:
        session: The client session object.
        raw_data: The raw packet data.
    """
    # Parse the incoming packet (assuming it matches the client's WriteChangeLook)
    payload = raw_data[4:]  # Skip header (type and length)
    br = BitReader(payload)  # Assuming you have a BitReader class

    head = br.read_string()
    hair = br.read_string()
    mouth = br.read_string()
    face = br.read_string()
    gender = br.read_string()
    hair_color = br.read_bits(EntType.CHAR_COLOR_BITSTOSEND)
    skin_color = br.read_bits(EntType.CHAR_COLOR_BITSTOSEND)

    # Update the character's data
    chars = session.player_data.get("characters", [])
    for char in chars:
        if char.get("name") == session.current_character:
            char["headSet"] = head
            char["hairSet"] = hair
            char["mouthSet"] = mouth
            char["faceSet"] = face
            char["gender"] = gender
            char["hairColor"] = hair_color
            char["skinColor"] = skin_color
            break

    # Save updated data to disk
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(session.player_data, f, indent=2)

    # Send the look update packet to the requesting client
    entity_id = session.clientEntID  # The entity ID of the character
    send_look_update_packet(session, entity_id, head, hair, mouth, face, gender, hair_color, skin_color)

    # Optionally broadcast to other clients in the same level
    for other_session in all_sessions:  # all_sessions should be a global or accessible list
        if (other_session != session and
                other_session.world_loaded and
                other_session.current_level == session.current_level):
            send_look_update_packet(other_session, entity_id, head, hair, mouth, face, gender, hair_color, skin_color)

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
    from constants import LinkUpdater, class_111, class_1_const_254, class_64_const_218, class_111_const_432

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

    # ONLY check hasSession, not status==1
    if mf.get("hasSession") and available >= idols_to_spend:
        # Deduct idols
        char["mammothIdols"] = available - idols_to_spend

        # Mark forge as sped‑up
        mf["status"]   = class_111.const_264  # completed via speed‑up
        mf["duration"] = 0


        # Persist save
        save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(session.player_data, f, indent=2)

        # Build the 0xCD “forge update” response
        bb = BitBuffer()
        bb.write_method_6(mf.get("primary", 0), class_1_const_254)
        bb.write_method_91(mf.get("var_2675", 0))
        bb.write_method_91(mf.get("var_2316", 0))
        bb._append_bits(0, 1)  # no secondary/usedlist

        resp_payload = bb.to_bytes()
        resp = struct.pack(">HH", 0xcd, len(resp_payload)) + resp_payload
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

    # 9) Sync session.player_data (if you still use it elsewhere)
    session.player_data["characters"] = session.char_list

    # 10) Persist to disk using your existing helper
    save_characters(session.user_id, session.char_list)
    print(f"[{session.addr}] Forge session started and saved")


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
        message        = br.read_method_13()
        print(f"[{session.addr}] [PKT46] Private message from {session.current_character} to {recipient_name}: {message}")

        # find recipient session
        recipient_session = next(
            (s for s in all_sessions
             if s.current_character
             and s.current_character.lower() == recipient_name.lower()
             and s.authenticated),
            None
        )

        if recipient_session:
            bb = BitBuffer()
            bb.write_method_13(session.current_character)  # sender
            bb.write_method_13(message)                   # message
            payload_out = bb.to_bytes()

            pkt = struct.pack(">HH", 0x47, len(payload_out)) + payload_out
            recipient_session.conn.sendall(pkt)
            print(f"[{session.addr}] [PKT47] Sent private message to {recipient_session.addr}")

        else:
            print(f"[{session.addr}] [PKT46] Recipient {recipient_name} not found")
            err = f"Player {recipient_name} not found".encode("utf-8")
            pl  = struct.pack(">H", len(err)) + err
            session.conn.sendall(struct.pack(">HH", 0x1B, len(pl)) + pl)

    except Exception as e:
        print(f"[{session.addr}] [PKT46] Parse error: {e}, raw payload = {payload.hex()}")


def handle_entity_update(session, data, all_sessions):
    # Sanity check
    if len(data) < 4:
        #print(f"[{session.addr}] [PKT07] Invalid packet (too short): raw={data.hex()}")
        return

    payload = data[4:]
    #print(f"[{session.addr}] [PKT07] Raw payload: {payload.hex()}")

    br = BitReader(payload, debug=False)
    try:
        # --- Read & validate entity ID ---
        ent_id = br.read_method_9()
        #print(f"[{session.addr}] [PKT07] Read ent_id = {ent_id}")
        if ent_id != session.clientEntID:
           # print(f"[{session.addr}] [PKT07] WRONG ent_id: {ent_id} vs clientEntID {session.clientEntID}")
            return

        # Ensure we have an entry
        if ent_id not in session.entities:
            session.entities[ent_id] = {
                "x": 360.0, "y": 1458.99, "z": 0.0,
                "entState": Entity.const_6,
                "is_player": True
            }

        entity = session.entities[ent_id]

        # --- Read movement deltas ---
        dx  = br.read_int24();  #print(f"[{session.addr}] [PKT07] dx = {dx}")
        dy  = br.read_int24();  #(f"[{session.addr}] [PKT07] dy = {dy}")
        dvx = br.read_int24();  #print(f"[{session.addr}] [PKT07] dvx = {dvx}")

        # Compute new pos/vel
        entity['x'] = entity.get('x', 360.0) + dx
        entity['y'] = entity.get('y', 1458.99) + dy
        entity['velocity_x'] = entity.get('velocity_x', 0) + (dvx * LinkUpdater.VELOCITY_DEFLATE)
        #print(f"[{session.addr}] [PKT07] Updated x,y = ({entity['x']:.2f}, {entity['y']:.2f}), vx = {entity['velocity_x']:.2f}")

        # --- Read entity state ---
        ent_state = br.read_method_6(Entity.const_316)
        #print(f"[{session.addr}] [PKT07] ent_state = {ent_state}")
        entity['entState'] = ent_state

        # --- Read input flags ---
        flags = {
            "left":     bool(br.read_bit()),
            "running":  bool(br.read_bit()),
            "jumping":  bool(br.read_bit()),
            "dropping": bool(br.read_bit()),
            "backpedal":bool(br.read_bit())
        }
        #print(f"[{session.addr}] [PKT07] flags = {flags}")
        entity.update(flags)

        # --- Airborne vs surface ---
        is_airborne = bool(br.read_bit())
        #print(f"[{session.addr}] [PKT07] is_airborne = {is_airborne}")
        if is_airborne:
            raw_vy = br.read_int24()
            vy = raw_vy * LinkUpdater.VELOCITY_DEFLATE
            #print(f"[{session.addr}] [PKT07] raw_vy={raw_vy}, vy={vy:.2f}")
            if ent_state != Entity.const_6:
                entity['velocity_y'] = vy
                entity['surface']    = None
        else:
            entity['surface']     = True
            entity['velocity_y']  = 0
            #print(f"[{session.addr}] [PKT07] On surface → velocity_y=0")

        # Write back and broadcast
        session.entities[ent_id] = entity

        for other in all_sessions:
            if other is not session and other.world_loaded and other.current_level == session.current_level:
                pkt_data = Send_Entity_Data(entity, is_player=True)
                other.conn.sendall(struct.pack(">HH", 0x0F, len(pkt_data)) + pkt_data)
                #print(f"[{session.addr}] [PKT07] Broadcast to {other.addr}: x={entity['x']:.2f}, y={entity['y']:.2f}")

    except Exception as e:
        #print(f"[{session.addr}] [PKT07] Parse error: {e}")
        #print(f"[{session.addr}] [PKT07] Debug log: {br.get_debug_log()}")
        pass
