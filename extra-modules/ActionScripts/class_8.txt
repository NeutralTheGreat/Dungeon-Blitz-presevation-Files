package
{
   import flash.utils.Dictionary;
   
   public class class_8
   {
      
      public static const const_658:uint = 7;
      
      public static const const_890:uint = 10;
      
      public static const const_1409:uint = 11;
      
      public static const const_256:uint = 7;
      
      public static const const_1119:Array = [8,22,50,101,171,310,462,697,945,1442];
      
      public static const const_1055:Array = [1800,4800,10800,21600,36000,64800,96000,144000,192000,288000];
      
      public static const const_1018:Array = [1,2,3,4,5,7,10,13,16,20];
      
      public static const const_395:Array = [6,12,18,24,30,36,42,48,54,60,66];
      
      public static const const_731:uint = 7;
      
      public static const const_1040:Array = [0,1,5,15,29,42,54];
      
      public static const const_1240:Array = [0,1,1.5,2,2.5,3,3.5];
      
      public static const const_1286:Array = [0,0,0.2,0.4,0.6,0.8,1];
      
      public static const const_968:Number = 0.9;
      
      public static const const_1072:Number = 0.4;
      
      public static const const_1299:Number = 0.01;
      
      public static const const_1024:Number = 0.02;
      
      public static const const_1191:Number = 0.03;
      
      public static const const_705:uint = 1;
      
      public static const const_725:uint = 3;
      
      public static const const_637:uint = 9;
       
      
      internal var var_140:uint;
      
      internal var var_537:String;
      
      internal var displayName:String;
      
      internal var iconName:String;
      
      internal var var_139:String;
      
      internal var var_103:String;
      
      internal var var_2537:String;
      
      internal var var_2672:Boolean;
      
      public function class_8()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_629,class_14.var_2015,class_14.var_2342);
      }
      
      public static function method_631(param1:XML) : class_8
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc2_:class_8 = new class_8();
         _loc2_.var_537 = param1.attribute("MaterialName");
         for each(_loc3_ in param1.*)
         {
            if((_loc4_ = String(_loc3_.name().toString())) == "MaterialID")
            {
               _loc2_.var_140 = uint(_loc3_);
            }
            else if(_loc4_ == "DisplayName")
            {
               _loc2_.displayName = _loc3_.toString();
            }
            else if(_loc4_ == "IconName")
            {
               _loc2_.iconName = _loc3_.toString();
            }
            else if(_loc4_ == "Kingdom")
            {
               _loc2_.var_103 = _loc3_.toString();
            }
            else if(_loc4_ == "Rarity")
            {
               _loc2_.var_139 = _loc3_.toString();
            }
            else if(_loc4_ == "DropRealm")
            {
               _loc2_.var_2537 = _loc3_.toString();
            }
            else if(_loc4_ == "FromRoyalStore")
            {
               _loc2_.var_2672 = MathUtil.method_50(_loc3_);
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc2_.var_537 + ": " + _loc4_);
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary, param4:Array) : void
      {
         var _loc5_:XML = null;
         var _loc6_:class_8 = null;
         var _loc7_:String = null;
         for each(_loc5_ in param1.*)
         {
            if((_loc6_ = method_631(_loc5_)).var_140)
            {
               if(param2[_loc6_.var_140])
               {
                  class_24.method_7("Multiple materials with ID: " + _loc6_.var_140);
               }
               if(param3[_loc6_.var_537])
               {
                  class_24.method_7("Multiple materials with name: " + _loc6_.var_537);
               }
               if(_loc6_.var_140 >= Math.pow(2,const_658))
               {
                  class_24.method_7("Item bits to send limit reached, increment bits needed: " + _loc6_.var_140);
               }
               _loc7_ = _loc6_.var_103 + _loc6_.var_2537 + _loc6_.var_139;
               if(_loc6_.var_537 != _loc7_)
               {
                  class_24.method_7("Material name does not follow convention: " + _loc6_.var_537 + " != " + _loc7_);
               }
               param2[_loc6_.var_140] = _loc6_;
               param3[_loc6_.var_537] = _loc6_;
               if(_loc6_.var_2672)
               {
                  param4.push(_loc6_);
               }
            }
         }
         if(const_395[const_395.length - 1] >= Math.pow(2,const_731))
         {
            class_24.method_7("Material StackCount bits to send too low for max materials");
         }
      }
      
      public static function method_220(param1:String) : uint
      {
         if(param1 == "R")
         {
            return const_725;
         }
         if(param1 == "L")
         {
            return const_637;
         }
         return const_705;
      }
   }
}
