package
{
   import flash.display.DisplayObject;
   import flash.display.DisplayObjectContainer;
   import flash.display.FrameLabel;
   import flash.display.MovieClip;
   import flash.display.Scene;
   import flash.display.Sprite;
   import flash.filters.ColorMatrixFilter;
   import flash.filters.GlowFilter;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   import flash.text.TextFormat;
   import flash.utils.Dictionary;
   import flash.utils.getQualifiedClassName;
   
   public class MathUtil
   {
      
      public static const const_1391:uint = 604800;
      
      private static var var_2209:Point = new Point();
      
      private static const const_739:Dictionary = new Dictionary();
       
      
      public function MathUtil()
      {
         super();
      }
      
      public static function method_1144(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Point = null) : Number
      {
         var _loc13_:Number = NaN;
         var _loc8_:Number = -param6;
         var _loc9_:Number = param5;
         var _loc10_:Number;
         if(_loc10_ = Math.sqrt(_loc8_ * _loc8_ + _loc9_ * _loc9_))
         {
            _loc13_ = -1 / _loc10_;
            _loc8_ *= _loc13_;
            _loc9_ *= _loc13_;
         }
         if(param7)
         {
            param7.x = _loc8_;
            param7.y = _loc9_;
         }
         var _loc11_:Number = param1 - param3;
         var _loc12_:Number = param2 - param4;
         return _loc11_ * _loc8_ + _loc12_ * _loc9_;
      }
      
      public static function method_222(param1:Number, param2:Point, param3:Number) : Number
      {
         var _loc7_:Number = NaN;
         var _loc4_:Number = 0;
         var _loc6_:Number;
         var _loc5_:Number;
         if((_loc6_ = (_loc5_ = param2.x > 0 ? Math.asin(param2.y) : Math.PI - Math.asin(param2.y)) * 180 / Math.PI + 90) > param1)
         {
            _loc7_ = _loc6_ - param1;
         }
         else
         {
            _loc7_ = 360 - param1 + _loc6_;
         }
         if(_loc7_ > 180)
         {
            _loc7_ -= 360;
         }
         if(Math.abs(_loc7_) < param3)
         {
            _loc4_ = _loc6_;
         }
         else
         {
            _loc4_ = param1 + param3 * (Math.abs(_loc7_) / _loc7_);
         }
         return _loc4_;
      }
      
      public static function method_2019(param1:Point, param2:Point, param3:Number) : void
      {
         var _loc4_:Number = param3 * (Math.PI / 180);
         var _loc5_:Number = Math.cos(_loc4_);
         var _loc6_:Number = Math.sin(_loc4_);
         var _loc7_:Number = param1.x;
         var _loc8_:Number = param1.y;
         param1.x = _loc7_ * _loc5_ - _loc8_ * _loc6_;
         param1.y = _loc8_ * _loc5_ + _loc7_ * _loc6_;
         _loc7_ = param2.x;
         _loc8_ = param2.y;
         param2.x = _loc7_ * _loc5_ - _loc8_ * _loc6_;
         param2.y = _loc8_ * _loc5_ + _loc7_ * _loc6_;
      }
      
      public static function method_500(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number, param8:Number, param9:Point) : Boolean
      {
         var _loc10_:Number;
         if(!(_loc10_ = (param8 - param6) * (param3 - param1) - (param7 - param5) * (param4 - param2)))
         {
            return false;
         }
         var _loc11_:Number;
         var _loc12_:Number = (_loc11_ = 1 / _loc10_) * ((param7 - param5) * (param2 - param6) - (param8 - param6) * (param1 - param5));
         var _loc13_:Number = _loc11_ * ((param3 - param1) * (param2 - param6) - (param4 - param2) * (param1 - param5));
         if(_loc12_ >= 0 && _loc12_ <= 1 && _loc13_ >= 0 && _loc13_ <= 1)
         {
            param9.x = param1 + _loc12_ * (param3 - param1);
            param9.y = param2 + _loc12_ * (param4 - param2);
            return true;
         }
         return false;
      }
      
      public static function method_160(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number) : Number
      {
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         var _loc9_:Number = param5 - param1;
         var _loc10_:Number = param6 - param2;
         var _loc11_:Number;
         if((_loc11_ = param3 * _loc9_ + param4 * _loc10_) < 0)
         {
            _loc7_ = param1;
            _loc8_ = param2;
         }
         else if(!(_loc14_ = param3 * param3 + param4 * param4))
         {
            _loc7_ = param1;
            _loc8_ = param2;
         }
         else if(_loc11_ > _loc14_)
         {
            _loc7_ = param1 + param3;
            _loc8_ = param2 + param4;
         }
         else
         {
            _loc15_ = _loc11_ / _loc14_;
            _loc7_ = param1 + param3 * _loc15_;
            _loc8_ = param2 + param4 * _loc15_;
         }
         var _loc12_:Number = param5 - _loc7_;
         var _loc13_:Number = param6 - _loc8_;
         return _loc12_ * _loc12_ + _loc13_ * _loc13_;
      }
      
      public static function dot(param1:Number, param2:Number, param3:Number, param4:Number) : Number
      {
         return param1 * param3 + param2 * param4;
      }
      
      public static function method_724(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number, param8:Number) : Number
      {
         var _loc9_:Number = method_160(param1,param2,param3,param4,param5,param6);
         var _loc10_:Number = method_160(param5,param6,param7,param8,param1,param2);
         var _loc11_:Number = method_160(param1,param2,param3,param4,param5 + param7,param6 + param8);
         var _loc12_:Number = method_160(param5,param6,param7,param8,param1 + param3,param2 + param4);
         if(_loc9_ < _loc10_)
         {
            _loc10_ = _loc9_;
         }
         if(_loc11_ < _loc12_)
         {
            _loc12_ = _loc11_;
         }
         if(_loc10_ < _loc12_)
         {
            _loc12_ = _loc10_;
         }
         return _loc12_;
      }
      
      public static function method_1246(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number, param8:Number, param9:Number, param10:Number) : Boolean
      {
         if(method_500(param1,param2,param1 + param3,param2 + param4,param6,param7,param6 + param8,param7 + param9,var_2209))
         {
            return true;
         }
         var _loc11_:Number = param5 + param10;
         var _loc12_:Number;
         return (_loc12_ = method_724(param1,param2,param3,param4,param6,param7,param8,param9)) <= _loc11_ * _loc11_;
      }
      
      public static function method_2032(param1:Number, param2:Number, param3:Point, param4:Point) : Number
      {
         var _loc5_:Number = NaN;
         if(param1 < param2)
         {
            _loc5_ = param1 * 0.5;
            param3.x = 0;
            param3.y = -_loc5_;
            param4.x = 0;
            param4.y = -param2 + param1;
         }
         else
         {
            _loc5_ = param2 * 0.5;
            param3.x = -(param1 * 0.5) + _loc5_;
            param3.y = -(param2 * 0.5);
            param4.x = param1 - param2;
            param4.y = 0;
         }
         return _loc5_;
      }
      
      public static function method_703(param1:Number, param2:Number, param3:Number, param4:Number, param5:Vector.<Number>, param6:Vector.<Number>, param7:Number) : int
      {
         var _loc20_:Number = NaN;
         var _loc21_:Number = NaN;
         var _loc22_:Number = NaN;
         var _loc23_:Number = NaN;
         var _loc24_:Number = NaN;
         var _loc25_:int = 0;
         var _loc27_:Number = NaN;
         var _loc28_:Number = NaN;
         var _loc8_:int = 0;
         var _loc9_:Number = param4 - param2;
         var _loc10_:Number = param3 - param1;
         if(_loc9_ < 0)
         {
            _loc9_ = -_loc9_;
         }
         if(_loc10_ < 0)
         {
            _loc10_ = -_loc10_;
         }
         var _loc11_:*;
         if(_loc11_ = _loc9_ > _loc10_)
         {
            _loc27_ = param1;
            param1 = param2;
            param2 = _loc27_;
            _loc27_ = param3;
            param3 = param4;
            param4 = _loc27_;
         }
         if(param1 > param3)
         {
            _loc28_ = param1;
            param1 = param3;
            param3 = _loc28_;
            _loc28_ = param2;
            param2 = param4;
            param4 = _loc28_;
         }
         var _loc12_:*;
         if(_loc12_ = param4 < param2)
         {
            param4 = -param4;
            param2 = -param2;
         }
         var _loc13_:Number = 1 / param7;
         var _loc14_:Number = Math.floor(param1 * _loc13_) * param7;
         var _loc15_:Number = Math.floor(param2 * _loc13_) * param7;
         param1 -= _loc14_;
         param2 -= _loc15_;
         param3 -= _loc14_;
         var _loc16_:Number = ((param4 -= _loc15_) - param2) / (param3 - param1);
         var _loc17_:Number = param2 - _loc16_ * param1;
         var _loc18_:Number = 0;
         var _loc19_:Number = 0;
         while(param3 >= _loc18_)
         {
            param5[_loc8_] = _loc18_;
            var _loc29_:*;
            param6[_loc29_ = _loc8_++] = _loc19_;
            _loc21_ = (_loc18_ += param7) < param3 ? _loc18_ : param3;
            if((_loc20_ = _loc16_ * _loc21_ + _loc17_) >= _loc19_ + param7)
            {
               _loc19_ += param7;
               param5[_loc8_] = _loc18_ - param7;
               var _loc30_:*;
               param6[_loc30_ = _loc8_++] = _loc19_;
            }
         }
         var _loc26_:int = _loc8_;
         _loc25_ = 0;
         while(_loc25_ < _loc26_)
         {
            _loc23_ = param5[_loc25_] + _loc14_;
            _loc24_ = param6[_loc25_] + _loc15_;
            if(_loc12_)
            {
               _loc24_ = -_loc24_ - param7;
            }
            if(_loc11_)
            {
               _loc22_ = _loc23_;
               _loc23_ = _loc24_;
               _loc24_ = _loc22_;
            }
            param5[_loc25_] = _loc23_;
            param6[_loc25_] = _loc24_;
            _loc25_++;
         }
         return _loc8_;
      }
      
      public static function method_2035(param1:Number, param2:Number, param3:Number, param4:Number, param5:Vector.<Point>) : void
      {
         var _loc11_:Number = NaN;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         if(param1 > param3)
         {
            _loc15_ = param1;
            param1 = param3;
            param3 = _loc15_;
            _loc15_ = param2;
            param2 = param4;
            param4 = _loc15_;
         }
         var _loc7_:Number = param3 - param1;
         var _loc8_:Number = Math.abs(param4 - param2);
         var _loc9_:Number = 0;
         var _loc10_:Number = _loc8_ / _loc7_;
         var _loc12_:Number = param2;
         _loc11_ = param2 < param4 ? 1 : -1;
         var _loc13_:int = param1;
         while(_loc13_ < param3)
         {
            param5.push(new Point(_loc12_,_loc13_));
            if((_loc9_ += _loc10_) >= 0.5)
            {
               _loc12_ += _loc11_;
               _loc9_--;
            }
            _loc13_++;
         }
      }
      
      public static function method_1546(param1:uint, param2:uint, param3:uint) : uint
      {
         return uint(param1 << 16 | param2 << 8 | param3);
      }
      
      public static function method_2050(param1:uint) : Array
      {
         var _loc2_:Array = [];
         var _loc3_:uint = uint(param1 >> 16 & 255);
         var _loc4_:uint = uint(param1 >> 8 & 255);
         var _loc5_:uint = uint(param1 & 255);
         _loc2_.push(_loc3_,_loc4_,_loc5_);
         return _loc2_;
      }
      
      public static function method_1971(param1:uint, param2:uint, param3:uint) : Array
      {
         var _loc4_:uint = Math.max(param1,param2,param3);
         var _loc5_:uint = Math.min(param1,param2,param3);
         var _loc6_:Number = 0;
         var _loc7_:Number = 0;
         var _loc8_:Number = 0;
         var _loc9_:Array = [];
         if(_loc4_ == _loc5_)
         {
            _loc6_ = 0;
         }
         else if(_loc4_ == param1)
         {
            _loc6_ = (60 * (param2 - param3) / (_loc4_ - _loc5_) + 360) % 360;
         }
         else if(_loc4_ == param2)
         {
            _loc6_ = 60 * (param3 - param1) / (_loc4_ - _loc5_) + 120;
         }
         else if(_loc4_ == param3)
         {
            _loc6_ = 60 * (param1 - param2) / (_loc4_ - _loc5_) + 240;
         }
         _loc8_ = _loc4_;
         if(_loc4_ == 0)
         {
            _loc7_ = 0;
         }
         else
         {
            _loc7_ = (_loc4_ - _loc5_) / _loc4_;
         }
         return [Math.round(_loc6_),Math.round(_loc7_ * 100),Math.round(_loc8_ / 255 * 100)];
      }
      
      public static function method_1652(param1:Number, param2:Number, param3:Number) : Array
      {
         var _loc4_:Number = 0;
         var _loc5_:Number = 0;
         var _loc6_:Number = 0;
         var _loc7_:Array = [];
         var _loc8_:Number = param2 / 100;
         var _loc9_:Number = param3 / 100;
         var _loc10_:int = Math.floor(param1 / 60) % 6;
         var _loc11_:Number = param1 / 60 - Math.floor(param1 / 60);
         var _loc12_:Number = _loc9_ * (1 - _loc8_);
         var _loc13_:Number = _loc9_ * (1 - _loc11_ * _loc8_);
         var _loc14_:Number = _loc9_ * (1 - (1 - _loc11_) * _loc8_);
         switch(_loc10_)
         {
            case 0:
               _loc4_ = _loc9_;
               _loc5_ = _loc14_;
               _loc6_ = _loc12_;
               break;
            case 1:
               _loc4_ = _loc13_;
               _loc5_ = _loc9_;
               _loc6_ = _loc12_;
               break;
            case 2:
               _loc4_ = _loc12_;
               _loc5_ = _loc9_;
               _loc6_ = _loc14_;
               break;
            case 3:
               _loc4_ = _loc12_;
               _loc5_ = _loc13_;
               _loc6_ = _loc9_;
               break;
            case 4:
               _loc4_ = _loc14_;
               _loc5_ = _loc12_;
               _loc6_ = _loc9_;
               break;
            case 5:
               _loc4_ = _loc9_;
               _loc5_ = _loc12_;
               _loc6_ = _loc13_;
         }
         return [Math.round(_loc4_ * 255),Math.round(_loc5_ * 255),Math.round(_loc6_ * 255)];
      }
      
      public static function method_50(param1:String) : Boolean
      {
         if(param1.toUpperCase() == "TRUE")
         {
            return true;
         }
         return false;
      }
      
      public static function method_2(param1:TextField, param2:String, param3:Boolean = false) : void
      {
         var _loc4_:TextFormat = null;
         if(param1)
         {
            _loc4_ = param1.getTextFormat();
            if(param3)
            {
               param1.htmlText = !!param2 ? param2 : "";
            }
            else
            {
               param1.text = !!param2 ? param2 : "";
               param1.defaultTextFormat = _loc4_;
               param1.setTextFormat(_loc4_);
            }
         }
      }
      
      public static function method_2025(param1:MovieClip, param2:String) : uint
      {
         var _loc3_:FrameLabel = null;
         var _loc4_:Scene = param1.currentScene;
         var _loc5_:Array;
         var _loc6_:uint = (_loc5_ = param1.scenes[0].labels).length;
         var _loc7_:uint = 0;
         while(_loc7_ < _loc6_)
         {
            _loc3_ = _loc5_[_loc7_];
            if(_loc3_.name == param2)
            {
               return _loc3_.frame;
            }
            _loc7_++;
         }
         return 0;
      }
      
      public static function method_2089(param1:Dictionary) : void
      {
         var _loc3_:String = null;
         var _loc2_:* = "Dictionary {";
         for(_loc3_ in param1)
         {
            _loc2_ += _loc3_ + ": " + param1[_loc3_] + ", ";
         }
         _loc2_ += "}";
      }
      
      public static function method_2143(param1:uint) : String
      {
         var _loc2_:uint = param1 % 10;
         param1 = uint(param1 / 10);
         var _loc3_:uint = param1 % 60;
         var _loc5_:*;
         var _loc4_:uint;
         return (_loc5_ = (_loc5_ = (_loc4_ = uint(param1 / 60)) + ":") + (_loc3_ < 10 ? "0" + _loc3_ : _loc3_)) + ("." + _loc2_);
      }
      
      public static function method_29(param1:int, param2:Boolean = false) : String
      {
         var _loc3_:String = param1.toString();
         var _loc4_:uint;
         if((_loc4_ = uint(_loc3_.length)) <= 3 || !param2 && _loc4_ <= 4)
         {
            return _loc3_;
         }
         var _loc5_:String = "";
         var _loc6_:uint = (_loc4_ - 1) / 3;
         var _loc7_:uint = 1;
         while(_loc7_ <= _loc6_)
         {
            _loc5_ = "," + _loc3_.substr(_loc7_ * -3,3) + _loc5_;
            _loc7_++;
         }
         return _loc3_.substr(0,_loc4_ - _loc6_ * 3) + _loc5_;
      }
      
      public static function method_259(param1:String) : String
      {
         var _loc2_:* = param1.indexOf("<") != -1;
         var _loc3_:* = param1.indexOf(">") != -1;
         if(_loc2_)
         {
            param1 = param1.split("<").join("&lt;");
         }
         if(_loc3_)
         {
            param1 = param1.split(">").join("&gt;");
         }
         return param1;
      }
      
      public static function method_235(param1:DisplayObjectContainer) : void
      {
         if(!param1)
         {
            return;
         }
         var _loc2_:MovieClip = param1 as MovieClip;
         if(_loc2_)
         {
            _loc2_.gotoAndStop(1);
         }
         var _loc3_:uint = uint(param1.numChildren);
         var _loc4_:uint = 0;
         while(_loc4_ < _loc3_)
         {
            method_235(param1.getChildAt(_loc4_) as DisplayObjectContainer);
            _loc4_++;
         }
      }
      
      public static function method_2056(param1:Point) : Number
      {
         var _loc2_:Number = Math.sqrt(param1.x * param1.x + param1.y * param1.y);
         param1.x /= _loc2_;
         param1.y /= _loc2_;
         return _loc2_;
      }
      
      public static function method_1401(param1:uint) : String
      {
         var _loc2_:int = param1 / (60 * 60);
         var _loc3_:int = param1 % (60 * 60);
         var _loc4_:int = _loc3_ / 60;
         var _loc5_:int = param1 % 60;
         return _loc2_ + ":" + method_371(_loc4_) + ":" + method_371(_loc5_);
      }
      
      public static function method_2093(param1:uint) : String
      {
         var _loc2_:uint = param1 / (60 * 60 * 24);
         var _loc3_:uint = param1 % (60 * 60 * 24);
         var _loc4_:uint = _loc3_ / (60 * 60);
         var _loc5_:uint;
         var _loc6_:uint = (_loc5_ = param1 % (60 * 60)) / 60;
         var _loc7_:uint = param1 % 60;
         if(_loc5_ > 0)
         {
            if((_loc4_ += 1) >= 24)
            {
               _loc4_ = 0;
               _loc2_ += 1;
            }
         }
         if(_loc2_)
         {
            return String(_loc2_) + "d";
         }
         if(_loc4_)
         {
            return String(_loc4_) + "h";
         }
         if(_loc6_)
         {
            return String(_loc6_) + "m";
         }
         return String(_loc7_) + "s";
      }
      
      private static function method_371(param1:uint) : String
      {
         if(param1 < 10)
         {
            return "0" + String(param1);
         }
         return String(param1);
      }
      
      public static function method_1884(param1:Number = 1) : ColorMatrixFilter
      {
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         var _loc6_:Array = null;
         var _loc2_:ColorMatrixFilter = const_739[param1];
         if(!_loc2_)
         {
            _loc3_ = 0.212671;
            _loc4_ = 0.71516;
            _loc5_ = 0.072169;
            _loc6_ = [_loc3_,_loc4_,_loc5_,0,0,_loc3_,_loc4_,_loc5_,0,0,_loc3_,_loc4_,_loc5_,0,0,0,0,0,param1,0];
            _loc2_ = new ColorMatrixFilter(_loc6_);
            const_739[param1] = _loc2_;
         }
         return _loc2_;
      }
      
      public static function method_1892(param1:MovieClip, param2:DisplayObject, param3:String, param4:String) : void
      {
         param2.filters = null;
         var _loc5_:String = getQualifiedClassName(param1);
         var _loc6_:String = param3.charAt(0) == "a" ? param3 : "?";
         var _loc7_:String = param4.charAt(0) == "a" ? param4 : "?";
         class_24.method_19(_loc5_ + ": filter on " + _loc6_ + "(" + _loc7_ + ") in " + (getQualifiedClassName(param2.parent) == _loc5_ ? "ROOT" : ""));
         var _loc8_:DisplayObject = param2.parent;
         while(Boolean(_loc8_) && getQualifiedClassName(_loc8_) != _loc5_)
         {
            class_24.method_19("--" + getQualifiedClassName(_loc8_) + "(" + (_loc8_.name.charAt(0) == "a" ? _loc8_.name : "?") + ")");
            _loc8_ = _loc8_.parent;
         }
      }
      
      public static function method_138(param1:DisplayObject, param2:DisplayObject) : Rectangle
      {
         var _loc9_:Number = NaN;
         var _loc10_:Number = NaN;
         var _loc11_:Number = NaN;
         var _loc12_:Number = NaN;
         if(!param1.visible)
         {
            return null;
         }
         var _loc3_:DisplayObjectContainer = param1 as DisplayObjectContainer;
         return param1.getBounds(param2);
      }
      
      public static function method_8(param1:TextField, param2:String, param3:uint, param4:int = -1) : void
      {
         var _loc5_:GlowFilter = null;
         if(!param1)
         {
            return;
         }
         param1.textColor = param3;
         if(param4 > -1)
         {
            (_loc5_ = param1.filters[0]).color = param4;
            param1.filters = [_loc5_];
         }
         method_2(param1,param2);
      }
      
      public static function method_69() : Sprite
      {
         var _loc1_:Sprite = new Sprite();
         _loc1_.mouseEnabled = false;
         _loc1_.mouseChildren = false;
         return _loc1_;
      }
      
      public static function method_2140(param1:Number, param2:Number, param3:Number) : Number
      {
         var _loc4_:Number = NaN;
         if(param1 > param2)
         {
            _loc4_ = param1 < param3 ? param1 : (param3 > param2 ? param3 : param2);
         }
         else
         {
            _loc4_ = param2 < param3 ? param2 : (param3 > param1 ? param3 : param1);
         }
         return _loc4_;
      }
      
      public static function method_2022(param1:uint, param2:uint, param3:Number = 0.5) : Number
      {
         var _loc4_:Number = 1 - param3;
         var _loc5_:Number = (param1 >> 16) * param3 + (param2 >> 16) * _loc4_;
         var _loc6_:Number = (param1 >> 8 & 255) * param3 + (param2 >> 8 & 255) * _loc4_;
         var _loc7_:Number = (param1 & 255) * param3 + (param2 & 255) * _loc4_;
         return (_loc5_ << 16) + (_loc6_ << 8) + _loc7_;
      }
      
      public static function method_2075(param1:*, param2:Function) : void
      {
         var _loc3_:Object = null;
         var _loc4_:uint = 0;
         var _loc5_:uint = uint(param1.length);
         var _loc6_:uint = 0;
         while(_loc6_ < _loc5_)
         {
            _loc3_ = param1[_loc6_];
            _loc4_ = param2() * _loc5_;
            param1[_loc6_] = param1[_loc4_];
            param1[_loc4_] = _loc3_;
            _loc6_++;
         }
      }
      
      public static function method_2142(param1:uint) : String
      {
         var _loc3_:uint = 0;
         var _loc2_:String = "th";
         if(param1 < 4 || param1 > 20)
         {
            _loc3_ = param1 % 10;
            switch(_loc3_)
            {
               case 1:
                  _loc2_ = "st";
                  break;
               case 2:
                  _loc2_ = "nd";
                  break;
               case 3:
                  _loc2_ = "rd";
            }
         }
         return String(param1) + _loc2_;
      }
   }
}
