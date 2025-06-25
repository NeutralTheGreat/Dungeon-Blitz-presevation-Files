package
{
   import flash.display.Bitmap;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.filters.*;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   import flash.utils.Dictionary;
   
   public class ScreenArmory extends class_32
   {
      
      private static const const_1307:BevelFilter = new BevelFilter(2,45,0,0.9,16777215,0.9,1,1,4,BitmapFilterQuality.HIGH,BitmapFilterType.INNER,false);
      
      public static const const_1091:GlowFilter = new GlowFilter(7792093,1,4,4,30,BitmapFilterQuality.HIGH);
      
      public static const const_1422:GlowFilter = new GlowFilter(1502741,1,4,4,30,BitmapFilterQuality.HIGH);
      
      public static const const_1355:GlowFilter = new GlowFilter(1502741,1,2,2,30,BitmapFilterQuality.HIGH);
      
      public static const const_24:uint = 15655612;
      
      public static const const_315:uint = 52275;
      
      public static const const_22:uint = 39423;
      
      public static const const_23:uint = 16309573;
      
      public static const const_137:uint = 14296385;
      
      public static const const_106:uint = 52479;
      
      public static const const_11:uint = 15655612;
      
      public static const const_9:uint = 10066329;
      
      public static const const_455:uint = 3418894;
      
      public static const const_1125:uint = 23319;
      
      public static const const_814:uint = 11336;
      
      public static const const_672:uint = 5194498;
      
      public static const const_169:uint = 6230044;
      
      public static const const_417:uint = 11575;
      
      public static const const_47:uint = 3418894;
      
      public static const const_17:uint = 3552822;
      
      public static const const_59:uint = 4870213;
      
      public static const const_915:uint = 6640667;
      
      private static const const_1367:String = "am_Charm_Icon";
      
      private static const const_25:Dictionary = new Dictionary();
      
      public static const const_857:uint = 0;
      
      public static const const_881:uint = 1;
      
      public static const const_1107:uint = 2;
      
      private static const const_120:uint = 0;
      
      private static const const_86:uint = 1;
      
      private static const const_231:uint = 2;
      
      private static const const_68:uint = 3;
      
      private static const const_242:uint = 4;
      
      private static const const_278:uint = 5;
      
      private static const const_799:uint = 6;
      
      private static const const_402:uint = 0;
      
      private static const const_284:uint = 1;
      
      private static const const_484:uint = 2;
      
      private static const const_335:uint = 3;
      
      private static const const_427:uint = 4;
      
      private static const const_668:uint = 5;
      
      private static const const_134:uint = 6;
      
      public static const const_10:uint = 28;
      
      private static const STAT_PAGE1_NAMES:Dictionary = new Dictionary();
      
      private static const STAT_PAGE2_NAMES:Dictionary = new Dictionary();
      
      private static const STAT_PAGE1_DESCRIPTIONS:Dictionary = new Dictionary();
      
      private static const STAT_PAGE2_DESCRIPTIONS:Dictionary = new Dictionary();
      
      private static var var_21:Dictionary = new Dictionary();
      
      private static var var_22:Dictionary = new Dictionary();
      
      private static var var_32:Dictionary = new Dictionary();
      
      private static const const_708:String = "<font color=\'#999999\'>" + "??" + class_127.var_121;
      
      private static const const_678:String = "<font color=\'#999999\'>" + "??" + class_127.var_121;
      
      private static const const_1327:Vector.<String> = Vector.<String>(["Gear","Charm","Material","Pet","Mount","Consumable"]);
      
      private static const const_940:Vector.<String> = Vector.<String>(["Gear","Charms","Crafting Materials","Pets","Mounts","Consumables"]);
      
      private static const const_1288:uint = 8;
      
      public static const const_12:uint = 28;
      
      private static const const_806:Number = 1.012;
      
      public static const const_179:uint = 0;
      
      public static const const_180:uint = 1;
      
      public static const const_196:uint = 2;
      
      public static const const_504:uint = 3;
      
      private static const const_434:uint = 0;
      
      private static const const_462:uint = 1;
      
      private static const const_575:uint = 2;
      
      private static const const_493:uint = 3;
      
      public static const const_514:uint = 4;
      
      private static const const_412:uint = 0;
      
      private static const const_488:uint = 1;
      
      private static const const_510:uint = 2;
      
      private static const const_566:uint = 3;
      
      private static const const_418:uint = 4;
      
      private static const const_450:uint = 5;
      
      private static const const_460:uint = 6;
      
      private static const const_489:uint = 7;
      
      private static const const_519:uint = 8;
      
      public static const const_513:uint = 9;
      
      private static const const_486:uint = 0;
      
      private static const const_541:uint = 1;
      
      private static const const_453:uint = 2;
      
      private static const const_444:uint = 3;
      
      public static const const_497:uint = 4;
      
      public static const const_815:uint = 3;
      
      public static const const_155:uint = 18;
      
      public static const const_27:uint = 3;
      
      public static const const_397:uint = 4;
      
      private static const const_1098:Number = 1;
      
      private static const const_1034:Number = 0.35;
      
      private static const const_407:Number = -50;
      
      private static const const_1292:ColorMatrixFilter = new ColorMatrixFilter([0,0,0,0,const_407,0,0,0,0,const_407,0,0,0,0,const_407,0,0,0,1,0]);
      
      private static const const_875:uint = 4;
      
      private static const const_1030:Number = 0.75;
      
      private static const const_375:uint = 30;
      
      private static const const_955:String = "M";
      
      private static const const_1318:String = "R";
      
      private static const const_1050:String = "L";
      
      private static const const_471:uint = 13;
      
      private static const const_38:Vector.<String> = new Vector.<String>(const_471,true);
      
      {
         const_25["NewbieRoad"] = 0;
         const_25["NewbieRoadHard"] = 0;
         const_25["SwampRoadNorth"] = 1;
         const_25["SwampRoadNorthHard"] = 1;
         const_25["BridgeTown"] = 3;
         const_25["BridgeTownHard"] = 3;
         const_25["CemeteryHill"] = 4;
         const_25["CemeteryHillHard"] = 4;
         const_25["OldMineMountain"] = 6;
         const_25["OldMineMountainHard"] = 6;
         const_25["EmeraldGlades"] = 8;
         const_25["EmeraldGladesHard"] = 8;
         const_25["Castle"] = 9;
         const_25["CastleHard"] = 9;
         const_25["ShazariDesert"] = 10;
         const_25["ShazariDesertHard"] = 10;
         const_25["JadeCity"] = 11;
         const_25["JadeCityHard"] = 11;
         STAT_PAGE1_NAMES[0] = "Class and Level";
         STAT_PAGE1_NAMES[1] = "Health";
         STAT_PAGE1_NAMES[2] = "Attack";
         STAT_PAGE1_NAMES[3] = "Expertise";
         STAT_PAGE1_NAMES[4] = "Defense";
         STAT_PAGE1_NAMES[5] = "Attack Speed";
         STAT_PAGE1_NAMES[6] = "Critical Chance";
         STAT_PAGE1_NAMES[7] = "Critical Power";
         STAT_PAGE1_NAMES[8] = "Recovery";
         STAT_PAGE1_NAMES[9] = "Movement Speed";
         STAT_PAGE1_NAMES[10] = "Tenacity";
         STAT_PAGE2_NAMES[0] = "Gear Finding";
         STAT_PAGE2_NAMES[1] = "Material Finding";
         STAT_PAGE2_NAMES[2] = "Gold Finding";
         STAT_PAGE2_NAMES[3] = "XP Boost";
         STAT_PAGE2_NAMES[4] = "Ice Slaying";
         STAT_PAGE2_NAMES[5] = "Ice Protection";
         STAT_PAGE2_NAMES[6] = "Fire Slaying";
         STAT_PAGE2_NAMES[7] = "Fire Protection";
         STAT_PAGE2_NAMES[8] = "Air Slaying";
         STAT_PAGE2_NAMES[9] = "Air Protection";
         STAT_PAGE2_NAMES[10] = "Earth Slaying";
         STAT_PAGE2_NAMES[11] = "Earth Protection";
         STAT_PAGE2_NAMES[12] = "Life Slaying";
         STAT_PAGE2_NAMES[13] = "Life Protection";
         STAT_PAGE2_NAMES[14] = "Dark Slaying";
         STAT_PAGE2_NAMES[15] = "Dark Protection";
         STAT_PAGE1_DESCRIPTIONS[0] = "Your character\'s class and level";
         STAT_PAGE1_DESCRIPTIONS[1] = "Amount of damage you can take before you die";
         STAT_PAGE1_DESCRIPTIONS[2] = "Determines the amount of damage you deal with attacks";
         STAT_PAGE1_DESCRIPTIONS[3] = "Determines the effectiveness of healing and status effects";
         STAT_PAGE1_DESCRIPTIONS[4] = "Reduces the amount of damage you take from monsters";
         STAT_PAGE1_DESCRIPTIONS[5] = "Increases the speed of your basic melee and ranged attacks";
         STAT_PAGE1_DESCRIPTIONS[6] = "Increases the chance of gaining a critical hit";
         STAT_PAGE1_DESCRIPTIONS[7] = "Increases the damage of your critical hits";
         STAT_PAGE1_DESCRIPTIONS[8] = "Increases the amount of healing you receive";
         STAT_PAGE1_DESCRIPTIONS[9] = "Increases how fast your chatacter can run";
         STAT_PAGE1_DESCRIPTIONS[10] = "Reduces the duration of movement impairing effects";
         STAT_PAGE2_DESCRIPTIONS[0] = "Increases the chance of finding new gear when you kill monsters";
         STAT_PAGE2_DESCRIPTIONS[1] = "Increases the chance of finding materials when you kill monsters";
         STAT_PAGE2_DESCRIPTIONS[2] = "Increases the amount of gold dropped by monsters";
         STAT_PAGE2_DESCRIPTIONS[3] = "Increases the amount of XP gained from monsters";
         STAT_PAGE2_DESCRIPTIONS[4] = "Increases the damage dealt to Ice elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[5] = "Reduces the damage taken from Ice elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[6] = "Increases the damage dealt to Fire elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[7] = "Reduces the damage taken from Fire elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[8] = "Increases the damage dealt to Air elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[9] = "Reduces the damage taken from Air elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[10] = "Increases the damage dealt to Earth elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[11] = "Reduces the damage taken from Earth elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[12] = "Increases the damage dealt to Life elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[13] = "Reduces the damage taken from Life elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[14] = "Increases the damage dealt to Dark elemental creatures";
         STAT_PAGE2_DESCRIPTIONS[15] = "Reduces the damage taken from Dark elemental creatures";
         var_21["AncientDragonGold"] = "Grand Marshal Sythokahn";
         var_21["DreadLord"] = "Dread Paladin Lothyr";
         var_21["SpiritDragon"] = "General Sythoryll";
         var_21["SpiritDemonMaligner"] = "Nephit";
         var_21["AncientDragonSilver"] = "Legion Commander Sythrog";
         var_21["NephitLargeEye"] = "Nephit";
         var_21["BanditTwinB"] = "Delexa";
         var_21["GriffonStar"] = "Wrath";
         var_21["MeylourBossMage"] = "Tessa, The High Witch";
         var_21["AbominationBrute"] = "Steward of Felbridge";
         var_21["YoungDragonGray"] = "Ravenous Drake";
         var_21["DogChieftain"] = "Kamak the Packlord";
         var_21["RedGhostLord"] = "Cornelius Hocke";
         var_21["GreaterSkeletonBoss"] = "Lord Tilly";
         var_21["DemonMaligner"] = "Nephit the Great and Wise";
         var_21["MummyBoss"] = "Dottore Aeschius";
         var_21["DragonBone"] = "Nephit the Terrible";
         var_21["JackalChieftain"] = "Rafhiu the Liberator";
         var_21["AshenDryadWizard"] = "Ashen Mother";
         var_21["AshenDryadHero"] = "Coalglow";
         var_21["DragonSea"] = "Meylour\'s Sacrifice";
         var_21["FirePriestBoss"] = "Gohzani Priest of Meylour";
         var_21["FirePriestWizard"] = "Ahjani, Priest of Meylour";
         var_21["ImperialChampion"] = "Imperial Commander Grahl";
         var_21["GreaterBoneGolem"] = "Seelie Ravager";
         var_21["DefectorMage"] = "Prince Friedrich Hocke";
         var_21["RatlingKing"] = "The Gutter Lord";
         var_21["PortalMaster"] = "An\'Irus, Seelie Lord";
         var_21["NephitDragon"] = "The Last Bad Dream";
         var_21["Emperor"] = "Emperor Sigismund Hocke";
         var_21["GuardCaptain"] = "Commander Hagen";
         var_21["RisenBandit"] = "Shadow of Authority";
         var_21["DragonTemple"] = "General Sytherix, Retired";
         var_21["BrigandChamp"] = "Davan Longcut";
         var_21["GoblinBoss2"] = "Chief Tourzahl";
         var_21["GoblinBoss1"] = "Tag Ugo";
         var_21["GrayGhostLord"] = "Nephit";
         var_21["YoungDragonDream"] = "Sythokhan’s Dream";
         var_21["BlackGoblinBoss1"] = "Red Fang";
         var_21["CaveWizard"] = "Sindra";
         var_21["CyclopsChieftain"] = "Gaze of Meylour";
         var_21["BlackGhostLord"] = "Watchman Siggard";
         var_21["LionLord"] = "General Svahl";
         var_21["DragonRed"] = "Svael the Glorious";
         var_21["GriffonSun"] = "Transcendent Gnole";
         var_21["RockCyclopsChieftain"] = "Overseer";
         var_21["GriffonMoon"] = "Scion of Meylour";
         var_21["DragonGray"] = "Sveyl, Meylour\'s Chosen";
         var_21["RockHulkKing"] = "Avatar of Meylour";
         var_21["MagmaCyclopsBoss"] = "Meylour";
         var_21["RageGuardian"] = "Pharoh Amenrahtep";
         var_21["ScarabScorpion"] = "Enormous Sandspawn";
         var_21["OutlanderBoss"] = "The Pit Lord";
         var_21["OasisVizier"] = "Dejih the Ogre-Magus";
         var_21["SandWormGreater"] = "Sand Leviathan";
         var_21["GolemLord"] = "The Prime Builder";
         var_21["LizardLord"] = "Tuatara Commander";
         var_21["SwampKing"] = "Lord Yornak";
         var_21["YoungDragonGreen"] = "General Svar";
         var_21["WyrmGreat"] = "Brood Mother";
         var_21["GreatLizardLord"] = "Grand Vizier Hslat";
         var_21["DevourerGreat"] = "Devourer Queen";
         var_21["DragonGreen"] = "General Svath";
         var_21["SwampSpiderQueen"] = "Arachnae";
         var_22["AncientDragonGold"] = "AC_Mission1";
         var_22["DreadLord"] = "AC_Mission2";
         var_22["SpiritDragon"] = "AC_Mission3";
         var_22["SpiritDemonMaligner"] = "AC_Mission4";
         var_22["AncientDragonSilver"] = "AC_Mission5";
         var_22["NephitLargeEye"] = "AC_Mission6";
         var_22["BanditTwinB"] = "BT_Mission1";
         var_22["GriffonStar"] = "BT_Mission2";
         var_22["MeylourBossMage"] = "BT_Mission3";
         var_22["AbominationBrute"] = "BT_Mission4";
         var_22["YoungDragonGray"] = "CH_Mission1";
         var_22["DogChieftain"] = "CH_Mission2";
         var_22["RedGhostLord"] = "CH_Mission3";
         var_22["GreaterSkeletonBoss"] = "CH_Mission4";
         var_22["DemonMaligner"] = "CH_Mission5";
         var_22["MummyBoss"] = "CH_Mission6";
         var_22["DragonBone"] = "CH_Mission7";
         var_22["JackalChieftain"] = "CH_Mission8";
         var_22["AshenDryadWizard"] = "EG_Mission1";
         var_22["AshenDryadHero"] = "EG_Mission2";
         var_22["DragonSea"] = "EG_Mission3";
         var_22["FirePriestBoss"] = "EG_Mission4";
         var_22["FirePriestWizard"] = "EG_Mission5";
         var_22["ImperialChampion"] = "JC_Mission1";
         var_22["GreaterBoneGolem"] = "JC_Mission2";
         var_22["DefectorMage"] = "JC_Mission3";
         var_22["RatlingKing"] = "JC_Mission4";
         var_22["PortalMaster"] = "JC_Mission5";
         var_22["NephitDragon"] = "JC_Mission6";
         var_22["Emperor"] = "JC_Mission7";
         var_22["GuardCaptain"] = "JC_Mission8";
         var_22["RisenBandit"] = "JC_Mission9";
         var_22["DragonTemple"] = "JC_Mission10";
         var_22["BrigandChamp"] = "JC_Mission11";
         var_22["GoblinBoss2"] = "GoblinRiverDungeon";
         var_22["GoblinBoss1"] = "TutorialDungeon";
         var_22["GrayGhostLord"] = "GhostBossDungeon";
         var_22["YoungDragonDream"] = "DreamDragonDungeon";
         var_22["BlackGoblinBoss1"] = "OMM_Mission1";
         var_22["CaveWizard"] = "OMM_Mission2";
         var_22["CyclopsChieftain"] = "OMM_Mission3";
         var_22["BlackGhostLord"] = "OMM_Mission4";
         var_22["LionLord"] = "OMM_Mission5";
         var_22["DragonRed"] = "OMM_Mission6";
         var_22["GriffonSun"] = "OMM_Mission7";
         var_22["RockCyclopsChieftain"] = "OMM_Mission8";
         var_22["GriffonMoon"] = "OMM_Mission9";
         var_22["DragonGray"] = "OMM_Mission10";
         var_22["RockHulkKing"] = "OMM_Mission11";
         var_22["MagmaCyclopsBoss"] = "OMM_Mission12";
         var_22["RageGuardian"] = "SD_Mission1";
         var_22["ScarabScorpion"] = "SD_Mission2";
         var_22["OutlanderBoss"] = "SD_Mission3";
         var_22["OasisVizier"] = "SD_Mission4";
         var_22["SandWormGreater"] = "SD_Mission5";
         var_22["GolemLord"] = "SD_Mission6";
         var_22["LizardLord"] = "SRN_Mission1";
         var_22["SwampKing"] = "SRN_Mission2";
         var_22["YoungDragonGreen"] = "SRN_Mission3";
         var_22["WyrmGreat"] = "SRN_Mission4";
         var_22["GreatLizardLord"] = "SRN_Mission5";
         var_22["DevourerGreat"] = "SRN_Mission6";
         var_22["DragonGreen"] = "SRN_Mission7";
         var_22["SwampSpiderQueen"] = "SwampRoadConnectionMission";
         var_32["Ghost5"] = "DreamDragonDungeon";
         var_32["Goblin3"] = "GoblinRiverDungeon";
         var_32["Skeleton4"] = "DreamDragonDungeon";
         var_32["Lizard6"] = "SRN_Mission1";
         var_32["Treant7"] = "SRN_Mission6";
         var_32["Devourer8"] = "SRN_Mission7";
         var_32["Spider7"] = "SRN_Mission6";
         var_32["Wyrm8"] = "SRN_Mission4";
         var_32["Skeleton9"] = "SRN_Mission7";
         var_32["Lizard9"] = "SRN_Mission5";
         var_32["Wolf11"] = "CH_Mission1";
         var_32["Ghost12"] = "CH_Mission4";
         var_32["Skeleton12"] = "CH_Mission4";
         var_32["Ghost13"] = "CH_Mission3";
         var_32["Wolf15"] = "CH_Mission8";
         var_32["Skeleton15"] = "CH_Mission6";
         var_32["Mummy14"] = "CH_Mission6";
         var_32["Human12"] = "BT_Mission1";
         var_32["Human14"] = "BT_Mission4";
         var_32["Abomination15"] = "BT_Mission4";
         var_32["Raptor20"] = "EG_Mission4";
         var_32["Dryad19"] = "EG_Mission1";
         var_32["Devourer19"] = "EG_Mission2";
         var_32["Human20"] = "EG_Mission5";
         var_32["Cyclops17"] = "OMM_Mission7";
         var_32["Cyclops18"] = "OMM_Mission8";
         var_32["RockHulk18"] = "OMM_Mission11";
         var_32["Ghost17"] = "OMM_Mission4";
         var_32["Goblin17"] = "OMM_Mission10";
         var_32["Cyclops16"] = "OMM_Mission3";
         var_32["Lion17"] = "OMM_Mission5";
         var_32["Lizard18"] = "OMM_Mission11";
         var_32["RockHulk20"] = "OMM_Mission12";
         var_32["Lizard22"] = "AC_Mission1";
         var_32["Spirit22"] = "AC_Mission4";
         var_32["Dread21"] = "AC_Mission2";
         var_32["Raptor23"] = "SD_Mission1";
         var_32["Construct25"] = "SD_Mission6";
         var_32["Shade23"] = "SD_Mission1";
         var_32["Scarab25"] = "SD_Mission5";
         var_32["Scarab23"] = "SD_Mission2";
         var_32["Human24"] = "SD_Mission3";
         var_32["Giant24"] = "SD_Mission4";
         var_32["Minotaur24"] = "SD_Mission3";
         var_32["Skeleton28"] = "JC_Mission3";
         var_32["Imperial27"] = "JC_Mission1";
         var_32["Human27"] = "JC_Mission11";
         var_32["Shade27"] = "JC_Mission5";
         var_32["Spirit29"] = "JC_Mission6";
         var_32["Demon29"] = "JC_Mission5";
         var_32["Raptor29"] = "JC_Mission4";
         var_32["Ratling29"] = "JC_Mission4";
         var_32["Imperial29"] = "JC_Mini1";
         const_38[0] = "Wolf\'s End Gear";
         const_38[1] = "Black Rose Mire Gear 1/2";
         const_38[2] = "Black Rose Mire Gear 2/2";
         const_38[3] = "Felbridge Gear";
         const_38[4] = "Cemetery Hill Gear 1/2";
         const_38[5] = "Cemetery Hill Gear 2/2";
         const_38[6] = "Stormshard Mountain Gear 1/2";
         const_38[7] = "Stormshard Mountain Gear 2/2";
         const_38[8] = "The Emerald Glades Gear";
         const_38[9] = "Castle Hocke Gear";
         const_38[10] = "Shazari Desert Gear";
         const_38[11] = "Valhaven Gear 1/2";
         const_38[12] = "Valhaven Gear 2/2";
      }
      
      internal var var_529:Boolean;
      
      internal var var_1915:int = -1;
      
      public var var_2298:Array;
      
      private var var_1373:class_33;
      
      private var var_95:Vector.<class_33>;
      
      private var var_500:Vector.<class_33>;
      
      private var var_1764:class_33;
      
      private var var_587:Vector.<class_33>;
      
      private var var_56:uint;
      
      private var var_148:class_33;
      
      private var var_695:Vector.<class_33>;
      
      private var var_227:int;
      
      private var var_311:class_33;
      
      private var var_472:Vector.<class_33>;
      
      private var var_225:Vector.<class_33>;
      
      private var var_455:class_33;
      
      private var var_413:class_33;
      
      private var var_902:class_33;
      
      private var var_591:class_33;
      
      private var var_281:Vector.<class_33>;
      
      private var var_1291:Vector.<class_33>;
      
      private var var_1359:Vector.<class_33>;
      
      private var var_1012:class_33;
      
      private var var_1614:Vector.<class_33>;
      
      private var var_1493:class_33;
      
      private var var_1347:class_33;
      
      private var var_98:class_33;
      
      private var var_215:class_33;
      
      private var var_762:Vector.<class_33>;
      
      private var var_1863:Boolean = false;
      
      private var var_405:Vector.<class_33>;
      
      private var var_369:Vector.<class_33>;
      
      private var var_648:Vector.<class_33>;
      
      private var var_542:Vector.<class_33>;
      
      private var var_260:Vector.<class_33>;
      
      private var var_583:Vector.<class_33>;
      
      private var var_622:Vector.<class_33>;
      
      private var var_297:Vector.<class_33>;
      
      private var var_2851:class_138;
      
      private var var_1054:class_33;
      
      private var var_1885:class_33;
      
      private var mFilterPanelAbilityIconHolder0:class_33;
      
      private var mFilterPanelAbilityIconHolder1:class_33;
      
      private var mFilterPanelAbilityIconHolder2:class_33;
      
      private var var_2491:class_138;
      
      private var var_1768:class_33;
      
      private var var_1917:class_33;
      
      private var var_721:Vector.<class_33>;
      
      private var var_754:class_33;
      
      private var var_2738:class_138;
      
      private var var_2697:class_138;
      
      private var var_2000:Vector.<class_33>;
      
      private var var_1675:Vector.<class_33>;
      
      private var var_1684:Vector.<class_33>;
      
      private var var_1806:Vector.<class_33>;
      
      private var var_1941:Vector.<class_33>;
      
      private var var_1754:Vector.<class_33>;
      
      private var var_1892:class_33;
      
      private var var_1824:class_33;
      
      private var var_200:int = -1;
      
      private var var_570:int = -1;
      
      private var var_80:int = -1;
      
      private var var_1991:class_87;
      
      private var var_3001:int = -1;
      
      private var var_1965:class_3;
      
      private var var_2995:int = -1;
      
      public var var_2058:uint = 0;
      
      public var var_73:class_150;
      
      public var var_654:Vector.<class_103>;
      
      private var var_465:int = 0;
      
      private var var_466:class_33;
      
      private var var_2284:class_33;
      
      private var var_2409:class_33;
      
      private var var_2408:class_33;
      
      private var var_2009:Vector.<class_33>;
      
      private var var_1997:Vector.<class_33>;
      
      private var var_1798:Vector.<class_33>;
      
      private var var_601:Dictionary;
      
      private var var_977:Dictionary;
      
      private var var_2307:class_138;
      
      private var var_2012:class_33;
      
      private var var_2290:class_138;
      
      private var var_726:Dictionary;
      
      public function ScreenArmory(param1:Game)
      {
         super(param1,"a_ArmoryWindow",null);
      }
      
      public static function method_1229(param1:GearType, param2:TextField) : void
      {
         if(param1.var_8 == "L")
         {
            MathUtil.method_8(param2,param1.displayName,const_23);
         }
         else if(param1.var_8 == "R")
         {
            MathUtil.method_8(param2,param1.displayName,const_22);
         }
         else
         {
            MathUtil.method_8(param2,param1.displayName,const_24);
         }
      }
      
      public static function method_1818(param1:EntType, param2:GearType, param3:TextField) : void
      {
         var _loc4_:String = "";
         if(param2.var_8 == "L")
         {
            _loc4_ = "Legendary ";
         }
         else if(param2.var_8 == "R")
         {
            _loc4_ = "Rare ";
         }
         else
         {
            _loc4_ = "Magic ";
         }
         MathUtil.method_2(param3,_loc4_ + GearType.method_395(param1.className,param2.type));
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc6_:MovieClip = null;
         var _loc21_:MovieClip = null;
         var _loc22_:MovieClip = null;
         var _loc1_:MovieClip = var_2.am_InventoryGrid;
         this.var_95 = new Vector.<class_33>(const_12,true);
         var _loc2_:uint = 0;
         while(_loc2_ < const_12)
         {
            (_loc21_ = _loc1_["am_Slot" + _loc2_] as MovieClip).am_New.visible = false;
            _loc21_.am_Selector.visible = false;
            this.var_95[_loc2_] = method_3(_loc21_,_loc2_,this.method_1420,this.method_1298,this.method_74);
            _loc2_++;
         }
         this.var_1373 = method_27(var_2.am_ItemMaterialDetail);
         var _loc3_:MovieClip = var_2.am_TabGroupLower;
         this.var_587 = new Vector.<class_33>(const_799,true);
         this.var_587[const_120] = method_3(_loc3_.am_TabGear,const_120,this.method_179);
         this.var_587[const_86] = method_3(_loc3_.am_TabCharms,const_86,this.method_179);
         this.var_587[const_231] = method_3(_loc3_.am_TabMaterials,const_231,this.method_179);
         this.var_587[const_68] = method_3(_loc3_.am_TabPets,const_68,this.method_179);
         this.var_587[const_242] = method_3(_loc3_.am_TabMounts,const_242,this.method_179);
         this.var_587[const_278] = method_3(_loc3_.am_TabConsumables,const_278,this.method_179);
         this.var_56 = const_120;
         var _loc4_:MovieClip = var_2.am_SlideOut;
         this.var_148 = method_1(_loc4_);
         method_5(_loc4_.am_Panel.am_CloseSlideOut,this.method_1226);
         this.var_148.Hide();
         this.var_695 = new Vector.<class_33>(const_668,true);
         var _loc5_:MovieClip = var_2.am_SlideOutTabs;
         this.var_695[const_402] = method_3(_loc5_.am_TabStatistics,const_402,this.method_274);
         this.var_695[const_284] = method_3(_loc5_.am_TabStatistics2,const_284,this.method_274);
         this.var_695[const_484] = method_3(_loc5_.am_TabPrefab,const_484,this.method_274);
         this.var_695[const_335] = method_3(_loc5_.am_TabTreasureMap,const_335,this.method_274);
         this.var_695[const_427] = method_3(_loc5_.am_TabCurrency,const_427,this.method_274);
         this.var_227 = -1;
         var _loc7_:MovieClip;
         var _loc8_:uint = uint((_loc7_ = _loc4_.am_Panel.am_StatisticsGroup.am_ContactGroup).numChildren);
         _loc2_ = 0;
         while(_loc2_ < _loc8_)
         {
            _loc6_ = _loc7_["am_Contact" + _loc2_] as MovieClip;
            method_3(_loc6_,_loc2_,null,this.method_817,this.method_970);
            _loc2_++;
         }
         _loc8_ = uint((_loc7_ = _loc4_.am_Panel.am_ElementsGroup.am_ContactGroup).numChildren);
         _loc2_ = 0;
         while(_loc2_ < _loc8_)
         {
            _loc6_ = _loc7_["am_Contact" + _loc2_] as MovieClip;
            method_3(_loc6_,_loc2_,null,this.method_817,this.method_970);
            _loc2_++;
         }
         this.var_902 = method_1(var_2.am_StatisticDetail);
         this.var_902.Hide();
         var _loc9_:MovieClip;
         var _loc10_:MovieClip = (_loc9_ = _loc4_.am_Panel.am_Prefabs).am_GearSets;
         this.var_472 = new Vector.<class_33>(const_134,true);
         _loc2_ = 0;
         while(_loc2_ < const_134)
         {
            (_loc22_ = _loc10_["am_GearSet" + _loc2_] as MovieClip).am_Plus.visible = false;
            _loc22_.am_Selector.visible = false;
            this.var_472[_loc2_] = method_3(_loc22_,_loc2_,this.method_1905);
            _loc2_++;
         }
         var _loc11_:MovieClip = _loc9_.am_EquipmentGroup;
         this.var_225 = new Vector.<class_33>(EntType.MAX_SLOTS,true);
         this.var_225[EntType.SWORD_SLOT] = method_3(_loc11_.am_Sword,EntType.SWORD_SLOT,this.method_204,this.method_228,this.method_74);
         this.var_225[EntType.SHIELD_SLOT] = method_3(_loc11_.am_Shield,EntType.SHIELD_SLOT,this.method_204,this.method_228,this.method_74);
         this.var_225[EntType.HAT_SLOT] = method_3(_loc11_.am_Hat,EntType.HAT_SLOT,this.method_204,this.method_228,this.method_74);
         this.var_225[EntType.ARMOR_SLOT] = method_3(_loc11_.am_Armor,EntType.ARMOR_SLOT,this.method_204,this.method_228,this.method_74);
         this.var_225[EntType.GLOVES_SLOT] = method_3(_loc11_.am_Gloves,EntType.GLOVES_SLOT,this.method_204,this.method_228,this.method_74);
         this.var_225[EntType.BOOTS_SLOT] = method_3(_loc11_.am_Boots,EntType.BOOTS_SLOT,this.method_204,this.method_228,this.method_74);
         this.var_1892 = method_5(_loc9_.am_Equip,this.method_1025);
         this.var_1824 = method_5(_loc9_.am_Rename,this.method_1166);
         this.var_455 = method_5(_loc9_.am_Save,this.method_814);
         this.var_413 = method_5(_loc9_.am_Overwrite,this.method_814);
         this.var_413.Hide();
         this.var_311 = method_1(_loc9_.am_RenamePrompt);
         method_5(_loc9_.am_RenamePrompt.am_CloseRename,this.method_1651);
         method_5(_loc9_.am_RenamePrompt.am_SaveName,this.method_1867);
         this.var_311.Hide();
         var _loc12_:TextField;
         (_loc12_ = this.var_311.mMovieClip.am_NameField).maxChars = 16;
         _loc12_.restrict = "A-Za-z0-9/.,;\'[]\\-=<>?:\"{}_+\\\\~!@#$%\\^&*() ";
         var _loc13_:MovieClip = var_2.am_EquipmentSlots;
         var _loc14_:uint = uint(const_1288 + 1);
         this.var_500 = new Vector.<class_33>(_loc14_,true);
         this.var_500[EntType.SWORD_SLOT] = method_3(_loc13_.am_Sword,EntType.SWORD_SLOT,this.method_217,this.method_199,this.method_74);
         this.var_500[EntType.SHIELD_SLOT] = method_3(_loc13_.am_Shield,EntType.SHIELD_SLOT,this.method_217,this.method_199,this.method_74);
         this.var_500[EntType.HAT_SLOT] = method_3(_loc13_.am_Hat,EntType.HAT_SLOT,this.method_217,this.method_199,this.method_74);
         this.var_500[EntType.ARMOR_SLOT] = method_3(_loc13_.am_Armor,EntType.ARMOR_SLOT,this.method_217,this.method_199,this.method_74);
         this.var_500[EntType.GLOVES_SLOT] = method_3(_loc13_.am_Gloves,EntType.GLOVES_SLOT,this.method_217,this.method_199,this.method_74);
         this.var_500[EntType.BOOTS_SLOT] = method_3(_loc13_.am_Boots,EntType.BOOTS_SLOT,this.method_217,this.method_199,this.method_74);
         method_208();
         method_23(var_2.am_CloseInventory);
         this.var_1764 = method_5(var_2.am_FilterInventory,this.method_1038);
         this.var_591 = method_1(var_2.am_PetPanel);
         this.var_591.Hide();
         this.var_281 = new Vector.<class_33>();
         this.var_1291 = new Vector.<class_33>();
         this.var_1359 = new Vector.<class_33>();
         this.var_1614 = new Vector.<class_33>(const_397,true);
         var _loc15_:uint = 0;
         while(_loc15_ < const_397)
         {
            this.var_281[_loc15_] = method_3(this.var_591.mMovieClip["am_Pet" + _loc15_],_loc15_,this.method_1290,this.method_1724,this.method_1578);
            this.var_1291[_loc15_] = method_1(this.var_281[_loc15_].mMovieClip.am_Icon);
            this.var_1359[_loc15_] = method_1(this.var_1291[_loc15_].mMovieClip.am_Selector);
            this.var_1614[_loc15_] = method_1(this.var_281[_loc15_].mMovieClip.am_Notice);
            _loc15_++;
         }
         this.var_1012 = method_17(this.var_281[0].mMovieClip.am_Progress,"Progress",1);
         this.var_1493 = method_1(this.var_281[0].mMovieClip.am_MaxRank);
         this.var_1347 = method_10(var_2.am_PetPanel.am_FeedPet,this.method_1362);
         var _loc16_:MovieClip = var_2.am_SocketPanel;
         this.var_98 = method_1(_loc16_);
         this.var_98.Hide();
         var _loc17_:MovieClip = var_2.am_ArrowGroup2;
         this.var_762 = new Vector.<class_33>(const_134,true);
         _loc2_ = 0;
         while(_loc2_ < const_134)
         {
            this.var_762[_loc2_] = method_1(_loc17_["am_Pointer" + _loc2_] as MovieClip);
            _loc2_++;
         }
         this.var_405 = new Vector.<class_33>(EntType.MAX_SLOTS,true);
         this.var_405[EntType.SWORD_SLOT] = method_1(this.var_98.mMovieClip.am_Sword);
         this.var_405[EntType.SHIELD_SLOT] = method_1(this.var_98.mMovieClip.am_Shield);
         this.var_405[EntType.HAT_SLOT] = method_1(this.var_98.mMovieClip.am_Hat);
         this.var_405[EntType.ARMOR_SLOT] = method_1(this.var_98.mMovieClip.am_Armor);
         this.var_405[EntType.GLOVES_SLOT] = method_1(this.var_98.mMovieClip.am_Gloves);
         this.var_405[EntType.BOOTS_SLOT] = method_1(this.var_98.mMovieClip.am_Boots);
         this.var_2000 = new Vector.<class_33>(const_27);
         this.var_1675 = new Vector.<class_33>(const_27);
         this.var_1684 = new Vector.<class_33>(const_27);
         this.var_1806 = new Vector.<class_33>(const_27);
         this.var_1941 = new Vector.<class_33>(const_27);
         this.var_1754 = new Vector.<class_33>(const_27);
         var _loc18_:uint = 0;
         while(_loc18_ < 3)
         {
            this.var_2000[_loc18_] = method_3(this.var_98.mMovieClip.am_Sword["am_Charm" + _loc18_],_loc18_ + 0 * const_27,this.method_221,this.method_230,this.method_183);
            this.var_1675[_loc18_] = method_3(this.var_98.mMovieClip.am_Shield["am_Charm" + _loc18_],_loc18_ + 1 * const_27,this.method_221,this.method_230,this.method_183);
            this.var_1806[_loc18_] = method_3(this.var_98.mMovieClip.am_Hat["am_Charm" + _loc18_],_loc18_ + 2 * const_27,this.method_221,this.method_230,this.method_183);
            this.var_1684[_loc18_] = method_3(this.var_98.mMovieClip.am_Armor["am_Charm" + _loc18_],_loc18_ + 3 * const_27,this.method_221,this.method_230,this.method_183);
            this.var_1941[_loc18_] = method_3(this.var_98.mMovieClip.am_Gloves["am_Charm" + _loc18_],_loc18_ + 4 * const_27,this.method_221,this.method_230,this.method_183);
            this.var_1754[_loc18_] = method_3(this.var_98.mMovieClip.am_Boots["am_Charm" + _loc18_],_loc18_ + 5 * const_27,this.method_221,this.method_230,this.method_183);
            _loc18_++;
         }
         this.var_215 = method_1(var_2.am_FilterPanel);
         this.var_215.Hide();
         var _loc19_:MovieClip = this.var_215.mMovieClip;
         this.var_369 = new Vector.<class_33>(EntType.MAX_SLOTS);
         this.var_369[EntType.SWORD_SLOT] = method_3(_loc19_.am_SlotList["am_Selection" + 0],EntType.SWORD_SLOT,this.method_203,this.method_196,this.method_39);
         this.var_369[EntType.SHIELD_SLOT] = method_3(_loc19_.am_SlotList["am_Selection" + 1],EntType.SHIELD_SLOT,this.method_203,this.method_196,this.method_39);
         this.var_369[EntType.HAT_SLOT] = method_3(_loc19_.am_SlotList["am_Selection" + 2],EntType.HAT_SLOT,this.method_203,this.method_196,this.method_39);
         this.var_369[EntType.ARMOR_SLOT] = method_3(_loc19_.am_SlotList["am_Selection" + 3],EntType.ARMOR_SLOT,this.method_203,this.method_196,this.method_39);
         this.var_369[EntType.GLOVES_SLOT] = method_3(_loc19_.am_SlotList["am_Selection" + 4],EntType.GLOVES_SLOT,this.method_203,this.method_196,this.method_39);
         this.var_369[EntType.BOOTS_SLOT] = method_3(_loc19_.am_SlotList["am_Selection" + 5],EntType.BOOTS_SLOT,this.method_203,this.method_196,this.method_39);
         this.var_648 = new Vector.<class_33>(const_504);
         this.var_648[const_179] = method_3(_loc19_.am_RarityList["am_Selection" + const_179],const_179,this.method_519,this.method_473,this.method_39);
         this.var_648[const_180] = method_3(_loc19_.am_RarityList["am_Selection" + const_180],const_180,this.method_519,this.method_473,this.method_39);
         this.var_648[const_196] = method_3(_loc19_.am_RarityList["am_Selection" + const_196],const_196,this.method_519,this.method_473,this.method_39);
         this.var_542 = new Vector.<class_33>(const_514);
         this.var_542[const_434] = method_3(_loc19_.am_StatList["am_Selection" + const_434],const_434,this.method_347,this.method_281,this.method_39);
         this.var_542[const_462] = method_3(_loc19_.am_StatList["am_Selection" + const_462],const_462,this.method_347,this.method_281,this.method_39);
         this.var_542[const_575] = method_3(_loc19_.am_StatList["am_Selection" + const_575],const_575,this.method_347,this.method_281,this.method_39);
         this.var_542[const_493] = method_3(_loc19_.am_StatList["am_Selection" + const_493],const_493,this.method_347,this.method_281,this.method_39);
         this.var_260 = new Vector.<class_33>(const_513);
         this.var_260[const_412] = method_3(_loc19_.am_CharmList["am_Selection" + const_412],const_412,this.method_133,this.method_137,this.method_39);
         this.var_260[const_488] = method_3(_loc19_.am_CharmList["am_Selection" + const_488],const_488,this.method_133,this.method_137,this.method_39);
         this.var_260[const_510] = method_3(_loc19_.am_CharmList["am_Selection" + const_510],const_510,this.method_133,this.method_137,this.method_39);
         this.var_260[const_566] = method_3(_loc19_.am_CharmList["am_Selection" + const_566],const_566,this.method_133,this.method_137,this.method_39);
         this.var_260[const_418] = method_3(_loc19_.am_CharmList["am_Selection" + const_418],const_418,this.method_133,this.method_137,this.method_39);
         this.var_260[const_450] = method_3(_loc19_.am_CharmList["am_Selection" + const_450],const_450,this.method_133,this.method_137,this.method_39);
         this.var_260[const_460] = method_3(_loc19_.am_CharmList["am_Selection" + const_460],const_460,this.method_133,this.method_137,this.method_39);
         this.var_260[const_489] = method_3(_loc19_.am_CharmList["am_Selection" + const_489],const_489,this.method_133,this.method_137,this.method_39);
         this.var_260[const_519] = method_3(_loc19_.am_CharmList["am_Selection" + const_519],const_519,this.method_133,this.method_137,this.method_39);
         this.var_583 = new Vector.<class_33>(const_497);
         this.var_583[const_486] = method_3(_loc19_.am_BonusList["am_Selection" + const_486],const_486,this.method_376,this.method_308,this.method_39);
         this.var_583[const_541] = method_3(_loc19_.am_BonusList["am_Selection" + const_541],const_541,this.method_376,this.method_308,this.method_39);
         this.var_583[const_453] = method_3(_loc19_.am_BonusList["am_Selection" + const_453],const_453,this.method_376,this.method_308,this.method_39);
         this.var_583[const_444] = method_3(_loc19_.am_BonusList["am_Selection" + const_444],const_444,this.method_376,this.method_308,this.method_39);
         this.var_622 = new Vector.<class_33>(const_815);
         this.var_622[0] = method_3(_loc19_.am_AbilityList["am_Selection" + 0],0,this.method_462,this.method_437,this.method_39);
         this.var_622[1] = method_3(_loc19_.am_AbilityList["am_Selection" + 1],1,this.method_462,this.method_437,this.method_39);
         this.var_622[2] = method_3(_loc19_.am_AbilityList["am_Selection" + 2],2,this.method_462,this.method_437,this.method_39);
         this.var_297 = new Vector.<class_33>(const_155);
         var _loc20_:uint = 0;
         while(_loc20_ < const_155)
         {
            this.var_297[_loc20_] = method_3(_loc19_.am_RuneList["am_Selection" + _loc20_],_loc20_,this.method_1019,this.method_1735,this.method_39);
            _loc20_++;
         }
         this.var_73 = new class_150(var_1);
         this.var_2851 = method_21(_loc19_.am_RuneText1);
         this.var_1054 = method_1(_loc19_.am_AbilityIconGroup);
         this.var_1885 = method_1(_loc19_.am_AbilityList);
         this.mFilterPanelAbilityIconHolder0 = method_1(this.var_1054.mMovieClip.am_Icon0.am_ButtonHolder.am_Button);
         this.mFilterPanelAbilityIconHolder1 = method_1(this.var_1054.mMovieClip.am_Icon1.am_ButtonHolder.am_Button);
         this.mFilterPanelAbilityIconHolder2 = method_1(this.var_1054.mMovieClip.am_Icon2.am_ButtonHolder.am_Button);
         this.var_2491 = method_21(_loc19_.am_RuneText2);
         this.var_1768 = method_1(_loc19_.am_RuneIconGroup);
         this.var_1917 = method_1(_loc19_.am_RuneList);
         this.var_721 = new Vector.<class_33>(const_155);
         _loc20_ = 0;
         while(_loc20_ < const_155)
         {
            this.var_721[_loc20_] = method_1(_loc19_.am_RuneIconGroup["am_Rune" + _loc20_]);
            _loc20_++;
         }
         this.var_754 = method_27(this.var_215.mMovieClip.am_DynamicTooltip);
         this.var_2738 = method_21(this.var_754.mMovieClip.am_Text);
         this.var_2697 = method_21(_loc19_.am_Description);
         this.var_2298 = this.var_721[0].mMovieClip.am_RuneHolder.filters;
         this.method_1111();
         this.var_281[0].mMovieClip.am_TrainingText.text = "";
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_98 = null;
         this.var_215 = null;
         this.var_762 = null;
         var _loc1_:int = 0;
         while(_loc1_ < this.var_369.length)
         {
            this.var_369[_loc1_] = null;
            _loc1_++;
         }
         this.var_369 = null;
         _loc1_ = 0;
         while(_loc1_ < this.var_648.length)
         {
            this.var_648[_loc1_] = null;
            _loc1_++;
         }
         this.var_648 = null;
         _loc1_ = 0;
         while(_loc1_ < this.var_542.length)
         {
            this.var_542[_loc1_] = null;
            _loc1_++;
         }
         this.var_542 = null;
         _loc1_ = 0;
         while(_loc1_ < this.var_260.length)
         {
            this.var_260[_loc1_] = null;
            _loc1_++;
         }
         this.var_260 = null;
         _loc1_ = 0;
         while(_loc1_ < this.var_583.length)
         {
            this.var_583[_loc1_] = null;
            _loc1_++;
         }
         this.var_583 = null;
         _loc1_ = 0;
         while(_loc1_ < this.var_622.length)
         {
            this.var_622[_loc1_] = null;
            _loc1_++;
         }
         this.var_622 = null;
         _loc1_ = 0;
         while(_loc1_ < this.var_297.length)
         {
            this.var_297[_loc1_] = null;
            _loc1_++;
         }
         this.var_297 = null;
         _loc1_ = 0;
         while(_loc1_ < const_27)
         {
            this.var_2000[_loc1_] = null;
            this.var_1675[_loc1_] = null;
            this.var_1684[_loc1_] = null;
            this.var_1806[_loc1_] = null;
            this.var_1941[_loc1_] = null;
            this.var_1754[_loc1_] = null;
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_405.length)
         {
            this.var_405[_loc1_] = null;
            _loc1_++;
         }
         this.var_405 = null;
         this.var_2000 = null;
         this.var_1675 = null;
         this.var_1684 = null;
         this.var_1806 = null;
         this.var_1941 = null;
         this.var_1754 = null;
         this.var_297 = null;
         this.var_73.method_1233();
         this.var_73 = null;
         this.var_2851 = null;
         this.var_1054 = null;
         this.var_1885 = null;
         this.mFilterPanelAbilityIconHolder0 = null;
         this.mFilterPanelAbilityIconHolder1 = null;
         this.mFilterPanelAbilityIconHolder2 = null;
         this.var_2491 = null;
         this.var_1768 = null;
         this.var_1917 = null;
         var _loc2_:uint = 0;
         while(_loc2_ < const_155)
         {
            this.var_721[_loc2_] = null;
            _loc2_++;
         }
         this.var_721 = null;
         this.var_754 = null;
         this.var_2738 = null;
         this.var_2697 = null;
         this.var_1892 = null;
         this.var_1824 = null;
         this.var_455 = null;
         this.var_413 = null;
         this.var_311 = null;
         _loc1_ = _loc1_;
         while(_loc1_ < this.var_225.length)
         {
            this.var_225[_loc1_] = null;
            _loc1_++;
         }
         this.var_225 = null;
         this.var_695 = null;
         this.var_148 = null;
         this.var_587 = null;
         this.var_472 = null;
         this.var_500 = null;
         this.var_1764 = null;
         this.var_95 = null;
         this.var_902 = null;
         this.var_2298 = null;
         this.var_591 = null;
         this.var_1614 = null;
         this.var_1291 = null;
         this.var_1359 = null;
         this.var_1012 = null;
         this.var_1493 = null;
         this.var_1347 = null;
         _loc1_ = 0;
         while(_loc1_ < this.var_281.length)
         {
            method_14(this.var_281[_loc1_].mMovieClip.am_Icon.am_ItemIconHolder);
            _loc1_++;
         }
         this.var_281 = null;
         this.var_1991 = null;
         this.var_1965 = null;
         this.method_1993();
      }
      
      public function OnInitDisplay() : void
      {
         var_1.screenHudTop.ResetNewInventoryCount();
         this.method_1020();
         this.var_754.Hide();
         MathUtil.method_2(this.var_215.mMovieClip.am_Description,"");
         this.var_529 = false;
         this.var_73.method_119();
         this.method_624();
         this.method_937();
         this.method_608();
         this.method_385();
         this.var_466.Hide();
         var_1.screenHudTooltip.HideTooltip(true);
         this.var_1373.Hide(true);
         this.method_1349();
         this.method_176(this.var_56 != const_68);
         this.method_140();
      }
      
      private function method_1686(param1:Entity) : void
      {
         var _loc5_:uint = 0;
         var _loc6_:class_42 = null;
         var _loc7_:GearType = null;
         var _loc4_:uint = 1;
         while(_loc4_ < EntType.MAX_SLOTS)
         {
            _loc7_ = !!(_loc6_ = !!(_loc5_ = param1.mEquipGear[_loc4_]) ? var_1.GetBestOwnedGearByID(_loc5_) : null) ? _loc6_.gearType : null;
            var_1.screenHudTooltip.SkinEquipmentIcon(_loc7_,this.var_500[_loc4_]);
            _loc4_++;
         }
      }
      
      public function LinkGearInChat(param1:uint, param2:class_42 = null) : void
      {
         var _loc4_:class_42 = null;
         var _loc6_:Array = null;
         var _loc7_:int = 0;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         if(param2)
         {
            _loc4_ = param2;
         }
         if(!_loc4_)
         {
            _loc6_ = var_1.mFilteredOwnedGear;
            if((_loc7_ = this.method_260(_loc6_,param1)) >= _loc6_.length || _loc7_ < 0)
            {
               this.var_95[param1].PlayAnimation("Ready");
               return;
            }
            _loc4_ = _loc6_[_loc7_];
         }
         var _loc5_:* = (_loc5_ = (_loc5_ = "{" + class_127.const_8[0] + ":") + _loc4_.method_1528()) + "}";
         var_1.screenChat.AddItemInfoToChatEntry("[" + _loc4_.gearType.displayName + "]",_loc5_);
      }
      
      public function LinkCharmInChat(param1:uint, param2:class_64 = null) : void
      {
         var _loc4_:class_64 = null;
         var _loc6_:Vector.<class_114> = null;
         var _loc7_:uint = 0;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         if(param2)
         {
            _loc4_ = param2;
         }
         if(!_loc4_)
         {
            _loc6_ = this.method_214(_loc3_);
            if((_loc7_ = param1 + const_12 * var_16) >= _loc6_.length)
            {
               this.var_95[param1].PlayAnimation("Ready");
               return;
            }
            _loc4_ = _loc6_[_loc7_].charmData;
         }
         var _loc5_:* = (_loc5_ = (_loc5_ = "{" + class_127.const_8[1] + ":") + _loc4_.method_75().toString()) + "}";
         var_1.screenChat.AddItemInfoToChatEntry("[" + _loc4_.method_49() + "]",_loc5_);
      }
      
      public function LinkMaterialInChat(param1:uint, param2:class_8 = null) : void
      {
         var _loc6_:Vector.<class_76> = null;
         var _loc7_:uint = 0;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_8;
         if(!(_loc4_ = param2))
         {
            _loc6_ = this.method_480(_loc3_);
            if((_loc7_ = param1 + var_16 * const_12) >= _loc6_.length)
            {
               this.var_95[param1].PlayAnimation("Ready");
               return;
            }
            _loc4_ = _loc6_[_loc7_].materialType;
         }
         var _loc5_:* = (_loc5_ = (_loc5_ = "{" + class_127.const_8[2] + ":") + _loc4_.var_140.toString()) + "}";
         var_1.screenChat.AddItemInfoToChatEntry("[" + _loc4_.displayName + "]",_loc5_);
      }
      
      public function method_1287(param1:uint, param2:class_3 = null) : void
      {
         var _loc6_:Vector.<class_103> = null;
         var _loc7_:uint = 0;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_3;
         if(!(_loc4_ = param2))
         {
            _loc6_ = this.var_654;
            if((_loc7_ = param1 + var_16 * const_12) >= _loc6_.length)
            {
               this.var_95[param1].PlayAnimation("Ready");
               return;
            }
            _loc4_ = _loc6_[_loc7_].consumableType;
         }
         var _loc5_:* = (_loc5_ = (_loc5_ = "{" + class_127.const_8[9] + ":") + String(_loc4_.consumableID)) + "}";
         var_1.screenChat.AddItemInfoToChatEntry("[" + _loc4_.displayName + "]",_loc5_);
      }
      
      public function method_2081(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(param1.ctrlKey && Boolean(_loc3_.mEquipPet))
         {
            this.LinkPetInChat(0,_loc3_.mEquipPet);
         }
      }
      
      public function LinkPetInChat(param1:uint, param2:class_87 = null) : void
      {
         var _loc4_:class_87 = null;
         var _loc6_:Vector.<class_87> = null;
         var _loc7_:uint = 0;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         if(param2)
         {
            _loc4_ = param2;
         }
         if(!_loc4_)
         {
            _loc6_ = var_1.mEggPetInfo.mOwnedPets;
            if((_loc7_ = param1 + var_16 * const_12) >= _loc6_.length)
            {
               this.var_95[param1].PlayAnimation("Ready");
               return;
            }
            _loc4_ = _loc6_[_loc7_];
         }
         var _loc5_:* = (_loc5_ = (_loc5_ = (_loc5_ = (_loc5_ = "{" + class_127.const_8[3]) + (":" + _loc4_.mPetType.var_104.toString())) + (":" + _loc4_.var_23.toString())) + (":" + _loc4_.var_110.toString())) + "}";
         var_1.screenChat.AddItemInfoToChatEntry("[" + _loc4_.mPetType.displayName + "]",_loc5_);
      }
      
      private function method_2065(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(param1.ctrlKey && Boolean(_loc3_.mEquipMount))
         {
            this.LinkMountInChat(0,_loc3_.mEquipMount);
         }
      }
      
      public function LinkMountInChat(param1:uint, param2:class_20 = null) : void
      {
         var _loc6_:Vector.<class_20> = null;
         var _loc7_:uint = 0;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_20;
         if(!(_loc4_ = param2))
         {
            _loc6_ = this.method_296(_loc3_);
            if((_loc7_ = var_16 * const_10 + param1) >= _loc6_.length)
            {
               return;
            }
            _loc4_ = _loc6_[_loc7_];
         }
         var _loc5_:* = (_loc5_ = (_loc5_ = "{" + class_127.const_8[4]) + (":" + _loc4_.var_197.toString())) + "}";
         var_1.screenChat.AddItemInfoToChatEntry("[" + _loc4_.displayName + "]",_loc5_);
      }
      
      private function method_260(param1:Array, param2:uint) : int
      {
         var _loc3_:uint = uint(var_1.mLockboxData.mUniqueLockboxes);
         if(var_16 == 0 && param2 > const_10 - _loc3_ - 1)
         {
            return -1;
         }
         var _loc4_:uint = 0;
         if(var_16 > 0 || param2 > const_10 - _loc3_ - 1)
         {
            _loc4_ = _loc3_;
         }
         return int(param1.length - var_16 * const_10 - 1 - param2 + _loc4_);
      }
      
      private function method_58(param1:uint) : void
      {
         var _loc8_:uint = 0;
         var _loc9_:class_151 = null;
         var _loc10_:class_15 = null;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_ || !var_1.CanSendPacket())
         {
            return;
         }
         var _loc3_:Array = var_1.mFilteredOwnedGear;
         if(this.method_490(param1))
         {
            _loc8_ = param1 - (const_10 - var_1.mLockboxData.mUniqueLockboxes);
            if(_loc9_ = var_1.mLockboxData.mLockboxList[_loc8_])
            {
               _loc10_ = _loc9_.var_286;
               var_1.mLockboxData.mLockboxID = _loc10_.lockboxID;
               var_1.screenLockBox.Display();
            }
            return;
         }
         var _loc4_:int;
         if((_loc4_ = this.method_260(_loc3_,param1)) < 0)
         {
            return;
         }
         if(_loc4_ >= _loc3_.length)
         {
            this.var_95[param1].PlayAnimation("Ready");
            return;
         }
         var _loc5_:GearType;
         var _loc6_:uint = (_loc5_ = _loc3_[_loc4_].gearType).gearID;
         var _loc7_:uint = uint(EntType.method_87(_loc5_.type));
         if(_loc6_ == _loc2_.mEquipGear[_loc7_])
         {
            _loc6_ = 0;
            var_1.screenHudTooltip.HideTooltip();
         }
         var_1.linkUpdater.WriteUpdateSingleGear(_loc2_,_loc7_,_loc6_);
         _loc2_.method_303(_loc7_,_loc6_);
         var_1.screenHudTooltip.mGearEquippedTooltip.Hide(true);
         this.var_1915 = param1;
         if(SoundConfig.var_199)
         {
            SoundManager.Play(SoundConfig.var_199);
         }
         Refresh();
      }
      
      private function method_217(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_ || !var_1.CanSendPacket())
         {
            return;
         }
         var _loc4_:uint = _loc3_.mEquipGear[param2];
         var _loc6_:class_42;
         var _loc5_:Array;
         if(!(_loc6_ = (_loc5_ = var_1.mOwnedGear)[_loc4_]))
         {
            return;
         }
         if(param1.ctrlKey)
         {
            this.LinkGearInChat(0,_loc6_);
            return;
         }
         var _loc7_:GearType = _loc6_.gearType;
         var _loc8_:uint = uint(EntType.method_87(_loc7_.type));
         var_1.linkUpdater.WriteUpdateSingleGear(_loc3_,_loc8_,0);
         _loc3_.method_303(_loc8_,0);
         if(SoundConfig.var_199)
         {
            SoundManager.Play(SoundConfig.var_199);
         }
         var_1.screenHudTooltip.HideTooltip();
         Refresh();
      }
      
      private function method_1058(param1:uint) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:Vector.<class_87> = var_1.mEggPetInfo.mOwnedPets;
         var _loc4_:uint;
         if((_loc4_ = var_16 * const_10 + param1) >= _loc3_.length)
         {
            return;
         }
         var _loc5_:class_87;
         if(!(_loc5_ = _loc3_[_loc4_]))
         {
            return;
         }
         if(this.var_200 <= -1)
         {
            return;
         }
         this.method_1665(_loc5_,param1);
         this.method_140();
      }
      
      private function method_1318(param1:uint) : void
      {
         var _loc6_:Packet = null;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_ || !var_1.CanSendPacket())
         {
            return;
         }
         var _loc3_:uint = var_16 * const_10 + param1;
         var _loc4_:Vector.<class_20> = this.method_296(_loc2_);
         if(_loc3_ >= _loc4_.length)
         {
            return;
         }
         var _loc5_:class_20;
         if(!(_loc5_ = _loc4_[_loc3_]))
         {
            return;
         }
         if(var_1.mOwnedMounts[_loc5_.var_197])
         {
            _loc2_.method_525(_loc5_);
            (_loc6_ = new Packet(LinkUpdater.const_709)).method_9(var_1.clientEntID);
            _loc6_.method_20(class_20.const_297,_loc5_.var_197);
            var_1.serverConn.SendPacket(_loc6_);
         }
         if(SoundConfig.var_199)
         {
            SoundManager.Play(SoundConfig.var_199);
         }
         Refresh();
      }
      
      private function method_1291(param1:uint) : void
      {
         var _loc6_:uint = 0;
         var _loc7_:* = false;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_ || !var_1.CanSendPacket())
         {
            return;
         }
         var _loc3_:uint = var_16 * const_10 + param1;
         if(_loc3_ >= this.var_654.length)
         {
            return;
         }
         var _loc4_:class_103;
         if(!(_loc4_ = this.var_654[_loc3_]) || !_loc4_.stackCount)
         {
            return;
         }
         var _loc5_:class_3;
         if((_loc5_ = _loc4_.consumableType).var_427)
         {
            _loc6_ = 0;
            if(_loc2_.mNextPotion == _loc5_)
            {
               _loc5_ = null;
            }
            else
            {
               _loc6_ = _loc5_.consumableID;
            }
            _loc7_ = var_1.clientEnt.mCurrPotion != null;
            var_1.QueuePotion(_loc5_,false);
            if(_loc5_ && _loc5_ != this.var_1965 && !_loc7_)
            {
               this.var_1965 = _loc5_;
               this.method_1243(_loc5_,param1);
            }
            if(SoundConfig.var_199)
            {
               SoundManager.Play(SoundConfig.var_199);
            }
            Refresh();
         }
         else if(_loc5_.type == "PetFood" && Boolean(var_1.mEggPetInfo.mActivePet))
         {
            this.method_179(null,const_68);
            var_1.screenFeedPet.Display(var_1.mEggPetInfo.mActivePet);
         }
         this.method_753(var_1.clientEnt,param1);
      }
      
      private function method_1420(param1:MouseEvent, param2:uint) : void
      {
         if(this.var_56 == const_120)
         {
            if(param1.ctrlKey)
            {
               this.LinkGearInChat(param2);
            }
            else
            {
               this.method_58(param2);
            }
         }
         else if(this.var_56 == const_86)
         {
            if(param1.ctrlKey)
            {
               this.LinkCharmInChat(param2);
            }
            else
            {
               this.method_1698(param2);
               this.method_166();
            }
         }
         else if(this.var_56 == const_231)
         {
            if(param1.ctrlKey)
            {
               this.LinkMaterialInChat(param2);
            }
         }
         else if(this.var_56 == const_68)
         {
            if(param1.ctrlKey)
            {
               this.LinkPetInChat(param2);
            }
            else
            {
               this.method_1058(param2);
            }
         }
         else if(this.var_56 == const_242)
         {
            if(param1.ctrlKey)
            {
               this.LinkMountInChat(param2);
            }
            else
            {
               this.method_1318(param2);
            }
         }
         else if(this.var_56 == const_278)
         {
            if(param1.ctrlKey)
            {
               this.method_1287(param2);
            }
            else
            {
               this.method_1291(param2);
            }
         }
      }
      
      private function method_1298(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         if(this.var_56 == const_120)
         {
            this.method_815(_loc3_,param2);
         }
         else if(this.var_56 == const_86)
         {
            this.method_1042(_loc3_,param2);
         }
         else if(this.var_56 == const_231)
         {
            this.method_1270(_loc3_,param2);
         }
         else if(this.var_56 == const_68)
         {
            this.method_1781(_loc3_,param2);
         }
         else if(this.var_56 == const_242)
         {
            this.method_1090(_loc3_,param2);
         }
         else if(this.var_56 == const_278)
         {
            this.method_753(_loc3_,param2);
         }
      }
      
      public function method_815(param1:Entity, param2:uint) : void
      {
         var _loc6_:class_42 = null;
         var _loc3_:Array = var_1.mFilteredOwnedGear;
         if(this.method_490(param2))
         {
            var_1.screenHudTooltip.ShowLockboxTooltip(276,386);
            return;
         }
         var _loc4_:int;
         if((_loc4_ = this.method_260(_loc3_,param2)) < 0)
         {
            return;
         }
         if(_loc4_ >= _loc3_.length)
         {
            this.var_95[param2].PlayAnimation("Ready");
            return;
         }
         var _loc5_:uint = uint(_loc3_[_loc4_].gearType.gearID);
         var_1.screenHudTooltip.ShowGearTooltip(param1,_loc5_,false,null,370.5,387);
         var_1.screenHudTooltip.ShowGearTooltip(param1,_loc5_,true,null,46.5,387);
         if(Boolean(_loc5_) && this.method_250())
         {
            _loc6_ = _loc3_[_loc4_];
            this.method_170(param1,_loc6_);
         }
      }
      
      private function method_1042(param1:Entity, param2:uint) : void
      {
         var _loc3_:Vector.<class_114> = this.method_214(param1);
         var _loc4_:uint;
         if((_loc4_ = param2 + const_12 * var_16) >= _loc3_.length)
         {
            this.var_95[param2].PlayAnimation("Ready");
            return;
         }
         var _loc5_:class_114 = _loc3_[_loc4_];
         var_1.screenHudTooltip.ShowCharmTooltip(_loc5_.charmData,369.25,364.05);
      }
      
      private function method_1270(param1:Entity, param2:uint) : void
      {
         var _loc3_:Vector.<class_76> = this.method_480(param1);
         var _loc4_:uint;
         if((_loc4_ = param2 + var_16 * const_12) >= _loc3_.length)
         {
            this.var_95[param2].PlayAnimation("Ready");
            return;
         }
         var _loc5_:class_76 = _loc3_[_loc4_];
         this.method_1149(_loc5_.materialType);
         this.var_1373.Show();
      }
      
      private function method_1781(param1:Entity, param2:uint) : void
      {
         var _loc3_:Vector.<class_87> = var_1.mEggPetInfo.mOwnedPets;
         var _loc4_:uint;
         if((_loc4_ = param2 + var_16 * const_12) >= _loc3_.length)
         {
            this.var_95[param2].PlayAnimation("Ready");
            return;
         }
         var _loc5_:class_87 = _loc3_[_loc4_];
         var_1.screenHudTooltip.ShowPetTooltip(_loc5_,false,253.75,381.2);
      }
      
      private function method_753(param1:Entity, param2:uint) : void
      {
         var _loc3_:uint = param2 + var_16 * const_12;
         if(_loc3_ >= this.var_654.length)
         {
            this.var_95[param2].PlayAnimation("Ready");
            return;
         }
         var _loc4_:class_103;
         if(_loc4_ = this.var_654[_loc3_])
         {
            var_1.screenHudTooltip.ShowConsumableTooltip(_loc4_.consumableType,265.25,386.95);
         }
         else
         {
            this.var_95[param2].PlayAnimation("Ready");
         }
      }
      
      private function method_1090(param1:Entity, param2:uint) : void
      {
         var _loc3_:Vector.<class_20> = this.method_296(param1);
         var _loc4_:uint;
         if((_loc4_ = param2 + var_16 * const_12) >= _loc3_.length)
         {
            this.var_95[param2].PlayAnimation("Ready");
            return;
         }
         var _loc5_:class_20;
         if(_loc5_ = _loc3_[_loc4_])
         {
            var_1.screenHudTooltip.ShowMountTooltip(_loc5_,265.25,386.95);
         }
      }
      
      private function method_1149(param1:class_8) : void
      {
         var _loc2_:MovieClip = this.var_1373.mMovieClip;
         if(param1.var_139 == "M")
         {
            MathUtil.method_8(_loc2_.am_Name,param1.displayName,const_24);
         }
         else if(param1.var_139 == "R")
         {
            MathUtil.method_8(_loc2_.am_Name,param1.displayName,const_22);
         }
         else if(param1.var_139 == "L")
         {
            MathUtil.method_8(_loc2_.am_Name,param1.displayName,const_23);
         }
         MathUtil.method_2(_loc2_.am_Type,"Material");
      }
      
      private function method_74(param1:MouseEvent, param2:uint) : void
      {
         var_1.screenHudTooltip.HideTooltip(true);
         this.var_1373.Hide();
         var _loc3_:Entity = var_1.clientEnt;
         if(Boolean(_loc3_) && this.method_250())
         {
            this.method_170(var_1.clientEnt);
         }
      }
      
      private function method_1578(param1:MouseEvent, param2:uint) : void
      {
         if(param2 == 0)
         {
            this.var_281[param2].mMovieClip.am_XPText.visible = false;
         }
         this.method_74(param1,param2);
      }
      
      override public function RefreshPaperDoll() : void
      {
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:String = this.GetPaperDollType();
         if(!_loc2_)
         {
            return;
         }
         EntType.method_57(_loc2_,"MeUI");
         if(!mPaperDoll)
         {
            mPaperDoll = new Entity(var_1,"MeUI:PaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,_loc1_.mExpLevel,0,null,_loc1_.var_85.method_272(),_loc1_.mMasterClass,_loc1_.var_329,_loc1_.mEquipPet,_loc1_.mCurrPotion);
         }
         else
         {
            mPaperDoll.ResetEntType(EntType.method_48("PaperDoll","MeUI"));
         }
         var_2.am_PaperDollHolder.addChild(mPaperDoll.gfx.m_TheDO);
         if(this.method_250() && this.var_1915 > -1)
         {
            this.method_815(_loc1_,this.var_1915);
            this.var_1915 = -1;
         }
         if(this.method_250())
         {
            this.method_170(_loc1_);
         }
      }
      
      private function method_1038(param1:MouseEvent) : void
      {
         if(this.var_56 != const_120)
         {
            return;
         }
         if(this.var_215.mbVisible)
         {
            this.method_211();
         }
         else
         {
            this.var_215.Show();
         }
         Refresh();
      }
      
      private function method_199(param1:MouseEvent, param2:uint) : void
      {
         var _loc4_:uint = 0;
         var _loc5_:class_20 = null;
         var _loc6_:class_87 = null;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         if(param2 < EntType.const_283)
         {
            if((_loc4_ = _loc3_.mEquipGear[param2]) != 0)
            {
               var_1.screenHudTooltip.ShowGearTooltip(_loc3_,_loc4_,false,null,370.5,387);
               var_1.screenHudTooltip.ShowGearTooltip(_loc3_,_loc4_,true,null,46.5,387);
            }
         }
         else if(param2 == EntType.const_330)
         {
            _loc5_ = _loc3_.mEquipMount;
            if(_loc3_.mEquipMount)
            {
               var_1.screenHudTooltip.ShowMountTooltip(_loc5_,265.25,386.95);
            }
         }
         else if(param2 == EntType.const_283)
         {
            if(_loc6_ = _loc3_.mEquipPet)
            {
               var_1.screenHudTooltip.ShowPetTooltip(_loc6_,false,253.75,381.2);
            }
         }
      }
      
      private function method_179(param1:MouseEvent, param2:uint) : void
      {
         if(this.var_56 != param2)
         {
            var_16 = 0;
            this.var_56 = param2;
            Refresh();
            if(param2 == const_68)
            {
               this.var_200 = 0;
               this.method_140();
            }
            else if(param2 == const_86)
            {
               this.var_200 = -1;
               this.method_166();
            }
         }
      }
      
      private function method_404() : void
      {
         var _loc1_:uint = 0;
         while(_loc1_ < const_799)
         {
            this.var_587[_loc1_].mMovieClip.am_Selector.visible = false;
            _loc1_++;
         }
         this.var_587[this.var_56].mMovieClip.am_Selector.visible = true;
         MathUtil.method_2(var_2.am_InventoryMode,const_940[this.var_56]);
         _loc1_ = 0;
         while(_loc1_ < const_668)
         {
            this.var_695[_loc1_].mMovieClip.am_Selector.visible = false;
            _loc1_++;
         }
         if(this.var_227 != -1)
         {
            this.var_695[this.var_227].mMovieClip.am_Selector.visible = true;
         }
      }
      
      private function method_274(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         if(param2 == this.var_227)
         {
            this.method_879();
            if(this.var_466.mbVisible)
            {
               this.var_466.Hide();
            }
            return;
         }
         this.var_227 = param2;
         var _loc5_:MovieClip;
         var _loc4_:MovieClip;
         (_loc5_ = (_loc4_ = this.var_148.mMovieClip).am_Panel).am_ElementsGroup.visible = false;
         _loc5_.am_StatisticsGroup.visible = false;
         _loc5_.am_Prefabs.visible = false;
         _loc5_.am_CurrencyGroup.visible = false;
         if(this.var_466.mbVisible)
         {
            this.var_466.Hide();
         }
         if(this.var_227 == const_402)
         {
            _loc5_.am_StatisticsGroup.visible = true;
            this.method_170(_loc3_);
         }
         else if(this.var_227 == const_284)
         {
            _loc5_.am_ElementsGroup.visible = true;
            this.method_170(_loc3_);
         }
         else if(this.var_227 == const_484)
         {
            _loc5_.am_Prefabs.visible = true;
            this.method_552(_loc3_);
         }
         else if(this.var_227 == const_335)
         {
            this.method_1877();
            if(this.var_148.mbVisible)
            {
               this.var_148.Hide();
            }
         }
         else if(this.var_227 == const_427)
         {
            _loc5_.am_CurrencyGroup.visible = true;
            this.method_1182(_loc3_,_loc5_.am_CurrencyGroup);
         }
         if(!this.var_148.mbVisible && !this.var_466.mbVisible)
         {
            this.var_148.Show();
         }
         this.method_404();
      }
      
      private function method_1226(param1:MouseEvent) : void
      {
         this.method_879();
      }
      
      private function method_879() : void
      {
         this.var_227 = -1;
         if(this.var_148.mbVisible)
         {
            this.var_148.Hide();
         }
         this.method_404();
         this.var_529 = false;
      }
      
      private function method_817(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:MovieClip = this.var_902.mMovieClip;
         if(this.var_227 == const_402)
         {
            MathUtil.method_2(_loc3_.am_Name,STAT_PAGE1_NAMES[param2]);
            MathUtil.method_2(_loc3_.am_Desc,STAT_PAGE1_DESCRIPTIONS[param2]);
         }
         else if(this.var_227 == const_284)
         {
            MathUtil.method_2(_loc3_.am_Name,STAT_PAGE2_NAMES[param2]);
            MathUtil.method_2(_loc3_.am_Desc,STAT_PAGE2_DESCRIPTIONS[param2]);
         }
         this.var_902.Show();
      }
      
      private function method_970(param1:MouseEvent, param2:uint) : void
      {
         if(this.var_902.mbVisible)
         {
            this.var_902.Hide();
         }
      }
      
      private function method_1182(param1:Entity, param2:MovieClip) : void
      {
         MathUtil.method_2(param2.am_Gold,MathUtil.method_29(param1.currGold));
         MathUtil.method_2(param2.am_Dragoneore,MathUtil.method_29(param1.currGems));
         MathUtil.method_2(param2.am_SilverSigils,MathUtil.method_29(var_1.mLockboxData.mRoyalSigils));
         MathUtil.method_2(param2.am_DragonKeys,MathUtil.method_29(var_1.mLockboxData.mLockboxKeys));
         MathUtil.method_2(param2.am_MammothIdols,MathUtil.method_29(var_1.mMammothIdols));
         MathUtil.method_2(this.var_148.mMovieClip.am_Panel.am_SlideOutName,"Currencies");
      }
      
      private function method_170(param1:Entity, param2:class_42 = null) : void
      {
         var _loc55_:MovieClip = null;
         var _loc57_:Entity = null;
         var _loc58_:uint = 0;
         var _loc59_:uint = 0;
         var _loc60_:uint = 0;
         var _loc61_:uint = 0;
         var _loc62_:uint = 0;
         var _loc63_:uint = 0;
         var _loc64_:uint = 0;
         var _loc65_:Number = NaN;
         var _loc66_:Number = NaN;
         var _loc67_:Number = NaN;
         var _loc68_:Number = NaN;
         var _loc69_:Number = NaN;
         var _loc70_:Number = NaN;
         var _loc71_:Number = NaN;
         var _loc72_:Number = NaN;
         var _loc73_:Number = NaN;
         var _loc74_:Number = NaN;
         var _loc75_:Number = NaN;
         var _loc76_:Number = NaN;
         var _loc77_:Number = NaN;
         var _loc78_:Number = NaN;
         var _loc79_:Number = NaN;
         var _loc80_:Number = NaN;
         var _loc81_:Number = NaN;
         var _loc82_:Number = NaN;
         var _loc83_:Number = NaN;
         var _loc84_:Number = NaN;
         var _loc85_:Number = NaN;
         var _loc86_:Number = NaN;
         var _loc87_:uint = 0;
         var _loc88_:String = null;
         var _loc3_:uint = uint(param1.maxHP);
         var _loc4_:uint = uint(param1.meleeDamage);
         var _loc5_:uint = uint(param1.magicDamage);
         var _loc6_:uint = param1.armorClass;
         var _loc7_:Number = param1.var_1337;
         var _loc8_:Number = param1.var_667 + param1.var_640;
         var _loc9_:Number = param1.var_412;
         var _loc10_:Number = param1.var_571;
         var _loc11_:Number = param1.var_237;
         var _loc12_:Number = Math.round(1000 * (param1.totalMods.var_251 * const_806) / param1.entType.var_251) / 10;
         var _loc13_:Number = param1.totalMods.itemDrop;
         var _loc14_:Number = param1.totalMods.var_152;
         var _loc15_:Number = param1.totalMods.var_79;
         var _loc16_:Number = param1.totalMods.var_697;
         var _loc17_:Number = !!param1.var_65["AirSlay"] ? Number(param1.var_65["AirSlay"]) : 0;
         var _loc18_:Number = !!param1.var_65["DeathSlay"] ? Number(param1.var_65["DeathSlay"]) : 0;
         var _loc19_:Number = !!param1.var_65["EarthSlay"] ? Number(param1.var_65["EarthSlay"]) : 0;
         var _loc20_:Number = !!param1.var_65["FireSlay"] ? Number(param1.var_65["FireSlay"]) : 0;
         var _loc21_:Number = !!param1.var_65["IceSlay"] ? Number(param1.var_65["IceSlay"]) : 0;
         var _loc22_:Number = !!param1.var_65["LifeSlay"] ? Number(param1.var_65["LifeSlay"]) : 0;
         var _loc23_:Number = !!param1.var_66["ResistAir"] ? Number(param1.var_66["ResistAir"]) : 0;
         var _loc24_:Number = !!param1.var_66["ResistDeath"] ? Number(param1.var_66["ResistDeath"]) : 0;
         var _loc25_:Number = !!param1.var_66["ResistEarth"] ? Number(param1.var_66["ResistEarth"]) : 0;
         var _loc26_:Number = !!param1.var_66["ResistFire"] ? Number(param1.var_66["ResistFire"]) : 0;
         var _loc27_:Number = !!param1.var_66["ResistIce"] ? Number(param1.var_66["ResistIce"]) : 0;
         var _loc28_:Number = !!param1.var_66["ResistLife"] ? Number(param1.var_66["ResistLife"]) : 0;
         var _loc29_:String = String(_loc3_);
         var _loc30_:String = String(_loc4_);
         var _loc31_:String = String(_loc5_);
         var _loc32_:String = String(_loc6_);
         var _loc33_:* = "+" + Math.round(_loc11_ * 100) + "%";
         var _loc34_:* = "+" + Math.round(_loc9_ * 100) + "%";
         var _loc35_:* = "+" + Math.round(_loc7_ * 100) + "%";
         var _loc36_:* = "+" + _loc12_ + "%";
         var _loc37_:* = "+" + Math.round(_loc8_ * 100) + "%";
         var _loc38_:* = "+" + Math.round(_loc10_ * 100) + "%";
         var _loc39_:* = "+" + Math.round(_loc13_ * 100) + "%";
         var _loc40_:* = "+" + Math.round(_loc14_ * 100) + "%";
         var _loc41_:* = "+" + Math.round(_loc15_ * 100) + "%";
         var _loc42_:* = "+" + Math.round(_loc16_ * 100) + "%";
         var _loc43_:* = "+" + Math.round(_loc17_ * 100) + "%";
         var _loc44_:* = "+" + Math.round(_loc18_ * 100) + "%";
         var _loc45_:* = "+" + Math.round(_loc19_ * 100) + "%";
         var _loc46_:* = "+" + Math.round(_loc20_ * 100) + "%";
         var _loc47_:* = "+" + Math.round(_loc21_ * 100) + "%";
         var _loc48_:* = "+" + Math.round(_loc22_ * 100) + "%";
         var _loc49_:* = "+" + Math.round(_loc23_ * 100) + "%";
         var _loc50_:* = "+" + Math.round(_loc24_ * 100) + "%";
         var _loc51_:* = "+" + Math.round(_loc25_ * 100) + "%";
         var _loc52_:* = "+" + Math.round(_loc26_ * 100) + "%";
         var _loc53_:* = "+" + Math.round(_loc27_ * 100) + "%";
         var _loc54_:* = "+" + Math.round(_loc28_ * 100) + "%";
         if(Boolean(param2) && Boolean(mPaperDoll))
         {
            _loc57_ = Entity(mPaperDoll);
            _loc58_ = EntType.ARMOR_SLOT;
            while(_loc58_ < EntType.MAX_SLOTS)
            {
               _loc87_ = param1.mEquipGear[_loc58_];
               _loc57_.method_319(_loc58_,_loc87_);
               _loc58_++;
            }
            _loc57_.ResetEntType(_loc57_.entType,true);
            _loc59_ = param2.gearType.gearID;
            _loc60_ = uint(EntType.method_87(param2.gearType.type));
            _loc57_.method_319(_loc60_,_loc59_);
            _loc57_.ResetEntType(_loc57_.entType,true);
            _loc61_ = uint(_loc57_.maxHP);
            _loc62_ = uint(_loc57_.meleeDamage);
            _loc63_ = uint(_loc57_.magicDamage);
            _loc64_ = _loc57_.armorClass;
            _loc65_ = _loc57_.var_1337;
            _loc66_ = _loc57_.var_667 + _loc57_.var_640;
            _loc67_ = _loc57_.var_412;
            _loc68_ = _loc57_.var_571;
            _loc69_ = _loc57_.var_237;
            _loc70_ = Math.round(1000 * (_loc57_.totalMods.var_251 * const_806) / _loc57_.entType.var_251) / 10;
            _loc71_ = _loc57_.totalMods.itemDrop;
            _loc72_ = _loc57_.totalMods.var_152;
            _loc73_ = _loc57_.totalMods.var_79;
            _loc74_ = _loc57_.totalMods.var_697;
            _loc75_ = !!_loc57_.var_65["AirSlay"] ? Number(_loc57_.var_65["AirSlay"]) : 0;
            _loc76_ = !!_loc57_.var_65["DeathSlay"] ? Number(_loc57_.var_65["DeathSlay"]) : 0;
            _loc77_ = !!_loc57_.var_65["EarthSlay"] ? Number(_loc57_.var_65["EarthSlay"]) : 0;
            _loc78_ = !!_loc57_.var_65["FireSlay"] ? Number(_loc57_.var_65["FireSlay"]) : 0;
            _loc79_ = !!_loc57_.var_65["IceSlay"] ? Number(_loc57_.var_65["IceSlay"]) : 0;
            _loc80_ = !!_loc57_.var_65["LifeSlay"] ? Number(_loc57_.var_65["LifeSlay"]) : 0;
            _loc81_ = !!_loc57_.var_66["ResistAir"] ? Number(_loc57_.var_66["ResistAir"]) : 0;
            _loc82_ = !!_loc57_.var_66["ResistDeath"] ? Number(_loc57_.var_66["ResistDeath"]) : 0;
            _loc83_ = !!_loc57_.var_66["ResistEarth"] ? Number(_loc57_.var_66["ResistEarth"]) : 0;
            _loc84_ = !!_loc57_.var_66["ResistFire"] ? Number(_loc57_.var_66["ResistFire"]) : 0;
            _loc85_ = !!_loc57_.var_66["ResistIce"] ? Number(_loc57_.var_66["ResistIce"]) : 0;
            _loc86_ = !!_loc57_.var_66["ResistLife"] ? Number(_loc57_.var_66["ResistLife"]) : 0;
            _loc29_ = this.method_43(_loc3_,_loc61_);
            _loc30_ = this.method_43(_loc4_,_loc62_);
            _loc31_ = this.method_43(_loc5_,_loc63_);
            _loc32_ = this.method_43(_loc6_,_loc64_);
            _loc33_ = this.method_43(Math.round(_loc11_ * 100),Math.round(_loc69_ * 100),true);
            _loc34_ = this.method_43(Math.round(_loc9_ * 100),Math.round(_loc67_ * 100),true);
            _loc35_ = this.method_43(Math.round(_loc7_ * 100),Math.round(_loc65_ * 100),true);
            _loc36_ = this.method_43(_loc12_,_loc70_,true);
            _loc37_ = this.method_43(Math.round(_loc8_ * 100),Math.round(_loc66_ * 100),true);
            _loc38_ = this.method_43(Math.round(_loc10_ * 100),Math.round(_loc68_ * 100),true);
            _loc39_ = this.method_43(Math.round(_loc13_ * 100),Math.round(_loc71_ * 100),true);
            _loc40_ = this.method_43(Math.round(_loc14_ * 100),Math.round(_loc72_ * 100),true);
            _loc41_ = this.method_43(Math.round(_loc15_ * 100),Math.round(_loc73_ * 100),true);
            _loc42_ = this.method_43(Math.round(_loc16_ * 100),Math.round(_loc74_ * 100),true);
            _loc43_ = this.method_43(Math.round(_loc17_ * 100),Math.round(_loc75_ * 100),true);
            _loc44_ = this.method_43(Math.round(_loc18_ * 100),Math.round(_loc76_ * 100),true);
            _loc45_ = this.method_43(Math.round(_loc19_ * 100),Math.round(_loc77_ * 100),true);
            _loc46_ = this.method_43(Math.round(_loc20_ * 100),Math.round(_loc78_ * 100),true);
            _loc47_ = this.method_43(Math.round(_loc21_ * 100),Math.round(_loc79_ * 100),true);
            _loc48_ = this.method_43(Math.round(_loc22_ * 100),Math.round(_loc80_ * 100),true);
            _loc49_ = this.method_43(Math.round(_loc23_ * 100),Math.round(_loc81_ * 100),true);
            _loc50_ = this.method_43(Math.round(_loc24_ * 100),Math.round(_loc82_ * 100),true);
            _loc51_ = this.method_43(Math.round(_loc25_ * 100),Math.round(_loc83_ * 100),true);
            _loc52_ = this.method_43(Math.round(_loc26_ * 100),Math.round(_loc84_ * 100),true);
            _loc53_ = this.method_43(Math.round(_loc27_ * 100),Math.round(_loc85_ * 100),true);
            _loc54_ = this.method_43(Math.round(_loc28_ * 100),Math.round(_loc86_ * 100),true);
         }
         var _loc56_:*;
         if(!(_loc56_ = this.var_227 == const_284))
         {
            _loc55_ = this.var_148.mMovieClip.am_Panel.am_StatisticsGroup;
            MathUtil.method_2(_loc55_.am_Health,_loc29_,true);
            MathUtil.method_2(_loc55_.am_Melee,_loc30_,true);
            MathUtil.method_2(_loc55_.am_Magic,_loc31_,true);
            MathUtil.method_2(_loc55_.am_Haste,_loc34_,true);
            MathUtil.method_2(_loc55_.am_Defense,_loc32_,true);
            MathUtil.method_2(_loc55_.am_Recovery,_loc33_,true);
            MathUtil.method_2(_loc55_.am_Critical,_loc35_,true);
            MathUtil.method_2(_loc55_.am_Speed,_loc36_,true);
            MathUtil.method_2(_loc55_.am_CriticalPower,_loc37_,true);
            MathUtil.method_2(_loc55_.am_Tenacity,_loc38_,true);
            if(_loc88_ = param1.mMasterClass)
            {
               MathUtil.method_2(_loc55_.am_Class,Game.method_226(_loc88_));
            }
            else
            {
               MathUtil.method_2(_loc55_.am_Class,param1.entType.className.toString());
            }
            MathUtil.method_2(_loc55_.am_Level,"Level " + param1.mExpLevel);
         }
         else
         {
            _loc55_ = this.var_148.mMovieClip.am_Panel.am_ElementsGroup;
            MathUtil.method_2(_loc55_.am_ItemFind,_loc39_,true);
            MathUtil.method_2(_loc55_.am_CraftFind,_loc40_,true);
            MathUtil.method_2(_loc55_.am_GoldFind,_loc41_,true);
            MathUtil.method_2(_loc55_.am_XPBonus,_loc42_,true);
            MathUtil.method_2(_loc55_.am_AttackIce,_loc47_,true);
            MathUtil.method_2(_loc55_.am_AttackFire,_loc46_,true);
            MathUtil.method_2(_loc55_.am_AttackAir,_loc43_,true);
            MathUtil.method_2(_loc55_.am_AttackEarth,_loc45_,true);
            MathUtil.method_2(_loc55_.am_AttackLife,_loc48_,true);
            MathUtil.method_2(_loc55_.am_AttackDeath,_loc44_,true);
            MathUtil.method_2(_loc55_.am_DefenseIce,_loc53_,true);
            MathUtil.method_2(_loc55_.am_DefenseFire,_loc52_,true);
            MathUtil.method_2(_loc55_.am_DefenseAir,_loc49_,true);
            MathUtil.method_2(_loc55_.am_DefenseEarth,_loc51_,true);
            MathUtil.method_2(_loc55_.am_DefenseLife,_loc54_,true);
            MathUtil.method_2(_loc55_.am_DefenseDeath,_loc50_,true);
         }
         MathUtil.method_2(this.var_148.mMovieClip.am_Panel.am_SlideOutName,"Statistics");
      }
      
      private function method_552(param1:Entity) : void
      {
         var _loc2_:MovieClip = this.var_148.mMovieClip.am_Panel.am_Prefabs;
         this.method_151();
         MathUtil.method_2(this.var_148.mMovieClip.am_Panel.am_SlideOutName,"Gear Manager");
      }
      
      private function method_1162(param1:Entity) : void
      {
         if(this.var_215.mbVisible)
         {
            MathUtil.method_2(var_2.am_CharacterName,"Search Your Gear For:");
         }
         else if(this.var_56 == const_86)
         {
            MathUtil.method_2(var_2.am_CharacterName,"Charm Socketing");
         }
         else if(this.var_56 == const_68)
         {
            MathUtil.method_2(var_2.am_CharacterName,"Pet Manager");
         }
         else
         {
            MathUtil.method_2(var_2.am_CharacterName,var_1.clientEntName);
         }
      }
      
      private function method_228(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         if(this.var_80 < 0 || this.var_80 >= var_1.mGearsetList.length)
         {
            return;
         }
         var _loc5_:uint;
         var _loc4_:Vector.<uint>;
         if((_loc5_ = (_loc4_ = var_1.mGearsetList[this.var_80])[param2]) != 0)
         {
            var_1.screenHudTooltip.ShowGearTooltip(_loc3_,_loc5_,false,null,370.5,387);
            var_1.screenHudTooltip.ShowGearTooltip(_loc3_,_loc5_,true,null,46.5,387);
         }
      }
      
      private function method_204(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_ || !var_1.CanSendPacket())
         {
            return;
         }
         if(this.var_80 < 0 || this.var_80 >= var_1.mGearsetList.length)
         {
            return;
         }
         var _loc4_:Vector.<uint>;
         var _loc5_:uint = (_loc4_ = var_1.mGearsetList[this.var_80])[param2];
         var _loc6_:class_42;
         if(!(_loc6_ = var_1.mOwnedGear[_loc5_]))
         {
            return;
         }
         if(param1.ctrlKey)
         {
            this.LinkGearInChat(0,_loc6_);
            return;
         }
         var _loc7_:GearType = _loc6_.gearType;
         var _loc8_:uint = uint(EntType.method_87(_loc7_.type));
         if(_loc5_ == _loc3_.mEquipGear[_loc8_])
         {
            return;
         }
         var_1.linkUpdater.WriteUpdateSingleGear(_loc3_,_loc8_,_loc5_);
         _loc3_.method_303(_loc8_,_loc5_);
         if(SoundConfig.var_199)
         {
            SoundManager.Play(SoundConfig.var_199);
         }
         this.method_827(_loc8_,_loc8_,_loc7_);
         Refresh();
      }
      
      private function method_1905(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Vector.<uint> = null;
         var _loc4_:uint = 0;
         var _loc5_:Boolean = false;
         var _loc6_:uint = 0;
         var _loc7_:MovieClip = null;
         var _loc8_:MovieClip = null;
         var _loc9_:MovieClip = null;
         var _loc10_:uint = 0;
         var _loc11_:class_42 = null;
         var _loc12_:GearType = null;
         var _loc13_:SuperAnimInstance = null;
         var _loc14_:String = null;
         this.method_151();
         if(param2 < var_1.mGearsetList.length)
         {
            _loc3_ = var_1.mGearsetList[param2];
            this.var_80 = param2;
            _loc4_ = 0;
            while(_loc4_ < const_134)
            {
               _loc7_ = this.var_472[_loc4_].mMovieClip;
               if(_loc4_ == this.var_80)
               {
                  _loc7_.am_Selector.visible = true;
               }
               else
               {
                  _loc7_.am_Selector.visible = false;
               }
               _loc4_++;
            }
            _loc5_ = true;
            _loc6_ = 1;
            while(_loc6_ < this.var_225.length)
            {
               _loc9_ = (_loc8_ = this.var_225[_loc6_].mMovieClip).am_IconHolder.am_Button;
               method_14(_loc9_);
               this.method_116(_loc8_);
               _loc10_ = _loc3_[_loc6_];
               if(_loc11_ = var_1.mOwnedGear[_loc10_])
               {
                  _loc5_ = false;
                  _loc12_ = _loc11_.gearType;
                  _loc13_ = var_1.RenderGear(Game.const_95,_loc12_,0.43);
                  method_52(_loc9_,_loc13_);
                  if((_loc14_ = _loc12_.var_8) == "R")
                  {
                     _loc8_.am_RarityRare.visible = true;
                  }
                  else if(_loc14_ == "L")
                  {
                     _loc8_.am_RarityLegendary.visible = true;
                  }
                  else
                  {
                     _loc8_.am_RarityMagic.visible = true;
                  }
               }
               _loc6_++;
            }
            this.method_564();
            if(_loc5_)
            {
               this.var_455.Show();
               this.var_413.Hide();
            }
            else
            {
               this.var_455.Hide();
               this.var_413.Show();
            }
         }
         else if(param2 == var_1.mGearsetList.length)
         {
            this.method_1955(param2);
            this.method_881();
         }
      }
      
      private function method_814(param1:MouseEvent) : void
      {
         var _loc6_:MovieClip = null;
         var _loc7_:MovieClip = null;
         var _loc8_:uint = 0;
         var _loc9_:class_42 = null;
         var _loc10_:GearType = null;
         var _loc11_:SuperAnimInstance = null;
         var _loc12_:String = null;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         if(this.var_80 < 0 || this.var_80 >= var_1.mGearsetList.length)
         {
            return;
         }
         var _loc3_:Vector.<uint> = var_1.mGearsetList[this.var_80];
         if(!this.method_1904(_loc2_,_loc3_))
         {
            return;
         }
         var _loc4_:Boolean = true;
         var _loc5_:uint = 1;
         while(_loc5_ < EntType.MAX_SLOTS)
         {
            _loc7_ = (_loc6_ = this.var_225[_loc5_].mMovieClip).am_IconHolder.am_Button;
            method_14(_loc7_);
            this.method_116(_loc6_);
            _loc3_[_loc5_] = _loc2_.mEquipGear[_loc5_];
            _loc8_ = _loc3_[_loc5_];
            if(_loc9_ = var_1.mOwnedGear[_loc8_])
            {
               _loc4_ = false;
               _loc10_ = _loc9_.gearType;
               _loc11_ = var_1.RenderGear(Game.const_95,_loc10_,0.43);
               method_52(_loc7_,_loc11_);
               if((_loc12_ = _loc10_.var_8) == "R")
               {
                  _loc6_.am_RarityRare.visible = true;
               }
               else if(_loc12_ == "L")
               {
                  _loc6_.am_RarityLegendary.visible = true;
               }
               else
               {
                  _loc6_.am_RarityMagic.visible = true;
               }
               this.method_1488(_loc5_,_loc5_,_loc10_);
            }
            _loc5_++;
         }
         if(_loc4_)
         {
            this.var_455.Show();
            this.var_413.Hide();
         }
         else
         {
            this.var_455.Hide();
            this.var_413.Show();
         }
         this.method_1743(this.var_80);
         Refresh();
      }
      
      private function method_827(param1:uint, param2:uint, param3:GearType) : void
      {
         var _loc4_:MovieClip;
         var _loc5_:Rectangle = (_loc4_ = this.var_225[param1].mMovieClip.am_Locator).getBounds(mWindow.mMovieClip);
         var _loc6_:MovieClip = this.var_500[param2].mMovieClip.am_Locator;
         this.method_707(_loc5_.x,_loc5_.y,_loc6_,param3);
      }
      
      private function method_1488(param1:uint, param2:uint, param3:GearType) : void
      {
         var _loc4_:MovieClip;
         var _loc5_:Rectangle = (_loc4_ = this.var_500[param1].mMovieClip.am_Locator).getBounds(mWindow.mMovieClip);
         var _loc6_:MovieClip = this.var_225[param2].mMovieClip.am_Locator;
         this.method_707(_loc5_.x,_loc5_.y,_loc6_,param3);
      }
      
      private function method_707(param1:Number, param2:Number, param3:MovieClip, param4:GearType) : void
      {
         var _loc5_:MovieClip = class_4.method_16("a_EmptyGearSlotMoveable");
         var _loc6_:SuperAnimInstance = var_1.RenderGear(Game.const_95,param4,0.43);
         method_52(_loc5_.am_IconHolder.am_Button,_loc6_);
         if(param4.var_8 == "L")
         {
            _loc5_.am_Base.am_RarityMagic.visible = false;
            _loc5_.am_Base.am_RarityRare.visible = false;
            _loc5_.am_Base.am_RarityLegendary.visible = true;
         }
         else if(param4.var_8 == "R")
         {
            _loc5_.am_Base.am_RarityMagic.visible = false;
            _loc5_.am_Base.am_RarityRare.visible = true;
            _loc5_.am_Base.am_RarityLegendary.visible = false;
         }
         else
         {
            _loc5_.am_Base.am_RarityMagic.visible = true;
            _loc5_.am_Base.am_RarityRare.visible = false;
            _loc5_.am_Base.am_RarityLegendary.visible = false;
         }
         method_201(_loc5_,param1,param2,param3,300,class_137.method_113);
      }
      
      private function method_1349() : void
      {
         var _loc1_:uint = uint(var_496.length);
         var _loc2_:uint = 0;
         while(_loc2_ < _loc1_)
         {
            var_496[_loc2_].ForceComplete();
            _loc2_++;
         }
      }
      
      private function method_1025(param1:MouseEvent) : void
      {
         var _loc6_:uint = 0;
         var _loc7_:class_42 = null;
         var _loc8_:GearType = null;
         var _loc9_:uint = 0;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_ || !var_1.CanSendPacket())
         {
            return;
         }
         if(this.var_80 < 0 || this.var_80 >= var_1.mGearsetList.length)
         {
            return;
         }
         var _loc3_:Boolean = false;
         var _loc4_:Vector.<uint> = var_1.mGearsetList[this.var_80];
         var _loc5_:uint = 1;
         while(_loc5_ < EntType.MAX_SLOTS)
         {
            if(_loc6_ = _loc4_[_loc5_])
            {
               _loc8_ = (_loc7_ = var_1.mOwnedGear[_loc6_]).gearType;
               _loc9_ = uint(EntType.method_87(_loc8_.type));
               if(_loc6_ != _loc2_.mEquipGear[_loc9_])
               {
                  _loc3_ = true;
                  this.method_827(_loc5_,_loc9_,_loc8_);
               }
            }
            _loc5_++;
         }
         if(_loc3_)
         {
            var_1.linkUpdater.WriteUpdateEquipment(_loc2_,_loc4_);
            _loc2_.method_1899(_loc4_);
         }
         if(SoundConfig.var_199)
         {
            SoundManager.Play(SoundConfig.var_199);
         }
         Refresh();
      }
      
      private function method_1867(param1:MouseEvent) : void
      {
         this.method_575();
         this.method_151();
      }
      
      private function method_575() : void
      {
         var _loc1_:String = String(this.var_311.mMovieClip.am_NameField.text);
         this.method_1247(this.var_80,_loc1_);
         var_1.mGearsetListName[this.var_80] = _loc1_;
         var _loc2_:MovieClip = this.var_472[this.var_80].mMovieClip;
         var _loc3_:TextField = _loc2_.am_SlideOutName;
         MathUtil.method_2(_loc3_,_loc1_);
      }
      
      private function method_881() : void
      {
         var _loc1_:TextField = null;
         if(this.var_80 >= 0 && this.var_80 < var_1.mGearsetList.length)
         {
            if(this.var_311.mbVisible)
            {
               this.method_151();
            }
            else
            {
               this.var_529 = true;
               _loc1_ = this.var_311.mMovieClip.am_NameField;
               MathUtil.method_2(_loc1_,var_1.mGearsetListName[this.var_80]);
               _loc1_.stage.focus = _loc1_;
               _loc1_.setSelection(0,_loc1_.text.length);
               this.var_311.Show();
            }
         }
      }
      
      private function method_1166(param1:MouseEvent) : void
      {
         this.method_881();
      }
      
      private function method_608() : void
      {
         var _loc2_:MovieClip = null;
         var _loc3_:uint = 0;
         var _loc5_:TextField = null;
         var _loc6_:uint = 0;
         var _loc7_:TextField = null;
         var _loc8_:MovieClip = null;
         var _loc9_:Vector.<uint> = null;
         var _loc10_:uint = 0;
         var _loc11_:class_42 = null;
         var _loc12_:GearType = null;
         var _loc13_:SuperAnimInstance = null;
         var _loc14_:String = null;
         this.var_529 = false;
         var _loc1_:uint = uint(var_1.mGearsetList.length);
         this.method_564();
         _loc3_ = 0;
         while(_loc3_ < const_134)
         {
            _loc2_ = this.var_472[_loc3_].mMovieClip;
            _loc5_ = _loc2_.am_SlideOutName;
            if(_loc3_ < _loc1_)
            {
               this.var_472[_loc3_].Show();
               _loc2_.am_Plus.visible = false;
               _loc2_.am_ShieldIcon.visible = true;
               _loc6_ = uint(_loc3_ + 1);
               _loc7_ = _loc2_.am_ShieldIcon.am_Count;
               MathUtil.method_2(_loc5_,var_1.mGearsetListName[_loc3_]);
               MathUtil.method_2(_loc7_,_loc6_.toString());
            }
            else if(_loc3_ == _loc1_)
            {
               this.var_472[_loc3_].Show();
               _loc2_.am_Plus.visible = true;
               _loc2_.am_ShieldIcon.visible = false;
            }
            else
            {
               this.var_472[_loc3_].Hide();
            }
            if(_loc3_ == this.var_80)
            {
               _loc2_.am_Selector.visible = true;
            }
            else
            {
               _loc2_.am_Selector.visible = false;
            }
            _loc3_++;
         }
         var _loc4_:Boolean = true;
         _loc3_ = 1;
         while(_loc3_ < EntType.MAX_SLOTS)
         {
            _loc2_ = this.var_225[_loc3_].mMovieClip;
            _loc8_ = _loc2_.am_IconHolder.am_Button;
            method_14(_loc8_);
            this.method_116(_loc2_);
            if(this.var_80 >= 0 && this.var_80 < var_1.mGearsetList.length)
            {
               _loc10_ = (_loc9_ = var_1.mGearsetList[this.var_80])[_loc3_];
               if(_loc11_ = var_1.mOwnedGear[_loc10_])
               {
                  _loc4_ = false;
                  _loc12_ = _loc11_.gearType;
                  _loc13_ = var_1.RenderGear(Game.const_95,_loc12_,0.43);
                  method_52(_loc8_,_loc13_);
                  if((_loc14_ = _loc12_.var_8) == "R")
                  {
                     _loc2_.am_RarityRare.visible = true;
                  }
                  else if(_loc14_ == "L")
                  {
                     _loc2_.am_RarityLegendary.visible = true;
                  }
                  else
                  {
                     _loc2_.am_RarityMagic.visible = true;
                  }
               }
            }
            _loc3_++;
         }
         if(this.var_80 != -1)
         {
            if(_loc4_)
            {
               this.var_455.Show();
               this.var_413.Hide();
            }
            else
            {
               this.var_455.Hide();
               this.var_413.Show();
            }
         }
      }
      
      private function method_1591(param1:Entity) : void
      {
         var _loc6_:MovieClip = null;
         var _loc7_:MovieClip = null;
         var _loc8_:uint = 0;
         var _loc9_:class_42 = null;
         var _loc10_:GearType = null;
         var _loc11_:uint = 0;
         var _loc12_:SuperAnimInstance = null;
         var _loc13_:String = null;
         var _loc14_:uint = 0;
         var _loc15_:class_151 = null;
         var _loc16_:class_15 = null;
         var _loc17_:MovieClip = null;
         var _loc2_:Array = var_1.mFilteredOwnedGear;
         var _loc3_:int = this.method_260(_loc2_,0);
         var _loc4_:int = _loc3_ > const_10 ? _loc3_ - const_10 : 0;
         var _loc5_:uint = 0;
         while(_loc5_ < const_10)
         {
            _loc7_ = (_loc6_ = this.var_95[_loc5_].mMovieClip).am_GearIconHolder.am_Button;
            _loc8_ = uint(this.method_260(_loc2_,_loc5_));
            method_14(_loc7_);
            this.method_116(_loc6_);
            _loc6_.am_GearIconHolder.visible = true;
            if(this.method_490(_loc5_))
            {
               _loc14_ = _loc5_ - (const_10 - var_1.mLockboxData.mUniqueLockboxes);
               if(_loc15_ = var_1.mLockboxData.mLockboxList[_loc14_])
               {
                  _loc16_ = _loc15_.var_286;
                  _loc17_ = method_12(_loc7_,_loc16_.iconName);
                  _loc17_.x -= 22;
                  _loc17_.y -= 37;
                  _loc6_.am_Quantity.visible = true;
                  MathUtil.method_2(_loc6_.am_Quantity,String(_loc15_.stackCount));
               }
            }
            else if(_loc3_ >= _loc4_)
            {
               if(_loc8_ >= 0)
               {
                  if(_loc9_ = _loc2_[_loc8_])
                  {
                     _loc10_ = _loc9_.gearType;
                     _loc11_ = uint(EntType.method_87(_loc10_.type));
                     _loc6_.am_Equipped.visible = _loc10_.gearID == param1.mEquipGear[_loc11_];
                     if(!_loc9_.var_1814)
                     {
                        _loc6_.am_New.visible = false;
                     }
                     else
                     {
                        _loc6_.am_New.visible = true;
                        _loc9_.var_1814 = false;
                     }
                     _loc12_ = var_1.RenderGear(Game.const_95,_loc10_,0.43);
                     method_52(_loc7_,_loc12_);
                     if((_loc13_ = _loc10_.var_8) == "R")
                     {
                        _loc6_.am_RarityRare.visible = true;
                     }
                     else if(_loc13_ == "L")
                     {
                        _loc6_.am_RarityLegendary.visible = true;
                     }
                     else
                     {
                        _loc6_.am_RarityMagic.visible = true;
                     }
                  }
               }
            }
            _loc5_++;
         }
      }
      
      private function method_1456(param1:Entity) : void
      {
         var _loc7_:MovieClip = null;
         var _loc8_:MovieClip = null;
         var _loc9_:class_114 = null;
         var _loc2_:Vector.<class_114> = this.method_214(param1);
         var _loc3_:uint = _loc2_.length;
         var _loc4_:int = var_16 * const_10;
         var _loc5_:int = (var_16 + 1) * const_10 >= _loc3_ ? int(_loc3_) : int((var_16 + 1) * const_10);
         var _loc6_:uint = 0;
         while(_loc6_ < const_12)
         {
            _loc8_ = (_loc7_ = this.var_95[_loc6_].mMovieClip).am_CharmIconHolder;
            method_14(_loc8_);
            this.method_116(_loc7_);
            _loc7_.am_Quantity.visible = true;
            _loc7_.am_CharmIconHolder.visible = true;
            _loc7_.am_RarityMagic.visible = true;
            MathUtil.method_2(_loc7_.am_Quantity,"");
            if(_loc4_ < _loc5_)
            {
               if(_loc9_ = _loc2_[_loc4_])
               {
                  _loc9_.charmData.method_78(this,_loc8_);
                  MathUtil.method_2(_loc7_.am_Quantity,_loc9_.var_181.toString());
               }
            }
            _loc4_++;
            _loc6_++;
         }
      }
      
      private function method_1879(param1:Entity) : void
      {
         var _loc7_:MovieClip = null;
         var _loc8_:MovieClip = null;
         var _loc9_:class_76 = null;
         var _loc2_:Vector.<class_76> = this.method_480(param1);
         var _loc3_:uint = _loc2_.length;
         var _loc4_:int = var_16 * const_10;
         var _loc5_:int = (var_16 + 1) * const_10 >= _loc3_ ? int(_loc3_) : int((var_16 + 1) * const_10);
         var _loc6_:uint = 0;
         while(_loc6_ < const_12)
         {
            _loc8_ = (_loc7_ = this.var_95[_loc6_].mMovieClip).am_ItemIconHolder;
            method_14(_loc8_);
            this.method_116(_loc7_);
            _loc7_.am_Quantity.visible = true;
            _loc7_.am_ItemIconHolder.visible = true;
            MathUtil.method_2(_loc7_.am_Quantity,"");
            if(_loc4_ < _loc5_)
            {
               if(_loc9_ = _loc2_[_loc4_])
               {
                  method_12(_loc8_,_loc9_.materialType.iconName);
                  MathUtil.method_2(_loc7_.am_Quantity,_loc9_.var_181.toString());
               }
            }
            _loc4_++;
            _loc6_++;
         }
      }
      
      private function method_1514(param1:Entity) : void
      {
         var _loc9_:MovieClip = null;
         var _loc10_:MovieClip = null;
         var _loc11_:class_87 = null;
         var _loc12_:Bitmap = null;
         var _loc2_:Vector.<class_87> = var_1.mEggPetInfo.mOwnedPets;
         var _loc3_:Vector.<class_87> = var_1.mEggPetInfo.mRestingPetList;
         var _loc4_:uint = _loc2_.length;
         var _loc5_:int = var_16 * const_10;
         var _loc6_:int = (var_16 + 1) * const_10 >= _loc4_ ? int(_loc4_) : int((var_16 + 1) * const_10);
         var _loc7_:Number = Number(var_1.main.overallScale);
         var _loc8_:uint = 0;
         while(_loc8_ < const_12)
         {
            _loc10_ = (_loc9_ = this.var_95[_loc8_].mMovieClip).am_ItemIconHolder;
            method_14(_loc10_);
            this.method_116(_loc9_);
            _loc9_.am_RarityMagic.visible = true;
            _loc9_.am_ItemIconHolder.visible = true;
            if(_loc5_ < _loc6_)
            {
               if(!(_loc11_ = _loc2_[_loc5_]))
               {
                  _loc9_.am_IconActive.visible = false;
                  _loc9_.am_IconPassive.visible = false;
               }
               else
               {
                  _loc12_ = class_41.method_85(_loc11_.mPetType,2,2,44,44,_loc7_);
                  _loc10_.addChild(_loc12_);
                  if(_loc11_.var_23 == class_7.const_35)
                  {
                     _loc9_.am_Star.visible = true;
                  }
                  else
                  {
                     _loc9_.am_Level.visible = true;
                     MathUtil.method_2(_loc9_.am_Level,String(_loc11_.var_23));
                  }
                  _loc9_.am_IconActive.visible = _loc11_ == var_1.mEggPetInfo.mActivePet;
                  _loc9_.am_IconPassive.visible = var_1.mEggPetInfo.mRestingPetList.indexOf(_loc11_) >= 0;
                  if(_loc11_ == var_1.mEggPetInfo.mTrainingPet)
                  {
                     _loc10_.filters = [class_50.const_112];
                  }
                  else
                  {
                     _loc10_.filters = [];
                  }
               }
            }
            _loc5_++;
            _loc8_++;
         }
      }
      
      private function method_1427(param1:Entity) : void
      {
         var _loc8_:MovieClip = null;
         var _loc9_:MovieClip = null;
         var _loc10_:class_20 = null;
         var _loc11_:Bitmap = null;
         var _loc2_:Vector.<class_20> = this.method_296(param1);
         var _loc3_:uint = _loc2_.length;
         var _loc4_:int = var_16 * const_10;
         var _loc5_:int = (var_16 + 1) * const_10 >= _loc3_ ? int(_loc3_) : int((var_16 + 1) * const_10);
         var _loc6_:Number = Number(var_1.main.overallScale);
         var _loc7_:uint = 0;
         while(_loc7_ < const_12)
         {
            _loc9_ = (_loc8_ = this.var_95[_loc7_].mMovieClip).am_ItemIconHolder;
            method_14(_loc9_);
            this.method_116(_loc8_);
            _loc8_.am_RarityMagic.visible = true;
            _loc8_.am_ItemIconHolder.visible = true;
            if(_loc4_ < _loc5_)
            {
               if(!(_loc10_ = _loc2_[_loc4_]))
               {
                  _loc8_.am_Equipped.visible = false;
               }
               else
               {
                  _loc11_ = class_41.method_168(_loc10_,2,2,44,44,_loc6_);
                  _loc9_.addChild(_loc11_);
                  _loc8_.am_Equipped.visible = _loc10_ == param1.mEquipMount ? true : false;
               }
            }
            _loc4_++;
            _loc7_++;
         }
      }
      
      private function method_1447(param1:Entity) : void
      {
         var _loc7_:MovieClip = null;
         var _loc8_:MovieClip = null;
         var _loc9_:class_103 = null;
         var _loc10_:class_3 = null;
         var _loc11_:MovieClip = null;
         var_1.mConsumablesList.sort(this.method_877);
         this.var_654 = this.method_1732(var_1.mConsumablesList);
         var_44 = this.method_1382();
         var _loc2_:uint = this.var_654.length;
         var _loc3_:int = var_16 * const_10;
         var _loc4_:int = (var_16 + 1) * const_10 >= _loc2_ ? int(_loc2_) : int((var_16 + 1) * const_10);
         var _loc6_:uint = 0;
         while(_loc6_ < const_12)
         {
            _loc8_ = (_loc7_ = this.var_95[_loc6_].mMovieClip).am_ItemIconHolder;
            method_14(_loc8_);
            this.method_116(_loc7_);
            _loc7_.am_RarityMagic.visible = true;
            _loc7_.am_ItemIconHolder.visible = true;
            _loc7_.am_Quantity.visible = true;
            MathUtil.method_2(_loc7_.am_Quantity,"");
            if(_loc3_ < _loc4_)
            {
               if(_loc9_ = this.var_654[_loc3_])
               {
                  _loc10_ = _loc9_.consumableType;
                  method_12(_loc8_,_loc9_.consumableType.iconName);
                  if(_loc10_ == param1.mCurrPotion)
                  {
                     MathUtil.method_2(_loc7_.am_Quantity,String(_loc9_.method_915()));
                  }
                  else
                  {
                     MathUtil.method_2(_loc7_.am_Quantity,String(_loc9_.method_943()));
                  }
                  _loc7_.am_Equipped.visible = _loc10_ == param1.mNextPotion ? true : false;
                  if((_loc11_ = MovieClip(_loc8_.getChildAt(0))) && !_loc10_.var_821 && !_loc10_.var_427 || _loc10_.type == "PetFood" && !var_1.mEggPetInfo.mActivePet)
                  {
                     _loc11_.alpha = 0.75;
                     _loc11_.filters = [class_50.const_112];
                  }
                  else if(_loc11_)
                  {
                     _loc11_.alpha = 1;
                     _loc11_.filters = [];
                  }
               }
            }
            _loc3_++;
            _loc6_++;
         }
      }
      
      private function method_116(param1:MovieClip) : void
      {
         if(param1.am_Equipped)
         {
            param1.am_Equipped.visible = false;
         }
         if(param1.am_IconActive)
         {
            param1.am_IconActive.visible = false;
         }
         if(param1.am_IconPassive)
         {
            param1.am_IconPassive.visible = false;
         }
         if(param1.am_RarityRare)
         {
            param1.am_RarityRare.visible = false;
         }
         if(param1.am_RarityMagic)
         {
            param1.am_RarityMagic.visible = false;
         }
         if(param1.am_RarityLegendary)
         {
            param1.am_RarityLegendary.visible = false;
         }
         if(param1.am_GearIconHolder)
         {
            param1.am_GearIconHolder.visible = false;
         }
         if(param1.am_ItemIconHolder)
         {
            param1.am_ItemIconHolder.visible = false;
         }
         if(param1.am_CharmIconHolder)
         {
            param1.am_CharmIconHolder.visible = false;
         }
         if(param1.am_Quantity)
         {
            param1.am_Quantity.visible = false;
         }
         if(param1.am_New)
         {
            param1.am_New.visible = false;
         }
         if(param1.am_Level)
         {
            param1.am_Level.visible = false;
         }
         if(param1.am_Star)
         {
            param1.am_Star.visible = false;
         }
      }
      
      private function method_2040(param1:Entity) : Vector.<class_42>
      {
         var _loc6_:GearType = null;
         var _loc7_:class_42 = null;
         var _loc2_:String = param1.entType.className;
         var _loc3_:Vector.<GearType> = class_14.var_842[_loc2_ + ":" + var_16 + ":" + "M"];
         var _loc4_:Vector.<GearType> = class_14.var_842[_loc2_ + ":" + var_16 + ":" + "R"];
         var _loc5_:Vector.<GearType> = class_14.var_842[_loc2_ + ":" + var_16 + ":" + "L"];
         var _loc8_:Array = var_1.mOwnedGear;
         var _loc9_:uint = _loc3_.length;
         var _loc10_:Vector.<class_42> = new Vector.<class_42>();
         var _loc11_:uint = 0;
         while(_loc11_ < _loc9_)
         {
            _loc6_ = _loc5_[_loc11_];
            if(_loc7_ = _loc8_[_loc6_.gearID])
            {
               _loc10_.push(_loc7_);
            }
            else
            {
               _loc6_ = _loc4_[_loc11_];
               if(_loc7_ = _loc8_[_loc6_.gearID])
               {
                  _loc10_.push(_loc7_);
               }
               else
               {
                  _loc6_ = _loc3_[_loc11_];
                  if(_loc7_ = _loc8_[_loc6_.gearID])
                  {
                     _loc10_.push(_loc7_);
                  }
               }
            }
            _loc11_++;
         }
         _loc10_.fixed = true;
         return _loc10_;
      }
      
      private function method_296(param1:Entity) : Vector.<class_20>
      {
         var _loc6_:class_20 = null;
         var _loc2_:Array = var_1.mOwnedMounts;
         var _loc3_:Vector.<class_20> = new Vector.<class_20>();
         var _loc4_:uint = _loc2_.length;
         var _loc5_:uint = 0;
         while(_loc5_ < _loc4_)
         {
            if(_loc6_ = _loc2_[_loc5_])
            {
               _loc6_ = class_14.var_464[_loc6_.var_197];
               _loc3_.push(_loc6_);
            }
            _loc5_++;
         }
         _loc3_.fixed = true;
         return _loc3_;
      }
      
      private function method_214(param1:Entity) : Vector.<class_114>
      {
         var _loc4_:class_114 = null;
         var _loc2_:Array = var_1.mOwnedCharms;
         var _loc3_:Vector.<class_114> = new Vector.<class_114>();
         for each(_loc4_ in _loc2_)
         {
            _loc3_.push(_loc4_);
         }
         _loc3_.sort(this.method_1603);
         _loc3_.fixed = true;
         return _loc3_;
      }
      
      private function method_480(param1:Entity) : Vector.<class_76>
      {
         var _loc4_:class_76 = null;
         var _loc2_:Array = var_1.mOwnedMaterials;
         var _loc3_:Vector.<class_76> = new Vector.<class_76>();
         for each(_loc4_ in _loc2_)
         {
            _loc3_.push(_loc4_);
         }
         _loc3_.sort(class_75.method_1201);
         _loc3_.fixed = true;
         return _loc3_;
      }
      
      private function method_2066(param1:Entity) : Vector.<class_103>
      {
         var _loc4_:class_103 = null;
         var _loc2_:Array = var_1.mOwnedConsumables;
         var _loc3_:Vector.<class_103> = new Vector.<class_103>();
         for each(_loc4_ in _loc2_)
         {
            _loc3_.push(_loc4_);
         }
         _loc3_.sort(this.method_877);
         _loc3_.fixed = true;
         return _loc3_;
      }
      
      private function method_1603(param1:class_114, param2:class_114) : int
      {
         var _loc3_:class_1 = param1.charmData.var_13;
         var _loc4_:class_1 = param2.charmData.var_13;
         var _loc5_:uint = _loc3_.var_2208;
         var _loc6_:uint = _loc4_.var_2208;
         if(_loc5_ < _loc6_)
         {
            return 1;
         }
         if(_loc5_ > _loc6_)
         {
            return -1;
         }
         if(_loc3_.var_68 < _loc4_.var_68)
         {
            return 1;
         }
         if(_loc3_.var_68 > _loc4_.var_68)
         {
            return -1;
         }
         if(param1.charmData.secondary < param2.charmData.secondary)
         {
            return 1;
         }
         if(param1.charmData.secondary > param2.charmData.secondary)
         {
            return -1;
         }
         return param1.charmData.var_8 < param2.charmData.var_8 ? 1 : -1;
      }
      
      private function method_877(param1:class_103, param2:class_103) : int
      {
         var _loc3_:class_3 = param1.consumableType;
         var _loc4_:class_3 = param2.consumableType;
         if(_loc3_.var_427 && !_loc4_.var_427)
         {
            return -1;
         }
         if(_loc4_.var_427 && !_loc3_.var_427)
         {
            return 1;
         }
         if(_loc3_.var_821 && !_loc4_.var_821)
         {
            return -1;
         }
         if(_loc4_.var_821 && !_loc3_.var_821)
         {
            return 1;
         }
         return _loc3_.consumableID < _loc4_.consumableID ? 1 : -1;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc2_:uint = 0;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         if(this.var_148.mMovieClip.currentFrame != 1)
         {
            if(this.var_148.mMovieClip.am_Panel.am_Prefabs.visible)
            {
               this.method_552(_loc1_);
            }
            else if(this.var_148.mMovieClip.am_Panel.am_StatisticsGroup.visible)
            {
               this.method_170(_loc1_);
            }
         }
         else if(!this.var_466.mbVisible && this.var_227 == const_335)
         {
            this.var_227 = -1;
         }
         this.var_1764.DisableButton("Inactive");
         if(this.var_56 == const_120)
         {
            var_44 = this.method_1480();
            this.var_1764.EnableButton();
            this.method_176();
            this.method_1591(_loc1_);
            this.var_98.Hide();
            this.var_591.Hide();
            var_2.am_PaperDollHolder.visible = !this.var_215.mbVisible;
         }
         else if(this.var_56 == const_86)
         {
            if(!this.var_1863)
            {
               _loc2_ = 0;
               while(_loc2_ < const_134)
               {
                  this.var_762[_loc2_].PlayAnimation("FadeIn");
                  _loc2_++;
               }
               this.var_1863 = true;
            }
            var_44 = this.method_1715();
            this.method_1456(_loc1_);
            this.method_211();
            this.method_1123();
            this.var_98.Show();
            this.var_591.Hide();
            var_2.am_PaperDollHolder.visible = false;
         }
         else if(this.var_56 == const_231)
         {
            var_44 = this.method_1367();
            this.method_1879(_loc1_);
            this.method_211();
            this.method_176();
            this.var_98.Hide();
            this.var_591.Hide();
            var_2.am_PaperDollHolder.visible = true;
         }
         else if(this.var_56 == const_68)
         {
            var_44 = this.method_1209();
            this.method_1514(_loc1_);
            this.method_211();
            this.method_176(false);
            this.method_1839();
            this.var_98.Hide();
            this.var_591.Show();
            var_2.am_PaperDollHolder.visible = false;
         }
         else if(this.var_56 == const_242)
         {
            var_44 = this.method_1614();
            this.method_1427(_loc1_);
            this.method_211();
            this.method_176();
            this.var_98.Hide();
            this.var_591.Hide();
            var_2.am_PaperDollHolder.visible = true;
         }
         else if(this.var_56 == const_278)
         {
            this.method_1447(_loc1_);
            this.method_211();
            this.method_176();
            this.var_98.Hide();
            this.var_591.Hide();
            var_2.am_PaperDollHolder.visible = true;
         }
         if(!var_44)
         {
            var_44 = 1;
         }
         if(var_16 >= var_44)
         {
            var_16 = var_44 - 1;
         }
         var_37 = true;
         this.method_1686(_loc1_);
         this.method_1162(_loc1_);
         this.method_404();
         if(this.method_250())
         {
            this.method_170(_loc1_);
         }
      }
      
      public function GetPaperDollType() : String
      {
         var _loc2_:Entity = var_1.clientEnt;
         var _loc3_:EntType = _loc2_.entType;
         var _loc4_:* = (_loc4_ = (_loc4_ = "<EntType EntName=\"PaperDoll\" parent=\"Player:" + _loc3_.entName + "\">") + "<GfxType>") + ("<AnimScale>" + 1.75 + "</AnimScale>");
         if(_loc3_.gfxType.var_522)
         {
            _loc4_ += "<FlipAnim>False</FlipAnim>";
         }
         if(_loc3_.className == "Rogue")
         {
            _loc4_ += "<BaseAnim>Relaxed</BaseAnim>";
         }
         return (_loc4_ += "</GfxType>") + "</EntType>";
      }
      
      public function method_1020() : void
      {
         var _loc2_:MovieClip = null;
         var _loc3_:MovieClip = null;
         var _loc1_:uint = 0;
         while(_loc1_ < const_12)
         {
            _loc2_ = this.var_95[_loc1_].mMovieClip;
            _loc3_ = _loc2_.am_GearIconHolder.am_Button;
            method_14(_loc3_);
            this.method_116(_loc2_);
            _loc2_.am_GearIconHolder.visible = true;
            _loc1_++;
         }
      }
      
      public function method_1480() : uint
      {
         return Math.ceil(var_1.mFilteredOwnedGear.length / const_10);
      }
      
      public function method_1382() : uint
      {
         return Math.ceil(this.var_654.length / const_10);
      }
      
      public function method_1614() : uint
      {
         var _loc2_:class_20 = null;
         var _loc1_:uint = 0;
         for each(_loc2_ in var_1.mOwnedMounts)
         {
            _loc1_++;
         }
         return Math.ceil(_loc1_ / const_10);
      }
      
      public function method_1209() : uint
      {
         var _loc2_:class_87 = null;
         var _loc1_:uint = 0;
         for each(_loc2_ in var_1.mEggPetInfo.mOwnedPets)
         {
            _loc1_++;
         }
         return Math.ceil(_loc1_ / const_10);
      }
      
      public function method_1715() : uint
      {
         var _loc2_:class_114 = null;
         var _loc1_:uint = 0;
         for each(_loc2_ in var_1.mOwnedCharms)
         {
            _loc1_++;
         }
         return Math.ceil(_loc1_ / const_10);
      }
      
      public function method_1367() : uint
      {
         var _loc2_:class_76 = null;
         var _loc1_:uint = 0;
         for each(_loc2_ in var_1.mOwnedMaterials)
         {
            _loc1_++;
         }
         return Math.ceil(_loc1_ / const_10);
      }
      
      public function method_1032() : Boolean
      {
         return this.var_56 == const_120 && Boolean(mbVisible);
      }
      
      public function method_203(param1:MouseEvent, param2:uint) : void
      {
         this.var_73.Toggle(class_150.const_93,param2,true);
         this.method_83(class_150.const_93,param2);
         this.method_624();
         this.method_937();
         this.method_385();
         this.var_73.method_798();
         Refresh();
      }
      
      public function method_519(param1:MouseEvent, param2:uint) : void
      {
         this.var_73.Toggle(class_150.const_88,param2);
         this.method_83(class_150.const_88,param2);
      }
      
      public function method_347(param1:MouseEvent, param2:uint) : void
      {
         this.var_73.Toggle(class_150.const_87,param2);
         this.method_385();
      }
      
      public function method_133(param1:MouseEvent, param2:uint) : void
      {
         this.var_73.Toggle(class_150.const_91,param2);
         this.method_83(class_150.const_91,param2);
      }
      
      public function method_376(param1:MouseEvent, param2:uint) : void
      {
         this.var_73.Toggle(class_150.const_97,param2);
         this.method_83(class_150.const_97,param2);
      }
      
      public function method_462(param1:MouseEvent, param2:uint) : void
      {
         this.var_73.Toggle(class_150.const_81,param2);
         this.method_83(class_150.const_81,param2);
      }
      
      public function method_1019(param1:MouseEvent, param2:uint) : void
      {
         this.var_73.Toggle(class_150.const_44,param2);
         this.method_83(class_150.const_44,param2);
      }
      
      public function method_83(param1:uint, param2:uint) : void
      {
         if(param1 == class_150.const_93)
         {
            this.var_369[param2].mMovieClip.am_CheckMark.visible = this.var_73.method_178(class_150.const_93,param2);
         }
         if(param1 == class_150.const_88)
         {
            this.var_648[param2].mMovieClip.am_CheckMark.visible = this.var_73.method_178(class_150.const_88,param2);
         }
         if(param1 == class_150.const_87)
         {
            this.var_542[param2].mMovieClip.am_CheckMark.visible = this.var_73.method_178(class_150.const_87,param2);
         }
         if(param1 == class_150.const_91)
         {
            this.var_260[param2].mMovieClip.am_CheckMark.visible = this.var_73.method_178(class_150.const_91,param2);
         }
         if(param1 == class_150.const_97)
         {
            this.var_583[param2].mMovieClip.am_CheckMark.visible = this.var_73.method_178(class_150.const_97,param2);
         }
         if(param1 == class_150.const_81)
         {
            this.var_622[param2].mMovieClip.am_CheckMark.visible = this.var_73.method_178(class_150.const_81,param2);
         }
         if(param1 == class_150.const_44)
         {
            this.var_297[param2].mMovieClip.am_CheckMark.visible = this.var_73.method_178(class_150.const_44,param2);
         }
      }
      
      public function method_385() : void
      {
         var _loc1_:uint = 0;
         _loc1_ = 1;
         while(_loc1_ < this.var_369.length)
         {
            this.method_83(class_150.const_93,_loc1_);
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_648.length)
         {
            this.method_83(class_150.const_88,_loc1_);
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_542.length)
         {
            this.method_83(class_150.const_87,_loc1_);
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_260.length)
         {
            this.method_83(class_150.const_91,_loc1_);
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_583.length)
         {
            this.method_83(class_150.const_97,_loc1_);
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_622.length)
         {
            this.method_83(class_150.const_81,_loc1_);
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_297.length)
         {
            this.method_83(class_150.const_44,_loc1_);
            _loc1_++;
         }
      }
      
      public function method_624() : void
      {
         var _loc1_:Vector.<PowerType> = null;
         if(this.var_73.method_1047())
         {
            MathUtil.method_8(this.var_215.mMovieClip.am_RuneText1,"Ability Rune",const_11);
            this.var_1054.Show();
            this.var_1885.Show();
            _loc1_ = this.var_73.method_1051();
            method_12(this.mFilterPanelAbilityIconHolder0.mMovieClip,!!_loc1_[0] ? _loc1_[0].iconName : "");
            method_12(this.mFilterPanelAbilityIconHolder1.mMovieClip,!!_loc1_[1] ? _loc1_[1].iconName : "");
            method_12(this.mFilterPanelAbilityIconHolder2.mMovieClip,!!_loc1_[2] ? _loc1_[2].iconName : "");
         }
         else
         {
            MathUtil.method_8(this.var_215.mMovieClip.am_RuneText1,"Ability Rune",const_9);
            this.var_1054.Hide();
            this.var_73.method_1234();
            this.var_1885.Hide();
         }
      }
      
      public function method_937() : void
      {
         if(this.var_73.method_1096())
         {
            this.var_1768.Show();
            MathUtil.method_8(this.var_215.mMovieClip.am_RuneText2,"Effect Rune",const_11);
            this.var_1917.Show();
            this.method_394();
         }
         else
         {
            this.var_73.method_1930();
            this.var_1768.Hide();
            MathUtil.method_8(this.var_215.mMovieClip.am_RuneText2,"Effect Rune",const_9);
            this.var_1917.Hide();
         }
      }
      
      public function method_394() : void
      {
         var _loc4_:MovieClip = null;
         var _loc1_:Dictionary = this.var_73.method_1244();
         var _loc2_:Vector.<PowerType> = this.var_73.method_394();
         var _loc3_:uint = 0;
         while(_loc3_ < const_155)
         {
            if(_loc3_ >= _loc2_.length)
            {
               this.var_721[_loc3_].Hide();
               this.var_297[_loc3_].Hide();
            }
            else
            {
               this.var_721[_loc3_].Show();
               _loc4_ = this.var_721[_loc3_].mMovieClip.am_RuneHolder;
               method_12(_loc4_,_loc2_[_loc3_].runeIcon);
               this.var_297[_loc3_].Show();
               if(!_loc1_[_loc2_[_loc3_].powerName])
               {
                  this.var_297[_loc3_].DisableButton("sdfsd");
                  this.var_297[_loc3_].Hide();
                  this.var_73.method_1919(_loc3_);
                  _loc4_.filters = [MathUtil.method_1884(0.2)];
               }
               else
               {
                  this.var_297[_loc3_].EnableButton();
                  this.var_297[_loc3_].Show();
                  _loc4_.filters = this.var_2298;
               }
            }
            _loc3_++;
         }
      }
      
      public function method_196(param1:MouseEvent, param2:uint) : void
      {
         this.method_169(class_150.const_93,param2);
      }
      
      public function method_473(param1:MouseEvent, param2:uint) : void
      {
         this.method_169(class_150.const_88,param2);
      }
      
      public function method_281(param1:MouseEvent, param2:uint) : void
      {
         this.method_169(class_150.const_87,param2);
      }
      
      public function method_137(param1:MouseEvent, param2:uint) : void
      {
         this.method_169(class_150.const_91,param2);
      }
      
      public function method_308(param1:MouseEvent, param2:uint) : void
      {
         this.method_169(class_150.const_97,param2);
      }
      
      public function method_437(param1:MouseEvent, param2:uint) : void
      {
         this.method_169(class_150.const_81,param2);
      }
      
      public function method_1735(param1:MouseEvent, param2:uint) : void
      {
         this.method_169(class_150.const_44,param2);
      }
      
      public function method_169(param1:uint, param2:uint) : void
      {
         var _loc3_:String = this.var_73.method_888(param1,param2);
         var _loc4_:String = this.var_73.method_635(param1,param2);
         MathUtil.method_2(this.var_754.mMovieClip.am_Text,_loc3_);
         MathUtil.method_2(this.var_215.mMovieClip.am_Description,_loc4_);
         this.var_754.mMovieClip.y = this.method_1216(param1);
         this.var_754.Show();
      }
      
      public function method_39(param1:MouseEvent, param2:uint) : void
      {
         this.var_754.Hide();
      }
      
      private function method_1216(param1:uint) : Number
      {
         var _loc2_:Number = NaN;
         var _loc3_:MovieClip = this.var_215.mMovieClip;
         if(param1 == class_150.const_93)
         {
            _loc2_ = Number(_loc3_.am_SlotList.y);
         }
         if(param1 == class_150.const_88)
         {
            _loc2_ = Number(_loc3_.am_RarityList.y);
         }
         if(param1 == class_150.const_87)
         {
            _loc2_ = Number(_loc3_.am_StatList.y);
         }
         if(param1 == class_150.const_91)
         {
            _loc2_ = Number(_loc3_.am_CharmList.y);
         }
         if(param1 == class_150.const_97)
         {
            _loc2_ = Number(_loc3_.am_BonusList.y);
         }
         if(param1 == class_150.const_81)
         {
            _loc2_ = Number(_loc3_.am_AbilityList.y);
         }
         if(param1 == class_150.const_44)
         {
            _loc2_ = Number(_loc3_.am_RuneList.y);
         }
         return _loc2_;
      }
      
      private function method_211() : void
      {
         this.var_73.method_119();
         this.method_385();
         this.var_215.Hide();
      }
      
      private function method_221(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = null;
         var _loc4_:Vector.<class_114> = null;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc8_:class_42 = null;
         var _loc9_:class_64 = null;
         if(param1.ctrlKey)
         {
            _loc3_ = var_1.clientEnt;
            if(!_loc3_)
            {
               return;
            }
            _loc4_ = this.method_214(_loc3_);
            _loc5_ = uint(this.method_174(param2));
            _loc6_ = param2 % 3;
            _loc7_ = _loc3_.mEquipGear[_loc5_];
            if(_loc8_ = var_1.mOwnedGear[_loc7_])
            {
               if(_loc6_ == 0)
               {
                  _loc9_ = _loc8_.var_189;
               }
               if(_loc6_ == 1)
               {
                  _loc9_ = _loc8_.var_196;
               }
               if(_loc6_ == 2)
               {
                  _loc9_ = _loc8_.var_187;
               }
            }
            if(_loc9_)
            {
               this.LinkCharmInChat(0,_loc9_);
            }
         }
         else
         {
            this.method_1136(param2);
            this.method_166();
         }
      }
      
      private function method_230(param1:MouseEvent, param2:uint) : void
      {
         var _loc8_:class_64 = null;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:uint = uint(this.method_174(param2));
         var _loc5_:uint = param2 % 3;
         var _loc6_:uint = _loc3_.mEquipGear[_loc4_];
         var _loc7_:class_42;
         if(_loc7_ = var_1.mOwnedGear[_loc6_])
         {
            if(_loc5_ == 0)
            {
               _loc8_ = _loc7_.var_189;
            }
            if(_loc5_ == 1)
            {
               _loc8_ = _loc7_.var_196;
            }
            if(_loc5_ == 2)
            {
               _loc8_ = _loc7_.var_187;
            }
            if(_loc8_)
            {
               var_1.screenHudTooltip.ShowCharmTooltip(_loc8_,369.25,364.05);
            }
         }
      }
      
      private function method_183(param1:MouseEvent, param2:uint) : void
      {
         var_1.screenHudTooltip.mCharmTooltip.Hide();
      }
      
      private function method_1123() : void
      {
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:String = null;
         var _loc7_:uint = 0;
         var _loc9_:uint = 0;
         var _loc10_:class_42 = null;
         var _loc11_:class_64 = null;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:Boolean = false;
         var _loc3_:uint = 0;
         while(_loc3_ < const_27 * 6)
         {
            _loc4_ = uint(this.method_174(_loc3_));
            _loc5_ = uint(this.method_1345(_loc4_));
            _loc6_ = this.method_491(_loc3_);
            _loc7_ = _loc3_ % 3;
            _loc9_ = _loc1_.mEquipGear[_loc4_];
            if(_loc10_ = var_1.mOwnedGear[_loc9_])
            {
               _loc11_ = null;
               if(_loc7_ == 0)
               {
                  _loc11_ = _loc10_.var_189;
               }
               else if(_loc7_ == 1)
               {
                  _loc11_ = _loc10_.var_196;
               }
               else if(_loc7_ == 2)
               {
                  _loc11_ = _loc10_.var_187;
               }
               if(_loc11_)
               {
                  _loc11_.method_78(this,this.var_98.mMovieClip[_loc6_]["am_Charm" + _loc7_].am_IconHolder);
               }
               else
               {
                  method_14(this.var_98.mMovieClip[_loc6_]["am_Charm" + _loc7_].am_IconHolder);
               }
               this.var_405[_loc4_].Show();
               this.var_762[_loc5_].Show();
               _loc2_ = true;
            }
            else
            {
               this.var_405[_loc4_].Hide();
               this.var_762[_loc5_].Hide();
               if(this.var_200 == _loc3_)
               {
                  this.var_200 = -1;
                  this.method_166();
               }
            }
            _loc3_++;
         }
         if(!_loc2_)
         {
            this.var_98.mMovieClip.am_NoGearMessage.visible = true;
         }
         else
         {
            this.var_98.mMovieClip.am_NoGearMessage.visible = false;
         }
      }
      
      private function method_1839() : void
      {
         var _loc3_:class_87 = null;
         var _loc4_:class_33 = null;
         var _loc5_:MovieClip = null;
         var _loc6_:Bitmap = null;
         var _loc7_:MovieClip = null;
         var _loc10_:MovieClip = null;
         var _loc11_:String = null;
         var _loc12_:String = null;
         var _loc13_:int = 0;
         var _loc14_:int = 0;
         var _loc15_:String = null;
         var _loc16_:* = false;
         var _loc17_:Boolean = false;
         var _loc18_:class_103 = null;
         var _loc19_:Number = NaN;
         var _loc1_:class_81 = var_1.mEggPetInfo;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:* = false;
         var _loc8_:Number = Number(var_1.main.overallScale);
         var _loc9_:uint = 0;
         while(_loc9_ < const_397)
         {
            _loc4_ = this.var_281[_loc9_];
            _loc5_ = this.var_1291[_loc9_].mMovieClip;
            _loc2_ = _loc9_ == 0;
            _loc7_ = _loc5_.am_ItemIconHolder;
            method_14(_loc7_);
            _loc3_ = _loc2_ ? _loc1_.mActivePet : _loc1_.mRestingPetList[_loc9_ - 1];
            if(!_loc3_)
            {
               _loc10_ = _loc4_.mMovieClip;
               MathUtil.method_2(_loc10_.am_Name,"");
               MathUtil.method_2(_loc10_.am_Passive,"");
               MathUtil.method_2(_loc10_.am_XPText,"");
               _loc5_.am_Star.visible = false;
               MathUtil.method_2(_loc5_.am_Level,"");
               this.var_1614[_loc9_].Show();
               if(_loc9_ == 0)
               {
                  this.var_1012.Hide();
                  this.var_1493.Hide();
                  _loc10_.am_TrainingText.visible = false;
                  this.var_1347.Hide();
               }
            }
            else
            {
               MathUtil.method_2(_loc4_.mMovieClip.am_Name,_loc3_.mPetType.displayName);
               _loc11_ = _loc3_.method_518(_loc2_);
               if(_loc12_ = _loc3_.method_938(_loc2_))
               {
                  _loc11_ += ", " + _loc12_;
               }
               MathUtil.method_2(_loc4_.mMovieClip.am_Passive,_loc11_);
               _loc13_ = int(_loc3_.var_110);
               _loc14_ = int(class_7.method_154(_loc3_.var_23));
               _loc15_ = "";
               if(_loc3_.var_23 != class_7.const_35)
               {
                  _loc15_ = " / " + MathUtil.method_29(_loc14_);
               }
               if(_loc3_.var_110 < _loc14_)
               {
                  MathUtil.method_2(_loc4_.mMovieClip.am_XPText,MathUtil.method_29(_loc3_.var_110) + _loc15_);
               }
               else
               {
                  MathUtil.method_2(_loc4_.mMovieClip.am_XPText,"<font color=\'#00CCFF\'>" + MathUtil.method_29(_loc3_.var_110) + "</font>" + _loc15_,true);
               }
               this.var_1614[_loc9_].Hide();
               if(_loc16_ = _loc3_.var_23 == class_7.const_35)
               {
                  if(_loc2_)
                  {
                     _loc5_.am_Star.visible = false;
                  }
                  else
                  {
                     _loc5_.am_Star.visible = true;
                  }
                  _loc5_.am_Level.visible = false;
               }
               else
               {
                  _loc5_.am_Star.visible = false;
                  _loc5_.am_Level.visible = true;
                  MathUtil.method_2(_loc5_.am_Level,String(_loc3_.var_23));
               }
               _loc6_ = class_41.method_85(_loc3_.mPetType,2,2,54,54,_loc8_);
               _loc7_.addChild(_loc6_);
               if(_loc9_ == 0)
               {
                  if(_loc16_)
                  {
                     this.var_1012.Hide();
                     this.var_1493.Show();
                     _loc4_.mMovieClip.am_XPText.visible = false;
                     _loc4_.mMovieClip.am_TrainingText.visible = false;
                  }
                  else
                  {
                     _loc19_ = _loc3_.method_324();
                     this.var_1012.Show();
                     this.var_1012.BeginHealthMode("Progress",0);
                     this.var_1012.mHealthPerc = _loc19_;
                     this.var_1493.Hide();
                     if(_loc19_ >= 1)
                     {
                        _loc4_.mMovieClip.am_TrainingText.visible = true;
                     }
                     else
                     {
                        _loc4_.mMovieClip.am_TrainingText.visible = false;
                     }
                     _loc4_.mMovieClip.am_XPText.visible = false;
                  }
                  _loc17_ = false;
                  for each(_loc18_ in var_1.mOwnedConsumables)
                  {
                     if(_loc18_ && _loc18_.stackCount && _loc18_.consumableType.type == "PetFood")
                     {
                        _loc17_ = true;
                        break;
                     }
                  }
                  if(_loc17_)
                  {
                     this.var_1347.Show();
                  }
                  else
                  {
                     this.var_1347.Hide();
                  }
               }
            }
            _loc9_++;
         }
      }
      
      private function method_2121() : void
      {
         var _loc2_:uint = 0;
         var _loc3_:String = null;
         var _loc4_:uint = 0;
         var _loc1_:uint = 0;
         while(_loc1_ < const_27 * 6)
         {
            _loc2_ = uint(this.method_174(_loc1_));
            _loc3_ = this.method_491(_loc1_);
            _loc4_ = _loc1_ % 3;
            this.var_98.mMovieClip[_loc3_]["am_Charm" + _loc4_].am_Selector.visible = false;
            _loc1_++;
         }
      }
      
      private function method_174(param1:uint) : int
      {
         var _loc2_:uint = 0;
         if(Math.floor(param1 / 3) == 0)
         {
            _loc2_ = EntType.SWORD_SLOT;
         }
         if(Math.floor(param1 / 3) == 1)
         {
            _loc2_ = EntType.SHIELD_SLOT;
         }
         if(Math.floor(param1 / 3) == 2)
         {
            _loc2_ = EntType.HAT_SLOT;
         }
         if(Math.floor(param1 / 3) == 3)
         {
            _loc2_ = EntType.ARMOR_SLOT;
         }
         if(Math.floor(param1 / 3) == 4)
         {
            _loc2_ = EntType.GLOVES_SLOT;
         }
         if(Math.floor(param1 / 3) == 5)
         {
            _loc2_ = EntType.BOOTS_SLOT;
         }
         return _loc2_;
      }
      
      private function method_1345(param1:uint) : int
      {
         if(param1 == EntType.SWORD_SLOT)
         {
            return 0;
         }
         if(param1 == EntType.SHIELD_SLOT)
         {
            return 1;
         }
         if(param1 == EntType.HAT_SLOT)
         {
            return 2;
         }
         if(param1 == EntType.ARMOR_SLOT)
         {
            return 3;
         }
         if(param1 == EntType.GLOVES_SLOT)
         {
            return 4;
         }
         if(param1 == EntType.BOOTS_SLOT)
         {
            return 5;
         }
         return -1;
      }
      
      private function method_491(param1:uint) : String
      {
         var _loc2_:String = null;
         if(Math.floor(param1 / 3) == 0)
         {
            _loc2_ = "am_Sword";
         }
         if(Math.floor(param1 / 3) == 1)
         {
            _loc2_ = "am_Shield";
         }
         if(Math.floor(param1 / 3) == 2)
         {
            _loc2_ = "am_Hat";
         }
         if(Math.floor(param1 / 3) == 3)
         {
            _loc2_ = "am_Armor";
         }
         if(Math.floor(param1 / 3) == 4)
         {
            _loc2_ = "am_Gloves";
         }
         if(Math.floor(param1 / 3) == 5)
         {
            _loc2_ = "am_Boots";
         }
         return _loc2_;
      }
      
      private function method_166() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:* = false;
         var _loc3_:uint = 0;
         var _loc4_:String = null;
         var _loc5_:uint = 0;
         var _loc6_:MovieClip = null;
         var _loc7_:MovieClip = null;
         _loc1_ = 0;
         while(_loc1_ < const_27 * 6)
         {
            _loc3_ = uint(this.method_174(_loc1_));
            _loc4_ = this.method_491(_loc1_);
            _loc5_ = _loc1_ % 3;
            _loc2_ = _loc1_ == this.var_200;
            this.var_98.mMovieClip[_loc4_]["am_Charm" + _loc5_].am_Selector.visible = _loc2_;
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < const_12)
         {
            _loc7_ = (_loc6_ = this.var_95[_loc1_].mMovieClip).am_CharmIconHolder;
            _loc2_ = _loc1_ == this.var_570;
            _loc6_.am_Selector.visible = _loc2_;
            _loc1_++;
         }
      }
      
      public function method_176(param1:Boolean = true) : void
      {
         var _loc2_:uint = 0;
         if(this.var_56 != const_86 && this.var_1863)
         {
            _loc2_ = 0;
            while(_loc2_ < const_134)
            {
               if(this.var_762[_loc2_].mbVisible)
               {
                  this.var_762[_loc2_].PlayAnimation("FadeOut");
               }
               _loc2_++;
            }
            this.var_1863 = false;
         }
         if(param1)
         {
            this.var_200 = -1;
            this.var_570 = -1;
         }
         this.method_166();
      }
      
      private function method_1136(param1:uint) : void
      {
         var _loc8_:class_64 = null;
         var _loc9_:uint = 0;
         var _loc10_:class_114 = null;
         var _loc11_:class_64 = null;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:Vector.<class_114> = this.method_214(_loc2_);
         if(this.var_570 >= _loc3_.length)
         {
            return;
         }
         var _loc4_:uint = uint(this.method_174(param1));
         var _loc5_:uint = param1 % 3;
         var _loc6_:uint = _loc2_.mEquipGear[_loc4_];
         var _loc7_:class_42 = var_1.mOwnedGear[_loc6_];
         if(this.var_570 > -1)
         {
            if(_loc7_)
            {
               if(_loc5_ == 0)
               {
                  _loc8_ = _loc7_.var_189;
               }
               if(_loc5_ == 1)
               {
                  _loc8_ = _loc7_.var_196;
               }
               if(_loc5_ == 2)
               {
                  _loc8_ = _loc7_.var_187;
               }
               _loc9_ = this.var_570 + var_16 * const_12;
               if(_loc10_ = _loc3_[_loc9_])
               {
                  _loc11_ = _loc10_.charmData;
                  if(_loc8_)
                  {
                     var_1.screenReplace.Display(_loc11_,_loc6_,_loc5_ + 1,_loc8_);
                  }
                  else if(!_loc11_.method_379())
                  {
                     var_1.screenSocket.Display(_loc11_,_loc6_,_loc5_ + 1);
                  }
                  else
                  {
                     var_1.screenChat.ReceiveChat(var_1.clientEntID,"^t" + "Not a Valid Target for Charm Remover");
                  }
               }
            }
         }
         else if(_loc7_)
         {
            if(this.var_200 == param1)
            {
               this.var_200 = -1;
            }
            else
            {
               this.var_200 = param1;
            }
         }
      }
      
      private function method_1698(param1:uint) : void
      {
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc8_:class_42 = null;
         var _loc9_:class_64 = null;
         var _loc10_:class_114 = null;
         var _loc11_:class_64 = null;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:Vector.<class_114> = this.method_214(_loc2_);
         var _loc4_:uint;
         if((_loc4_ = param1 + const_12 * var_16) >= _loc3_.length)
         {
            return;
         }
         if(this.var_200 > -1)
         {
            _loc5_ = uint(this.method_174(this.var_200));
            _loc6_ = this.var_200 % 3;
            _loc7_ = _loc2_.mEquipGear[_loc5_];
            if(_loc8_ = var_1.mOwnedGear[_loc7_])
            {
               if(_loc6_ == 0)
               {
                  _loc9_ = _loc8_.var_189;
               }
               if(_loc6_ == 1)
               {
                  _loc9_ = _loc8_.var_196;
               }
               if(_loc6_ == 2)
               {
                  _loc9_ = _loc8_.var_187;
               }
               _loc11_ = (_loc10_ = _loc3_[_loc4_]).charmData;
               if(_loc10_)
               {
                  if(_loc9_)
                  {
                     var_1.screenReplace.Display(_loc11_,_loc7_,_loc6_ + 1,_loc9_);
                  }
                  else if(!_loc11_.method_379())
                  {
                     var_1.screenSocket.Display(_loc11_,_loc7_,_loc6_ + 1);
                  }
                  else
                  {
                     var_1.screenChat.ReadUnsafeStatusText("Not a Valid Target for Charm Remover");
                  }
               }
            }
         }
         else if(this.var_570 == param1)
         {
            this.var_570 = -1;
         }
         else
         {
            this.var_570 = param1;
         }
      }
      
      private function method_1743(param1:uint) : void
      {
         var _loc2_:Packet = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(param1 < var_1.mGearsetList.length)
         {
            _loc2_ = new Packet(LinkUpdater.const_893);
            _loc2_.method_20(GearType.const_348,param1);
            var_1.serverConn.SendPacket(_loc2_);
         }
      }
      
      private function method_1955(param1:uint) : void
      {
         var _loc2_:Vector.<Vector.<uint>> = null;
         var _loc3_:Vector.<String> = null;
         var _loc4_:Vector.<uint> = null;
         var _loc5_:uint = 0;
         var _loc6_:String = null;
         var _loc7_:Packet = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         _loc2_ = var_1.mGearsetList;
         _loc3_ = var_1.mGearsetListName;
         if(param1 < Game.const_1057 && param1 == _loc2_.length)
         {
            _loc4_ = new Vector.<uint>(EntType.MAX_SLOTS);
            _loc2_.push(_loc4_);
            _loc5_ = uint(param1 + 1);
            _loc6_ = "GearSet " + _loc5_;
            _loc3_.push(_loc6_);
            this.var_80 = param1;
            this.method_608();
            (_loc7_ = new Packet(LinkUpdater.const_843)).method_20(GearType.const_348,param1);
            var_1.serverConn.SendPacket(_loc7_);
            this.var_455.Show();
            this.var_413.Hide();
         }
      }
      
      private function method_1247(param1:uint, param2:String) : void
      {
         var _loc3_:Packet = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(param1 < var_1.mGearsetList.length)
         {
            _loc3_ = new Packet(LinkUpdater.const_976);
            _loc3_.method_20(GearType.const_348,param1);
            _loc3_.method_26(param2);
            var_1.serverConn.SendPacket(_loc3_);
         }
      }
      
      private function method_844() : void
      {
         if(this.var_529 && this.var_311.mMovieClip.am_NameField.stage && this.var_311.mMovieClip.am_NameField.stage.focus != this.var_311.mMovieClip.am_NameField)
         {
            this.var_311.mMovieClip.am_NameField.stage.focus = this.var_311.mMovieClip.am_NameField;
         }
      }
      
      override public function Hide() : void
      {
         if(this.var_529)
         {
            this.var_529 = false;
            this.method_151();
         }
         var_1.screenSocket.Hide();
         var_1.screenFeedPet.Hide();
         var_1.screenReplace.Hide();
         super.Hide();
      }
      
      public function method_54(param1:int) : Boolean
      {
         if(var_1.screenKeybind.mbVisible)
         {
            return false;
         }
         this.method_844();
         if(this.var_529)
         {
            switch(param1)
            {
               case Game.const_240:
                  this.method_151();
                  return true;
               case Game.const_570:
                  this.method_575();
                  this.method_151();
                  return true;
            }
         }
         return this.var_529;
      }
      
      public function method_1651(param1:MouseEvent) : void
      {
         this.method_151();
      }
      
      public function method_151() : void
      {
         this.var_529 = false;
         this.var_311.Hide();
      }
      
      public function method_564() : void
      {
         if(this.var_80 == -1)
         {
            this.var_1824.Hide();
            this.var_455.Hide();
            this.var_413.Hide();
            this.var_1892.Hide();
         }
         else
         {
            this.var_1824.Show();
            this.var_455.Show();
            this.var_413.Show();
            this.var_1892.Show();
         }
      }
      
      private function method_250() : Boolean
      {
         return Boolean(this.var_148.mMovieClip.am_Panel.am_StatisticsGroup.visible) || Boolean(this.var_148.mMovieClip.am_Panel.am_ElementsGroup.visible);
      }
      
      public function method_1904(param1:Entity, param2:Vector.<uint>) : Boolean
      {
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         _loc3_ = 1;
         while(_loc3_ < EntType.MAX_SLOTS)
         {
            _loc4_ = param1.mEquipGear[_loc3_];
            if((_loc5_ = param2[_loc3_]) != _loc4_)
            {
               return true;
            }
            _loc3_++;
         }
         return false;
      }
      
      public function method_601() : void
      {
         this.var_56 = const_120;
      }
      
      public function method_2063() : void
      {
         var _loc1_:class_33 = null;
         if(!this.var_472)
         {
            return;
         }
         for each(_loc1_ in this.var_472)
         {
            MathUtil.method_2(_loc1_.mMovieClip.am_SlideOutName,"");
         }
         this.var_80 = -1;
      }
      
      private function method_1290(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:class_87 = null;
         if(param1.ctrlKey)
         {
            if(param2 > 0)
            {
               _loc3_ = var_1.mEggPetInfo.mRestingPetList[param2 - 1];
            }
            else if(param2 == 0)
            {
               _loc3_ = var_1.mEggPetInfo.mActivePet;
            }
            if(_loc3_)
            {
               this.LinkPetInChat(0,_loc3_);
            }
            return;
         }
         this.method_1601(param2);
         this.method_140();
      }
      
      private function method_1724(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:class_87 = null;
         var _loc4_:Number = NaN;
         _loc3_ = param2 == 0 ? var_1.mEggPetInfo.mActivePet : var_1.mEggPetInfo.mRestingPetList[param2 - 1];
         if(_loc3_)
         {
            if(param2 == 0)
            {
               _loc4_ = _loc3_.method_324();
               if(_loc3_.var_23 == class_7.const_35)
               {
                  this.var_281[param2].mMovieClip.am_XPText.visible = false;
               }
               else
               {
                  this.var_281[param2].mMovieClip.am_XPText.visible = true;
               }
            }
            var_1.screenHudTooltip.ShowPetTooltip(_loc3_,false,253.75,381.2);
         }
      }
      
      private function method_1601(param1:uint) : void
      {
         this.var_200 = param1;
         this.method_140();
      }
      
      private function method_140() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:MovieClip = null;
         var _loc3_:MovieClip = null;
         _loc1_ = 0;
         while(_loc1_ < const_397)
         {
            if(_loc1_ == this.var_200)
            {
               this.var_1359[_loc1_].Show();
            }
            else
            {
               this.var_1359[_loc1_].Hide();
            }
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < const_12)
         {
            _loc2_ = this.var_95[_loc1_].mMovieClip;
            _loc3_ = _loc2_.am_CharmIconHolder;
            _loc2_.am_Selector.visible = false;
            _loc1_++;
         }
      }
      
      private function method_1665(param1:class_87, param2:uint) : void
      {
         var _loc3_:Entity = null;
         var _loc4_:Boolean = false;
         var _loc5_:Vector.<class_87> = null;
         var _loc6_:int = 0;
         var _loc7_:class_87 = null;
         var _loc8_:int = 0;
         var _loc9_:uint = 0;
         _loc3_ = var_1.clientEnt;
         if(!_loc3_ || !var_1.CanSendPacket())
         {
            return;
         }
         if(var_1.mEggPetInfo.mTrainingPet == param1)
         {
            return;
         }
         _loc4_ = false;
         if(param1)
         {
            _loc5_ = var_1.mEggPetInfo.mRestingPetList;
            _loc6_ = -1;
            _loc7_ = null;
            if(var_1.mEggPetInfo.mActivePet == param1)
            {
               _loc6_ = 0;
            }
            else if((_loc6_ = _loc5_.indexOf(param1)) >= 0)
            {
               _loc6_++;
            }
            if(this.var_200 == 0)
            {
               if((_loc8_ = _loc5_.indexOf(param1)) >= 0)
               {
                  _loc5_[_loc8_] = null;
               }
               _loc7_ = var_1.mEggPetInfo.mActivePet;
               this.method_533(param1);
            }
            else
            {
               if(var_1.mEggPetInfo.mActivePet == param1)
               {
                  this.method_533(null);
               }
               _loc9_ = uint(this.var_200 - 1);
               _loc7_ = _loc5_[_loc9_];
               if((_loc8_ = _loc5_.indexOf(param1)) >= 0)
               {
                  _loc5_[_loc8_] = null;
               }
               this.ChangeRestingPets(_loc9_,param1);
            }
            if(var_1.mEggPetInfo.mTrainingPet == _loc7_)
            {
               _loc7_ = null;
            }
            if(Boolean(_loc7_) && _loc7_ != param1)
            {
               if(_loc6_ == 0)
               {
                  this.method_533(_loc7_);
               }
               else if(_loc6_ > 0)
               {
                  this.ChangeRestingPets(_loc6_ - 1,_loc7_);
               }
            }
            if(SoundConfig.var_199)
            {
               SoundManager.Play(SoundConfig.var_199);
            }
            var_1.mEggPetInfo.SendPetInfoToServer();
            if(_loc7_ != param1 && this.var_1991 != param1)
            {
               this.var_1991 = param1;
               this.method_1882(param1,param2,this.var_200);
               _loc4_ = true;
            }
            var_1.screenHudTooltip.ShowPetTooltip(param1,false,253.75,381.2);
         }
         if(!_loc4_)
         {
            Refresh();
            this.method_140();
         }
      }
      
      override internal function PageLeft(param1:MouseEvent) : void
      {
         if(var_16)
         {
            --var_16;
            this.var_570 = -1;
            if(this.var_56 == const_86)
            {
               this.method_166();
            }
            else if(this.var_56 == const_68)
            {
               this.method_140();
            }
            Refresh();
         }
      }
      
      override internal function PageRight(param1:MouseEvent) : void
      {
         if(var_16 < var_44 - 1)
         {
            ++var_16;
            this.var_570 = -1;
            if(this.var_56 == const_86)
            {
               this.method_166();
            }
            else if(this.var_56 == const_68)
            {
               this.method_140();
            }
            Refresh();
         }
      }
      
      public function method_1562() : Boolean
      {
         return this.var_56 == const_68;
      }
      
      private function method_1882(param1:class_87, param2:int, param3:int) : void
      {
         var _loc4_:MovieClip = null;
         var _loc5_:Rectangle = null;
         var _loc6_:MovieClip = null;
         (_loc4_ = new MovieClip()).addChild(class_41.method_85(param1.mPetType,4,4,54,54,var_1.main.overallScale));
         _loc5_ = this.var_95[param2].mMovieClip.getBounds(mWindow.mMovieClip);
         _loc6_ = this.var_1291[param3].mMovieClip;
         method_201(_loc4_,_loc5_.x,_loc5_.y,_loc6_,250,class_137.method_113,this.method_1835);
      }
      
      private function method_1835() : void
      {
         Refresh();
         this.method_140();
         this.var_1991 = null;
      }
      
      private function method_1243(param1:class_3, param2:int) : void
      {
         var _loc3_:MovieClip = null;
         var _loc4_:Rectangle = null;
         var _loc5_:MovieClip = null;
         _loc3_ = new MovieClip();
         method_12(_loc3_,param1.iconName);
         _loc4_ = this.var_95[param2].mMovieClip.getBounds(mWindow.mMovieClip);
         _loc5_ = var_1.screenHudTopRight.mPotionContainer.mMovieClip;
         method_201(_loc3_,_loc4_.x,_loc4_.y,_loc5_,250,class_137.method_113,this.method_1211);
      }
      
      private function method_1211() : void
      {
         Refresh();
         this.var_1965 = null;
         var_1.screenHudTopRight.Refresh();
      }
      
      private function method_43(param1:Number, param2:Number, param3:Boolean = false) : String
      {
         var _loc4_:String = null;
         var _loc5_:String = null;
         _loc4_ = "";
         _loc5_ = "";
         if(param3)
         {
            _loc4_ = "+";
            _loc5_ = "%";
         }
         if(param1 > param2)
         {
            return "<font color=\"#FF0000\">" + _loc4_ + param2 + _loc5_ + "</font>";
         }
         if(param1 < param2)
         {
            return "<font color=\"#00FF00\">" + _loc4_ + param2 + _loc5_ + "</font>";
         }
         return _loc4_ + param2.toString() + _loc5_;
      }
      
      public function method_533(param1:class_87) : void
      {
         var_1.clientEnt.ChangePet(param1);
         var_1.mEggPetInfo.SetActivePetData(param1);
         if(var_1.screenArmory.mPaperDoll)
         {
            var_1.screenArmory.mPaperDoll.ChangePet(param1);
         }
      }
      
      public function ChangeRestingPets(param1:uint, param2:class_87) : void
      {
         var_1.clientEnt.ChangeRestingPets(param1,param2);
         var_1.mEggPetInfo.SetRestingPetData(param2,param1);
         if(var_1.screenArmory.mPaperDoll)
         {
            var_1.screenArmory.mPaperDoll.ChangeRestingPets(param1,param2);
         }
      }
      
      private function method_1111() : void
      {
         var _loc1_:MovieClip = null;
         var _loc2_:uint = 0;
         this.var_726 = new Dictionary();
         _loc1_ = var_2.am_TreasureMap;
         this.var_466 = method_1(_loc1_);
         this.var_2284 = method_1(_loc1_.am_IconsMage);
         this.var_2409 = method_1(_loc1_.am_IconsPaladin);
         this.var_2408 = method_1(_loc1_.am_IconsRogue);
         this.var_2009 = new Vector.<class_33>(const_375,true);
         this.var_1997 = new Vector.<class_33>(const_375,true);
         this.var_1798 = new Vector.<class_33>(const_375,true);
         _loc2_ = 0;
         while(_loc2_ < const_375)
         {
            this.var_2009[_loc2_] = method_3(_loc1_.am_IconsMage.getChildAt(_loc2_) as MovieClip,_loc2_,null,this.method_426,this.method_457);
            this.var_1997[_loc2_] = method_3(_loc1_.am_IconsPaladin.getChildAt(_loc2_) as MovieClip,_loc2_,null,this.method_426,this.method_457);
            this.var_1798[_loc2_] = method_3(_loc1_.am_IconsRogue.getChildAt(_loc2_) as MovieClip,_loc2_,null,this.method_426,this.method_457);
            _loc2_++;
         }
         this.var_601 = new Dictionary();
         this.var_601["Mage"] = this.var_2284;
         this.var_601["Paladin"] = this.var_2409;
         this.var_601["Rogue"] = this.var_2408;
         this.var_977 = new Dictionary();
         this.var_977["Mage"] = this.var_2009;
         this.var_977["Paladin"] = this.var_1997;
         this.var_977["Rogue"] = this.var_1798;
         method_5(_loc1_.am_CloseTreasureMap,this.method_1154);
         method_5(_loc1_.am_PageRightTreasureMap,this.method_1141);
         method_5(_loc1_.am_PageLeftTreasureMap,this.method_1644);
         this.var_2307 = method_21(_loc1_.am_ProgressGroup.am_Name);
         this.var_2012 = method_17(_loc1_.am_ProgressGroup.am_Progress,"Progress",0);
         this.var_2290 = method_21(this.var_2012.mMovieClip.am_Count);
      }
      
      private function method_1993() : void
      {
         var _loc1_:String = null;
         this.var_466 = null;
         this.var_2284 = null;
         this.var_2409 = null;
         this.var_2408 = null;
         this.var_2009 = null;
         this.var_1997 = null;
         this.var_1798 = null;
         for(_loc1_ in this.var_977)
         {
            delete this.var_977[_loc1_];
         }
         this.var_977 = null;
         for(_loc1_ in this.var_601)
         {
            delete this.var_601[_loc1_];
         }
         this.var_601 = null;
         this.var_2307 = null;
         this.var_2012 = null;
         this.var_2290 = null;
      }
      
      private function method_1154(param1:MouseEvent) : void
      {
         this.var_466.Hide();
         Refresh();
      }
      
      private function method_1141(param1:MouseEvent) : void
      {
         ++this.var_465;
         if(this.var_465 > const_471 - 1)
         {
            this.var_465 = 0;
         }
         this.method_509();
      }
      
      private function method_1644(param1:MouseEvent) : void
      {
         --this.var_465;
         if(this.var_465 < 0)
         {
            this.var_465 = const_471 - 1;
         }
         this.method_509();
      }
      
      private function method_1877() : void
      {
         this.var_466.Show();
         this.method_509();
      }
      
      public function method_509() : void
      {
         var _loc1_:Entity = null;
         var _loc2_:Array = null;
         var _loc3_:String = null;
         var _loc5_:Vector.<GearType> = null;
         var _loc6_:MovieClip = null;
         var _loc7_:String = null;
         var _loc8_:uint = 0;
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc11_:uint = 0;
         var _loc12_:uint = 0;
         var _loc13_:uint = 0;
         var _loc14_:uint = 0;
         var _loc15_:uint = 0;
         var _loc16_:MovieClip = null;
         var _loc17_:GearType = null;
         var _loc19_:class_42 = null;
         var _loc20_:uint = 0;
         var _loc21_:class_33 = null;
         var _loc22_:Boolean = false;
         _loc1_ = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         _loc2_ = var_1.mOwnedGear;
         _loc3_ = _loc1_.entType.className;
         var _loc4_:Dictionary = class_14.gearTypesDict;
         _loc5_ = class_14.var_842[_loc3_ + ":" + this.var_465 + ":" + const_1050];
         for(_loc7_ in this.var_601)
         {
            _loc21_ = this.var_601[_loc7_];
            if(_loc7_ != _loc3_)
            {
               _loc21_.Hide();
            }
            else
            {
               _loc21_.Show();
               _loc6_ = _loc21_.mMovieClip;
            }
         }
         _loc8_ = 0;
         _loc9_ = 0;
         _loc10_ = 0;
         _loc11_ = 0;
         _loc12_ = 0;
         _loc13_ = 0;
         _loc14_ = 0;
         while(_loc14_ < const_875)
         {
            (_loc6_["am_Hat" + _loc14_] as MovieClip).visible = false;
            _loc14_++;
         }
         _loc15_ = 0;
         _loc20_ = _loc5_.length;
         _loc14_ = 0;
         while(_loc14_ < _loc20_)
         {
            if(_loc14_ < _loc20_)
            {
               _loc17_ = _loc5_[_loc14_];
               switch(_loc17_.type)
               {
                  case "Sword":
                     _loc16_ = _loc6_["am_Sword" + _loc8_] as MovieClip;
                     this.var_726["am_Sword" + _loc8_] = _loc17_;
                     _loc8_++;
                     break;
                  case "Shield":
                     _loc16_ = _loc6_["am_Shield" + _loc9_] as MovieClip;
                     this.var_726["am_Shield" + _loc9_] = _loc17_;
                     _loc9_++;
                     break;
                  case "Boots":
                     _loc16_ = _loc6_["am_Boots" + _loc11_] as MovieClip;
                     this.var_726["am_Boots" + _loc11_] = _loc17_;
                     _loc11_++;
                     break;
                  case "Armor":
                     _loc16_ = _loc6_["am_Armor" + _loc12_] as MovieClip;
                     this.var_726["am_Armor" + _loc12_] = _loc17_;
                     _loc12_++;
                     break;
                  case "Gloves":
                     _loc16_ = _loc6_["am_Gloves" + _loc13_] as MovieClip;
                     this.var_726["am_Gloves" + _loc13_] = _loc17_;
                     _loc13_++;
                     break;
                  case "Hat":
                     _loc16_ = _loc6_["am_Hat" + _loc10_] as MovieClip;
                     this.var_726["am_Hat" + _loc10_] = _loc17_;
                     _loc16_.visible = true;
                     _loc10_++;
               }
               _loc19_ = _loc2_[_loc17_.gearID];
               _loc22_ = true;
               if(this.var_2058 == const_857 && Boolean(_loc19_))
               {
                  _loc22_ = false;
               }
               if(this.var_2058 == const_881 && _loc19_ && (_loc19_.gearType.var_8 == "R" || _loc19_.gearType.var_8 == "L"))
               {
                  _loc22_ = false;
               }
               if(this.var_2058 == const_1107 && _loc19_ && _loc19_.gearType.var_8 == "L")
               {
                  _loc22_ = false;
               }
               if(!_loc22_)
               {
                  _loc15_ += this.method_620(_loc1_,_loc19_.gearType,true,_loc16_);
               }
               else
               {
                  _loc15_ += this.method_620(_loc1_,_loc17_,false,_loc16_);
               }
            }
            _loc14_++;
         }
         this.var_2290.SetText(_loc15_ + "/" + _loc20_);
         this.var_2012.mHealthPerc = _loc15_ / _loc20_;
         this.var_2307.SetText(const_38[this.var_465]);
      }
      
      private function method_620(param1:Entity, param2:GearType, param3:Boolean, param4:MovieClip) : uint
      {
         var _loc5_:Sprite = null;
         param4.am_New.visible = false;
         (_loc5_ = method_52(param4.am_GearIcon,var_1.RenderGear(Game.const_404,param2,const_1030,param1)).m_TheDO).x = param2.var_2580;
         _loc5_.y = param2.var_2787;
         if(param3)
         {
            _loc5_.alpha = const_1098;
            _loc5_.filters = [];
            return 1;
         }
         _loc5_.alpha = const_1034;
         _loc5_.filters = [const_1292];
         return 0;
      }
      
      private function method_426(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = null;
         var _loc4_:String = null;
         var _loc5_:MovieClip = null;
         var _loc6_:String = null;
         var _loc14_:String = null;
         var _loc15_:uint = 0;
         var _loc16_:GearType = null;
         var _loc17_:uint = 0;
         var _loc18_:class_42 = null;
         var _loc19_:Boolean = false;
         var _loc20_:String = null;
         var _loc21_:uint = 0;
         var _loc22_:uint = 0;
         var _loc23_:uint = 0;
         var _loc24_:MovieClip = null;
         var _loc25_:GearType = null;
         var _loc26_:GearType = null;
         var _loc27_:GearType = null;
         var _loc28_:GearType = null;
         var _loc29_:String = null;
         var _loc30_:String = null;
         var _loc31_:String = null;
         var _loc32_:class_2 = null;
         _loc3_ = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         _loc4_ = _loc3_.entType.className;
         _loc6_ = (_loc5_ = MovieClip(param1.target)).name;
         var _loc13_:Vector.<GearType> = class_14.var_842[_loc4_ + ":" + this.var_465 + ":" + const_955];
         if(_loc6_.indexOf("am_Sword") > -1)
         {
            _loc14_ = "am_Sword";
         }
         else if(_loc6_.indexOf("am_Shield") > -1)
         {
            _loc14_ = "am_Shield";
         }
         else if(_loc6_.indexOf("am_Boots") > -1)
         {
            _loc14_ = "am_Boots";
         }
         else if(_loc6_.indexOf("am_Armor") > -1)
         {
            _loc14_ = "am_Armor";
         }
         else if(_loc6_.indexOf("am_Gloves") > -1)
         {
            _loc14_ = "am_Gloves";
         }
         else if(_loc6_.indexOf("am_Hat") > -1)
         {
            _loc14_ = "am_Hat";
         }
         _loc15_ = uint(_loc6_.replace(_loc14_,""));
         if(!(_loc16_ = this.var_726[_loc14_ + _loc15_.toString()]))
         {
            return;
         }
         _loc17_ = _loc16_.gearID;
         _loc18_ = var_1.mOwnedGear[_loc17_];
         _loc21_ = const_23;
         _loc22_ = const_22;
         _loc23_ = const_24;
         _loc24_ = var_1.screenHudTooltip.mTreasureMapDetails.mMovieClip;
         _loc25_ = null;
         if(!_loc18_)
         {
            _loc21_ = const_9;
            _loc22_ = const_9;
            _loc23_ = const_9;
            _loc24_.am_CheckBoxLegendary.am_CheckMark.visible = false;
            _loc24_.am_CheckBoxRare.am_CheckMark.visible = false;
            _loc24_.am_CheckBoxMagic.am_CheckMark.visible = false;
         }
         else
         {
            _loc19_ = true;
            if((_loc20_ = (_loc25_ = _loc18_.gearType).var_8) == "L")
            {
               _loc24_.am_CheckBoxLegendary.am_CheckMark.visible = true;
               _loc24_.am_CheckBoxRare.am_CheckMark.visible = true;
               _loc24_.am_CheckBoxMagic.am_CheckMark.visible = true;
            }
            else if(_loc20_ == "R")
            {
               _loc24_.am_CheckBoxLegendary.am_CheckMark.visible = false;
               _loc24_.am_CheckBoxRare.am_CheckMark.visible = true;
               _loc24_.am_CheckBoxMagic.am_CheckMark.visible = true;
               _loc21_ = const_9;
            }
            else if(_loc20_ == "M")
            {
               _loc24_.am_CheckBoxLegendary.am_CheckMark.visible = false;
               _loc24_.am_CheckBoxRare.am_CheckMark.visible = false;
               _loc24_.am_CheckBoxMagic.am_CheckMark.visible = true;
               _loc21_ = const_9;
               _loc22_ = const_9;
            }
         }
         _loc26_ = Game.method_445(_loc17_,"L");
         _loc27_ = Game.method_445(_loc17_,"R");
         _loc28_ = Game.method_445(_loc17_,"M");
         _loc29_ = const_678;
         _loc30_ = const_708;
         if(_loc26_.var_775)
         {
            _loc29_ = "<font color=\'#DA2541\'>" + ScreenArmory.var_21[_loc26_.var_775] + class_127.var_121;
            if(_loc31_ = String(var_22[_loc26_.var_775]))
            {
               if(_loc32_ = class_14.var_430[_loc31_])
               {
                  _loc30_ = String(class_14.var_430[_loc31_].displayName);
               }
            }
         }
         else if(_loc26_.var_106)
         {
            _loc29_ = this.method_1991(_loc26_.var_106);
            if(_loc31_ = String(var_32[_loc26_.var_106 + _loc26_.var_1816]))
            {
               if(_loc32_ = class_14.var_430[_loc31_])
               {
                  _loc30_ = String(class_14.var_430[_loc31_].displayName);
               }
            }
         }
         else
         {
            _loc29_ = "Starter Gear";
            _loc30_ = "Starter Gear";
         }
         if(!_loc19_)
         {
            _loc29_ = const_678;
            _loc30_ = const_708;
         }
         this.method_661(_loc5_,true);
         var_1.screenHudTooltip.ShowBigTooltip(var_1.screenHudTooltip.mTreasureMapDetails);
         MathUtil.method_8(_loc24_.am_NameLegendary,_loc26_.displayName,_loc21_);
         MathUtil.method_8(_loc24_.am_NameRare,_loc27_.displayName,_loc22_);
         MathUtil.method_8(_loc24_.am_NameMagic,_loc28_.displayName,_loc23_);
         MathUtil.method_2(_loc24_.am_MonsterName,"<font color=\'#00CCFF\'>Drops From: " + class_127.var_121 + _loc29_,true);
         MathUtil.method_2(_loc24_.am_DungeonName,"<font color=\'#00CCFF\'>Dungeon: " + class_127.var_121 + _loc30_,true);
      }
      
      private function method_457(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:MovieClip = null;
         _loc3_ = MovieClip(param1.target);
         this.method_661(_loc3_,false);
         var_1.screenHudTooltip.ShowBigTooltip(null);
      }
      
      private function method_1991(param1:String) : String
      {
         if(param1 == "Cyclops")
         {
            return param1;
         }
         if(param1 == "Mummy")
         {
            return "Mummies";
         }
         if(param1 == "RockHulk")
         {
            return "Rock Hulks";
         }
         if(param1 == "Wolf")
         {
            return "Wolves";
         }
         return param1 + "s";
      }
      
      public function method_661(param1:MovieClip, param2:Boolean) : void
      {
         if(!param1)
         {
            return;
         }
         param1.filters = param2 ? [const_1091] : null;
      }
      
      private function method_490(param1:uint) : Boolean
      {
         if(var_16 == 0 && param1 >= const_10 - var_1.mLockboxData.mUniqueLockboxes)
         {
            return true;
         }
         return false;
      }
      
      private function method_1362(param1:MouseEvent) : void
      {
         var _loc2_:Entity = null;
         _loc2_ = var_1.clientEnt;
         if(!_loc2_ || !_loc2_.mEquipPet)
         {
            return;
         }
         var_1.screenFeedPet.Display(_loc2_.mEquipPet);
      }
      
      private function method_1732(param1:Vector.<class_103>) : Vector.<class_103>
      {
         var _loc2_:uint = 0;
         var _loc3_:Vector.<class_103> = null;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:class_3 = null;
         var _loc7_:class_3 = null;
         var _loc8_:uint = 0;
         var _loc9_:uint = 0;
         var _loc10_:int = 0;
         _loc2_ = 7;
         _loc3_ = new Vector.<class_103>();
         if(!param1 || !param1.length)
         {
            return _loc3_;
         }
         _loc5_ = _loc4_ = param1.length;
         _loc7_ = _loc6_ = param1[0].consumableType;
         _loc8_ = 1;
         _loc9_ = 0;
         _loc3_.push(param1[0]);
         _loc10_ = 1;
         while(_loc10_ < _loc5_)
         {
            if(_loc8_ > _loc4_)
            {
               break;
            }
            if(_loc10_ < _loc9_)
            {
               _loc3_.push(null);
            }
            else if((_loc6_ = param1[_loc8_].consumableType).type == _loc7_.type || _loc6_.var_427 == _loc7_.var_427 && _loc6_.var_821 == _loc7_.var_821 || _loc9_ && _loc10_ >= _loc9_)
            {
               _loc3_.push(param1[_loc8_]);
               _loc8_++;
               _loc9_ = 0;
               _loc7_ = _loc6_;
            }
            else
            {
               _loc9_ = (Math.floor(_loc10_ / _loc2_) + 1) * _loc2_;
               _loc5_ += _loc9_ - _loc10_;
               _loc3_.push(null);
            }
            _loc10_++;
         }
         return _loc3_;
      }
   }
}
