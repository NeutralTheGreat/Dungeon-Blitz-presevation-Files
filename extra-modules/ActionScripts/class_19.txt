package
{
   import flash.utils.Dictionary;
   
   public class class_19
   {
       
      
      internal var var_2524:String;
      
      internal var tip:String;
      
      public function class_19()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,null,class_14.var_1729);
      }
      
      public static function method_729(param1:XML) : class_19
      {
         var _loc2_:class_19 = new class_19();
         _loc2_.var_2524 = param1.attribute("name");
         _loc2_.tip = param1;
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary) : void
      {
         var _loc4_:XML = null;
         var _loc5_:class_19 = null;
         for each(_loc4_ in param1.*)
         {
            _loc5_ = method_729(_loc4_);
            param3[_loc5_.var_2524] = _loc5_;
         }
      }
      
      public static function method_254(param1:String) : String
      {
         var _loc2_:class_19 = class_14.var_1729[param1];
         if(_loc2_)
         {
            return _loc2_.tip;
         }
         return null;
      }
   }
}
