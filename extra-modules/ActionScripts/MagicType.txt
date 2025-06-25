package
{
   import flash.utils.Dictionary;
   
   public class MagicType
   {
       
      
      internal var magicID:uint;
      
      internal var magicName:String;
      
      internal var displayName:String;
      
      internal var description:String;
      
      internal var runeIcon:String;
      
      internal var var_1218:class_134;
      
      public function MagicType()
      {
         this.var_1218 = new class_134();
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.magicTypes,class_14.magicTypesDict);
      }
      
      public static function method_743(param1:XML) : MagicType
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc2_:MagicType = new MagicType();
         _loc2_.magicName = param1.attribute("MagicName").toString();
         for each(_loc3_ in param1.*)
         {
            if((_loc4_ = String(_loc3_.name().toString())) == "MagicID")
            {
               _loc2_.magicID = uint(_loc3_);
            }
            else if(_loc4_ == "MagicName")
            {
               _loc2_.magicName = _loc3_.toString();
            }
            else if(_loc4_ == "DisplayName")
            {
               _loc2_.displayName = _loc3_.toString();
            }
            else if(_loc4_ == "RuneIcon")
            {
               _loc2_.runeIcon = _loc3_.toString();
            }
            else if(_loc4_ == "Description")
            {
               _loc2_.description = _loc3_.toString();
            }
            else if(_loc4_ == "Speed")
            {
               _loc2_.var_1218.var_251 = Number(_loc3_);
            }
            else if(_loc4_ == "GoldDrop")
            {
               _loc2_.var_1218.var_79 = Number(_loc3_);
            }
            else if(_loc4_ == "ItemDrop")
            {
               _loc2_.var_1218.itemDrop = Number(_loc3_);
            }
            else if(_loc4_ == "CraftDrop")
            {
               _loc2_.var_1218.var_152 = Number(_loc3_);
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc2_.magicName + ": " + _loc3_.name());
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary) : void
      {
         var _loc4_:XML = null;
         var _loc5_:MagicType = null;
         for each(_loc4_ in param1.*)
         {
            if((_loc5_ = method_743(_loc4_)).magicID)
            {
               if(param3[_loc5_.magicName])
               {
                  class_24.method_7("Multiple magic types with name: " + _loc5_.magicName);
               }
               if(param2[_loc5_.magicID])
               {
                  class_24.method_7("Multiple magic types with ID: " + _loc5_.magicID);
               }
               param2[_loc5_.magicID] = _loc5_;
               param3[_loc5_.magicName] = _loc5_;
            }
         }
      }
   }
}
