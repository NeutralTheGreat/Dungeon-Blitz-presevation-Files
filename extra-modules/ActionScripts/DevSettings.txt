package
{
   public class DevSettings
   {
      
      private static var FLAG_ITERATOR:uint = 0;
      
      public static const DEVFLAG_STANDALONE_CLIENT:uint = 1 << 0;
      
      public static const DEVFLAG_SERVERLOCAL:uint = 1 << 1;
      
      public static const DEVFLAG_SHOWENTITYCOLLISION:uint = 1 << 2;
      
      public static const DEVFLAG_SHOWENTITYGHOST:uint = 1 << 3;
      
      public static const DEVFLAG_PERFORMANCETEST:uint = 1 << 4;
      
      public static const DEVFLAG_SPAWN_MONSTERS:uint = 1 << 5;
      
      public static const DEVFLAG_DUMBMONSTERS:uint = 1 << 6;
      
      public static const DEVFLAG_OUTLINE_REMOTE_ENTS:uint = 1 << 7;
      
      public static const DEVFLAG_MASTER_CLIENT:uint = 1 << 8;
      
      public static const DEVFLAG_NO_GRAPHICS:uint = 1 << 9;
      
      public static const DEVFLAG_NO_PLAYERENT:uint = 1 << 10;
      
      public static const DEVFLAG_SHOWCUES:uint = 1 << 11;
      
      public static const DEVFLAG_ADDXMLDEVSETTINGS:uint = 1 << 12;
      
      public static const DEVFLAG_SHOWCHARACTERCREATE:uint = 1 << 13;
      
      public static const DEVFLAG_SHOWPOWERRANGE:uint = 1 << 14;
      
      public static const DEVFLAG_SHOWBEHAVIOR:uint = 1 << 15;
      
      public static const const_511:uint = 1 << 16;
      
      public static const DEVFLAG_SHOWRESOURCEMONITOR:uint = 1 << 17;
      
      public static const DEVFLAG_DEVSPAWNENABLED:uint = 1 << 18;
      
      public static const DEVFLAG_SHOWWORLDCOLLISION:uint = 1 << 19;
      
      public static const const_938:uint = 1 << 20;
      
      public static const DEVFLAG_SHOWPERFORMANCE:uint = 1 << 21;
      
      public static const const_1124:uint = 1 << 22;
      
      public static var flags:uint;
      
      public static var var_2032:String = "127.0.0.1";
      
      public static var standAlonePlayerEntType:String = "DevPaladin";
      
      public static var var_2990:String;
      
      public static var standAloneMapName:String = "LevelsHome.swf/a_Level_Home";
      
      public static var standAloneMomentParams:String = "";
      
      public static var standAloneAlterParams:String = "";
      
      public static var standAloneMapInternalName:String = "CraftTown";
      
      public static var standAloneMapLevel:uint = 1;
      
      public static var var_1351:uint = 1;
      
      public static var standAloneIsInstanced:Boolean = true;
      
      public static var var_5:Array = new Array();
      
      {
         var_5["01CraftTown"] = "LevelsHome.swf/a_Level_Home 1 1 true";
         var_5["02CraftTownTutorial"] = "LevelsHome.swf/a_Level_HomeTutorial 1 1 true";
         var_5["055--------WOLFS END------------"] = "";
         var_5["06TutorialBoat"] = "LevelsTut.swf/a_Level_TutorialBoat 1 1 true";
         var_5["07NewbieRoad"] = "LevelsNR.swf/a_Level_NewbieRoad 1 1 false";
         var_5["07NewbieRoadHard"] = "LevelsNR.swf/a_Level_NewbieRoad 36 1 false Hard";
         var_5["08TutorialDungeon"] = "LevelsNR.swf/a_Level_NRTutorial 2 2 true";
         var_5["08TutorialDungeonHard"] = "LevelsNR.swf/a_Level_GoblinBeachHard 37 2 true Hard";
         var_5["08GoblinRiverDungeon"] = "LevelsNR.swf/a_Level_GoblinRiver 3 3 true";
         var_5["08GoblinRiverDungeonHard"] = "LevelsNR.swf/a_Level_GoblinRiver 38 3 true Hard";
         var_5["09GhostBossDungeon"] = "LevelsNR.swf/a_Level_NRGhost 4 4 true";
         var_5["09GhostBossDungeonHard"] = "LevelsNR.swf/a_Level_NRGhost 39 4 true Hard";
         var_5["100DreamDragonDungeon"] = "LevelsNR.swf/a_Level_NRDragon 5 5 true";
         var_5["100DreamDragonDungeonHard"] = "LevelsNR.swf/a_Level_NRDragon 40 5 true Hard";
         var_5["101NR_Tales1Keep"] = "TalesNR.swf/a_Level_NRTales1Keep 44 29 true";
         var_5["102NR_Tales2Anna"] = "TalesNR.swf/a_Level_NRTales2Anna 44 29 true";
         var_5["103NR_Tales3Bazaar"] = "TalesNR.swf/a_Level_NRTales3Bazaar 44 29 true";
         var_5["104NR_Tales4Research"] = "TalesNR.swf/a_Level_NRTales4Research 44 29 true";
         var_5["105NR_Tales5DreamCave"] = "TalesNR.swf/a_Level_NRTales5DreamCave 44 29 true";
         var_5["107--------BLACKROSE MIRE------------"] = "";
         var_5["11SwampRoadNorth"] = "LevelsSRN.swf/a_Level_SwampRoadNorth 6 6 false";
         var_5["11SwampRoadNorthHard"] = "LevelsSRN.swf/a_Level_SwampRoadNorth 31 6 false Hard";
         var_5["12SRN_Mission1"] = "LevelsSRN.swf/a_Level_SRNMission1Castout 6 6 true";
         var_5["12SRN_Mission1Hard"] = "LevelsSRN.swf/a_Level_SRNMission1Castout 31 6 true Hard";
         var_5["13SRN_Mission2"] = "LevelsSRN.swf/a_Level_SRNMission2Yornak 7 7 true";
         var_5["13SRN_Mission2Hard"] = "LevelsSRN.swf/a_Level_SRNMission2Yornak 32 7 true Hard";
         var_5["14SRN_Mission3"] = "LevelsSRN.swf/a_Level_SRNMission3Svar 8 8 true";
         var_5["14SRN_Mission3Hard"] = "LevelsSRN.swf/a_Level_SRNMission3Svar 33 8 true Hard";
         var_5["15SRN_Mission4"] = "LevelsSRN.swf/a_Level_SRNMission4Ooyak 8 8 true";
         var_5["15SRN_Mission4Hard"] = "LevelsSRN.swf/a_Level_SRNMission4Ooyak 33 8 true Hard";
         var_5["16SRN_Mission5"] = "LevelsSRN.swf/a_Level_SRNMission5Broodvictor 9 9 true";
         var_5["16SRN_Mission5Hard"] = "LevelsSRN.swf/a_Level_SRNMission5Broodvictor 34 9 true Hard";
         var_5["17SRN_Mission6"] = "LevelsSRN.swf/a_Level_SRNMission6MindlessQueen 8 8 true";
         var_5["17SRN_Mission6Hard"] = "LevelsSRN.swf/a_Level_SRNMission6MindlessQueen 33 8 true Hard";
         var_5["18SRN_Mission7"] = "LevelsSRN.swf/a_Level_SRNMission7Svath 9 9 true";
         var_5["18SRN_Mission7Hard"] = "LevelsSRN.swf/a_Level_SRNMission7Svath 34 9 true Hard";
         var_5["19SwampRoadConnection"] = "LevelsSRN.swf/a_Level_SwampRoadConnection 10 10 false";
         var_5["19SwampRoadConnectionHard"] = "LevelsSRN.swf/a_Level_SwampRoadConnection 35 10 false Hard";
         var_5["200SwampRoadConnectionMission"] = "LevelsSRN.swf/a_Level_SwampRoadConnectionMission 10 10 true";
         var_5["200SwampRoadConnectionMissionHard"] = "LevelsSRN.swf/a_Level_SwampRoadConnectionMission 35 10 true Hard";
         var_5["205--------FELBRIDGE------------"] = "";
         var_5["21BridgeTown"] = "LevelsBT.swf/a_Level_BridgeTown 10 10 false";
         var_5["21BridgeTownHard"] = "LevelsBT.swf/a_Level_BridgeTown 25 10 false Hard";
         var_5["22BT_Mission1"] = "LevelsBT.swf/a_Level_BTMission1 11 11 true";
         var_5["22BT_Mission1Hard"] = "LevelsBT.swf/a_Level_BTMission1 26 11 true Hard";
         var_5["23BT_Mission2"] = "LevelsBT.swf/a_Level_BTMission2 12 12 true";
         var_5["23BT_Mission2Hard"] = "LevelsBT.swf/a_Level_BTMission2 27 12 true Hard";
         var_5["24BT_Mission3"] = "LevelsBT.swf/a_Level_BTMission3 14 14 true";
         var_5["24BT_Mission3Hard"] = "LevelsBT.swf/a_Level_BTMission3 29 14 true Hard";
         var_5["250BT_Mission4"] = "LevelsBT.swf/a_Level_BTMission4 15 15 true";
         var_5["250BT_Mission4Hard"] = "LevelsBT.swf/a_Level_BTMission4 30 15 true Hard";
         var_5["251LDArena1"] = "LevelsLD.swf/a_Level_LDArena1 50 50 true";
         var_5["255--------CEMETERY HILL------------"] = "";
         var_5["26CemeteryHill"] = "LevelsCH.swf/a_Level_CemeteryHill 11 11 false";
         var_5["26CemeteryHillHard"] = "LevelsCH.swf/a_Level_CemeteryHill 26 11 false Hard";
         var_5["27CH_Mission1"] = "LevelsCH.swf/a_Level_CHMission1 11 11 true";
         var_5["27CH_Mission1Hard"] = "LevelsCH.swf/a_Level_CHMission1 26 11 true Hard";
         var_5["28CH_Mission2"] = "LevelsCH.swf/a_Level_CHMission2 11 11 true";
         var_5["28CH_Mission2Hard"] = "LevelsCH.swf/a_Level_CHMission2 26 11 true Hard";
         var_5["29CH_Mission3"] = "LevelsCH.swf/a_Level_CHMission3 13 13 true";
         var_5["29CH_Mission3Hard"] = "LevelsCH.swf/a_Level_CHMission3 28 13 true Hard";
         var_5["30CH_Mission4"] = "LevelsCH.swf/a_Level_CHMission4 12 12 true";
         var_5["30CH_Mission4Hard"] = "LevelsCH.swf/a_Level_CHMission4 27 12 true Hard";
         var_5["31CH_Mission5"] = "LevelsCH.swf/a_Level_CHMission5 12 12 true";
         var_5["31CH_Mission5Hard"] = "LevelsCH.swf/a_Level_CHMission5 27 12 true Hard";
         var_5["32CH_Mission6"] = "LevelsCH.swf/a_Level_CHMission6 14 14 true";
         var_5["32CH_Mission6Hard"] = "LevelsCH.swf/a_Level_CHMission6 29 14 true Hard";
         var_5["33CH_Mission7"] = "LevelsCH.swf/a_Level_CHMission7 15 15 true";
         var_5["33CH_Mission7Hard"] = "LevelsCH.swf/a_Level_CHMission7 30 15 true Hard";
         var_5["34CH_Mission8"] = "LevelsCH.swf/a_Level_CHMission8 15 15 true";
         var_5["34CH_Mission8Hard"] = "LevelsCH.swf/a_Level_CHMission8 30 15 true Hard";
         var_5["35CH_MiniMission1"] = "LevelsCH.swf/a_Level_CHMini1 11 11 true";
         var_5["35CH_MiniMission1Hard"] = "LevelsCH.swf/a_Level_CHMini1 26 11 true Hard";
         var_5["36CH_MiniMission2"] = "LevelsCH.swf/a_Level_CHMini2 11 11 true";
         var_5["36CH_MiniMission2Hard"] = "LevelsCH.swf/a_Level_CHMini2 26 11 true Hard";
         var_5["37CH_MiniMission3"] = "LevelsCH.swf/a_Level_CHMini3 12 12 true";
         var_5["37CH_MiniMission3Hard"] = "LevelsCH.swf/a_Level_CHMini3 27 12 true Hard";
         var_5["38CH_MiniMission4"] = "LevelsCH.swf/a_Level_CHMini4 12 12 true";
         var_5["38CH_MiniMission4Hard"] = "LevelsCH.swf/a_Level_CHMini4 27 12 true Hard";
         var_5["39CH_MiniMission5"] = "LevelsCH.swf/a_Level_CHMini5 13 13 true";
         var_5["39CH_MiniMission5Hard"] = "LevelsCH.swf/a_Level_CHMini5 28 13 true Hard";
         var_5["40CH_MiniMission6"] = "LevelsCH.swf/a_Level_CHMini6 13 13 true";
         var_5["40CH_MiniMission6Hard"] = "LevelsCH.swf/a_Level_CHMini6 28 13 true Hard";
         var_5["41CH_MiniMission7"] = "LevelsCH.swf/a_Level_CHMini7 14 14 true";
         var_5["41CH_MiniMission7Hard"] = "LevelsCH.swf/a_Level_CHMini7 29 14 true Hard";
         var_5["42CH_MiniMission8"] = "LevelsCH.swf/a_Level_CHMini8 14 14 true";
         var_5["42CH_MiniMission8Hard"] = "LevelsCH.swf/a_Level_CHMini8 29 14 true Hard";
         var_5["430CH_MiniMission9"] = "LevelsCH.swf/a_Level_CHMini9 15 15 true";
         var_5["430CH_MiniMission9Hard"] = "LevelsCH.swf/a_Level_CHMini9 30 15 true Hard";
         var_5["435--------STORMSHARD------------"] = "";
         var_5["44OldMineMountain"] = "LevelsOMM.swf/a_Level_OldMineMountain 16 16 false";
         var_5["44OldMineMountainHard"] = "LevelsOMM.swf/a_Level_OldMineMountain 31 16 false Hard";
         var_5["45OMM_Mission1"] = "LevelsOMM.swf/a_Level_OMMMission01GiveVoiceToStone 16 16 true";
         var_5["45OMM_Mission1Hard"] = "LevelsOMM.swf/a_Level_OMMMission01GiveVoiceToStone 31 16 true Hard";
         var_5["46OMM_Mission2"] = "LevelsOMM.swf/a_Level_OMMMission02RockHulkGarden 16 16 true";
         var_5["46OMM_Mission2Hard"] = "LevelsOMM.swf/a_Level_OMMMission02RockHulkGarden 31 16 true Hard";
         var_5["47OMM_Mission3"] = "LevelsOMM.swf/a_Level_OMMMission03EyeOfTheTyrant 16 16 true";
         var_5["47OMM_Mission3Hard"] = "LevelsOMM.swf/a_Level_OMMMission03EyeOfTheTyrant 31 16 true Hard";
         var_5["48OMM_Mission4"] = "LevelsOMM.swf/a_Level_OMMMission04AbandonedArmory 17 17 true";
         var_5["48OMM_Mission4Hard"] = "LevelsOMM.swf/a_Level_OMMMission04AbandonedArmory 32 17 true Hard";
         var_5["49OMM_Mission5"] = "LevelsOMM.swf/a_Level_OMMMission05HuntedToTheEdge 17 17 true";
         var_5["49OMM_Mission5Hard"] = "LevelsOMM.swf/a_Level_OMMMission05HuntedToTheEdge 32 17 true Hard";
         var_5["50OMM_Mission6"] = "LevelsOMM.swf/a_Level_OMMMission06ForgottenForge 17 17 true";
         var_5["50OMM_Mission6Hard"] = "LevelsOMM.swf/a_Level_OMMMission06ForgottenForge 32 17 true Hard";
         var_5["51OMM_Mission7"] = "LevelsOMM.swf/a_Level_OMMMission07GriffinsRedoubt 17 17 true";
         var_5["51OMM_Mission7Hard"] = "LevelsOMM.swf/a_Level_OMMMission07GriffinsRedoubt 32 17 true Hard";
         var_5["52OMM_Mission8"] = "LevelsOMM.swf/a_Level_OMMMission08BloodInTheVeins 18 18 true";
         var_5["52OMM_Mission8Hard"] = "LevelsOMM.swf/a_Level_OMMMission08BloodInTheVeins 33 18 true Hard";
         var_5["53OMM_Mission9"] = "LevelsOMM.swf/a_Level_OMMMission09GrahlsRebellion 18 18 true";
         var_5["53OMM_Mission9Hard"] = "LevelsOMM.swf/a_Level_OMMMission09GrahlsRebellion 33 18 true Hard";
         var_5["54OMM_Mission10"] = "LevelsOMM.swf/a_Level_OMMMission10DragonsQuarry 18 18 true";
         var_5["54OMM_Mission10Hard"] = "LevelsOMM.swf/a_Level_OMMMission10DragonsQuarry 33 18 true Hard";
         var_5["550OMM_Mission11"] = "LevelsOMM.swf/a_Level_OMMMission11CutToTheHeart 18 18 true";
         var_5["550OMM_Mission11Hard"] = "LevelsOMM.swf/a_Level_OMMMission11CutToTheHeart 33 18 true Hard";
         var_5["551OMM_Mission12"] = "LevelsOMM.swf/a_Level_OMMMission12MeylourFinale 21 21 true";
         var_5["551OMM_Mission12Hard"] = "LevelsOMM.swf/a_Level_OMMMission12MeylourFinale 36 21 true Hard";
         var_5["555--------EMERALD GLADES-----------"] = "";
         var_5["56EmeraldGlades"] = "LevelsEG.swf/a_Level_EmeraldGlade 19 19 false";
         var_5["56EmeraldGladesHard"] = "LevelsEG.swf/a_Level_EmeraldGlade 34 19 false Hard";
         var_5["57EG_Mission1"] = "LevelsEG.swf/a_Level_EGMission1 19 19 true";
         var_5["57EG_Mission1Hard"] = "LevelsEG.swf/a_Level_EGMission1 34 19 true Hard";
         var_5["58EG_Mission2"] = "LevelsEG.swf/a_Level_EGMission2 19 19 true";
         var_5["58EG_Mission2Hard"] = "LevelsEG.swf/a_Level_EGMission2 34 19 true Hard";
         var_5["59EG_Mission3"] = "LevelsEG.swf/a_Level_EGMission3 20 20 true";
         var_5["59EG_Mission3Hard"] = "LevelsEG.swf/a_Level_EGMission3 35 20 true Hard";
         var_5["60EG_Mission4"] = "LevelsEG.swf/a_Level_EGMission4 20 20 true";
         var_5["60EG_Mission4Hard"] = "LevelsEG.swf/a_Level_EGMission4 35 20 true Hard";
         var_5["610EG_Mission5"] = "LevelsEG.swf/a_Level_EGMission5 20 20 true";
         var_5["610EG_Mission5Hard"] = "LevelsEG.swf/a_Level_EGMission5 35 20 true Hard";
         var_5["615--------DEEPGARD CASTLE------------"] = "";
         var_5["62Castle"] = "LevelsAC.swf/a_Level_DeepgardCastle 21 21 false";
         var_5["62CastleHard"] = "LevelsAC.swf/a_Level_DeepgardCastle 36 21 false Hard";
         var_5["63AC_Mission1"] = "LevelsAC.swf/a_Level_DeepgardDragon 21 21 true";
         var_5["63AC_Mission1Hard"] = "LevelsAC.swf/a_Level_DeepgardDragon 36 21 true Hard";
         var_5["64AC_Mission2"] = "LevelsAC.swf/a_Level_TheEmeraldThrone 21 21 true";
         var_5["64AC_Mission2Hard"] = "LevelsAC.swf/a_Level_TheEmeraldThrone 36 21 true Hard";
         var_5["65AC_Mission3"] = "LevelsAC.swf/a_Level_BattlesLostAndWon 21 21 true";
         var_5["65AC_Mission3Hard"] = "LevelsAC.swf/a_Level_BattlesLostAndWon 36 21 true Hard";
         var_5["66AC_Mission4"] = "LevelsAC.swf/a_Level_AethericObservatory 22 22 true";
         var_5["66AC_Mission4Hard"] = "LevelsAC.swf/a_Level_AethericObservatory 37 22 true Hard";
         var_5["67AC_Mission5"] = "LevelsAC.swf/a_Level_Ramparts 22 22 true";
         var_5["67AC_Mission5Hard"] = "LevelsAC.swf/a_Level_Ramparts 37 22 true Hard";
         var_5["680AC_Mission6"] = "LevelsAC.swf/a_Level_Capstone 22 22 true";
         var_5["680AC_Mission6Hard"] = "LevelsAC.swf/a_Level_Capstone 37 22 true Hard";
         var_5["687--------SHAZARI DESERT------------"] = "";
         var_5["69ShazariDesert"] = "LevelsSD.swf/a_Level_ShazariDesert 23 23 false";
         var_5["69ShazariDesertHard"] = "LevelsSD.swf/a_Level_ShazariDesert 38 23 false Hard";
         var_5["70SD_Mission1"] = "LevelsSD.swf/a_Level_SDMission1 23 23 true";
         var_5["70SD_Mission1Hard"] = "LevelsSD.swf/a_Level_SDMission1 38 23 true Hard";
         var_5["71SD_Mission2"] = "LevelsSD.swf/a_Level_SDMission2 23 23 true";
         var_5["71SD_Mission2Hard"] = "LevelsSD.swf/a_Level_SDMission2 38 23 true Hard";
         var_5["72SD_Mission3"] = "LevelsSD.swf/a_Level_SDMission3 24 24 true";
         var_5["72SD_Mission3Hard"] = "LevelsSD.swf/a_Level_SDMission3 39 24 true Hard";
         var_5["73SD_Mission4"] = "LevelsSD.swf/a_Level_SDMission4 24 24 true";
         var_5["73SD_Mission4Hard"] = "LevelsSD.swf/a_Level_SDMission4 39 24 true Hard";
         var_5["74SD_Mission5"] = "LevelsSD.swf/a_Level_SDMission5 25 25 true";
         var_5["74SD_Mission5Hard"] = "LevelsSD.swf/a_Level_SDMission5 40 25 true Hard";
         var_5["750SD_Mission6"] = "LevelsSD.swf/a_Level_SDMission6 25 25 true";
         var_5["750SD_Mission6Hard"] = "LevelsSD.swf/a_Level_SDMission6 40 25 true Hard";
         var_5["751SD_Tales1Escort"] = "TalesSD.swf/a_Level_SDTales1Escort 44 29 true";
         var_5["752SD_Tales2Surprise"] = "TalesSD.swf/a_Level_SDTales2Surprise 44 29 true";
         var_5["753SD_Tales3Remodel"] = "TalesSD.swf/a_Level_SDTales3Remodel 44 29 true";
         var_5["754SD_Tales4Oasis"] = "TalesSD.swf/a_Level_SDTales4Oasis 44 29 true";
         var_5["755SD_Tales5Defense"] = "TalesSD.swf/a_Level_SDTales5Defense 44 29 true";
         var_5["756SD_Tales6Time"] = "TalesSD.swf/a_Level_SDTales6Time 44 29 true";
         var_5["757--------VALHAVEN------------"] = "";
         var_5["76JadeCity"] = "LevelsJC.swf/a_Level_JadeCity 26 26 false";
         var_5["76JadeCityHard"] = "LevelsJC.swf/a_Level_JadeCity 41 26 false Hard";
         var_5["77JC_Mission1"] = "LevelsJC.swf/a_Level_JCMission1 26 26 true";
         var_5["77JC_Mission1Hard"] = "LevelsJC.swf/a_Level_JCMission1 41 26 true Hard";
         var_5["78JC_Mission2"] = "LevelsJC.swf/a_Level_JCMission2 27 27 true";
         var_5["78JC_Mission2Hard"] = "LevelsJC.swf/a_Level_JCMission2 42 27 true Hard";
         var_5["79JC_Mission3"] = "LevelsJC.swf/a_Level_JCMission3 27 27 true";
         var_5["79JC_Mission3Hard"] = "LevelsJC.swf/a_Level_JCMission3 42 27 true Hard";
         var_5["80JC_Mission4"] = "LevelsJC.swf/a_Level_JCMission4 28 28 true";
         var_5["80JC_Mission4Hard"] = "LevelsJC.swf/a_Level_JCMission4 43 28 true Hard";
         var_5["81JC_Mission5"] = "LevelsJC.swf/a_Level_JCMission5 28 28 true";
         var_5["81JC_Mission5Hard"] = "LevelsJC.swf/a_Level_JCMission5 43 28 true Hard";
         var_5["82JC_Mission6"] = "LevelsJC.swf/a_Level_JCMission6 29 29 true";
         var_5["82JC_Mission6Hard"] = "LevelsJC.swf/a_Level_JCMission6 44 29 true Hard";
         var_5["83JC_Mission7"] = "LevelsJC.swf/a_Level_JCMission7 30 30 true";
         var_5["83JC_Mission7Hard"] = "LevelsJC.swf/a_Level_JCMission7 45 30 true Hard";
         var_5["84JC_Mission8"] = "LevelsJC.swf/a_Level_JCMission8 29 29 true";
         var_5["84JC_Mission8Hard"] = "LevelsJC.swf/a_Level_JCMission8 44 29 true Hard";
         var_5["85JC_Mission9"] = "LevelsJC.swf/a_Level_JCMission9 28 28 true";
         var_5["85JC_Mission9Hard"] = "LevelsJC.swf/a_Level_JCMission9 43 28 true Hard";
         var_5["86JC_Mission10"] = "LevelsJC.swf/a_Level_JCMission10 28 28 true";
         var_5["86JC_Mission10Hard"] = "LevelsJC.swf/a_Level_JCMission10 43 28 true Hard";
         var_5["87JC_Mission11"] = "LevelsJC.swf/a_Level_JCMission11 27 27 true";
         var_5["87JC_Mission11Hard"] = "LevelsJC.swf/a_Level_JCMission11 42 27 true Hard";
         var_5["88JC_Mini1"] = "LevelsJC.swf/a_Level_JCMini1 29 29 true";
         var_5["88JC_Mini1Hard"] = "LevelsJC.swf/a_Level_JCMini1 44 29 true Hard";
         var_5["89JC_Mini2"] = "LevelsJC.swf/a_Level_JCMini2 29 29 true";
         var_5["90JC_Mini2Hard"] = "LevelsJC.swf/a_Level_JCMini2 44 29 true Hard";
         var_5["93--------PROTOTYPES------------"] = "";
      }
      
      public function DevSettings()
      {
         super();
      }
      
      public static function method_1539(param1:class_34) : void
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc2_:XML = new XML(param1.var_182.data);
         for each(_loc3_ in _loc2_.*)
         {
            _loc4_ = String(_loc3_.name().toString().toUpperCase());
            if(DevSettings[_loc4_])
            {
               DevSettings.flags = DevSettings.flags | DevSettings[_loc4_];
            }
            else if(_loc4_ == "STANDALONEMAPNAME")
            {
               DevSettings.standAloneMapName = _loc3_.attribute("value");
            }
            else if(_loc4_ == "STANDALONEMAPINTERNALNAME")
            {
               DevSettings.standAloneMapInternalName = _loc3_.attribute("value");
            }
            else if(_loc4_ == "STANDALONEMOMENTPARAMS")
            {
               DevSettings.standAloneMomentParams = _loc3_.attribute("value");
            }
            else if(_loc4_ == "STANDALONEALTERPARAMS")
            {
               DevSettings.standAloneAlterParams = _loc3_.attribute("value");
            }
            else if(_loc4_ == "STANDALONEPLAYERENTTYPE")
            {
               DevSettings.standAlonePlayerEntType = _loc3_.attribute("value");
            }
            else if(_loc4_ == "STANDALONEISINSTANCED")
            {
               DevSettings.standAloneIsInstanced = MathUtil.method_50(_loc3_.attribute("value"));
            }
            else if(_loc4_ == "STANDALONEMAPLEVEL")
            {
               DevSettings.standAloneMapLevel = uint(_loc3_.attribute("value"));
            }
            else if(_loc4_ == "STANDALONEBASELEVEL")
            {
               DevSettings.var_1351 = uint(_loc3_.attribute("value"));
            }
         }
      }
      
      public static function method_275() : void
      {
         if(Boolean(flags) && !(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
         {
            class_24.method_7("Cannot load this swf");
         }
      }
   }
}
