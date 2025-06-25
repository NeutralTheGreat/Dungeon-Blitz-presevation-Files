package
{
   import flash.utils.ByteArray;
   
   public class Crypto
   {
      
      public static const const_117:Array = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"];
      
      private static const kSHA256:Array = [];
      
      private static const const_325:Array = [];
      
      private static const MD5_SHIFT_COUNT:Array = [];
      
      private static const const_991:Array = [24,16,8,0];
      
      private static const const_1013:Array = [0,8,16,24];
       
      
      public function Crypto()
      {
         super();
      }
      
      private static function method_55(param1:uint, param2:uint) : uint
      {
         return param1 << 32 - param2 | param1 >>> param2;
      }
      
      private static function method_148(param1:uint, param2:uint) : uint
      {
         return param1 << param2 | param1 >>> 32 - param2;
      }
      
      private static function method_360(param1:String, param2:Boolean) : Array
      {
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc8_:Array = null;
         if(param2)
         {
            _loc6_ = 0;
            _loc7_ = 1;
            _loc8_ = const_1013;
         }
         else
         {
            _loc6_ = 1;
            _loc7_ = 0;
            _loc8_ = const_991;
         }
         var _loc9_:uint = 0;
         var _loc10_:uint;
         var _loc11_:uint = uint((_loc10_ = uint(param1.length)) + 1);
         var _loc12_:Array = new Array();
         param1 += String.fromCharCode(128);
         while(_loc9_ < _loc11_)
         {
            _loc5_ = uint(param1.charCodeAt(_loc9_) & 255);
            _loc4_ = uint(_loc8_[_loc9_ & 3]);
            _loc3_ = uint(_loc9_ >>> 2);
            _loc12_[_loc3_] |= _loc5_ << _loc4_;
            _loc9_++;
         }
         var _loc13_:uint = uint((_loc9_ + 7 & ~63) + 56 >>> 2);
         _loc3_ += 1;
         while(_loc3_ < _loc13_)
         {
            _loc12_[_loc3_] = 0;
            _loc3_++;
         }
         _loc12_[_loc13_ + _loc6_] = _loc10_ << 3;
         _loc12_[_loc13_ + _loc7_] = _loc10_ >> 29;
         return _loc12_;
      }
      
      public static function method_164(param1:String) : String
      {
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         var _loc16_:Array = null;
         var _loc17_:uint = 0;
         var _loc18_:uint = 0;
         var _loc19_:uint = 0;
         var _loc20_:uint = 0;
         var _loc21_:uint = 0;
         var _loc22_:uint = 0;
         var _loc23_:uint = 0;
         var _loc24_:uint = 0;
         var _loc25_:uint = 0;
         var _loc26_:uint = 0;
         var _loc27_:uint = 0;
         var _loc28_:uint = 0;
         var _loc29_:uint = 0;
         var _loc30_:uint = 0;
         var _loc31_:uint = 0;
         var _loc32_:uint = 0;
         var _loc33_:String = null;
         var _loc34_:uint = 0;
         var _loc4_:uint = 1779033703;
         var _loc5_:uint = 3144134277;
         var _loc6_:uint = 1013904242;
         var _loc7_:uint = 2773480762;
         var _loc8_:uint = 1359893119;
         var _loc9_:uint = 2600822924;
         var _loc10_:uint = 528734635;
         var _loc11_:uint = 1541459225;
         var _loc12_:Array;
         var _loc13_:uint = (_loc12_ = method_360(param1,false)).length;
         _loc2_ = 0;
         while(_loc2_ < _loc13_)
         {
            _loc16_ = new Array();
            _loc3_ = 0;
            while(_loc3_ < 16)
            {
               _loc16_[_loc3_] = _loc12_[_loc2_ + _loc3_];
               _loc3_++;
            }
            _loc3_ = 16;
            while(_loc3_ < 64)
            {
               _loc25_ = uint(method_55(_loc16_[_loc3_ - 15],7) ^ method_55(_loc16_[_loc3_ - 15],18) ^ _loc16_[_loc3_ - 15] >>> 3);
               _loc26_ = uint(method_55(_loc16_[_loc3_ - 2],17) ^ method_55(_loc16_[_loc3_ - 2],19) ^ _loc16_[_loc3_ - 2] >>> 10);
               _loc16_[_loc3_] = _loc16_[_loc3_ - 16] + _loc25_ + _loc16_[_loc3_ - 7] + _loc26_;
               _loc3_++;
            }
            _loc17_ = _loc4_;
            _loc18_ = _loc5_;
            _loc19_ = _loc6_;
            _loc20_ = _loc7_;
            _loc21_ = _loc8_;
            _loc22_ = _loc9_;
            _loc23_ = _loc10_;
            _loc24_ = _loc11_;
            _loc3_ = 0;
            while(_loc3_ < 64)
            {
               _loc27_ = uint(method_55(_loc17_,2) ^ method_55(_loc17_,13) ^ method_55(_loc17_,22));
               _loc28_ = uint(_loc17_ & _loc18_ ^ _loc17_ & _loc19_ ^ _loc18_ & _loc19_);
               _loc29_ = _loc27_ + _loc28_;
               _loc30_ = uint(method_55(_loc21_,6) ^ method_55(_loc21_,11) ^ method_55(_loc21_,25));
               _loc31_ = uint(_loc21_ & _loc22_ ^ ~_loc21_ & _loc23_);
               _loc32_ = _loc24_ + _loc30_ + _loc31_ + kSHA256[_loc3_] + _loc16_[_loc3_];
               _loc24_ = _loc23_;
               _loc23_ = _loc22_;
               _loc22_ = _loc21_;
               _loc21_ = _loc20_ + _loc32_;
               _loc20_ = _loc19_;
               _loc19_ = _loc18_;
               _loc18_ = _loc17_;
               _loc17_ = _loc32_ + _loc29_;
               _loc3_++;
            }
            _loc4_ += _loc17_;
            _loc5_ += _loc18_;
            _loc6_ += _loc19_;
            _loc7_ += _loc20_;
            _loc8_ += _loc21_;
            _loc9_ += _loc22_;
            _loc10_ += _loc23_;
            _loc11_ += _loc24_;
            _loc2_ += 16;
         }
         var _loc14_:* = "";
         var _loc15_:Array = [_loc4_.toString(16),_loc5_.toString(16),_loc6_.toString(16),_loc7_.toString(16),_loc8_.toString(16),_loc9_.toString(16),_loc10_.toString(16),_loc11_.toString(16)];
         _loc2_ = 0;
         while(_loc2_ < 8)
         {
            _loc33_ = String(_loc15_[_loc2_]);
            _loc34_ = uint(8 - _loc33_.length);
            _loc3_ = 0;
            while(_loc3_ < _loc34_)
            {
               _loc14_ += "0";
               _loc3_++;
            }
            _loc14_ += _loc33_;
            _loc2_++;
         }
         return _loc14_;
      }
      
      public static function MD5(param1:String) : String
      {
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc15_:uint = 0;
         var _loc16_:uint = 0;
         var _loc17_:uint = 0;
         var _loc18_:uint = 0;
         var _loc19_:String = null;
         var _loc20_:uint = 0;
         var _loc7_:uint = 1732584193;
         var _loc8_:uint = 4023233417;
         var _loc9_:uint = 2562383102;
         var _loc10_:uint = 271733878;
         var _loc11_:Array;
         var _loc12_:uint = (_loc11_ = method_360(param1,true)).length;
         _loc2_ = 0;
         while(_loc2_ < _loc12_)
         {
            _loc15_ = _loc7_;
            _loc16_ = _loc8_;
            _loc17_ = _loc9_;
            _loc18_ = _loc10_;
            _loc3_ = 0;
            while(_loc3_ < 16)
            {
               _loc4_ = uint(_loc16_ & _loc17_ | ~_loc16_ & _loc18_);
               _loc5_ = _loc3_;
               _loc6_ = _loc18_;
               _loc18_ = _loc17_;
               _loc17_ = _loc16_;
               _loc16_ += method_148(_loc15_ + _loc4_ + const_325[_loc3_] + _loc11_[_loc5_ + _loc2_],MD5_SHIFT_COUNT[_loc3_]);
               _loc15_ = _loc6_;
               _loc3_++;
            }
            _loc3_ = 16;
            while(_loc3_ < 32)
            {
               _loc4_ = uint(_loc18_ & _loc16_ | ~_loc18_ & _loc17_);
               _loc5_ = uint(5 * _loc3_ + 1 & 15);
               _loc6_ = _loc18_;
               _loc18_ = _loc17_;
               _loc17_ = _loc16_;
               _loc16_ += method_148(_loc15_ + _loc4_ + const_325[_loc3_] + _loc11_[_loc5_ + _loc2_],MD5_SHIFT_COUNT[_loc3_]);
               _loc15_ = _loc6_;
               _loc3_++;
            }
            _loc3_ = 32;
            while(_loc3_ < 48)
            {
               _loc4_ = uint(_loc16_ ^ _loc17_ ^ _loc18_);
               _loc5_ = uint(3 * _loc3_ + 5 & 15);
               _loc6_ = _loc18_;
               _loc18_ = _loc17_;
               _loc17_ = _loc16_;
               _loc16_ += method_148(_loc15_ + _loc4_ + const_325[_loc3_] + _loc11_[_loc5_ + _loc2_],MD5_SHIFT_COUNT[_loc3_]);
               _loc15_ = _loc6_;
               _loc3_++;
            }
            _loc3_ = 48;
            while(_loc3_ < 64)
            {
               _loc4_ = uint(_loc17_ ^ (_loc16_ | ~_loc18_));
               _loc5_ = uint(7 * _loc3_ & 15);
               _loc6_ = _loc18_;
               _loc18_ = _loc17_;
               _loc17_ = _loc16_;
               _loc16_ += method_148(_loc15_ + _loc4_ + const_325[_loc3_] + _loc11_[_loc5_ + _loc2_],MD5_SHIFT_COUNT[_loc3_]);
               _loc15_ = _loc6_;
               _loc3_++;
            }
            _loc7_ += _loc15_;
            _loc8_ += _loc16_;
            _loc9_ += _loc17_;
            _loc10_ += _loc18_;
            _loc2_ += 16;
         }
         var _loc13_:String = "";
         var _loc14_:Array = [_loc7_.toString(16),_loc8_.toString(16),_loc9_.toString(16),_loc10_.toString(16)];
         _loc2_ = 0;
         while(_loc2_ < 4)
         {
            _loc19_ = String(_loc14_[_loc2_]);
            _loc20_ = uint(8 - _loc19_.length);
            _loc3_ = 0;
            while(_loc3_ < _loc20_)
            {
               _loc19_ = "0" + _loc19_;
               _loc3_++;
            }
            _loc13_ += _loc19_.substr(6,2) + _loc19_.substr(4,2) + _loc19_.substr(2,2) + _loc19_.substr(0,2);
            _loc2_++;
         }
         return _loc13_;
      }
      
      public static function method_1413(param1:ByteArray) : String
      {
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc8_:uint = 0;
         var _loc9_:uint = 0;
         var _loc2_:String = "";
         var _loc10_:uint;
         var _loc11_:uint = (_loc10_ = param1.length) / 3;
         _loc4_ = 0;
         while(_loc4_ < _loc11_)
         {
            _loc3_ = uint(param1[_loc5_] << 16);
            _loc3_ += param1[_loc5_ + 1] << 8;
            _loc3_ += param1[_loc5_ + 2];
            _loc6_ = uint(_loc3_ >> 18 & 63);
            _loc7_ = uint(_loc3_ >> 12 & 63);
            _loc8_ = uint(_loc3_ >> 6 & 63);
            _loc9_ = uint(_loc3_ & 63);
            _loc2_ += const_117[_loc6_] + const_117[_loc7_] + const_117[_loc8_] + const_117[_loc9_];
            _loc4_++;
            _loc5_ += 3;
         }
         var _loc12_:uint;
         if((_loc12_ = _loc10_ - _loc11_ * 3) == 2)
         {
            _loc3_ = uint(param1[_loc5_] << 16);
            _loc3_ += param1[_loc5_ + 1] << 8;
            _loc6_ = uint(_loc3_ >> 18 & 255);
            _loc7_ = uint(_loc3_ >> 12 & 255);
            _loc8_ = uint(_loc3_ >> 6 & 255);
            _loc2_ += const_117[_loc6_] + const_117[_loc7_] + const_117[_loc8_] + "=";
         }
         else if(_loc12_ == 1)
         {
            _loc3_ = uint(param1[_loc5_] << 16);
            _loc6_ = uint(_loc3_ >> 18 & 255);
            _loc7_ = uint(_loc3_ >> 12 & 255);
            _loc2_ += const_117[_loc6_] + const_117[_loc7_] + "==";
         }
         return _loc2_;
      }
   }
}
