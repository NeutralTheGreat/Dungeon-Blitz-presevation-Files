package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.DisplayObjectContainer;
   import flash.display.FrameLabel;
   import flash.display.MovieClip;
   import flash.display.PixelSnapping;
   import flash.display.StageQuality;
   import flash.events.MouseEvent;
   import flash.geom.Matrix;
   import flash.utils.Dictionary;
   
   public class class_33
   {
      
      public static const const_36:uint = 1 << 0;
      
      public static const const_80:uint = 1 << 1;
      
      public static const const_14:uint = 1 << 2;
      
      public static const const_972:uint = 1 << 3;
      
      public static const const_298:uint = 0;
      
      public static const const_344:uint = 1;
      
      public static const const_494:uint = 2;
      
      public static var var_1480:String = "";
      
      private static const const_1038:uint = 0;
      
      private static const const_457:uint = 500;
      
      private static const const_997:uint = 100;
       
      
      public var var_1:Game;
      
      public var mMovieClip:MovieClip;
      
      public var var_393:Dictionary;
      
      public var var_175:Number = 1;
      
      public var var_720:uint = 1;
      
      public var mHealthPerc:Number = 0;
      
      public var var_564:Boolean = false;
      
      private var var_2076:Number = 0;
      
      private var var_300:Number = 0;
      
      private var var_1246:uint = 0;
      
      private var var_2035:uint = 0;
      
      private var var_1390:Number = 0;
      
      public var mbCompleted:Boolean = false;
      
      public var mbVisible:Boolean = true;
      
      public var mActiveTimeline:class_139 = null;
      
      public var var_1027:Boolean = false;
      
      public var var_363:MovieClip;
      
      public var var_271:MovieClip;
      
      public var var_1193:MovieClip;
      
      public var var_390:Bitmap;
      
      public var var_1129:String;
      
      private var var_2113:Boolean;
      
      private var var_1060:class_139 = null;
      
      private var var_845:class_139 = null;
      
      private var var_748:class_139 = null;
      
      private var var_568:Function = null;
      
      private var var_889:Function = null;
      
      private var var_940:Function = null;
      
      public var var_1230:Boolean = false;
      
      private var var_1604:uint;
      
      private var var_1565:Boolean = false;
      
      public var var_387:uint;
      
      public var var_1722:Boolean = false;
      
      private var var_722:Number = 0;
      
      private var var_901:uint;
      
      private var var_1153:uint;
      
      public function class_33(param1:Game, param2:MovieClip)
      {
         this.var_393 = new Dictionary();
         this.var_2113 = var_1480 != "";
         super();
         this.var_1 = param1;
         this.mMovieClip = param2;
         param2.gotoAndStop(1);
         this.method_1188();
         this.var_363 = this.mMovieClip.am_Tooltip;
         if(this.var_363)
         {
            this.var_363.visible = false;
            this.var_363.mouseEnabled = false;
            this.var_363.mouseChildren = false;
         }
         if(this.mMovieClip.am_CacheIcon)
         {
            this.method_298();
         }
      }
      
      public function DestroyUIMovieClip() : void
      {
         var _loc1_:String = null;
         this.method_535();
         this.var_1060 = null;
         this.var_845 = null;
         this.var_748 = null;
         this.var_568 = null;
         this.var_889 = null;
         this.var_940 = null;
         this.var_363 = null;
         this.var_271 = null;
         this.var_1193 = null;
         if(this.var_390)
         {
            if(this.var_390.bitmapData)
            {
               this.var_390.bitmapData.dispose();
               this.var_390.bitmapData = null;
            }
            this.var_390 = null;
         }
         this.mMovieClip = null;
         for(_loc1_ in this.var_393)
         {
            delete this.var_393[_loc1_];
         }
         this.var_393 = null;
         this.mActiveTimeline = null;
         this.var_1 = null;
      }
      
      private function method_1188() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:String = null;
         var _loc3_:FrameLabel = null;
         var _loc4_:class_139 = null;
         var _loc5_:uint = uint(this.mMovieClip.totalFrames);
         var _loc6_:Array;
         var _loc7_:uint = (_loc6_ = this.mMovieClip.scenes[0].labels).length;
         var _loc8_:uint = 0;
         while(_loc8_ < _loc7_)
         {
            _loc3_ = _loc6_[_loc8_];
            _loc2_ = _loc3_.name;
            _loc1_ = uint(_loc3_.frame);
            if(!_loc2_.indexOf("PlaySound"))
            {
               _loc4_.var_2191 = _loc1_;
            }
            else
            {
               if(_loc4_)
               {
                  _loc4_.var_1348 = _loc1_ - 1;
               }
               _loc4_ = new class_139(_loc2_,_loc1_,_loc5_);
               this.var_393[_loc2_] = _loc4_;
            }
            _loc8_++;
         }
         if(!_loc7_)
         {
            this.var_393["Ready"] = new class_139("Ready",1,_loc5_);
         }
      }
      
      public function Hide(param1:Boolean = false) : void
      {
         if(!this.var_1722 || param1)
         {
            this.mMovieClip.visible = false;
            this.mbVisible = false;
            this.mbCompleted = true;
         }
         else if(!this.var_901)
         {
            this.var_722 = this.mMovieClip.alpha;
            this.var_901 = this.var_722 >= 1 ? this.var_1.mTimeThisTick : uint(this.var_1.mTimeThisTick - const_457);
            this.var_1153 = 0;
         }
      }
      
      public function Show(param1:Boolean = false) : void
      {
         if(this.var_1722)
         {
            if(param1)
            {
               this.mMovieClip.alpha = 1;
               this.var_901 = 0;
            }
            else if(!this.var_1153)
            {
               this.var_722 = this.mbVisible ? this.mMovieClip.alpha : 0;
               this.var_1153 = this.var_1.mTimeThisTick;
               this.var_901 = 0;
            }
         }
         this.mMovieClip.visible = true;
         this.mbVisible = true;
         if(this.var_564)
         {
            this.mbCompleted = false;
         }
      }
      
      public function method_42() : void
      {
         var _loc1_:DisplayObjectContainer = this.mMovieClip.parent;
         if(_loc1_)
         {
            _loc1_.removeChild(this.mMovieClip);
         }
         this.Hide();
      }
      
      public function method_141(param1:uint) : void
      {
         this.Show();
         if(param1 == const_298)
         {
            this.var_1.var_89.addChild(this.mMovieClip);
         }
         else if(param1 == const_344)
         {
            this.var_1.var_245.addChild(this.mMovieClip);
         }
         else
         {
            this.var_1.var_272.addChild(this.mMovieClip);
         }
      }
      
      public function method_941(param1:uint) : void
      {
         this.Show();
         this.var_1.var_89.addChildAt(this.mMovieClip,param1);
      }
      
      private function method_623(param1:MouseEvent) : void
      {
         if(this.var_845)
         {
            this.PlayAnimation(this.var_845.name);
         }
         if(this.var_889 != null)
         {
            if(this.var_1565)
            {
               this.var_889(param1,this.var_1604);
            }
            else
            {
               this.var_889(param1);
            }
         }
         if(this.var_363)
         {
            this.var_363.visible = true;
         }
         param1.stopPropagation();
      }
      
      private function method_698(param1:MouseEvent) : void
      {
         if(this.var_1060)
         {
            this.PlayAnimation(this.var_1060.name);
         }
         if(this.var_940 != null)
         {
            if(this.var_1565)
            {
               this.var_940(param1,this.var_1604);
            }
            else
            {
               this.var_940(param1);
            }
         }
         if(this.var_363)
         {
            this.var_363.visible = false;
         }
         param1.stopPropagation();
      }
      
      private function method_865(param1:MouseEvent) : void
      {
         if(this.var_845)
         {
            this.PlayAnimation(this.var_845.name);
         }
         param1.stopPropagation();
      }
      
      private function method_286(param1:MouseEvent) : void
      {
         if(this.var_748)
         {
            this.PlayAnimation(this.var_748.name);
         }
         if(this.var_2113)
         {
            SoundManager.Play(var_1480);
         }
         if(!this.var_1230 && this.var_568 != null)
         {
            if(this.var_1565)
            {
               this.var_568(param1,this.var_1604);
            }
            else
            {
               this.var_568(param1);
            }
         }
         param1.stopPropagation();
      }
      
      private function method_342(param1:MouseEvent) : void
      {
         if(this.var_568 != null)
         {
            if(this.var_1565)
            {
               this.var_568(param1,this.var_1604);
            }
            else
            {
               this.var_568(param1);
            }
         }
         param1.stopPropagation();
      }
      
      private function method_535() : void
      {
         if(this.var_363)
         {
            this.var_363.visible = false;
         }
         if(Boolean(this.var_748) || this.var_568 != null)
         {
            this.mMovieClip.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_286);
            this.mMovieClip.removeEventListener(MouseEvent.RIGHT_MOUSE_DOWN,this.method_286);
         }
         if(this.var_845 || this.var_889 != null || this.var_940 != null)
         {
            this.mMovieClip.removeEventListener(MouseEvent.ROLL_OVER,this.method_623);
            this.mMovieClip.removeEventListener(MouseEvent.ROLL_OUT,this.method_698);
         }
         if(this.var_748)
         {
            this.mMovieClip.removeEventListener(MouseEvent.MOUSE_UP,this.method_865);
         }
         if(this.var_1230)
         {
            this.mMovieClip.removeEventListener(MouseEvent.CLICK,this.method_342);
            this.mMovieClip.removeEventListener(MouseEvent.RIGHT_CLICK,this.method_342);
         }
      }
      
      private function method_637() : void
      {
         if(Boolean(this.var_748) || this.var_568 != null)
         {
            this.mMovieClip.addEventListener(MouseEvent.MOUSE_DOWN,this.method_286);
            this.mMovieClip.addEventListener(MouseEvent.RIGHT_MOUSE_DOWN,this.method_286);
         }
         if(this.var_845 || this.var_889 != null || this.var_940 != null)
         {
            this.mMovieClip.addEventListener(MouseEvent.ROLL_OVER,this.method_623);
            this.mMovieClip.addEventListener(MouseEvent.ROLL_OUT,this.method_698);
         }
         if(this.var_748)
         {
            this.mMovieClip.addEventListener(MouseEvent.MOUSE_UP,this.method_865);
         }
         if(this.var_1230)
         {
            this.mMovieClip.addEventListener(MouseEvent.CLICK,this.method_342);
            this.mMovieClip.addEventListener(MouseEvent.RIGHT_CLICK,this.method_342);
         }
      }
      
      public function EnableButton() : void
      {
         if(this.var_1027)
         {
            if(this.var_1060)
            {
               this.PlayAnimation(this.var_1060.name);
            }
            this.method_637();
            this.var_1027 = false;
         }
      }
      
      public function DisableButton(param1:String) : void
      {
         if(!this.var_1027)
         {
            this.method_535();
            this.PlayAnimation(param1);
            this.var_1027 = true;
         }
      }
      
      public function PresetRollCalls(param1:Function, param2:Function) : void
      {
         this.var_889 = param1;
         this.var_940 = param2;
      }
      
      public function method_837(param1:uint) : void
      {
         this.var_1565 = true;
         this.var_1604 = param1;
      }
      
      public function method_2076() : void
      {
         this.var_2113 = false;
      }
      
      public function BecomeButton(param1:String, param2:String, param3:String, param4:Function, param5:Boolean = true) : void
      {
         this.method_535();
         this.var_1060 = this.var_393[param1];
         this.var_845 = this.var_393[param2];
         this.var_748 = this.var_393[param3];
         this.var_568 = param4;
         this.var_1230 = !param5;
         this.mMovieClip.mouseEnabled = true;
         this.mMovieClip.mouseChildren = false;
         this.method_637();
      }
      
      public function method_298() : void
      {
         if(!this.var_271)
         {
            this.var_271 = this.mMovieClip.am_CacheIcon;
            if(!this.var_271)
            {
               return;
            }
            this.var_1193 = new MovieClip();
            while(this.var_271.numChildren)
            {
               this.var_1193.addChild(this.var_271.removeChildAt(0));
            }
            this.var_390 = new Bitmap(null,PixelSnapping.ALWAYS);
         }
         while(this.var_271.numChildren)
         {
            this.var_271.removeChildAt(0);
         }
         this.var_271.addChild(this.var_1193);
         if(this.var_390.bitmapData)
         {
            this.var_390.bitmapData.dispose();
         }
         var _loc1_:Number = this.var_1.main.overallScale * this.mMovieClip.scaleX;
         var _loc2_:uint = Math.ceil(this.var_271.width * _loc1_);
         var _loc3_:uint = Math.ceil(this.var_271.height * _loc1_);
         if(!_loc3_ || !_loc2_)
         {
            return;
         }
         var _loc4_:BitmapData;
         (_loc4_ = new BitmapData(_loc2_,_loc3_,true,0)).drawWithQuality(this.var_271,new Matrix(_loc1_,0,0,_loc1_),null,null,null,false,StageQuality.HIGH);
         this.var_390.bitmapData = _loc4_;
         var _loc5_:Number = 1 / _loc1_;
         this.var_390.scaleX = _loc5_;
         this.var_390.scaleY = _loc5_;
         this.var_271.removeChild(this.var_1193);
         this.var_271.addChild(this.var_390);
      }
      
      public function ClearAnimation() : void
      {
         this.var_175 = 1;
         this.mbCompleted = true;
         this.mActiveTimeline = null;
         this.mMovieClip.gotoAndStop(this.var_175);
      }
      
      public function PlayAnimation(param1:String, param2:uint = 0) : Boolean
      {
         var _loc3_:class_139 = this.var_393[param1];
         if(!_loc3_)
         {
            return false;
         }
         if(param2 & const_972)
         {
            this.Show();
         }
         if(_loc3_ != this.mActiveTimeline || this.mbCompleted)
         {
            this.var_175 = !!(param2 & const_80) ? _loc3_.var_1348 : _loc3_.var_1401;
            this.var_720 = _loc3_.var_1348;
            this.mActiveTimeline = _loc3_;
         }
         this.mbCompleted = false;
         this.var_564 = false;
         this.var_387 = param2;
         this.var_1129 = null;
         return true;
      }
      
      public function method_147(param1:String, param2:String, param3:uint = 0) : void
      {
         var _loc4_:Boolean;
         if((_loc4_ = this.PlayAnimation(param1,param3)) && Boolean(this.mActiveTimeline.var_2191))
         {
            this.var_1129 = param2;
         }
      }
      
      public function BeginHealthMode(param1:String, param2:Number, param3:Number = 0) : void
      {
         var _loc5_:Number = NaN;
         var _loc4_:class_139;
         if(_loc4_ = this.var_393[param1])
         {
            this.mHealthPerc = 0;
            this.var_2076 = 0;
            this.var_300 = 0;
            this.var_1246 = 0;
            this.var_2035 = uint(param3 * 1000);
            this.mbCompleted = false;
            this.var_564 = true;
            this.var_387 = 0;
            this.var_1129 = null;
            this.mActiveTimeline = this.var_393[param1];
            this.var_175 = this.mActiveTimeline.var_1401;
            this.var_720 = this.mActiveTimeline.var_1348;
            if(!param2)
            {
               this.var_1390 = 0;
            }
            else
            {
               _loc5_ = this.var_720 - this.var_175 + 1;
               this.var_1390 = _loc5_ / (param2 * Game.TARGETFPS);
            }
         }
      }
      
      public function method_1012() : void
      {
         this.var_1722 = true;
      }
      
      public function TickMovieClip() : void
      {
         if(this.var_1722)
         {
            this.method_1979();
         }
         if(!this.mbCompleted && Boolean(this.mActiveTimeline))
         {
            if(this.var_564)
            {
               this.method_1365();
            }
            else
            {
               this.method_1422();
            }
         }
      }
      
      private function method_1365() : void
      {
         var _loc6_:uint = 0;
         if(this.var_2035)
         {
            _loc6_ = this.var_1.mTimeThisTick;
            if(!this.var_1246 && this.var_2076 != this.mHealthPerc)
            {
               this.var_1246 = _loc6_ + this.var_2035;
            }
            this.var_2076 = this.mHealthPerc;
            if(!this.var_1246 || _loc6_ < this.var_1246)
            {
               return;
            }
         }
         var _loc1_:int = int(this.mActiveTimeline.var_1401);
         var _loc2_:int = this.var_720 - _loc1_;
         var _loc3_:Number = this.mHealthPerc > 1 ? 1 : (this.mHealthPerc < 0 ? 0 : this.mHealthPerc);
         var _loc4_:int = _loc1_ + Math.round(_loc2_ * _loc3_);
         if(!this.var_300 || !this.var_1390)
         {
            this.var_300 = _loc4_;
         }
         else if(_loc4_ < this.var_300)
         {
            this.var_300 -= this.var_1.TIMESTEP * this.var_1390;
            if(this.var_300 < _loc4_)
            {
               this.var_300 = _loc4_;
            }
         }
         else if(_loc4_ > this.var_300)
         {
            this.var_300 += this.var_1.TIMESTEP * this.var_1390;
            if(this.var_300 > _loc4_)
            {
               this.var_300 = _loc4_;
            }
         }
         else
         {
            this.var_1246 = 0;
         }
         var _loc5_:int;
         if((_loc5_ = this.var_300) != this.mMovieClip.currentFrame)
         {
            this.mMovieClip.gotoAndStop(_loc5_);
         }
      }
      
      private function method_1422() : void
      {
         var _loc1_:int = 0;
         var _loc4_:int = 0;
         var _loc2_:int = int(this.mActiveTimeline.var_1401);
         if(this.var_387 & const_80)
         {
            _loc1_ = Math.ceil(this.var_175);
            if(_loc1_ >= _loc2_)
            {
               this.var_175 -= this.var_1.TIMESTEP;
            }
            else if(this.var_387 & const_36)
            {
               _loc1_ = int(this.var_720);
               this.var_175 = this.var_720;
            }
            else
            {
               _loc1_ = _loc2_;
               this.mbCompleted = true;
               if(this.var_387 & const_14)
               {
                  this.Hide();
               }
            }
         }
         else
         {
            _loc1_ = this.var_175;
            if(_loc1_ <= this.var_720)
            {
               this.var_175 += this.var_1.TIMESTEP;
            }
            else if(this.var_387 & const_36)
            {
               _loc1_ = _loc2_;
               this.var_175 = _loc2_;
            }
            else
            {
               _loc1_ = int(this.var_720);
               this.mbCompleted = true;
               if(this.var_387 & const_14)
               {
                  this.Hide();
               }
            }
         }
         var _loc3_:int = this.mMovieClip.currentFrame;
         if(_loc1_ != _loc3_)
         {
            this.mMovieClip.gotoAndStop(_loc1_);
            if(this.var_1129)
            {
               _loc4_ = int(this.mActiveTimeline.var_2191);
               if(this.var_387 & const_80)
               {
                  if(_loc4_ <= _loc3_ && _loc4_ > _loc1_)
                  {
                     SoundManager.Play(this.var_1129);
                  }
               }
               else if(_loc4_ >= _loc3_ && _loc4_ < _loc1_)
               {
                  SoundManager.Play(this.var_1129);
               }
            }
         }
      }
      
      private function method_1979() : void
      {
         var _loc2_:uint = 0;
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc5_:uint = 0;
         var _loc1_:uint = this.var_1.mTimeThisTick;
         if(this.var_901)
         {
            _loc5_ = uint(_loc1_ - this.var_901);
            if(this.var_722 == 1 && _loc5_ < const_457)
            {
               _loc3_ = 1;
            }
            else
            {
               _loc2_ = (_loc4_ = this.var_722) * const_997;
               _loc3_ = !!_loc2_ ? this.var_722 - (_loc5_ - const_457) / _loc2_ : 0;
               if(_loc3_ <= 0)
               {
                  this.var_901 = 0;
                  _loc3_ = 0;
                  this.mMovieClip.visible = false;
                  this.mbVisible = false;
                  this.mbCompleted = true;
               }
            }
            this.mMovieClip.alpha = _loc3_;
         }
         else if(this.var_1153)
         {
            _loc2_ = (_loc4_ = 1 - this.var_722) * const_1038;
            _loc3_ = !!_loc2_ ? this.var_722 + (this.var_1.mTimeThisTick - this.var_1153) / _loc2_ : 1;
            if(_loc3_ >= 1)
            {
               this.var_1153 = 0;
               _loc3_ = 1;
            }
            this.mMovieClip.alpha = _loc3_;
         }
      }
   }
}
