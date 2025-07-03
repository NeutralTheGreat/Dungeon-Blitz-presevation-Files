import json, struct
from bitreader import BitReader
from constants import Game, GearType, EntType, class_64, class_1
from BitUtils import BitBuffer
from constants import get_dye_color
SAVE_PATH_TEMPLATE = "saves/{user_id}.json"

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
    chars = session.player_data.get("characters", [])
    for char in chars:
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
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(session.player_data, f, indent=2)

    print(f"[Save] activeAbilities for {session.current_character} = {active} saved to {save_path}")

def handle_masterclass_packet(session, raw_data):
    # 1) parse once
    payload = raw_data[4:]
    br = BitReader(payload)
    entity_id        = br.read_method_4()
    master_class_id  = br.read_method_6(Game.const_209)
    print(f"[MasterClass] Player {session.user_id} → classID={master_class_id}")

    # 2) update the in‑memory save
    pd = session.player_data
    if isinstance(pd, dict) and "characters" in pd:
        chars = pd["characters"]
    elif isinstance(pd, list):
        chars = pd
    else:
        print(f"[ERROR] unexpected save format for user {session.user_id}")
        return

    for char in chars:
        if char.get("name") == session.current_character:
            char["MasterClass"] = master_class_id
            print(f"[UPDATE] Set MasterClass={master_class_id} on {char['name']}")
            break
    else:
        print(f"[WARNING] Character {session.current_character} not found in save!")
        return

    # 3) persist to disk
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(pd, f, indent=2)
    print(f"[Save] MasterClass for {session.current_character} saved to {save_path}")

    # 4) echo back to client so it clears bWaitingForChangeMasterClassResponse
    bb = BitBuffer()
    bb.write_method_4(entity_id)
    bb.write_method_6(master_class_id, Game.const_209)
    resp = struct.pack(">HH", 0xC3, len(bb.to_bytes())) + bb.to_bytes()
    session.conn.sendall(resp)
    print(f"[Reply C3] entity={entity_id}, class={master_class_id}")

def handle_research_packet(session, raw_data):
    """
    Handle the client’s ClearResearch() call (packet 0xDF).
    Clears any in‑progress research and persists it, then echoes 0xDF back.
    """
    # 1) Clear in‑memory research state
    pd = session.player_data
    # Determine where characters live
    chars = pd.get("characters", pd if isinstance(pd, list) else [])
    for char in chars:
        if char.get("name") == session.current_character:
            char["towerResearch"] = {"masterClassID": 0, "endTime": 0}
            break

    # 2) Persist to disk
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(pd, f, indent=2)

    # 3) Echo back a zero‑length 0xDF so the client stops logging “unhandled”
    session.conn.sendall(struct.pack(">HH", 0xDF, 0))

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

    pd = session.player_data
    chars = pd.get("characters", pd if isinstance(pd, list) else [])
    for char in chars:
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

    # Save
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(pd, f, indent=2)
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
    pd = session.player_data
    chars = pd.get("characters", pd if isinstance(pd, list) else [])

    for char in chars:
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

    # Save updated data
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(pd, f, indent=2)

    print("[Save] Dye info applied and synced to inventory.")


def handle_rune_packet(session, raw_data):
    payload = raw_data[4:]
    br = BitReader(payload)
    entity_id = br.read_method_4()
    gear_id = br.read_method_6(GearType.GEARTYPE_BITSTOSEND)
    gear_tier = br.read_method_6(GearType.const_176)
    rune_id = br.read_method_6(class_64.const_101)
    rune_slot = br.read_method_6(class_1.const_765)
    print(f"[Rune] entity={entity_id}, gear={gear_id}, tier={gear_tier}, rune_id={rune_id}, rune_slot={rune_slot}")

    pd = session.player_data
    chars = pd.get("characters", pd if isinstance(pd, list) else [])
    for char in chars:
        if char.get("name") != session.current_character:
            continue
        eq = char.setdefault("equippedGears", [])
        inv = char.setdefault("inventoryGears", [])

        # Adjust slot logic: flash game uses MAX_SLOTS - 1 actual slots
        desired_slots = EntType.MAX_SLOTS - 1
        # Ensure equipped list has exactly desired_slots slots
        while len(eq) < desired_slots:
            eq.append({
                "gearID": 0,
                "tier": 0,
                "runes": [0, 0, 0],
                "colors": [0, 0]
            })
        # Optionally trim any extra slot if present
        if len(eq) > desired_slots:
            eq[:] = eq[:desired_slots]

        # Find the gear in equipped slots
        gear_found = False
        for slot in range(len(eq)):
            if eq[slot].get("gearID") == gear_id and eq[slot].get("tier") == gear_tier:
                # Update the specified rune slot (1-based to 0-based index)
                if 1 <= rune_slot <= 3:
                    eq[slot]["runes"][rune_slot - 1] = rune_id
                    gear_found = True
                # Update inventory to keep it in sync
                for item in inv:
                    if item.get("gearID") == gear_id and item.get("tier") == gear_tier:
                        item["runes"][rune_slot - 1] = rune_id
                        break
                else:
                    inv.append(eq[slot].copy())
                break
        if not gear_found:
            print(
                f"[Warning] Gear {gear_id} (tier {gear_tier}) not found in equipped slots for {session.current_character}")
            return
        break
    else:
        print(f"[Warning] Character {session.current_character} not found in save!")
        return

    # Save updated data
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(pd, f, indent=2)
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

def handle_change_look(session, raw_data):
    """
    Packet 0x8E: change character look.
    Fields: head:String, hair:String, mouth:String, face:String,
            gender:String, shirtColor:uint, pantColor:uint
    """
    payload = raw_data[4:]
    br = BitReader(payload)

    # read the five strings
    head   = br.read_string()
    hair   = br.read_string()
    mouth  = br.read_string()
    face   = br.read_string()
    gender = br.read_string()

    # then two 24‑bit color values
    hair_color = br.read_bits(EntType.CHAR_COLOR_BITSTOSEND)
    skin_color  = br.read_bits(EntType.CHAR_COLOR_BITSTOSEND)

    print(f"[ChangeLook] {session.current_character} →"
          f" head={head}, hair={hair}, mouth={mouth}, face={face},"
          f" gender={gender}, shirt={hex(hair_color)}, pant={hex(skin_color)}")

    # 1) Update in‑memory save
    chars = session.player_data.get("characters", [])
    for char in chars:
        if char.get("name") != session.current_character:
            continue

        char["headSet"]       = head
        char["hairSet"]       = hair
        char["mouthSet"]      = mouth
        char["faceSet"]       = face
        char["gender"]     = gender
        char["hairColor"] = hair_color
        char["skinColor"]  = skin_color
        break
    else:
        print(f"[WARNING] Character {session.current_character} not found for change look")
        return

    # 2) Persist to disk
    save_path = SAVE_PATH_TEMPLATE.format(user_id=session.user_id)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(session.player_data, f, indent=2)
    print(f"[Save] Updated look for {session.current_character} in {save_path}")

    # 3) Echo this packet back so the client applies it immediately
    session.conn.sendall(raw_data)

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