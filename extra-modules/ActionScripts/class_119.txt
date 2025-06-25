package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.MovieClip;
   import flash.display.PixelSnapping;
   import flash.display.Stage;
   import flash.display.StageQuality;
   import flash.events.MouseEvent;
   import flash.geom.Matrix;
   import flash.geom.Point;
   import flash.utils.Dictionary;
   import flash.utils.getTimer;
   
   public class class_119 extends class_32
   {
      
      private static const const_1398:Number = 10;
      
      private static const const_1416:Number = 15;
      
      private static const const_1331:Number = 115;
      
      private static const const_1421:Friend = new Friend();
      
      private static const const_1350:String = "<font color=\'#7FFFFF\'>";
      
      private static const const_1237:uint = 8;
      
      private static const const_659:uint = 7;
      
      private static const const_896:uint = 6;
      
      private static const const_1283:uint = 5;
      
      private static const const_597:uint = 4;
      
      private static const const_1199:uint = 3;
      
      private static const const_1150:uint = 2;
      
      private static const const_1225:uint = 1;
      
      private static const const_771:uint = 0;
      
      private static const const_723:uint = 10;
      
      public static const const_228:uint = 4;
      
      private static const const_679:uint = 600;
      
      private static const const_378:String = "Global";
      
      private static const const_820:String = "";
      
      private static const const_363:String = "Hard";
      
      private static const const_490:int = 810;
      
      private static const const_1418:int = 560;
      
      private static const const_4:Dictionary = new Dictionary();
      
      {
         const_4["NewbieRoad"] = const_4["NewbieRoadHard"] = new Vector.<class_158>();
         const_4["NewbieRoad"].push(new class_158(3,13600,19980,1380,2500,new Point(14780,800),new Point(13600,1940)));
         const_4["NewbieRoad"].push(new class_158(2,6940,13300,1380,2500,new Point(8200,900),new Point(6940,1940)));
         const_4["NewbieRoad"].push(new class_158(4,11400,13500,-1600,-800,new Point(11220,420),new Point(11400,-1200)));
         const_4["NewbieRoad"].push(new class_158(5,15400,17000,-1200,-800,new Point(16300,260),new Point(17000,-1000)));
         const_4["SwampRoadNorth"] = const_4["SwampRoadNorthHard"] = new Vector.<class_158>();
         const_4["SwampRoadNorth"].push(new class_158(6,16850,18600,3000,3800,new Point(16980,2100),new Point(16850,3400)));
         const_4["SwampRoadNorth"].push(new class_158(3,14760,23600,4540,5760,new Point(17820,820),new Point(14760,5150)));
         const_4["SwampRoadNorth"].push(new class_158(2,14760,20240,1340,2520,new Point(10500,780),new Point(14760,1930)));
         const_4["SwampRoadNorth"].push(new class_158(4,19600,21600,-1800,-1000,new Point(20020,400),new Point(19600,-1400)));
         const_4["SwampRoadNorth"].push(new class_158(5,12400,14400,-1400,-700,new Point(12740,400),new Point(12400,-1050)));
         const_4["BridgeTown"] = const_4["BridgeTownHard"] = new Vector.<class_158>();
         const_4["BridgeTown"].push(new class_158(2,10600,16050,1500,2800,new Point(12200,700),new Point(10600,2150)));
         const_4["BridgeTown"].push(new class_158(3,11450,13000,3800,4400,new Point(13040,2360),new Point(11450,4100)));
         const_4["BridgeTown"].push(new class_158(4,8200,10000,2300,3200,new Point(15380,2000),new Point(8200,2750)));
         const_4["BridgeTown"].push(new class_158(5,4550,6475,1300,2300,new Point(5980,860),new Point(4550,1800)));
         const_4["CemeteryHill"] = const_4["CemeteryHillHard"] = new Vector.<class_158>();
         const_4["CemeteryHill"].push(new class_158(2,4550,13800,2200,6000));
         const_4["CemeteryHill"].push(new class_158(3,22300,28625,-300,1400));
         const_4["OldMineMountain"] = const_4["OldMineMountainHard"] = new Vector.<class_158>();
         const_4["OldMineMountain"].push(new class_158(6,14300,19000,3080,4200,new Point(21380,800),new Point(14300,3640)));
         const_4["OldMineMountain"].push(new class_158(5,8540,13340,2220,3540,new Point(16440,-1240),new Point(13340,2880)));
         const_4["OldMineMountain"].push(new class_158(4,16100,19020,-1680,-640,new Point(18970,-630),new Point(18970,-650)));
         const_4["OldMineMountain"].push(new class_158(3,11920,19520,-1580,120,new Point(12050,-1585),new Point(12050,-1575)));
         const_4["OldMineMountain"].push(new class_158(2,8160,21560,140,1780,new Point(8470,135),new Point(8470,145)));
         const_4["OldMineMountain"].push(new class_158(7,17400,19000,-3150,2700,new Point(17410,-3160),new Point(17410,-3140)));
         const_4["EmeraldGlades"] = const_4["EmeraldGladesHard"] = new Vector.<class_158>();
         const_4["EmeraldGlades"].push(new class_158(2,-1800,550,-2500,-1200,new Point(-1800,-680),new Point(550,-1850)));
         const_4["EmeraldGlades"].push(new class_158(3,-1850,5600,-900,600));
         const_4["EmeraldGlades"].push(new class_158(4,5600,10154,-900,600));
         const_4["EmeraldGlades"].push(new class_158(5,10154,14000,-226,900));
         const_4["EmeraldGlades"].push(new class_158(6,14000,17500,-900,800));
         const_4["EmeraldGlades"].push(new class_158(7,700,7050,1400,2700,new Point(17120,-40),new Point(700,2050)));
         const_4["EmeraldGlades"].push(new class_158(8,2900,8800,-2400,-1300,new Point(16520,560),new Point(2900,-1850)));
         const_4["EmeraldGlades"].push(new class_158(9,9000,18000,-1500,-225));
         const_4["Castle"] = const_4["CastleHard"] = new Vector.<class_158>();
         const_4["Castle"].push(new class_158(2,-1600,1900,-2600,-1600));
         const_4["Castle"].push(new class_158(3,2300,9400,-2400,-1600));
         const_4["Castle"].push(new class_158(4,13000,18000,-2300,-1900,new Point(12120,-360),new Point(13000,-2100)));
         const_4["Castle"].push(new class_158(5,12500,16200,950,2400,new Point(12600,280),new Point(12500,1675)));
         const_4["Castle"].push(new class_158(6,15300,22100,-600,1000));
         const_4["Castle"].push(new class_158(7,9400,14900,-600,300));
         const_4["ShazariDesert"] = const_4["ShazariDesertHard"] = new Vector.<class_158>();
         const_4["ShazariDesert"].push(new class_158(6,20050,21020,1820,2520,new Point(20153,900),new Point(20050,2419)));
         const_4["ShazariDesert"].push(new class_158(5,7850,8900,-2500,-1800,new Point(8376,100),new Point(8900,-1941)));
         const_4["ShazariDesert"].push(new class_158(7,7850,8900,-1300,-600,new Point(8395,420),new Point(8900,-661)));
         const_4["ShazariDesert"].push(new class_158(8,7100,8050,1400,2150,new Point(7757,400),new Point(7100,2058)));
         const_4["ShazariDesert"].push(new class_158(2,2400,5450,1900,3000,new Point(3790,670),new Point(2400,2300)));
         const_4["ShazariDesert"].push(new class_158(3,10900,19200,1600,2700,new Point(14420,1240),new Point(10900,2179)));
         const_4["ShazariDesert"].push(new class_158(4,21800,25200,-1500,200,new Point(23930,1150),new Point(21800,-22)));
         const_4["JadeCity"] = const_4["JadeCityHard"] = new Vector.<class_158>();
         const_4["JadeCity"].push(new class_158(23,17850,21520,-4500,-3400,new Point(17070,-3542),new Point(17850,-3580)));
         const_4["JadeCity"].push(new class_158(24,22000,24400,-4500,-3400,new Point(23704,-750),new Point(22900,-3200)));
         const_4["JadeCity"].push(new class_158(21,9490,17070,-4500,-3400,new Point(8980,-3580),new Point(9490,-3542)));
         const_4["JadeCity"].push(new class_158(20,-2580,-730,-4900,-3300,new Point(245,-3550),new Point(-985,-3320)));
         const_4["JadeCity"].push(new class_158(22,-4650,-3440,-4900,-3000,new Point(-2500,-3839),new Point(-3440,-3700)));
         const_4["JadeCity"].push(new class_158(19,5300,8980,-4500,-2500,new Point(6095,-800),new Point(7000,-3200)));
         const_4["JadeCity"].push(new class_158(18,-400,4750,-4300,-2730,new Point(5300,-3542),new Point(4749,-3542)));
         const_4["JadeCity"].push(new class_158(17,3560,7090,-2500,-1400,new Point(5590,-850),new Point(3560,-1950)));
         const_4["JadeCity"].push(new class_158(15,955,8000,-1200,0,new Point(8820,800),new Point(7950,-400)));
         const_4["JadeCity"].push(new class_158(14,6840,14225,1800,2800,new Point(2213,600),new Point(7067,1900)));
         const_4["JadeCity"].push(new class_158(10,8910,10000,-1200,-400,new Point(9453,800),new Point(8910,-522)));
         const_4["JadeCity"].push(new class_158(2,1530,10390,-800,6000));
         const_4["JadeCity"].push(new class_158(3,10391,11600,200,1500));
         const_4["JadeCity"].push(new class_158(4,11601,13460,200,1500));
         const_4["JadeCity"].push(new class_158(5,13461,16399,200,1500));
         const_4["JadeCity"].push(new class_158(6,16400,18200,200,1500,new Point(16399,1018),new Point(16400,998)));
         const_4["JadeCity"].push(new class_158(7,18360,23408,200,1025,new Point(18200,998),new Point(18360,759)));
         const_4["JadeCity"].push(new class_158(8,18100,20000,1026,1500,new Point(19387,1160),new Point(19387,1000)));
         const_4["JadeCity"].push(new class_158(9,23409,25000,200,6000));
         const_4["JadeCity"].push(new class_158(11,13200,14350,-1200,-400,new Point(14133,900),new Point(14350,-522)));
         const_4["JadeCity"].push(new class_158(12,14850,19750,-1200,-100,new Point(15544,500),new Point(15301,-100)));
         const_4["JadeCity"].push(new class_158(13,20600,24000,-1200,-400,new Point(17484,-700),new Point(21065,-800)));
         const_4["JadeCity"].push(new class_158(16,918,2010,-2250,-1800,new Point(1500,-800),new Point(2010,-1822)));
      }
      
      internal var var_1994:MovieClip;
      
      internal var var_2391:MovieClip;
      
      internal var var_2181:MovieClip;
      
      internal var var_538:MovieClip;
      
      internal var var_515:MovieClip;
      
      internal var var_109:MovieClip;
      
      internal var var_1107:MovieClip;
      
      internal var var_608:MovieClip;
      
      internal var var_691:Dictionary;
      
      internal var var_349:Dictionary;
      
      internal var var_1360:Vector.<class_159>;
      
      internal var var_632:Dictionary;
      
      internal var var_756:Dictionary;
      
      internal var var_118:Bitmap;
      
      internal var var_111:Bitmap;
      
      internal var var_1106:uint;
      
      internal var var_2222:Boolean;
      
      internal var var_2263:class_159;
      
      internal var var_1432:class_33;
      
      internal var var_1511:class_33;
      
      internal var var_1288:class_33;
      
      internal var var_2066:class_33;
      
      internal var var_1084:class_33;
      
      internal var var_2318:class_33;
      
      internal var var_1250:class_33;
      
      internal var var_1185:class_33;
      
      internal var var_1165:class_33;
      
      internal var var_1286:class_33;
      
      internal var var_102:String;
      
      internal var var_1387:String;
      
      internal var var_1487:String;
      
      internal var var_985:MovieClip;
      
      internal var var_578:Dictionary;
      
      internal var var_1340:MovieClip;
      
      internal var var_513:MovieClip;
      
      internal var var_711:Vector.<Vector.<Number>>;
      
      internal var var_1099:Vector.<Vector.<Number>>;
      
      internal var mActivePath:class_158;
      
      public function class_119(param1:Game)
      {
         super(param1,"a_MissionMap","am_Panel");
      }
      
      public static function method_144(param1:MovieClip, param2:uint) : void
      {
         if(param2 > const_723)
         {
            param2 = const_723;
         }
         else if(param2 < const_771)
         {
            param2 = const_771;
         }
         param1.gotoAndStop(param2 + 1);
         param1.visible = true;
      }
      
      public static function method_408(param1:String, param2:Number, param3:Number) : class_158
      {
         var _loc5_:class_158 = null;
         var _loc4_:Vector.<class_158>;
         if(!(_loc4_ = const_4[param1]))
         {
            return null;
         }
         for each(_loc5_ in _loc4_)
         {
            if(param2 >= _loc5_.var_2253 && param2 <= _loc5_.var_2330 && param3 >= _loc5_.var_2615 && param3 <= _loc5_.var_2495)
            {
               return _loc5_;
            }
         }
         return null;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:Class = null;
         var _loc3_:uint = 0;
         var _loc19_:MovieClip = null;
         var _loc20_:MovieClip = null;
         var _loc21_:MovieClip = null;
         var _loc22_:String = null;
         var _loc23_:String = null;
         var _loc24_:Number = NaN;
         var _loc25_:Number = NaN;
         var _loc26_:Number = NaN;
         var _loc27_:MovieClip = null;
         var _loc28_:class_159 = null;
         var _loc29_:MovieClip = null;
         var _loc30_:String = null;
         var _loc31_:MovieClip = null;
         var _loc32_:String = null;
         if(var_1.mbSleepingLands)
         {
            _loc1_ = ResourceManager.const_40["GlobalMap02.swf"].applicationDomain.getDefinition("a_GlobalMap2");
         }
         else
         {
            _loc1_ = ResourceManager.const_40["GlobalMap01.swf"].applicationDomain.getDefinition("a_GlobalMap");
         }
         var _loc2_:MovieClip = new _loc1_();
         this.var_1994 = _loc2_.am_MapArt;
         this.var_2391 = this.var_1994.am_Scaler.am_Moment_Hard;
         this.var_2181 = _loc2_.am_Slugs;
         this.var_538 = _loc2_.am_Highlights;
         this.var_515 = _loc2_.am_Boxes;
         this.var_109 = var_2.am_MapHolder;
         while(this.var_109.numChildren)
         {
            this.var_109.removeChildAt(0);
         }
         this.var_118 = new Bitmap(null,PixelSnapping.ALWAYS,true);
         this.var_109.addChild(this.var_118);
         this.var_111 = new Bitmap(null,PixelSnapping.ALWAYS,true);
         this.var_111.visible = false;
         this.var_109.addChild(this.var_111);
         var _loc4_:uint = uint(this.var_538.numChildren);
         _loc3_ = 0;
         while(_loc3_ < _loc4_)
         {
            (_loc19_ = this.var_538.getChildAt(_loc3_) as MovieClip).mouseChildren = false;
            _loc19_.mouseEnabled = false;
            _loc19_.visible = false;
            _loc3_++;
         }
         this.var_109.addChild(this.var_538);
         _loc4_ = uint(this.var_515.numChildren);
         _loc3_ = 0;
         while(_loc3_ < _loc4_)
         {
            (_loc20_ = this.var_515.getChildAt(_loc3_) as MovieClip).addEventListener(MouseEvent.CLICK,this.method_883);
            _loc20_.addEventListener(MouseEvent.ROLL_OVER,this.method_694);
            _loc20_.addEventListener(MouseEvent.ROLL_OUT,this.method_897);
            _loc3_++;
         }
         this.var_109.addChild(this.var_515);
         var _loc5_:MovieClip = _loc2_.am_Cutouts;
         this.var_349 = new Dictionary();
         this.var_1360 = new Vector.<class_159>();
         _loc4_ = uint(_loc5_.numChildren);
         _loc3_ = 0;
         while(_loc3_ < _loc4_)
         {
            if(_loc23_ = (_loc22_ = (_loc21_ = _loc5_.getChildAt(_loc3_) as MovieClip).name).substr(3))
            {
               _loc24_ = _loc21_.x;
               _loc25_ = _loc21_.y;
               _loc26_ = Camera.SCREEN_WIDTH / _loc21_.width;
               _loc27_ = _loc21_.am_Header;
               _loc21_.removeChild(_loc27_);
               _loc21_.x = 0;
               _loc21_.y = 0;
               _loc28_ = new class_159(_loc23_,_loc24_,_loc25_,_loc26_,_loc27_.x,_loc27_.y,_loc21_);
               this.var_349[_loc23_] = _loc28_;
               this.var_349[_loc23_ + const_363] = _loc28_;
               this.var_1360.push(_loc28_);
            }
            _loc3_++;
         }
         var _loc6_:MovieClip;
         var _loc7_:uint = uint((_loc6_ = _loc2_.am_Roads).numChildren);
         this.var_632 = new Dictionary();
         _loc3_ = 0;
         while(_loc3_ < _loc7_)
         {
            (_loc29_ = _loc6_.getChildAt(_loc3_) as MovieClip).gotoAndStop(1);
            _loc30_ = _loc29_.name;
            this.var_632[_loc30_] = _loc29_;
            this.var_632[_loc30_ + const_363] = _loc29_;
            _loc3_++;
         }
         var _loc8_:MovieClip;
         var _loc9_:uint = uint((_loc8_ = _loc2_.am_Markers).numChildren);
         this.var_756 = new Dictionary();
         _loc3_ = 0;
         while(_loc3_ < _loc9_)
         {
            _loc32_ = (_loc31_ = _loc8_.getChildAt(_loc3_) as MovieClip).name;
            this.var_756[_loc32_] = _loc31_;
            this.var_756[_loc32_ + const_363] = _loc31_;
            _loc3_++;
         }
         this.var_608 = new MovieClip();
         this.var_109.addChild(this.var_608);
         this.var_1107 = new MovieClip();
         this.var_109.addChild(this.var_1107);
         this.var_1432 = method_10(var_2.am_Zoom,this.method_1637);
         method_23(var_2.am_Exit);
         var _loc10_:MovieClip = class_4.method_16("a_MapScrollHeader");
         this.var_1511 = method_1(_loc10_);
         this.var_109.addChild(_loc10_);
         var _loc11_:Entity;
         var _loc12_:String = !!(_loc11_ = var_1.clientEnt) ? _loc11_.entType.entName : "";
         this.var_1340 = this.method_555(0,_loc12_);
         var _loc13_:MovieClip = class_4.method_16("a_MapCardQuest");
         this.var_1288 = method_1(_loc13_);
         this.var_2066 = method_17(_loc13_.am_ProgressBar,"Progress",0);
         this.var_109.addChild(_loc13_);
         var _loc14_:MovieClip = class_4.method_16("a_MapCardQuestFlipped");
         this.var_1084 = method_1(_loc14_);
         this.var_2318 = method_17(_loc14_.am_ProgressBar,"Progress",0);
         this.var_109.addChild(_loc14_);
         var _loc15_:MovieClip = class_4.method_16("a_MapCardNewQuest");
         this.var_1250 = method_1(_loc15_);
         this.var_109.addChild(_loc15_);
         var _loc16_:MovieClip = class_4.method_16("a_MapCardNewQuestFlipped");
         this.var_1185 = method_1(_loc16_);
         this.var_109.addChild(_loc16_);
         var _loc17_:MovieClip = class_4.method_16("a_MapCardDungeon");
         method_144(_loc17_.am_StarRating,0);
         this.var_1165 = method_1(_loc17_);
         this.var_109.addChild(_loc17_);
         var _loc18_:MovieClip = class_4.method_16("a_MapCardDungeonFlipped");
         method_144(_loc18_.am_StarRating,0);
         this.var_1286 = method_1(_loc18_);
         this.var_109.addChild(_loc18_);
         this.var_691 = new Dictionary();
         this.var_1487 = const_820;
      }
      
      override public function OnDestroyScreen() : void
      {
         var _loc1_:String = null;
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         var _loc4_:MovieClip = null;
         var _loc5_:class_159 = null;
         this.method_795();
         this.method_517(this.var_1340);
         this.var_1340 = null;
         this.var_1994 = null;
         this.var_2391 = null;
         this.var_2181 = null;
         this.var_538 = null;
         this.var_109 = null;
         this.var_1107 = null;
         this.var_608 = null;
         if(this.var_691)
         {
            for(_loc1_ in this.var_691)
            {
               delete this.var_691[_loc1_];
            }
            this.var_691 = null;
         }
         if(this.var_632)
         {
            for(_loc1_ in this.var_632)
            {
               delete this.var_632[_loc1_];
            }
            this.var_632 = null;
         }
         if(this.var_756)
         {
            for(_loc1_ in this.var_756)
            {
               delete this.var_756[_loc1_];
            }
            this.var_756 = null;
         }
         if(this.var_515)
         {
            _loc2_ = uint(this.var_515.numChildren);
            _loc3_ = 0;
            while(_loc3_ < _loc2_)
            {
               (_loc4_ = this.var_515.getChildAt(_loc3_) as MovieClip).removeEventListener(MouseEvent.MOUSE_DOWN,this.method_883);
               _loc4_.removeEventListener(MouseEvent.ROLL_OVER,this.method_694);
               _loc4_.removeEventListener(MouseEvent.ROLL_OUT,this.method_897);
               _loc3_++;
            }
            this.var_515 = null;
         }
         if(this.var_349)
         {
            for(_loc1_ in this.var_349)
            {
               delete this.var_349[_loc1_];
            }
            this.var_349 = null;
         }
         if(this.var_1360)
         {
            for each(_loc5_ in this.var_1360)
            {
               _loc5_.method_1696();
            }
            this.var_1360 = null;
         }
         if(this.var_118)
         {
            this.var_118.bitmapData = null;
            if(this.var_118.parent)
            {
               this.var_118.parent.removeChild(this.var_118);
            }
            this.var_118 = null;
         }
         if(this.var_111)
         {
            this.var_111.bitmapData = null;
            if(this.var_111.parent)
            {
               this.var_111.parent.removeChild(this.var_111);
            }
            this.var_111 = null;
         }
         this.var_2263 = null;
         this.var_985 = null;
         this.var_1432 = null;
         this.var_1511 = null;
         this.var_1288 = null;
         this.var_2066 = null;
         this.var_1084 = null;
         this.var_2318 = null;
         this.var_1250 = null;
         this.var_1185 = null;
         this.var_1165 = null;
         this.var_1286 = null;
         this.var_513 = null;
         this.var_711 = null;
         this.var_1099 = null;
         this.mActivePath = null;
      }
      
      public function OnInitDisplay() : void
      {
         var _loc1_:String = String(var_1.level.internalName);
         this.var_102 = Level.method_182(_loc1_);
         if(!this.var_102)
         {
            this.var_102 = const_378;
         }
         if(Boolean(this.var_118) && this.var_102 != this.var_1387)
         {
            this.var_118.bitmapData = null;
         }
         if(var_1.mTutorialStage == Game.const_150)
         {
            var_1.SetNewTutorialStage(Game.const_266);
         }
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:Bitmap = null;
         var _loc10_:Number = NaN;
         var _loc11_:Number = NaN;
         var _loc12_:BitmapData = null;
         var _loc13_:Matrix = null;
         var _loc14_:MovieClip = null;
         var _loc15_:Stage = null;
         var _loc16_:BitmapData = null;
         var _loc17_:String = null;
         var _loc19_:Mission = null;
         var _loc20_:class_13 = null;
         var _loc21_:uint = 0;
         var _loc22_:uint = 0;
         var _loc23_:Dictionary = null;
         var _loc24_:Dictionary = null;
         var _loc25_:String = null;
         var _loc26_:MovieClip = null;
         var _loc27_:MovieClip = null;
         var _loc28_:MovieClip = null;
         var _loc29_:MovieClip = null;
         var _loc1_:class_159 = this.var_349[this.var_102];
         if(!_loc1_)
         {
            return;
         }
         this.method_738();
         var _loc2_:Boolean = Boolean(var_1.InHardMode());
         var _loc3_:String = _loc2_ ? const_363 : const_820;
         if(this.var_1487 != _loc3_)
         {
            this.method_593();
         }
         this.var_1487 = _loc3_;
         var _loc4_:MovieClip;
         (_loc4_ = this.var_1511.mMovieClip).x = _loc1_.var_2759;
         _loc4_.y = _loc1_.var_2842;
         var _loc5_:String;
         if(_loc5_ = Level.method_73(this.var_102))
         {
            MathUtil.method_2(_loc4_.am_Zone.am_Name,_loc5_);
         }
         else if(var_1.mbSleepingLands)
         {
            MathUtil.method_2(_loc4_.am_Zone.am_Name,_loc2_ ? "The Nightmare Lands" : "The Sleeping Lands");
         }
         else
         {
            MathUtil.method_2(_loc4_.am_Zone.am_Name,_loc2_ ? "Ruins of Ellyria" : "Kingdom of Ellyria");
         }
         if(this.var_1387 != this.var_102)
         {
            _loc6_ = Number(var_1.main.overallScale);
            _loc7_ = this.var_109.scaleX * _loc6_;
            _loc8_ = this.var_109.scaleY * _loc6_;
            if(!_loc1_.var_509 && !(DevSettings.flags & DevSettings.DEVFLAG_NO_GRAPHICS))
            {
               this.var_2391.visible = _loc2_;
               _loc9_ = new Bitmap(null,PixelSnapping.ALWAYS,true);
               _loc10_ = _loc7_ * _loc1_.var_586;
               _loc11_ = _loc8_ * _loc1_.var_586;
               _loc12_ = new BitmapData(_loc7_ * Camera.SCREEN_WIDTH,_loc8_ * Camera.PLAY_SCREEN_HEIGHT,true,0);
               _loc13_ = new Matrix(_loc10_,0,0,_loc11_,-_loc1_.var_1287 * _loc10_,-_loc1_.var_1208 * _loc11_);
               _loc12_.drawWithQuality(this.var_1994,_loc13_,null,null,null,true,StageQuality.HIGH);
               _loc9_.bitmapData = _loc12_;
               (_loc14_ = _loc1_.var_2055).scaleX = _loc7_;
               _loc14_.scaleY = _loc8_;
               _loc15_ = var_1.main.stage;
               _loc9_.mask = _loc14_;
               _loc9_.cacheAsBitmap = true;
               _loc14_.cacheAsBitmap = true;
               _loc15_.addChild(_loc9_);
               _loc15_.addChild(_loc14_);
               (_loc16_ = new BitmapData(_loc12_.width,_loc12_.height,true,0)).drawWithQuality(_loc9_,null,null,null,null,false,StageQuality.HIGH);
               _loc1_.var_509 = _loc16_;
               _loc9_.cacheAsBitmap = false;
               _loc14_.cacheAsBitmap = false;
               _loc15_.removeChild(_loc9_);
               _loc15_.removeChild(_loc14_);
            }
            if(this.var_118.bitmapData)
            {
               this.var_1106 = getTimer();
               if(this.var_102 != const_378)
               {
                  this.var_2222 = false;
                  this.var_111.bitmapData = _loc1_.var_509;
                  this.var_111.alpha = 0;
                  this.var_118.alpha = 1;
               }
               else
               {
                  this.var_2222 = true;
                  this.var_2263 = this.var_349[this.var_1387];
                  this.var_111.bitmapData = this.var_118.bitmapData;
                  this.var_118.bitmapData = _loc1_.var_509;
                  this.var_111.alpha = 1;
                  this.var_111.scaleX = this.var_118.scaleX;
                  this.var_111.scaleY = this.var_118.scaleY;
                  this.var_118.alpha = 0;
               }
               this.var_111.visible = true;
               this.var_1432.Hide();
               this.var_538.visible = false;
               this.var_608.visible = false;
               this.var_1107.visible = false;
            }
            if(!this.var_1106)
            {
               this.method_842();
            }
            this.var_1511.PlayAnimation("Ready");
            this.var_1511.TickMovieClip();
            this.var_1387 = this.var_102;
         }
         this.method_795();
         this.var_985 = null;
         this.var_578 = new Dictionary();
         this.var_1288.Hide();
         this.var_1084.Hide();
         this.var_1250.Hide();
         this.var_1185.Hide();
         this.var_1165.Hide();
         this.var_1286.Hide();
         if(this.var_102)
         {
            _loc23_ = new Dictionary();
            _loc24_ = new Dictionary();
            for each(_loc20_ in class_14.var_238)
            {
               if(_loc20_.var_431 != this.var_102)
               {
                  if(!_loc20_.var_186)
                  {
                     continue;
                  }
                  if(_loc20_.var_186 != this.var_102)
                  {
                     if(this.var_102 != "OldMineMountain" && this.var_102 != "OldMineMountainHard")
                     {
                        continue;
                     }
                     if(_loc20_.var_431 != "EmeraldGlades" && _loc20_.var_431 != "EmeraldGladesHard")
                     {
                        continue;
                     }
                     if(_loc20_.var_186 != "BridgeTown" && _loc20_.var_186 != "BridgeTownHard")
                     {
                        continue;
                     }
                  }
               }
               if(!(!(_loc19_ = var_1.mMissionInfoList[_loc20_.missionID]) && !var_1.HasCompletedPreReqs(_loc20_)))
               {
                  if(!_loc19_)
                  {
                     if(_loc20_.var_160)
                     {
                        _loc22_ = const_1283;
                        _loc17_ = _loc20_.var_160;
                     }
                     else if(_loc20_.var_134 && !_loc20_.var_319 && _loc20_.var_231 >= class_13.const_584)
                     {
                        _loc22_ = const_597;
                        _loc17_ = _loc20_.var_134;
                     }
                     else
                     {
                        _loc22_ = 0;
                        _loc17_ = null;
                     }
                  }
                  else if(_loc19_.var_145 == Mission.const_58)
                  {
                     if(Boolean(_loc20_.var_186) && _loc20_.var_186 != this.var_102)
                     {
                        _loc22_ = const_659;
                        _loc17_ = this.var_102 + "_" + _loc20_.var_186;
                     }
                     else
                     {
                        _loc22_ = const_1237;
                        _loc17_ = _loc20_.var_319;
                     }
                  }
                  else if(_loc19_.var_145 == Mission.const_213)
                  {
                     if(_loc20_.var_134)
                     {
                        _loc22_ = const_597;
                        _loc17_ = _loc20_.var_134;
                     }
                     else if(_loc20_.var_1323)
                     {
                        _loc22_ = const_659;
                        _loc17_ = _loc20_.var_1323;
                     }
                     else
                     {
                        _loc22_ = const_896;
                        _loc17_ = _loc20_.var_160;
                     }
                  }
                  else if(_loc20_.var_134)
                  {
                     if(_loc19_.var_588 >= 10)
                     {
                        _loc22_ = const_1199;
                     }
                     else if(_loc19_.var_588 >= 8)
                     {
                        _loc22_ = const_1150;
                     }
                     else
                     {
                        _loc22_ = const_1225;
                     }
                     _loc17_ = _loc20_.var_134;
                     _loc24_[_loc17_] = _loc19_.var_588;
                  }
                  else
                  {
                     _loc22_ = 0;
                     _loc17_ = null;
                  }
                  if(_loc17_)
                  {
                     _loc21_ = uint(_loc23_[_loc17_]);
                     if(_loc22_ > _loc21_)
                     {
                        this.var_578[_loc17_] = _loc20_;
                        _loc23_[_loc17_] = _loc22_;
                     }
                  }
               }
            }
            for(_loc17_ in _loc23_)
            {
               _loc25_ = "am_" + _loc17_;
               _loc21_ = uint(_loc23_[_loc17_]);
               _loc26_ = this.var_756[_loc25_];
               _loc20_ = this.var_578[_loc17_];
               if(!(!_loc26_ || !_loc20_ || !_loc21_))
               {
                  (_loc28_ = class_4.method_16("a_MapMarkerSimple")).mouseEnabled = true;
                  _loc28_.name = _loc25_;
                  _loc28_.gotoAndStop(_loc21_);
                  _loc28_.addEventListener(MouseEvent.MOUSE_DOWN,this.method_704);
                  _loc28_.addEventListener(MouseEvent.ROLL_OVER,this.method_858);
                  _loc28_.addEventListener(MouseEvent.ROLL_OUT,this.method_669);
                  if(_loc29_ = _loc28_.am_Stars)
                  {
                     method_144(_loc29_,_loc24_[_loc17_]);
                  }
                  if(_loc27_ = _loc28_.am_Selected)
                  {
                     if(var_1.mTrackedMission != _loc20_)
                     {
                        _loc27_.visible = false;
                     }
                     else
                     {
                        _loc27_.visible = true;
                        this.var_985 = _loc28_;
                     }
                  }
                  _loc28_.x = (_loc26_.x - _loc1_.var_1287) * _loc1_.var_586;
                  _loc28_.y = (_loc26_.y - _loc1_.var_1208) * _loc1_.var_586;
                  this.var_608.addChild(_loc28_);
               }
            }
         }
      }
      
      private function method_795() : void
      {
         var _loc1_:MovieClip = null;
         var _loc2_:String = null;
         if(this.var_608)
         {
            while(this.var_608.numChildren)
            {
               _loc1_ = this.var_608.removeChildAt(0) as MovieClip;
               _loc1_.removeEventListener(MouseEvent.CLICK,this.method_704);
               _loc1_.removeEventListener(MouseEvent.ROLL_OVER,this.method_858);
               _loc1_.removeEventListener(MouseEvent.ROLL_OUT,this.method_669);
            }
         }
         if(this.var_578)
         {
            for(_loc2_ in this.var_578)
            {
               delete this.var_578[_loc2_];
            }
            this.var_578 = null;
         }
      }
      
      private function method_704(param1:MouseEvent) : void
      {
         var _loc10_:MovieClip = null;
         var _loc11_:class_33 = null;
         var _loc2_:MovieClip = param1.target as MovieClip;
         var _loc3_:String = _loc2_.name.substr(3);
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_13;
         if(!(_loc4_ = this.var_578[_loc3_]))
         {
            return;
         }
         if(var_1.mTrackedMission == _loc4_)
         {
            return;
         }
         var _loc5_:Level;
         var _loc6_:String = (_loc5_ = var_1.level).internalName;
         var _loc7_:String;
         if((_loc7_ = Level.method_182(_loc6_)) != _loc4_.var_431 && !_loc4_.var_186)
         {
            return;
         }
         var _loc8_:Mission = var_1.mMissionInfoList[_loc4_.missionID];
         if(_loc5_.bInstanced && (!_loc8_ || _loc4_.var_186))
         {
            return;
         }
         var _loc9_:* = _loc2_.x <= const_490;
         if(!_loc8_ || _loc8_.var_145 != Mission.const_72)
         {
            if(_loc10_ = _loc2_.am_Selected)
            {
               _loc10_.visible = true;
            }
            if(!_loc8_)
            {
               _loc11_ = _loc9_ ? this.var_1250 : this.var_1185;
            }
            else if(Boolean(_loc4_.var_134) && _loc8_.var_145 != Mission.const_58)
            {
               _loc11_ = _loc9_ ? this.var_1165 : this.var_1286;
            }
            else
            {
               _loc11_ = _loc9_ ? this.var_1288 : this.var_1084;
            }
            _loc11_.mMovieClip.am_Selected.visible = true;
            if(Boolean(this.var_985) && Boolean(this.var_985.am_Selected))
            {
               this.var_985.am_Selected.visible = false;
            }
            this.var_985 = _loc2_;
            var_1.SelectMissionToTrack(_loc4_);
         }
      }
      
      private function method_858(param1:MouseEvent) : void
      {
         var _loc5_:MovieClip = null;
         var _loc6_:String = null;
         var _loc7_:String = null;
         var _loc8_:class_33 = null;
         var _loc9_:class_33 = null;
         var _loc2_:MovieClip = param1.target as MovieClip;
         var _loc3_:String = _loc2_.name.substr(3);
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_13;
         if(!(_loc4_ = this.var_578[_loc3_]))
         {
            return;
         }
         var _loc10_:* = _loc2_.x <= const_490;
         var _loc11_:Mission;
         if(!(_loc11_ = var_1.mMissionInfoList[_loc4_.missionID]))
         {
            _loc5_ = (_loc8_ = _loc10_ ? this.var_1250 : this.var_1185).mMovieClip;
            MathUtil.method_2(_loc5_.am_ContactName,class_35.const_379[_loc4_.var_160]);
            MathUtil.method_2(_loc5_.am_Name,_loc4_.displayName);
            _loc8_.Show();
         }
         else if(Boolean(_loc4_.var_134) && _loc11_.var_145 != Mission.const_58)
         {
            if(_loc11_.var_145 != Mission.const_72)
            {
               _loc6_ = "Active";
            }
            else if(_loc11_.var_588 >= 10)
            {
               _loc6_ = "Gold";
            }
            else if(_loc11_.var_588 >= 8)
            {
               _loc6_ = "Silver";
            }
            else
            {
               _loc6_ = "Bronze";
            }
            _loc5_ = (_loc8_ = _loc10_ ? this.var_1165 : this.var_1286).mMovieClip;
            MathUtil.method_2(_loc5_.am_Name,_loc4_.displayName);
            MathUtil.method_2(_loc5_.am_Score,!!_loc11_.var_1745 ? MathUtil.method_29(_loc11_.var_1745,true) : "");
            MathUtil.method_2(_loc5_.am_Description,_loc4_.description);
            method_144(_loc5_.am_StarRating,_loc11_.var_588);
            _loc8_.Show();
            _loc8_.PlayAnimation(_loc6_);
            _loc8_.TickMovieClip();
         }
         else
         {
            _loc8_ = _loc10_ ? this.var_1288 : this.var_1084;
            _loc9_ = _loc10_ ? this.var_2066 : this.var_2318;
            _loc5_ = _loc8_.mMovieClip;
            if(_loc11_.var_145 == Mission.const_213)
            {
               _loc6_ = !!_loc4_.var_1323 ? "Target" : "Active";
               _loc7_ = _loc4_.var_160;
               _loc9_.mHealthPerc = _loc11_.currCount / _loc4_.var_908;
               MathUtil.method_2(_loc5_.am_ProgressText,_loc11_.currCount + "/" + _loc4_.var_908);
            }
            else if(Boolean(_loc4_.var_186) && _loc4_.var_186 != this.var_102)
            {
               _loc6_ = "Target";
               _loc7_ = this.var_102 + "_" + _loc4_.var_186;
               _loc9_.mHealthPerc = 0;
               MathUtil.method_2(_loc5_.am_ProgressText,"0/1");
            }
            else
            {
               _loc6_ = "Return";
               _loc7_ = _loc4_.var_319;
               _loc9_.mHealthPerc = 100;
               MathUtil.method_2(_loc5_.am_ProgressText,"Quest Complete");
            }
            MathUtil.method_2(_loc5_.am_ContactName,class_35.const_379[_loc7_]);
            MathUtil.method_2(_loc5_.am_Name,_loc4_.displayName);
            MathUtil.method_2(_loc5_.am_Description,_loc4_.description);
            _loc8_.Show();
            _loc8_.PlayAnimation(_loc6_);
            _loc8_.TickMovieClip();
            _loc9_.TickMovieClip();
         }
         _loc5_.x = _loc2_.x;
         _loc5_.y = _loc2_.y;
         _loc5_.am_Selected.visible = var_1.mTrackedMission == _loc4_;
      }
      
      private function method_669(param1:MouseEvent) : void
      {
         var _loc5_:class_33 = null;
         var _loc2_:MovieClip = param1.target as MovieClip;
         var _loc3_:String = _loc2_.name.substr(3);
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_13;
         if(!(_loc4_ = this.var_578[_loc3_]))
         {
            return;
         }
         var _loc6_:* = _loc2_.x <= const_490;
         var _loc7_:Mission;
         if(!(_loc7_ = var_1.mMissionInfoList[_loc4_.missionID]))
         {
            _loc5_ = _loc6_ ? this.var_1250 : this.var_1185;
         }
         else if(Boolean(_loc4_.var_134) && _loc7_.var_145 != Mission.const_58)
         {
            _loc5_ = _loc6_ ? this.var_1165 : this.var_1286;
         }
         else
         {
            _loc5_ = _loc6_ ? this.var_1288 : this.var_1084;
         }
         _loc5_.Hide();
      }
      
      override public function OnTickScreen() : void
      {
         var _loc1_:class_159 = null;
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:uint = 0;
         var _loc6_:Number = NaN;
         var _loc7_:class_159 = null;
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         var _loc10_:Number = NaN;
         if(this.var_1106)
         {
            _loc1_ = this.var_349[this.var_102];
            _loc2_ = Number(var_1.main.overallScale);
            _loc3_ = this.var_109.scaleX * _loc2_;
            _loc4_ = this.var_109.scaleY * _loc2_;
            if((_loc5_ = var_1.mTimeThisTick - this.var_1106) >= const_679)
            {
               this.var_1106 = 0;
               this.method_842();
            }
            else
            {
               if((_loc6_ = (var_1.mTimeThisTick - this.var_1106) / const_679) < 0)
               {
                  _loc6_ = 0;
               }
               _loc7_ = _loc1_;
               if(this.var_2222)
               {
                  _loc6_ = 1 - _loc6_;
                  _loc7_ = this.var_2263;
               }
               _loc9_ = (_loc8_ = 1 / _loc7_.var_586) + _loc6_ * (1 - _loc8_);
               _loc10_ = 1 - _loc6_;
               this.var_111.scaleX = _loc9_ / _loc3_;
               this.var_111.scaleY = _loc9_ / _loc4_;
               this.var_111.x = _loc7_.var_1287 * _loc10_;
               this.var_111.y = _loc7_.var_1208 * _loc10_;
               this.var_111.alpha = _loc6_;
               this.var_118.alpha = _loc10_;
            }
         }
      }
      
      private function method_738() : void
      {
         if(this.var_102 != const_378)
         {
            this.var_1432.Show();
            this.var_515.visible = false;
            this.var_538.visible = false;
         }
         else
         {
            this.var_1432.Hide();
            this.var_515.visible = true;
            this.var_538.visible = true;
         }
         this.var_608.visible = true;
         this.var_1107.visible = true;
         var_2.am_InfoText.visible = this.var_102 == "NewbieRoad";
      }
      
      private function method_842() : void
      {
         var _loc1_:class_159 = this.var_349[this.var_102];
         var _loc2_:Number = Number(var_1.main.overallScale);
         var _loc3_:Number = this.var_109.scaleX * _loc2_;
         var _loc4_:Number = this.var_109.scaleY * _loc2_;
         this.var_118.bitmapData = _loc1_.var_509;
         this.var_118.scaleX = 1 / _loc3_;
         this.var_118.scaleY = 1 / _loc4_;
         this.var_118.alpha = 1;
         this.var_111.visible = false;
         this.method_738();
      }
      
      public function method_593() : void
      {
         var _loc1_:BitmapData = null;
         var _loc2_:class_159 = null;
         for each(_loc2_ in this.var_349)
         {
            _loc1_ = _loc2_.var_509;
            if(_loc1_)
            {
               _loc1_.dispose();
               _loc2_.var_509 = null;
            }
         }
         if(this.var_118)
         {
            this.var_118.bitmapData = null;
         }
         if(this.var_111)
         {
            this.var_111.bitmapData = null;
         }
         this.var_1387 = null;
      }
      
      private function method_883(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = param1.target as MovieClip;
         var _loc3_:String = _loc2_.name.substr(3);
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_33;
         if(_loc4_ = this.var_691[_loc3_])
         {
            _loc4_.Hide();
         }
         this.var_102 = _loc3_ + this.var_1487;
         Refresh();
      }
      
      private function method_694(param1:MouseEvent) : void
      {
         var _loc8_:MovieClip = null;
         var _loc9_:MovieClip = null;
         var _loc2_:MovieClip = param1.target as MovieClip;
         var _loc3_:String = _loc2_.name.substr(3);
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_33;
         if(!(_loc4_ = this.var_691[_loc3_]))
         {
            _loc8_ = this.var_2181["am_" + _loc3_];
            _loc9_ = class_4.method_16("a_Slugline");
            if(_loc8_)
            {
               _loc9_.x = _loc8_.x;
               _loc9_.y = _loc8_.y;
            }
            this.var_109.addChild(_loc9_);
            _loc4_ = method_1(_loc9_);
            this.var_691[_loc3_] = _loc4_;
         }
         _loc4_.Show();
         _loc4_.PlayAnimation("FadeIn");
         var _loc5_:String = _loc3_ + this.var_1487;
         var _loc6_:String = Level.method_73(_loc5_);
         MathUtil.method_2(_loc4_.mMovieClip.am_TextWrap.am_ZoneSet,_loc6_);
         var _loc7_:MovieClip;
         if(_loc7_ = this.var_538["am_" + _loc3_])
         {
            _loc7_.visible = true;
         }
      }
      
      private function method_897(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = param1.target as MovieClip;
         var _loc3_:String = _loc2_.name.substr(3);
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_33;
         if(_loc4_ = this.var_691[_loc3_])
         {
            _loc4_.PlayAnimation("FadeIn",class_33.const_80 | class_33.const_14);
         }
         var _loc5_:MovieClip;
         if(_loc5_ = this.var_538["am_" + _loc3_])
         {
            _loc5_.visible = false;
         }
      }
      
      private function method_1637(param1:MouseEvent) : void
      {
         this.var_102 = const_378;
         Refresh();
      }
      
      public function method_320() : void
      {
         var _loc4_:uint = 0;
         var _loc5_:Level = null;
         var _loc6_:int = 0;
         var _loc7_:int = 0;
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         var _loc10_:String = null;
         var _loc11_:class_158 = null;
         var _loc12_:* = false;
         var _loc13_:uint = 0;
         var _loc14_:Vector.<Number> = null;
         var _loc15_:Vector.<Number> = null;
         var _loc16_:Number = NaN;
         var _loc17_:Number = NaN;
         var _loc18_:int = 0;
         var _loc19_:int = 0;
         var _loc20_:Number = NaN;
         var _loc21_:Number = NaN;
         var _loc22_:Number = NaN;
         var _loc23_:Number = NaN;
         var _loc24_:Number = NaN;
         var _loc25_:Number = NaN;
         var _loc26_:Number = NaN;
         var _loc27_:class_159 = null;
         var _loc28_:MovieClip = null;
         var _loc29_:class_133 = null;
         var _loc30_:Packet = null;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         if(this.var_711)
         {
            _loc4_ = 1;
            _loc5_ = var_1.level;
            _loc6_ = _loc1_.appearPosX;
            _loc7_ = _loc1_.appearPosY;
            _loc8_ = _loc5_.var_1090.left;
            _loc9_ = _loc5_.var_1090.right;
            _loc10_ = _loc5_.internalName;
            if(_loc11_ = method_408(_loc10_,_loc6_,_loc7_))
            {
               _loc4_ = _loc11_.var_2730;
               _loc8_ = _loc11_.var_2253;
               _loc9_ = _loc11_.var_2330;
            }
            _loc12_ = this.mActivePath != _loc11_;
            this.mActivePath = _loc11_;
            if(_loc12_)
            {
               var_1.screenQuestTracker.Refresh();
            }
            if((_loc13_ = _loc4_ - 1) >= this.var_711.length)
            {
               _loc13_ = 0;
            }
            _loc14_ = this.var_711[_loc13_];
            _loc15_ = this.var_1099[_loc13_];
            _loc16_ = _loc14_.length - 1;
            if((_loc17_ = (_loc1_.appearPosX - _loc8_) * _loc16_ / (_loc9_ - _loc8_)) < 0)
            {
               _loc17_ = 0;
            }
            if(_loc17_ >= _loc16_)
            {
               _loc17_ = _loc16_;
            }
            if((_loc18_ = int(uint(_loc17_))) < 0)
            {
               _loc18_ = 0;
            }
            if(_loc18_ >= _loc16_)
            {
               _loc18_ = _loc16_;
            }
            if((_loc19_ = _loc18_ + 1) >= _loc16_)
            {
               _loc19_ = _loc16_;
            }
            _loc20_ = _loc14_[_loc18_];
            _loc21_ = _loc15_[_loc18_];
            _loc22_ = _loc14_[_loc19_];
            _loc23_ = _loc15_[_loc19_];
            _loc24_ = _loc17_ - Number(_loc18_);
            _loc25_ = _loc20_ + (_loc22_ - _loc20_) * _loc24_;
            _loc26_ = _loc21_ + (_loc23_ - _loc21_) * _loc24_;
            _loc2_ = uint(_loc25_);
            _loc3_ = uint(_loc26_);
            if(_loc27_ = this.var_349[this.var_102])
            {
               this.var_1340.x = (_loc25_ - _loc27_.var_1287) * _loc27_.var_586;
               this.var_1340.y = (_loc26_ - _loc27_.var_1208) * _loc27_.var_586;
               for each(_loc29_ in var_1.groupmates)
               {
                  if(_loc28_ = _loc29_.var_623)
                  {
                     _loc28_.x = (_loc29_.var_2131 - _loc27_.var_1287) * _loc27_.var_586;
                     _loc28_.y = (_loc29_.var_2048 - _loc27_.var_1208) * _loc27_.var_586;
                  }
               }
            }
         }
         if(var_1.CanSendPacket() && var_1.groupmates.length && (_loc2_ != var_1.lastSentMapX || _loc3_ != var_1.lastSentMapY))
         {
            (_loc30_ = new Packet(LinkUpdater.const_874)).method_236(_loc2_);
            _loc30_.method_236(_loc3_);
            var_1.serverConn.SendPacket(_loc30_);
            var_1.lastSentMapX = _loc2_;
            var_1.lastSentMapY = _loc3_;
         }
      }
      
      public function method_1807() : void
      {
         var _loc4_:uint = 0;
         var _loc5_:MovieClip = null;
         var _loc6_:Vector.<Number> = null;
         var _loc7_:Vector.<Number> = null;
         if(!this.var_632)
         {
            Display();
            Hide();
         }
         var _loc1_:String = "am_" + var_1.level.internalName;
         this.var_513 = this.var_632[_loc1_];
         if(!this.var_513)
         {
            return;
         }
         var _loc2_:uint = 1;
         this.var_513.gotoAndStop(1);
         while(this.var_513["am_Path" + _loc2_])
         {
            _loc2_++;
         }
         _loc2_--;
         if(!_loc2_)
         {
            return;
         }
         this.var_711 = new Vector.<Vector.<Number>>(_loc2_,true);
         this.var_1099 = new Vector.<Vector.<Number>>(_loc2_,true);
         var _loc3_:uint = 0;
         while(_loc3_ < _loc2_)
         {
            this.var_711[_loc3_] = new Vector.<Number>();
            this.var_1099[_loc3_] = new Vector.<Number>();
            _loc3_++;
         }
         var _loc8_:Number = this.var_513.x;
         var _loc9_:Number = this.var_513.y;
         var _loc10_:uint = uint(this.var_513.totalFrames);
         var _loc11_:uint = 1;
         while(_loc11_ <= _loc10_)
         {
            this.var_513.gotoAndStop(_loc11_);
            _loc3_ = 0;
            while(_loc3_ < _loc2_)
            {
               _loc4_ = uint(_loc3_ + 1);
               if(_loc5_ = this.var_513["am_Path" + _loc4_])
               {
                  (_loc6_ = this.var_711[_loc3_]).push(_loc5_.x + _loc8_);
                  (_loc7_ = this.var_1099[_loc3_]).push(_loc5_.y + _loc9_);
               }
               _loc3_++;
            }
            _loc11_++;
         }
         _loc3_ = 0;
         while(_loc3_ < _loc2_)
         {
            (_loc6_ = this.var_711[_loc3_]).fixed = true;
            (_loc7_ = this.var_1099[_loc3_]).fixed = true;
            _loc3_++;
         }
      }
      
      private function method_699(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = param1.target as MovieClip;
         var_1.tooltip.TriggerTooltip("MAPTEAMMATE$" + _loc2_.name);
      }
      
      private function method_759(param1:MouseEvent) : void
      {
         var_1.tooltip.UntriggerTooltip();
      }
      
      public function method_517(param1:MovieClip) : void
      {
         param1.removeEventListener(MouseEvent.ROLL_OVER,this.method_699);
         param1.removeEventListener(MouseEvent.ROLL_OUT,this.method_759);
         if(param1.parent)
         {
            param1.parent.removeChild(param1);
         }
      }
      
      public function method_555(param1:uint, param2:String) : MovieClip
      {
         var _loc3_:MovieClip = class_4.method_16(!!param1 ? "a_MapMarkerPartyMember" : "a_MapMarker");
         _loc3_.name = param2;
         _loc3_.mouseEnabled = true;
         _loc3_.addEventListener(MouseEvent.ROLL_OVER,this.method_699);
         _loc3_.addEventListener(MouseEvent.ROLL_OUT,this.method_759);
         this.var_1107.addChild(_loc3_);
         return _loc3_;
      }
   }
}
