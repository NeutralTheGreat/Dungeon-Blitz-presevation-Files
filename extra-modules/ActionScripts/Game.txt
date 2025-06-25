package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.DisplayObject;
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import flash.display.PixelSnapping;
   import flash.display.Sprite;
   import flash.display.Stage;
   import flash.display.StageQuality;
   import flash.events.Event;
   import flash.events.KeyboardEvent;
   import flash.events.MouseEvent;
   import flash.external.ExternalInterface;
   import flash.filters.BitmapFilterQuality;
   import flash.filters.BlurFilter;
   import flash.filters.DropShadowFilter;
   import flash.filters.GlowFilter;
   import flash.geom.Matrix;
   import flash.geom.Point;
   import flash.net.SharedObject;
   import flash.ui.Keyboard;
   import flash.utils.ByteArray;
   import flash.utils.Dictionary;
   import flash.utils.getQualifiedClassName;
   import flash.utils.getTimer;
   
   public class Game
   {
      
      public static const const_1057:uint = 6;
      
      public static const const_1135:uint = 2000;
      
      public static const const_390:uint = 5;
      
      public static const const_1267:uint = 20;
      
      public static const const_186:uint = 1 << 0;
      
      public static const const_443:uint = 1 << 1;
      
      public static const const_421:uint = 1 << 2;
      
      public static const const_501:uint = 1 << 3;
      
      public static const const_646:uint = 4;
      
      public static const const_306:uint = 1;
      
      public static const const_313:uint = 2;
      
      public static const const_212:uint = 3;
      
      public static const const_150:uint = 4;
      
      public static const const_266:uint = 5;
      
      public static const const_358:uint = 6;
      
      public static const const_688:uint = 7;
      
      public static const const_393:uint = 8;
      
      public static const const_500:uint = 9;
      
      public static const const_372:uint = 10;
      
      public static const const_433:uint = 11;
      
      public static const const_355:uint = 12;
      
      public static const const_598:uint = 13;
      
      public static const const_349:uint = 14;
      
      public static const TUTORIALSTAGE_ATTOME2:uint = 15;
      
      public static const const_310:uint = 16;
      
      public static const const_377:uint = 17;
      
      public static const const_414:uint = 18;
      
      public static const const_311:uint = 19;
      
      public static const const_392:uint = 20;
      
      public static const const_502:uint = 21;
      
      public static const const_370:uint = 22;
      
      public static const const_389:uint = 23;
      
      public static const const_552:uint = 24;
      
      public static const const_337:uint = 25;
      
      public static const const_270:uint = 26;
      
      public static const const_476:uint = 27;
      
      public static const const_246:uint = 28;
      
      public static const const_253:uint = 29;
      
      public static const const_302:uint = 30;
      
      public static const const_230:uint = 31;
      
      public static const const_287:uint = 32;
      
      public static const const_410:uint = 33;
      
      public static var var_1899:Point = new Point(3338,200);
      
      public static var var_2120:Point = new Point(3158,200);
      
      public static var var_1423:Point = new Point(1638,500);
      
      public static var var_1834:Point = new Point(925,1100);
      
      public static var var_2097:Point = new Point(-850,1020);
      
      public static var var_2251:Point = new Point(680,1100);
      
      public static var var_2277:Point = new Point(270,1200);
      
      public static var var_2365:Point = new Point(2550,1190);
      
      public static var var_2177:Point = new Point(1899,1210);
      
      public static var var_2073:Point = new Point(2110,1150);
      
      private static const const_480:Dictionary = new Dictionary();
      
      private static const const_727:Dictionary = new Dictionary();
      
      private static const const_662:Dictionary = new Dictionary();
      
      public static const const_703:uint = 1200;
      
      public static const const_181:int = 180;
      
      private static const const_1226:uint = 4194304;
      
      public static const UPGRADE_TIMEOUT:uint = 10;
      
      public static const const_1344:Number = 1.75;
      
      internal static const const_153:int = 1;
      
      internal static const const_151:int = 2;
      
      internal static const const_158:int = 3;
      
      internal static const const_188:int = 4;
      
      internal static const COMMAND_SPELL1:int = 5;
      
      internal static const COMMAND_SPELL2:int = 6;
      
      internal static const COMMAND_SPELL3:int = 7;
      
      internal static const COMMAND_SPELL4:int = 8;
      
      internal static const COMMAND_SPELL5:int = 9;
      
      internal static const COMMAND_SPELL6:int = 10;
      
      internal static const const_277:int = 11;
      
      internal static const const_274:int = 12;
      
      internal static const const_401:int = 13;
      
      internal static const const_317:int = 14;
      
      internal static const const_328:int = 15;
      
      internal static const const_346:int = 16;
      
      internal static const const_367:int = 17;
      
      internal static const const_364:int = 18;
      
      internal static const const_357:int = 19;
      
      internal static const const_314:int = 20;
      
      internal static const const_329:int = 21;
      
      internal static const const_321:int = 22;
      
      internal static const const_320:int = 23;
      
      internal static const const_458:int = 24;
      
      internal static const const_430:int = 25;
      
      internal static const const_574:int = 26;
      
      public static const const_79:uint = 26;
      
      internal static const const_240:int = 28;
      
      internal static const const_570:int = 29;
      
      internal static const const_543:int = 30;
      
      internal static const COMMAND2_SCROLLUP:int = 1;
      
      internal static const COMMAND2_SCROLLDOWN:int = 2;
      
      internal static const COMMAND2_ESCAPE:int = 3;
      
      internal static const COMMAND2_ENTER:int = 4;
      
      internal static const COMMAND2_BACKSPACE:int = 5;
      
      internal static const COMMAND2_DELETE:int = 6;
      
      internal static const const_526:int = 0;
      
      internal static const const_533:int = 1;
      
      internal static const const_545:int = 2;
      
      internal static const const_437:int = 3;
      
      internal static const const_442:int = 4;
      
      internal static const const_415:int = 5;
      
      internal static const const_472:int = 6;
      
      internal static const const_479:int = 7;
      
      internal static const const_491:int = 8;
      
      internal static const const_550:int = 9;
      
      internal static const const_209:int = 4;
      
      internal static const const_21:Array = new Array();
      
      internal static const const_85:Dictionary = new Dictionary();
      
      public static const const_1108:uint = 0;
      
      public static const const_394:uint = 1;
      
      public static const const_666:uint = 2;
      
      public static const const_528:uint = 3;
      
      public static var var_2979:int;
      
      public static var var_172:class_91;
      
      public static const const_152:uint = CollisionManager.const_110 << 0;
      
      public static const const_140:uint = CollisionManager.const_110 << 1;
      
      public static const const_237:uint = CollisionManager.const_110 << 2;
      
      public static const const_160:uint = CollisionManager.const_110 << 3;
      
      public static const const_391:uint = CollisionManager.const_110 << 4;
      
      public static const const_250:uint = CollisionManager.const_110 << 5;
      
      public static const const_469:uint = CollisionManager.const_110 << 6;
      
      public static const const_682:uint = CollisionManager.const_110 << 7;
      
      public static const const_413:uint = CollisionManager.const_110 << 8;
      
      public static const const_403:Number = 0.25;
      
      public static const const_908:Matrix = new Matrix(const_403,0,0,const_403);
      
      public static const const_1021:BlurFilter = new BlurFilter(3,3,BitmapFilterQuality.HIGH);
      
      public static const const_1232:Number = 20;
      
      public static const const_452:Number = 1 / const_1232;
      
      public static const GAME_VERSION:uint = 100;
      
      public static const const_914:String = "815bfb010cd7b1b4e6aa90abc7679028";
      
      public static const const_858:String = "aab5525963671384955f114997e5180008dd54df";
      
      public static const const_971:String = "cc9c404568c085b07491b25d000f6094";
      
      public static const const_869:String = "ccd780b26950c033e11f553ff1ee0a2c48a104cb";
      
      public static const const_175:uint = 255;
      
      public static const const_745:uint = 32767;
      
      public static const const_579:uint = 2147483647;
      
      public static const ENEMY:uint = 1 << 1;
      
      public static const MELEEABLE:uint = 1 << 2;
      
      public static const FRIEND:uint = 1 << 3;
      
      public static const INTENTIONAL_MELEE:uint = 1 << 4;
      
      public static const ONLY_DEADGUYS:uint = 1 << 5;
      
      public static const STATE_LOGIN:String = "Login";
      
      public static const STATE_TRANSFER:String = "Transfer";
      
      public static const STATE_PLAY:String = "Play";
      
      public static const STATE_NONE:String = "None";
      
      public static const const_207:uint = 8;
      
      public static const const_1385:uint = 8;
      
      public static const TARGETFPS:Number = 24;
      
      public static const const_690:uint = 4000;
      
      public static const const_1375:uint = 4;
      
      public static const const_813:uint = 2;
      
      public static const const_1078:Array = [1,1.2,1.4,1.6];
      
      public static const const_1085:Number = 1.5;
      
      public static const const_790:Array = [1,1.7,2.4,3.1];
      
      public static const const_612:Number = 1.5;
      
      public static const const_794:uint = 4;
      
      private static var sGlobalTimeOrder:Vector.<String> = null;
      
      private static var sGlobalTimeMap:Dictionary = null;
      
      private static const const_950:Number = 200;
      
      private static const MIN_TIME_BETWEEN_INTERACTS:int = 50;
      
      private static var var_1484:Point = new Point();
      
      private static const const_906:Number = 20;
      
      public static const const_1376:String = "Gear";
      
      public static const const_1015:String = "Loot";
      
      public static const const_404:String = "Display";
      
      public static const const_95:String = "Icon";
      
      public static const const_1315:String = "Dye";
      
      private static var timeSpent:Array = new Array();
      
      private static var timeStarted:Array = new Array();
      
      public static var bTracePerf:Boolean = false;
      
      private static const const_508:String = "a_CustomMouse_UI";
      
      private static const const_536:String = "a_CustomMouse_SwordMelee";
      
      private static const const_438:String = "a_CustomMouse_SwordRanged";
      
      private static const const_680:String = "a_CustomMouse_Chat";
      
      private static const const_766:String = "a_CustomMouse_ChatMore";
      
      private static const const_818:String = "a_CustomMouse_ChatEnd";
      
      private static const const_827:String = "a_CustomMouse_Hotspot";
      
      private static const const_811:String = "a_CustomMouse_Inspect";
      
      private static const const_777:String = "a_CustomMouse_Door";
      
      private static const const_702:String = "a_CustomMouse_ZoneDoor";
      
      private static const const_824:String = "a_CustomMouse_Forge";
      
      private static const const_1043:String = "a_CustomMouse_Forge";
      
      private static const const_580:String = "a_CustomMouse_Housing";
      
      private static const const_693:String = "a_CustomMouse_Key";
      
      private static const const_1054:String = "a_CustomMouse_KeyWaiting";
      
      private static const const_581:String = "a_CustomMouse_Dye";
      
      private static const const_634:String = "a_CustomMouse_Sigil";
      
      private static const const_1373:uint = 3;
      
      public static const const_515:DropShadowFilter = new DropShadowFilter(5,45,0,1,5,5);
      
      public static const const_621:DropShadowFilter = new DropShadowFilter(2,45,0,2,3,3);
      
      public static const const_1312:DropShadowFilter = new DropShadowFilter(2,45,0,1,3,3);
      
      public static const const_1309:GlowFilter = new GlowFilter(16777215,1,20,20,0.5,BitmapFilterQuality.HIGH,true);
      
      public static const const_1356:GlowFilter = new GlowFilter(15677476,1,15,15,1,BitmapFilterQuality.HIGH);
      
      public static const const_1413:GlowFilter = new GlowFilter(15655580,1,15,15,3,BitmapFilterQuality.MEDIUM);
      
      public static const const_1380:GlowFilter = new GlowFilter(2293538,1,3,3,2000,BitmapFilterQuality.HIGH);
      
      public static var var_1655:Dictionary = new Dictionary();
      
      {
         method_28(const_306,"am_HighlighterCompleteQuest","NewbieRoad",var_1423);
         method_28(const_313,"am_HighlighterAcceptQuests","NewbieRoad",var_1423);
         method_28(const_212,"am_HighlighterQuestInfo","NewbieRoad",var_1423);
         method_28(const_150,"am_HighlighterMap");
         method_28(const_266,"am_HighlighterTalkToRistas","NewbieRoad",var_1899);
         method_28(const_358,"am_HighlighterAcceptRistasQuest","NewbieRoad",var_1899);
         method_28(const_393,"am_HighlighterHome");
         method_28(const_500,"am_HighlighterTomeArrow","CraftTown",var_1834);
         method_28(const_372,"am_HighlighterLeaveKeep");
         method_28(const_433,"am_HighlighterAcceptAnnaQuest","NewbieRoad",var_2120);
         method_28(const_349,"am_HighlighterTome");
         method_28(TUTORIALSTAGE_ATTOME2,"am_HighlighterTomeArrow","CraftTown",var_1834);
         method_28(const_310,"am_HighlighterBarn");
         method_28(const_377,"am_HighlighterBarnArrow","CraftTown",var_2097);
         method_28(const_311,"am_HighlighterForge");
         method_28(const_392,"am_HighlighterForgeArrow","CraftTown",var_2251);
         method_28(const_370,"am_HighlighterTower");
         method_28(const_389,"am_HighlighterTowerArrow","CraftTown",var_2277);
         method_28(const_337,"am_HighlighterDye");
         method_28(const_270,"am_HighlighterDyeArrow","CraftTown",var_2365);
         method_28(const_246,"am_HighlighterTrove");
         method_28(const_253,"am_HighlighterTroveArrow","CraftTown",var_2177);
         method_28(const_230,"am_HighlighterSigil");
         method_28(const_287,"am_HighlighterSigilArrow","CraftTown",var_2073);
         const_21[const_533] = "executioner";
         const_21[const_545] = "shadowwalker";
         const_21[const_437] = "soulthief";
         const_21[const_442] = "sentinel";
         const_21[const_415] = "justicar";
         const_21[const_472] = "templar";
         const_21[const_479] = "frostwarden";
         const_21[const_491] = "flameseer";
         const_21[const_550] = "necromancer";
         const_85[const_21[const_533]] = "Viperblade";
         const_85[const_21[const_545]] = "Shadowstalker";
         const_85[const_21[const_437]] = "Soulthief";
         const_85[const_21[const_442]] = "Sentinel";
         const_85[const_21[const_415]] = "Justicar";
         const_85[const_21[const_472]] = "Templar";
         const_85[const_21[const_479]] = "Frostbringer";
         const_85[const_21[const_491]] = "Flameseer";
         const_21[const_550] = "necromancer";
         const_85["necromancer"] = "Necromancer";
         var_1655["OminousDungeonLongLoopFunky_26.mp3"] = 2;
      }
      
      internal var main:Main;
      
      internal var var_1040:Sprite;
      
      internal var levelLayer:Sprite;
      
      internal var var_773:Sprite;
      
      internal var playerEntLayer:Sprite;
      
      internal var var_272:Sprite;
      
      internal var var_781:Sprite;
      
      internal var var_89:Sprite;
      
      internal var edgeLayer:Sprite;
      
      internal var var_245:Sprite;
      
      internal var var_256:MovieClip;
      
      internal var var_2755:uint;
      
      internal var var_107:class_23;
      
      internal var var_171:class_82;
      
      internal var var_2560:Array;
      
      internal var var_776:Number = 0;
      
      internal var var_77:class_123;
      
      internal var mUIManager:class_4;
      
      internal var var_1828:class_132;
      
      internal var var_742:class_67;
      
      internal var var_737:class_71;
      
      internal var screenRespecConfirm:class_125;
      
      internal var var_2781:class_47;
      
      internal var var_2059:class_74;
      
      internal var var_2159:class_65;
      
      internal var var_2093:class_98;
      
      internal var var_2231:class_49;
      
      internal var var_2359:class_57;
      
      internal var var_2694:class_128;
      
      internal var var_2582:class_106;
      
      internal var var_2561:class_54;
      
      internal var var_2448:class_55;
      
      internal var var_2761:class_84;
      
      internal var screenNotification:class_46;
      
      internal var screenHud:class_58;
      
      internal var screenHudTopRight:class_70;
      
      internal var screenQuestTracker:class_112;
      
      internal var screenHudTop:class_79;
      
      internal var screenChat:class_127;
      
      internal var screenHudTooltip:class_101;
      
      internal var var_2344:class_59;
      
      internal var var_2306:class_100;
      
      internal var screenWalkthrough:class_62;
      
      internal var var_655:class_97;
      
      internal var screenBuyIdols:class_63;
      
      internal var var_1808:ScreenLevelComplete;
      
      internal var screenLinkBar:class_48;
      
      internal var var_2523:class_126;
      
      internal var screenInteractiveTutorial:class_89;
      
      internal var var_936:class_95;
      
      internal var var_890:class_68;
      
      internal var screenMenu:class_124;
      
      internal var screenRoyalSigilStorePrompt:class_115;
      
      internal var screenRoyalSigilStore:class_107;
      
      internal var screenLockBox:class_73;
      
      internal var screenLockBoxBuyKeys:class_90;
      
      internal var screenLockBoxBuyTroves:class_85;
      
      internal var screenMap:class_119;
      
      internal var screenSocket:class_78;
      
      internal var screenReplace:class_109;
      
      internal var screenFeedPet:class_110;
      
      internal var screenArmory:ScreenArmory;
      
      internal var screenSigil:class_83;
      
      internal var screenKeybind:class_92;
      
      internal var screenSpellbook:class_129;
      
      internal var screenLook:class_102;
      
      internal var var_273:class_51;
      
      internal var screenMasterClassSelection:class_52;
      
      internal var var_996:class_117;
      
      internal var screenCatalysts:class_120;
      
      internal var screenForge:class_75;
      
      internal var screenDyeGear:class_121;
      
      internal var screenClassTowers:class_69;
      
      internal var screenTome:class_50;
      
      internal var var_758:class_88;
      
      internal var screenUpgrading:class_96;
      
      internal var screenBarn:class_99;
      
      internal var screenGoldShort:class_93;
      
      internal var var_1717:class_61;
      
      internal var var_641:class_60;
      
      internal var var_933:ScreenTransfer;
      
      internal var var_94:class_94;
      
      internal var var_398:ScreenNewAccount;
      
      internal var var_479:ScreenLogin;
      
      internal var var_341:ScreenCharacterSelection;
      
      internal var var_141:ScreenCharacterCreation;
      
      internal var screenFriend:class_56;
      
      internal var var_2224:class_80;
      
      internal var mbSleepingLands:Boolean;
      
      internal var tooltip:class_104;
      
      internal var var_137:CustomMouse;
      
      internal var dayNightManager:DayNightManager;
      
      internal var var_406:Vector.<int>;
      
      internal var groupmates:Vector.<class_133>;
      
      internal var var_2905:Vector.<String>;
      
      internal var friendList:Vector.<Friend>;
      
      internal var var_124:Vector.<Friend>;
      
      internal var var_340:Vector.<Friend>;
      
      internal var var_1004:Vector.<Friend>;
      
      internal var mMissionInfoList:Array;
      
      internal var mTrackedMission:class_13;
      
      internal var mTutorialsCompletedList:uint = 0;
      
      internal var mTutorialStage:uint;
      
      internal var mAlertState:uint;
      
      internal var var_2031:Boolean = false;
      
      internal var var_144:Array;
      
      internal var mOwnedGear:Array;
      
      internal var mOwnedGear2:Dictionary;
      
      internal var mFilteredOwnedGear:Array;
      
      internal var mGearsetList:Vector.<Vector.<uint>>;
      
      internal var mGearsetListName:Vector.<String>;
      
      internal var var_3004:uint = 0;
      
      internal var var_2978:uint = 0;
      
      internal var var_2973:uint = 100;
      
      internal var var_2981:Boolean = false;
      
      internal var var_898:uint;
      
      internal var var_1081:uint = 0;
      
      internal var mOwnedMaterials:Array;
      
      internal var mOwnedCharms:Array;
      
      internal var mRespecStoneCount:uint = 0;
      
      internal var mLockboxData:class_131;
      
      internal var mOwnedDyes:Array;
      
      internal var var_1407:uint;
      
      internal var mOwnedMounts:Array;
      
      internal var mBuildingInfo:class_105;
      
      internal var mEggPetInfo:class_81;
      
      internal var mOwnedConsumables:Array;
      
      internal var mConsumablesList:Vector.<class_103>;
      
      internal var var_2619:Boolean;
      
      internal var mMagicForgeStatus:class_111;
      
      internal var mCraftTalentData:class_86;
      
      internal var mMasterClassTower:class_66;
      
      internal var mNewsData:class_116;
      
      internal var var_163:Dictionary;
      
      internal var var_1601:Boolean;
      
      internal var var_2047:Boolean = false;
      
      internal var var_1922:Boolean;
      
      internal var bWaitingForChangeMasterClassResponse:Boolean;
      
      internal var mAbilityBook:class_45;
      
      internal var var_2724:uint = 0;
      
      internal var var_1868:Boolean = true;
      
      internal var var_2878:uint = 0;
      
      internal var var_2193:Number = 0;
      
      internal var var_532:Vector.<class_72>;
      
      internal var var_326:Vector.<Loot>;
      
      internal var entities:Vector.<Entity>;
      
      internal var var_371:Vector.<class_130>;
      
      internal var var_1810:Dictionary;
      
      internal var clientEntID:uint;
      
      internal var var_1725:uint;
      
      internal var clientUserID:uint;
      
      internal var clientFacebookID:String;
      
      internal var clientKongID:String;
      
      internal var clientEntName:String;
      
      internal var var_1274:String;
      
      internal var var_1703:Boolean = true;
      
      internal var var_2052:Boolean = false;
      
      internal var var_1445:Vector.<ChatBubble>;
      
      internal var clientEnt:Entity;
      
      internal var lastSentMapX:uint;
      
      internal var lastSentMapY:uint;
      
      internal var mbTransferMode:Boolean;
      
      internal var var_934:Boolean;
      
      internal var var_2853:String;
      
      internal var var_1306:Array;
      
      internal var mMammothIdols:uint;
      
      internal var mbShowHigher:Boolean;
      
      internal var var_2132:uint;
      
      internal var var_193:Bitmap;
      
      internal var var_2417:MovieClip;
      
      internal var var_2137:Boolean;
      
      internal var var_1419:Boolean;
      
      internal var var_2256:Boolean;
      
      internal var var_164:SharedObject = null;
      
      internal var var_304:SharedObject = null;
      
      internal var var_1125:String;
      
      internal var var_2020:Boolean = false;
      
      internal var var_2056:Boolean = false;
      
      internal var var_2138:Boolean = false;
      
      internal var var_1447:String;
      
      internal var var_1257:String;
      
      internal var var_2098:Boolean = false;
      
      internal var var_1198:Boolean = false;
      
      internal var var_612:Boolean = false;
      
      internal var var_2129:Dictionary;
      
      internal var var_1909:String;
      
      internal var var_355:Vector.<Object> = null;
      
      internal var loginMaxChars:uint = 8;
      
      internal var var_2681:int;
      
      internal var var_2852:int;
      
      internal var var_2450:int;
      
      internal var var_2655:int;
      
      internal var var_2723:int;
      
      internal var var_2636:uint;
      
      internal var var_2465:int;
      
      internal var var_2735:int;
      
      internal var var_2476:int;
      
      internal var var_2817:int;
      
      internal var var_2797:int;
      
      internal var var_1706:Boolean;
      
      internal var var_2060:Boolean;
      
      internal var var_2743:String;
      
      internal var var_2799:uint;
      
      internal var var_2584:uint;
      
      internal var var_2784:String;
      
      internal var var_2839:String;
      
      internal var var_2773:String;
      
      internal var var_2567:Boolean;
      
      internal var var_2092:Boolean;
      
      internal var var_2461:uint;
      
      internal var mbPageIsLiked:Boolean;
      
      internal var var_2080:Boolean;
      
      internal var var_2022:Boolean;
      
      internal var targetDoor:uint = 0;
      
      internal var var_2115:Boolean = false;
      
      internal var var_1025:Point = null;
      
      internal var level:Level;
      
      internal var var_1280:Dictionary;
      
      internal var collMan:CollisionManager;
      
      internal var bProfaneFilter:Boolean = true;
      
      internal var bIgnoreStrangerInvites:Boolean = false;
      
      internal var bShowGroupFloaters:Boolean = false;
      
      internal var gameState:String;
      
      internal var var_2334:uint = 0;
      
      internal var var_2976:Boolean = true;
      
      internal var mBonusLevels:int = 0;
      
      internal var var_1778:Boolean = false;
      
      internal var mTimeThisTick:uint;
      
      internal var TIMESTEP:Number = 0;
      
      internal var var_2107:uint;
      
      internal var mServerGameTime:uint;
      
      internal var var_961:Vector.<SuperAnimInstance>;
      
      internal var var_2963:uint = 0;
      
      internal var serverConn:Connection;
      
      internal var linkUpdater:LinkUpdater;
      
      public var var_1495:Dictionary;
      
      public var var_1412:Boolean = false;
      
      internal var var_1602:Array;
      
      public var bAmGroupLeader:Boolean = false;
      
      public var bGroupIsLocked:Boolean = false;
      
      public var var_2958:Boolean = false;
      
      public var bSuppressGoldDisplay:Boolean = false;
      
      public var var_2558:Boolean;
      
      public var mKeybindManager:class_108;
      
      public var CONTEXT_NORMAL:int;
      
      public var CONTEXT_CHAT:int;
      
      internal var var_505:uint = 0;
      
      internal var var_2142:uint = 0;
      
      internal var g:int;
      
      internal var var_2986:int;
      
      internal var var_1918:Array;
      
      internal var var_1791:GlowFilter;
      
      public function Game(param1:Main)
      {
         this.var_144 = new Array();
         this.mOwnedGear = new Array();
         this.mOwnedGear2 = new Dictionary();
         this.mFilteredOwnedGear = new Array();
         this.mGearsetList = new Vector.<Vector.<uint>>();
         this.mGearsetListName = new Vector.<String>();
         this.mOwnedMaterials = new Array();
         this.mOwnedCharms = new Array();
         this.mOwnedMounts = new Array();
         this.var_1918 = new Array();
         this.var_1791 = new GlowFilter(11701805,1,1,1,10);
         super();
         this.main = param1;
         this.method_1435();
      }
      
      private static function method_28(param1:uint, param2:String, param3:String = null, param4:Point = null) : void
      {
         const_480[param1] = param2;
         if(param3)
         {
            const_727[param1] = param3;
            const_662[param1] = param4;
         }
      }
      
      public static function method_2096(param1:String) : void
      {
         timeStarted[param1] = getTimer();
      }
      
      public static function method_2064(param1:String) : void
      {
         timeSpent[param1] += getTimer() - timeStarted[param1];
      }
      
      public static function method_2139(param1:String, param2:Boolean) : Number
      {
         var _loc3_:Number = Number(timeSpent[param1]);
         if(param2 && bTracePerf)
         {
         }
         timeSpent[param1] = 0;
         return _loc3_;
      }
      
      public static function method_766(param1:String) : int
      {
         if(!param1)
         {
            return const_526;
         }
         param1 = param1.toLocaleLowerCase();
         if(param1 == "frostwarden")
         {
            return const_479;
         }
         if(param1 == "flameseer")
         {
            return const_491;
         }
         if(param1 == "necromancer")
         {
            return const_550;
         }
         if(param1 == "sentinel")
         {
            return const_442;
         }
         if(param1 == "justicar")
         {
            return const_415;
         }
         if(param1 == "templar")
         {
            return const_472;
         }
         if(param1 == "executioner")
         {
            return const_533;
         }
         if(param1 == "shadowwalker")
         {
            return const_545;
         }
         if(param1 == "soulthief")
         {
            return const_437;
         }
         return const_526;
      }
      
      public static function method_233(param1:int) : String
      {
         if(param1 < 0 || param1 >= const_21.length)
         {
            return "";
         }
         return const_21[param1];
      }
      
      public static function method_226(param1:String) : String
      {
         return const_85[param1.toLowerCase()];
      }
      
      public static function method_2112(param1:String, param2:String) : Boolean
      {
         var _loc3_:Boolean = false;
         if(param1 == "Mage")
         {
            if(param2.toLowerCase() == "frostwarden")
            {
               _loc3_ = true;
            }
            if(param2.toLowerCase() == "flameseer")
            {
               _loc3_ = true;
            }
            if(param2.toLowerCase() == "necromancer")
            {
               _loc3_ = true;
            }
         }
         if(param1 == "Rogue")
         {
            if(param2.toLowerCase() == "executioner")
            {
               _loc3_ = true;
            }
            if(param2.toLowerCase() == "shadowwalker")
            {
               _loc3_ = true;
            }
            if(param2.toLowerCase() == "soulthief")
            {
               _loc3_ = true;
            }
         }
         if(param1 == "Paladin")
         {
            if(param2.toLowerCase() == "sentinel")
            {
               _loc3_ = true;
            }
            if(param2.toLowerCase() == "justicar")
            {
               _loc3_ = true;
            }
            if(param2.toLowerCase() == "templar")
            {
               _loc3_ = true;
            }
         }
         return _loc3_;
      }
      
      public static function method_445(param1:uint, param2:String) : GearType
      {
         return class_14.var_421[param1 + param2];
      }
      
      public static function method_110(param1:uint, param2:uint) : String
      {
         var _loc3_:String = "M";
         if(param2 == 1)
         {
            _loc3_ = "R";
         }
         if(param2 == 2)
         {
            _loc3_ = "L";
         }
         return String(param1) + _loc3_;
      }
      
      public static function method_257(param1:int) : uint
      {
         if(param1 <= const_181)
         {
            return 0;
         }
         return Math.ceil(param1 / const_703);
      }
      
      public static function method_229(param1:int) : String
      {
         if(param1 <= const_181)
         {
            return "Free";
         }
         return String(Math.ceil(param1 / const_703));
      }
      
      public static function method_70(param1:uint, param2:Boolean = false) : String
      {
         var _loc3_:int = param1 / 3600 / 24;
         param1 -= _loc3_ * 3600 * 24;
         var _loc4_:int = int(param1 / 3600);
         param1 -= _loc4_ * 3600;
         var _loc5_:int = param1 / 60;
         param1 -= _loc5_ * 60;
         var _loc6_:Boolean = false;
         var _loc7_:* = _loc3_ + "d ";
         var _loc8_:* = _loc4_ + "h ";
         var _loc9_:* = _loc5_ + "m ";
         var _loc11_:* = param1 + "s";
         if(_loc3_ == 0)
         {
            _loc7_ = "";
         }
         else
         {
            _loc6_ = true;
         }
         if(_loc4_ == 0)
         {
            _loc8_ = "";
         }
         else
         {
            _loc6_ = true;
         }
         if(_loc5_ == 0)
         {
            _loc9_ = "";
         }
         else
         {
            _loc6_ = true;
         }
         if(param1 == 0 && (param2 && _loc6_))
         {
            _loc11_ = "";
         }
         return _loc7_ + _loc8_ + _loc9_ + _loc11_;
      }
      
      public function method_1435() : void
      {
         var _loc8_:String = null;
         var _loc9_:DisplayObject = null;
         var _loc10_:MagicObject = null;
         var _loc11_:Boolean = false;
         var _loc12_:Number = NaN;
         var _loc13_:Number = NaN;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         this.mTimeThisTick = getTimer();
         var _loc1_:Object = this.main.root.loaderInfo.parameters;
         if(Boolean(_loc1_) && (Boolean(_loc1_.fb) || Boolean(_loc1_.kg)))
         {
            this.clientKongID = _loc1_.kg;
            this.clientFacebookID = _loc1_.fb;
            this.var_2853 = _loc1_.ak;
            if(uint(_loc1_.ha))
            {
               _loc8_ = String(_loc1_.ci);
               this.var_1306 = !!_loc8_ ? _loc8_.split(":") : null;
               this.var_934 = true;
            }
         }
         if(!(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
         {
            this.method_1542();
         }
         this.var_961 = new Vector.<SuperAnimInstance>();
         if(!(DevSettings.flags & DevSettings.DEVFLAG_NO_GRAPHICS))
         {
            this.var_107 = new class_23(this);
         }
         this.var_171 = new class_82(this);
         this.var_77 = new class_123(this);
         this.method_1710();
         this.method_1040();
         this.method_1323();
         var_172 = new class_91(this);
         this.var_1602 = new Array();
         var _loc2_:int = 1;
         while(_loc2_ <= 32767)
         {
            this.var_1602.push(_loc2_);
            _loc2_++;
         }
         var _loc3_:MovieClip = class_4.method_16("a_EdgeHud");
         var _loc4_:MovieClip = new MovieClip();
         var _loc5_:int = 0;
         while(_loc5_ < _loc3_.numChildren)
         {
            _loc9_ = _loc3_.getChildAt(_loc5_);
            _loc10_ = this.var_171.method_412(_loc9_,true,true,true);
            _loc4_.addChild(_loc10_.var_51);
            this.var_171.method_193(_loc10_,true);
            _loc5_++;
         }
         this.edgeLayer.addChild(_loc4_);
         _loc4_.visible = false;
         _loc4_.name = "am_EdgeNarrow";
         var _loc6_:MovieClip;
         (_loc6_ = class_4.method_16("a_EdgeFull")).visible = true;
         _loc6_.name = "am_EdgeFull";
         this.edgeLayer.addChild(_loc6_);
         this.tooltip = new class_104(this);
         this.var_2560 = new Array();
         if(!(DevSettings.DEVFLAG_NO_GRAPHICS & DevSettings.flags))
         {
            this.var_137 = new CustomMouse(this);
         }
         this.dayNightManager = new DayNightManager(this);
         this.var_406 = new Vector.<int>();
         this.groupmates = new Vector.<class_133>();
         this.friendList = new Vector.<Friend>();
         this.var_124 = new Vector.<Friend>();
         this.var_340 = new Vector.<Friend>();
         this.var_1004 = new Vector.<Friend>();
         this.var_163 = new Dictionary();
         this.mKeybindManager = new class_108(const_79);
         this.mAbilityBook = new class_45(this);
         this.mMagicForgeStatus = new class_111(this);
         this.mBuildingInfo = new class_105(this);
         this.mEggPetInfo = new class_81(this);
         this.mCraftTalentData = new class_86(this);
         this.mLockboxData = new class_131(this);
         this.mOwnedDyes = new Array();
         this.mMasterClassTower = new class_66(this);
         this.mNewsData = new class_116(this);
         this.mOwnedConsumables = new Array();
         this.mConsumablesList = new Vector.<class_103>();
         this.method_1880();
         this.mMissionInfoList = new Array();
         this.level = new Level(this);
         this.var_1280 = new Dictionary();
         this.collMan = new CollisionManager(this);
         if(!(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
         {
            this.var_304 = SharedObject.getLocal("dbSavedGameData","/");
            _loc11_ = Boolean(this.var_304.data.dbSoundManagerMuted);
            _loc12_ = Number(this.var_304.data.dbSoundVolumeInverted);
            _loc13_ = Number(this.var_304.data.dbMusicVolumeInverted);
            _loc14_ = !!_loc12_ ? 1 - _loc12_ : 1;
            _loc15_ = !!_loc13_ ? 1 - _loc13_ : 1;
            if(_loc14_ < 0 || _loc15_ < 0)
            {
               _loc11_ = true;
               _loc14_ = -_loc14_;
               _loc15_ = -_loc15_;
            }
            SoundManager.SetSoundVolume(_loc14_);
            SoundManager.method_218(Main.const_108,_loc14_);
            SoundManager.method_218(Main.const_77,_loc15_);
            SoundManager.method_401(_loc11_);
            this.bProfaneFilter = !this.var_304.data.dbProfaneFilterOff;
            this.bShowGroupFloaters = this.var_304.data.dbShowGroupFloaters;
         }
         if(ExternalInterface.available)
         {
            ExternalInterface.addCallback("SWFFinishPurchaseCallback",this.SWFFinishPurchaseCallback);
            if(this.clientFacebookID)
            {
               ExternalInterface.addCallback("GetScreenShotHTML",this.GetScreenShotHTML);
               ExternalInterface.addCallback("SWFGetLikeStatusCallback",this.SWFGetLikeStatusCallback);
               ExternalInterface.addCallback("SWFFinishEarnCallback",this.SWFFinishEarnCallback);
               ExternalInterface.addCallback("SWFInviteFriendCallback",this.SWFInviteFriendCallback);
               this.var_2092 = true;
            }
         }
         var _loc7_:Number = Number(this.main.overallScale);
         this.var_89.scaleX = _loc7_;
         this.var_89.scaleY = _loc7_;
         this.edgeLayer.scaleX = _loc7_;
         this.edgeLayer.scaleY = _loc7_;
         this.var_245.scaleX = _loc7_;
         this.var_245.scaleY = _loc7_;
         if(!(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
         {
            if(DevSettings.flags & DevSettings.DEVFLAG_SHOWCHARACTERCREATE)
            {
               this.var_273.Display();
            }
            else if(DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT)
            {
               this.method_282(0,DevSettings.standAloneMapName,DevSettings.standAloneMapLevel,!!DevSettings.var_1351 ? DevSettings.var_1351 : DevSettings.standAloneMapLevel,DevSettings.standAloneMapInternalName,DevSettings.standAloneMomentParams,DevSettings.standAloneAlterParams,DevSettings.standAloneIsInstanced);
            }
            else
            {
               this.method_2000();
            }
         }
      }
      
      public function method_571() : void
      {
         var _loc1_:class_133 = null;
         var _loc2_:Mission = null;
         var _loc3_:SuperAnimInstance = null;
         var _loc4_:uint = 0;
         var _loc5_:class_76 = null;
         var _loc6_:class_114 = null;
         var _loc7_:class_103 = null;
         var _loc8_:DisplayObject = null;
         var _loc9_:DisplayObject = null;
         if(this.serverConn)
         {
            this.serverConn.method_205();
            this.serverConn = null;
         }
         if(this.linkUpdater)
         {
            this.linkUpdater.method_756();
            this.linkUpdater = null;
         }
         if(this.gameState == STATE_PLAY)
         {
            this.method_447();
         }
         this.var_77.method_1963();
         this.var_77 = null;
         this.collMan.method_784();
         this.collMan = null;
         this.level.method_905();
         this.level = null;
         this.collMan = null;
         this.var_171.method_954();
         this.var_1025 = null;
         for each(_loc1_ in this.groupmates)
         {
            _loc1_.method_811();
         }
         this.groupmates = null;
         if(Boolean(this.var_256) && Boolean(this.var_256.parent))
         {
            this.var_256.parent.removeChild(this.var_256);
         }
         this.var_256 = null;
         for each(_loc2_ in this.mMissionInfoList)
         {
            if(_loc2_)
            {
               _loc2_.method_736();
            }
         }
         this.mMissionInfoList = null;
         this.var_2905 = null;
         this.friendList = null;
         this.var_124 = null;
         this.var_340 = null;
         this.var_1004 = null;
         this.var_406 = null;
         this.var_163 = null;
         this.mAbilityBook.method_1185();
         this.mAbilityBook = null;
         if(this.edgeLayer)
         {
            if(_loc8_ = this.edgeLayer.getChildByName("am_EdgeFull") as DisplayObject)
            {
               _loc8_.visible = true;
            }
            if(_loc9_ = this.edgeLayer.getChildByName("am_EdgeNarrow") as DisplayObject)
            {
               _loc9_.visible = false;
            }
         }
         this.dayNightManager.method_1179();
         this.dayNightManager = null;
         if(this.var_137)
         {
            this.var_137.method_1856();
         }
         this.var_137 = null;
         if(this.tooltip)
         {
            this.tooltip.method_1744();
         }
         this.tooltip = null;
         this.method_1755();
         this.method_1471();
         this.method_1140();
         if(this.var_107)
         {
            this.var_107.method_643(true);
         }
         this.var_107 = null;
         this.var_2560 = null;
         for each(_loc3_ in this.var_961)
         {
            _loc3_.DestroySuperAnimInstance();
         }
         this.var_961 = null;
         this.var_1306 = null;
         this.var_164 = null;
         this.var_304 = null;
         this.var_171.method_1558();
         this.var_171 = null;
         this.var_1602 = null;
         this.main = null;
         this.mOwnedGear = null;
         this.mOwnedGear2 = null;
         this.var_144 = null;
         this.mOwnedMounts = null;
         this.mFilteredOwnedGear = null;
         _loc4_ = 0;
         while(_loc4_ < this.mGearsetList.length)
         {
            this.mGearsetList[_loc4_] = null;
            _loc4_++;
         }
         this.mGearsetList[_loc4_] = null;
         this.mGearsetListName = null;
         this.mBuildingInfo.method_1455();
         this.mBuildingInfo = null;
         this.mEggPetInfo.method_1900();
         this.mEggPetInfo = null;
         for each(_loc5_ in this.mOwnedMaterials)
         {
            _loc5_.method_626();
         }
         this.mOwnedMaterials = null;
         for each(_loc6_ in this.mOwnedCharms)
         {
            _loc6_.method_833();
         }
         this.mOwnedCharms = null;
         this.mMagicForgeStatus = null;
         this.mCraftTalentData = null;
         this.mMasterClassTower.method_1399();
         this.mMasterClassTower = null;
         this.mLockboxData = null;
         this.mOwnedDyes = null;
         for each(_loc7_ in this.mOwnedConsumables)
         {
            _loc7_.method_786();
         }
         this.mOwnedConsumables = null;
         this.mConsumablesList = null;
      }
      
      public function method_1323() : void
      {
         this.var_273 = new class_51(this);
         this.var_141 = new ScreenCharacterCreation(this);
         this.var_398 = new ScreenNewAccount(this);
         this.var_479 = new ScreenLogin(this);
         this.var_94 = new class_94(this);
         this.var_341 = new ScreenCharacterSelection(this);
         this.var_933 = new ScreenTransfer(this);
         this.var_641 = new class_60(this);
         this.var_1717 = new class_61(this);
         this.var_737 = new class_71(this);
         this.var_655 = new class_97(this);
         this.screenFriend = new class_56(this);
         this.mUIManager = new class_4(this);
         this.var_742 = this.mUIManager.method_22(class_67) as class_67;
         this.var_936 = this.mUIManager.method_22(class_95) as class_95;
         this.screenLinkBar = this.mUIManager.method_22(class_48) as class_48;
         this.var_2344 = this.mUIManager.method_22(class_59) as class_59;
         this.var_2523 = this.mUIManager.method_22(class_126) as class_126;
         this.var_2781 = this.mUIManager.method_22(class_47) as class_47;
         this.var_2059 = this.mUIManager.method_22(class_74) as class_74;
         this.var_2159 = this.mUIManager.method_22(class_65) as class_65;
         this.var_2093 = this.mUIManager.method_22(class_98) as class_98;
         this.var_2231 = this.mUIManager.method_22(class_49) as class_49;
         this.var_2359 = this.mUIManager.method_22(class_57) as class_57;
         this.var_2694 = this.mUIManager.method_22(class_128) as class_128;
         this.var_2582 = this.mUIManager.method_22(class_106) as class_106;
         this.var_2561 = this.mUIManager.method_22(class_54) as class_54;
         this.var_2448 = this.mUIManager.method_22(class_55) as class_55;
         this.var_2761 = this.mUIManager.method_22(class_84) as class_84;
         this.screenNotification = this.mUIManager.method_22(class_46) as class_46;
         this.screenHudTooltip = this.mUIManager.method_22(class_101) as class_101;
         this.screenChat = this.mUIManager.method_22(class_127) as class_127;
         this.screenInteractiveTutorial = new class_89(this);
         this.screenBuyIdols = this.mUIManager.method_22(class_63) as class_63;
         this.screenGoldShort = this.mUIManager.method_22(class_93) as class_93;
         this.screenRoyalSigilStorePrompt = this.mUIManager.method_22(class_115) as class_115;
         this.screenRoyalSigilStore = this.mUIManager.method_22(class_107) as class_107;
         this.screenUpgrading = this.mUIManager.method_22(class_96) as class_96;
         this.screenKeybind = this.mUIManager.method_22(class_92) as class_92;
         this.screenMenu = this.mUIManager.method_22(class_124) as class_124;
         this.screenRespecConfirm = this.mUIManager.method_22(class_125) as class_125;
         this.screenLockBoxBuyKeys = this.mUIManager.method_22(class_90) as class_90;
         this.screenLockBoxBuyTroves = this.mUIManager.method_22(class_85) as class_85;
         this.screenLockBox = this.mUIManager.method_22(class_73) as class_73;
         this.screenSocket = this.mUIManager.method_22(class_78) as class_78;
         this.screenReplace = this.mUIManager.method_22(class_109) as class_109;
         this.screenFeedPet = this.mUIManager.method_22(class_110) as class_110;
         this.screenArmory = this.mUIManager.method_22(ScreenArmory) as ScreenArmory;
         this.screenLook = this.mUIManager.method_22(class_102) as class_102;
         this.screenMasterClassSelection = this.mUIManager.method_22(class_52) as class_52;
         this.var_996 = this.mUIManager.method_22(class_117) as class_117;
         this.screenCatalysts = this.mUIManager.method_22(class_120) as class_120;
         this.screenForge = this.mUIManager.method_22(class_75) as class_75;
         this.screenDyeGear = this.mUIManager.method_22(class_121) as class_121;
         this.screenClassTowers = this.mUIManager.method_22(class_69) as class_69;
         this.screenTome = this.mUIManager.method_22(class_50) as class_50;
         this.var_758 = this.mUIManager.method_22(class_88) as class_88;
         this.screenBarn = this.mUIManager.method_22(class_99) as class_99;
         this.var_2224 = this.mUIManager.method_22(class_80) as class_80;
         this.screenHudTop = this.mUIManager.method_22(class_79) as class_79;
         this.screenHudTopRight = this.mUIManager.method_22(class_70) as class_70;
         this.screenQuestTracker = this.mUIManager.method_22(class_112) as class_112;
         this.screenHud = this.mUIManager.method_22(class_58) as class_58;
         this.var_1828 = this.mUIManager.method_22(class_132) as class_132;
         this.var_2306 = this.mUIManager.method_22(class_100) as class_100;
         this.screenWalkthrough = this.mUIManager.method_22(class_62) as class_62;
         this.var_1808 = this.mUIManager.method_22(ScreenLevelComplete) as ScreenLevelComplete;
         this.var_890 = this.mUIManager.method_22(class_68) as class_68;
         this.screenMap = this.mUIManager.method_22(class_119) as class_119;
         this.screenSigil = this.mUIManager.method_22(class_83) as class_83;
         this.screenSpellbook = this.mUIManager.method_22(class_129) as class_129;
         this.mUIManager.method_1338();
      }
      
      public function method_1755() : void
      {
         this.var_273.method_1821();
         this.var_273 = null;
         this.var_141.method_1532();
         this.var_141 = null;
         this.var_398.method_1921();
         this.var_398 = null;
         this.var_479.method_1769();
         this.var_479 = null;
         this.var_94.method_1258();
         this.var_94 = null;
         this.var_341.method_1064();
         this.var_341 = null;
         this.var_933.method_1197();
         this.var_933 = null;
         this.var_641.method_1351();
         this.var_641 = null;
         this.var_1717.method_1371();
         this.var_1717 = null;
         this.var_737.method_1599();
         this.var_737 = null;
         this.var_655.method_1936();
         this.var_655 = null;
         this.screenInteractiveTutorial.method_448();
         this.screenInteractiveTutorial = null;
         this.screenFriend.method_1803();
         this.screenFriend = null;
         this.screenRoyalSigilStorePrompt = null;
         this.screenRoyalSigilStore = null;
         this.screenLockBox = null;
         this.screenLockBoxBuyKeys = null;
         this.screenLockBoxBuyTroves = null;
         this.screenMasterClassSelection = null;
         this.screenFeedPet = null;
         this.screenArmory = null;
         this.var_890 = null;
         this.screenLinkBar = null;
         this.var_1808 = null;
         this.var_936 = null;
         this.screenLook = null;
         this.screenMap = null;
         this.screenMenu = null;
         this.screenCatalysts = null;
         this.screenForge = null;
         this.var_996 = null;
         this.screenSocket = null;
         this.screenReplace = null;
         this.var_2781 = null;
         this.var_2159 = null;
         this.var_2059 = null;
         this.var_2093 = null;
         this.var_2231 = null;
         this.var_2359 = null;
         this.var_2694 = null;
         this.var_2582 = null;
         this.var_2561 = null;
         this.var_2448 = null;
         this.var_2761 = null;
         this.screenNotification = null;
         this.var_2306 = null;
         this.screenHud = null;
         this.screenHudTop = null;
         this.screenHudTopRight = null;
         this.screenQuestTracker = null;
         this.screenWalkthrough = null;
         this.screenBuyIdols = null;
         this.var_742 = null;
         this.var_2344 = null;
         this.var_2224 = null;
         this.screenDyeGear = null;
         this.screenSigil = null;
         this.screenKeybind = null;
         this.screenSpellbook = null;
         this.screenChat = null;
         this.screenClassTowers = null;
         this.screenTome = null;
         this.var_758 = null;
         this.screenUpgrading = null;
         this.var_2523 = null;
         this.screenBarn = null;
         this.screenGoldShort = null;
         this.var_1828 = null;
         this.mUIManager.method_1085();
         this.mUIManager = null;
      }
      
      public function method_1938() : void
      {
         var _loc1_:uint = uint(getTimer());
         var _loc2_:uint = uint(_loc1_ - this.mTimeThisTick);
         this.mTimeThisTick = _loc1_;
         this.TIMESTEP = _loc2_ * 0.001 * Game.TARGETFPS;
         var _loc3_:uint = uint(this.mTimeThisTick / 1000);
         this.mServerGameTime += _loc3_ - this.var_2107;
         this.var_2107 = _loc3_;
      }
      
      public function method_1633(param1:uint) : void
      {
         this.var_2107 = uint(this.mTimeThisTick / 1000);
         this.mServerGameTime = param1;
      }
      
      public function CanSendPacket() : Boolean
      {
         return Boolean(this.serverConn) && !this.mbTransferMode;
      }
      
      public function method_1542() : void
      {
         var _loc1_:Date = new Date();
         var _loc2_:String = !!this.clientFacebookID ? "FB:" + this.clientFacebookID : (!!this.clientKongID ? "KG:" + this.clientKongID : "DB:" + _loc1_.time + "x" + uint(Math.random() * 1000000));
         class_53.method_125(const_971,const_869,GAME_VERSION,_loc2_);
         class_53.method_79("LoginStart",1);
      }
      
      public function method_1650() : void
      {
         class_53.method_125(const_914,const_858,GAME_VERSION,String(this.clientUserID));
         class_53.method_79("GameStart",1);
      }
      
      public function method_234(param1:DisplayObject) : Point
      {
         var _loc2_:Point = param1.localToGlobal(new Point(0,0));
         if(param1.stage)
         {
            _loc2_ = this.levelLayer.localToGlobal(_loc2_);
         }
         return _loc2_;
      }
      
      public function method_47() : Boolean
      {
         return Boolean(this.var_94.var_88) && this.var_94.var_88.visible;
      }
      
      public function PointOnScreenWithinDist(param1:Number, param2:Number, param3:Number, param4:Number) : Boolean
      {
         return param1 >= -this.levelLayer.x - param3 && param1 <= -this.levelLayer.x + Camera.SCREEN_WIDTH + param3 && param2 >= -this.levelLayer.y - param4 && param2 <= -this.levelLayer.y + Camera.SCREEN_HEIGHT + param4;
      }
      
      public function method_82(param1:String, param2:Number, param3:Number, param4:Number = 1) : void
      {
         if(!this.PointOnScreenWithinDist(param2,param3,Camera.SCREEN_WIDTH * 0.1,Camera.SCREEN_HEIGHT * 0.1))
         {
            return;
         }
         SoundManager.Play(param1,param4);
      }
      
      public function method_2047(param1:Point) : Point
      {
         var _loc2_:Point = new Point();
         _loc2_.x = Camera.SCREEN_WIDTH * 0.5 - this.levelLayer.x;
         _loc2_.y = Camera.SCREEN_HEIGHT * 0.5 - this.levelLayer.y;
         return param1.subtract(_loc2_);
      }
      
      private function method_440(param1:String, param2:Number) : void
      {
         var _loc3_:uint = sGlobalTimeOrder.length;
         if(Boolean(_loc3_) && param2 <= sGlobalTimeMap[sGlobalTimeOrder[_loc3_ - 1]])
         {
            class_24.method_7("Global time must always be greater than the previous.");
         }
         sGlobalTimeOrder.push(param1);
         sGlobalTimeMap[param1] = param2;
      }
      
      public function method_263(param1:uint = 0) : void
      {
         var _loc3_:String = null;
         var _loc4_:class_13 = null;
         if(!sGlobalTimeMap)
         {
            sGlobalTimeMap = new Dictionary();
            sGlobalTimeOrder = new Vector.<String>();
            this.method_440("RescueAnna",1);
            this.method_440("SlayTheDragon",2);
            this.method_440("SlaySvath",10);
            sGlobalTimeOrder.fixed = true;
         }
         var _loc2_:class_13 = class_14.var_238[param1];
         if(Boolean(param1) && !_loc2_)
         {
            return;
         }
         if(!param1 || Boolean(sGlobalTimeMap[_loc2_.var_525]))
         {
            this.var_2193 = 0;
            for each(_loc3_ in sGlobalTimeOrder)
            {
               _loc4_ = class_14.var_42[_loc3_];
               if(!this.method_36(_loc4_.missionID))
               {
                  break;
               }
               this.var_2193 = sGlobalTimeMap[_loc3_];
            }
         }
         this.method_1464(!!_loc2_ ? _loc2_.var_525 : null);
         this.method_1082();
      }
      
      private function method_25(param1:String, param2:Boolean, param3:Boolean) : void
      {
         var _loc4_:Entity = null;
         this.var_1810[param1] = !param2;
         if(!param3)
         {
            return;
         }
         for each(_loc4_ in this.entities)
         {
            if(Boolean(_loc4_.cue) && _loc4_.cue.characterName == param1)
            {
               _loc4_.var_2235 = !param2;
               break;
            }
         }
      }
      
      private function method_936(param1:String, param2:Boolean, param3:Boolean) : void
      {
         var _loc4_:Room = null;
         var _loc5_:Boolean = false;
         var _loc6_:Array = null;
         var _loc7_:DisplayObject = null;
         for each(_loc4_ in this.level.var_299)
         {
            _loc5_ = false;
            if(_loc6_ = _loc4_.method_1251(param1))
            {
               for each(_loc7_ in _loc6_)
               {
                  if(_loc7_.visible != param2)
                  {
                     _loc7_.visible = param2;
                     _loc5_ = true;
                  }
               }
               if(this.var_107 && _loc5_ && param3)
               {
                  this.var_107.method_120();
               }
            }
         }
      }
      
      public function method_1464(param1:String) : void
      {
         var _loc2_:Door = null;
         var _loc3_:Boolean = false;
         var _loc4_:* = false;
         var _loc5_:class_13 = null;
         if(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT)
         {
            return;
         }
         var _loc6_:String;
         if((_loc6_ = String(this.level.internalName)) == "NewbieRoad")
         {
            if(!param1 || param1 == "MeetTheTown")
            {
               _loc5_ = class_14.var_42["MeetTheTown"];
               _loc3_ = this.MissionIsComplete(_loc5_.missionID);
               _loc4_ = !this.method_36(class_13.const_544);
               _loc2_ = this.level.GetDoorFromID(class_11.const_641);
               if(_loc2_)
               {
                  _loc2_.bDisabled = !_loc3_ && !_loc4_;
               }
            }
            if(!param1 || param1 == "RescueAnna")
            {
               _loc5_ = class_14.var_42["RescueAnna"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("AnnaOutside",_loc3_,true);
            }
            if(!param1 || param1 == "GoblinRiver")
            {
               _loc5_ = class_14.var_42["GoblinRiver"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("NR_QuestAnna01",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("AnnaOutside",false,true);
               }
            }
            if(!param1 || param1 == "KillNephit")
            {
               _loc5_ = class_14.var_42["KillNephit"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("NR_QuestAnna02",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("NR_QuestAnna01",false,true);
               }
            }
            if(!param1 || param1 == "SlayTheDragon")
            {
               _loc5_ = class_14.var_42["SlayTheDragon"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("NR_QuestAnna03",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("NR_QuestAnna02",false,true);
               }
            }
            if(!param1 || param1 == "DeliverToSwamp")
            {
               _loc5_ = class_14.var_42["DeliverToSwamp"];
               _loc3_ = this.MissionIsComplete(_loc5_.missionID);
               if(_loc3_)
               {
                  this.method_25("AnnaOutside",true,true);
                  this.method_25("NR_QuestAnna03",false,true);
               }
            }
         }
         if(_loc6_ == "NewbieRoadHard")
         {
            if(!param1 || param1 == "RescueAnnaHard")
            {
               _loc5_ = class_14.var_42["RescueAnnaHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("AnnaOutsideHard",_loc3_,true);
            }
            if(!param1 || param1 == "GoblinRiverHard")
            {
               _loc5_ = class_14.var_42["GoblinRiverHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("NR_QuestAnna01Hard",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("AnnaOutsideHard",false,true);
               }
            }
            if(!param1 || param1 == "KillNephitHard")
            {
               _loc5_ = class_14.var_42["KillNephitHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("NR_QuestAnna02Hard",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("NR_QuestAnna01Hard",false,true);
               }
            }
            if(!param1 || param1 == "SlayTheDragonHard")
            {
               _loc5_ = class_14.var_42["SlayTheDragonHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("NR_QuestAnna03Hard",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("NR_QuestAnna02Hard",false,true);
               }
               _loc3_ = this.MissionIsComplete(_loc5_.missionID);
               if(_loc3_)
               {
                  this.method_25("AnnaOutsideHard",true,true);
                  this.method_25("NR_QuestAnna03Hard",false,false);
               }
            }
         }
         else if(_loc6_ == "BridgeTown")
         {
            if(!param1 || param1 == "DefeatBanditCamp")
            {
               _loc5_ = class_14.var_42["DefeatBanditCamp"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_936("am_OldHeroPath",!_loc3_,true);
            }
            if(!param1 || param1 == "OutpostReport")
            {
               _loc5_ = class_14.var_42["OutpostReport"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("BT_Mayor01",!_loc3_,true);
            }
            if(!param1 || param1 == "MouthOfMeylour")
            {
               _loc5_ = class_14.var_42["MouthOfMeylour"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("BT_SubWarden",!_loc3_,true);
            }
            if(!param1 || param1 == "DerelictionOfDuty")
            {
               _loc5_ = class_14.var_42["DerelictionOfDuty"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("MeylourMageNPC",!_loc3_,true);
               this.method_25("MeylourMageNPC2",!_loc3_,true);
            }
         }
         else if(_loc6_ == "BridgeTownHard")
         {
            if(!param1 || param1 == "DefeatBanditCampHard")
            {
               _loc5_ = class_14.var_42["DefeatBanditCampHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_936("am_OldHeroPath",!_loc3_,true);
            }
            if(!param1 || param1 == "OutpostReportHard")
            {
               _loc5_ = class_14.var_42["OutpostReportHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("BT_Mayor01Hard",!_loc3_,true);
            }
            if(!param1 || param1 == "MouthOfMeylourHard")
            {
               _loc5_ = class_14.var_42["MouthOfMeylourHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("BT_SubWardenHard",!_loc3_,true);
            }
            if(!param1 || param1 == "DerelictionOfDutyHard")
            {
               _loc5_ = class_14.var_42["DerelictionOfDutyHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("MeylourMageNPCHard",!_loc3_,true);
               this.method_25("MeylourMageNPC2Hard",!_loc3_,true);
            }
         }
         else if(_loc6_ == "CemeteryHill")
         {
            if(!param1 || param1 == "RescueYagaga")
            {
               _loc5_ = class_14.var_42["RescueYagaga"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("CH_Mayor02",_loc3_,true);
            }
         }
         else if(_loc6_ == "CemeteryHillHard")
         {
            if(!param1 || param1 == "RescueYagagaHard")
            {
               _loc5_ = class_14.var_42["RescueYagagaHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("CH_Mayor02Hard",_loc3_,true);
            }
         }
         else if(_loc6_ == "Castle")
         {
            if(!param1 || param1 == "BattlesLostAndWon")
            {
               _loc5_ = class_14.var_42["BattlesLostAndWon"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("AC_Titus01",_loc3_,true);
            }
            if(!param1 || param1 == "LastStand")
            {
               _loc5_ = class_14.var_42["LastStand"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("AC_Titus02",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("AC_Titus01",false,true);
               }
            }
            if(!param1 || param1 == "Capstone")
            {
               _loc5_ = class_14.var_42["Capstone"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("AC_Titus03",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("AC_Titus01",false,true);
                  this.method_25("AC_Titus02",false,true);
               }
            }
            if(!param1 || param1 == "IntoTheDepths")
            {
               _loc5_ = class_14.var_42["IntoTheDepths"];
               _loc3_ = this.MissionIsComplete(_loc5_.missionID);
               if(_loc3_)
               {
                  this.method_25("AC_Titus03",false,true);
               }
            }
         }
         else if(_loc6_ == "CastleHard")
         {
            if(!param1 || param1 == "BattlesLostAndWonHard")
            {
               _loc5_ = class_14.var_42["BattlesLostAndWonHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("AC_Titus01Hard",_loc3_,true);
            }
            if(!param1 || param1 == "LastStandHard")
            {
               _loc5_ = class_14.var_42["LastStandHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("AC_Titus02Hard",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("AC_Titus01Hard",false,true);
               }
            }
            if(!param1 || param1 == "CapstoneHard")
            {
               _loc5_ = class_14.var_42["CapstoneHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("AC_Titus03Hard",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("AC_Titus01Hard",false,true);
                  this.method_25("AC_Titus02Hard",false,true);
               }
            }
            if(!param1 || param1 == "IntoTheDepthsHard")
            {
               _loc5_ = class_14.var_42["IntoTheDepthsHard"];
               _loc3_ = this.MissionIsComplete(_loc5_.missionID);
               if(_loc3_)
               {
                  this.method_25("AC_Titus03Hard",false,true);
               }
            }
         }
         else if(_loc6_ == "ShazariDesert")
         {
            if(!param1 || param1 == "TravelToTownOne")
            {
               _loc5_ = class_14.var_42["TravelToTownOne"];
               _loc3_ = this.MissionIsComplete(_loc5_.missionID);
               this.method_25("SD_Titus01",!_loc3_,true);
            }
            if(!param1 || param1 == "AncientBurialGrounds")
            {
               _loc5_ = class_14.var_42["AncientBurialGrounds"];
               _loc3_ = this.MissionIsComplete(_loc5_.missionID);
               this.method_25("SD_Titus02",_loc3_,true);
            }
         }
         else if(_loc6_ == "ShazariDesertHard")
         {
            if(!param1 || param1 == "TravelToTownOneHard")
            {
               _loc5_ = class_14.var_42["TravelToTownOneHard"];
               _loc3_ = this.MissionIsComplete(_loc5_.missionID);
               this.method_25("SD_Titus01Hard",!_loc3_,true);
            }
            if(!param1 || param1 == "AncientBurialGroundsHard")
            {
               _loc5_ = class_14.var_42["AncientBurialGroundsHard"];
               _loc3_ = this.MissionIsComplete(_loc5_.missionID);
               this.method_25("SD_Titus02Hard",_loc3_,true);
            }
         }
         else if(_loc6_ == "JadeCity")
         {
            if(!param1 || param1 == "TheProdigalSon")
            {
               _loc5_ = class_14.var_42["TheProdigalSon"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("VH_FabMab01",_loc3_,true);
            }
            if(!param1 || param1 == "Intervention")
            {
               _loc5_ = class_14.var_42["Intervention"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("VH_FabMab02",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("VH_FabMab01",false,true);
               }
            }
            if(!param1 || param1 == "ShadowsOfThePast")
            {
               _loc5_ = class_14.var_42["ShadowsOfThePast"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("VH_Skitts01",!_loc3_,true);
            }
         }
         else if(_loc6_ == "JadeCityHard")
         {
            if(!param1 || param1 == "TheProdigalSonHard")
            {
               _loc5_ = class_14.var_42["TheProdigalSonHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("VH_FabMab01Hard",_loc3_,true);
            }
            if(!param1 || param1 == "InterventionHard")
            {
               _loc5_ = class_14.var_42["InterventionHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("VH_FabMab02Hard",_loc3_,true);
               if(_loc3_)
               {
                  this.method_25("VH_FabMab01Hard",false,true);
               }
            }
            if(!param1 || param1 == "ShadowsOfThePastHard")
            {
               _loc5_ = class_14.var_42["ShadowsOfThePastHard"];
               _loc3_ = this.method_36(_loc5_.missionID);
               this.method_25("VH_Skitts01Hard",!_loc3_,true);
            }
         }
      }
      
      public function SelectMissionToTrack(param1:class_13 = null) : void
      {
         var _loc2_:Mission = null;
         var _loc3_:class_13 = null;
         var _loc4_:String = null;
         var _loc5_:String = null;
         var _loc6_:Boolean = false;
         var _loc7_:class_13 = null;
         var _loc8_:Boolean = false;
         if(param1)
         {
            this.mTrackedMission = param1;
         }
         else
         {
            _loc4_ = String(this.level.internalName);
            _loc5_ = Level.method_182(_loc4_);
            _loc6_ = this.InHardMode();
            for each(_loc7_ in class_14.var_238)
            {
               if(!(_loc7_.var_431 != _loc5_ && !_loc7_.var_186))
               {
                  if(_loc7_.var_2814 == _loc6_)
                  {
                     _loc2_ = this.mMissionInfoList[_loc7_.missionID];
                     if(!(!_loc2_ && !this.HasCompletedPreReqs(_loc7_)))
                     {
                        if(!(Boolean(_loc2_) && _loc2_.var_145 == Mission.const_72))
                        {
                           if(Boolean(_loc7_.var_134) && _loc7_.var_134 == _loc4_)
                           {
                              _loc3_ = _loc7_;
                              break;
                           }
                           if(!(this.level.bInstanced && (!_loc2_ || _loc7_.var_186)))
                           {
                              if(!_loc3_)
                              {
                                 _loc3_ = _loc7_;
                              }
                              else
                              {
                                 _loc8_ = Boolean(_loc3_) && Boolean(this.mMissionInfoList[_loc3_.missionID]);
                                 if(_loc2_ && !_loc8_ && _loc7_.var_231 >= _loc3_.var_231)
                                 {
                                    _loc3_ = _loc7_;
                                 }
                                 else if(_loc7_.var_231 > _loc3_.var_231)
                                 {
                                    _loc3_ = _loc7_;
                                 }
                              }
                           }
                        }
                     }
                  }
               }
            }
            this.mTrackedMission = _loc3_;
         }
         this.screenQuestTracker.Refresh();
      }
      
      public function method_365(param1:Vector.<Friend>) : void
      {
         this.friendList = this.method_1531(param1);
         this.screenHudTop.method_1730(this.friendList);
         this.screenFriend.method_489(this.friendList,false);
      }
      
      public function method_1531(param1:Vector.<Friend>) : Vector.<Friend>
      {
         var _loc4_:Friend = null;
         var _loc2_:Vector.<Friend> = new Vector.<Friend>();
         var _loc3_:Vector.<Friend> = new Vector.<Friend>();
         for each(_loc4_ in param1)
         {
            if(_loc4_.var_276)
            {
               _loc3_.push(_loc4_);
            }
            else if(_loc4_.bOnline)
            {
               _loc2_.unshift(_loc4_);
            }
            else
            {
               _loc2_.push(_loc4_);
            }
         }
         return _loc3_.concat(_loc2_);
      }
      
      public function UpdateAlert(param1:uint) : void
      {
         if(!this.CanSendPacket())
         {
            return;
         }
         var _loc2_:Packet = new Packet(LinkUpdater.const_1272);
         _loc2_.method_20(const_646,param1);
         this.serverConn.SendPacket(_loc2_);
         this.mAlertState |= param1;
      }
      
      public function method_1794(param1:Array) : void
      {
         var _loc2_:Mission = null;
         for each(_loc2_ in this.mMissionInfoList)
         {
            if(_loc2_)
            {
               _loc2_.method_736();
            }
         }
         this.mMissionInfoList = param1;
         this.SetNewTutorialStage(0);
         this.method_530();
         this.method_263();
         this.method_195();
         this.SelectMissionToTrack();
         this.screenMap.Refresh();
         this.screenHudTop.Refresh();
         this.screenQuestTracker.Refresh();
      }
      
      public function method_531(param1:uint) : Boolean
      {
         var _loc2_:Mission = this.mMissionInfoList[param1];
         return _loc2_ != null;
      }
      
      public function method_999(param1:uint) : Boolean
      {
         var _loc2_:Mission = this.mMissionInfoList[param1];
         return Boolean(_loc2_) && _loc2_.var_145 == Mission.const_213;
      }
      
      public function method_36(param1:uint) : Boolean
      {
         var _loc2_:Mission = this.mMissionInfoList[param1];
         return Boolean(_loc2_) && _loc2_.var_145 != Mission.const_213;
      }
      
      public function method_701(param1:uint) : Boolean
      {
         var _loc2_:Mission = this.mMissionInfoList[param1];
         return Boolean(_loc2_) && _loc2_.var_145 == Mission.const_58;
      }
      
      public function MissionIsComplete(param1:uint) : Boolean
      {
         var _loc2_:Mission = this.mMissionInfoList[param1];
         return Boolean(_loc2_) && _loc2_.var_145 == Mission.const_72;
      }
      
      public function SetNewTutorialStage(param1:uint) : void
      {
         var _loc2_:String = null;
         var _loc3_:Point = null;
         if(this.mTutorialStage != param1)
         {
            this.var_655.method_187(const_480[this.mTutorialStage]);
            _loc2_ = String(const_727[param1]);
            if(!_loc2_ || _loc2_ == this.level.internalName)
            {
               _loc3_ = const_662[param1];
               this.var_655.method_290(const_480[param1],_loc3_);
            }
            this.mTutorialStage = param1;
            if(this.mTutorialStage == const_150)
            {
               this.var_2359.Display();
               SoundManager.Play("UI_UnlockMap");
            }
         }
         if(Boolean(this.clientEnt) && Boolean(this.clientEnt.currRoom))
         {
            this.method_799(this.clientEnt.currRoom);
         }
      }
      
      public function method_799(param1:Room) : void
      {
         if(param1.var_2025)
         {
            this.method_1561(param1);
         }
         else if(param1.var_2259)
         {
            this.method_1908(param1);
         }
         else if(param1.var_2046)
         {
            this.method_1678(param1);
         }
         else if(param1.var_2308)
         {
            this.method_1833(param1);
         }
         else if(param1.var_2024)
         {
            this.method_1048(param1);
         }
      }
      
      public function method_1561(param1:Room) : void
      {
         if(this.mTutorialStage > 0 && this.mTutorialStage <= const_393 && this.level.internalName == "NewbieRoad")
         {
            param1.SetDynamicCollision("am_DynamicCollision_BoatTutorial",true);
         }
         else
         {
            param1.SetDynamicCollision("am_DynamicCollision_BoatTutorial",false);
         }
         if(this.mTutorialStage >= const_306 && this.mTutorialStage <= const_313 && this.level.internalName == "NewbieRoad")
         {
            param1.SetDynamicCollision("am_DynamicCollision_BoatTutorialClickFink",true);
         }
         else
         {
            param1.SetDynamicCollision("am_DynamicCollision_BoatTutorialClickFink",false);
         }
      }
      
      public function method_1678(param1:Room) : void
      {
         if(this.method_531(class_13.const_426) && !this.MissionIsComplete(class_13.const_426) && this.level.internalName == "NewbieRoad")
         {
            param1.SetDynamicCollision("am_DynamicCollision_OutsideTutorial",true);
         }
         else
         {
            param1.SetDynamicCollision("am_DynamicCollision_OutsideTutorial",false);
         }
      }
      
      public function method_1833(param1:Room) : void
      {
         if(this.mTutorialStage == const_355 && this.level.internalName == "NewbieRoad")
         {
            param1.SetDynamicCollision("am_DynamicCollision_ForkInRoad",true);
         }
         else
         {
            param1.SetDynamicCollision("am_DynamicCollision_ForkInRoad",false);
         }
      }
      
      public function method_1908(param1:Room) : void
      {
         if(this.mTutorialStage >= const_212 && this.mTutorialStage <= const_358 && this.level.internalName == "NewbieRoad")
         {
            param1.SetDynamicCollision("am_DynamicCollision_RistasTutorialClickRistas",true);
         }
         else
         {
            param1.SetDynamicCollision("am_DynamicCollision_RistasTutorialClickRistas",false);
         }
         if(this.mTutorialStage >= const_212 && this.mTutorialStage <= const_150 && this.level.internalName == "NewbieRoad")
         {
            this.SetNewTutorialStage(const_266);
         }
      }
      
      public function method_1048(param1:Room) : void
      {
         if(this.mTutorialStage == const_349)
         {
            this.SetNewTutorialStage(TUTORIALSTAGE_ATTOME2);
         }
         else if(this.mTutorialStage == const_310)
         {
            this.SetNewTutorialStage(const_377);
         }
         else if(this.mTutorialStage == const_311)
         {
            this.SetNewTutorialStage(const_392);
         }
         else if(this.mTutorialStage == const_370)
         {
            this.SetNewTutorialStage(const_389);
         }
         else if(this.mTutorialStage == const_337)
         {
            this.SetNewTutorialStage(const_270);
         }
         else if(this.mTutorialStage == const_246)
         {
            this.SetNewTutorialStage(const_253);
         }
         else if(this.mTutorialStage == const_230)
         {
            this.SetNewTutorialStage(const_287);
         }
      }
      
      public function method_1082() : void
      {
         if(this.level.bInstanced && this.level.internalName != "CraftTown")
         {
            return;
         }
         var _loc1_:class_9 = null;
         var _loc2_:class_9 = null;
         var _loc3_:class_9 = null;
         var _loc4_:* = false;
         if(this.mBuildingInfo)
         {
            _loc1_ = this.mBuildingInfo.GetOwnedBuildingByName("Tome");
            _loc2_ = this.mBuildingInfo.GetOwnedBuildingByName("Barn");
            _loc3_ = this.mBuildingInfo.GetOwnedBuildingByName("Forge");
            _loc4_ = this.mBuildingInfo.mStatus == class_105.const_339;
         }
         if(this.mTutorialStage >= const_410)
         {
            this.SetNewTutorialStage(const_410);
         }
         else if(this.mTutorialStage >= const_287)
         {
            this.SetNewTutorialStage(const_287);
         }
         else if(this.mTutorialStage >= const_230 || this.MissionIsComplete(class_13.const_118) && !(this.mAlertState & const_443) && this.mLockboxData.mRoyalSigils)
         {
            this.SetNewTutorialStage(const_230);
         }
         else if(this.mTutorialStage >= const_302)
         {
            this.SetNewTutorialStage(const_302);
         }
         else if(this.mTutorialStage >= const_253)
         {
            this.SetNewTutorialStage(const_253);
         }
         else if(this.mTutorialStage >= const_246 || this.MissionIsComplete(class_13.const_118) && !(this.mAlertState & const_186) && this.mLockboxData.method_662())
         {
            this.SetNewTutorialStage(const_246);
         }
         else if(this.mTutorialStage >= const_476)
         {
            this.SetNewTutorialStage(const_476);
         }
         else if(this.mTutorialStage >= const_270)
         {
            this.SetNewTutorialStage(const_270);
         }
         else if(this.mTutorialStage >= const_337 || this.clientEnt && this.clientEnt.mExpLevel >= Entity.const_1230 && this.var_1407 >= 1 && !(this.mAlertState & const_501))
         {
            this.SetNewTutorialStage(const_337);
         }
         else if(this.mTutorialStage >= const_552)
         {
            this.SetNewTutorialStage(const_552);
         }
         else if(this.mTutorialStage >= const_389)
         {
            this.SetNewTutorialStage(const_389);
         }
         else if(this.mTutorialStage >= const_370 || !_loc4_ && this.clientEnt && !this.clientEnt.mMasterClass && this.clientEnt.mExpLevel >= Entity.const_695)
         {
            this.SetNewTutorialStage(const_370);
         }
         else if(this.mTutorialStage >= const_502)
         {
            this.SetNewTutorialStage(const_502);
         }
         else if(this.mTutorialStage >= const_392)
         {
            this.SetNewTutorialStage(const_392);
         }
         else if(this.mTutorialStage >= const_311 || !_loc4_ && this.clientEnt && this.clientEnt.mExpLevel >= Entity.const_834 && (!_loc3_ || !_loc3_.rank))
         {
            this.SetNewTutorialStage(const_311);
         }
         else if(this.mTutorialStage >= const_414)
         {
            this.SetNewTutorialStage(const_414);
         }
         else if(this.mTutorialStage >= const_377)
         {
            this.SetNewTutorialStage(const_377);
         }
         else if(this.mTutorialStage >= const_310 || !_loc4_ && this.clientEnt && this.clientEnt.mExpLevel >= Entity.const_796 && (!_loc2_ || !_loc2_.rank))
         {
            this.SetNewTutorialStage(const_310);
         }
         else if(this.mTutorialStage >= TUTORIALSTAGE_ATTOME2)
         {
            this.SetNewTutorialStage(TUTORIALSTAGE_ATTOME2);
         }
         else if(this.mTutorialStage >= const_349 || this.MissionIsComplete(class_13.const_557) && (!_loc1_ || !_loc1_.rank))
         {
            this.SetNewTutorialStage(const_349);
         }
         else if(this.mTutorialStage >= const_598 || this.MissionIsComplete(class_13.const_557))
         {
            this.SetNewTutorialStage(const_598);
         }
         else if(this.mTutorialStage >= const_355 || this.method_531(class_13.const_557))
         {
            this.SetNewTutorialStage(const_355);
         }
         else if(this.mTutorialStage >= const_433 || this.MissionIsComplete(class_13.const_118) && this.level.internalName == "NewbieRoad")
         {
            this.SetNewTutorialStage(const_433);
         }
         else if(this.mTutorialStage >= const_372)
         {
            this.SetNewTutorialStage(const_372);
         }
         else if(this.mTutorialStage >= const_500 || this.MissionIsComplete(class_13.const_118) && this.level.internalName == "CraftTown" && (!_loc1_ || !_loc1_.rank))
         {
            this.SetNewTutorialStage(const_500);
         }
         else if(this.mTutorialStage >= const_393 || this.method_999(class_13.const_118))
         {
            this.SetNewTutorialStage(const_393);
         }
         else if(this.mTutorialStage >= const_688 || this.method_531(class_13.const_426))
         {
            this.SetNewTutorialStage(const_688);
         }
         else if(this.mTutorialStage >= const_358 || this.MissionIsComplete(class_13.const_831))
         {
            this.SetNewTutorialStage(const_358);
         }
         else if(this.mTutorialStage >= const_266)
         {
            this.SetNewTutorialStage(const_266);
         }
         else if(this.mTutorialStage >= const_150)
         {
            this.SetNewTutorialStage(const_150);
         }
         else if(this.mTutorialStage >= const_212 || this.method_701(class_13.const_831))
         {
            this.SetNewTutorialStage(const_212);
         }
         else if(this.mTutorialStage >= const_313 || this.MissionIsComplete(class_13.const_544))
         {
            this.SetNewTutorialStage(const_313);
         }
         else if(this.mTutorialStage >= const_306 || this.method_701(class_13.const_544))
         {
            this.SetNewTutorialStage(const_306);
         }
      }
      
      public function method_1076() : Boolean
      {
         if(this.mUIManager.var_981)
         {
            return true;
         }
         if(Boolean(this.screenChat) && this.screenChat.var_981)
         {
            return true;
         }
         return this.var_1412;
      }
      
      public function method_1729(param1:uint) : void
      {
         var _loc2_:Entity = null;
         this.mBonusLevels = param1;
         for each(_loc2_ in this.entities)
         {
            _loc2_.method_1929();
         }
         if(!(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
         {
            var_172.method_973();
         }
      }
      
      public function method_708(param1:uint) : void
      {
         var _loc2_:Entity = null;
         for each(_loc2_ in this.entities)
         {
            _loc2_.method_961(param1);
         }
         this.var_2142 = param1;
         var_172.method_1108();
      }
      
      public function method_527(param1:int, param2:Number, param3:Number, param4:uint, param5:Boolean, param6:Boolean, param7:Boolean, param8:Boolean = false, param9:uint = 0) : void
      {
         var _loc10_:String = "";
         if(param1 < 0)
         {
            param1 = -param1;
            if(!param7)
            {
               _loc10_ = "";
            }
         }
         var _loc11_:Number = const_950;
         var _loc12_:Number = param5 ? 0.8 * 1.3 : 0.8;
         if(param8)
         {
            _loc12_ = 0.8 * 1.5;
         }
         var _loc14_:class_72 = new class_72(this,_loc10_ + param1.toString(),param2,param3 - _loc11_,param4,_loc12_,true,null,null,param9);
         if(param8)
         {
            _loc14_.var_2642 = true;
         }
         if(param5)
         {
            _loc14_.var_847 = 800;
            _loc14_.var_1053 = 920;
            _loc14_.var_514 = 2.5;
            _loc14_.var_2225 = 0.18;
         }
         else
         {
            _loc14_.var_847 = 450;
            _loc14_.var_514 = 6.5;
            _loc14_.var_1053 = 720;
            _loc14_.var_2225 = param6 ? 0.7 : 0.35;
         }
         this.var_532.push(_loc14_);
      }
      
      public function GetEntFromID(param1:int) : Entity
      {
         var _loc2_:Entity = null;
         for each(_loc2_ in this.entities)
         {
            if(_loc2_.id == param1)
            {
               return _loc2_;
            }
         }
         return null;
      }
      
      public function method_2004(param1:int, param2:int) : class_130
      {
         var _loc3_:class_130 = null;
         for each(_loc3_ in this.var_371)
         {
            if(_loc3_.var_19.id == param1 && _loc3_.remoteMissileID == param2)
            {
               return _loc3_;
            }
         }
         return null;
      }
      
      public function GetSummonedCreatures(param1:uint, param2:PowerType) : Vector.<Entity>
      {
         var _loc3_:Entity = null;
         var _loc4_:uint = 0;
         var _loc5_:uint = this.entities.length;
         var _loc6_:Vector.<Entity> = new Vector.<Entity>();
         _loc4_ = 0;
         for(; _loc4_ < _loc5_; _loc4_++)
         {
            _loc3_ = this.entities[_loc4_];
            if(_loc3_.summonerId == param1)
            {
               if(param2)
               {
                  if(!_loc3_.var_99)
                  {
                     continue;
                  }
                  if(param2.basePowerName)
                  {
                     if(param2.basePowerName != _loc3_.var_99.basePowerName)
                     {
                        continue;
                     }
                  }
                  if(_loc3_.var_99 != param2)
                  {
                     continue;
                  }
               }
               if(_loc3_.entState != Entity.const_6)
               {
                  _loc6_.push(_loc3_);
               }
            }
         }
         return _loc6_;
      }
      
      public function GatherEntities(param1:Entity, param2:Number, param3:Number, param4:Number, param5:Number, param6:uint) : Array
      {
         var _loc8_:* = false;
         var _loc9_:Boolean = false;
         var _loc17_:Number = NaN;
         var _loc18_:Number = NaN;
         var _loc19_:Number = NaN;
         var _loc20_:Number = NaN;
         var _loc21_:Number = NaN;
         var _loc25_:Entity = null;
         var _loc7_:Array = new Array();
         var _loc10_:* = param6 & ENEMY;
         var _loc11_:* = param6 & FRIEND;
         var _loc12_:Boolean = !_loc10_ && !_loc11_;
         var _loc13_:Number = param2 - param4;
         var _loc14_:Number = param2 + param4;
         var _loc15_:Number = param3 - param5;
         var _loc16_:Number = param3 + param5;
         var _loc22_:uint = Entity.const_6;
         var _loc23_:Boolean = Boolean(param6 & ONLY_DEADGUYS);
         var _loc24_:Boolean = Boolean(param6 & INTENTIONAL_MELEE);
         for each(_loc25_ in this.entities)
         {
            _loc17_ = _loc25_.entType.width * 0.5;
            if((_loc18_ = _loc25_.appearPosX - _loc17_) <= _loc14_)
            {
               if((_loc19_ = _loc25_.appearPosX + _loc17_) >= _loc13_)
               {
                  if((_loc21_ = _loc25_.appearPosY) >= _loc15_)
                  {
                     if((_loc20_ = _loc25_.appearPosY - _loc25_.entType.height) <= _loc16_)
                     {
                        if(!(!_loc24_ && _loc25_.behaviorType.var_1225))
                        {
                           if(_loc25_.method_156())
                           {
                              if((_loc8_ = _loc25_.entState == _loc22_) == _loc23_)
                              {
                                 _loc9_ = param1.team != _loc25_.team && _loc25_.team != Entity.NEUTRAL;
                                 if(_loc12_ || _loc10_ && _loc9_ || _loc11_ && !_loc9_)
                                 {
                                    _loc7_.push(_loc25_);
                                 }
                              }
                           }
                        }
                     }
                  }
               }
            }
         }
         return _loc7_;
      }
      
      public function method_2135(param1:Point, param2:Number) : Vector.<class_130>
      {
         var _loc5_:class_130 = null;
         var _loc6_:Point = null;
         var _loc7_:Number = NaN;
         var _loc3_:Vector.<class_130> = new Vector.<class_130>();
         var _loc4_:Number = param2 * param2;
         for each(_loc5_ in this.var_371)
         {
            if((_loc7_ = (_loc6_ = _loc5_.var_11.subtract(param1)).x * _loc6_.x + _loc6_.y * _loc6_.y) < _loc4_)
            {
               _loc3_.push(_loc5_);
            }
         }
         return _loc3_;
      }
      
      public function method_2120(param1:Entity, param2:Point, param3:Number, param4:uint) : Vector.<class_130>
      {
         var _loc8_:Boolean = false;
         var _loc11_:class_130 = null;
         var _loc12_:Point = null;
         var _loc13_:Number = NaN;
         var _loc5_:* = param4 & ENEMY;
         var _loc6_:* = param4 & FRIEND;
         var _loc7_:Boolean = !_loc5_ && !_loc6_;
         var _loc9_:Vector.<class_130> = new Vector.<class_130>();
         var _loc10_:Number = param3 * param3;
         for each(_loc11_ in this.var_371)
         {
            if((_loc13_ = (_loc12_ = _loc11_.var_11.subtract(param2)).x * _loc12_.x + _loc12_.y * _loc12_.y) < _loc10_)
            {
               _loc8_ = param1.team != _loc11_.var_19.team && _loc11_.var_19.team != Entity.NEUTRAL;
               if(_loc7_ || _loc5_ && _loc8_ || _loc6_ && !_loc8_)
               {
                  _loc9_.push(_loc11_);
               }
            }
         }
         return _loc9_;
      }
      
      public function method_2109(param1:Entity, param2:Point, param3:Number, param4:uint) : class_130
      {
         var _loc8_:Boolean = false;
         var _loc11_:class_130 = null;
         var _loc12_:Point = null;
         var _loc13_:Number = NaN;
         var _loc5_:* = param4 & ENEMY;
         var _loc6_:* = param4 & FRIEND;
         var _loc7_:Boolean = !_loc5_ && !_loc6_;
         var _loc9_:class_130 = null;
         var _loc10_:Number = param3 * param3;
         for each(_loc11_ in this.var_371)
         {
            if((_loc13_ = (_loc12_ = _loc11_.var_11.subtract(param2)).x * _loc12_.x + _loc12_.y * _loc12_.y) < _loc10_)
            {
               _loc8_ = param1.team != _loc11_.var_19.team && _loc11_.var_19.team != Entity.NEUTRAL;
               if(_loc7_ || _loc5_ && _loc8_ || _loc6_ && !_loc8_)
               {
                  _loc9_ = _loc11_;
                  _loc10_ = _loc13_;
               }
            }
         }
         return _loc9_;
      }
      
      public function method_885(param1:KeyboardEvent) : void
      {
         var _loc2_:int = int(this.mKeybindManager.method_907(param1.keyCode,this.CONTEXT_NORMAL));
         var _loc3_:int = this.var_406.indexOf(_loc2_);
         if(_loc3_ != -1)
         {
            this.var_406.splice(_loc3_,1);
         }
         if(_loc2_ == Game.const_158)
         {
            this.clientEnt.var_24.method_727();
         }
         if(_loc2_ == Game.const_188)
         {
            this.clientEnt.var_24.method_725();
         }
      }
      
      public function method_668(param1:uint) : void
      {
         var _loc5_:Packet = null;
         var _loc6_:String = null;
         var _loc7_:uint = 0;
         var _loc8_:class_9 = null;
         var _loc9_:class_9 = null;
         var _loc10_:class_9 = null;
         var _loc11_:class_9 = null;
         var _loc12_:class_9 = null;
         var _loc13_:class_6 = null;
         var _loc2_:Entity = this.GetEntFromID(param1);
         var _loc3_:a_Cue = !!_loc2_ ? _loc2_.cue : null;
         if(!_loc3_ || !this.CanSendPacket())
         {
            return;
         }
         var _loc4_:String;
         if(!(_loc4_ = _loc3_.characterName))
         {
            return;
         }
         if(this.mTimeThisTick - _loc2_.var_2703 < MIN_TIME_BETWEEN_INTERACTS)
         {
            return;
         }
         _loc2_.var_2703 = this.mTimeThisTick;
         _loc2_.var_2144 = true;
         if(this.level.var_333)
         {
            this.method_1916(_loc2_,_loc3_,_loc4_);
         }
         else
         {
            (_loc5_ = new Packet(LinkUpdater.PKTTYPE_TALK_TO_NPC)).method_9(_loc2_.id);
            this.serverConn.SendPacket(_loc5_);
         }
         if(this.mTutorialStage == Game.const_212 && _loc4_ == "CaptainFink")
         {
            this.SetNewTutorialStage(const_150);
         }
         if(Boolean(this.clientEnt) && !this.var_2619)
         {
            _loc6_ = "";
            _loc7_ = uint(this.mBuildingInfo.mWorkerBuildingID);
            _loc8_ = class_14.var_278[_loc7_];
            if(_loc8_ = this.mBuildingInfo.method_256(_loc8_))
            {
               _loc6_ = (_loc8_ = class_9.method_132(_loc8_)).type;
            }
            if(_loc4_ == "Special_CraftForge")
            {
               if((_loc9_ = this.mBuildingInfo.GetOwnedBuildingByName("Forge")).rank == 0 && _loc6_ != "Forge")
               {
                  if(this.clientEnt.mExpLevel < Entity.const_834)
                  {
                     this.screenChat.ReceiveChat(0,"Is this a Forge? Perhaps when I\'m more experienced...",false);
                  }
                  else
                  {
                     if(_loc8_)
                     {
                        this.screenChat.ReceiveChat(0,"The workers are busy upgrading the " + _loc8_.displayName,false);
                        return;
                     }
                     if(_loc10_ = this.mBuildingInfo.UpgradeBuilding(_loc9_))
                     {
                        this.screenUpgrading.Display(_loc10_);
                     }
                  }
               }
               else if(_loc6_ != "Forge")
               {
                  if(this.mMagicForgeStatus.status == class_111.const_264)
                  {
                     this.var_996.Display();
                  }
                  else
                  {
                     this.screenForge.Display();
                  }
               }
               else
               {
                  this.screenUpgrading.Display(_loc8_);
               }
               return;
            }
            if(_loc4_ == "Special_AbilityTome")
            {
               if((_loc11_ = this.mBuildingInfo.GetOwnedBuildingByName("Tome")).rank == 0 && _loc6_ != "Tome")
               {
                  if(_loc8_)
                  {
                     this.screenChat.ReceiveChat(0,"The workers are busy upgrading the " + _loc8_.displayName,false);
                     return;
                  }
                  if(_loc10_ = this.mBuildingInfo.UpgradeBuilding(_loc11_))
                  {
                     this.screenUpgrading.Display(_loc10_);
                  }
               }
               else if(_loc6_ != "Tome")
               {
                  this.screenTome.Display(this.clientEnt.entType.className);
               }
               else
               {
                  this.screenUpgrading.Display(_loc8_);
               }
               return;
            }
            if(_loc4_ == "Special_ClassTower")
            {
               if(_loc6_ != "Tower")
               {
                  if(this.clientEnt.mExpLevel < Entity.const_695)
                  {
                     this.screenChat.ReceiveChat(0,"This looks interesting. Perhaps when I\'m more experienced...",false);
                  }
                  else if(!this.clientEnt.mMasterClass)
                  {
                     this.screenMasterClassSelection.Display();
                  }
                  else if(this.clientEnt.getTowerLevel() >= 1)
                  {
                     this.screenClassTowers.Display();
                  }
               }
               else
               {
                  this.screenUpgrading.Display(_loc8_);
               }
               return;
            }
            if(_loc4_ == "Special_Barn")
            {
               if((_loc12_ = this.mBuildingInfo.GetOwnedBuildingByName("Barn")).rank == 0 && _loc6_ != "Barn")
               {
                  if(this.clientEnt.mExpLevel < Entity.const_796)
                  {
                     this.screenChat.ReceiveChat(0,"Wow! My very own barn. Perhaps when I\'m more experienced...",false);
                  }
                  else
                  {
                     if(_loc8_)
                     {
                        this.screenChat.ReceiveChat(0,"The workers are busy upgrading the " + _loc8_.displayName,false);
                        return;
                     }
                     if(_loc10_ = this.mBuildingInfo.UpgradeBuilding(_loc12_))
                     {
                        this.screenUpgrading.Display(_loc10_);
                     }
                  }
               }
               else if(_loc6_ != "Barn")
               {
                  this.screenBarn.Display();
               }
               else
               {
                  this.screenUpgrading.Display(_loc8_);
               }
               return;
            }
            if(_loc4_ == "Special_LookChange")
            {
               this.screenLook.Display();
               return;
            }
            if(_loc4_ == "Special_Dyer")
            {
               this.screenDyeGear.Display();
               return;
            }
            if(_loc4_ == "Special_RoyalSigil")
            {
               if(this.mAlertState & const_186)
               {
                  this.screenRoyalSigilStore.Display();
                  return;
               }
            }
            if(_loc4_ == "Special_TreasureTrove")
            {
               if(!this.mLockboxData.method_662())
               {
                  this.screenChat.ReceiveChat(0,"Maybe that old man knows how to open this...",false);
               }
               else
               {
                  this.mLockboxData.mLockboxID = this.mLockboxData.method_1459();
                  this.screenLockBox.Display();
               }
               return;
            }
            if(_loc4_ == "Special_Halloween_Statue_First" || _loc4_ == "Special_Halloween_Statue_FirstHard")
            {
               if(_loc13_ = class_14.var_661[1])
               {
                  _loc2_.StartSkit(_loc13_.var_1646,true,this.clientEnt);
               }
               return;
            }
            if(_loc4_ == "Special_Halloween_Statue_Second" || _loc4_ == "Special_Halloween_Statue_SecondHard")
            {
               if(_loc13_ = class_14.var_661[2])
               {
                  _loc2_.StartSkit(_loc13_.var_1646,true,this.clientEnt);
               }
               return;
            }
            if(_loc4_ == "Special_Halloween_Statue_Third" || _loc4_ == "Special_Halloween_Statue_ThirdHard")
            {
               if(_loc13_ = class_14.var_661[3])
               {
                  _loc2_.StartSkit(_loc13_.var_1646,true,this.clientEnt);
               }
               return;
            }
            if(_loc4_ == "Special_Halloween_Statue_Fourth" || _loc4_ == "Special_Halloween_Statue_FourthHard")
            {
               if(_loc13_ = class_14.var_661[4])
               {
                  _loc2_.StartSkit(_loc13_.var_1646,true,this.clientEnt);
               }
               return;
            }
         }
      }
      
      public function method_778(param1:uint) : void
      {
         this.var_890.Display(param1);
      }
      
      public function method_1093(param1:class_77) : void
      {
         if(!this.clientEnt)
         {
            return;
         }
         var _loc2_:String = param1.dObj.sayOnInteract;
         if(_loc2_)
         {
            this.clientEnt.StartSkit(_loc2_,true,this.clientEnt);
         }
      }
      
      public function method_867(param1:Entity, param2:String, param3:Door) : void
      {
         var _loc4_:Door = null;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         var _loc7_:class_37 = null;
         for each(_loc4_ in this.level.targetList)
         {
            if(_loc4_.localTarget == param2 && _loc4_ != param3)
            {
               if(param1.bFacingLeft() != _loc4_.bFacingLeft)
               {
                  param1.bLeft = _loc4_.bFacingLeft;
                  param1.bBackpedal = false;
               }
               _loc5_ = _loc4_.posX;
               _loc6_ = _loc4_.posY;
               if(_loc7_ = this.collMan.getFloorCollision(0,_loc4_.posX,_loc4_.posY - 10,new Point(0,80),var_1484,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0))
               {
                  _loc5_ = var_1484.x;
                  _loc6_ = var_1484.y - Entity.PULLBACK_DIST;
                  param1.SetCurrSurface(_loc7_);
               }
               param1.TeleportTo(_loc5_,_loc6_);
               break;
            }
         }
      }
      
      public function OpenDoor(param1:Door) : void
      {
         var _loc3_:Packet = null;
         if(!this.clientEnt)
         {
            return;
         }
         var _loc2_:Boolean = this.level.internalName == "BridgeTownHard" && param1.doorID == class_95.const_837;
         if(!_loc2_ && this.clientEnt.entState == Entity.const_6)
         {
            return;
         }
         if(param1.localTarget)
         {
            this.method_867(this.clientEnt,param1.localTarget,param1);
         }
         else if(this.CanSendPacket())
         {
            _loc3_ = new Packet(LinkUpdater.PKTTYPE_OPEN_DOOR);
            _loc3_.method_9(param1.doorID);
            this.serverConn.SendPacket(_loc3_);
            this.mbTransferMode = true;
         }
      }
      
      public function method_1060(param1:int) : void
      {
         if(this.clientEnt.bFiring || Boolean(this.clientEnt.combatState.mActivePower))
         {
            return;
         }
         if(param1 == Game.const_151 && this.var_406.indexOf(Game.const_151) == -1 || param1 == Game.const_153 && this.var_406.indexOf(Game.const_153) == -1)
         {
            this.clientEnt.var_1787 = 0;
         }
      }
      
      private function method_1949(param1:uint) : Boolean
      {
         if(param1 == Game.const_240)
         {
            if(this.screenKeybind.mbVisible)
            {
               this.screenKeybind.Hide();
               return true;
            }
            if(this.screenSocket.mbVisible)
            {
               this.screenSocket.Hide();
               return true;
            }
            if(this.screenReplace.mbVisible)
            {
               this.screenReplace.Hide();
               return true;
            }
            if(this.screenBuyIdols.mbVisible)
            {
               this.screenBuyIdols.Hide();
               return true;
            }
            if(this.screenGoldShort.mbVisible)
            {
               this.screenGoldShort.Hide();
               return true;
            }
            if(this.screenCatalysts.mbVisible)
            {
               this.screenCatalysts.Hide();
               return true;
            }
            if(this.screenLockBoxBuyTroves.mbVisible)
            {
               this.screenLockBoxBuyTroves.Hide();
               return true;
            }
            if(this.screenLockBoxBuyKeys.mbVisible)
            {
               this.screenLockBoxBuyKeys.Hide();
               return true;
            }
            if(this.screenRoyalSigilStorePrompt.mbVisible)
            {
               this.screenRoyalSigilStorePrompt.Hide();
               return true;
            }
            if(this.screenRoyalSigilStore.mbVisible)
            {
               this.screenRoyalSigilStore.Hide();
               return true;
            }
            if(this.screenFeedPet.mbVisible)
            {
               this.screenFeedPet.Hide();
               return true;
            }
            if(this.screenBarn.mbVisible)
            {
               this.screenBarn.Hide();
               return true;
            }
            if(this.screenMasterClassSelection.mbVisible)
            {
               this.screenMasterClassSelection.Hide();
               return true;
            }
            if(this.screenUpgrading.mbVisible)
            {
               this.screenUpgrading.Hide();
               return true;
            }
            if(this.screenClassTowers.mbVisible)
            {
               this.screenClassTowers.Hide();
               return true;
            }
            if(this.screenSigil.mbVisible)
            {
               this.screenSigil.Hide();
               return true;
            }
            if(this.screenSpellbook.mbVisible)
            {
               this.screenSpellbook.Hide();
               return true;
            }
            if(this.screenTome.mbVisible)
            {
               this.screenTome.Hide();
               return true;
            }
            if(this.screenForge.mbVisible)
            {
               this.screenForge.Hide();
               return true;
            }
            if(this.var_890.mbVisible)
            {
               this.var_890.Hide();
               return true;
            }
            if(this.screenArmory.mbVisible)
            {
               this.screenArmory.Hide();
               return true;
            }
            if(this.screenMap.mbVisible)
            {
               this.screenMap.Hide();
               return true;
            }
            if(this.screenFriend.method_40())
            {
               this.screenFriend.Hide();
               return true;
            }
            if(this.screenWalkthrough.mbVisible)
            {
               this.screenWalkthrough.Hide();
               return true;
            }
            if(this.screenDyeGear.mbVisible)
            {
               this.screenDyeGear.Hide();
               return true;
            }
            if(this.screenLook.mbVisible)
            {
               this.screenLook.Hide();
               return true;
            }
            if(this.var_758.mbVisible)
            {
               this.var_758.Hide();
               return true;
            }
            if(this.screenLockBox.mbVisible)
            {
               this.screenLockBox.Hide();
               return true;
            }
         }
         return false;
      }
      
      public function method_702(param1:KeyboardEvent) : void
      {
         var _loc4_:int = 0;
         var _loc5_:String = null;
         var _loc6_:Boolean = false;
         var _loc7_:Boolean = false;
         var _loc8_:Boolean = false;
         var _loc9_:PowerType = null;
         var _loc10_:PowerType = null;
         var _loc11_:PowerType = null;
         var _loc12_:PowerType = null;
         if(this.var_742.mbVisible)
         {
            return;
         }
         var _loc2_:int = int(this.mKeybindManager.method_907(param1.keyCode));
         var _loc3_:int = int(param1.keyCode);
         if(this.mKeybindManager.mbStatePickKey)
         {
            if(_loc3_ == Keyboard.ESCAPE)
            {
               _loc3_ = 255;
            }
            if(this.mKeybindManager.method_1805(_loc3_))
            {
               _loc4_ = this.mKeybindManager.method_32(this.mKeybindManager.mActiveCommand,_loc3_,true,true);
               this.screenKeybind.method_1556(_loc3_);
               this.screenKeybind.method_1089(this.mKeybindManager.mActiveCommand,_loc3_);
               this.mKeybindManager.mbStatePickKey = false;
               this.mKeybindManager.mActiveCommand = 0;
            }
            else
            {
               this.screenKeybind.method_292("Pick Another Key");
            }
            return;
         }
         if(this.screenLockBox.method_972())
         {
            return;
         }
         if(this.screenArmory.method_54(_loc2_))
         {
            return;
         }
         if(this.screenChat.method_54(_loc2_))
         {
            return;
         }
         if(this.screenHud.method_54(_loc2_))
         {
            return;
         }
         if(this.method_1949(_loc2_))
         {
            return;
         }
         if(this.main.stage.focus == this.screenChat.var_2.am_ChatHistory)
         {
            this.main.stage.focus = this.main;
            this.main.stage.focus = null;
         }
         if(this.screenKeybind.mbVisible)
         {
            return;
         }
         this.method_1060(_loc2_);
         if(this.var_406.indexOf(_loc2_) == -1)
         {
            this.var_406.push(_loc2_);
         }
         switch(_loc2_)
         {
            case Game.const_158:
               if(this.clientEnt)
               {
                  this.clientEnt.var_24.Jump();
               }
               break;
            case Game.const_188:
               if(this.clientEnt)
               {
                  this.clientEnt.var_24.Drop();
               }
               break;
            case Game.const_401:
               if(this.clientEnt)
               {
                  this.clientEnt.DoEmote("Wave",false);
               }
               break;
            case Game.const_317:
               if(this.clientEnt)
               {
                  this.clientEnt.DoEmote("Cheer L",false);
               }
               break;
            case Game.const_574:
               if(this.clientEnt)
               {
                  this.clientEnt.DoEmote("Dance L",false);
               }
               break;
            case Game.const_328:
               if(!this.screenInteractiveTutorial.method_134())
               {
                  this.screenMap.Toggle();
               }
               class_53.method_79("Map:Hotkey",1);
               break;
            case Game.const_346:
               if(Boolean(this.clientEnt.mMasterClass) && !this.screenInteractiveTutorial.method_134())
               {
                  if(!this.screenSigil.mbVisible && this.bWaitingForChangeMasterClassResponse)
                  {
                     break;
                  }
                  this.screenSigil.Toggle(this.clientEnt.mMasterClass);
               }
               break;
            case Game.const_367:
               if(!this.screenInteractiveTutorial.method_134())
               {
                  this.screenFriend.Toggle();
               }
               break;
            case Game.const_240:
               if(!this.screenLinkBar.method_54(_loc2_) && !this.screenInteractiveTutorial.method_134())
               {
                  this.screenMenu.Toggle();
               }
               break;
            case Game.const_364:
               if(!this.screenInteractiveTutorial.method_134())
               {
                  this.screenArmory.Toggle();
               }
               break;
            case Game.const_357:
               if(!this.screenInteractiveTutorial.method_134())
               {
                  this.screenBuyIdols.Toggle(0);
               }
               break;
            case Game.const_314:
               if(!this.screenInteractiveTutorial.method_134())
               {
                  if(Boolean(this.clientEnt) && Boolean(this.clientEnt.var_916))
                  {
                     this.OpenDoor(this.clientEnt.var_916);
                     break;
                  }
                  if(Boolean(this.clientEnt) && Boolean(this.clientEnt.var_1783))
                  {
                     this.method_668(this.clientEnt.var_1783);
                  }
               }
               break;
            case Game.const_329:
               if(!this.screenInteractiveTutorial.method_134())
               {
                  _loc5_ = String(this.level.internalName);
                  _loc6_ = Boolean(this.mMissionInfoList[class_13.const_118]) || _loc5_ != "NewbieRoad";
                  _loc8_ = !(_loc7_ = Boolean(this.level.var_333)) && this.level.bInstanced;
                  if(this.clientEnt && this.clientEnt.combatState.method_123(4000) && !_loc8_ && _loc7_)
                  {
                     this.OpenDoor(new Door("LeaveHome",0,0,null,0,null));
                  }
                  if(this.clientEnt && this.clientEnt.combatState.method_123(4000) && !_loc8_ && !_loc7_ && _loc6_)
                  {
                     this.OpenDoor(new Door("GoHome",0,0,null,class_11.const_759,null));
                  }
               }
               break;
            case Game.const_321:
               if(Boolean(this.clientEnt) && !this.screenInteractiveTutorial.method_134())
               {
                  this.screenSpellbook.Toggle(this.clientEnt.entType.className);
               }
               break;
            case Game.const_274:
               if(Boolean(this.clientEnt) && Boolean(this.clientEnt.mEquipMount))
               {
                  if(this.clientEnt.combatState.var_270)
                  {
                     _loc9_ = class_14.powerTypesDict["Dismount"];
                     this.clientEnt.method_252(_loc9_);
                     break;
                  }
                  if(_loc10_ = PowerType.var_440)
                  {
                     this.clientEnt.method_252(_loc10_);
                  }
               }
               break;
            case Game.const_277:
               if(Boolean(this.clientEnt) && Boolean(this.clientEnt.mEquipPet))
               {
                  if(this.clientEnt.combatState.var_724)
                  {
                     _loc11_ = class_14.powerTypesDict["DismissPet"];
                     this.clientEnt.method_252(_loc11_);
                     break;
                  }
                  if(_loc12_ = class_14.powerTypesDict[this.clientEnt.mEquipPet.mPetType.var_1138])
                  {
                     this.clientEnt.method_252(_loc12_);
                  }
                  break;
               }
         }
      }
      
      public function GetPlayerEntFromEntName(param1:String) : Entity
      {
         return this.var_1495[param1];
      }
      
      public function method_1252() : Boolean
      {
         var _loc1_:Number = getTimer() - Main.var_1468;
         return _loc1_ < const_906;
      }
      
      private function method_329(param1:MouseEvent) : void
      {
         var _loc2_:* = false;
         if(this.var_742.mbVisible)
         {
            param1.stopPropagation();
            return;
         }
         if(this.method_1252())
         {
            param1.stopPropagation();
            return;
         }
         if(this.var_1601)
         {
            param1.stopPropagation();
            return;
         }
         if(this.screenChat)
         {
            this.screenChat.method_803();
         }
         if(this.var_890.mbVisible)
         {
            this.var_890.Hide();
         }
         else if(this.screenFriend.method_40())
         {
            this.screenFriend.Hide();
         }
         else if(this.screenChat && this.screenChat.mWindow && this.screenChat.var_1343)
         {
            this.screenChat.method_658();
         }
         else if(this.clientEnt)
         {
            _loc2_ = this.clientEnt.var_485 != 0;
            if(!_loc2_ && this.clientEnt.var_848 && this.clientEnt.var_2008)
            {
               this.OpenDoor(this.clientEnt.var_848);
            }
            else if(!_loc2_ && Boolean(this.clientEnt.var_518))
            {
               this.method_668(this.clientEnt.var_518);
            }
            else if(!_loc2_ && this.clientEnt.var_1216 && this.clientEnt.combatState.method_123(const_690))
            {
               this.method_778(this.clientEnt.var_1216);
            }
            else if(!_loc2_ && Boolean(this.clientEnt.var_1113))
            {
               this.method_1093(this.clientEnt.var_1113);
            }
            else
            {
               this.clientEnt.var_24.Fire();
            }
         }
      }
      
      private function method_146(param1:MouseEvent) : void
      {
         if(param1.buttonDown)
         {
            return;
         }
         if(this.clientEnt)
         {
            this.clientEnt.var_24.method_674();
         }
      }
      
      public function method_790(param1:Event) : void
      {
         if(Boolean(this.clientEnt) && Boolean(this.clientEnt.var_24.var_418))
         {
            this.clientEnt.var_24.var_418.method_1582();
         }
      }
      
      public function method_829(param1:MouseEvent) : void
      {
         if(Boolean(this.clientEnt) && Boolean(this.clientEnt.var_24.var_418))
         {
            this.clientEnt.var_24.var_418.method_1102();
         }
      }
      
      public function method_1710() : void
      {
         this.main.stage.addEventListener(MouseEvent.MOUSE_MOVE,this.method_829);
         this.main.stage.addEventListener(MouseEvent.MOUSE_DOWN,this.method_329);
         this.main.stage.addEventListener(MouseEvent.RIGHT_MOUSE_DOWN,this.method_329);
         this.main.stage.addEventListener(Event.MOUSE_LEAVE,this.method_790);
         this.main.stage.addEventListener(MouseEvent.MOUSE_UP,this.method_146);
         this.main.stage.addEventListener(MouseEvent.MOUSE_UP,this.method_146,true);
         this.main.stage.addEventListener(MouseEvent.RIGHT_MOUSE_UP,this.method_146);
         this.main.stage.addEventListener(MouseEvent.RIGHT_MOUSE_UP,this.method_146,true);
      }
      
      public function method_1140() : void
      {
         this.main.stage.removeEventListener(MouseEvent.MOUSE_MOVE,this.method_829);
         this.main.stage.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_329);
         this.main.stage.removeEventListener(MouseEvent.RIGHT_MOUSE_DOWN,this.method_329);
         this.main.stage.removeEventListener(Event.MOUSE_LEAVE,this.method_790);
         this.main.stage.removeEventListener(MouseEvent.MOUSE_UP,this.method_146);
         this.main.stage.removeEventListener(MouseEvent.MOUSE_UP,this.method_146,true);
         this.main.stage.removeEventListener(MouseEvent.RIGHT_MOUSE_UP,this.method_146);
         this.main.stage.removeEventListener(MouseEvent.RIGHT_MOUSE_UP,this.method_146,true);
      }
      
      private function method_1933() : void
      {
         var _loc1_:Packet = new Packet(LinkUpdater.PKTTYPE_TRANSFER_READY);
         _loc1_.method_9(this.var_1725);
         _loc1_.method_26(this.var_1274);
         this.serverConn.SendPacket(_loc1_);
         this.var_1274 = null;
      }
      
      private function method_1968() : void
      {
         var _loc1_:Packet = new Packet(LinkUpdater.PKTTYPE_LOGIN_VERSION);
         _loc1_.method_9(Game.GAME_VERSION);
         this.serverConn.SendPacket(_loc1_);
         this.var_94.method_71("Connected!");
      }
      
      private function method_1610() : void
      {
         this.var_94.method_71("Could not connect to server. Please check your connection and try again.",true);
      }
      
      public function method_429(param1:Boolean) : void
      {
         if(!param1)
         {
            this.serverConn = new Connection(this,this.method_1933);
         }
         else
         {
            this.var_94.method_71("Connecting...");
            this.serverConn = new Connection(this,this.method_1968,this.method_1610);
         }
         var _loc2_:String = !!(DevSettings.flags & DevSettings.DEVFLAG_SERVERLOCAL) ? DevSettings.var_2032 : LinkUpdater.const_1264;
         this.serverConn.method_403(_loc2_,Connection.LOGINSERVER_PORT);
      }
      
      private function method_1168() : void
      {
         var _loc1_:Packet = new Packet(LinkUpdater.PKTTYPE_GAMESERVER_LOGIN);
         _loc1_.method_9(this.var_1725);
         _loc1_.method_26(this.var_1274);
         _loc1_.method_15(this.var_1703);
         this.serverConn.SendPacket(_loc1_);
         this.var_1274 = null;
         this.var_1703 = false;
         this.var_2052 = true;
      }
      
      private function method_1139() : void
      {
         var _loc1_:Packet = new Packet(LinkUpdater.PKTTYPE_MASTER_CLIENT);
         _loc1_.method_9(this.var_2334);
         _loc1_.method_15(this.var_1703);
         this.serverConn.SendPacket(_loc1_);
         this.var_1703 = false;
      }
      
      public function method_730() : void
      {
         if(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT)
         {
            this.serverConn = new Connection(this,this.method_1139);
         }
         else
         {
            this.serverConn = new Connection(this,this.method_1168);
         }
         this.serverConn.method_403(this.main.var_2392,this.main.var_2363);
      }
      
      public function method_158(param1:MovieClip) : void
      {
         if(param1 && param1.visible && Boolean(param1.parent))
         {
            param1.visible = false;
            param1.parent.removeChild(param1);
         }
      }
      
      private function method_617(param1:Event) : void
      {
         this.var_1412 = true;
         param1.stopPropagation();
      }
      
      private function method_606(param1:Event) : void
      {
         this.var_1412 = false;
         param1.stopPropagation();
      }
      
      private function method_373(param1:Event) : void
      {
         if(this.screenChat)
         {
            this.screenChat.method_803();
         }
         param1.stopPropagation();
      }
      
      public function method_1398(param1:String, param2:Function = null) : MovieClip
      {
         var _loc3_:MovieClip = class_4.method_16(param1,true);
         _loc3_.addEventListener(MouseEvent.ROLL_OVER,this.method_617);
         _loc3_.addEventListener(MouseEvent.ROLL_OUT,this.method_606);
         _loc3_.dyn_MouseDownCallback = param2;
         if(_loc3_.dyn_MouseDownCallback)
         {
            _loc3_.addEventListener(MouseEvent.MOUSE_DOWN,_loc3_.dyn_MouseDownCallback);
         }
         else
         {
            _loc3_.addEventListener(MouseEvent.MOUSE_DOWN,this.method_373);
         }
         return _loc3_;
      }
      
      public function method_1878(param1:MovieClip) : void
      {
         param1.removeEventListener(MouseEvent.ROLL_OVER,this.method_617);
         param1.removeEventListener(MouseEvent.ROLL_OUT,this.method_606);
         if(param1.dyn_MouseDownCallback)
         {
            param1.removeEventListener(MouseEvent.MOUSE_DOWN,param1.dyn_MouseDownCallback);
         }
         else
         {
            param1.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_373);
         }
         param1.dyn_MouseDownCallback = null;
         if(param1.parent)
         {
            param1.parent.removeChild(param1);
         }
      }
      
      public function method_127() : void
      {
         this.var_398.Hide();
         this.var_479.Hide();
         this.var_94.Hide();
         this.var_273.Hide();
         this.var_341.Hide();
         this.var_141.Hide();
         this.var_933.Hide();
         this.screenFriend.Hide();
         this.mUIManager.method_1045();
      }
      
      public function method_267(param1:String, param2:String, param3:Boolean, param4:Boolean) : void
      {
         this.var_1447 = param1;
         this.var_1257 = param2;
         this.var_2098 = true;
         this.var_2020 = param4;
         if(Boolean(this.clientFacebookID) || Boolean(this.clientKongID))
         {
            return;
         }
         if(this.var_164)
         {
            this.var_164.data.dbUserEmail = param1;
            this.var_164.data.dbPassHash = param3 ? param2 : "";
            try
            {
               this.var_164.flush();
            }
            catch(error:Error)
            {
            }
         }
      }
      
      public function method_1239(param1:String, param2:String, param3:uint, param4:String) : void
      {
         if(Boolean(this.clientFacebookID) || Boolean(this.clientKongID))
         {
            return;
         }
         if(this.var_164)
         {
            this.var_164.data.dbCharName = param1;
            this.var_164.data.dbCharClass = param2;
            this.var_164.data.dbCharLevel = param3;
            this.var_164.data.dbEntType = param4;
            try
            {
               this.var_164.flush();
            }
            catch(error:Error)
            {
            }
         }
      }
      
      public function StoreGameInfo() : void
      {
         if(this.var_304)
         {
            this.var_304.data.dbProfaneFilterOff = !this.bProfaneFilter;
            this.var_304.data.dbShowGroupFloaters = this.bShowGroupFloaters;
            this.var_304.data.dbSoundManagerMuted = SoundManager.var_804;
            this.var_304.data.dbSoundVolumeInverted = 1 - SoundManager.var_597;
            this.var_304.data.dbMusicVolumeInverted = 1 - SoundManager.method_920(Main.const_77);
            try
            {
               this.var_304.flush();
            }
            catch(error:Error)
            {
            }
         }
      }
      
      public function method_2000() : void
      {
         var _loc1_:Object = null;
         this.gameState = STATE_LOGIN;
         this.var_2256 = false;
         this.var_2129 = new Dictionary();
         this.var_164 = SharedObject.getLocal("dbSavedData","/");
         this.main.stage.addEventListener(KeyboardEvent.KEY_DOWN,this.method_930);
         this.var_2417 = class_4.method_16("a_LoginBackground");
         this.var_193 = new Bitmap(null,PixelSnapping.ALWAYS,false);
         this.edgeLayer.addChildAt(this.var_193,0);
         this.var_2137 = true;
         this.var_1419 = true;
         this.method_557();
         this.screenLinkBar.Display();
         this.screenLinkBar.method_434();
         if(this.var_934)
         {
            if(this.var_1306)
            {
               this.var_341.Display();
            }
            else
            {
               this.var_273.Display();
            }
         }
         else
         {
            _loc1_ = this.var_164.data;
            if(Boolean(_loc1_.dbCharName) && Boolean(_loc1_.dbCharClass) && Boolean(_loc1_.dbCharLevel) && Boolean(_loc1_.dbEntType))
            {
               this.var_341.Display();
            }
            else if(!_loc1_.dbUserEmail)
            {
               this.var_273.Display();
            }
            else
            {
               this.var_479.Display();
               this.var_612 = false;
               this.var_1198 = true;
            }
         }
      }
      
      public function DoFullScreenUIEmote() : void
      {
         if(Boolean(this.clientEnt) && this.clientEnt.entState != Entity.const_6)
         {
            this.clientEnt.DoEmote(class_127.var_2336 + " loop");
         }
      }
      
      public function method_930(param1:KeyboardEvent) : void
      {
         var _loc2_:int = int(param1.keyCode);
         if(this.screenLinkBar.method_54(_loc2_))
         {
            return;
         }
         if(this.var_94.method_54(_loc2_))
         {
            return;
         }
         if(this.var_398.method_54(_loc2_))
         {
            return;
         }
         if(this.var_479.method_54(_loc2_))
         {
            return;
         }
         if(this.var_141.method_54(_loc2_))
         {
            return;
         }
         if(this.var_341.method_54(_loc2_))
         {
            return;
         }
         if(this.var_273.method_54(_loc2_))
         {
            return;
         }
      }
      
      public function method_557() : void
      {
         var _loc1_:Number = Number(this.main.overallScale);
         if(this.var_1419)
         {
            if(this.var_193.bitmapData)
            {
               this.var_193.bitmapData.dispose();
            }
            this.var_193.bitmapData = new BitmapData(Math.ceil(Camera.SCREEN_WIDTH * _loc1_),Math.ceil(Camera.SCREEN_HEIGHT * _loc1_),false);
            this.var_193.bitmapData.fillRect(this.var_193.bitmapData.rect,4737365);
            this.var_1419 = false;
         }
         var _loc2_:Number = 1 / _loc1_;
         this.var_193.bitmapData.drawWithQuality(this.var_2417,new Matrix(_loc1_,0,0,_loc1_),null,null,null,false,StageQuality.HIGH);
         this.var_193.scaleX = _loc2_;
         this.var_193.scaleY = _loc2_;
         this.var_2137 = false;
      }
      
      public function method_1312() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:String = null;
         var _loc3_:uint = 0;
         var _loc4_:Packet = null;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc8_:uint = 0;
         var _loc9_:Packet = null;
         if(SoundConfig.var_1662)
         {
            if(!this.var_2256)
            {
               SoundManager.method_103(Main.const_77,SoundConfig.var_1662,1);
               this.var_2256 = true;
            }
         }
         if(this.var_2137 || this.var_1419)
         {
            this.method_557();
         }
         if(this.serverConn && !this.serverConn.var_1203 && !this.serverConn.method_353())
         {
            this.serverConn.method_205();
            this.serverConn = null;
         }
         if(this.var_2098)
         {
            if(!this.serverConn)
            {
               this.var_1909 = null;
               this.var_355 = null;
               this.var_2138 = false;
               this.var_2056 = false;
               if(Boolean(this.var_1447) && Boolean(this.var_1257))
               {
                  this.method_429(true);
               }
               else
               {
                  this.var_479.Display();
               }
            }
            this.var_2098 = false;
         }
         if(Boolean(this.serverConn) && Boolean(this.linkUpdater))
         {
            if(Boolean(this.var_1909) && Boolean(this.var_1447) && Boolean(this.var_1257))
            {
               _loc1_ = this.var_2020 && !this.var_934 ? LinkUpdater.PKTTYPE_LOGIN_CREATE : LinkUpdater.PKTTYPE_LOGIN_AUTHENTICATE;
               _loc2_ = "";
               _loc3_ = 0;
               while(_loc3_ < this.var_1257.length)
               {
                  _loc5_ = uint(parseInt(this.var_1909.charAt(_loc3_),16));
                  _loc6_ = uint(parseInt(this.var_1257.charAt(_loc3_),16));
                  _loc7_ = uint(_loc5_ ^ _loc6_);
                  _loc2_ += _loc7_.toString(16);
                  _loc3_++;
               }
               (_loc4_ = new Packet(_loc1_)).method_26(this.clientFacebookID);
               _loc4_.method_26(this.clientKongID);
               _loc4_.method_26(this.var_1447);
               _loc4_.method_26(_loc2_);
               _loc4_.method_26(this.var_2853);
               this.serverConn.SendPacket(_loc4_);
               this.var_94.method_71("Authenticating...");
               this.var_1447 = null;
               this.var_1257 = null;
            }
            else if(Boolean(this.var_355) && !this.var_2138)
            {
               if(this.var_2020)
               {
                  this.var_398.Hide();
                  this.var_141.Display(this.var_141.var_250,this.var_141.var_216);
                  this.var_141.method_604();
               }
               else
               {
                  _loc8_ = this.var_355.length;
                  this.var_94.Hide();
                  if(!_loc8_)
                  {
                     this.var_273.Display();
                  }
                  else if(this.var_612 && _loc8_ < this.loginMaxChars)
                  {
                     this.var_273.Display();
                  }
                  else
                  {
                     this.var_341.Display();
                  }
               }
               this.var_2138 = true;
               this.var_612 = false;
            }
            else if(Boolean(this.var_355) && this.var_612)
            {
               this.var_273.Display();
               this.var_612 = false;
            }
            else if(this.var_355 && this.var_1125 && !this.var_2056)
            {
               (_loc9_ = new Packet(LinkUpdater.PKTTYPE_LOGIN_CHARACTER_SELECT)).method_26(this.var_1125);
               this.serverConn.SendPacket(_loc9_);
               this.var_2056 = true;
            }
         }
         this.var_273.RefreshPaperDoll();
         this.var_341.RefreshPaperDoll();
         this.var_141.RefreshPaperDoll();
         this.var_94.method_1983();
         this.var_479.method_1774();
         this.var_398.method_1927();
         this.mUIManager.method_249();
      }
      
      public function method_1716() : void
      {
         this.var_2417 = null;
         this.main.stage.removeEventListener(KeyboardEvent.KEY_DOWN,this.method_930);
         if(Boolean(this.clientKongID) && ExternalInterface.available)
         {
            ExternalInterface.call("JSRecordStat","dblogin",1);
         }
         if(!(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
         {
            this.method_1650();
         }
         this.method_127();
         this.screenLinkBar.Hide();
         this.main.stage.focus = null;
         this.gameState = STATE_NONE;
      }
      
      public function method_282(param1:uint, param2:String, param3:uint, param4:uint, param5:String, param6:String, param7:String, param8:Boolean) : void
      {
         this.gameState = STATE_TRANSFER;
         this.var_1706 = false;
         this.var_2060 = false;
         this.var_1725 = param1;
         this.var_933.Display();
         class_24.method_680();
         this.var_505 = const_1108;
         SoundManager.method_103(Main.const_77,null);
         SoundManager.method_103(Main.const_108,null);
         this.var_2743 = param2;
         this.var_2799 = param3;
         this.var_2584 = param4;
         this.var_2784 = param5;
         this.var_2839 = param6;
         this.var_2773 = param7;
         this.var_2567 = param8;
      }
      
      public function method_1445() : Boolean
      {
         var _loc1_:Boolean = ResourceManager.method_149("Game");
         if(this.var_2052 && _loc1_ && (!this.serverConn || !this.serverConn.method_353()))
         {
            this.var_737.Hide();
            if(!this.var_742.mbVisible)
            {
               class_53.method_524("Disconnect:Transfer");
               this.var_742.Display(true);
            }
            this.mUIManager.method_249();
            return false;
         }
         if(_loc1_)
         {
            if(!this.var_1706)
            {
               this.level.method_1853(this.var_2743,this.var_2799,this.var_2584,this.var_2784,this.var_2839,this.var_2773,this.var_2567);
               this.var_1706 = true;
            }
         }
         this.var_933.method_253();
         this.mUIManager.method_249();
         if(this.var_1706 && !this.var_2060 && this.level.method_1195())
         {
            this.method_1453();
            this.var_2060 = true;
         }
         return true;
      }
      
      public function method_1453() : void
      {
         if(this.serverConn)
         {
            this.serverConn.method_205();
            this.method_730();
         }
         else if(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT)
         {
            this.method_730();
         }
         else
         {
            this.method_429(false);
         }
      }
      
      public function method_1164() : void
      {
         this.var_2052 = false;
         this.method_127();
         this.var_1808.Hide();
         this.var_936.Hide();
         this.gameState = STATE_NONE;
      }
      
      public function method_1448() : void
      {
         this.var_1445.length = 0;
      }
      
      public function method_1070() : void
      {
         var _loc1_:ChatBubble = null;
         for each(_loc1_ in this.var_1445)
         {
            if(_loc1_ && _loc1_.var_19 && _loc1_.var_19.bIAmValid)
            {
               _loc1_.method_901();
            }
         }
      }
      
      public function method_1296() : Boolean
      {
         if(!this.serverConn || !this.serverConn.method_353())
         {
            this.var_737.Hide();
            if(!this.var_742.mbVisible)
            {
               class_53.method_524("Disconnect:Play");
               this.var_742.Display(true);
            }
            this.mUIManager.method_249();
            return false;
         }
         if(!this.method_1337() && !this.method_1333())
         {
            return true;
         }
         this.dayNightManager.method_1547();
         this.level.method_1003();
         this.method_1448();
         this.method_1970();
         if(Boolean(this.clientEnt) && Boolean(this.clientEnt.var_24))
         {
            this.clientEnt.method_1948();
            this.method_1070();
            this.method_1103();
         }
         class_133.method_1956(this);
         this.var_655.method_1976();
         this.var_641.method_253();
         this.var_1717.method_253();
         this.var_737.method_1156();
         this.var_936.method_1865();
         this.screenMap.method_320();
         this.mUIManager.method_249();
         this.var_77.method_1808();
         this.var_171.method_1829();
         if(this.var_107)
         {
            this.var_107.method_1753();
         }
         if(this.var_1601)
         {
            this.method_568();
         }
         return true;
      }
      
      private function method_1103() : void
      {
         var _loc1_:Boolean = this.clientEnt.InActiveCutScene();
         var _loc2_:Boolean = Boolean(this.clientEnt.currRoom) && this.clientEnt.currRoom.var_1925;
         if(this.var_505 == const_394)
         {
            if(_loc2_)
            {
               if(_loc1_)
               {
                  SoundManager.method_103(Main.const_77,null);
                  this.var_505 = const_666;
               }
               else
               {
                  SoundManager.method_103(Main.const_77,"D01_DramaLoop_DreamDragonLair.mp3",0.8);
                  this.var_505 = const_528;
               }
            }
         }
         else if(this.var_505 == const_666)
         {
            if(!_loc1_)
            {
               if(_loc2_)
               {
                  SoundManager.method_103(Main.const_77,"D01_DramaLoop_DreamDragonLair.mp3",0.8);
                  this.var_505 = const_528;
               }
               else
               {
                  this.method_420();
                  this.var_505 = const_394;
               }
            }
         }
         else if(this.var_505 == const_528)
         {
            if(!_loc2_)
            {
               this.method_420();
               this.var_505 = const_394;
            }
         }
      }
      
      private function method_1970() : void
      {
         var _loc1_:int = 0;
         var _loc2_:Entity = null;
         var _loc3_:Boolean = false;
         var _loc5_:class_130 = null;
         var _loc7_:Loot = null;
         var _loc10_:class_72 = null;
         var _loc4_:int = int(this.entities.length);
         _loc1_ = 0;
         while(_loc1_ < _loc4_)
         {
            _loc2_ = this.entities[_loc1_];
            if(_loc2_.var_38)
            {
               _loc3_ = _loc2_.method_1366();
            }
            else
            {
               _loc3_ = _loc2_.method_1770();
            }
            if(!_loc3_)
            {
               _loc2_.DestroyEntity(true);
               this.entities.splice(_loc1_,1);
               _loc4_--;
               _loc1_--;
            }
            _loc1_++;
         }
         var _loc6_:int = int(this.var_371.length);
         _loc1_ = 0;
         while(_loc1_ < _loc6_)
         {
            if(!(_loc5_ = this.var_371[_loc1_]).TickMissile())
            {
               _loc5_.method_770();
               this.var_371.splice(_loc1_,1);
               _loc6_--;
               _loc1_--;
            }
            _loc1_++;
         }
         var _loc8_:int = int(this.var_326.length);
         _loc1_ = 0;
         while(_loc1_ < _loc8_)
         {
            if(!(_loc7_ = this.var_326[_loc1_]).method_1300())
            {
               _loc7_.method_946();
               this.var_326.splice(_loc1_,1);
               _loc8_--;
               _loc1_--;
            }
            _loc1_++;
         }
         var _loc9_:Boolean = class_72.var_970 > const_1226 || class_72.var_1506;
         var _loc11_:int = int(this.var_532.length);
         _loc1_ = 0;
         while(_loc1_ < _loc11_)
         {
            if(!(_loc10_ = this.var_532[_loc1_]).method_1939() || _loc9_ && !_loc10_.var_1344)
            {
               _loc10_.method_963();
               this.var_532.splice(_loc1_,1);
               _loc11_--;
               _loc1_--;
            }
            _loc1_++;
         }
         if(_loc9_)
         {
            this.method_846();
            class_72.var_1506 = false;
         }
      }
      
      public function method_846() : void
      {
         var _loc1_:BitmapData = null;
         for each(_loc1_ in class_72.var_1236)
         {
            _loc1_.dispose();
         }
         class_72.var_1236 = new Array();
         class_72.var_970 = 0;
      }
      
      public function method_530() : void
      {
         var _loc1_:Door = null;
         for each(_loc1_ in this.level.var_264)
         {
            _loc1_.var_2326 = false;
            _loc1_.var_1260 = null;
         }
      }
      
      public function method_2134() : void
      {
         var _loc3_:uint = 0;
         var _loc6_:class_72 = null;
         var _loc7_:class_72 = null;
         var _loc1_:uint = class_24.var_1128;
         var _loc2_:Vector.<String> = class_24.const_779;
         var _loc4_:uint;
         var _loc5_:uint = (_loc4_ = _loc2_.length) >= 12 ? 12 : _loc4_;
         _loc3_ = 0;
         while(_loc3_ < _loc5_)
         {
            _loc6_ = new class_72(this,_loc2_[_loc3_],Camera.SCREEN_WIDTH * 0.5,_loc1_,16724787,0.5,false);
            _loc6_.var_847 = _loc6_.var_1053 = 2000000;
            _loc6_.var_514 = 0;
            this.var_532.push(_loc6_);
            _loc1_ += 20;
            _loc3_++;
         }
         if(_loc5_ != _loc4_)
         {
            _loc7_ = new class_72(this,String(_loc4_ - _loc5_) + " more errors...",Camera.SCREEN_WIDTH * 0.5,_loc1_,16724787,0.5,false);
            _loc7_.var_847 = _loc7_.var_1053 = 2000000;
            _loc7_.var_514 = 0;
            this.var_532.push(_loc7_);
            _loc1_ += 15;
         }
         class_24.method_680();
         class_24.var_1128 = _loc1_;
      }
      
      public function method_1649(param1:int, param2:String, param3:uint, param4:uint, param5:uint, param6:uint, param7:class_118, param8:String, param9:uint, param10:Vector.<class_87>) : void
      {
         var _loc11_:String = null;
         var _loc12_:DisplayObject = null;
         var _loc13_:DisplayObject = null;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         var _loc16_:Point = null;
         var _loc17_:class_37 = null;
         var _loc18_:class_37 = null;
         var _loc19_:class_37 = null;
         var _loc20_:String = null;
         var _loc21_:Boolean = false;
         var _loc22_:Door = null;
         var _loc23_:Door = null;
         var _loc24_:Door = null;
         var _loc25_:a_Cue = null;
         var _loc26_:Number = NaN;
         var _loc27_:Number = NaN;
         var _loc28_:Number = NaN;
         var _loc29_:Number = NaN;
         var _loc30_:Number = NaN;
         var _loc31_:Room = null;
         var _loc32_:a_Cue = null;
         var _loc33_:Point = null;
         var _loc34_:Number = NaN;
         var _loc35_:Number = NaN;
         var _loc36_:Number = NaN;
         var _loc37_:Point = null;
         var _loc38_:Point = null;
         var _loc39_:Door = null;
         this.gameState = STATE_PLAY;
         this.clientEntID = param1;
         this.clientEntName = param2;
         this.mBonusLevels = param9;
         if(this.var_193)
         {
            if(this.var_193.bitmapData)
            {
               this.var_193.bitmapData.dispose();
            }
            this.var_193.bitmapData = null;
            if(this.var_193.parent)
            {
               this.var_193.parent.removeChild(this.var_193);
            }
            this.var_193 = null;
         }
         this.mbTransferMode = false;
         this.mTimeThisTick = getTimer();
         this.main.var_860 = 1000;
         this.main.var_903 = this.mTimeThisTick + this.main.var_860;
         this.var_936.var_787 = 0;
         this.var_655.method_1799();
         this.var_406 = new Vector.<int>();
         this.var_1495 = new Dictionary();
         this.var_532 = new Vector.<class_72>();
         this.var_1445 = new Vector.<ChatBubble>();
         this.var_326 = new Vector.<Loot>();
         this.entities = new Vector.<Entity>();
         this.var_371 = new Vector.<class_130>();
         this.var_1810 = new Dictionary();
         this.screenHudTooltip.Display();
         this.screenChat.Display();
         this.screenHud.Display();
         this.screenQuestTracker.Display();
         this.screenHudTop.Display();
         this.var_1828.Display();
         if(_loc11_ = Level.method_73(this.level.internalName))
         {
            this.screenChat.ReadUnsafeStatusText("Welcome to " + _loc11_ + "!");
         }
         if(this.edgeLayer)
         {
            if(_loc12_ = this.edgeLayer.getChildByName("am_EdgeFull") as DisplayObject)
            {
               _loc12_.visible = false;
            }
            if(_loc13_ = this.edgeLayer.getChildByName("am_EdgeNarrow") as DisplayObject)
            {
               _loc13_.visible = true;
            }
         }
         if(!(DevSettings.DEVFLAG_NO_PLAYERENT & DevSettings.flags))
         {
            _loc14_ = 0.01;
            _loc15_ = 0.01;
            if(Boolean(this.level.var_1269) && Boolean(DevSettings.flags & DevSettings.DEVFLAG_DEVSPAWNENABLED))
            {
               _loc14_ = Number(this.level.var_1269.x);
               _loc15_ = Number(this.level.var_1269.y);
            }
            else if(this.level.var_239)
            {
               _loc14_ = Number(this.level.var_239.x);
               _loc15_ = Number(this.level.var_239.y);
            }
            if(this.targetDoor)
            {
               for each(_loc22_ in this.level.var_264)
               {
                  if(_loc22_.doorID == this.targetDoor)
                  {
                     _loc14_ = _loc22_.posX;
                     _loc15_ = _loc22_.posY;
                     break;
                  }
               }
            }
            else if(this.var_1025)
            {
               _loc14_ = this.var_1025.x;
               _loc15_ = this.var_1025.y - class_122.PRECISION_FIX_OFFSET;
            }
            this.targetDoor = 0;
            this.var_1025 = null;
            _loc16_ = new Point();
            if(_loc17_ = this.collMan.getFloorCollision(0,_loc14_,_loc15_ - 59,new Point(0,160),_loc16_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0))
            {
               _loc14_ = _loc16_.x;
               _loc15_ = _loc16_.y - Entity.PULLBACK_DIST;
            }
            _loc18_ = this.collMan.getFloorCollision(0,_loc14_,_loc15_,new Point(-20,0),_loc16_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0);
            _loc19_ = this.collMan.getFloorCollision(0,_loc14_,_loc15_,new Point(20,0),_loc16_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0);
            if(_loc18_ && _loc18_.room && _loc18_ == _loc19_)
            {
               _loc23_ = null;
               for each(_loc24_ in this.level.var_264)
               {
                  _loc26_ = _loc24_.var_443.x + _loc24_.posX;
                  _loc27_ = _loc24_.var_443.y + _loc24_.posY;
                  _loc28_ = _loc26_ + _loc24_.var_443.width;
                  _loc29_ = _loc27_ + _loc24_.var_443.height;
                  if(_loc14_ >= _loc26_ - Door.const_62 && _loc14_ <= _loc28_ + Door.const_62 && _loc15_ >= _loc27_ - Door.const_62 && _loc15_ <= _loc29_ + Door.const_62)
                  {
                     _loc23_ = _loc24_;
                  }
               }
               _loc25_ = null;
               if(!_loc23_)
               {
                  _loc31_ = _loc18_.room;
                  for each(_loc32_ in _loc31_.var_460)
                  {
                     _loc33_ = this.method_234(_loc32_);
                     _loc34_ = _loc14_ - _loc33_.x;
                     _loc35_ = _loc15_ - _loc33_.y;
                     _loc36_ = _loc34_ * _loc34_ + _loc35_ * _loc35_;
                     if(!_loc25_ || _loc36_ < _loc30_)
                     {
                        _loc25_ = _loc32_;
                        _loc30_ = _loc36_;
                     }
                  }
               }
               if(_loc23_)
               {
                  _loc14_ = _loc23_.posX;
                  _loc15_ = _loc23_.posY;
               }
               else if(_loc25_)
               {
                  _loc37_ = this.method_234(_loc25_);
                  _loc38_ = new Point(_loc37_.x,_loc37_.y);
                  _loc31_.method_838(_loc37_,_loc38_,true);
                  _loc14_ = _loc38_.x;
                  _loc15_ = _loc38_.y;
               }
               else if(this.level.var_239)
               {
                  _loc14_ = Number(this.level.var_239.x);
                  _loc15_ = Number(this.level.var_239.y);
               }
               else if(this.level.var_264.length)
               {
                  _loc14_ = (_loc39_ = this.level.var_264[0]).posX;
                  _loc15_ = _loc39_.posY;
               }
               else
               {
                  _loc14_ = 0.01;
                  _loc15_ = 0.01;
               }
               if(_loc17_ = this.collMan.getFloorCollision(0,_loc14_,_loc15_ - 59,new Point(0,160),_loc16_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0))
               {
                  _loc14_ = _loc16_.x;
                  _loc15_ = _loc16_.y - Entity.PULLBACK_DIST;
               }
            }
            this.clientEnt = new Entity(this,param2,null,_loc14_,_loc15_,Entity.LOCAL | Entity.PLAYER,Entity.GOODGUY,this.clientEntID,param3,0,null,param7,param8,param10,null,null);
            this.clientEnt.var_859 = param4;
            this.method_764(param4);
            this.clientEnt.currGold = param5;
            this.clientEnt.currGems = param6;
            this.clientEnt.SetCurrSurface(_loc17_);
            this.screenHudTopRight.Display(this.clientEnt);
            this.entities.push(this.clientEnt);
            _loc21_ = (_loc20_ = String(!!this.level.internalName ? Level.method_182(this.level.internalName) : null)) == "ShazariDesert" || _loc20_ == "JadeCity" || _loc20_ == "ShazariDesertHard" || _loc20_ == "JadeCityHard";
            if(_loc20_ != "Global" && this.mbSleepingLands != _loc21_)
            {
               this.screenMap.method_119();
               this.screenMap.method_448();
               this.mbSleepingLands = _loc21_;
               this.screenMap = new class_119(this);
            }
            this.screenMap.method_1807();
         }
         this.dayNightManager.method_576();
         this.method_420();
         this.var_505 = const_394;
         if(this.clientEnt)
         {
            this.clientEnt.gfx.m_TheDO.visible = true;
            this.clientEnt.var_471.length = 0;
            this.clientEnt.var_24.var_418.var_556 = true;
            this.main.stage.addEventListener(KeyboardEvent.KEY_DOWN,this.method_702);
            this.main.stage.addEventListener(KeyboardEvent.KEY_UP,this.method_885);
         }
      }
      
      public function method_447() : void
      {
         var _loc1_:Entity = null;
         var _loc2_:class_130 = null;
         var _loc3_:Loot = null;
         var _loc4_:class_72 = null;
         if(Boolean(this.clientEnt) && Boolean(this.clientEnt.combatState))
         {
            this.var_2080 = this.clientEnt.combatState.var_270 != null;
            this.var_2022 = this.clientEnt.combatState.var_724 != null;
         }
         this.dayNightManager.method_747();
         this.gameState = STATE_NONE;
         this.clientEntID = 0;
         if(this.clientEnt)
         {
            this.main.stage.removeEventListener(KeyboardEvent.KEY_DOWN,this.method_702);
            this.main.stage.removeEventListener(KeyboardEvent.KEY_UP,this.method_885);
         }
         this.clientEnt = null;
         for each(_loc1_ in this.entities)
         {
            _loc1_.DestroyEntity(false);
         }
         this.entities = null;
         for each(_loc2_ in this.var_371)
         {
            _loc2_.method_770();
         }
         this.var_371 = null;
         this.var_1810 = null;
         SoundManager.method_103(Main.const_108,null);
         if(this.serverConn)
         {
            this.serverConn.method_205();
            this.serverConn = null;
         }
         for each(_loc3_ in this.var_326)
         {
            _loc3_.method_946();
         }
         this.var_326 = null;
         for each(_loc4_ in this.var_532)
         {
            _loc4_.method_963();
         }
         this.var_532 = null;
         this.var_1445 = null;
         this.method_846();
         this.var_1495 = null;
         this.level.method_905();
         this.level = new Level(this);
         this.var_1280 = new Dictionary();
         this.collMan.method_784();
         this.collMan = new CollisionManager(this);
         this.var_77.method_929();
         this.var_171.method_954();
         this.dayNightManager.var_1078 = DayNightManager.const_518;
         SuperAnimData.method_1109(null);
      }
      
      public function method_1737(param1:DisplayObjectContainer) : void
      {
         var _loc2_:int = 0;
         var _loc3_:DisplayObject = null;
         var _loc4_:String = null;
         var _loc6_:a_Cue = null;
         _loc2_ = 0;
         while(_loc2_ < param1.numChildren)
         {
            _loc3_ = param1.getChildAt(_loc2_);
            _loc4_ = getQualifiedClassName(_loc3_);
            if(_loc3_ is a_Cue)
            {
               _loc6_ = _loc3_ as a_Cue;
            }
            if(_loc3_ is DisplayObjectContainer)
            {
               this.method_1737(_loc3_ as DisplayObjectContainer);
            }
            _loc2_++;
         }
      }
      
      public function method_950(param1:String) : void
      {
         if(!(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
         {
            this.var_94.method_71(param1,false);
            this.main.addChild(this.var_94.var_88);
            this.var_94.var_88 = null;
         }
      }
      
      private function method_1218() : void
      {
         if(this.mTimeThisTick - this.var_2461 < 1000)
         {
            return;
         }
         if(ExternalInterface.call("CheckInitFB"))
         {
            ExternalInterface.call("JSGetLikeStatus");
            this.var_2092 = false;
         }
         this.var_2461 = this.mTimeThisTick;
      }
      
      public function GetScreenShotHTML() : String
      {
         var _loc1_:Stage = null;
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:BitmapData = null;
         var _loc5_:ByteArray = null;
         var _loc6_:String = null;
         _loc1_ = this.main.stage;
         _loc2_ = _loc1_.stageWidth;
         _loc3_ = _loc1_.stageHeight;
         if(!_loc2_ || !_loc2_)
         {
            return "";
         }
         (_loc4_ = new BitmapData(_loc2_ * const_403,_loc3_ * const_403,false,4737365)).drawWithQuality(_loc1_,const_908,null,null,null,false,StageQuality.HIGH);
         _loc4_.applyFilter(_loc4_,_loc4_.rect,new Point(0,0),const_1021);
         _loc5_ = class_113.method_1997(_loc4_);
         _loc6_ = Crypto.method_1413(_loc5_);
         return "data:image/png;base64," + _loc6_;
      }
      
      public function SWFInviteFriendCallback(param1:Object) : void
      {
      }
      
      public function SWFFinishPurchaseCallback(param1:String) : void
      {
         this.screenBuyIdols.Hide();
      }
      
      public function SWFFinishEarnCallback(param1:String) : void
      {
         this.screenBuyIdols.Hide();
      }
      
      public function SWFGetLikeStatusCallback(param1:Object) : void
      {
         if(!param1 || !param1.data)
         {
            return;
         }
         this.mbPageIsLiked = param1.data.length > 0;
         this.screenLinkBar.Refresh();
      }
      
      private function method_1666() : void
      {
         var _loc1_:class_32 = null;
         var _loc2_:SuperAnimInstance = null;
         var _loc3_:SuperAnimInstance = null;
         var _loc4_:class_33 = null;
         for each(_loc1_ in this.mUIManager.mActiveScreens)
         {
            for each(_loc2_ in _loc1_.var_1024)
            {
               if(!_loc2_.m_bFinished)
               {
                  _loc2_.method_105();
               }
            }
            for each(_loc3_ in _loc1_.var_819)
            {
               if(!_loc3_.m_bFinished)
               {
                  _loc3_.method_105();
               }
            }
            for each(_loc4_ in _loc1_.var_321)
            {
               if(_loc4_.var_271)
               {
                  _loc4_.method_298();
               }
            }
            if(_loc1_.mWindow.var_1193)
            {
               _loc1_.mWindow.method_298();
            }
         }
         this.screenHud.method_1505();
         this.screenDyeGear.Refresh();
      }
      
      public function method_1923() : void
      {
         this.var_171.method_1049();
         class_72.var_1506 = true;
         this.screenMap.method_593();
         this.screenMap.Refresh();
         this.var_1419 = true;
         SuperAnimData.method_1563();
         this.main.var_2102 = false;
         this.var_1778 = false;
         class_133.method_956(this,this.groupmates,false);
         this.screenLinkBar.Refresh();
         this.method_1666();
         this.level.method_1316();
         this.screenArmory.Refresh();
         this.screenBarn.Refresh();
      }
      
      public function method_1852() : void
      {
         var _loc1_:String = null;
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         var _loc4_:String = null;
         var _loc5_:String = null;
         var _loc6_:String = null;
         var _loc7_:Boolean = false;
         if(DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT)
         {
            _loc1_ = String(this.level.levelName);
            _loc2_ = uint(this.level.mapLevel);
            _loc3_ = uint(this.level.baseLevel);
            _loc4_ = String(this.level.internalName);
            _loc5_ = String(this.level.momentParamsString);
            _loc6_ = String(this.level.alterParamsString);
            _loc7_ = Boolean(this.level.bInstanced);
            this.method_447();
            this.method_282(this.var_1725,_loc1_,_loc2_,_loc3_,_loc4_,_loc5_,_loc6_,_loc7_);
         }
         else
         {
            this.method_447();
            this.method_127();
            this.var_933.Display();
            this.method_429(false);
         }
         this.var_2115 = false;
      }
      
      public function method_1062() : void
      {
         var _loc1_:Boolean = false;
         _loc1_ = this.gameState == STATE_PLAY && !(DevSettings.flags & DevSettings.const_938);
         if(!_loc1_ || Main.var_1468 > Main.var_1954)
         {
            this.var_737.var_2153 = false;
         }
         else if(_loc1_)
         {
            this.var_737.var_2153 = true;
            if(Boolean(this.clientEnt) && Boolean(this.clientEnt.var_24))
            {
               this.var_406.length = 0;
               this.clientEnt.var_24.method_727();
               this.clientEnt.var_24.method_725();
               this.clientEnt.var_24.method_674();
            }
         }
      }
      
      public function method_1947() : void
      {
         if(!this.main.var_374)
         {
            this.main.var_374 = this.main.var_147;
            this.main.var_147 = new Bitmap(null,PixelSnapping.ALWAYS,false);
            this.main.var_147.name = "the_FinalCanvas";
            this.main.var_147.bitmapData = new BitmapData(Math.ceil(Camera.SCREEN_WIDTH * this.main.overallScale),Math.ceil(Camera.PLAY_SCREEN_HEIGHT * this.main.overallScale),false);
            this.main.var_147.bitmapData.fillRect(this.main.var_147.bitmapData.rect,4737365);
            this.main.addChildAt(this.main.var_147,this.main.getChildIndex(this.main.var_374) + 1);
            this.var_1778 = false;
         }
         if(this.mTimeThisTick < this.main.var_903)
         {
            this.main.var_147.alpha = (this.main.var_860 - (this.main.var_903 - this.mTimeThisTick)) / this.main.var_860;
         }
         else
         {
            this.main.removeChild(this.main.var_374);
            if(this.main.var_374.bitmapData)
            {
               this.main.var_374.bitmapData.dispose();
            }
            this.main.var_374 = null;
            this.main.var_903 = 0;
            this.main.var_860 = 0;
            this.main.var_147.alpha = 1;
         }
      }
      
      public function method_1636() : Boolean
      {
         try
         {
            return this.method_789();
         }
         catch(error:Error)
         {
            method_950("Your game seems to have crashed.\n\nPlease hit refresh to fix the problem.");
            method_297(error);
            class_53.method_524("Crash:" + (!!gameState ? gameState : "Unknown"));
            return false;
         }
      }
      
      public function method_1325() : void
      {
         var _loc1_:int = 0;
         var _loc2_:SuperAnimInstance = null;
         _loc1_ = int(this.var_961.length - 1);
         while(_loc1_ >= 0)
         {
            _loc2_ = this.var_961[_loc1_];
            if(_loc2_.m_bFinished || _loc2_.method_105())
            {
               _loc2_.DestroySuperAnimInstance();
               this.var_961.splice(_loc1_,1);
            }
            _loc1_--;
         }
         if(!(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
         {
            SuperAnimData.method_1675(this.mTimeThisTick);
         }
         SuperAnimData.var_1220 = false;
      }
      
      public function method_789() : Boolean
      {
         var _loc1_:Boolean = false;
         this.method_1938();
         if(this.var_2092)
         {
            this.method_1218();
         }
         if(this.main.var_2102)
         {
            this.method_1923();
         }
         if(this.linkUpdater)
         {
            this.linkUpdater.method_1750();
         }
         if(this.var_2115)
         {
            this.method_1852();
         }
         _loc1_ = true;
         if(this.gameState == STATE_TRANSFER)
         {
            _loc1_ = this.method_1445();
         }
         else if(this.gameState == STATE_LOGIN)
         {
            this.method_1312();
         }
         else if(this.gameState == STATE_PLAY)
         {
            _loc1_ = this.method_1296();
         }
         if(!_loc1_)
         {
            return true;
         }
         if(this.tooltip)
         {
            this.tooltip.method_1543();
         }
         if(this.var_137)
         {
            this.var_137.method_2003();
         }
         if(this.serverConn)
         {
            this.serverConn.method_1935();
         }
         this.method_1062();
         this.method_1325();
         if(this.linkUpdater)
         {
            this.linkUpdater.method_1926();
         }
         if(!(DevSettings.flags & DevSettings.DEVFLAG_NO_GRAPHICS))
         {
            if(this.main.var_903)
            {
               this.method_1947();
            }
            this.method_1946();
         }
         return true;
      }
      
      public function method_1946() : void
      {
         var _loc1_:Boolean = false;
         var _loc2_:Number = NaN;
         var _loc3_:Sprite = null;
         var _loc4_:BitmapData = null;
         var _loc5_:Matrix = null;
         var _loc6_:Matrix = null;
         var _loc7_:int = 0;
         var _loc8_:int = 0;
         var _loc9_:Sprite = null;
         var _loc10_:int = 0;
         var _loc11_:int = 0;
         var _loc12_:Sprite = null;
         var _loc13_:Matrix = null;
         var _loc14_:Sprite = null;
         var _loc16_:Matrix = null;
         _loc1_ = Boolean(this.screenMap.mbVisible) || Boolean(this.screenForge.mbVisible);
         if(this.gameState == STATE_PLAY && (!_loc1_ || !this.var_1778))
         {
            this.var_1778 = true;
            _loc4_ = this.main.var_147.bitmapData;
            _loc5_ = new Matrix(this.main.overallScale,0,0,this.main.overallScale);
            _loc8_ = this.var_1040.numChildren;
            _loc7_ = 0;
            while(_loc7_ < _loc8_)
            {
               _loc3_ = this.var_1040.getChildAt(_loc7_) as Sprite;
               if(_loc3_.visible)
               {
                  (_loc6_ = _loc3_.transform.matrix).concat(_loc5_);
                  if(_loc3_ == this.levelLayer)
                  {
                     _loc11_ = (_loc9_ = _loc3_).numChildren;
                     _loc10_ = 0;
                     while(_loc10_ < _loc11_)
                     {
                        if((_loc12_ = _loc9_.getChildAt(_loc10_) as Sprite).visible)
                        {
                           (_loc13_ = _loc12_.transform.matrix).concat(_loc6_);
                           if(_loc12_ == this.var_107.var_343)
                           {
                              _loc14_ = _loc12_;
                              (_loc16_ = new Matrix()).tx = (_loc9_.x + _loc14_.x) * this.main.overallScale;
                              _loc16_.ty = (_loc9_.y + _loc14_.y) * this.main.overallScale;
                              _loc4_.drawWithQuality(_loc14_,_loc16_,null,null,null,false,StageQuality.HIGH);
                           }
                           else if(_loc12_ == this.playerEntLayer)
                           {
                              _loc4_.drawWithQuality(_loc12_,_loc13_,null,null,null,false,StageQuality.HIGH);
                           }
                           else
                           {
                              _loc4_.drawWithQuality(_loc12_,_loc13_,null,null,null,false,StageQuality.HIGH);
                           }
                        }
                        _loc10_++;
                     }
                  }
                  else
                  {
                     _loc4_.drawWithQuality(_loc3_,_loc6_,null,null,null,false,StageQuality.HIGH);
                  }
               }
               _loc7_++;
            }
         }
         _loc2_ = Number(this.main.overallScale);
         this.var_89.scaleX = _loc2_;
         this.var_89.scaleY = _loc2_;
         this.edgeLayer.scaleX = _loc2_;
         this.edgeLayer.scaleY = _loc2_;
         this.var_245.scaleX = _loc2_;
         this.var_245.scaleY = _loc2_;
         if(this.main.var_147.smoothing)
         {
            this.main.var_147.smoothing = false;
         }
         this.main.stage.invalidate();
      }
      
      public function RenderGear(param1:String, param2:GearType, param3:Number = 1, param4:Entity = null, param5:class_21 = null, param6:class_21 = null, param7:Boolean = false) : SuperAnimInstance
      {
         var _loc8_:Entity = null;
         var _loc9_:EntType = null;
         var _loc10_:EntTypeGear = null;
         var _loc11_:uint = 0;
         var _loc12_:class_42 = null;
         var _loc13_:String = null;
         var _loc14_:GfxType = null;
         var _loc15_:SuperAnimInstance = null;
         _loc10_ = (_loc9_ = (_loc8_ = !!param4 ? param4 : this.clientEnt).entType).equippedGear[_loc11_];
         _loc11_ = uint(EntType.method_87(param2.type));
         _loc12_ = this.mOwnedGear[param2.gearID];
         if(!param5 && Boolean(_loc12_))
         {
            param5 = _loc12_.var_295;
         }
         if(!param5 && Boolean(_loc10_))
         {
            param5 = class_14.var_194[_loc10_.var_644];
         }
         if(!param6 && Boolean(_loc12_))
         {
            param6 = _loc12_.var_307;
         }
         if(!param6 && Boolean(_loc10_))
         {
            param6 = class_14.var_194[_loc10_.var_705];
         }
         _loc13_ = param1 + param2.type;
         _loc14_ = param2.method_1887(param1,param3,_loc8_,param5,param6);
         (_loc15_ = new SuperAnimInstance(this,_loc14_,true,!param7)).m_Seq.method_34(Seq.C_USEPOWER,_loc13_,true);
         _loc15_.method_105();
         return _loc15_;
      }
      
      public function method_2131(param1:Sprite, param2:Number, param3:Number) : void
      {
         var _loc4_:Matrix = null;
         var _loc5_:int = 0;
         var _loc6_:Sprite = null;
         _loc4_ = new Matrix();
         _loc5_ = 0;
         while(_loc5_ < param1.numChildren)
         {
            _loc6_ = param1.getChildAt(_loc5_) as Sprite;
            _loc4_.tx = int((param2 + _loc6_.x) * this.main.overallScale);
            _loc4_.ty = int((param3 + _loc6_.y) * this.main.overallScale);
            this.main.var_147.bitmapData.drawWithQuality(_loc6_,_loc4_,null,null,null,false,StageQuality.HIGH);
            _loc5_++;
         }
      }
      
      public function method_1412(param1:DisplayObjectContainer) : void
      {
         var _loc2_:MovieClip = null;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         if(!param1)
         {
            return;
         }
         if(param1.mouseChildren)
         {
         }
         if(param1.mouseEnabled)
         {
         }
         _loc2_ = param1 as MovieClip;
         if(Boolean(_loc2_) && _loc2_.buttonMode)
         {
         }
         if(Boolean(_loc2_) && this.method_1069(_loc2_))
         {
         }
         _loc3_ = !!param1 ? uint(param1.numChildren) : 0;
         _loc4_ = 0;
         while(_loc4_ < _loc3_)
         {
            this.method_1412(param1.getChildAt(_loc4_) as DisplayObjectContainer);
            _loc4_++;
         }
      }
      
      private function method_1069(param1:MovieClip) : Boolean
      {
         var _loc2_:* = false;
         if(param1.db_LastFrame == undefined)
         {
            param1.db_LastFrame = param1.currentFrame;
         }
         _loc2_ = param1.db_LastFrame != param1.currentFrame;
         param1.db_LastFrame = param1.currentFrame;
         return _loc2_;
      }
      
      public function method_297(param1:Error) : void
      {
         var _loc2_:Packet = null;
         if(this.serverConn)
         {
            _loc2_ = new Packet(LinkUpdater.PKTTYPE_CLIENT_ERROR);
            _loc2_.method_26(param1.getStackTrace());
            this.serverConn.SendPacket(_loc2_);
         }
      }
      
      public function method_1040() : void
      {
         this.var_1040 = MathUtil.method_69();
         this.levelLayer = MathUtil.method_69();
         this.var_773 = MathUtil.method_69();
         this.playerEntLayer = MathUtil.method_69();
         this.var_272 = MathUtil.method_69();
         this.var_781 = MathUtil.method_69();
         this.var_89 = MathUtil.method_69();
         this.edgeLayer = MathUtil.method_69();
         this.var_245 = MathUtil.method_69();
         this.levelLayer.addChild(this.var_77.var_589);
         if(this.var_107)
         {
            this.levelLayer.addChild(this.var_107.var_343);
         }
         this.levelLayer.addChild(this.var_77.var_572);
         this.levelLayer.addChild(this.var_773);
         this.levelLayer.addChild(this.playerEntLayer);
         this.levelLayer.addChild(this.var_77.var_592);
         this.levelLayer.addChild(this.var_272);
         this.levelLayer.addChild(this.var_781);
         this.var_1040.addChild(this.var_77.var_829);
         this.var_1040.addChild(this.levelLayer);
         this.var_1040.addChild(this.var_77.var_891);
         this.main.addChild(this.edgeLayer);
         this.main.addChild(this.var_89);
         this.main.addChild(this.var_245);
         this.var_89.mouseChildren = true;
         this.var_245.mouseChildren = true;
         if(DevSettings.flags & DevSettings.DEVFLAG_NO_GRAPHICS)
         {
            this.var_89.visible = false;
            this.edgeLayer.visible = false;
            this.var_245.visible = false;
         }
      }
      
      public function method_1471() : void
      {
         if(Boolean(this.var_89) && Boolean(this.var_89.parent))
         {
            this.var_89.parent.removeChild(this.var_89);
         }
         this.var_89 = null;
         if(Boolean(this.edgeLayer) && Boolean(this.edgeLayer.parent))
         {
            this.edgeLayer.parent.removeChild(this.edgeLayer);
         }
         this.edgeLayer = null;
         if(Boolean(this.var_245) && Boolean(this.var_245.parent))
         {
            this.var_245.parent.removeChild(this.var_245);
         }
         this.var_245 = null;
         if(Boolean(this.var_272) && Boolean(this.var_272.parent))
         {
            this.var_272.parent.removeChild(this.var_272);
         }
         this.var_272 = null;
         if(Boolean(this.var_781) && Boolean(this.var_781.parent))
         {
            this.var_781.parent.removeChild(this.var_781);
         }
         this.var_781 = null;
         if(Boolean(this.playerEntLayer) && Boolean(this.playerEntLayer.parent))
         {
            this.playerEntLayer.parent.removeChild(this.playerEntLayer);
         }
         this.playerEntLayer = null;
         if(Boolean(this.var_773) && Boolean(this.var_773.parent))
         {
            this.var_773.parent.removeChild(this.var_773);
         }
         this.var_773 = null;
         if(Boolean(this.levelLayer) && Boolean(this.levelLayer.parent))
         {
            this.levelLayer.parent.removeChild(this.levelLayer);
         }
         this.levelLayer = null;
         this.var_1040 = null;
      }
      
      public function method_111(param1:uint) : Room
      {
         var _loc2_:Room = null;
         for each(_loc2_ in this.level.var_299)
         {
            if(_loc2_.var_113 == param1)
            {
               return _loc2_;
            }
         }
         return null;
      }
      
      public function method_2090(param1:String, param2:Boolean) : void
      {
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         _loc3_ = getTimer();
         if(param2)
         {
            if(_loc5_ = Number(this.var_1918[param1]))
            {
               _loc4_ = _loc3_ - this.var_1918[param1];
            }
         }
         this.var_1918[param1] = _loc3_;
      }
      
      public function method_195(param1:String = null) : void
      {
         var _loc2_:a_Cue = null;
         var _loc3_:uint = 0;
         var _loc4_:Entity = null;
         var _loc5_:String = null;
         var _loc6_:class_35 = null;
         for each(_loc4_ in this.entities)
         {
            _loc2_ = _loc4_.cue;
            if(_loc2_)
            {
               if(_loc5_ = _loc2_.characterName)
               {
                  if(!(Boolean(param1) && _loc5_ != param1))
                  {
                     if(_loc6_ = class_14.var_999[_loc5_])
                     {
                        _loc3_ = this.method_793(_loc6_);
                        _loc4_.method_397(_loc3_);
                     }
                  }
               }
            }
         }
      }
      
      public function method_1787(param1:uint) : void
      {
         var _loc2_:class_13 = null;
         var _loc3_:Mission = null;
         _loc2_ = class_14.var_238[param1];
         if(!_loc2_)
         {
            return;
         }
         _loc3_ = this.mMissionInfoList[param1];
         if(_loc3_)
         {
            _loc3_.var_145 = Mission.const_58;
         }
         else
         {
            _loc3_ = new Mission(param1,Mission.const_58,0);
            this.mMissionInfoList[param1] = _loc3_;
         }
         if(_loc2_.var_160)
         {
            this.method_195(_loc2_.var_160);
         }
         if(Boolean(_loc2_.var_319) && _loc2_.var_319 != _loc2_.var_160)
         {
            this.method_195(_loc2_.var_319);
         }
         this.method_263(param1);
         this.screenMap.Refresh();
         this.screenQuestTracker.Refresh();
         if(_loc2_.var_2309)
         {
            this.screenChat.ReceiveChat(this.clientEntID,_loc2_.var_2309,false);
         }
      }
      
      public function method_1472(param1:uint, param2:uint, param3:uint) : void
      {
         var _loc4_:class_13 = null;
         var _loc5_:Mission = null;
         var _loc6_:MovieClip = null;
         var _loc7_:class_72 = null;
         if(!(_loc4_ = class_14.var_238[param1]))
         {
            return;
         }
         if(_loc5_ = this.mMissionInfoList[param1])
         {
            _loc5_.var_145 = Mission.const_72;
         }
         else
         {
            _loc5_ = new Mission(param1,Mission.const_72,0);
            this.mMissionInfoList[param1] = _loc5_;
         }
         _loc5_.var_588 = param2;
         _loc5_.var_1745 = param3;
         this.method_195();
         this.method_263(param1);
         this.method_530();
         this.SelectMissionToTrack();
         this.screenMap.Refresh();
         if(_loc4_.var_2136)
         {
            this.screenChat.ReceiveChat(this.clientEntID,_loc4_.var_2136,false);
         }
         if(_loc4_.var_1775)
         {
            if(SoundConfig.var_1728)
            {
               SoundManager.Play(SoundConfig.var_1728);
            }
            _loc6_ = class_4.method_16("a_AchieveFloater_Silver");
            MathUtil.method_2(_loc6_.am_AchieveName,_loc4_.displayName);
            (_loc7_ = new class_72(this,"",Camera.SCREEN_WIDTH * 0.5,220,0,1,false,_loc6_,null)).var_514 = 0;
            _loc7_.var_847 = 3500;
            _loc7_.var_1053 = 5000;
            this.var_532.push(_loc7_);
         }
         else
         {
            this.var_2059.Display(_loc4_.missionID);
            SoundManager.Play("UI_CompleteQuest");
         }
      }
      
      public function method_1873(param1:uint, param2:uint) : void
      {
         var _loc3_:class_13 = null;
         var _loc4_:Mission = null;
         _loc3_ = class_14.var_238[param1];
         if(!_loc3_)
         {
            return;
         }
         if(!(_loc4_ = this.mMissionInfoList[param1]))
         {
            return;
         }
         _loc4_.currCount += param2;
         this.screenMap.Refresh();
         this.screenQuestTracker.Refresh();
         if(_loc3_.var_2319)
         {
            this.var_2093.Display(_loc3_.missionID);
         }
      }
      
      public function method_1380(param1:uint, param2:Boolean) : void
      {
         var _loc3_:class_13 = null;
         var _loc4_:uint = 0;
         var _loc5_:Mission = null;
         var _loc6_:Boolean = false;
         _loc3_ = class_14.var_238[param1];
         if(!_loc3_)
         {
            return;
         }
         _loc4_ = param2 ? Mission.const_213 : Mission.const_58;
         _loc5_ = new Mission(param1,_loc4_,0);
         this.mMissionInfoList[param1] = _loc5_;
         if(_loc3_.var_160)
         {
            this.method_195(_loc3_.var_160);
         }
         if(Boolean(_loc3_.var_319) && _loc3_.var_319 != _loc3_.var_160)
         {
            this.method_195(_loc3_.var_319);
         }
         this.method_263(param1);
         this.method_530();
         _loc6_ = Boolean(this.mTrackedMission) && Boolean(this.mMissionInfoList[this.mTrackedMission.missionID]);
         if(!this.mTrackedMission)
         {
            this.SelectMissionToTrack(_loc3_);
         }
         else if(_loc6_ && _loc3_.var_231 > this.mTrackedMission.var_231)
         {
            this.SelectMissionToTrack(_loc3_);
         }
         else if(!_loc6_ && _loc3_.var_231 >= this.mTrackedMission.var_231)
         {
            this.SelectMissionToTrack(_loc3_);
         }
         else if(_loc3_ == this.mTrackedMission)
         {
            this.screenQuestTracker.Refresh();
         }
         this.screenMap.Refresh();
         if(_loc3_.var_2425)
         {
            this.screenChat.ReceiveChat(this.clientEntID,_loc3_.var_2425,false);
         }
         if(SoundConfig.var_1948)
         {
            SoundManager.Play(SoundConfig.var_1948,0.7);
         }
         if(_loc3_.missionID != class_13.const_118)
         {
            this.var_2159.Display(param1);
         }
         else
         {
            this.screenHudTop.Refresh();
            this.var_2231.Display();
            SoundManager.Play("UI_UnlockHouse");
         }
      }
      
      public function method_1916(param1:Entity, param2:a_Cue, param3:String) : void
      {
         var _loc4_:String = null;
         var _loc5_:class_35 = null;
         _loc4_ = null;
         if(_loc5_ = class_14.var_999[param3])
         {
            _loc4_ = this.method_1662(_loc5_);
         }
         else if(param2.sayOnInteract)
         {
            _loc4_ = param2.sayOnInteract;
         }
         if(_loc4_)
         {
            if(param1.var_1264 && this.mTimeThisTick < param1.var_1395)
            {
               param1.StartSkit("",true,this.clientEnt);
            }
            else
            {
               param1.StartSkit(_loc4_,true,this.clientEnt);
            }
         }
      }
      
      public function method_1662(param1:class_35) : String
      {
         var _loc2_:Mission = null;
         var _loc3_:class_13 = null;
         var _loc4_:class_13 = null;
         var _loc5_:class_13 = null;
         var _loc6_:class_13 = null;
         for each(_loc3_ in param1.var_1701)
         {
            _loc2_ = this.mMissionInfoList[_loc3_.missionID];
            if(Boolean(_loc2_) && _loc2_.var_145 == Mission.const_58)
            {
               return _loc3_.method_224(class_13.const_802);
            }
         }
         _loc4_ = null;
         _loc5_ = null;
         _loc6_ = null;
         for each(_loc3_ in param1.var_1886)
         {
            _loc2_ = this.mMissionInfoList[_loc3_.missionID];
            if(_loc2_)
            {
               if(_loc2_.var_145 != Mission.const_72)
               {
                  return _loc3_.method_224(class_13.const_619);
               }
               _loc4_ = _loc3_;
            }
            else if(!this.HasCompletedPreReqs(_loc3_))
            {
               if(!_loc5_)
               {
                  _loc5_ = _loc3_;
               }
            }
            else if(!_loc6_)
            {
               _loc6_ = _loc3_;
            }
         }
         if(_loc6_)
         {
            return _loc6_.method_224(class_13.const_785);
         }
         if(_loc5_)
         {
            return _loc5_.method_224(class_13.const_578);
         }
         if(_loc4_)
         {
            return _loc4_.method_224(class_13.const_735);
         }
         return null;
      }
      
      public function method_793(param1:class_35) : uint
      {
         var _loc2_:Mission = null;
         var _loc3_:class_13 = null;
         var _loc4_:Boolean = false;
         for each(_loc3_ in param1.var_1701)
         {
            _loc2_ = this.mMissionInfoList[_loc3_.missionID];
            if(Boolean(_loc2_) && _loc2_.var_145 == Mission.const_58)
            {
               return Entity.const_482;
            }
         }
         _loc4_ = false;
         for each(_loc3_ in param1.var_1886)
         {
            _loc2_ = this.mMissionInfoList[_loc3_.missionID];
            if(_loc2_)
            {
               if(_loc2_.var_145 != Mission.const_72)
               {
                  return Entity.const_599;
               }
            }
            else if(this.HasCompletedPreReqs(_loc3_))
            {
               if(!_loc4_)
               {
                  _loc4_ = true;
               }
            }
         }
         return _loc4_ ? Entity.const_449 : Entity.const_282;
      }
      
      public function HasCompletedPreReqs(param1:class_13) : Boolean
      {
         var _loc2_:Vector.<Vector.<class_13>> = null;
         var _loc3_:Mission = null;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:Boolean = false;
         var _loc7_:Vector.<class_13> = null;
         var _loc8_:class_13 = null;
         _loc2_ = param1.var_2734;
         if(!_loc2_)
         {
            return true;
         }
         _loc4_ = _loc2_.length;
         _loc5_ = 0;
         while(true)
         {
            if(_loc5_ >= _loc4_)
            {
               return false;
            }
            _loc6_ = true;
            _loc7_ = _loc2_[_loc5_];
            for each(_loc8_ in _loc7_)
            {
               _loc3_ = this.mMissionInfoList[_loc8_.missionID];
               if(!_loc3_ || _loc3_.var_145 != Mission.const_72)
               {
                  _loc6_ = false;
                  break;
               }
            }
            if(_loc6_)
            {
               break;
            }
            _loc5_++;
         }
         return true;
      }
      
      public function method_1004() : Boolean
      {
         if(!ResourceManager.method_149("Game"))
         {
            return false;
         }
         this.var_137.method_66(const_508);
         this.var_137.method_66(const_536);
         this.var_137.method_66(const_438);
         this.var_137.method_66(const_680);
         this.var_137.method_66(const_766);
         this.var_137.method_66(const_818);
         this.var_137.method_66(const_827);
         this.var_137.method_66(const_811);
         this.var_137.method_66(const_777);
         this.var_137.method_66(const_702);
         this.var_137.method_66(const_824);
         this.var_137.method_66(const_580);
         this.var_137.method_66(const_693);
         this.var_137.method_66(const_1054);
         this.var_137.method_66(const_581);
         this.var_137.method_66(const_634);
         return true;
      }
      
      public function method_1416() : String
      {
         var _loc1_:Entity = null;
         var _loc2_:String = null;
         if(this.gameState != Game.STATE_PLAY || !this.clientEnt)
         {
            return const_508;
         }
         if(this.method_1076())
         {
            return const_508;
         }
         if(this.var_1601 == true)
         {
            return const_1043;
         }
         if(this.clientEnt.bFiring || Boolean(this.clientEnt.var_485))
         {
            return this.clientEnt.method_529() ? const_536 : const_438;
         }
         if(Boolean(this.clientEnt.var_848) && this.clientEnt.var_2008)
         {
            return this.clientEnt.var_848.doorID >= 100 ? const_777 : const_702;
         }
         if(this.clientEnt.var_518)
         {
            _loc1_ = this.GetEntFromID(this.clientEnt.var_518);
            _loc2_ = _loc1_.entType.entName;
            if(_loc2_ == "CraftForge")
            {
               return const_824;
            }
            if(_loc2_ == "CraftTome" || _loc2_ == "CraftTower" || _loc2_ == "CraftBarn")
            {
               return const_580;
            }
            if(_loc2_ == "NPCHomeAlchemist")
            {
               return const_581;
            }
            if(_loc2_ == "NPCHomeGemMerchant")
            {
               if(this.mAlertState & const_186)
               {
                  return const_634;
               }
            }
            if(_loc2_ == "NPCTreasureTrove")
            {
               return const_693;
            }
            if(_loc1_.var_1264 && this.mTimeThisTick < _loc1_.var_1395)
            {
               return const_818;
            }
            if(!_loc1_ || !_loc1_.var_426 || this.mTimeThisTick >= _loc1_.var_1395)
            {
               return const_680;
            }
            return const_766;
         }
         if(Boolean(this.clientEnt.var_1113) && this.clientEnt.var_2650)
         {
            return const_827;
         }
         if(Boolean(this.clientEnt.var_1216) && this.clientEnt.combatState.method_123(Game.const_690))
         {
            return const_811;
         }
         return this.clientEnt.method_529() ? const_536 : const_438;
      }
      
      public function UIBasicButton_CreateBasicButton(param1:MovieClip, param2:Function, param3:String = null, param4:Boolean = false, param5:Boolean = false) : void
      {
         param1.mouseEnabled = true;
         param1.mouseChildren = false;
         param1.filters = param4 ? [Game.const_515] : [];
         param1.db_ClickCallback = param2;
         param1.db_bOnMouseDown = param5;
         if(param2 != null)
         {
            param1.addEventListener(param5 ? MouseEvent.MOUSE_DOWN : MouseEvent.CLICK,param2);
         }
         if(param3)
         {
            param1.addEventListener(MouseEvent.ROLL_OVER,this.method_314);
            param1.addEventListener(MouseEvent.ROLL_OUT,this.method_315);
            param1.db_Tooltip = param3;
         }
      }
      
      public function UIBasicButton_DestroyBasicButton(param1:MovieClip) : void
      {
         param1.filters = [];
         if(param1.db_ClickCallback != null)
         {
            param1.removeEventListener(!!param1.db_bOnMouseDown ? MouseEvent.MOUSE_DOWN : MouseEvent.CLICK,param1.db_ClickCallback);
            param1.db_ClickCallback = null;
         }
         if(param1.db_Tooltip)
         {
            param1.removeEventListener(MouseEvent.ROLL_OVER,this.method_314);
            param1.removeEventListener(MouseEvent.ROLL_OUT,this.method_315);
            param1.db_Tooltip = null;
         }
      }
      
      public function method_2070(param1:MovieClip, param2:String = null) : void
      {
         if(!param2)
         {
            param1.removeEventListener(MouseEvent.ROLL_OVER,this.method_314);
            param1.removeEventListener(MouseEvent.ROLL_OUT,this.method_315);
            param1.db_Tooltip = null;
         }
         else
         {
            if(!param1.db_Tooltip)
            {
               param1.addEventListener(MouseEvent.ROLL_OVER,this.method_314);
               param1.addEventListener(MouseEvent.ROLL_OUT,this.method_315);
            }
            param1.db_Tooltip = param2;
         }
      }
      
      private function method_314(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = null;
         _loc2_ = param1.target as MovieClip;
         if(_loc2_.db_disabled)
         {
            return;
         }
         if(_loc2_.db_Tooltip)
         {
            this.tooltip.TriggerTooltip(_loc2_.db_Tooltip);
         }
      }
      
      private function method_315(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = null;
         _loc2_ = param1.target as MovieClip;
         if(_loc2_.db_disabled)
         {
            return;
         }
         if(_loc2_.db_Tooltip)
         {
            this.tooltip.UntriggerTooltip();
         }
      }
      
      public function method_1285(param1:String) : Boolean
      {
         return Level.method_182(param1) != param1;
      }
      
      public function FindInFriendList(param1:String) : Friend
      {
         var _loc2_:Friend = null;
         var _loc3_:Friend = null;
         _loc2_ = null;
         for each(_loc3_ in this.friendList)
         {
            if(_loc3_.charName == param1)
            {
               _loc2_ = _loc3_;
               break;
            }
         }
         return _loc2_;
      }
      
      public function method_420() : void
      {
         var _loc1_:String = null;
         var _loc2_:Number = NaN;
         _loc1_ = Level.method_1551(this.level.internalName);
         if(!_loc1_)
         {
            return;
         }
         _loc2_ = Number(var_1655[_loc1_]);
         if(!_loc2_)
         {
            _loc2_ = 0.5;
         }
         SoundManager.method_103(Main.const_77,_loc1_,_loc2_);
      }
      
      public function FormatHotName(param1:String) : String
      {
         var _loc2_:* = null;
         var _loc3_:String = null;
         if(this.clientEntName == param1 && !(DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT))
         {
            return param1;
         }
         _loc2_ = "<a href=\'event:" + param1 + "\'>";
         _loc3_ = "</a>";
         return _loc2_ + param1 + _loc3_;
      }
      
      public function InHardMode() : Boolean
      {
         return this.level.alterParamsString == "Hard";
      }
      
      public function method_1333() : Boolean
      {
         var _loc1_:Packet = null;
         if(Boolean(this.var_2132) && Math.abs(this.var_2132 - this.mTimeThisTick) > 10000)
         {
            return false;
         }
         _loc1_ = new Packet(LinkUpdater.const_924);
         this.serverConn.SendPacket(_loc1_);
         this.var_2132 = this.mTimeThisTick;
         return true;
      }
      
      public function ChangeHouseArt(param1:String, param2:String) : void
      {
         this.var_163[param1] = param2;
         if(this.level.var_333)
         {
            this.var_2047 = true;
         }
      }
      
      public function SetSwapCategory(param1:String, param2:String) : void
      {
         this.var_758.var_980 = param1;
         if(param1)
         {
            this.var_758.Display();
         }
         else
         {
            this.var_758.Hide();
         }
      }
      
      public function method_1199(param1:Boolean) : void
      {
         if(param1)
         {
            this.main.addChild(this.level.var_178);
            this.level.var_178.addEventListener(MouseEvent.MOUSE_OVER,this.method_719,false,0,true);
            this.level.var_178.addEventListener(MouseEvent.MOUSE_OUT,this.method_985,false,0,true);
            this.level.var_178.addEventListener(MouseEvent.CLICK,this.method_642,false,0,true);
            this.method_568();
         }
         else
         {
            this.level.var_178.removeEventListener(MouseEvent.MOUSE_OVER,this.method_719);
            this.level.var_178.removeEventListener(MouseEvent.MOUSE_OUT,this.method_985);
            this.level.var_178.removeEventListener(MouseEvent.CLICK,this.method_642);
            this.main.removeChild(this.level.var_178);
            this.var_758.Hide();
         }
         this.var_1601 = param1;
      }
      
      public function method_568() : void
      {
         this.level.var_178.scaleX = this.main.overallScale;
         this.level.var_178.scaleY = this.main.overallScale;
         this.level.var_178.x = this.levelLayer.x * this.main.overallScale;
         this.level.var_178.y = this.levelLayer.y * this.main.overallScale;
         if(this.var_2047)
         {
            this.var_2047 = false;
            this.method_1199(this.var_1601);
         }
      }
      
      public function method_985(param1:MouseEvent) : void
      {
         var _loc2_:Sprite = null;
         _loc2_ = param1.target as Sprite;
         _loc2_.filters = [this.var_1791];
      }
      
      public function method_719(param1:MouseEvent) : void
      {
         var _loc2_:Sprite = null;
         _loc2_ = param1.target as Sprite;
         _loc2_.filters = [new GlowFilter(11701805,1,5,5,10)];
      }
      
      public function method_642(param1:MouseEvent) : void
      {
         var _loc2_:Sprite = null;
         var _loc3_:String = null;
         var _loc4_:Array = null;
         var _loc5_:String = null;
         var _loc6_:String = null;
         _loc2_ = param1.target as Sprite;
         _loc2_.filters = [this.var_1791];
         _loc3_ = getQualifiedClassName(_loc2_);
         _loc5_ = String((_loc4_ = _loc3_.split("_"))[2]);
         _loc6_ = String(_loc4_[3]);
         this.SetSwapCategory(_loc5_,_loc6_);
      }
      
      public function method_1337() : Boolean
      {
         if(!this.clientEnt)
         {
            return true;
         }
         if(this.var_2681 != int(this.clientEnt.var_859 / 2))
         {
            return false;
         }
         if(this.var_2852 != int(this.clientEnt.mExpLevel * 8))
         {
            return false;
         }
         if(this.var_2450 != int(this.clientEnt.var_64 * 10))
         {
            return false;
         }
         if(this.var_2465 != int(this.clientEnt.maxHP * 12))
         {
            return false;
         }
         if(this.var_2655 != int(this.clientEnt.meleeDamage * 20))
         {
            return false;
         }
         if(this.var_2723 != int(this.clientEnt.magicDamage * 18))
         {
            return false;
         }
         if(this.var_2636 != int(this.clientEnt.armorClass * 16))
         {
            return false;
         }
         if(this.var_2735 != int(this.clientEnt.currHP * 14))
         {
            return false;
         }
         if(this.var_2476 != int(this.clientEnt.maxSpeed * 24))
         {
            return false;
         }
         if(this.var_2817 != int(this.clientEnt.var_412 * 26))
         {
            return false;
         }
         if(this.var_2797 != int(this.clientEnt.var_31 * 28))
         {
            return false;
         }
         return true;
      }
      
      public function method_764(param1:uint) : void
      {
         this.var_2681 = int(param1 / 2);
      }
      
      public function method_439(param1:int, param2:int) : void
      {
         this.var_2852 = int(param1 * 8);
         this.var_2450 = int(param2 * 10);
      }
      
      public function method_418(param1:int) : void
      {
         this.var_2465 = int(param1 * 12);
      }
      
      public function method_1934(param1:int, param2:int, param3:uint) : void
      {
         this.var_2655 = int(param1 * 20);
         this.var_2723 = int(param2 * 18);
         this.var_2636 = int(param3 * 16);
      }
      
      public function method_184(param1:int) : void
      {
         this.var_2735 = int(param1 * 14);
      }
      
      public function method_1443(param1:Number) : void
      {
         this.var_2476 = int(param1 * 24);
      }
      
      public function method_1189(param1:Number) : void
      {
         this.var_2817 = int(param1 * 26);
      }
      
      public function method_114(param1:Number) : void
      {
         this.var_2797 = int(param1 * 28);
      }
      
      public function method_1880() : void
      {
         this.CONTEXT_NORMAL = this.mKeybindManager.method_794();
         this.mKeybindManager.SetContext(this.CONTEXT_NORMAL);
         this.mKeybindManager.method_32(Game.const_240,Keyboard.ESCAPE,false);
         this.mKeybindManager.method_32(Game.const_153,Keyboard.LEFT,false);
         this.mKeybindManager.method_32(Game.const_151,Keyboard.RIGHT,false);
         this.mKeybindManager.method_32(Game.const_158,Keyboard.UP,false);
         this.mKeybindManager.method_32(Game.const_188,Keyboard.DOWN,false);
         this.mKeybindManager.method_32(Game.const_570,Keyboard.ENTER,false);
         this.mKeybindManager.method_32(Game.const_158,Keyboard.SPACE,false);
         this.mKeybindManager.method_32(Game.const_543,Keyboard.SLASH,false);
         this.mKeybindManager.method_32(Game.const_543,Keyboard.BACKSLASH,false);
         this.mKeybindManager.method_181(Keyboard.SHIFT);
         this.mKeybindManager.method_181(Keyboard.CONTROL);
         this.mKeybindManager.method_181(Keyboard.ALTERNATE);
         this.mKeybindManager.method_181(Keyboard.CAPS_LOCK);
         this.mKeybindManager.method_181(91);
         this.mKeybindManager.method_181(92);
         this.mKeybindManager.method_181(93);
         this.mKeybindManager.method_32(Game.const_153,Keyboard.A);
         this.mKeybindManager.method_32(Game.const_151,Keyboard.D);
         this.mKeybindManager.method_32(Game.const_158,Keyboard.W);
         this.mKeybindManager.method_32(Game.const_188,Keyboard.S);
         this.mKeybindManager.method_32(Game.COMMAND_SPELL1,Keyboard.NUMBER_1);
         this.mKeybindManager.method_32(Game.COMMAND_SPELL2,Keyboard.NUMBER_2);
         this.mKeybindManager.method_32(Game.COMMAND_SPELL3,Keyboard.NUMBER_3);
         this.mKeybindManager.method_32(Game.COMMAND_SPELL4,Keyboard.NUMBER_4);
         this.mKeybindManager.method_32(Game.COMMAND_SPELL5,Keyboard.NUMBER_5);
         this.mKeybindManager.method_32(Game.COMMAND_SPELL6,Keyboard.NUMBER_6);
         this.mKeybindManager.method_32(Game.const_401,Keyboard.V);
         this.mKeybindManager.method_32(Game.const_317,Keyboard.C);
         this.mKeybindManager.method_32(Game.const_328,Keyboard.M);
         this.mKeybindManager.method_32(Game.const_346,Keyboard.N);
         this.mKeybindManager.method_32(Game.const_367,Keyboard.O);
         this.mKeybindManager.method_32(Game.const_321,Keyboard.P);
         this.mKeybindManager.method_32(Game.const_364,Keyboard.I);
         this.mKeybindManager.method_32(Game.const_357,Keyboard.B);
         this.mKeybindManager.method_32(Game.const_314,Keyboard.E);
         this.mKeybindManager.method_32(Game.const_320,Keyboard.R);
         this.mKeybindManager.method_32(Game.const_277,Keyboard.NUMBER_7);
         this.mKeybindManager.method_32(Game.const_274,Keyboard.NUMBER_8);
         this.mKeybindManager.method_32(Game.const_329,Keyboard.H);
         this.CONTEXT_CHAT = this.mKeybindManager.method_794();
         this.mKeybindManager.SetContext(this.CONTEXT_CHAT);
         this.mKeybindManager.method_32(Game.COMMAND2_ENTER,Keyboard.ENTER,false);
         this.mKeybindManager.method_32(Game.COMMAND2_ESCAPE,Keyboard.ESCAPE,false);
         this.mKeybindManager.method_32(Game.COMMAND2_SCROLLUP,Keyboard.UP,false);
         this.mKeybindManager.method_32(Game.COMMAND2_SCROLLDOWN,Keyboard.DOWN,false);
         this.mKeybindManager.method_32(Game.COMMAND2_BACKSPACE,Keyboard.BACKSPACE,false);
         this.mKeybindManager.method_32(Game.COMMAND2_DELETE,Keyboard.DELETE,false);
         this.mKeybindManager.SetContext(this.CONTEXT_NORMAL);
         this.mKeybindManager.method_1424(this.CONTEXT_NORMAL);
         this.mKeybindManager.method_44("Left",const_153);
         this.mKeybindManager.method_44("Right",const_151);
         this.mKeybindManager.method_44("Jump",const_158);
         this.mKeybindManager.method_44("Drop",const_188);
         this.mKeybindManager.method_44("Hotbar 1",COMMAND_SPELL1);
         this.mKeybindManager.method_44("Hotbar 2",COMMAND_SPELL2);
         this.mKeybindManager.method_44("Hotbar 3",COMMAND_SPELL3);
         this.mKeybindManager.method_44("Hotbar 4",COMMAND_SPELL4);
         this.mKeybindManager.method_44("Hotbar 5",COMMAND_SPELL5);
         this.mKeybindManager.method_44("Hotbar 6",COMMAND_SPELL6);
         this.mKeybindManager.method_44("Wave",const_401);
         this.mKeybindManager.method_44("Dance",const_574);
         this.mKeybindManager.method_44("Cheer",const_317);
         this.mKeybindManager.method_44("Map",const_328);
         this.mKeybindManager.method_44("Talents",const_346);
         this.mKeybindManager.method_44("Social",const_367);
         this.mKeybindManager.method_44("Inventory",const_364);
         this.mKeybindManager.method_44("Store",const_357);
         this.mKeybindManager.method_44("Door",const_314);
         this.mKeybindManager.method_44("Home",const_329);
         this.mKeybindManager.method_44("Spellbook",const_321);
         this.mKeybindManager.method_44("Reply",const_320);
         this.mKeybindManager.method_44("Pet",const_277);
         this.mKeybindManager.method_44("Mount",const_274);
         this.mKeybindManager.method_44("Party Chat",const_458);
         this.mKeybindManager.method_44("Guild Chat",const_430);
      }
      
      public function method_532(param1:uint, param2:uint, param3:uint, param4:uint, param5:uint, param6:Boolean, param7:uint, param8:uint) : class_42
      {
         var _loc9_:String = null;
         var _loc10_:GearType = null;
         var _loc11_:class_64 = null;
         var _loc12_:class_64 = null;
         var _loc13_:class_64 = null;
         var _loc14_:class_21 = null;
         var _loc15_:class_21 = null;
         var _loc16_:class_42 = null;
         _loc9_ = method_110(param1,param2);
         _loc10_ = class_14.var_421[_loc9_];
         _loc11_ = !!param3 ? class_64.method_56(param3) : null;
         _loc12_ = !!param4 ? class_64.method_56(param4) : null;
         _loc13_ = !!param5 ? class_64.method_56(param5) : null;
         _loc14_ = class_14.var_194[param7];
         _loc15_ = class_14.var_194[param8];
         if(!_loc10_)
         {
            return null;
         }
         _loc16_ = new class_42(_loc10_,_loc11_,_loc12_,_loc13_,_loc14_,_loc15_,param6);
         this.mOwnedGear[_loc10_.gearID] = _loc16_;
         this.var_144.push(_loc16_);
         this.mFilteredOwnedGear = this.var_144;
         this.mOwnedGear2[method_110(param1,param2)] = _loc16_;
         if(param6)
         {
            this.screenArmory.method_601();
         }
         return _loc16_;
      }
      
      public function method_1657(param1:Vector.<uint>) : void
      {
         var _loc2_:uint = 0;
         var _loc3_:Vector.<class_42> = null;
         var _loc4_:class_42 = null;
         var _loc5_:uint = 0;
         var _loc6_:class_42 = null;
         var _loc7_:uint = 0;
         _loc2_ = 0;
         _loc3_ = new Vector.<class_42>(EntType.MAX_SLOTS - 1);
         this.var_898 = 0;
         _loc5_ = param1[EntType.SWORD_SLOT];
         if(_loc4_ = this.mOwnedGear[_loc5_])
         {
            _loc3_[5] = _loc4_;
         }
         _loc5_ = param1[EntType.SHIELD_SLOT];
         if(_loc4_ = this.mOwnedGear[_loc5_])
         {
            _loc3_[4] = _loc4_;
         }
         _loc5_ = param1[EntType.HAT_SLOT];
         if(_loc4_ = this.mOwnedGear[_loc5_])
         {
            _loc3_[3] = _loc4_;
         }
         _loc5_ = param1[EntType.ARMOR_SLOT];
         if(_loc4_ = this.mOwnedGear[_loc5_])
         {
            _loc3_[2] = _loc4_;
         }
         _loc5_ = param1[EntType.GLOVES_SLOT];
         if(_loc4_ = this.mOwnedGear[_loc5_])
         {
            _loc3_[1] = _loc4_;
         }
         _loc5_ = param1[EntType.BOOTS_SLOT];
         if(_loc4_ = this.mOwnedGear[_loc5_])
         {
            _loc3_[0] = _loc4_;
         }
         _loc2_ = 0;
         while(_loc2_ < _loc3_.length)
         {
            if(_loc6_ = _loc3_[_loc2_])
            {
               if((_loc7_ = uint(this.var_144.indexOf(_loc6_))) > -1)
               {
                  this.var_144.splice(_loc7_,1);
                  this.var_144.push(_loc6_);
                  ++this.var_898;
               }
            }
            _loc2_++;
         }
      }
      
      public function method_709() : void
      {
         var _loc1_:int = 0;
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc8_:class_42 = null;
         var _loc9_:GearType = null;
         var _loc10_:uint = 0;
         var _loc11_:uint = 0;
         var _loc12_:uint = 0;
         _loc1_ = 0;
         _loc2_ = 0;
         _loc3_ = 0;
         _loc5_ = (_loc4_ = int(this.var_144.length - 1)) - ScreenArmory.const_12 >= 0 ? _loc4_ - ScreenArmory.const_12 : 0;
         _loc6_ = 0;
         _loc7_ = this.var_144.length;
         while(_loc4_ >= 0)
         {
            _loc1_ = _loc4_;
            while(_loc1_ >= _loc5_)
            {
               if(_loc1_ < _loc7_ - this.var_898 - this.var_1081)
               {
                  _loc8_ = this.var_144[_loc1_];
                  _loc10_ = (_loc10_ = _loc6_ == 0 ? this.var_898 + this.var_1081 : _loc6_ * ScreenArmory.const_12) + _loc2_;
                  if(_loc8_)
                  {
                     if((_loc9_ = _loc8_.gearType).var_8 == "L")
                     {
                        this.var_144.splice(_loc1_,1);
                        this.var_144.splice(_loc7_ - _loc10_ - 1,0,_loc8_);
                        _loc2_++;
                        _loc11_ = uint(_loc7_ - _loc10_);
                     }
                  }
               }
               _loc1_--;
            }
            _loc1_ = _loc4_;
            while(_loc1_ >= _loc5_)
            {
               if(_loc1_ < _loc7_ - this.var_898 - this.var_1081)
               {
                  _loc8_ = this.var_144[_loc1_];
                  _loc10_ = (_loc10_ = uint((_loc10_ = _loc6_ == 0 ? this.var_898 + this.var_1081 : _loc6_ * ScreenArmory.const_12) + _loc2_)) + _loc3_;
                  if(_loc8_)
                  {
                     if((_loc9_ = _loc8_.gearType).var_8 == "R")
                     {
                        this.var_144.splice(_loc1_,1);
                        this.var_144.splice(_loc7_ - _loc10_ - 1,0,_loc8_);
                        _loc3_++;
                        _loc12_ = uint(_loc7_ - _loc10_);
                     }
                  }
               }
               _loc1_--;
            }
            _loc5_ = (_loc4_ -= ScreenArmory.const_12) - ScreenArmory.const_12 >= 0 ? _loc4_ - ScreenArmory.const_12 : 0;
            _loc6_++;
            _loc2_ = 0;
            _loc3_ = 0;
         }
      }
      
      public function GetBestOwnedGearByID(param1:uint) : class_42
      {
         var _loc2_:* = null;
         _loc2_ = String(param1) + "L";
         if(this.mOwnedGear2[_loc2_])
         {
            return this.mOwnedGear2[_loc2_];
         }
         _loc2_ = String(param1) + "R";
         if(this.mOwnedGear2[_loc2_])
         {
            return this.mOwnedGear2[_loc2_];
         }
         _loc2_ = String(param1) + "M";
         if(this.mOwnedGear2[_loc2_])
         {
            return this.mOwnedGear2[_loc2_];
         }
         return null;
      }
      
      public function method_2129(param1:uint, param2:String) : class_42
      {
         var _loc3_:String = null;
         _loc3_ = String(param1) + param2;
         if(this.mOwnedGear2[_loc3_])
         {
            return this.mOwnedGear2[_loc3_];
         }
         return null;
      }
      
      public function HasBetterOrEven(param1:GearType) : Boolean
      {
         var _loc2_:Boolean = false;
         var _loc3_:uint = 0;
         var _loc4_:class_42 = null;
         var _loc5_:String = null;
         _loc2_ = false;
         if(!param1)
         {
            return _loc2_;
         }
         _loc3_ = param1.gearID;
         if(!(_loc4_ = this.GetBestOwnedGearByID(_loc3_)))
         {
            return _loc2_;
         }
         _loc5_ = param1.var_8;
         if(_loc4_)
         {
            if(_loc5_ == "M")
            {
               _loc2_ = true;
            }
            else if(_loc5_ == "R")
            {
               if(_loc4_.gearType.var_8 == "M")
               {
                  _loc2_ = false;
               }
               else
               {
                  _loc2_ = true;
               }
            }
            else if(_loc5_ == "L")
            {
               if(_loc4_.gearType.var_8 == "M" || _loc4_.gearType.var_8 == "R")
               {
                  _loc2_ = false;
               }
               else
               {
                  _loc2_ = true;
               }
            }
         }
         return _loc2_;
      }
      
      public function method_1178() : void
      {
         this.var_163 = new Dictionary();
      }
      
      public function UpdateBuildingUpgradePanel(param1:MovieClip, param2:class_9, param3:class_33) : void
      {
         var _loc4_:String = null;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc8_:Boolean = false;
         var _loc10_:uint = 0;
         var _loc11_:Boolean = false;
         var _loc12_:* = null;
         var _loc13_:class_9 = null;
         var _loc15_:class_9 = null;
         _loc4_ = "";
         _loc5_ = 0;
         _loc6_ = 0;
         _loc7_ = 0;
         _loc8_ = false;
         if(param2)
         {
            _loc7_ = uint(param2.rank + 1);
            _loc13_ = class_9.method_94(param2.var_242,_loc7_);
            _loc4_ = param2.displayName;
            if(!_loc13_)
            {
               param1.am_MaxRank.visible = true;
               param1.am_Arrow.visible = false;
               _loc8_ = true;
            }
            else
            {
               _loc5_ = _loc13_.var_129;
               _loc6_ = _loc13_.upgradeTime;
               param1.am_MaxRank.visible = false;
               param1.am_Arrow.visible = true;
            }
         }
         MathUtil.method_2(param1.am_Name,_loc4_);
         var _loc9_:* = false;
         _loc10_ = 0;
         _loc11_ = false;
         if(this.clientEnt)
         {
            _loc9_ = this.clientEnt.currGold >= _loc5_;
            _loc10_ = class_105.method_551(this.clientEnt.mExpLevel);
         }
         if(_loc8_)
         {
            MathUtil.method_8(param1.am_Time,"--",ScreenArmory.const_9,ScreenArmory.const_17);
            MathUtil.method_8(param1.am_Gold,"--",ScreenArmory.const_9,ScreenArmory.const_17);
         }
         else
         {
            MathUtil.method_8(param1.am_Time,Game.method_70(_loc6_,true),ScreenArmory.const_11,ScreenArmory.const_59);
            MathUtil.method_8(param1.am_Gold,MathUtil.method_29(_loc5_),ScreenArmory.const_11,ScreenArmory.const_59);
         }
         _loc12_ = param2.var_1499;
         if(!_loc13_)
         {
            _loc11_ = true;
         }
         else if(_loc10_ < _loc7_)
         {
            _loc12_ = "Must be level " + (_loc7_ - 1) * 5 + " to upgrade";
            _loc11_ = true;
         }
         else if(this.mBuildingInfo.mStatus != class_105.const_29)
         {
            if(_loc15_ = this.mBuildingInfo.GetCurrentBuilding())
            {
               _loc12_ = "Busy upgrading " + _loc15_.displayName;
            }
            _loc11_ = true;
         }
         if(_loc11_)
         {
            param3.Hide();
            MathUtil.method_8(param1.am_Message,_loc12_,ScreenArmory.const_137,ScreenArmory.const_169);
         }
         else
         {
            param3.Show();
            MathUtil.method_8(param1.am_Message,_loc12_,ScreenArmory.const_106,ScreenArmory.const_417);
         }
      }
      
      public function method_2042(param1:class_9) : void
      {
         if(!param1)
         {
            return;
         }
         switch(param1.type)
         {
            case "Tome":
               this.screenTome.Refresh();
               break;
            case "Forge":
               this.screenForge.Refresh();
               break;
            case "Tower":
               this.screenClassTowers.Refresh();
               break;
            case "Barn":
               this.screenBarn.Refresh();
         }
      }
      
      public function method_312(param1:String, param2:Boolean) : void
      {
         var _loc3_:Packet = null;
         if(!this.CanSendPacket())
         {
            return;
         }
         if(!this.clientEnt || this.clientEnt.entState == Entity.const_6)
         {
            return;
         }
         _loc3_ = new Packet(LinkUpdater.const_1197);
         _loc3_.method_26(param1);
         _loc3_.method_15(param2);
         this.serverConn.SendPacket(_loc3_);
         this.mbTransferMode = true;
      }
      
      public function method_1838(param1:Boolean = false, param2:uint = 7, param3:uint = 0) : void
      {
         var _loc4_:Packet = null;
         if(!this.clientEnt || !this.CanSendPacket())
         {
            return;
         }
         if(this.mTimeThisTick > this.var_2724 + const_1135)
         {
            if(this.var_1868)
            {
            }
            this.var_2724 = this.mTimeThisTick;
            (_loc4_ = new Packet(LinkUpdater.const_1099)).method_24(this.clientEnt.currHP);
            _loc4_.method_20(const_390,param3);
            _loc4_.method_15(this.var_1868);
            this.serverConn.SendPacket(_loc4_);
         }
      }
      
      public function method_389() : void
      {
         this.var_1868 = false;
      }
      
      public function GainCharm(param1:class_64, param2:Boolean) : void
      {
         var _loc3_:class_1 = null;
         var _loc4_:class_114 = null;
         _loc3_ = param1.var_13;
         if(_loc3_)
         {
            if(_loc3_.var_68 == class_1.const_405)
            {
               ++this.mRespecStoneCount;
               if(param2)
               {
                  this.mMagicForgeStatus.var_2434 = true;
               }
            }
            else
            {
               if(!(_loc4_ = this.mOwnedCharms[param1.method_75()]))
               {
                  _loc4_ = new class_114(0,param1);
                  this.mOwnedCharms[param1.method_75()] = _loc4_;
               }
               else
               {
                  param1.method_266();
                  param1 = null;
               }
               ++_loc4_.var_181;
               this.screenArmory.Refresh();
            }
         }
      }
      
      public function method_1134(param1:class_21, param2:Boolean = false) : void
      {
         var _loc3_:uint = 0;
         this.mOwnedDyes[param1.var_57] = true;
         ++this.var_1407;
         if(!param2)
         {
            _loc3_ = param1.var_8 == "L" ? class_46.const_546 : class_46.const_532;
            this.screenNotification.ShowNotification(_loc3_,param1.displayName,param1.var_8,true,null,null,null,param1);
         }
         this.screenDyeGear.Refresh();
      }
      
      public function method_1202(param1:class_3, param2:uint, param3:Boolean) : void
      {
         var _loc4_:class_103 = null;
         var _loc5_:String = null;
         if(!(_loc4_ = this.mOwnedConsumables[param1.consumableID]))
         {
            _loc4_ = new class_103(param1,param2);
            this.mOwnedConsumables[param1.consumableID] = _loc4_;
            this.mConsumablesList.push(_loc4_);
         }
         else
         {
            _loc4_.stackCount += param2;
         }
         if(!param3)
         {
            if(param1.var_427)
            {
               param2 = uint(param2 / class_3.const_133);
            }
            if((_loc5_ = param1.var_8) == "M")
            {
               _loc5_ = "U";
            }
            this.screenNotification.ShowNotification(class_46.const_353,param1.displayName + " x" + param2,_loc5_,true,null,param1.iconName);
         }
         this.screenArmory.Refresh();
      }
      
      public function QueuePotion(param1:class_3, param2:Boolean = true) : void
      {
         var _loc3_:uint = 0;
         var _loc4_:Packet = null;
         var _loc5_:uint = 0;
         var _loc6_:Packet = null;
         if(!this.CanSendPacket())
         {
            return;
         }
         if(!this.clientEnt)
         {
            return;
         }
         this.clientEnt.mNextPotion = param1;
         _loc3_ = !!param1 ? param1.consumableID : 0;
         (_loc4_ = new Packet(LinkUpdater.const_909)).method_20(class_3.const_69,_loc3_);
         this.serverConn.SendPacket(_loc4_);
         if(!this.clientEnt.mCurrPotion)
         {
            _loc5_ = !!param1 ? param1.consumableID : 0;
            this.clientEnt.method_190(this.clientEnt.mNextPotion);
            (_loc6_ = new Packet(LinkUpdater.const_252)).method_9(this.clientEntID);
            _loc6_.method_20(class_3.const_69,_loc5_);
            this.serverConn.SendPacket(_loc6_);
         }
         if(param2)
         {
            this.screenHudTopRight.Refresh();
         }
      }
   }
}
