package
{
   import flash.utils.Dictionary;
   
   public class class_7
   {
      
      public static const const_871:String = "Lockbox01";
      
      public static const const_1106:String = "SigilLegendary01";
      
      public static const const_1308:Number = 0.3;
      
      public static const const_19:uint = 7;
      
      public static const const_75:uint = 6;
      
      public static const const_1325:uint = 6;
      
      public static const const_1317:uint = 1;
      
      public static const const_1332:uint = 10;
      
      public static const const_220:uint = 0;
      
      public static const const_199:uint = 1;
      
      public static const const_187:uint = 2;
      
      public static const const_684:uint = 3;
      
      public static const const_1313:uint = 2;
      
      public static const const_35:uint = 20;
      
      public static const const_164:Array = [0,4000,12500,24200,39400,57300,78800,103200,130100,158800,192100,229000,272100,320300,375500,434600,501100,573800,655300,744400,2147483648];
      
      public static const const_1138:uint = 110;
      
      public static const const_797:Array = [0,0,180,1800,7200,14400,28800,57600,86400,115200,144000,172800,201600,230400,259200,345600,432000,518400,604800,691200,777600];
      
      public static const const_685:Array = [0,0,2000,4000,6000,8000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,200000,300000,400000,500000,600000];
      
      public static const const_650:Array = [0,0,1,2,3,4,5,10,15,20,25,30,35,38,39,40,54,67,80,94,107];
      
      public static const const_179:uint = 0;
      
      public static const const_180:uint = 1;
      
      public static const const_196:uint = 2;
      
      public static const const_661:Number = 0.1;
       
      
      internal var var_104:uint;
      
      internal var var_2923:uint;
      
      internal var var_310:String;
      
      internal var displayName:String;
      
      internal var var_1138:String;
      
      internal var var_365:uint;
      
      internal var var_284:String;
      
      internal var color:String;
      
      internal var description:String;
      
      internal var var_255:String;
      
      internal var var_103:String;
      
      internal var var_2919:String;
      
      internal var var_2234:Boolean = false;
      
      internal var var_2296:Boolean = false;
      
      internal var var_2421:Boolean = false;
      
      internal var var_2178:Boolean = false;
      
      internal var var_2922:Boolean = false;
      
      internal var var_1977:Boolean = false;
      
      internal var var_2394:Boolean = false;
      
      internal var var_2057:Boolean = false;
      
      internal var var_1698:Boolean = false;
      
      internal var var_2294:Boolean = false;
      
      public function class_7()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_224,class_14.var_233,class_14.var_2088);
      }
      
      public static function method_746(param1:XML) : class_7
      {
         var _loc3_:String = null;
         var _loc4_:XML = null;
         var _loc2_:class_7 = new class_7();
         _loc2_.var_310 = param1.attribute("PetName").toString();
         for each(_loc4_ in param1.*)
         {
            _loc3_ = String(_loc4_.name().toString());
            if(_loc3_ == "PetID")
            {
               _loc2_.var_104 = uint(_loc4_);
            }
            else if(_loc3_ == "PetLevel")
            {
               _loc2_.var_2923 = uint(_loc4_);
            }
            else if(_loc3_ == "DisplayName")
            {
               _loc2_.displayName = _loc4_.toString();
            }
            else if(_loc3_ == "PetPower")
            {
               _loc2_.var_1138 = _loc4_.toString();
            }
            else if(_loc3_ == "Description")
            {
               _loc2_.description = _loc4_.toString();
            }
            else if(_loc3_ == "IdolCost")
            {
               _loc2_.var_365 = uint(_loc4_);
            }
            else if(_loc3_ == "Kingdom")
            {
               _loc2_.var_103 = _loc4_.toString();
            }
            else if(_loc3_ == "BonusInfo")
            {
               _loc2_.var_2919 = _loc4_.toString();
            }
            else if(_loc3_ == "ClassType")
            {
               _loc2_.var_284 = _loc4_.toString();
            }
            else if(_loc3_ == "Color")
            {
               _loc2_.color = _loc4_.toString();
            }
            else if(_loc3_ == "ItemFind")
            {
               _loc2_.var_2234 = MathUtil.method_50(_loc4_.toString());
            }
            else if(_loc3_ == "GoldFind")
            {
               _loc2_.var_2296 = MathUtil.method_50(_loc4_.toString());
            }
            else if(_loc3_ == "CraftFind")
            {
               _loc2_.var_2421 = MathUtil.method_50(_loc4_.toString());
            }
            else if(_loc3_ == "ExpBonus")
            {
               _loc2_.var_2178 = MathUtil.method_50(_loc4_.toString());
            }
            else if(_loc3_ == "UseVanityPower")
            {
               _loc2_.var_2294 = MathUtil.method_50(_loc4_.toString());
            }
            else if(_loc3_ == "DisplayRarity")
            {
               _loc2_.var_255 = _loc4_.toString();
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc2_.var_310 + ": " + _loc3_);
            }
         }
         if(_loc2_.var_103 == "Any")
         {
            _loc2_.var_2922 = true;
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary, param4:Dictionary) : void
      {
         var _loc6_:XML = null;
         var _loc7_:class_7 = null;
         var _loc8_:String = null;
         var _loc9_:Vector.<class_7> = null;
         var _loc5_:uint = 0;
         for each(_loc6_ in param1.*)
         {
            if((_loc7_ = method_746(_loc6_)).var_104)
            {
               if(param3[_loc7_.var_310])
               {
                  class_24.method_7("Multiple pet types with name: " + _loc7_.var_310);
               }
               if(param2[_loc7_.var_104])
               {
                  class_24.method_7("Multiple pet types with ID: " + _loc7_.var_104);
               }
               if(_loc7_.var_104 != _loc5_ + 1)
               {
                  class_24.method_7("Pets types should have sequential IDs: " + _loc7_.var_104);
               }
               if(_loc7_.var_104 >= Math.pow(2,const_19))
               {
                  class_24.method_7("Pet bits to send limit reached, increment bits needed: " + _loc7_.var_104);
               }
               if(_loc7_.var_284 == const_871)
               {
                  _loc7_.var_1977 = true;
               }
               if(_loc7_.var_284 == const_1106)
               {
                  _loc7_.var_1698 = true;
               }
               param2[_loc7_.var_104] = _loc7_;
               param3[_loc7_.var_310] = _loc7_;
               _loc5_ = _loc7_.var_104;
               _loc8_ = _loc7_.var_284 + _loc7_.color;
               if(!(_loc9_ = param4[_loc8_]))
               {
                  _loc9_ = new Vector.<class_7>();
                  param4[_loc8_] = _loc9_;
               }
               _loc9_.push(_loc7_);
            }
         }
      }
      
      public static function method_1520(param1:uint) : uint
      {
         return const_1138;
      }
      
      public static function method_154(param1:uint) : uint
      {
         if(param1 >= const_164.length)
         {
            return 0;
         }
         return const_164[param1];
      }
      
      public static function method_516(param1:uint) : uint
      {
         if(param1 >= const_797.length)
         {
            return 0;
         }
         return const_797[param1];
      }
      
      public static function method_383(param1:uint) : uint
      {
         if(param1 >= const_685.length)
         {
            return 0;
         }
         return const_685[param1];
      }
      
      public static function method_1876(param1:uint) : uint
      {
         if(param1 >= const_650.length)
         {
            return 0;
         }
         return const_650[param1];
      }
   }
}
