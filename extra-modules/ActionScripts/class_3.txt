package
{
   import flash.utils.Dictionary;
   
   public class class_3
   {
      
      private static var var_46:uint = 1;
      
      internal static var var_1415:uint = var_46++;
      
      internal static var var_2082:uint = var_46++;
      
      internal static var var_1374:uint = var_46++;
      
      internal static var var_1462:uint = var_46++;
      
      internal static var var_715:uint = var_46++;
      
      internal static var var_2559:uint = var_46++;
      
      internal static var var_2868:uint = var_46++;
      
      internal static var var_2564:uint = var_46++;
      
      internal static var var_1959:uint = var_46++;
      
      internal static var var_1829:uint = var_46++;
      
      internal static var var_2021:uint = var_46++;
      
      internal static var var_2488:uint = var_46++;
      
      internal static var var_2711:uint = var_46++;
      
      public static var var_1127:Dictionary = new Dictionary();
      
      public static var var_477:Dictionary = new Dictionary();
      
      internal static const const_133:uint = 5000;
      
      internal static const const_1322:Array = new Array(0,0,10,100,200,400);
      
      public static const const_69:uint = 5;
      
      {
         var_1127["ResPotion"] = "Potion";
         var_1127["ForgeXP"] = "Forge Boost";
         var_1127["PetFood"] = "Pet Food";
         var_477["Potion"] = "Usage: Click to equip this potion";
         var_477["Potion_Unequip"] = "Usage: Click to unequip this potion";
         var_477["Potion_Queue"] = "Usage: Click to queue this potion to be used next";
         var_477["PetFood"] = "Usage: Click to feed this food to your active pet";
         var_477["PetFood_NoPet"] = "Usage: Equip an active pet, then click this to feed it";
         var_477["Catalyst"] = "Usage: Use to craft power charms at your Magic Forge";
         var_477["ForgeXP"] = "Usage: Use at your Magic Forge";
         var_477["ResPotion"] = "Usage: Use at time of death";
      }
      
      internal var consumableID:uint;
      
      internal var var_1950:String;
      
      internal var displayName:String;
      
      internal var iconName:String;
      
      internal var var_1831:Number = 0;
      
      internal var var_1711:Number = 0;
      
      internal var var_2720:uint;
      
      internal var var_2646:Number = 0;
      
      internal var var_2762:Number = 0;
      
      internal var var_2719:Number = 0;
      
      internal var var_2666:Number = 0;
      
      internal var var_8:String;
      
      internal var var_2821:uint;
      
      internal var description:String;
      
      internal var type:String;
      
      internal var var_427:Boolean = false;
      
      internal var var_821:Boolean = false;
      
      public function class_3()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_419,class_14.var_303);
      }
      
      public static function method_773(param1:XML) : class_3
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc2_:class_3 = new class_3();
         _loc2_.var_1950 = param1.attribute("ConsumableName");
         for each(_loc3_ in param1.*)
         {
            if((_loc4_ = String(_loc3_.name().toString())) == "ConsumableID")
            {
               _loc2_.consumableID = uint(_loc3_);
            }
            else if(_loc4_ == "DisplayName")
            {
               _loc2_.displayName = _loc3_.toString();
            }
            else if(_loc4_ == "IconName")
            {
               _loc2_.iconName = _loc3_.toString();
            }
            else if(_loc4_ == "RareBoost")
            {
               _loc2_.var_1831 = Number(_loc3_);
            }
            else if(_loc4_ == "LegendaryBoost")
            {
               _loc2_.var_1711 = Number(_loc3_);
            }
            else if(_loc4_ == "ArtisanXP")
            {
               _loc2_.var_2720 = uint(_loc3_);
            }
            else if(_loc4_ == "GearFind")
            {
               _loc2_.var_2646 = Number(_loc3_);
            }
            else if(_loc4_ == "GoldFind")
            {
               _loc2_.var_2762 = Number(_loc3_);
            }
            else if(_loc4_ == "MaterialFind")
            {
               _loc2_.var_2719 = Number(_loc3_);
            }
            else if(_loc4_ == "Magnitude")
            {
               _loc2_.var_2821 = uint(_loc3_);
            }
            else if(_loc4_ == "XP")
            {
               _loc2_.var_2666 = Number(_loc3_);
            }
            else if(_loc4_ == "Description")
            {
               _loc2_.description = _loc3_.toString();
            }
            else if(_loc4_ == "Type")
            {
               _loc2_.type = _loc3_.toString();
            }
            else if(_loc4_ == "Rarity")
            {
               _loc2_.var_8 = _loc3_.toString();
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc2_.var_1950 + ": " + _loc4_);
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary) : void
      {
         var _loc4_:XML = null;
         var _loc5_:class_3 = null;
         for each(_loc4_ in param1.*)
         {
            if((_loc5_ = method_773(_loc4_)).consumableID)
            {
               if(_loc5_.consumableID >= Math.pow(2,const_69))
               {
                  class_24.method_7("CONSUMABLETYPE BitsToSend limit reached, increment bits needed: " + _loc5_.consumableID);
               }
               param2[_loc5_.consumableID] = _loc5_;
               param3[_loc5_.var_1950] = _loc5_;
               if(_loc5_.type == "Potion")
               {
                  _loc5_.var_427 = true;
               }
               if(_loc5_.type == "PetFood")
               {
                  _loc5_.var_821 = true;
               }
            }
         }
      }
      
      public static function method_2010(param1:uint) : Boolean
      {
         return param1 == var_1829 || param1 == var_2021;
      }
      
      public function method_73() : String
      {
         var _loc1_:String = String(var_1127[this.type]);
         return !!_loc1_ ? _loc1_ : this.type;
      }
   }
}
