package
{
   public class class_86
   {
      
      public static const const_369:uint = 50;
      
      public static const const_222:Array = [0,8,24,55,102,168,254,364,503,679,904,1182,1521,1929,2414,2985,3658,4443,5340,6359,7500,8784,10210,11840,13674,15712,18157,21009,24269,27936,32011,36493,41382,46679,52383,58495,65014,71940,79274,86608,93942,101276,108610,115944,123278,130612,137946,145280,152614,159948,2147483648];
      
      public static const const_935:uint = 15;
      
      public static const const_873:uint = 240;
      
      public static const const_1095:uint = 3840;
      
      public static const const_1269:uint = 61440;
      
      public static const const_1042:uint = 983040;
      
      public static const const_84:uint = 4;
      
      public static const const_174:uint = 0;
      
      public static const const_146:uint = 1;
      
      public static const const_210:uint = 2;
      
      public static const const_255:uint = 3;
      
      public static const const_193:uint = 4;
      
      public static const const_373:uint = 5;
      
      public static const const_33:uint = 10;
      
      public static const const_184:Vector.<String> = new Vector.<String>(const_373,true);
      
      public static const const_204:Vector.<String> = new Vector.<String>(const_373,true);
      
      public static const const_144:Vector.<Array> = new Vector.<Array>(const_373,true);
      
      {
         const_184[0] = "Furnace";
         const_204[0] = "Decreases the time it takes to craft a charm";
         const_144[0] = "0% 1% 2% 3% 4% 5% 6% 7% 8% 9% 10%".split(" ");
         const_184[1] = "Anvil";
         const_204[1] = "Increases your chance to craft a rare or legendary charm";
         const_144[1] = "0%,0% 0.9%,0.4% 1.8%,0.8% 2.7%,1.2% 3.6%,1.6% 4.5%,2.0% 5.4%,2.4% 6.3%,2.8% 7.2%,3.2% 8.1%,3.6% 9%,4%".split(" ");
         const_184[2] = "Hammer";
         const_204[2] = "Decreases material required to gain craft bonuses";
         const_144[2] = "0% 2% 4% 6% 8% 10% 12% 14% 16% 18% 20%".split(" ");
         const_184[3] = "Bellows";
         const_204[3] = "Increases the total number of materials for each charm";
         const_144[3] = "6 12 18 24 30 36 42 48 54 60 66".split(" ");
         const_184[4] = "Coals";
         const_204[4] = "Increases the speed that craft experience is gained";
         const_144[4] = "0% 3% 6% 9% 12% 15% 18% 21% 24% 27% 30%".split(" ");
      }
      
      internal var var_1:Game;
      
      internal var craftXP:uint = 0;
      
      internal var var_965:uint = 0;
      
      internal var var_1017:uint = 0;
      
      internal var var_905:uint = 0;
      
      internal var var_585:uint = 0;
      
      internal var var_946:uint = 0;
      
      internal var var_861:uint = 0;
      
      internal var var_827:uint = 0;
      
      internal var var_809:uint = 0;
      
      internal var var_763:uint = 0;
      
      internal var var_856:uint = 0;
      
      internal var craftLevel:uint = 0;
      
      public function class_86(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public static function method_380(param1:uint) : uint
      {
         var _loc2_:uint = 1;
         while(_loc2_ <= const_369)
         {
            if(param1 < const_222[_loc2_])
            {
               return _loc2_;
            }
            _loc2_++;
         }
         return const_369;
      }
      
      public function method_1681(param1:uint) : void
      {
         this.var_965 = (param1 & const_935) >> const_84 * const_174;
         this.var_1017 = (param1 & const_873) >> const_84 * const_146;
         this.var_905 = (param1 & const_1095) >> const_84 * const_210;
         this.var_585 = (param1 & const_1269) >> const_84 * const_255;
         this.var_946 = (param1 & const_1042) >> const_84 * const_193;
      }
      
      public function method_1965(param1:uint, param2:uint) : void
      {
         this.craftXP = param2;
         this.craftLevel = method_380(this.craftXP);
         this.method_1681(param1);
      }
      
      public function SetXP(param1:uint) : void
      {
         this.craftXP = param1;
         this.craftLevel = method_380(this.craftXP);
      }
      
      public function GetCraftTalentBonus(param1:uint) : uint
      {
         var _loc2_:uint = 0;
         switch(param1)
         {
            case const_174:
               _loc2_ = this.var_965;
               break;
            case const_146:
               _loc2_ = this.var_1017;
               break;
            case const_210:
               _loc2_ = this.var_905;
               break;
            case const_255:
               _loc2_ = this.var_585;
               break;
            case const_193:
               _loc2_ = this.var_946;
         }
         return _loc2_;
      }
      
      public function method_1297(param1:uint) : uint
      {
         var _loc2_:uint = 0;
         switch(param1)
         {
            case const_174:
               _loc2_ = this.var_861;
               break;
            case const_146:
               _loc2_ = this.var_827;
               break;
            case const_210:
               _loc2_ = this.var_809;
               break;
            case const_255:
               _loc2_ = this.var_763;
               break;
            case const_193:
               _loc2_ = this.var_856;
         }
         return _loc2_;
      }
      
      public function method_1843(param1:uint) : void
      {
         switch(param1)
         {
            case const_174:
               ++this.var_861;
               if(this.var_861 + this.var_965 > const_33)
               {
                  this.var_861 = const_33;
               }
               break;
            case const_146:
               ++this.var_827;
               if(this.var_827 + this.var_1017 > const_33)
               {
                  this.var_827 = const_33;
               }
               break;
            case const_210:
               ++this.var_809;
               if(this.var_809 + this.var_905 > const_33)
               {
                  this.var_809 = const_33;
               }
               break;
            case const_255:
               ++this.var_763;
               if(this.var_763 + this.var_585 > const_33)
               {
                  this.var_763 = const_33;
               }
               break;
            case const_193:
               ++this.var_856;
               if(this.var_856 + this.var_946 > const_33)
               {
                  this.var_856 = const_33;
                  break;
               }
         }
      }
      
      public function method_1785() : void
      {
         if(!this.var_1.CanSendPacket())
         {
            return;
         }
         var _loc1_:uint = uint(this.var_965 << const_174 * const_84 | this.var_1017 << const_146 * const_84 | this.var_905 << const_210 * const_84 | this.var_585 << const_255 * const_84 | this.var_946 << const_193 * const_84);
         var _loc2_:Packet = new Packet(LinkUpdater.const_1047);
         _loc2_.method_9(_loc1_);
         this.var_1.serverConn.SendPacket(_loc2_);
      }
      
      public function method_1307() : void
      {
         this.var_965 += this.var_861;
         this.var_1017 += this.var_827;
         this.var_905 += this.var_809;
         this.var_585 += this.var_763;
         this.var_946 += this.var_856;
         this.method_496();
      }
      
      public function method_496() : void
      {
         this.var_861 = this.var_827 = this.var_809 = this.var_763 = this.var_856 = 0;
      }
      
      public function GetTalentPointsRemaining() : uint
      {
         return this.craftLevel - (this.method_554() + this.GetTotalPendingPoints());
      }
      
      public function method_554() : uint
      {
         return this.var_965 + this.var_1017 + this.var_905 + this.var_585 + this.var_946;
      }
      
      public function GetTotalPendingPoints() : uint
      {
         return this.var_861 + this.var_827 + this.var_809 + this.var_763 + this.var_856;
      }
      
      public function GetTimeAfterBonuses(param1:class_1) : uint
      {
         var _loc2_:uint = param1.var_930;
         if(!this.craftXP && _loc2_ == 1)
         {
            return Game.const_181;
         }
         if(param1.var_68 == class_1.const_405)
         {
            if(this.var_1.mMagicForgeStatus.var_2434)
            {
               return class_64.const_1073;
            }
            return Game.const_181;
         }
         if(param1.var_68 == class_1.const_459)
         {
            return class_64.const_1166;
         }
         var _loc3_:Number = 0;
         _loc3_ = this.GetCraftTalentBonus(class_86.const_174);
         return Math.ceil(class_8.const_1055[_loc2_ - 1] * (1 - _loc3_ * class_8.const_1299));
      }
      
      public function GetXpGained(param1:class_1) : uint
      {
         if(!param1)
         {
            return 0;
         }
         var _loc2_:uint = param1.var_930;
         if(_loc2_ == 0)
         {
            return 0;
         }
         return Math.ceil(class_8.const_1119[_loc2_ - 1] * (1 + this.GetCraftTalentBonus(const_193) * class_8.const_1191));
      }
      
      public function GetMaxMats() : uint
      {
         if(this.var_585 >= 0 && this.var_585 < class_8.const_395.length)
         {
            return class_8.const_395[this.var_585];
         }
         return 0;
      }
   }
}
