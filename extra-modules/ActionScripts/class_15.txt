package
{
   import flash.utils.Dictionary;
   
   public class class_15
   {
      
      public static const const_300:uint = 2;
      
      public static var var_2716:uint;
      
      public static const const_1316:Array = new Array(0,1,2,4,10,99);
      
      public static const const_1305:Array = new Array(5,7,10,15,20);
      
      public static const const_1357:uint = 7;
      
      public static const const_1328:uint = 20;
      
      public static const const_1419:uint = 1;
      
      public static const const_1360:uint = 99;
       
      
      internal var lockboxID:uint;
      
      internal var var_1375:String;
      
      internal var displayName:String;
      
      internal var var_2810:String;
      
      internal var iconName:String;
      
      internal var var_2467:Boolean;
      
      internal var var_2457:uint;
      
      internal var description:String;
      
      internal var var_2926:uint;
      
      public function class_15()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_838,class_14.var_2176,class_14.var_2148);
      }
      
      public static function method_638(param1:XML) : class_15
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc2_:class_15 = new class_15();
         _loc2_.var_1375 = param1.attribute("LockboxName");
         for each(_loc3_ in param1.*)
         {
            if((_loc4_ = String(_loc3_.name().toString())) == "LockboxID")
            {
               _loc2_.lockboxID = uint(_loc3_);
            }
            else if(_loc4_ == "DisplayName")
            {
               _loc2_.displayName = _loc3_.toString();
            }
            else if(_loc4_ == "CustomArt")
            {
               _loc2_.var_2810 = _loc3_.toString();
            }
            else if(_loc4_ == "IconName")
            {
               _loc2_.iconName = _loc3_.toString();
            }
            else if(_loc4_ == "Droppable")
            {
               _loc2_.var_2467 = MathUtil.method_50(_loc3_);
            }
            else if(_loc4_ == "DroppableWeight")
            {
               _loc2_.var_2457 = uint(_loc3_);
            }
            else if(_loc4_ == "Description")
            {
               _loc2_.description = _loc3_.toString();
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc2_.var_1375 + ": " + _loc4_);
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Array, param4:Dictionary) : void
      {
         var _loc6_:XML = null;
         var _loc7_:class_15 = null;
         var _loc5_:uint = 0;
         for each(_loc6_ in param1.*)
         {
            if((_loc7_ = method_638(_loc6_)).lockboxID)
            {
               if(_loc7_.lockboxID >= Math.pow(2,const_300))
               {
                  class_24.method_7("LockboxType BitsToSend limit reached, increment bits needed: " + _loc7_.lockboxID);
               }
               param2[_loc7_.lockboxID] = _loc7_;
               param4[_loc7_.var_1375] = _loc7_;
               if(_loc7_.var_2467)
               {
                  param3.push(_loc7_);
                  _loc5_ += _loc7_.var_2457;
                  _loc7_.var_2926 = _loc5_;
               }
            }
         }
         var_2716 = _loc5_;
      }
   }
}
