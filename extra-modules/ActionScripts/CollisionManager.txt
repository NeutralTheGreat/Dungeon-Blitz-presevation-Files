package
{
   import flash.geom.Point;
   import flash.utils.Dictionary;
   
   public class CollisionManager
   {
      
      public static const GRIDRES:int = 100;
      
      public static const MAXGRID:int = 16000;
      
      public static const INVGRIDRES:Number = 1 / GRIDRES;
      
      public static const BLUE_LINE:uint = 255;
      
      public static const CYAN_LINE:uint = 65535;
      
      public static const MAGENTA_LINE:uint = 16711935;
      
      public static const RED_LINE:uint = 16711680;
      
      public static const GREEN_LINE:uint = 65280;
      
      public static const WHITE_LINE:uint = 16777215;
      
      public static const YELLOW_LINE:uint = 16776960;
      
      public static const const_1140:uint = 16777113;
      
      public static const BLACK_LINE:uint = 0;
      
      public static const const_1109:uint = 6710886;
      
      public static const const_1132:uint = 10027263;
      
      public static const const_1215:uint = 26112;
      
      public static const const_1224:uint = 102;
      
      public static const const_882:uint = 6684672;
      
      public static const HARD_FLOOR:uint = 1 << 0;
      
      public static const SOFT_FLOOR:uint = 1 << 1;
      
      public static const TRIGGER_BOUNDARY:uint = 1 << 2;
      
      public static const const_110:uint = 1 << 3;
      
      public static const const_258:int = -1;
      
      public static const SEARCHFLAG_UPWARD_INCLUDE_SOFT:uint = 1 << 0;
      
      private static const const_505:Point = new Point();
      
      private static const const_289:Point = new Point(0,0);
      
      private static const MAX_COLL_LINES:uint = 1024;
      
      private static const const_456:Vector.<class_37> = new Vector.<class_37>(MAX_COLL_LINES,true);
      
      internal static const const_582:Dictionary = new Dictionary();
      
      internal static const const_82:Dictionary = new Dictionary();
      
      private static const MAX_GCC_PLOTS:uint = 10240;
      
      private static var gccLinePlotsX:Vector.<Number> = new Vector.<Number>(MAX_GCC_PLOTS,true);
      
      private static var gccLinePlotsY:Vector.<Number> = new Vector.<Number>(MAX_GCC_PLOTS,true);
      
      {
         const_82["DoorLocal"] = true;
         const_82["Door"] = true;
         const_82["Plummet"] = true;
         const_82["Trigger"] = true;
         const_82["MultiTrigger"] = true;
         const_82["Badge"] = true;
         const_82["RoomAggro"] = true;
         const_82["Think"] = true;
         const_82["CutScene"] = true;
         const_82["Script"] = true;
      }
      
      internal var var_1:Game;
      
      internal var var_259:Dictionary;
      
      internal var var_2180:Vector.<class_37>;
      
      private var var_1182:Vector.<class_37>;
      
      public function CollisionManager(param1:Game)
      {
         super();
         this.var_1 = param1;
         this.var_259 = new Dictionary();
         this.var_1182 = new Vector.<class_37>();
         this.var_2180 = new Vector.<class_37>();
      }
      
      public static function method_77(param1:uint, param2:uint) : void
      {
         const_582[param1] = param2;
      }
      
      public static function method_318(param1:Number, param2:Number) : uint
      {
         var _loc3_:int = Math.floor(param1 + 0.01) * INVGRIDRES;
         var _loc4_:int = Math.floor(param2 + 0.01) * INVGRIDRES;
         return _loc3_ + MAXGRID << 16 | _loc4_ + MAXGRID;
      }
      
      public function method_784() : void
      {
         var _loc1_:String = null;
         var _loc2_:uint = 0;
         var _loc3_:Vector.<class_37> = null;
         var _loc4_:class_37 = null;
         for(_loc1_ in this.var_259)
         {
            _loc3_ = this.var_259[_loc1_];
            for each(_loc4_ in _loc3_)
            {
               _loc4_.method_1778();
            }
            delete this.var_259[_loc1_];
         }
         this.var_259 = null;
         this.var_1182 = null;
         this.var_2180 = null;
         _loc2_ = 0;
         while(_loc2_ < MAX_COLL_LINES)
         {
            const_456[_loc2_] = null;
            _loc2_++;
         }
         this.var_1 = null;
      }
      
      public function method_1043() : void
      {
         var _loc1_:String = null;
         var _loc2_:Vector.<class_37> = null;
         for(_loc1_ in this.var_259)
         {
            _loc2_ = this.var_259[_loc1_];
            _loc2_.fixed = true;
         }
      }
      
      public function method_2071() : void
      {
         var _loc1_:String = null;
         var _loc2_:Vector.<class_37> = null;
         for(_loc1_ in this.var_259)
         {
            _loc2_ = this.var_259[_loc1_];
            _loc2_.fixed = false;
         }
      }
      
      public function method_1952(param1:class_37) : void
      {
         var _loc2_:uint = 0;
         var _loc3_:int = 0;
         var _loc4_:int = MathUtil.method_703(param1.startX,param1.startY,param1.endX,param1.endY,gccLinePlotsX,gccLinePlotsY,GRIDRES);
         _loc3_ = 0;
         while(_loc3_ < _loc4_)
         {
            _loc2_ = method_318(gccLinePlotsX[_loc3_],gccLinePlotsY[_loc3_]);
            if(this.var_259[_loc2_] == undefined)
            {
               this.var_259[_loc2_] = new Vector.<class_37>();
            }
            this.var_259[_loc2_].push(param1);
            _loc3_++;
         }
         this.var_2180.push(param1);
      }
      
      public function method_1522(param1:class_37) : void
      {
         this.var_1182.fixed = false;
         this.var_1182.push(param1);
         param1.var_2914 = true;
         this.var_1182.fixed = true;
      }
      
      public function method_1598(param1:Number, param2:Number, param3:Number, param4:Number, param5:Vector.<class_37>) : int
      {
         var _loc6_:uint = 0;
         var _loc8_:class_37 = null;
         var _loc9_:Vector.<class_37> = null;
         var _loc10_:int = 0;
         var _loc7_:int = 0;
         var _loc11_:int = MathUtil.method_703(param1,param2,param3,param4,gccLinePlotsX,gccLinePlotsY,GRIDRES);
         _loc10_ = 0;
         while(_loc10_ < _loc11_)
         {
            _loc6_ = method_318(gccLinePlotsX[_loc10_],gccLinePlotsY[_loc10_]);
            if(_loc9_ = this.var_259[_loc6_])
            {
               for each(_loc8_ in _loc9_)
               {
                  var _loc14_:*;
                  param5[_loc14_ = _loc7_++] = _loc8_;
               }
            }
            _loc10_++;
         }
         for each(_loc8_ in this.var_1182)
         {
            param5[_loc14_ = _loc7_++] = _loc8_;
         }
         return _loc7_;
      }
      
      public function getFloorCollision(param1:uint, param2:Number, param3:Number, param4:Point, param5:Point, param6:class_37, param7:Point, param8:Point, param9:uint, param10:uint, param11:int = 0, param12:uint = 0, param13:Vector.<class_37> = null) : class_37
      {
         var _loc16_:class_37 = null;
         var _loc17_:Number = NaN;
         var _loc18_:class_37 = null;
         var _loc22_:int = 0;
         var _loc14_:Number = param4.x;
         var _loc15_:Number = param4.y;
         if(!_loc14_ && !_loc15_)
         {
            return null;
         }
         var _loc19_:Number = param2 + _loc14_;
         var _loc20_:Number = param3 + _loc15_;
         var _loc21_:* = param11 != const_258;
         var _loc23_:int = this.method_1598(param2,param3,_loc19_,_loc20_,const_456);
         _loc22_ = 0;
         while(_loc22_ < _loc23_)
         {
            if((_loc16_ = const_456[_loc22_]).type & param9)
            {
               if(!_loc16_.bDisabled)
               {
                  if(!(_loc21_ && _loc16_.var_941 != param11))
                  {
                     if(!(Boolean(_loc16_.var_2286) && _loc16_.var_2286 == param1))
                     {
                        if(!(_loc16_.type & param12))
                        {
                           if(_loc16_ != param6)
                           {
                              if((_loc17_ = MathUtil.method_1144(param2,param3,_loc16_.startX,_loc16_.startY,_loc16_.endX - _loc16_.startX,_loc16_.endY - _loc16_.startY,const_505)) >= 0 || !(param9 & CollisionManager.SOFT_FLOOR) || !(_loc16_.type & CollisionManager.SOFT_FLOOR) || Boolean(param10 & SEARCHFLAG_UPWARD_INCLUDE_SOFT))
                              {
                                 if(MathUtil.method_500(param2,param3,_loc19_,_loc20_,_loc16_.startX,_loc16_.startY,_loc16_.endX,_loc16_.endY,const_289))
                                 {
                                    _loc18_ = _loc16_;
                                    if(param7)
                                    {
                                       param7.x = const_505.x;
                                       param7.y = const_505.y;
                                    }
                                    if(param8)
                                    {
                                       param8.x = _loc17_;
                                    }
                                    if(!param13)
                                    {
                                       _loc19_ = const_289.x;
                                       _loc20_ = const_289.y;
                                       _loc14_ = _loc19_ - param2;
                                       _loc15_ = _loc20_ - param3;
                                    }
                                    else if(param13.indexOf(_loc16_) == -1)
                                    {
                                       param13.push(_loc16_);
                                    }
                                 }
                              }
                           }
                        }
                     }
                  }
               }
            }
            _loc22_++;
         }
         if(_loc18_)
         {
            param5.x = const_289.x;
            param5.y = const_289.y;
            param4.x = _loc14_;
            param4.y = _loc15_;
            return _loc18_;
         }
         return null;
      }
   }
}
