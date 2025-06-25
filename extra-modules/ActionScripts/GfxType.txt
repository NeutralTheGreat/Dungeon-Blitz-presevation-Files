package
{
   public class GfxType
   {
      
      internal static var var_1588:Boolean = false;
      
      internal static var var_1315:Array;
       
      
      internal var var_29:String;
      
      internal var animClass:String = "a__Animation";
      
      internal var animScale:Number = 1;
      
      internal var moveAnimSpeed:Number = 1;
      
      internal var customArts:Vector.<CustomArt>;
      
      internal var colorSwaps:Vector.<ColorSwap>;
      
      internal var var_522:Boolean = false;
      
      internal var baseAnim:String = "Ready";
      
      internal var var_1466:String = "Run";
      
      internal var var_209:String;
      
      internal var var_918:Boolean = false;
      
      internal var var_927:Boolean = false;
      
      internal var bFireAndForget:Boolean = false;
      
      internal var bRandomFrameStart:Boolean = false;
      
      internal var var_1126:Boolean = false;
      
      internal var var_947:String = null;
      
      internal var var_1526:Boolean = false;
      
      internal var var_1598:Boolean = false;
      
      internal var var_527:Boolean = false;
      
      internal var tint:uint = 0;
      
      internal var var_177:Number = 1;
      
      internal var var_843:String = null;
      
      internal var var_1864:Number = 0;
      
      public function GfxType()
      {
         this.customArts = new Vector.<CustomArt>();
         this.colorSwaps = new Vector.<ColorSwap>();
         super();
      }
      
      public static function method_125(param1:Array, param2:Boolean = false) : void
      {
         var_1315 = param1;
         var_1588 = param2;
      }
      
      public static function method_2051(param1:String) : Boolean
      {
         var _loc2_:Number = Number(var_1315[param1]);
         return _loc2_ >= 0;
      }
      
      public static function method_1116(param1:XML, param2:GfxType, param3:int) : GfxType
      {
         var _loc5_:XML = null;
         var _loc6_:String = null;
         var _loc7_:Number = NaN;
         var _loc8_:Array = null;
         var _loc9_:CustomArt = null;
         var _loc10_:String = null;
         var _loc11_:Array = null;
         var _loc12_:String = null;
         var _loc13_:uint = 0;
         var _loc14_:String = null;
         var _loc15_:uint = 0;
         var _loc4_:GfxType = param2;
         for each(_loc5_ in param1.*)
         {
            if((_loc6_ = String(_loc5_.name())) == "AnimFile")
            {
               _loc4_.var_29 = _loc5_.toString();
            }
            else if(_loc6_ == "AnimClass")
            {
               _loc4_.animClass = _loc5_.toString();
            }
            else if(_loc6_ == "AnimScale")
            {
               if((_loc7_ = Number(_loc5_)) > 0)
               {
                  _loc4_.animScale *= _loc7_;
               }
               else
               {
                  _loc4_.animScale = _loc7_ * -1;
               }
            }
            else if(_loc6_ == "MoveAnimSpeed")
            {
               _loc4_.moveAnimSpeed = Number(_loc5_);
            }
            else if(_loc6_ == "BaseAnim")
            {
               _loc4_.baseAnim = _loc5_.toString();
            }
            else if(_loc6_ == "RunAnim")
            {
               _loc4_.var_1466 = _loc5_.toString();
            }
            else if(_loc6_ == "Shadow")
            {
               _loc4_.var_209 = _loc5_.toString();
            }
            else if(_loc6_ == "FlipAnim")
            {
               _loc4_.var_522 = MathUtil.method_50(_loc5_);
            }
            else if(_loc6_ == "FireAndForget")
            {
               _loc4_.bFireAndForget = MathUtil.method_50(_loc5_);
            }
            else if(_loc6_ == "RandomFrameStart")
            {
               _loc4_.bRandomFrameStart = MathUtil.method_50(_loc5_);
            }
            else if(_loc6_ == "Desynch")
            {
               _loc4_.var_1126 = MathUtil.method_50(_loc5_);
            }
            else if(_loc6_ == "Tint")
            {
               _loc4_.tint = uint(_loc5_);
            }
            else if(!_loc6_.indexOf("CustomArt"))
            {
               _loc8_ = _loc5_.toString().split("/");
               _loc9_ = new CustomArt(_loc8_[0],_loc8_[1]);
               _loc4_.customArts.push(_loc9_);
            }
            else if(!_loc6_.indexOf("ColorSwap"))
            {
               if((_loc11_ = (_loc10_ = _loc5_.toString()).split("=")).length != 2)
               {
                  class_24.method_7("Color not in format OLDCOLOR=NEWCOLOR : " + _loc10_ + " in file " + _loc4_.var_29);
               }
               _loc13_ = (_loc12_ = String(_loc11_[0])).charAt(0) != "0" ? uint(var_1315[_loc12_]) : uint(_loc12_);
               _loc15_ = (_loc14_ = String(_loc11_[1])).charAt(0) != "0" ? uint(var_1315[_loc14_]) : uint(_loc14_);
               _loc4_.colorSwaps.push(new ColorSwap(_loc13_,_loc15_,param3));
            }
         }
         if(Boolean(_loc4_.var_209) && _loc4_.var_209.indexOf("a_ShadowSpirit") != -1)
         {
            _loc4_.var_1526 = true;
         }
         _loc4_.var_927 = Boolean(_loc4_.animClass) && !_loc4_.animClass.indexOf("a_Sign");
         return _loc4_;
      }
      
      public static function method_53(param1:XML, param2:GfxType, param3:int = 0) : GfxType
      {
         if(param1.children().length() > 0)
         {
            if(!param2)
            {
               param2 = new GfxType();
            }
            return GfxType.method_1116(param1,param2,param3);
         }
         return param2;
      }
      
      public static function method_321(param1:GfxType, param2:XML) : Vector.<GfxType>
      {
         var _loc3_:Array = param1.animClass.split("_");
         var _loc4_:int;
         if((_loc4_ = _loc3_.length - 3) < 0 || _loc3_[_loc4_] != "Random")
         {
            return null;
         }
         var _loc5_:uint = uint(_loc3_[_loc4_ + 1]);
         var _loc6_:uint = uint(_loc3_[_loc4_ + 2]);
         if(!_loc5_ || !_loc6_)
         {
            class_24.method_7("Start and End Index of a Random Fire Gfx must be nonzero: " + param1.animClass);
         }
         if(_loc5_ >= _loc6_)
         {
            class_24.method_7("Start Index must be less than the End Index of a Random Fire Gfx: " + param1.animClass);
         }
         _loc3_.splice(_loc4_,3);
         var _loc7_:Vector.<GfxType> = new Vector.<GfxType>();
         var _loc8_:String = _loc3_.join("_");
         while(_loc5_ <= _loc6_)
         {
            param1.animClass = _loc8_ + (_loc5_ < 10 ? "0" : "") + _loc5_;
            _loc7_.push(param1);
            param1 = GfxType.method_53(param2,null);
            _loc5_++;
         }
         _loc7_.fixed = true;
         return _loc7_;
      }
      
      public static function method_1518(param1:GfxType, param2:XML) : Vector.<GfxType>
      {
         var _loc3_:Array = param1.animClass.split("_");
         var _loc4_:int;
         if((_loc4_ = _loc3_.length - 3) < 0 || _loc3_[_loc4_] != "Sequence")
         {
            return null;
         }
         var _loc5_:uint = uint(_loc3_[_loc4_ + 1]);
         var _loc6_:uint = uint(_loc3_[_loc4_ + 2]);
         if(!_loc5_ || !_loc6_)
         {
            class_24.method_7("Start and End Index of a Sequence Fire Gfx must be nonzero: " + param1.animClass);
         }
         if(_loc5_ >= _loc6_)
         {
            class_24.method_7("Start Index must be less than the End Index of a Sequence Fire Gfx: " + param1.animClass);
         }
         _loc3_.splice(_loc4_,3);
         var _loc7_:Vector.<GfxType> = new Vector.<GfxType>();
         var _loc8_:String = _loc3_.join("_");
         while(_loc5_ <= _loc6_)
         {
            param1.animClass = _loc8_ + (_loc5_ < 10 ? "0" : "") + _loc5_;
            _loc7_.push(param1);
            param1 = GfxType.method_53(param2,null);
            _loc5_++;
         }
         _loc7_.fixed = true;
         return _loc7_;
      }
      
      public static function method_1733(param1:GfxType, param2:XML) : GfxType
      {
         var _loc3_:Array = param1.animClass.split(",");
         if(_loc3_.length <= 1)
         {
            return null;
         }
         var _loc4_:GfxType;
         (_loc4_ = GfxType.method_53(param2,null)).animClass = _loc3_[1];
         param1.animClass = _loc3_[0];
         return _loc4_;
      }
      
      public static function method_368(param1:GfxType, param2:XML) : GfxType
      {
         var _loc5_:String = null;
         var _loc6_:GfxType = null;
         var _loc3_:Array = param1.animClass.split("_");
         var _loc4_:uint = _loc3_.length - 1;
         if(_loc3_[_loc4_] == "Both")
         {
            _loc3_.splice(_loc4_,1);
            _loc5_ = _loc3_.join("_");
            param1.animClass = _loc5_ + "_Front";
            (_loc6_ = GfxType.method_53(param2,null)).animClass = _loc5_ + "_Rear";
            return _loc6_;
         }
         return null;
      }
      
      public function method_1554() : String
      {
         var _loc2_:CustomArt = null;
         var _loc3_:ColorSwap = null;
         var _loc1_:String = this.var_29 + this.animClass + this.animScale + this.moveAnimSpeed;
         for each(_loc2_ in this.customArts)
         {
            _loc1_ += _loc2_.fileName + _loc2_.setName;
         }
         for each(_loc3_ in this.colorSwaps)
         {
            _loc1_ += _loc3_.var_1354 + ":" + _loc3_.var_411 + ":" + _loc3_.var_1150;
         }
         _loc1_ += this.var_522;
         _loc1_ += this.baseAnim;
         _loc1_ += this.var_1466;
         _loc1_ += this.var_209;
         _loc1_ += this.var_918;
         _loc1_ += this.var_927;
         _loc1_ += this.bFireAndForget;
         _loc1_ += this.bRandomFrameStart;
         _loc1_ += this.var_947;
         _loc1_ += this.var_1598;
         _loc1_ += this.tint;
         return _loc1_ + this.var_843;
      }
      
      public function method_1289() : void
      {
      }
      
      public function GetDuplicate() : GfxType
      {
         var _loc1_:GfxType = new GfxType();
         _loc1_.var_29 = this.var_29;
         _loc1_.animClass = this.animClass;
         _loc1_.animScale = this.animScale;
         _loc1_.moveAnimSpeed = this.moveAnimSpeed;
         _loc1_.customArts = this.customArts.slice();
         _loc1_.colorSwaps = this.colorSwaps.slice();
         _loc1_.var_522 = this.var_522;
         _loc1_.baseAnim = this.baseAnim;
         _loc1_.var_1466 = this.var_1466;
         _loc1_.var_209 = this.var_209;
         _loc1_.var_918 = this.var_918;
         _loc1_.var_927 = this.var_927;
         _loc1_.bFireAndForget = this.bFireAndForget;
         _loc1_.bRandomFrameStart = this.bRandomFrameStart;
         _loc1_.var_1126 = this.var_1126;
         _loc1_.var_947 = this.var_947;
         _loc1_.var_1526 = this.var_1526;
         _loc1_.var_1598 = this.var_1598;
         _loc1_.var_527 = this.var_527;
         _loc1_.tint = this.tint;
         _loc1_.var_177 = this.var_177;
         _loc1_.var_843 = this.var_843;
         return _loc1_;
      }
   }
}
