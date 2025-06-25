package
{
   import flash.display.DisplayObject;
   import flash.display.DisplayObjectContainer;
   import flash.display.LoaderInfo;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.geom.ColorTransform;
   import flash.geom.Matrix;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.system.ApplicationDomain;
   import flash.utils.Dictionary;
   import flash.utils.getQualifiedClassName;
   
   public class Level
   {
      
      public static const LEVELID:uint = 0;
      
      private static const const_425:Dictionary = new Dictionary();
      
      private static const const_336:uint = 1 << 0;
      
      private static const const_592:uint = 1 << 1;
      
      private static const const_305:uint = 1 << 2;
      
      private static const const_483:String = "ac_GenericEnt";
      
      private static const const_1223:uint = 1;
      
      private static const const_1222:uint = 0;
      
      private static const const_1296:uint = 4;
      
      private static const const_30:Boolean = Boolean(DevSettings.flags & DevSettings.DEVFLAG_SHOWCUES);
      
      private static const const_919:Boolean = Boolean(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT || DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT);
      
      {
         const_425["fireCycle"] = true;
         const_425["fireTiming"] = true;
      }
      
      internal var var_1:Game;
      
      internal var levelName:String = null;
      
      internal var mapLevel:uint = 0;
      
      internal var baseLevel:uint = 0;
      
      internal var var_2606:uint = 0;
      
      internal var var_2549:MovieClip = null;
      
      internal var var_239:Point = null;
      
      internal var var_2481:MovieClip = null;
      
      internal var var_1269:Point = null;
      
      internal var momentParamsString:String = null;
      
      internal var var_1550:Array;
      
      internal var internalName:String = null;
      
      internal var alterParamsString:String = null;
      
      internal var bInstanced:Boolean = false;
      
      internal var var_2070:a_LevelDirector;
      
      internal var var_2526:String = null;
      
      internal var var_1657:Boolean = false;
      
      internal var var_2911:int = 0;
      
      internal var var_2931:int = 0;
      
      internal var var_1666:int = 0;
      
      internal var var_1920:int = 0;
      
      internal var var_59:MovieClip;
      
      internal var var_1090:Rectangle;
      
      internal var var_1266:Number = 0;
      
      internal var var_1067:Number = 0;
      
      internal var var_299:Vector.<Room>;
      
      internal var var_264:Vector.<Door>;
      
      internal var targetList:Vector.<Door>;
      
      internal var var_1046:Dictionary;
      
      internal var var_1690:Dictionary;
      
      internal var var_456:Dictionary;
      
      internal var var_1140:Vector.<class_77>;
      
      internal var var_1214:MovieClip;
      
      internal var var_1143:String;
      
      internal var levelFileName:String;
      
      internal var levelSymbolName:String;
      
      internal var var_1119:Vector.<Sprite>;
      
      internal var var_2468:Boolean = false;
      
      internal var var_333:Boolean = false;
      
      internal var var_178:Sprite;
      
      internal var var_690:uint;
      
      internal var var_968:uint;
      
      internal var var_1270:uint;
      
      internal var var_728:uint;
      
      internal var var_1096:uint;
      
      internal var var_2081:Boolean;
      
      internal var var_2744:uint;
      
      internal var var_811:Vector.<GearType>;
      
      internal var var_1229:Vector.<SuperAnimInstance>;
      
      internal var mask:Sprite;
      
      internal var var_2480:uint;
      
      internal var var_1974:Number;
      
      internal var var_717:Dictionary;
      
      public function Level(param1:Game)
      {
         this.var_1046 = new Dictionary();
         this.var_1690 = new Dictionary();
         this.var_456 = new Dictionary();
         super();
         this.var_1 = param1;
         this.var_299 = new Vector.<Room>();
         this.var_264 = new Vector.<Door>();
         this.targetList = new Vector.<Door>();
         this.var_1140 = new Vector.<class_77>();
         this.var_178 = new Sprite();
      }
      
      public static function method_73(param1:String) : String
      {
         var _loc2_:class_2 = class_14.var_430[param1];
         return !!_loc2_ ? _loc2_.displayName : "";
      }
      
      public static function method_1476(param1:String) : String
      {
         var _loc2_:class_2 = class_14.var_430[param1];
         return !!_loc2_ ? _loc2_.var_2796 : null;
      }
      
      public static function method_182(param1:String) : String
      {
         var _loc2_:class_2 = class_14.var_430[param1];
         return !!_loc2_ ? _loc2_.var_431 : null;
      }
      
      public static function method_1551(param1:String) : String
      {
         var _loc2_:class_2 = class_14.var_430[param1];
         return !!_loc2_ ? _loc2_.var_2756 : null;
      }
      
      public function method_905() : void
      {
         var _loc1_:String = null;
         var _loc2_:String = null;
         var _loc3_:String = null;
         var _loc4_:Door = null;
         var _loc5_:Door = null;
         var _loc6_:Room = null;
         var _loc7_:class_77 = null;
         var _loc8_:String = null;
         var _loc9_:SuperAnimInstance = null;
         for(_loc1_ in this.var_456)
         {
            delete this.var_456[_loc1_];
         }
         this.var_456 = new Dictionary();
         for(_loc2_ in this.var_1046)
         {
            delete this.var_1046[_loc2_];
         }
         this.var_1046 = new Dictionary();
         for(_loc3_ in this.var_1690)
         {
            delete this.var_1690[_loc3_];
         }
         this.var_1690 = new Dictionary();
         for each(_loc4_ in this.var_264)
         {
            _loc4_.method_791();
         }
         this.var_264 = new Vector.<Door>();
         for each(_loc5_ in this.targetList)
         {
            _loc5_.method_791();
         }
         this.targetList = new Vector.<Door>();
         for each(_loc6_ in this.var_299)
         {
            _loc6_.method_1691();
         }
         this.var_299 = new Vector.<Room>();
         for each(_loc7_ in this.var_1140)
         {
            _loc7_.method_1050();
         }
         this.var_1140 = new Vector.<class_77>();
         if(Boolean(this.var_178) && Boolean(this.var_178.parent))
         {
            this.var_178.parent.removeChild(this.var_178);
         }
         this.var_178 = null;
         this.var_59 = null;
         this.var_1214 = null;
         this.var_2070 = null;
         this.var_1550 = null;
         this.var_2481 = null;
         this.var_1269 = null;
         this.var_2549 = null;
         this.var_239 = null;
         this.var_1 = null;
         this.var_811 = null;
         if(this.var_717)
         {
            for(_loc8_ in this.var_717)
            {
               delete this.var_717[_loc8_];
            }
            this.var_717 = null;
         }
         if(this.var_1229)
         {
            for each(_loc9_ in this.var_1229)
            {
               _loc9_.DestroySuperAnimInstance();
            }
            this.var_1229 = null;
         }
      }
      
      public function method_2001() : uint
      {
         if(!this.levelFileName)
         {
            return 0;
         }
         var _loc1_:class_34 = ResourceManager.method_471(this.levelFileName);
         if(!_loc1_ || !_loc1_.var_192)
         {
            return 0;
         }
         return 100 * (_loc1_.var_1649 / _loc1_.var_1295);
      }
      
      public function method_1853(param1:String, param2:uint, param3:uint, param4:String, param5:String, param6:String, param7:Boolean) : void
      {
         this.levelName = param1;
         this.mapLevel = param2;
         this.baseLevel = param3;
         this.internalName = param4;
         this.bInstanced = param7;
         this.momentParamsString = !!param5 ? param5 : "Normal";
         this.var_1550 = this.momentParamsString.split(",");
         this.alterParamsString = param6;
         var _loc8_:Array = this.levelName.split("/");
         this.levelFileName = _loc8_[0];
         this.levelSymbolName = _loc8_.length > 1 ? String(_loc8_[1]) : "a_Level";
         this.var_2606 = this.mapLevel > this.baseLevel ? uint(this.mapLevel - this.baseLevel) : 0;
         this.var_2468 = this.levelSymbolName == "a_Level_TutorialBoat";
         this.var_333 = this.levelSymbolName == "a_Level_Home";
         ResourceManager.method_143(this.levelFileName,"Level");
         ResourceManager.method_497("Level");
      }
      
      public function method_1195() : Boolean
      {
         var _loc7_:Sprite = null;
         var _loc9_:DisplayObject = null;
         var _loc10_:String = null;
         var _loc11_:MovieClip = null;
         var _loc12_:Room = null;
         var _loc13_:Rectangle = null;
         var _loc1_:LoaderInfo = ResourceManager.const_40[this.levelFileName];
         var _loc2_:Vector.<Sprite> = new Vector.<Sprite>();
         if(!_loc1_)
         {
            return false;
         }
         var _loc3_:ApplicationDomain = _loc1_.applicationDomain;
         if(!_loc3_.hasDefinition(this.levelSymbolName))
         {
            return false;
         }
         var _loc4_:Class = _loc3_.getDefinition(this.levelSymbolName) as Class;
         this.var_59 = new _loc4_();
         MathUtil.method_235(this.var_59);
         this.var_1119 = new Vector.<Sprite>();
         this.var_1.main.stage.addChild(this.var_59);
         this.var_1.levelLayer.x = 0;
         this.var_1.levelLayer.y = 0;
         this.var_1067 = 0;
         if(this.levelSymbolName == "a_Level_TutorialBoat")
         {
            this.var_1067 += 4000;
         }
         var _loc5_:uint = uint(this.var_59.numChildren);
         var _loc6_:uint = 0;
         while(_loc6_ < _loc5_)
         {
            _loc9_ = this.var_59.getChildAt(_loc6_);
            _loc10_ = getQualifiedClassName(_loc9_);
            if(Boolean(_loc9_.filters) && Boolean(_loc9_.filters.length))
            {
               _loc9_.filters = null;
               class_24.method_19("Object has Filters: " + _loc10_ + " - " + _loc9_.name);
            }
            if(!this.method_923(_loc9_))
            {
               _loc9_.visible = false;
            }
            else if(_loc10_ == "a_Handle")
            {
               _loc9_.visible = false;
            }
            else if(!_loc10_.indexOf("a_Room_"))
            {
               _loc11_ = _loc9_ as MovieClip;
               _loc12_ = new Room(this.var_1,_loc11_);
               this.var_299.push(_loc12_);
               _loc11_.gotoAndStop(1);
               if(Boolean(_loc11_) && _loc11_.hasOwnProperty("InitRoom"))
               {
                  _loc12_.var_122 = new a_GameHook(_loc12_);
                  _loc11_.InitRoom(_loc12_.var_122);
               }
               this.method_232(_loc11_,_loc12_,1,0,null,null);
               _loc12_.method_1874();
               if(!_loc12_.var_323)
               {
                  _loc12_.method_896("Basic");
               }
               if(_loc13_ = MathUtil.method_138(_loc11_,_loc11_))
               {
                  this.var_1067 += _loc13_.width;
               }
            }
            else if(!_loc10_.indexOf("a_Mask"))
            {
               this.mask = _loc9_ as Sprite;
               this.var_1119.push(this.mask);
            }
            else if(!_loc10_.indexOf("a_Soundscape"))
            {
               this.var_1214 = _loc9_ as MovieClip;
               this.var_1143 = _loc10_.split("_")[2];
               _loc9_.visible = const_30;
            }
            else if(!_loc10_.indexOf("a_Stinger"))
            {
               this.var_1214 = _loc9_ as MovieClip;
               this.var_1143 = _loc10_.split("_")[2];
               _loc9_.visible = const_30;
            }
            else if(!_loc10_.indexOf("a_LevelDirector"))
            {
               this.var_2070 = _loc9_ as a_LevelDirector;
               this.var_2526 = _loc10_.substr(2 + 13 + 1);
               _loc9_.visible = const_30;
            }
            else if(!_loc9_.name.indexOf(class_123.const_862))
            {
               _loc2_.push(_loc9_ as Sprite);
            }
            else if(!_loc10_.indexOf(class_123.const_1206))
            {
               this.var_1.var_77.method_802(_loc9_ as MovieClip);
               this.var_1119.push(_loc9_);
            }
            else
            {
               class_24.method_19("Unknown Object At Level Depth: " + _loc10_ + " - " + _loc9_.name);
               _loc9_.visible = false;
            }
            _loc6_++;
         }
         if(_loc2_.length)
         {
            this.var_1.var_77.method_1693(_loc2_);
         }
         this.var_1.var_77.method_1604();
         for each(_loc7_ in this.var_1119)
         {
            if(_loc7_ && Boolean(_loc7_.parent))
            {
               _loc7_.parent.removeChild(_loc7_);
            }
         }
         this.var_1119 = null;
         this.var_1090 = this.var_59.getBounds(this.var_59.parent);
         this.var_1266 = this.var_1090.bottom;
         if(this.var_59.parent)
         {
            this.var_59.parent.removeChild(this.var_59);
         }
         this.var_1.collMan.method_1043();
         this.method_194();
         if(this.levelSymbolName == "a_Level_SwampRoadNorth" || this.levelSymbolName == "a_Level_SwampRoadNorthHard")
         {
            this.method_663(!class_6.var_1677);
         }
         if(this.var_1.var_107)
         {
            this.var_1.var_107.method_120();
         }
         if(!this.var_239)
         {
            class_24.method_19("Level needs a PlayerSpawn");
         }
         this.var_690 = 0;
         this.var_2931 = this.var_1.mTimeThisTick;
         this.var_968 = 0;
         this.var_1270 = 0;
         this.var_728 = 0;
         this.var_1096 = 0;
         var _loc8_:uint = this.var_299.length;
         this.var_1974 = !!_loc8_ ? 100 / _loc8_ : 100;
         return true;
      }
      
      public function method_2055() : void
      {
         var _loc1_:class_37 = null;
         var _loc3_:String = null;
         var _loc4_:Boolean = false;
         var _loc5_:String = null;
         var _loc6_:Door = null;
         var _loc7_:Dictionary = null;
         var _loc8_:String = null;
         var _loc9_:Door = null;
         var _loc10_:Door = null;
         var _loc11_:Vector.<class_37> = null;
         var _loc12_:String = null;
         var _loc13_:Array = null;
         var _loc14_:String = null;
         var _loc15_:String = null;
         var _loc2_:Dictionary = new Dictionary();
         for(_loc3_ in this.var_1.collMan.var_259)
         {
            _loc11_ = this.var_1.collMan.var_259[_loc3_];
            for each(_loc1_ in _loc11_)
            {
               if(_loc1_.var_573)
               {
                  for each(_loc12_ in _loc1_.var_573)
                  {
                     if((_loc14_ = String((_loc13_ = _loc12_.split("_"))[0])) == "DoorLocal")
                     {
                        _loc15_ = String(_loc13_[1]);
                        _loc2_[_loc15_] = true;
                     }
                  }
               }
            }
         }
         _loc7_ = new Dictionary();
         for(_loc8_ in _loc2_)
         {
            _loc4_ = false;
            _loc5_ = _loc8_;
            for each(_loc6_ in this.targetList)
            {
               if(_loc6_.localTarget == _loc5_)
               {
                  _loc7_[_loc5_] = true;
                  _loc4_ = true;
               }
            }
            if(!_loc4_)
            {
               class_24.method_19("NO TARGET FOR LOCALDOOR COLLISION LINE am_LocalDoor_" + _loc5_);
            }
         }
         for each(_loc9_ in this.var_264)
         {
            _loc4_ = false;
            if(_loc5_ = _loc9_.localTarget)
            {
               for each(_loc6_ in this.targetList)
               {
                  if(_loc6_.localTarget == _loc5_ && _loc6_ != _loc9_)
                  {
                     _loc7_[_loc5_] = true;
                     _loc4_ = true;
                  }
               }
               if(!_loc4_)
               {
                  class_24.method_19("NO TARGET FOR LOCAL CLICK DOOR LocalDoor" + _loc5_);
               }
            }
         }
         for each(_loc10_ in this.targetList)
         {
            if(!_loc7_[_loc10_.localTarget])
            {
               class_24.method_19("UNTARGETTED TARGET " + _loc10_.localTarget);
            }
         }
      }
      
      public function method_923(param1:DisplayObject) : Boolean
      {
         var _loc3_:String = null;
         var _loc4_:int = 0;
         var _loc6_:String = null;
         var _loc2_:String = param1.name;
         if(!_loc2_ || _loc2_.indexOf("am_Moment") == -1)
         {
            return true;
         }
         var _loc5_:Array = _loc2_.split("$");
         for each(_loc6_ in _loc5_)
         {
            if(!_loc6_.indexOf("am_Moment"))
            {
               _loc4_ = _loc6_.lastIndexOf("_");
               _loc3_ = _loc6_.substr(_loc4_ + 1);
               if(this.var_1550.indexOf(_loc3_) != -1)
               {
                  return true;
               }
            }
         }
         return false;
      }
      
      public function method_232(param1:Sprite, param2:Room, param3:int, param4:uint, param5:String, param6:String) : void
      {
         var _loc14_:DisplayObject = null;
         var _loc15_:String = null;
         var _loc16_:String = null;
         var _loc17_:String = null;
         var _loc18_:String = null;
         var _loc19_:Matrix = null;
         var _loc20_:class_145 = null;
         var _loc21_:Array = null;
         var _loc22_:Point = null;
         var _loc23_:Array = null;
         var _loc24_:uint = 0;
         var _loc25_:Point = null;
         var _loc26_:Array = null;
         var _loc27_:LoaderInfo = null;
         var _loc28_:ApplicationDomain = null;
         var _loc29_:Sprite = null;
         var _loc30_:Array = null;
         var _loc31_:* = false;
         var _loc32_:String = null;
         var _loc33_:String = null;
         var _loc34_:String = null;
         var _loc35_:class_9 = null;
         var _loc36_:Class = null;
         var _loc37_:Sprite = null;
         var _loc38_:Class = null;
         var _loc39_:MovieClip = null;
         var _loc40_:Array = null;
         var _loc41_:Matrix = null;
         var _loc42_:uint = 0;
         var _loc43_:Matrix = null;
         var _loc44_:Rectangle = null;
         var _loc45_:class_11 = null;
         var _loc46_:String = null;
         var _loc47_:Matrix = null;
         var _loc48_:Rectangle = null;
         var _loc49_:String = null;
         var _loc50_:Matrix = null;
         var _loc51_:Rectangle = null;
         var _loc52_:Door = null;
         var _loc53_:MovieClip = null;
         var _loc54_:Sprite = null;
         var _loc55_:Matrix = null;
         var _loc56_:DisplayObjectContainer = null;
         var _loc57_:int = 0;
         var _loc58_:int = 0;
         var _loc59_:String = null;
         var _loc60_:class_147 = null;
         var _loc61_:int = 0;
         var _loc62_:int = 0;
         var _loc63_:int = 0;
         if(param1.x < Room.ROOM_MIN_X || param1.x > Room.ROOM_MAX_X)
         {
            class_24.method_19(getQualifiedClassName(param1) + " outside of valid x-bounds: " + param1.x);
         }
         if(param1.y < Room.ROOM_MIN_Y || param1.y > Room.ROOM_MAX_Y)
         {
            class_24.method_19(getQualifiedClassName(param1) + " outside of valid y-bounds: " + param1.y);
         }
         var _loc7_:Door = null;
         var _loc8_:DisplayObject = null;
         var _loc9_:Number = 0;
         var _loc10_:Number = 0;
         var _loc11_:String;
         if((Boolean(_loc11_ = param1.name)) && !_loc11_.indexOf("am_"))
         {
            param5 = _loc11_;
         }
         var _loc12_:Boolean = false;
         var _loc13_:int = 0;
         while(_loc13_ < param1.numChildren)
         {
            _loc14_ = param1.getChildAt(_loc13_);
            _loc15_ = getQualifiedClassName(_loc14_);
            _loc16_ = _loc14_.name;
            _loc17_ = param6;
            if(Boolean(_loc14_.filters) && Boolean(_loc14_.filters.length))
            {
               MathUtil.method_1892(param2.var_150,_loc14_,_loc15_,_loc16_);
            }
            if(!this.method_923(_loc14_))
            {
               _loc14_.visible = false;
            }
            else if(_loc15_ == "a_Handle")
            {
               _loc14_.visible = false;
            }
            else if(!_loc15_.indexOf("a_Volume"))
            {
               if(_loc18_ = _loc14_.name)
               {
                  _loc19_ = _loc14_.transform.concatenatedMatrix;
                  _loc20_ = new class_145(_loc18_,_loc19_.tx,_loc19_.ty,_loc14_.width,_loc14_.height,param2,++this.var_2480);
                  param2.var_1219.push(_loc20_);
               }
               _loc14_.visible = const_30;
            }
            else if(!_loc15_.indexOf("a_Soundscape"))
            {
               param2.var_1214 = _loc14_ as MovieClip;
               param2.var_1143 = _loc15_.split("_")[2];
               _loc14_.visible = const_30;
            }
            else if(!_loc15_.indexOf("a_BossTarget"))
            {
               _loc21_ = _loc15_.substr(12).split("_");
               if(param2.var_780[_loc21_[0]] == null)
               {
                  param2.var_780[_loc21_[0]] = new Array();
               }
               _loc22_ = new Point();
               this.method_269(_loc14_,_loc22_);
               param2.var_780[_loc21_[0]][int(_loc21_[1])] = _loc22_;
               _loc14_.visible = const_30;
            }
            else if(!_loc15_.indexOf("a_CameraTarget"))
            {
               _loc23_ = _loc15_.split("_");
               if((_loc24_ = uint(_loc23_[2])) == Room.const_243)
               {
                  class_24.method_19(getQualifiedClassName(param1) + ": " + _loc15_ + "is not a valid Camera Target.");
               }
               _loc25_ = new Point();
               this.method_269(_loc14_,_loc25_);
               param2.var_1082[_loc24_] = _loc25_;
               _loc14_.visible = const_30;
            }
            else
            {
               if(Boolean(_loc16_) && !_loc16_.indexOf("am_"))
               {
                  if(!(_loc26_ = param2.var_854[_loc16_]))
                  {
                     _loc26_ = new Array();
                     param2.var_854[_loc16_] = _loc26_;
                  }
                  _loc26_.push(_loc14_);
                  if(!_loc16_.indexOf("am_Target"))
                  {
                     _loc14_.visible = false;
                  }
               }
               if(_loc15_.indexOf("a_Upgrade") == 0 || _loc15_.indexOf("a_Swap") == 0)
               {
                  _loc28_ = (_loc27_ = ResourceManager.const_40[this.levelFileName]).applicationDomain;
                  _loc29_ = _loc14_ as Sprite;
                  _loc31_ = (_loc30_ = _loc15_.split("_"))[1] == "Swap";
                  _loc32_ = String(_loc30_[2]);
                  _loc33_ = null;
                  if(_loc31_)
                  {
                     if(_loc34_ = String(this.var_1.var_163[_loc32_]))
                     {
                        _loc33_ = "a_Swap_" + _loc32_ + "_" + _loc34_;
                     }
                  }
                  else if(_loc35_ = this.var_1.var_163[_loc32_])
                  {
                     _loc33_ = _loc35_.var_266;
                  }
                  if(_loc33_ != _loc15_)
                  {
                     if(_loc28_.hasDefinition(_loc33_))
                     {
                        if(_loc37_ = new (_loc36_ = _loc28_.getDefinition(_loc33_) as Class)())
                        {
                           _loc14_.parent.addChildAt(_loc37_,_loc14_.parent.getChildIndex(_loc14_));
                           _loc37_.transform = _loc14_.transform;
                           _loc14_.parent.removeChild(_loc14_);
                           _loc14_ = _loc37_;
                           _loc15_ = _loc33_;
                        }
                     }
                  }
                  _loc17_ = this.method_521(_loc14_);
                  if(_loc31_)
                  {
                     if(_loc28_.hasDefinition(_loc15_))
                     {
                        if(_loc39_ = new (_loc38_ = _loc28_.getDefinition(_loc15_) as Class)())
                        {
                           this.var_178.addChild(_loc39_);
                           _loc39_.transform = _loc14_.transform;
                           _loc39_.transform.matrix = _loc14_.transform.concatenatedMatrix;
                           _loc39_.transform.colorTransform = new ColorTransform(0,0,0,0.5,17,17,17);
                           _loc39_.mouseChildren = false;
                           _loc39_.cacheAsBitmap = true;
                           _loc39_.filters = [this.var_1.var_1791];
                        }
                     }
                     if(Boolean(_loc14_) && _loc34_ == "NONE")
                     {
                        _loc14_.visible = false;
                     }
                  }
               }
               if(_loc15_ == "a_PlayerSpawn")
               {
                  this.var_239 = new Point();
                  this.var_2549 = this.method_269(_loc14_,this.var_239);
               }
               else if(_loc15_ == "a_PlayerRespawn")
               {
                  param2.var_928 = new Point();
                  param2.var_2678 = this.method_269(_loc14_,param2.var_928);
               }
               else if(_loc15_ == "a_PlayerDevSpawn")
               {
                  this.var_1269 = new Point();
                  this.var_2481 = this.method_269(_loc14_,this.var_1269);
               }
               else if(_loc14_ is a_Cue)
               {
                  this.method_1130(_loc14_,_loc15_,param2,param1);
               }
               else if(_loc14_ is a_Hotspot)
               {
                  this.method_1240(_loc14_ as a_Hotspot);
               }
               else if(_loc14_ is a_RoomDirector)
               {
                  _loc40_ = _loc15_.split("_");
                  param2.method_896(_loc40_[2]);
                  _loc14_.visible = const_30;
               }
               else if(_loc15_ == "a_DoorMarker")
               {
                  if(_loc8_)
                  {
                     class_24.method_19("Multiple door markers in Room: " + getQualifiedClassName(param1));
                  }
                  _loc9_ = (_loc41_ = _loc14_.transform.concatenatedMatrix).tx;
                  _loc10_ = _loc41_.ty;
                  _loc8_ = _loc14_;
                  _loc14_.visible = const_30;
               }
               else if(!_loc15_.indexOf("a_Door_"))
               {
                  if(_loc42_ = uint(int(_loc15_.substr(2 + 5))))
                  {
                     _loc43_ = _loc14_.transform.concatenatedMatrix;
                     _loc44_ = MathUtil.method_138(_loc14_,_loc14_);
                     _loc44_.x *= _loc14_.scaleX;
                     _loc44_.width *= _loc14_.scaleX;
                     _loc44_.y *= _loc14_.scaleY;
                     _loc44_.height *= _loc14_.scaleY;
                     if(_loc7_)
                     {
                        class_24.method_19("Multiple doors in Room: Door_" + _loc42_);
                     }
                     _loc7_ = new Door(_loc16_,_loc43_.tx,_loc43_.ty,_loc44_,_loc42_,null,_loc14_.transform.matrix.a < 0);
                     this.var_264.push(_loc7_);
                     if(_loc45_ = class_11.method_545(this.internalName,_loc42_))
                     {
                        this.var_456[_loc45_.var_929] = new Point(_loc43_.tx,_loc43_.ty);
                        if(this.internalName == "OldMineMountain" && _loc45_.var_929 == "BridgeTown" || this.internalName == "OldMineMountainHard" && _loc45_.var_929 == "BridgeTownHard")
                        {
                           this.var_456["BridgeTown"] = new Point(_loc43_.tx,_loc43_.ty);
                        }
                        if(this.internalName == "EmeraldGlades" && _loc45_.var_929 == "OldMineMountain" || this.internalName == "EmeraldGladesHard" && _loc45_.var_929 == "OldMineMountainHard")
                        {
                           this.var_456["BridgeTown"] = new Point(_loc43_.tx,_loc43_.ty);
                           this.var_456["OMM_Mission12"] = new Point(_loc43_.tx,_loc43_.ty);
                        }
                     }
                  }
                  _loc14_.visible = const_30;
               }
               else if(!_loc15_.indexOf("a_Target_"))
               {
                  if(_loc46_ = String(_loc15_.split("_")[2]))
                  {
                     _loc47_ = _loc14_.transform.concatenatedMatrix;
                     _loc48_ = MathUtil.method_138(_loc14_,_loc14_);
                     _loc48_.x *= _loc14_.scaleX;
                     _loc48_.width *= _loc14_.scaleX;
                     _loc48_.y *= _loc14_.scaleY;
                     _loc48_.height *= _loc14_.scaleY;
                     this.targetList.unshift(new Door(_loc16_,_loc47_.tx,_loc47_.ty,_loc48_,0,_loc46_,_loc14_.transform.matrix.a < 0));
                  }
                  _loc14_.visible = const_30;
               }
               else if(!_loc15_.indexOf("a_DoorLocal_"))
               {
                  if(_loc49_ = String(_loc15_.split("_")[2]))
                  {
                     _loc50_ = _loc14_.transform.concatenatedMatrix;
                     _loc51_ = MathUtil.method_138(_loc14_,_loc14_);
                     _loc51_.x *= _loc14_.scaleX;
                     _loc51_.width *= _loc14_.scaleX;
                     _loc51_.y *= _loc14_.scaleY;
                     _loc51_.height *= _loc14_.scaleY;
                     _loc52_ = new Door(_loc16_,_loc50_.tx,_loc50_.ty,_loc51_,0,_loc49_,_loc14_.transform.matrix.a < 0);
                     this.var_264.push(_loc52_);
                     this.targetList.push(_loc52_);
                     if((_loc53_ = _loc14_ as MovieClip).hasOwnProperty("bDisabled"))
                     {
                        _loc52_.bDisabled = _loc53_.bDisabled;
                     }
                  }
                  _loc14_.visible = const_30;
               }
               else if(_loc14_ is Sprite)
               {
                  _loc54_ = _loc14_ as Sprite;
                  if(Boolean(_loc16_) && !_loc16_.indexOf("am_CollisionObject"))
                  {
                     class_154.method_444(_loc54_,param2.var_150,param2.var_1276,param2,this.var_456,false,this.var_1.collMan);
                     if(!(DevSettings.flags & DevSettings.DEVFLAG_SHOWWORLDCOLLISION))
                     {
                        _loc14_.visible = false;
                     }
                     if(_loc12_)
                     {
                        class_24.method_19("Room has two Collision Objects am_CollisionObject " + getQualifiedClassName(param1));
                     }
                     _loc12_ = true;
                  }
                  else if(Boolean(_loc16_) && !_loc16_.indexOf("am_Rack"))
                  {
                     if(!this.var_717)
                     {
                        this.var_717 = new Dictionary();
                     }
                     this.var_717[_loc16_] = _loc14_;
                     _loc57_ = 0;
                     while(_loc57_ < _loc54_.numChildren)
                     {
                        _loc56_ = DisplayObjectContainer(_loc54_.getChildAt(_loc57_));
                        _loc58_ = 0;
                        while(_loc58_ < _loc56_.numChildren)
                        {
                           _loc56_.getChildAt(_loc58_).visible = false;
                           _loc58_++;
                        }
                        _loc57_++;
                     }
                  }
                  else if(!_loc15_.indexOf(class_123.const_718))
                  {
                     _loc55_ = _loc54_.transform.concatenatedMatrix;
                     _loc59_ = !_loc16_.indexOf("am_") ? _loc16_ : param5;
                     _loc60_ = this.var_1.var_77.method_625(_loc54_ as MovieClip,_loc15_,_loc59_,this.levelFileName,_loc55_,_loc17_,Boolean(param4 & const_336) || !_loc16_.indexOf("am_Foreground"),Boolean(param4 & const_305) || !_loc16_.indexOf("am_Background"));
                     param2.var_1530.push(_loc60_);
                     _loc54_.visible = false;
                     this.var_1119.push(_loc54_);
                     if(this.levelSymbolName == "a_Level_TutorialBoat")
                     {
                        _loc60_.width += 4000;
                     }
                  }
                  else if(!_loc16_.indexOf("am_Foreground"))
                  {
                     if(!param4)
                     {
                        _loc61_ = this.var_1.var_77.var_592.numChildren;
                        this.method_232(_loc54_,param2,param3 + 1,param4 | const_336,null,_loc17_);
                        this.var_1.var_77.method_711(_loc54_,_loc61_,_loc17_);
                        _loc13_--;
                     }
                  }
                  else if(!_loc16_.indexOf("am_Midground"))
                  {
                     if(!param4)
                     {
                        _loc62_ = this.var_1.var_77.var_572.numChildren;
                        this.method_232(_loc54_,param2,param3 + 1,param4 | const_592,null,_loc17_);
                        this.var_1.var_77.method_948(_loc54_,_loc62_,_loc17_);
                        _loc13_--;
                     }
                  }
                  else if(!_loc16_.indexOf("am_Background"))
                  {
                     if(!param4)
                     {
                        _loc63_ = this.var_1.var_77.var_589.numChildren;
                        this.method_232(_loc54_,param2,param3 + 1,param4 | const_305,null,_loc17_);
                        this.var_1.var_77.method_914(_loc54_,_loc63_,_loc17_);
                        _loc13_--;
                     }
                  }
                  else
                  {
                     this.method_232(_loc54_,param2,param3 + 1,param4,param5,_loc17_);
                  }
               }
            }
            _loc13_++;
         }
         if(!_loc7_ && Boolean(_loc8_))
         {
            class_24.method_19("Room has a marker, but no door: " + getQualifiedClassName(param1));
         }
         else if(Boolean(_loc7_) && !_loc8_)
         {
            _loc7_.var_2280 = _loc7_.posX - 220;
            _loc7_.var_2285 = _loc7_.posY - _loc7_.var_443.height - 150;
            class_24.method_19(getQualifiedClassName(param1) + ": missing marker for Door_" + _loc7_.doorID);
         }
         else if(Boolean(_loc7_) && Boolean(_loc8_))
         {
            _loc7_.var_2280 = _loc9_;
            _loc7_.var_2285 = _loc10_;
         }
         if(param3 == 1 && !_loc12_)
         {
            class_24.method_19("Room has no Collision Object am_CollisionObject " + getQualifiedClassName(param1));
         }
      }
      
      public function method_269(param1:DisplayObject, param2:Point) : MovieClip
      {
         var _loc3_:Matrix = param1.transform.concatenatedMatrix;
         param2.x = _loc3_.tx;
         param2.y = _loc3_.ty;
         param1.visible = const_30;
         return param1 as MovieClip;
      }
      
      public function method_1130(param1:DisplayObject, param2:String, param3:Room, param4:Sprite) : void
      {
         var _loc9_:a_Group = null;
         var _loc10_:Array = null;
         var _loc11_:* = false;
         var _loc12_:class_35 = null;
         var _loc13_:BehaviorType = null;
         var _loc14_:String = null;
         var _loc15_:Array = null;
         var _loc16_:String = null;
         var _loc5_:a_Cue;
         (_loc5_ = param1 as a_Cue).entType = param2.slice(3);
         if(Boolean(param3.var_122) && _loc5_.name == BossFight.const_734)
         {
            param3.var_122.bDoubleBossFight = true;
         }
         if((Boolean(!!param1.parent ? param1.parent.name : null)) && !null.indexOf("am_"))
         {
            if(!(_loc9_ = param3.method_691(null)))
            {
               _loc9_ = new a_Group(null,param3);
               param3.var_1159.push(_loc9_);
            }
            _loc5_.groupName = null;
            _loc9_.AddNewCue(_loc5_);
            if(!null.indexOf("am_Wave"))
            {
               _loc5_.bDoNotAutoSpawn = true;
            }
         }
         if(_loc5_.bHoldSpawn)
         {
            _loc5_.bDoNotAutoSpawn = true;
         }
         _loc5_.room = param3;
         param3.var_460.push(_loc5_);
         if(param2 == const_483)
         {
            if(!_loc5_.characterName)
            {
               class_24.method_19(getQualifiedClassName(param4) + " " + const_483 + " must have characterName field in the form \'characterName,entType\', or \',entType\' if no characterName");
            }
            else
            {
               if((_loc10_ = _loc5_.characterName.split(",")).length == 1)
               {
                  class_24.method_19(getQualifiedClassName(param4) + " " + const_483 + " must have characterName field in the form \'characterName,entType\', or \',entType\' if no characterName.");
               }
               _loc5_.characterName = _loc10_[0];
               _loc5_.entType = _loc10_[1];
            }
         }
         if(Boolean(_loc5_.characterName) && this.alterParamsString == "Hard")
         {
            _loc5_.characterName += "Hard";
         }
         var _loc7_:String;
         if(_loc7_ = _loc5_.characterName)
         {
            _loc11_ = _loc5_.displayName == "Hidden";
            if(_loc12_ = class_14.var_999[_loc7_])
            {
               if(_loc5_.team != "neutral")
               {
                  class_24.method_19(getQualifiedClassName(param4) + ": " + _loc7_ + " contact should be set to team neutral.");
               }
               if(_loc5_.sayOnInteract)
               {
                  class_24.method_19(getQualifiedClassName(param4) + ": " + _loc7_ + " contact should not have a sayOnInteract text.");
               }
               if(Boolean(_loc5_.displayName) && !_loc11_)
               {
                  class_24.method_19(getQualifiedClassName(param4) + ": " + _loc7_ + " contact should not have a displayName.");
               }
               _loc5_.displayName = _loc12_.displayName;
            }
            else if(_loc5_.team == "neutral")
            {
               if(!_loc5_.sayOnInteract)
               {
                  class_24.method_19(getQualifiedClassName(param4) + ": " + _loc5_.characterName + " contact needs to have a sayOnInteract text.");
               }
               if(!_loc5_.displayName)
               {
                  class_24.method_19(getQualifiedClassName(param4) + ": " + _loc5_.characterName + " contact needs to have a displayName or name it \'Hidden\'");
               }
            }
            if(this.var_1046[_loc7_])
            {
               class_24.method_19(getQualifiedClassName(param4) + ": " + _loc5_.characterName + " contact needs a unique character name.");
            }
            this.var_1046[_loc7_] = _loc5_;
            this.var_456[_loc7_] = this.var_1.method_234(_loc5_);
            if(_loc11_)
            {
               _loc5_.displayName = null;
            }
            if(_loc5_.sayOnInteract == "Nothing")
            {
               _loc5_.sayOnInteract = null;
            }
         }
         else if(_loc5_.sayOnInteract)
         {
            _loc5_.sayOnInteract = null;
            class_24.method_19(getQualifiedClassName(param4) + ": " + param2 + " has sayOnInteract, but no characterName.");
         }
         var _loc8_:EntType;
         if(!(_loc8_ = EntType.method_48(_loc5_.entType)))
         {
            class_24.method_19(getQualifiedClassName(param4) + ": " + param2 + " specifies an unknown ent type: " + _loc5_.entType);
         }
         else if(this.alterParamsString == "Hard")
         {
            if(!(_loc13_ = BehaviorType.method_367(_loc8_.var_562)).var_2117)
            {
               _loc5_.entType += "Hard";
               if(!EntType.method_48(_loc5_.entType))
               {
                  class_24.method_19(getQualifiedClassName(param4) + ": " + param2 + " promotes to an unknown ent type: " + _loc5_.entType);
               }
            }
         }
         else if(Boolean(_loc5_.entType) && _loc5_.entType.indexOf("Hard") != -1)
         {
            class_24.method_19(getQualifiedClassName(param4) + ": Hard mode monster placed in regular zone: " + _loc5_.entType);
         }
         if(_loc5_.params)
         {
            for each(_loc14_ in _loc5_.params)
            {
               _loc16_ = String((_loc15_ = _loc14_.split("="))[0]);
               if(!const_425[_loc16_])
               {
                  class_24.method_19("Invalid params key specified: " + _loc16_);
               }
               else if(_loc15_.length != 2)
               {
                  class_24.method_19("Invalid params, must follow format x=y: " + _loc14_);
               }
               else
               {
                  if(!_loc5_.parsedParams)
                  {
                     _loc5_.parsedParams = new Dictionary();
                  }
                  _loc5_.parsedParams[_loc16_] = _loc15_[1];
               }
            }
         }
         _loc5_.visible = const_30;
      }
      
      public function method_1240(param1:a_Hotspot) : void
      {
         var _loc2_:Matrix = param1.transform.concatenatedMatrix;
         var _loc3_:Rectangle = MathUtil.method_138(param1,param1);
         _loc3_.x *= param1.scaleX;
         _loc3_.width *= param1.scaleX;
         _loc3_.y *= param1.scaleY;
         _loc3_.height *= param1.scaleY;
         this.var_1140.push(new class_77(_loc2_.tx,_loc2_.ty,_loc3_,param1));
         param1.visible = const_30;
      }
      
      public function method_1003() : void
      {
         var _loc3_:Room = null;
         var _loc5_:uint = 0;
         var _loc6_:Number = NaN;
         var _loc7_:Room = null;
         var _loc8_:Room = null;
         var _loc9_:a_Cue = null;
         var _loc10_:Number = NaN;
         var _loc11_:Packet = null;
         if(!this.var_2468)
         {
            this.var_1.var_776 = 0;
         }
         else
         {
            _loc5_ = this.var_1.mTimeThisTick % 3000;
            _loc6_ = 5 * Math.sin(Math.PI * (_loc5_ - 1500) / 1500);
            this.var_1.var_776 = _loc6_;
            for each(_loc7_ in this.var_299)
            {
               if(_loc7_.var_323 == "IntroBoatFight")
               {
                  _loc7_.method_1647();
               }
            }
         }
         if(!const_919)
         {
            if(this.var_333)
            {
               for each(_loc8_ in this.var_299)
               {
                  if(!_loc8_.bInitialized)
                  {
                     for each(_loc9_ in _loc8_.var_460)
                     {
                        _loc8_.SpawnCue(_loc9_,true);
                     }
                     _loc8_.bInitialized = true;
                  }
               }
            }
            return;
         }
         this.var_1666 = 0;
         this.var_1920 = 0;
         var _loc1_:uint = 0;
         var _loc2_:Number = 0;
         for each(_loc3_ in this.var_299)
         {
            if(!_loc3_.bInitialized)
            {
               _loc3_.method_275();
               _loc3_.bInitialized = true;
            }
            if(_loc3_.var_1118)
            {
               _loc3_.method_1027();
            }
            if(!_loc3_.var_2527)
            {
               ++this.var_1920;
               if(_loc3_.var_584)
               {
                  ++this.var_1666;
               }
               _loc10_ = _loc3_.method_1264() * this.var_1974;
               _loc2_ += _loc10_ == this.var_1974 ? this.var_1974 : Math.floor(_loc10_);
            }
            if(_loc3_.var_584)
            {
               _loc1_++;
            }
         }
         if(!this.bInstanced)
         {
            return;
         }
         var _loc4_:uint;
         if((_loc4_ = Math.round(_loc2_)) != this.var_690)
         {
            this.method_528(_loc4_);
            (_loc11_ = new Packet(LinkUpdater.const_791)).method_9(this.var_690);
            this.var_1.serverConn.SendPacket(_loc11_);
         }
         if(Boolean(this.var_2070) && !this.var_1657)
         {
            if(this.var_2526 == "DefeatBoss")
            {
               this.method_1802();
            }
            else
            {
               this.method_1385();
            }
         }
      }
      
      public function method_528(param1:uint) : void
      {
         this.var_690 = param1;
         this.var_1.screenQuestTracker.Refresh();
      }
      
      public function method_682() : void
      {
         var _loc3_:Room = null;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:Entity = null;
         var _loc7_:uint = 0;
         this.var_1657 = true;
         this.var_2911 = this.var_1.mTimeThisTick;
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         for each(_loc3_ in this.var_299)
         {
            if(_loc3_.var_584)
            {
               _loc1_++;
            }
            if(Boolean(_loc3_.var_241) && Boolean(_loc3_.var_241.var_1213))
            {
               _loc2_ += _loc3_.var_241.var_1213;
            }
         }
         _loc4_ = this.var_299.length;
         _loc5_ = 0;
         for each(_loc6_ in this.var_1.entities)
         {
            if(_loc6_.cue && _loc6_.behaviorType.var_1832 && _loc6_.entState != Entity.const_6)
            {
               _loc5_++;
            }
         }
         _loc7_ = _loc5_ >= this.var_968 ? this.var_968 : uint(this.var_968 - _loc5_);
         var _loc8_:Packet;
         (_loc8_ = new Packet(LinkUpdater.PKTTYPE_SET_LEVEL_COMPLETE)).method_9(this.var_690);
         _loc8_.method_9(_loc2_);
         _loc8_.method_9(this.var_1096);
         _loc8_.method_9(this.var_728);
         _loc8_.method_9(this.var_1270);
         _loc8_.method_9(_loc7_);
         _loc8_.method_9(this.var_968);
         _loc8_.method_9(this.var_1067);
         this.var_1.serverConn.SendPacket(_loc8_);
      }
      
      public function method_1385() : void
      {
         if(!this.var_1657 && this.var_1666 >= this.var_1920)
         {
            this.method_682();
         }
      }
      
      public function method_1802() : void
      {
         var _loc1_:Boolean = false;
         var _loc2_:Room = null;
         if(!this.var_1657)
         {
            _loc1_ = true;
            for each(_loc2_ in this.var_299)
            {
               if(_loc2_.var_2769 && !_loc2_.var_584)
               {
                  _loc1_ = false;
                  break;
               }
            }
            if(_loc1_)
            {
               this.method_682();
            }
         }
      }
      
      public function method_1462(param1:String) : Door
      {
         var _loc2_:Door = null;
         for each(_loc2_ in this.var_264)
         {
            if(_loc2_.var_2504 == param1)
            {
               return _loc2_;
            }
         }
         return null;
      }
      
      public function GetDoorFromID(param1:uint) : Door
      {
         var _loc2_:Door = null;
         for each(_loc2_ in this.var_264)
         {
            if(_loc2_.doorID == param1)
            {
               return _loc2_;
            }
         }
         return null;
      }
      
      public function method_112(param1:uint, param2:String, param3:String, param4:String) : void
      {
         var _loc5_:String = param1.toString() + "^" + param2 + "^" + param3;
         var _loc6_:String = param4;
         this.method_1525(_loc5_,_loc6_);
         this.method_474(_loc5_,_loc6_);
      }
      
      public function method_1525(param1:String, param2:String) : void
      {
         var _loc3_:Packet = new Packet(LinkUpdater.PKTTYPE_LEVEL_STATE);
         _loc3_.method_26(param1);
         _loc3_.method_26(param2);
         this.var_1.serverConn.SendPacket(_loc3_);
      }
      
      public function method_474(param1:String, param2:String) : void
      {
         var _loc7_:Room = null;
         var _loc3_:Array = param1.split("^");
         var _loc4_:uint = uint(_loc3_[0]);
         var _loc5_:String = String(_loc3_[1]);
         var _loc6_:String = String(_loc3_[2]);
         if(_loc4_ == Level.LEVELID)
         {
            this.method_1627(_loc5_,_loc6_,param2);
         }
         else if(_loc7_ = this.var_1.method_111(_loc4_))
         {
            _loc7_.method_1147(_loc5_,_loc6_,param2);
         }
      }
      
      public function method_1627(param1:String, param2:String, param3:String) : void
      {
      }
      
      public function method_506(param1:String) : void
      {
         var _loc12_:DisplayObject = null;
         var _loc13_:Sprite = null;
         var _loc14_:Room = null;
         var _loc2_:int = 0;
         var _loc3_:Array = param1.split("_");
         if(_loc3_.length < 3)
         {
            class_24.method_19("Bad Swap Name: " + param1 + " All upgrades and swaps are named a_Upgrade|Swap_<Type>(_<ParticularOne>) (last bit optional)");
            return;
         }
         var _loc4_:String = _loc3_[0] + "_" + _loc3_[1] + "_" + _loc3_[2];
         var _loc5_:Array = new Array();
         var _loc6_:Array = new Array();
         _loc2_ = 0;
         while(_loc2_ < this.var_59.numChildren)
         {
            _loc12_ = this.var_59.getChildAt(_loc2_);
            if(!getQualifiedClassName(_loc12_).indexOf("a_Room_"))
            {
               this.method_667(_loc12_,_loc4_,_loc5_,_loc6_,this.method_1016(_loc12_));
            }
            _loc2_++;
         }
         if(!_loc5_.length)
         {
            return;
         }
         var _loc7_:Class = null;
         var _loc9_:ApplicationDomain;
         var _loc8_:LoaderInfo;
         if((_loc9_ = (_loc8_ = ResourceManager.const_40[this.levelFileName]).applicationDomain).hasDefinition(param1))
         {
            _loc7_ = _loc9_.getDefinition(param1) as Class;
         }
         if(!_loc7_)
         {
            return;
         }
         var _loc10_:Number = this.var_59.x;
         var _loc11_:Number = this.var_59.y;
         this.var_1.main.stage.addChild(this.var_59);
         this.var_59.x = 0;
         this.var_59.y = 0;
         _loc2_ = 0;
         while(_loc2_ < _loc5_.length)
         {
            _loc13_ = _loc5_[_loc2_] as Sprite;
            _loc14_ = _loc6_[_loc2_];
            if(param1 != getQualifiedClassName(_loc13_))
            {
               this.method_1806(_loc13_,new _loc7_(),_loc14_);
            }
            _loc2_++;
         }
         this.var_1.main.stage.removeChild(this.var_59);
         this.var_59.x = _loc10_;
         this.var_59.y = _loc11_;
         if(this.var_1.var_107)
         {
            this.var_1.var_107.method_120();
         }
      }
      
      public function method_1016(param1:DisplayObject) : Room
      {
         var _loc3_:Room = null;
         var _loc2_:String = getQualifiedClassName(param1);
         for each(_loc3_ in this.var_299)
         {
            if(getQualifiedClassName(_loc3_.var_150) == _loc2_)
            {
               return _loc3_;
            }
         }
         return null;
      }
      
      private function method_1806(param1:Sprite, param2:Sprite, param3:Room) : void
      {
         var _loc6_:class_147 = null;
         var _loc4_:String = this.method_521(param1);
         var _loc5_:int = 0;
         while(_loc5_ < this.var_1.var_77.var_595.length)
         {
            _loc6_ = this.var_1.var_77.var_595[_loc5_];
            if(!_loc4_.indexOf(_loc6_.var_2603))
            {
               _loc6_.superAnim.m_Data.method_261();
               _loc6_.method_720();
               this.var_1.var_77.var_595.splice(_loc5_,1);
               _loc5_--;
            }
            _loc5_++;
         }
         param1.parent.addChildAt(param2,param1.parent.getChildIndex(param1));
         param2.transform = param1.transform;
         param2.name = param1.name;
         param1.parent.removeChild(param1);
         this.method_264(param2,param3,0,null,this.method_521(param2));
      }
      
      private function method_521(param1:DisplayObject) : String
      {
         return getQualifiedClassName(param1) + ":x" + param1.x + "y" + param1.y;
      }
      
      private function method_264(param1:Sprite, param2:Room, param3:uint, param4:String, param5:String) : void
      {
         var _loc8_:DisplayObject = null;
         var _loc9_:String = null;
         var _loc10_:String = null;
         var _loc11_:Sprite = null;
         var _loc12_:Matrix = null;
         var _loc13_:String = null;
         var _loc14_:class_147 = null;
         var _loc15_:int = 0;
         var _loc16_:int = 0;
         var _loc17_:int = 0;
         var _loc6_:String;
         if((Boolean(_loc6_ = param1.name)) && !_loc6_.indexOf("am_"))
         {
            param4 = _loc6_;
         }
         var _loc7_:int = 0;
         while(_loc7_ < param1.numChildren)
         {
            _loc8_ = param1.getChildAt(_loc7_);
            _loc9_ = getQualifiedClassName(_loc8_);
            _loc10_ = _loc8_.name;
            if(_loc8_ is Sprite)
            {
               _loc11_ = _loc8_ as Sprite;
               if(!_loc9_.indexOf(class_123.const_718))
               {
                  if(_loc11_.visible)
                  {
                     _loc12_ = _loc11_.transform.concatenatedMatrix;
                     _loc13_ = !_loc10_.indexOf("am_") ? _loc10_ : param4;
                     _loc14_ = this.var_1.var_77.method_625(_loc11_ as MovieClip,_loc9_,_loc13_,this.levelFileName,_loc12_,param5,Boolean(param3 & const_336) || !_loc10_.indexOf("am_Foreground"),Boolean(param3 & const_305) || !_loc10_.indexOf("am_Background"));
                     param2.var_1530.push(_loc14_);
                     _loc11_.visible = false;
                  }
               }
               else if(!_loc10_.indexOf("am_Foreground"))
               {
                  _loc15_ = this.var_1.var_77.var_592.numChildren;
                  this.method_264(_loc11_,param2,param3 | const_336,null,param5);
                  this.var_1.var_77.method_711(_loc11_,_loc15_,param5);
                  _loc7_--;
               }
               else if(!_loc10_.indexOf("am_Midground"))
               {
                  _loc16_ = this.var_1.var_77.var_572.numChildren;
                  this.method_264(_loc11_,param2,param3 | const_592,null,param5);
                  this.var_1.var_77.method_948(_loc11_,_loc16_,param5);
                  _loc7_--;
               }
               else if(!_loc10_.indexOf("am_Background"))
               {
                  _loc17_ = this.var_1.var_77.var_589.numChildren;
                  this.method_264(_loc11_,param2,param3 | const_305,null,param5);
                  this.var_1.var_77.method_914(_loc11_,_loc17_,param5);
                  _loc7_--;
               }
               else
               {
                  this.method_264(_loc11_,param2,param3,param4,param5);
               }
            }
            _loc7_++;
         }
      }
      
      private function method_667(param1:DisplayObject, param2:String, param3:Array, param4:Array, param5:Room) : void
      {
         var _loc6_:DisplayObjectContainer = null;
         var _loc7_:uint = 0;
         if(!getQualifiedClassName(param1).indexOf(param2))
         {
            param3.push(param1);
            param4.push(param5);
         }
         else if(_loc6_ = param1 as DisplayObjectContainer)
         {
            _loc7_ = 0;
            while(_loc7_ < _loc6_.numChildren)
            {
               this.method_667(_loc6_.getChildAt(_loc7_),param2,param3,param4,param5);
               _loc7_++;
            }
         }
      }
      
      public function method_194() : void
      {
         var _loc3_:Boolean = false;
         var _loc4_:MagicObject = null;
         var _loc5_:Sprite = null;
         var _loc6_:MovieClip = null;
         var _loc7_:String = null;
         var _loc8_:Array = null;
         var _loc9_:String = null;
         var _loc1_:uint = uint(this.var_1.var_163["Scaffolding"]);
         var _loc2_:class_9 = null;
         if(_loc1_)
         {
            _loc2_ = class_14.var_278[_loc1_];
         }
         for each(_loc4_ in this.var_1.var_171.var_410)
         {
            if((Boolean(_loc5_ = _loc4_.dObj as Sprite)) && _loc5_.numChildren == 1)
            {
               if(_loc6_ = _loc5_.getChildAt(0) as MovieClip)
               {
                  if(!(_loc7_ = getQualifiedClassName(_loc6_)).indexOf("a_Scaffolding_"))
                  {
                     _loc3_ = false;
                     if(_loc2_)
                     {
                        if((_loc9_ = String((_loc8_ = _loc7_.split("_"))[2])) == _loc2_.type)
                        {
                           _loc3_ = true;
                        }
                     }
                     if(_loc4_.var_51.parent)
                     {
                        _loc4_.var_51.parent.setChildIndex(_loc4_.var_51,_loc4_.var_51.parent.numChildren - 1);
                     }
                     _loc4_.var_51.visible = _loc3_;
                  }
               }
            }
         }
      }
      
      private function method_1079(param1:Sprite, param2:Sprite) : void
      {
         param1.parent.addChildAt(param2,param1.parent.getChildIndex(param1));
         param2.transform = param1.transform;
         param2.name = param1.name;
         param1.parent.removeChild(param1);
      }
      
      public function method_977() : void
      {
         if(this.var_2081 || !this.var_1.CanSendPacket())
         {
            return;
         }
         var _loc1_:Packet = new Packet(LinkUpdater.const_996);
         _loc1_.method_9(this.var_2744);
         this.var_1.serverConn.SendPacket(_loc1_);
         this.var_2081 = true;
      }
      
      public function method_1316() : void
      {
         this.method_735();
         this.method_1152();
      }
      
      public function method_1152() : void
      {
         if(!class_6.var_1148.length)
         {
            return;
         }
         this.method_663(false);
      }
      
      public function method_735() : void
      {
         var _loc7_:String = null;
         var _loc8_:Number = NaN;
         var _loc9_:GearType = null;
         var _loc10_:String = null;
         var _loc11_:int = 0;
         var _loc12_:Sprite = null;
         var _loc13_:Sprite = null;
         var _loc14_:DisplayObject = null;
         var _loc15_:SuperAnimInstance = null;
         if(!this.var_811 || !this.var_811.length)
         {
            return;
         }
         var _loc1_:int = 0;
         var _loc2_:String = this.var_811[0].usedBy;
         var _loc3_:Number = this.var_59.x;
         var _loc4_:Number = this.var_59.y;
         this.var_1.main.stage.addChild(this.var_59);
         this.var_59.x = 0;
         this.var_59.y = 0;
         var _loc5_:Dictionary = class_14.var_1762;
         var _loc6_:Vector.<GearType> = null;
         _loc1_ = 0;
         while(_loc1_ < this.var_811.length)
         {
            _loc7_ = Game.const_95;
            _loc8_ = 0.5;
            _loc9_ = this.var_811[_loc1_];
            _loc10_ = "am_Rack" + _loc2_ + _loc9_.type;
            if((_loc11_ = (_loc6_ = _loc5_[_loc2_ + ":" + _loc9_.type + ":" + _loc9_.var_8]).indexOf(_loc9_)) == -1)
            {
               class_24.method_19("Incorrect Gear List used. Problem with key.");
            }
            else
            {
               _loc12_ = this.var_717[_loc10_];
               if(_loc10_ == "Sword" && _loc2_ == "Paladin")
               {
                  _loc7_ = Game.const_404;
               }
               if(_loc10_ == "Sword" && _loc2_ == "Mage")
               {
                  _loc7_ = Game.const_404;
               }
               if(_loc13_ = _loc12_.getChildByName("am_Holder" + _loc11_.toString()) as Sprite)
               {
                  if(_loc9_.var_8 == "L")
                  {
                     if(_loc14_ = _loc13_.getChildByName("am_LegendaryBack"))
                     {
                        _loc14_.visible = true;
                     }
                  }
                  else if(_loc9_.var_8 == "R")
                  {
                     if(_loc14_ = _loc13_.getChildByName("am_RareBack"))
                     {
                        _loc14_.visible = true;
                     }
                  }
                  _loc15_ = this.var_1.RenderGear(_loc7_,_loc9_,_loc8_);
                  this.method_1079(Sprite(_loc13_.getChildByName("am_SampleGear")),_loc15_.m_TheDO);
               }
            }
            _loc1_++;
         }
         this.var_1.main.stage.removeChild(this.var_59);
         this.var_59.x = _loc3_;
         this.var_59.y = _loc4_;
         if(this.var_1.var_107)
         {
            this.var_1.var_107.method_120();
         }
      }
      
      public function method_663(param1:Boolean) : void
      {
         var _loc3_:GfxType = null;
         var _loc7_:uint = 0;
         var _loc8_:Sprite = null;
         var _loc9_:class_6 = null;
         var _loc10_:SuperAnimInstance = null;
         if(!this.var_59)
         {
            return;
         }
         if(!ResourceManager.method_149("Game"))
         {
            return;
         }
         var _loc2_:Sprite = this.var_59["am_HalloweenRoom"] as Sprite;
         if(!_loc2_)
         {
            return;
         }
         var _loc4_:uint;
         var _loc5_:uint = (_loc4_ = param1 ? const_1223 : const_1222) + const_1296;
         var _loc6_:uint = _loc4_;
         while(_loc6_ < _loc5_)
         {
            _loc7_ = _loc6_;
            if(param1)
            {
               _loc3_ = class_6.method_1052(_loc6_);
            }
            else if(_loc6_ < class_6.var_1148.length)
            {
               _loc3_ = class_6.var_1148[_loc6_];
            }
            if(_loc3_)
            {
               if(!param1)
               {
                  _loc7_++;
               }
               if(_loc7_ == 1)
               {
                  _loc8_ = _loc2_["am_StatueFirst"] as Sprite;
               }
               if(_loc7_ == 2)
               {
                  _loc8_ = _loc2_["am_StatueSecond"] as Sprite;
               }
               if(_loc7_ == 3)
               {
                  _loc8_ = _loc2_["am_StatueThird"] as Sprite;
               }
               if(_loc7_ == 4)
               {
                  _loc8_ = _loc2_["am_StatueFourth"] as Sprite;
               }
               if(_loc8_)
               {
                  _loc9_ = class_14.var_661[_loc7_];
                  (_loc10_ = new SuperAnimInstance(this.var_1,_loc3_,true,true)).method_1815(_loc9_.var_2763,_loc9_.var_2542);
                  _loc10_.m_TheDO.x = _loc9_.var_2490;
                  _loc10_.m_TheDO.y = _loc9_.var_2767;
                  _loc10_.m_TheDO.scaleX = _loc9_.var_2229 ? -1 : 1;
                  _loc8_.addChildAt(_loc10_.m_TheDO,0);
                  if(!this.var_1229)
                  {
                     this.var_1229 = new Vector.<SuperAnimInstance>();
                  }
                  this.var_1229.push(_loc10_);
               }
               if(param1)
               {
                  class_6.var_1148.push(_loc3_);
               }
            }
            _loc6_++;
         }
         if(param1)
         {
            class_6.var_1677 = true;
         }
      }
   }
}
