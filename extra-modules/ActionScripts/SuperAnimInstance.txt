package
{
   import flash.display.Bitmap;
   import flash.display.DisplayObject;
   import flash.display.PixelSnapping;
   import flash.display.Sprite;
   import flash.geom.ColorTransform;
   import flash.geom.Matrix;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.utils.Dictionary;
   import flash.utils.getTimer;
   
   public class SuperAnimInstance
   {
      
      public static var var_1683:Array = new Array();
      
      public static const MAGIC_CAPE_SCALER:Number = 0.25;
      
      private static const const_936:Array = ["0x262626","0x363636"];
      
      private static const TIME_TO_STOP_RENDERING:int = 40;
      
      public static const const_347:int = 20;
      
      internal static var var_1821:Dictionary = new Dictionary();
       
      
      internal var var_1:Game;
      
      internal var m_TheDO:Sprite;
      
      internal var var_128:Sprite;
      
      internal var var_166:SuperAnimInstance = null;
      
      internal var m_Seq:Seq;
      
      internal var var_285:Rectangle = null;
      
      internal var var_1029:Boolean;
      
      internal var var_151:Bitmap = null;
      
      internal var m_Sprite:Sprite = null;
      
      internal var var_131:SuperAnimInstance = null;
      
      internal var var_210:SuperAnimInstance = null;
      
      internal var var_1316:SuperAnimInstance = null;
      
      internal var var_184:SuperAnimInstance = null;
      
      internal var m_Data:SuperAnimData;
      
      internal var var_615:Number = 1;
      
      internal var var_1726:Boolean = false;
      
      internal var m_bFinished:Boolean = false;
      
      internal var var_1076:Boolean = false;
      
      internal var var_1843:uint;
      
      internal const const_1194:uint = 2500;
      
      internal var var_1971:Boolean = false;
      
      internal var var_1345:uint = 2500;
      
      internal var var_1380:Boolean = false;
      
      internal var var_1366:Boolean = false;
      
      internal var var_2500:uint = 250;
      
      internal var var_917:Number = 0;
      
      internal var var_1854:Number = 0;
      
      public function SuperAnimInstance(param1:Game, param2:GfxType, param3:Boolean, param4:Boolean = false)
      {
         super();
         this.var_1 = param1;
         this.m_Data = SuperAnimData.method_939(param2);
         this.var_1726 = param3;
         this.var_151 = new Bitmap(null,PixelSnapping.AUTO,false);
         if(this.var_1.main.var_1976)
         {
            this.var_151.smoothing = true;
            this.var_151.pixelSnapping = PixelSnapping.NEVER;
         }
         this.m_TheDO = new Sprite();
         this.m_TheDO.mouseEnabled = false;
         this.m_TheDO.mouseChildren = false;
         this.m_Sprite = new Sprite();
         this.m_Sprite.mouseEnabled = false;
         this.m_Sprite.mouseChildren = false;
         this.m_TheDO.addChild(this.m_Sprite);
         if(param2.var_918)
         {
            this.method_1726(param2,param4);
         }
         if(param2.var_1526)
         {
            this.method_1689();
         }
         this.m_Seq = new Seq(param2);
         if(!param4)
         {
            this.var_1.var_961.push(this);
         }
      }
      
      public function DestroySuperAnimInstance() : void
      {
         this.m_Data = null;
         if(this.var_131)
         {
            this.var_131.DestroySuperAnimInstance();
         }
         this.var_131 = null;
         if(this.var_210)
         {
            this.var_210.DestroySuperAnimInstance();
         }
         this.var_210 = null;
         if(this.var_1316)
         {
            this.var_1316.DestroySuperAnimInstance();
         }
         this.var_1316 = null;
         if(this.var_184)
         {
            this.var_184.DestroySuperAnimInstance();
         }
         this.var_184 = null;
         if(this.var_166)
         {
            this.var_166.DestroySuperAnimInstance();
         }
         this.var_166 = null;
         if(Boolean(this.var_151) && Boolean(this.var_151.parent))
         {
            this.var_151.parent.removeChild(this.var_151);
         }
         this.var_151 = null;
         if(this.m_Seq)
         {
            this.m_Seq.method_399();
         }
         this.m_Seq = null;
         this.method_295(null);
         if(Boolean(this.m_TheDO) && Boolean(this.m_TheDO.parent))
         {
            this.m_TheDO.parent.removeChild(this.m_TheDO);
         }
         this.m_TheDO = null;
         if(this.m_Sprite)
         {
            while(this.m_Sprite.numChildren)
            {
               this.m_Sprite.removeChildAt(0);
            }
            this.m_Sprite = null;
         }
         this.var_285 = null;
         this.var_1 = null;
         this.m_bFinished = true;
      }
      
      public function method_1689() : void
      {
         var _loc2_:Number = this.m_Data.var_36.animScale;
         _loc2_ = Number(int(_loc2_ * 4) / int(4));
         _loc2_ += _loc2_ / (4 * 2);
         var _loc3_:GfxType = var_1821[_loc2_];
         if(!_loc3_)
         {
            _loc3_ = new GfxType();
            _loc3_.var_29 = "SFX_1.swf";
            _loc3_.bFireAndForget = false;
            _loc3_.animClass = "a_SpiritGlow";
            _loc3_.var_177 = 0;
            _loc3_.animScale = _loc2_;
            var_1821[_loc2_] = _loc3_;
         }
         this.var_1316 = new SuperAnimInstance(this.var_1,_loc3_,false);
         this.m_TheDO.addChildAt(this.var_1316.m_TheDO,0);
      }
      
      public function method_1726(param1:GfxType, param2:Boolean) : void
      {
         var _loc5_:CustomArt = null;
         var _loc8_:ColorSwap = null;
         var _loc9_:int = 0;
         var _loc10_:String = null;
         var _loc11_:GfxType = null;
         var _loc3_:String = param1.var_29;
         var _loc4_:String = "a_Cape";
         var _loc6_:int = int(param1.customArts.length - 1);
         while(_loc6_ >= 0)
         {
            _loc5_ = param1.customArts[_loc6_];
            if(this.m_Data.method_334("a_Cape",_loc5_.fileName,_loc5_.setName))
            {
               _loc3_ = _loc5_.fileName;
               _loc4_ = "a_Cape_" + _loc5_.setName;
               break;
            }
            _loc6_--;
         }
         var _loc7_:int = 0;
         for each(_loc8_ in this.m_Data.var_36.colorSwaps)
         {
            if(_loc8_.var_1354 == 2500134 && (_loc8_.var_1150 == SuperAnimData.var_1363 || _loc8_.var_1150 <= 0))
            {
               _loc7_ = int(_loc8_.var_411);
               break;
            }
         }
         _loc9_ = int(this.m_Data.var_36.animScale * 5 + 0.5);
         _loc10_ = _loc3_ + "^" + _loc4_ + "^" + String(_loc7_) + "^" + String(_loc9_);
         if(!(_loc11_ = var_1683[_loc10_]))
         {
            (_loc11_ = new GfxType()).animClass = _loc4_;
            _loc11_.var_29 = _loc3_;
            _loc11_.colorSwaps = this.m_Data.var_36.colorSwaps;
            _loc11_.bRandomFrameStart = true;
            _loc11_.var_1126 = true;
            _loc11_.animScale = this.m_Data.var_36.animScale;
            if(_loc3_ == "Animation_Rogue.swf")
            {
               _loc11_.animScale *= MAGIC_CAPE_SCALER;
            }
            var_1683[_loc10_] = _loc11_;
         }
         this.var_131 = new SuperAnimInstance(this.var_1,_loc11_,this.var_1726,param2);
         this.var_131.m_Data.var_1221 = SuperAnimData.method_402(this.var_131.m_Data.var_1221,const_936,SuperAnimData.var_1363);
         this.var_131.var_151.smoothing = true;
         this.m_TheDO.addChildAt(this.var_131.m_TheDO,0);
      }
      
      public function method_295(param1:String) : void
      {
         var _loc2_:Array = null;
         var _loc3_:String = null;
         var _loc4_:String = null;
         var _loc5_:Object = null;
         var _loc6_:Class = null;
         if(Boolean(this.var_128) && Boolean(this.var_128.parent))
         {
            this.var_128.parent.removeChild(this.var_128);
         }
         this.var_128 = null;
         if(Boolean(param1) && param1 != "None")
         {
            _loc2_ = param1.split("/");
            if(_loc2_.length == 1)
            {
               _loc3_ = "SFX_1.swf";
               _loc4_ = String(_loc2_[0]);
            }
            else
            {
               _loc3_ = String(_loc2_[0]);
               _loc4_ = String(_loc2_[1]);
            }
            if(_loc5_ = ResourceManager.const_40[_loc3_])
            {
               _loc6_ = _loc5_.applicationDomain.getDefinition(_loc4_);
               this.var_128 = new _loc6_();
               this.var_128.mouseEnabled = false;
               this.var_128.mouseChildren = false;
               this.var_128.name = "the_Shadow";
               this.var_1.var_773.addChild(this.var_128);
            }
         }
      }
      
      public function method_105() : Boolean
      {
         var _loc1_:Boolean = false;
         var _loc2_:Number = 1;
         if(this.var_184)
         {
            this.var_184.m_Seq.var_1842 = this.m_Seq.var_1842;
            this.var_184.m_Seq.var_120 = this.m_Seq.var_120;
            this.var_184.method_105();
            if(this.m_Data.var_36.var_29 == "Animation_Paladin.swf")
            {
               _loc2_ = 1.1 / 0.75;
            }
         }
         _loc1_ = this.m_Seq.method_983(this.var_1.TIMESTEP,!!this.var_184 ? this.var_184.m_Seq : null);
         if(!_loc1_ && this.m_TheDO.visible)
         {
            if(this.method_1392(this.m_Seq.var_30,this.m_Seq.var_314))
            {
               this.m_Data.method_866(this.m_Seq.var_30,this.m_Seq.var_314,this.m_Sprite,this.var_151,_loc2_);
               if(this.var_285)
               {
                  this.method_1007();
               }
               else
               {
                  if(this.var_151.scrollRect)
                  {
                     this.var_151.scrollRect = null;
                  }
                  if(this.m_Sprite.scrollRect)
                  {
                     this.m_Sprite.scrollRect = null;
                  }
               }
               if(this.var_131)
               {
                  this.method_1712(this.m_Seq.var_314);
               }
               if(this.var_210)
               {
                  this.method_1840(this.m_Seq.var_314);
               }
            }
            this.m_Data.var_1826 = this.var_1.mTimeThisTick;
         }
         if(this.var_1076 || this.var_1366 || this.var_1380 || this.var_1971)
         {
            this.method_1352();
         }
         return _loc1_;
      }
      
      private function method_1392(param1:class_26, param2:class_28) : Boolean
      {
         if(!this.m_Sprite.numChildren)
         {
            return true;
         }
         if(this.var_1726)
         {
            return true;
         }
         var _loc3_:class_27 = this.m_Data.var_1501[param1.var_1859];
         if(Boolean(_loc3_) && Boolean(_loc3_.var_575[param2.var_2034]))
         {
            return true;
         }
         if(getTimer() - this.var_1.mTimeThisTick <= TIME_TO_STOP_RENDERING)
         {
            return true;
         }
         if(SuperAnimData.var_1220)
         {
            return true;
         }
         return false;
      }
      
      public function method_325(param1:uint, param2:uint = 0) : void
      {
         this.var_1029 = true;
         var _loc3_:* = (param2 & 16711680) >> 16;
         var _loc4_:* = (param2 & 65280) >> 8;
         var _loc5_:* = param2 & 255;
         var _loc6_:Number = ((param1 & 16711680) >> 16) / 255;
         var _loc7_:Number = ((param1 & 65280) >> 8) / 255;
         var _loc8_:Number = (param1 & 255) / 255;
         this.m_TheDO.transform.colorTransform = new ColorTransform(_loc6_,_loc7_,_loc8_,1,_loc3_,_loc4_,_loc5_,0);
      }
      
      public function method_2023(param1:uint, param2:uint = 0, param3:Number = 1) : void
      {
         this.var_1029 = true;
         var _loc4_:Number = ((param1 & 16711680) >> 16) / 255;
         var _loc5_:Number = ((param1 & 65280) >> 8) / 255;
         var _loc6_:Number = (param1 & 255) / 255;
         _loc4_ = (_loc4_ - 1) * param3 + 1;
         _loc5_ = (_loc5_ - 1) * param3 + 1;
         _loc6_ = (_loc6_ - 1) * param3 + 1;
         var _loc7_:* = (param2 & 16711680) >> 16;
         var _loc8_:* = (param2 & 65280) >> 8;
         var _loc9_:* = param2 & 255;
         this.m_TheDO.transform.colorTransform = new ColorTransform(_loc4_,_loc5_,_loc6_,1,_loc7_,_loc8_,_loc9_,0);
      }
      
      public function method_627(param1:uint, param2:uint = 0, param3:uint = 0) : void
      {
         this.var_1076 = true;
         this.var_1029 = true;
         this.m_TheDO.transform.colorTransform = new ColorTransform();
         this.var_1843 = this.var_1.mTimeThisTick;
         if(param3)
         {
            this.var_1971 = true;
            this.var_1076 = false;
            this.var_1345 = this.const_1194;
         }
      }
      
      public function method_880(param1:Number = 0.1) : void
      {
         this.var_1366 = false;
         this.var_1029 = true;
         this.var_1380 = true;
         this.m_TheDO.transform.colorTransform = new ColorTransform();
         this.var_1843 = this.var_1.mTimeThisTick;
         this.var_917 = param1;
      }
      
      public function method_1703() : void
      {
         this.var_1380 = false;
         this.var_1029 = true;
         this.var_1366 = true;
         this.m_TheDO.transform.colorTransform = new ColorTransform();
         this.var_1843 = this.var_1.mTimeThisTick;
      }
      
      public function method_1026() : void
      {
         if(this.var_1029)
         {
            this.var_1029 = false;
            this.m_TheDO.transform.colorTransform = new ColorTransform();
         }
         this.var_1076 = false;
         this.var_1971 = false;
      }
      
      public function method_1007() : void
      {
         var _loc1_:Rectangle = null;
         if(Boolean(this.var_151) && Boolean(this.var_151.bitmapData))
         {
            if(!this.var_151.scrollRect)
            {
               this.var_285.width = this.var_151.bitmapData.width;
               this.var_285.height = -this.var_151.y - const_347 * this.var_1.main.overallScale;
               this.var_151.scrollRect = this.var_285;
            }
            else
            {
               _loc1_ = this.var_151.scrollRect;
               this.var_285.width = _loc1_.width;
               this.var_285.height = _loc1_.height - const_347 * this.var_1.main.overallScale;
               this.var_285.x = _loc1_.x;
               this.var_285.y = _loc1_.y;
               this.var_151.scrollRect = this.var_285;
            }
         }
      }
      
      private function method_1712(param1:class_28) : void
      {
         var _loc2_:DisplayObject = this.var_131.m_TheDO;
         var _loc3_:Matrix = param1.var_2388;
         if(!_loc3_)
         {
            _loc2_.visible = false;
            return;
         }
         var _loc4_:Number = this.m_Data.var_36.animScale;
         var _loc5_:Number = this.var_1.main.overallScale;
         var _loc6_:Matrix;
         (_loc6_ = new Matrix(_loc5_,0,0,_loc5_)).concat(_loc3_);
         _loc6_.scale(_loc4_,_loc4_);
         _loc2_.transform.matrix = _loc6_;
         _loc2_.visible = true;
      }
      
      public function method_1840(param1:class_28) : void
      {
         if(this.var_210.m_bFinished)
         {
            this.var_210 = null;
            return;
         }
         var _loc2_:DisplayObject = this.var_210.m_TheDO;
         var _loc3_:Point = param1.var_1807;
         if(!_loc3_)
         {
            _loc2_.visible = false;
            return;
         }
         var _loc4_:Number = this.m_Data.var_36.animScale;
         var _loc5_:Matrix;
         (_loc5_ = new Matrix(1,0,0,1,_loc3_.x,_loc3_.y)).scale(_loc4_,_loc4_);
         _loc2_.transform.matrix = _loc5_;
         _loc2_.visible = true;
      }
      
      public function method_957(param1:GfxType) : void
      {
         var _loc2_:Dictionary = null;
         var _loc3_:int = 0;
         if(this.var_184)
         {
            if(this.var_184)
            {
               this.var_184.DestroySuperAnimInstance();
            }
            this.var_184 = null;
         }
         if(param1)
         {
            _loc2_ = this.m_Seq.var_71.var_69;
            if(param1.var_29 == "Animation_DireMount.swf")
            {
               this.m_Seq.var_218 = _loc2_["ReadyDire"];
               this.m_Seq.var_689 = _loc2_["JumpDire"];
               this.m_Seq.var_348 = _loc2_["JumpDire"];
               this.m_Seq.var_463 = _loc2_["RunDire"];
               this.m_Seq.var_384 = _loc2_["JumpDire"];
            }
            else if(param1.var_29 == "Animation_HorseMount.swf")
            {
               this.m_Seq.var_218 = _loc2_["ReadyHorse"];
               this.m_Seq.var_689 = _loc2_["JumpHorse"];
               this.m_Seq.var_348 = _loc2_["JumpHorse"];
               this.m_Seq.var_463 = _loc2_["RunHorse"];
               this.m_Seq.var_384 = _loc2_["JumpHorse"];
            }
            this.var_184 = new SuperAnimInstance(this.var_1,param1,false,true);
            this.var_184.m_Seq.var_348 = this.var_184.m_Seq.var_689;
            this.var_184.m_Seq.var_384 = this.var_184.m_Seq.var_689;
            _loc3_ = 0;
            if(this.var_131 && this.var_131.m_TheDO && this.var_131.m_TheDO.parent == this.m_TheDO)
            {
               _loc3_ = this.m_TheDO.getChildIndex(this.var_131.m_TheDO) + 1;
            }
            this.m_TheDO.addChildAt(this.var_184.m_TheDO,_loc3_);
            this.method_295(param1.var_209);
         }
         else
         {
            this.m_Seq.method_781();
            this.method_295(this.m_Data.var_36.var_209);
         }
      }
      
      public function method_366(param1:GfxType) : void
      {
         if(this.var_210)
         {
            if(param1)
            {
               this.var_210.m_bFinished = true;
               this.var_210 = null;
            }
            else if(!this.var_210.m_bFinished)
            {
               this.var_210.m_Seq.method_131();
            }
         }
         if(param1)
         {
            this.var_210 = new SuperAnimInstance(this.var_1,param1,this.var_1726);
            this.m_TheDO.addChild(this.var_210.m_TheDO);
         }
      }
      
      public function method_1815(param1:String, param2:uint) : void
      {
         var _loc3_:Number = this.var_1.TIMESTEP;
         this.var_1.TIMESTEP = 0;
         this.m_Seq.method_34(Seq.C_USEPOWER,param1,true);
         this.m_Seq.method_983(0,null);
         this.m_Seq.var_324 = param2;
         this.method_105();
         if(this.var_131)
         {
            this.var_131.m_Seq.var_324 = 14;
            this.var_131.method_105();
         }
         this.var_1.TIMESTEP = _loc3_;
      }
      
      public function method_1352() : void
      {
         var _loc1_:ColorTransform = null;
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         var _loc4_:int = 0;
         var _loc5_:uint = 0;
         var _loc6_:Number = NaN;
         if(Boolean(this.m_TheDO) && Boolean(this.m_TheDO.transform))
         {
            _loc1_ = this.m_TheDO.transform.colorTransform;
            if(_loc1_)
            {
               _loc2_ = uint(this.var_1.mTimeThisTick - this.var_1843);
               if(this.var_1076)
               {
                  _loc3_ = _loc2_ % this.const_1194;
                  _loc5_ = uint(this.const_1194 >> 1);
                  if(_loc3_ < _loc5_)
                  {
                     _loc4_ = (1 - (_loc5_ - _loc3_) / _loc5_) * 100;
                  }
                  else
                  {
                     _loc3_ -= _loc5_;
                     _loc4_ = (_loc5_ - _loc3_) / _loc5_ * 100;
                  }
                  _loc1_.redOffset = _loc4_;
                  _loc1_.blueOffset = _loc4_;
                  _loc1_.greenOffset = _loc4_;
                  this.m_TheDO.transform.colorTransform = _loc1_;
               }
               else if(this.var_1366)
               {
                  _loc6_ = (_loc6_ = _loc2_ / this.var_2500) * (1 - this.var_917) + this.var_917;
                  _loc1_.alphaMultiplier = _loc6_;
                  this.m_TheDO.transform.colorTransform = _loc1_;
                  if(_loc6_ >= 1)
                  {
                     this.var_1366 = false;
                  }
               }
               else if(this.var_1380)
               {
                  if((_loc6_ = (_loc6_ = 1 - _loc2_ / this.var_2500) * (1 - this.var_917) + this.var_917) <= this.var_917)
                  {
                     this.var_1380 = false;
                     _loc6_ = this.var_917;
                  }
                  _loc1_.alphaMultiplier = _loc6_;
                  this.m_TheDO.transform.colorTransform = _loc1_;
               }
               else if(this.var_1971)
               {
                  _loc3_ = _loc2_ % this.var_1345;
                  _loc5_ = uint(this.var_1345 >> 1);
                  if(_loc3_ < _loc5_)
                  {
                     _loc4_ = (1 - (_loc5_ - _loc3_) / _loc5_) * 180;
                  }
                  else
                  {
                     _loc3_ -= _loc5_;
                     _loc4_ = (_loc5_ - _loc3_) / _loc5_ * 180;
                  }
                  _loc1_.redOffset = _loc4_;
                  this.m_TheDO.transform.colorTransform = _loc1_;
                  this.var_1345 -= 7;
               }
            }
         }
      }
   }
}
