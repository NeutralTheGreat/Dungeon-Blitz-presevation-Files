package
{
   import flash.display.MovieClip;
   import flash.utils.Dictionary;
   
   public class class_18
   {
      
      private static var var_1913:MovieClip;
      
      private static var var_1809:MovieClip;
      
      public static var var_1686:Dictionary = new Dictionary();
      
      public static const const_291:String = "Mount";
      
      public static const const_411:String = "Pet";
      
      public static const const_171:String = "Egg";
      
      public static const const_322:String = "Consumable";
      
      public static const const_190:String = "Gear";
      
      public static const const_1351:String = "Rewardpack";
      
      public static const const_384:String = "Gold";
      
      public static const const_374:String = "Charm";
      
      public static const const_333:String = "Dye";
      
      public static var var_1319:Dictionary = new Dictionary();
      
      public static var var_1174:Dictionary = new Dictionary();
      
      public static var var_676:Array = new Array();
      
      public static const const_1159:uint = 100;
      
      public static const const_1245:Array = new Array(21,22,22,23,23,23,24,24,24,24,25,25,25,25,25,26,26,26,26,26,27,27,27,27,27,27,28,28,28,28,28,28,28,29,29,29,29,29,29,29,29,30,30,30,30,30,30,30,30,30,31,31,31,31,31,31,31,31,32,32,32,32,32,32,32,34,34,34,34,34,34,36,36,36,36,36,38,38,38,38,38,40,40,40,40,40,42,42,42,42,42,44,44,44,44,46,46,46,48,50);
      
      public static var var_1846:uint = 3;
      
      public static var var_1776:uint = 6;
      
      private static const const_730:Array = new Array("Mage","Paladin","Rogue");
      
      private static const name_1:Array = new Array("","Armor","Gloves","Boots","Hat","Sword","Shield");
       
      
      internal var var_1:Game;
      
      internal var var_673:String;
      
      internal var var_459:uint;
      
      internal var var_162:String;
      
      internal var value:uint;
      
      internal var var_86:String;
      
      internal var var_2946:String;
      
      internal var var_8:String;
      
      internal var cumulativeChance:Number = 0;
      
      internal var position:uint;
      
      public function class_18()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_2297,class_14.var_1856);
      }
      
      public static function method_855(param1:XML, param2:class_18) : class_18
      {
         var _loc5_:Boolean = false;
         var _loc6_:XML = null;
         var _loc7_:String = null;
         var _loc3_:class_18 = new class_18();
         _loc3_.var_673 = param1.attribute("RewardpackName");
         var _loc4_:* = _loc3_.var_673 != "";
         for each(_loc6_ in param1.*)
         {
            if((_loc7_ = String(_loc6_.name().toString())) == "RewardpackID")
            {
               _loc3_.var_459 = uint(_loc6_);
               _loc5_ = true;
            }
            else if(_loc7_ == "RewardItem")
            {
               _loc3_.var_162 = _loc6_.toString();
            }
            else if(_loc7_ == "Value")
            {
               _loc3_.value = uint(_loc6_);
            }
            else if(_loc7_ == "RewardType")
            {
               _loc3_.var_86 = _loc6_.toString();
            }
            else if(_loc7_ == "AlternateRewardpack")
            {
               _loc3_.var_2946 = _loc6_.toString();
            }
            else if(_loc7_ == "Rarity")
            {
               _loc3_.var_8 = _loc6_.toString();
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc3_.var_673 + ": " + _loc7_);
            }
         }
         if(!_loc5_)
         {
            _loc3_.var_459 = param2.var_459;
         }
         if(!_loc4_)
         {
            _loc3_.var_673 = param2.var_673;
         }
         return _loc3_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary) : void
      {
         var _loc4_:class_18 = null;
         var _loc5_:class_18 = null;
         var _loc11_:XML = null;
         var_1174 = new Dictionary();
         var_676 = new Array();
         var _loc6_:uint = 0;
         var _loc7_:Vector.<class_18> = new Vector.<class_18>();
         var _loc8_:Vector.<class_18> = new Vector.<class_18>();
         var _loc10_:uint = 0;
         for each(_loc11_ in param1.*)
         {
            _loc4_ = method_855(_loc11_,_loc5_);
            if(Boolean(_loc5_) && _loc4_.var_459 != _loc5_.var_459)
            {
               var_1686[_loc4_.var_673] = 0;
               _loc6_ = 0;
            }
            else
            {
               _loc6_++;
            }
            _loc4_.position = _loc6_;
            _loc4_.cumulativeChance = 0;
            param2[_loc4_.var_459] = _loc4_;
            param3[_loc4_.var_673] = _loc4_;
            _loc8_ = var_676[_loc4_.var_459];
            _loc7_ = var_1174[_loc4_.var_673];
            if(!_loc8_)
            {
               _loc8_ = new Vector.<class_18>();
               var_1174[_loc4_.var_673] = _loc8_;
            }
            if(!_loc7_)
            {
               _loc7_ = new Vector.<class_18>();
               var_676[_loc4_.var_459] = _loc7_;
            }
            _loc8_.push(_loc4_);
            _loc7_.push(_loc4_);
            _loc10_ = _loc8_.length > _loc10_ ? _loc8_.length : _loc10_;
            _loc5_ = _loc4_;
            if(_loc4_.var_459 >= Math.pow(2,var_1846))
            {
               class_24.method_7("REWARDPACK_BITSTOSEND BitsToSend limit reached, increment bits needed: " + _loc4_.var_459);
            }
            if(_loc10_ >= Math.pow(2,var_1776))
            {
               class_24.method_7("REWARDPACKPOSITION BitsToSend limit reached, increment bits needed: " + _loc10_);
            }
         }
      }
      
      public static function method_2092(param1:String) : class_18
      {
         var _loc2_:class_18 = class_14.var_1856[param1];
         if(!_loc2_)
         {
            return null;
         }
         var _loc3_:uint = _loc2_.var_459;
         var _loc4_:Number = Number(var_1686[param1]);
         var _loc5_:Number = Math.random() * _loc4_;
         var _loc6_:Vector.<class_18> = var_676[_loc3_];
         var _loc7_:Number = 0;
         var _loc8_:uint = 0;
         while(_loc5_ > _loc7_ && _loc8_ < _loc6_.length)
         {
            _loc7_ = _loc6_[_loc8_].cumulativeChance;
            _loc8_++;
         }
         return _loc6_[_loc8_ - 1];
      }
      
      public static function method_1084(param1:uint, param2:uint) : class_18
      {
         return var_676[param1][param2];
      }
      
      public static function Init() : void
      {
         var _loc1_:Vector.<class_18> = null;
         var _loc2_:uint = 0;
         var _loc3_:class_18 = null;
         for each(_loc1_ in class_18.var_676)
         {
            _loc2_ = 0;
            while(_loc2_ < _loc1_.length)
            {
               _loc3_ = _loc1_[_loc2_];
               if(_loc3_.var_86 == class_18.const_190)
               {
                  class_18.method_1567(_loc3_.var_162);
               }
               _loc2_++;
            }
         }
      }
      
      public static function method_1567(param1:String) : void
      {
         var _loc2_:GearType = null;
         var _loc4_:String = null;
         var _loc5_:String = null;
         var _loc6_:uint = 0;
         var _loc7_:String = null;
         var _loc8_:* = null;
         var _loc3_:uint = 0;
         while(_loc3_ < const_730.length)
         {
            _loc4_ = String(const_730[_loc3_]);
            _loc5_ = param1 + _loc4_;
            var_1319[_loc5_] = new Vector.<GearType>();
            _loc6_ = 1;
            while(_loc6_ < name_1.length)
            {
               _loc7_ = String(name_1[_loc6_]);
               _loc8_ = "Unique" + _loc4_ + param1 + _loc7_ + "30L";
               _loc2_ = class_14.gearTypesDict[_loc8_];
               if(!_loc2_)
               {
                  class_24.method_7("Gear Builder for rewardpacks bad");
               }
               var_1319[_loc5_].push(_loc2_);
               _loc6_++;
            }
            _loc3_++;
         }
      }
      
      public static function method_2080(param1:String, param2:String) : Vector.<GearType>
      {
         var _loc3_:String = param1 + param2;
         return var_1319[_loc3_];
      }
      
      public static function method_2108() : uint
      {
         var _loc1_:uint = Math.floor(Math.random() * const_1159);
         return uint(const_1245[_loc1_]);
      }
      
      public function method_839(param1:String, param2:String) : String
      {
         var _loc3_:class_7 = null;
         var _loc5_:class_21 = null;
         var _loc6_:GearType = null;
         var _loc7_:class_20 = null;
         var _loc8_:class_1 = null;
         var _loc9_:class_3 = null;
         var _loc4_:String = this.var_162;
         if(param2)
         {
            if(this.var_86 == const_171)
            {
               _loc3_ = class_14.var_233[param2];
               if(_loc3_)
               {
                  _loc4_ = _loc3_.displayName;
               }
            }
            if(this.var_86 == const_333)
            {
               if(_loc5_ = class_14.var_1194[param2])
               {
                  _loc4_ = _loc5_.displayName;
               }
            }
            if(this.var_86 == const_190)
            {
               if(_loc6_ = class_14.gearTypesDict[param2])
               {
                  _loc4_ = _loc6_.displayName;
               }
            }
         }
         if(this.var_86 == const_384)
         {
            _loc4_ = MathUtil.method_29(this.value) + " " + _loc4_;
         }
         if(this.var_86 == const_291)
         {
            _loc4_ = (_loc7_ = class_14.var_362[this.var_162]).displayName;
         }
         if(this.var_86 == const_411)
         {
            _loc3_ = class_14.var_233[this.var_162];
            _loc4_ = _loc3_.displayName;
         }
         if(this.var_86 == const_374)
         {
            _loc4_ = (_loc8_ = class_14.var_142[this.var_162]).displayName;
         }
         if(this.var_86 == const_322)
         {
            _loc4_ = (_loc9_ = class_14.var_303[this.var_162]).displayName;
         }
         return _loc4_;
      }
      
      public function method_996(param1:Game, param2:class_32, param3:MovieClip, param4:String) : void
      {
         var _loc5_:class_3 = null;
         var _loc6_:class_21 = null;
         var _loc7_:MovieClip = null;
         var _loc8_:class_1 = null;
         var _loc9_:MovieClip = null;
         var _loc10_:class_7 = null;
         var _loc11_:class_7 = null;
         var _loc12_:GearType = null;
         var _loc13_:SuperAnimInstance = null;
         var _loc14_:class_20 = null;
         if(this.var_86 == const_384)
         {
            if(this.value <= 150000)
            {
               param2.method_12(param3,"a_RewardTypeIcon_GoldSmall");
            }
            else if(this.value <= 500000)
            {
               param2.method_12(param3,"a_RewardTypeIcon_GoldMedium");
            }
            else if(this.value <= 1250000)
            {
               param2.method_12(param3,"a_RewardTypeIcon_GoldLarge");
            }
            else
            {
               param2.method_12(param3,"a_RewardTypeIcon_GoldJackpot");
            }
            return;
         }
         if(this.var_86 == const_322)
         {
            _loc5_ = class_14.var_303[this.var_162];
            param2.method_12(param3,_loc5_.iconName);
            return;
         }
         if(this.var_86 == const_333)
         {
            if(!var_1913 || !var_1809)
            {
               var_1913 = class_4.method_16("a_RewardTypeIcon_DyeSmall");
               var_1809 = class_4.method_16("a_RewardTypeIcon_DyeLarge");
            }
            _loc6_ = class_14.var_1194[param4];
            param2.method_14(param3);
            _loc7_ = _loc6_.var_8 == "L" ? var_1809 : var_1913;
            param1.screenHudTooltip.SkinDyeIcon(_loc6_,_loc7_.am_DyeSwap);
            param3.addChild(_loc7_);
            return;
         }
         if(this.var_86 == const_374)
         {
            _loc8_ = class_14.var_142[this.var_162];
            param2.method_12(param3,_loc8_.iconName);
            (_loc9_ = param3.getChildAt(0) as MovieClip).gotoAndStop(1);
            _loc9_.am_SecondaryCharm.visible = false;
            return;
         }
         if(this.var_86 == const_171)
         {
            _loc10_ = class_14.var_233[param4];
            param2.method_14(param3);
            param3.addChild(class_41.method_85(_loc10_,0,0,58,58,param1.main.overallScale));
            return;
         }
         if(this.var_86 == const_411)
         {
            _loc11_ = class_14.var_233[this.var_162];
            param2.method_14(param3);
            param3.addChild(class_41.method_85(_loc11_,0,0,58,58,param1.main.overallScale));
            return;
         }
         if(this.var_86 == const_190)
         {
            _loc12_ = class_14.gearTypesDict[param4];
            (_loc13_ = param1.RenderGear(Game.const_95,_loc12_,0.5)).m_TheDO.x = 22;
            _loc13_.m_TheDO.y = 44;
            param2.method_52(param3,_loc13_);
            return;
         }
         if(this.var_86 == const_291)
         {
            _loc14_ = class_14.var_362[this.var_162];
            param2.method_14(param3);
            param3.addChild(class_41.method_168(_loc14_,0,0,58,58,param1.main.overallScale));
            return;
         }
      }
      
      public function method_734() : String
      {
         var _loc2_:class_3 = null;
         var _loc1_:String = this.var_86;
         if(this.var_86 == const_171)
         {
            _loc1_ = this.var_8 == "L" ? "Pet" : "Pet (Level 10)";
         }
         else if(this.var_86 == const_322)
         {
            _loc2_ = class_14.var_303[this.var_162];
            _loc1_ = !!_loc2_ ? _loc2_.method_73() : "UNKNOWN";
         }
         return _loc1_;
      }
   }
}
