package
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   
   public class class_32
   {
       
      
      internal var var_1:Game;
      
      internal var var_530:class_4;
      
      internal var mWindow:class_33;
      
      internal var var_2:MovieClip;
      
      internal var var_321:Vector.<class_33>;
      
      internal var var_496:Vector.<class_137>;
      
      internal var var_1137:Vector.<class_138>;
      
      private var var_1984:Vector.<MovieClip>;
      
      internal var var_819:Vector.<SuperAnimInstance>;
      
      internal var var_1024:Vector.<SuperAnimInstance>;
      
      internal var mbVisible:Boolean;
      
      private var var_790:Boolean;
      
      private var var_1292:Boolean;
      
      private var var_1752:uint;
      
      internal var var_1173:String;
      
      internal var var_2105:String;
      
      internal var var_1450:uint;
      
      internal var mPaperDoll:Object;
      
      internal var var_37:Boolean;
      
      internal var var_16:uint;
      
      internal var var_44:uint;
      
      internal var var_731:class_33;
      
      internal var var_810:class_33;
      
      internal var var_656:class_33;
      
      internal var var_279:class_32;
      
      private var var_2157:Function;
      
      internal var var_15:Boolean;
      
      internal var mbHideOnClear:Boolean;
      
      internal var var_45:String;
      
      internal var var_87:String;
      
      internal var var_92:uint;
      
      internal var var_112:Boolean;
      
      internal var var_101:Boolean;
      
      public function class_32(param1:Game, param2:String, param3:String)
      {
         super();
         this.var_1 = param1;
         this.var_530 = param1.mUIManager;
         this.var_1173 = param2;
         this.var_2105 = param3;
         this.var_321 = new Vector.<class_33>();
         this.var_1137 = new Vector.<class_138>();
         this.var_1984 = new Vector.<MovieClip>();
         this.var_496 = new Vector.<class_137>();
         this.var_819 = new Vector.<SuperAnimInstance>();
         this.var_1024 = new Vector.<SuperAnimInstance>();
         this.var_15 = false;
         this.mbHideOnClear = true;
         this.var_45 = "Ready";
         this.var_87 = null;
         this.var_92 = 0;
         this.var_112 = false;
         this.var_101 = true;
         this.var_2157 = hasOwnProperty("OnInitDisplay") ? this["OnInitDisplay"] : null;
      }
      
      public function OnCreateScreen() : void
      {
      }
      
      public function OnDestroyScreen() : void
      {
      }
      
      public function OnRefreshScreen() : void
      {
      }
      
      public function OnClearScreen() : void
      {
      }
      
      public function OnTickScreen() : void
      {
      }
      
      public function RefreshPaperDoll() : void
      {
      }
      
      public function method_448() : void
      {
         var _loc1_:SuperAnimInstance = null;
         var _loc2_:SuperAnimInstance = null;
         var _loc3_:class_33 = null;
         var _loc4_:class_138 = null;
         var _loc5_:class_137 = null;
         var _loc6_:MovieClip = null;
         if(this.mWindow)
         {
            this.OnDestroyScreen();
         }
         if(this.mPaperDoll)
         {
            this.mPaperDoll.DestroyEntity(false);
            this.mPaperDoll = null;
         }
         for each(_loc1_ in this.var_819)
         {
            _loc1_.DestroySuperAnimInstance();
         }
         this.var_819 = null;
         for each(_loc2_ in this.var_1024)
         {
            _loc2_.DestroySuperAnimInstance();
         }
         this.var_1024 = null;
         for each(_loc3_ in this.var_321)
         {
            _loc3_.DestroyUIMovieClip();
         }
         this.var_321 = null;
         for each(_loc4_ in this.var_1137)
         {
            _loc4_.method_1593();
         }
         this.var_1137 = null;
         for each(_loc5_ in this.var_496)
         {
            _loc5_.method_862();
         }
         this.var_496 = null;
         for each(_loc6_ in this.var_1984)
         {
            class_136.method_1536(_loc6_);
         }
         this.var_1984 = null;
         this.var_731 = null;
         this.var_810 = null;
         this.var_279 = null;
         this.var_656 = null;
         if(this.mWindow)
         {
            this.var_530.method_1999(this.mWindow.mMovieClip);
            this.mWindow.method_42();
            this.mWindow.DestroyUIMovieClip();
            this.mWindow = null;
         }
         this.var_2 = null;
         this.var_530 = null;
         this.var_1 = null;
      }
      
      public function Refresh() : void
      {
         this.var_1752 = 0;
         if(this.mbVisible)
         {
            this.OnRefreshScreen();
            this.method_177();
            if(this.var_279)
            {
               this.var_279.Refresh();
            }
         }
      }
      
      public function method_119() : void
      {
         var _loc1_:SuperAnimInstance = null;
         var _loc2_:Vector.<class_32> = null;
         var _loc3_:int = 0;
         if(this.mWindow)
         {
            this.OnClearScreen();
            this.mWindow.method_42();
            this.mWindow.ClearAnimation();
         }
         this.mbVisible = false;
         if(this.var_112 && this.var_1292)
         {
            this.var_530.var_1983 = false;
         }
         this.var_1292 = false;
         if(this.mPaperDoll)
         {
            this.mPaperDoll.DestroyEntity(false);
            this.mPaperDoll = null;
         }
         for each(_loc1_ in this.var_819)
         {
            _loc1_.DestroySuperAnimInstance();
         }
         this.var_819.length = 0;
         _loc2_ = this.var_530.mActiveScreens;
         _loc3_ = _loc2_.indexOf(this);
         if(_loc3_ != -1)
         {
            _loc2_.splice(_loc3_,1);
         }
      }
      
      public function Hide() : void
      {
         if(Boolean(this.mWindow) && !this.var_790)
         {
            if(this.var_87)
            {
               this.mWindow.PlayAnimation(this.var_87);
            }
            else
            {
               this.mWindow.PlayAnimation(this.var_45,class_33.const_80);
            }
            this.var_790 = true;
            this.method_483(false);
         }
         if(this.var_279)
         {
            this.var_279.Hide();
            this.var_279 = null;
         }
      }
      
      public function method_483(param1:Boolean) : void
      {
         if(!this.mWindow)
         {
            return;
         }
         var _loc2_:MovieClip = this.mWindow.mMovieClip;
         if(_loc2_)
         {
            _loc2_.mouseEnabled = param1;
            _loc2_.mouseChildren = param1;
         }
      }
      
      public function method_265(param1:String) : void
      {
         if(this.mWindow)
         {
            this.mWindow.PlayAnimation(param1);
            this.var_790 = true;
            this.method_483(false);
         }
      }
      
      public function Display(... rest) : void
      {
         var _loc3_:SuperAnimInstance = null;
         var _loc4_:MovieClip = null;
         var _loc5_:MovieClip = null;
         if(!this.mWindow)
         {
            _loc4_ = this.var_530.method_990(this.var_1173);
            this.mWindow = new class_33(this.var_1,_loc4_);
            this.mWindow.method_42();
            this.var_2 = !!this.var_2105 ? _loc4_[this.var_2105] : _loc4_;
            if(_loc5_ = this.var_2.am_TutorialWindow)
            {
               this.var_656 = this.method_5(_loc5_,this.method_1746);
            }
            this.OnCreateScreen();
            if(this.mWindow.mMovieClip.am_CacheIcon)
            {
               this.mWindow.method_298();
            }
         }
         if(this.var_656)
         {
            this.var_656.Hide();
         }
         if(this.var_2157 != null)
         {
            this.var_2157.apply(null,rest);
         }
         if(this.mbVisible && !this.var_790)
         {
            this.Refresh();
            this.var_37 = true;
            return;
         }
         if(!this.var_15)
         {
            this.var_1.method_127();
         }
         this.mbVisible = true;
         this.var_790 = false;
         this.method_483(this.var_101);
         var _loc2_:Vector.<class_32> = this.var_530.mActiveScreens;
         if(_loc2_.indexOf(this) == -1)
         {
            _loc2_.unshift(this);
         }
         this.Refresh();
         this.mWindow.PlayAnimation(this.var_45);
         this.var_37 = true;
         for each(_loc3_ in this.var_1024)
         {
            _loc3_.method_105();
         }
         if(this.var_279)
         {
            this.var_279.Display();
         }
      }
      
      public function method_2034(param1:class_32) : void
      {
         if(Boolean(this.var_279) && this.var_279 != param1)
         {
            this.var_279.method_119();
         }
         this.var_279 = param1;
         if(this.var_1292)
         {
            this.var_279.Display();
            this.var_279.method_434();
         }
      }
      
      private function method_1746(param1:MouseEvent) : void
      {
         if(this.var_656.mbVisible)
         {
            this.var_656.Hide();
         }
         else
         {
            this.var_656.Show();
         }
      }
      
      public function Toggle(... rest) : void
      {
         if(this.mbVisible && !this.var_790)
         {
            this.Hide();
         }
         else
         {
            this.Display.apply(null,rest);
         }
      }
      
      public function method_434() : void
      {
         var _loc1_:class_33 = null;
         var _loc2_:class_138 = null;
         var _loc3_:int = 0;
         var _loc5_:SuperAnimInstance = null;
         var _loc6_:class_32 = null;
         var _loc7_:class_32 = null;
         var _loc8_:Sprite = null;
         var _loc9_:MovieClip = null;
         var _loc10_:uint = 0;
         var _loc11_:class_137 = null;
         if(!this.var_1292)
         {
            if(this.var_790)
            {
               this.method_119();
               return;
            }
            if(this.var_112 && this.var_530.var_1983)
            {
               return;
            }
            _loc6_ = null;
            for each(_loc7_ in this.var_530.mActiveScreens)
            {
               if(_loc7_.var_1292)
               {
                  if(this.var_1450 > _loc7_.var_1450)
                  {
                     if(!_loc6_ || _loc7_.var_1450 > _loc6_.var_1450)
                     {
                        _loc6_ = _loc7_;
                     }
                  }
               }
            }
            _loc8_ = this.var_1.var_89;
            if(!_loc6_)
            {
               this.mWindow.method_941(_loc8_.numChildren);
            }
            else if((_loc9_ = _loc6_.mWindow.mMovieClip).parent != _loc8_)
            {
               class_24.method_19("UIWindow was not on the UILayer, someone made a mistake");
            }
            else
            {
               _loc10_ = uint(_loc8_.getChildIndex(_loc9_));
               this.mWindow.method_941(_loc10_);
            }
            if(this.var_112)
            {
               this.var_530.var_1983 = true;
            }
            this.var_1292 = true;
         }
         this.OnTickScreen();
         for each(_loc1_ in this.var_321)
         {
            _loc1_.TickMovieClip();
         }
         for each(_loc2_ in this.var_1137)
         {
            _loc2_.TickTextField();
         }
         _loc3_ = int(this.var_496.length - 1);
         while(_loc3_ >= 0)
         {
            if((_loc11_ = this.var_496[_loc3_]).method_1931())
            {
               _loc11_.method_862();
               this.var_496.splice(_loc3_,1);
            }
            _loc3_--;
         }
         var _loc4_:uint = this.var_1.mTimeThisTick;
         for each(_loc5_ in this.var_819)
         {
            _loc5_.m_Data.var_1826 = this.var_1.mTimeThisTick;
         }
         for each(_loc5_ in this.var_1024)
         {
            _loc5_.m_Data.var_1826 = this.var_1.mTimeThisTick;
         }
         if(this.var_37)
         {
            this.RefreshPaperDoll();
            this.var_37 = false;
         }
         this.mWindow.TickMovieClip();
         if(this.mWindow.mbCompleted)
         {
            if(this.var_790)
            {
               this.method_119();
            }
            else if(this.var_92)
            {
               if(!this.var_1752)
               {
                  this.var_1752 = _loc4_ + this.var_92;
               }
               else if(_loc4_ >= this.var_1752)
               {
                  this.Hide();
               }
            }
         }
      }
      
      public function method_177() : void
      {
         if(!this.var_731 || !this.var_810)
         {
            return;
         }
         if(this.var_44 <= 1)
         {
            this.var_731.Hide();
            this.var_810.Hide();
            if(this.var_2.am_PageNumber)
            {
               MathUtil.method_2(this.var_2.am_PageNumber,"");
            }
            return;
         }
         if(this.var_16 < this.var_44 - 1)
         {
            this.var_810.EnableButton();
         }
         else
         {
            this.var_810.DisableButton("Inactive");
         }
         this.var_810.Show();
         if(this.var_16)
         {
            this.var_731.EnableButton();
         }
         else
         {
            this.var_731.DisableButton("Inactive");
         }
         this.var_731.Show();
         if(this.var_2.am_PageNumber)
         {
            MathUtil.method_2(this.var_2.am_PageNumber,this.var_16 + 1 + "/" + this.var_44);
         }
      }
      
      internal function PageLeft(param1:MouseEvent) : void
      {
         if(this.var_16)
         {
            --this.var_16;
            this.Refresh();
         }
      }
      
      internal function PageRight(param1:MouseEvent) : void
      {
         if(this.var_16 < this.var_44 - 1)
         {
            ++this.var_16;
            this.Refresh();
         }
      }
      
      public function method_14(param1:MovieClip) : void
      {
         while(param1.numChildren)
         {
            param1.removeChildAt(0);
         }
      }
      
      public function method_68(param1:String, param2:Number, param3:Number, param4:MovieClip, param5:uint, param6:Function = null, param7:Function = null, param8:Boolean = false) : class_137
      {
         var _loc9_:MovieClip;
         (_loc9_ = class_4.method_16(param1)).x = param2;
         _loc9_.y = param3;
         _loc9_.mouseEnabled = false;
         this.mWindow.mMovieClip.addChild(_loc9_);
         var _loc10_:Rectangle = param4.getBounds(this.mWindow.mMovieClip);
         var _loc11_:class_137;
         (_loc11_ = new class_137(this.var_1)).method_546(_loc9_);
         _loc11_.method_1283(param8);
         _loc11_.method_470(_loc10_.x,_loc10_.y,param5,param6,param7);
         this.var_496.push(_loc11_);
         return _loc11_;
      }
      
      public function method_201(param1:MovieClip, param2:Number, param3:Number, param4:MovieClip, param5:uint, param6:Function = null, param7:Function = null) : class_137
      {
         param1.x = param2;
         param1.y = param3;
         param1.mouseEnabled = false;
         this.mWindow.mMovieClip.addChild(param1);
         var _loc8_:Rectangle = param4.getBounds(this.mWindow.mMovieClip);
         var _loc9_:class_137;
         (_loc9_ = new class_137(this.var_1)).method_546(param1);
         _loc9_.method_470(_loc8_.x,_loc8_.y,param5,param6,param7);
         this.var_496.push(_loc9_);
         return _loc9_;
      }
      
      public function method_909(param1:MovieClip, param2:Number, param3:Number, param4:uint, param5:Function = null, param6:Function = null) : class_137
      {
         var _loc7_:class_137;
         (_loc7_ = new class_137(this.var_1)).method_546(param1,false);
         _loc7_.method_470(param2,param3,param4,param5,param6);
         this.var_496.push(_loc7_);
         return _loc7_;
      }
      
      public function method_12(param1:MovieClip, param2:String) : MovieClip
      {
         var _loc3_:MovieClip = class_4.method_16(param2);
         while(param1.numChildren)
         {
            param1.removeChildAt(0);
         }
         param1.addChild(_loc3_);
         return _loc3_;
      }
      
      public function method_52(param1:MovieClip, param2:SuperAnimInstance) : SuperAnimInstance
      {
         while(param1.numChildren)
         {
            param1.removeChildAt(0);
         }
         param1.addChild(param2.m_TheDO);
         this.var_819.push(param2);
         return param2;
      }
      
      public function method_2028(param1:MovieClip, param2:SuperAnimInstance) : SuperAnimInstance
      {
         while(param1.numChildren)
         {
            param1.removeChildAt(0);
         }
         param1.addChild(param2.m_TheDO);
         this.var_1024.push(param2);
         return param2;
      }
      
      public function method_208() : void
      {
         this.var_731 = this.method_10(this.var_2.am_PageLeft,this.PageLeft);
         this.var_810 = this.method_10(this.var_2.am_PageRight,this.PageRight);
      }
      
      private function method_1143(param1:MouseEvent) : void
      {
         this.Hide();
      }
      
      public function method_23(param1:MovieClip) : class_33
      {
         var _loc2_:class_33 = new class_33(this.var_1,param1);
         _loc2_.BecomeButton("Ready","Over","Click",this.method_1143,false);
         this.var_321.push(_loc2_);
         return _loc2_;
      }
      
      public function method_10(param1:MovieClip, param2:Function, param3:Function = null, param4:Function = null) : class_33
      {
         var _loc5_:class_33 = new class_33(this.var_1,param1);
         if(param3 != null || param4 != null)
         {
            _loc5_.PresetRollCalls(param3,param4);
         }
         _loc5_.BecomeButton("Ready","Over","Click",param2,false);
         this.var_321.push(_loc5_);
         return _loc5_;
      }
      
      public function method_117(param1:MovieClip, param2:uint, param3:Function, param4:Function = null, param5:Function = null) : class_33
      {
         var _loc6_:class_33 = new class_33(this.var_1,param1);
         if(param4 != null || param5 != null)
         {
            _loc6_.PresetRollCalls(param4,param5);
         }
         _loc6_.BecomeButton("Ready","Over","Click",param3,false);
         _loc6_.method_837(param2);
         this.var_321.push(_loc6_);
         return _loc6_;
      }
      
      public function method_5(param1:MovieClip, param2:Function, param3:Function = null, param4:Function = null) : class_33
      {
         var _loc5_:class_33 = new class_33(this.var_1,param1);
         if(param3 != null || param4 != null)
         {
            _loc5_.PresetRollCalls(param3,param4);
         }
         _loc5_.BecomeButton("Ready","Over","Click",param2);
         this.var_321.push(_loc5_);
         return _loc5_;
      }
      
      public function method_3(param1:MovieClip, param2:uint, param3:Function, param4:Function = null, param5:Function = null) : class_33
      {
         var _loc6_:class_33 = new class_33(this.var_1,param1);
         if(param4 != null || param5 != null)
         {
            _loc6_.PresetRollCalls(param4,param5);
         }
         _loc6_.BecomeButton("Ready","Over","Click",param3);
         _loc6_.method_837(param2);
         this.var_321.push(_loc6_);
         return _loc6_;
      }
      
      public function method_17(param1:MovieClip, param2:String, param3:Number, param4:Number = 0) : class_33
      {
         var _loc5_:class_33;
         (_loc5_ = new class_33(this.var_1,param1)).BeginHealthMode(param2,param3,param4);
         this.var_321.push(_loc5_);
         return _loc5_;
      }
      
      public function method_1(param1:MovieClip) : class_33
      {
         var _loc2_:class_33 = new class_33(this.var_1,param1);
         this.var_321.push(_loc2_);
         return _loc2_;
      }
      
      public function method_27(param1:MovieClip) : class_33
      {
         var _loc2_:class_33 = new class_33(this.var_1,param1);
         _loc2_.method_1012();
         param1.mouseEnabled = false;
         param1.mouseChildren = false;
         this.var_321.push(_loc2_);
         return _loc2_;
      }
      
      public function method_21(param1:TextField) : class_138
      {
         var _loc2_:class_138 = new class_138(this.var_1,param1);
         this.var_1137.push(_loc2_);
         return _loc2_;
      }
      
      public function method_92(param1:TextField, param2:Number = 2, param3:String = "") : class_138
      {
         var _loc4_:class_138;
         (_loc4_ = new class_138(this.var_1,param1)).method_878(param2,param3);
         this.var_1137.push(_loc4_);
         return _loc4_;
      }
      
      public function method_313(param1:MovieClip, param2:Function, param3:Function, param4:Number = 0) : MovieClip
      {
         class_136.method_1078(param1,param2,param3,param4);
         this.var_1984.push(param1);
         return param1;
      }
   }
}
