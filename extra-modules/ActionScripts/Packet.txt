package
{
   import flash.utils.ByteArray;
   
   public class Packet
   {
       
      
      internal var type:int;
      
      internal var var_50:BitStream;
      
      public function Packet(param1:int, param2:ByteArray = null)
      {
         super();
         this.type = param1;
         this.var_50 = new BitStream(param2);
      }
      
      public static function method_361(param1:uint) : uint
      {
         var _loc2_:uint = 0;
         while(param1)
         {
            param1 >>>= 1;
            _loc2_++;
         }
         return !!_loc2_ ? _loc2_ : 1;
      }
      
      public function method_2136() : uint
      {
         return this.var_50.method_685();
      }
      
      public function method_11() : Boolean
      {
         return !!this.var_50.method_76(1);
      }
      
      public function method_2039() : String
      {
         return this.var_50.method_1281();
      }
      
      public function method_393() : uint
      {
         return this.var_50.method_1414();
      }
      
      public function method_739() : int
      {
         if(this.var_50.method_76(1))
         {
            return -this.method_91();
         }
         return this.method_91();
      }
      
      public function method_45() : int
      {
         if(this.var_50.method_76(1))
         {
            return -this.method_4();
         }
         return this.method_4();
      }
      
      public function method_91() : uint
      {
         var _loc1_:uint = this.var_50.method_76(3);
         var _loc2_:uint = uint(_loc1_ + 1 << 1);
         return this.var_50.method_76(_loc2_);
      }
      
      public function method_4() : uint
      {
         var _loc1_:uint = this.var_50.method_76(4);
         var _loc2_:uint = uint(_loc1_ + 1 << 1);
         return this.var_50.method_76(_loc2_);
      }
      
      public function ReceiveUnsignedInt64() : String
      {
         var _loc1_:uint = this.var_50.method_76(5);
         var _loc2_:uint = uint(_loc1_ + 1 << 1);
         var _loc3_:* = _loc2_.toString() + ":";
         if(_loc2_ <= 32)
         {
            _loc3_ += "0:" + this.var_50.method_76(_loc2_).toString();
         }
         else
         {
            _loc3_ += this.var_50.method_76(_loc2_ - 32).toString() + ":";
            _loc3_ += this.var_50.method_76(32).toString();
         }
         return _loc3_;
      }
      
      public function method_560() : Number
      {
         return this.var_50.method_1068();
      }
      
      public function method_13() : String
      {
         return this.var_50.method_1527();
      }
      
      public function method_6(param1:uint) : uint
      {
         return this.var_50.method_76(param1);
      }
      
      public function method_15(param1:Boolean) : void
      {
         this.var_50.method_65(1,param1 ? 1 : 0);
      }
      
      public function method_2128(param1:String) : void
      {
         this.var_50.method_1327(param1);
      }
      
      public function method_1860(param1:uint) : void
      {
         this.var_50.method_1576(param1);
      }
      
      public function method_706(param1:int) : void
      {
         if(param1 < 0)
         {
            this.var_50.method_65(1,1);
            this.method_236(-param1);
         }
         else
         {
            this.var_50.method_65(1,0);
            this.method_236(param1);
         }
      }
      
      public function method_24(param1:int) : void
      {
         if(param1 < 0)
         {
            this.var_50.method_65(1,1);
            this.method_9(-param1);
         }
         else
         {
            this.var_50.method_65(1,0);
            this.method_9(param1);
         }
      }
      
      public function method_236(param1:uint) : void
      {
         var _loc2_:uint = method_361(param1);
         var _loc3_:uint = uint(_loc2_ + (_loc2_ & 1));
         var _loc4_:uint = uint((_loc3_ >>> 1) - 1);
         this.var_50.method_65(3,_loc4_);
         this.var_50.method_65(_loc3_,param1);
      }
      
      public function method_9(param1:uint) : void
      {
         var _loc2_:uint = method_361(param1);
         var _loc3_:uint = uint(_loc2_ + (_loc2_ & 1));
         var _loc4_:uint = uint((_loc3_ >>> 1) - 1);
         this.var_50.method_65(4,_loc4_);
         this.var_50.method_65(_loc3_,param1);
      }
      
      public function SendUnsignedInt64(param1:String) : void
      {
         var _loc2_:Array = param1.split(":");
         var _loc3_:uint = uint(_loc2_[0]);
         var _loc4_:uint = uint((_loc3_ >>> 1) - 1);
         var _loc5_:uint = uint(_loc2_[1]);
         var _loc6_:uint = uint(_loc2_[2]);
         this.var_50.method_65(5,_loc4_);
         if(_loc3_ <= 32)
         {
            this.var_50.method_65(_loc3_,_loc6_);
         }
         else
         {
            this.var_50.method_65(_loc3_ - 32,_loc5_);
            this.var_50.method_65(32,_loc6_);
         }
      }
      
      public function method_309(param1:Number) : void
      {
         this.var_50.method_1214(param1);
      }
      
      public function method_26(param1:String) : void
      {
         this.var_50.method_1250(!!param1 ? param1 : "");
      }
      
      public function method_20(param1:uint, param2:uint) : void
      {
         this.var_50.method_65(param1,param2);
      }
   }
}
