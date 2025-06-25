package
{
   import flash.utils.Dictionary;
   
   public class class_10
   {
      
      public static const const_83:uint = 7;
      
      public static const const_665:uint = 4;
      
      public static const const_105:uint = 10;
       
      
      internal var abilityID:uint;
      
      internal var abilityName:String;
      
      internal var rank:uint;
      
      internal var type:String;
      
      internal var className:String;
      
      internal var var_1911:String;
      
      internal var var_90:int;
      
      internal var var_1014:String;
      
      internal var var_129:uint;
      
      internal var var_365:uint;
      
      internal var upgradeTime:uint;
      
      internal var var_2920:Dictionary;
      
      internal var var_223:Boolean = false;
      
      internal var var_2189:Boolean = false;
      
      public function class_10()
      {
         this.var_2920 = new Dictionary();
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_478,class_14.var_704,class_14.var_526,class_14.var_1101);
      }
      
      public static function method_636(param1:XML, param2:class_10) : class_10
      {
         var _loc5_:Boolean = false;
         var _loc6_:Boolean = false;
         var _loc7_:Boolean = false;
         var _loc8_:Boolean = false;
         var _loc9_:Boolean = false;
         var _loc10_:Boolean = false;
         var _loc11_:XML = null;
         var _loc12_:String = null;
         var _loc3_:class_10 = new class_10();
         _loc3_.abilityName = param1.attribute("AbilityName");
         var _loc4_:* = _loc3_.abilityName != "";
         for each(_loc11_ in param1.*)
         {
            if((_loc12_ = String(_loc11_.name().toString())) == "AbilityID")
            {
               _loc3_.abilityID = uint(_loc11_);
               _loc5_ = true;
            }
            else if(_loc12_ == "Rank")
            {
               _loc3_.rank = uint(_loc11_);
            }
            else if(_loc12_ == "BaseClass")
            {
               _loc3_.var_1911 = _loc11_.toString();
               _loc6_ = true;
            }
            else if(_loc12_ == "Class")
            {
               _loc3_.className = _loc11_.toString();
               _loc7_ = true;
            }
            else if(_loc12_ == "HotbarLocation")
            {
               _loc3_.var_90 = uint(_loc11_);
               _loc8_ = true;
            }
            else if(_loc12_ == "Category")
            {
               _loc3_.var_1014 = _loc11_.toString();
               _loc9_ = true;
            }
            else if(_loc12_ == "GoldCost")
            {
               _loc3_.var_129 = uint(_loc11_);
            }
            else if(_loc12_ == "IdolCost")
            {
               _loc3_.var_365 = uint(_loc11_);
            }
            else if(_loc12_ == "UpgradeTime")
            {
               _loc3_.upgradeTime = uint(_loc11_);
            }
            else if(_loc12_ == "Type")
            {
               _loc3_.type = _loc11_.toString();
               _loc10_ = true;
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc3_.abilityName + ": " + _loc12_);
            }
         }
         if(!_loc4_)
         {
            _loc3_.abilityName = param2.abilityName;
         }
         if(!_loc5_)
         {
            _loc3_.abilityID = param2.abilityID;
         }
         if(!_loc6_)
         {
            _loc3_.var_1911 = param2.var_1911;
         }
         if(!_loc7_)
         {
            _loc3_.className = param2.className;
         }
         if(!_loc8_)
         {
            _loc3_.var_90 = param2.var_90;
         }
         if(!_loc9_)
         {
            _loc3_.var_1014 = param2.var_1014;
         }
         if(!_loc10_)
         {
            _loc3_.type = param2.type;
         }
         if(_loc3_.var_90 == 0 || _loc3_.var_90 > 3)
         {
            _loc3_.var_223 = true;
         }
         if(_loc3_.var_90 == 0)
         {
            _loc3_.var_2189 = true;
         }
         return _loc3_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary, param4:Dictionary, param5:Dictionary) : void
      {
         var _loc6_:class_10 = null;
         var _loc7_:XML = null;
         var _loc8_:class_10 = null;
         for each(_loc7_ in param1.*)
         {
            _loc6_ = _loc8_ = method_636(_loc7_,_loc6_);
            if(_loc8_.abilityID)
            {
               if(_loc8_.abilityID >= Math.pow(2,const_83))
               {
                  class_24.method_7("Ability BitsToSend limit reached, increment bits needed: " + _loc8_.abilityID);
               }
               param2[_loc8_.abilityID] = _loc8_;
               param3[_loc8_.abilityName] = _loc8_;
               param4[_loc8_.className.toLowerCase() + _loc8_.var_90] = _loc8_;
               param5[_loc8_.abilityName + _loc8_.rank] = _loc8_;
            }
         }
      }
      
      public static function method_352(param1:String, param2:uint) : class_10
      {
         var _loc3_:String = param1 + String(param2);
         return class_14.var_1101[_loc3_];
      }
      
      public static function method_591(param1:uint, param2:uint) : class_10
      {
         var _loc5_:class_10 = null;
         var _loc3_:class_10 = null;
         var _loc4_:class_10;
         if(_loc4_ = class_14.var_478[param1])
         {
            if(_loc5_ = method_352(_loc4_.abilityName,param2))
            {
               _loc3_ = _loc5_;
            }
         }
         return _loc3_;
      }
      
      public static function method_1363(param1:class_10, param2:class_10) : Number
      {
         return method_331(param1) - method_331(param2);
      }
      
      public static function method_331(param1:class_10) : Number
      {
         if(param1.var_90 >= 4)
         {
            return 1000000 + param1.abilityID;
         }
         var _loc2_:Number = 100000 * param1.var_90;
         var _loc3_:String = param1.abilityName;
         if(_loc3_ == "ReduceArmor" || _loc3_ == "GroupHoT" || _loc3_ == "IceStorm")
         {
            _loc2_ -= 5000;
         }
         return _loc2_;
      }
   }
}
