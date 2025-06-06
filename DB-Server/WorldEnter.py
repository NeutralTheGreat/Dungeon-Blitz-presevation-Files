# WorldEnter.py

from BitUtils import BitBuffer
import struct

ENT_MAX_SLOTS = 7
GS_BITS = 2             # Game.const_813
MAX_CHAR_LEVEL_BITS = 6 # Entity.MAX_CHAR_LEVEL_BITS

# (1) Bit-width for master-class ID
Game_const_209     = 4

# (2) Bit-width for “alert state”
Game_const_646     = 4

# (3) Maximum dye index (so we write exactly that many 1-bit flags)
class_21_const_763 = 250

# (4) Bit-width for ability IDs/ranks
class_10_const_83  = 7

# (5) Bit-width for master-class tower data
class_66_const_409 = 6

# (6) Bit-width for pet-ID in egg/pet loops
class_16_const_167 = 6

class class_118:
    const_43 = 27


class GearType:
    GEARTYPE_BITSTOSEND = 11   # (for example—use whatever the AS3 says)
    const_348          = 3   # (for example)
    const_176          = 2   # (for example)


# ─── Define the same “var_911” lookup in Python ───
NEWS_EVENTS = {
    1: [
        "a_NewsGoldIcon",
        "Double Gold Event",
        "While this event is in place all gold will be doubled world wide",
        "http://www.dungeonblitz.com/",
        1387602000,
    ],
    2: [
        "a_NewsGearIcon",
        "Double Gear Event",
        "While this event is in place all gear drops will be doubled world wide",
        "http://www.dungeonblitz.com/",
        1387602000,
    ],
    3: [
        "a_NewsMatsIcon",
        "Double Material Event",
        "While this event is in place all material drops will be doubled world wide",
        "http://www.dungeonblitz.com/",
        1387602000,
    ],
    4: [
        "a_NewsXPIcon",
        "Double XP Event",
        "While this event is in place all XP gained will be doubled world wide",
        "http://www.dungeonblitz.com/",
        1387602000,
    ],
    5: [
        "a_NewsPetXPIcon",
        "Double Pet XP Event",
        "While this event is in place all pet XP gained will be doubled world wide",
        "http://www.dungeonblitz.com/",
        1387602000,
    ],
}


_MASTERCLASS_TO_ID = {
    "frostwarden":   7,
    "flameseer":     8,
    "necromancer":   9,
    "sentinel":      4,
    "justicar":      5,
    "templar":       6,
    "executioner":   1,
    "shadowwalker":  2,
    "soulthief":     3,
}

def _masterclass_to_id(name: str) -> int:
    if not name:
        return 0
    return _MASTERCLASS_TO_ID.get(name.lower(), 0)

