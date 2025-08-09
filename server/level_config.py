def get_spawn_coordinates(char: dict, current_level: str, target_level: str) -> tuple[float, float, bool]:

    # detect dungeon flag
    is_dungeon = LEVEL_CONFIG.get(target_level, (None, None, None, False))[3]
    # special exception (if you still want coords in CraftTown, for example)
    if is_dungeon and target_level != "CraftTown":
        return 0, 0, False

    # Special cases
    if current_level == "SwampRoadNorth" and target_level == "NewbieRoad":
        return 20298.00, 639.00, True
    if current_level == "SwampRoadNorthHard" and target_level == "NewbieRoadHard":
        return 20298.00, 639.00, True

    if current_level == "EmeraldGlades" and target_level == "OldMineMountain":
        return 18552, 4021, True
    if current_level == "EmeraldGladesHard" and target_level == "OldMineMountainHard":
        return 18552, 4021, True

    if current_level == "SwampRoadNorth" and target_level == "SwampRoadConnection":
        return 325.00, 368.00, True
    if current_level == "SwampRoadNorthHard" and target_level == "SwampRoadConnectionHard":
        return 325.00, 368.00, True

    if current_level == "BridgeTown" and target_level == "SwampRoadConnection":
        return 10533.00, 461.00, True
    if current_level == "BridgeTownHard" and target_level == "SwampRoadConnectionHard":
        return 10533.00, 461.00, True

    if current_level == "OldMineMountain" and target_level == "BridgeTown":
        return 16986, -296.01, True
    if current_level == "OldMineMountainHard" and target_level == "BridgeTownHard":
        return 16986, -296.01, True

    if current_level == "BridgeTown" and target_level == "BridgeTownHard":
        return 11439, 2198.99, True
    if current_level == "BridgeTownHard" and target_level == "BridgeTown":
        return 11439, 2198.99, True

    if current_level == "Castle" and target_level == "BridgeTown":
        return 10566, 492.99, True
    if current_level == "CastleHard" and target_level == "BridgeTownHard":
        return 10566, 492.99, True

    if current_level == "ShazariDesert" and target_level == "ShazariDesertHard":
        return 14851.25, 638.4691666666666, True
    if current_level == "ShazariDesertHard" and target_level == "ShazariDesert":
        return 14851.25, 638.4691666666666, True

    if current_level == "JadeCity" and target_level == "ShazariDesert":
        return 25857.25, 1298.4691666666668, True
    if current_level == "JadeCityHard" and target_level == "ShazariDesertHard":
        return 25857.25, 1298.4691666666668, True

    # Default spawn points for the (non-dungeon) target level
    spawn = SPAWN_POINTS.get(target_level, {"x": 0.0, "y": 0.0})

    # Check if target level is previously visited
    current_level_data = char.get("CurrentLevel", {})
    prev_level_data    = char.get("PreviousLevel", {})

    if (target_level == current_level_data.get("name")) and "x" in current_level_data and "y" in current_level_data:
        return int(round(current_level_data["x"])), int(round(current_level_data["y"])), True
    elif prev_level_data.get("name") == target_level and "x" in prev_level_data and "y" in prev_level_data:
        return int(round(prev_level_data["x"])), int(round(prev_level_data["y"])), True
    else:
        # new non-dungeon level → default spawn
        return int(round(spawn["x"])), int(round(spawn["y"])), True

