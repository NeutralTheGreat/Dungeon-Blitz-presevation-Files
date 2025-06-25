package
{
   import flash.utils.Dictionary;
   
   public class class_16
   {
      
      public static const const_167:uint = 6;
      
      public static const const_1290:uint = 8;
      
      public static const const_1251:uint = 4;
      
      public static const const_993:uint = 3600 * 24 * 3;
      
      public static const const_1093:uint = 3600 * 24 * 6;
      
      public static const const_907:uint = 3600 * 24 * 10;
      
      public static const const_303:uint = 0;
      
      public static const const_376:uint = 1;
      
      public static const const_809:uint = 2;
      
      public static const const_1324:uint = 63;
      
      public static const const_1394:uint = 6;
      
      public static const const_644:Array = [0,5000,25000,50000,75000,250000,500000,750000];
      
      public static const const_600:Array = [0,3,13,25,37,60,94,119];
       
      
      internal var var_206:uint;
      
      internal var var_1205:String;
      
      internal var displayName:String;
      
      internal var var_284:String;
      
      internal var color:String;
      
      internal var description:String;
      
      internal var var_392:uint;
      
      internal var var_266:String;
      
      public function class_16()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_212,class_14.var_2236,class_14.var_1951);
      }
      
      public static function method_641(param1:XML) : class_16
      {
         var _loc3_:String = null;
         var _loc4_:XML = null;
         var _loc2_:class_16 = new class_16();
         _loc2_.var_1205 = param1.attribute("EggName").toString();
         for each(_loc4_ in param1.*)
         {
            _loc3_ = String(_loc4_.name().toString());
            if(_loc3_ == "EggID")
            {
               _loc2_.var_206 = uint(_loc4_);
            }
            else if(_loc3_ == "DisplayName")
            {
               _loc2_.displayName = _loc4_.toString();
            }
            else if(_loc3_ == "ClassType")
            {
               _loc2_.var_284 = _loc4_.toString();
            }
            else if(_loc3_ == "Color")
            {
               _loc2_.color = _loc4_.toString();
            }
            else if(_loc3_ == "Description")
            {
               _loc2_.description = _loc4_.toString();
            }
            else if(_loc3_ == "EggRank")
            {
               _loc2_.var_392 = uint(_loc4_);
            }
            else if(_loc3_ == "Art")
            {
               _loc2_.var_266 = _loc4_.toString();
            }
         }
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary, param4:Dictionary) : void
      {
         var _loc6_:XML = null;
         var _loc7_:class_16 = null;
         var _loc8_:Vector.<class_16> = null;
         var _loc9_:String = null;
         var _loc10_:String = null;
         var _loc5_:uint = 0;
         for each(_loc6_ in param1.*)
         {
            if((_loc7_ = method_641(_loc6_)).var_206)
            {
               if(param3[_loc7_.var_1205])
               {
                  class_24.method_7("Multiple Eggs types with name: " + _loc7_.var_1205);
               }
               if(param2[_loc7_.var_206])
               {
                  class_24.method_7("Multiple Eggs types with ID: " + _loc7_.var_206);
               }
               if(_loc7_.var_206 != _loc5_ + 1)
               {
                  class_24.method_7("Egg types should have sequential IDs: " + _loc7_.var_206);
               }
               if(_loc7_.var_206 >= Math.pow(2,const_167))
               {
                  class_24.method_7("Egg bits to send limit reached, increment bits needed: " + _loc7_.var_206);
               }
               param2[_loc7_.var_206] = _loc7_;
               param3[_loc7_.var_1205] = _loc7_;
               _loc5_ = _loc7_.var_206;
               if(_loc7_.var_284 == "Dragon")
               {
                  if(!(_loc8_ = param4["GenericBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["GenericBrown"] = _loc8_;
                  if(!(_loc8_ = param4["CommonBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["CommonBrown"] = _loc8_;
                  if(!(_loc8_ = param4["OrdinaryBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["OrdinaryBrown"] = _loc8_;
                  _loc9_ = "Generic" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc9_ = "Common" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc9_ = "Ordinary" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc10_ = _loc7_.var_284 + _loc7_.color;
                  if(!(_loc8_ = param4[_loc10_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc10_] = _loc8_;
               }
               else if(_loc7_.var_284 == "Bird")
               {
                  if(!(_loc8_ = param4["CommonBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["CommonBrown"] = _loc8_;
                  if(!(_loc8_ = param4["OrdinaryBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["OrdinaryBrown"] = _loc8_;
                  if(!(_loc8_ = param4["PlainBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["PlainBrown"] = _loc8_;
                  _loc9_ = "Common" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc9_ = "Ordinary" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc9_ = "Plain" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc10_ = _loc7_.var_284 + _loc7_.color;
                  if(!(_loc8_ = param4[_loc10_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc10_] = _loc8_;
               }
               else if(_loc7_.var_284 == "Ancient")
               {
                  if(!(_loc8_ = param4["GenericBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["GenericBrown"] = _loc8_;
                  if(!(_loc8_ = param4["OrdinaryBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["OrdinaryBrown"] = _loc8_;
                  if(!(_loc8_ = param4["PlainBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["PlainBrown"] = _loc8_;
                  _loc9_ = "Generic" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc9_ = "Ordinary" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc9_ = "Plain" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc10_ = _loc7_.var_284 + _loc7_.color;
                  if(!(_loc8_ = param4[_loc10_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc10_] = _loc8_;
               }
               else if(_loc7_.var_284 == "Ghost")
               {
                  if(!(_loc8_ = param4["GenericBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["GenericBrown"] = _loc8_;
                  if(!(_loc8_ = param4["CommonBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["CommonBrown"] = _loc8_;
                  if(!(_loc8_ = param4["PlainBrown"]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4["PlainBrown"] = _loc8_;
                  _loc9_ = "Generic" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc9_ = "Common" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc9_ = "Plain" + _loc7_.color;
                  if(!(_loc8_ = param4[_loc9_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc9_] = _loc8_;
                  _loc10_ = _loc7_.var_284 + _loc7_.color;
                  if(!(_loc8_ = param4[_loc10_]))
                  {
                     _loc8_ = new Vector.<class_16>();
                  }
                  _loc8_.push(_loc7_);
                  param4[_loc10_] = _loc8_;
               }
            }
         }
      }
      
      public static function method_467(param1:uint, param2:Boolean) : uint
      {
         if(param2)
         {
            return Game.const_181;
         }
         if(param1 == const_303)
         {
            return const_993;
         }
         if(param1 == const_376)
         {
            return const_1093;
         }
         return const_907;
      }
      
      public static function method_2123(param1:class_16) : class_16
      {
         if(!param1)
         {
            return null;
         }
         var _loc2_:Vector.<class_16> = class_14.var_1951[param1.var_1205];
         if(!_loc2_)
         {
            return null;
         }
         var _loc3_:uint = Math.floor(Math.random() * _loc2_.length);
         return _loc2_[_loc3_];
      }
      
      public static function method_2132(param1:uint) : uint
      {
         if(param1 == 1)
         {
            return 3;
         }
         if(param1 == 2)
         {
            return 4;
         }
         if(param1 == 3)
         {
            return 4;
         }
         if(param1 == 4)
         {
            return 5;
         }
         if(param1 == 5)
         {
            return 5;
         }
         if(param1 == 6)
         {
            return 6;
         }
         if(param1 == 7)
         {
            return 6;
         }
         if(param1 == 8)
         {
            return 7;
         }
         if(param1 == 9)
         {
            return 7;
         }
         if(param1 == 10)
         {
            return 8;
         }
         return 0;
      }
      
      public static function method_2068(param1:uint) : Vector.<uint>
      {
         var _loc7_:class_16 = null;
         var _loc8_:uint = 0;
         var _loc9_:uint = 0;
         var _loc2_:Vector.<uint> = new Vector.<uint>();
         var _loc3_:Vector.<uint> = new Vector.<uint>();
         var _loc4_:Vector.<uint> = new Vector.<uint>();
         var _loc5_:uint = 1;
         while(_loc5_ < class_14.var_212.length)
         {
            if((_loc7_ = class_14.var_212[_loc5_]).var_392 == const_303)
            {
               _loc2_.push(_loc7_.var_206);
            }
            if(_loc7_.var_392 == const_376)
            {
               _loc3_.push(_loc7_.var_206);
            }
            if(_loc7_.var_392 == const_809)
            {
               _loc4_.push(_loc7_.var_206);
            }
            _loc5_++;
         }
         _loc5_ = 0;
         while(_loc5_ < _loc2_.length)
         {
            _loc8_ = Math.floor(Math.random() * _loc2_.length);
            _loc9_ = _loc2_[_loc5_];
            _loc2_[_loc5_] = _loc2_[_loc8_];
            _loc2_[_loc8_] = _loc9_;
            _loc5_++;
         }
         _loc5_ = 0;
         while(_loc5_ < _loc3_.length)
         {
            _loc8_ = Math.floor(Math.random() * _loc3_.length);
            _loc9_ = _loc3_[_loc5_];
            _loc3_[_loc5_] = _loc3_[_loc8_];
            _loc3_[_loc8_] = _loc9_;
            _loc5_++;
         }
         _loc5_ = 0;
         while(_loc5_ < _loc4_.length)
         {
            _loc8_ = Math.floor(Math.random() * _loc4_.length);
            _loc9_ = _loc4_[_loc5_];
            _loc4_[_loc5_] = _loc4_[_loc8_];
            _loc4_[_loc8_] = _loc9_;
            _loc5_++;
         }
         var _loc6_:Vector.<uint> = new Vector.<uint>(param1);
         _loc5_ = 0;
         while(_loc5_ < param1)
         {
            if(_loc5_ == 0)
            {
               _loc6_[0] = _loc2_[0];
            }
            if(_loc5_ == 1)
            {
               _loc6_[1] = _loc2_[1];
            }
            if(_loc5_ == 2)
            {
               _loc6_[2] = _loc3_[0];
            }
            if(_loc5_ == 3)
            {
               _loc6_[3] = _loc3_[1];
            }
            if(_loc5_ == 4)
            {
               _loc6_[4] = _loc3_[2];
            }
            if(_loc5_ == 5)
            {
               _loc6_[5] = _loc4_[0];
            }
            if(_loc5_ == 6)
            {
               _loc6_[6] = _loc4_[1];
            }
            if(_loc5_ == 7)
            {
               _loc6_[7] = _loc4_[2];
            }
            _loc5_++;
         }
         return _loc6_;
      }
      
      public static function method_2072(param1:uint, param2:Vector.<uint>) : uint
      {
         var _loc7_:class_16 = null;
         var _loc8_:uint = 0;
         var _loc9_:uint = 0;
         if(param1 < 3 || param1 > 7)
         {
            return 1;
         }
         var _loc3_:Vector.<uint> = new Vector.<uint>();
         var _loc4_:Vector.<uint> = new Vector.<uint>();
         var _loc5_:Vector.<uint> = new Vector.<uint>();
         var _loc6_:uint = 1;
         while(_loc6_ < class_14.var_212.length)
         {
            if((_loc7_ = class_14.var_212[_loc6_]).var_392 == const_303)
            {
               _loc3_.push(_loc7_.var_206);
            }
            if(_loc7_.var_392 == const_376)
            {
               _loc4_.push(_loc7_.var_206);
            }
            if(_loc7_.var_392 == const_809)
            {
               _loc5_.push(_loc7_.var_206);
            }
            _loc6_++;
         }
         _loc6_ = 0;
         while(_loc6_ < _loc3_.length)
         {
            _loc8_ = Math.floor(Math.random() * _loc3_.length);
            _loc9_ = _loc3_[_loc6_];
            _loc3_[_loc6_] = _loc3_[_loc8_];
            _loc3_[_loc8_] = _loc9_;
            _loc6_++;
         }
         _loc6_ = 0;
         while(_loc6_ < _loc4_.length)
         {
            _loc8_ = Math.floor(Math.random() * _loc4_.length);
            _loc9_ = _loc4_[_loc6_];
            _loc4_[_loc6_] = _loc4_[_loc8_];
            _loc4_[_loc8_] = _loc9_;
            _loc6_++;
         }
         _loc6_ = 0;
         while(_loc6_ < _loc5_.length)
         {
            _loc8_ = Math.floor(Math.random() * _loc5_.length);
            _loc9_ = _loc5_[_loc6_];
            _loc5_[_loc6_] = _loc5_[_loc8_];
            _loc5_[_loc8_] = _loc9_;
            _loc6_++;
         }
         if(param1 == 3)
         {
            if(_loc4_[0] == param2[2])
            {
               return _loc4_[1];
            }
            return _loc4_[0];
         }
         if(param1 == 4)
         {
            if(_loc4_[0] == param2[2] || _loc4_[0] == param2[3])
            {
               if(_loc4_[1] == param2[2] || _loc4_[1] == param2[3])
               {
                  return _loc4_[2];
               }
               return _loc4_[1];
            }
            return _loc4_[0];
         }
         if(param1 == 5)
         {
            return _loc5_[0];
         }
         if(param1 == 6)
         {
            if(_loc5_[0] == param2[5])
            {
               return _loc5_[1];
            }
            return _loc5_[0];
         }
         if(param1 == 7)
         {
            if(_loc5_[0] == param2[5] || _loc5_[0] == param2[6])
            {
               if(_loc5_[1] == param2[5] || _loc5_[1] == param2[6])
               {
                  return _loc5_[2];
               }
               return _loc5_[1];
            }
            return _loc5_[0];
         }
         return 1;
      }
      
      public static function method_586(param1:int) : uint
      {
         if(param1 < 0 || param1 >= const_644.length)
         {
            return 0;
         }
         return const_644[param1];
      }
      
      public static function method_1241(param1:int) : uint
      {
         if(param1 < 0 || param1 >= const_600.length)
         {
            return 0;
         }
         return const_600[param1];
      }
      
      public function method_450() : String
      {
         if(this.var_392 == const_303)
         {
            return "M";
         }
         if(this.var_392 == const_376)
         {
            return "R";
         }
         return "L";
      }
   }
}
