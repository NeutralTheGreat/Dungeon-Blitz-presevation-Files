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

# (7) How many equipment slots does the client loop over?
#     In AS3 it was EntType.MAX_SLOTS (which is 7).

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
                       transfer_token: int = 1,
                       pos_x: float = None,
                       pos_y: float = None) -> bytes:
    """
    Build the “minimal welcome” packet (0x10) that the client expects
    right after TRANSFER_BEGIN (0x21). We write bits in exactly the order
    that the client’s method_1379 expects:
      1) transfer_token (method_4)
      2) zero (method_4)
      3) GS_BITS (method_6)
      4) zero (method_4)
      5) name (UTF)
      6) customization flag = 1, then class/gender/head/hair/mouth/face/colors
      7) gear slots, numeric fields (level, currGold, currGems, bonusLevels, mammothIdols, extraField)
      8) showHigher (1 bit)
      9) hasOldCoord (1 bit) – we’ll send 0
     10) hasPosition (1 bit) – if 1, **immediately** after is two floats (param1.method_45())
     11) **extendedDataPresent** (1 bit) – if 1, client enters the “extended” block: gear inventory, mounts, etc.

    Once extendedDataPresent=1, we write the rest (gear inventory count, mounts count, etc.)
    exactly as before. If pos_x/pos_y are None, we send hasPosition=0 and skip writing floats.
    """

    # ─────────────────────────────────────────────────────────────────
    # PART A (bits up through hasPosition)
    bufA = BitBuffer()

    # 1) transfer_token
    bufA.write_method_4(transfer_token)

    # 2) zero (oldLevelId placeholder)
    bufA.write_method_4(0)

    # 3) GS_BITS (always 0 here)
    bufA.write_method_6(0, GS_BITS)

    # 4) zero (unused)
    bufA.write_method_4(0)

    # 5) Name and customization
    bufA.write_utf_string(char.get("name", ""))    # name
    bufA._append_bits(1, 1)                        # hasCustomization = 1
    bufA.write_utf_string(char.get("class", ""))   # class name
    bufA.write_utf_string(char.get("gender", ""))  # gender
    bufA.write_utf_string(char.get("headSet", "")) # headSet
    bufA.write_utf_string(char.get("hairSet", "")) # hairSet
    bufA.write_utf_string(char.get("mouthSet", ""))# mouthSet
    bufA.write_utf_string(char.get("faceSet", "")) # faceSet
    bufA._append_bits(char.get("hairColor", 0), 24)
    bufA._append_bits(char.get("skinColor", 0), 24)
    bufA._append_bits(char.get("shirtColor", 0), 24)
    bufA._append_bits(char.get("pantColor", 0), 24)

    # 6) Gear slots (6 slots), each: 1 bit “present?”, then If present: 11+2+16+16+16+8+8 bits
    gear_list = char.get("gearList", [0] * 6)
    for i in range(6):
        gear_id = gear_list[i] if i < len(gear_list) else 0
        if gear_id:
            bufA._append_bits(1, 1)         # ▸ slot present
            bufA._append_bits(gear_id, 11)  # 11 bits for gear ID
            bufA._append_bits(0, 2)         # two spare bits
            bufA._append_bits(0, 16)        # 16 bits
            bufA._append_bits(0, 16)        # 16 bits
            bufA._append_bits(0, 16)        # 16 bits
            bufA._append_bits(10, 8)        # 8 bits
            bufA._append_bits(10, 8)        # 8 bits
        else:
            bufA._append_bits(0, 1)         # ▸ empty slot

    # 7) Numeric fields (level, currGold, currGems, bonusLevels, mammothIdols, extraField)
    bufA.write_method_6(char.get("level", 1), MAX_CHAR_LEVEL_BITS)   # level
    bufA.write_method_4(char.get("currGold", 0))    # currGold
    bufA.write_method_4(char.get("currGems", 0))    # currGems
    bufA.write_method_4(char.get("bonusLevels", 0)) # bonusLevels
    bufA.write_method_4(char.get("mammothIdols", 0))# mammothIdols
    bufA.write_method_4(char.get("extraField", 0))  # extraField

    # 8) showHigher (1 bit)
    bufA._append_bits(int(char.get("showHigher", False)), 1)

    # 9) hasOldCoord (1 bit) – we always send 0 in this implementation
    has_old_coord = 0
    bufA._append_bits(has_old_coord, 1)

    # 10) hasPosition (1 bit)
    has_pos = 1 if (pos_x is not None and pos_y is not None) else 0
    bufA._append_bits(has_pos, 1)

    # At this point, if has_pos == 1, the client’s next step is:
    #   if (param1.method_11()) {  // that bit was hasPosition
    #       x = param1.method_45();
    #       y = param1.method_45();
    #   }
    #
    # So we must byte-align here, then append exactly two IEEE-754 float32 (big-endian)
    float_bytes = b""
    if has_pos:
        bufA.align_to_byte()
        float_bytes = struct.pack(">ff", float(pos_x), float(pos_y))

    # Convert bufA to raw bytes up through (hasOldCoord, hasPosition).
    bufA_bytes = bufA.to_bytes()
    prefix = bufA_bytes + float_bytes

    # ─────────────────────────────────────────────────────────────────
    # PART B: extendedDataPresent (1 bit) → we want to send 1
    # Then immediately the “extended” portion: gear-inventory count, mounts, pets, dyes, news, etc.

    bufB = BitBuffer()

    # 11) extendedDataPresent = 1 (client’s next param1.method_11())
    bufB._append_bits(1, 1)

    # Now everything that client method_1379 expects if extendedDataPresent==true:

    # (a) Gear-inventory count (uint32)
    bufB.write_method_4(0)

    # (b) Gear-sets count (uint32)
    bufB.write_method_4(0)

    # (c) Keybinds? (1 bit)
    bufB._append_bits(0, 1)

    # (d) Mounts count (uint32)
    bufB.write_method_4(0)

    # (e) Egg/pet flags (3 bits + “egg cooldown?” bit)
    bufB._append_bits(0, 1)
    bufB._append_bits(0, 1)
    bufB._append_bits(0, 1)
    bufB._append_bits(0, 1)

    # (f) Charms loop: “0” bit
    bufB._append_bits(0, 1)

    # (g) Materials loop: “0” bit
    bufB._append_bits(0, 1)

    # (h) Lockboxes loop: “0” bit + two uint32
    bufB._append_bits(0, 1)
    bufB.write_method_4(0)
    bufB.write_method_4(0)

    # (i) Alert state (4 bits) + Dye loop (250 bits)
    bufB._append_bits(0, Game_const_646)
    for _ in range(class_21_const_763):
        bufB._append_bits(0, 1)

    # (j) Consumables loop: “0” bit
    bufB._append_bits(0, 1)

    # (k) Missions count (uint32)
    bufB.write_method_4(0)

    # (l) Friends count (uint32)
    bufB.write_method_4(0)

    # (m) Ability-ranks count (7 bits)
    bufB._append_bits(0, class_10_const_83)

    # (n) Three “master-class loadout” IDs (7 bits each)
    bufB._append_bits(0, class_10_const_83)
    bufB._append_bits(0, class_10_const_83)
    bufB._append_bits(0, class_10_const_83)

    # (o) Craft talent points (uint32)
    bufB.write_method_4(0)

    # (p) Tower data: 3 × (6 bits)
    bufB._append_bits(0, class_66_const_409)
    bufB._append_bits(0, class_66_const_409)
    bufB._append_bits(0, class_66_const_409)

    # (q) Magic Forge? (1 bit)
    bufB._append_bits(0, 1)

    # (r) Ability research? (1 bit)
    bufB._append_bits(0, 1)

    # (s) Building info? (1 bit)
    bufB._append_bits(0, 1)

    # (t) Tower research? (1 bit)
    bufB._append_bits(0, 1)

    # (u) Egg-pet “SetEggData”? (1 bit)
    bufB._append_bits(0, 1)

    # (v) PetID count (6 bits) + loop end
    bufB._append_bits(0, class_16_const_167)

    # (w) Eggs in stable (uint32)
    bufB.write_method_4(0)

    # (x) Resting pet slots: 3 bits + 1 extra
    bufB._append_bits(0, 1)
    bufB._append_bits(0, 1)
    bufB._append_bits(0, 1)
    bufB._append_bits(0, 1)

    # (y) hasNews? (1 bit) → we send 1, then 4 × UTF + 1 × uint32
    bufB._append_bits(1, 1)
    bufB.write_utf_string("")  # news string #1
    bufB.write_utf_string("")  # news string #2
    bufB.write_utf_string("")  # news string #3
    bufB.write_utf_string("")  # news string #4
    bufB.write_method_4(0)     # news uint32

    # MasterClassID (4 bits)
    mc_id = _masterclass_to_id(char.get("MasterClass", ""))
    bufB._append_bits(mc_id, Game_const_209)

    # hasMasterRanks? = 0 (1 bit)
    bufB._append_bits(0, 1)

    # equip-gear loop (slots 1..6): one bit each
    for _slot_idx in range(1, ENT_MAX_SLOTS):
        bufB._append_bits(0, 1)

    # Seven consecutive uint32s: cosmeticOverrideID, activePetID, etc.
    bufB.write_method_4(0)  # cosmeticOverrideID
    bufB.write_method_4(0)  # activePetID
    bufB.write_method_4(0)  # activePetIteration
    bufB.write_method_4(0)  # hotbarPotionID
    bufB.write_method_4(0)  # hotbarPotionIteration
    bufB.write_method_4(0)  # levelData count
    bufB.write_method_4(0)  # roomData count
    # ─────────────────────────────────────────────────────────────────

    # Combine PART A prefix + PART B suffix:
    payload = prefix + bufB.to_bytes()
    header = struct.pack(">HH", 0x10, len(payload))
    return header + payload

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
