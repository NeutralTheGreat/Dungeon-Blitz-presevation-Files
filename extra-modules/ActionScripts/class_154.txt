package
{
   import flash.display.*;
   import flash.geom.Point;
   import flash.utils.Dictionary;
   import flash.utils.getQualifiedClassName;
   
   public class class_154
   {
      
      private static const const_1374:uint = 100;
      
      private static var var_1247:int = 1;
      
      private static const const_234:uint = 10;
      
      private static const const_307:Number = 1 / const_234;
      
      private static const const_819:uint = 4;
      
      private static const const_630:uint = 10;
      
      private static const const_1173:Number = 125;
      
      private static var var_383:Point = new Point();
      
      private static var var_302:Point = new Point();
      
      private static var var_1431:Point = new Point();
      
      private static var var_643:Point = new Point();
      
      private static var var_692:Point = new Point();
       
      
      public function class_154()
      {
         super();
      }
      
      public static function method_444(param1:Sprite, param2:Sprite, param3:Dictionary, param4:Room, param5:Dictionary, param6:Boolean, param7:CollisionManager) : void
      {
         var _loc9_:DisplayObject = null;
         var _loc8_:Vector.<IGraphicsData>;
         if((_loc8_ = param1.graphics.readGraphicsData(false)).length)
         {
            class_24.method_7("THIS SPRITE HAS A NONEMPTY GRAPHICS OBJECT. I WAS NOT EXPECTING THAT");
         }
         var _loc10_:int = 0;
         while(_loc10_ < param1.numChildren)
         {
            if((_loc9_ = param1.getChildAt(_loc10_)) is Shape)
            {
               method_679(_loc9_ as Shape,param1,param2,param3,param4,param5,param6,param7);
            }
            else if(_loc9_ is Sprite)
            {
               method_444(_loc9_ as Sprite,param2,param3,param4,param5,param6,param7);
            }
            _loc10_++;
         }
      }
      
      public static function method_679(param1:Shape, param2:Sprite, param3:Sprite, param4:Dictionary, param5:Room, param6:Dictionary, param7:Boolean, param8:CollisionManager) : void
      {
         var _loc9_:GraphicsPath = null;
         var _loc18_:IGraphicsData = null;
         var _loc19_:int = 0;
         var _loc20_:GraphicsStroke = null;
         var _loc21_:GraphicsSolidFill = null;
         var _loc10_:uint = 0;
         var _loc11_:int = 0;
         var _loc12_:int = 0;
         var _loc13_:uint = 0;
         var _loc14_:int = 0;
         var _loc15_:Boolean = false;
         var _loc16_:Vector.<IGraphicsData>;
         var _loc17_:int = int((_loc16_ = param1.graphics.readGraphicsData(false)).length);
         ++var_1247;
         _loc11_ = 0;
         while(_loc11_ < _loc17_)
         {
            if((_loc18_ = _loc16_[_loc11_] as IGraphicsData) is GraphicsPath)
            {
               _loc9_ = _loc18_ as GraphicsPath;
               var_383.x = 0;
               var_383.y = 0;
               var_302.x = 0;
               var_302.y = 0;
               _loc14_ = 0;
               _loc13_ = _loc9_.commands.length;
               _loc12_ = 0;
               while(_loc12_ < _loc13_)
               {
                  if((_loc19_ = _loc9_.commands[_loc12_]) == GraphicsPathCommand.CURVE_TO)
                  {
                     var_1431.x = _loc9_.data[_loc14_++];
                     var_1431.y = _loc9_.data[_loc14_++];
                     var_302.x = _loc9_.data[_loc14_++];
                     var_302.y = _loc9_.data[_loc14_++];
                     if(!_loc15_)
                     {
                        class_24.method_7("ROOM " + getQualifiedClassName(param5.var_150) + " No line color set in collision object?");
                     }
                     method_346(var_383,var_302,var_1431,_loc10_,param2,param3,param4,param5,param6,param7,param8);
                     var_383.x = var_302.x;
                     var_383.y = var_302.y;
                  }
                  else if(_loc19_ == GraphicsPathCommand.MOVE_TO)
                  {
                     var_383.x = _loc9_.data[_loc14_++];
                     var_383.y = _loc9_.data[_loc14_++];
                  }
                  else if(_loc19_ == GraphicsPathCommand.LINE_TO)
                  {
                     var_302.x = _loc9_.data[_loc14_++];
                     var_302.y = _loc9_.data[_loc14_++];
                     if(!_loc15_)
                     {
                        class_24.method_7("ROOM " + getQualifiedClassName(param5.var_150) + " No line color set in collision object?");
                     }
                     method_346(var_383,var_302,null,_loc10_,param2,param3,param4,param5,param6,param7,param8);
                     var_383.x = var_302.x;
                     var_383.y = var_302.y;
                  }
                  else if(_loc19_ != GraphicsPathCommand.NO_OP)
                  {
                     class_24.method_7("ROOM " + getQualifiedClassName(param5.var_150) + " has a messed up collision object. Either it\'s not alone on the top layer, or its got garbage in it");
                  }
                  _loc12_++;
               }
            }
            else if(_loc18_ is GraphicsStroke)
            {
               if(_loc21_ = (_loc20_ = _loc18_ as GraphicsStroke).fill as GraphicsSolidFill)
               {
                  _loc10_ = _loc21_.color;
                  _loc15_ = true;
               }
               if(!_loc21_ && Boolean(_loc20_.fill))
               {
                  class_24.method_7("This is not a Graphics Solid Fill Strange");
               }
            }
            _loc11_++;
         }
      }
      
      private static function method_346(param1:Point, param2:Point, param3:Point, param4:uint, param5:Sprite, param6:Sprite, param7:Dictionary, param8:Room, param9:Dictionary, param10:Boolean, param11:CollisionManager) : void
      {
         var _loc13_:Point = null;
         var _loc14_:uint = 0;
         var _loc15_:Vector.<String> = null;
         var _loc16_:Vector.<String> = null;
         var _loc17_:int = 0;
         var _loc18_:uint = 0;
         var _loc19_:String = null;
         var _loc20_:Array = null;
         var _loc21_:String = null;
         var _loc22_:String = null;
         var _loc23_:Array = null;
         var _loc24_:String = null;
         var _loc25_:uint = 0;
         var _loc26_:uint = 0;
         var _loc27_:String = null;
         var _loc28_:Number = NaN;
         var _loc29_:Number = NaN;
         var _loc30_:uint = 0;
         var _loc31_:uint = 0;
         var _loc32_:Number = NaN;
         var _loc33_:Number = NaN;
         var _loc34_:Number = NaN;
         var _loc35_:Number = NaN;
         var _loc36_:Number = NaN;
         var _loc37_:Number = NaN;
         var _loc12_:uint = uint(CollisionManager.const_582[param4]);
         param1 = param5.localToGlobal(param1);
         param2 = param5.localToGlobal(param2);
         if(param3)
         {
            param3 = param5.localToGlobal(param3);
         }
         if(param1.x > param2.x)
         {
            _loc13_ = param2;
            param2 = param1;
            param1 = _loc13_;
         }
         param1.x = Math.round(param1.x * const_307) * const_234;
         param1.y = Math.round(param1.y * const_307) * const_234;
         param2.x = Math.round(param2.x * const_307) * const_234;
         param2.y = Math.round(param2.y * const_307) * const_234;
         if(param1.x != param2.x || param1.y != param2.y)
         {
            _loc14_ = 0;
            _loc15_ = null;
            _loc16_ = null;
            _loc17_ = 0;
            if(!(_loc19_ = param5.name).indexOf("am_") && _loc19_ != "am_CollisionObject" && _loc19_ != "am_CollisionLayer")
            {
               _loc20_ = _loc19_.split("$");
               for each(_loc21_ in _loc20_)
               {
                  if(_loc21_.indexOf("am_"))
                  {
                     class_24.method_19("BadLineName Bad Convention: " + _loc21_ + " @ (" + Math.round(param1.x) + ", " + Math.round(param1.y) + ") - (" + Math.round(param2.x) + ", " + Math.round(param2.y) + ")");
                  }
                  else if((_loc24_ = String((_loc23_ = (_loc22_ = _loc21_.substr(3)).split("_"))[0])) == "DynamicCollision")
                  {
                     if(!_loc16_)
                     {
                        _loc16_ = new Vector.<String>();
                     }
                     _loc16_.push(_loc21_);
                  }
                  else if(_loc24_ == "Water")
                  {
                     if(_loc23_[1] == "Blue")
                     {
                        _loc14_ |= class_37.const_464;
                     }
                     else
                     {
                        _loc14_ |= class_37.const_439;
                     }
                  }
                  else if(_loc24_ == "Ice")
                  {
                     _loc14_ |= class_37.const_782;
                  }
                  else if(_loc24_ == "Metal")
                  {
                     _loc14_ |= class_37.const_704;
                  }
                  else if(_loc24_ == "Wood")
                  {
                     _loc14_ |= class_37.const_786;
                  }
                  else if(_loc24_ == "Puddle")
                  {
                     _loc14_ |= class_37.const_706;
                  }
                  else if(_loc24_ == "RopeBridge")
                  {
                     _loc14_ |= class_37.const_638;
                  }
                  else if(CollisionManager.const_82[_loc24_])
                  {
                     if(!_loc15_)
                     {
                        _loc15_ = new Vector.<String>();
                     }
                     _loc15_.push(_loc22_);
                     if(_loc24_ == "Badge")
                     {
                        _loc25_ = 0.5 * (param1.x + param2.x);
                        _loc26_ = 0.5 * (param1.y + param2.y);
                        _loc27_ = String(_loc23_[1]);
                        if(param9)
                        {
                           param9[_loc27_] = new Point(_loc25_,_loc26_);
                        }
                        else
                        {
                           class_24.method_19("Badge Collision line, but this game doesn\'t support badges!: " + getQualifiedClassName(param6));
                        }
                     }
                  }
                  else if(_loc24_.indexOf("CameraZone") != -1)
                  {
                     _loc17_ = var_1247;
                  }
                  else if(_loc24_ == "Team")
                  {
                     _loc18_ = uint(_loc23_[1]);
                  }
                  else
                  {
                     class_24.method_19("BadLineName NoSuch: " + getQualifiedClassName(param6) + " => (" + _loc21_ + ")");
                  }
               }
            }
            if(!param3)
            {
               method_192(param1,param2,_loc12_,_loc14_,_loc15_,param8,_loc17_,param11,_loc16_,param7,param10,_loc18_);
            }
            else
            {
               _loc28_ = Math.abs(param2.x - param3.x) + Math.abs(param1.x - param3.x);
               _loc29_ = Math.abs(param2.y - param3.y) + Math.abs(param1.y - param3.y);
               if((_loc30_ = Math.round((_loc28_ + _loc29_) / const_1173)) < const_819)
               {
                  _loc30_ = const_819;
               }
               else if(_loc30_ > const_630)
               {
                  _loc30_ = const_630;
               }
               var_643.x = param1.x;
               var_643.y = param1.y;
               _loc31_ = 1;
               while(_loc31_ <= _loc30_)
               {
                  _loc32_ = _loc31_ / _loc30_;
                  _loc33_ = 1 - _loc32_;
                  _loc34_ = (param3.x - param1.x) * _loc32_;
                  _loc35_ = (param3.x - param2.x) * _loc33_;
                  var_692.x = (param1.x + _loc34_) * _loc33_ + (param2.x + _loc35_) * _loc32_;
                  _loc36_ = (param3.y - param1.y) * _loc32_;
                  _loc37_ = (param3.y - param2.y) * _loc33_;
                  var_692.y = (param1.y + _loc36_) * _loc33_ + (param2.y + _loc37_) * _loc32_;
                  if(var_643.x <= var_692.x)
                  {
                     method_192(var_643,var_692,_loc12_,_loc14_,_loc15_,param8,_loc17_,param11,_loc16_,param7,param10,_loc18_);
                  }
                  else
                  {
                     method_192(var_692,var_643,_loc12_,_loc14_,_loc15_,param8,_loc17_,param11,_loc16_,param7,param10,_loc18_);
                  }
                  var_643.x = var_692.x;
                  var_643.y = var_692.y;
                  _loc31_++;
               }
            }
         }
      }
      
      private static function method_192(param1:Point, param2:Point, param3:uint, param4:uint, param5:Vector.<String>, param6:Room, param7:int, param8:CollisionManager, param9:Vector.<String>, param10:Dictionary, param11:Boolean, param12:uint) : void
      {
         var _loc14_:String = null;
         var _loc15_:Array = null;
         var _loc13_:class_37 = new class_37(param1,param2,param3,param4,param5,param6,param7,param12);
         if(Boolean(param9) && param11)
         {
            param8.method_1522(_loc13_);
         }
         else
         {
            param8.method_1952(_loc13_);
         }
         if(param9)
         {
            for each(_loc14_ in param9)
            {
               if(!(_loc15_ = param10[_loc14_]))
               {
                  _loc15_ = param10[_loc14_] = new Array();
               }
               _loc15_.push(_loc13_);
            }
         }
      }
   }
}