def Player_Data_Packet(char: dict,
                       event_index: int = 2,   # e.g. 1 for “double‐gold,” 2 for “double‐gear,” etc.
                       transfer_token: int = 1) -> bytes:

    buf = BitBuffer()

    # ────────────── (1) Preamble ──────────────
    buf.write_method_4(transfer_token)     # _loc2_
    buf.write_method_4(0)                  # _loc3_
    buf.write_method_6(0, GS_BITS)         # _loc4_
    buf.write_method_4(0)                  # _loc5_

    # ────────────── (2) Customization ──────────────
    buf.write_utf_string(char.get("name", "") or "")  # _loc6_
    buf._append_bits(1, 1)                            # hasCustomization = true
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

    # ────────────── (3) Gear slots (6 slots) ──────────────
    gear_list = char.get("gearList", [0] * 6)
    for i in range(6):
        gear_id = gear_list[i] if i < len(gear_list) else 0
        if gear_id:
            buf._append_bits(1, 1)
            buf._append_bits(gear_id, 11)
            buf._append_bits(0, 2)
            buf._append_bits(0, 16)
            buf._append_bits(0, 16)
            buf._append_bits(0, 16)
            buf._append_bits(10, 8)
            buf._append_bits(10, 8)
        else:
            buf._append_bits(0, 1)

    # ────────────── (4) Numeric fields ──────────────
    buf.write_method_6(char.get("level", 1), MAX_CHAR_LEVEL_BITS)
    buf.write_method_4(char.get("currGold",  0))
    buf.write_method_4(char.get("currGems",  0))
    buf.write_method_4(char.get("bonusLevels", 0))
    buf.write_method_4(char.get("mammothIdols",0))
    buf.write_method_4(char.get("extraField", 0))
    buf._append_bits(int(char.get("showHigher", False)), 1)

    # ────────────── (5) Teleport / “big init‐block” ──────────────
    buf._append_bits(0, 1)   # hasOldCoord? = false
    buf._append_bits(0, 1)   # hasPosition? = false
    buf._append_bits(1, 1)   # initBlockPresent? = true

    #  (a) Gear‐inventory count (bits)
    buf._append_bits(0, GearType.GEARTYPE_BITSTOSEND)

    #  (b) Gear‐sets count (bits)
    buf._append_bits(0, GearType.const_348)

    #  (c) Keybinds? (1 bit)
    buf._append_bits(0, 1)

    #  (d) Mounts count (uint32)
    buf.write_method_4(0)

    #  (e1–e4) Pet flags (4 × 1 bit)
    buf._append_bits(0, 1)
    buf._append_bits(0, 1)
    buf._append_bits(0, 1)
    buf._append_bits(0, 1)

    #  (f) Charms loop (1 bit)
    buf._append_bits(0, 1)

    #  (g) Materials loop (1 bit)
    buf._append_bits(0, 1)

    #  (h) Lockboxes loop (1 bit) + two uint32s
    buf._append_bits(0, 1)
    buf.write_method_4(0)
    buf.write_method_4(0)

    #  (i) Alert state (4 bits)
    buf._append_bits(0, Game_const_646)

    # ═══ Dye loop (250 bits) ═══
    for _ in range(class_21_const_763):
        buf._append_bits(0, 1)

    #  (j) Consumables loop (1 bit)
    buf._append_bits(0, 1)

    #  (k) Missions (uint32)
    buf.write_method_4(0)

    #  (l) Friends (uint32)
    buf.write_method_4(0)

    #  (m) Ability ranks (7 bits)
    buf._append_bits(0, class_10_const_83)

    #  (n) Master‐class loadout IDs (3 × 7 bits)
    buf._append_bits(0, class_10_const_83)
    buf._append_bits(0, class_10_const_83)
    buf._append_bits(0, class_10_const_83)

    #  (o) Craft talent points (uint32)
    buf.write_method_4(0)

    #  (p) Tower data (3 × 6 bits)
    buf._append_bits(0, class_66_const_409)
    buf._append_bits(0, class_66_const_409)
    buf._append_bits(0, class_66_const_409)

    # ─── (q) Magic Forge? (1 bit) = false ───
    buf._append_bits(0, 1)

    # ─── “Quick‐and‐dirty” 2‐bit pad → so that the next four UTF‐writes begin on a byte boundary ───
    buf.write_method_6(0, 2)

    # ─── Now, if event_index is provided, send exactly those five “news” fields; otherwise send four empty strings + 0 ───
    if event_index in NEWS_EVENTS:
        icon_name, title, body, url, end_time = NEWS_EVENTS[event_index]
        buf.write_utf_string(icon_name)
        buf.write_utf_string(title)
        buf.write_utf_string(body)
        buf.write_utf_string(url)
        buf.write_method_4(end_time)
    else:
        # no event → four empty strings + zero
        buf.write_utf_string("")
        buf.write_utf_string("")
        buf.write_utf_string("")
        buf.write_utf_string("")
        buf.write_method_4(0)

    mc_id = _masterclass_to_id(char.get("MasterClass", ""))
    buf._append_bits(mc_id, Game_const_209)

    # (aa) “hasMasterRanks?” (1 bit).
    # We’ll send 1 so the client tries to read 27 zero-bits below and builds (null,0) for each.
    buf._append_bits(1, 1)

    # (ab) Exactly class_118.const_43 zero-bits so the client does “new class_148(null,0)” that many times
    for _ in range(class_118.const_43):
        buf._append_bits(0, 1)

    # (ac) Equip-gear loop (slots 1..ENT_MAX_SLOTS−1, each 1 bit)
    for _slot_idx in range(1, ENT_MAX_SLOTS):
        buf._append_bits(0, 1)

    # (ad) cosmeticOverride (uint32)
    buf.write_method_4(0)

    # (ae) activePetID (uint32)
    buf.write_method_4(0)

    # (af) activePetIteration (uint32)
    buf.write_method_4(0)

    # (ag) potion1 (uint32)
    buf.write_method_4(0)

    # (ah) potion2 (uint32)
    buf.write_method_4(0)

    # (ai) levelData count (uint32)
    buf.write_method_4(0)

    # (aj) roomData count (uint32)
    buf.write_method_4(0)

    # ─────────────────────────────────────────
    #   Finally, build and return
    payload = buf.to_bytes()
    return struct.pack(">HH", 0x10, len(payload)) + payload







