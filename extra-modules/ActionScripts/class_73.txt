package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   
   public class class_73 extends class_32
   {
      
      private static const const_1176:uint = 1100;
      
      private static const const_953:uint = 1700;
      
      private static const const_1424:uint = 2500;
      
      private static const const_1022:uint = 7000;
       
      
      private var var_1929:Boolean;
      
      private var var_1883:Boolean;
      
      private var var_2670:uint;
      
      private var var_2791:uint;
      
      private var var_994:uint;
      
      private var var_2206:uint;
      
      private var var_991:String;
      
      private var var_155:class_18;
      
      private var var_2186:String;
      
      private var var_396:class_33;
      
      private var var_2104:uint;
      
      private var var_1537:class_138;
      
      private var var_2329:class_138;
      
      private var var_1874:class_138;
      
      private var var_1429:class_33;
      
      private var var_962:class_33;
      
      private var var_1540:class_33;
      
      private var var_1050:class_33;
      
      private var var_2891:class_33;
      
      private var var_910:class_33;
      
      private var var_1469:class_33;
      
      private var var_2718:class_33;
      
      private var mRewardFloater1:class_33;
      
      private var mRewardFloater2:class_33;
      
      private var var_2726:class_33;
      
      private var var_2398:class_138;
      
      private var var_2164:class_138;
      
      private var var_1191:MovieClip;
      
      private var var_1085:MovieClip;
      
      private var var_446:class_33;
      
      private var var_699:SuperAnimInstance;
      
      private var var_487:class_33;
      
      private var var_618:SuperAnimInstance;
      
      private var var_453:SuperAnimInstance;
      
      private var var_269:class_33;
      
      private var var_1253:class_33;
      
      public function class_73(param1:Game)
      {
         super(param1,"a_ScreenLockBoxAD",null);
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_1537 = method_21(var_2.am_KeyCounter);
         this.var_2329 = method_21(var_2.am_LockboxCounter);
         var _loc1_:MovieClip = var_2.am_RewardFloater0;
         this.mRewardFloater1 = method_1(_loc1_);
         this.mRewardFloater2 = method_1(var_2.am_RewardFloater1);
         this.var_2726 = method_5(_loc1_.am_Icon,this.method_1800,this.method_1624,this.HideTooltip);
         this.var_2398 = method_21(_loc1_.am_NameWrapper.am_Name);
         this.var_2164 = method_21(_loc1_.am_TypeWrapper.am_Type);
         this.var_1191 = _loc1_.am_Icon.am_ItemIconHolder;
         this.var_1085 = _loc1_.am_Icon.am_MaskIconHolder;
         this.var_2718 = method_1(var_2.am_OpenButtonBase);
         this.var_1429 = method_10(var_2.am_Ok,this.method_1132);
         this.var_962 = method_10(var_2.am_Open,this.method_782);
         this.var_1540 = method_10(var_2.am_OpenAnother,this.method_782);
         this.var_1050 = method_10(var_2.am_GetKeys,this.method_1461);
         this.var_2891 = method_10(var_2.am_OpenSigilStore,this.method_1889);
         this.var_910 = method_10(var_2.am_GetTroves,this.method_1208);
         var _loc2_:MovieClip = var_2.am_Lockbox;
         this.var_396 = method_1(_loc2_);
         this.var_1874 = method_92(var_2.am_EarnedSigils);
         this.var_487 = method_1(var_2.am_SparkleContainer);
         this.var_446 = method_1(var_2.am_SparkleFoutainContainer);
         this.var_269 = method_1(var_2.am_AmbientGlowContainer);
         this.var_1469 = method_1(var_2.am_RewardsTooltip);
         this.var_1253 = method_1(var_2.am_SigilFloatAnim);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1537 = null;
         this.var_2329 = null;
         this.var_962 = null;
         this.var_1050 = null;
         this.var_1540 = null;
         this.mRewardFloater1 = null;
         this.mRewardFloater2 = null;
         this.var_2398 = null;
         this.var_2164 = null;
         this.var_2718 = null;
         this.var_1874 = null;
         this.var_155 = null;
         method_14(this.var_1191);
         this.var_1191 = null;
         method_14(this.var_1085);
         this.var_1085 = null;
         this.var_2726 = null;
         this.var_1429 = null;
         this.var_1253 = null;
         this.var_910 = null;
         this.var_1469 = null;
         this.method_714();
         this.var_487 = null;
         this.var_446 = null;
         this.var_269 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:class_151 = var_1.mLockboxData.mOwnedLockboxes[var_1.mLockboxData.mLockboxID];
         this.var_2329.SetText(!!_loc1_ ? String(_loc1_.stackCount) : "0");
         if(!_loc1_ || !_loc1_.stackCount)
         {
            this.var_910.Show();
         }
         else
         {
            this.var_910.Hide();
         }
         var _loc2_:uint = uint(var_1.mLockboxData.mLockboxKeys);
         if(!_loc2_)
         {
            this.var_1050.Show();
         }
         else
         {
            this.var_1050.Hide();
         }
         this.var_1537.SetText(String(_loc2_));
         this.var_1874.var_213 = var_1.mLockboxData.mRoyalSigils;
      }
      
      override public function OnTickScreen() : void
      {
         var _loc2_:String = null;
         var _loc1_:uint = uint(var_1.mTimeThisTick);
         if(this.var_994)
         {
            if(_loc1_ - this.var_2206 > this.var_994)
            {
               this.var_1429.EnableButton();
               this.var_1540.EnableButton();
               this.var_1050.EnableButton();
               this.var_910.EnableButton();
               this.var_994 = 0;
               var_1.bSuppressGoldDisplay = false;
            }
         }
         if(_loc1_ - this.var_2670 > this.var_2791)
         {
            _loc2_ = !!this.var_396.mActiveTimeline ? this.var_396.mActiveTimeline.name : null;
            if(_loc2_ == "Open" || _loc2_ == "OpenJackpot" || _loc2_ == "Jitter")
            {
               this.var_396.method_147("SpawnNewChest","LockBox_Spawn");
               if(this.var_269.mbVisible)
               {
                  this.var_269.Hide();
                  this.var_453.m_TheDO.visible = false;
               }
            }
            else
            {
               this.var_396.method_147("Idle","LockBox_Jump");
            }
            this.method_248(_loc1_);
            this.var_1929 = false;
         }
      }
      
      public function OnInitDisplay() : void
      {
         this.var_962.Show();
         this.var_1469.Show();
         this.var_1929 = false;
         this.var_1883 = false;
         this.var_2186 = !!var_1.clientEnt ? String(var_1.clientEnt.entType.className) : "Mage";
         this.var_2104 = 0;
         this.var_1874.SetText("--");
         this.var_1537.var_213 = 0;
         this.var_1537.SetText("0");
         if(this.var_487.mbVisible)
         {
            this.var_487.Hide();
         }
         if(this.var_446.mbVisible)
         {
            this.var_446.Hide();
         }
         if(this.var_269.mbVisible)
         {
            this.var_269.Hide();
         }
         this.var_1253.Hide();
         this.method_248(var_1.mTimeThisTick);
         this.var_396.ClearAnimation();
         this.var_396.method_147("Drop","LockBox_Spawn");
         this.var_994 = 0;
         this.var_2206 = 0;
         this.mRewardFloater1.ClearAnimation();
         this.mRewardFloater2.ClearAnimation();
         this.method_1517();
         if(!(var_1.mAlertState & Game.const_186))
         {
            var_1.UpdateAlert(Game.const_186);
         }
         if(var_1.mTutorialStage == Game.const_246 || var_1.mTutorialStage == Game.const_253)
         {
            var_1.SetNewTutorialStage(Game.const_302);
         }
      }
      
      override public function Hide() : void
      {
         if(this.method_972())
         {
            return;
         }
         this.method_714();
         method_14(this.var_1191);
         method_14(this.var_1085);
         super.Hide();
      }
      
      public function method_972() : Boolean
      {
         return Boolean(this.var_994) || this.var_1883;
      }
      
      private function method_1461(param1:MouseEvent) : void
      {
         var_1.screenLockBoxBuyKeys.Display(true);
      }
      
      private function method_1208(param1:MouseEvent) : void
      {
         var_1.screenLockBoxBuyTroves.Display(true);
      }
      
      public function method_1978(param1:uint) : void
      {
         if(this.var_269.mbVisible)
         {
            this.var_269.Hide();
            this.var_453.m_TheDO.visible = false;
         }
         this.var_396.ClearAnimation();
         this.var_396.method_147("Drop","LockBox_Spawn");
         this.method_248(var_1.mTimeThisTick);
      }
      
      private function method_782(param1:MouseEvent) : void
      {
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(this.var_1469.mbVisible)
         {
            this.var_1469.Hide();
         }
         var _loc2_:class_151 = var_1.mLockboxData.mOwnedLockboxes[var_1.mLockboxData.mLockboxID];
         if(!_loc2_ || !_loc2_.stackCount)
         {
            var_1.screenLockBoxBuyTroves.Display(true);
         }
         else if(!var_1.mLockboxData.mLockboxKeys)
         {
            var_1.screenLockBoxBuyKeys.Display(true);
         }
         else
         {
            this.var_1429.DisableButton("Inactive");
            this.var_1540.DisableButton("Inactive");
            this.var_1050.DisableButton("Inactive");
            this.var_910.DisableButton("Inactive");
            if(this.var_962.mbVisible)
            {
               this.var_962.Hide();
            }
            var_1.mLockboxData.OpenLockbox(var_1.mLockboxData.mLockboxID);
            this.var_1883 = true;
         }
      }
      
      private function method_1889(param1:MouseEvent) : void
      {
         var_1.screenRoyalSigilStore.Display();
         var_1.screenRoyalSigilStore.mbFromLockBox = true;
      }
      
      public function method_1148(param1:String, param2:class_18) : void
      {
         var _loc5_:MovieClip = null;
         var _loc3_:uint = uint(var_1.mTimeThisTick);
         this.mRewardFloater1.ClearAnimation();
         this.mRewardFloater2.ClearAnimation();
         var _loc4_:String;
         if((_loc4_ = param2.var_8) == "L")
         {
            if(!this.var_446.mbVisible)
            {
               this.var_446.Show();
               this.var_699.m_TheDO.visible = true;
            }
            this.var_699.m_Seq.method_34(Seq.C_USEPOWER,"Sparkle",false);
            if(!this.var_269.mbVisible)
            {
               this.var_269.Show();
               this.var_453.m_TheDO.visible = true;
            }
            this.var_453.m_Seq.method_34(Seq.C_USEPOWER,"AmbientGlow",true);
            if(this.var_487.mbVisible)
            {
               this.var_487.Hide();
               this.var_618.m_TheDO.visible = false;
            }
            this.mRewardFloater1.method_147("DisplayJackpot","LockBox_Legendary_Reveal");
            this.mRewardFloater2.PlayAnimation("DisplayJackpot");
            this.method_248(_loc3_,const_1022);
            this.var_396.method_147("OpenJackpot","LockBox_Legendary_Open");
            this.var_994 = const_953;
         }
         else
         {
            if(!this.var_487.mbVisible)
            {
               this.var_487.Show();
               this.var_618.m_TheDO.visible = true;
            }
            this.var_618.m_Seq.method_34(Seq.C_USEPOWER,"Sparkle",false);
            if(this.var_446.mbVisible)
            {
               this.var_446.Hide();
               this.var_699.m_TheDO.visible = false;
            }
            if(this.var_269.mbVisible)
            {
               this.var_269.Hide();
               this.var_453.m_TheDO.visible = false;
            }
            this.mRewardFloater1.method_147("DisplayNormal","LockBox_Basic_Reveal");
            this.mRewardFloater2.PlayAnimation("DisplayNormal");
            if(!this.var_1929)
            {
               this.var_396.method_147("Open","LockBox_Basic_Open");
            }
            else
            {
               this.var_396.PlayAnimation("Jitter");
               SoundManager.Play("LockBox_Basic_Open",1,false,300);
            }
            this.method_248(_loc3_);
            this.var_994 = const_1176;
            this.var_1929 = true;
         }
         this.var_2206 = _loc3_;
         this.var_1429.DisableButton("Inactive");
         this.var_1540.DisableButton("Inactive");
         this.var_1050.DisableButton("Inactive");
         this.var_910.DisableButton("Inactive");
         if(this.var_962.mbVisible)
         {
            this.var_962.Hide();
         }
         if(param2.var_86 == class_18.const_190 || param2.var_86 == class_18.const_291 || param2.var_86 == class_18.const_411 || param2.var_86 == class_18.const_171)
         {
            _loc5_ = this.var_1085;
            method_14(this.var_1191);
         }
         else
         {
            _loc5_ = this.var_1191;
            method_14(this.var_1085);
         }
         param2.method_996(var_1,this,_loc5_,param1);
         MathUtil.method_8(this.var_2398.mTextField,param2.method_839(this.var_2186,param1),class_101.method_37(_loc4_,null,param2.var_86));
         this.var_2164.SetText(param2.method_734());
         this.var_991 = param1;
         this.var_155 = param2;
         var _loc6_:uint = uint(var_1.mLockboxData.mEarnedSigilsCache);
         var _loc7_:String = String(_loc6_);
         this.var_2104 += _loc6_;
         MathUtil.method_2(this.mRewardFloater2.mMovieClip.am_CountWrapper.am_Count,"x" + _loc7_);
         MathUtil.method_2(this.var_1253.mMovieClip.am_Wrapper.am_Amount,"+" + _loc7_);
         this.var_1253.Show();
         this.var_1253.PlayAnimation("Float",class_33.const_14);
         this.var_1883 = false;
         Refresh();
      }
      
      private function method_1624(param1:MouseEvent) : void
      {
         var _loc3_:class_1 = null;
         var _loc4_:class_64 = null;
         var _loc5_:class_7 = null;
         var _loc6_:class_87 = null;
         var _loc7_:GearType = null;
         var _loc8_:class_20 = null;
         var _loc9_:class_3 = null;
         var _loc2_:String = this.var_155.var_86;
         if(_loc2_ == class_18.const_333)
         {
            var_1.screenHudTooltip.ShowBasicItemTooltip(this.var_155.method_839(this.var_2186,this.var_991),_loc2_,this.var_155.var_8,447.75,81.8);
         }
         else if(_loc2_ == class_18.const_374)
         {
            _loc3_ = class_14.var_142[this.var_155.var_162];
            _loc4_ = class_64.method_56(_loc3_.var_68);
            if(this.var_155.var_8 == "L")
            {
               var_1.screenHudTooltip.ShowCharmTooltip(_loc4_,448.05,15.8);
            }
            else
            {
               var_1.screenHudTooltip.ShowCharmTooltip(_loc4_,448.05,42.8);
            }
         }
         else if(_loc2_ == class_18.const_171 || _loc2_ == "Pet")
         {
            _loc5_ = this.var_155.var_8 == "L" ? class_14.var_233[this.var_155.var_162] : class_14.var_233[this.var_991];
            if(_loc6_ = var_1.mEggPetInfo.GetNewestPetDataByID(_loc5_.var_104))
            {
               var_1.screenHudTooltip.ShowPetTooltip(_loc6_,true,447.3,42.8);
            }
         }
         else if(_loc2_ == class_18.const_190)
         {
            _loc7_ = class_14.gearTypesDict[this.var_991];
            var_1.screenHudTooltip.ShowGearTooltip(var_1.clientEnt,_loc7_.gearID,false,null,446.6,22.75);
         }
         else if(_loc2_ == class_18.const_291)
         {
            _loc8_ = class_14.var_362[this.var_155.var_162];
            var_1.screenHudTooltip.ShowBasicDescriptionTooltip(_loc8_.displayName,_loc2_,this.var_155.var_8,_loc8_.description,447.75,60.75);
         }
         else if(_loc2_ == class_18.const_384)
         {
            var_1.screenHudTooltip.ShowBasicItemTooltip("Pile of Gold","Gold",this.var_155.var_8,447.75,81.8);
         }
         else
         {
            _loc9_ = class_14.var_303[this.var_155.var_162];
            var_1.screenHudTooltip.ShowBasicDescriptionTooltip(_loc9_.displayName,this.var_155.method_734(),this.var_155.var_8,_loc9_.description,447.75,60.75);
         }
      }
      
      private function method_1800(param1:MouseEvent) : void
      {
         var _loc2_:* = null;
         var _loc3_:String = null;
         var _loc4_:class_21 = null;
         var _loc5_:class_1 = null;
         var _loc6_:class_64 = null;
         var _loc7_:class_7 = null;
         var _loc8_:class_87 = null;
         var _loc9_:GearType = null;
         var _loc10_:String = null;
         var _loc11_:class_20 = null;
         var _loc12_:class_3 = null;
         if(param1.ctrlKey)
         {
            _loc3_ = this.var_155.var_86;
            if(_loc3_ == class_18.const_333)
            {
               _loc4_ = class_14.var_1194[this.var_991];
               _loc2_ = "{" + class_127.const_8[8] + ":" + _loc4_.var_57.toString() + "}";
               var_1.screenChat.AddItemInfoToChatEntry("[" + _loc4_.displayName + "]",_loc2_);
            }
            else if(_loc3_ == class_18.const_374)
            {
               _loc5_ = class_14.var_142[this.var_155.var_162];
               _loc6_ = class_64.method_56(_loc5_.var_68);
               _loc2_ = "{" + class_127.const_8[1] + ":" + _loc6_.method_75().toString() + "}";
               var_1.screenChat.AddItemInfoToChatEntry("[" + _loc6_.method_49() + "]",_loc2_);
            }
            else if(_loc3_ == class_18.const_171 || _loc3_ == "Pet")
            {
               _loc7_ = this.var_155.var_8 == "L" ? class_14.var_233[this.var_155.var_162] : class_14.var_233[this.var_991];
               _loc8_ = var_1.mEggPetInfo.GetPetDataByIDIteration(_loc7_.var_104,0);
               _loc2_ = "{" + class_127.const_8[3] + ":" + _loc7_.var_104.toString() + ":" + _loc8_.var_23.toString() + ":" + _loc8_.var_110.toString() + "}";
               var_1.screenChat.AddItemInfoToChatEntry("[" + _loc7_.displayName + "]",_loc2_);
            }
            else if(_loc3_ == class_18.const_190)
            {
               _loc9_ = class_14.gearTypesDict[this.var_991];
               _loc10_ = EntTypeGear.method_172(_loc9_.gearName,0,0,0,0,0);
               _loc2_ = "{" + class_127.const_8[0] + ":" + _loc10_ + "}";
               var_1.screenChat.AddItemInfoToChatEntry("[" + _loc9_.displayName + "]",_loc2_);
            }
            else if(_loc3_ == class_18.const_291)
            {
               _loc11_ = class_14.var_362[this.var_155.var_162];
               _loc2_ = "{" + class_127.const_8[4] + ":" + _loc11_.var_197.toString() + "}";
               var_1.screenChat.AddItemInfoToChatEntry("[" + _loc11_.displayName + "]",_loc2_);
            }
            else
            {
               _loc12_ = class_14.var_303[this.var_155.var_162];
               _loc2_ = "{" + class_127.const_8[9] + ":" + String(_loc12_.consumableID) + "}";
               var_1.screenChat.AddItemInfoToChatEntry("[" + _loc12_.displayName + "]",_loc2_);
            }
         }
      }
      
      private function HideTooltip(param1:MouseEvent) : void
      {
         var_1.screenHudTooltip.HideTooltip(true);
      }
      
      private function method_1132(param1:MouseEvent) : void
      {
         this.Hide();
      }
      
      private function method_248(param1:uint, param2:uint = 2500) : void
      {
         this.var_2791 = param2;
         this.var_2670 = param1;
      }
      
      private function method_1517() : void
      {
         var _loc1_:GfxType = new GfxType();
         _loc1_.animClass = "a_SparkleGroup";
         _loc1_.var_29 = "UI_4.swf";
         _loc1_.animScale = 1;
         _loc1_.moveAnimSpeed = 1;
         this.var_618 = new SuperAnimInstance(var_1,_loc1_,false);
         this.var_487.mMovieClip.removeChildren();
         this.var_487.mMovieClip.addChild(this.var_618.m_TheDO);
         this.var_618.m_TheDO.visible = false;
         var _loc2_:GfxType = new GfxType();
         _loc2_.animClass = "a_SparkleFountainGroup";
         _loc2_.var_29 = "UI_4.swf";
         _loc2_.animScale = 1;
         _loc2_.moveAnimSpeed = 1;
         this.var_699 = new SuperAnimInstance(var_1,_loc2_,false);
         this.var_446.mMovieClip.removeChildren();
         this.var_446.mMovieClip.addChild(this.var_699.m_TheDO);
         this.var_699.m_TheDO.visible = false;
         var _loc3_:GfxType = new GfxType();
         _loc3_.animClass = "a_Lockbox_AmbientGlowAnim";
         _loc3_.var_29 = "UI_4.swf";
         _loc3_.animScale = 1;
         _loc3_.moveAnimSpeed = 1;
         this.var_453 = new SuperAnimInstance(var_1,_loc3_,false);
         this.var_269.mMovieClip.removeChildren();
         this.var_269.mMovieClip.addChild(this.var_453.m_TheDO);
         this.var_453.m_TheDO.visible = false;
      }
      
      private function method_714() : void
      {
         if(this.var_618)
         {
            this.var_487.mMovieClip.removeChildren();
            this.var_618.DestroySuperAnimInstance();
            this.var_618 = null;
         }
         if(this.var_699)
         {
            this.var_446.mMovieClip.removeChildren();
            this.var_699.DestroySuperAnimInstance();
            this.var_699 = null;
         }
         if(this.var_453)
         {
            this.var_269.mMovieClip.removeChildren();
            this.var_453.DestroySuperAnimInstance();
            this.var_453 = null;
         }
      }
   }
}
