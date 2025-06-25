package
{
   public class class_87
   {
       
      
      internal var var_1:Game;
      
      internal var mPetType:class_7;
      
      internal var var_23:uint;
      
      internal var var_110:uint;
      
      internal var var_670:uint;
      
      internal var var_1693:PowerType;
      
      public function class_87(param1:Game, param2:class_7, param3:uint, param4:uint, param5:uint)
      {
         super();
         this.var_1 = param1;
         this.mPetType = param2;
         this.var_23 = param3;
         this.var_110 = param4;
         this.var_670 = param5;
         this.var_1693 = class_14.powerTypesDict[this.mPetType.var_1138];
      }
      
      public function method_1460() : void
      {
         this.mPetType = null;
         this.var_1 = null;
         this.var_1693 = null;
      }
      
      public function method_518(param1:Boolean) : String
      {
         var _loc3_:* = null;
         var _loc2_:Number = 1;
         if(!param1)
         {
            _loc2_ = 1;
         }
         if(this.mPetType.var_2296)
         {
            _loc3_ = "+" + Math.round(this.method_423() * 100 * _loc2_) + "% Gold Find";
         }
         if(this.mPetType.var_2234)
         {
            _loc3_ = "+" + Math.round(this.method_493() * 100 * _loc2_) + "% Gear Find";
         }
         if(this.mPetType.var_2178)
         {
            _loc3_ = "+" + Math.round(this.method_443() * 100 * _loc2_) + "% Exp Bonus";
         }
         if(this.mPetType.var_2421)
         {
            _loc3_ = "+" + Math.round(this.method_427() * 100 * _loc2_) + "% Material Find";
         }
         return _loc3_;
      }
      
      public function method_938(param1:Boolean) : String
      {
         var _loc3_:* = null;
         var _loc2_:Number = 1;
         if(!param1)
         {
            _loc2_ = 1;
         }
         if(this.mPetType.var_2394)
         {
            _loc3_ = "+" + Math.round(this.method_792() * 100 * _loc2_) + "% XP Find";
         }
         if(this.mPetType.var_1698)
         {
            _loc3_ = "+" + Math.round(this.method_598() * 100 * _loc2_) + "% Gear Find";
         }
         if(this.mPetType.var_2057)
         {
            _loc3_ = "+" + Math.round(this.method_826() * 100 * _loc2_) + "% Material Find";
         }
         if(this.mPetType.var_1977)
         {
            _loc3_ = "+" + Math.round(this.method_697() * 100 * _loc2_) + "% Gold Find";
         }
         return _loc3_;
      }
      
      public function method_443() : Number
      {
         if(this.mPetType.var_2178)
         {
            return this.method_150(this.var_23);
         }
         return 0;
      }
      
      public function method_493() : Number
      {
         if(this.mPetType.var_2234)
         {
            return this.method_150(this.var_23);
         }
         return 0;
      }
      
      public function method_427() : Number
      {
         if(this.mPetType.var_2421)
         {
            return this.method_150(this.var_23);
         }
         return 0;
      }
      
      public function method_423() : Number
      {
         if(this.mPetType.var_2296)
         {
            return this.method_150(this.var_23);
         }
         return 0;
      }
      
      public function method_792() : Number
      {
         if(this.mPetType.var_2394)
         {
            return this.method_150(this.var_23);
         }
         return this.method_443();
      }
      
      public function method_598() : Number
      {
         if(this.mPetType.var_1698)
         {
            return this.method_150(this.var_23);
         }
         return this.method_493();
      }
      
      public function method_826() : Number
      {
         if(this.mPetType.var_2057)
         {
            return this.method_150(this.var_23);
         }
         return this.method_427();
      }
      
      public function method_697() : Number
      {
         if(this.mPetType.var_1977)
         {
            return this.method_150(this.var_23);
         }
         return this.method_423();
      }
      
      public function method_150(param1:uint) : Number
      {
         if(this.var_23 == class_7.const_35)
         {
            return class_7.const_661 + this.var_23 / 100;
         }
         return class_7.const_661 + (this.var_23 - 1) / 100;
      }
      
      public function method_324() : Number
      {
         var _loc1_:uint = class_7.method_154(this.var_23);
         var _loc2_:uint = class_7.method_154(this.var_23 - 1);
         var _loc3_:uint = uint(_loc1_ - _loc2_);
         return (this.var_110 - _loc2_) / _loc3_;
      }
      
      public function method_1533() : Boolean
      {
         if(this.var_23 >= class_7.const_35)
         {
            return false;
         }
         return true;
      }
   }
}