transfer_token = 1
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

#TODO... full player save file data
"""
def Player_Data_Packet(char: dict, transfer_token: int = 1) -> bytes:

    buf = BitBuffer()

    # ─────────────────────────────────────────────────────────────────
    #  1) Preamble
    buf.write_method_4(transfer_token)      # _loc2_: transfer_token
    buf.write_method_4(0)                   # _loc3_: zero
    buf.write_method_6(0, GS_BITS)          # _loc4_: zero (Game.const_813)
    buf.write_method_4(0)                   # _loc5_: zero
    # ─────────────────────────────────────────────────────────────────

    # ─────────────────────────────────────────────────────────────────
    #  2) Customization (hasCustomization = 1)
    buf.write_utf_string(char.get("name", "") or "")  # _loc6_: name
    buf._append_bits(1, 1)                           # “has customization = true”
    buf.write_utf_string(char.get("class", "") or "")
    buf.write_utf_string(char.get("gender", "") or "")
    buf.write_utf_string(char.get("headSet", "") or "")
    buf.write_utf_string(char.get("hairSet", "") or "")
    buf.write_utf_string(char.get("mouthSet", "") or "")
    buf.write_utf_string(char.get("faceSet", "") or "")
    buf._append_bits(char.get("hairColor", 0),  24)
    buf._append_bits(char.get("skinColor", 0),  24)
    buf._append_bits(char.get("shirtColor", 0), 24)
    buf._append_bits(char.get("pantColor", 0),  24)

    #  3) Gear slots (6 slots).  Each slot: 1 bit “present?”, then (if present) 11+2+16+16+16+8+8 bits.
    gear_list = char.get("gearList", [0] * 6)
    for i in range(6):
        gear_id = gear_list[i] if i < len(gear_list) else 0
        if gear_id:
            buf._append_bits(1, 1)       # “this slot has an item”
            buf._append_bits(gear_id, 11)
            buf._append_bits(0, 2)
            buf._append_bits(0, 16)
            buf._append_bits(0, 16)
            buf._append_bits(0, 16)
            buf._append_bits(10, 8)
            buf._append_bits(10, 8)
        else:
            buf._append_bits(0, 1)       # “no item in this slot”
    # ─────────────────────────────────────────────────────────────────

    # ─────────────────────────────────────────────────────────────────
    #  4) Numeric fields
    buf.write_method_6(char.get("level", 1), MAX_CHAR_LEVEL_BITS)  # _loc8_
    buf.write_method_4(char.get("currGold",  0))  # _loc9_
    buf.write_method_4(char.get("currGems",  0))  # _loc10_
    buf.write_method_4(char.get("bonusLevels", 0))# _loc11_
    buf.write_method_4(char.get("mammothIdols",0))# _loc12_
    buf.write_method_4(char.get("extraField", 0)) # _loc13_
    buf._append_bits(int(char.get("showHigher", False)), 1) # _loc14_
    # ─────────────────────────────────────────────────────────────────

    # ─────────────────────────────────────────────────────────────────
    #  5) hasOldCoord?   ( _loc15_ )
    buf._append_bits(0, 1)  # “no saved coordinate”
    #  6) hasPosition?
    buf._append_bits(0, 1)  # “no immediate teleport”
    #  7) initBlockPresent?  ← MUST be 1 so client enters the big init‐block
    buf._append_bits(1, 1)
    # ─────────────────────────────────────────────────────────────────

    #
    # Now the client’s method_1379 sees “if (_loc32_ = param1.method_11())” as true,
    # and enters the init‐block.  It expects these sub‐fields in exactly this order:
    #
    #   (a) Gear‐inventory count (uint32)
    #   (b) Gear‐sets count (uint32)
    #   (c) Keybinds? (1 bit)
    #   (d) Mounts count (uint32)
    #   (e) Egg/pet flags (3 bits + 1 “egg cooldown?” bit)
    #   (f) Charms loop start (while method_11())
    #   (g) Materials loop start (while method_11())
    #   (h) Lockboxes loop start (while method_11()), then two uint32 (keys, sigils)
    #   (i) Alert state (Game_const_646 bits), then Dye loop (250 bits)
    #   (j) Consumables loop start (while method_11())
    #   (k) Missions: read count (uint32), then loop
    #   (l) Friends: read count (uint32), then loop
    #   (m) Ability‐ranks count (class_10_const_83 bits)
    #   (n) Three “master‐class loadout” IDs (class_10_const_83 bits each)
    #   (o) Craft talent points (uint32)
    #   (p) Tower data: 3 × (class_66_const_409 bits)
    #   (q) Magic Forge? (1 bit)
    #   (r) Ability research? (1 bit)
    #   (s) Building info? (1 bit)
    #   (t) Tower research? (1 bit)
    #   (u) Egg‐pet “SetEggData”? (1 bit)
    #   (v) PetID count (class_16_const_167 bits) + loop
    #   (w) “How many eggs in stable?” (uint32)
    #   (x) Resting pet slots: 3 bits + 1 extra bit (“if method_11()”)
    #   (y) hasNews? (1 bit) + (if true) 4×UTF + 1×uint32
    #

    #  (a) Gear‐inventory count:

    buf.write_method_4(0)

    #  (b) Gear‐sets count:
    buf.write_method_4(0)

    #  (c) Keybinds? (1 bit)
    buf._append_bits(0, 1)

    #  (d) Mounts count:
    buf.write_method_4(0)

    #  (e1) Pet slot 1 flag:
    buf._append_bits(0, 1)
    #  (e2) Pet slot 2 flag:
    buf._append_bits(0, 1)
    #  (e3) Pet slot 3 flag:
    buf._append_bits(0, 1)
    #  (e4) “egg cooldown?” bit:
    buf._append_bits(0, 1)

    #  (f) Charms loop:
    buf._append_bits(0, 1)

    #  (g) Materials loop:
    buf._append_bits(0, 1)

    #  (h) Lockboxes loop:
    buf._append_bits(0, 1)
    #     Then two uint32: lockboxKeys, royalSigils
    buf.write_method_4(0)
    buf.write_method_4(0)

    #  (i) Alert state (Game_const_646 bits):
    buf._append_bits(0, Game_const_646)

    #      Dye loop: EXACTLY 250 bits
    for _ in range(250):
        buf._append_bits(0, 1)

    #  (j) Consumables loop:
    buf._append_bits(0, 1)

    #  (k) Missions: count (uint32) + skip
    buf.write_method_4(0)

    #  (l) Friends: count (uint32) + skip
    buf.write_method_4(0)

    #  (m) Ability‐ranks count (class_10_const_83 bits):
    buf._append_bits(0, class_10_const_83)

    #  (n) Three “master‐class loadout” IDs (class_10_const_83 bits each):
    buf._append_bits(0, class_10_const_83)
    buf._append_bits(0, class_10_const_83)
    buf._append_bits(0, class_10_const_83)

    #  (o) Craft talent points (uint32):
    buf.write_method_4(0)

    # After tower data
    # (p) Tower data: 3 × (class_66_const_409 bits)
    buf._append_bits(0, class_66_const_409)
    buf._append_bits(0, class_66_const_409)
    buf._append_bits(0, class_66_const_409)

    # (q) Magic Forge? (1 bit)
    buf._append_bits(0, 1)

    # (r) Ability research? (1 bit)
    buf._append_bits(0, 1)

    # (s) Building info? (1 bit)
    buf._append_bits(0, 1)

    # (t) Tower research? (1 bit)
    buf._append_bits(0, 1)

    # (u) Egg-pet “SetEggData”? (1 bit)
    buf._append_bits(0, 1)

    # (v) “How many petIDs follow?” (class_16_const_167 bits)
    buf._append_bits(0, class_16_const_167)



    # (w) “How many eggs in stable?” (uint32)
    buf.write_method_4(0)

    # (x1) Resting pet slot #1? (1 bit)
    buf._append_bits(0, 1)

    # (x2) Resting pet slot #2? (1 bit)
    buf._append_bits(0, 1)

    # (x3) Resting pet slot #3? (1 bit)
    buf._append_bits(0, 1)

    # (x4) Extra “if (method_11())” for SetRestingPetData? (1 bit)
    buf._append_bits(0, 1)

    # (y) hasNews? (1 bit) – must be 1 to trigger news reading
    buf._append_bits(1, 1)

    # News data: four UTF strings + one uint32

    buf.write_utf_string("")  # _loc66_
    buf.write_utf_string("")  # _loc67_
    buf.write_utf_string("")  # _loc68_
    buf.write_utf_string("")  # _loc69_
    buf.write_method_4(0)  # _loc70_

    # Master class ID
    master_name = char.get("MasterClass", "")
    mc_id = _masterclass_to_id(master_name)  # e.g., 6 for "templar"
    buf._append_bits(mc_id, Game_const_209)

    #  9) Now the client checks “hasMasterRanks?”:
    #       if ((_loc34_ = param1.method_11()) && Boolean(_loc20_)) { …read defaults… }
    #    We send 0 so it skips reading any default ranks:
    buf._append_bits(0, 1)

    # 10) Next is the “equip‐gear” loop (one bit per slot, slots 1..ENT_MAX_SLOTS-1):
    for _slot_idx in range(1, ENT_MAX_SLOTS):
        buf._append_bits(0, 1)

    # 11) After that, the client reads _loc37_ (4 bytes), then _loc39_, _loc40_, _loc42_, _loc43_,
    #     followed by _loc46_ (levelData count), then _loc47_ (roomData count).  So we write:
    buf.write_method_4(0)  # _loc37_: cosmetic override
    buf.write_method_4(0)  # _loc39_: activePetID
    buf.write_method_4(0)  # _loc40_: activePetIteration
    buf.write_method_4(0)  # _loc42_: potion ID
    buf.write_method_4(0)  # _loc43_: potion iteration
    buf.write_method_4(0)  # _loc46_: levelData count
    buf.write_method_4(0)  # _loc47_: roomData count
    # ─────────────────────────────────────────────────────────────────

    # Build and return
    payload = buf.to_bytes()
    return struct.pack(">HH", 0x10, len(payload)) + payload
"""
