from BitUtils import BitBuffer
from constants import Entity
COORD_SCALE = 1

def scale_coordinates(x: float, y: float, z: float):
    """Convert floats to integers for method_45."""
    return int(x), int(y), int(z)

def Send_Entity_Data(entity: dict, is_player: bool = False) -> bytes:
    bb = BitBuffer()

    # Core header
    bb.write_method_4(entity.get("id", 0))  # Entity ID
    bb.write_method_13(entity.get("name", ""))  # Entity name
    bb.write_bits(0, 1)  # Appearance flag (0 for NPCs)

    # Coordinates
    x_scaled, y_scaled, z_scaled = scale_coordinates(
        entity.get("x", 0.0), entity.get("y", 0.0), entity.get("z", 0.0)
    )
    bb.write_signed_method_45(x_scaled)  # X coordinate
    bb.write_signed_method_45(y_scaled)  # Y coordinate
    bb.write_signed_method_45(z_scaled)  # Z coordinate
    bb.write_method_6(entity.get("team", 0), Entity.TEAM_BITS or 2)  # Team
    bb.write_method_6(entity.get("entState", 0), Entity.const_316)

    # Entity type
    bb.write_bits(0, 1)  # Player flag (0 for NPCs)

    # NPC-specific fields
    bb.write_bits(1 if entity.get("untargetable", False) else 0, 1)  # Untargetable flag
    bb.write_method_739(entity.get("behavior_id", 0))  # Behavior ID (target_id)
    behavior_speed = entity.get("behavior_speed", 0.0)
    bb.write_bits(1 if behavior_speed > 0 else 0, 1)  # Behavior speed flag
    if behavior_speed > 0:
        bb.write_method_4(int(behavior_speed * Entity.VELOCITY_INFLATE))  # Scaled

        # Optional strings
    guild = entity.get("guild", "")
    bb.write_bits(1 if guild else 0, 1)  # Guild name flag
    if guild:
       bb.write_method_13(guild)
    title = entity.get("title", "")
    bb.write_bits(1 if title else 0, 1)  # Title flag
    if title:
        bb.write_method_13(title)
    subtitle = entity.get("subtitle", "")
    bb.write_bits(1 if subtitle else 0, 1)  # Subtitle (mount name) flag
    if subtitle:
        bb.write_method_13(subtitle)
    # Level and power type
    level = entity.get("level", 0)
    bb.write_bits(1 if level > 0 else 0, 1)  # Level flag
    if level > 0:
        bb.write_method_4(level)
    power_id = entity.get("power_id", 0)
    bb.write_bits(1 if power_id > 0 else 0, 1)  # Power type flag
    if power_id > 0:
        bb.write_method_4(power_id)

    # State (again), facing, health, buffs
    bb.write_bits(1 if entity.get("facing_left", False) else 0, 1)  # Facing left
    bb.write_signed_method_45(entity.get("health_delta", 0))  # Health delta
    buffs = entity.get("buffs", [])
    bb.write_method_4(len(buffs))  # Buff count
    bb.write_signed_method_45(entity.get("health_delta", 0))  # Health delta


    # Stop here to test up to entState (added later)
    payload = bb.to_bytes()
    #print(f"Send_Entity_Data: id={entity.get('id')}, name={entity.get('name')}, hex={payload.hex()}, debug_log={bb.get_debug_log()}")
    return payload