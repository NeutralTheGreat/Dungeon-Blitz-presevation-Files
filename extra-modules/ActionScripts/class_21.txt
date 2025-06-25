package
{
   import flash.utils.Dictionary;
   
   public class class_21
   {
      
      public static const const_1338:uint = 20;
      
      public static const const_1365:uint = 165;
      
      public static const const_640:uint = 185;
      
      public static const const_763:uint = 250;
      
      public static const const_50:uint = 8;
       
      
      internal var var_57:uint;
      
      internal var var_1215:String;
      
      internal var displayName:String;
      
      internal var color:uint;
      
      internal var var_935:uint;
      
      internal var var_209:uint;
      
      internal var var_492:uint;
      
      internal var var_8:String;
      
      public function class_21()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_194,class_14.var_686,class_14.var_2278,class_14.var_1194,class_14.var_949);
      }
      
      public static function method_966(param1:XML) : class_21
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc2_:class_21 = new class_21();
         for each(_loc3_ in param1.*)
         {
            if((_loc4_ = String(_loc3_.name().toString())) == "DyeName")
            {
               _loc2_.var_1215 = _loc3_.toString();
            }
            else if(_loc4_ == "DyeID")
            {
               _loc2_.var_57 = uint(_loc3_);
            }
            else if(_loc4_ == "DisplayName")
            {
               _loc2_.displayName = _loc3_.toString();
            }
            else if(_loc4_ == "Color")
            {
               _loc2_.color = uint(_loc3_);
            }
            else if(_loc4_ == "Highlight")
            {
               _loc2_.var_935 = uint(_loc3_);
            }
            else if(_loc4_ == "Shadow")
            {
               _loc2_.var_209 = uint(_loc3_);
            }
            else if(_loc4_ == "Order")
            {
               _loc2_.var_492 = uint(_loc3_);
            }
            else if(_loc4_ == "Rarity")
            {
               _loc2_.var_8 = _loc3_.toString();
            }
            else
            {
               class_24.method_7("Unrecognized Property for DyeType: " + _loc2_.var_1215 + " - " + _loc4_);
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Array, param4:Dictionary, param5:Dictionary, param6:Array) : void
      {
         var _loc7_:XML = null;
         var _loc8_:class_21 = null;
         var _loc9_:Vector.<class_21> = null;
         for each(_loc7_ in param1.*)
         {
            if((_loc8_ = method_966(_loc7_)).var_57)
            {
               if(param2[_loc8_.var_57])
               {
                  class_24.method_7("Multiple dye types with ID: " + _loc8_.var_57);
               }
               if(param5[_loc8_.var_1215])
               {
                  class_24.method_7("Multiple dye types with name: " + _loc8_.var_1215);
               }
               if(_loc8_.var_57 >= Math.pow(2,const_50))
               {
                  class_24.method_7("Dye bits to send limit reached, increment bits needed: " + _loc8_.var_57);
               }
               if(_loc8_.var_57 > Game.const_175)
               {
                  class_24.method_7("Database assumes all IDs will be less <= " + Game.const_175 + ", Contact Programmer: " + _loc8_.var_57);
               }
               if(_loc8_.var_57 > const_763)
               {
                  class_24.method_7("Apparently we have added more than 250 dyes. Update the constant and server.");
               }
               if(Boolean(param3[_loc8_.var_492]) && Boolean(_loc8_.var_492))
               {
                  class_24.method_7("Multiple dye types with order ID: " + _loc8_.var_492);
               }
               if(_loc8_.var_492 > Game.const_175)
               {
                  class_24.method_7("Database assumes all IDs will be less <= " + Game.const_175 + ", Contact Programmer: " + _loc8_.var_492);
               }
               if(_loc8_.var_492 > const_640)
               {
                  class_24.method_7("Order ID (" + _loc8_.var_492 + ")" + " > NUMBER_TOTAL_DISPLAYED_DYES (" + const_640 + ")");
               }
               if(Boolean(_loc8_.var_492) && !_loc8_.var_8)
               {
                  class_24.method_7("Dye has an order but not a rarity. DyeID: " + _loc8_.var_57);
               }
               if(!_loc8_.var_492 && Boolean(_loc8_.var_8))
               {
                  class_24.method_7("Dye has a rarity but not an order. DyeID: " + _loc8_.var_57);
               }
               param2[_loc8_.var_57] = _loc8_;
               param3[_loc8_.var_492] = _loc8_;
               param5[_loc8_.var_1215] = _loc8_;
               param6[_loc8_.color] = _loc8_;
               if(!(_loc9_ = param4[_loc8_.var_8]))
               {
                  _loc9_ = new Vector.<class_21>();
                  param4[_loc8_.var_8] = _loc9_;
               }
               _loc9_.push(_loc8_);
            }
         }
      }
      
      public static function method_2082(param1:String) : String
      {
         if(param1 == "DyeLegendary")
         {
            return "L";
         }
         if(param1 == "DyeRare")
         {
            return "R";
         }
         if(param1 == "DyeMagic")
         {
            return "M";
         }
         return null;
      }
   }
}
