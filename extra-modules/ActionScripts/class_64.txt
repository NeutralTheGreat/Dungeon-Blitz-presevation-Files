package
{
   import flash.display.MovieClip;
   
   public class class_64
   {
      
      internal static const const_142:uint = 9;
      
      internal static const const_218:uint = 5;
      
      internal static const const_499:uint = 2;
      
      private static var var_2472:Array = new Array();
      
      private static const const_866:uint = Math.pow(2,const_142) - 1;
      
      private static const const_1094:uint = Math.pow(2,const_218) - 1 << const_142;
      
      private static const const_912:uint = Math.pow(2,const_499) - 1 << const_142 + const_218;
      
      internal static const const_312:uint = 2;
      
      internal static const const_341:uint = 1;
      
      internal static const const_1333:uint = 0;
      
      internal static const const_1402:uint = 7;
      
      internal static const const_179:uint = 0;
      
      internal static const const_180:uint = 1;
      
      internal static const const_196:uint = 2;
      
      internal static const const_775:uint = 4;
      
      internal static const const_787:uint = 5;
      
      internal static const const_101:uint = 16;
      
      internal static const const_26:Array = ["","Trog","Infernal","Undead","Mythic","Draconic","Sylvan","Melee","Magic","Armor","RespecStone","CharmRemover"];
      
      internal static const const_1278:Array = ["","of Luck","of Skill","of Greed","of Foraging","of Carnage","of Health","of Strength","of the Mind","of Deflecting"];
      
      internal static const const_1155:Array = ["","of Fortune","of Precision","of Wealth","of Scouring","of Ruin","of Fortitude","of Might","of Brilliance","of Protection"];
      
      internal static const const_780:Array = ["Empty","R","L"];
      
      internal static const const_217:uint = 9;
      
      internal static const const_422:uint = 1;
      
      internal static const const_524:uint = 1;
      
      internal static const const_366:String = "RespecStone";
      
      internal static const const_323:String = "CharmRemover";
      
      internal static const const_1073:uint = 24 * 4 * 3600;
      
      internal static const const_1166:uint = 24 * 1 * 3600;
      
      internal static const const_729:Number = 1;
      
      internal static const const_593:Number = 0.5;
      
      internal static const const_522:Number = 0;
       
      
      internal var var_13:class_1;
      
      internal var secondary:uint;
      
      internal var var_8:uint;
      
      public function class_64(param1:class_1 = null, param2:uint = 0, param3:uint = 0)
      {
         super();
         this.var_13 = param1;
         this.secondary = param2;
         this.var_8 = param3;
      }
      
      public static function method_56(param1:uint) : class_64
      {
         var _loc2_:uint = uint(param1 & const_866);
         var _loc3_:class_1 = class_14.var_767[_loc2_];
         if(!_loc3_)
         {
            return null;
         }
         var _loc4_:uint = uint((param1 & const_1094) >> const_142);
         var _loc5_:uint = uint((param1 & const_912) >> const_142 + const_218);
         return new class_64(_loc3_,_loc4_,_loc5_);
      }
      
      public static function method_2141(param1:uint) : uint
      {
         var _loc2_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc3_:uint = param1;
         _loc2_ = 0;
         while(_loc3_)
         {
            _loc2_ += _loc3_ & 1;
            _loc3_ >>= 1;
         }
         if(const_217 == _loc2_)
         {
            return 0;
         }
         _loc4_ = Math.floor(Math.random() * (const_217 - _loc2_));
         _loc6_ = 0;
         _loc5_ = 0;
         while(_loc5_ < const_217)
         {
            if((1 << _loc5_ & param1) == 0)
            {
               if(_loc4_ == 0)
               {
                  break;
               }
               _loc4_--;
            }
            _loc5_++;
         }
         return _loc5_ + 1;
      }
      
      public static function method_830(param1:uint) : uint
      {
         var _loc2_:uint = 0;
         if(param1 > 0 && param1 <= class_8.const_890)
         {
            _loc2_ = uint(class_8.const_1018[param1 - 1]);
         }
         return _loc2_;
      }
      
      public function method_266() : void
      {
         this.var_13 = null;
      }
      
      public function method_538() : class_64
      {
         return new class_64(this.var_13,this.secondary,this.var_8);
      }
      
      public function method_75() : uint
      {
         if(!this.var_13)
         {
            return 0;
         }
         return uint(this.var_13.var_68 | this.secondary << const_142 | this.var_8 << const_142 + const_218);
      }
      
      public function method_1842() : MovieClip
      {
         var _loc1_:MovieClip = class_4.method_16(this.var_13.iconName);
         var _loc2_:String = this.method_718();
         if(!this.method_396())
         {
            _loc1_.am_SecondaryCharm.gotoAndStop(_loc2_);
         }
         return _loc1_;
      }
      
      public function method_78(param1:class_32, param2:MovieClip) : MovieClip
      {
         var _loc3_:MovieClip = param1.method_12(param2,this.var_13.iconName);
         var _loc4_:String = this.method_718();
         if(!this.method_396())
         {
            _loc3_.am_SecondaryCharm.gotoAndStop(_loc4_);
         }
         return _loc3_;
      }
      
      public function method_115() : class_1
      {
         var _loc3_:String = null;
         var _loc4_:String = null;
         var _loc5_:String = null;
         var _loc1_:class_1 = this.var_13;
         var _loc2_:class_1 = null;
         if(_loc1_)
         {
            if(this.secondary)
            {
               _loc3_ = this.method_818();
               _loc5_ = (_loc4_ = String(const_26[this.secondary])) + _loc3_;
               _loc2_ = class_14.var_142[_loc5_];
            }
         }
         return _loc2_;
      }
      
      public function method_171() : String
      {
         var _loc1_:class_1 = this.method_115();
         var _loc2_:String = _loc1_.var_203;
         var _loc3_:Number = this.method_421() * parseFloat(_loc2_);
         var _loc4_:int = _loc2_.indexOf(" ");
         var _loc5_:int = _loc2_.indexOf("%");
         var _loc6_:String = "";
         if(_loc5_ > -1)
         {
            _loc6_ = "%";
         }
         return "+" + _loc3_ + _loc6_ + " " + _loc2_.substr(_loc4_ + 1);
      }
      
      public function method_2105() : String
      {
         if(!this.var_13)
         {
            return "";
         }
         var _loc1_:String = this.var_13.var_203;
         if(this.secondary)
         {
            _loc1_ += ", " + this.method_171();
         }
         return _loc1_;
      }
      
      public function method_1418() : String
      {
         if(this.var_8 == const_180)
         {
            return const_1278[this.secondary];
         }
         if(this.var_8 == const_196)
         {
            return const_1155[this.secondary];
         }
         return "";
      }
      
      public function method_718() : String
      {
         var _loc1_:class_1 = this.method_115();
         if(_loc1_)
         {
            return _loc1_.var_115 + const_780[this.var_8];
         }
         return "Empty";
      }
      
      public function method_49() : String
      {
         if(!this.var_13)
         {
            return "";
         }
         var _loc1_:String = this.var_13.displayName;
         if(this.secondary)
         {
            _loc1_ += " " + this.method_1418();
         }
         return _loc1_;
      }
      
      public function method_421() : Number
      {
         if(this.var_8 == 0)
         {
            return const_522;
         }
         if(this.var_8 == 1)
         {
            return const_593;
         }
         if(this.var_8 == 2)
         {
            return const_729;
         }
         return const_522;
      }
      
      public function method_818() : String
      {
         if(!this.var_13)
         {
            return "";
         }
         var _loc1_:String = this.var_13.var_115;
         var _loc2_:String = this.var_13.var_693;
         return _loc2_.replace(_loc1_,"");
      }
      
      public function method_2020() : uint
      {
         return uint(this.method_818());
      }
      
      public function method_1708() : Boolean
      {
         return this.var_13.var_68 == class_1.const_405;
      }
      
      public function method_118() : Boolean
      {
         return class_1.method_118(this.var_13);
      }
      
      public function method_124() : Boolean
      {
         return class_1.method_124(this.var_13);
      }
      
      public function method_379() : Boolean
      {
         return this.var_13.var_68 == class_1.const_459;
      }
      
      public function method_396() : Boolean
      {
         return this.var_13.var_68 == class_1.const_459 || this.var_13.var_68 == class_1.const_405;
      }
   }
}
