package
{
   import flash.utils.Dictionary;
   
   public class class_9
   {
      
      public static const const_851:uint = 2;
      
      public static const const_129:uint = 5;
      
      public static const const_28:uint = 5;
      
      public static const const_1334:uint = 2;
      
      public static const const_214:uint = 10;
      
      public static const const_1404:uint = 0;
      
      public static const const_1390:uint = 1;
      
      public static var var_1357:Vector.<uint> = new Vector.<uint>();
      
      public static var var_1616:Vector.<uint> = new Vector.<uint>();
      
      public static var var_1618:Vector.<uint> = new Vector.<uint>();
       
      
      internal var var_242:String;
      
      internal var var_208:uint;
      
      internal var displayName:String;
      
      internal var var_2934:uint;
      
      internal var rank:uint;
      
      internal var var_129:uint;
      
      internal var var_365:uint;
      
      internal var upgradeTime:uint;
      
      internal var var_266:String;
      
      internal var type:String;
      
      internal var var_2301:String;
      
      internal var var_1861:String;
      
      internal var var_1499:String;
      
      public function class_9()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_278,class_14.var_1770,class_14.var_1371);
      }
      
      public static function method_928(param1:XML, param2:class_9) : class_9
      {
         var _loc7_:Boolean = false;
         var _loc8_:Boolean = false;
         var _loc9_:Boolean = false;
         var _loc10_:Boolean = false;
         var _loc11_:Boolean = false;
         var _loc12_:Boolean = false;
         var _loc13_:XML = null;
         var _loc14_:String = null;
         var _loc3_:class_9 = new class_9();
         _loc3_.var_242 = param1.attribute("BuildingName");
         var _loc6_:* = _loc3_.var_242 != "";
         for each(_loc13_ in param1.*)
         {
            if((_loc14_ = String(_loc13_.name().toString())) == "BuildingID")
            {
               _loc3_.var_208 = uint(_loc13_);
               _loc7_ = true;
            }
            else if(_loc14_ == "DisplayName")
            {
               _loc3_.displayName = _loc13_.toString();
               _loc8_ = true;
            }
            else if(_loc14_ == "Type")
            {
               _loc3_.type = _loc13_.toString();
               _loc10_ = true;
            }
            else if(_loc14_ == "Rank")
            {
               _loc3_.rank = uint(_loc13_);
            }
            else if(_loc14_ == "PlayerLevel")
            {
               _loc3_.var_2934 = uint(_loc13_);
            }
            else if(_loc14_ == "GoldCost")
            {
               _loc3_.var_129 = uint(_loc13_);
            }
            else if(_loc14_ == "IdolCost")
            {
               _loc3_.var_365 = uint(_loc13_);
            }
            else if(_loc14_ == "UpgradeTime")
            {
               _loc3_.upgradeTime = uint(_loc13_);
            }
            else if(_loc14_ == "Art")
            {
               _loc3_.var_266 = _loc13_.toString();
               _loc9_ = true;
            }
            else if(_loc14_ == "BackgroundArt")
            {
               _loc3_.var_2301 = _loc13_.toString();
               _loc11_ = true;
            }
            else if(_loc14_ == "UpgradeIcon")
            {
               _loc3_.var_1861 = _loc13_.toString();
               _loc12_ = true;
            }
            else if(_loc14_ == "UpgradeDescription")
            {
               _loc3_.var_1499 = _loc13_.toString();
            }
         }
         if(!_loc6_)
         {
            _loc3_.var_242 = param2.var_242;
         }
         if(!_loc7_)
         {
            _loc3_.var_208 = param2.var_208;
         }
         if(!_loc8_)
         {
            _loc3_.displayName = param2.displayName;
         }
         if(!_loc9_)
         {
            _loc3_.var_266 = param2.var_266;
         }
         if(!_loc10_)
         {
            _loc3_.type = param2.type;
         }
         if(!_loc11_)
         {
            _loc3_.var_2301 = param2.var_2301;
         }
         if(!_loc12_)
         {
            _loc3_.var_1861 = param2.var_1861;
         }
         return _loc3_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary, param4:Dictionary) : void
      {
         var _loc5_:class_9 = null;
         var _loc6_:class_9 = null;
         var _loc7_:XML = null;
         var _loc8_:String = null;
         for each(_loc7_ in param1.*)
         {
            _loc5_ = _loc6_ = method_928(_loc7_,_loc5_);
            if(_loc6_.var_208 >= Math.pow(2,const_129))
            {
               class_24.method_7("Building bits to send limit reached, increment bits needed: " + _loc6_.var_208);
            }
            if(_loc6_.rank >= Math.pow(2,const_28))
            {
               class_24.method_7("Building rank bits to send limit reached, increment bits needed: " + _loc6_.rank);
            }
            param2[_loc6_.var_208] = _loc6_;
            _loc8_ = _loc6_.var_242.toLowerCase();
            param3[_loc8_] = _loc6_;
            param4[_loc6_.var_242 + _loc6_.rank] = _loc6_;
            if(_loc6_.rank == 0)
            {
               if(_loc8_ == "justicartower" || _loc8_ == "sentineltower" || _loc8_ == "templartower")
               {
                  var_1616.push(_loc6_.var_208);
               }
               if(_loc8_ == "flameseertower" || _loc8_ == "frostwardentower" || _loc8_ == "necromancertower")
               {
                  var_1357.push(_loc6_.var_208);
               }
               if(_loc8_ == "soulthieftower" || _loc8_ == "shadowwalkertower" || _loc8_ == "executionertower")
               {
                  var_1618.push(_loc6_.var_208);
               }
            }
         }
      }
      
      public static function method_216(param1:uint, param2:uint) : class_9
      {
         var _loc3_:class_9 = class_14.var_278[param1];
         return !!_loc3_ ? class_14.var_1371[_loc3_.var_242 + param2] : null;
      }
      
      public static function method_94(param1:String, param2:uint) : class_9
      {
         return class_14.var_1371[param1 + param2];
      }
      
      public static function method_132(param1:class_9) : class_9
      {
         var _loc3_:class_9 = null;
         var _loc2_:uint = uint(param1.rank + 1);
         if(_loc2_ > const_214)
         {
            _loc3_ = method_216(param1.var_208,const_214);
         }
         else
         {
            _loc3_ = method_216(param1.var_208,_loc2_);
         }
         return _loc3_;
      }
      
      public static function method_2043(param1:uint) : String
      {
         var _loc2_:String = "";
         var _loc3_:class_9 = class_14.var_278[param1];
         var _loc5_:uint;
         var _loc4_:String;
         if((_loc5_ = uint((_loc4_ = _loc3_.var_242).indexOf("Tower"))) > -1)
         {
            _loc2_ = _loc4_.substr(0,_loc5_);
         }
         return _loc2_;
      }
      
      public static function method_472(param1:String) : uint
      {
         if(!param1)
         {
            return 0;
         }
         var _loc2_:class_9 = class_14.var_1770[param1.toLowerCase() + "tower"];
         return !!_loc2_ ? _loc2_.var_208 : 0;
      }
      
      public static function method_2044(param1:uint) : String
      {
         if(!param1)
         {
            return "";
         }
         var _loc2_:class_9 = class_14.var_278[param1];
         return !!_loc2_ ? _loc2_.type : "";
      }
   }
}
