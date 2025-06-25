package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.MovieClip;
   import flash.display.PixelSnapping;
   import flash.display.Sprite;
   import flash.display.StageQuality;
   import flash.events.MouseEvent;
   import flash.geom.Matrix;
   import flash.geom.Rectangle;
   
   public class class_133
   {
      
      public static const const_951:Number = 95;
      
      public static const const_880:Number = 45;
      
      public static const const_382:Number = 1;
      
      public static var var_835:GfxType = new GfxType();
      
      {
         var_835.var_29 = "SFX_1.swf";
         var_835.animScale = 0.25;
         var_835.bFireAndForget = true;
         var_835.animClass = "a_GroupmateFanfare";
         var_835.var_177 = 0;
      }
      
      internal var var_1:Game;
      
      internal var charName:String;
      
      internal var var_2870:Boolean;
      
      internal var bOnline:Boolean;
      
      internal var var_2370:Boolean;
      
      internal var var_652:String;
      
      internal var var_2641:Boolean;
      
      internal var groupFrame:MovieClip;
      
      internal var var_2131:uint;
      
      internal var var_2048:uint;
      
      internal var var_623:MovieClip;
      
      internal var var_580:Array;
      
      internal var var_2484:Boolean;
      
      internal var var_2288:Boolean = false;
      
      internal var var_2704:int = 0;
      
      internal var var_634:class_33;
      
      internal var var_1498:class_33;
      
      internal var var_1548:class_33;
      
      internal var var_1491:class_33;
      
      internal var var_1326:class_33;
      
      internal var var_1465:class_33;
      
      public function class_133(param1:String, param2:Boolean, param3:Boolean, param4:Boolean, param5:String, param6:Game)
      {
         super();
         this.var_1 = param6;
         this.charName = param1;
         this.var_2870 = param2;
         this.bOnline = param3;
         this.var_652 = param5;
         this.var_2370 = param4;
         var _loc7_:String = !!this.var_652 ? Level.method_182(this.var_652) : null;
         this.var_2641 = _loc7_ == "ShazariDesert" || _loc7_ == "JadeCity" || _loc7_ == "ShazariDesertHard" || _loc7_ == "JadeCityHard";
      }
      
      public static function method_1956(param1:Game) : void
      {
         var _loc2_:class_133 = null;
         for each(_loc2_ in param1.groupmates)
         {
            _loc2_.method_1570();
         }
      }
      
      public static function method_956(param1:Game, param2:Vector.<class_133>, param3:Boolean) : void
      {
         var _loc6_:class_133 = null;
         var _loc7_:Number = NaN;
         var _loc4_:Boolean = false;
         var _loc5_:Array = new Array();
         for each(_loc6_ in param1.groupmates)
         {
            _loc5_.push(_loc6_.charName);
            _loc6_.method_1824();
         }
         _loc7_ = const_880;
         param1.groupmates = param2;
         for each(_loc6_ in param2)
         {
            _loc7_ = Number(_loc6_.method_1186(_loc7_,param1));
            if(_loc5_.indexOf(_loc6_.charName) < 0)
            {
               _loc6_.var_2484 = true;
               _loc4_ = true;
            }
         }
         if(param3 && _loc4_)
         {
            for each(_loc6_ in param2)
            {
               if(_loc6_.var_2484)
               {
                  _loc6_.method_1776();
               }
            }
            if(SoundConfig.var_1973)
            {
               SoundManager.Play(SoundConfig.var_1973);
            }
         }
         param1.screenHudTop.Refresh();
      }
      
      public static function method_659(param1:EntType, param2:Number, param3:Game) : Array
      {
         var _loc4_:Entity = null;
         var _loc6_:Number = param2 / 56;
         var _loc7_:* = (_loc7_ = (_loc7_ = "<EntType EntName=\"PaperDoll\" parent=\"Player:" + param1.entName + "\">") + ("<GfxType><AnimScale>-" + _loc6_ + "</AnimScale></GfxType>")) + "</EntType>";
         EntType.method_57(_loc7_,"HeadshotUI");
         (_loc4_ = new Entity(param3,"HeadshotUI:PaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,0,0,null,null,null,null,null,null)).gfx.m_Seq.method_34(Seq.C_USEPOWER,"Headshot",true);
         _loc4_.gfx.method_105();
         var _loc8_:Bitmap = method_189(_loc4_.gfx,param2,param3);
         _loc4_.gfx.m_Seq.method_34(Seq.C_USEPOWER,"HeadshotHurt",true);
         _loc4_.gfx.method_105();
         var _loc9_:Bitmap = method_189(_loc4_.gfx,param2,param3);
         _loc4_.gfx.m_Seq.method_34(Seq.C_USEPOWER,"HeadshotDead",true);
         _loc4_.gfx.method_105();
         var _loc10_:Bitmap = method_189(_loc4_.gfx,param2,param3);
         _loc4_.DestroyEntity(false);
         var _loc11_:Array;
         (_loc11_ = new Array()).push(_loc8_);
         _loc11_.push(_loc9_);
         _loc11_.push(_loc10_);
         return _loc11_;
      }
      
      public static function method_189(param1:SuperAnimInstance, param2:int, param3:Game) : Bitmap
      {
         var _loc4_:Bitmap = new Bitmap();
         var _loc5_:Sprite;
         var _loc6_:Number = (_loc5_ = param1.m_Sprite).scaleX;
         var _loc7_:Number = _loc5_.scaleY;
         param1.m_Sprite.scaleX = 1;
         param1.m_Sprite.scaleY = 1;
         param2 *= param3.main.overallScale;
         param2 += 1;
         var _loc8_:Rectangle = _loc5_.getBounds(_loc5_);
         var _loc9_:Matrix = new Matrix(1,0,0,1,0,0);
         _loc9_.tx -= _loc8_.x;
         _loc9_.ty -= _loc8_.y;
         if(_loc8_.width == 0)
         {
            _loc8_.width = 1;
         }
         _loc4_.bitmapData = new BitmapData(_loc8_.width,-_loc8_.y + param2,true,0);
         _loc4_.bitmapData.drawWithQuality(param1.m_Sprite,_loc9_,null,null,null,false,StageQuality.HIGH);
         _loc4_.x = _loc8_.x;
         _loc4_.y = _loc8_.y;
         _loc4_.smoothing = false;
         _loc4_.scaleX = 1 / param3.main.overallScale;
         _loc4_.scaleY = 1 / param3.main.overallScale;
         _loc4_.pixelSnapping = PixelSnapping.ALWAYS;
         param1.m_Sprite.scaleX = _loc6_;
         param1.m_Sprite.scaleY = _loc7_;
         return _loc4_;
      }
      
      public function method_1824() : void
      {
         this.method_811();
         if(this.var_623)
         {
            this.var_1.screenMap.method_517(this.var_623);
            this.var_623 = null;
         }
         this.var_1 = null;
      }
      
      public function method_1186(param1:Number, param2:Game) : Number
      {
         this.var_1 = param2;
         this.method_1738(param1);
         return param1 + const_951;
      }
      
      public function method_1776() : void
      {
         var _loc1_:SuperAnimInstance = new SuperAnimInstance(this.var_1,var_835,true);
         this.var_1.var_89.addChildAt(_loc1_.m_TheDO,this.var_1.var_89.getChildIndex(this.groupFrame));
         _loc1_.m_TheDO.x = this.groupFrame.x + 30;
         _loc1_.m_TheDO.y = 60;
      }
      
      public function method_811() : void
      {
         var _loc1_:MovieClip = null;
         if(this.groupFrame)
         {
            if(this.groupFrame.parent)
            {
               this.groupFrame.parent.removeChild(this.groupFrame);
            }
            _loc1_ = this.groupFrame.am_Hotbox;
            _loc1_.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_964);
            _loc1_.removeEventListener(MouseEvent.ROLL_OVER,this.method_477);
            _loc1_.removeEventListener(MouseEvent.ROLL_OUT,this.method_163);
            this.var_1498.DestroyUIMovieClip();
            this.var_1498 = null;
            this.var_1548.DestroyUIMovieClip();
            this.var_1548 = null;
            this.var_1465.DestroyUIMovieClip();
            this.var_1465 = null;
            this.var_1491.DestroyUIMovieClip();
            this.var_1491 = null;
            this.var_1326.DestroyUIMovieClip();
            this.var_1326 = null;
            this.var_634.DestroyUIMovieClip();
            this.var_634 = null;
            this.groupFrame = null;
            this.var_580 = null;
         }
      }
      
      public function method_1738(param1:Number) : void
      {
         var _loc4_:String = null;
         this.groupFrame = class_4.method_16("a_GroupFrame",true);
         this.groupFrame.x = param1;
         this.groupFrame.scaleX = const_382;
         this.groupFrame.scaleY = const_382;
         this.groupFrame.mouseEnabled = false;
         this.groupFrame.am_Hotbox.am_Options.visible = false;
         this.groupFrame.am_GroupLeader.visible = this.var_2870;
         if(!this.bOnline)
         {
            MathUtil.method_2(this.groupFrame.am_Location,"(Offline)");
         }
         else if(this.var_2370)
         {
            MathUtil.method_2(this.groupFrame.am_Location,"");
         }
         else
         {
            _loc4_ = Level.method_73(this.var_652);
            MathUtil.method_2(this.groupFrame.am_Location,!!_loc4_ ? _loc4_ : "Unknown");
         }
         MathUtil.method_2(this.groupFrame.am_MemberName,this.charName);
         this.var_1.var_89.addChildAt(this.groupFrame,0);
         var _loc2_:MovieClip = this.groupFrame.am_Hotbox;
         _loc2_.addEventListener(MouseEvent.MOUSE_DOWN,this.method_964);
         _loc2_.addEventListener(MouseEvent.ROLL_OVER,this.method_477);
         _loc2_.addEventListener(MouseEvent.ROLL_OUT,this.method_163);
         var _loc3_:MovieClip = _loc2_.am_Options;
         this.var_1498 = new class_33(this.var_1,_loc3_.am_Whisper);
         this.var_1548 = new class_33(this.var_1,_loc3_.am_Promote);
         this.var_1465 = new class_33(this.var_1,_loc3_.am_Inspect);
         this.var_1491 = new class_33(this.var_1,_loc3_.am_Remove);
         this.var_1326 = new class_33(this.var_1,_loc3_.am_Friend);
         this.var_1498.BecomeButton("Ready","Over","Click",this.method_1717,false);
         this.var_1548.BecomeButton("Ready","Over","Click",this.method_1836,false);
         this.var_1465.BecomeButton("Ready","Over","Click",this.method_1067,false);
         this.var_1491.BecomeButton("Ready","Over","Click",this.method_1718,false);
         this.var_1326.BecomeButton("Ready","Over","Click",this.method_1504,false);
         this.var_634 = new class_33(this.var_1,this.groupFrame.am_Teleport);
         this.var_634.PresetRollCalls(this.method_477,this.method_163);
         this.var_634.BecomeButton("Ready","Over","Click",this.method_1153,false);
         this.var_634.Hide();
         MathUtil.method_2(this.groupFrame.am_Dist,"");
         this.groupFrame.am_Left.visible = false;
         this.groupFrame.am_Right.visible = false;
         this.groupFrame.am_Left.mouseEnabled = false;
         this.groupFrame.am_Right.mouseEnabled = false;
         this.groupFrame.am_Dist.mouseEnabled = false;
         this.groupFrame.am_Left.mouseChildren = false;
         this.groupFrame.am_Right.mouseChildren = false;
         this.groupFrame.am_GroupLeader.mouseEnabled = false;
         this.groupFrame.am_GroupLeader.mouseChildren = false;
         this.groupFrame.am_Headshot.mouseEnabled = false;
         this.groupFrame.am_Headshot.mouseChildren = false;
         this.groupFrame.am_HPBar.mouseEnabled = false;
         this.groupFrame.am_HPBar.mouseChildren = false;
         this.groupFrame.am_MemberName.mouseEnabled = false;
         this.groupFrame.am_Location.mouseEnabled = false;
      }
      
      private function method_1475(param1:Entity) : void
      {
         var _loc2_:MovieClip = this.groupFrame.am_Headshot;
         while(_loc2_.numChildren)
         {
            _loc2_.removeChildAt(0);
         }
         var _loc3_:Number = 1 / const_382;
         _loc2_.scaleX = _loc3_;
         _loc2_.scaleY = _loc3_;
         this.var_580 = method_659(param1.entType,56 * const_382,this.var_1);
         _loc2_.addChild(this.var_580[0]);
         _loc2_.addChild(this.var_580[1]);
         _loc2_.addChild(this.var_580[2]);
      }
      
      private function method_501(param1:Boolean) : void
      {
         var _loc2_:Number = param1 ? 1 : 0.5;
         this.groupFrame.am_HPBar.alpha = _loc2_;
         this.groupFrame.am_MemberName.alpha = _loc2_;
         this.groupFrame.am_Location.alpha = _loc2_;
         this.groupFrame.am_Headshot.alpha = _loc2_;
      }
      
      public function method_1570() : void
      {
         var _loc3_:Boolean = false;
         var _loc4_:Boolean = false;
         var _loc5_:Boolean = false;
         var _loc6_:int = 0;
         var _loc7_:Number = NaN;
         if(!this.groupFrame)
         {
            return;
         }
         this.var_634.TickMovieClip();
         this.var_1498.TickMovieClip();
         this.var_1548.TickMovieClip();
         this.var_1465.TickMovieClip();
         this.var_1491.TickMovieClip();
         this.var_1326.TickMovieClip();
         var _loc1_:MovieClip = this.groupFrame.am_HPBar;
         var _loc2_:Entity = this.var_1.GetPlayerEntFromEntName(this.charName);
         if(_loc2_)
         {
            if(!this.var_580)
            {
               this.method_1475(_loc2_);
               MathUtil.method_2(this.groupFrame.am_MemberName,"");
            }
            if((_loc6_ = int(_loc2_.currHP / _loc2_.maxHP * 100)) <= 0)
            {
               _loc5_ = true;
            }
            else if(_loc6_ <= 30)
            {
               _loc4_ = true;
            }
            else
            {
               _loc3_ = true;
            }
            this.var_580[0].visible = _loc3_;
            this.var_580[1].visible = _loc4_;
            this.var_580[2].visible = _loc5_;
            if(_loc6_ > 100)
            {
               _loc6_ = 100;
            }
            if(_loc6_ < 1)
            {
               _loc6_ = 1;
            }
            _loc1_.gotoAndStop(_loc6_);
            this.method_501(true);
            if(Boolean(this.groupFrame.am_Hotbox.am_Options.visible) || this.var_1.PointOnScreenWithinDist(_loc2_.var_10,_loc2_.var_12,_loc2_.entType.width,_loc2_.entType.height))
            {
               MathUtil.method_2(this.groupFrame.am_Dist,"");
               this.groupFrame.am_Left.visible = false;
               this.groupFrame.am_Right.visible = false;
            }
            else if((_loc7_ = _loc2_.physPosX - this.var_1.clientEnt.physPosX) < 0)
            {
               this.groupFrame.am_Left.visible = true;
               this.groupFrame.am_Right.visible = false;
               _loc7_ = int(-_loc7_ * Game.const_452 / 5) * 5;
               MathUtil.method_2(this.groupFrame.am_Dist,_loc7_ + "ft");
            }
            else
            {
               this.groupFrame.am_Left.visible = false;
               this.groupFrame.am_Right.visible = true;
               _loc7_ = int(_loc7_ * Game.const_452 / 5) * 5;
               MathUtil.method_2(this.groupFrame.am_Dist,_loc7_ + "ft");
            }
         }
         else if(this.bOnline)
         {
            _loc1_.gotoAndStop(100);
            this.method_501(false);
            MathUtil.method_2(this.groupFrame.am_Dist,"");
            this.groupFrame.am_Left.visible = false;
            this.groupFrame.am_Right.visible = false;
         }
         else
         {
            _loc1_.gotoAndStop(100);
            this.method_501(false);
            MathUtil.method_2(this.groupFrame.am_Dist,"");
            this.groupFrame.am_Left.visible = false;
            this.groupFrame.am_Right.visible = false;
         }
         if(this.bOnline && !this.var_2370 && this.var_1.method_1285(this.var_652))
         {
            this.var_634.Show();
         }
         else
         {
            this.var_634.Hide();
         }
         if(this.groupFrame.am_Hotbox.am_Options.visible)
         {
            if(!this.var_2288 && (this.var_2704 + 333 < this.var_1.mTimeThisTick || this.var_1.var_2031))
            {
               this.groupFrame.am_Hotbox.am_Options.visible = false;
            }
         }
      }
      
      private function method_477(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = null;
         MathUtil.method_2(this.groupFrame.am_MemberName,this.charName);
         if(Boolean(this.var_1.clientEnt) && this.var_1.clientEnt.combatState.method_123(2000))
         {
            _loc2_ = this.groupFrame.am_Hotbox.am_Options;
            _loc2_.visible = true;
            _loc2_.am_Promote.visible = this.var_1.bAmGroupLeader;
            _loc2_.am_Remove.visible = this.var_1.bAmGroupLeader;
            this.var_2288 = true;
            this.var_1.var_2031 = true;
            this.var_1.var_1412 = true;
         }
      }
      
      private function method_163(param1:MouseEvent) : void
      {
         if(this.var_580)
         {
            MathUtil.method_2(this.groupFrame.am_MemberName,"");
         }
         this.var_2704 = this.var_1.mTimeThisTick;
         this.var_2288 = false;
         this.var_1.var_2031 = false;
         this.var_1.var_1412 = false;
      }
      
      private function method_964(param1:MouseEvent) : void
      {
         param1.stopPropagation();
      }
      
      private function method_1717(param1:MouseEvent) : void
      {
         this.var_1.screenChat.BeginChat("/tell " + this.charName + " ");
         this.method_163(param1);
         param1.stopPropagation();
      }
      
      private function method_1836(param1:MouseEvent) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/leader " + this.charName);
         this.method_163(param1);
         param1.stopPropagation();
      }
      
      private function method_1067(param1:MouseEvent) : void
      {
         var _loc2_:Entity = this.var_1.GetPlayerEntFromEntName(this.charName);
         if(!_loc2_)
         {
            this.var_1.screenChat.ReceiveChat(this.var_1.clientEntID,"^t" + this.charName + " is not close enough to inspect");
         }
         else
         {
            this.var_1.method_778(_loc2_.id);
         }
         this.method_163(param1);
         param1.stopPropagation();
      }
      
      private function method_1153(param1:MouseEvent) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/teleport " + this.charName);
         param1.stopPropagation();
      }
      
      private function method_1718(param1:MouseEvent) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/kick " + this.charName);
         this.method_163(param1);
         param1.stopPropagation();
      }
      
      private function method_1504(param1:MouseEvent) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/friend " + this.charName);
         this.method_163(param1);
         param1.stopPropagation();
      }
      
      public function method_320(param1:uint, param2:uint, param3:uint, param4:String) : void
      {
         this.var_2131 = param1;
         this.var_2048 = param2;
         if((Boolean(this.var_2131) || Boolean(this.var_2048)) && this.var_2641 == this.var_1.mbSleepingLands)
         {
            if(!this.var_623)
            {
               this.var_623 = this.var_1.screenMap.method_555(param3,param4);
            }
         }
         else if(this.var_623)
         {
            this.var_1.screenMap.method_517(this.var_623);
            this.var_623 = null;
         }
      }
   }
}
