package
{
   import flash.display.MovieClip;
   
   public class class_61
   {
      
      private static const const_979:uint = 585;
      
      private static const const_1203:uint = 565;
       
      
      internal var var_1:Game;
      
      private const const_999:Number = 7;
      
      private const const_1231:Number = 0.6;
      
      internal var var_135:class_33;
      
      internal var var_680:class_33;
      
      internal var var_659:class_33;
      
      internal var var_132:class_33;
      
      internal var var_682:class_33;
      
      internal var var_636:class_33;
      
      internal var var_662:class_33;
      
      internal var var_600:class_33;
      
      internal var var_702:String;
      
      internal var var_1088:String;
      
      public function class_61(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1371() : void
      {
         if(this.var_135)
         {
            this.var_135.method_42();
            this.var_135.DestroyUIMovieClip();
            this.var_135 = null;
         }
         if(this.var_680)
         {
            this.var_680.method_42();
            this.var_680.DestroyUIMovieClip();
            this.var_680 = null;
         }
         if(this.var_659)
         {
            this.var_659.method_42();
            this.var_659.DestroyUIMovieClip();
            this.var_659 = null;
         }
         if(this.var_132)
         {
            this.var_132.method_42();
            this.var_132.DestroyUIMovieClip();
            this.var_132 = null;
         }
         if(this.var_682)
         {
            this.var_682.method_42();
            this.var_682.DestroyUIMovieClip();
            this.var_682 = null;
         }
         if(this.var_636)
         {
            this.var_636.method_42();
            this.var_636.DestroyUIMovieClip();
            this.var_636 = null;
         }
         if(this.var_662)
         {
            this.var_662.method_42();
            this.var_662.DestroyUIMovieClip();
            this.var_662 = null;
         }
         if(this.var_600)
         {
            this.var_600.method_42();
            this.var_600.DestroyUIMovieClip();
            this.var_600 = null;
         }
         this.var_1 = null;
      }
      
      public function Display(param1:Room) : void
      {
         var _loc2_:MovieClip = null;
         var _loc3_:MovieClip = null;
         if(!this.var_135)
         {
            _loc2_ = class_4.method_16("a_BossBar");
            _loc2_.x = Camera.SCREEN_WIDTH * 0.5;
            this.var_135 = new class_33(this.var_1,_loc2_);
            this.var_135.method_42();
            this.var_680 = new class_33(this.var_1,_loc2_.am_BossBar);
            this.var_659 = new class_33(this.var_1,_loc2_.am_BossBarCatchUp);
         }
         if(!this.var_132)
         {
            _loc3_ = class_4.method_16("a_BossBar_Double");
            _loc3_.x = Camera.SCREEN_WIDTH * 0.5;
            this.var_132 = new class_33(this.var_1,_loc3_);
            this.var_132.method_42();
            this.var_682 = new class_33(this.var_1,_loc3_.am_BossBar1);
            this.var_636 = new class_33(this.var_1,_loc3_.am_BossBarCatchUp1);
            this.var_662 = new class_33(this.var_1,_loc3_.am_BossBar2);
            this.var_600 = new class_33(this.var_1,_loc3_.am_BossBarCatchUp2);
         }
         if(Boolean(param1.var_122) && param1.var_122.bDoubleBossFight)
         {
            this.var_135.method_42();
            this.var_132.method_141(class_33.const_298);
            this.var_132.PlayAnimation("BuildUp");
            this.var_132.mMovieClip.y = const_1203;
            this.var_682.BeginHealthMode("Health",0);
            this.var_682.mHealthPerc = 100;
            this.var_636.BeginHealthMode("Health",this.const_999,this.const_1231);
            this.var_636.mHealthPerc = 100;
            this.var_662.BeginHealthMode("Health",0);
            this.var_662.mHealthPerc = 100;
            this.var_600.BeginHealthMode("Health",this.const_999,this.const_1231);
            this.var_600.mHealthPerc = 100;
         }
         else
         {
            this.var_132.method_42();
            this.var_135.method_141(class_33.const_298);
            this.var_135.PlayAnimation("BuildUp");
            this.var_135.mMovieClip.y = const_979;
            this.var_680.BeginHealthMode("Health",0);
            this.var_680.mHealthPerc = 100;
            this.var_659.BeginHealthMode("Health",this.const_999,this.const_1231);
            this.var_659.mHealthPerc = 100;
         }
         this.var_702 = null;
         this.var_1088 = null;
         this.method_317();
      }
      
      private function method_317() : void
      {
         MathUtil.method_2(this.var_135.mMovieClip.am_BossWrapper.am_BossName,this.var_702);
         MathUtil.method_2(this.var_132.mMovieClip.am_BossWrapper.am_BossName,this.var_702);
         MathUtil.method_2(this.var_132.mMovieClip.am_BossWrapper2.am_BossName,this.var_1088);
      }
      
      private function method_1409(param1:Room) : void
      {
         if(!this.var_135 || !this.var_135.mbVisible || this.var_1.var_641.method_40())
         {
            return;
         }
         if(param1.var_1358 != this.var_702)
         {
            this.var_702 = param1.var_1358;
            this.method_317();
         }
         this.var_135.TickMovieClip();
         this.var_680.TickMovieClip();
         this.var_659.TickMovieClip();
         if(!this.var_135.mbCompleted)
         {
            return;
         }
         var _loc2_:Entity = !!param1.var_1047 ? this.var_1.GetEntFromID(param1.var_1047) : null;
         var _loc3_:Number = !!_loc2_ ? _loc2_.currHP / _loc2_.maxHP : 0;
         this.var_680.mHealthPerc = _loc3_;
         this.var_659.mHealthPerc = _loc3_;
      }
      
      private function method_1128(param1:Room) : void
      {
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         if(!this.var_132 || !this.var_132.mbVisible || this.var_1.var_641.method_40())
         {
            return;
         }
         this.var_132.TickMovieClip();
         this.var_682.TickMovieClip();
         this.var_636.TickMovieClip();
         this.var_662.TickMovieClip();
         this.var_600.TickMovieClip();
         var _loc2_:String = param1.var_1358;
         var _loc3_:String = param1.var_2199;
         if(_loc2_ != this.var_702 || _loc3_ != this.var_1088)
         {
            this.var_702 = _loc2_;
            this.var_1088 = _loc3_;
            this.method_317();
         }
         if(!this.var_132.mbCompleted)
         {
            return;
         }
         var _loc4_:Entity = !!param1.var_1047 ? this.var_1.GetEntFromID(param1.var_1047) : null;
         var _loc5_:Entity = !!param1.var_1377 ? this.var_1.GetEntFromID(param1.var_1377) : null;
         var _loc6_:Number = !!_loc4_ ? _loc4_.currHP / _loc4_.maxHP : 0;
         var _loc7_:Number = !!_loc5_ ? _loc5_.currHP / _loc5_.maxHP : 0;
         if(_loc6_ > 0 && _loc7_ > 0)
         {
            _loc8_ = _loc6_;
            _loc9_ = _loc7_;
         }
         else if(_loc6_ > 0)
         {
            _loc3_ = null;
            _loc8_ = _loc6_;
            _loc9_ = _loc6_;
         }
         else
         {
            _loc2_ = null;
            _loc8_ = _loc7_;
            _loc9_ = _loc7_;
         }
         this.var_682.mHealthPerc = _loc8_;
         this.var_636.mHealthPerc = _loc8_;
         this.var_662.mHealthPerc = _loc9_;
         this.var_600.mHealthPerc = _loc9_;
         if(_loc2_ != this.var_702 || _loc3_ != this.var_1088)
         {
            this.var_702 = _loc2_;
            this.var_1088 = _loc3_;
            this.method_317();
         }
      }
      
      public function method_253() : void
      {
         if(DevSettings.flags & DevSettings.DEVFLAG_NO_GRAPHICS)
         {
            return;
         }
         var _loc1_:Boolean = this.method_40();
         var _loc2_:Room = !!this.var_1.clientEnt ? this.var_1.clientEnt.currRoom : null;
         var _loc3_:Boolean = Boolean(_loc2_) && _loc2_.var_1925;
         if(!_loc1_ && !_loc3_)
         {
            return;
         }
         if(_loc1_ && !_loc3_)
         {
            this.Hide();
            return;
         }
         if(!_loc1_ && _loc3_)
         {
            this.Display(_loc2_);
         }
         if(this.var_1.var_641.method_40())
         {
            this.var_135.mMovieClip.alpha = 0;
            this.var_132.mMovieClip.alpha = 0;
         }
         else
         {
            this.var_135.mMovieClip.alpha = 1;
            this.var_132.mMovieClip.alpha = 1;
         }
         this.method_1409(_loc2_);
         this.method_1128(_loc2_);
      }
      
      public function Hide() : void
      {
         if(this.var_135)
         {
            this.var_135.method_42();
         }
         if(this.var_132)
         {
            this.var_132.method_42();
         }
      }
      
      public function method_40() : Boolean
      {
         return Boolean(this.var_135) && this.var_135.mbVisible || Boolean(this.var_132) && this.var_132.mbVisible;
      }
   }
}
