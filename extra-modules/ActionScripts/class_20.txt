package
{
   import flash.utils.Dictionary;
   
   public class class_20
   {
      
      public static const const_297:uint = 7;
       
      
      internal var var_197:uint;
      
      internal var var_2876:uint;
      
      internal var var_566:String;
      
      internal var displayName:String;
      
      internal var var_2969:String;
      
      internal var var_365:uint;
      
      internal var description:String;
      
      internal var var_255:String;
      
      public function class_20()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_464,class_14.var_362);
      }
      
      public static function method_968(param1:XML) : class_20
      {
         var _loc3_:String = null;
         var _loc4_:XML = null;
         var _loc2_:class_20 = new class_20();
         _loc2_.var_566 = param1.attribute("MountName").toString();
         for each(_loc4_ in param1.*)
         {
            _loc3_ = String(_loc4_.name().toString());
            if(_loc3_ == "MountID")
            {
               _loc2_.var_197 = uint(_loc4_);
            }
            else if(_loc3_ == "MountLevel")
            {
               _loc2_.var_2876 = uint(_loc4_);
            }
            else if(_loc3_ == "DisplayName")
            {
               _loc2_.displayName = _loc4_.toString();
            }
            else if(_loc3_ == "IdolCost")
            {
               _loc2_.var_365 = uint(_loc4_);
            }
            else if(_loc3_ == "Description")
            {
               _loc2_.description = _loc4_.toString();
            }
            else if(_loc3_ == "DisplayRarity")
            {
               _loc2_.var_255 = _loc4_.toString();
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc2_.var_566 + ": " + _loc3_);
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary) : void
      {
         var _loc5_:XML = null;
         var _loc6_:class_20 = null;
         var _loc4_:uint = 0;
         for each(_loc5_ in param1.*)
         {
            if((_loc6_ = method_968(_loc5_)).var_197)
            {
               if(param3[_loc6_.var_566])
               {
                  class_24.method_7("Multiple mount types with name: " + _loc6_.var_566);
               }
               if(param2[_loc6_.var_197])
               {
                  class_24.method_7("Multiple mount types with ID: " + _loc6_.var_197);
               }
               if(_loc6_.var_197 != _loc4_ + 1)
               {
                  class_24.method_7("Mount types should have sequential IDs: " + _loc6_.var_197);
               }
               if(_loc6_.var_197 >= Math.pow(2,const_297))
               {
                  class_24.method_7("Mount bits to send limit reached, increment bits needed: " + _loc6_.var_197);
               }
               param2[_loc6_.var_197] = _loc6_;
               param3[_loc6_.var_566] = _loc6_;
               _loc4_ = _loc6_.var_197;
            }
         }
      }
   }
}
