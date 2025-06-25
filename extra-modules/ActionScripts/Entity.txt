package
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.media.SoundChannel;
   import flash.text.TextField;
   import flash.text.TextFormat;
   import flash.utils.Dictionary;
   import flash.utils.getTimer;
   
   public class Entity
   {
      
      public static const const_835:uint = 400;
      
      public static const const_836:Number = 60;
      
      public static const const_236:uint = 0;
      
      public static const const_139:uint = 1;
      
      public static const const_309:uint = 2;
      
      public static const const_308:uint = 3;
      
      public static const const_470:uint = 4;
      
      public static const const_172:uint = 3;
      
      public static const const_78:uint = 0;
      
      public static const const_399:uint = 1;
      
      public static const const_467:uint = 2;
      
      public static const const_6:uint = 3;
      
      public static const const_316:uint = 2;
      
      public static const const_1053:uint = 10;
      
      private static const const_1045:Number = 22;
      
      public static const const_461:Number = 10;
      
      private static var gtLevelUpFront:GfxType = new GfxType();
      
      private static var gtLevelUpRear:GfxType = new GfxType();
      
      private static const const_334:GfxType = new GfxType();
      
      public static const const_282:uint = 0;
      
      public static const const_449:uint = 1;
      
      public static const const_599:uint = 2;
      
      public static const const_482:uint = 3;
      
      public static const const_626:int = 6;
      
      private static const const_994:uint = 60000;
      
      public static const const_1230:uint = 12;
      
      public static const const_695:uint = 10;
      
      public static const const_834:uint = 8;
      
      public static const const_796:uint = 6;
      
      public static const const_429:uint = 80;
      
      public static const TIME_MONSTER_LAYS_DEAD_BEFORE_VANISHING:Number = 10000;
      
      public static const MONSTER_FADE_TIME:Number = 500;
      
      public static const const_902:uint = 3000;
      
      public static const const_531:uint = 0;
      
      public static const GOODGUY:uint = 1;
      
      public static const BADGUY:uint = 2;
      
      public static const NEUTRAL:uint = 3;
      
      public static const TEAM_BITS:uint = 2;
      
      public static const PLAYER:uint = 1 << 0;
      
      public static const MONSTER:uint = 1 << 1;
      
      public static const REMOTE:uint = 1 << 2;
      
      public static const LOCAL:uint = 1 << 3;
      
      public static const const_16:uint = 1 << 4;
      
      public static const const_241:uint = 1 << 5;
      
      public static const MAX_CHAR_LEVEL:uint = 50;
      
      public static const MAX_CHAR_LEVEL_BITS:uint = 6;
      
      public static const const_1382:uint = 0;
      
      public static const const_1341:uint = 1;
      
      public static const const_1343:uint = 2;
      
      public static const const_244:uint = 2;
      
      public static const YOFFSET_RANGE_HIGH:int = -30;
      
      public static const YOFFSET_RANGE_LOW:int = 25;
      
      public static const FRICTION:Number = 1;
      
      public static const ACCELERATION:Number = 1.7;
      
      public static const ICE_FRICTION:Number = 0.1 * FRICTION;
      
      public static const ICE_ACCELERATION:Number = 0.5 * ACCELERATION;
      
      public static const WATER_SLOW_FACTOR:Number = 0.7;
      
      public static const WATER_FRICTION:Number = 1.1 * FRICTION;
      
      public static const WATER_ACCELERATION:Number = 1.3 * ACCELERATION;
      
      public static const TERMINAL_VELOCITY:Number = 15;
      
      public static const DROP_IMPULSE:Number = 1;
      
      public static const GRAVITY:Number = 2;
      
      public static const JUMP_IMPULSE:Number = 18;
      
      public static const JUMPJET:Number = 1.2;
      
      public static const const_957:Number = 0.8;
      
      public static const const_1136:Number = 1.3;
      
      public static const const_1167:Number = 1.5;
      
      public static const const_1064:Number = 4.5;
      
      public static const const_829:Number = 0.02;
      
      public static const const_549:Number = 0.13;
      
      public static const TIME_TO_HOLD_CONVERSATION_THREAD:int = 10000;
      
      public static const const_642:int = 2000;
      
      public static const const_833:int = 50;
      
      public static const const_655:Array = [0,455,550,595,650,735,795,890,965,1075,1155,1285,1385,1520,1685,1810,1985,2180,2380,2600,2845,3090,3375,3710,4025,4410,4790,5225,5705,6215,6750,7340,8020,8690,9455,10300,11230,12185,13255,14405,15635,17010,18475,20050,21725,23650,25640,27835,30165,32730,35540];
      
      public static const const_1016:Array = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,5,5,5,6,6,7,7,8,8,9,10,11,11,12,13,14,16,17];
      
      public static const EXPERIENCE_TABLE:Array = [0,0,100,360,810,1490,2490,3870,5690,8090,11240,15240,20300,26660,34590,44390,56390,71110,89130,110910,137320,169320,207960,254380,310270,377230,457230,552910,666850,802650,964180,1156180,1384030,1654110,1974210,2352970,2800970,3330170,3955100,4692300,5561610,6585610,7791420,9210180,10878580,12839660,15143660,17848920,21024240,24749040,29116900,4294967295];
      
      public static const MONSTER_EXP_TABLE:Array = [0,10,13,15,17,20,23,26,30,35,40,46,53,61,70,80,92,106,121,139,160,184,211,243,279,320,368,422,485,557,640,735,844,970,1114,1280,1470,1689,1940,2229,2560,2941,3378,3880,4457,5120,5881,6756,7760,8914,10240];
      
      public static const MONSTER_GOLD_TABLE:Array = [0,43,46,49,53,57,61,65,70,75,80,86,92,98,106,113,121,130,139,149,160,171,184,197,211,226,243,260,279,299,320,343,368,394,422,453,485,520,557,597,640,686,735,788,844,905,970,1040,1114,1194,1280];
      
      public static const const_589:Array = [0,25,50,75,100,125,150,175,200,225,256,268,281,295,309,324,339,356,373,391,410,429,450,472,494,518,543,569,597,625,655,687,720,755,791,829,869,911,954,1000,1049,1099,1152,1207,1265,1326,1390,1457,1527,1601,1678,1758,1843,1932,2025,2122];
      
      public static const const_867:Array = [100,4920,5580,6020,6520,7040,7580,8180,8800,9480,10180,10960,11740,12640,13540,14540,15560,16660,17860,19120,20440,21860,23360,24960,26680,28460,30380,32420,34580,36900,39320,41920,44660,47560,50660,53940,57420,61080,64980,69120,73520,78160,83100,88300,93820,99700,105880,112460,119400,126760,134560];
      
      public static const PLAYER_HITPOINTS:Array = [100,7400,8031,8369,8724,9095,9485,9893,10321,10770,11240,11733,12249,12791,13358,13953,14576,15229,15914,16632,17384,18172,18999,19865,20773,21724,22722,23767,24862,26011,27214,28476,29798,31184,32636,34159,35755,37427,39180,41017,42943,44961,47077,49294,51618,54054,56607,59283,62088,65028,68109,71338,74723,78271,81989,85887];
      
      public static const const_631:Array = [0.5,0.525,0.55,0.575,0.6,0.625,0.65,0.675,0.7,0.725,0.75,0.775,0.8,0.825,0.85,0.875,0.9,0.925,0.95,1];
      
      public static const const_13:uint = 6;
      
      public static const const_717:uint = 0;
      
      public static const const_681:uint = 1;
      
      public static const const_741:uint = 2;
      
      public static const const_832:uint = 3;
      
      public static const const_752:uint = 4;
      
      public static const const_769:uint = 5;
      
      public static const const_1311:uint = 6;
      
      public static const const_165:Vector.<String> = new Vector.<String>(const_13,true);
      
      private static const const_1131:uint = 3;
      
      private static const const_830:Vector.<String> = Vector.<String>(["Paladin","Rogue","Mage"]);
      
      private static var var_628:GfxType = new GfxType();
      
      private static var var_798:GfxType = new GfxType();
      
      private static const const_596:Number = 120;
      
      private static var var_718:Point = new Point();
      
      private static var var_974:Point = new Point();
      
      private static var rippleGfxTypes:Array;
      
      private static const const_594:Number = 5;
      
      private static const const_651:Number = 20;
      
      private static const const_967:Number = 20;
      
      private static const const_1116:Number = 20;
      
      private static const const_294:Boolean = Boolean(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT || DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT);
      
      public static const PULLBACK_DIST:Number = 1.01;
      
      private static const const_654:Number = 50;
      
      private static const const_895:Number = 10;
      
      private static const const_931:Number = 500;
      
      private static const const_781:Number = 100;
      
      private static var var_922:Point = new Point();
      
      private static var var_420:Point = new Point();
      
      private static var var_1168:Point = new Point();
      
      private static var var_958:Point = new Point();
      
      private static var var_1190:Point = new Point();
      
      private static var var_1443:Point = new Point();
      
      private static var var_366:Point = new Point();
      
      private static var var_52:Point = new Point();
      
      private static var var_425:Point = new Point();
      
      private static var var_226:Point = new Point();
      
      private static var var_407:Point = new Point();
      
      private static var var_906:Point = new Point();
      
      private static const const_1362:uint = 4478925;
      
      private static const const_1314:int = 14644051;
      
      private static const const_1381:uint = 15317305;
      
      private static const const_1388:uint = 7842286;
      
      private static const const_974:Vector.<String> = Vector.<String>(["BridgeTown","BridgeTownHard","EmeraldGlades","EmeraldGladesHard","ShazariDesert","ShazariDesertHard"]);
      
      private static const const_689:uint = 35;
      
      {
         gtLevelUpFront.var_29 = "SFX_1.swf";
         gtLevelUpFront.animClass = "a_LevelUp_Front";
         gtLevelUpFront.animScale = 0.6;
         gtLevelUpFront.moveAnimSpeed = 3;
         gtLevelUpFront.bFireAndForget = true;
         gtLevelUpFront.var_177 = 0;
         gtLevelUpRear.var_29 = "SFX_1.swf";
         gtLevelUpRear.animClass = "a_LevelUp_Rear";
         gtLevelUpRear.animScale = 0.6;
         gtLevelUpRear.moveAnimSpeed = 3;
         gtLevelUpRear.bFireAndForget = true;
         gtLevelUpRear.var_177 = 0;
         const_334.var_29 = "SFX_1.swf";
         const_334.animClass = "a_Revive";
         const_334.bFireAndForget = true;
         const_165[const_717] = "Infernal";
         const_165[const_681] = "Draconic";
         const_165[const_741] = "Mythic";
         const_165[const_832] = "Sylvan";
         const_165[const_752] = "Trog";
         const_165[const_769] = "Undead";
         var_628.var_29 = "SFX_1.swf";
         var_628.animClass = "a_Teleport";
         var_628.animScale = 1;
         var_628.moveAnimSpeed = 1;
         var_628.bFireAndForget = true;
         var_628.var_177 = 0;
         var_798.var_29 = "SFX_1.swf";
         var_798.animClass = "a_Appear";
         var_798.animScale = 1;
         var_798.moveAnimSpeed = 1;
         var_798.bFireAndForget = true;
         var_798.var_177 = 0;
         method_630();
      }
      
      internal var var_1:Game;
      
      internal var id:uint;
      
      internal var entType:EntType;
      
      internal var var_20:uint;
      
      internal var team:uint;
      
      internal var mMasterClass:String;
      
      internal var currHP:int;
      
      internal var var_228:Number;
      
      internal var var_859:uint;
      
      internal var currGold:uint;
      
      internal var currGems:uint;
      
      internal var var_2276:int;
      
      internal var var_2410:Boolean;
      
      internal var var_31:Number = 0;
      
      internal const const_156:Number = 100;
      
      internal var var_997:Boolean = false;
      
      internal var var_494:Boolean = false;
      
      internal var var_2760:Boolean = false;
      
      internal var var_1835:Boolean = false;
      
      internal var var_1122:Boolean;
      
      internal var var_2170:Number;
      
      internal var var_1841:uint;
      
      internal var var_1878:uint;
      
      internal var var_2820:Room;
      
      internal var bIAmValid:Boolean;
      
      internal var cue:a_Cue = null;
      
      internal var var_1609:Room = null;
      
      internal var gfx:SuperAnimInstance;
      
      internal var physPosX:Number;
      
      internal var physPosY:Number;
      
      internal var appearPosX:Number;
      
      internal var appearPosY:Number;
      
      internal var var_10:Number;
      
      internal var var_12:Number;
      
      internal var yOffsetToSimulateZ:int;
      
      internal var var_1958:String;
      
      internal var var_1879:String;
      
      internal var var_868:uint;
      
      internal var currRoom:Room;
      
      internal var currSurface:class_37;
      
      internal var var_979:class_145;
      
      internal var var_703:class_37;
      
      internal var startPhysPosX:Number;
      
      internal var startPhysPosY:Number;
      
      internal var var_1460:Boolean = true;
      
      internal var var_916:Door = null;
      
      internal var var_848:Door = null;
      
      internal var var_2008:Boolean = false;
      
      internal var var_277:Sprite;
      
      internal var var_170:Sprite;
      
      internal var var_1931:String;
      
      internal var var_2039:uint;
      
      internal var var_436:SoundChannel = null;
      
      internal var var_467:SoundChannel = null;
      
      internal var var_2028:String = null;
      
      internal var var_746:SoundChannel = null;
      
      internal var var_386:ChatBubble;
      
      internal var velocity:Point;
      
      internal var var_2471:uint;
      
      internal var var_549:Boolean = false;
      
      internal var var_2194:Boolean = false;
      
      internal var var_2800:Boolean = false;
      
      internal var var_1111:Boolean = false;
      
      internal var var_1781:Boolean = false;
      
      internal var var_1760:Boolean = false;
      
      internal var var_1933:Boolean = false;
      
      internal var var_1836:Boolean = false;
      
      internal var var_1932:Boolean = false;
      
      internal var var_2545:Number = 0;
      
      internal var var_282:Point;
      
      internal var var_91:Point;
      
      internal var var_959:int;
      
      internal var var_874:int;
      
      internal var var_1258:int;
      
      internal var var_2569:int;
      
      internal var var_2753:int;
      
      internal var var_2583:int;
      
      internal var var_2693:Number = 0;
      
      internal var targetOffsetY:int;
      
      internal var var_471:Array;
      
      internal var entState:uint = 0;
      
      internal var var_2458:uint = 0;
      
      internal var var_2695:uint = 0;
      
      internal var var_596:Number = 22;
      
      internal var var_351:Number = 10;
      
      internal var var_2843:Boolean = true;
      
      internal var var_602:Boolean = false;
      
      internal var triggersHit:Vector.<class_144>;
      
      internal var var_610:Vector.<class_144>;
      
      internal var summonerId:uint = 0;
      
      internal var var_1459:Number = 0;
      
      internal var var_99:PowerType = null;
      
      internal var currEmote:String;
      
      internal var var_2652:int;
      
      internal var var_1262:int;
      
      internal var gotoLocationX:int;
      
      internal var gotoLocationY:int;
      
      internal var var_2749:uint;
      
      internal var bGotoLocation:Boolean;
      
      internal var var_24:class_143 = null;
      
      internal var brain:Brain = null;
      
      internal var var_38:class_122 = null;
      
      internal var var_1523:uint = 0;
      
      internal var mExpLevel:int;
      
      internal var var_64:int;
      
      internal var var_2384:int;
      
      internal var baseMaxHP:int = 0;
      
      internal var maxHP:int = 0;
      
      internal var var_1785:Number = 0;
      
      internal var maxSpeed:Number = 0;
      
      internal var armorClass:uint = 0;
      
      internal var meleeDamage:int = 0;
      
      internal var magicDamage:int = 0;
      
      internal var behaviorSpeedMod:Number = 1;
      
      internal var totalMods:class_134;
      
      internal var var_1562:Dictionary;
      
      internal var var_1516:Dictionary;
      
      internal var var_719:Dictionary;
      
      internal var var_1472:Dictionary;
      
      internal var var_18:class_44;
      
      internal var var_1283:Vector.<uint>;
      
      public const const_1396:Number = 0.15;
      
      internal var var_1086:Number;
      
      internal var var_1337:Number;
      
      internal var var_1553:Vector.<PowerType>;
      
      internal var var_667:Number = 0;
      
      internal var var_640:Number = 0;
      
      internal var var_1142:Number = 0;
      
      internal var var_1079:Number = 0;
      
      internal var var_1293:Number = 0;
      
      internal var var_66:Dictionary;
      
      internal var var_65:Dictionary;
      
      internal var var_412:Number = 0;
      
      internal var var_237:Number = 0;
      
      internal var var_571:Number = 0;
      
      internal var var_1028:Number = 0;
      
      internal var var_1065:Number = 0;
      
      internal var var_1783:uint = 0;
      
      internal var var_2830:uint = 0;
      
      internal var var_518:uint = 0;
      
      internal var var_485:uint = 0;
      
      internal var var_1812:uint = 0;
      
      internal var var_1216:uint = 0;
      
      internal var var_1113:class_77 = null;
      
      internal var var_2992:Number = 0;
      
      internal var var_2816:Boolean = false;
      
      internal var var_2650:Boolean = false;
      
      internal var var_2703:int = 0;
      
      internal var var_2144:Boolean = false;
      
      internal var var_309:SuperAnimInstance = null;
      
      internal var var_308:SuperAnimInstance = null;
      
      internal var var_599:uint = 0;
      
      internal var var_133:MovieClip = null;
      
      internal var combatState:CombatState;
      
      internal var var_85:class_118;
      
      internal var behaviorType:BehaviorType;
      
      internal var var_78:MovieClip;
      
      internal var var_1282:uint;
      
      internal var var_1400:Sprite;
      
      internal var var_2386:Boolean = false;
      
      internal var var_2959:Vector.<Buff>;
      
      internal const const_1411:String = "am_Buff";
      
      internal var var_2841:uint = 0;
      
      internal const const_1427:uint = 2000;
      
      internal var var_389:MovieClip;
      
      internal var debugPowerGfx:MovieClip;
      
      internal var var_2270:Boolean = false;
      
      internal var var_1714:Boolean = false;
      
      internal var var_1944:Boolean = false;
      
      internal var var_1715:Boolean = false;
      
      internal var var_1872:Boolean = false;
      
      internal var var_2533:Boolean = false;
      
      internal var var_2788:Boolean = false;
      
      internal var var_2701:Boolean = false;
      
      internal var var_2252:Boolean = false;
      
      internal var var_2079:Boolean = false;
      
      internal var var_1136:Boolean = false;
      
      internal var var_1630:Boolean = false;
      
      internal var var_2415:Boolean = false;
      
      internal var var_2305:Boolean = false;
      
      private var var_1712:Number = 0;
      
      private var var_2360:Number = 0;
      
      private var var_2348:Number = 0;
      
      private var var_2832:uint = 0;
      
      private var var_807:uint = 0;
      
      private var var_2980:int = 0;
      
      private var var_2998:int = 0;
      
      internal var bFiring:Boolean = false;
      
      internal var bJumping:Boolean = false;
      
      internal var bDropping:Boolean = false;
      
      internal var bRunning:Boolean = false;
      
      internal var bLeft:Boolean = false;
      
      internal var bBackpedal:Boolean = false;
      
      internal var var_1787:Number;
      
      internal var var_687:Boolean = false;
      
      internal var var_1170:Boolean = false;
      
      internal var var_2380:Boolean = false;
      
      internal var bLeftFacing:Boolean = false;
      
      internal var var_1875:Boolean = false;
      
      internal var var_1897:Number = 0;
      
      internal var var_2692:Number = 1;
      
      internal var var_2358:Boolean = false;
      
      internal var bSmackingAWallOrCeiling:Boolean = false;
      
      internal var var_2608:Boolean = false;
      
      internal var var_217:int;
      
      internal var var_2265:uint = 0;
      
      internal var var_2233:uint = 0;
      
      internal var bUntargetable:Boolean = false;
      
      internal var var_195:class_146;
      
      internal var var_818:class_146;
      
      internal var var_426:int = 0;
      
      internal var var_1395:int = 0;
      
      internal var var_2625:String = null;
      
      internal var var_1264:Boolean = false;
      
      internal var var_353:PowerType;
      
      internal var var_280:PowerType;
      
      internal var hudPowers:Vector.<PowerType>;
      
      internal var var_234:Vector.<PowerType>;
      
      internal var var_2455:Boolean = false;
      
      internal var var_2860:Boolean = false;
      
      internal var mEquipGear:Vector.<uint>;
      
      internal var var_694:EntType;
      
      internal var mEquipMount:class_20;
      
      internal var var_2337:EntType;
      
      internal var mEquipPet:class_87;
      
      internal var var_183:Entity;
      
      internal var var_329:Vector.<class_87>;
      
      internal var mCurrPotion:class_3;
      
      internal var mNextPotion:class_3;
      
      internal var var_1862:uint = 0;
      
      internal var var_2235:Boolean = false;
      
      internal var var_822:Boolean = false;
      
      internal var var_2685:Boolean = false;
      
      internal var var_2776:uint = 750;
      
      internal var var_2691:Number = 0;
      
      internal var var_2454:Number = 0;
      
      internal var var_2890:Number = 40;
      
      internal var var_2247:Number = 70;
      
      public function Entity(param1:Game, param2:String, param3:a_Cue, param4:Number, param5:Number, param6:uint, param7:uint, param8:uint, param9:uint, param10:uint, param11:PowerType, param12:class_118, param13:String, param14:Vector.<class_87>, param15:class_87, param16:class_3)
      {
         var _loc17_:MovieClip = null;
         var _loc18_:String = null;
         var _loc19_:TextField = null;
         var _loc20_:TextFormat = null;
         var _loc21_:uint = 0;
         var _loc22_:Level = null;
         var _loc23_:String = null;
         var _loc24_:uint = 0;
         var _loc25_:class_35 = null;
         this.mEquipGear = new Vector.<uint>(EntType.MAX_SLOTS,true);
         this.var_329 = new Vector.<class_87>(class_7.const_684,true);
         super();
         this.var_1 = param1;
         if(param6 & const_16)
         {
            this.id = 0;
         }
         else if(param8)
         {
            this.id = param8;
         }
         else
         {
            this.var_1862 = this.var_1.var_1602.shift();
            this.id = this.var_1862 << 16 | this.var_1.clientEntID;
         }
         this.var_20 = param6;
         this.cue = param3;
         this.summonerId = param10;
         this.var_99 = param11;
         this.entType = EntType.method_48(param2,!!(this.var_20 & PLAYER) ? "Player" : null);
         if(!this.entType)
         {
            class_24.method_7("Could not find EntType, is LoadedData missing? " + param2);
         }
         this.var_195 = new class_146(true);
         this.var_818 = new class_146(false);
         this.triggersHit = new Vector.<class_144>();
         this.var_610 = new Vector.<class_144>();
         this.var_386 = new ChatBubble(this);
         this.velocity = new Point(0,0);
         this.var_282 = new Point(0,0);
         this.var_91 = new Point(0,0);
         this.physPosX = param4;
         this.physPosY = param5;
         this.startPhysPosX = param4;
         this.startPhysPosY = param5;
         this.appearPosX = this.physPosX;
         this.appearPosY = this.physPosY + this.yOffsetToSimulateZ + this.var_1.var_776;
         this.SetCurrSurface(null);
         this.currRoom = null;
         this.var_217 = 0;
         if(DevSettings.flags & DevSettings.DEVFLAG_SHOWENTITYCOLLISION)
         {
            this.var_389 = new MovieClip();
            this.var_1.levelLayer.addChild(this.var_389);
         }
         if(DevSettings.flags & DevSettings.DEVFLAG_SHOWPOWERRANGE)
         {
            this.debugPowerGfx = new MovieClip();
            this.var_1.levelLayer.addChild(this.debugPowerGfx);
         }
         if(Boolean(param6 & LOCAL) && Boolean(param6 & PLAYER))
         {
            this.var_24 = new class_143(this.var_1,this);
         }
         else if(Boolean(param6 & LOCAL) && Boolean(param6 & MONSTER))
         {
            this.brain = new Brain(this.var_1,this);
         }
         else if(param6 & REMOTE)
         {
            this.var_38 = new class_122(this.var_1,this);
         }
         this.team = param7;
         if(this.team == const_531)
         {
            this.team = this.entType.entName == "EmberBush" ? GOODGUY : BADGUY;
         }
         this.mExpLevel = param9;
         if(this.id == this.var_1.clientEntID)
         {
            this.var_1.method_439(this.mExpLevel,this.var_64);
         }
         if(param6 & PLAYER)
         {
            if(!(param6 & LOCAL))
            {
               _loc17_ = class_4.method_16("a_PlayerName");
               MathUtil.method_2(_loc17_.am_NameText,this.entType.entName);
            }
            this.var_1.var_1495[this.entType.entName] = this;
         }
         else if(this.cue && this.cue.displayName && this.team != BADGUY)
         {
            _loc17_ = class_4.method_16("a_PlayerName");
            if(DevSettings.flags & DevSettings.const_511)
            {
               _loc18_ = this.cue.displayName + "\nCharName: " + this.cue.characterName + "\nEntType: " + this.entType.entName;
               _loc19_ = _loc17_.am_NameText;
               (_loc20_ = new TextFormat()).size = 12;
               _loc19_.setTextFormat(_loc20_);
               _loc19_.multiline = true;
               _loc19_.height = 100;
               _loc19_.y -= 20;
               MathUtil.method_2(_loc17_.am_NameText,_loc18_);
            }
            else
            {
               MathUtil.method_2(_loc17_.am_NameText,this.cue.displayName);
            }
         }
         else if(Boolean(DevSettings.flags & (DevSettings.const_511 | DevSettings.DEVFLAG_SHOWBEHAVIOR)) && Boolean(this.entType.displayName))
         {
            _loc17_ = class_4.method_16("a_PlayerName");
            MathUtil.method_2(_loc17_.am_NameText,this.entType.entName);
            this.method_436(EntType.const_157[this.entType.var_138] + " " + this.entType.baseLevel,0);
         }
         if(_loc17_)
         {
            this.var_277 = SuperAnimData.method_807(_loc17_,this.var_1.main.overallScale);
            this.var_1.var_272.addChild(this.var_277);
         }
         this.var_471 = new Array();
         this.combatState = new CombatState(this);
         this.var_85 = param12;
         this.mMasterClass = param13;
         if(param14)
         {
            _loc21_ = 0;
            while(_loc21_ < this.var_329.length && _loc21_ < param14.length)
            {
               this.var_329[_loc21_] = param14[_loc21_];
               _loc21_++;
            }
         }
         this.mEquipPet = param15;
         this.mCurrPotion = param16;
         this.ResetEntType(this.entType);
         this.currHP = this.maxHP;
         this.var_2276 = this.currHP;
         this.var_228 = 0;
         this.var_31 = 0;
         if(this.id == this.var_1.clientEntID)
         {
            this.var_1.method_184(this.currHP);
            this.var_1.method_114(this.var_31);
         }
         if(this.brain)
         {
            this.brain.method_275();
         }
         if(this.method_355())
         {
            _loc22_ = this.var_1.level;
            _loc23_ = this.cue.characterName;
            this.var_2235 = this.var_1.var_1810[_loc23_];
            _loc24_ = const_282;
            if(_loc25_ = class_14.var_999[_loc23_])
            {
               _loc24_ = this.var_1.method_793(_loc25_);
            }
            this.method_397(_loc24_);
         }
         this.var_822 = this.behaviorType.var_1023 || this.behaviorType.var_2200 || this.behaviorType.var_2543;
         this.gfx.m_TheDO.visible = !this.method_503() && !this.var_822;
         if(!(this.var_20 & const_241) && this.var_1.linkUpdater && !this.var_38)
         {
            this.var_1.linkUpdater.method_780(this);
            if(Boolean(DevSettings.flags & DevSettings.DEVFLAG_SHOWENTITYGHOST) && Boolean(DevSettings.flags & DevSettings.DEVFLAG_SERVERLOCAL))
            {
               this.var_1.linkUpdater.method_981(this,true);
            }
         }
         this.bIAmValid = true;
      }
      
      public static function method_415(param1:String, param2:String) : String
      {
         var _loc4_:String = null;
         var _loc7_:int = 0;
         var _loc3_:String = null;
         if(!param2)
         {
            return null;
         }
         if(!param1 || param1 == "")
         {
            return null;
         }
         var _loc5_:Array = class_127.const_245[param2];
         var _loc6_:String = param1.toUpperCase();
         _loc7_ = 0;
         while(_loc7_ < _loc5_.length)
         {
            if(!(_loc4_ = String(_loc5_[_loc7_])).toUpperCase().indexOf(_loc6_))
            {
               _loc3_ = _loc4_;
               break;
            }
            _loc7_++;
         }
         return _loc3_;
      }
      
      public static function method_244(param1:uint) : String
      {
         if(param1 < 0 || param1 >= const_1131)
         {
            return null;
         }
         return const_830[param1];
      }
      
      public static function method_2024(param1:String) : uint
      {
         var _loc2_:int = const_830.indexOf(param1);
         if(_loc2_ < 0)
         {
            _loc2_ = 0;
         }
         return _loc2_;
      }
      
      public static function method_850(param1:uint) : String
      {
         if(param1 == const_236)
         {
            return "GuildMaster";
         }
         if(param1 == const_139)
         {
            return "Officer";
         }
         if(param1 == const_309)
         {
            return "Member";
         }
         if(param1 == const_308)
         {
            return "Initiate";
         }
         if(param1 == const_470)
         {
            return "Silenced";
         }
         return "Unknown";
      }
      
      public static function method_128(param1:uint) : int
      {
         return PLAYER_HITPOINTS[param1];
      }
      
      public static function method_630() : void
      {
         var _loc1_:GfxType = null;
         rippleGfxTypes = new Array();
         _loc1_ = new GfxType();
         _loc1_.var_29 = "SFX_1.swf";
         _loc1_.animClass = "a_ExtraRipple";
         _loc1_.animScale = 1.2;
         _loc1_.bFireAndForget = true;
         _loc1_.var_527 = true;
         rippleGfxTypes.push(_loc1_);
         _loc1_ = new GfxType();
         _loc1_.var_29 = "SFX_1.swf";
         _loc1_.animClass = "a_Ripple";
         _loc1_.animScale = 1.2;
         _loc1_.bFireAndForget = false;
         _loc1_.var_527 = true;
         rippleGfxTypes.push(_loc1_);
         _loc1_ = new GfxType();
         _loc1_.var_29 = "SFX_1.swf";
         _loc1_.animClass = "a_RippleBlue";
         _loc1_.animScale = 1.2;
         _loc1_.bFireAndForget = false;
         _loc1_.var_527 = true;
         rippleGfxTypes.push(_loc1_);
      }
      
      public static function method_1630(param1:uint) : uint
      {
         var _loc2_:uint = 2;
         while(_loc2_ <= MAX_CHAR_LEVEL)
         {
            if(param1 < EXPERIENCE_TABLE[_loc2_])
            {
               return _loc2_ - 1;
            }
            _loc2_++;
         }
         return MAX_CHAR_LEVEL;
      }
      
      public static function method_574(param1:Entity, param2:Entity) : Boolean
      {
         if(param1.team == NEUTRAL || param2.team == NEUTRAL)
         {
            return false;
         }
         return param1.team != param2.team;
      }
      
      public function DestroyEntity(param1:Boolean) : void
      {
         var _loc2_:class_144 = null;
         if(!(this.var_20 & const_241) && this.var_1.linkUpdater && !this.var_38 && param1)
         {
            this.var_1.linkUpdater.method_1397(this);
         }
         this.bIAmValid = false;
         if(this.var_20 & PLAYER)
         {
            delete this.var_1.var_1495[this.entType.entName];
         }
         if(this.var_1862)
         {
            this.var_1.var_1602.push(this.var_1862);
         }
         this.SetCurrSurface(null);
         this.currSurface = null;
         this.var_703 = null;
         this.var_979 = null;
         this.var_694 = null;
         this.mEquipMount = null;
         if(this.var_183)
         {
            this.var_183.var_1835 = true;
            this.var_183 = null;
         }
         this.var_2337 = null;
         this.mEquipPet = null;
         this.var_329 = null;
         if(Boolean(this.currRoom) && Boolean(this.var_20 & Entity.PLAYER))
         {
            this.currRoom.method_886(this);
         }
         this.currRoom = null;
         this.mEquipGear = null;
         this.var_353 = null;
         this.var_280 = null;
         this.hudPowers = null;
         this.var_234 = null;
         this.var_195.method_834();
         this.var_195 = null;
         this.var_818.method_834();
         this.var_818 = null;
         if(this.var_309)
         {
            this.var_309.DestroySuperAnimInstance();
         }
         this.var_309 = null;
         if(this.var_308)
         {
            this.var_308.DestroySuperAnimInstance();
         }
         this.var_308 = null;
         if(Boolean(this.var_389) && Boolean(this.var_389.parent))
         {
            this.var_389.parent.removeChild(this.var_389);
         }
         this.var_389 = null;
         if(Boolean(this.debugPowerGfx) && Boolean(this.debugPowerGfx.parent))
         {
            this.debugPowerGfx.parent.removeChild(this.debugPowerGfx);
         }
         this.debugPowerGfx = null;
         if(Boolean(this.var_1400) && Boolean(this.var_1400.parent))
         {
            this.var_1400.parent.removeChild(this.var_1400);
         }
         this.var_1400 = null;
         if(Boolean(this.var_78) && Boolean(this.var_78.parent))
         {
            this.var_78.parent.removeChild(this.var_78);
         }
         this.var_78 = null;
         this.behaviorType = null;
         this.combatState.method_1206();
         this.combatState = null;
         if(this.var_85)
         {
            this.var_85.method_213();
         }
         this.var_85 = null;
         if(Boolean(this.var_133) && Boolean(this.var_133.parent))
         {
            this.var_133.parent.removeChild(this.var_133);
         }
         this.var_133 = null;
         this.totalMods.method_1383();
         this.totalMods = null;
         if(this.var_18)
         {
            this.var_18.method_577();
            this.var_18 = null;
         }
         this.var_1562 = null;
         this.var_1516 = null;
         this.var_719 = null;
         this.var_1472 = null;
         this.var_1113 = null;
         this.var_1283 = null;
         this.var_65 = null;
         this.var_66 = null;
         if(this.var_38)
         {
            this.var_38.method_1998();
            this.var_38 = null;
         }
         if(this.brain)
         {
            this.brain.method_1106();
            this.brain = null;
         }
         if(this.var_24)
         {
            this.var_24.method_1489();
            this.var_24 = null;
         }
         this.var_99 = null;
         for each(_loc2_ in this.triggersHit)
         {
            _loc2_.method_285();
         }
         this.triggersHit = null;
         for each(_loc2_ in this.var_610)
         {
            _loc2_.method_285();
         }
         this.var_610 = null;
         this.var_471 = null;
         this.var_2820 = null;
         this.velocity = null;
         this.var_282 = null;
         this.var_91 = null;
         this.var_386.method_1793();
         this.var_386 = null;
         if(this.var_436)
         {
            this.var_436 = SoundManager.method_155(this.var_436);
         }
         if(this.var_467)
         {
            this.var_467 = SoundManager.method_155(this.var_467);
         }
         if(this.var_746)
         {
            this.var_746 = SoundManager.method_155(this.var_746);
         }
         this.var_2028 = null;
         if(Boolean(this.var_277) && Boolean(this.var_277.parent))
         {
            this.var_277.parent.removeChild(this.var_277);
            SuperAnimData.method_504(this.var_277);
         }
         this.var_277 = null;
         if(Boolean(this.var_170) && Boolean(this.var_170.parent))
         {
            this.var_170.parent.removeChild(this.var_170);
            SuperAnimData.method_504(this.var_170);
         }
         this.var_170 = null;
         this.var_848 = null;
         this.var_916 = null;
         this.gfx.DestroySuperAnimInstance();
         this.gfx = null;
         if(this.var_1609)
         {
            this.var_1609.method_1581(this);
         }
         this.var_1609 = null;
         this.cue = null;
         this.entType = null;
         this.var_1 = null;
      }
      
      public function StartSkit(param1:String, param2:Boolean, param3:Entity) : void
      {
         var _loc10_:Packet = null;
         var _loc11_:Array = null;
         var _loc12_:Number = NaN;
         if(param1 == "")
         {
            if(param2)
            {
               this.var_1.screenChat.ReceiveChat(0,"",false);
               this.var_1.screenChat.ReceiveChat(this.id,"",false);
            }
            else
            {
               (_loc10_ = new Packet(LinkUpdater.const_451)).method_9(this.id);
               _loc10_.method_15(false);
               _loc10_.method_26("");
               this.var_1.serverConn.SendPacket(_loc10_);
               (_loc10_ = new Packet(LinkUpdater.const_451)).method_9(this.id);
               _loc10_.method_15(true);
               _loc10_.method_26("");
               this.var_1.serverConn.SendPacket(_loc10_);
            }
            this.var_1264 = false;
            this.var_426 = 0;
            return;
         }
         var _loc4_:Array;
         if((_loc4_ = param1.split("{")).length > 1)
         {
            if((_loc11_ = _loc4_[1].split("}")).length > 1)
            {
               _loc12_ = Number(_loc11_[0]);
               if(this.var_1.var_2193 >= _loc12_)
               {
                  param1 = String(_loc11_[1]);
               }
               else
               {
                  param1 = String(_loc4_[0]);
               }
            }
         }
         var _loc5_:int = int(this.var_1.mTimeThisTick);
         if(this.var_2625 != param1 || _loc5_ >= this.var_1395)
         {
            this.var_426 = 0;
         }
         this.var_2625 = param1;
         this.var_1264 = false;
         var _loc6_:Array;
         var _loc7_:uint = (_loc6_ = param1.split("=")).length;
         this.var_426 %= _loc7_;
         param1 = String(_loc6_[this.var_426]);
         ++this.var_426;
         this.var_1395 = _loc5_ + TIME_TO_HOLD_CONVERSATION_THREAD;
         if(_loc7_ == 1)
         {
            this.var_426 = 0;
         }
         else if(this.var_426 >= _loc7_)
         {
            this.var_1264 = true;
         }
         var _loc8_:Array;
         param1 = String((_loc8_ = param1.split("%"))[int(Math.random() * _loc8_.length)]);
         param1 = StringUtils.method_80(param1);
         var _loc9_:class_146 = param2 ? this.var_195 : this.var_818;
         if(Boolean(param3) && Boolean(param3.entType))
         {
            _loc9_.var_2412 = param3.entType.var_620;
            _loc9_.targetName = param3.entType.entName;
            _loc9_.targetClass = param3.entType.className;
         }
         else
         {
            _loc9_.var_2412 = false;
            _loc9_.targetName = "Adventurer";
            _loc9_.targetClass = "Hero";
         }
         this.method_340(param1.split(":"),_loc9_);
      }
      
      public function method_340(param1:Array, param2:class_146) : void
      {
         var _loc6_:Array = null;
         var _loc7_:String = null;
         var _loc8_:String = null;
         var _loc9_:String = null;
         var _loc10_:Packet = null;
         var _loc3_:int = 0;
         var _loc4_:Boolean = false;
         param2.skit = null;
         param2.var_1500 = 0;
         if(!param1 || param1.length == 0)
         {
            return;
         }
         var _loc5_:String = String(param1[0]);
         if((_loc5_ = StringUtils.method_80(_loc5_)) != "")
         {
            _loc5_ = String((_loc6_ = _loc5_.split("+"))[0]);
            _loc5_ = StringUtils.method_80(_loc5_);
            if(_loc6_.length > 1)
            {
               _loc7_ = String(_loc6_[1]);
               _loc3_ = parseInt(_loc7_,10) * 250;
            }
         }
         if(_loc5_.charAt(0) == "@")
         {
            _loc5_ = _loc5_.slice(1);
            _loc4_ = true;
         }
         while(_loc5_ != "" && _loc5_.charAt(0) == "<")
         {
            if(!(_loc8_ = StringUtils.method_1611(_loc5_,"<",">")).indexOf("Goto"))
            {
               _loc9_ = _loc8_.substr(5);
               this.method_945(_loc9_,Flags.CANCEL_ON_AGGRO);
            }
            else if(!_loc8_.indexOf("Disappear"))
            {
               this.var_822 = true;
            }
            else
            {
               this.DoEmote(_loc8_,param2.bLocal);
            }
            _loc5_ = StringUtils.method_400(_loc5_,">");
            _loc5_ = StringUtils.method_80(_loc5_);
         }
         if(param1.length > 1)
         {
            if(_loc3_ == 0)
            {
               _loc3_ = const_642 + _loc5_.length * const_833;
            }
            param2.var_1500 = this.var_1.mTimeThisTick + _loc3_;
            param2.skit = param1.slice(1);
         }
         if(_loc5_)
         {
            _loc5_ = (_loc5_ = _loc5_.replace("#tn#",param2.targetName)).replace("#tc#",param2.targetClass);
            _loc5_ = this.method_1631(_loc5_,param2.var_2412);
            if(param2.bLocal)
            {
               this.var_1.screenChat.ReceiveChat(_loc4_ ? 0 : this.id,_loc5_,false);
            }
            else
            {
               (_loc10_ = new Packet(LinkUpdater.const_451)).method_9(this.id);
               _loc10_.method_15(_loc4_);
               _loc10_.method_26(_loc5_);
               this.var_1.serverConn.SendPacket(_loc10_);
            }
         }
      }
      
      public function method_1631(param1:String, param2:Boolean) : String
      {
         var _loc3_:int = 0;
         var _loc4_:String = null;
         var _loc5_:Array;
         if((_loc5_ = param1.split("|")).length == 1)
         {
            return param1;
         }
         _loc3_ = 0;
         while(_loc3_ < _loc5_.length - 1)
         {
            if(param2)
            {
               if(StringUtils.contains(_loc5_[_loc3_],"("))
               {
                  _loc5_[_loc3_] = StringUtils.method_722(_loc5_[_loc3_],"(");
                  _loc5_[_loc3_ + 1] = StringUtils.method_925(_loc5_[_loc3_ + 1],")",true);
               }
               else
               {
                  _loc5_[_loc3_] = StringUtils.method_722(_loc5_[_loc3_]," ") + " ";
               }
            }
            else if(StringUtils.contains(_loc5_[_loc3_ + 1],")"))
            {
               _loc5_[_loc3_ + 1] = StringUtils.method_400(_loc5_[_loc3_ + 1],")");
               _loc5_[_loc3_] = StringUtils.method_925(_loc5_[_loc3_],"(",true);
            }
            else
            {
               _loc5_[_loc3_ + 1] = " " + StringUtils.method_400(_loc5_[_loc3_ + 1]," ");
            }
            _loc3_++;
         }
         _loc4_ = String(_loc5_[0]);
         _loc3_ = 1;
         while(_loc3_ < _loc5_.length)
         {
            _loc4_ = _loc4_.concat(_loc5_[_loc3_]);
            _loc3_++;
         }
         StringUtils.method_80(_loc4_);
         return _loc4_;
      }
      
      public function DoEmote(param1:String, param2:Boolean = false) : void
      {
         var _loc3_:Packet = null;
         var _loc4_:Packet = null;
         if(param1 == null)
         {
            return;
         }
         param1 = StringUtils.method_80(param1);
         this.method_438(param1);
         if(!param2)
         {
            if(param1 != "")
            {
               _loc3_ = new Packet(LinkUpdater.PKTTYPE_EMOTE_BEGIN);
               _loc3_.method_9(this.id);
               _loc3_.method_26(param1);
               this.var_1.serverConn.SendPacket(_loc3_);
            }
            else
            {
               (_loc4_ = new Packet(LinkUpdater.PKTTYPE_EMOTE_END)).method_9(this.id);
               this.var_1.serverConn.SendPacket(_loc4_);
            }
         }
      }
      
      public function method_438(param1:String) : void
      {
         var _loc5_:String = null;
         var _loc6_:String = null;
         var _loc2_:Boolean = false;
         var _loc3_:Array = param1.split(" ");
         param1 = String(_loc3_[0]);
         param1 = StringUtils.method_80(param1);
         if(param1 == class_127.var_1979)
         {
            if(_loc3_.length > 1)
            {
               _loc5_ = _loc3_.slice(1).join(" ");
               if(this.id != this.var_1.clientEntID)
               {
                  _loc5_ = class_127.method_167(_loc5_);
               }
               this.var_1.screenChat.method_1339(this.entType.entName,_loc5_);
            }
            return;
         }
         if(this.combatState.var_39 == class_14.powerTypesDict["SentinelForm1"].powerID)
         {
            return;
         }
         if(this.combatState.var_270)
         {
            return;
         }
         if(this.currEmote != "")
         {
            this.gfx.m_Seq.method_108();
            this.currEmote = null;
         }
         if(param1 == "" || param1 == "end")
         {
            return;
         }
         if(Boolean(this.var_20 & PLAYER) && !method_415(param1,this.entType.className) && !(DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT))
         {
            return;
         }
         var _loc4_:class_26;
         if(_loc4_ = this.gfx.m_Seq.var_71.var_69[param1])
         {
            if(_loc3_.length > 1)
            {
               if((_loc6_ = String(_loc3_[1])) == "KO")
               {
                  this.gfx.m_Seq.var_800 = _loc4_;
                  _loc2_ = true;
               }
               else
               {
                  _loc2_ = true;
               }
            }
            this.var_2652 = this.var_1.mTimeThisTick;
            this.var_1262 = _loc2_ ? 0 : int(this.var_2652 + _loc4_.var_710 / 24 * 1000);
            if(this.var_1262)
            {
               this.currEmote = param1;
            }
            this.gfx.m_Seq.method_34(Seq.C_EMOTE,param1,_loc2_);
            if(param1 == class_127.var_1566)
            {
               this.var_386.method_328("^t" + class_127.var_1825);
            }
            if(Boolean(this.var_20 & PLAYER) && Boolean(this.currRoom))
            {
               this.currRoom.method_79("Emote^Any");
               this.currRoom.method_79("Emote^" + param1.toUpperCase());
            }
         }
      }
      
      public function method_279(param1:String) : Point
      {
         var _loc2_:Room = Boolean(this.cue) && Boolean(this.cue.room) ? this.cue.room as Room : null;
         if(!_loc2_)
         {
            return null;
         }
         var _loc3_:Array = param1.split(" ");
         if(_loc3_.length < 2)
         {
            return null;
         }
         var _loc4_:Point;
         if(!(_loc4_ = _loc2_.var_780[_loc3_[0]][_loc3_[1]]))
         {
            return null;
         }
         return _loc4_;
      }
      
      public function method_945(param1:String, param2:uint) : void
      {
         var _loc3_:Point = this.method_279(param1);
         if(_loc3_)
         {
            this.gotoLocationX = _loc3_.x;
            if(this.entType.var_832)
            {
               this.gotoLocationY = _loc3_.y;
            }
            this.var_2749 = param2;
            this.bGotoLocation = true;
         }
      }
      
      public function method_831(param1:int, param2:Boolean) : void
      {
         this.TakeDamage(-param1,true);
         if(!param2)
         {
            this.var_228 = 0;
         }
         var _loc3_:SuperAnimInstance = new SuperAnimInstance(this.var_1,const_334,false);
         _loc3_.m_TheDO.x = this.appearPosX;
         _loc3_.m_TheDO.y = this.appearPosY;
         this.var_1.playerEntLayer.addChildAt(_loc3_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.gfx.m_TheDO) + 1);
         this.gfx.m_Seq.method_34(Seq.C_USEPOWER,"Revive",false);
         if(SoundConfig.var_1704)
         {
            this.var_1.method_82(SoundConfig.var_1704,this.var_10,this.var_12);
         }
      }
      
      public function BeginSleep() : void
      {
         var _loc1_:String = !!this.var_1879 ? this.var_1879 : this.entType.sleepAnim;
         if(Boolean(_loc1_) && _loc1_.toUpperCase() != "NONE")
         {
            this.gfx.m_Seq.method_34(Seq.const_590,_loc1_,true);
         }
      }
      
      public function BeginDrama() : void
      {
         var _loc1_:String = !!this.var_1958 ? this.var_1958 : this.entType.dramaAnim;
         if(Boolean(_loc1_) && _loc1_.toUpperCase() != "NONE")
         {
            this.gfx.m_Seq.method_34(Seq.C_USEPOWER,_loc1_,true);
         }
      }
      
      public function BeginActive() : void
      {
         this.gfx.m_Seq.method_108();
         if(this.entType.var_1570)
         {
            this.var_1.method_82(this.entType.var_1570,this.var_10,this.var_12);
         }
      }
      
      public function method_156() : Boolean
      {
         if(this.bUntargetable)
         {
            return false;
         }
         if(Boolean(this.combatState) && this.combatState.var_1421)
         {
            return false;
         }
         if(this.behaviorType.bUntargetable)
         {
            return false;
         }
         if(this.entState == const_467 && !this.behaviorType.var_1124)
         {
            return false;
         }
         return true;
      }
      
      public function method_503() : Boolean
      {
         return this.var_2235 && this.var_599 != const_449 && this.var_599 != const_482;
      }
      
      public function method_397(param1:uint) : void
      {
         var _loc2_:* = this.var_599 != param1;
         this.var_599 = param1;
         if(DevSettings.flags & DevSettings.DEVFLAG_NO_GRAPHICS)
         {
            return;
         }
         if(this.var_133)
         {
            this.var_133.parent.removeChild(this.var_133);
            this.var_133 = null;
         }
         if(this.var_599 == const_482)
         {
            this.var_133 = class_4.method_16("a_Notify_ReturnQuest");
         }
         else if(this.var_599 == const_449)
         {
            this.var_133 = class_4.method_16("a_Notify_NewQuest");
         }
         else if(this.var_599 == const_599)
         {
            this.var_133 = class_4.method_16("a_Notify_ActiveQuest");
         }
         if(this.var_133)
         {
            this.var_133.x = this.appearPosX;
            this.var_133.y = this.appearPosY - this.entType.height - 20;
            this.var_1.var_272.addChildAt(this.var_133,0);
         }
         if(_loc2_)
         {
            this.var_426 = 0;
            this.var_1264 = false;
         }
      }
      
      public function method_1915(param1:uint, param2:class_64, param3:uint) : void
      {
         var _loc7_:class_64 = null;
         var _loc10_:String = null;
         var _loc4_:class_42 = this.var_1.mOwnedGear[param1];
         var _loc5_:class_114;
         if(!(_loc5_ = this.var_1.mOwnedCharms[param2.method_75()]) || !_loc4_ || !param3)
         {
            return;
         }
         if(!_loc5_.var_181)
         {
            return;
         }
         var _loc6_:Boolean = param2.method_379();
         var _loc8_:class_64 = _loc5_.charmData;
         if(param3 == 1)
         {
            if(!_loc6_)
            {
               _loc4_.var_189 = _loc8_.method_538();
            }
            else
            {
               _loc7_ = _loc4_.var_189;
               _loc4_.var_189 = null;
            }
         }
         else if(param3 == 2)
         {
            if(!_loc6_)
            {
               _loc4_.var_196 = _loc8_.method_538();
            }
            else
            {
               _loc7_ = _loc4_.var_196;
               _loc4_.var_196 = null;
            }
         }
         else if(!_loc6_)
         {
            _loc4_.var_187 = _loc8_.method_538();
         }
         else
         {
            _loc7_ = _loc4_.var_187;
            _loc4_.var_187 = null;
         }
         --_loc5_.var_181;
         if(!_loc5_.var_181)
         {
            delete this.var_1.mOwnedCharms[_loc8_.method_75()];
            _loc5_.method_833();
         }
         if(_loc7_)
         {
            if(_loc7_.var_8 == class_64.const_196 || _loc7_.method_118())
            {
               §§push("L");
            }
            else
            {
               _loc10_ = _loc7_.var_8 == class_64.const_180 || _loc7_.method_124() ? "R" : "M";
               this.var_1.screenNotification.ShowNotification(class_46.const_211,_loc7_.method_49(),_loc10_,true,null,null,_loc7_);
               this.var_1.GainCharm(_loc7_,false);
               §§goto(addr280);
            }
            §§goto(addr216);
         }
         addr280:
         var _loc9_:uint = uint(EntType.method_87(_loc4_.gearType.type));
         this.entType.equippedGear[_loc9_] = _loc4_.method_908();
         this.ResetEntType(this.entType);
         this.var_1.screenArmory.method_176();
         this.var_1.screenArmory.Refresh();
      }
      
      public function method_622() : Boolean
      {
         return !(this.var_20 & PLAYER) && this.team != GOODGUY;
      }
      
      public function method_1929() : void
      {
         if(this.behaviorType.var_988)
         {
            return;
         }
         if(this.var_602)
         {
            this.var_602 = false;
            this.entState = const_78;
         }
         this.var_868 = 0;
         var _loc1_:int = this.maxHP;
         this.ResetEntType(this.entType);
         if(this.entState != const_6)
         {
            this.currHP += this.maxHP - _loc1_;
            if(this.id == this.var_1.clientEntID)
            {
               this.var_1.method_184(this.currHP);
            }
         }
      }
      
      public function method_961(param1:uint) : void
      {
         if(param1 == this.var_1523 || !this.method_622())
         {
            return;
         }
         if(this.var_602 && param1 > this.var_1523)
         {
            this.var_602 = false;
            this.entState = const_78;
         }
         if(this.entState == const_6)
         {
            return;
         }
         var _loc2_:Number = Number(Game.const_790[param1]);
         if(this.entType.var_913)
         {
            _loc2_ += Game.const_612;
         }
         var _loc3_:int = Math.round(this.method_986() * _loc2_);
         var _loc4_:int = _loc3_ - this.baseMaxHP;
         this.baseMaxHP += _loc4_;
         this.maxHP += _loc4_;
         this.currHP += _loc4_;
         this.var_1523 = param1;
         if(this.id == this.var_1.clientEntID)
         {
            this.var_868 = 0;
            this.var_1.method_418(this.maxHP);
            this.var_1.method_184(this.currHP);
         }
      }
      
      public function method_511(param1:int) : void
      {
         var _loc5_:Entity = null;
         var _loc6_:int = 0;
         this.yOffsetToSimulateZ = param1;
         this.appearPosX = this.physPosX;
         this.appearPosY = this.physPosY + this.yOffsetToSimulateZ + this.var_1.var_776;
         this.var_12 = this.appearPosY - this.entType.height * 0.5;
         this.gfx.m_TheDO.y = this.appearPosY;
         if(this.gfx.m_TheDO.parent)
         {
            this.gfx.m_TheDO.parent.removeChild(this.gfx.m_TheDO);
         }
         var _loc2_:Entity = null;
         var _loc3_:int = -99999999;
         var _loc4_:Number = this.yOffsetToSimulateZ;
         if(!this.entType.var_2677)
         {
            for each(_loc5_ in this.var_1.entities)
            {
               if(_loc5_ != this)
               {
                  _loc6_ = _loc5_.yOffsetToSimulateZ;
                  if(_loc4_ > _loc6_ && _loc6_ > _loc3_)
                  {
                     _loc2_ = _loc5_;
                     _loc3_ = _loc6_;
                  }
               }
            }
         }
         if(this.entType.var_2928)
         {
            this.var_1.playerEntLayer.addChildAt(this.gfx.m_TheDO,this.var_1.playerEntLayer.numChildren - 1);
         }
         else if(_loc2_)
         {
            this.var_1.playerEntLayer.addChildAt(this.gfx.m_TheDO,this.var_1.playerEntLayer.getChildIndex(_loc2_.gfx.m_TheDO) + 1);
         }
         else
         {
            this.var_1.playerEntLayer.addChildAt(this.gfx.m_TheDO,0);
         }
      }
      
      public function method_436(param1:String, param2:uint) : void
      {
         var _loc3_:MovieClip = null;
         this.var_1931 = param1;
         this.var_2039 = param2;
         if(!this.var_277)
         {
            return;
         }
         if(Boolean(this.var_170) && Boolean(this.var_170.parent))
         {
            this.var_170.parent.removeChild(this.var_170);
            SuperAnimData.method_504(this.var_170);
         }
         this.var_170 = null;
         if(Boolean(param1) && (!(this.var_20 & LOCAL) || !(this.var_20 & PLAYER)))
         {
            _loc3_ = class_4.method_16("a_GuildName");
            MathUtil.method_2(_loc3_.am_NameText,"<" + param1 + ">");
            this.var_170 = SuperAnimData.method_807(_loc3_,this.var_1.main.overallScale);
            this.var_1.var_272.addChild(this.var_170);
         }
      }
      
      public function method_1350(param1:String) : void
      {
         var _loc2_:PowerType = null;
         if(param1)
         {
            _loc2_ = class_14.powerTypesDict[param1];
            if(_loc2_)
            {
               this.hudPowers.push(_loc2_);
            }
         }
      }
      
      public function method_1437(param1:String) : void
      {
         if(!param1)
         {
            return;
         }
         var _loc2_:PowerType = class_14.powerTypesDict[param1];
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:int = this.hudPowers.indexOf(_loc2_);
         if(_loc3_ >= 0)
         {
            this.hudPowers.splice(_loc3_,1);
         }
      }
      
      public function method_1587() : void
      {
         this.method_822(this.entType.var_1200);
         this.var_353 = !!this.entType.meleePower ? class_14.powerTypesDict[this.entType.meleePower] : null;
         this.var_280 = !!this.entType.rangedPower ? class_14.powerTypesDict[this.entType.rangedPower] : null;
      }
      
      public function method_1400(param1:String) : void
      {
         this.var_353 = !!param1 ? class_14.powerTypesDict[param1] : null;
      }
      
      public function method_1254(param1:String) : void
      {
         this.var_280 = !!param1 ? class_14.powerTypesDict[param1] : null;
      }
      
      public function method_822(param1:Array) : void
      {
         var _loc2_:String = null;
         var _loc3_:PowerType = null;
         if(!(this.var_20 & (PLAYER | const_16)))
         {
            this.hudPowers = new Vector.<PowerType>();
            for each(_loc2_ in param1)
            {
               _loc3_ = class_14.powerTypesDict[_loc2_];
               if(_loc3_)
               {
                  this.hudPowers.push(_loc3_);
               }
            }
            return;
         }
      }
      
      private function method_485(param1:class_64) : void
      {
         var _loc3_:class_1 = null;
         var _loc4_:Number = NaN;
         var _loc2_:class_1 = param1.var_13;
         this.totalMods.var_79 += _loc2_.var_79;
         this.totalMods.itemDrop += _loc2_.itemDrop;
         this.totalMods.var_152 += _loc2_.var_152;
         this.var_667 += _loc2_.var_2402;
         this.var_1142 += _loc2_.var_2118;
         this.meleeDamage += _loc2_.var_2429;
         this.magicDamage += _loc2_.var_2040;
         this.armorClass += _loc2_.var_2033;
         this.totalMods.var_377 += _loc2_.var_1593;
         if(param1.secondary)
         {
            _loc3_ = param1.method_115();
            _loc4_ = param1.method_421();
            this.totalMods.var_79 += _loc3_.var_79 * _loc4_;
            this.totalMods.itemDrop += _loc3_.itemDrop * _loc4_;
            this.totalMods.var_152 += _loc3_.var_152 * _loc4_;
            this.var_667 += _loc3_.var_2402 * _loc4_;
            this.var_1142 += _loc3_.var_2118 * _loc4_;
            this.meleeDamage += _loc3_.var_2429 * _loc4_;
            this.magicDamage += _loc3_.var_2040 * _loc4_;
            this.armorClass += _loc3_.var_2033 * _loc4_;
            this.totalMods.var_377 += _loc3_.var_1593 * _loc4_;
         }
      }
      
      private function method_1457() : void
      {
         var _loc6_:MagicType = null;
         var _loc9_:String = null;
         var _loc10_:PowerType = null;
         var _loc11_:EntTypeGear = null;
         var _loc12_:String = null;
         var _loc13_:GearType = null;
         var _loc14_:class_64 = null;
         var _loc15_:class_64 = null;
         var _loc16_:class_64 = null;
         var _loc17_:uint = 0;
         var _loc18_:MagicType = null;
         var _loc19_:class_10 = null;
         var _loc20_:PowerType = null;
         var _loc21_:PowerType = null;
         var _loc22_:PowerType = null;
         var _loc23_:class_134 = null;
         var _loc24_:String = null;
         var _loc25_:Number = NaN;
         var _loc26_:String = null;
         var _loc27_:Number = NaN;
         var _loc28_:String = null;
         var _loc29_:Number = NaN;
         var _loc30_:uint = 0;
         var _loc31_:class_87 = null;
         this.var_353 = !!this.entType.meleePower ? class_14.powerTypesDict[this.entType.meleePower] : null;
         this.var_280 = !!this.entType.rangedPower ? class_14.powerTypesDict[this.entType.rangedPower] : null;
         if(!(this.var_20 & (PLAYER | const_16)))
         {
            this.hudPowers = new Vector.<PowerType>();
            for each(_loc9_ in this.entType.var_1200)
            {
               if(_loc10_ = class_14.powerTypesDict[_loc9_])
               {
                  this.hudPowers.push(_loc10_);
               }
            }
            return;
         }
         if(!this.entType.className)
         {
            this.method_1086();
            return;
         }
         var _loc1_:EntTypeGear = this.entType.equippedGear[EntType.SWORD_SLOT];
         var _loc2_:GearType = !!_loc1_ ? class_14.gearTypesDict[_loc1_.gearName] : null;
         if(Boolean(_loc2_) && Boolean(_loc2_.meleePower))
         {
            this.var_353 = class_14.powerTypesDict[_loc2_.meleePower];
         }
         if(Boolean(_loc2_) && Boolean(_loc2_.rangedPower))
         {
            this.var_280 = class_14.powerTypesDict[_loc2_.rangedPower];
         }
         var _loc3_:Vector.<MagicType> = new Vector.<MagicType>();
         this.hudPowers = new Vector.<PowerType>(EntType.const_238,true);
         this.var_1553 = new Vector.<PowerType>();
         var _loc5_:int = 1;
         while(_loc5_ < EntType.MAX_SLOTS)
         {
            if(_loc12_ = !!(_loc11_ = this.entType.equippedGear[_loc5_]) ? _loc11_.gearName : null)
            {
               if(_loc13_ = class_14.gearTypesDict[_loc12_])
               {
                  _loc14_ = !!_loc11_.var_432 ? class_64.method_56(_loc11_.var_432) : null;
                  _loc15_ = !!_loc11_.var_501 ? class_64.method_56(_loc11_.var_501) : null;
                  _loc16_ = !!_loc11_.var_486 ? class_64.method_56(_loc11_.var_486) : null;
                  _loc17_ = _loc13_.method_377(this.var_64);
                  this.meleeDamage += _loc13_.method_121("Attack",_loc17_,false);
                  this.magicDamage += _loc13_.method_121("Expertise",_loc17_,false);
                  this.armorClass += _loc13_.method_121("Armor",_loc17_,false);
                  if(_loc18_ = !!_loc13_.var_1197 ? class_14.magicTypesDict[_loc13_.var_1197] : null)
                  {
                     _loc3_.push(_loc18_);
                  }
                  if(_loc14_)
                  {
                     this.method_485(_loc14_);
                  }
                  if(_loc15_)
                  {
                     this.method_485(_loc15_);
                  }
                  if(_loc16_)
                  {
                     this.method_485(_loc16_);
                  }
                  _loc14_ = null;
                  _loc15_ = null;
                  _loc16_ = null;
                  if(_loc5_ == EntType.SWORD_SLOT)
                  {
                     if(_loc13_.var_100)
                     {
                        this.var_1553.push(class_14.powerTypesDict[_loc13_.var_100]);
                     }
                     if(_loc13_.procRune2)
                     {
                        this.var_1553.push(class_14.powerTypesDict[_loc13_.procRune2]);
                     }
                  }
                  if(_loc13_.var_100 == "CritChance")
                  {
                     this.var_1079 += CombatState.const_560;
                  }
                  if(_loc13_.procRune2 == "CritChance")
                  {
                     this.var_1079 += CombatState.const_560;
                  }
                  if(_loc13_.var_100 == "CritDamage")
                  {
                     this.var_640 += CombatState.const_466;
                  }
                  if(_loc13_.procRune2 == "CritDamage")
                  {
                     this.var_640 += CombatState.const_466;
                  }
                  if(_loc13_.var_100 == "HealthPercent")
                  {
                     this.var_1293 += CombatState.const_260;
                  }
                  if(_loc13_.procRune2 == "HealthPercent")
                  {
                     this.var_1293 += CombatState.const_260;
                  }
                  if(Boolean(_loc13_.var_100) && _loc13_.var_100.indexOf("Resist") > -1)
                  {
                     this.var_66[_loc13_.var_100] = CombatState.const_126 + (!!this.var_66[_loc13_.var_100] ? this.var_66[_loc13_.var_100] : 0);
                  }
                  if(Boolean(_loc13_.procRune2) && _loc13_.procRune2.indexOf("Resist") > -1)
                  {
                     this.var_66[_loc13_.procRune2] = CombatState.const_126 + (!!this.var_66[_loc13_.procRune2] ? this.var_66[_loc13_.procRune2] : 0);
                  }
                  if(Boolean(_loc13_.var_100) && _loc13_.var_100.indexOf("Slay") >= 0)
                  {
                     this.var_65[_loc13_.var_100] = CombatState.const_136 + (!!this.var_65[_loc13_.var_100] ? this.var_65[_loc13_.var_100] : 0);
                  }
                  if(Boolean(_loc13_.procRune2) && _loc13_.procRune2.indexOf("Slay") >= 0)
                  {
                     this.var_65[_loc13_.procRune2] = CombatState.const_136 + (!!this.var_65[_loc13_.procRune2] ? this.var_65[_loc13_.procRune2] : 0);
                  }
                  if(_loc13_.var_100 == "RecoveryBoost")
                  {
                     this.var_237 += CombatState.const_556;
                  }
                  if(_loc13_.procRune2 == "RecoveryBoost")
                  {
                     this.var_237 += CombatState.const_556;
                  }
                  if(_loc13_.var_100 == "Resilience")
                  {
                     this.var_571 += CombatState.const_569;
                  }
                  if(_loc13_.procRune2 == "Resilience")
                  {
                     this.var_571 += CombatState.const_569;
                  }
                  if(_loc13_.var_100 == "Haste")
                  {
                     this.var_412 += CombatState.const_548;
                  }
                  if(_loc13_.procRune2 == "Haste")
                  {
                     this.var_412 += CombatState.const_548;
                  }
               }
            }
            _loc5_++;
         }
         if(this.var_1.mAbilityBook)
         {
            for each(_loc19_ in this.var_1.mAbilityBook.mHotbarList)
            {
               if(_loc20_ = !!_loc19_ ? this.GetPowerFromAbilityType(_loc19_) : null)
               {
                  this.hudPowers[_loc19_.var_90] = _loc20_;
               }
            }
         }
         this.var_1337 = this.var_1142 + this.var_1079 + this.var_18.method_64("ProcChance");
         this.var_1086 = this.const_1396 * (1 + this.var_1337);
         this.meleeDamage += this.var_18.method_64("Melee");
         this.magicDamage += this.var_18.method_64("Magic");
         this.armorClass += this.var_18.method_64("Armor");
         this.var_237 += this.var_18.method_64("Recovery");
         this.var_571 += this.var_18.method_64("CCReduction");
         this.meleeDamage += Math.ceil(this.magicDamage * this.var_18.method_64("MeleeFromWis"));
         this.armorClass += Math.ceil(this.magicDamage * this.var_18.method_64("ArmorFromWis"));
         this.var_237 *= 1 + this.magicDamage * this.var_18.method_64("RecoveryFromWis");
         this.var_1028 += this.var_18.method_64("DoTResist");
         if(this.var_1028 > 1)
         {
            this.var_1028 = 1;
         }
         this.var_1065 += this.var_18.method_64("DebuffResist");
         if(this.var_1065 > 1)
         {
            this.var_1065 = 1;
         }
         if(this.mEquipMount)
         {
            if(_loc21_ = PowerType.var_440)
            {
               _loc21_.displayName = "Summon " + this.mEquipMount.displayName;
               _loc21_.description = this.mEquipMount.description;
               this.hudPowers[EntType.const_330] = _loc21_;
            }
         }
         if(this.mEquipPet)
         {
            _loc22_ = this.mEquipPet.mPetType.var_2294 ? PowerType.var_315 : PowerType.var_511;
            this.hudPowers[EntType.const_283] = _loc22_;
            if(!this.var_2860)
            {
               this.var_2860 = true;
               if((_loc22_ = PowerType.var_511).coolDownTime)
               {
                  this.combatState.var_114[_loc22_.powerID] = this.var_1.mTimeThisTick + _loc22_.coolDownTime;
               }
               if((_loc22_ = PowerType.var_315).coolDownTime)
               {
                  this.combatState.var_114[_loc22_.powerID] = this.var_1.mTimeThisTick + _loc22_.coolDownTime;
               }
            }
         }
         if(this.mMasterClass)
         {
            this.method_1886();
         }
         else
         {
            this.combatState.var_354 = BuffType.const_624;
         }
         for each(_loc6_ in _loc3_)
         {
            _loc23_ = _loc6_.var_1218;
            this.totalMods.var_251 += _loc23_.var_251;
            this.totalMods.var_1680 += _loc23_.var_1680;
            this.totalMods.var_1724 += _loc23_.var_1724;
            this.totalMods.var_79 += _loc23_.var_79;
            this.totalMods.itemDrop += _loc23_.itemDrop;
            this.totalMods.var_152 += _loc23_.var_152;
            this.totalMods.var_1695 += _loc23_.var_1695;
            this.totalMods.var_1318 += _loc23_.var_1318;
            this.totalMods.var_1492 += _loc23_.var_1492;
            this.totalMods.meleeDamage += _loc23_.meleeDamage;
            this.totalMods.magicDamage += _loc23_.magicDamage;
            this.totalMods.var_377 += _loc23_.var_377;
            if(_loc23_.var_2427)
            {
               for each(_loc24_ in _loc23_.var_2427)
               {
                  _loc25_ = Number(this.var_1562[_loc24_]);
                  this.var_1562[_loc24_] = !!_loc25_ ? _loc25_ + _loc23_.var_2840 : _loc23_.var_2840;
               }
            }
            if(_loc23_.var_2023)
            {
               for each(_loc26_ in _loc23_.var_2023)
               {
                  _loc27_ = Number(this.var_1516[_loc26_]);
                  this.var_1516[_loc26_] = !!_loc27_ ? _loc27_ + _loc23_.var_2503 : _loc23_.var_2503;
               }
            }
            if(_loc23_.var_157)
            {
               for each(_loc28_ in _loc23_.var_157)
               {
                  _loc29_ = Number(this.var_719[_loc28_]);
                  this.var_719[_loc28_] = !!_loc29_ ? _loc29_ + _loc23_.var_2746 : _loc23_.var_2746;
               }
            }
         }
         if(this.mEquipPet)
         {
            this.totalMods.var_79 += this.mEquipPet.method_697();
            this.totalMods.var_152 += this.mEquipPet.method_826();
            this.totalMods.itemDrop += this.mEquipPet.method_598();
            this.totalMods.var_697 += this.mEquipPet.method_792();
         }
         if(this.var_329)
         {
            _loc30_ = 0;
            while(_loc30_ < this.var_329.length)
            {
               if(_loc31_ = this.var_329[_loc30_])
               {
                  this.totalMods.var_79 += _loc31_.method_423();
                  this.totalMods.var_152 += _loc31_.method_427();
                  this.totalMods.itemDrop += _loc31_.method_493();
                  this.totalMods.var_697 += _loc31_.method_443();
               }
               _loc30_++;
            }
         }
         if(this.mCurrPotion)
         {
            this.totalMods.var_79 += this.mCurrPotion.var_2762;
            this.totalMods.var_152 += this.mCurrPotion.var_2719;
            this.totalMods.itemDrop += this.mCurrPotion.var_2646;
            this.totalMods.var_697 += this.mCurrPotion.var_2666;
         }
         var _loc7_:Number = this.var_18.method_64("HPFromWis");
         var _loc8_:uint = Math.ceil(this.magicDamage * _loc7_);
         this.totalMods.var_377 += this.var_18.method_64("Health");
         this.totalMods.var_377 += _loc8_;
         this.maxHP += this.totalMods.var_377;
         this.maxHP += this.maxHP * this.var_1293;
         this.combatState.var_555 = true;
      }
      
      public function method_1086() : void
      {
         var _loc3_:String = null;
         var _loc7_:PowerType = null;
         var _loc1_:uint = 1;
         var _loc2_:EntType = EntType.method_48(this.entType.parentEntType);
         this.hudPowers = new Vector.<PowerType>(EntType.const_238,true);
         this.var_234 = null;
         for each(_loc3_ in _loc2_.var_1200)
         {
            if((Boolean(_loc7_ = class_14.powerTypesDict[_loc3_])) && _loc1_ < EntType.const_238)
            {
               this.hudPowers[_loc1_] = _loc7_;
               _loc1_++;
            }
         }
         this.var_353 = !!_loc2_.meleePower ? class_14.powerTypesDict[_loc2_.meleePower] : null;
         this.var_280 = !!_loc2_.rangedPower ? class_14.powerTypesDict[_loc2_.rangedPower] : null;
         var _loc4_:Array;
         var _loc5_:uint = !!(_loc4_ = EntType.const_132[_loc2_.var_138]) ? uint(_loc4_[this.var_64]) : 0;
         var _loc6_:uint = uint(EntType.const_754[this.var_64]);
         this.meleeDamage = Math.round(_loc5_ * _loc2_.meleeDamage);
         this.magicDamage = Math.round(_loc6_ * _loc2_.var_1044);
         this.armorClass = Math.round(const_589[this.var_64] * _loc2_.armorClass);
      }
      
      public function method_1677(param1:String) : PowerType
      {
         return class_14.powerTypesDict[param1];
      }
      
      public function method_775(param1:String) : PowerType
      {
         var _loc2_:PowerType = class_14.powerTypesDict[param1];
         return !!_loc2_ ? _loc2_ : null;
      }
      
      public function GetPowerFromAbilityType(param1:class_10) : PowerType
      {
         if(!param1)
         {
            return null;
         }
         var _loc2_:uint = 0;
         if(this.var_1.mAbilityBook)
         {
            _loc2_ = uint(this.var_1.mAbilityBook.mAbilityListTrainedRanks[param1.abilityID]);
         }
         var _loc3_:String = !!_loc2_ ? param1.abilityName + _loc2_ : param1.abilityName;
         var _loc4_:PowerType;
         if(!(_loc4_ = class_14.powerTypesDict[_loc3_]))
         {
            _loc4_ = class_14.powerTypesDict[param1.abilityName + "1"];
         }
         return !!_loc4_ ? _loc4_ : null;
      }
      
      public function method_38(param1:String, param2:uint) : PowerType
      {
         var _loc3_:class_10 = class_14.var_526[param1.toLowerCase() + param2];
         var _loc4_:PowerType = null;
         if(_loc3_)
         {
            _loc4_ = this.GetPowerFromAbilityType(_loc3_);
         }
         if(!_loc4_)
         {
            _loc4_ = class_14.powerTypesDict[_loc3_.abilityName];
         }
         return !!_loc4_ ? _loc4_ : null;
      }
      
      public function method_302(param1:String, param2:uint) : class_10
      {
         return class_14.var_526[param1.toLowerCase() + param2];
      }
      
      public function ResetEntType(param1:EntType, param2:Boolean = false) : void
      {
         this.entType = param1;
         this.method_1442();
         if(!param2)
         {
            this.method_1826();
         }
      }
      
      private function method_986() : int
      {
         if(!this.entType.var_939)
         {
            return 1073741823;
         }
         var _loc1_:int = Math.round(const_867[this.var_64] * this.entType.var_939);
         return !!_loc1_ ? _loc1_ : 1;
      }
      
      public function RecalculateSpeed() : void
      {
         if(Boolean(this.var_694) && !this.combatState.var_2173)
         {
            this.maxSpeed = (1 + this.combatState.var_2405) * this.entType.var_251 * this.behaviorSpeedMod;
         }
         else
         {
            this.maxSpeed = (1 + this.combatState.var_540) * (this.entType.var_251 + this.totalMods.var_251) * this.behaviorSpeedMod;
         }
         if(this.id == this.var_1.clientEntID)
         {
            this.var_1.method_1443(this.maxSpeed);
         }
      }
      
      public function method_1646() : void
      {
         var _loc1_:SuperAnimInstance = null;
         _loc1_ = new SuperAnimInstance(this.var_1,var_628,this.var_24 != null);
         _loc1_.m_TheDO.x = this.appearPosX;
         _loc1_.m_TheDO.y = this.appearPosY;
         this.var_1.playerEntLayer.addChildAt(_loc1_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.gfx.m_TheDO) + 1);
         if(SoundConfig.var_1987)
         {
            this.var_1.method_82(SoundConfig.var_1987,this.var_10,this.var_12);
         }
         this.gfx.m_Seq.method_34(Seq.C_EMOTE,"Appear",true);
      }
      
      public function method_1273() : void
      {
         this.var_1841 = this.var_1.mTimeThisTick;
      }
      
      public function method_407(param1:uint, param2:int) : void
      {
         var _loc3_:Level = this.var_1.level;
         var _loc4_:uint = _loc3_.bInstanced && !_loc3_.var_333 ? uint(this.var_64) : param1;
         var _loc5_:int = method_128(_loc4_) - method_128(this.var_64);
         this.baseMaxHP += _loc5_;
         this.maxHP += _loc5_;
         this.currHP += _loc5_;
         this.TakeDamage(-param2,true,null,null);
         this.mExpLevel = param1;
         this.var_64 = _loc4_;
         this.var_2384 = this.mExpLevel - this.var_64;
         if(this.id == this.var_1.clientEntID)
         {
            this.var_868 = 0;
            this.var_1.method_418(this.maxHP);
            this.var_1.method_184(this.currHP);
            this.var_1.method_439(param1,_loc4_);
         }
         this.ResetEntType(this.entType);
         if(this.var_309)
         {
            this.var_309.DestroySuperAnimInstance();
         }
         this.var_309 = new SuperAnimInstance(this.var_1,gtLevelUpFront,this.var_24 != null);
         this.var_309.m_TheDO.x = this.appearPosX;
         this.var_309.m_TheDO.y = this.appearPosY;
         this.var_1.playerEntLayer.addChildAt(this.var_309.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.gfx.m_TheDO) + 1);
         if(this.var_308)
         {
            this.var_308.DestroySuperAnimInstance();
         }
         this.var_308 = new SuperAnimInstance(this.var_1,gtLevelUpRear,this.var_24 != null);
         this.var_308.m_TheDO.x = this.appearPosX;
         this.var_308.m_TheDO.y = this.appearPosY;
         this.var_1.playerEntLayer.addChildAt(this.var_308.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.gfx.m_TheDO));
         if(SoundConfig.var_1947)
         {
            this.var_1.method_82(SoundConfig.var_1947,this.var_10,this.var_12);
         }
      }
      
      public function method_1663() : void
      {
         var _loc2_:class_37 = null;
         var _loc1_:Sprite = this.gfx.var_128;
         if(_loc1_)
         {
            if(Boolean(this.currSurface) || this.behaviorType.bNoPhysics)
            {
               _loc1_.x = this.appearPosX;
               _loc1_.y = this.appearPosY;
               _loc1_.alpha = 1;
            }
            else
            {
               var_718.x = 0;
               var_718.y = const_596;
               var_974.x = this.appearPosX + var_718.x;
               var_974.y = this.appearPosY + var_718.y;
               _loc2_ = this.var_1.collMan.getFloorCollision(0,this.appearPosX,this.appearPosY + 1,var_718,var_974,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0);
               _loc1_.x = var_974.x;
               _loc1_.y = var_974.y + this.yOffsetToSimulateZ;
               _loc1_.alpha = 1 - var_718.length / const_596;
               if(Boolean(_loc2_) && (Boolean(_loc2_.var_120 & class_37.const_439) || Boolean(_loc2_.var_120 & class_37.const_464)))
               {
                  _loc1_.alpha = 0;
               }
            }
            if(_loc1_.alpha > this.gfx.var_615)
            {
               _loc1_.alpha = this.gfx.var_615;
            }
            _loc1_.scaleX = this.gfx.m_Data.var_36.animScale * this.gfx.m_TheDO.scaleX;
            _loc1_.scaleY = this.gfx.m_Data.var_36.animScale;
            _loc1_.visible = this.gfx.var_151.visible;
            if(this.var_549)
            {
               _loc1_.visible = false;
            }
            if(this.var_997)
            {
               _loc1_.visible = false;
            }
         }
      }
      
      public function method_1590() : void
      {
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:SuperAnimInstance = null;
         var _loc6_:SuperAnimInstance = null;
         var _loc1_:Number = this.var_1.mTimeThisTick;
         var _loc2_:Boolean = false;
         if(this.var_549)
         {
            if(!this.gfx.var_285)
            {
               this.gfx.var_285 = new Rectangle(0,0,0,0);
            }
            if(!this.gfx.var_166 && Boolean(this.gfx.m_TheDO.parent))
            {
               if(this.var_2194)
               {
                  this.gfx.var_166 = new SuperAnimInstance(this.var_1,rippleGfxTypes[2],this.var_24 != null);
               }
               else
               {
                  this.gfx.var_166 = new SuperAnimInstance(this.var_1,rippleGfxTypes[1],this.var_24 != null);
               }
               _loc3_ = 1 + (this.entType.width / this.var_2247 - 1) * 0.5;
               if(_loc3_ > 1.5)
               {
                  _loc3_ = 1.5;
               }
               if(_loc3_ < 0.75)
               {
                  _loc3_ = 0.75;
               }
               this.gfx.var_166.m_TheDO.scaleX = _loc3_;
               _loc2_ = true;
            }
            if(this.gfx.var_166)
            {
               _loc4_ = this.gfx.m_TheDO.parent.getChildIndex(this.gfx.m_TheDO);
               this.var_1.playerEntLayer.addChildAt(this.gfx.var_166.m_TheDO,_loc4_ + 1);
            }
            if(Math.abs(this.gfx.m_TheDO.x - this.var_2454) > this.var_2890 || _loc2_)
            {
               (_loc5_ = this.method_589()).m_TheDO.x = this.gfx.m_TheDO.x;
               _loc5_.m_TheDO.y = this.gfx.m_TheDO.y - SuperAnimInstance.const_347;
               this.var_2691 = _loc1_;
               this.var_2454 = this.gfx.m_TheDO.x;
            }
         }
         else if(this.gfx.var_285)
         {
            this.gfx.var_285 = null;
         }
         if(!this.var_549 && Boolean(this.gfx.var_166))
         {
            (_loc6_ = this.method_589()).m_TheDO.x = this.gfx.var_166.m_TheDO.x;
            _loc6_.m_TheDO.y = this.gfx.var_166.m_TheDO.y;
            this.gfx.var_166.m_bFinished = true;
            this.gfx.var_166 = null;
         }
         if(this.gfx.var_166)
         {
            this.gfx.var_166.m_TheDO.x = this.gfx.m_TheDO.x;
            this.gfx.var_166.m_TheDO.y = this.gfx.m_TheDO.y - SuperAnimInstance.const_347;
         }
         if(!this.var_549)
         {
            this.var_2691 = 0;
         }
      }
      
      public function method_589() : SuperAnimInstance
      {
         var _loc2_:Number = NaN;
         var _loc1_:SuperAnimInstance = new SuperAnimInstance(this.var_1,rippleGfxTypes[0],this.var_24 != null);
         if(this.gfx.var_166)
         {
            _loc2_ = this.gfx.var_166.m_TheDO.parent.getChildIndex(this.gfx.var_166.m_TheDO);
            this.var_1.playerEntLayer.addChildAt(_loc1_.m_TheDO,_loc2_ + 1);
         }
         return _loc1_;
      }
      
      public function method_853() : void
      {
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         var _loc10_:int = 0;
         var _loc11_:Number = NaN;
         var _loc12_:int = 0;
         var _loc13_:Number = NaN;
         var _loc1_:Boolean = this.bLeftFacing;
         this.bLeftFacing = this.bLeft != this.bBackpedal;
         this.gfx.m_TheDO.scaleX = this.bLeftFacing == this.gfx.m_Data.var_36.var_522 ? 1 : -1;
         this.method_1663();
         this.method_1590();
         var _loc2_:Boolean = this.entState != const_6 && this.entType.var_832;
         var _loc3_:uint = 0;
         if(this.bRunning && (_loc2_ || !this.var_1170) && this.maxSpeed > 0)
         {
            _loc3_ |= Seq.RUNNING;
         }
         if(this.bDropping && !_loc2_ && !this.currSurface)
         {
            _loc3_ |= Seq.DROPPING;
         }
         if(this.bJumping && !_loc2_ && !this.bSmackingAWallOrCeiling)
         {
            _loc3_ |= Seq.JUMPING;
         }
         if(this.var_1170 && !_loc2_)
         {
            _loc3_ |= Seq.AIRBORNE;
         }
         this.var_2608 = this.entState == const_6 && Boolean(this.currSurface) && this.var_1.mTimeThisTick - this.var_217 >= 150;
         if(this.var_2608)
         {
            _loc3_ |= Seq.FINALSPLAT;
         }
         if(this.entState == const_6)
         {
            _loc3_ |= Seq.KOED;
         }
         if(this.combatState.var_683)
         {
            _loc3_ |= Seq.STUNNED;
         }
         if(this.combatState.var_445)
         {
            _loc3_ |= Seq.FROZEN;
         }
         if(this.combatState.var_1421)
         {
            _loc3_ |= Seq.const_663;
         }
         if(this.var_2358)
         {
            _loc3_ |= Seq.DROPPING;
            this.var_2358 = false;
         }
         if(this.var_2415)
         {
            _loc3_ |= Seq.NEW_JUMP;
         }
         if(this.bLeftFacing != _loc1_)
         {
            _loc3_ |= Seq.const_712;
         }
         if(!this.bLeftFacing && this.velocity.x > const_594 || this.bLeftFacing && this.velocity.x < -const_594)
         {
            _loc3_ |= Seq.const_649;
         }
         if(this.var_1875)
         {
            if(!this.combatState.var_270)
            {
               if((_loc7_ = this.var_1897 / this.maxHP) >= this.entType.var_1336)
               {
                  _loc3_ |= Seq.HIT_REACT;
               }
               if(this.entType.var_2538 && !this.var_91.x && _loc7_ >= const_829)
               {
                  if((_loc7_ -= const_829) > const_549)
                  {
                     _loc7_ = const_549;
                  }
                  _loc8_ = _loc7_ / const_549;
                  _loc9_ = const_1167 + _loc8_ * const_1064;
                  this.var_91.x = _loc9_ * this.var_2692;
               }
            }
            this.var_1897 = 0;
            this.var_1875 = false;
         }
         var _loc4_:Seq;
         (_loc4_ = this.gfx.m_Seq).var_1842 = this.var_549 ? 0.7 : 1;
         _loc4_.var_120 = _loc3_;
         var _loc5_:Boolean;
         var _loc6_:Boolean = (_loc5_ = Boolean(this.var_1.clientEnt) && Boolean(this.var_1.clientEnt.var_24) && this.var_1.PointOnScreenWithinDist(this.var_10,this.var_12,this.entType.width * 2,this.entType.height * 2)) && !this.method_503() && !this.var_822;
         if(this.gfx.m_TheDO.visible != _loc6_)
         {
            this.gfx.m_TheDO.visible = _loc6_;
         }
         if(this.gfx.var_128 && this.gfx.var_128.visible == true && this.gfx.var_128.visible != _loc6_)
         {
            this.gfx.var_128.visible = _loc6_;
         }
         if(this.entState == const_6 && !(this.var_20 & PLAYER) && !this.behaviorType.var_995 && !this.InActiveCutScene())
         {
            _loc10_ = this.var_1.mTimeThisTick - this.var_217;
            if((_loc11_ = (TIME_MONSTER_LAYS_DEAD_BEFORE_VANISHING - _loc10_) / MONSTER_FADE_TIME) < 1)
            {
               this.gfx.var_615 = Math.max(0,_loc11_);
               if(this.gfx.m_TheDO)
               {
                  this.gfx.m_TheDO.alpha = this.gfx.var_615;
               }
               if(this.gfx.var_128)
               {
                  this.gfx.var_128.alpha = this.gfx.var_615;
               }
            }
         }
         else if(this.gfx.var_615 < 1 || this.var_1.mTimeThisTick - this.var_1841 < const_835)
         {
            _loc12_ = this.var_1.mTimeThisTick - this.var_1841;
            if((_loc13_ = 0.05 + _loc12_ / const_835) > 1)
            {
               _loc13_ = 1;
            }
            else if(_loc13_ < 0.05)
            {
               _loc13_ = 0.05;
               this.var_1841 = this.var_1.mTimeThisTick;
            }
            this.gfx.var_615 = _loc13_;
            if(this.gfx.m_TheDO)
            {
               this.gfx.m_TheDO.alpha = this.gfx.var_615;
            }
            if(this.gfx.var_128)
            {
               this.gfx.var_128.alpha = this.gfx.var_615;
            }
         }
         else if(this.var_1878)
         {
            if((_loc11_ = (MONSTER_FADE_TIME + this.var_1878 - this.var_1.mTimeThisTick) / (2 * MONSTER_FADE_TIME)) < 1)
            {
               if(this.gfx.m_TheDO)
               {
                  this.gfx.m_TheDO.alpha = _loc11_;
               }
               if(this.gfx.var_128)
               {
                  this.gfx.var_128.alpha = _loc11_;
               }
               if(_loc11_ <= 0)
               {
                  this.var_1878 = 0;
                  this.var_822 = true;
               }
            }
         }
         if(Boolean(this.gfx.var_1854) && Boolean(this.gfx.m_TheDO))
         {
            if(this.gfx.m_TheDO.alpha > this.gfx.var_1854)
            {
               this.gfx.m_TheDO.alpha = this.gfx.var_1854;
            }
            if(this.gfx.var_128)
            {
               this.gfx.var_128.alpha = this.gfx.m_TheDO.alpha;
            }
         }
         if(Boolean(this.var_277) && this.var_277.visible != _loc6_)
         {
            this.var_277.visible = _loc6_;
         }
         if(Boolean(this.var_170) && this.var_170.visible != _loc6_)
         {
            this.var_170.visible = _loc6_;
         }
         if(Boolean(this.var_133) && this.var_133.visible != _loc6_)
         {
            this.var_133.visible = _loc6_;
         }
         this.method_1862();
      }
      
      public function method_1862() : void
      {
         var _loc1_:String = null;
         var _loc2_:String = null;
         if(this.entState != const_6 && this.bRunning && !this.var_1170 && this == this.var_1.clientEnt)
         {
            if(this.var_549)
            {
               _loc1_ = SoundConfig.var_2350;
            }
            else if(this.var_1760)
            {
               _loc1_ = SoundConfig.var_2317;
            }
            else if(this.var_1933)
            {
               _loc1_ = SoundConfig.var_2165;
            }
            else if(this.var_1836)
            {
               _loc1_ = SoundConfig.var_2271;
            }
            else if(this.var_1932)
            {
               _loc1_ = SoundConfig.var_2407;
            }
            else if(this.entType.className == "Mage")
            {
               _loc1_ = SoundConfig.var_2340;
            }
            else if(this.entType.className == "Paladin")
            {
               _loc1_ = SoundConfig.var_2166;
            }
            else if(this.entType.className == "Rogue")
            {
               _loc1_ = SoundConfig.var_2016;
            }
         }
         if(this.var_2545 >= this.var_1.mTimeThisTick && this == this.var_1.clientEnt)
         {
            if(this.var_549)
            {
               if(SoundConfig.var_1949)
               {
                  _loc2_ = SoundConfig.var_1949;
               }
            }
            else if(this.var_1760)
            {
               if(SoundConfig.var_1750)
               {
                  _loc2_ = SoundConfig.var_1750;
               }
            }
            else if(this.var_1933)
            {
               if(SoundConfig.var_1844)
               {
                  _loc2_ = SoundConfig.var_1844;
               }
            }
            else if(this.var_1836)
            {
               if(SoundConfig.var_1734)
               {
                  _loc2_ = SoundConfig.var_1734;
               }
            }
            else if(this.var_1932)
            {
               if(SoundConfig.var_1782)
               {
                  _loc2_ = SoundConfig.var_1782;
               }
            }
            else if(SoundConfig.var_1716)
            {
               _loc2_ = SoundConfig.var_1716;
            }
         }
         if(_loc1_ != this.var_2028)
         {
            if(this.var_746)
            {
               this.var_746 = SoundManager.method_155(this.var_746);
            }
            if(_loc1_)
            {
               this.var_746 = SoundManager.Play(_loc1_,1,true);
            }
         }
         if(_loc2_)
         {
            SoundManager.Play(_loc2_,1,false);
         }
         this.var_2028 = _loc1_;
      }
      
      public function bFacingLeft() : Boolean
      {
         return this.bLeft != this.bBackpedal;
      }
      
      public function method_1690(param1:Number, param2:Number) : void
      {
         var _loc3_:Number = this.var_12 - param2;
         var _loc4_:Number = param1 - this.var_10;
         var _loc5_:String = this.gfx.m_Seq.method_869(_loc3_,_loc4_);
         this.gfx.m_Seq.method_34(Seq.C_USEPOWER,_loc5_,false);
      }
      
      public function method_252(param1:PowerType) : Boolean
      {
         return Boolean(param1) && this.combatState.method_51(param1,false);
      }
      
      public function method_186(param1:Point) : Point
      {
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:GfxType = null;
         var _loc2_:Point = !!this.gfx.m_Seq ? this.gfx.m_Seq.var_314.var_1807 : null;
         if(_loc2_ != null)
         {
            _loc3_ = _loc2_.x;
            _loc4_ = _loc2_.y;
            if((_loc5_ = this.gfx.m_Data.var_36).var_522)
            {
               _loc3_ = -_loc3_;
            }
            _loc3_ *= _loc5_.animScale;
            _loc4_ *= _loc5_.animScale;
            param1.x = this.appearPosX + _loc3_;
            param1.y = this.appearPosY + _loc4_;
            return param1;
         }
         param1.x = this.var_10;
         param1.y = this.var_12;
         return param1;
      }
      
      public function method_219(param1:Point, param2:String = "Shoot") : Point
      {
         var _loc11_:Number = NaN;
         var _loc12_:Number = NaN;
         var _loc3_:String = param2;
         if(_loc3_ != "Shoot")
         {
            param1 = null;
         }
         else if(param1)
         {
            _loc11_ = this.var_12 - param1.y;
            _loc12_ = param1.x - this.var_10;
            _loc3_ = this.gfx.m_Seq.method_869(_loc11_,_loc12_);
         }
         if(!_loc3_ || !this.gfx.m_Seq)
         {
            return this.method_186(new Point());
         }
         var _loc5_:class_26;
         var _loc4_:Dictionary;
         if(!(_loc5_ = (_loc4_ = this.gfx.m_Seq.var_71.var_69)[_loc3_]))
         {
            _loc5_ = _loc4_["Shoot"];
         }
         if(!_loc5_)
         {
            return this.method_186(new Point());
         }
         var _loc6_:int = int(_loc5_.var_751);
         var _loc7_:class_28;
         if(!(_loc7_ = _loc5_.var_604[_loc6_]))
         {
            _loc7_ = _loc5_.method_242(_loc6_);
         }
         var _loc8_:Point;
         if(!(_loc8_ = _loc7_.var_2381))
         {
            return this.method_186(new Point());
         }
         var _loc9_:Number = _loc8_.x;
         var _loc10_:Number = _loc8_.y;
         if(Boolean(param1) && !this.behaviorType.bNoAutoFace)
         {
            _loc9_ = param1.x < this.appearPosX ? -_loc9_ : _loc9_;
         }
         else if(this.bFacingLeft())
         {
            _loc9_ = -_loc9_;
         }
         if(this.gfx.m_Data.var_36.var_522)
         {
            _loc9_ = -_loc9_;
         }
         _loc9_ *= this.gfx.m_Data.var_36.animScale;
         _loc10_ *= this.gfx.m_Data.var_36.animScale;
         return new Point(this.appearPosX + _loc9_,this.appearPosY + _loc10_);
      }
      
      public function method_1510(param1:uint) : void
      {
         this.var_1.screenHud.method_1266(param1);
         if(this.var_859 < 4294967295 - param1)
         {
            this.var_859 += param1;
         }
         if(this.id == this.var_1.clientEntID)
         {
            this.var_1.method_764(this.var_859);
         }
         var _loc2_:uint = uint(this.mExpLevel);
         while(_loc2_ < MAX_CHAR_LEVEL && this.var_859 >= EXPERIENCE_TABLE[_loc2_ + 1])
         {
            _loc2_++;
         }
         if(_loc2_ != this.mExpLevel)
         {
            this.var_1.var_2344.Display();
            if(DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT)
            {
               this.method_407(_loc2_,this.maxHP - this.currHP);
            }
            else
            {
               this.method_407(_loc2_,0);
            }
            this.var_1.method_263();
            this.var_1.screenHud.Refresh();
         }
      }
      
      public function GainMoney(param1:int, param2:Boolean) : void
      {
         if(param2)
         {
            this.var_1.bSuppressGoldDisplay = true;
         }
         this.currGold += param1;
         if(this.currGold > Game.const_579)
         {
            this.currGold = Game.const_579;
         }
      }
      
      public function method_2124(param1:int) : void
      {
         this.currGems += param1;
      }
      
      public function method_1796(param1:uint, param2:uint, param3:Boolean) : void
      {
         var _loc5_:class_76 = null;
         var _loc6_:String = null;
         var _loc4_:class_8;
         if(_loc4_ = class_14.var_629[param1])
         {
            if(!(_loc5_ = this.var_1.mOwnedMaterials[param1]))
            {
               _loc5_ = new class_76(0,_loc4_);
               this.var_1.mOwnedMaterials[param1] = _loc5_;
            }
            _loc5_.var_181 += param2;
            if(!param3)
            {
               _loc6_ = "";
               if(param2 > 1)
               {
                  _loc6_ = " x" + param2;
               }
               this.var_1.screenNotification.ShowNotification(class_46.const_726,_loc4_.displayName + _loc6_,_loc4_.var_139,true,_loc4_.var_103);
            }
            this.var_1.screenArmory.Refresh();
         }
      }
      
      public function SpendMaterial(param1:uint, param2:uint) : void
      {
         var _loc3_:class_76 = this.var_1.mOwnedMaterials[param1];
         if(!_loc3_)
         {
            return;
         }
         _loc3_.var_181 -= param2;
         if(_loc3_.var_181 <= 0)
         {
            _loc3_.method_626();
            delete this.var_1.mOwnedMaterials[param1];
            this.var_1.screenArmory.Refresh();
         }
      }
      
      public function GainMount(param1:uint, param2:Boolean) : void
      {
         var _loc4_:String = null;
         var _loc3_:class_20 = class_14.var_464[param1];
         if(!_loc3_)
         {
            return;
         }
         this.var_1.mOwnedMounts[_loc3_.var_197] = _loc3_;
         if(!this.mEquipMount)
         {
            this.method_525(_loc3_);
         }
         if(!param2)
         {
            _loc4_ = "Mount:" + _loc3_.var_566;
            this.var_1.screenNotification.ShowNotification(class_46.const_761,_loc3_.displayName,_loc3_.var_255,true,null,_loc4_);
         }
      }
      
      public function GainNewGear(param1:uint, param2:uint, param3:Boolean) : void
      {
         var _loc4_:class_42 = null;
         var _loc7_:uint = 0;
         var _loc8_:String = null;
         var _loc9_:GearType = null;
         var _loc10_:uint = 0;
         var _loc5_:class_42;
         if(!(_loc5_ = this.var_1.mOwnedGear[param1]))
         {
            _loc4_ = this.var_1.method_532(param1,param2,0,0,0,true,0,0);
         }
         else
         {
            _loc7_ = uint(GearType.var_603[_loc5_.gearType.var_8]);
            _loc8_ = Game.method_110(param1,param2);
            _loc9_ = class_14.var_421[_loc8_];
            _loc5_.gearType = _loc9_;
            if((_loc10_ = uint(this.var_1.var_144.indexOf(_loc5_))) <= -1)
            {
               return;
            }
            this.var_1.var_144.splice(_loc10_,1);
            this.var_1.var_144.push(_loc5_);
            this.var_1.mFilteredOwnedGear = this.var_1.var_144;
            delete this.var_1.mOwnedGear2[Game.method_110(param1,_loc7_)];
            this.var_1.mOwnedGear2[_loc8_] = _loc5_;
            this.var_1.screenArmory.method_601();
            (_loc4_ = _loc5_).var_1814 = true;
         }
         if(!_loc4_)
         {
            return;
         }
         ++this.var_1.var_1081;
         this.var_1.method_709();
         if(!param3)
         {
            this.var_1.screenNotification.ShowNotification(class_46.const_828,_loc4_.gearType.displayName,_loc4_.gearType.var_8);
         }
         this.var_1.screenHudTop.method_1660();
         _loc9_ = _loc4_.gearType;
         var _loc6_:uint = uint(EntType.method_87(_loc9_.type));
         if(!this.mEquipGear[_loc6_])
         {
            this.var_1.linkUpdater.WriteUpdateSingleGear(this,_loc6_,param1);
            this.method_303(_loc6_,_loc9_.gearID);
         }
         if(this.var_1.screenArmory.method_1032())
         {
            this.var_1.screenArmory.var_73.method_119();
            this.var_1.screenArmory.OnInitDisplay();
            this.var_1.screenArmory.Refresh();
         }
      }
      
      public function TakeDamage(param1:int, param2:Boolean, param3:Entity = null, param4:PowerType = null, param5:uint = 0) : void
      {
         var _loc6_:Boolean = false;
         var _loc7_:PowerType = null;
         var _loc8_:BuffType = null;
         var _loc9_:Buff = null;
         var _loc10_:PowerType = null;
         var _loc11_:PowerType = null;
         var _loc12_:int = 0;
         var _loc13_:int = 0;
         var _loc14_:PowerType = null;
         var _loc15_:Buff = null;
         var _loc16_:int = 0;
         var _loc17_:PowerType = null;
         var _loc18_:int = 0;
         var _loc19_:int = 0;
         var _loc20_:Buff = null;
         var _loc21_:PowerType = null;
         var _loc22_:int = 0;
         var _loc23_:Packet = null;
         var _loc24_:PowerType = null;
         var _loc25_:Buff = null;
         var _loc26_:class_141 = null;
         var _loc27_:String = null;
         var _loc28_:Boolean = false;
         var _loc29_:Boolean = false;
         var _loc30_:uint = 0;
         var _loc31_:Boolean = false;
         var _loc32_:Boolean = false;
         var _loc33_:String = null;
         var _loc34_:uint = 0;
         var _loc35_:Number = NaN;
         var _loc36_:* = false;
         var _loc37_:Boolean = false;
         if(!this.bIAmValid || !param1)
         {
            return;
         }
         _loc6_ = false;
         if(param4)
         {
            if(param4 == class_14.powerTypesDict["ProcCriticalHit"])
            {
               _loc6_ = true;
            }
            if(Boolean(this.var_20 & LOCAL) && Boolean(param3))
            {
               if(this.combatState.var_1710)
               {
                  _loc10_ = this.GetPowerFromAbilityType(class_14.var_704["Retribution"]);
                  _loc11_ = class_14.powerTypesDict["ProcRetribution"];
                  _loc12_ = this.magicDamage;
                  if(this.combatState.var_552)
                  {
                     if(this.combatState.var_552 >= 7)
                     {
                        _loc8_ = class_14.buffTypesDict["Retribution7"];
                     }
                     else if(Boolean(this.combatState.var_552) && this.combatState.var_552 < 3)
                     {
                        _loc8_ = class_14.buffTypesDict["Retribution1"];
                     }
                     else
                     {
                        _loc8_ = class_14.buffTypesDict["Retribution"];
                     }
                     _loc9_ = this.combatState.method_135(_loc8_);
                     if(this.combatState.var_552 >= 10)
                     {
                        _loc12_ = this.magicDamage * 1.55;
                     }
                     else if(this.combatState.var_552 >= 6)
                     {
                        _loc12_ = this.magicDamage * 1.3;
                     }
                     else if(this.combatState.var_552 >= 5)
                     {
                        _loc12_ = this.magicDamage * 1.23;
                     }
                     else if(this.combatState.var_552 == 1)
                     {
                        _loc12_ = this.magicDamage * 0.8;
                     }
                  }
                  else
                  {
                     _loc8_ = class_14.buffTypesDict["Retribution"];
                  }
                  if(_loc9_ && param1 > 0 && param4 != _loc11_)
                  {
                     _loc13_ = _loc9_.method_357(_loc12_);
                     this.combatState.method_72(_loc11_,param3,new Point(param3.var_10,param3.var_12),_loc13_,_loc11_.powerID);
                     if(_loc9_.var_1114)
                     {
                        this.combatState.RemoveBuff(_loc8_);
                     }
                  }
               }
               if(!param4.bIsProjectile && !param4.var_301)
               {
                  _loc14_ = class_14.powerTypesDict["ProcRetribution"];
                  if(this.combatState.var_1674)
                  {
                     if((Boolean(_loc15_ = this.combatState.method_135(class_14.buffTypesDict["Thorns"]))) && param1 > 0)
                     {
                        _loc16_ = _loc15_.method_357(this.magicDamage);
                        this.combatState.method_72(_loc14_,param3,new Point(param3.var_10,param3.var_12),_loc16_,_loc14_.powerID);
                     }
                     if(_loc15_.var_1114)
                     {
                        this.combatState.RemoveBuff(class_14.buffTypesDict["Thorns"]);
                     }
                  }
                  if(this.combatState.var_1455 && param3 && Boolean(param3.combatState.var_1234))
                  {
                     _loc17_ = class_14.powerTypesDict["FireShield" + this.combatState.var_1455];
                     this.combatState.method_46(_loc17_,param3,new Point(param3.var_10,param3.var_12),true);
                  }
               }
               if(param4.basePowerName == "ShadowBlade")
               {
                  if(_loc18_ = this.combatState.var_1032)
                  {
                     this.combatState.RemoveBuff(class_14.buffTypesDict["Bleeding"]);
                  }
               }
            }
            if(Boolean(this.var_20 & LOCAL) && Boolean(this.combatState.var_651))
            {
               _loc19_ = this.combatState.var_651;
               if((Boolean(_loc20_ = this.combatState.method_135(class_14.buffTypesDict["DetShield" + _loc19_]))) && param1 > 0)
               {
                  _loc21_ = class_14.powerTypesDict["Barrier" + _loc19_];
                  _loc22_ = _loc20_.method_357(param1);
                  this.TakeDamage(-_loc22_,true,this,_loc21_,_loc21_.powerID);
                  (_loc23_ = new Packet(LinkUpdater.PKTTYPE_CHAR_REGEN)).method_9(this.id);
                  _loc23_.method_24(_loc22_);
                  this.var_1.serverConn.SendPacket(_loc23_);
                  if(_loc20_.var_1114)
                  {
                     _loc24_ = class_14.powerTypesDict["DetShieldDetonate" + _loc19_];
                     this.combatState.method_51(_loc24_,false);
                     this.combatState.RemoveBuff(class_14.buffTypesDict["DetShield" + _loc19_]);
                  }
               }
            }
            if(this.combatState.var_2246)
            {
               if(param1 > this.maxHP * 0.2)
               {
                  param1 = this.maxHP * 0.2;
               }
            }
            if(param1 < 0)
            {
               param1 *= this.combatState.var_1139;
               if(param1 > 0)
               {
                  if(_loc25_ = this.combatState.method_135(class_14.buffTypesDict["Doomed"]))
                  {
                     _loc26_ = _loc25_.var_47[0];
                     param3 = this.var_1.GetEntFromID(_loc26_.entID);
                     param2 = false;
                     this.combatState.RemoveBuff(class_14.buffTypesDict["Doomed"]);
                  }
               }
            }
         }
         Game.var_172.method_175(!!param4 ? param4 : class_14.powerTypes[param5],param3,this,param1,false,param4 != null);
         this.currHP -= param1;
         if(this.id == this.var_1.clientEntID)
         {
            this.var_1.method_184(this.currHP);
            _loc27_ = !!param4 ? param4.powerName : "unknown";
            if(param3)
            {
               if(param3.id == this.var_1.clientEntID)
               {
                  this.var_1.method_389();
               }
               else if(param3.summonerId == this.var_1.clientEntID)
               {
                  this.var_1.method_389();
               }
               else if(Boolean(param4) && param4.var_275)
               {
                  this.var_1.method_389();
               }
            }
            else
            {
               this.var_1.method_389();
            }
         }
         if((Boolean(_loc7_ = class_14.powerTypes[param5])) && _loc7_.var_2900)
         {
            this.method_280();
         }
         else if(!param2)
         {
            _loc29_ = (_loc28_ = param3 && param4 && param3.var_353 != param4 && param3.var_280 != param4) && param4.var_301;
            _loc31_ = false;
            if(param1 < 0)
            {
               _loc30_ = 65280;
               _loc31_ = true;
               _loc28_ = false;
               if(_loc29_)
               {
                  this.var_351 -= 20;
               }
            }
            else
            {
               if(_loc6_)
               {
                  _loc30_ = 16763904;
                  _loc29_ = false;
               }
               else if(_loc29_)
               {
                  this.var_351 -= 30;
                  _loc30_ = 16763904;
               }
               else if(_loc28_)
               {
                  this.var_596 = -this.var_596 * 1.3;
                  this.var_351 = -this.var_351 * 1.1;
                  _loc30_ = this.team == GOODGUY ? 16400195 : 16776977;
               }
               else
               {
                  this.var_596 = -this.var_596;
                  _loc30_ = this.team == GOODGUY ? 16400195 : 16750848;
               }
               if(!_loc29_ && Boolean(param4))
               {
                  this.var_2841 = this.var_1.mTimeThisTick;
               }
            }
            _loc32_ = false;
            if(this.var_1.bShowGroupFloaters && param3 && Boolean(param3.var_20 & Entity.PLAYER))
            {
               _loc33_ = param3.entType.entName;
               _loc32_ = this.method_611(param3.entType.entName);
            }
            if(this == this.var_1.clientEnt || param3 == this.var_1.clientEnt || param3 && param3.behaviorType && param3.behaviorType.var_332 && param3.summonerId == this.var_1.clientEntID || _loc32_)
            {
               _loc34_ = 0;
               if(Boolean(param4) && param4.basePowerName == "ShadowStepClose")
               {
                  _loc34_ = 200;
               }
               if(_loc22_)
               {
                  this.var_1.method_527(-(param1 - _loc22_),this.gfx.m_TheDO.x + this.var_596,this.gfx.m_TheDO.y - this.entType.height + this.var_351,_loc30_,_loc28_,_loc31_,_loc29_,_loc6_,_loc34_);
                  _loc30_ = 10053375;
                  this.var_1.method_527(-_loc22_,this.gfx.m_TheDO.x + this.var_596,this.gfx.m_TheDO.y - this.entType.height + this.var_351 - 30,_loc30_,false,false,false,_loc6_,_loc34_);
               }
               else
               {
                  this.var_1.method_527(-param1,this.gfx.m_TheDO.x + this.var_596,this.gfx.m_TheDO.y - this.entType.height + this.var_351,_loc30_,_loc28_,_loc31_,_loc29_,_loc6_,_loc34_);
               }
            }
            this.method_280();
            if(this.var_596 > 50)
            {
               this.var_596 = const_1045;
            }
            if(this.var_351 > 50)
            {
               this.var_351 = const_461;
            }
            if(_loc29_)
            {
               this.var_351 = const_461;
            }
         }
         if(this.currHP <= 0)
         {
            if(this.entState != const_6)
            {
               Game.var_172.method_410(param4,param3,this);
               this.entState = const_6;
               this.var_217 = this.var_1.mTimeThisTick;
               if(Boolean(this.cue) && Boolean(this.cue.room))
               {
                  this.cue.defeatTick = this.cue.room.mRoomTick;
               }
               if(param3 && param3.var_99 && Boolean(param3.summonerId))
               {
                  this.var_2265 = param3.summonerId;
                  this.var_2233 = param3.var_99.powerID;
               }
               else
               {
                  this.var_2265 = !!param3 ? param3.id : 0;
                  this.var_2233 = param5;
               }
               if(Boolean(this.gfx) && Boolean(this.gfx.m_Seq))
               {
                  this.gfx.m_Seq.method_428();
               }
               if(this.entType.var_1635)
               {
                  this.var_1.method_82(this.entType.var_1635,this.var_10,this.var_12,0.5 + Math.random() * 0.5);
               }
               if(!(this.var_20 & PLAYER) && !this.behaviorType.var_72)
               {
                  if(param3 && param4 && !param4.var_2520)
                  {
                     if(param3.combatState.var_39 == class_14.powerTypesDict["SentinelForm1"].powerID)
                     {
                        this.var_91.x = 30 + Math.random() * 15;
                        this.var_91.y = -20 - Math.random() * 10;
                     }
                     else
                     {
                        this.var_91.x = 20 + Math.random() * 5;
                        this.var_91.y = -15 - Math.random() * 5;
                     }
                     if(this.appearPosX < param3.appearPosX)
                     {
                        this.var_91.x = -this.var_91.x;
                     }
                  }
                  else if(this.entType.var_832)
                  {
                     this.var_91.y = -10;
                     this.var_1460 = true;
                  }
               }
               if(this.var_38)
               {
                  this.var_602 = true;
               }
               else
               {
                  if(Boolean(DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT) && Boolean(this.var_20 & PLAYER))
                  {
                     ++this.var_1.level.var_1270;
                  }
                  if(Boolean(this.cue) && Boolean(this.cue.sayOnDeath))
                  {
                     this.StartSkit(this.cue.sayOnDeath,false,!!this.brain ? this.brain.mostHatedEnt : null);
                  }
                  this.method_1727();
               }
            }
         }
         else
         {
            if(this.entState == const_6)
            {
               this.entState = const_78;
               if(this.var_38)
               {
                  this.var_602 = false;
               }
            }
            _loc35_ = 0.5 + Math.random() * 0.5;
            if(_loc37_ = (_loc36_ = this.currHP < this.maxHP * 0.33) && this.var_2843)
            {
               this.var_2843 = false;
               if(this.brain && this.cue && Boolean(this.cue.sayOnBloodied))
               {
                  this.StartSkit(this.cue.sayOnBloodied,false,this.brain.mostHatedEnt);
               }
            }
            if(_loc37_ && Boolean(this.entType.var_1452))
            {
               this.var_1.method_82(this.entType.var_1452,this.var_10,this.var_12,_loc35_);
            }
            else if(Boolean(param4) && Boolean(this.entType.var_738))
            {
               if(this.var_1.mTimeThisTick - this.var_2471 > 1000)
               {
                  this.var_2471 = this.var_1.mTimeThisTick;
                  this.var_1.method_82(this.entType.var_738,this.var_10,this.var_12,_loc35_);
               }
            }
         }
      }
      
      public function method_1727() : void
      {
         var _loc1_:Number = NaN;
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:String = null;
         var _loc5_:uint = 0;
         var _loc6_:Entity = null;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc11_:uint = 0;
         var _loc12_:* = false;
         var _loc13_:* = false;
         var _loc14_:* = false;
         var _loc15_:* = false;
         var _loc16_:Number = NaN;
         var _loc17_:Number = NaN;
         var _loc18_:Number = NaN;
         var _loc19_:Number = NaN;
         var _loc20_:Number = NaN;
         var _loc21_:Number = NaN;
         var _loc22_:Number = NaN;
         var _loc23_:uint = 0;
         var _loc24_:uint = 0;
         var _loc25_:uint = 0;
         var _loc26_:uint = 0;
         var _loc27_:Point = null;
         var _loc28_:Point = null;
         var _loc29_:class_37 = null;
         var _loc30_:int = 0;
         var _loc31_:class_87 = null;
         var _loc32_:uint = 0;
         var _loc33_:Number = NaN;
         var _loc34_:Number = NaN;
         var _loc35_:uint = 0;
         var _loc36_:uint = 0;
         var _loc37_:uint = 0;
         var _loc38_:String = null;
         var _loc39_:Array = null;
         var _loc40_:int = 0;
         var _loc41_:String = null;
         var _loc42_:Array = null;
         var _loc43_:String = null;
         var _loc44_:Array = null;
         var _loc45_:Number = NaN;
         var _loc46_:Array = null;
         var _loc47_:Number = NaN;
         var _loc48_:Number = NaN;
         var _loc49_:Number = NaN;
         var _loc50_:Number = NaN;
         var _loc51_:Number = NaN;
         var _loc52_:Number = NaN;
         var _loc53_:Number = NaN;
         var _loc54_:Number = NaN;
         var _loc55_:Number = NaN;
         if(!this.brain)
         {
            return;
         }
         _loc1_ = 1;
         _loc2_ = 1;
         _loc3_ = 1;
         if(!this.var_1.level.bInstanced)
         {
            _loc1_ = 0.25;
            _loc2_ = 0.1;
         }
         else if(this.entType.var_913)
         {
            _loc3_ = 1.5;
         }
         for(_loc4_ in this.brain.var_792)
         {
            _loc5_ = uint(_loc4_);
            if(!(!(_loc6_ = this.var_1.GetEntFromID(_loc5_)) || !(_loc6_.var_20 & Entity.PLAYER)))
            {
               _loc7_ = this.physPosX;
               _loc8_ = this.physPosY;
               if(Boolean(this.currRoom) && _loc8_ < this.currRoom.var_1266)
               {
                  _loc27_ = new Point(0,this.currRoom.var_1266 - _loc8_);
                  _loc28_ = new Point(0,0);
                  if(_loc29_ = this.var_1.collMan.getFloorCollision(0,_loc7_,_loc8_,_loc27_,_loc28_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0))
                  {
                     _loc7_ = _loc28_.x;
                     _loc8_ = _loc28_.y - Entity.PULLBACK_DIST;
                  }
               }
               _loc9_ = 0;
               _loc10_ = 0;
               _loc11_ = 0;
               _loc12_ = false;
               _loc13_ = false;
               _loc14_ = false;
               _loc15_ = false;
               _loc16_ = 1;
               _loc17_ = 1;
               _loc18_ = 0;
               _loc19_ = 0;
               _loc20_ = 0;
               _loc21_ = 0;
               _loc22_ = 0;
               _loc23_ = 0;
               _loc24_ = Entity.PLAYER_HITPOINTS[this.var_64] * this.entType.var_1109;
               if(!this.var_2305)
               {
                  if((_loc30_ = this.var_64 + _loc6_.var_2384) > MAX_CHAR_LEVEL)
                  {
                     _loc30_ = int(MAX_CHAR_LEVEL);
                  }
                  else if(_loc30_ < 1)
                  {
                     _loc30_ = 1;
                  }
                  if(_loc31_ = _loc6_.mEquipPet)
                  {
                     _loc35_ = _loc31_.var_23;
                     _loc23_ = Math.floor(this.entType.var_1036 * class_7.method_1520(_loc35_) * _loc2_);
                  }
                  _loc32_ = 4 * this.entType.var_1036 * MONSTER_EXP_TABLE[_loc6_.mExpLevel];
                  _loc9_ = this.entType.var_1036 * MONSTER_EXP_TABLE[_loc30_];
                  if((_loc9_ = Math.ceil(_loc9_ * (1 + _loc6_.totalMods.var_697))) > _loc32_)
                  {
                     _loc9_ = _loc32_;
                  }
                  _loc33_ = Math.random();
                  _loc34_ = this.entType.var_1817;
                  if(_loc33_ < _loc34_)
                  {
                     _loc36_ = this.entType.var_1594 * MONSTER_GOLD_TABLE[_loc6_.mExpLevel];
                     if((_loc10_ = this.entType.var_1594 * MONSTER_GOLD_TABLE[_loc30_] * 0.5 * _loc3_ * _loc1_) > _loc36_)
                     {
                        _loc10_ = _loc36_;
                     }
                  }
                  if(Boolean(this.cue) && Boolean(this.cue.itemDrop))
                  {
                     _loc37_ = this.var_1.level.mapLevel;
                     _loc38_ = _loc6_.entType.className;
                     _loc39_ = this.cue.itemDrop.split("|");
                     _loc40_ = Math.random() * _loc39_.length;
                     _loc42_ = (_loc41_ = String(_loc39_[_loc40_])).split(",");
                     for each(_loc43_ in _loc42_)
                     {
                        if(!_loc43_.indexOf("Gold"))
                        {
                           _loc45_ = (_loc44_ = _loc43_.split("_")).length <= 1 ? 1 : Number(_loc44_[1]);
                           _loc10_ = MONSTER_GOLD_TABLE[_loc37_] * 0.5 * _loc45_;
                        }
                        else if(!_loc43_.indexOf("Health"))
                        {
                           _loc47_ = (_loc46_ = _loc43_.split("_")).length <= 1 ? 1 : Number(_loc46_[1]);
                           _loc24_ = method_128(_loc37_) * _loc47_;
                        }
                     }
                  }
                  else if(this.entType.var_2198)
                  {
                     _loc48_ = Math.random();
                     _loc49_ = this.entType.var_2198 * _loc1_;
                     _loc12_ = _loc48_ < _loc49_;
                     _loc16_ = 1 + _loc6_.totalMods.itemDrop;
                  }
                  if(this.entType.var_2809)
                  {
                     _loc50_ = Math.random();
                     _loc51_ = EntType.const_247[this.entType.var_138] * _loc1_;
                     _loc13_ = _loc50_ < _loc51_;
                     _loc17_ = 1 + _loc6_.totalMods.var_152;
                  }
                  if(this.entType.var_2604)
                  {
                     _loc52_ = Math.random();
                     _loc53_ = _loc1_;
                     _loc14_ = _loc52_ < _loc53_;
                  }
                  if(this.entType.var_2783)
                  {
                     _loc54_ = Math.random();
                     _loc55_ = EntType.const_267[this.entType.var_138] * _loc1_;
                     _loc15_ = _loc54_ < _loc55_;
                  }
               }
               _loc25_ = _loc24_ + _loc24_ * (_loc6_.totalMods.var_1695 + _loc6_.var_237 + _loc6_.combatState.var_546);
               _loc26_ = _loc10_ + uint((_loc10_ * 2 + 1) * Math.random());
               if(_loc9_)
               {
                  _loc26_ = Math.ceil(_loc26_ * (1 + _loc6_.totalMods.var_79));
               }
               _loc6_.method_1944(this,_loc7_,_loc8_,_loc12_,_loc13_,_loc17_,_loc9_,_loc26_,_loc25_,_loc16_,_loc23_,_loc14_,_loc15_);
            }
         }
         this.var_2305 = true;
      }
      
      public function method_1944(param1:Entity, param2:Number, param3:Number, param4:Boolean, param5:Boolean, param6:Number, param7:uint, param8:uint, param9:uint, param10:Number, param11:uint, param12:Boolean, param13:Boolean) : void
      {
         var _loc14_:Packet = null;
         (_loc14_ = new Packet(LinkUpdater.PKTTYPE_GRANT_REWARD)).method_9(this.id);
         _loc14_.method_9(param1.id);
         _loc14_.method_15(param4);
         _loc14_.method_309(param10);
         _loc14_.method_15(param5);
         _loc14_.method_309(param6);
         _loc14_.method_15(param12);
         _loc14_.method_15(param13);
         _loc14_.method_9(param7);
         _loc14_.method_9(param11);
         _loc14_.method_9(param9);
         _loc14_.method_9(param8);
         _loc14_.method_24(param2);
         _loc14_.method_24(param3);
         if(param1.var_2265 != this.id)
         {
            _loc14_.method_15(false);
         }
         else
         {
            _loc14_.method_15(true);
            _loc14_.method_9(param1.var_2233);
         }
         this.var_1.serverConn.SendPacket(_loc14_);
      }
      
      public function method_819() : void
      {
         if(this.var_389)
         {
            this.var_389.graphics.clear();
            this.var_389.graphics.beginFill(8947712,0.5);
            this.var_389.graphics.drawRoundRect(this.appearPosX - 0.5 * this.entType.width,this.appearPosY - this.entType.height,this.entType.width,this.entType.height,this.entType.width,this.entType.width);
            this.var_389.graphics.endFill();
         }
      }
      
      public function method_525(param1:class_20) : void
      {
         this.mEquipMount = param1;
         this.ResetEntType(this.entType);
         this.var_1.screenHud.var_2062 = true;
      }
      
      public function ChangePet(param1:class_87) : void
      {
         if(this.combatState.var_823)
         {
            this.method_343();
         }
         this.mEquipPet = param1;
         this.ResetEntType(this.entType);
         this.var_1.screenHud.var_2091 = true;
      }
      
      public function method_190(param1:class_3) : void
      {
         this.mCurrPotion = param1;
         this.ResetEntType(this.entType);
      }
      
      public function ChangeRestingPets(param1:uint, param2:class_87) : void
      {
         this.var_329[param1] = param2;
         this.ResetEntType(this.entType);
      }
      
      public function method_319(param1:uint, param2:uint) : void
      {
         var _loc3_:uint = 0;
         var _loc4_:class_42 = null;
         _loc3_ = this.mEquipGear[param1];
         if(_loc3_ == param2)
         {
            return;
         }
         if(_loc4_ = this.var_1.mOwnedGear[param2])
         {
            this.entType.equippedGear[param1] = _loc4_.method_908();
         }
         else
         {
            this.entType.equippedGear[param1] = new EntTypeGear("No" + this.entType.className + EntType.method_523(param1),0,0,0);
         }
         this.mEquipGear[param1] = param2;
      }
      
      public function method_303(param1:uint, param2:uint) : void
      {
         this.method_319(param1,param2);
         this.entType.gfxType = this.entType.method_60();
         this.ResetEntType(this.entType);
      }
      
      public function method_1899(param1:Vector.<uint>) : void
      {
         var _loc2_:uint = 0;
         _loc2_ = 1;
         while(_loc2_ < EntType.MAX_SLOTS)
         {
            this.method_319(_loc2_,param1[_loc2_]);
            _loc2_++;
         }
         this.entType.gfxType = this.entType.method_60();
         this.ResetEntType(this.entType);
      }
      
      public function method_1439(param1:String, param2:String, param3:String, param4:String, param5:String, param6:uint, param7:uint) : void
      {
         this.entType.var_760 = param1;
         this.entType.var_857 = param2;
         this.entType.var_769 = param3;
         this.entType.var_779 = param4;
         this.entType.var_855 = param6;
         this.entType.var_782 = param7;
         this.entType.var_439 = param5;
         this.entType.method_686();
         this.entType.gfxType = this.entType.method_60();
         this.ResetEntType(this.entType);
      }
      
      public function method_280() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc3_:MovieClip = null;
         var _loc4_:Number = NaN;
         if(this == this.var_1.clientEnt)
         {
            return;
         }
         if(!this.var_78)
         {
            this.var_78 = class_4.method_16(this.team == GOODGUY ? "a_HealthHeart_Player" : "a_HealthHeart");
            this.var_78.x = this.appearPosX;
            this.var_78.y = this.appearPosY + 20;
            this.var_78.alpha = 0.2;
            this.var_78.dyn_BaseWidth = this.var_78.am_HealthLevel.width / 100;
            this.var_1.var_272.addChild(this.var_78);
            MathUtil.method_235(this.var_78.am_IconGroup);
         }
         _loc1_ = this.var_1.mTimeThisTick;
         _loc2_ = uint(_loc1_ - this.var_1282);
         _loc3_ = this.var_78.am_HealthLevel;
         if((_loc4_ = 100 * (this.currHP / this.maxHP)) > 100)
         {
            _loc4_ = 100;
         }
         if(_loc2_ > 1900)
         {
            this.var_1282 = _loc1_;
         }
         else if(_loc2_ > 1500)
         {
            this.var_1282 = _loc1_ - (2000 - _loc2_);
         }
         else if(_loc2_ > 500)
         {
            this.var_1282 = _loc1_ - 500;
         }
         if(_loc4_ > 0)
         {
            _loc3_.width = Math.max(1,_loc4_) * this.var_78.dyn_BaseWidth;
         }
         else
         {
            this.var_1282 = _loc1_ - 5000;
            this.var_78.visible = false;
         }
      }
      
      public function method_1271() : void
      {
         var _loc1_:Number = NaN;
         if(this.var_78)
         {
            this.var_78.x = this.appearPosX;
            this.var_78.y = this.appearPosY + 20;
            this.var_78.visible = true;
            _loc1_ = this.var_1.mTimeThisTick - this.var_1282;
            if(_loc1_ <= 500)
            {
               this.var_78.alpha = 0.2 + 0.8 * _loc1_ / 500;
            }
            else if(_loc1_ <= 1500)
            {
               this.var_78.alpha = 1;
            }
            else if(_loc1_ <= 2000)
            {
               this.var_78.alpha = 1 - (_loc1_ - 1500) / 500;
            }
            else
            {
               this.var_78.visible = false;
            }
         }
      }
      
      public function method_1667() : void
      {
         var _loc1_:Array = null;
         var _loc2_:MovieClip = null;
         var _loc3_:MovieClip = null;
         var _loc4_:uint = 0;
         var _loc5_:int = 0;
         var _loc6_:uint = 0;
         if(!this.var_78 || !this.combatState.var_1910 || Boolean(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
         {
            return;
         }
         _loc1_ = !!this.var_1.clientEnt ? this.var_1.clientEnt.combatState.var_354 : null;
         if(!_loc1_)
         {
            return;
         }
         _loc4_ = 0;
         while(_loc4_ < const_626)
         {
            _loc2_ = this.var_78.am_IconGroup.getChildByName(this.const_1411 + _loc4_) as MovieClip;
            _loc3_ = _loc2_.am_IconHolder;
            while(_loc3_.numChildren)
            {
               _loc3_.removeChildAt(0);
            }
            this.var_78.am_IconGroup.gotoAndStop(1);
            _loc4_++;
         }
         _loc5_ = 0;
         _loc4_ = 0;
         while(_loc4_ < BuffType.const_932)
         {
            _loc6_ = uint(_loc1_[_loc4_]);
            if(this.combatState.var_1176 & _loc6_)
            {
               _loc2_ = this.var_78.am_IconGroup.getChildByName(this.const_1411 + _loc5_) as MovieClip;
               _loc3_ = _loc2_.am_IconHolder;
               _loc3_.addChild(class_4.method_16(BuffType.method_1811(_loc6_)));
               if(this.combatState.var_1157 & _loc6_)
               {
                  _loc2_.am_ExpirationFrame.visible = true;
                  _loc2_.am_ExpirationFrame.play();
               }
               else
               {
                  _loc2_.am_ExpirationFrame.visible = false;
                  _loc2_.am_ExpirationFrame.stop();
               }
               this.var_78.am_IconGroup.gotoAndStop(_loc5_ + 2);
               _loc5_++;
               if(_loc5_ >= const_626)
               {
                  break;
               }
            }
            _loc4_++;
         }
         this.combatState.var_1910 = false;
      }
      
      public function method_671() : void
      {
         this.method_1271();
         this.method_1667();
         if(this.var_386 && this.var_386.var_34 && this.var_386.var_34.visible)
         {
            this.var_1.var_1445.push(this.var_386);
         }
         if(this.var_1.var_2755 == this.id)
         {
            this.var_1.var_256.x = this.appearPosX;
            this.var_1.var_256.y = this.appearPosY + 20;
            this.var_2386 = true;
         }
         else if(this.var_1.mTimeThisTick < this.var_2841 + this.const_1427)
         {
            this.var_2386 = true;
         }
         else
         {
            this.var_2386 = false;
         }
         if(this.id == this.var_1.clientEntID)
         {
            this.method_280();
         }
         if(this.var_277)
         {
            this.var_277.x = this.appearPosX;
            this.var_277.y = this.appearPosY + const_651;
         }
         if(this.var_170)
         {
            this.var_170.x = this.appearPosX;
            this.var_170.y = this.appearPosY + const_651 + const_1116;
         }
         if(this.var_133)
         {
            this.var_133.x = this.appearPosX;
            this.var_133.y = this.appearPosY - this.entType.height - const_967;
         }
         if(this.var_309)
         {
            if(this.var_309.m_bFinished)
            {
               this.var_309 = null;
            }
            else
            {
               this.var_309.m_TheDO.x = this.appearPosX;
               this.var_309.m_TheDO.y = this.appearPosY;
            }
         }
         if(this.var_308)
         {
            if(this.var_308.m_bFinished)
            {
               this.var_308 = null;
            }
            else
            {
               this.var_308.m_TheDO.x = this.appearPosX;
               this.var_308.m_TheDO.y = this.appearPosY;
            }
         }
      }
      
      public function method_900() : void
      {
         var _loc1_:Number = NaN;
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:int = 0;
         if(Boolean(this.targetOffsetY) && this.targetOffsetY != this.yOffsetToSimulateZ)
         {
            _loc4_ = this.yOffsetToSimulateZ;
            if(Math.abs(this.targetOffsetY - this.yOffsetToSimulateZ) <= 3)
            {
               _loc4_ = this.targetOffsetY;
            }
            else if(this.targetOffsetY > this.yOffsetToSimulateZ)
            {
               _loc4_ += 3;
            }
            else if(this.targetOffsetY < this.yOffsetToSimulateZ)
            {
               _loc4_ -= 3;
            }
            this.method_511(_loc4_);
         }
         _loc1_ = this.var_1.main.overallScale;
         _loc2_ = _loc1_ * this.appearPosX;
         _loc3_ = _loc1_ * this.appearPosY;
         _loc2_ = Math.floor(_loc2_);
         _loc3_ = Math.floor(_loc3_);
         _loc2_ /= _loc1_;
         _loc3_ /= _loc1_;
         this.appearPosX = _loc2_;
         this.appearPosY = _loc3_;
         this.gfx.m_TheDO.x = this.appearPosX;
         this.gfx.m_TheDO.y = this.appearPosY;
      }
      
      public function method_1366() : Boolean
      {
         var _loc1_:uint = 0;
         _loc1_ = this.var_1.mTimeThisTick;
         if(this.var_38.var_2778)
         {
            return false;
         }
         if(Boolean(this.var_195.skit) && _loc1_ > this.var_195.var_1500)
         {
            this.method_340(this.var_195.skit,this.var_195);
         }
         if(this.currEmote && this.var_1262 && _loc1_ >= this.var_1262)
         {
            this.currEmote = null;
         }
         this.var_38.method_550();
         this.method_864();
         this.method_900();
         this.combatState.method_960();
         this.method_853();
         this.method_671();
         this.method_819();
         return true;
      }
      
      public function method_1643(param1:class_144) : void
      {
         var _loc2_:class_37 = null;
         var _loc3_:String = null;
         var _loc4_:Boolean = false;
         _loc2_ = param1.var_553;
         if(_loc2_.var_573)
         {
            for each(_loc3_ in _loc2_.var_573)
            {
               _loc4_ = false;
               if(this.currRoom && !this.currRoom.var_1330[_loc3_] && Boolean(this.var_20 & PLAYER))
               {
                  _loc4_ = true;
                  this.currRoom.var_1330[_loc3_] = true;
               }
            }
         }
      }
      
      public function method_1219(param1:class_144) : void
      {
         var _loc2_:class_37 = null;
         var _loc3_:String = null;
         var _loc4_:Array = null;
         var _loc5_:String = null;
         var _loc6_:Boolean = false;
         var _loc7_:String = null;
         var _loc8_:uint = 0;
         var _loc9_:String = null;
         var _loc10_:Packet = null;
         var _loc11_:String = null;
         var _loc12_:String = null;
         _loc2_ = param1.var_553;
         if(_loc2_.var_573)
         {
            for each(_loc3_ in _loc2_.var_573)
            {
               _loc5_ = String((_loc4_ = _loc3_.split("_"))[0]);
               _loc6_ = Boolean(_loc2_.room) && !_loc2_.room.var_1330[_loc3_];
               if(_loc5_ == "DoorLocal")
               {
                  _loc7_ = String(_loc4_[1]);
                  if(!this.var_38 && (this.var_24 || this.behaviorType.var_1536))
                  {
                     this.var_1.method_867(this,_loc7_,null);
                  }
               }
               else if(_loc5_ == "Door")
               {
                  _loc8_ = uint(_loc4_[1]);
                  if(this.var_24)
                  {
                     this.var_1.OpenDoor(new Door("Trigger",0,0,null,_loc8_,null));
                  }
               }
               else if(_loc5_ == "Badge")
               {
                  _loc9_ = String(_loc4_[1]);
                  if(Boolean(this.var_24) && Boolean(_loc9_))
                  {
                     (_loc10_ = new Packet(LinkUpdater.const_1161)).method_26(_loc9_);
                     this.var_1.serverConn.SendPacket(_loc10_);
                  }
               }
               else if(_loc5_ == "Plummet")
               {
                  this.Plummet();
               }
               else if(_loc5_ == "RoomAggro")
               {
                  if(Boolean(this.var_20 & PLAYER) && const_294)
                  {
                     _loc2_.room.RoomAggro(this);
                  }
               }
               else if(_loc5_ == "Trigger")
               {
                  if(this.var_20 & PLAYER && _loc6_ && const_294)
                  {
                     _loc2_.room.method_79("am_" + _loc3_);
                  }
               }
               else if(_loc5_ == "MultiTrigger")
               {
                  if(Boolean(this.var_20 & PLAYER) && const_294)
                  {
                     _loc2_.room.method_79("am_" + _loc3_);
                  }
                  if(Boolean(this.var_24) && _loc3_ == "MultiTrigger_ClickFink")
                  {
                     if(Boolean(this.var_195) && !this.var_195.skit)
                     {
                        this.StartSkit("Wait, I need to talk to Captain Fink first:He\'s right behind me",true,null);
                     }
                  }
                  if(Boolean(this.var_24) && _loc3_ == "MultiTrigger_ClickRistas")
                  {
                     if(Boolean(this.var_195) && !this.var_195.skit)
                     {
                        this.StartSkit("Wait, I need to talk to Mayor Ristas first:He\'s right behind me",true,null);
                     }
                  }
                  if(Boolean(this.var_24) && _loc3_ == "MultiTrigger_TakeFork")
                  {
                     if(Boolean(this.var_195) && !this.var_195.skit)
                     {
                        this.StartSkit("Wait, I need to take the fork in the road:It\'s right below me",true,null);
                     }
                  }
               }
               else if(_loc5_ == "CutScene")
               {
                  if(this.var_20 & PLAYER && _loc6_ && const_294)
                  {
                     _loc11_ = "CutScene";
                     if(_loc4_.length > 1)
                     {
                        _loc11_ += "_" + _loc4_[1];
                     }
                     if(_loc2_.room.var_150.hasOwnProperty(_loc11_))
                     {
                        _loc2_.room.method_465(_loc2_.room.var_150[_loc11_]);
                     }
                  }
               }
               else if(_loc5_ == "Script")
               {
                  if(this.var_20 & PLAYER && _loc6_ && const_294)
                  {
                     _loc12_ = "Script";
                     if(_loc4_.length > 1)
                     {
                        _loc12_ += "_" + _loc4_[1];
                     }
                     if(_loc2_.room.var_150.hasOwnProperty(_loc12_))
                     {
                        _loc2_.room.method_744(_loc2_.room.var_150[_loc12_]);
                     }
                  }
               }
            }
         }
      }
      
      public function InActiveCutScene() : Boolean
      {
         if(Boolean(this.currRoom) && this.currRoom.var_1052)
         {
            return !this.currRoom.var_1417;
         }
         return false;
      }
      
      public function Plummet() : void
      {
         if(this.var_20 & Entity.PLAYER)
         {
            if(!this.var_38)
            {
               this.var_1122 = true;
               this.var_2170 = this.var_1.mTimeThisTick;
            }
            if(SoundConfig.var_1687)
            {
               this.var_746 = SoundManager.Play(SoundConfig.var_1687,1,false);
            }
         }
      }
      
      public function method_1213() : void
      {
         var _loc1_:Number = NaN;
         var _loc2_:Number = NaN;
         var _loc3_:Door = null;
         this.var_2170 = 0;
         this.var_1122 = false;
         this.velocity.x = 0;
         if(this.currRoom.var_928)
         {
            this.TeleportTo(this.currRoom.var_928.x,this.currRoom.var_928.y);
         }
         else if(this.var_703)
         {
            _loc1_ = this.var_703.startX + (this.var_703.endX - this.var_703.startX) / 2;
            _loc2_ = this.var_703.startY + (this.var_703.endY - this.var_703.startY) / 2;
            _loc2_ -= 5;
            this.TeleportTo(_loc1_,_loc2_);
         }
         else if(this.var_1.level.var_239)
         {
            this.TeleportTo(this.var_1.level.var_239.x,this.var_1.level.var_239.y);
         }
         else
         {
            _loc3_ = this.var_1.level.var_264[0];
            if(_loc3_)
            {
               this.TeleportTo(_loc3_.posX,_loc3_.posY);
            }
         }
      }
      
      public function UpdatePos(param1:Number, param2:Number) : void
      {
         this.physPosX = param1;
         this.physPosY = param2;
         this.appearPosX = this.physPosX;
         this.appearPosY = this.physPosY + this.yOffsetToSimulateZ + this.var_1.var_776;
         this.var_10 = this.appearPosX;
         this.var_12 = this.appearPosY - this.entType.height * 0.5;
      }
      
      public function TeleportTo(param1:Number, param2:Number) : void
      {
         this.UpdatePos(param1,param2);
         this.var_1460 = true;
         if(this.var_24)
         {
            this.var_24.var_418.var_556 = true;
            this.var_1.main.var_860 = 500;
            this.var_1.main.var_903 = this.var_1.mTimeThisTick + this.var_1.main.var_860;
         }
      }
      
      public function method_1039(param1:class_37) : Number
      {
         var _loc2_:Number = NaN;
         if(param1.endX == param1.startX)
         {
            _loc2_ = 9999999;
         }
         else
         {
            _loc2_ = (param1.endY - param1.startY) / (param1.endX - param1.startX);
         }
         return _loc2_;
      }
      
      private function method_616(param1:Number) : Number
      {
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         _loc2_ = this.var_1781 ? ICE_FRICTION : (this.var_1111 ? WATER_FRICTION : FRICTION);
         if(this.behaviorType.var_844)
         {
            _loc2_ = const_957;
         }
         _loc3_ = param1 > 0 ? 1 : -1;
         if((_loc4_ = _loc3_ * param1 - _loc2_ * this.var_1.TIMESTEP) < 0)
         {
            _loc4_ = 0;
         }
         return _loc4_ * _loc3_;
      }
      
      public function method_864() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:class_37 = null;
         var _loc3_:Boolean = false;
         var _loc4_:Boolean = false;
         var _loc5_:class_37 = null;
         var _loc6_:Boolean = false;
         var _loc7_:Boolean = false;
         var _loc8_:class_37 = null;
         var _loc9_:Number = NaN;
         var _loc10_:Number = NaN;
         var _loc11_:Number = NaN;
         var _loc12_:Number = NaN;
         var _loc13_:class_37 = null;
         var _loc14_:class_37 = null;
         var _loc15_:class_37 = null;
         var _loc16_:Number = NaN;
         var _loc17_:class_37 = null;
         var _loc18_:Boolean = false;
         var _loc19_:class_144 = null;
         var _loc20_:class_145 = null;
         var _loc21_:class_145 = null;
         var _loc22_:String = null;
         this.startPhysPosX = this.physPosX;
         this.startPhysPosY = this.physPosY;
         if(!this.velocity.x && !this.velocity.y && !this.bRunning && !this.var_91.x && !this.var_91.y && !this.bJumping && !this.bDropping && !this.var_1944 && !this.var_1714 && !this.var_1460)
         {
            this.appearPosX = this.physPosX;
            this.appearPosY = this.physPosY + this.yOffsetToSimulateZ + this.var_1.var_776;
            this.var_12 = this.appearPosY - this.entType.height * 0.5;
            return;
         }
         this.var_1460 = false;
         if(this.behaviorType.bNoPhysics)
         {
            return;
         }
         _loc1_ = uint(CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR);
         _loc2_ = this.currSurface;
         this.bSmackingAWallOrCeiling = false;
         _loc3_ = this.entState != const_6 && this.entType.var_832;
         if(this.entType.var_2516 && this.entType.var_832)
         {
            _loc3_ = true;
         }
         if(this.velocity.x != 0)
         {
            this.velocity.x = this.method_616(this.velocity.x);
         }
         if(_loc3_ && this.velocity.y != 0)
         {
            this.velocity.y = this.method_616(this.velocity.y);
         }
         if(Boolean(this.currSurface) && !_loc3_)
         {
            this.velocity.y = 0;
         }
         if(this.entState != const_6)
         {
            _loc9_ = this.maxSpeed;
            if(this.var_1111)
            {
               _loc9_ *= WATER_SLOW_FACTOR;
            }
            _loc10_ = this.var_1781 ? ICE_ACCELERATION : (this.var_1111 ? WATER_ACCELERATION : ACCELERATION);
            if(this.behaviorType.var_844)
            {
               _loc10_ = const_1136;
            }
            if(_loc3_)
            {
               if(this.bJumping && this.velocity.y > -_loc9_)
               {
                  this.velocity.y -= _loc10_ * this.var_1.TIMESTEP;
                  if(this.velocity.y <= -_loc9_)
                  {
                     this.velocity.y = -_loc9_;
                  }
               }
               else if(this.bDropping && this.velocity.y < _loc9_)
               {
                  this.velocity.y += _loc10_ * this.var_1.TIMESTEP;
                  if(this.velocity.y >= _loc9_)
                  {
                     this.velocity.y = _loc9_;
                  }
               }
            }
            if(this.bRunning)
            {
               if(this.bLeft && this.velocity.x > -_loc9_)
               {
                  this.velocity.x -= _loc10_ * this.var_1.TIMESTEP;
                  if(this.velocity.x <= -_loc9_)
                  {
                     this.velocity.x = -_loc9_;
                  }
               }
               else if(!this.bLeft && this.velocity.x < _loc9_)
               {
                  this.velocity.x += _loc10_ * this.var_1.TIMESTEP;
                  if(this.velocity.x >= _loc9_)
                  {
                     this.velocity.x = _loc9_;
                  }
               }
            }
            if(!_loc3_)
            {
               this.var_2415 = false;
               if((this.var_1944 || this.bJumping) && !this.combatState.var_1313)
               {
                  if(this.currSurface)
                  {
                     if((_loc11_ = this.method_1039(this.currSurface)) > 1 && this.velocity.x < 0)
                     {
                        this.velocity.x /= _loc11_;
                     }
                     if(_loc11_ < -1 && this.velocity.x > 0)
                     {
                        this.velocity.x /= _loc11_ * -1;
                     }
                     this.SetCurrSurface(null);
                     this.var_91.y -= JUMP_IMPULSE;
                     this.var_2415 = true;
                     if(!this.var_38 && Boolean(this.entType.var_1350))
                     {
                        SoundManager.Play(this.entType.var_1350);
                     }
                  }
                  else
                  {
                     this.velocity.y -= JUMPJET * this.var_1.TIMESTEP;
                  }
               }
            }
            if(this.var_1714 || this.bDropping || _loc3_)
            {
               _loc1_ = CollisionManager.HARD_FLOOR;
               if(Boolean(this.currSurface) && this.currSurface.type == CollisionManager.SOFT_FLOOR)
               {
                  this.SetCurrSurface(null);
                  this.var_91.y += DROP_IMPULSE;
               }
            }
         }
         this.velocity.x += this.var_282.x;
         this.velocity.x += this.var_91.x;
         if(this.currSurface)
         {
            _loc12_ = this.velocity.x * this.var_1.TIMESTEP;
            while(_loc12_)
            {
               var_922.x = this.currSurface.endX - this.currSurface.startX;
               var_922.y = this.currSurface.endY - this.currSurface.startY;
               var_922.normalize(_loc12_);
               var_420.x = var_922.x;
               var_420.y = var_922.y;
               var_1168.x = this.physPosX + var_420.x;
               var_1168.y = this.physPosY + var_420.y;
               _loc13_ = this.var_1.collMan.getFloorCollision(0,this.physPosX,this.physPosY,var_420,var_1168,this.currSurface,null,null,_loc1_,0);
               this.physPosX += var_420.x;
               this.physPosY += var_420.y;
               if(!_loc13_)
               {
                  if(!_loc3_)
                  {
                     var_1190.x = 0;
                     var_1190.y = const_654;
                     if((Boolean(_loc14_ = this.var_1.collMan.getFloorCollision(0,this.physPosX,this.physPosY,var_1190,var_1168,null,null,null,_loc1_,0))) && _loc14_ != this.currSurface)
                     {
                        if(var_1190.y < const_895)
                        {
                           this.var_91.y += const_654;
                           break;
                        }
                        this.var_2380 = true;
                     }
                  }
                  break;
               }
               this.SetCurrSurface(_loc13_);
               var_958.x = var_420.x;
               var_958.y = var_420.y;
               var_958.normalize(PULLBACK_DIST);
               this.physPosX -= var_958.x;
               this.physPosY -= var_958.y;
               _loc12_ -= var_420.length * (Math.abs(_loc12_) / _loc12_);
               if(_loc13_.endX - _loc13_.startX < 0.01)
               {
                  break;
               }
            }
         }
         if(!_loc3_)
         {
            this.velocity.y += this.var_91.y;
            this.velocity.y += GRAVITY * this.var_1.TIMESTEP;
            if(this.velocity.y > TERMINAL_VELOCITY)
            {
               this.velocity.y = TERMINAL_VELOCITY;
            }
         }
         if(_loc4_ = _loc3_ || !this.currSurface)
         {
            this.velocity.y += this.var_282.y;
         }
         var_366.x = this.velocity.x * this.var_1.TIMESTEP;
         var_366.y = this.velocity.y * this.var_1.TIMESTEP;
         if(this.currSurface)
         {
            var_366.y += PULLBACK_DIST * 2;
            var_366.x = 0;
         }
         var_52.x = var_366.x;
         var_52.y = var_366.y;
         var_425.x = this.physPosX + var_52.x;
         var_425.y = this.physPosY + var_52.y;
         _loc5_ = this.var_1.collMan.getFloorCollision(0,this.physPosX,this.physPosY,var_52,var_425,null,null,null,_loc1_,0);
         _loc6_ = false;
         if(!this.currSurface)
         {
            _loc15_ = null;
            var_226.x = var_366.x;
            var_226.y = var_366.y;
            var_407.x = this.physPosX + var_226.x;
            var_407.y = this.physPosY + var_226.y;
            if((Boolean(_loc15_ = this.var_1.collMan.getFloorCollision(0,this.physPosX,this.physPosY - const_781,var_226,var_407,null,null,null,CollisionManager.HARD_FLOOR,0))) && var_226.length < var_52.length)
            {
               var_52.x = var_226.x;
               var_52.y = var_226.y;
               var_425.x = var_407.x;
               var_425.y = var_407.y;
               if(_loc15_.startX != _loc15_.endX)
               {
                  _loc6_ = true;
               }
               _loc5_ = _loc15_;
            }
         }
         this.SetCurrSurface(_loc5_);
         this.physPosX += var_52.x;
         this.physPosY += var_52.y;
         if(this.currSurface)
         {
            var_906.x = var_52.x;
            var_906.y = var_52.y;
            var_906.normalize(PULLBACK_DIST);
            this.physPosX -= var_906.x;
            this.physPosY -= var_906.y;
         }
         _loc7_ = false;
         if(_loc6_)
         {
            if(this.velocity.y < GRAVITY * this.var_1.TIMESTEP)
            {
               this.velocity.y = GRAVITY * this.var_1.TIMESTEP;
            }
            _loc16_ = (_loc16_ = var_366.length - var_52.length) + PULLBACK_DIST;
            var_52.x = 0;
            var_52.y = _loc16_;
            _loc7_ = true;
         }
         else if(Boolean(_loc5_) && _loc5_.startX == _loc5_.endX)
         {
            var_52.x = 0;
            var_52.y = this.velocity.y * this.var_1.TIMESTEP;
            _loc7_ = true;
         }
         if(_loc7_)
         {
            _loc17_ = this.var_1.collMan.getFloorCollision(0,this.physPosX,this.physPosY,var_52,var_425,null,null,null,_loc1_,0);
            _loc15_ = null;
            var_226.x = var_52.x;
            var_226.y = var_52.y;
            var_407.x = this.physPosX + var_52.x;
            var_407.y = this.physPosY + var_52.y;
            if((Boolean(_loc15_ = this.var_1.collMan.getFloorCollision(0,this.physPosX,this.physPosY - const_781,var_226,var_407,null,null,null,CollisionManager.HARD_FLOOR,0))) && var_226.length < var_52.length)
            {
               var_52.x = var_226.x;
               var_52.y = var_226.y;
               var_425.x = var_407.x;
               var_425.y = var_407.y;
               _loc17_ = null;
               this.physPosY += PULLBACK_DIST;
               if(this.velocity.y < GRAVITY * this.var_1.TIMESTEP)
               {
                  this.velocity.y = GRAVITY * this.var_1.TIMESTEP;
               }
            }
            this.physPosX += var_52.x;
            this.physPosY += var_52.y;
            if(_loc17_)
            {
               this.physPosY -= PULLBACK_DIST;
            }
            this.SetCurrSurface(_loc17_);
            if(Boolean(_loc5_) && !this.currSurface)
            {
               this.bSmackingAWallOrCeiling = true;
            }
         }
         if(!(this.var_20 & Entity.PLAYER) && !this.currSurface && _loc2_ && this.entState != Entity.const_6 && !this.bGotoLocation)
         {
            if(!(_loc18_ = this.behaviorType.var_696))
            {
               var_1443.x = 0;
               var_1443.y = const_931;
               if(!this.var_1.collMan.getFloorCollision(0,this.physPosX,this.physPosY,var_1443,var_425,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0))
               {
                  _loc18_ = true;
               }
            }
            if(_loc18_)
            {
               this.bRunning = false;
               this.SetCurrSurface(_loc2_);
               this.UpdatePos(this.startPhysPosX,this.startPhysPosY);
            }
         }
         this.var_1170 = !!this.currSurface ? false : true;
         if(this.var_2380)
         {
            this.var_1170 = false;
         }
         if(this.currSurface)
         {
            this.var_2380 = false;
         }
         this.velocity.x -= this.var_282.x;
         if(_loc4_)
         {
            this.velocity.y -= this.var_282.y;
         }
         this.var_91.x = 0;
         this.var_91.y = 0;
         var_52.x = this.physPosX - this.startPhysPosX;
         var_52.y = this.physPosY - this.startPhysPosY;
         var_52.x *= 1.1;
         var_52.y *= 1.1;
         if(_loc8_ = this.var_1.collMan.getFloorCollision(0,this.startPhysPosX - var_52.x * 0.05,this.startPhysPosY - var_52.y * 0.05,var_52,var_425,null,null,null,CollisionManager.TRIGGER_BOUNDARY,0))
         {
            (_loc19_ = new class_144()).var_553 = _loc8_;
            this.triggersHit.push(_loc19_);
            this.var_610.push(_loc19_);
            if(Boolean(_loc8_.room) && _loc8_.room != this.currRoom)
            {
               this.method_895(_loc8_.room);
            }
         }
         this.appearPosX = this.physPosX;
         this.appearPosY = this.physPosY + this.yOffsetToSimulateZ + this.var_1.var_776;
         this.var_10 = this.appearPosX;
         this.var_12 = this.appearPosY - this.entType.height * 0.5;
         if(Boolean(this.currSurface) && this.currSurface.room != this.currRoom)
         {
            this.method_895(this.currSurface.room);
         }
         if(Boolean(this.var_20 & PLAYER) && Boolean(this.currRoom))
         {
            _loc20_ = null;
            if(this.currRoom)
            {
               for each(_loc21_ in this.currRoom.var_1219)
               {
                  if(_loc21_.method_810(this.physPosX,this.physPosY))
                  {
                     _loc20_ = _loc21_;
                     break;
                  }
               }
            }
            if(Boolean(this.var_979) && (!_loc20_ || _loc20_.id != this.var_979.id))
            {
               this.currRoom.method_79("ExitVolume^" + this.var_979.var_1833);
            }
            if(Boolean(_loc20_) && (!this.var_979 || _loc20_.id != this.var_979.id))
            {
               _loc22_ = _loc20_.var_1833;
               this.currRoom.method_79("EnterVolume^" + _loc22_);
               if(_loc22_ == "am_BossFight")
               {
                  if(!this.currRoom.var_241)
                  {
                     this.currRoom.method_307();
                  }
               }
               else if(_loc22_ == "am_KeepRequest")
               {
                  this.var_1.level.method_977();
               }
            }
            this.var_979 = _loc20_;
         }
         if(Boolean(this.currSurface) && !_loc2_)
         {
            this.var_2545 = this.var_1.mTimeThisTick;
         }
         this.method_1701(this.currSurface);
         this.method_1309();
         if(this.var_807)
         {
            this.var_807 = this.var_1.mTimeThisTick;
         }
         if(Boolean(this.currSurface) && !_loc3_)
         {
            this.velocity.y = 0;
         }
      }
      
      public function method_1309() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:class_144 = null;
         var _loc3_:class_37 = null;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:class_144 = null;
         _loc3_ = null;
         if(_loc4_ = this.triggersHit.length)
         {
            _loc3_ = null;
            _loc1_ = 0;
            while(_loc1_ < _loc4_)
            {
               _loc2_ = this.triggersHit[_loc1_];
               if(_loc2_.var_553 != _loc3_)
               {
                  _loc3_ = _loc2_.var_553;
                  this.method_1219(_loc2_);
               }
               _loc1_++;
            }
         }
         if(_loc5_ = this.var_610.length)
         {
            _loc3_ = null;
            _loc1_ = 0;
            while(_loc1_ < _loc5_)
            {
               _loc2_ = this.var_610[_loc1_];
               if(_loc2_.var_553 != _loc3_)
               {
                  _loc3_ = _loc2_.var_553;
                  this.method_1643(_loc2_);
               }
               _loc1_++;
            }
         }
         if(_loc4_)
         {
            for each(_loc6_ in this.triggersHit)
            {
               _loc6_.method_285();
            }
            this.triggersHit.length = 0;
         }
         if(_loc5_)
         {
            for each(_loc6_ in this.var_610)
            {
               _loc6_.method_285();
            }
            this.var_610.length = 0;
         }
      }
      
      public function SetCurrSurface(param1:class_37) : Boolean
      {
         var _loc2_:class_144 = null;
         var _loc3_:class_144 = null;
         if(param1 == this.currSurface)
         {
            return false;
         }
         if(Boolean(this.currSurface) && Boolean(this.currSurface.var_573))
         {
            _loc2_ = new class_144();
            _loc2_.var_553 = this.currSurface;
            this.var_610.push(_loc2_);
         }
         if(Boolean(param1) && Boolean(param1.var_573))
         {
            _loc3_ = new class_144();
            _loc3_.var_553 = param1;
            this.triggersHit.push(_loc3_);
         }
         if(!this.var_1122 && param1 && param1.startX != param1.endX)
         {
            this.var_703 = param1;
         }
         this.currSurface = param1;
         return true;
      }
      
      public function method_1701(param1:class_37) : void
      {
         var _loc2_:uint = 0;
         this.var_549 = false;
         this.var_2800 = false;
         this.var_1760 = false;
         this.var_1933 = false;
         this.var_1836 = false;
         this.var_1932 = false;
         _loc2_ = 0;
         if(param1)
         {
            this.var_1111 = false;
            this.var_1781 = false;
            _loc2_ = param1.var_120;
         }
         if(_loc2_)
         {
            if(_loc2_ & class_37.const_439)
            {
               this.var_549 = true;
               this.var_1111 = true;
               this.var_2194 = false;
            }
            else if(_loc2_ & class_37.const_464)
            {
               this.var_549 = true;
               this.var_1111 = true;
               this.var_2194 = true;
            }
            else if(_loc2_ & class_37.const_782)
            {
               this.var_2800 = true;
               this.var_1781 = true;
            }
            else if(_loc2_ & class_37.const_704)
            {
               this.var_1933 = true;
            }
            else if(_loc2_ & class_37.const_786)
            {
               this.var_1836 = true;
            }
            else if(_loc2_ & class_37.const_706)
            {
               this.var_1760 = true;
            }
            else if(_loc2_ & class_37.const_638)
            {
               this.var_1932 = true;
            }
         }
      }
      
      public function GetMeleePower() : PowerType
      {
         if(this.combatState.var_1823)
         {
            return class_14.powerTypesDict[this.combatState.var_1823];
         }
         return this.var_353;
      }
      
      public function GetRangedPower() : PowerType
      {
         if(this.combatState.var_1651)
         {
            return class_14.powerTypesDict[this.combatState.var_1651];
         }
         return this.var_280;
      }
      
      public function method_529() : Boolean
      {
         var _loc1_:PowerType = null;
         var _loc2_:uint = 0;
         var _loc3_:Array = null;
         var _loc4_:int = 0;
         var _loc5_:Point = null;
         _loc1_ = this.GetMeleePower();
         if(!_loc1_)
         {
            return false;
         }
         _loc2_ = _loc1_.method_63(this);
         if(this.var_24)
         {
            if(!(_loc4_ = int(this.mEquipGear[EntType.SWORD_SLOT])))
            {
               return true;
            }
            if((_loc5_ = this.var_24.method_375(class_36.const_847)).x >= this.appearPosX - _loc2_ && _loc5_.x <= this.appearPosX + _loc2_ && _loc5_.y <= this.appearPosY && _loc5_.y >= this.appearPosY - this.entType.height)
            {
               return true;
            }
         }
         if(_loc1_.var_6 == PowerType.TARGETMETHOD_MELEE)
         {
            _loc3_ = this.var_1.GatherEntities(this,this.var_10,this.var_12,_loc2_,this.entType.height * 0.5,Game.ENEMY | Game.MELEEABLE);
         }
         else if(_loc1_.aoeRadius)
         {
            _loc3_ = this.var_1.GatherEntities(this,this.var_10,this.var_12,_loc1_.aoeRadius,_loc1_.aoeRadius,Game.ENEMY | Game.MELEEABLE);
         }
         else
         {
            _loc3_ = this.var_1.GatherEntities(this,this.var_10,this.var_12,_loc2_,_loc2_,Game.ENEMY | Game.MELEEABLE);
         }
         return _loc3_.length > 0;
      }
      
      public function method_895(param1:Room) : void
      {
         var _loc2_:Boolean = false;
         _loc2_ = Boolean(this.var_20 & Entity.PLAYER);
         if(Boolean(this.currRoom) && _loc2_)
         {
            this.currRoom.method_886(this);
         }
         this.currRoom = param1;
         if(param1.var_928)
         {
            this.var_2820 = param1;
         }
         if(Boolean(this.currRoom) && _loc2_)
         {
            this.currRoom.method_1326(this);
         }
      }
      
      public function method_1597(param1:Point) : void
      {
         var _loc2_:Number = NaN;
         var _loc3_:Door = null;
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         var _loc10_:Boolean = false;
         var _loc11_:Packet = null;
         var _loc12_:Number = NaN;
         _loc2_ = 100000;
         this.var_848 = null;
         this.var_916 = null;
         for each(_loc3_ in this.var_1.level.var_264)
         {
            if(_loc3_.bDisabled)
            {
               this.method_579(_loc3_,false);
            }
            else
            {
               _loc4_ = _loc3_.var_443.x + _loc3_.posX;
               _loc5_ = _loc3_.var_443.y + _loc3_.posY;
               _loc6_ = _loc4_ + _loc3_.var_443.width;
               _loc7_ = _loc5_ + _loc3_.var_443.height;
               _loc8_ = (_loc6_ + _loc4_) * 0.5;
               _loc9_ = (_loc7_ + _loc5_) * 0.5;
               if(_loc3_.doorID)
               {
                  if(!_loc3_.var_2326 && (this.appearPosX >= _loc4_ - Door.const_632 && this.appearPosX <= _loc6_ + Door.const_632))
                  {
                     (_loc11_ = new Packet(LinkUpdater.PKTTYPE_REQUEST_DOOR_STATE)).method_9(_loc3_.doorID);
                     this.var_1.serverConn.SendPacket(_loc11_);
                     _loc3_.var_2326 = true;
                  }
                  _loc10_ = false;
                  if(!this.var_1.level.bInstanced)
                  {
                     _loc10_ = this.var_10 >= _loc4_ - Door.const_62 && this.var_10 <= _loc6_ + Door.const_62 && this.var_12 >= _loc5_ - Door.const_62 && this.var_12 <= _loc7_ + Door.const_62;
                  }
                  _loc10_ ||= param1.x >= _loc4_ && param1.x <= _loc6_ && param1.y >= _loc5_ && param1.y <= _loc7_;
                  this.method_579(_loc3_,_loc10_);
               }
               if(this.var_1.level.var_333)
               {
                  if((_loc12_ = (this.var_10 - _loc8_) * (this.var_10 - _loc8_) + (this.var_12 - _loc9_) * (this.var_12 - _loc9_)) < _loc2_)
                  {
                     this.var_916 = _loc3_;
                     _loc2_ = _loc12_;
                  }
               }
               else if(this.var_10 >= _loc4_ - Door.const_62 && this.var_10 <= _loc6_ + Door.const_62 && this.var_12 >= _loc5_ - Door.const_62 && this.var_12 <= _loc7_ + Door.const_62)
               {
                  this.var_916 = _loc3_;
               }
               if(param1.x >= _loc4_ && param1.x <= _loc6_ && param1.y >= _loc5_ && param1.y <= _loc7_)
               {
                  this.var_848 = _loc3_;
                  this.var_2008 = this.var_916 == this.var_848;
               }
               if(this.var_1.level.var_333)
               {
                  this.var_2008 = true;
               }
            }
         }
      }
      
      public function method_579(param1:Door, param2:Boolean) : void
      {
         var _loc3_:class_33 = null;
         var _loc5_:* = false;
         var _loc6_:String = null;
         var _loc7_:MovieClip = null;
         var _loc8_:MovieClip = null;
         var _loc9_:Boolean = false;
         var _loc10_:String = null;
         var _loc11_:* = false;
         var _loc12_:MovieClip = null;
         var _loc13_:uint = 0;
         var _loc14_:uint = 0;
         _loc3_ = param1.var_517;
         if(!param2)
         {
            if(Boolean(_loc3_) && _loc3_.mbVisible)
            {
               if(!(_loc3_.var_387 & class_33.const_80))
               {
                  _loc3_.PlayAnimation("Appear",class_33.const_80);
               }
               _loc3_.TickMovieClip();
               if(_loc3_.mbCompleted)
               {
                  _loc3_.method_42();
               }
            }
            return;
         }
         if(param1.doorState == Door.DOORSTATE_CLOSED || param1.doorState == Door.DOORSTATE_LOCKED)
         {
            return;
         }
         if(!param1.var_1260)
         {
            return;
         }
         if(!_loc3_)
         {
            _loc5_ = const_974.indexOf(param1.var_1260) != -1;
            _loc6_ = Level.method_73(param1.var_1260);
            _loc7_ = null;
            _loc8_ = null;
            _loc9_ = false;
            if(param1.doorState == Door.DOORSTATE_STATIC || _loc5_)
            {
               _loc8_ = (_loc7_ = class_4.method_16("a_DungeonDoorPlateTravel")).am_DoorPlate;
               _loc9_ = true;
            }
            else if(param1.doorState != Door.DOORSTATE_MISSIONREPEAT)
            {
               _loc8_ = (_loc7_ = class_4.method_16("a_DungeonDoorPlate")).am_DoorPlate;
            }
            else
            {
               _loc8_ = (_loc7_ = class_4.method_16("a_DungeonDoorPlateComplete")).am_DoorPlate;
               class_119.method_144(_loc8_.am_StarRating,param1.var_2671);
            }
            _loc10_ = "";
            if(_loc11_ = this.var_1.level.var_1550.indexOf("Hard") != -1)
            {
               _loc8_.am_DreadMode.visible = true;
            }
            else
            {
               _loc8_.am_DreadMode.visible = false;
               _loc13_ = uint((_loc12_ = _loc8_.am_FireGroup).numChildren);
               _loc14_ = 0;
               while(_loc14_ < _loc13_)
               {
                  (_loc12_.getChildAt(_loc14_) as MovieClip).gotoAndStop(0);
                  _loc14_++;
               }
               _loc12_.gotoAndStop(0);
               _loc12_.visible = false;
            }
            _loc10_ = _loc9_ || _loc5_ ? (this.var_1.level.bInstanced && param1.doorID != 2 ? "Return to" : "Travel to") : "Dungeon";
            MathUtil.method_2(_loc8_.am_Header,_loc10_);
            MathUtil.method_2(_loc8_.am_MapName,_loc6_);
            _loc7_.x = param1.var_2280;
            _loc7_.y = param1.var_2285;
            _loc3_ = new class_33(this.var_1,_loc7_);
            param1.var_517 = _loc3_;
            _loc3_.PlayAnimation("Appear");
            _loc3_.method_141(class_33.const_494);
         }
         var _loc4_:class_13 = class_14.var_1391[param1.var_1260];
         if(_loc3_.var_387 & class_33.const_80)
         {
            _loc3_.PlayAnimation("Appear");
         }
         if(!_loc3_.mbVisible)
         {
            _loc3_.method_141(class_33.const_494);
         }
         _loc3_.TickMovieClip();
      }
      
      public function method_355() : Boolean
      {
         return Boolean(this.cue) && Boolean(this.cue.characterName) && this.team == NEUTRAL;
      }
      
      public function method_611(param1:String) : Boolean
      {
         var _loc2_:class_133 = null;
         for each(_loc2_ in this.var_1.groupmates)
         {
            if(_loc2_.charName == param1)
            {
               return true;
            }
         }
         return false;
      }
      
      public function method_1589(param1:Point, param2:Number, param3:Number) : void
      {
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         var _loc10_:Number = NaN;
         var _loc11_:Number = NaN;
         var _loc12_:Number = NaN;
         var _loc13_:Number = NaN;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         var _loc16_:EntType = null;
         var _loc17_:Entity = null;
         var _loc18_:String = null;
         this.var_1783 = 0;
         this.var_518 = 0;
         this.var_2830 = 0;
         this.var_485 = 0;
         this.var_1216 = 0;
         this.var_1812 = 0;
         this.var_2816 = false;
         for each(_loc17_ in this.var_1.entities)
         {
            if(!(!_loc17_.method_156() || _loc17_.method_503()))
            {
               _loc15_ = _loc17_.var_599 == const_282 ? 0 : const_836;
               _loc5_ = Math.abs(param2 - _loc17_.var_10);
               _loc6_ = Math.abs(param3 - _loc17_.var_12);
               _loc7_ = (_loc16_ = _loc17_.entType).width * 0.5 + 100;
               _loc8_ = _loc16_.height * 0.5 + 100;
               if(_loc17_ != this && _loc5_ <= _loc7_ && _loc6_ <= _loc8_)
               {
                  if(_loc17_.team != this.team && _loc17_.team != NEUTRAL)
                  {
                     this.var_2830 = _loc17_.id;
                  }
                  else if(_loc17_.method_355())
                  {
                     this.var_1783 = _loc17_.id;
                  }
               }
               _loc7_ = _loc17_.entType.width * 0.5 + const_689;
               _loc8_ = _loc17_.entType.height * 0.5 + const_689 + _loc15_;
               _loc9_ = Math.abs(param1.x - _loc17_.var_10);
               _loc10_ = Math.abs(param1.y - _loc17_.var_12);
               if(_loc9_ <= _loc7_ && _loc10_ <= _loc8_)
               {
                  _loc4_ = _loc9_ * _loc9_ + _loc10_ * _loc10_;
                  if(_loc17_ == this)
                  {
                     this.var_2816 = true;
                  }
                  else if(_loc17_.var_20 & Entity.PLAYER)
                  {
                     _loc18_ = _loc16_.entName;
                     if(!this.method_611(_loc18_))
                     {
                        if(!this.var_1216 || _loc4_ < _loc12_)
                        {
                           this.var_1216 = _loc17_.id;
                           _loc12_ = _loc4_;
                        }
                     }
                     else if(!this.var_1812 || _loc4_ < _loc13_)
                     {
                        this.var_1812 = _loc17_.id;
                        _loc13_ = _loc4_;
                     }
                  }
                  else if(_loc17_.team != this.team && _loc17_.team != NEUTRAL)
                  {
                     if(_loc17_.entState != const_6)
                     {
                        if(!this.var_485 || _loc4_ < _loc11_)
                        {
                           this.var_485 = _loc17_.id;
                           _loc11_ = _loc4_;
                        }
                     }
                  }
                  else if(_loc17_.method_355())
                  {
                     if(!this.var_518 || _loc4_ < _loc14_)
                     {
                        this.var_518 = _loc17_.id;
                        _loc14_ = _loc4_;
                     }
                  }
               }
            }
         }
      }
      
      public function method_1766(param1:Point) : void
      {
         var _loc2_:int = 0;
         _loc2_ = this.method_1181(param1,this.var_1.level.var_1140);
         if(_loc2_ == -1)
         {
            this.var_1113 = null;
         }
         else
         {
            this.var_1113 = this.var_1.level.var_1140[_loc2_];
         }
         this.var_2650 = true;
      }
      
      public function method_1181(param1:Point, param2:Vector.<class_77>) : int
      {
         var _loc3_:int = 0;
         var _loc4_:Number = NaN;
         var _loc5_:class_77 = null;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         _loc3_ = 0;
         _loc4_ = param2.length;
         _loc3_ = 0;
         while(_loc3_ < _loc4_)
         {
            _loc6_ = (_loc5_ = param2[_loc3_]).rect.x + _loc5_.posX;
            _loc7_ = _loc5_.rect.y + _loc5_.posY;
            if(_loc6_ <= param1.x && param1.x <= _loc6_ + _loc5_.rect.width && _loc7_ <= param1.y && param1.y <= _loc7_ + _loc5_.rect.height)
            {
               return _loc3_;
            }
            _loc3_++;
         }
         return -1;
      }
      
      public function method_1973(param1:Point) : Point
      {
         var _loc2_:Boolean = false;
         if(this.var_24)
         {
            return this.var_24.method_375(param1);
         }
         if(this.behaviorType.var_1267)
         {
            this.method_186(param1);
            _loc2_ = this.bFacingLeft();
            if(_loc2_)
            {
               param1.x -= 2 * (param1.x - this.appearPosX);
            }
            if(this.behaviorType.var_2668)
            {
               param1.y += 200;
            }
            else if(this.behaviorType.var_2565)
            {
               param1.y -= 200;
            }
            else
            {
               param1.x += _loc2_ ? -200 : 200;
            }
            return param1;
         }
         if(this.brain)
         {
            if(this.brain.var_1151)
            {
               param1.x = this.brain.var_1151.x;
               param1.y = this.brain.var_1151.y;
               return param1;
            }
            if(this.brain.target)
            {
               param1.x = this.brain.target.var_10;
               param1.y = this.brain.target.var_12;
               return param1;
            }
         }
         param1.x = this.var_10;
         param1.y = this.var_12;
         return param1;
      }
      
      public function method_1524() : void
      {
         var _loc1_:Number = NaN;
         _loc1_ = 1 - (this.maxHP - this.currHP) / this.maxHP;
         if(0.1 < _loc1_ && _loc1_ <= 0.25)
         {
            if(!this.var_436 && Boolean(SoundConfig.var_1784))
            {
               this.var_436 = SoundManager.Play(SoundConfig.var_1784,1,true);
            }
            if(this.var_467)
            {
               this.var_467 = SoundManager.method_155(this.var_467);
            }
         }
         else if(0 < _loc1_ && _loc1_ <= 0.1)
         {
            if(this.var_436)
            {
               this.var_436 = SoundManager.method_155(this.var_436);
            }
            if(!this.var_467 && Boolean(SoundConfig.var_1849))
            {
               this.var_467 = SoundManager.Play(SoundConfig.var_1849,1,true);
            }
         }
         else
         {
            if(this.var_436)
            {
               this.var_436 = SoundManager.method_155(this.var_436);
            }
            if(this.var_467)
            {
               this.var_467 = SoundManager.method_155(this.var_467);
            }
         }
      }
      
      public function method_1030() : void
      {
         var _loc1_:PowerType = null;
         var _loc2_:Entity = null;
         if(this.var_1.var_256)
         {
            this.var_1.var_256.visible = false;
         }
         _loc1_ = this.GetMeleePower();
         if(Boolean(this.combatState) && Boolean(_loc1_))
         {
            _loc2_ = this.combatState.method_656(_loc1_);
            if(!_loc2_ && Boolean(this.var_485))
            {
               _loc2_ = this.var_1.GetEntFromID(this.var_485);
            }
            if(_loc2_)
            {
               _loc2_.method_280();
               if(!this.var_1.var_256)
               {
                  this.var_1.var_256 = class_4.method_16("a_TargetDiamond");
                  this.var_1.var_272.addChild(this.var_1.var_256);
               }
               this.var_1.var_256.x = _loc2_.appearPosX;
               this.var_1.var_256.y = _loc2_.appearPosY + 20;
               this.var_1.var_256.visible = true;
               this.var_1.var_2755 = _loc2_.id;
            }
         }
      }
      
      private function method_1656() : void
      {
         var _loc1_:Number = NaN;
         var _loc2_:Number = NaN;
         var _loc3_:Point = null;
         var _loc4_:class_37 = null;
         var _loc5_:Point = null;
         if(this.var_1122)
         {
            return;
         }
         if(Boolean(this.var_1.level) && this.physPosY > this.var_1.level.var_1266)
         {
            _loc1_ = 0.01;
            _loc2_ = 0.01;
            if(this.cue)
            {
               if(this.cue.bDidGroundSnap)
               {
                  _loc1_ = this.cue.groupSnapPos.x;
                  _loc2_ = this.cue.groupSnapPos.y;
               }
               else
               {
                  _loc1_ = (_loc5_ = this.var_1.method_234(this.cue)).x;
                  _loc2_ = _loc5_.y;
               }
            }
            else if(this.var_1.level.var_239)
            {
               _loc1_ = this.var_1.level.var_239.x;
               _loc2_ = this.var_1.level.var_239.y;
            }
            _loc3_ = new Point();
            if(_loc4_ = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc2_ - 19,new Point(0,120),_loc3_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0))
            {
               _loc1_ = _loc3_.x;
               _loc2_ = _loc3_.y - Entity.PULLBACK_DIST;
            }
            this.TeleportTo(_loc1_,_loc2_);
         }
      }
      
      public function method_1075() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:PowerType = null;
         this.var_2270 = false;
         this.var_1714 = false;
         this.var_1944 = false;
         for each(_loc1_ in this.var_471)
         {
            if(_loc1_ == class_143.PRESSED_FIRE)
            {
               this.var_2270 = true;
               this.bFiring = true;
            }
            else if(_loc1_ == class_143.RELEASED_FIRE)
            {
               this.bFiring = false;
            }
            else if(_loc1_ == class_143.PRESSED_DROP)
            {
               this.var_1715 = true;
               this.var_1714 = true;
               this.bDropping = true;
            }
            else if(_loc1_ == class_143.RELEASED_DROP)
            {
               this.bDropping = false;
            }
            else if(_loc1_ == class_143.PRESSED_JUMP)
            {
               if(this.method_1151())
               {
                  this.var_1872 = true;
                  this.var_1944 = true;
                  this.bJumping = true;
               }
            }
            else if(_loc1_ == class_143.RELEASED_JUMP)
            {
               this.bJumping = false;
            }
         }
         this.var_471.length = 0;
         if(!this.combatState.mActivePower && (this.bFiring || this.var_2270))
         {
            if(this.method_529())
            {
               this.combatState.method_51(this.GetMeleePower(),true);
            }
            else if(!this.combatState.var_1488 && (!this.brain || this.brain.target || this.behaviorType.var_1267))
            {
               _loc2_ = this.GetRangedPower();
               if(_loc2_)
               {
                  this.combatState.method_51(_loc2_,true);
               }
            }
         }
      }
      
      public function method_1770() : Boolean
      {
         var _loc1_:Number = NaN;
         var _loc2_:uint = 0;
         var _loc3_:Entity = null;
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         var _loc6_:PowerType = null;
         _loc1_ = this.velocity.x;
         _loc2_ = this.var_1.mTimeThisTick;
         if(this.var_1835)
         {
            return false;
         }
         if(this.entState == const_6 && !this.var_24 && !this.behaviorType.var_995 && _loc2_ - this.var_217 >= TIME_MONSTER_LAYS_DEAD_BEFORE_VANISHING)
         {
            return false;
         }
         if(Boolean(this.var_818.skit) && _loc2_ > this.var_818.var_1500)
         {
            this.method_340(this.var_818.skit,this.var_818);
         }
         if(Boolean(this.var_195.skit) && _loc2_ > this.var_195.var_1500)
         {
            this.method_340(this.var_195.skit,this.var_195);
         }
         if(this.currEmote && this.var_1262 && _loc2_ >= this.var_1262)
         {
            this.currEmote = null;
         }
         this.method_1656();
         if(this.var_1122 && this.var_1.mTimeThisTick - this.var_2170 > const_902)
         {
            this.method_1213();
         }
         if(this.var_99)
         {
            _loc3_ = this.var_1.GetEntFromID(this.summonerId);
            _loc4_ = 0;
            if(Boolean(_loc3_) && Boolean(_loc3_.var_18))
            {
               _loc4_ = _loc3_.var_18.method_102(_loc3_,this.var_99.basePowerName,"SpawnDuration");
            }
            if(this.entState != const_6 && this.var_99.var_1962 && this.var_99.var_1962 + _loc4_ < this.var_1.mTimeThisTick - this.var_1459)
            {
               if(this.entType.entName == "DragonSoul")
               {
                  if(_loc3_)
                  {
                     if(this.var_99.var_7 >= 8)
                     {
                        _loc3_.combatState.RemoveBuff(class_14.buffTypesDict["DragonSoulRank8"]);
                     }
                     else if(this.var_99.var_7 >= 3)
                     {
                        _loc3_.combatState.RemoveBuff(class_14.buffTypesDict["DragonSoulRank3"]);
                     }
                     else
                     {
                        _loc3_.combatState.RemoveBuff(class_14.buffTypesDict["DragonSoulRank1"]);
                     }
                  }
               }
               this.entState = const_6;
               this.var_217 = this.var_1.mTimeThisTick - TIME_MONSTER_LAYS_DEAD_BEFORE_VANISHING + 2000;
               if(this.entType.entName.indexOf("ShadowLegionClone") == 0)
               {
                  if(this.var_99.var_7 >= 4)
                  {
                     if(this.var_99.var_7 >= 10)
                     {
                        this.combatState.method_46(class_14.powerTypesDict["ShadowLegionExplode10"],null,new Point(this.appearPosX,this.appearPosY));
                     }
                     else if(this.var_99.var_7 >= 7)
                     {
                        this.combatState.method_46(class_14.powerTypesDict["ShadowLegionExplode7"],null,new Point(this.appearPosX,this.appearPosY));
                     }
                     else
                     {
                        this.combatState.method_46(class_14.powerTypesDict["ShadowLegionExplode4"],null,new Point(this.appearPosX,this.appearPosY));
                     }
                  }
                  this.var_217 -= 1500;
               }
               if(!this.entType.entName.indexOf("Pet"))
               {
                  this.var_217 -= 1500;
               }
            }
            if(this.entState == const_6)
            {
               if(!this.var_2760)
               {
                  if(this.entType.entName == "Decoy")
                  {
                     _loc3_ = this.var_1.GetEntFromID(this.summonerId);
                     _loc6_ = !!(_loc5_ = !!this.var_99 ? this.var_99.var_7 : 0) ? class_14.powerTypesDict["DecoyExplode" + _loc5_] : class_14.powerTypesDict["DecoyExplode"];
                     _loc3_.combatState.method_46(_loc6_,null,new Point(this.physPosX,this.physPosY));
                  }
                  this.var_2760 = true;
               }
            }
         }
         if(this.entState != const_6)
         {
            if(this.var_24)
            {
               this.var_24.method_550();
            }
            else if(this.brain)
            {
               this.brain.Think();
            }
            this.method_1075();
         }
         this.method_864();
         this.method_900();
         this.combatState.method_960();
         this.method_853();
         this.method_671();
         this.method_819();
         this.method_1368(_loc1_);
         return true;
      }
      
      public function method_1368(param1:Number) : void
      {
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:Date = null;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         var _loc10_:Boolean = false;
         var _loc11_:uint = 0;
         var _loc12_:Number = NaN;
         var _loc13_:Packet = null;
         this.var_1136 = this.var_1136 || this.bJumping != this.var_2533 || this.bDropping != this.var_2788 || this.bRunning != this.var_2701 || this.bLeft != this.var_2252 || this.bBackpedal != this.var_2079 || this.entState != this.var_2458;
         this.var_2533 = this.bJumping;
         this.var_2788 = this.bDropping;
         this.var_2701 = this.bRunning;
         this.var_2252 = this.bLeft;
         this.var_2079 = this.bBackpedal;
         this.var_2458 = this.entState;
         _loc2_ = this.startPhysPosX - this.physPosX;
         _loc3_ = this.startPhysPosY - this.physPosY;
         _loc4_ = param1 - this.velocity.x;
         if(_loc2_ < -0.0001 || _loc2_ > 0.0001 || _loc3_ < -0.0001 || _loc3_ > 0.0001 || _loc4_ < -0.0001 || _loc4_ > 0.0001)
         {
            this.var_1630 = true;
         }
         if(Boolean(this.var_24) && this.var_1.mTimeThisTick - this.var_2832 >= 1000)
         {
            _loc5_ = new Date();
            _loc6_ = getTimer();
            if(!this.var_1712)
            {
               this.var_1712 = _loc6_;
               this.var_2360 = _loc5_.time;
               this.var_2348 = -120000;
            }
            _loc7_ = _loc6_ - this.var_1712;
            _loc8_ = _loc5_.time - this.var_2360;
            _loc9_ = _loc7_ > _loc8_ ? _loc7_ - _loc8_ : _loc8_ - _loc7_;
            _loc10_ = false;
            if(_loc9_ >= 1000)
            {
               if((_loc12_ = _loc6_ - this.var_2348) < 120000)
               {
                  _loc10_ = true;
               }
               else
               {
                  this.var_2348 = _loc6_;
                  this.var_1712 = _loc6_;
                  this.var_2360 = _loc5_.time;
               }
            }
            _loc11_ = this.var_1.mServerGameTime;
            if(_loc10_ || _loc11_ - this.var_2695 >= const_1053)
            {
               (_loc13_ = new Packet(LinkUpdater.const_1090)).method_24(_loc7_);
               _loc13_.method_15(_loc10_);
               _loc13_.method_24(_loc8_);
               this.var_1.serverConn.SendPacket(_loc13_);
               this.var_2695 = _loc11_;
            }
            this.var_2832 = this.var_1.mTimeThisTick;
         }
      }
      
      public function method_1948() : void
      {
         var _loc1_:Point = null;
         var _loc2_:Level = null;
         var _loc4_:Packet = null;
         var _loc5_:class_105 = null;
         var _loc6_:Packet = null;
         this.var_24.var_418.method_1073();
         _loc1_ = this.var_24.method_375(class_36.const_922);
         this.method_1597(_loc1_);
         this.method_1589(_loc1_,this.var_10,this.var_12);
         this.method_1766(_loc1_);
         this.method_1524();
         this.method_1030();
         if(!this.bFiring || this.var_1.level.bInstanced)
         {
            this.var_807 = 0;
         }
         else if(!this.var_807)
         {
            this.var_807 = this.var_1.mTimeThisTick;
         }
         if(Boolean(this.var_807) && this.var_1.mTimeThisTick - this.var_807 >= const_994)
         {
            _loc4_ = new Packet(LinkUpdater.const_1171);
            this.var_1.serverConn.SendPacket(_loc4_);
            this.var_807 = 0;
         }
         _loc2_ = this.var_1.level;
         var _loc3_:String = _loc2_.internalName;
         if(_loc2_.var_333)
         {
            if((Boolean(_loc5_ = this.var_1.mBuildingInfo)) && _loc5_.mStatus == class_105.const_521)
            {
               _loc5_.method_1421();
               _loc6_ = new Packet(LinkUpdater.const_878);
               this.var_1.serverConn.SendPacket(_loc6_);
            }
            if(Boolean(this.currRoom) && !this.currRoom.var_2420)
            {
               if(!_loc2_.var_2081)
               {
                  _loc2_.method_977();
               }
               else if(_loc2_.var_811)
               {
                  _loc2_.method_735();
                  this.currRoom.var_2420 = true;
               }
            }
         }
      }
      
      public function method_1088(param1:EntType) : void
      {
         if(Boolean(this.var_694) && !param1)
         {
            this.var_2358 = true;
         }
         this.var_694 = param1;
         this.gfx.method_957(!!this.var_694 ? this.var_694.gfxType : null);
         this.gfx.m_Seq.method_108();
      }
      
      public function method_2002(param1:EntType) : void
      {
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         var _loc6_:Point = null;
         var _loc7_:Seq = null;
         var _loc8_:class_26 = null;
         this.var_2337 = param1;
         if(this.var_183)
         {
            this.var_183.entState = const_6;
            this.var_183.var_217 = this.var_1.mTimeThisTick - TIME_MONSTER_LAYS_DEAD_BEFORE_VANISHING + this.var_2776;
            this.var_183.velocity.x = 0;
            this.var_183.velocity.y = 0;
            this.var_183.bRunning = false;
            this.var_183.bDropping = false;
            this.var_183.bJumping = false;
            this.var_183 = null;
         }
         if(param1)
         {
            _loc2_ = 50;
            _loc3_ = 100;
            _loc3_ = this.bFacingLeft() ? _loc3_ : _loc3_ * -1;
            _loc4_ = this.physPosX + _loc3_;
            _loc5_ = this.physPosY - _loc2_;
            _loc6_ = new Point(0,0);
            if(this.var_1.collMan.getFloorCollision(0,this.physPosX,this.physPosY - _loc2_,new Point(_loc3_,0),_loc6_,null,null,null,CollisionManager.HARD_FLOOR,0))
            {
               _loc4_ = _loc6_.x;
               _loc5_ = _loc6_.y;
               _loc4_ += this.bFacingLeft() ? -2 : 2;
            }
            this.var_183 = new Entity(this.var_1,this.var_2337.entName,null,_loc4_,_loc5_,Entity.LOCAL | Entity.MONSTER | Entity.const_241,Entity.NEUTRAL,0,0,this.id,null,null,null,null,null,null);
            this.var_1.entities.push(this.var_183);
            _loc8_ = (_loc7_ = this.var_183.gfx.m_Seq).var_218;
            _loc7_.var_218 = _loc8_;
            _loc7_.var_689 = _loc8_;
            _loc7_.var_348 = _loc8_;
            _loc7_.var_463 = _loc8_;
            _loc7_.var_384 = _loc8_;
         }
      }
      
      private function method_1151() : Boolean
      {
         if(this.combatState && this.combatState.mActivePower && this.combatState.mActivePower.powerType.basePowerName == "LeapStrike")
         {
            return false;
         }
         if(Boolean(this.combatState) && this.combatState.var_1313)
         {
            return false;
         }
         if(Boolean(this.combatState) && this.combatState.var_39 == class_14.powerTypesDict["SentinelForm1"].powerID)
         {
            return false;
         }
         return true;
      }
      
      public function method_247(param1:Boolean, param2:Boolean, param3:int = 0) : void
      {
         var _loc4_:PowerType = null;
         var _loc5_:PowerType = null;
         var _loc6_:Number = NaN;
         var _loc7_:Seq = null;
         var _loc8_:Dictionary = null;
         _loc4_ = class_14.powerTypesDict["SentinelForm1"];
         if(this.combatState.var_39)
         {
            if(!param1 && this.combatState.var_39 == _loc4_.powerID)
            {
               _loc5_ = class_14.powerTypesDict["SentinelForm" + this.combatState.var_498];
               this.var_494 = false;
               if(!param2)
               {
                  this.combatState.RemoveBuff(class_14.buffTypesDict["SentinelForm" + this.combatState.var_498]);
               }
               this.entType.gfxType = this.entType.method_60();
               this.combatState.var_39 = 0;
               this.combatState.var_498 = 0;
               this.ResetEntType(this.entType);
               this.gfx.m_Seq.method_108();
               this.combatState.var_545 = false;
               this.combatState.var_114[_loc5_.powerID] = this.var_1.mTimeThisTick + _loc5_.coolDownTime;
               _loc6_ = 0.75 * (this.var_31 / this.const_156);
               this.combatState.method_390(_loc5_,_loc6_);
               this.var_31 = 0;
               if(this.id == this.var_1.clientEntID)
               {
                  this.var_1.method_114(this.var_31);
               }
            }
         }
         else if(param1)
         {
            this.var_494 = true;
            this.combatState.var_39 = _loc4_.powerID;
            this.combatState.var_498 = param3;
            this.ResetEntType(this.entType);
            if((_loc8_ = (_loc7_ = this.gfx.m_Seq).var_71.var_69)["HeavyFall"])
            {
               _loc7_.var_348 = _loc8_["HeavyFall"];
            }
            if(_loc8_["HeavyDrop"])
            {
               _loc7_.var_384 = _loc8_["HeavyDrop"];
            }
            if(_loc8_["HeavyHitReact"])
            {
               _loc7_.var_1304 = _loc8_["HeavyHitReact"];
            }
            if(_loc8_["HeavyReady"])
            {
               _loc7_.var_218 = _loc8_["HeavyReady"];
            }
            if(_loc8_["HeavyWalk"])
            {
               _loc7_.var_463 = _loc8_["HeavyWalk"];
            }
            this.var_31 = 100;
            if(this.id == this.var_1.clientEntID)
            {
               this.var_1.method_114(this.var_31);
            }
         }
      }
      
      public function method_262(param1:Boolean, param2:Boolean, param3:int = 0) : void
      {
         var _loc4_:int = 0;
         var _loc5_:GfxType = null;
         var _loc6_:SuperAnimInstance = null;
         _loc4_ = this.var_1.playerEntLayer.getChildIndex(this.gfx.m_TheDO);
         if(this.combatState.var_39)
         {
            if(this.combatState.var_39 == class_14.powerTypesDict["HailstoneEmbrace1"].powerID && !param1)
            {
               if(!param2)
               {
                  this.combatState.RemoveBuff(class_14.buffTypesDict["IceArmor" + this.combatState.var_498]);
                  this.combatState.RemoveBuff(class_14.buffTypesDict["MistEffect"]);
               }
               this.var_494 = false;
               this.combatState.var_39 = 0;
               this.combatState.var_498 = 0;
               this.entType.gfxType = this.entType.method_60();
               this.ResetEntType(this.entType);
               (_loc5_ = new GfxType()).var_29 = "SFX_3.swf";
               _loc5_.bFireAndForget = true;
               _loc5_.animClass = "a_FrostArmorFallOff";
               (_loc6_ = new SuperAnimInstance(this.var_1,_loc5_,true)).m_TheDO.x = this.var_10;
               _loc6_.m_TheDO.y = this.var_12;
               _loc6_.m_TheDO.scaleX = Math.random() > 0.5 ? -1 : 1;
               this.var_1.playerEntLayer.addChildAt(_loc6_.m_TheDO,_loc4_ + 1);
               this.combatState.var_545 = false;
            }
         }
         else if(param1)
         {
            this.combatState.var_39 = class_14.powerTypesDict["HailstoneEmbrace1"].powerID;
            this.combatState.var_498 = param3;
            this.var_494 = true;
            this.ResetEntType(this.entType);
         }
         this.var_1.playerEntLayer.setChildIndex(this.gfx.m_TheDO,_loc4_);
      }
      
      public function method_391(param1:Boolean, param2:Boolean) : void
      {
         var _loc3_:int = 0;
         _loc3_ = this.var_1.playerEntLayer.getChildIndex(this.gfx.m_TheDO);
         if(this.combatState.var_39)
         {
            if(this.combatState.var_39 == class_14.powerTypesDict["SeekingBlades1"].powerID && !param1)
            {
               if(!param2)
               {
                  this.combatState.RemoveBuff(class_14.buffTypesDict["SeekingBlades"]);
               }
               this.var_494 = false;
               this.combatState.var_39 = 0;
               this.entType.gfxType = this.entType.method_60();
               this.ResetEntType(this.entType);
               this.combatState.var_545 = false;
            }
         }
         else
         {
            this.combatState.var_39 = class_14.powerTypesDict["SeekingBlades1"].powerID;
            this.var_494 = true;
            this.ResetEntType(this.entType);
         }
         this.var_1.playerEntLayer.setChildIndex(this.gfx.m_TheDO,_loc3_);
      }
      
      public function method_475(param1:Boolean, param2:Boolean, param3:int = 0) : void
      {
         var _loc4_:int = 0;
         var _loc5_:String = null;
         _loc4_ = this.var_1.playerEntLayer.getChildIndex(this.gfx.m_TheDO);
         if(this.combatState.var_39)
         {
            if(this.combatState.var_39 == class_14.powerTypesDict["Pyromania1"].powerID && !param1)
            {
               if(!param2)
               {
                  _loc5_ = "Pyromania";
                  if(this.combatState.var_498)
                  {
                     _loc5_ += this.combatState.var_498;
                  }
                  this.combatState.RemoveBuff(class_14.buffTypesDict[_loc5_]);
               }
               this.var_494 = false;
               this.combatState.var_39 = 0;
               this.combatState.var_498 = 0;
               this.entType.gfxType = this.entType.method_60();
               this.ResetEntType(this.entType);
               this.combatState.var_545 = false;
            }
         }
         else
         {
            this.combatState.var_39 = class_14.powerTypesDict["Pyromania1"].powerID;
            this.combatState.var_498 = param3;
            this.var_494 = true;
            this.ResetEntType(this.entType);
         }
         this.var_1.playerEntLayer.setChildIndex(this.gfx.m_TheDO,_loc4_);
      }
      
      public function method_354(param1:Boolean, param2:Boolean, param3:int = 0) : void
      {
         var _loc4_:int = 0;
         _loc4_ = this.var_1.playerEntLayer.getChildIndex(this.gfx.m_TheDO);
         if(this.combatState.var_39)
         {
            if(this.combatState.var_39 == class_14.powerTypesDict["ShadowArmor1"].powerID && !param1)
            {
               if(!param2)
               {
                  this.combatState.RemoveBuff(class_14.buffTypesDict["ShadowArmor" + param3]);
               }
               this.var_494 = false;
               this.combatState.var_39 = 0;
               this.entType.gfxType = this.entType.method_60();
               this.ResetEntType(this.entType);
               this.combatState.var_545 = false;
            }
         }
         else if(param1)
         {
            this.combatState.var_39 = class_14.powerTypesDict["ShadowArmor1"].powerID;
            this.var_494 = true;
            this.ResetEntType(this.entType);
         }
         this.var_1.playerEntLayer.setChildIndex(this.gfx.m_TheDO,_loc4_);
      }
      
      public function method_1658() : void
      {
         var _loc1_:Vector.<Entity> = null;
         var _loc2_:Entity = null;
         _loc1_ = this.var_1.entities;
         for each(_loc2_ in _loc1_)
         {
            if(_loc2_.summonerId && _loc2_.brain && _loc2_.summonerId == this.id)
            {
               _loc2_.brain.method_356();
            }
         }
      }
      
      public function method_1138(param1:PowerType, param2:int) : void
      {
         if(param2 > this.hudPowers.length)
         {
            return;
         }
         if(!this.var_234)
         {
            this.var_234 = new Vector.<PowerType>(this.hudPowers.length);
         }
         this.hudPowers[param2] = param1;
         this.var_234[param2] = param1;
      }
      
      public function method_993(param1:PowerType) : void
      {
         var _loc2_:Boolean = false;
         var _loc3_:int = 0;
         var _loc4_:int = 0;
         _loc2_ = false;
         if(this.var_234)
         {
            _loc3_ = int(this.var_234.length);
            _loc4_ = 0;
            while(_loc4_ < _loc3_)
            {
               if(this.var_234[_loc4_] == param1)
               {
                  this.var_234[_loc4_] = null;
                  _loc2_ = true;
               }
               _loc4_++;
            }
            if(_loc2_)
            {
               this.method_904();
            }
         }
      }
      
      public function method_1886() : void
      {
         this.combatState.var_1995 = 1;
         this.combatState.var_937 = 0;
         this.combatState.var_1146 = 0;
         this.combatState.masterDangerRegenInterval = 0;
         this.combatState.var_2951 = 0;
         this.combatState.var_2579 = 0;
         this.combatState.var_1586 = 0;
         this.combatState.var_663 = 0;
         this.combatState.var_2163 = 0;
         this.combatState.var_1853 = 0;
         this.combatState.var_2036 = false;
         if(this.mMasterClass == "frostwarden")
         {
            this.combatState.var_937 = 330;
            this.combatState.masterDangerRegenInterval = 990;
            this.combatState.var_354 = BuffType.const_1274;
         }
         else if(this.mMasterClass == "executioner")
         {
            this.combatState.var_1146 = 0.4;
            this.combatState.var_354 = BuffType.const_1100;
         }
         else if(this.mMasterClass == "sentinel")
         {
            this.combatState.var_354 = BuffType.const_1210;
         }
         else if(this.mMasterClass == "flameseer")
         {
            this.combatState.var_937 = 800;
            this.combatState.var_1995 = -1;
            this.combatState.var_1146 = 0.7;
            this.combatState.var_354 = BuffType.const_1049;
         }
         else if(this.mMasterClass == "shadowwalker")
         {
            this.combatState.var_937 = 330;
            this.combatState.var_354 = BuffType.const_1275;
         }
         else if(this.mMasterClass == "justicar")
         {
            this.combatState.var_354 = BuffType.const_986;
         }
         else if(this.mMasterClass == "necromancer")
         {
            this.combatState.var_937 = 200;
            this.combatState.var_354 = BuffType.const_1268;
         }
         else if(this.mMasterClass == "templar")
         {
            this.combatState.var_354 = BuffType.const_1025;
         }
         else if(this.mMasterClass == "soulthief")
         {
            this.combatState.var_1146 = 0.4;
            this.combatState.var_354 = BuffType.const_1056;
         }
         else
         {
            this.combatState.var_354 = BuffType.const_624;
         }
         this.method_904();
      }
      
      public function method_904() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:int = 0;
         var _loc3_:int = 0;
         _loc1_ = this.var_85.method_245();
         this.var_280 = this.GetPowerFromAbilityType(this.method_302(this.mMasterClass,0));
         this.hudPowers[4] = this.GetPowerFromAbilityType(this.method_302(this.mMasterClass,4));
         switch(_loc1_)
         {
            case 6:
               this.hudPowers[6] = this.GetPowerFromAbilityType(this.method_302(this.mMasterClass,6));
            case 5:
               this.hudPowers[5] = this.GetPowerFromAbilityType(this.method_302(this.mMasterClass,5));
         }
         if(this.var_234)
         {
            _loc2_ = int(this.var_234.length);
            _loc3_ = 0;
            while(_loc3_ < _loc2_)
            {
               if(this.var_234[_loc3_])
               {
                  this.hudPowers[_loc3_] = this.var_234[_loc3_];
               }
               _loc3_++;
            }
         }
         if(!this.var_2455 && Boolean(this.hudPowers))
         {
            this.var_2455 = true;
            if(Boolean(this.hudPowers[4]) && Boolean(this.hudPowers[4].coolDownTime))
            {
               this.combatState.var_114[this.hudPowers[4].powerID] = this.var_1.mTimeThisTick + this.hudPowers[4].coolDownTime;
            }
            if(Boolean(this.hudPowers[5]) && Boolean(this.hudPowers[5].coolDownTime))
            {
               this.combatState.var_114[this.hudPowers[5].powerID] = this.var_1.mTimeThisTick + this.hudPowers[5].coolDownTime;
            }
            if(Boolean(this.hudPowers[6]) && Boolean(this.hudPowers[6].coolDownTime))
            {
               this.combatState.var_114[this.hudPowers[6].powerID] = this.var_1.mTimeThisTick + this.hudPowers[6].coolDownTime;
            }
         }
      }
      
      public function method_1494() : uint
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         _loc1_ = this.var_1.mMasterClassTower.GetPointsByMC(this.mMasterClass);
         _loc2_ = this.mExpLevel >= 10 ? uint(this.mExpLevel - 10) : 0;
         return _loc1_ + _loc2_;
      }
      
      public function method_2054() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:class_9 = null;
         _loc1_ = !!this.mMasterClass ? class_9.method_472(this.mMasterClass) : 0;
         _loc2_ = class_14.var_278[_loc1_];
         _loc2_.rank = Math.round(Math.random() * (this.mExpLevel / 2) + this.mExpLevel / 2);
      }
      
      public function getTowerLevel() : uint
      {
         var _loc1_:uint = 0;
         var _loc2_:class_9 = null;
         _loc1_ = !!this.mMasterClass ? class_9.method_472(this.mMasterClass) : 0;
         _loc2_ = class_14.var_278[_loc1_];
         return _loc2_.rank;
      }
      
      public function method_1828() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc3_:Number = NaN;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:int = 0;
         var _loc7_:Number = NaN;
         var _loc8_:uint = 0;
         var _loc9_:Packet = null;
         var _loc10_:EntTypeGear = null;
         var _loc11_:String = null;
         var _loc12_:GearType = null;
         var _loc13_:class_64 = null;
         var _loc14_:class_64 = null;
         var _loc15_:class_64 = null;
         _loc1_ = 0;
         _loc2_ = this.var_18.method_64("Health");
         _loc3_ = 0;
         _loc4_ = uint(method_128(this.var_64));
         _loc5_ = 0;
         _loc6_ = 1;
         while(_loc6_ < EntType.MAX_SLOTS)
         {
            if(_loc11_ = !!(_loc10_ = this.entType.equippedGear[_loc6_]) ? _loc10_.gearName : null)
            {
               if(_loc12_ = class_14.gearTypesDict[_loc11_])
               {
                  _loc13_ = !!_loc10_.var_432 ? class_64.method_56(_loc10_.var_432) : null;
                  _loc14_ = !!_loc10_.var_501 ? class_64.method_56(_loc10_.var_501) : null;
                  _loc15_ = !!_loc10_.var_486 ? class_64.method_56(_loc10_.var_486) : null;
                  if(_loc13_)
                  {
                     _loc1_ += this.method_544(_loc13_);
                  }
                  if(_loc14_)
                  {
                     _loc1_ += this.method_544(_loc14_);
                  }
                  if(_loc15_)
                  {
                     _loc1_ += this.method_544(_loc15_);
                  }
                  _loc13_ = null;
                  _loc14_ = null;
                  _loc15_ = null;
                  if(_loc12_.var_100 == "HealthPercent")
                  {
                     _loc3_ += CombatState.const_260;
                  }
                  if(_loc12_.procRune2 == "HeatlhPercent")
                  {
                     _loc3_ += CombatState.const_260;
                  }
               }
            }
            _loc6_++;
         }
         _loc5_ = (_loc5_ += _loc1_) + _loc2_;
         _loc7_ = this.var_18.method_64("HPFromWis");
         _loc8_ = Math.ceil(this.magicDamage * _loc7_);
         _loc5_ += _loc8_;
         _loc5_ += _loc5_ * _loc3_;
         (_loc9_ = new Packet(LinkUpdater.const_900)).method_24(this.var_64);
         _loc9_.method_24(_loc4_);
         _loc9_.method_24(_loc1_);
         _loc9_.method_24(_loc2_);
         _loc9_.method_24(_loc8_);
         _loc9_.method_309(_loc3_);
         _loc9_.method_24(this.currHP);
         this.var_1.serverConn.SendPacket(_loc9_);
      }
      
      public function method_544(param1:class_64) : uint
      {
         var _loc2_:uint = 0;
         var _loc3_:class_1 = null;
         var _loc4_:class_1 = null;
         var _loc5_:Number = NaN;
         _loc2_ = 0;
         _loc3_ = param1.var_13;
         _loc2_ += _loc3_.var_1593;
         if(param1.secondary)
         {
            _loc4_ = param1.method_115();
            _loc5_ = param1.method_421();
            _loc2_ += _loc4_.var_1593 * _loc5_;
         }
         return _loc2_;
      }
      
      public function method_1819(param1:Vector.<uint>) : void
      {
         if(!param1 || param1.length == 0)
         {
            return;
         }
         if(!this.var_1283)
         {
            this.var_1283 = new Vector.<uint>();
         }
         this.var_1283 = this.var_1283.concat(param1);
         this.ResetEntType(this.entType);
      }
      
      public function method_343() : void
      {
         var _loc1_:Vector.<Entity> = null;
         var _loc2_:Entity = null;
         _loc1_ = this.var_1.GetSummonedCreatures(this.id,PowerType.var_315);
         for each(_loc2_ in _loc1_)
         {
            _loc2_.var_1459 = 0;
            _loc2_.entState = const_6;
            _loc2_.var_217 = this.var_1.mTimeThisTick - TIME_MONSTER_LAYS_DEAD_BEFORE_VANISHING + this.var_2776;
            _loc2_.velocity.x = 0;
            _loc2_.velocity.y = 0;
            _loc2_.bRunning = false;
            _loc2_.bDropping = false;
            _loc2_.bJumping = false;
         }
         this.combatState.RemoveBuff(BuffType.var_709);
      }
      
      private function method_1826() : void
      {
         var _loc1_:Seq = null;
         var _loc2_:Seq = null;
         var _loc3_:GfxType = null;
         var _loc4_:Boolean = false;
         var _loc5_:int = 0;
         var _loc6_:EntType = null;
         var _loc7_:Vector.<CustomArt> = null;
         var _loc8_:uint = 0;
         var _loc9_:PowerType = null;
         var _loc10_:class_26 = null;
         var _loc11_:BuffType = null;
         _loc1_ = null;
         _loc2_ = null;
         _loc3_ = null;
         _loc4_ = false;
         if(this.gfx)
         {
            if(Boolean(this.gfx.var_210) && Boolean(this.gfx.var_210.m_Data))
            {
               _loc3_ = this.gfx.var_210.m_Data.var_36;
            }
            _loc4_ = this.gfx.var_1076;
            if(this.gfx.m_Seq.var_350.animClass == this.entType.gfxType.animClass && this.gfx.m_Seq.var_350.var_29 == this.entType.gfxType.var_29)
            {
               _loc1_ = this.gfx.m_Seq;
               this.gfx.m_Seq = null;
               if(this.gfx.var_131)
               {
                  _loc2_ = this.gfx.var_131.m_Seq;
                  this.gfx.var_131.m_Seq = null;
               }
            }
            this.gfx.DestroySuperAnimInstance();
         }
         this.var_10 = this.appearPosX;
         this.var_12 = this.appearPosY - this.entType.height * 0.5;
         if(Boolean(this.combatState.var_39) && this.combatState.var_39 == class_14.powerTypesDict["SentinelForm1"].powerID)
         {
            _loc6_ = EntType.method_48("ThunderGolem");
            this.entType.gfxType = _loc6_.method_60();
         }
         if(this.entType.var_2241 && Boolean(this.var_20 & PLAYER))
         {
            _loc7_ = this.entType.gfxType.customArts;
            _loc8_ = 1;
            while(_loc8_ < EntType.MAX_SLOTS)
            {
               if((Boolean(_loc9_ = this.hudPowers[_loc8_])) && Boolean(_loc9_.var_2346))
               {
                  _loc7_.push(new CustomArt(this.entType.gfxType.var_29,_loc9_.var_2346));
               }
               _loc8_++;
            }
         }
         if(this.var_494)
         {
            if(this.combatState.var_39 == class_14.powerTypesDict["HailstoneEmbrace1"].powerID)
            {
               this.entType.gfxType = this.entType.method_60();
               (_loc7_ = this.entType.gfxType.customArts).push(new CustomArt("Gfx_Mage_1.swf","FrostArmor"));
               if(this.entType.var_439 == "Male")
               {
                  _loc7_.push(new CustomArt("Gfx_Mage_1.swf","FrostArmorMale"));
               }
            }
            else if(this.combatState.var_39 == class_14.powerTypesDict["SeekingBlades1"].powerID)
            {
               this.entType.gfxType = this.entType.method_60();
               (_loc7_ = this.entType.gfxType.customArts).push(new CustomArt("Gfx_Paladin_1.swf","SeekingBlades"));
               _loc7_.push(new CustomArt("Gfx_Rogue_1.swf","SeekingBlades"));
               _loc7_.push(new CustomArt("Animation_Rogue.swf","HatHair"));
            }
            else if(this.combatState.var_39 == class_14.powerTypesDict["ShadowArmor1"].powerID)
            {
               this.entType.gfxType = this.entType.method_60();
               (_loc7_ = this.entType.gfxType.customArts).push(new CustomArt("Gfx_Paladin_1.swf","Midnight"));
               _loc7_.push(new CustomArt("Gfx_Rogue_1.swf","Shade"));
               _loc7_.push(new CustomArt("Animation_Rogue.swf","HatHair"));
            }
            else if(this.combatState.var_39 == class_14.powerTypesDict["Pyromania1"].powerID)
            {
               this.entType.gfxType = this.entType.method_60();
               (_loc7_ = this.entType.gfxType.customArts).push(new CustomArt("Gfx_Mage_1.swf","FlameArmor"));
               if(this.entType.var_439 == "Male")
               {
                  _loc7_.push(new CustomArt("Gfx_Mage_1.swf","FlameArmorMale"));
               }
            }
         }
         if(this.entType.gfxType.animClass == "a__Animation" && this.entType.gfxType.var_29 == "Animation_Rogue.swf")
         {
            this.entType.gfxType.var_918 = true;
         }
         if(this.entType.var_106 == "Wisp")
         {
            this.entType.gfxType.var_918 = true;
         }
         this.entType.gfxType.var_927 = true;
         if(this.entType.var_1685 && this.entType.className == "Mage")
         {
            this.entType.gfxType.var_843 = "Male";
         }
         if(Boolean(this.var_20 & const_16) || this.entType.entName.indexOf("Dragon") != -1)
         {
            this.entType.gfxType.var_177 = 0;
         }
         else if(this.entType.entName.indexOf("Kraken") != -1)
         {
            this.entType.gfxType.var_177 = 0;
         }
         else if(this.entType.var_562 == "NPC")
         {
            this.entType.gfxType.var_177 = 0;
         }
         else if(this.entType.entName.indexOf("Player:") != -1)
         {
            this.entType.gfxType.var_177 *= 0.5;
         }
         this.gfx = new SuperAnimInstance(this.var_1,this.entType.gfxType,this.var_24 != null || Boolean(this.var_20 & const_16));
         this.gfx.m_TheDO.x = this.appearPosX;
         this.gfx.m_TheDO.y = this.appearPosY;
         if(_loc1_)
         {
            this.gfx.m_Seq.method_399();
            this.gfx.m_Seq = _loc1_;
            if(Boolean(this.gfx.var_131) && Boolean(_loc2_))
            {
               this.gfx.var_131.m_Seq.method_399();
               this.gfx.var_131.m_Seq = _loc2_;
            }
         }
         if(this.entType.var_2215)
         {
            this.gfx.method_366(this.entType.var_2215);
         }
         this.gfx.method_957(!!this.var_694 ? this.var_694.gfxType : null);
         if(!this.entType.entName.indexOf("NatureGuard") || !this.entType.entName.indexOf("DragonSoul") || !this.entType.entName.indexOf("ShadowLegionClone") || !this.entType.entName.indexOf("SummonGuard") || !this.entType.entName.indexOf("PetDjinn"))
         {
            if(_loc10_ = this.gfx.m_Seq.var_71.var_69["SummonKO"])
            {
               this.gfx.m_Seq.var_800 = _loc10_;
            }
            if(!this.entType.entName.indexOf("ShadowLegionClone"))
            {
               this.gfx.m_Seq.var_1149 = _loc10_;
               this.gfx.m_Seq.var_1074 = _loc10_;
            }
         }
         if(this.entType.var_562 == "Wisp" || this.entType.var_562 == "Ember")
         {
            this.gfx.m_Seq.var_1074 = null;
            this.gfx.m_Seq.var_1149 = null;
         }
         if(this.entType.entName == "PolarSentry")
         {
            if(_loc10_ = this.gfx.m_Seq.var_71.var_69["Submerge"])
            {
               this.gfx.m_Seq.var_800 = _loc10_;
               this.gfx.m_Seq.var_1003 = _loc10_;
            }
         }
         if(this.var_20 & PLAYER)
         {
            this.gfx.m_Seq.var_1003 = null;
         }
         if(this.cue)
         {
            _loc5_ = this.cue.groupSnapOffsetY;
         }
         else if(this.var_24)
         {
            _loc5_ = 0;
         }
         else if(this.var_20 & PLAYER)
         {
            _loc5_ = -1 + int(Math.random() * -5);
         }
         else if(this.var_20 & const_16)
         {
            _loc5_ = 0;
         }
         else if(Boolean(this.behaviorType) && this.behaviorType.var_844)
         {
            _loc5_ = Entity.YOFFSET_RANGE_HIGH;
         }
         else
         {
            _loc5_ = 1 + int(Math.random() * YOFFSET_RANGE_LOW);
         }
         this.method_511(_loc5_);
         if(this.cue)
         {
            this.var_1958 = this.cue.dramaAnim;
            this.var_1879 = this.cue.sleepAnim;
         }
         this.gfx.method_295(this.gfx.m_Data.var_36.var_209);
         this.entType.var_2241 = false;
         if(_loc3_)
         {
            this.gfx.method_366(_loc3_);
         }
         if(_loc4_)
         {
            _loc11_ = class_14.buffTypesDict["FrostShock"];
            if(this.combatState.var_1957)
            {
               this.gfx.method_627(_loc11_.var_932,_loc11_.var_1235);
               this.gfx.method_325(_loc11_.var_932,_loc11_.var_1235);
            }
         }
      }
      
      private function method_1442() : void
      {
         var _loc1_:Level = null;
         var _loc2_:Array = null;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:Number = NaN;
         var _loc6_:Entity = null;
         var _loc7_:int = 0;
         var _loc8_:int = 0;
         var _loc9_:int = 0;
         var _loc10_:uint = 0;
         var _loc11_:int = 0;
         var _loc12_:Packet = null;
         var _loc13_:int = 0;
         var _loc14_:Packet = null;
         this.behaviorType = BehaviorType.method_367(this.entType.var_562);
         if(Boolean(this.cue) && Boolean(this.cue.behaviorTweaks))
         {
            this.behaviorType = BehaviorType.TweakBehavior(this.behaviorType,this.cue.behaviorTweaks);
         }
         if(Boolean(this.brain) && this.behaviorType.var_1279)
         {
            this.brain.var_2827 = true;
         }
         if(this.var_20 & (PLAYER | const_16))
         {
            _loc1_ = this.var_1.level;
            if(_loc1_.bInstanced && !_loc1_.var_333 && !(this.var_20 & const_16))
            {
               this.var_64 = this.var_1.mBonusLevels + _loc1_.mapLevel;
            }
            else
            {
               this.var_64 = this.mExpLevel;
            }
            this.var_2384 = this.mExpLevel - this.var_64;
            if(this.id == this.var_1.clientEntID)
            {
               this.var_1.method_439(this.mExpLevel,this.var_64);
            }
            this.meleeDamage = 0;
            this.magicDamage = 0;
            this.armorClass = 0;
            this.baseMaxHP = method_128(this.var_64);
         }
         else
         {
            if(this.behaviorType.var_1643)
            {
               if((Boolean(_loc6_ = this.var_1.GetEntFromID(this.summonerId))) && Boolean(_loc6_.mEquipPet))
               {
                  this.var_64 = _loc6_.mEquipPet.var_23 * 2 + 5;
               }
               else
               {
                  this.var_64 = 1;
               }
            }
            else if(this.behaviorType.var_988)
            {
               this.var_64 = this.entType.baseLevel;
            }
            else
            {
               _loc7_ = this.var_1.mBonusLevels;
               if((_loc9_ = (_loc8_ = int(this.entType.baseLevel + this.var_1.level.var_2606)) - this.var_1.level.mapLevel) <= 0)
               {
                  _loc8_ += _loc7_;
               }
               else if(_loc7_ > _loc9_)
               {
                  _loc8_ += _loc7_ - _loc9_;
               }
               if(_loc8_ > MAX_CHAR_LEVEL)
               {
                  _loc8_ = int(MAX_CHAR_LEVEL);
               }
               this.var_64 = _loc8_;
            }
            _loc2_ = EntType.const_132[this.entType.var_138];
            _loc3_ = !!_loc2_ ? uint(_loc2_[this.var_64]) : 0;
            _loc4_ = uint(EntType.const_754[this.var_64]);
            this.meleeDamage = Math.round(_loc3_ * this.entType.meleeDamage);
            this.magicDamage = Math.round(_loc4_ * this.entType.var_1044);
            this.armorClass = Math.round(const_589[this.var_64] * this.entType.armorClass);
            _loc5_ = Number(Game.const_790[this.var_1523]);
            if(this.entType.var_913)
            {
               _loc5_ += Game.const_612;
            }
            this.baseMaxHP = Math.round(this.method_986() * _loc5_);
         }
         this.maxHP = this.baseMaxHP;
         this.var_1785 = const_429;
         this.totalMods = new class_134();
         this.var_1562 = new Dictionary();
         this.var_1516 = new Dictionary();
         this.var_719 = new Dictionary();
         this.var_667 = 0;
         this.var_1472 = new Dictionary();
         this.var_1086 = this.const_1396;
         this.var_640 = 0;
         this.var_1142 = 0;
         this.var_1079 = 0;
         this.var_1293 = 0;
         this.var_66 = new Dictionary();
         this.var_65 = new Dictionary();
         this.var_237 = 0;
         this.var_571 = 0;
         this.var_412 = 0;
         this.var_1028 = 0;
         this.var_1065 = 0;
         this.var_18 = new class_44(this.var_1,this.var_85,this);
         this.method_961(this.var_1.var_2142);
         this.method_1457();
         this.RecalculateSpeed();
         if(this.behaviorType)
         {
            if(this.behaviorType.var_533)
            {
               if(_loc6_ = this.var_1.GetEntFromID(this.summonerId))
               {
                  this.meleeDamage = _loc6_.meleeDamage * this.entType.meleeDamage;
                  this.magicDamage = _loc6_.magicDamage * this.entType.var_1044;
                  this.baseMaxHP = this.entType.var_939 * _loc6_.maxHP;
                  this.maxHP = this.baseMaxHP;
                  this.armorClass = this.entType.armorClass * _loc6_.armorClass;
                  this.var_64 = _loc6_.var_64;
               }
            }
            else if(this.behaviorType.var_1643)
            {
               _loc10_ = 1;
               if((Boolean(_loc6_ = this.var_1.GetEntFromID(this.summonerId))) && Boolean(_loc6_.mEquipPet))
               {
                  if(_loc6_.mEquipPet)
                  {
                     _loc10_ = _loc6_.mEquipPet.var_23;
                  }
                  this.meleeDamage = const_631[_loc10_ - 1] * _loc6_.meleeDamage * this.entType.meleeDamage;
                  this.magicDamage = const_631[_loc10_ - 1] * _loc6_.magicDamage * this.entType.var_1044;
                  this.baseMaxHP = _loc6_.baseMaxHP * this.entType.var_939;
                  this.maxHP = this.baseMaxHP;
                  this.armorClass = _loc6_.armorClass * this.entType.armorClass;
               }
            }
         }
         if(Boolean(this.var_1.clientEntID) && this.var_1.clientEntID == this.id)
         {
            this.var_1.method_418(this.maxHP);
            this.var_1.method_1934(this.meleeDamage,this.magicDamage,this.armorClass);
            this.var_1.method_1189(this.var_412);
            if(!this.var_868)
            {
               this.var_868 = this.maxHP;
            }
            else if(this.var_868 != this.maxHP)
            {
               _loc11_ = this.maxHP - this.var_868;
               (_loc12_ = new Packet(LinkUpdater.const_1127)).method_24(_loc11_);
               this.var_1.serverConn.SendPacket(_loc12_);
               if(this.currHP > this.maxHP)
               {
                  _loc13_ = this.currHP - this.maxHP;
                  this.TakeDamage(_loc13_,true);
                  (_loc14_ = new Packet(LinkUpdater.PKTTYPE_CHAR_REGEN)).method_9(this.id);
                  _loc14_.method_24(-_loc13_);
                  this.var_1.serverConn.SendPacket(_loc14_);
               }
               this.var_868 = this.maxHP;
            }
         }
      }
   }
}
