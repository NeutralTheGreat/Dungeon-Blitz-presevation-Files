package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.PixelSnapping;
   import flash.display.Sprite;
   import flash.display.StageQuality;
   import flash.geom.Matrix;
   import flash.geom.Rectangle;
   import flash.utils.Dictionary;
   
   public class class_23
   {
      
      private static const const_525:uint = 262144;
      
      private static var var_757:Number;
      
      private static var var_1002:Number;
      
      private static var var_1607:uint;
      
      private static var var_1425:int;
      
      private static var var_1069:uint;
      
      private static var var_2077:int;
      
      private static const const_208:class_135 = new class_135();
      
      {
         const_208.var_312 = null;
         const_208.x = -100;
         const_208.y = -100;
         const_208.var_926 = 0;
      }
      
      internal var var_1:Game;
      
      internal var var_343:Sprite;
      
      internal var var_986:Vector.<class_135>;
      
      internal var var_581:Dictionary;
      
      internal var var_1707:int;
      
      internal var var_2152:int;
      
      internal var var_1881:int;
      
      public function class_23(param1:Game)
      {
         super();
         this.var_1 = param1;
         this.var_343 = MathUtil.method_69();
         this.var_343.scaleX = 1 / this.var_1.main.var_982;
         this.var_343.scaleY = 1 / this.var_1.main.var_982;
         this.method_942();
         this.method_120();
      }
      
      public static function method_1579(param1:uint, param2:uint, param3:int, param4:uint, param5:uint) : void
      {
         var_757 = param1;
         var_1002 = param2;
         var_2077 = param5 * const_525;
         var_1069 = var_2077 / (var_757 * var_1002);
         var_1425 = param3;
         var_1607 = param4;
      }
      
      public function method_643(param1:Boolean = false) : void
      {
         var _loc3_:class_135 = null;
         var _loc4_:Bitmap = null;
         this.method_120();
         var _loc2_:uint = 0;
         while(_loc2_ < var_1069)
         {
            _loc3_ = this.var_986[_loc2_];
            (_loc4_ = _loc3_.var_312).bitmapData.dispose();
            _loc4_.bitmapData = null;
            _loc3_.var_312 = null;
            this.var_986[_loc2_] = null;
            _loc2_++;
         }
         this.var_986 = null;
         this.var_581 = null;
         if(param1)
         {
            if(Boolean(this.var_343) && Boolean(this.var_343.parent))
            {
               this.var_343.parent.removeChild(this.var_343);
            }
            this.var_343 = null;
         }
      }
      
      public function method_942() : void
      {
         var _loc1_:class_135 = null;
         var _loc2_:BitmapData = null;
         this.var_986 = new Vector.<class_135>(var_1069,true);
         this.var_1707 = Math.ceil(var_757 * this.var_1.main.var_982) + var_1425;
         this.var_2152 = Math.ceil(var_1002 * this.var_1.main.var_982) + var_1425;
         this.var_1881 = 0;
         var _loc3_:uint = 0;
         while(_loc3_ < var_1069)
         {
            _loc1_ = new class_135();
            _loc2_ = new BitmapData(this.var_1707,this.var_2152,true);
            this.var_1881 += this.var_1707 * this.var_2152;
            _loc1_.var_312 = new Bitmap(_loc2_,PixelSnapping.ALWAYS,false);
            if(this.var_1.main.var_1976)
            {
               _loc1_.var_312.smoothing = true;
               _loc1_.var_312.pixelSnapping = PixelSnapping.NEVER;
            }
            this.var_986[_loc3_] = _loc1_;
            _loc3_++;
         }
         this.var_581 = new Dictionary();
      }
      
      public function method_120() : void
      {
         var _loc2_:class_135 = null;
         this.var_581 = new Dictionary();
         var _loc1_:uint = 0;
         while(_loc1_ < var_1069)
         {
            _loc2_ = this.var_986[_loc1_];
            _loc2_.x = -100;
            _loc2_.y = -100;
            _loc2_.var_926 = 0;
            if(Boolean(_loc2_.var_312) && Boolean(_loc2_.var_312.parent))
            {
               _loc2_.var_312.parent.removeChild(_loc2_.var_312);
            }
            _loc1_++;
         }
      }
      
      public function method_1753() : void
      {
         var _loc1_:Rectangle = this.var_1.level.var_1090;
         this.var_343.x = _loc1_.x;
         this.var_343.y = _loc1_.y;
         if(this.var_1707 != var_757 * this.var_1.main.var_982 + var_1425)
         {
            this.method_643();
            this.method_942();
            this.method_120();
         }
         var _loc2_:Sprite = this.var_1.levelLayer;
         var _loc3_:Number = -(_loc2_.x / _loc2_.scaleX + _loc1_.x);
         var _loc4_:Number = -(_loc2_.y / _loc2_.scaleY + _loc1_.y);
         var _loc5_:int = Math.floor(_loc3_ / (var_757 * 0.5));
         var _loc6_:int = Math.floor(_loc4_ / var_1002);
         var _loc7_:uint = 0;
         while(_loc7_ < var_1607)
         {
            this.method_287(_loc5_ + _loc7_,_loc6_,_loc5_,_loc6_);
            this.method_287(_loc5_ + _loc7_,_loc6_ + 1,_loc5_,_loc6_);
            _loc7_++;
         }
         if((_loc5_ + _loc6_) % 2)
         {
            this.method_287(_loc5_ + var_1607,_loc6_ + 1,_loc5_,_loc6_);
         }
         else
         {
            this.method_287(_loc5_ + var_1607,_loc6_,_loc5_,_loc6_);
         }
      }
      
      public function method_287(param1:int, param2:int, param3:int, param4:int) : void
      {
         var _loc9_:Bitmap = null;
         var _loc10_:Number = NaN;
         var _loc11_:Number = NaN;
         var _loc12_:Rectangle = null;
         var _loc13_:Number = NaN;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         var _loc16_:Matrix = null;
         var _loc17_:Rectangle = null;
         if(param1 < 0 || param2 < 0)
         {
            return;
         }
         var _loc5_:Rectangle = this.var_1.level.var_1090;
         var _loc6_:int = 1 + _loc5_.width / (var_757 / 2) + 1;
         if(param1 > _loc6_)
         {
            return;
         }
         var _loc7_:int = 1 + _loc5_.height / var_1002;
         if(param2 > _loc7_)
         {
            return;
         }
         if((param1 + param2) % 2)
         {
            param1--;
         }
         if(!this.var_581[param1])
         {
            this.var_581[param1] = new Dictionary();
         }
         var _loc8_:class_135;
         if(!(_loc8_ = this.var_581[param1][param2]))
         {
            _loc8_ = this.method_1389(param3,param4);
            this.var_581[param1][param2] = _loc8_;
            _loc8_.x = param1;
            _loc8_.y = param2;
            _loc9_ = _loc8_.var_312;
            _loc10_ = param1 * (var_757 * 0.5);
            _loc11_ = param2 * var_1002;
            _loc12_ = new Rectangle(0,0,_loc9_.bitmapData.width,_loc9_.bitmapData.height);
            _loc9_.bitmapData.fillRect(_loc12_,0);
            _loc13_ = _loc10_ + _loc5_.x;
            _loc14_ = _loc11_ + _loc5_.y;
            _loc15_ = this.var_1.main.var_982;
            (_loc16_ = new Matrix(1,0,0,1,-_loc13_,-_loc14_)).scale(_loc15_,_loc15_);
            _loc9_.bitmapData.drawWithQuality(this.var_1.level.var_59,_loc16_,null,null,_loc12_,true,StageQuality.HIGH);
            _loc9_.x = _loc15_ * _loc10_;
            _loc9_.y = _loc15_ * _loc11_;
            if(!(_loc17_ = _loc9_.bitmapData.getColorBoundsRect(4278190080,0,false)).width || !_loc17_.height)
            {
               this.method_607(_loc8_,const_208);
               _loc8_ = const_208;
            }
         }
         _loc8_.var_926 = this.var_1.mTimeThisTick;
      }
      
      public function method_1389(param1:Number, param2:Number) : class_135
      {
         var _loc3_:class_135 = null;
         var _loc4_:class_135 = null;
         for each(_loc4_ in this.var_986)
         {
            if(!(param1 - 1 <= _loc4_.x && _loc4_.x <= param1 + 2 && (param2 - 1 <= _loc4_.y && _loc4_.y <= param2 + 2)))
            {
               if(!_loc3_ || _loc3_.var_926 > _loc4_.var_926)
               {
                  _loc3_ = _loc4_;
               }
            }
         }
         if(_loc3_.var_926)
         {
            this.method_607(_loc3_,null);
         }
         if(!_loc3_.var_312.parent)
         {
            this.var_343.addChild(_loc3_.var_312);
         }
         return _loc3_;
      }
      
      public function method_607(param1:class_135, param2:class_135) : void
      {
         var _loc3_:Bitmap = param1.var_312;
         if(_loc3_.parent)
         {
            _loc3_.parent.removeChild(_loc3_);
         }
         _loc3_.bitmapData.fillRect(new Rectangle(0,0,_loc3_.bitmapData.width,_loc3_.bitmapData.height),0);
         if(Boolean(this.var_581[param1.x]) && this.var_581[param1.x][param1.y] == param1)
         {
            this.var_581[param1.x][param1.y] = param2;
         }
         else
         {
            class_24.method_19("No tile could be found at (" + param1.x + ", " + param1.y + ")");
         }
         param1.x = -100;
         param1.y = -100;
         param1.var_926 = 0;
      }
   }
}
