package
{
   import flash.utils.Dictionary;
   
   public class class_5
   {
      
      public static const const_852:uint = 5;
      
      public static const const_625:uint = 11;
      
      public static const const_1185:uint = 55;
      
      private static var var_1564:int = 1;
       
      
      internal var var_2696:uint;
      
      internal var groupName:String;
      
      internal var displayName:String;
      
      internal var var_2667:Vector.<Vector.<String>>;
      
      private var var_1368:uint;
      
      internal var var_2184:Vector.<String>;
      
      public function class_5()
      {
         this.var_2667 = new Vector.<Vector.<String>>(const_1185,true);
         this.var_2184 = new Vector.<String>();
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_809(param1,class_14.var_2127,class_14.var_2322);
      }
      
      public static function method_670(param1:XML, param2:Dictionary) : class_5
      {
         var _loc5_:XML = null;
         var _loc6_:String = null;
         var _loc7_:uint = 0;
         var _loc8_:Array = null;
         var _loc9_:Vector.<String> = null;
         var _loc10_:String = null;
         var _loc11_:uint = 0;
         var _loc3_:String = param1.attribute("GroupName");
         var _loc4_:class_5;
         if(!(_loc4_ = param2[_loc3_]))
         {
            (_loc4_ = new class_5()).groupName = _loc3_;
            _loc4_.var_2696 = var_1564++;
         }
         for each(_loc5_ in param1.*)
         {
            if((_loc6_ = String(_loc5_.name().toString())) == "DisplayName")
            {
               _loc4_.displayName = _loc5_.toString();
            }
            else if(_loc6_ == "ProgressReward")
            {
               _loc4_.var_2184.push(_loc5_.toString());
            }
            else if(!_loc6_.indexOf("Mission"))
            {
               if(!(_loc7_ = uint(_loc6_.substr(7))) || _loc7_ > const_625)
               {
                  class_24.method_7("Bad mission number in Group - " + _loc4_.groupName + ": " + _loc7_);
               }
               _loc8_ = _loc5_.toString().split(",");
               _loc9_ = new Vector.<String>();
               for each(_loc10_ in _loc8_)
               {
                  _loc9_.push(_loc10_);
               }
               _loc9_.fixed = true;
               _loc11_ = _loc4_.var_1368 * const_625 + _loc7_ - 1;
               _loc4_.var_2667[_loc11_] = _loc9_;
            }
            else
            {
               class_24.method_7("Unrecognized Property in Mission Group - " + _loc4_.groupName + ": " + _loc6_);
            }
         }
         ++_loc4_.var_1368;
         return _loc4_;
      }
      
      public static function method_809(param1:XML, param2:Array, param3:Dictionary) : void
      {
         var _loc4_:class_5 = null;
         var _loc5_:XML = null;
         for each(_loc5_ in param1.*)
         {
            _loc4_ = method_670(_loc5_,param3);
            param2[_loc4_.var_2696] = _loc4_;
            param3[_loc4_.groupName] = _loc4_;
         }
         for each(_loc4_ in param2)
         {
            _loc4_.var_2184.fixed = true;
            if(_loc4_.var_1368 != const_852)
            {
               class_24.method_7("Bad mission group size for Group - " + _loc4_.groupName + ": " + _loc4_.var_1368);
            }
         }
      }
   }
}