# Default Player Spawn Point for handle_entity_incremental_update
SPAWN_POINTS = {
    "CraftTown":{"x": 360, "y": 1458.99},
    "--------WOLFS END------------": "",
    "NewbieRoad": {"x": 1421.25, "y": 826.615},
    "NewbieRoadHard": {"x": 1421.25, "y": 826.615},

    "--------BLACKROSE MIRE------------": "",
    "SwampRoadNorth": {"x": 4360.5, "y": 595.615},
    "SwampRoadNorthHard": {"x": 4360.5, "y": 595.615},

    "--------FELBRIDGE------------": "",
    "BridgeTown": {"x": 3944, "y": 838.99},
    "BridgeTownHard": {"x": 3944, "y": 838.99},

    "--------CEMETERY HILL------------": "",
    "CemeteryHill": {"x": 00, "y": 00},#missing files Unknown spawn coordinates
    "CemeteryHillHard": {"x": 00, "y": 00},

    "--------STORMSHARD------------": "",
    "OldMineMountain": {"x": 189.25, "y": 1335.99},
    "OldMineMountainHard": {"x": 189.25, "y": 1335.99},

    "--------EMERALD GLADES-----------": "",
    "EmeraldGlades": {"x": -1433.75, "y": -1883.6236363636363},
    "EmeraldGladesHard": {"x": -1433.75, "y": -1883.6236363636363},

    "--------DEEPGARD CASTLE------------": "",
    "Castle": {"x": -1280, "y": -1941.01},
    "CastleHard": {"x": -1280, "y": -1941.01},

    "--------SHAZARI DESERT------------": "",
    "ShazariDesert": {"x": 618.25, "y": 647.4691666666666},
    "ShazariDesertHard": {"x": 618.25, "y": 647.4691666666666},

    "--------VALHAVEN------------": "",
    "JadeCity": {"x": 10430.5, "y": 1058.99},
    "JadeCityHard": {"x": 10430.5, "y": 1058.99},
}
_raw_level_config  = {
    "CraftTown": "LevelsHome.swf/a_Level_Home 1 1 true",
    "CraftTownTutorial": "LevelsHome.swf/a_Level_HomeTutorial 1 1 true",
    "--------WOLFS END------------": "",
    "TutorialBoat": "LevelsTut.swf/a_Level_TutorialBoat 1 1 true",
    "NewbieRoad": "LevelsNR.swf/a_Level_NewbieRoad 1 1 false",
    "NewbieRoadHard": "LevelsNR.swf/a_Level_NewbieRoad 36 1 false Hard",
    "TutorialDungeon": "LevelsNR.swf/a_Level_NRTutorial 2 2 true",
    "TutorialDungeonHard": "LevelsNR.swf/a_Level_GoblinBeachHard 37 2 true Hard",
    "GoblinRiverDungeon": "LevelsNR.swf/a_Level_GoblinRiver 3 3 true",
    "GoblinRiverDungeonHard": "LevelsNR.swf/a_Level_GoblinRiver 38 3 true Hard",
    "GhostBossDungeon": "LevelsNR.swf/a_Level_NRGhost 4 4 true",
    "GhostBossDungeonHard": "LevelsNR.swf/a_Level_NRGhost 39 4 true Hard",
    "DreamDragonDungeon": "LevelsNR.swf/a_Level_NRDragon 5 5 true",
    "DreamDragonDungeonHard": "LevelsNR.swf/a_Level_NRDragon 40 5 true Hard",
    "NR_Tales1Keep": "TalesNR.swf/a_Level_NRTales1Keep 44 29 true",
    "NR_Tales2Anna": "TalesNR.swf/a_Level_NRTales2Anna 44 29 true",
    "NR_Tales3Bazaar": "TalesNR.swf/a_Level_NRTales3Bazaar 44 29 true",
    "NR_Tales4Research": "TalesNR.swf/a_Level_NRTales4Research 44 29 true",
    "NR_Tales5DreamCave": "TalesNR.swf/a_Level_NRTales5DreamCave 44 29 true",
    "--------BLACKROSE MIRE------------": "",
    "SwampRoadNorth": "LevelsSRN.swf/a_Level_SwampRoadNorth 6 6 false",
    "SwampRoadNorthHard": "LevelsSRN.swf/a_Level_SwampRoadNorth 31 6 false Hard",
    "SRN_Mission1": "LevelsSRN.swf/a_Level_SRNMission1Castout 6 6 true",
    "SRN_Mission1Hard": "LevelsSRN.swf/a_Level_SRNMission1Castout 31 6 true Hard",
    "SRN_Mission2": "LevelsSRN.swf/a_Level_SRNMission2Yornak 7 7 true",
    "SRN_Mission2Hard": "LevelsSRN.swf/a_Level_SRNMission2Yornak 32 7 true Hard",
    "SRN_Mission3": "LevelsSRN.swf/a_Level_SRNMission3Svar 8 8 true",
    "SRN_Mission3Hard": "LevelsSRN.swf/a_Level_SRNMission3Svar 33 8 true Hard",
    "SRN_Mission4": "LevelsSRN.swf/a_Level_SRNMission4Ooyak 8 8 true",
    "SRN_Mission4Hard": "LevelsSRN.swf/a_Level_SRNMission4Ooyak 33 8 true Hard",
    "SRN_Mission5": "LevelsSRN.swf/a_Level_SRNMission5Broodvictor 9 9 true",
    "SRN_Mission5Hard": "LevelsSRN.swf/a_Level_SRNMission5Broodvictor 34 9 true Hard",
    "SRN_Mission6": "LevelsSRN.swf/a_Level_SRNMission6MindlessQueen 8 8 true",
    "SRN_Mission6Hard": "LevelsSRN.swf/a_Level_SRNMission6MindlessQueen 33 8 true Hard",
    "SRN_Mission7": "LevelsSRN.swf/a_Level_SRNMission7Svath 9 9 true",
    "SRN_Mission7Hard": "LevelsSRN.swf/a_Level_SRNMission7Svath 34 9 true Hard",
    "SwampRoadConnection": "LevelsSRN.swf/a_Level_SwampRoadConnection 10 10 false",
    "SwampRoadConnectionHard": "LevelsSRN.swf/a_Level_SwampRoadConnection 35 10 false Hard",
    "SwampRoadConnectionMission": "LevelsSRN.swf/a_Level_SwampRoadConnectionMission 10 10 true",
    "SwampRoadConnectionMissionHard": "LevelsSRN.swf/a_Level_SwampRoadConnectionMission 35 10 true Hard",
    "--------FELBRIDGE------------": "",
    "BridgeTown": "LevelsBT.swf/a_Level_BridgeTown 10 10 false",
    "BridgeTownHard": "LevelsBT.swf/a_Level_BridgeTown 25 10 false Hard",
    "BT_Mission1": "LevelsBT.swf/a_Level_BTMission1 11 11 true",
    "BT_Mission1Hard": "LevelsBT.swf/a_Level_BTMission1 26 11 true Hard",
    "BT_Mission2": "LevelsBT.swf/a_Level_BTMission2 12 12 true",
    "BT_Mission2Hard": "LevelsBT.swf/a_Level_BTMission2 27 12 true Hard",
    "BT_Mission3": "LevelsBT.swf/a_Level_BTMission3 14 14 true",
    "BT_Mission3Hard": "LevelsBT.swf/a_Level_BTMission3 29 14 true Hard",
    "BT_Mission4": "LevelsBT.swf/a_Level_BTMission4 15 15 true",
    "BT_Mission4Hard": "LevelsBT.swf/a_Level_BTMission4 30 15 true Hard",
    "LDArena1": "LevelsLD.swf/a_Level_LDArena1 50 50 true",
    "--------CEMETERY HILL------------": "",
    "CemeteryHill": "LevelsCH.swf/a_Level_CemeteryHill 11 11 false",
    "CemeteryHillHard": "LevelsCH.swf/a_Level_CemeteryHill 26 11 false Hard",
    "CH_Mission1": "LevelsCH.swf/a_Level_CHMission1 11 11 true",
    "CH_Mission1Hard": "LevelsCH.swf/a_Level_CHMission1 26 11 true Hard",
    "CH_Mission2": "LevelsCH.swf/a_Level_CHMission2 11 11 true",
    "CH_Mission2Hard": "LevelsCH.swf/a_Level_CHMission2 26 11 true Hard",
    "CH_Mission3": "LevelsCH.swf/a_Level_CHMission3 13 13 true",
    "CH_Mission3Hard": "LevelsCH.swf/a_Level_CHMission3 28 13 true Hard",
    "CH_Mission4": "LevelsCH.swf/a_Level_CHMission4 12 12 true",
    "CH_Mission4Hard": "LevelsCH.swf/a_Level_CHMission4 27 12 true Hard",
    "CH_Mission5": "LevelsCH.swf/a_Level_CHMission5 12 12 true",
    "CH_Mission5Hard": "LevelsCH.swf/a_Level_CHMission5 27 12 true Hard",
    "CH_Mission6": "LevelsCH.swf/a_Level_CHMission6 14 14 true",
    "CH_Mission6Hard": "LevelsCH.swf/a_Level_CHMission6 29 14 true Hard",
    "CH_Mission7": "LevelsCH.swf/a_Level_CHMission7 15 15 true",
    "CH_Mission7Hard": "LevelsCH.swf/a_Level_CHMission7 30 15 true Hard",
    "CH_Mission8": "LevelsCH.swf/a_Level_CHMission8 15 15 true",
    "CH_Mission8Hard": "LevelsCH.swf/a_Level_CHMission8 30 15 true Hard",
    "CH_MiniMission1": "LevelsCH.swf/a_Level_CHMini1 11 11 true",
    "CH_MiniMission1Hard": "LevelsCH.swf/a_Level_CHMini1 26 11 true Hard",
    "CH_MiniMission2": "LevelsCH.swf/a_Level_CHMini2 11 11 true",
    "CH_MiniMission2Hard": "LevelsCH.swf/a_Level_CHMini2 26 11 true Hard",
    "CH_MiniMission3": "LevelsCH.swf/a_Level_CHMini3 12 12 true",
    "CH_MiniMission3Hard": "LevelsCH.swf/a_Level_CHMini3 27 12 true Hard",
    "CH_MiniMission4": "LevelsCH.swf/a_Level_CHMini4 12 12 true",
    "CH_MiniMission4Hard": "LevelsCH.swf/a_Level_CHMini4 27 12 true Hard",
    "CH_MiniMission5": "LevelsCH.swf/a_Level_CHMini5 13 13 true",
    "CH_MiniMission5Hard": "LevelsCH.swf/a_Level_CHMini5 28 13 true Hard",
    "CH_MiniMission6": "LevelsCH.swf/a_Level_CHMini6 13 13 true",
    "CH_MiniMission6Hard": "LevelsCH.swf/a_Level_CHMini6 28 13 true Hard",
    "CH_MiniMission7": "LevelsCH.swf/a_Level_CHMini7 14 14 true",
    "CH_MiniMission7Hard": "LevelsCH.swf/a_Level_CHMini7 29 14 true Hard",
    "CH_MiniMission8": "LevelsCH.swf/a_Level_CHMini8 14 14 true",
    "CH_MiniMission8Hard": "LevelsCH.swf/a_Level_CHMini8 29 14 true Hard",
    "0CH_MiniMission9": "LevelsCH.swf/a_Level_CHMini9 15 15 true",
    "0CH_MiniMission9Hard": "LevelsCH.swf/a_Level_CHMini9 30 15 true Hard",
    "--------STORMSHARD------------": "",
    "OldMineMountain": "LevelsOMM.swf/a_Level_OldMineMountain 16 16 false",
    "OldMineMountainHard": "LevelsOMM.swf/a_Level_OldMineMountain 31 16 false Hard",
    "OMM_Mission1": "LevelsOMM.swf/a_Level_OMMMission01GiveVoiceToStone 16 16 true",
    "OMM_Mission1Hard": "LevelsOMM.swf/a_Level_OMMMission01GiveVoiceToStone 31 16 true Hard",
    "OMM_Mission2": "LevelsOMM.swf/a_Level_OMMMission02RockHulkGarden 16 16 true",
    "OMM_Mission2Hard": "LevelsOMM.swf/a_Level_OMMMission02RockHulkGarden 31 16 true Hard",
    "OMM_Mission3": "LevelsOMM.swf/a_Level_OMMMission03EyeOfTheTyrant 16 16 true",
    "OMM_Mission3Hard": "LevelsOMM.swf/a_Level_OMMMission03EyeOfTheTyrant 31 16 true Hard",
    "OMM_Mission4": "LevelsOMM.swf/a_Level_OMMMission04AbandonedArmory 17 17 true",
    "OMM_Mission4Hard": "LevelsOMM.swf/a_Level_OMMMission04AbandonedArmory 32 17 true Hard",
    "OMM_Mission5": "LevelsOMM.swf/a_Level_OMMMission05HuntedToTheEdge 17 17 true",
    "OMM_Mission5Hard": "LevelsOMM.swf/a_Level_OMMMission05HuntedToTheEdge 32 17 true Hard",
    "OMM_Mission6": "LevelsOMM.swf/a_Level_OMMMission06ForgottenForge 17 17 true",
    "OMM_Mission6Hard": "LevelsOMM.swf/a_Level_OMMMission06ForgottenForge 32 17 true Hard",
    "OMM_Mission7": "LevelsOMM.swf/a_Level_OMMMission07GriffinsRedoubt 17 17 true",
    "OMM_Mission7Hard": "LevelsOMM.swf/a_Level_OMMMission07GriffinsRedoubt 32 17 true Hard",
    "OMM_Mission8": "LevelsOMM.swf/a_Level_OMMMission08BloodInTheVeins 18 18 true",
    "OMM_Mission8Hard": "LevelsOMM.swf/a_Level_OMMMission08BloodInTheVeins 33 18 true Hard",
    "OMM_Mission9": "LevelsOMM.swf/a_Level_OMMMission09GrahlsRebellion 18 18 true",
    "OMM_Mission9Hard": "LevelsOMM.swf/a_Level_OMMMission09GrahlsRebellion 33 18 true Hard",
    "OMM_Mission10": "LevelsOMM.swf/a_Level_OMMMission10DragonsQuarry 18 18 true",
    "OMM_Mission10Hard": "LevelsOMM.swf/a_Level_OMMMission10DragonsQuarry 33 18 true Hard",
    "OMM_Mission11": "LevelsOMM.swf/a_Level_OMMMission11CutToTheHeart 18 18 true",
    "OMM_Mission11Hard": "LevelsOMM.swf/a_Level_OMMMission11CutToTheHeart 33 18 true Hard",
    "OMM_Mission12": "LevelsOMM.swf/a_Level_OMMMission12MeylourFinale 21 21 true",
    "OMM_Mission12Hard": "LevelsOMM.swf/a_Level_OMMMission12MeylourFinale 36 21 true Hard",
    "--------EMERALD GLADES-----------": "",
    "EmeraldGlades": "LevelsEG.swf/a_Level_EmeraldGlade 19 19 false",
    "EmeraldGladesHard": "LevelsEG.swf/a_Level_EmeraldGlade 34 19 false Hard",
    "EG_Mission1": "LevelsEG.swf/a_Level_EGMission1 19 19 true",
    "EG_Mission1Hard": "LevelsEG.swf/a_Level_EGMission1 34 19 true Hard",
    "EG_Mission2": "LevelsEG.swf/a_Level_EGMission2 19 19 true",
    "EG_Mission2Hard": "LevelsEG.swf/a_Level_EGMission2 34 19 true Hard",
    "EG_Mission3": "LevelsEG.swf/a_Level_EGMission3 20 20 true",
    "EG_Mission3Hard": "LevelsEG.swf/a_Level_EGMission3 35 20 true Hard",
    "EG_Mission4": "LevelsEG.swf/a_Level_EGMission4 20 20 true",
    "G_Mission4Hard": "LevelsEG.swf/a_Level_EGMission4 35 20 true Hard",
    "EG_Mission5": "LevelsEG.swf/a_Level_EGMission5 20 20 true",
    "EG_Mission5Hard": "LevelsEG.swf/a_Level_EGMission5 35 20 true Hard",
    "--------DEEPGARD CASTLE------------": "",
    "Castle": "LevelsAC.swf/a_Level_DeepgardCastle 21 21 false",
    "CastleHard": "LevelsAC.swf/a_Level_DeepgardCastle 36 21 false Hard",
    "AC_Mission1": "LevelsAC.swf/a_Level_DeepgardDragon 21 21 true",
    "AC_Mission1Hard": "LevelsAC.swf/a_Level_DeepgardDragon 36 21 true Hard",
    "AC_Mission2": "LevelsAC.swf/a_Level_TheEmeraldThrone 21 21 true",
    "AC_Mission2Hard": "LevelsAC.swf/a_Level_TheEmeraldThrone 36 21 true Hard",
    "AC_Mission3": "LevelsAC.swf/a_Level_BattlesLostAndWon 21 21 true",
    "AC_Mission3Hard": "LevelsAC.swf/a_Level_BattlesLostAndWon 36 21 true Hard",
    "AC_Mission4": "LevelsAC.swf/a_Level_AethericObservatory 22 22 true",
    "AC_Mission4Hard": "LevelsAC.swf/a_Level_AethericObservatory 37 22 true Hard",
    "AC_Mission5": "LevelsAC.swf/a_Level_Ramparts 22 22 true",
    "AC_Mission5Hard": "LevelsAC.swf/a_Level_Ramparts 37 22 true Hard",
    "AC_Mission6": "LevelsAC.swf/a_Level_Capstone 22 22 true",
    "AC_Mission6Hard": "LevelsAC.swf/a_Level_Capstone 37 22 true Hard",
    "--------SHAZARI DESERT------------": "",
    "ShazariDesert": "LevelsSD.swf/a_Level_ShazariDesert 23 23 false",
    "ShazariDesertHard": "LevelsSD.swf/a_Level_ShazariDesert 38 23 false Hard",
    "SD_Mission1": "LevelsSD.swf/a_Level_SDMission1 23 23 true",
    "SD_Mission1Hard": "LevelsSD.swf/a_Level_SDMission1 38 23 true Hard",
    "SD_Mission2": "LevelsSD.swf/a_Level_SDMission2 23 23 true",
    "SD_Mission2Hard": "LevelsSD.swf/a_Level_SDMission2 38 23 true Hard",
    "SD_Mission3": "LevelsSD.swf/a_Level_SDMission3 24 24 true",
    "SD_Mission3Hard": "LevelsSD.swf/a_Level_SDMission3 39 24 true Hard",
    "SD_Mission4": "LevelsSD.swf/a_Level_SDMission4 24 24 true",
    "SD_Mission4Hard": "LevelsSD.swf/a_Level_SDMission4 39 24 true Hard",
    "SD_Mission5": "LevelsSD.swf/a_Level_SDMission5 25 25 true",
    "SD_Mission5Hard": "LevelsSD.swf/a_Level_SDMission5 40 25 true Hard",
    "SD_Mission6": "LevelsSD.swf/a_Level_SDMission6 25 25 true",
    "SD_Mission6Hard": "LevelsSD.swf/a_Level_SDMission6 40 25 true Hard",
    "SD_Tales1Escort": "TalesSD.swf/a_Level_SDTales1Escort 44 29 true",
    "SD_Tales2Surprise": "TalesSD.swf/a_Level_SDTales2Surprise 44 29 true",
    "SD_Tales3Remodel": "TalesSD.swf/a_Level_SDTales3Remodel 44 29 true",
    "SD_Tales4Oasis": "TalesSD.swf/a_Level_SDTales4Oasis 44 29 true",
    "SD_Tales5Defense": "TalesSD.swf/a_Level_SDTales5Defense 44 29 true",
    "SD_Tales6Time": "TalesSD.swf/a_Level_SDTales6Time 44 29 true",
    "--------VALHAVEN------------": "",
    "JadeCity": "LevelsJC.swf/a_Level_JadeCity 26 26 false",
    "JadeCityHard": "LevelsJC.swf/a_Level_JadeCity 41 26 false Hard",
    "JC_Mission1": "LevelsJC.swf/a_Level_JCMission1 26 26 true",
    "JC_Mission1Hard": "LevelsJC.swf/a_Level_JCMission1 41 26 true Hard",
    "JC_Mission2": "LevelsJC.swf/a_Level_JCMission2 27 27 true",
    "JC_Mission2Hard": "LevelsJC.swf/a_Level_JCMission2 42 27 true Hard",
    "JC_Mission3": "LevelsJC.swf/a_Level_JCMission3 27 27 true",
    "JC_Mission3Hard": "LevelsJC.swf/a_Level_JCMission3 42 27 true Hard",
    "JC_Mission4": "LevelsJC.swf/a_Level_JCMission4 28 28 true",
    "JC_Mission4Hard": "LevelsJC.swf/a_Level_JCMission4 43 28 true Hard",
    "JC_Mission5": "LevelsJC.swf/a_Level_JCMission5 28 28 true",
    "JC_Mission5Hard": "LevelsJC.swf/a_Level_JCMission5 43 28 true Hard",
    "JC_Mission6": "LevelsJC.swf/a_Level_JCMission6 29 29 true",
    "JC_Mission6Hard": "LevelsJC.swf/a_Level_JCMission6 44 29 true Hard",
    "JC_Mission7": "LevelsJC.swf/a_Level_JCMission7 30 30 true",
    "JC_Mission7Hard": "LevelsJC.swf/a_Level_JCMission7 45 30 true Hard",
    "JC_Mission8": "LevelsJC.swf/a_Level_JCMission8 29 29 true",
    "JC_Mission8Hard": "LevelsJC.swf/a_Level_JCMission8 44 29 true Hard",
    "JC_Mission9": "LevelsJC.swf/a_Level_JCMission9 28 28 true",
    "JC_Mission9Hard": "LevelsJC.swf/a_Level_JCMission9 43 28 true Hard",
    "JC_Mission10": "LevelsJC.swf/a_Level_JCMission10 28 28 true",
    "JC_Mission10Hard": "LevelsJC.swf/a_Level_JCMission10 43 28 true Hard",
    "JC_Mission11": "LevelsJC.swf/a_Level_JCMission11 27 27 true",
    "JC_Mission11Hard": "LevelsJC.swf/a_Level_JCMission11 42 27 true Hard",
    "JC_Mini1": "LevelsJC.swf/a_Level_JCMini1 29 29 true",
    "JC_Mini1Hard": "LevelsJC.swf/a_Level_JCMini1 44 29 true Hard",
    "JC_Mini2": "LevelsJC.swf/a_Level_JCMini2 29 29 true",
    "JC_Mini2Hard": "LevelsJC.swf/a_Level_JCMini2 44 29 true Hard",
    "--------PROTOTYPES------------": ""
}

