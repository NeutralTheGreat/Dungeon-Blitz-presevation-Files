package
{
   import flash.utils.Dictionary;
   
   public class class_11
   {
      
      public static const const_641:uint = 104;
      
      public static const const_759:uint = 999;
      
      public static const const_1218:uint = 1000;
       
      
      internal var var_652:String;
      
      internal var doorID:uint;
      
      internal var var_929:String;
      
      internal var var_2896:uint;
      
      internal var var_2901:String;
      
      internal var var_2885:Array;
      
      internal var var_2883:Array;
      
      public function class_11()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_2248,class_14.var_1921);
      }
      
      public static function method_590(param1:XML) : class_11
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc2_:class_11 = new class_11();
         for each(_loc3_ in param1.*)
         {
            if((_loc4_ = String(_loc3_.name().toString())) == "MapName")
            {
               _loc2_.var_652 = _loc3_.toString();
            }
            else if(_loc4_ == "DoorID")
            {
               _loc2_.doorID = uint(_loc3_);
            }
            else if(_loc4_ == "TargetMapName")
            {
               _loc2_.var_929 = _loc3_.toString();
            }
            else if(_loc4_ == "TargetDoorID")
            {
               _loc2_.var_2896 = uint(_loc3_);
            }
            else if(_loc4_ == "LockedMessage")
            {
               _loc2_.var_2901 = _loc3_.toString();
            }
            else if(_loc4_ == "RequiredMissions")
            {
               _loc2_.var_2885 = _loc3_.toString().split(",");
            }
            else if(_loc4_ == "CompletedMissions")
            {
               _loc2_.var_2883 = _loc3_.toString().split(",");
            }
            else
            {
               class_24.method_7("Unrecognized Property on map " + _loc2_.var_652 + ":" + _loc2_.doorID + " - " + _loc4_);
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary) : void
      {
         var _loc4_:XML = null;
         var _loc5_:class_11 = null;
         var _loc6_:class_11 = null;
         var _loc7_:String = null;
         for each(_loc4_ in param1.*)
         {
            _loc7_ = (_loc6_ = method_590(_loc4_)).var_652 + ":" + _loc6_.doorID;
            if(param3[_loc7_])
            {
               class_24.method_7("Multiple doors with key: " + _loc7_);
            }
            param2.push(_loc6_);
            param3[_loc7_] = _loc6_;
         }
         if(!(_loc5_ = method_545("NewbieRoad",const_641)) || _loc5_.var_929 != "TutorialBoat")
         {
            class_24.method_7("Tutorial Boat ID has changed, please fix constant DOOR_TUTORIALBOAT");
         }
      }
      
      public static function method_545(param1:String, param2:uint) : class_11
      {
         var _loc3_:String = param1 + ":" + param2;
         return class_14.var_1921[_loc3_];
      }
   }
}
