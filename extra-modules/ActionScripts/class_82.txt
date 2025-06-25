package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.DisplayObject;
   import flash.display.PixelSnapping;
   import flash.display.StageQuality;
   import flash.geom.Matrix;
   import flash.geom.Rectangle;
   import flash.utils.Dictionary;
   import flash.utils.getTimer;
   
   public class class_82
   {
      
      public static const const_503:Number = 2300;
       
      
      internal var var_1:Game;
      
      internal var var_410:Dictionary;
      
      internal var var_745:Dictionary;
      
      internal var var_2576:int = 1;
      
      internal var var_1522:int = 0;
      
      public function class_82(param1:Game)
      {
         super();
         this.var_1 = param1;
         this.var_410 = new Dictionary();
      }
      
      public function method_488(param1:MagicObject) : void
      {
         this.method_364(param1);
         delete this.var_410[param1.var_51.name];
         param1.method_1477();
      }
      
      public function method_412(param1:DisplayObject, param2:Boolean = false, param3:Boolean = false, param4:Boolean = false, param5:String = null, param6:String = null) : MagicObject
      {
         var _loc7_:MagicObject = null;
         (_loc7_ = new MagicObject()).dObj = param1;
         _loc7_.var_1751 = param2;
         _loc7_.var_2857 = param3;
         _loc7_.var_2771 = param4;
         _loc7_.var_2848 = param6;
         if(Boolean(param5) && !param5.indexOf("a_"))
         {
            _loc7_.var_1967 = param5;
         }
         _loc7_.var_741 = _loc7_.dObj.getBounds(_loc7_.dObj.parent);
         var _loc8_:Bitmap;
         (_loc8_ = new Bitmap(null,PixelSnapping.AUTO,false)).name = "MyID" + this.var_2576++;
         this.var_410[_loc8_.name] = _loc7_;
         _loc7_.var_51 = _loc8_;
         return _loc7_;
      }
      
      public function method_1829() : void
      {
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc12_:MagicObject = null;
         var _loc13_:MagicObject = null;
         var _loc1_:Number = -this.var_1.levelLayer.x;
         var _loc2_:Number = _loc1_ + Camera.SCREEN_WIDTH;
         var _loc3_:Number = -this.var_1.levelLayer.y;
         var _loc4_:Number = _loc3_ + Camera.PLAY_SCREEN_HEIGHT;
         var _loc9_:Number = this.var_1.mTimeThisTick;
         var _loc14_:Boolean = false;
         for each(_loc12_ in this.var_410)
         {
            _loc5_ = Number(_loc12_.var_741.x);
            _loc6_ = _loc12_.var_741.x + _loc12_.var_741.width;
            _loc7_ = _loc12_.var_741.y;
            _loc8_ = _loc12_.var_741.y + _loc12_.var_741.height;
            if(_loc5_ <= _loc2_ + Camera.SCREEN_WIDTH * 0.5 && _loc6_ >= _loc1_ - Camera.SCREEN_WIDTH * 0.5 && _loc7_ <= _loc4_ && _loc8_ >= _loc3_)
            {
               if(_loc5_ <= _loc2_ && _loc6_ >= _loc1_ && _loc7_ <= _loc4_ && _loc8_ >= _loc3_)
               {
                  if(this.method_193(_loc12_,true))
                  {
                     _loc14_ = true;
                  }
               }
               else if(!_loc12_.var_716)
               {
                  _loc13_ = _loc12_;
               }
            }
            else if(_loc12_.var_716)
            {
               if(!_loc12_.var_1751 && _loc9_ - _loc12_.var_2589 > 20000 && _loc12_.var_1967 == null)
               {
                  this.method_364(_loc12_);
               }
            }
         }
         if(!_loc14_ && Boolean(_loc13_))
         {
            this.method_193(_loc13_,false);
         }
      }
      
      public function method_193(param1:MagicObject, param2:Boolean) : Boolean
      {
         var _loc5_:Rectangle = null;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc8_:uint = 0;
         var _loc9_:uint = 0;
         var _loc10_:String = null;
         var _loc11_:BitmapData = null;
         var _loc12_:Number = NaN;
         var _loc13_:Number = NaN;
         var _loc14_:uint = 0;
         var _loc15_:uint = 0;
         param1.var_2589 = getTimer();
         if(Boolean(DevSettings.flags & DevSettings.DEVFLAG_NO_GRAPHICS) || param1.var_1766)
         {
            return false;
         }
         var _loc3_:DisplayObject = param1.dObj;
         var _loc4_:Bitmap = param1.var_51;
         if(!param1.var_716)
         {
            if(!(_loc5_ = MathUtil.method_138(_loc3_,_loc3_)) || !_loc5_.height || !_loc5_.width)
            {
               return false;
            }
            _loc6_ = this.var_1.main.var_2825;
            _loc7_ = 1 / _loc6_;
            _loc8_ = Math.ceil(_loc5_.width * _loc6_);
            _loc9_ = Math.ceil(_loc5_.height * _loc6_);
            _loc4_.x = _loc5_.x + _loc3_.x;
            _loc4_.y = _loc5_.y + _loc3_.y;
            _loc4_.scaleX = _loc7_;
            _loc4_.scaleY = _loc7_;
            param1.var_716 = new Matrix(_loc6_,0,0,_loc6_,-_loc5_.x * _loc6_,-_loc5_.y * _loc6_);
            if(!(_loc11_ = !!(_loc10_ = param1.var_1967) ? this.var_745[_loc10_] : null))
            {
               _loc11_ = new BitmapData(_loc8_,_loc9_,true,0);
               this.var_1522 += _loc8_ * _loc9_;
               if(_loc10_)
               {
                  this.var_745[_loc10_] = _loc11_;
               }
            }
            else
            {
               param2 = false;
               param1.var_1766 = true;
            }
            _loc4_.bitmapData = _loc11_;
            _loc12_ = _loc6_ * _loc4_.x;
            _loc13_ = _loc6_ * _loc4_.y;
            _loc12_ = Math.floor(_loc12_);
            _loc13_ = Math.floor(_loc13_);
            _loc12_ *= _loc7_;
            _loc13_ *= _loc7_;
            _loc4_.x = _loc12_;
            _loc4_.y = _loc13_;
         }
         if(param2)
         {
            if(!(DevSettings.flags & DevSettings.DEVFLAG_SHOWPERFORMANCE))
            {
               _loc4_.bitmapData.drawWithQuality(_loc3_,param1.var_716,_loc3_.transform.colorTransform,null,null,false,StageQuality.HIGH);
            }
            else
            {
               _loc14_ = uint(getTimer());
               _loc4_.bitmapData.drawWithQuality(_loc3_,param1.var_716,_loc3_.transform.colorTransform,null,null,false,StageQuality.HIGH);
               _loc15_ = uint(getTimer() - _loc14_);
               class_155.method_1187(_loc4_.bitmapData,_loc15_,"Cacher",null);
            }
            param1.var_1766 = true;
         }
         return true;
      }
      
      public function method_364(param1:MagicObject) : void
      {
         var _loc2_:BitmapData = null;
         if(!param1)
         {
            return;
         }
         if(param1.var_1967 == null)
         {
            _loc2_ = param1.var_51.bitmapData;
            if(_loc2_)
            {
               this.var_1522 -= _loc2_.height * _loc2_.width;
               _loc2_.dispose();
               param1.var_51.bitmapData = null;
            }
         }
         param1.var_716 = null;
         param1.var_1766 = false;
      }
      
      public function method_1049() : void
      {
         var _loc1_:BitmapData = null;
         var _loc2_:MagicObject = null;
         for each(_loc1_ in this.var_745)
         {
            _loc1_.dispose();
         }
         this.var_745 = new Dictionary();
         for each(_loc2_ in this.var_410)
         {
            this.method_364(_loc2_);
            if(_loc2_.var_1751)
            {
               this.method_193(_loc2_,true);
            }
         }
      }
      
      public function method_1558() : void
      {
         var _loc1_:MagicObject = null;
         var _loc2_:BitmapData = null;
         for each(_loc1_ in this.var_410)
         {
            this.method_488(_loc1_);
         }
         this.var_410 = null;
         for each(_loc2_ in this.var_745)
         {
            _loc2_.dispose();
         }
         this.var_745 = null;
      }
      
      public function method_954() : void
      {
         var _loc2_:String = null;
         var _loc3_:BitmapData = null;
         var _loc4_:MagicObject = null;
         var _loc1_:Dictionary = new Dictionary();
         for(_loc2_ in this.var_410)
         {
            if((_loc4_ = this.var_410[_loc2_]).var_2771)
            {
               _loc1_[_loc2_] = _loc4_;
            }
            else
            {
               this.method_488(_loc4_);
            }
         }
         this.var_410 = _loc1_;
         for each(_loc3_ in this.var_745)
         {
            _loc3_.dispose();
         }
         this.var_745 = new Dictionary();
      }
   }
}
