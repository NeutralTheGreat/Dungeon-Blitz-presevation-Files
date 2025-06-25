package
{
   import flash.utils.ByteArray;
   
   public class BitStream
   {
      
      public static const sBitMask:Vector.<uint> = Vector.<uint>([0,1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535,131071,262143,524287,1048575,2097151,4194303,8388607,16777215,33554431,67108863,134217727,268435455,536870911,1073741823,2147483647,4294967295]);
       
      
      internal var var_359:ByteArray;
      
      internal var var_808:uint = 0;
      
      internal var var_677:uint = 0;
      
      public function BitStream(param1:ByteArray = null)
      {
         super();
         this.var_359 = !!param1 ? param1 : new ByteArray();
      }
      
      public function method_685() : uint
      {
         return this.var_677 + 7 >>> 3;
      }
      
      public function method_65(param1:uint, param2:uint) : void
      {
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         while(param1)
         {
            _loc3_ = uint(this.var_677 >>> 3);
            _loc4_ = uint(this.var_677 & 7);
            _loc5_ = uint(8 - _loc4_);
            _loc6_ = param1 < _loc5_ ? param1 : _loc5_;
            _loc7_ = uint((param2 & sBitMask[param1]) >>> param1 - _loc6_);
            this.var_359[_loc3_] |= _loc7_ << _loc5_ - _loc6_;
            param1 -= _loc6_;
            this.var_677 += _loc6_;
         }
      }
      
      public function method_76(param1:uint) : uint
      {
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         while(param1)
         {
            _loc2_ = uint(this.var_808 >>> 3);
            _loc3_ = uint(this.var_808 & 7);
            _loc4_ = uint(8 - _loc3_);
            _loc5_ = param1 < _loc4_ ? param1 : _loc4_;
            _loc6_ = uint((this.var_359[_loc2_] & sBitMask[_loc4_]) >>> _loc4_ - _loc5_);
            _loc7_ |= _loc6_ << param1 - _loc5_;
            param1 -= _loc5_;
            this.var_808 += _loc5_;
         }
         return _loc7_;
      }
      
      public function method_344(param1:ByteArray) : void
      {
         var _loc2_:uint = 0;
         var _loc7_:uint = 0;
         var _loc3_:uint = param1.length;
         var _loc4_:uint = uint(_loc3_ << 3);
         var _loc5_:uint = uint(this.var_677 >>> 3);
         var _loc6_:uint;
         if(!(_loc6_ = uint(this.var_677 & 7)))
         {
            _loc2_ = 0;
            while(_loc2_ < _loc3_)
            {
               var _loc8_:*;
               this.var_359[_loc8_ = _loc5_++] = param1[_loc2_];
               _loc2_++;
            }
         }
         else
         {
            _loc7_ = uint(8 - _loc6_);
            _loc2_ = 0;
            while(_loc2_ < _loc3_)
            {
               this.var_359[_loc8_ = _loc5_++] = this.var_359[_loc8_] | param1[_loc2_] >>> _loc6_;
               this.var_359[_loc5_] |= param1[_loc2_] << _loc7_;
               _loc2_++;
            }
         }
         this.var_677 += _loc4_;
      }
      
      public function method_387(param1:uint) : ByteArray
      {
         var _loc3_:uint = 0;
         var _loc7_:uint = 0;
         var _loc2_:ByteArray = new ByteArray();
         var _loc4_:uint = uint(param1 << 3);
         var _loc5_:uint = uint(this.var_808 >>> 3);
         var _loc6_:uint;
         if(!(_loc6_ = uint(this.var_808 & 7)))
         {
            _loc3_ = 0;
            while(_loc3_ < param1)
            {
               _loc2_[_loc3_] = this.var_359[_loc5_++];
               _loc3_++;
            }
         }
         else
         {
            _loc7_ = uint(8 - _loc6_);
            _loc3_ = 0;
            while(_loc3_ < param1)
            {
               _loc2_[_loc3_] = this.var_359[_loc5_++] << _loc6_;
               _loc2_[_loc3_] |= this.var_359[_loc5_] >>> _loc7_;
               _loc3_++;
            }
         }
         this.var_808 += _loc4_;
         return _loc2_;
      }
      
      public function method_1327(param1:String) : void
      {
         this.method_65(8,param1.charCodeAt(0));
      }
      
      public function method_1576(param1:uint) : void
      {
         this.method_65(8,param1);
      }
      
      public function method_1436(param1:uint) : void
      {
         var _loc2_:ByteArray = new ByteArray();
         _loc2_.writeShort(param1);
         this.method_344(_loc2_);
      }
      
      public function method_2017(param1:uint) : void
      {
         var _loc2_:ByteArray = new ByteArray();
         _loc2_.writeInt(param1);
         this.method_344(_loc2_);
      }
      
      public function method_1214(param1:Number) : void
      {
         var _loc2_:ByteArray = new ByteArray();
         _loc2_.writeFloat(param1);
         this.method_344(_loc2_);
      }
      
      public function method_1250(param1:String) : void
      {
         var _loc2_:ByteArray = new ByteArray();
         _loc2_.writeUTFBytes(param1);
         var _loc3_:uint = _loc2_.length;
         if(_loc3_ > 65535)
         {
            _loc3_ = 65535;
         }
         this.method_1436(_loc3_);
         this.method_344(_loc2_);
      }
      
      public function method_1281() : String
      {
         return String.fromCharCode(this.method_76(8));
      }
      
      public function method_1414() : uint
      {
         return this.method_76(8);
      }
      
      public function method_1194() : uint
      {
         var _loc1_:ByteArray = this.method_387(2);
         return _loc1_.readShort();
      }
      
      public function method_2125() : uint
      {
         var _loc1_:ByteArray = this.method_387(4);
         return _loc1_.readInt();
      }
      
      public function method_1068() : Number
      {
         var _loc1_:ByteArray = this.method_387(4);
         return _loc1_.readFloat();
      }
      
      public function method_1527() : String
      {
         var _loc1_:uint = this.method_1194();
         var _loc2_:ByteArray = this.method_387(_loc1_);
         return _loc2_.readUTFBytes(_loc1_);
      }
   }
}
