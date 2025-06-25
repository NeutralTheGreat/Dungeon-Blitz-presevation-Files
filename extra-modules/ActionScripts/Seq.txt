package
{
   public class Seq
   {
      
      private static const const_119:Array = new Array();
      
      public static const RUNNING:uint = 1 << 0;
      
      public static const AIRBORNE:uint = 1 << 1;
      
      public static const DROPPING:uint = 1 << 2;
      
      public static const JUMPING:uint = 1 << 3;
      
      public static const KOED:uint = 1 << 4;
      
      public static const HIT_REACT:uint = 1 << 5;
      
      public static const STUNNED:uint = 1 << 6;
      
      public static const FROZEN:uint = 1 << 7;
      
      public static const const_663:uint = 1 << 8;
      
      public static const FINALSPLAT:uint = 1 << 9;
      
      public static const const_649:uint = 1 << 10;
      
      public static const const_712:uint = 1 << 11;
      
      public static const NEW_JUMP:uint = 1 << 12;
      
      public static const C_USEPOWER:uint = 1;
      
      public static const C_EMOTE:uint = 2;
      
      public static const const_590:uint = 3;
      
      {
         const_119[1] = "Shoot45";
         const_119[2] = "Shoot45";
         const_119[3] = "ShootUp90";
         const_119[4] = "ShootUp90";
         const_119[11] = "ShootDown90";
         const_119[12] = "ShootDown90";
         const_119[13] = "ShootDown45";
         const_119[14] = "ShootDown45";
      }
      
      internal var var_350:GfxType;
      
      internal var var_71:class_30;
      
      internal var var_218:class_26;
      
      internal var var_463:class_26;
      
      internal var var_689:class_26;
      
      internal var var_348:class_26;
      
      internal var var_384:class_26;
      
      internal var var_1304:class_26;
      
      internal var var_800:class_26;
      
      internal var var_1003:class_26;
      
      internal var var_1149:class_26;
      
      internal var var_1074:class_26;
      
      internal var var_120:uint;
      
      internal var var_30:class_26;
      
      internal var var_314:class_28;
      
      internal var var_317:uint;
      
      internal var var_324:Number = 0;
      
      internal var var_2598:Number = 0;
      
      internal var var_2378:class_26;
      
      internal var var_1026:uint;
      
      internal var var_735:Boolean;
      
      internal var var_1842:Number = 1;
      
      internal var var_2741:Boolean;
      
      private var var_2160:Boolean;
      
      private var var_2083:Boolean;
      
      private var var_1547:Boolean;
      
      private var var_796:Boolean;
      
      private var var_1673:Boolean;
      
      private var var_2054:Boolean;
      
      public function Seq(param1:GfxType)
      {
         super();
         this.var_120 = 0;
         this.var_350 = param1;
         this.var_71 = class_29.method_765(param1.animClass,param1.var_29,param1.var_843);
         if(!this.var_71)
         {
            this.var_71 = class_29.method_602(param1.animClass,param1.var_29,param1.animClass,param1.var_843);
         }
         this.method_781();
         this.method_180(this.var_218,param1.bRandomFrameStart);
         this.var_314 = this.var_30.var_604[this.var_317];
         if(!this.var_314)
         {
            this.var_314 = this.var_30.method_242(this.var_317);
         }
      }
      
      public function method_399() : void
      {
         this.var_350 = null;
         this.var_314 = null;
      }
      
      public function method_781() : void
      {
         var _loc1_:class_26 = null;
         this.var_218 = this.var_71.var_69[this.var_350.baseAnim];
         if(!this.var_218)
         {
            var _loc2_:int = 0;
            var _loc3_:* = this.var_71.var_69;
            for each(_loc1_ in _loc3_)
            {
               this.var_218 = _loc1_;
            }
            class_24.method_19("BaseAnim Missing for: " + this.var_350.baseAnim + " in file: " + this.var_350.var_29 + "/" + this.var_350.animClass);
         }
         this.var_689 = this.var_71.var_69["Jump"];
         this.var_348 = this.var_71.var_69["Fall"];
         if(!this.var_348)
         {
            this.var_348 = this.var_689;
         }
         this.var_384 = this.var_71.var_69["Drop"];
         if(!this.var_384)
         {
            this.var_384 = this.var_348;
         }
         this.var_1304 = this.var_71.var_69["HitReact"];
         if(!this.var_1304)
         {
            this.var_1304 = this.var_218;
         }
         this.var_463 = this.var_71.var_69[this.var_350.var_1466];
         if(!this.var_463)
         {
            this.var_463 = this.var_218;
         }
         this.var_800 = this.var_71.var_69["KOed"];
         if(!this.var_800)
         {
            this.var_800 = this.var_218;
         }
         this.var_1149 = this.var_71.var_69["FinalSplat"];
         this.var_1074 = this.var_71.var_69["FinalSplat2"];
         this.var_1003 = this.var_71.var_69["KOed2"];
      }
      
      public function method_983(param1:Number, param2:Seq) : Boolean
      {
         var _loc9_:Boolean = false;
         var _loc10_:class_26 = null;
         var _loc11_:Boolean = false;
         var _loc12_:Boolean = false;
         var _loc13_:* = false;
         var _loc14_:uint = 0;
         var _loc15_:int = 0;
         var _loc16_:int = 0;
         var _loc17_:Number = NaN;
         var _loc18_:Number = NaN;
         var _loc19_:class_26 = null;
         var _loc20_:int = 0;
         var _loc21_:int = 0;
         if(this.var_30.var_153 == this.var_463 || this.var_30.var_153 == this.var_218 || this.var_30.var_153 == this.var_348 || this.var_30.var_153 == this.var_384)
         {
            param1 *= this.var_350.moveAnimSpeed;
            param1 *= this.var_1842;
         }
         if(this.var_350.var_1126)
         {
            param1 *= 1 + (Math.random() - 0.5) * 0.2;
         }
         this.var_324 += param1;
         var _loc3_:Boolean = false;
         var _loc4_:Boolean = false;
         var _loc5_:Boolean = false;
         var _loc6_:Boolean = false;
         var _loc7_:Boolean = false;
         if(param2)
         {
            if(this.var_1026)
            {
               this.var_1026 = 0;
            }
            if(param2.var_2741)
            {
               _loc5_ = true;
            }
         }
         if(this.var_1026)
         {
            _loc9_ = false;
            if(this.var_1026 == const_590 && this.var_30.var_153 != this.var_2378)
            {
               _loc9_ = true;
            }
            this.method_180(this.var_2378,_loc9_);
            this.var_796 = true;
            if(this.var_1026 == C_EMOTE)
            {
               this.var_2160 = true;
               this.var_2083 = true;
               if(this.var_735)
               {
                  this.var_796 = false;
               }
               if(this.var_317 >= this.var_30.var_2354)
               {
                  this.var_796 = false;
               }
            }
            this.var_1026 = 0;
         }
         if(!this.var_796 && (!this.var_735 || this.var_2083))
         {
            _loc10_ = null;
            _loc11_ = false;
            _loc12_ = false;
            if(Boolean(this.var_120 & FINALSPLAT) && Boolean(this.var_1149))
            {
               if(this.var_30.var_153 == this.var_1149 || this.var_30.var_153 == this.var_1074)
               {
                  _loc10_ = this.var_30;
               }
               else if(this.var_30.var_153 == this.var_1003 && Boolean(this.var_1074))
               {
                  _loc10_ = this.var_1074;
               }
               else
               {
                  _loc10_ = this.var_1149;
               }
            }
            else if(this.var_120 & KOED)
            {
               if(this.var_30.var_153 == this.var_800 || this.var_30.var_153 == this.var_1003)
               {
                  _loc10_ = this.var_30;
               }
               else if(this.var_120 & AIRBORNE && this.var_1003 && Math.random() > 0.5)
               {
                  _loc10_ = this.var_1003;
               }
               else
               {
                  _loc10_ = this.var_800;
               }
            }
            else if(this.var_120 & JUMPING && this.var_689 && (this.var_30 != this.var_348 && this.var_30 != this.var_384 || this.var_120 & NEW_JUMP))
            {
               _loc10_ = this.var_689;
               _loc12_ = Boolean(this.var_120 & NEW_JUMP);
            }
            else if(this.var_120 & STUNNED)
            {
               _loc10_ = this.var_71.var_69["Stunned"];
            }
            else if(this.var_120 & FROZEN)
            {
               _loc10_ = this.var_71.var_69["Frozen"];
            }
            else if(this.var_120 & HIT_REACT)
            {
               _loc11_ = true;
               _loc10_ = this.var_1304;
            }
            else if(this.var_120 & const_663)
            {
               _loc10_ = this.var_71.var_69["Sleep"];
            }
            else if(Boolean(this.var_120 & DROPPING) && Boolean(this.var_384))
            {
               _loc10_ = this.var_384;
            }
            else if(Boolean(this.var_120 & AIRBORNE) && Boolean(this.var_348))
            {
               _loc10_ = this.var_348;
            }
            else if(this.var_120 & RUNNING)
            {
               _loc10_ = this.var_463;
               _loc12_ = Boolean(this.var_120 & const_712);
            }
            if(_loc10_)
            {
               _loc7_ = true;
               if(this.var_30.var_153 != _loc10_ || this.var_1547 || _loc12_)
               {
                  _loc13_ = _loc10_.var_1802 == "Stunned";
                  this.method_180(_loc10_,_loc13_);
                  this.var_796 = _loc11_;
                  this.var_735 = false;
                  if(_loc10_ == this.var_463 && Boolean(this.var_120 & const_649))
                  {
                     _loc4_ = true;
                  }
               }
            }
            else if(!this.var_1547 && this.var_30.var_153 != this.var_218 && !this.var_2160)
            {
               _loc3_ = true;
            }
         }
         if(this.var_30.var_153 == this.var_218 && !this.var_350.bFireAndForget && !this.var_2054)
         {
            _loc7_ = true;
         }
         if(this.var_735)
         {
            _loc7_ = true;
         }
         if(this.var_1673 && !this.var_1547)
         {
            this.var_1673 = false;
            _loc3_ = true;
         }
         var _loc8_:int = int(this.var_324 + 0.2);
         if(_loc3_)
         {
            if(this.var_30.var_153 == this.var_463 && _loc8_ < this.var_30.var_751)
            {
               _loc8_ = int(this.var_30.var_710 - 1);
               this.var_324 = _loc8_;
            }
            else if(this.var_30.var_1463)
            {
               for each(_loc14_ in this.var_30.var_1463)
               {
                  if(this.var_2598 <= _loc14_ && _loc14_ <= this.var_324)
                  {
                     _loc8_ = int(this.var_30.var_408);
                     this.var_324 = _loc8_;
                  }
               }
            }
            else
            {
               _loc8_ = int(this.var_30.var_408);
               this.var_324 = _loc8_;
            }
         }
         else if(_loc4_)
         {
            _loc8_ = int(this.var_30.var_751);
            this.var_324 = _loc8_;
         }
         if(_loc7_ && (_loc8_ >= this.var_30.var_408 || _loc5_))
         {
            _loc15_ = _loc8_ - this.var_30.var_408;
            if(this.var_30.var_153 != this.var_30)
            {
               this.method_180(this.var_30.var_153,false,true);
            }
            else if(this.var_30.var_1077)
            {
               _loc17_ = 0;
               _loc18_ = Math.random();
               for each(_loc19_ in this.var_30.var_1077)
               {
                  _loc17_ += _loc19_.var_2482;
                  if(_loc18_ < _loc17_)
                  {
                     this.method_180(_loc19_,false,true);
                     break;
                  }
               }
            }
            _loc16_ = 0;
            if(!_loc5_)
            {
               if((_loc20_ = this.var_30.var_408 - this.var_30.var_751) < 1)
               {
                  _loc20_ = 1;
               }
               _loc16_ = _loc15_ % _loc20_;
            }
            this.var_317 = this.var_30.var_751 + _loc16_;
            this.var_324 = this.var_317;
         }
         else
         {
            if(this.var_30.var_153 != this.var_30 && !_loc7_ && _loc8_ >= this.var_30.var_408)
            {
               _loc21_ = _loc8_ - this.var_30.var_408;
               this.method_180(this.var_30.var_153,false,true);
               _loc8_ = this.var_30.var_408 + _loc21_;
            }
            if(_loc8_ >= this.var_30.var_710)
            {
               if(this.var_350.bFireAndForget || this.var_2054)
               {
                  _loc6_ = true;
               }
               else
               {
                  this.method_180(this.var_218,false);
               }
            }
            else
            {
               this.var_317 = _loc8_;
               if(_loc8_ >= this.var_30.var_408)
               {
                  this.var_1547 = true;
               }
            }
         }
         this.var_2741 = _loc7_ && this.var_324 == Number(this.var_30.var_751);
         if(this.var_317 >= this.var_30.var_2354)
         {
            this.var_796 = false;
         }
         this.var_314 = this.var_30.var_604[this.var_317];
         if(!this.var_314)
         {
            this.var_314 = this.var_30.method_242(this.var_317);
         }
         return _loc6_;
      }
      
      private function method_180(param1:class_26, param2:Boolean, param3:Boolean = false) : void
      {
         if(param2)
         {
            this.var_317 = uint((param1.var_408 - param1.var_751) * Math.random());
         }
         else
         {
            this.var_317 = 0;
         }
         this.var_324 = this.var_317;
         this.var_2598 = this.var_317;
         this.var_30 = param1;
         if(!param3)
         {
            this.var_1547 = false;
            this.var_796 = false;
            this.var_1673 = false;
            this.var_2160 = false;
            this.var_2083 = false;
         }
      }
      
      public function method_428() : void
      {
         this.var_735 = false;
         this.var_796 = false;
      }
      
      public function method_108() : void
      {
         this.var_735 = false;
         this.var_1673 = true;
      }
      
      public function method_131() : void
      {
         this.method_108();
         this.var_2054 = true;
      }
      
      public function method_34(param1:uint, param2:String, param3:Boolean) : void
      {
         var _loc4_:class_26;
         if(!(_loc4_ = this.var_71.var_69[param2]))
         {
            return;
         }
         this.var_1026 = param1;
         this.var_2378 = _loc4_;
         this.var_735 = param3;
      }
      
      public function method_869(param1:Number, param2:Number) : String
      {
         var _loc3_:String = null;
         var _loc4_:Number = Math.abs(param2);
         var _loc5_:Number;
         if((_loc5_ = Math.atan2(param1,_loc4_)) < 0)
         {
            _loc5_ = Math.PI * 2 + _loc5_;
         }
         var _loc6_:Number = 180 / Math.PI * _loc5_;
         var _loc7_:uint = uint(_loc6_ / 22.5);
         _loc3_ = String(const_119[_loc6_]);
         if(!_loc3_ || !this.var_71.var_69[_loc3_])
         {
            _loc3_ = "Shoot";
         }
         return _loc3_;
      }
   }
}
