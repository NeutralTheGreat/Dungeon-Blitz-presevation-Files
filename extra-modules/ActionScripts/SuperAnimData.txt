package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.DisplayObject;
   import flash.display.GraphicsGradientFill;
   import flash.display.GraphicsSolidFill;
   import flash.display.IGraphicsData;
   import flash.display.MovieClip;
   import flash.display.PixelSnapping;
   import flash.display.Sprite;
   import flash.display.StageQuality;
   import flash.filters.ColorMatrixFilter;
   import flash.geom.ColorTransform;
   import flash.geom.Matrix;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.geom.Transform;
   import flash.utils.Dictionary;
   
   public class SuperAnimData
   {
      
      public static var aaMain:Main;
      
      private static const const_1169:ColorMatrixFilter = new ColorMatrixFilter([0.8,0.5,0.5,0,0,0.5,0.8,0.5,0,0,0.5,0.5,1.1,0,0,0,0,0,0.75,0]);
      
      private static const const_1003:ColorMatrixFilter = new ColorMatrixFilter([0.21602000296115875,0.4265799820423126,0.05739999935030937,0,33.04999923706055,0.21602000296115875,0.4265799820423126,0.05739999935030937,0,33.04999923706055,0.21602000296115875,0.4265799820423126,0.05739999935030937,0,33.04999923706055,0,0,0,1,0]);
      
      private static const const_431:Bitmap = new Bitmap();
      
      public static var var_2126:Dictionary;
      
      public static var var_1363:uint;
      
      private static const const_783:Dictionary = new Dictionary();
      
      private static const const_738:Dictionary = new Dictionary();
      
      private static var var_2014:Sprite = new Sprite();
      
      private static var tf:Sprite = new Sprite();
      
      private static var var_394:Rectangle = new Rectangle();
      
      private static var var_2854:Rectangle = new Rectangle();
      
      private static const MAGIC_ANTI_PIXEL_POPPING_SCALE:Number = 1.2;
      
      private static const TOP_LEFT_POINT:Point = new Point(0,0);
      
      private static const const_296:Point = new Point(0,0);
      
      public static var var_1403:Sprite = new Sprite();
      
      private static var var_1924:MovieClip = new MovieClip();
      
      private static var var_1966:Dictionary = new Dictionary();
      
      private static var var_1848:Dictionary = new Dictionary();
      
      private static var var_2626:Sprite = null;
      
      private static var var_2644:Number = 0;
      
      private static var var_2782:Number = 0;
      
      private static var var_2828:Number = 0.1;
      
      private static var var_1507:Dictionary = new Dictionary();
      
      private static var var_357:Vector.<SuperAnimData> = new Vector.<SuperAnimData>();
      
      private static var var_512:Dictionary = new Dictionary();
      
      public static var var_1220:Boolean = false;
      
      public static var var_263:int = 0;
      
      public static var var_665:int = 0;
      
      private static var var_853:BitmapData = null;
      
      private static var var_423:BitmapData = null;
      
      private static var s_Common128Canvas:BitmapData = null;
      
      private static var s_Common256Canvas:BitmapData = null;
      
      private static var s_Common384Canvas:BitmapData = null;
      
      private static var s_Common512Canvas:BitmapData = null;
      
      private static var MAX_ENT_BMP_HEIGHT:int = 530;
      
      private static var MAX_ENT_BMP_WIDTH:int = 590;
      
      private static var sadTotal:int = 0;
      
      internal static var boneBitmapLastChecked:uint = 0;
      
      internal static var var_1333:uint = 0;
      
      internal static const const_371:uint = 1000;
      
      internal static const const_525:uint = 262144;
      
      internal static const const_1423:int = 30 * const_371;
      
      internal static const const_1026:int = 60 * const_371;
      
      internal static const const_1083:int = 100 * const_525;
      
      internal static const const_989:int = 200 * const_525;
      
      internal static const const_1243:int = 400 * const_525;
      
      internal static const const_1096:uint = 419;
      
      internal static const BONEBITMAP_LIMIT_CHECK_FREQUENCY:int = 100 * const_371;
      
      internal static const BONEBITMAP_LIMIT_UNLOAD_TIME:int = 120 * const_371;
       
      
      internal var var_36:GfxType;
      
      private var var_1871:Dictionary;
      
      internal var var_71:class_30;
      
      internal var var_1501:Vector.<class_27>;
      
      internal var var_1221:Vector.<uint>;
      
      internal var var_1780:Dictionary;
      
      internal var var_1031:Boolean = false;
      
      internal var var_1826:uint = 0;
      
      internal var var_1271:Number = 1;
      
      internal var var_1021:int = 0;
      
      internal var var_1285:int = 0;
      
      internal var var_1341:Boolean;
      
      internal var var_2993:int;
      
      public function SuperAnimData(param1:GfxType)
      {
         var _loc6_:int = 0;
         var _loc7_:uint = 0;
         var _loc8_:ColorSwap = null;
         this.var_1871 = new Dictionary();
         super();
         this.var_36 = param1;
         var _loc2_:String = this.var_36.var_29;
         var _loc3_:String = this.var_36.animClass;
         this.var_71 = class_29.method_765(_loc3_,_loc2_,this.var_36.var_843);
         if(!this.var_71)
         {
            this.var_71 = class_29.method_602(_loc3_,_loc2_,_loc3_,this.var_36.var_843);
         }
         this.var_1501 = new Vector.<class_27>(this.var_71.var_1996,true);
         this.var_1341 = !_loc3_.indexOf("a_Cape");
         this.var_1221 = this.method_1171();
         this.var_1780 = new Dictionary();
         var _loc4_:Vector.<ColorSwap> = this.var_36.colorSwaps;
         var _loc5_:int;
         _loc6_ = (_loc5_ = int(this.var_36.colorSwaps.length)) - 1;
         while(_loc6_ >= 0)
         {
            _loc7_ = uint((_loc8_ = this.var_36.colorSwaps[_loc6_]).var_1354 | _loc8_.var_1150 << 24);
            this.var_1780[_loc7_] = _loc8_.var_411;
            _loc6_--;
         }
         this.var_1031 = !_loc2_.indexOf("Animation_") && !const_783[_loc2_];
         if(const_738[_loc3_])
         {
            this.var_1031 = false;
         }
         if(!_loc3_.indexOf("a_LightningStorm") || !_loc3_.indexOf("a_DeathMarkBone"))
         {
            this.var_36.var_177 = 0;
            this.var_1031 = true;
         }
         if(!_loc3_.indexOf("a_Animation_EB_"))
         {
            this.var_36.var_177 = 0;
            this.var_1031 = true;
         }
         if(this.var_1341)
         {
            this.var_1031 = false;
         }
         this.var_1271 = this.var_36.var_177;
         if(!this.var_1031)
         {
            this.var_1271 *= 10;
         }
      }
      
      public static function method_125(param1:Dictionary, param2:Array, param3:Array) : void
      {
         var _loc4_:String = null;
         var _loc5_:String = null;
         var_2126 = param1;
         var_1363 = param1["a_Cape"];
         for each(_loc4_ in param2)
         {
            const_783[_loc4_] = true;
         }
         for each(_loc5_ in param3)
         {
            const_738[_loc5_] = true;
         }
      }
      
      public static function method_402(param1:Vector.<uint>, param2:Array, param3:int) : Vector.<uint>
      {
         var _loc7_:uint = 0;
         var _loc8_:int = 0;
         var _loc9_:int = 0;
         var _loc10_:int = 0;
         var _loc4_:Vector.<uint> = new Vector.<uint>();
         var _loc5_:int = int(param2.length);
         var _loc6_:int = param1.length / 3;
         _loc9_ = 0;
         while(_loc9_ < _loc5_)
         {
            _loc7_ = uint(param2[_loc9_]);
            _loc10_ = 0;
            while(_loc10_ < _loc6_)
            {
               _loc8_ = _loc10_ * 3;
               if(_loc7_ == param1[_loc8_] && (param1[_loc8_ + 2] == 0 || param1[_loc8_ + 2] == param3))
               {
                  _loc4_.push(param1[_loc8_]);
                  _loc4_.push(param1[_loc8_ + 1]);
                  _loc4_.push(param1[_loc8_ + 2]);
               }
               _loc10_++;
            }
            _loc9_++;
         }
         return _loc4_;
      }
      
      public static function method_982(param1:DisplayObject) : Bitmap
      {
         var _loc8_:BitmapData = null;
         if(!param1.parent)
         {
            tf.addChild(param1);
         }
         var _loc2_:Rectangle = param1.getBounds(param1.parent);
         var _loc3_:Number = Math.floor(_loc2_.x);
         var _loc4_:Number = Math.floor(_loc2_.y);
         var _loc5_:Number = int(_loc2_.width + (_loc2_.x - _loc3_) + 2);
         var _loc6_:Number = int(_loc2_.height + (_loc2_.y - _loc4_) + 2);
         var _loc7_:Bitmap;
         (_loc7_ = new Bitmap(null,PixelSnapping.ALWAYS,true)).x = _loc3_;
         _loc7_.y = _loc4_;
         if(_loc5_ < 128 && _loc6_ < 128)
         {
            _loc8_ = SuperAnimData.s_Common128Canvas;
         }
         else if(_loc5_ < 256 && _loc6_ < 256)
         {
            _loc8_ = SuperAnimData.s_Common256Canvas;
         }
         else if(_loc5_ < 384 && _loc6_ < 384)
         {
            _loc8_ = SuperAnimData.s_Common384Canvas;
         }
         else if(_loc5_ < 512 && _loc6_ < 512)
         {
            _loc8_ = SuperAnimData.s_Common512Canvas;
         }
         else if(_loc5_ < SuperAnimData.var_423.width && _loc6_ < SuperAnimData.var_423.height)
         {
            _loc8_ = SuperAnimData.var_423;
         }
         else
         {
            _loc8_ = SuperAnimData.var_853;
         }
         var _loc9_:Matrix = param1.transform.matrix;
         _loc9_.tx -= _loc7_.x;
         _loc9_.ty -= _loc7_.y;
         _loc8_.drawWithQuality(param1,_loc9_,param1.transform.colorTransform,null,null,true,StageQuality.HIGH);
         var_394.x = 0;
         var_394.y = 0;
         var_394.height = _loc6_;
         var_394.width = _loc5_;
         var _loc10_:Rectangle;
         var _loc11_:Number = (_loc10_ = _loc8_.getColorBoundsRect(4278190080,0,false)).width > 1 ? _loc10_.width : 1;
         var _loc12_:Number = _loc10_.height > 1 ? _loc10_.height : 1;
         _loc7_.bitmapData = new BitmapData(_loc11_,_loc12_,true,0);
         _loc7_.bitmapData.copyPixels(_loc8_,_loc10_,const_296,null,null,false);
         _loc7_.x += _loc10_.x;
         _loc7_.y += _loc10_.y;
         _loc8_.fillRect(var_394,0);
         if(tf.numChildren)
         {
            tf.removeChild(param1);
         }
         return _loc7_;
      }
      
      public static function method_200(param1:Sprite, param2:Number, param3:uint, param4:Dictionary, param5:uint, param6:Boolean = false) : Bitmap
      {
         var _loc14_:BitmapData = null;
         var _loc15_:BitmapData = null;
         var _loc17_:uint = 0;
         var _loc18_:GraphicsGradientFill = null;
         var _loc19_:GraphicsSolidFill = null;
         var _loc20_:uint = 0;
         var _loc21_:int = 0;
         var _loc22_:Vector.<IGraphicsData> = null;
         var _loc23_:int = 0;
         var _loc24_:Rectangle = null;
         var _loc25_:Number = NaN;
         var _loc26_:Number = NaN;
         var _loc27_:Matrix = null;
         if(!param1.parent)
         {
            tf.addChild(param1);
         }
         param1.scaleX *= param2;
         param1.scaleY *= param2;
         var _loc7_:Rectangle = param1.getBounds(param1.parent);
         if(param2 > _loc7_.width)
         {
            _loc7_.width = param2;
         }
         if(param2 > _loc7_.height)
         {
            _loc7_.height = param2;
         }
         var _loc8_:Number = Math.floor(_loc7_.x);
         var _loc9_:Number = Math.floor(_loc7_.y);
         var _loc10_:Number = _loc7_.width + (_loc7_.x - _loc8_) + param2 + 2;
         var _loc11_:Number = _loc7_.height + (_loc7_.y - _loc9_) + param2 + 2;
         var _loc12_:Matrix = param1.transform.matrix;
         _loc12_.tx -= _loc8_;
         _loc12_.ty -= _loc9_;
         var _loc13_:ColorTransform = param3 == 0 ? null : new ColorTransform(((param3 & 16711680) >> 16) / 256,((param3 & 65280) >> 8) / 256,(param3 & 255) / 256,1,0,0,0,0);
         if(param6)
         {
            if(_loc10_ < 128 && _loc11_ < 128)
            {
               _loc14_ = SuperAnimData.s_Common128Canvas;
            }
            else if(_loc10_ < 256 && _loc11_ < 256)
            {
               _loc14_ = SuperAnimData.s_Common256Canvas;
            }
            else if(_loc10_ < 384 && _loc11_ < 384)
            {
               _loc14_ = SuperAnimData.s_Common384Canvas;
            }
            else if(_loc10_ < 512 && _loc11_ < 512)
            {
               _loc14_ = SuperAnimData.s_Common512Canvas;
            }
            else if(_loc10_ < SuperAnimData.var_423.width && _loc11_ < SuperAnimData.var_423.height)
            {
               _loc14_ = SuperAnimData.var_423;
            }
            else
            {
               _loc14_ = SuperAnimData.var_853;
            }
         }
         else
         {
            _loc14_ = new BitmapData(_loc10_,_loc11_,true,0);
         }
         if(param4)
         {
            _loc21_ = 0;
            _loc23_ = int((_loc22_ = param1.graphics.readGraphicsData(true)).length);
            _loc21_ = 0;
            while(_loc21_ < _loc23_)
            {
               if(_loc19_ = _loc22_[_loc21_] as GraphicsSolidFill)
               {
                  if(param5)
                  {
                     _loc20_ = uint(param4[_loc19_.color | param5 << 24]);
                  }
                  if(!param5 || !_loc20_)
                  {
                     _loc20_ = uint(param4[_loc19_.color]);
                  }
                  if(_loc20_)
                  {
                     _loc19_.color = _loc20_;
                  }
               }
               else if(_loc18_ = _loc22_[_loc21_] as GraphicsGradientFill)
               {
                  _loc17_ = uint(16777215 & _loc18_.colors[0]);
                  if(param5)
                  {
                     _loc20_ = uint(param4[_loc17_ | param5 << 24]);
                  }
                  if(!param5 || !_loc20_)
                  {
                     _loc20_ = uint(param4[_loc17_]);
                  }
                  if(_loc20_)
                  {
                     _loc18_.colors[0] = 4278190080 | _loc20_;
                  }
                  _loc17_ = uint(16777215 & _loc18_.colors[1]);
                  if(param5)
                  {
                     _loc20_ = uint(param4[_loc17_ | param5 << 24]);
                  }
                  if(!param5 || !_loc20_)
                  {
                     _loc20_ = uint(param4[_loc17_]);
                  }
                  if(_loc20_)
                  {
                     _loc18_.colors[1] = 4278190080 | _loc20_;
                  }
               }
               _loc21_++;
            }
            var_1403.graphics.clear();
            var_1403.graphics.drawGraphicsData(_loc22_);
            _loc14_.draw(var_1403,_loc12_,_loc13_,null,null,true);
         }
         else
         {
            _loc14_.draw(param1,_loc12_,_loc13_,null,null,true);
         }
         if(param6)
         {
            var_394.x = 0;
            var_394.y = 0;
            var_394.height = _loc11_;
            var_394.width = _loc10_;
            _loc25_ = (_loc24_ = _loc14_.getColorBoundsRect(4278190080,0,false)).width > 1 ? _loc24_.width : 1;
            _loc26_ = _loc24_.height > 1 ? _loc24_.height : 1;
            (_loc15_ = new BitmapData(_loc25_,_loc26_,true,0)).copyPixels(_loc14_,_loc24_,const_296,null,null,false);
            _loc14_.fillRect(var_394,0);
         }
         else
         {
            _loc15_ = _loc14_;
         }
         var _loc16_:Bitmap;
         (_loc16_ = new Bitmap()).bitmapData = _loc15_;
         _loc16_.smoothing = true;
         _loc16_.pixelSnapping = PixelSnapping.NEVER;
         param1.scaleX /= param2;
         param1.scaleY /= param2;
         _loc12_.invert();
         _loc16_.transform.matrix = _loc12_;
         if(param6)
         {
            (_loc27_ = _loc12_.clone()).translate(_loc24_.x,_loc24_.y);
            _loc16_.transform.matrix = _loc27_;
         }
         if(tf.numChildren)
         {
            tf.removeChild(param1);
         }
         return _loc16_;
      }
      
      public static function method_807(param1:Sprite, param2:Number) : Sprite
      {
         var _loc4_:Bitmap = null;
         var _loc3_:Sprite = new Sprite();
         if(!(DevSettings.flags & DevSettings.DEVFLAG_NO_GRAPHICS))
         {
            (_loc4_ = method_200(param1,param2,0,null,0,true)).smoothing = false;
            _loc4_.pixelSnapping = PixelSnapping.ALWAYS;
            _loc3_.addChild(_loc4_);
         }
         return _loc3_;
      }
      
      public static function method_504(param1:Sprite) : void
      {
         var _loc2_:Bitmap = null;
         if(Boolean(param1) && param1.numChildren == 1)
         {
            _loc2_ = param1.getChildAt(0) as Bitmap;
            if(Boolean(_loc2_) && Boolean(_loc2_.bitmapData))
            {
               _loc2_.bitmapData.dispose();
            }
         }
      }
      
      public static function method_939(param1:GfxType) : SuperAnimData
      {
         var _loc2_:String = param1.method_1554();
         var _loc3_:SuperAnimData = var_1507[_loc2_];
         if(!_loc3_)
         {
            ++sadTotal;
            _loc3_ = new SuperAnimData(param1);
            SuperAnimData.var_1507[_loc2_] = _loc3_;
         }
         return _loc3_;
      }
      
      public static function method_1675(param1:uint) : void
      {
         var _loc2_:Number = NaN;
         var _loc3_:SuperAnimData = null;
         if(var_263 < const_1083)
         {
            return;
         }
         if(param1 - var_1333 < const_1096)
         {
            return;
         }
         var_1333 = param1;
         var _loc6_:Number = var_263 >= const_989 ? (var_263 >= const_1243 ? 16 : 4) : 1;
         var _loc7_:int = int(var_357.length - 1);
         while(_loc7_ >= 0)
         {
            _loc3_ = var_357[_loc7_];
            _loc2_ = _loc6_ * (param1 - _loc3_.var_1826) / _loc3_.var_1271;
            if(_loc2_ > const_1026)
            {
               _loc3_.method_261();
               break;
            }
            _loc7_--;
         }
      }
      
      public static function method_1109(param1:GfxType) : void
      {
         var _loc3_:SuperAnimData = null;
         var _loc4_:int = int(var_357.length - 1);
         while(_loc4_ >= 0)
         {
            _loc3_ = var_357[_loc4_];
            if(!(_loc3_.var_1271 >= 100 || _loc3_.var_36 == param1))
            {
               _loc3_.method_261();
            }
            _loc4_--;
         }
      }
      
      public static function method_684() : void
      {
         var _loc1_:Bitmap = null;
         var _loc2_:Array = null;
         var _loc3_:Array = null;
         for each(_loc2_ in var_512)
         {
            for each(_loc3_ in _loc2_)
            {
               for each(_loc1_ in _loc3_)
               {
                  if(_loc1_.bitmapData)
                  {
                     var_665 -= _loc1_.bitmapData.height * _loc1_.bitmapData.width;
                     _loc1_.bitmapData.dispose();
                     _loc1_.bitmapData = null;
                  }
               }
            }
         }
         var_512 = new Dictionary();
      }
      
      public static function method_806() : void
      {
         if(DevSettings.DEVFLAG_NO_GRAPHICS & DevSettings.flags)
         {
            return;
         }
         var _loc1_:Number = 4 * aaMain.var_2243;
         if(var_853)
         {
            var_853.dispose();
         }
         var_853 = new BitmapData(MAX_ENT_BMP_WIDTH * _loc1_,MAX_ENT_BMP_HEIGHT * _loc1_,true,0);
         if(var_423)
         {
            var_423.dispose();
         }
         var_423 = new BitmapData(MAX_ENT_BMP_WIDTH * _loc1_ / 2,MAX_ENT_BMP_HEIGHT * _loc1_ / 2,true,0);
         if(s_Common128Canvas)
         {
            s_Common128Canvas.dispose();
         }
         s_Common128Canvas = new BitmapData(128,128,true,0);
         if(s_Common256Canvas)
         {
            s_Common256Canvas.dispose();
         }
         s_Common256Canvas = new BitmapData(256,256,true,0);
         if(s_Common384Canvas)
         {
            s_Common384Canvas.dispose();
         }
         s_Common384Canvas = new BitmapData(384,384,true,0);
         if(s_Common512Canvas)
         {
            s_Common512Canvas.dispose();
         }
         s_Common512Canvas = new BitmapData(512,512,true,0);
      }
      
      public static function method_1563() : void
      {
         var _loc1_:SuperAnimData = null;
         for each(_loc1_ in var_1507)
         {
            _loc1_.method_261();
         }
         var_357 = new Vector.<SuperAnimData>();
         method_684();
         method_806();
         var_1220 = true;
      }
      
      private function method_1171() : Vector.<uint>
      {
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:ColorSwap = null;
         var _loc1_:Vector.<ColorSwap> = this.var_36.colorSwaps;
         var _loc2_:uint = this.var_36.colorSwaps.length;
         var _loc3_:Vector.<uint> = new Vector.<uint>(_loc2_ * 3,true);
         _loc4_ = 0;
         _loc5_ = 0;
         while(_loc4_ < _loc2_)
         {
            _loc6_ = this.var_36.colorSwaps[_loc4_];
            _loc3_[_loc5_] = _loc6_.var_1354;
            _loc3_[_loc5_ + 1] = _loc6_.var_411;
            _loc3_[_loc5_ + 2] = _loc6_.var_1150;
            _loc4_++;
            _loc5_ += 3;
         }
         return _loc3_;
      }
      
      public function method_866(param1:class_26, param2:class_28, param3:Sprite, param4:Bitmap, param5:Number) : void
      {
         var _loc13_:uint = 0;
         var _loc14_:MovieClip = null;
         var _loc15_:Boolean = false;
         if(DevSettings.DEVFLAG_NO_GRAPHICS & DevSettings.flags)
         {
            return;
         }
         var _loc6_:class_27;
         if(!(_loc6_ = this.var_1501[param1.var_1859]))
         {
            _loc6_ = new class_27(param1);
            this.var_1501[param1.var_1859] = _loc6_;
         }
         while(param3.numChildren)
         {
            param3.removeChildAt(0);
         }
         var _loc7_:Number = this.var_36.var_1864 != 0 ? this.var_36.var_1864 : aaMain.var_2243;
         var _loc8_:Number = this.var_36.animScale * _loc7_ * param5;
         var _loc9_:Sprite = null;
         var _loc10_:int = int(param2.var_2034);
         var _loc11_:Bitmap;
         if(!(_loc11_ = _loc6_.var_575[_loc10_]))
         {
            if(this.var_1031)
            {
               if(!(_loc9_ = _loc6_.var_875[_loc10_]))
               {
                  (_loc9_ = this.method_902(this.var_36.customArts,param2.var_900,new Matrix(),null,_loc8_)).scaleX = _loc8_;
                  _loc9_.scaleY = _loc8_;
                  _loc6_.var_875[_loc10_] = _loc9_;
               }
               if(Boolean(this.var_1271) || Boolean(_loc9_.parent))
               {
                  _loc11_ = method_982(_loc9_);
               }
            }
            else
            {
               _loc13_ = uint(_loc10_ + param1.var_2175);
               if((_loc14_ = param1.var_1073).currentFrame != _loc13_)
               {
                  _loc14_.gotoAndStop(_loc13_);
               }
               _loc15_ = Boolean(this.var_1221) && Boolean(this.var_1221.length);
               _loc11_ = method_200(_loc14_,_loc8_,this.var_36.tint,_loc15_ ? this.var_1780 : null,this.var_1341 ? var_1363 : 0);
               if(!this.var_1341)
               {
                  _loc11_.x /= _loc11_.scaleX;
                  _loc11_.y /= _loc11_.scaleY;
                  _loc11_.scaleX = 1;
                  _loc11_.scaleY = 1;
               }
            }
            if(_loc11_)
            {
               if(this.var_36.var_1526)
               {
                  _loc11_.bitmapData.applyFilter(_loc11_.bitmapData,_loc11_.bitmapData.rect,const_296,const_1169);
               }
               else if(this.var_36.var_1598)
               {
                  _loc11_.bitmapData.applyFilter(_loc11_.bitmapData,_loc11_.bitmapData.rect,const_296,const_1003);
               }
               _loc6_.var_575[_loc10_] = _loc11_;
               if(!this.var_1021)
               {
                  var_357.push(this);
               }
               ++this.var_1021;
               this.var_1285 += _loc11_.bitmapData.height * _loc11_.bitmapData.width;
               var_263 += _loc11_.bitmapData.height * _loc11_.bitmapData.width;
            }
         }
         if(!_loc11_)
         {
            param3.addChild(_loc9_);
         }
         else
         {
            param4.bitmapData = _loc11_.bitmapData;
            if(aaMain.var_1976)
            {
               param4.pixelSnapping = PixelSnapping.NEVER;
               param4.smoothing = true;
            }
            if(this.var_1341)
            {
               param4.transform = new Transform(_loc11_);
               param4.smoothing = true;
            }
            else
            {
               param4.x = _loc11_.x;
               param4.y = _loc11_.y;
               param4.scrollRect = _loc11_.scrollRect;
            }
            param3.addChild(param4);
            if(this.var_36.var_527)
            {
               param4.pixelSnapping = PixelSnapping.AUTO;
               param4.smoothing = true;
            }
         }
         var _loc12_:Number = 1 / _loc7_;
         param3.scaleX = _loc12_;
         param3.scaleY = _loc12_;
      }
      
      private function method_902(param1:Vector.<CustomArt>, param2:Vector.<class_25>, param3:Matrix, param4:Sprite, param5:Number) : Sprite
      {
         var _loc7_:int = 0;
         var _loc8_:int = 0;
         var _loc9_:Sprite = null;
         var _loc10_:class_25 = null;
         var _loc11_:MovieClip = null;
         var _loc12_:Sprite = null;
         var _loc13_:CustomArt = null;
         var _loc15_:Matrix = null;
         var _loc16_:Matrix = null;
         var _loc17_:Array = null;
         var _loc18_:int = 0;
         var _loc19_:Bitmap = null;
         var _loc20_:DisplayObject = null;
         var _loc21_:uint = 0;
         var _loc22_:Vector.<uint> = null;
         var _loc23_:Boolean = false;
         var _loc24_:String = null;
         var _loc25_:uint = 0;
         var _loc26_:int = 0;
         var _loc27_:String = null;
         var _loc28_:Array = null;
         var _loc29_:Matrix = null;
         var _loc30_:Number = NaN;
         var _loc31_:Bitmap = null;
         var _loc32_:Matrix = null;
         var _loc6_:Sprite = new Sprite();
         var _loc14_:int = int(param2.length);
         _loc7_ = 0;
         while(_loc7_ < _loc14_)
         {
            _loc10_ = param2[_loc7_];
            _loc11_ = null;
            if(_loc10_.var_1263)
            {
               if(_loc10_.var_1866)
               {
                  _loc8_ = int(param1.length - 1);
                  while(_loc8_ >= 0)
                  {
                     _loc13_ = param1[_loc8_];
                     if(_loc9_ = this.method_334("a_Head",_loc13_.fileName,_loc13_.setName))
                     {
                        break;
                     }
                     _loc8_--;
                  }
               }
               (_loc15_ = _loc10_.var_1320.clone()).concat(param3);
               (_loc12_ = this.method_902(param1,_loc10_.var_1263,_loc15_,_loc10_.var_1866 ? _loc9_ : null,param5)).alpha = _loc10_.var_2320;
               _loc12_.transform.matrix = _loc10_.var_1320;
               _loc6_.addChild(_loc12_);
            }
            else
            {
               _loc16_ = null;
               if(param4)
               {
                  if(_loc20_ = param4.getChildAt(_loc7_))
                  {
                     _loc16_ = _loc20_.transform.matrix;
                  }
               }
               if(!_loc16_)
               {
                  _loc16_ = _loc10_.var_1320;
               }
               if(!(_loc17_ = this.var_1871[_loc10_.className]))
               {
                  this.var_1871[_loc10_.className] = _loc17_ = new Array();
               }
               _loc18_ = _loc10_.frame;
               if((Boolean(_loc19_ = _loc17_[_loc18_])) && !_loc19_.bitmapData)
               {
                  _loc19_ = null;
                  _loc17_[_loc18_] = null;
               }
               if(!_loc19_)
               {
                  _loc8_ = int(param1.length - 1);
                  while(_loc8_ >= 0)
                  {
                     if(!_loc11_)
                     {
                        _loc11_ = this.method_334(_loc10_.className,param1[_loc8_].fileName,param1[_loc8_].setName);
                     }
                     if(_loc11_)
                     {
                        break;
                     }
                     _loc8_--;
                  }
                  if(!_loc11_)
                  {
                     if(!_loc11_)
                     {
                        _loc11_ = this.method_334(_loc10_.className,this.var_36.var_29,null);
                     }
                  }
                  if(!_loc11_)
                  {
                     _loc19_ = const_431;
                  }
                  if(!_loc19_)
                  {
                     if(_loc11_.bHasColors)
                     {
                        _loc21_ = (_loc22_ = method_402(this.var_1221,_loc11_.a,_loc10_.var_2440)).length;
                     }
                     _loc23_ = Boolean(_loc22_) && Boolean(_loc22_.length);
                     _loc24_ = "!";
                     _loc25_ = 0;
                     while(_loc25_ < _loc21_)
                     {
                        _loc24_ += _loc22_[_loc25_];
                        _loc25_++;
                     }
                     _loc26_ = int(this.var_36.animScale * (!!this.var_36.var_1864 ? this.var_36.var_1864 : 1) * 5 + 0.5);
                     _loc27_ = _loc10_.frame.toString() + "^" + _loc26_.toString() + "^" + this.var_36.tint.toString();
                     if(!GfxType.var_1588 && Boolean(this.var_36.var_947))
                     {
                        _loc27_ += "^" + this.var_36.var_947;
                     }
                     if(!var_512[_loc11_])
                     {
                        var_512[_loc11_] = new Array();
                     }
                     if(!var_512[_loc11_][_loc27_])
                     {
                        var_512[_loc11_][_loc27_] = new Array();
                     }
                     if((_loc19_ = (_loc28_ = var_512[_loc11_][_loc27_])[_loc24_]) == null)
                     {
                        (_loc29_ = param3.clone()).concat(_loc16_);
                        _loc11_.transform.matrix = _loc29_;
                        if(_loc10_.frame != _loc11_.currentFrame)
                        {
                           _loc11_.gotoAndStop(_loc10_.frame);
                        }
                        var_2014.addChild(_loc11_);
                        if(_loc11_.width == 0 || _loc11_.height == 0)
                        {
                           _loc19_ = const_431;
                        }
                        else
                        {
                           _loc19_ = method_200(_loc11_,param5 * MAGIC_ANTI_PIXEL_POPPING_SCALE,this.var_36.tint,_loc23_ ? this.var_1780 : null,_loc10_.var_2440);
                           var_665 += _loc19_.bitmapData.height * _loc19_.bitmapData.width;
                        }
                        _loc30_ = _loc19_.alpha;
                        _loc28_[_loc24_] = _loc19_;
                     }
                  }
                  _loc17_[_loc18_] = _loc19_;
               }
               if(Boolean(_loc19_) && _loc19_ != const_431)
               {
                  (_loc31_ = new Bitmap(_loc19_.bitmapData,PixelSnapping.NEVER,true)).transform = new Transform(_loc19_);
                  (_loc32_ = _loc31_.transform.matrix).concat(_loc16_);
                  _loc31_.transform.matrix = _loc32_;
                  _loc31_.alpha = _loc10_.var_2320;
                  _loc6_.addChild(_loc31_);
               }
            }
            _loc7_++;
         }
         return _loc6_;
      }
      
      public function method_334(param1:String, param2:String, param3:String) : MovieClip
      {
         var _loc4_:Dictionary = null;
         var _loc6_:Dictionary = null;
         var _loc7_:String = null;
         var _loc8_:Class = null;
         var _loc9_:Object = null;
         if(param3)
         {
            if(!(_loc6_ = var_1848[param2]))
            {
               var_1848[param2] = _loc6_ = new Dictionary();
            }
            if(!(_loc4_ = _loc6_[param3]))
            {
               _loc6_[param3] = _loc4_ = new Dictionary();
            }
         }
         else if(!(_loc4_ = var_1966[param2]))
         {
            var_1966[param2] = _loc4_ = new Dictionary();
         }
         var _loc5_:MovieClip;
         if(!(_loc5_ = _loc4_[param1]))
         {
            _loc7_ = param1;
            if(param3)
            {
               _loc7_ += "_" + param3;
            }
            if((Boolean(_loc9_ = ResourceManager.const_40[param2])) && Boolean(_loc9_.applicationDomain.hasDefinition(_loc7_)))
            {
               _loc8_ = _loc9_.applicationDomain.getDefinition(_loc7_);
            }
            if(_loc8_)
            {
               (_loc5_ = new _loc8_() as MovieClip).gotoAndStop(1);
               if(_loc5_.hasOwnProperty("a"))
               {
                  _loc5_.bHasColors = true;
               }
               else
               {
                  _loc5_.a = null;
                  _loc5_.bHasColors = false;
               }
            }
            else
            {
               _loc5_ = var_1924;
            }
            _loc4_[param1] = _loc5_;
         }
         if(_loc5_ == var_1924)
         {
            return null;
         }
         return _loc5_;
      }
      
      public function method_2098(param1:class_27, param2:uint) : void
      {
         var _loc4_:int = 0;
         var _loc3_:uint = param1.method_1490(param2);
         if(!_loc3_)
         {
            return;
         }
         this.var_1285 -= _loc3_;
         var_263 -= _loc3_;
         --this.var_1021;
         if(!this.var_1021)
         {
            if((_loc4_ = var_357.indexOf(this)) != -1)
            {
               var_357.splice(_loc4_,1);
            }
         }
      }
      
      public function method_261() : void
      {
         var _loc1_:class_27 = null;
         var _loc2_:int = 0;
         for each(_loc1_ in this.var_1501)
         {
            if(_loc1_)
            {
               _loc1_.method_742();
               _loc1_.method_647();
            }
         }
         var_263 -= this.var_1285;
         this.var_1021 = 0;
         this.var_1285 = 0;
         this.var_1871 = new Dictionary();
         _loc2_ = var_357.indexOf(this);
         if(_loc2_ != -1)
         {
            var_357.splice(_loc2_,1);
         }
      }
   }
}
