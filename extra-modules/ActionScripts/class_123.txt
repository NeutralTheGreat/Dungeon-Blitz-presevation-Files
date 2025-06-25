package
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.geom.ColorTransform;
   import flash.geom.Matrix;
   import flash.geom.Rectangle;
   import flash.utils.getQualifiedClassName;
   
   public class class_123
   {
      
      private static const const_1252:String = "am_Platform_";
      
      public static const const_862:String = "am_Parallax";
      
      public static const const_1206:String = "a_Scene_";
      
      public static const const_718:String = "a_Animation";
      
      public static const const_988:String = "am_Platform";
      
      public static const const_608:String = "baseAnim";
      
      public static const const_635:String = "moveAnimSpeed";
      
      public static const const_636:String = "startAnim";
       
      
      internal var var_1:Game;
      
      internal var var_849:Vector.<class_162>;
      
      internal var var_595:Vector.<class_147>;
      
      internal var var_1489:Vector.<class_161>;
      
      internal var var_589:Sprite;
      
      internal var var_572:Sprite;
      
      internal var var_592:Sprite;
      
      internal var var_829:Sprite;
      
      internal var var_891:Sprite;
      
      internal var var_1095:Sprite;
      
      internal var var_2374:Boolean = false;
      
      public function class_123(param1:Game)
      {
         this.var_849 = new Vector.<class_162>();
         this.var_595 = new Vector.<class_147>();
         this.var_1489 = new Vector.<class_161>();
         super();
         this.var_1 = param1;
         this.var_589 = MathUtil.method_69();
         this.var_572 = MathUtil.method_69();
         this.var_592 = MathUtil.method_69();
         this.var_829 = MathUtil.method_69();
         this.var_891 = MathUtil.method_69();
         this.var_1095 = MathUtil.method_69();
      }
      
      public function method_1963() : void
      {
         this.method_929();
         this.var_849 = null;
         this.var_595 = null;
         this.var_1 = null;
         if(this.var_589.parent)
         {
            this.var_589.parent.removeChild(this.var_589);
         }
         this.var_589 = null;
         if(this.var_572.parent)
         {
            this.var_572.parent.removeChild(this.var_572);
         }
         this.var_572 = null;
         if(this.var_592.parent)
         {
            this.var_592.parent.removeChild(this.var_592);
         }
         this.var_592 = null;
         if(this.var_891.parent)
         {
            this.var_891.parent.removeChild(this.var_891);
         }
         this.var_891 = null;
         if(this.var_829.parent)
         {
            this.var_829.parent.removeChild(this.var_829);
         }
         this.var_829 = null;
         if(this.var_1095.parent)
         {
            this.var_1095.parent.removeChild(this.var_1095);
         }
         this.var_1095 = null;
      }
      
      public function method_929() : void
      {
         var _loc1_:class_160 = null;
         var _loc2_:class_162 = null;
         var _loc3_:class_147 = null;
         var _loc4_:class_161 = null;
         for each(_loc2_ in this.var_849)
         {
            for each(_loc1_ in _loc2_.var_1244)
            {
               this.var_1.var_171.method_488(_loc1_.var_954);
               _loc1_.method_1263();
            }
            _loc2_.method_1695();
         }
         this.var_849 = new Vector.<class_162>();
         for each(_loc3_ in this.var_595)
         {
            _loc3_.superAnim.m_Data.method_261();
            _loc3_.method_720();
         }
         this.var_595 = new Vector.<class_147>();
         for each(_loc4_ in this.var_1489)
         {
            _loc4_.method_1053();
         }
         this.var_1489 = new Vector.<class_161>();
      }
      
      public function method_1693(param1:Vector.<Sprite>) : void
      {
         var _loc2_:MovieClip = null;
         var _loc3_:int = 0;
         var _loc4_:Sprite = null;
         var _loc5_:Array = null;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         if(param1.length)
         {
            _loc2_ = new MovieClip();
            _loc2_.name = "am_GlobalParallax";
            this.var_1.level.var_59.addChild(_loc2_);
            _loc3_ = 0;
            while(_loc3_ < param1.length)
            {
               _loc2_.addChild(param1[_loc3_]);
               _loc5_ = (_loc4_ = param1[_loc3_]).name.split("_");
               _loc6_ = int(_loc5_[2]) * 0.01;
               _loc7_ = int(_loc5_[3]) * 0.01;
               if(this.var_1.main.var_1976)
               {
                  _loc4_.x = 0;
                  _loc4_.y = 0;
               }
               else
               {
                  _loc4_.x -= 576 - _loc6_ * 576;
                  _loc4_.y -= 334;
               }
               if(_loc7_ != 0)
               {
                  class_24.method_19("Y shift on Global Parallax" + _loc4_.name);
               }
               _loc3_++;
            }
            this.method_802(_loc2_,true,false);
            this.var_1.level.var_59.removeChild(_loc2_);
         }
      }
      
      public function method_802(param1:MovieClip, param2:Boolean = false, param3:Boolean = false) : class_162
      {
         var _loc4_:Rectangle = null;
         var _loc9_:MovieClip = null;
         var _loc10_:class_162 = null;
         var _loc11_:Sprite = null;
         var _loc12_:String = null;
         var _loc5_:Vector.<MovieClip> = new Vector.<MovieClip>();
         var _loc6_:uint = uint(param1.numChildren);
         if(param1.scaleX != 1 || param1.scaleY != 1)
         {
            class_24.method_19("No Scaling is allowed on scene objects!: " + getQualifiedClassName(param1));
         }
         var _loc7_:int = 0;
         while(_loc7_ < _loc6_)
         {
            if((_loc12_ = (_loc11_ = param1.getChildAt(_loc7_) as Sprite).name) == "am_Frame")
            {
               if(_loc4_)
               {
                  class_24.method_19("Multiple am_Frame objects exist inside Scene: " + getQualifiedClassName(param1));
               }
               _loc4_ = _loc11_.getRect(_loc11_.stage);
            }
            else if(_loc12_.indexOf("am_Parallax"))
            {
               class_24.method_19("Unknown object: " + _loc12_ + " in Scene: " + getQualifiedClassName(param1));
            }
            else
            {
               if(_loc11_.scaleX > 0.99 && _loc11_.scaleX < 1.01)
               {
                  _loc11_.scaleX = 1;
               }
               if(_loc11_.scaleY > 0.99 && _loc11_.scaleY < 1.01)
               {
                  _loc11_.scaleY = 1;
               }
               _loc5_.push(_loc11_);
            }
            _loc7_++;
         }
         if(!_loc5_.length)
         {
            class_24.method_19("No parallax objects found inside Scene: " + getQualifiedClassName(param1));
            return null;
         }
         var _loc8_:Vector.<class_160> = new Vector.<class_160>();
         for each(_loc9_ in _loc5_)
         {
            _loc8_.push(this.method_1315(_loc9_));
         }
         _loc8_.fixed = true;
         (_loc10_ = new class_162()).var_2628 = param1.x;
         _loc10_.var_2829 = param1.y;
         _loc10_.var_2406 = _loc4_;
         _loc10_.var_1244 = _loc8_;
         if(param2)
         {
            this.var_849.unshift(_loc10_);
         }
         else
         {
            this.var_849.push(_loc10_);
         }
         if(param3)
         {
            _loc10_.var_2740 = true;
         }
         return _loc10_;
      }
      
      private function method_1315(param1:MovieClip) : class_160
      {
         var _loc2_:Array = param1.name.split("$");
         var _loc3_:String = String(_loc2_[0]);
         var _loc4_:Array = _loc3_.split("_");
         var _loc5_:Number = Number(_loc4_[2]) * 0.01;
         var _loc6_:Number = Number(_loc4_[3]) * 0.01;
         var _loc7_:class_160;
         (_loc7_ = new class_160(param1.x,param1.y,_loc5_,_loc6_)).var_954 = this.var_1.var_171.method_412(param1,true,false,false,getQualifiedClassName(param1));
         return _loc7_;
      }
      
      public function method_482(param1:Sprite, param2:String) : MagicObject
      {
         var _loc3_:Rectangle = MathUtil.method_138(param1,param1);
         if(!_loc3_)
         {
            param1.parent.removeChild(param1);
            return null;
         }
         if(_loc3_.width > class_82.const_503 || _loc3_.height > class_82.const_503)
         {
            class_24.method_19("Too big Xground object: x:" + _loc3_.width + " y:" + _loc3_.height + " " + param1.name + "in " + getQualifiedClassName(param1.parent) + " -MAX " + class_82.const_503);
         }
         var _loc4_:Matrix = param1.transform.concatenatedMatrix;
         var _loc5_:ColorTransform = param1.transform.concatenatedColorTransform;
         param1.transform.matrix = _loc4_;
         param1.transform.colorTransform = _loc5_;
         var _loc6_:Sprite;
         (_loc6_ = new Sprite()).addChild(param1);
         return this.var_1.var_171.method_412(_loc6_,false,false,false,null,param2);
      }
      
      public function method_711(param1:Sprite, param2:int, param3:String) : void
      {
         var _loc4_:MagicObject;
         if(_loc4_ = this.method_482(param1,param3))
         {
            this.var_592.addChildAt(_loc4_.var_51,param2);
         }
      }
      
      public function method_948(param1:Sprite, param2:int, param3:String) : void
      {
         var _loc4_:MagicObject;
         if(_loc4_ = this.method_482(param1,param3))
         {
            this.var_572.addChildAt(_loc4_.var_51,param2);
         }
      }
      
      public function method_914(param1:Sprite, param2:int, param3:String) : void
      {
         var _loc4_:MagicObject;
         if(_loc4_ = this.method_482(param1,param3))
         {
            this.var_589.addChildAt(_loc4_.var_51,param2);
         }
      }
      
      public function method_625(param1:MovieClip, param2:String, param3:String, param4:String, param5:Matrix, param6:String, param7:Boolean, param8:Boolean) : class_147
      {
         var _loc19_:String = null;
         var _loc9_:String = param1.hasOwnProperty(const_608) ? String(param1[const_608]) : null;
         var _loc10_:Number = param1.hasOwnProperty(const_635) ? Number(param1[const_635]) : 1;
         var _loc11_:String = param1.hasOwnProperty(const_636) ? String(param1[const_636]) : null;
         var _loc12_:GfxType;
         (_loc12_ = new GfxType()).var_29 = param4;
         _loc12_.animClass = param2;
         _loc12_.bFireAndForget = false;
         _loc12_.bRandomFrameStart = true;
         _loc12_.moveAnimSpeed = _loc10_;
         _loc12_.var_1126 = true;
         _loc12_.var_527 = true;
         if(_loc9_)
         {
            _loc12_.baseAnim = _loc9_;
         }
         var _loc13_:SuperAnimInstance = new SuperAnimInstance(this.var_1,_loc12_,false);
         var _loc14_:Sprite = param7 ? this.var_592 : (param8 ? this.var_589 : this.var_572);
         _loc13_.m_TheDO.transform.matrix = param5;
         _loc13_.m_TheDO.transform.colorTransform = param1.transform.concatenatedColorTransform;
         if(_loc11_)
         {
            _loc13_.m_Seq.method_34(Seq.C_EMOTE,_loc11_,true);
         }
         _loc14_.addChild(_loc13_.m_TheDO);
         var _loc15_:Rectangle = param1.getBounds(param1.stage);
         var _loc16_:class_147;
         (_loc16_ = new class_147(_loc13_,param3,0.5 * (_loc15_.left + _loc15_.right),0.5 * (_loc15_.top + _loc15_.bottom),_loc15_.width,_loc15_.height)).var_2603 = param6;
         this.var_595.push(_loc16_);
         var _loc18_:*;
         var _loc17_:String;
         if(_loc18_ = !(_loc17_ = param1.name).indexOf(const_988))
         {
            _loc19_ = _loc17_.substr(const_1252.length);
            this.var_1489.push(new class_161(this.var_1,_loc19_,_loc13_));
         }
         return _loc16_;
      }
      
      public function method_1604() : void
      {
         var _loc1_:class_162 = null;
         for each(_loc1_ in this.var_849)
         {
            this.method_1740(_loc1_);
         }
      }
      
      public function method_1740(param1:class_162) : void
      {
         var _loc2_:MagicObject = null;
         var _loc3_:MovieClip = null;
         var _loc4_:class_160 = null;
         for each(_loc4_ in param1.var_1244)
         {
            _loc2_ = _loc4_.var_954;
            this.var_1.var_171.method_193(_loc2_,true);
            _loc3_ = _loc2_.dObj as MovieClip;
            _loc4_.var_2260 = _loc2_.var_51.x - _loc3_.x;
            _loc4_.var_2433 = _loc2_.var_51.y - _loc3_.y;
         }
      }
      
      public function method_1808() : void
      {
         var _loc1_:MagicObject = null;
         var _loc2_:MovieClip = null;
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:class_160 = null;
         var _loc6_:Boolean = false;
         var _loc7_:Sprite = null;
         var _loc8_:Array = null;
         var _loc9_:class_147 = null;
         var _loc10_:class_162 = null;
         var _loc11_:class_161 = null;
         var _loc12_:int = 0;
         var _loc14_:Boolean = false;
         var _loc15_:Rectangle = null;
         var _loc16_:Number = NaN;
         var _loc17_:Number = NaN;
         var _loc18_:Number = NaN;
         var _loc19_:Number = NaN;
         var _loc20_:Number = NaN;
         var _loc21_:Number = NaN;
         var _loc22_:Number = NaN;
         var _loc23_:Number = NaN;
         var _loc24_:Number = NaN;
         var _loc25_:Number = NaN;
         var _loc26_:Number = NaN;
         var _loc27_:class_160 = null;
         if(this.var_2374)
         {
            _loc8_ = new Array();
         }
         for each(_loc9_ in this.var_595)
         {
            _loc7_ = _loc9_.superAnim.m_TheDO;
            _loc6_ = this.var_1.PointOnScreenWithinDist(_loc9_.var_2822,_loc9_.var_2657,_loc9_.width + 150,_loc9_.height + 100);
            if(_loc7_.visible != _loc6_)
            {
               _loc7_.visible = _loc6_;
            }
         }
         for each(_loc10_ in this.var_849)
         {
            _loc14_ = false;
            _loc15_ = _loc10_.var_2406;
            _loc16_ = -this.var_1.levelLayer.x;
            _loc17_ = -this.var_1.levelLayer.y;
            _loc18_ = Camera.SCREEN_WIDTH;
            _loc19_ = Camera.PLAY_SCREEN_HEIGHT;
            if(!_loc10_.var_2949)
            {
               if(!_loc15_)
               {
                  _loc14_ = true;
               }
               else if(!(_loc15_.x > _loc16_ + _loc18_ || _loc15_.x + _loc15_.width < _loc16_) && !(_loc15_.y > _loc17_ + _loc19_ || _loc15_.y + _loc15_.height < _loc17_))
               {
                  _loc14_ = true;
               }
            }
            if(_loc14_)
            {
               for each(_loc5_ in _loc10_.var_1244)
               {
                  _loc1_ = _loc5_.var_954;
                  _loc2_ = _loc1_.dObj as MovieClip;
                  _loc20_ = _loc5_.var_2343 + Camera.SCREEN_WIDTH * 0.5;
                  _loc21_ = _loc5_.var_2423 + Camera.PLAY_SCREEN_HEIGHT * 0.5;
                  _loc22_ = this.var_1.levelLayer.x + _loc10_.var_2628 + _loc5_.var_2343;
                  _loc23_ = this.var_1.levelLayer.y + _loc10_.var_2829 + _loc5_.var_2423;
                  _loc3_ = _loc5_.mRateX;
                  _loc4_ = _loc5_.var_2640;
                  _loc2_.x = _loc20_ * (1 - _loc3_) + _loc22_ * _loc3_;
                  _loc2_.y = _loc21_ * (1 - _loc4_) + _loc23_ * _loc4_;
                  _loc1_.var_51.x = _loc2_.x + _loc5_.var_2260;
                  _loc1_.var_51.y = _loc2_.y + _loc5_.var_2433;
                  _loc25_ = (_loc24_ = this.var_1.main.overallScale) * _loc1_.var_51.x;
                  _loc26_ = _loc24_ * _loc1_.var_51.y;
                  _loc25_ = Math.floor(_loc25_);
                  _loc26_ = Math.floor(_loc26_);
                  _loc25_ /= _loc24_;
                  _loc26_ /= _loc24_;
                  _loc1_.var_51.x = _loc25_;
                  _loc1_.var_51.y = _loc26_;
                  if(!_loc2_.name.indexOf("am_ParallaxForeground"))
                  {
                     if(!_loc10_.var_1242)
                     {
                        this.var_891.addChild(_loc1_.var_51);
                     }
                  }
                  else if(_loc10_.var_2740)
                  {
                     if(!_loc10_.var_1242)
                     {
                        this.var_1095.addChild(_loc1_.var_51);
                     }
                  }
                  else if(this.var_2374)
                  {
                     _loc8_.push(_loc5_);
                  }
                  else if(!_loc10_.var_1242)
                  {
                     this.var_829.addChild(_loc1_.var_51);
                  }
               }
               _loc10_.var_1242 = true;
            }
            else if(_loc10_.var_1242)
            {
               for each(_loc5_ in _loc10_.var_1244)
               {
                  _loc1_ = _loc5_.var_954;
                  if(_loc1_.var_51.parent)
                  {
                     _loc1_.var_51.parent.removeChild(_loc1_.var_51);
                  }
               }
               _loc10_.var_1242 = false;
            }
         }
         if(this.var_2374)
         {
            this.method_1426(_loc8_,"mRateX");
            _loc12_ = 0;
            while(_loc12_ < _loc8_.length)
            {
               _loc27_ = _loc8_[_loc12_];
               this.var_829.addChild(_loc27_.var_954.var_51);
               _loc12_++;
            }
         }
         for each(_loc11_ in this.var_1489)
         {
            _loc11_.method_1259();
         }
      }
      
      public function method_1426(param1:Array, param2:String) : void
      {
         var _loc3_:int = 0;
         var _loc5_:Object = null;
         var _loc4_:int = int(param1.length);
         var _loc6_:Boolean = false;
         while(!_loc6_)
         {
            _loc6_ = true;
            _loc3_ = 0;
            while(_loc3_ < _loc4_ - 1)
            {
               if(Number(param1[_loc3_][param2]) > Number(param1[_loc3_ + 1][param2]))
               {
                  _loc5_ = param1[_loc3_];
                  param1[_loc3_] = param1[_loc3_ + 1];
                  param1[_loc3_ + 1] = _loc5_;
                  _loc3_--;
                  _loc6_ = false;
               }
               _loc3_++;
            }
         }
      }
   }
}
