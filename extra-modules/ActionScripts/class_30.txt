package
{
   import flash.display.MovieClip;
   import flash.utils.Dictionary;
   
   public class class_30
   {
       
      
      internal var var_858:String;
      
      internal var var_831:String;
      
      internal var var_69:Dictionary;
      
      internal var var_1996:uint;
      
      public function class_30(param1:String, param2:String)
      {
         super();
         this.var_858 = param1;
         this.var_831 = param2;
         this.var_69 = new Dictionary();
      }
      
      public function method_2085() : void
      {
         var _loc1_:String = null;
         var _loc2_:class_26 = null;
         for(_loc1_ in this.var_69)
         {
            _loc2_ = this.var_69[_loc1_];
            _loc2_.method_892();
            delete this.var_69[_loc1_];
         }
         this.var_69 = null;
      }
      
      public function method_856(param1:String, param2:MovieClip, param3:uint, param4:uint, param5:uint, param6:uint, param7:uint, param8:Vector.<uint>, param9:String) : void
      {
         var _loc15_:int = 0;
         var _loc16_:int = 0;
         var _loc17_:int = 0;
         var _loc18_:uint = 0;
         var _loc19_:uint = 0;
         var _loc20_:String = null;
         var _loc21_:class_26 = null;
         var _loc22_:String = null;
         var _loc23_:Number = NaN;
         var _loc10_:Boolean = true;
         if(!param1)
         {
            param3 = 1;
            param1 = "Ready";
            _loc10_ = false;
         }
         var _loc11_:Boolean = false;
         if(param9)
         {
            _loc15_ = param9.length;
            _loc16_ = param1.lastIndexOf(param9);
            _loc17_ = param1.length;
            if(_loc16_ >= 0 && _loc16_ == _loc17_ - _loc15_)
            {
               _loc11_ = true;
               param1 = param1.substr(0,_loc17_ - _loc15_);
            }
         }
         var _loc12_:class_26;
         if(_loc12_ = this.var_69[param1])
         {
            if(!_loc11_)
            {
               class_24.method_19("Duplicate move found for: " + param1 + " in file: " + this.var_831 + "/" + this.var_858);
               return;
            }
            _loc12_.method_892();
         }
         if(!param4)
         {
            param4 = uint(param2.totalFrames + 1);
            if(_loc10_)
            {
               class_24.method_19("End Missing for: " + param1 + " in file: " + this.var_831 + "/" + this.var_858);
            }
         }
         if(!param5)
         {
            param5 = param3;
            if(_loc10_)
            {
               class_24.method_19("Loop Missing for: " + param1 + " in file: " + this.var_831 + "/" + this.var_858);
            }
         }
         if(param5 == param4)
         {
            param4 += 1;
            class_24.method_19("Loop Invalid for: " + param1 + " in file: " + this.var_831 + "/" + this.var_858);
         }
         if(!param6)
         {
            param6 = param4;
            if(_loc10_)
            {
               class_24.method_19("Recover Missing for: " + param1 + " in file: " + this.var_831 + "/" + this.var_858);
            }
         }
         if(param6 <= param5)
         {
            param6 = uint(param5 + 1);
            class_24.method_19("Recover Early for: " + param1 + " in file: " + this.var_831 + "/" + this.var_858);
         }
         if(!param7)
         {
            param7 = param4;
            if(_loc10_)
            {
               class_24.method_19("Free Missing for: " + param1 + " in file: " + this.var_831 + "/" + this.var_858);
            }
         }
         if(param8)
         {
            _loc18_ = param8.length;
            while(_loc19_ < _loc18_)
            {
               param8[_loc19_] -= param3;
               _loc19_++;
            }
         }
         var _loc13_:class_26 = new class_26(param1,this.var_1996,param2,param3,param4 - param3,param5 - param3,param6 - param3,param7 - param3,param8);
         this.var_69[param1] = _loc13_;
         ++this.var_1996;
         var _loc14_:int;
         if((_loc14_ = param1.indexOf("%")) != -1)
         {
            _loc20_ = param1.substr(0,_loc14_);
            if(!(_loc21_ = this.var_69[_loc20_]))
            {
               class_24.method_19("The Move " + param1 + " has no root animation: " + _loc20_);
            }
            else
            {
               _loc22_ = param1.substr(_loc14_ + 1);
               if((_loc23_ = Number(_loc22_) / 100) <= 0 || _loc23_ >= 1)
               {
                  class_24.method_19("The Move " + param1 + " has a flawed chance: " + _loc23_);
                  _loc23_ = 0;
               }
               if(!_loc21_.var_1077)
               {
                  _loc21_.var_1077 = new Vector.<class_26>();
               }
               _loc21_.var_1077.push(_loc13_);
               _loc13_.var_153 = _loc21_;
               _loc13_.var_2482 = _loc23_;
            }
         }
      }
   }
}
