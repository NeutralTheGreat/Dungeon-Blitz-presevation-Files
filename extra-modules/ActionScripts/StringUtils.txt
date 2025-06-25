package
{
   public class StringUtils
   {
       
      
      public function StringUtils()
      {
         super();
      }
      
      public static function method_400(param1:String, param2:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         var _loc3_:int = param1.indexOf(param2);
         if(_loc3_ == -1)
         {
            return "";
         }
         _loc3_ += param2.length;
         return param1.substr(_loc3_);
      }
      
      public static function method_2101(param1:String, param2:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         var _loc3_:int = param1.lastIndexOf(param2);
         if(_loc3_ == -1)
         {
            return "";
         }
         _loc3_ += param2.length;
         return param1.substr(_loc3_);
      }
      
      public static function method_2061(param1:String, param2:String) : Boolean
      {
         if(param1 == null)
         {
            return false;
         }
         return param1.indexOf(param2) == 0;
      }
      
      public static function method_1002(param1:String, param2:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         var _loc3_:int = param1.indexOf(param2);
         if(_loc3_ == -1)
         {
            return param1;
         }
         return param1.substr(0,_loc3_);
      }
      
      public static function method_722(param1:String, param2:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         var _loc3_:int = param1.lastIndexOf(param2);
         if(_loc3_ == -1)
         {
            return "";
         }
         return param1.substr(0,_loc3_);
      }
      
      public static function method_1611(param1:String, param2:String, param3:String) : String
      {
         var _loc6_:int = 0;
         var _loc4_:String = "";
         if(param1 == null)
         {
            return _loc4_;
         }
         var _loc5_:int;
         if((_loc5_ = param1.indexOf(param2)) != -1)
         {
            _loc5_ += param2.length;
            if((_loc6_ = param1.indexOf(param3,_loc5_)) != -1)
            {
               _loc4_ = param1.substr(_loc5_,_loc6_ - _loc5_);
            }
         }
         return _loc4_;
      }
      
      public static function method_2118(param1:String, param2:uint, param3:String = ".") : Array
      {
         var _loc8_:String = null;
         var _loc4_:Array = new Array();
         if(param1 == null || !contains(param1,param3))
         {
            return _loc4_;
         }
         var _loc5_:uint = 0;
         var _loc6_:uint = uint(param1.length);
         var _loc7_:RegExp = new RegExp("[^" + method_212(param3) + "]+$");
         while(_loc5_ < _loc6_)
         {
            _loc8_ = param1.substr(_loc5_,param2);
            if(!contains(_loc8_,param3))
            {
               _loc4_.push(method_597(_loc8_,_loc8_.length));
               _loc5_ += _loc8_.length;
            }
            _loc8_ = _loc8_.replace(_loc7_,"");
            _loc4_.push(_loc8_);
            _loc5_ += _loc8_.length;
         }
         return _loc4_;
      }
      
      public static function method_1440(param1:String, ... rest) : String
      {
         var _loc3_:String = method_700(param1);
         if(rest[0] === true)
         {
            return _loc3_.replace(/^.|\b./g,method_732);
         }
         return _loc3_.replace(/(^\w)/,method_732);
      }
      
      public static function contains(param1:String, param2:String) : Boolean
      {
         if(param1 == null)
         {
            return false;
         }
         return param1.indexOf(param2) != -1;
      }
      
      public static function method_2030(param1:String, param2:String, param3:Boolean = true) : uint
      {
         if(param1 == null)
         {
            return 0;
         }
         var _loc4_:String = method_212(param2);
         var _loc5_:String = !param3 ? "ig" : "g";
         return param1.match(new RegExp(_loc4_,_loc5_)).length;
      }
      
      public static function method_673(param1:String, param2:String) : uint
      {
         var _loc3_:uint = 0;
         var _loc5_:uint = 0;
         var _loc8_:uint = 0;
         var _loc9_:String = null;
         var _loc10_:String = null;
         if(param1 == null)
         {
            param1 = "";
         }
         if(param2 == null)
         {
            param2 = "";
         }
         if(param1 == param2)
         {
            return 0;
         }
         var _loc4_:Array = new Array();
         var _loc6_:uint = uint(param1.length);
         var _loc7_:uint = uint(param2.length);
         if(_loc6_ == 0)
         {
            return _loc7_;
         }
         if(_loc7_ == 0)
         {
            return _loc6_;
         }
         _loc3_ = 0;
         while(_loc3_ <= _loc6_)
         {
            _loc4_[_loc3_] = new Array();
            _loc3_++;
         }
         _loc3_ = 0;
         while(_loc3_ <= _loc6_)
         {
            _loc4_[_loc3_][0] = _loc3_;
            _loc3_++;
         }
         _loc8_ = 0;
         while(_loc8_ <= _loc7_)
         {
            _loc4_[0][_loc8_] = _loc8_;
            _loc8_++;
         }
         _loc3_ = 1;
         while(_loc3_ <= _loc6_)
         {
            _loc9_ = param1.charAt(_loc3_ - 1);
            _loc8_ = 1;
            while(_loc8_ <= _loc7_)
            {
               _loc10_ = param2.charAt(_loc8_ - 1);
               if(_loc9_ == _loc10_)
               {
                  _loc5_ = 0;
               }
               else
               {
                  _loc5_ = 1;
               }
               _loc4_[_loc3_][_loc8_] = method_944(_loc4_[_loc3_ - 1][_loc8_] + 1,_loc4_[_loc3_][_loc8_ - 1] + 1,_loc4_[_loc3_ - 1][_loc8_ - 1] + _loc5_);
               _loc8_++;
            }
            _loc3_++;
         }
         return _loc4_[_loc6_][_loc7_];
      }
      
      public static function method_2116(param1:String, param2:String) : Boolean
      {
         var _loc3_:int = param1.length - param2.length;
         return param1.lastIndexOf(param2) == _loc3_ && _loc3_ > 0;
      }
      
      public static function method_2033(param1:String) : Boolean
      {
         var _loc2_:String = method_898(param1);
         return !!_loc2_.length;
      }
      
      public static function method_2048(param1:String) : Boolean
      {
         if(param1 == null)
         {
            return true;
         }
         return !param1.length;
      }
      
      public static function method_2057(param1:String) : Boolean
      {
         if(param1 == null)
         {
            return false;
         }
         var _loc2_:RegExp = /^[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$/;
         return _loc2_.test(param1);
      }
      
      public static function method_2013(param1:String, param2:String, param3:uint) : String
      {
         var _loc4_:String = param1;
         while(_loc4_.length < param3)
         {
            _loc4_ = param2 + _loc4_;
         }
         return _loc4_;
      }
      
      public static function method_2126(param1:String, param2:String, param3:uint) : String
      {
         var _loc4_:String = param1;
         while(_loc4_.length < param3)
         {
            _loc4_ += param2;
         }
         return _loc4_;
      }
      
      public static function method_2014(param1:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         var _loc2_:String = param1.toLowerCase().replace(/\b([^.?;!]+)/,method_1440);
         return _loc2_.replace(/\b[i]\b/,"I");
      }
      
      public static function method_2083(param1:String) : String
      {
         var _loc2_:RegExp = /[\\"\r\n]/g;
         return "\"" + param1.replace(_loc2_,method_1269) + "\"";
      }
      
      public static function method_925(param1:String, param2:String, param3:Boolean = true) : String
      {
         if(param1 == null)
         {
            return "";
         }
         var _loc4_:String = method_212(param2);
         var _loc5_:String = !param3 ? "ig" : "g";
         return param1.replace(new RegExp(_loc4_,_loc5_),"");
      }
      
      public static function method_898(param1:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         var _loc2_:String = method_80(param1);
         return _loc2_.replace(/\s+/g," ");
      }
      
      public static function reverse(param1:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         return param1.split("").reverse().join("");
      }
      
      public static function method_2005(param1:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         return param1.split(/\s+/).reverse().join("");
      }
      
      public static function method_2067(param1:String, param2:String) : Number
      {
         var _loc3_:uint = method_673(param1,param2);
         var _loc4_:uint;
         if((_loc4_ = Math.max(param1.length,param2.length)) == 0)
         {
            return 100;
         }
         return (1 - _loc3_ / _loc4_) * 100;
      }
      
      public static function method_2038(param1:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         return param1.replace(/<\/?[^>]+>/igm,"");
      }
      
      public static function method_2087(param1:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         return param1.replace(/(\w)/,method_1087);
      }
      
      public static function method_80(param1:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         return param1.replace(/^\s+|\s+$/g,"");
      }
      
      public static function method_700(param1:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         return param1.replace(/^\s+/,"");
      }
      
      public static function method_832(param1:String) : String
      {
         if(param1 == null)
         {
            return "";
         }
         return param1.replace(/\s+$/,"");
      }
      
      public static function method_2100(param1:String) : uint
      {
         if(param1 == null)
         {
            return 0;
         }
         return param1.match(/\b\w+\b/g).length;
      }
      
      public static function method_597(param1:String, param2:uint, param3:String = "...") : String
      {
         if(param1 == null)
         {
            return "";
         }
         param2 -= param3.length;
         var _loc4_:String;
         if((_loc4_ = param1).length > param2)
         {
            _loc4_ = _loc4_.substr(0,param2);
            if(/[^\s]/.test(param1.charAt(param2)))
            {
               _loc4_ = method_832(_loc4_.replace(/\w+$|\s+$/,""));
            }
            _loc4_ += param3;
         }
         return _loc4_;
      }
      
      private static function method_212(param1:String) : String
      {
         return param1.replace(/(\]|\[|\{|\}|\(|\)|\*|\+|\?|\.|\\)/g,"\\$1");
      }
      
      private static function method_944(param1:uint, param2:uint, param3:uint) : uint
      {
         return Math.min(param1,Math.min(param2,Math.min(param3,param1)));
      }
      
      private static function method_1269(param1:String, ... rest) : String
      {
         switch(param1)
         {
            case "\\":
               return "\\\\";
            case "\r":
               return "\\r";
            case "\n":
               return "\\n";
            case "\"":
               return "\\\"";
            default:
               return "";
         }
      }
      
      private static function method_732(param1:String, ... rest) : String
      {
         return param1.toUpperCase();
      }
      
      private static function method_1087(param1:String, ... rest) : String
      {
         var _loc3_:String = param1.toLowerCase();
         var _loc4_:String = param1.toUpperCase();
         switch(param1)
         {
            case _loc3_:
               return _loc4_;
            case _loc4_:
               return _loc3_;
            default:
               return param1;
         }
      }
   }
}
