package
{
   import flash.utils.Dictionary;
   
   public class class_150
   {
      
      public static const const_1120:uint = 7;
      
      public static const const_93:uint = 0;
      
      public static const const_88:uint = 1;
      
      public static const const_87:uint = 2;
      
      public static const const_91:uint = 3;
      
      public static const const_97:uint = 4;
      
      public static const const_81:uint = 5;
      
      public static const const_44:uint = 6;
      
      public static const const_168:Vector.<String> = new Vector.<String>(EntType.MAX_SLOTS,true);
      
      public static const const_143:Vector.<String> = new Vector.<String>(EntType.MAX_SLOTS,true);
      
      public static const const_170:Vector.<String> = new Vector.<String>(EntType.MAX_SLOTS,true);
      
      public static const const_327:Vector.<String> = new Vector.<String>(ScreenArmory.const_504,true);
      
      public static const const_239:Vector.<String> = new Vector.<String>(ScreenArmory.const_514,true);
      
      public static const const_98:Vector.<String> = new Vector.<String>(ScreenArmory.const_513,true);
      
      public static const const_262:Vector.<String> = new Vector.<String>(ScreenArmory.const_497,true);
      
      public static const const_1326:uint = 3;
      
      public static const const_1399:uint = 5;
      
      {
         const_262[0] = "Gear Find";
         const_262[1] = "Material Find";
         const_262[2] = "Gold Find";
         const_262[3] = "Speed";
         const_98[0] = "Ruby";
         const_98[1] = "Amethyst";
         const_98[2] = "Emerald";
         const_98[3] = "Topaz";
         const_98[4] = "Diamond";
         const_98[5] = "Zircon";
         const_98[6] = "Onyx";
         const_98[7] = "Sapphire";
         const_98[8] = "Citrine";
         const_239[0] = "Attack";
         const_239[1] = "Expertise";
         const_239[2] = "Defense";
         const_239[3] = "Balanced";
         const_327[0] = "Magic";
         const_327[1] = "Rare";
         const_327[2] = "Legendary";
         const_168[1] = "Robes";
         const_168[2] = "Gloves";
         const_168[3] = "Boots";
         const_168[4] = "Jewelry";
         const_168[5] = "Staves";
         const_168[6] = "Focuses";
         const_143[1] = "Sashes";
         const_143[2] = "Gloves";
         const_143[3] = "Boots";
         const_143[4] = "Hoods";
         const_143[5] = "Mainhands";
         const_143[6] = "Offhands";
         const_170[1] = "Armor";
         const_170[2] = "Gloves";
         const_170[3] = "Boots";
         const_170[4] = "Helms";
         const_170[5] = "Weapons";
         const_170[6] = "Shields";
      }
      
      private var var_244:Vector.<Boolean>;
      
      private var var_1505:Vector.<Boolean>;
      
      private var var_870:Vector.<Boolean>;
      
      private var var_1603:Vector.<Boolean>;
      
      private var var_1544:Vector.<Boolean>;
      
      private var var_1256:Vector.<Boolean>;
      
      private var var_1058:Vector.<Boolean>;
      
      private var var_1369:Vector.<String>;
      
      private var var_1370:Vector.<String>;
      
      private var var_1636:Vector.<String>;
      
      private var var_1381:Vector.<String>;
      
      private var var_180:Dictionary;
      
      private var var_1503:Vector.<String>;
      
      private var var_1071:Vector.<String>;
      
      public var var_126:Vector.<Vector.<Boolean>>;
      
      internal var name_1:Array;
      
      internal var var_2785:Array;
      
      internal var var_2660:Array;
      
      internal var var_2683:Array;
      
      internal var var_2910:Array;
      
      internal var var_2266:Array;
      
      internal var var_2578:Array;
      
      internal var var_1964:Array;
      
      internal var var_1887:Array;
      
      internal var var_2837:Array;
      
      internal var var_2310:String = "CritDamage";
      
      internal var var_2244:String = "CritChance";
      
      internal var var_2084:String = "HealthPercent";
      
      internal var var_2143:String = "RecoveryBoost";
      
      internal var var_2068:String = "Haste";
      
      internal var var_2213:String = "Resilience";
      
      public var var_27:Vector.<PowerType>;
      
      public var var_797:Vector.<PowerType>;
      
      private var var_1:Game;
      
      public function class_150(param1:Game)
      {
         this.name_1 = new Array("","Armor","Gloves","Boots","Hat","Sword","Shield");
         this.var_2785 = new Array("M","R","L");
         this.var_2660 = new Array("Attack","Expertise","Armor","Balanced");
         this.var_2683 = new Array("Draconic","Infernal","Sylvan","Undead","Trog","Mythic","Armor","Magic","Melee");
         this.var_2910 = new Array("ItemFind","CraftFind","GoldFind","Speed");
         this.var_2266 = new Array("ProcHeal","ProcHealTime","ProcMassive","ProcMassiveTime","ProcAir","ProcDeath","ProcEarth","ProcFire","ProcIce","ProcLife");
         this.var_2578 = new Array("AirSlay","DeathSlay","EarthSlay","FireSlay","IceSlay","LifeSlay","ResistAir","ResistDeath","ResistEarth","ResistFire","ResistIce","ResistLife","Haste","Resilience","HealthPercent","RecoveryBoost","CritChance","CritDamage");
         this.var_1964 = new Array("ResistAir","ResistDeath","ResistEarth","ResistFire","ResistIce","ResistLife");
         this.var_1887 = new Array("AirSlay","DeathSlay","EarthSlay","FireSlay","IceSlay","LifeSlay");
         this.var_2837 = new Array("ProcAir","ProcDeath","ProcEarth","ProcFire","ProcIce","ProcLife","ProcMassive","ProcMassiveTime","ProcHeal","ProcHealTime");
         super();
         this.var_1 = param1;
         this.var_244 = new Vector.<Boolean>(EntType.MAX_SLOTS,true);
         this.var_1505 = new Vector.<Boolean>(ScreenArmory.const_504,true);
         this.var_870 = new Vector.<Boolean>(ScreenArmory.const_514,true);
         this.var_1603 = new Vector.<Boolean>(ScreenArmory.const_513,true);
         this.var_1544 = new Vector.<Boolean>(ScreenArmory.const_497,true);
         this.var_1256 = new Vector.<Boolean>(ScreenArmory.const_815,true);
         this.var_1058 = new Vector.<Boolean>(ScreenArmory.const_155,true);
         this.var_126 = new Vector.<Vector.<Boolean>>(const_1120,true);
         this.var_27 = new Vector.<PowerType>(3);
         this.var_126[const_93] = this.var_244;
         this.var_126[const_88] = this.var_1505;
         this.var_126[const_87] = this.var_870;
         this.var_126[const_91] = this.var_1603;
         this.var_126[const_97] = this.var_1544;
         this.var_126[const_81] = this.var_1256;
         this.var_126[const_44] = this.var_1058;
      }
      
      public function method_1233() : void
      {
         this.var_244 = null;
         this.var_1505 = null;
         this.var_870 = null;
         this.var_1603 = null;
         this.var_1544 = null;
         this.var_1256 = null;
         this.var_1058 = null;
         this.var_126 = null;
      }
      
      public function method_178(param1:uint, param2:uint) : Boolean
      {
         if(param1 < this.var_126.length && param2 < this.var_126[param1].length)
         {
            return this.var_126[param1][param2];
         }
         return false;
      }
      
      public function Toggle(param1:uint, param2:uint, param3:Boolean = false) : void
      {
         var _loc4_:uint = 0;
         if(param1 < this.var_126.length && param2 < this.var_126[param1].length)
         {
            this.var_126[param1][param2] = !this.var_126[param1][param2];
         }
         if(param1 == const_87)
         {
            _loc4_ = 0;
            while(_loc4_ < this.var_870.length)
            {
               if(_loc4_ != param2)
               {
                  this.var_870[_loc4_] = false;
               }
               _loc4_++;
            }
         }
         if(!param3)
         {
            this.method_798();
            this.var_1.screenArmory.Refresh();
         }
      }
      
      public function method_119() : void
      {
         var _loc2_:uint = 0;
         var _loc1_:uint = 0;
         while(_loc1_ < this.var_126.length)
         {
            _loc2_ = 0;
            while(_loc2_ < this.var_126[_loc1_].length)
            {
               this.var_126[_loc1_][_loc2_] = false;
               _loc2_++;
            }
            _loc1_++;
         }
         this.var_1.mFilteredOwnedGear = this.var_1.var_144;
      }
      
      public function method_1047() : Boolean
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         while(_loc2_ < this.var_244.length)
         {
            if(this.var_244[_loc2_])
            {
               _loc1_++;
            }
            _loc2_++;
         }
         return _loc1_ == 1;
      }
      
      public function method_1096() : Boolean
      {
         var _loc1_:Boolean = this.var_244[EntType.SWORD_SLOT];
         var _loc2_:Boolean = false;
         var _loc3_:uint = 1;
         while(_loc3_ < this.var_244.length)
         {
            if(_loc3_ != EntType.SWORD_SLOT)
            {
               _loc2_ = this.var_244[_loc3_] || _loc2_;
            }
            _loc3_++;
         }
         return _loc2_ != _loc1_;
      }
      
      public function method_394() : Vector.<PowerType>
      {
         var _loc4_:uint = 0;
         var _loc5_:PowerType = null;
         var _loc1_:Boolean = this.var_244[EntType.SWORD_SLOT];
         this.var_797 = new Vector.<PowerType>();
         var _loc2_:Vector.<String> = new Vector.<String>(10);
         _loc2_[0] = "ProcHeal";
         _loc2_[1] = "ProcHealTime";
         _loc2_[2] = "ProcMassive";
         _loc2_[3] = "ProcMassiveTime";
         _loc2_[4] = "ProcAir";
         _loc2_[5] = "ProcDeath";
         _loc2_[6] = "ProcEarth";
         _loc2_[7] = "ProcFire";
         _loc2_[8] = "ProcIce";
         _loc2_[9] = "ProcLife";
         var _loc3_:Vector.<String> = new Vector.<String>(18);
         _loc3_[0] = "AirSlay";
         _loc3_[1] = "DeathSlay";
         _loc3_[2] = "EarthSlay";
         _loc3_[3] = "FireSlay";
         _loc3_[4] = "IceSlay";
         _loc3_[5] = "LifeSlay";
         _loc3_[6] = "ResistAir";
         _loc3_[7] = "ResistDeath";
         _loc3_[8] = "ResistEarth";
         _loc3_[9] = "ResistFire";
         _loc3_[10] = "ResistIce";
         _loc3_[11] = "ResistLife";
         _loc3_[12] = "Haste";
         _loc3_[13] = "Resilience";
         _loc3_[14] = "HealthPercent";
         _loc3_[15] = "RecoveryBoost";
         _loc3_[16] = "CritChance";
         _loc3_[17] = "CritDamage";
         if(_loc1_)
         {
            _loc4_ = 0;
            while(_loc4_ < _loc2_.length)
            {
               if(_loc5_ = class_14.powerTypesDict[_loc2_[_loc4_]])
               {
                  this.var_797.push(_loc5_);
               }
               _loc4_++;
            }
         }
         else
         {
            _loc4_ = 0;
            while(_loc4_ < _loc3_.length)
            {
               if(_loc5_ = class_14.powerTypesDict[_loc3_[_loc4_]])
               {
                  this.var_797.push(_loc5_);
               }
               _loc4_++;
            }
         }
         return this.var_797;
      }
      
      public function method_1234() : void
      {
         var _loc1_:uint = 0;
         while(_loc1_ < this.var_1256.length)
         {
            this.var_126[const_81][_loc1_] = false;
            _loc1_++;
         }
      }
      
      public function method_1930() : void
      {
         var _loc1_:uint = 0;
         while(_loc1_ < this.var_1058.length)
         {
            this.var_126[const_44][_loc1_] = false;
            _loc1_++;
         }
      }
      
      public function method_1919(param1:uint) : void
      {
         if(param1 < this.var_126[const_44].length)
         {
            this.var_126[const_44][param1] = false;
         }
      }
      
      public function method_1051() : Vector.<PowerType>
      {
         var _loc1_:String = null;
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         var _loc4_:Entity = null;
         if(this.var_1.clientEnt)
         {
            _loc1_ = this.var_1.clientEnt.entType.className;
            _loc2_ = 0;
            _loc3_ = 1;
            while(_loc3_ < this.var_244.length)
            {
               if(this.var_244[_loc3_])
               {
                  _loc2_ = _loc3_;
                  break;
               }
               _loc3_++;
            }
            _loc4_ = this.var_1.clientEnt;
            if(_loc1_ == "Mage" && _loc2_ == EntType.SWORD_SLOT)
            {
               this.var_27[0] = class_14.powerTypesDict["FireBlast"];
               this.var_27[1] = class_14.powerTypesDict["IceSpike"];
               this.var_27[2] = class_14.powerTypesDict["VineLance"];
            }
            if(_loc1_ == "Mage" && _loc2_ == EntType.SHIELD_SLOT)
            {
               this.var_27[0] = class_14.powerTypesDict["FirePillar"];
               this.var_27[1] = class_14.powerTypesDict["IceNova"];
               this.var_27[2] = class_14.powerTypesDict["PoisonCloud"];
            }
            if(_loc1_ == "Mage" && _loc2_ == EntType.HAT_SLOT)
            {
               this.var_27[0] = _loc4_.method_38("Frostwarden",6);
               this.var_27[1] = _loc4_.method_38("Flameseer",6);
               this.var_27[2] = _loc4_.method_38("Necromancer",6);
            }
            if(_loc1_ == "Mage" && _loc2_ == EntType.ARMOR_SLOT)
            {
               this.var_27[0] = class_14.powerTypesDict["Meteor"];
               this.var_27[1] = class_14.powerTypesDict["SummonGuard"];
               this.var_27[2] = class_14.powerTypesDict["IceStorm"];
            }
            if(_loc1_ == "Mage" && _loc2_ == EntType.GLOVES_SLOT)
            {
               this.var_27[0] = _loc4_.method_38("Frostwarden",4);
               this.var_27[1] = _loc4_.method_38("Flameseer",4);
               this.var_27[2] = _loc4_.method_38("Necromancer",4);
            }
            if(_loc1_ == "Mage" && _loc2_ == EntType.BOOTS_SLOT)
            {
               this.var_27[0] = _loc4_.method_38("Frostwarden",5);
               this.var_27[1] = _loc4_.method_38("Flameseer",5);
               this.var_27[2] = _loc4_.method_38("Necromancer",5);
            }
            if(_loc1_ == "Rogue" && _loc2_ == EntType.SWORD_SLOT)
            {
               this.var_27[0] = class_14.powerTypesDict["QuickStrike"];
               this.var_27[1] = class_14.powerTypesDict["StunStrike"];
               this.var_27[2] = class_14.powerTypesDict["PoisonStrike"];
            }
            if(_loc1_ == "Rogue" && _loc2_ == EntType.SHIELD_SLOT)
            {
               this.var_27[0] = class_14.powerTypesDict["RootStrike"];
               this.var_27[1] = class_14.powerTypesDict["SteelCyclone"];
               this.var_27[2] = class_14.powerTypesDict["Enfeeble"];
            }
            if(_loc1_ == "Rogue" && _loc2_ == EntType.HAT_SLOT)
            {
               this.var_27[0] = _loc4_.method_38("Executioner",6);
               this.var_27[1] = _loc4_.method_38("ShadowWalker",6);
               this.var_27[2] = _loc4_.method_38("Soulthief",6);
            }
            if(_loc1_ == "Rogue" && _loc2_ == EntType.ARMOR_SLOT)
            {
               this.var_27[0] = class_14.powerTypesDict["HawkStrike"];
               this.var_27[1] = class_14.powerTypesDict["Decoy"];
               this.var_27[2] = class_14.powerTypesDict["ReduceArmor"];
            }
            if(_loc1_ == "Rogue" && _loc2_ == EntType.GLOVES_SLOT)
            {
               this.var_27[0] = _loc4_.method_38("Executioner",4);
               this.var_27[1] = _loc4_.method_38("ShadowWalker",4);
               this.var_27[2] = _loc4_.method_38("Soulthief",4);
            }
            if(_loc1_ == "Rogue" && _loc2_ == EntType.BOOTS_SLOT)
            {
               this.var_27[0] = _loc4_.method_38("Executioner",5);
               this.var_27[1] = _loc4_.method_38("ShadowWalker",5);
               this.var_27[2] = _loc4_.method_38("Soulthief",5);
            }
            if(_loc1_ == "Paladin" && _loc2_ == EntType.SWORD_SLOT)
            {
               this.var_27[0] = class_14.powerTypesDict["Cleave"];
               this.var_27[1] = class_14.powerTypesDict["Smash"];
               this.var_27[2] = class_14.powerTypesDict["Skewer"];
            }
            if(_loc1_ == "Paladin" && _loc2_ == EntType.SHIELD_SLOT)
            {
               this.var_27[0] = class_14.powerTypesDict["ShieldStun"];
               this.var_27[1] = class_14.powerTypesDict["TouchHeal"];
               this.var_27[2] = class_14.powerTypesDict["Warcry"];
            }
            if(_loc1_ == "Paladin" && _loc2_ == EntType.HAT_SLOT)
            {
               this.var_27[0] = _loc4_.method_38("Sentinel",6);
               this.var_27[1] = _loc4_.method_38("Justicar",6);
               this.var_27[2] = _loc4_.method_38("Templar",6);
            }
            if(_loc1_ == "Paladin" && _loc2_ == EntType.ARMOR_SLOT)
            {
               this.var_27[0] = class_14.powerTypesDict["JumpSlam"];
               this.var_27[1] = class_14.powerTypesDict["GroupHoT"];
               this.var_27[2] = class_14.powerTypesDict["ToughShout"];
            }
            if(_loc1_ == "Paladin" && _loc2_ == EntType.GLOVES_SLOT)
            {
               this.var_27[0] = _loc4_.method_38("Sentinel",4);
               this.var_27[1] = _loc4_.method_38("Justicar",4);
               this.var_27[2] = _loc4_.method_38("Templar",4);
            }
            if(_loc1_ == "Paladin" && _loc2_ == EntType.BOOTS_SLOT)
            {
               this.var_27[0] = _loc4_.method_38("Sentinel",5);
               this.var_27[1] = _loc4_.method_38("Justicar",5);
               this.var_27[2] = _loc4_.method_38("Templar",5);
            }
         }
         return this.var_27;
      }
      
      public function method_888(param1:uint, param2:uint) : String
      {
         var _loc3_:Vector.<String> = null;
         var _loc5_:String = null;
         var _loc4_:String = "";
         if(this.var_1.clientEnt)
         {
            if((_loc5_ = this.var_1.clientEnt.entType.className) == "Mage")
            {
               _loc3_ = const_168;
            }
            if(_loc5_ == "Rogue")
            {
               _loc3_ = const_143;
            }
            if(_loc5_ == "Paladin")
            {
               _loc3_ = const_170;
            }
         }
         if(param1 == const_93)
         {
            if(Boolean(_loc3_) && param2 < _loc3_.length)
            {
               _loc4_ = _loc3_[param2];
            }
         }
         if(param1 == const_88)
         {
            _loc4_ = const_327[param2];
         }
         if(param1 == const_87)
         {
            _loc4_ = const_239[param2];
         }
         if(param1 == const_91)
         {
            _loc4_ = const_98[param2];
         }
         if(param1 == const_97)
         {
            _loc4_ = const_262[param2];
         }
         if(param1 == const_81)
         {
            if(Boolean(this.var_27) && param2 < this.var_27.length)
            {
               _loc4_ = this.var_27[param2].displayName;
            }
         }
         if(param1 == const_44)
         {
            if(Boolean(this.var_797) && param2 < this.var_797.length)
            {
               _loc4_ = this.var_797[param2].displayName;
            }
         }
         return _loc4_;
      }
      
      public function method_635(param1:uint, param2:uint) : String
      {
         var _loc4_:class_17 = null;
         var _loc3_:String = "";
         if(param1 == const_93 || param1 == const_88 || param1 == const_87 || param1 == const_91 || param1 == const_97)
         {
            _loc3_ = this.method_888(param1,param2);
         }
         else if(param1 == const_81)
         {
            if(_loc4_ = class_14.var_274["Rune" + this.var_27[param2].basePowerName])
            {
               _loc3_ = !!_loc4_.description ? String(_loc4_.description[0]) : "";
            }
         }
         else if(param1 == const_44)
         {
            _loc3_ = this.var_797[param2].description;
         }
         return _loc3_;
      }
      
      public function method_798() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc5_:String = null;
         var _loc6_:class_42 = null;
         this.var_1369 = new Vector.<String>();
         this.var_1370 = new Vector.<String>();
         this.var_1636 = new Vector.<String>();
         this.var_1381 = new Vector.<String>();
         this.var_180 = new Dictionary();
         this.var_1503 = new Vector.<String>();
         this.var_1071 = new Vector.<String>();
         var _loc3_:Boolean = false;
         _loc1_ = 1;
         while(_loc1_ < this.var_244.length)
         {
            if(this.var_244[_loc1_])
            {
               this.var_1369.push(this.name_1[_loc1_]);
               if(_loc1_ == EntType.SWORD_SLOT)
               {
                  _loc3_ = true;
               }
               _loc2_ = _loc1_;
            }
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_1505.length)
         {
            if(this.var_1505[_loc1_])
            {
               this.var_1370.push(this.var_2785[_loc1_]);
            }
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_870.length)
         {
            if(this.var_870[_loc1_])
            {
               _loc5_ = this.var_1.clientEnt.entType.className;
               this.var_1636.push(_loc5_ + this.var_2660[_loc1_]);
            }
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_1603.length)
         {
            if(this.var_1603[_loc1_])
            {
               this.var_1381.push(this.var_2683[_loc1_]);
            }
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_1544.length)
         {
            if(this.var_1544[_loc1_])
            {
               if(_loc1_ == 0)
               {
                  this.var_180["ItemDrop"] = true;
                  this.var_180["ItemDrop+CraftDrop"] = true;
                  this.var_180["ItemDrop+GoldDrop"] = true;
                  this.var_180["Speed+ItemDrop"] = true;
               }
               if(_loc1_ == 1)
               {
                  this.var_180["CraftDrop"] = true;
                  this.var_180["ItemDrop+CraftDrop"] = true;
                  this.var_180["GoldDrop+CraftDrop"] = true;
                  this.var_180["Speed+CraftDrop"] = true;
               }
               if(_loc1_ == 2)
               {
                  this.var_180["GoldDrop"] = true;
                  this.var_180["GoldDrop+CraftDrop"] = true;
                  this.var_180["ItemDrop+GoldDrop"] = true;
                  this.var_180["Speed+GoldDrop"] = true;
               }
               if(_loc1_ == 3)
               {
                  this.var_180["Speed"] = true;
                  this.var_180["Speed+CraftDrop"] = true;
                  this.var_180["Speed+ItemDrop"] = true;
                  this.var_180["Speed+GoldDrop"] = true;
               }
            }
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_1256.length)
         {
            if(this.var_1256[_loc1_])
            {
               this.var_1503.push(this.var_27[_loc1_].basePowerName);
            }
            _loc1_++;
         }
         _loc1_ = 0;
         while(_loc1_ < this.var_1058.length)
         {
            if(this.var_1058[_loc1_])
            {
               if(_loc3_)
               {
                  if(_loc1_ < this.var_2266.length)
                  {
                     this.var_1071.push(this.var_2266[_loc1_]);
                  }
               }
               else
               {
                  this.var_1071.push(this.var_2578[_loc1_]);
               }
            }
            _loc1_++;
         }
         var _loc4_:Array = new Array();
         _loc1_ = 0;
         while(_loc1_ < this.var_1.var_144.length)
         {
            _loc6_ = this.var_1.var_144[_loc1_];
            if(this.method_997(_loc6_))
            {
               _loc4_.push(_loc6_);
            }
            _loc1_++;
         }
         this.var_1.mFilteredOwnedGear = _loc4_;
         this.var_1.screenArmory.var_16 = 0;
         this.var_1.screenArmory.Refresh();
      }
      
      public function method_997(param1:class_42) : Boolean
      {
         var _loc2_:uint = 0;
         var _loc8_:Object = null;
         var _loc9_:Boolean = false;
         var _loc18_:String = null;
         var _loc20_:String = null;
         var _loc21_:String = null;
         var _loc22_:String = null;
         var _loc23_:String = null;
         var _loc24_:String = null;
         var _loc25_:String = null;
         var _loc3_:Boolean = !!this.var_1369.length ? false : true;
         var _loc4_:Boolean = !!this.var_1370.length ? false : true;
         var _loc5_:Boolean = !!this.var_1636.length ? false : true;
         var _loc6_:Boolean = !!this.var_1381.length ? false : true;
         var _loc7_:Boolean = true;
         var _loc26_:int = 0;
         var _loc27_:* = this.var_180;
         for(_loc8_ in _loc27_)
         {
            _loc7_ = false;
         }
         _loc9_ = !!this.var_1503.length ? false : true;
         var _loc10_:Boolean = !!this.var_1071.length ? false : true;
         var _loc11_:GearType = param1.gearType;
         var _loc12_:class_64 = param1.var_189;
         var _loc13_:class_64 = param1.var_196;
         var _loc14_:class_64 = param1.var_187;
         var _loc15_:String = "";
         var _loc16_:String = "";
         var _loc17_:String = "";
         if(_loc12_)
         {
            _loc15_ = _loc12_.var_13.var_115;
         }
         if(_loc13_)
         {
            _loc16_ = _loc13_.var_13.var_115;
         }
         if(_loc14_)
         {
            _loc17_ = _loc14_.var_13.var_115;
         }
         _loc2_ = 0;
         while(_loc2_ < this.var_1369.length)
         {
            _loc18_ = this.var_1369[_loc2_];
            _loc20_ = _loc11_.type;
            if(_loc18_ == _loc20_)
            {
               _loc3_ = true;
               break;
            }
            _loc2_++;
         }
         _loc2_ = 0;
         while(_loc2_ < this.var_1370.length)
         {
            _loc18_ = this.var_1370[_loc2_];
            if((_loc21_ = _loc11_.var_8) == _loc18_)
            {
               _loc4_ = true;
               break;
            }
            _loc2_++;
         }
         _loc2_ = 0;
         while(_loc2_ < this.var_1636.length)
         {
            _loc18_ = this.var_1636[_loc2_];
            _loc22_ = _loc11_.var_2258;
            if(_loc18_ == _loc22_)
            {
               _loc5_ = true;
               break;
            }
            _loc2_++;
         }
         _loc2_ = 0;
         while(_loc2_ < this.var_1381.length)
         {
            if((_loc18_ = this.var_1381[_loc2_]) == _loc15_ || _loc18_ == _loc16_ || _loc18_ == _loc17_)
            {
               _loc6_ = true;
               break;
            }
            _loc2_++;
         }
         var _loc19_:String = _loc11_.var_1197;
         if(this.var_180[_loc19_])
         {
            _loc7_ = true;
         }
         _loc2_ = 0;
         while(_loc2_ < this.var_1503.length)
         {
            _loc18_ = this.var_1503[_loc2_];
            _loc23_ = _loc11_.var_1062;
            if(_loc18_ == _loc23_)
            {
               _loc9_ = true;
               break;
            }
            _loc2_++;
         }
         _loc2_ = 0;
         while(_loc2_ < this.var_1071.length)
         {
            _loc18_ = this.var_1071[_loc2_];
            _loc24_ = _loc11_.var_100;
            _loc25_ = _loc11_.procRune2;
            if(_loc18_ == _loc24_ || _loc18_ == _loc25_)
            {
               _loc10_ = true;
               break;
            }
            _loc2_++;
         }
         return _loc3_ && _loc4_ && _loc5_ && _loc6_ && _loc7_ && _loc9_ && _loc10_;
      }
      
      public function method_1244() : Dictionary
      {
         var _loc4_:String = null;
         var _loc5_:String = null;
         var _loc6_:String = null;
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         while(_loc2_ < this.var_244.length)
         {
            if(this.var_244[_loc2_])
            {
               _loc1_ |= 1 << _loc2_;
            }
            _loc2_++;
         }
         var _loc3_:Dictionary = new Dictionary();
         if(_loc1_ >> EntType.ARMOR_SLOT & 1)
         {
            for each(_loc5_ in this.var_1964)
            {
               _loc3_[_loc5_] = true;
            }
            _loc3_[this.var_2310] = true;
            _loc3_[this.var_2244] = true;
            _loc3_[this.var_2213] = true;
            _loc3_[this.var_2143] = true;
         }
         if(_loc1_ >> EntType.GLOVES_SLOT & 1)
         {
            for each(_loc4_ in this.var_1887)
            {
               _loc3_[_loc4_] = true;
            }
            _loc3_[this.var_2244] = true;
            _loc3_[this.var_2068] = true;
            _loc3_[this.var_2143] = true;
         }
         if(_loc1_ >> EntType.BOOTS_SLOT & 1)
         {
            for each(_loc5_ in this.var_1964)
            {
               _loc3_[_loc5_] = true;
            }
            _loc3_[this.var_2310] = true;
            _loc3_[this.var_2213] = true;
            _loc3_[this.var_2143] = true;
            _loc3_[this.var_2084] = true;
         }
         if(_loc1_ >> EntType.HAT_SLOT & 1)
         {
            for each(_loc5_ in this.var_1964)
            {
               _loc3_[_loc5_] = true;
            }
            for each(_loc4_ in this.var_1887)
            {
               _loc3_[_loc4_] = true;
            }
            _loc3_[this.var_2310] = true;
            _loc3_[this.var_2068] = true;
            _loc3_[this.var_2213] = true;
            _loc3_[this.var_2084] = true;
         }
         if(_loc1_ >> EntType.SWORD_SLOT & 1)
         {
            for each(_loc6_ in this.var_2837)
            {
               _loc3_[_loc6_] = true;
            }
         }
         if(_loc1_ >> EntType.SHIELD_SLOT & 1)
         {
            for each(_loc4_ in this.var_1887)
            {
               _loc3_[_loc4_] = true;
            }
            _loc3_[this.var_2244] = true;
            _loc3_[this.var_2068] = true;
            _loc3_[this.var_2084] = true;
         }
         return _loc3_;
      }
   }
}
