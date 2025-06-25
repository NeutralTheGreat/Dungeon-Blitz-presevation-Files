package
{
   import flash.display.Bitmap;
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.filters.ColorMatrixFilter;
   
   public class class_99 extends class_32
   {
      
      private static const const_276:uint = 3;
      
      private static const const_930:ColorMatrixFilter = new ColorMatrixFilter([1,0,0,0,-100,0,1,0,0,-100,0,0,1,0,-100,0,0,0,1,0]);
      
      private static const const_448:uint = 8;
      
      private static const const_115:uint = 18;
      
      private static const const_203:uint = 44;
       
      
      public var var_60:class_33;
      
      public var var_1302:Boolean = true;
      
      private var var_759:Vector.<class_87>;
      
      private var var_1045:Boolean;
      
      private var var_190:class_33;
      
      private var var_499:class_33;
      
      private var var_712:class_33;
      
      private var var_1552:class_33;
      
      private var var_449:class_33;
      
      private var var_519:class_33;
      
      private var var_520:class_33;
      
      private var var_1746:class_33;
      
      private var var_261:class_33;
      
      private var var_1952:class_33;
      
      private var var_1882:class_33;
      
      private var var_214:class_33;
      
      private var var_1476:class_33;
      
      private var var_1134:class_33;
      
      private var var_1628:class_33;
      
      private var var_2377:class_33;
      
      private var var_516:class_33;
      
      private var var_1324:class_33;
      
      private var var_613:class_33;
      
      private var var_1049:int;
      
      private var var_1840:int;
      
      private var var_191:class_87;
      
      private var var_211:int;
      
      private var var_1130:class_16;
      
      private var var_2452:class_33;
      
      private var var_867:Vector.<class_33>;
      
      private var var_2663:class_33;
      
      private var var_727:Vector.<class_33>;
      
      private var var_1228:GfxType;
      
      private var var_788:EntType;
      
      private var var_744:class_33;
      
      private var var_799:class_33;
      
      private var var_826:class_33;
      
      private var var_1231:Vector.<class_33>;
      
      private var var_2375:int;
      
      public function class_99(param1:Game)
      {
         super(param1,"a_ScreenBarn","am_Panel");
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_759 = new Vector.<class_87>();
         var _loc1_:MovieClip = var_2.am_Shelf;
         var _loc2_:MovieClip = _loc1_.am_PetInventory;
         this.var_2452 = method_1(_loc2_);
         this.var_867 = new Vector.<class_33>(const_115,true);
         var _loc3_:uint = 0;
         while(_loc3_ < const_115)
         {
            this.var_867[_loc3_] = method_3(_loc2_["am_Slot" + _loc3_] as MovieClip,_loc3_,this.method_1714,this.method_1370,this.HideTooltip);
            _loc3_++;
         }
         var _loc4_:MovieClip = _loc1_.am_EggGroup;
         this.var_2663 = method_1(_loc4_);
         this.var_727 = new Vector.<class_33>(const_448,true);
         _loc3_ = 0;
         while(_loc3_ < const_448)
         {
            this.var_727[_loc3_] = method_3(_loc4_["am_Egg" + _loc3_] as MovieClip,_loc3_,this.method_1519,this.method_1405,this.HideTooltip);
            _loc3_++;
         }
         this.var_2377 = method_1(_loc1_.am_EggTimer);
         this.var_214 = method_1(var_2.am_TrainPanel);
         this.var_1476 = method_1(var_2.am_CancelPanel);
         this.var_1134 = method_1(var_2.am_SpeedUpPanel);
         this.var_449 = method_1(var_2.am_WarningAnim);
         this.var_519 = method_1(var_2.am_XPWarnAnim);
         this.var_520 = method_1(var_2.am_BarnLevelWarning);
         this.var_1746 = method_1(var_2.am_MaxRank);
         this.var_261 = method_1(var_2.am_Notice);
         method_10(var_2.am_CancelPanel.am_NeverMind,this.method_650);
         this.var_516 = method_10(var_2.am_TrainPanel.am_HatchEgg,this.TrainOrHatchClicked);
         this.var_1324 = method_10(var_2.am_SpeedUpPanel.am_SpeedUp,this.method_1410);
         this.var_190 = method_17(var_2.am_ProgressBar.am_Progress,"Progress",0);
         this.var_712 = method_1(var_2.am_TrainingIcon);
         this.var_499 = method_1(var_2.am_ProgressBar);
         this.var_1552 = method_5(var_2.am_Cancel,this.method_650);
         this.var_1952 = method_10(mWindow.mMovieClip.am_GlobalUpgradePanel.am_Upgrade,this.UpgradeBuilding);
         this.var_1882 = method_1(mWindow.mMovieClip.am_GlobalUpgradePanel);
         var _loc5_:MovieClip = var_2.am_Incubator.am_IncubatorTop;
         this.var_613 = method_1(_loc5_.am_HatchingEgg);
         this.var_744 = method_1(_loc5_.am_HotWater);
         this.var_799 = method_1(_loc5_.am_CalmWater);
         this.var_826 = method_1(_loc5_.am_TrainingAnim);
         var _loc6_:MovieClip = _loc5_.am_SwapAnimGroup;
         this.var_1231 = new Vector.<class_33>(const_276,true);
         _loc3_ = 0;
         while(_loc3_ < const_276)
         {
            this.var_1231[_loc3_] = method_1(_loc6_["am_SwapAnim" + _loc3_] as MovieClip);
            _loc3_++;
         }
         this.var_1628 = method_10(var_2.am_CancelPanel.am_CancelTraining,this.method_1083);
         method_208();
         this.var_60 = method_1(var_2.am_TutorialInteraction);
         this.var_60.Hide();
         method_23(var_2.am_Close);
         var_2.cacheAsBitmap = true;
      }
      
      override public function OnDestroyScreen() : void
      {
         var _loc3_:MovieClip = null;
         var _loc4_:Bitmap = null;
         var _loc1_:uint = 0;
         while(_loc1_ < const_115)
         {
            _loc3_ = this.var_867[_loc1_].mMovieClip.am_ItemIconHolder;
            _loc4_ = _loc3_.removeChildAt(0) as Bitmap;
            _loc4_ = null;
            _loc1_++;
         }
         var _loc2_:MovieClip = this.var_712.mMovieClip.am_ItemIconHolder;
         while(_loc2_.numChildren)
         {
            _loc2_.removeChildAt(0);
         }
         this.var_712 = null;
         if(mPaperDoll)
         {
            mPaperDoll.DestroyEntity(false);
            mPaperDoll = null;
         }
         this.var_613 = null;
         this.var_2452 = null;
         this.var_867 = null;
         this.var_2663 = null;
         this.var_727 = null;
         this.var_190 = null;
         this.var_1552 = null;
         this.var_516 = null;
         this.var_214 = null;
         this.var_1476 = null;
         this.var_1134 = null;
         this.var_2377 = null;
         this.var_449 = null;
         this.var_1324 = null;
         this.var_261 = null;
         this.var_1952 = null;
         this.var_1882 = null;
         this.var_191 = null;
         this.var_499 = null;
         this.var_519 = null;
         this.var_520 = null;
         this.var_1228 = null;
         this.var_788 = null;
         this.var_1231 = null;
         this.var_744 = null;
         this.var_799 = null;
         this.var_826 = null;
         this.var_1628 = null;
         this.var_1746 = null;
         this.var_60 = null;
      }
      
      public function OnInitDisplay() : void
      {
         var _loc2_:Vector.<class_33> = null;
         this.var_1302 = true;
         var _loc1_:uint = 0;
         while(_loc1_ < const_276)
         {
            this.var_1231[_loc1_].Hide();
            _loc1_++;
         }
         this.var_1045 = false;
         this.var_449.Hide();
         this.var_519.Hide();
         this.var_520.Hide();
         this.ResetSelectors();
         if(!var_1.screenInteractiveTutorial.CheckCompletedTutorials(class_89.const_281))
         {
            this.var_60.Show();
            _loc2_ = new Vector.<class_33>();
            _loc2_.push(this.var_727[0]);
            _loc2_.push(this.var_516);
            _loc2_.push(this.var_1324);
            var_1.screenInteractiveTutorial.SetTutorial(class_89.const_281,this,this.var_60,_loc2_);
         }
      }
      
      public function ResetSelectors(param1:Boolean = false) : void
      {
         if(this.var_211 != -1)
         {
            this.var_727[this.var_211].mMovieClip.am_Selector.visible = false;
         }
         this.var_211 = -1;
         this.var_1130 = null;
         if(this.var_1049 != -1)
         {
            this.var_867[this.var_1049].mMovieClip.am_Selector.visible = false;
         }
         this.var_1840 = -1;
         this.var_1049 = -1;
         this.var_191 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc7_:MovieClip = null;
         var _loc8_:MovieClip = null;
         var _loc15_:MovieClip = null;
         var _loc16_:MovieClip = null;
         var _loc17_:uint = 0;
         var _loc18_:* = false;
         var _loc19_:uint = 0;
         var _loc20_:* = false;
         var _loc21_:uint = 0;
         var _loc22_:String = null;
         var _loc23_:class_16 = null;
         var _loc24_:class_7 = null;
         var _loc25_:class_33 = null;
         var _loc26_:uint = 0;
         var _loc27_:class_16 = null;
         var _loc28_:class_87 = null;
         var _loc29_:uint = 0;
         var _loc30_:* = false;
         var _loc1_:class_9 = var_1.mBuildingInfo.GetOwnedBuildingByName("Barn");
         this.var_2375 = _loc1_.rank;
         var_1.UpdateBuildingUpgradePanel(this.var_1882.mMovieClip,_loc1_,this.var_1952);
         var _loc2_:class_81 = var_1.mEggPetInfo;
         var _loc3_:MovieClip = this.var_712.mMovieClip.am_ItemIconHolder;
         var _loc4_:Number = Number(var_1.main.overallScale);
         this.var_1746.Hide();
         var _loc5_:* = _loc2_.mEggStatus == class_81.const_131;
         var _loc6_:* = _loc2_.mPetTrainingStatus == class_81.const_107;
         if(!_loc5_ && !_loc6_)
         {
            this.var_214.Show();
            this.var_190.Show();
            this.var_1134.Hide();
            this.var_1552.Hide();
            this.var_1476.Hide();
            this.var_449.Hide();
            this.var_519.Hide();
            this.var_520.Hide();
            this.var_190.mHealthPerc = 0;
            this.var_826.PlayAnimation("Ready");
            this.var_826.Hide();
            this.var_744.PlayAnimation("Ready");
            this.var_744.Hide();
            this.var_799.PlayAnimation("Water",class_33.const_36);
            this.var_799.Show();
            if(this.var_1130)
            {
               _loc17_ = class_16.method_467(this.var_1130.var_392,!_loc2_.mOwnedPets.length);
               MathUtil.method_8(this.var_214.mMovieClip.am_Gold,MathUtil.method_29(class_16.method_586(this.var_211)),ScreenArmory.const_11,ScreenArmory.const_59);
               MathUtil.method_8(this.var_214.mMovieClip.am_Time,Game.method_70(_loc17_,true),ScreenArmory.const_11,ScreenArmory.const_59);
               MathUtil.method_2(this.var_516.mMovieClip.am_Text,"Hatch Egg");
               this.var_516.Show();
               MathUtil.method_2(this.var_499.mMovieClip.am_Name,"Hatch - " + this.var_1130.displayName);
               while(_loc3_.numChildren)
               {
                  _loc3_.removeChildAt(0);
               }
               method_12(_loc3_,"a_HatchEggIcon");
               this.var_190.mMovieClip.am_Time.visible = false;
               this.var_190.Show();
               this.var_499.Show();
               this.var_712.Show();
               this.var_261.Hide();
               this.var_613.Show();
               method_12(this.var_613.mMovieClip.am_IconHolder,this.var_1130.var_266);
               if(mPaperDoll)
               {
                  mPaperDoll.gfx.m_Sprite.visible = false;
               }
            }
            else if(this.var_191)
            {
               this.var_190.Show();
               this.var_516.Hide();
               _loc18_ = this.var_191.var_23 == class_7.const_35;
               if(_loc20_ = (_loc19_ = this.var_191.var_23 == class_7.const_35 ? this.var_191.var_23 : uint(this.var_191.var_23 + 1)) > _loc1_.rank * 2)
               {
                  this.var_519.Hide();
                  if(!this.var_520.mbVisible)
                  {
                     this.var_520.PlayAnimation("Warning");
                     this.var_520.Show();
                  }
                  MathUtil.method_8(this.var_214.mMovieClip.am_Gold,MathUtil.method_29(class_7.method_383(_loc19_)),ScreenArmory.const_11,ScreenArmory.const_59);
                  MathUtil.method_8(this.var_214.mMovieClip.am_Time,Game.method_70(_loc21_,true),ScreenArmory.const_11,ScreenArmory.const_59);
                  MathUtil.method_2(this.var_520.mMovieClip.am_Notice.am_Text,"Requires: Hatchery Level " + Math.ceil(_loc19_ / 2));
               }
               else
               {
                  _loc21_ = class_7.method_516(_loc19_);
                  if(_loc18_)
                  {
                     this.var_1746.Show();
                     this.var_190.Hide();
                     MathUtil.method_8(this.var_214.mMovieClip.am_Gold,"--",ScreenArmory.const_9,ScreenArmory.const_17);
                     MathUtil.method_8(this.var_214.mMovieClip.am_Time,"--",ScreenArmory.const_9,ScreenArmory.const_17);
                  }
                  else if(this.var_191.var_110 < class_7.const_164[this.var_191.var_23])
                  {
                     this.var_520.Hide();
                     if(!this.var_519.mbVisible)
                     {
                        this.var_519.PlayAnimation("Warning");
                        this.var_519.Show();
                     }
                     MathUtil.method_8(this.var_214.mMovieClip.am_Gold,MathUtil.method_29(class_7.method_383(_loc19_)),ScreenArmory.const_11,ScreenArmory.const_59);
                     MathUtil.method_8(this.var_214.mMovieClip.am_Time,Game.method_70(_loc21_,true),ScreenArmory.const_11,ScreenArmory.const_59);
                  }
                  else
                  {
                     this.var_516.Show();
                     MathUtil.method_8(this.var_214.mMovieClip.am_Gold,MathUtil.method_29(class_7.method_383(_loc19_)),ScreenArmory.const_11,ScreenArmory.const_59);
                     MathUtil.method_8(this.var_214.mMovieClip.am_Time,Game.method_70(_loc21_,true),ScreenArmory.const_11,ScreenArmory.const_59);
                  }
               }
               MathUtil.method_2(this.var_516.mMovieClip.am_Text,"Train Pet");
               if(_loc18_)
               {
                  MathUtil.method_2(this.var_499.mMovieClip.am_Name,this.var_191.mPetType.displayName);
               }
               else
               {
                  MathUtil.method_2(this.var_499.mMovieClip.am_Name,this.var_191.mPetType.displayName + " - Rank " + _loc19_);
               }
               while(_loc3_.numChildren)
               {
                  _loc3_.removeChildAt(0);
               }
               _loc3_.addChild(class_41.method_85(this.var_191.mPetType,2,2,const_203,const_203,_loc4_,_loc3_.parent.scaleX));
               this.var_190.mMovieClip.am_Time.visible = false;
               this.var_499.Show();
               this.var_712.Show();
               this.var_261.Hide();
               this.var_613.Hide();
               this.RefreshPaperDoll();
            }
            else
            {
               MathUtil.method_8(this.var_214.mMovieClip.am_Gold,"--",ScreenArmory.const_9,ScreenArmory.const_17);
               MathUtil.method_8(this.var_214.mMovieClip.am_Time,"--",ScreenArmory.const_9,ScreenArmory.const_17);
               MathUtil.method_2(this.var_516.mMovieClip.am_Text,"Hatch Egg");
               this.var_190.Hide();
               this.var_499.Hide();
               this.var_712.Hide();
               this.var_516.Hide();
               this.var_261.Show();
               this.var_613.Hide();
               if(mPaperDoll)
               {
                  mPaperDoll.gfx.m_Sprite.visible = false;
               }
            }
         }
         else
         {
            this.var_214.Hide();
            this.var_261.Hide();
            this.var_1134.Show();
            this.var_190.Show();
            this.var_499.Show();
            this.var_712.Show();
            while(_loc3_.numChildren)
            {
               _loc3_.removeChildAt(0);
            }
            _loc22_ = "";
            if(_loc5_)
            {
               _loc23_ = class_14.var_212[_loc2_.mIncubatingEggID];
               MathUtil.method_2(this.var_499.mMovieClip.am_Name,"Hatching - " + _loc23_.displayName);
               method_12(_loc3_,"a_HatchEggIcon");
               method_12(this.var_613.mMovieClip.am_IconHolder,_loc23_.var_266);
               this.var_190.mMovieClip.am_Time.visible = true;
               this.var_826.PlayAnimation("Ready");
               this.var_826.Hide();
               this.var_744.PlayAnimation("Water",class_33.const_36);
               this.var_744.Show();
               this.var_799.PlayAnimation("Ready");
               this.var_799.Hide();
               _loc22_ = "Cannot upgrade while hatching an egg";
               this.var_613.Show();
            }
            else
            {
               _loc24_ = _loc2_.mTrainingPet.mPetType;
               MathUtil.method_2(this.var_499.mMovieClip.am_Name,_loc24_.displayName + " - Rank " + (_loc2_.mTrainingPet.var_23 + 1));
               _loc3_.addChild(class_41.method_85(_loc24_,2,2,const_203,const_203,_loc4_));
               this.var_190.mMovieClip.am_Time.visible = true;
               this.var_826.PlayAnimation("Train",class_33.const_36);
               this.var_826.Show();
               this.var_744.PlayAnimation("Ready");
               this.var_744.Hide();
               this.var_799.PlayAnimation("Water",class_33.const_36);
               this.var_799.Show();
               _loc22_ = "Cannot upgrade while training a pet";
               this.RefreshPaperDoll();
               this.var_613.Hide();
            }
            this.var_1952.Hide();
            if(_loc1_.rank < class_9.const_214)
            {
               MathUtil.method_8(this.var_1882.mMovieClip.am_Message,_loc22_,ScreenArmory.const_137,ScreenArmory.const_169);
            }
            if(this.var_1045)
            {
               this.var_1552.Hide();
               this.var_1476.Show();
               this.var_449.Show();
               this.var_1628.Show();
               if(this.var_449.var_175 == 1)
               {
                  this.var_449.PlayAnimation("Warning");
               }
            }
            else
            {
               this.var_1552.Show();
               this.var_1476.Hide();
               this.var_1628.Hide();
               this.var_449.PlayAnimation("Ready");
               this.var_449.Hide();
            }
         }
         var _loc9_:Vector.<uint> = _loc2_.var_1233;
         var _loc10_:class_16 = class_14.var_212[_loc2_.mIncubatingEggID];
         var _loc11_:uint = 0;
         while(_loc11_ < const_448)
         {
            (_loc8_ = (_loc25_ = this.var_727[_loc11_]).mMovieClip).am_Selector.visible = this.var_211 == _loc11_;
            _loc7_ = _loc8_.am_IconHolder;
            while(_loc7_.numChildren)
            {
               _loc7_.removeChildAt(0);
            }
            if(!(_loc26_ = _loc2_.PickEgg(_loc11_)))
            {
               _loc25_.Hide();
            }
            else
            {
               _loc27_ = class_14.var_212[_loc26_];
               method_12(_loc7_,_loc27_.var_266);
               _loc25_.Show();
               if(_loc27_ == _loc10_)
               {
                  _loc7_.alpha = 0.5;
                  _loc7_.filters = [const_930];
               }
               else
               {
                  _loc7_.alpha = 1;
                  _loc7_.filters = [];
               }
            }
            _loc11_++;
         }
         if(this.var_1302)
         {
            this.method_992();
         }
         var _loc12_:Vector.<class_87>;
         var _loc13_:uint = (_loc12_ = this.var_759).length;
         var _loc14_:uint = var_16 * const_115;
         var_44 = Math.ceil(_loc13_ / const_115);
         _loc11_ = 0;
         while(_loc11_ < const_115)
         {
            (_loc16_ = this.var_867[_loc11_].mMovieClip).am_Selector.visible = this.var_1840 == var_16 * const_115 + _loc11_;
            _loc15_ = _loc16_.am_ItemIconHolder;
            while(_loc15_.numChildren)
            {
               _loc15_.removeChildAt(0);
            }
            _loc16_.am_IconActive.visible = false;
            _loc16_.am_IconPassive.visible = false;
            _loc16_.am_Star.visible = false;
            _loc16_.am_Level.visible = false;
            if(_loc14_ + _loc11_ < _loc13_)
            {
               _loc28_ = _loc12_[_loc14_ + _loc11_];
               _loc15_.addChild(class_41.method_85(_loc28_.mPetType,0,0,const_203,const_203,_loc4_));
               if(_loc28_ == _loc2_.mActivePet)
               {
                  _loc16_.am_IconActive.visible = true;
               }
               else if(_loc2_.mRestingPetList.indexOf(_loc28_) != -1)
               {
                  _loc16_.am_IconPassive.visible = true;
               }
               _loc29_ = _loc28_.var_23;
               MathUtil.method_2(_loc16_.am_Level,String(_loc29_));
               _loc30_ = _loc28_.var_110 >= class_7.const_164[_loc29_];
               if(_loc29_ == class_7.const_35)
               {
                  _loc15_.filters = [class_50.const_112];
                  _loc16_.am_Star.visible = true;
               }
               else if(!_loc30_ || _loc29_ >= this.var_2375 * 2 || _loc6_)
               {
                  _loc15_.filters = [class_50.const_112];
                  _loc16_.am_Level.visible = true;
               }
               else
               {
                  _loc15_.filters = [];
                  _loc16_.am_Level.visible = true;
               }
            }
            _loc11_++;
         }
      }
      
      override public function OnTickScreen() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc6_:class_16 = null;
         var _loc7_:int = 0;
         var _loc8_:Packet = null;
         var _loc9_:class_7 = null;
         var _loc10_:String = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         var _loc3_:Boolean = false;
         var _loc4_:class_81;
         if((_loc4_ = var_1.mEggPetInfo).mEggStatus == class_81.const_131)
         {
            _loc6_ = class_14.var_212[var_1.mEggPetInfo.mIncubatingEggID];
            _loc1_ = _loc4_.var_1179;
            _loc2_ = uint(24 * 10 * 3600);
            if(_loc6_)
            {
               _loc2_ = class_16.method_467(_loc6_.var_392,!_loc4_.mOwnedPets.length);
            }
            _loc3_ = true;
         }
         if(!_loc3_ && _loc4_.mPetTrainingStatus == class_81.const_107)
         {
            _loc1_ = _loc4_.var_943;
            _loc2_ = class_7.method_516(_loc4_.mTrainingPet.var_23 + 1);
            _loc3_ = true;
         }
         if(_loc3_)
         {
            if((_loc7_ = _loc1_ - var_1.mServerGameTime) < 0)
            {
               _loc7_ = 0;
            }
            MathUtil.method_8(this.var_190.mMovieClip.am_Time,Game.method_70(_loc7_),ScreenArmory.const_11,ScreenArmory.const_59);
            MathUtil.method_8(this.var_214.mMovieClip.am_Gold,"--",ScreenArmory.const_9,ScreenArmory.const_17);
            MathUtil.method_2(this.var_1134.mMovieClip.am_Idols,Game.method_229(_loc7_));
            this.var_190.mHealthPerc = 1 - _loc7_ / _loc2_;
         }
         var _loc5_:int;
         if((_loc5_ = var_1.mEggPetInfo.mEggResetEndTime - var_1.mServerGameTime) < 0)
         {
            _loc5_ = 0;
         }
         MathUtil.method_8(this.var_2377.mMovieClip.am_Time,Game.method_70(_loc5_),ScreenArmory.const_11,ScreenArmory.const_59);
         if(!var_1.mEggPetInfo.mbAskingForEggs && var_1.mServerGameTime > var_1.mEggPetInfo.mEggResetEndTime)
         {
            var_1.mEggPetInfo.mbAskingForEggs = true;
            _loc8_ = new Packet(LinkUpdater.const_849);
            var_1.serverConn.SendPacket(_loc8_);
         }
         if(_loc4_.mEggStatus == class_81.const_319 && Boolean(mWindow.mbCompleted))
         {
            var_1.serverConn.SendPacket(new Packet(LinkUpdater.const_978));
            Refresh();
         }
         if(_loc4_.mPetTrainingStatus == class_81.const_474 && Boolean(mWindow.mbCompleted))
         {
            _loc9_ = _loc4_.mTrainingPet.mPetType;
            _loc10_ = "Pet:" + _loc9_.var_310;
            var_1.screenNotification.ShowNotification(class_46.const_343,_loc9_.displayName + " Rank " + (_loc4_.mTrainingPet.var_23 + 1),_loc9_.var_255,true,null,_loc10_);
            _loc4_.method_1600();
            var_1.serverConn.SendPacket(new Packet(LinkUpdater.const_1081));
            this.var_1302 = true;
            Refresh();
         }
      }
      
      private function method_1370(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Vector.<class_87> = this.var_759;
         var _loc4_:class_81 = var_1.mEggPetInfo;
         var _loc5_:uint;
         if((_loc5_ = param2 + var_16 * const_115) >= _loc3_.length)
         {
            return;
         }
         var _loc6_:class_87 = _loc3_[_loc5_];
         var_1.screenHudTooltip.ShowPetTooltip(_loc6_,false,684.4,632.4);
      }
      
      private function method_1405(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:class_16 = class_14.var_212[var_1.mEggPetInfo.PickEgg(param2)];
         var_1.screenHudTooltip.ShowBasicDescriptionTooltip(_loc3_.displayName,"Egg",_loc3_.method_450(),_loc3_.description,686.4,662.4);
      }
      
      private function HideTooltip(param1:MouseEvent, param2:uint) : void
      {
         var_1.screenHudTooltip.HideTooltip();
      }
      
      private function method_1714(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:class_81 = var_1.mEggPetInfo;
         var _loc4_:uint;
         if((_loc4_ = param2 + var_16 * const_115) >= this.var_759.length)
         {
            return;
         }
         if(param1.ctrlKey && !var_1.screenInteractiveTutorial.mCurrentTutorialIdx)
         {
            var_1.screenArmory.LinkPetInChat(0,this.var_759[_loc4_]);
            return;
         }
         if(_loc4_ == this.var_1840)
         {
            return;
         }
         if(_loc3_.mEggStatus == class_81.const_131 || _loc3_.mPetTrainingStatus == class_81.const_107)
         {
            this.var_519.Hide();
            this.var_520.Hide();
            return;
         }
         this.ResetSelectors();
         this.var_1049 = param2;
         this.var_1840 = _loc4_;
         this.var_867[this.var_1049].mMovieClip.am_Selector.visible = false;
         this.var_191 = this.var_759[_loc4_];
         if(this.var_1049 != -1)
         {
            this.var_867[this.var_1049].mMovieClip.am_Selector.visible = false;
         }
         var _loc5_:class_33;
         (_loc5_ = this.var_1231[int(Math.random() * const_276)]).PlayAnimation("Sparkle",class_33.const_14);
         _loc5_.Show();
         this.RefreshPaperDoll();
         Refresh();
      }
      
      private function method_1519(param1:MouseEvent, param2:uint) : void
      {
         if(param1.ctrlKey && !var_1.screenInteractiveTutorial.mCurrentTutorialIdx)
         {
            this.method_1609(param2);
            return;
         }
         if(param2 == this.var_211)
         {
            return;
         }
         var _loc3_:class_81 = var_1.mEggPetInfo;
         if(_loc3_.mPetTrainingStatus == class_81.const_107 || _loc3_.mEggStatus == class_81.const_131)
         {
            this.var_519.Hide();
            return;
         }
         this.ResetSelectors();
         this.var_211 = param2;
         this.var_727[this.var_211].mMovieClip.am_Selector.visible = false;
         this.var_1130 = class_14.var_212[_loc3_.PickEgg(this.var_211)];
         if(this.var_211 != -1)
         {
            this.var_727[this.var_211].mMovieClip.am_Selector.visible = false;
         }
         var _loc4_:class_33;
         (_loc4_ = this.var_1231[int(Math.random() * const_276)]).PlayAnimation("Sparkle",class_33.const_14);
         _loc4_.Show();
         Refresh();
      }
      
      private function UpgradeBuilding(param1:MouseEvent) : void
      {
         var _loc6_:class_9 = null;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:class_105 = var_1.mBuildingInfo;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_9;
         if(!(_loc4_ = _loc3_.GetOwnedBuildingByName("Barn")))
         {
            return;
         }
         var _loc5_:class_9;
         if(!(_loc5_ = class_9.method_132(_loc4_)))
         {
            return;
         }
         if(_loc2_.currGold < _loc5_.var_129)
         {
            var_1.screenGoldShort.Display(_loc5_.var_129,_loc5_.var_365,class_93.const_178,_loc4_);
         }
         else if(_loc6_ = _loc3_.UpgradeBuilding(_loc4_))
         {
            Hide();
            var_1.screenUpgrading.Display(_loc6_);
         }
      }
      
      private function method_650(param1:MouseEvent) : void
      {
         this.var_1045 = !this.var_1045;
         Refresh();
      }
      
      private function method_1410(param1:MouseEvent) : void
      {
         var _loc3_:Packet = null;
         var _loc4_:int = 0;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         var _loc2_:class_81 = var_1.mEggPetInfo;
         if(_loc2_.mEggStatus == class_81.const_131)
         {
            _loc4_ = _loc2_.var_1179 - var_1.mServerGameTime;
            _loc3_ = new Packet(LinkUpdater.const_1190);
         }
         else
         {
            _loc4_ = _loc2_.var_943 - var_1.mServerGameTime;
            _loc3_ = new Packet(LinkUpdater.const_1262);
         }
         if(_loc4_ < 1)
         {
            return;
         }
         var _loc5_:uint = Game.method_257(_loc4_);
         if(var_1.mMammothIdols < _loc5_)
         {
            var_1.screenBuyIdols.Display(_loc5_ - var_1.mMammothIdols);
            return;
         }
         this.var_190.mHealthPerc = 0;
         this.var_1324.DisableButton("Inactive");
         _loc3_.method_9(_loc5_);
         var_1.serverConn.SendPacket(_loc3_);
         this.ResetSelectors();
      }
      
      public function TrainOrHatchClicked(param1:MouseEvent, param2:Boolean = false) : void
      {
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:class_87 = null;
         var _loc8_:uint = 0;
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc11_:uint = 0;
         var _loc12_:uint = 0;
         var _loc13_:class_16 = null;
         var _loc14_:uint = 0;
         var _loc15_:uint = 0;
         var _loc16_:uint = 0;
         var _loc17_:Packet = null;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_ || !var_1.CanSendPacket())
         {
            return;
         }
         if(this.var_191)
         {
            _loc5_ = this.var_191.mPetType.var_104;
            _loc6_ = this.var_191.var_670;
            _loc7_ = var_1.mEggPetInfo.GetPetDataByIDIteration(_loc5_,_loc6_);
            _loc8_ = class_7.method_383(_loc7_.var_23 + 1);
            _loc9_ = class_7.method_1876(_loc7_.var_23 + 1);
            if(_loc7_)
            {
               if(!param2 && _loc3_.currGold < _loc8_)
               {
                  var_1.screenGoldShort.Display(_loc8_,_loc9_,class_93.const_507,_loc7_);
               }
               else
               {
                  _loc3_.GainMoney(-_loc8_,false);
                  var_1.mEggPetInfo.TrainPet(_loc7_);
               }
            }
         }
         else if(this.var_211 != -1)
         {
            _loc10_ = class_16.method_586(this.var_211);
            _loc11_ = class_16.method_1241(this.var_211);
            if(!param2 && _loc3_.currGold < _loc10_)
            {
               var_1.screenGoldShort.Display(_loc10_,_loc11_,class_93.const_563,this.var_211);
            }
            else
            {
               if(!param2)
               {
                  _loc3_.GainMoney(-_loc10_,false);
               }
               _loc12_ = uint(var_1.mEggPetInfo.PickEgg(this.var_211));
               _loc14_ = (_loc13_ = class_14.var_212[_loc12_]).var_392;
               _loc15_ = class_16.method_467(_loc14_,!var_1.mEggPetInfo.mOwnedPets.length);
               _loc16_ = var_1.mServerGameTime + _loc15_;
               var_1.mEggPetInfo.SetEggData(_loc12_,_loc16_);
               (_loc17_ = new Packet(LinkUpdater.const_947)).method_20(class_16.const_1251,this.var_211);
               _loc17_.method_15(param2);
               var_1.serverConn.SendPacket(_loc17_);
            }
         }
         this.var_1324.EnableButton();
         Refresh();
      }
      
      private function method_1083(param1:MouseEvent) : void
      {
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(var_1.mEggPetInfo.mEggStatus == class_81.const_131)
         {
            var_1.mEggPetInfo.HatchEggCancel();
            var_1.serverConn.SendPacket(new Packet(LinkUpdater.const_877));
            this.var_190.mHealthPerc = 0;
         }
         if(var_1.mEggPetInfo.mPetTrainingStatus == class_81.const_107)
         {
            var_1.mEggPetInfo.PetTrainCancel();
            var_1.serverConn.SendPacket(new Packet(LinkUpdater.const_1036));
            this.var_190.mHealthPerc = 0;
         }
         this.var_1045 = false;
         Refresh();
      }
      
      private function method_992() : void
      {
         this.var_759 = var_1.mEggPetInfo.mOwnedPets.slice();
         this.var_759.sort(this.method_1623);
         this.var_1302 = false;
      }
      
      private function method_1623(param1:class_87, param2:class_87) : Number
      {
         return this.method_605(param2) - this.method_605(param1);
      }
      
      private function method_605(param1:class_87) : Number
      {
         var _loc2_:Number = 0;
         var _loc3_:Number = param1.method_324();
         if(var_1.mEggPetInfo.mTrainingPet == param1)
         {
            _loc2_ += 1000000;
         }
         if(_loc3_ == 1 && param1.var_23 < this.var_2375 * 2)
         {
            _loc2_ += 99999;
         }
         if(var_1.mEggPetInfo.mActivePet == param1)
         {
            _loc2_ += 50000;
         }
         if(var_1.mEggPetInfo.mRestingPetList.indexOf(param1) >= 0)
         {
            _loc2_ += 10000;
         }
         _loc2_ += 100 * _loc3_;
         return _loc2_ + param1.var_23;
      }
      
      private function method_1858() : void
      {
         this.var_788 = new EntType();
         this.var_788.entName = "UI_ScreenBarn_PetPaperDoll";
      }
      
      override public function RefreshPaperDoll() : void
      {
         var _loc1_:String = null;
         var _loc3_:EntType = null;
         var _loc2_:class_81 = var_1.mEggPetInfo;
         if(_loc2_.mPetTrainingStatus != class_81.const_107 && !this.var_191)
         {
            return;
         }
         if(_loc2_.mPetTrainingStatus == class_81.const_107)
         {
            _loc1_ = "Pet" + _loc2_.mTrainingPet.mPetType.var_310;
         }
         else
         {
            _loc1_ = "Pet" + this.var_191.mPetType.var_310;
         }
         if(!mPaperDoll)
         {
            mPaperDoll = new Entity(var_1,_loc1_,null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,1,0,null,null,null,null,null,null);
         }
         else
         {
            if(!this.var_788)
            {
               this.method_1858();
            }
            _loc3_ = EntType.method_48(_loc1_);
            if(this.var_1228)
            {
               this.var_1228 = null;
            }
            this.var_1228 = _loc3_.gfxType.GetDuplicate();
            this.var_1228.animScale = 1.25;
            this.var_788.var_1606 = _loc3_.var_1606;
            this.var_788.gfxType = this.var_1228;
            this.var_788.parentEntType = _loc3_.parentEntType;
            mPaperDoll.ResetEntType(this.var_788);
         }
         var_2.am_Incubator.am_IncubatorTop.am_PaperDoll.addChild(mPaperDoll.gfx.m_TheDO);
         mPaperDoll.gfx.m_Sprite.visible = true;
      }
      
      public function method_1609(param1:uint) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:class_16 = class_14.var_212[var_1.mEggPetInfo.PickEgg(param1)];
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:* = (_loc4_ = (_loc4_ = "{" + class_127.const_8[7]) + (":" + _loc3_.var_206.toString())) + "}";
         var_1.screenChat.AddItemInfoToChatEntry("[" + _loc3_.displayName + "]",_loc4_);
      }
   }
}
