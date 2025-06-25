package
{
   import flash.utils.Dictionary;
   
   public class class_2
   {
       
      
      internal var levelName:String;
      
      internal var displayName:String;
      
      internal var var_431:String;
      
      internal var var_2796:String;
      
      internal var var_2756:String;
      
      public function class_2()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_430);
      }
      
      public static function method_947(param1:XML) : class_2
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc2_:class_2 = new class_2();
         _loc2_.levelName = param1.attribute("LevelName").toString();
         for each(_loc3_ in param1.*)
         {
            if((_loc4_ = String(_loc3_.name().toString())) == "DisplayName")
            {
               _loc2_.displayName = _loc3_.toString();
            }
            else if(_loc4_ == "ZoneSet")
            {
               _loc2_.var_431 = _loc3_.toString();
            }
            else if(_loc4_ == "RankingsURL")
            {
               _loc2_.var_2796 = _loc3_.toString();
            }
            else if(_loc4_ == "MusicLoop")
            {
               _loc2_.var_2756 = _loc3_.toString();
            }
            else
            {
               class_24.method_7("Unrecognized Property for LevelType: " + _loc2_.levelName + " - " + _loc4_);
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Dictionary) : void
      {
         var _loc3_:XML = null;
         var _loc4_:class_2 = null;
         for each(_loc3_ in param1.*)
         {
            _loc4_ = method_947(_loc3_);
            if(param2[_loc4_.levelName])
            {
               class_24.method_7("Multiple level types with name: " + _loc4_.levelName);
            }
            param2[_loc4_.levelName] = _loc4_;
         }
      }
   }
}
