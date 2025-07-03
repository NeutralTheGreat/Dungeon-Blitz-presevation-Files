import json

def load_npc_data_for_level(level_name: str, json_path: str = r"data\npc_data.json") -> list:
    """
    Args:
        level_name (str): The level identifier (e.g., 'TutorialBoat').
        json_path (str): Path to the JSON file containing NPC data.

    Returns:
        list: List of dictionaries, each containing NPC data for the given level.
    """
    try:
        with open(json_path, 'r') as file:
            npc_data = json.load(file)
        return npc_data.get(level_name, [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading NPC data: {e}")
        return []

# Usage Example:
npc_list = load_npc_data_for_level("TutorialBoat")
for npc in npc_list:
    print(npc["name"])
