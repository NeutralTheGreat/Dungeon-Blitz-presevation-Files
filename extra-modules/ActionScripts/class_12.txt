package
{
   import flash.utils.Dictionary;
   
   public class class_12
   {
      
      public static const const_279:String = "Mount";
      
      public static const include:String = "Pet";
      
      public static const const_1407:String = "MaterialPack";
      
      public static const const_1354:String = "RespecStone";
      
      public static const const_205:String = "Consumable";
      
      public static const const_1363:String = "CharmRemover";
      
      public static const const_753:uint = 5;
       
      
      internal var var_865:uint;
      
      internal var var_257:String;
      
      internal var displayName:String;
      
      internal var iconName:String;
      
      internal var var_2882:uint;
      
      internal var var_2240:uint;
      
      internal var var_129:uint;
      
      internal var description:String;
      
      internal var var_1014:String;
      
      internal var type:String;
      
      internal var var_2505:Boolean;
      
      internal var var_1579:Boolean;
      
      internal var var_795:uint;
      
      public function class_12()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_1626,class_14.var_2027);
      }
      
      public static function method_619(param1:XML) : class_12
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc2_:class_12 = new class_12();
         _loc2_.var_257 = param1.attribute("RoyalStoreName");
         for each(_loc3_ in param1.*)
         {
            if((_loc4_ = String(_loc3_.name().toString())) == "RoyalStoreID")
            {
               _loc2_.var_865 = uint(_loc3_);
            }
            else if(_loc4_ == "DisplayName")
            {
               _loc2_.displayName = _loc3_.toString();
            }
            else if(_loc4_ == "IconName")
            {
               _loc2_.iconName = _loc3_.toString();
            }
            else if(_loc4_ == "Quantity")
            {
               _loc2_.var_2882 = uint(_loc3_);
            }
            else if(_loc4_ == "SigilCost")
            {
               _loc2_.var_2240 = uint(_loc3_);
            }
            else if(_loc4_ == "GoldCost")
            {
               _loc2_.var_129 = uint(_loc3_);
            }
            else if(_loc4_ == "Description")
            {
               _loc2_.description = _loc3_.toString();
            }
            else if(_loc4_ == "Category")
            {
               _loc2_.var_1014 = _loc3_.toString();
            }
            else if(_loc4_ == "Type")
            {
               _loc2_.type = _loc3_.toString();
            }
            else if(_loc4_ == "DisallowDupes")
            {
               _loc2_.var_2505 = MathUtil.method_50(_loc3_.toString());
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc2_.var_257 + ": " + _loc4_);
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary) : void
      {
         var _loc4_:XML = null;
         var _loc5_:class_12 = null;
         for each(_loc4_ in param1.*)
         {
            if((_loc5_ = method_619(_loc4_)).var_865)
            {
               if(_loc5_.var_865 >= Math.pow(2,const_753))
               {
                  class_24.method_7("RoyalStoreType BitsToSend limit reached, increment bits needed: " + _loc5_.var_865);
               }
               if(Boolean(_loc5_.var_129) && Boolean(_loc5_.var_2240))
               {
                  class_24.method_7("Items aren\'t allowed to have a gold cost and a sigil cost: " + _loc5_.var_865);
               }
               if(_loc5_.var_129)
               {
                  _loc5_.var_1579 = true;
                  _loc5_.var_795 = _loc5_.var_129;
               }
               else
               {
                  _loc5_.var_795 = _loc5_.var_2240;
               }
               if(_loc5_.var_1014 != "Special" && _loc5_.var_1014 != "Potions")
               {
                  class_24.method_7("Category must be Special or Potions: " + _loc5_.var_865);
               }
               param2[_loc5_.var_865] = _loc5_;
               param3[_loc5_.var_257] = _loc5_;
            }
         }
      }
   }
}
