package
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.geom.Matrix;
   import flash.geom.Point;
   import flash.geom.Transform;
   import flash.utils.getQualifiedClassName;
   
   public class class_26
   {
      
      private static const const_1086:uint = 5;
       
      
      internal var var_1802:String;
      
      internal var var_153:class_26;
      
      internal var var_1077:Vector.<class_26>;
      
      internal var var_2482:Number = 0;
      
      internal var var_1859:uint;
      
      internal var var_710:uint;
      
      internal var var_751:uint;
      
      internal var var_408:uint;
      
      internal var var_2354:uint;
      
      internal var var_604:Vector.<class_28>;
      
      internal var var_1463:Vector.<uint>;
      
      internal var var_1073:MovieClip;
      
      internal var var_2175:uint;
      
      private var var_2399:Sprite;
      
      public function class_26(param1:String, param2:uint, param3:MovieClip, param4:uint, param5:uint, param6:uint, param7:uint, param8:uint, param9:Vector.<uint>, param10:class_26 = null)
      {
         super();
         this.var_1802 = param1;
         this.var_153 = this;
         this.var_1859 = param2;
         this.var_2175 = param4;
         this.var_710 = param5;
         this.var_751 = param6;
         this.var_408 = param7;
         this.var_2354 = param8;
         this.var_1073 = param3;
         this.var_2399 = new Sprite();
         this.var_2399.addChild(this.var_1073);
         this.var_604 = new Vector.<class_28>(param5,true);
         if(param9)
         {
            this.var_1463 = param9;
            this.var_1463.fixed = true;
         }
      }
      
      private static function method_326(param1:MovieClip, param2:uint) : class_28
      {
         var _loc3_:MovieClip = null;
         var _loc4_:String = null;
         var _loc5_:uint = 0;
         var _loc6_:Transform = null;
         var _loc7_:class_25 = null;
         var _loc8_:int = 0;
         var _loc10_:Matrix = null;
         var _loc11_:MovieClip = null;
         var _loc12_:Matrix = null;
         var _loc13_:String = null;
         var _loc14_:Array = null;
         var _loc15_:class_28 = null;
         var _loc18_:int = 0;
         var _loc20_:Point = null;
         var _loc16_:class_28 = new class_28(param2);
         var _loc17_:Vector.<class_25> = new Vector.<class_25>();
         var _loc19_:int = param1.numChildren;
         _loc18_ = 0;
         for(; _loc18_ < _loc19_; _loc18_++)
         {
            _loc3_ = param1.getChildAt(_loc18_) as MovieClip;
            if(_loc3_)
            {
               if((_loc4_ = getQualifiedClassName(_loc3_)) == "a_FireSocket")
               {
                  _loc3_.visible = false;
                  _loc16_.var_2381 = new Point(_loc3_.x,_loc3_.y);
               }
               else if(_loc4_ == "a_PowerSocket")
               {
                  _loc3_.visible = false;
                  _loc10_ = _loc3_.transform.matrix;
                  if(_loc11_ = _loc3_["am_Scalinator"])
                  {
                     (_loc12_ = _loc11_.transform.matrix).concat(_loc10_);
                     _loc10_ = _loc12_;
                  }
                  _loc16_.var_1807 = new Point(_loc10_.tx,_loc10_.ty);
               }
               else
               {
                  if(_loc4_.indexOf("a_EB_Platform") != -1)
                  {
                     _loc20_ = new Point(_loc3_.x,_loc3_.y);
                     _loc16_.var_1813 = _loc20_;
                  }
                  if(_loc4_ == "a_Cape")
                  {
                     if(_loc18_ < const_1086)
                     {
                        _loc3_.gotoAndStop(1);
                        _loc3_.visible = false;
                        _loc16_.var_2388 = _loc3_.transform.matrix;
                        continue;
                     }
                  }
                  _loc6_ = _loc3_.transform;
                  _loc7_ = new class_25(_loc4_,_loc3_.name,_loc6_.matrix,_loc3_.alpha);
                  if((_loc5_ = uint(_loc3_.totalFrames)) > 1)
                  {
                     _loc8_ = int(param2);
                     if((_loc13_ = _loc3_.name).indexOf("_") != -1)
                     {
                        _loc14_ = _loc13_.split("_");
                        _loc8_ -= int(_loc14_[2]);
                     }
                     _loc8_ = _loc8_ % _loc5_ + 1;
                     _loc3_.gotoAndStop(_loc8_);
                     _loc7_.frame = _loc8_;
                  }
                  if(_loc7_.var_2639 || _loc7_.var_1866)
                  {
                     _loc15_ = method_326(_loc3_,0);
                     _loc7_.var_1263 = _loc15_.var_900;
                     _loc15_.var_900 = new Vector.<class_25>();
                     _loc15_.method_655();
                  }
                  _loc17_.push(_loc7_);
               }
            }
         }
         _loc17_.fixed = true;
         _loc16_.var_900 = _loc17_;
         return _loc16_;
      }
      
      public function method_892() : void
      {
         var _loc1_:class_28 = null;
         this.var_1463 = null;
         this.var_153 = null;
         this.var_1077 = null;
         this.var_2399 = null;
         this.var_1073 = null;
         for each(_loc1_ in this.var_604)
         {
            if(_loc1_)
            {
               _loc1_.method_655();
            }
         }
         this.var_604 = null;
      }
      
      public function method_242(param1:uint) : class_28
      {
         this.var_1073.gotoAndStop(this.var_2175 + param1);
         var _loc2_:class_28 = method_326(this.var_1073,param1);
         this.var_604[param1] = _loc2_;
         return _loc2_;
      }
   }
}
