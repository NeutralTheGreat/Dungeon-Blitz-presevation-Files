package
{
   import flash.utils.Dictionary;
   
   public class class_1
   {
      
      public static const const_254:uint = 7;
      
      public static const const_765:uint = 2;
      
      public static const const_405:uint = 91;
      
      public static const const_1193:uint = 92;
      
      public static const DOUBLEFIND1_CHARMID:uint = 93;
      
      public static const DOUBLEFIND2_CHARMID:uint = 94;
      
      public static const DOUBLEFIND3_CHARMID:uint = 95;
      
      public static const const_459:uint = 96;
       
      
      internal var var_68:uint;
      
      internal var var_693:String;
      
      internal var displayName:String;
      
      internal var iconName:String;
      
      internal var var_203:String;
      
      internal var var_2208:uint;
      
      internal var var_2947:String;
      
      internal var var_930:uint;
      
      internal var var_115:String;
      
      internal var var_2938:uint;
      
      internal var var_79:Number = 0;
      
      internal var itemDrop:Number = 0;
      
      internal var var_152:Number = 0;
      
      internal var var_2402:Number = 0;
      
      internal var var_2118:Number = 0;
      
      internal var var_1593:uint;
      
      internal var var_2429:uint;
      
      internal var var_2040:uint;
      
      internal var var_2033:uint;
      
      internal var var_2570:Boolean;
      
      internal var var_2441:Boolean;
      
      internal var var_2736:Boolean;
      
      internal var var_1327:String;
      
      internal var var_1397:String;
      
      internal var var_1617:String;
      
      internal var var_1321:String;
      
      internal var var_1560:String;
      
      internal var var_1510:String;
      
      internal var var_1339:String;
      
      internal var var_1513:String;
      
      internal var var_1482:String;
      
      internal var var_1353:String;
      
      public function class_1()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_767,class_14.var_142);
      }
      
      public static function method_965(param1:XML) : class_1
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc2_:class_1 = new class_1();
         _loc2_.var_693 = param1.attribute("CharmName");
         for each(_loc3_ in param1.*)
         {
            if((_loc4_ = String(_loc3_.name().toString())) == "CharmID")
            {
               _loc2_.var_68 = uint(_loc3_);
            }
            else if(_loc4_ == "DisplayName")
            {
               _loc2_.displayName = _loc3_.toString();
            }
            else if(_loc4_ == "IconName")
            {
               _loc2_.iconName = _loc3_.toString();
            }
            else if(_loc4_ == "Description")
            {
               _loc2_.var_203 = _loc3_.toString();
            }
            else if(_loc4_ == "CharmLevel")
            {
               _loc2_.var_2208 = uint(_loc3_);
            }
            else if(_loc4_ == "UpgradeCharm")
            {
               _loc2_.var_2947 = _loc3_.toString();
            }
            else if(_loc4_ == "PrimaryType")
            {
               _loc2_.var_115 = _loc3_.toString();
            }
            else if(_loc4_ == "PrimaryCost")
            {
               _loc2_.var_2938 = uint(_loc3_);
            }
            else if(_loc4_ == "CharmSize")
            {
               _loc2_.var_930 = uint(_loc3_);
            }
            else if(_loc4_ == "GoldDrop")
            {
               _loc2_.var_79 = Number(_loc3_);
            }
            else if(_loc4_ == "ItemDrop")
            {
               _loc2_.itemDrop = Number(_loc3_);
            }
            else if(_loc4_ == "CraftDrop")
            {
               _loc2_.var_152 = Number(_loc3_);
            }
            else if(_loc4_ == "PowerBonus")
            {
               _loc2_.var_2402 = Number(_loc3_);
            }
            else if(_loc4_ == "ProcChanceUp")
            {
               _loc2_.var_2118 = Number(_loc3_);
            }
            else if(_loc4_ == "HitPointBoost")
            {
               _loc2_.var_1593 = uint(_loc3_);
            }
            else if(_loc4_ == "MeleeBonus")
            {
               _loc2_.var_2429 = uint(_loc3_);
            }
            else if(_loc4_ == "MagicBonus")
            {
               _loc2_.var_2040 = uint(_loc3_);
            }
            else if(_loc4_ == "ArmorBonus")
            {
               _loc2_.var_2033 = uint(_loc3_);
            }
            else if(_loc4_ == "DisallowCrafting")
            {
               _loc2_.var_2736 = MathUtil.method_50(_loc3_);
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc2_.var_693 + ": " + _loc4_);
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary) : void
      {
         var _loc4_:XML = null;
         var _loc5_:class_1 = null;
         var _loc6_:Array = null;
         var _loc7_:Array = null;
         for each(_loc4_ in param1.*)
         {
            if((_loc5_ = method_965(_loc4_)).var_68)
            {
               if(param2[_loc5_.var_68])
               {
                  class_24.method_7("Multiple charms with ID: " + _loc5_.var_68);
               }
               if(param3[_loc5_.var_693])
               {
                  class_24.method_7("Multiple charms with name: " + _loc5_.var_693);
               }
               if(_loc5_.var_68 >= Math.pow(2,const_254))
               {
                  class_24.method_7("Charm bits to send limit reached, increment bits needed: " + _loc5_.var_68);
               }
               if(_loc5_.var_68 > Game.const_175)
               {
                  class_24.method_7("Database assumes all IDs will be less <= " + Game.const_175 + ", Contact Programmer: " + _loc5_.var_68);
               }
               param2[_loc5_.var_68] = _loc5_;
               param3[_loc5_.var_693] = _loc5_;
               if(_loc5_.var_68 == class_1.const_1193 || !_loc5_.var_693.indexOf("Triple"))
               {
                  _loc5_.var_2570 = true;
               }
               if(_loc5_.var_68 == class_1.DOUBLEFIND1_CHARMID || _loc5_.var_68 == class_1.DOUBLEFIND2_CHARMID || _loc5_.var_68 == class_1.DOUBLEFIND3_CHARMID || !_loc5_.var_693.indexOf("Double"))
               {
                  _loc5_.var_2441 = true;
               }
               if(method_118(_loc5_))
               {
                  if((_loc6_ = _loc5_.var_203.split(";")).length != 3)
                  {
                     class_24.method_7("Triple Charm needs 3 things in description field. Delimited by \';\'. " + _loc5_.var_68);
                  }
                  if((_loc7_ = _loc5_.var_115.split(";")).length != 3)
                  {
                     class_24.method_7("Triple Charm needs 3 things in Primary Type field. Delimited by \';\'. " + _loc5_.var_68);
                  }
                  _loc5_.var_1327 = _loc6_[0];
                  _loc5_.var_1397 = _loc6_[1];
                  _loc5_.var_1617 = _loc6_[2];
                  _loc5_.var_1321 = _loc7_[0];
                  _loc5_.var_1560 = _loc7_[1];
                  _loc5_.var_1510 = _loc7_[2];
               }
               if(method_124(_loc5_))
               {
                  if((_loc6_ = _loc5_.var_203.split(";")).length != 2)
                  {
                     class_24.method_7("Double Charm needs 2 things in description field. Delimited by \';\'. " + _loc5_.var_68);
                  }
                  if((_loc7_ = _loc5_.var_115.split(";")).length != 2)
                  {
                     class_24.method_7("Double Charm needs 2 things in Primary Type field. Delimited by \';\'. " + _loc5_.var_68);
                  }
                  _loc5_.var_1339 = _loc6_[0];
                  _loc5_.var_1513 = _loc6_[1];
                  _loc5_.var_1482 = _loc7_[0];
                  _loc5_.var_1353 = _loc7_[1];
               }
            }
         }
      }
      
      public static function method_118(param1:class_1) : Boolean
      {
         return param1.var_2570;
      }
      
      public static function method_124(param1:class_1) : Boolean
      {
         return param1.var_2441;
      }
   }
}