DOOR_MAP = {
    # from 'AC_Mission1'
    ('AC_Mission1', 2): 'Castle',
    # from 'AC_Mission1Hard'
    ('AC_Mission1Hard', 2): 'CastleHard',
    # from 'BT_Mission3'
    ('BT_Mission3', 2): 'BridgeTown',
    # from 'BT_Mission3Hard'
    ('BT_Mission3Hard', 2): 'BridgeTownHard',
    # from 'BridgeTown'
    ('BridgeTown', 1): 'SwampRoadConnectionMission',
    ('BridgeTown', 2): 'CemeteryHill',
    ('BridgeTown', 3): 'AC_Mission1',
    ('BridgeTown', 5): 'CemeteryHill',
    ('BridgeTown', 6): 'OldMineMountain',
    ('BridgeTown', 101): 'BT_Mission1',
    ('BridgeTown', 102): 'BT_Mission2',
    ('BridgeTown', 103): 'BT_Mission3',
    ('BridgeTown', 104): 'BT_Mission4',
    ('BridgeTown', 300): 'BridgeTownHard',
    # from 'BridgeTownHard'
    ('BridgeTownHard', 1): 'SwampRoadConnectionHard',
    ('BridgeTownHard', 2): 'CemeteryHillHard',
    ('BridgeTownHard', 3): 'AC_Mission1Hard',
    ('BridgeTownHard', 5): 'CemeteryHillHard',
    ('BridgeTownHard', 6): 'OldMineMountainHard',
    ('BridgeTownHard', 101): 'BT_Mission1Hard',
    ('BridgeTownHard', 102): 'BT_Mission2Hard',
    ('BridgeTownHard', 103): 'BT_Mission3Hard',
    ('BridgeTownHard', 104): 'BT_Mission4Hard',
    ('BridgeTownHard', 300): 'BridgeTown',
    # from 'Castle'
    ('Castle', 1): 'BridgeTown',
    ('Castle', 4): 'ShazariDesert',
    ('Castle', 101): 'AC_Mission1',
    ('Castle', 102): 'AC_Mission2',
    ('Castle', 103): 'AC_Mission3',
    ('Castle', 104): 'AC_Mission4',
    ('Castle', 105): 'AC_Mission5',
    ('Castle', 106): 'AC_Mission6',
    # from 'CastleHard'
    ('CastleHard', 1): 'BridgeTownHard',
    ('CastleHard', 4): 'ShazariDesertHard',
    ('CastleHard', 101): 'AC_Mission1Hard',
    ('CastleHard', 102): 'AC_Mission2Hard',
    ('CastleHard', 103): 'AC_Mission3Hard',
    ('CastleHard', 104): 'AC_Mission4Hard',
    ('CastleHard', 105): 'AC_Mission5Hard',
    ('CastleHard', 106): 'AC_Mission6Hard',
    # from 'CemeteryHill'
    ('CemeteryHill', 1): 'BridgeTown',
    ('CemeteryHill', 3): 'BridgeTown',
    ('CemeteryHill', 101): 'CH_Mission1',
    ('CemeteryHill', 102): 'CH_Mission2',
    ('CemeteryHill', 103): 'CH_Mission3',
    ('CemeteryHill', 104): 'CH_Mission4',
    ('CemeteryHill', 105): 'CH_Mission5',
    ('CemeteryHill', 106): 'CH_Mission6',
    ('CemeteryHill', 107): 'CH_Mission7',
    ('CemeteryHill', 108): 'CH_Mission8',
    ('CemeteryHill', 201): 'CH_MiniMission1',
    ('CemeteryHill', 202): 'CH_MiniMission2',
    ('CemeteryHill', 203): 'CH_MiniMission3',
    ('CemeteryHill', 204): 'CH_MiniMission4',
    ('CemeteryHill', 205): 'CH_MiniMission5',
    ('CemeteryHill', 206): 'CH_MiniMission6',
    ('CemeteryHill', 207): 'CH_MiniMission7',
    ('CemeteryHill', 208): 'CH_MiniMission8',
    ('CemeteryHill', 209): 'CH_MiniMission9',
    # from 'CemeteryHillHard'
    ('CemeteryHillHard', 1): 'BridgeTownHard',
    ('CemeteryHillHard', 3): 'BridgeTownHard',
    ('CemeteryHillHard', 101): 'CH_Mission1Hard',
    ('CemeteryHillHard', 102): 'CH_Mission2Hard',
    ('CemeteryHillHard', 103): 'CH_Mission3Hard',
    ('CemeteryHillHard', 104): 'CH_Mission4Hard',
    ('CemeteryHillHard', 105): 'CH_Mission5Hard',
    ('CemeteryHillHard', 106): 'CH_Mission6Hard',
    ('CemeteryHillHard', 107): 'CH_Mission7Hard',
    ('CemeteryHillHard', 108): 'CH_Mission8Hard',
    ('CemeteryHillHard', 201): 'CH_MiniMission1Hard',
    ('CemeteryHillHard', 202): 'CH_MiniMission2Hard',
    ('CemeteryHillHard', 203): 'CH_MiniMission3Hard',
    ('CemeteryHillHard', 204): 'CH_MiniMission4Hard',
    ('CemeteryHillHard', 205): 'CH_MiniMission5Hard',
    ('CemeteryHillHard', 206): 'CH_MiniMission6Hard',
    ('CemeteryHillHard', 207): 'CH_MiniMission7Hard',
    ('CemeteryHillHard', 208): 'CH_MiniMission8Hard',
    ('CemeteryHillHard', 209): 'CH_MiniMission9Hard',
    # from 'CraftTownTutorial'
    ('CraftTownTutorial', 2): 'CraftTown',
    # from 'EmeraldGlades'
    ('EmeraldGlades', 1): 'OldMineMountain',
    ('EmeraldGlades', 101): 'EG_Mission1',
    ('EmeraldGlades', 102): 'EG_Mission2',
    ('EmeraldGlades', 103): 'EG_Mission3',
    ('EmeraldGlades', 104): 'EG_Mission4',
    ('EmeraldGlades', 105): 'EG_Mission5',
    ('EmeraldGlades', 300): 'EmeraldGladesHard',
    # from 'EmeraldGladesHard'
    ('EmeraldGladesHard', 1): 'OldMineMountainHard',
    ('EmeraldGladesHard', 101): 'EG_Mission1Hard',
    ('EmeraldGladesHard', 102): 'EG_Mission2Hard',
    ('EmeraldGladesHard', 103): 'EG_Mission3Hard',
    ('EmeraldGladesHard', 104): 'EG_Mission4Hard',
    ('EmeraldGladesHard', 105): 'EG_Mission5Hard',
    ('EmeraldGladesHard', 300): 'EmeraldGlades',
    # from 'JC_Mission1'
    ('JC_Mission1', 2): 'JadeCity',
    # from 'JC_Mission1Hard'
    ('JC_Mission1Hard', 2): 'JadeCityHard',
    # from 'JC_Mission2'
    ('JC_Mission2', 2): 'JC_Mission3',
    # from 'JC_Mission2Hard'
    ('JC_Mission2Hard', 2): 'JC_Mission3Hard',
    # from 'JadeCity'
    ('JadeCity', 1): 'ShazariDesert',
    ('JadeCity', 101): 'JC_Mission1',
    ('JadeCity', 102): 'JC_Mission2',
    ('JadeCity', 103): 'JC_Mission3',
    ('JadeCity', 104): 'JC_Mission4',
    ('JadeCity', 105): 'JC_Mission5',
    ('JadeCity', 106): 'JC_Mission6',
    ('JadeCity', 107): 'JC_Mission7',
    ('JadeCity', 108): 'JC_Mission8',
    ('JadeCity', 109): 'JC_Mission9',
    ('JadeCity', 110): 'JC_Mission10',
    ('JadeCity', 111): 'JC_Mission11',
    ('JadeCity', 201): 'JC_Mini1',
    ('JadeCity', 202): 'JC_Mini2',
    ('JadeCity', 300): 'JadeCityHard',
    # from 'JadeCityHard'
    ('JadeCityHard', 1): 'ShazariDesertHard',
    ('JadeCityHard', 101): 'JC_Mission1Hard',
    ('JadeCityHard', 102): 'JC_Mission2Hard',
    ('JadeCityHard', 103): 'JC_Mission3Hard',
    ('JadeCityHard', 104): 'JC_Mission4Hard',
    ('JadeCityHard', 105): 'JC_Mission5Hard',
    ('JadeCityHard', 106): 'JC_Mission6Hard',
    ('JadeCityHard', 107): 'JC_Mission7Hard',
    ('JadeCityHard', 108): 'JC_Mission8Hard',
    ('JadeCityHard', 109): 'JC_Mission9Hard',
    ('JadeCityHard', 110): 'JC_Mission10Hard',
    ('JadeCityHard', 111): 'JC_Mission11Hard',
    ('JadeCityHard', 201): 'JC_Mini1Hard',
    ('JadeCityHard', 202): 'JC_Mini2Hard',
    ('JadeCityHard', 300): 'JadeCity',
    # from 'NewbieRoad'
    ('NewbieRoad', 2): 'SwampRoadNorth',
    ('NewbieRoad', 101): 'TutorialDungeon',
    ('NewbieRoad', 102): 'GhostBossDungeon',
    ('NewbieRoad', 103): 'DreamDragonDungeon',
    ('NewbieRoad', 104): 'TutorialBoat',
    ('NewbieRoad', 105): 'GoblinRiverDungeon',
    # from 'NewbieRoadHard'
    ('NewbieRoadHard', 2): 'SwampRoadNorthHard',
    ('NewbieRoadHard', 101): 'TutorialDungeonHard',
    ('NewbieRoadHard', 102): 'GhostBossDungeonHard',
    ('NewbieRoadHard', 103): 'DreamDragonDungeonHard',
    ('NewbieRoadHard', 105): 'GoblinRiverDungeonHard',
    # from 'OMM_Mission10'
    ('OMM_Mission10', 2): 'OMM_Mission11',
    # from 'OMM_Mission10Hard'
    ('OMM_Mission10Hard', 2): 'OMM_Mission11Hard',
    # from 'OMM_Mission11'
    ('OMM_Mission11', 2): 'EmeraldGlades',
    # from 'OMM_Mission11Hard'
    ('OMM_Mission11Hard', 2): 'EmeraldGladesHard',
    # from 'OMM_Mission8'
    ('OMM_Mission8', 2): 'OMM_Mission9',
    # from 'OMM_Mission8Hard'
    ('OMM_Mission8Hard', 2): 'OMM_Mission9Hard',
    # from 'OMM_Mission9'
    ('OMM_Mission9', 2): 'OMM_Mission10',
    # from 'OMM_Mission9Hard'
    ('OMM_Mission9Hard', 2): 'OMM_Mission10Hard',
    # from 'OldMineMountain'
    ('OldMineMountain', 1): 'BridgeTown',
    ('OldMineMountain', 2): 'EmeraldGlades',
    ('OldMineMountain', 101): 'OMM_Mission1',
    ('OldMineMountain', 102): 'OMM_Mission2',
    ('OldMineMountain', 103): 'OMM_Mission3',
    ('OldMineMountain', 104): 'OMM_Mission4',
    ('OldMineMountain', 105): 'OMM_Mission5',
    ('OldMineMountain', 106): 'OMM_Mission6',
    ('OldMineMountain', 107): 'OMM_Mission7',
    ('OldMineMountain', 108): 'OMM_Mission8',
    ('OldMineMountain', 109): 'OMM_Mission9',
    ('OldMineMountain', 110): 'OMM_Mission10',
    ('OldMineMountain', 111): 'OMM_Mission11',
    ('OldMineMountain', 112): 'OMM_Mission12',
    # from 'OldMineMountainHard'
    ('OldMineMountainHard', 1): 'BridgeTownHard',
    ('OldMineMountainHard', 2): 'EmeraldGladesHard',
    ('OldMineMountainHard', 101): 'OMM_Mission1Hard',
    ('OldMineMountainHard', 102): 'OMM_Mission2Hard',
    ('OldMineMountainHard', 103): 'OMM_Mission3Hard',
    ('OldMineMountainHard', 104): 'OMM_Mission4Hard',
    ('OldMineMountainHard', 105): 'OMM_Mission5Hard',
    ('OldMineMountainHard', 106): 'OMM_Mission6Hard',
    ('OldMineMountainHard', 107): 'OMM_Mission7Hard',
    ('OldMineMountainHard', 108): 'OMM_Mission8Hard',
    ('OldMineMountainHard', 109): 'OMM_Mission9Hard',
    ('OldMineMountainHard', 110): 'OMM_Mission10Hard',
    ('OldMineMountainHard', 111): 'OMM_Mission11Hard',
    ('OldMineMountainHard', 112): 'OMM_Mission12Hard',
    # from 'ShazariDesert'
    ('ShazariDesert', 1): 'Castle',
    ('ShazariDesert', 2): 'JC_Mission1',
    ('ShazariDesert', 101): 'SD_Mission1',
    ('ShazariDesert', 102): 'SD_Mission2',
    ('ShazariDesert', 103): 'SD_Mission3',
    ('ShazariDesert', 104): 'SD_Mission4',
    ('ShazariDesert', 105): 'SD_Mission5',
    ('ShazariDesert', 106): 'SD_Mission6',
    ('ShazariDesert', 300): 'ShazariDesertHard',
    # from 'ShazariDesertHard'
    ('ShazariDesertHard', 1): 'CastleHard',
    ('ShazariDesertHard', 2): 'JC_Mission1Hard',
    ('ShazariDesertHard', 101): 'SD_Mission1Hard',
    ('ShazariDesertHard', 102): 'SD_Mission2Hard',
    ('ShazariDesertHard', 103): 'SD_Mission3Hard',
    ('ShazariDesertHard', 104): 'SD_Mission4Hard',
    ('ShazariDesertHard', 105): 'SD_Mission5Hard',
    ('ShazariDesertHard', 106): 'SD_Mission6Hard',
    ('ShazariDesertHard', 300): 'ShazariDesert',
    # from 'SwampRoadConnection'
    ('SwampRoadConnection', 1): 'SwampRoadNorth',
    ('SwampRoadConnection', 2): 'BridgeTown',
    ('SwampRoadConnection', 101): 'SwampRoadConnectionMission',
    # from 'SwampRoadConnectionHard'
    ('SwampRoadConnectionHard', 1): 'SwampRoadNorthHard',
    ('SwampRoadConnectionHard', 2): 'BridgeTownHard',
    ('SwampRoadConnectionHard', 101): 'SwampRoadConnectionMissionHard',
    # from 'SwampRoadConnectionMission'
    ('SwampRoadConnectionMission', 2): 'BridgeTown',
    # from 'SwampRoadConnectionMissionHard'
    ('SwampRoadConnectionMissionHard', 2): 'BridgeTownHard',
    # from 'SwampRoadNorth'
    ('SwampRoadNorth', 1): 'SwampRoadConnectionMission',
    ('SwampRoadNorth', 2): 'NewbieRoad',
    ('SwampRoadNorth', 101): 'SRN_Mission1',
    ('SwampRoadNorth', 102): 'SRN_Mission2',
    ('SwampRoadNorth', 103): 'SRN_Mission3',
    ('SwampRoadNorth', 104): 'SRN_Mission4',
    ('SwampRoadNorth', 105): 'SRN_Mission5',
    ('SwampRoadNorth', 106): 'SRN_Mission6',
    ('SwampRoadNorth', 107): 'SRN_Mission7',
    # from 'SwampRoadNorthHard'
    ('SwampRoadNorthHard', 1): 'SwampRoadConnectionHard',
    ('SwampRoadNorthHard', 2): 'NewbieRoadHard',
    ('SwampRoadNorthHard', 101): 'SRN_Mission1Hard',
    ('SwampRoadNorthHard', 102): 'SRN_Mission2Hard',
    ('SwampRoadNorthHard', 103): 'SRN_Mission3Hard',
    ('SwampRoadNorthHard', 104): 'SRN_Mission4Hard',
    ('SwampRoadNorthHard', 105): 'SRN_Mission5Hard',
    ('SwampRoadNorthHard', 106): 'SRN_Mission6Hard',
    ('SwampRoadNorthHard', 107): 'SRN_Mission7Hard',
    # from 'TutorialDungeon'
    ('TutorialDungeon', 2): 'NewbieRoad',
}

LEVEL_CONFIG = {}
for name, spec in _raw_level_config.items():
    parts = spec.split()
    if len(parts) < 4 or not parts[0]:
        # skip blank entries or separators
        continue

    swf_path    = parts[0]
    map_lvl     = int(parts[1])
    base_lvl    = int(parts[2])
    is_inst     = parts[3].lower() == "true"
    # (we ignore any extra “Hard” token here)
    LEVEL_CONFIG[name] = (swf_path, map_lvl, base_lvl, is_inst)