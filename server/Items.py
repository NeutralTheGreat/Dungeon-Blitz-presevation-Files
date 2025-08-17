import json
import os

def load_gear_data(class_name):
    path = os.path.join("Starter_Items", f"{class_name.lower()}_gears.json")
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load {class_name} gear data: {e}")
        return []

inventory_gears = {
    "paladin": load_gear_data("paladin"),
    "mage": load_gear_data("mage"),
    "rogue": load_gear_data("rogue"),
}


with open("Starter_Items/MasteryClass.json", "r", encoding="utf-8") as f:
    Mastery_Class = json.load(f)

def get_starting_mastery(cls):
    return Mastery_Class.get(cls, [])

with open("Starter_Items/default_learned_abilities.Json", 'r') as f:
    default_learned_abilities = json.load(f)

with open("Starter_Items/starting_dyes.Json", "r") as f:
    starting_dyes = json.load(f)

with open("Starter_Items/Starting_Mounts.json", "r", encoding="utf-8") as f:
    Starting_Mounts = json.load(f)

with open("Starter_Items/Starting_Pets.json", "r", encoding="utf-8") as f:
    Starting_Pets = json.load(f)

with open("Starter_Items/Starting_Charms.json", "r", encoding="utf-8") as f:
    Starting_Charms = json.load(f)

with open("Starter_Items/Starting_Materials.json", "r", encoding="utf-8") as f:
    Starting_Materials = json.load(f)

with open("Starter_Items/Starting_Consumables.json", "r", encoding="utf-8") as f:
    Starting_Consumables = json.load(f)

with open("Starter_Items/Starting_Missions.json", "r", encoding="utf-8") as f:
    Starting_Missions = json.load(f)


Buildings = {
    "paladin": {
        "1": 10,
        "2": 10,
        "3": 10,
        "4": 10,
        "12": 0,
        "13": 10
    },
    "rogue": {
        "1": 10,
        "2": 10,
        "9": 10,
        "10": 10,
        "11": 10,
        "12": 0,
        "13": 10
    },
    "mage": {
        "1": 10,
        "2": 10,
        "6": 10,
        "7": 10,
        "8": 10,
        "12": 0,
        "13": 10
    }
}

Starter_Weapons = {
    "paladin": [{
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 1,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 13,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        }],
    "rogue": [{
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 27,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 39,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        }],
    "mage": [{
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 0,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 53,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        },
        {
          "gearID": 65,
          "tier": 0,
          "runes": [
            0,
            0,
            0
          ],
          "colors": [
            0,
            0
          ]
        }]
}

Active_Abilities = {
    "paladin": [
        20,
        24,
        25
      ],
    "rogue": [
        3,
        5,
        9
      ],
    "mage": [
        12,
        14,
        18
      ]}


Active_master_Class = {
    "paladin": 4,
    "rogue": 3,
    "mage": 9
}
