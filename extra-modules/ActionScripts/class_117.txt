package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   
   public class class_117 extends class_32
   {
      
      private static const const_1406:uint = 10;
      
      private static const const_677:uint = 511;
      
      private static const const_324:uint = 8;
      
      private static const const_1244:uint = 20;
       
      
      public var var_60:class_33;
      
      internal var var_356:class_33;
      
      internal var var_993:MovieClip;
      
      internal var var_159:MovieClip;
      
      internal var var_893:MovieClip;
      
      internal var var_1908:MovieClip;
      
      internal var var_198:MovieClip;
      
      internal var var_123:MovieClip;
      
      private var var_2095:class_33;
      
      private var var_1367:class_33;
      
      private var var_733:class_33;
      
      private var var_2764:class_33;
      
      private var var_1940:Vector.<class_33>;
      
      private var var_1736:Vector.<class_33>;
      
      private var var_1777:Boolean;
      
      private var var_1301:class_33;
      
      private var var_2295:uint;
      
      public function class_117(param1:Game)
      {
         super(param1,"a_ScreenCharmComplete",null);
         var_45 = "FadeIn";
         var_87 = "FadeOut";
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:MovieClip = null;
         var _loc2_:class_33 = null;
         this.var_356 = method_1(var_2.am_Reforge);
         this.var_993 = var_2.am_Information;
         this.var_159 = var_2.am_CharmStats;
         this.var_893 = this.var_356.mMovieClip.am_RerollRealms;
         this.var_1908 = this.var_356.mMovieClip.am_RerollAnimGroup;
         this.var_733 = method_10(this.var_356.mMovieClip.am_ReforgeButton,this.method_1302);
         this.var_2764 = method_10(this.var_356.mMovieClip.am_KeepThisOneButton,this.method_1731);
         this.var_1940 = new Vector.<class_33>(const_324,true);
         this.var_1736 = new Vector.<class_33>(const_324,true);
         var _loc3_:int = 0;
         while(_loc3_ < const_324)
         {
            _loc1_ = this.var_1908["am_RerollAnim" + _loc3_];
            _loc2_ = method_1(_loc1_);
            this.var_1940[_loc3_] = _loc2_;
            this.var_1736[_loc3_] = method_1(_loc1_.am_Realm);
            _loc3_++;
         }
         this.var_1367 = method_10(this.var_159.am_ReforgeButton,this.method_1632);
         this.var_2095 = method_10(this.var_159.am_TakeCharm,this.method_1771);
         this.var_60 = method_1(var_2.am_TutorialInteraction);
         this.var_60.Hide();
         this.method_618();
         var_2.cacheAsBitmap = true;
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_356 = null;
         this.var_1940 = null;
         this.var_1736 = null;
         this.var_993 = null;
         this.var_159 = null;
         this.var_893 = null;
         this.var_1908 = null;
         this.var_198 = null;
         this.var_123 = null;
         this.var_2095 = null;
         this.var_1367 = null;
         this.var_2764 = null;
         this.var_733 = null;
         this.var_1301 = null;
         this.var_60 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc3_:class_1 = null;
         var _loc1_:class_64 = var_1.mMagicForgeStatus.RetreiveCharm();
         method_14(this.var_993.am_CharmHolder.am_IconHolder);
         var _loc2_:Boolean = false;
         if(Boolean(_loc1_) && Boolean(_loc1_.var_13))
         {
            _loc2_ = Boolean(_loc1_.var_8);
            if(_loc2_ != this.var_1777)
            {
               this.var_1777 = _loc2_;
               this.method_618();
            }
            MathUtil.method_2(this.var_159.am_Name,_loc1_.var_13.displayName);
            MathUtil.method_2(this.var_159.am_PrimaryStat,_loc1_.var_13.var_203);
            _loc1_.method_78(this,this.var_993.am_CharmHolder.am_IconHolder);
            if(_loc1_.var_8 == class_64.const_180)
            {
               MathUtil.method_8(this.var_993.am_Name,_loc1_.method_49(),ScreenArmory.const_22,ScreenArmory.const_814);
               MathUtil.method_2(this.var_159.am_BonusType,"Rare Bonus");
               MathUtil.method_2(this.var_159.am_Type,"Rare Charm");
            }
            else if(_loc1_.var_8 == class_64.const_196)
            {
               MathUtil.method_8(this.var_993.am_Name,_loc1_.method_49(),ScreenArmory.const_23,ScreenArmory.const_672);
               MathUtil.method_2(this.var_159.am_BonusType,"Legendary Bonus");
               MathUtil.method_2(this.var_159.am_Type,"Legendary Charm");
            }
            else
            {
               MathUtil.method_8(this.var_993.am_Name,_loc1_.method_49(),ScreenArmory.const_24,ScreenArmory.const_455);
               MathUtil.method_2(this.var_159.am_Type,"Charm");
            }
            this.var_198.gotoAndStop(_loc1_.var_13.var_115);
            this.var_198.visible = true;
            if(this.var_1777)
            {
               _loc3_ = _loc1_.method_115();
               if(_loc3_)
               {
                  this.var_123.gotoAndStop(_loc3_.var_115);
                  MathUtil.method_2(this.var_159.am_SecondaryStat,_loc1_.method_171());
               }
            }
         }
         this.var_733.EnableButton();
         if(_loc2_)
         {
            this.var_1367.EnableButton();
         }
         else
         {
            this.var_1367.DisableButton("Inactive");
         }
      }
      
      public function method_618() : void
      {
         if(!this.var_1777)
         {
            this.var_159.gotoAndStop("SingleStat");
            this.var_159.am_BonusType.visible = false;
            this.var_159.am_SecondaryStat.visible = false;
         }
         else
         {
            this.var_159.gotoAndStop("DualStat");
            this.var_159.am_BonusType.visible = true;
            this.var_159.am_SecondaryStat.visible = true;
            this.var_123 = this.var_159.am_SecondaryColor;
         }
         this.var_198 = this.var_159.am_PrimaryColor;
      }
      
      public function method_609() : void
      {
         var _loc5_:MovieClip = null;
         var _loc6_:MovieClip = null;
         var _loc8_:String = null;
         var _loc12_:class_1 = null;
         var _loc13_:String = null;
         var _loc14_:class_1 = null;
         var _loc15_:String = null;
         var _loc1_:uint = class_75.method_337(var_1.mMagicForgeStatus.primary);
         var _loc2_:class_64 = var_1.mMagicForgeStatus.RetreiveCharm();
         var _loc3_:uint = uint(var_1.mMagicForgeStatus.usedlist);
         var _loc4_:MovieClip = this.var_356.mMovieClip;
         var _loc7_:int = 0;
         var _loc9_:String = _loc2_.var_13.var_930 == 10 ? "10" : "0" + _loc2_.var_13.var_930;
         var _loc10_:uint = class_64.method_830(_loc2_.var_13.var_930);
         MathUtil.method_2(TextField(this.var_356.mMovieClip.am_Idols),String(_loc10_));
         var _loc11_:int = 0;
         while(_loc11_ < const_324)
         {
            _loc7_++;
            if(_loc7_ == _loc1_)
            {
               _loc7_++;
            }
            _loc8_ = String(class_64.const_26[_loc7_]);
            if(!(1 << _loc7_ - 1 & _loc3_))
            {
               (_loc5_ = MovieClip(this.var_1908.getChildByName("am_RerollAnim" + _loc11_))).gotoAndStop(0);
               (_loc6_ = _loc5_.am_Realm).gotoAndStop(_loc8_);
               (_loc5_ = MovieClip(this.var_893.getChildByName("am_Realm" + _loc11_))).gotoAndStop(_loc8_);
               _loc12_ = class_14.var_142[_loc8_ + _loc9_];
               _loc13_ = this.method_635(_loc2_.var_8,_loc12_);
               MathUtil.method_8(TextField(this.var_893.getChildByName("am_Property" + _loc11_)),_loc13_,ScreenArmory.const_11,ScreenArmory.const_47);
            }
            else
            {
               _loc14_ = class_14.var_142[_loc8_ + _loc9_];
               _loc15_ = this.method_635(_loc2_.var_8,_loc14_);
               MathUtil.method_8(TextField(this.var_893.getChildByName("am_Property" + _loc11_)),_loc15_,ScreenArmory.const_9,ScreenArmory.const_17);
            }
            _loc11_++;
         }
         this.var_733.EnableButton();
      }
      
      public function method_955() : void
      {
         var _loc1_:class_64 = var_1.mMagicForgeStatus.RetreiveCharm();
         var _loc2_:class_1 = _loc1_.method_115();
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:MovieClip = this.var_356.mMovieClip;
         var _loc4_:MovieClip;
         (_loc4_ = _loc3_.am_CurrentRealm).gotoAndStop(_loc2_.var_115);
         MathUtil.method_2(_loc3_.am_SecondaryProperty,_loc1_.method_171());
         var _loc5_:uint;
         if((_loc5_ = uint(var_1.mMagicForgeStatus.usedlist)) == const_677)
         {
            this.var_733.DisableButton("Inactive");
         }
      }
      
      public function OnInitDisplay() : void
      {
         var _loc1_:Vector.<class_33> = null;
         this.var_2295 = 0;
         this.method_1736();
         this.var_356.Hide();
         if(!var_1.screenInteractiveTutorial.CheckCompletedTutorials(class_89.const_352))
         {
            this.var_60.Show();
            _loc1_ = new Vector.<class_33>();
            _loc1_.push(this.var_2095);
            _loc1_.push(this.var_1367);
            var_1.screenInteractiveTutorial.SetTutorial(class_89.const_352,this,this.var_60,_loc1_);
         }
      }
      
      override public function OnTickScreen() : void
      {
         var _loc2_:int = 0;
         var _loc3_:class_33 = null;
         var _loc4_:class_33 = null;
         var _loc5_:TextField = null;
         var _loc1_:uint = uint(var_1.mMagicForgeStatus.secondary);
         if(this.var_2295 != _loc1_ && this.var_356.mbVisible)
         {
            if(!this.var_1301)
            {
               _loc2_ = int(this.method_1909(_loc1_));
               _loc3_ = this.var_1940[_loc2_];
               _loc4_ = this.var_1736[_loc2_];
               _loc3_.PlayAnimation("Ready");
               _loc4_.PlayAnimation(class_64.const_26[_loc1_]);
               this.var_1301 = _loc3_;
               MovieClip(this.var_893.getChildByName("am_Realm" + _loc2_)).gotoAndStop(1);
               this.var_733.DisableButton("Inactive");
               _loc5_ = this.var_893["am_Property" + _loc2_];
               MathUtil.method_8(_loc5_,_loc5_.text,ScreenArmory.const_9,ScreenArmory.const_17);
            }
            else if(this.var_1301.var_175 >= const_1244)
            {
               if(var_1.mMagicForgeStatus.usedlist != const_677)
               {
                  this.var_733.EnableButton();
               }
               this.method_955();
               this.var_1301 = null;
               this.var_2295 = _loc1_;
            }
         }
      }
      
      private function method_1771(param1:MouseEvent = null) : void
      {
         this.method_1585();
      }
      
      private function method_1632(param1:MouseEvent = null) : void
      {
         this.var_356.Show();
         this.method_609();
         this.method_955();
      }
      
      private function method_1302(param1:MouseEvent) : void
      {
         var _loc4_:Packet = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(!var_1.mMagicForgeStatus.CanReroll())
         {
            return;
         }
         var _loc2_:class_1 = var_1.mMagicForgeStatus.GetCurrentlyCrafting();
         var _loc3_:uint = class_64.method_830(_loc2_.var_930);
         if(var_1.mMammothIdols < _loc3_)
         {
            var_1.screenBuyIdols.Display(_loc3_ - var_1.mMammothIdols);
         }
         else
         {
            this.var_733.DisableButton("Inactive");
            (_loc4_ = new Packet(LinkUpdater.const_1105)).method_20(class_111.const_432,var_1.mMagicForgeStatus.usedlist);
            var_1.serverConn.SendPacket(_loc4_);
         }
      }
      
      private function method_1909(param1:uint) : uint
      {
         var _loc2_:uint = class_75.method_337(var_1.mMagicForgeStatus.primary);
         if(param1 > _loc2_)
         {
            param1--;
         }
         param1--;
         return param1;
      }
      
      private function method_1731(param1:MouseEvent) : void
      {
         Refresh();
         this.var_356.Hide();
      }
      
      public function method_1736() : void
      {
         var _loc1_:class_64 = var_1.mMagicForgeStatus.RetreiveCharm();
         if(Boolean(_loc1_) && Boolean(_loc1_.var_13))
         {
            this.method_609();
         }
      }
      
      public function method_1585() : void
      {
         var _loc4_:uint = 0;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(!var_1.mMagicForgeStatus.CanAccept())
         {
            return;
         }
         var _loc1_:class_64 = var_1.mMagicForgeStatus.RetreiveCharm();
         if(!_loc1_.method_396())
         {
            _loc4_ = uint(var_1.mCraftTalentData.GetXpGained(_loc1_.var_13));
            var_1.mCraftTalentData.SetXP(var_1.mCraftTalentData.craftXP + _loc4_);
         }
         var_1.mMagicForgeStatus.FreeForge();
         var _loc2_:String = _loc1_.var_8 == class_64.const_196 ? "L" : (_loc1_.var_8 == class_64.const_180 ? "R" : "M");
         var_1.screenNotification.ShowNotification(class_46.const_211,_loc1_.method_49(),_loc2_,true,null,null,_loc1_);
         var_1.GainCharm(_loc1_,true);
         var _loc3_:Packet = new Packet(LinkUpdater.const_1273);
         var_1.serverConn.SendPacket(_loc3_);
         Hide();
         var_1.screenForge.Display();
      }
      
      private function method_635(param1:uint, param2:class_1) : String
      {
         var _loc3_:Number = 0;
         if(param1 == 0)
         {
            _loc3_ = class_64.const_522;
         }
         if(param1 == 1)
         {
            _loc3_ = class_64.const_593;
         }
         if(param1 == 2)
         {
            _loc3_ = class_64.const_729;
         }
         var _loc4_:String = param2.var_203;
         var _loc5_:Number = _loc3_ * parseFloat(_loc4_);
         var _loc6_:int = _loc4_.indexOf(" ");
         var _loc7_:int = _loc4_.indexOf("%");
         var _loc8_:String = "";
         if(_loc7_ > -1)
         {
            _loc8_ = "%";
         }
         return "+" + _loc5_ + _loc8_ + " " + _loc4_.substr(_loc6_ + 1);
      }
   }
}
