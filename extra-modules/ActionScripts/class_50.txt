package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.filters.ColorMatrixFilter;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   
   public class class_50 extends class_32
   {
      
      public static const const_112:ColorMatrixFilter = new ColorMatrixFilter([0.212671,0.71516,0.072169,0,0,0.212671,0.71516,0.072169,0,0,0.212671,0.71516,0.072169,0,0,0,0,0,1,0]);
      
      private static const const_285:uint = 5;
      
      private static const const_65:uint = 12;
      
      private static const const_1345:uint = 10;
      
      private static const const_446:uint = 9;
      
      private static const const_159:uint = 10;
      
      public static const const_614:Vector.<String> = Vector.<String>(["Mage","Frostwarden","Flameseer","Necromancer","Master"]);
      
      public static const const_656:Vector.<String> = Vector.<String>(["Rogue","Executioner","ShadowWalker","Soulthief","Master"]);
      
      public static const const_609:Vector.<String> = Vector.<String>(["Paladin","Sentinel","Justicar","Templar","Master"]);
      
      public static const const_776:Vector.<String> = Vector.<String>(["Wizardry Guild","Winter Order","Infernal Circle","Accursed Coven","Discipline Masteries"]);
      
      public static const const_657:Vector.<String> = Vector.<String>(["Tricks o’ Trade","Ambush & Onslaught","From the Shadows","The Dark Arts","Discipline Masteries"]);
      
      public static const const_701:Vector.<String> = Vector.<String>(["Martial Techniques","Chivalric Prowess","Sacred Castigations","Theurgical Devotions","Discipline Masteries"]);
      
      public static const const_643:Vector.<String> = Vector.<String>(["a_PowerIcon_Mage","a_PowerIcon_FrostArmor","a_PowerIcon_DragonWraith","a_PowerIcon_LichShot2","a_PowerIcon_BlindingLight"]);
      
      public static const const_669:Vector.<String> = Vector.<String>(["a_PowerIcon_Rogue","a_PowerIcon_SeverStrike","a_PowerIcon_BlackMiasma","a_PowerIcon_AgonizingBond","a_PowerIcon_BlindingLight"]);
      
      public static const const_713:Vector.<String> = Vector.<String>(["a_PowerIcon_Paladin","a_PowerIcon_HeroStrength","a_PowerIcon_LightningShieldBurst","a_PowerIcon_EmpyreanRadiance","a_PowerIcon_BlindingLight"]);
      
      public static const ROW_1_ENDIDX:int = 3;
      
      public static const ROW_2_ENDIDX:int = 7;
       
      
      public var var_60:class_33;
      
      private var var_605:Vector.<class_33>;
      
      private var var_1955:Vector.<class_33>;
      
      private var var_395:Vector.<class_33>;
      
      private var var_1692:Vector.<class_33>;
      
      private var var_1162:Vector.<class_33>;
      
      private var var_1779:class_33;
      
      private var var_2013:class_33;
      
      private var var_1546:class_33;
      
      private var var_765:Vector.<class_33>;
      
      private var var_429:int;
      
      private var var_254:class_10;
      
      private var var_246:Vector.<class_33>;
      
      private var var_1116:Vector.<class_33>;
      
      private var var_1508:class_33;
      
      private var var_528:uint;
      
      private var var_1404:Vector.<String>;
      
      private var var_672:Vector.<String>;
      
      private var var_1015:Vector.<String>;
      
      private var var_841:Vector.<class_10>;
      
      private var var_877:Vector.<class_10>;
      
      private var var_516:class_33;
      
      private var var_214:class_33;
      
      private var var_179:class_33;
      
      private var var_723:class_33;
      
      private var var_871:class_33;
      
      private var var_1222:class_33;
      
      private var var_2637:class_33;
      
      private var var_2687:class_33;
      
      private var var_1804:class_33;
      
      private var var_417:class_33;
      
      private var var_449:class_33;
      
      private var var_268:class_33;
      
      private var var_1561:class_33;
      
      private var var_2721:PowerType;
      
      private var var_1167:Boolean = false;
      
      private var var_1713:class_33;
      
      private var var_1870:class_33;
      
      private var var_1398:Boolean;
      
      public function class_50(param1:Game)
      {
         super(param1,"a_ScreenTome","am_Panel");
      }
      
      public static function method_454(param1:String) : Boolean
      {
         return false;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc6_:MovieClip = null;
         var _loc7_:MovieClip = null;
         var _loc8_:MovieClip = null;
         var _loc1_:MovieClip = var_2.am_SlotGroup;
         this.var_395 = new Vector.<class_33>(const_65,true);
         this.var_1692 = new Vector.<class_33>(const_65,true);
         this.var_1162 = new Vector.<class_33>(const_65,true);
         var _loc2_:uint = 0;
         while(_loc2_ < const_65)
         {
            (_loc6_ = _loc1_["am_Slot" + _loc2_] as MovieClip).am_Highlighter.visible = false;
            this.var_395[_loc2_] = method_3(_loc6_,_loc2_,this.method_1641,this.method_1713,this.method_1114);
            this.var_1692[_loc2_] = method_1(_loc6_.am_GlareAnim);
            this.var_1162[_loc2_] = method_1(_loc6_.am_Star);
            _loc2_++;
         }
         this.var_1779 = method_1(_loc1_);
         this.var_1546 = method_1(var_2.am_HeaderGroup);
         this.var_246 = new Vector.<class_33>(const_159,true);
         this.var_765 = new Vector.<class_33>(const_159,true);
         var _loc3_:MovieClip = var_2.am_UpgradePath.am_UpgradeGroup;
         _loc2_ = 0;
         while(_loc2_ < const_159)
         {
            (_loc7_ = _loc3_["am_Upgrade" + _loc2_] as MovieClip).am_Selector.visible = false;
            this.var_246[_loc2_] = method_3(_loc7_,_loc2_,this.method_1847,this.method_1118,this.method_1458);
            this.var_765[_loc2_] = method_1(_loc7_.am_RankAnimation);
            _loc2_++;
         }
         this.var_2013 = method_1(var_2.am_UpgradePath);
         this.var_1116 = new Vector.<class_33>(const_446,true);
         var _loc4_:MovieClip = var_2.am_UpgradePath.am_PathGroup;
         _loc2_ = 0;
         while(_loc2_ < const_446)
         {
            this.var_1116[_loc2_] = method_1(_loc4_["am_Path" + _loc2_] as MovieClip);
            _loc2_++;
         }
         this.var_1508 = method_1(_loc4_.am_Triangle);
         var _loc5_:MovieClip = var_2.am_TabGroup;
         this.var_605 = new Vector.<class_33>(const_285,true);
         this.var_1955 = new Vector.<class_33>(const_285,true);
         _loc2_ = 0;
         while(_loc2_ < const_285)
         {
            _loc8_ = _loc5_["am_Tab" + _loc2_] as MovieClip;
            this.var_605[_loc2_] = method_3(_loc8_,_loc2_,this.method_1376,this.method_1530,this.method_1526);
            this.var_1955[_loc2_] = method_1(_loc8_.am_GlareAnim);
            _loc2_++;
         }
         this.var_528 = 0;
         this.var_516 = method_10(var_2.am_TrainCostPanel.am_Train,this.Train);
         this.var_214 = method_1(var_2.am_TrainCostPanel);
         this.var_179 = method_1(var_2.am_TrainingProgressPanel);
         this.var_723 = method_1(var_2.am_CancelPanel);
         this.var_871 = method_1(var_2.am_SpeedUpPanel);
         this.var_1222 = method_5(var_2.am_Cancel,this.method_1786);
         this.var_2637 = method_10(this.var_723.mMovieClip.am_CancelTraining,this.method_1501);
         this.var_2687 = method_10(this.var_723.mMovieClip.am_NeverMind,this.method_1293);
         this.var_1804 = method_10(this.var_871.mMovieClip.am_SpeedUp,this.method_1124);
         this.var_417 = method_17(this.var_179.mMovieClip.am_Progress,"Progress",2);
         this.var_449 = method_1(var_2.am_WarningAnim);
         this.var_268 = method_1(var_2.am_WarningLevelTooLow);
         this.var_1713 = method_10(mWindow.mMovieClip.am_GlobalUpgradePanel.am_Upgrade,this.method_1372);
         this.var_1870 = method_1(mWindow.mMovieClip.am_GlobalUpgradePanel);
         this.var_1561 = method_1(var_2.am_Notice);
         method_23(var_2.am_Exit);
         this.var_60 = method_1(var_2.am_TutorialInteraction);
         this.var_60.Hide();
         var_2.cacheAsBitmap = true;
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_605 = null;
         this.var_395 = null;
         this.var_1692 = null;
         this.var_1162 = null;
         this.var_1404 = null;
         this.var_672 = null;
         this.var_1015 = null;
         this.var_841 = null;
         this.var_877 = null;
         this.var_1955 = null;
         this.var_246 = null;
         this.var_1116 = null;
         this.var_516 = null;
         this.var_1779 = null;
         this.var_2013 = null;
         this.var_1546 = null;
         this.var_214 = null;
         this.var_179 = null;
         this.var_723 = null;
         this.var_871 = null;
         this.var_1222 = null;
         this.var_2637 = null;
         this.var_2687 = null;
         this.var_1713 = null;
         this.var_1870 = null;
         this.var_417 = null;
         this.var_449 = null;
         this.var_268 = null;
         this.var_1561 = null;
         this.var_254 = null;
         this.var_765 = null;
         this.var_1508 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc7_:class_10 = null;
         var _loc8_:PowerType = null;
         var _loc9_:class_33 = null;
         var _loc10_:MovieClip = null;
         var _loc11_:String = null;
         var _loc12_:Boolean = false;
         var _loc13_:Boolean = false;
         var _loc14_:uint = 0;
         var _loc15_:class_33 = null;
         var _loc16_:class_33 = null;
         var _loc17_:uint = 0;
         var _loc18_:uint = 0;
         var _loc19_:class_10 = null;
         var _loc20_:* = false;
         var _loc21_:PowerType = null;
         var _loc22_:uint = 0;
         var _loc23_:uint = 0;
         var _loc24_:class_10 = null;
         var _loc25_:uint = 0;
         var _loc26_:PowerType = null;
         var _loc27_:uint = 0;
         var _loc28_:uint = 0;
         var _loc29_:class_9 = null;
         var _loc30_:uint = 0;
         var _loc31_:Boolean = false;
         var _loc32_:TextField = null;
         var _loc33_:String = null;
         var _loc34_:uint = 0;
         var _loc35_:class_33 = null;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         this.method_404();
         var _loc2_:String = this.var_672[this.var_528];
         var _loc3_:Boolean = class_50.method_454(_loc2_);
         if(_loc3_)
         {
            this.var_2013.Hide();
            this.var_1779.Hide();
            this.var_1546.Hide();
            this.var_214.Hide();
            this.var_723.Hide();
            this.var_179.Hide();
            this.var_871.Hide();
            this.var_1222.Hide();
            var_44 = 0;
            MathUtil.method_2(var_2.am_TierName0,"");
            MathUtil.method_2(var_2.am_TierName1,"");
            MathUtil.method_2(var_2.am_TierName2,"");
            return;
         }
         this.var_2013.Show();
         this.var_1779.Show();
         this.var_1546.Show();
         this.var_179.Show();
         this.var_214.Show();
         this.method_1176();
         this.method_1485();
         if(this.var_1398)
         {
            MathUtil.method_2(var_2.am_TierName0,Game.method_226(this.var_672[1].toLowerCase()));
            MathUtil.method_2(var_2.am_TierName1,Game.method_226(this.var_672[2].toLowerCase()));
            MathUtil.method_2(var_2.am_TierName2,Game.method_226(this.var_672[3].toLowerCase()));
         }
         else
         {
            MathUtil.method_2(var_2.am_TierName0,"Tier 1");
            MathUtil.method_2(var_2.am_TierName1,"Tier 2");
            MathUtil.method_2(var_2.am_TierName2,"Tier 3");
         }
         var_44 = Math.ceil(this.var_841.length / const_65);
         var _loc4_:uint = var_16 * const_65;
         this.method_332(this.var_429);
         this.var_877 = new Vector.<class_10>(const_65);
         this.var_1561.Show();
         this.var_179.Hide();
         var _loc5_:uint = _loc4_;
         var _loc6_:uint = 0;
         while(_loc6_ < const_65)
         {
            if(_loc5_ < this.var_841.length)
            {
               _loc7_ = this.var_841[_loc5_];
               _loc8_ = class_14.powerTypesDict[_loc7_.abilityName];
               if(!this.var_1398 && (_loc7_.var_90 > 1 && _loc6_ <= ROW_1_ENDIDX || _loc7_.var_90 > 2 && _loc6_ <= ROW_2_ENDIDX))
               {
                  _loc5_--;
               }
               else if(this.var_1398 && (_loc6_ == ROW_1_ENDIDX || _loc6_ == ROW_2_ENDIDX))
               {
                  _loc5_--;
               }
               else
               {
                  (_loc9_ = this.var_395[_loc6_]).Show();
                  _loc10_ = _loc9_.mMovieClip;
                  method_12(_loc10_.am_IconHolder,_loc8_.iconName);
                  this.var_877[_loc6_] = _loc7_;
                  if(!(_loc11_ = _loc7_.type))
                  {
                     _loc10_.am_MasterFrame.visible = false;
                  }
                  else if(_loc7_.var_223)
                  {
                     _loc10_.am_MasterFrame.visible = true;
                  }
                  else
                  {
                     _loc10_.am_MasterFrame.visible = false;
                  }
                  _loc13_ = (_loc12_ = Boolean(var_1.mAbilityBook.IsTrained(_loc7_))) || !_loc7_.var_223;
                  if(_loc12_)
                  {
                     if(!(_loc14_ = uint(var_1.mAbilityBook.mAbilityListTrainedRanks[_loc7_.abilityID])))
                     {
                        _loc14_ = 1;
                     }
                     _loc9_.PlayAnimation("Active");
                     MathUtil.method_8(_loc10_.am_Name,_loc8_.displayName,ScreenArmory.const_11,ScreenArmory.const_47);
                     MathUtil.method_8(_loc10_.am_Rank,_loc14_.toString(),ScreenArmory.const_24,ScreenArmory.const_915);
                     this.var_1162[_loc6_].Show();
                  }
                  else if(_loc13_)
                  {
                     _loc9_.PlayAnimation("Active");
                     MathUtil.method_8(_loc10_.am_Name,_loc8_.displayName,ScreenArmory.const_11,ScreenArmory.const_47);
                     MathUtil.method_2(_loc10_.am_Rank,"");
                     this.var_1162[_loc6_].Hide();
                  }
                  else
                  {
                     _loc9_.PlayAnimation("Inactive");
                     MathUtil.method_8(_loc10_.am_Name,_loc8_.displayName,ScreenArmory.const_9,ScreenArmory.const_17);
                     MathUtil.method_2(_loc10_.am_Rank,"");
                     this.var_1162[_loc6_].Hide();
                  }
               }
            }
            _loc6_++;
            _loc5_++;
         }
         if(!this.var_254)
         {
            for each(_loc15_ in this.var_1116)
            {
               _loc15_.Hide();
            }
            this.var_1508.Hide();
            this.var_246[const_159 - 1].Hide();
            this.var_246[0].Hide();
            for each(_loc16_ in this.var_246)
            {
               _loc16_.Hide();
            }
            this.var_516.Hide();
            this.var_179.mMovieClip.am_MaxRank.visible = false;
            MathUtil.method_8(this.var_214.mMovieClip.am_Gold,"--",ScreenArmory.const_9,ScreenArmory.const_17);
            MathUtil.method_8(this.var_214.mMovieClip.am_Time,"--",ScreenArmory.const_9,ScreenArmory.const_17);
            MathUtil.method_2(var_2.am_UpgradePath.am_Name,"");
         }
         else
         {
            if((_loc18_ = uint((_loc17_ = uint(var_1.mAbilityBook.GetCurrRankByAbilityID(this.var_254.abilityID))) + 1)) > class_10.const_105)
            {
               _loc18_ = class_10.const_105;
            }
            _loc19_ = class_10.method_352(this.var_254.abilityName,_loc18_);
            _loc20_ = _loc17_ == class_10.const_105;
            method_14(this.var_179.mMovieClip.am_IconHolder);
            _loc21_ = _loc1_.method_775(this.var_254.abilityName);
            if(var_1.mAbilityBook.mStatus == class_45.const_191)
            {
               _loc24_ = var_1.mAbilityBook.mAbilityResearch;
               _loc25_ = var_1.mAbilityBook.GetCurrRankByAbilityID(_loc24_.abilityID) + 1;
               _loc26_ = _loc1_.method_775(_loc24_.abilityName);
               this.var_179.mMovieClip.am_MaxRank.visible = false;
               method_12(this.var_179.mMovieClip.am_IconHolder,_loc26_.iconName);
               MathUtil.method_2(this.var_179.mMovieClip.am_Name,_loc26_.displayName + " - Rank " + _loc25_);
            }
            else
            {
               if(!_loc20_)
               {
                  MathUtil.method_2(this.var_179.mMovieClip.am_Name,_loc21_.displayName + " - Rank " + _loc18_);
                  this.var_417.Show();
                  this.var_179.mMovieClip.am_MaxRank.visible = false;
               }
               else
               {
                  MathUtil.method_2(this.var_179.mMovieClip.am_Name,_loc21_.displayName);
                  this.var_417.Hide();
                  this.var_179.mMovieClip.am_MaxRank.visible = true;
               }
               method_12(this.var_179.mMovieClip.am_IconHolder,_loc21_.iconName);
               this.var_417.mMovieClip.am_Time.visible = false;
            }
            MathUtil.method_2(var_2.am_UpgradePath.am_Name,_loc21_.displayName + " Rank: " + _loc17_ + "/" + class_10.const_105);
            this.var_1561.Hide();
            this.var_179.Show();
            if(Boolean(_loc19_) && var_1.mAbilityBook.mStatus == class_45.const_29)
            {
               _loc27_ = _loc19_.var_129;
               _loc28_ = _loc19_.upgradeTime;
               MathUtil.method_8(this.var_214.mMovieClip.am_Time,Game.method_70(_loc28_,true),ScreenArmory.const_11,ScreenArmory.const_47);
               MathUtil.method_8(this.var_214.mMovieClip.am_Gold,MathUtil.method_29(_loc27_),ScreenArmory.const_11,ScreenArmory.const_47);
               _loc29_ = var_1.mBuildingInfo.GetOwnedBuildingByName("Tome");
               _loc30_ = 0;
               if(_loc29_)
               {
                  _loc30_ = _loc29_.rank;
               }
               if((_loc31_ = _loc18_ <= _loc30_ && !_loc20_) && (!_loc19_.var_223 || _loc17_ > 0))
               {
                  this.var_516.Show();
                  this.var_516.EnableButton();
                  this.var_214.Show();
                  this.var_268.Hide();
                  this.var_268.PlayAnimation("Ready");
               }
               else
               {
                  this.var_516.Hide();
                  if(var_1.mAbilityBook.mStatus == class_45.const_29)
                  {
                     _loc32_ = this.var_268.mMovieClip.am_Notice.am_Text;
                     _loc33_ = "";
                     if(!this.var_254.var_223)
                     {
                        _loc33_ = "Requires: Tome Level " + _loc18_;
                     }
                     else if(!var_1.mAbilityBook.GetCurrRankByAbilityID(this.var_254.abilityID))
                     {
                        _loc33_ = "Learn this in your Talent Tree";
                     }
                     else if(!_loc31_)
                     {
                        _loc33_ = "Requires: Tome Level " + _loc18_;
                     }
                     MathUtil.method_2(_loc32_,_loc33_);
                     if(_loc33_ == "")
                     {
                        this.var_268.Hide();
                     }
                     else if(!this.var_268.mbVisible)
                     {
                        this.var_268.Show();
                        this.var_268.PlayAnimation("Warning");
                     }
                  }
                  else
                  {
                     this.var_268.Hide();
                     this.var_268.PlayAnimation("Ready");
                  }
               }
               if(_loc20_)
               {
                  MathUtil.method_8(this.var_214.mMovieClip.am_Gold,"--",ScreenArmory.const_9,ScreenArmory.const_17);
                  MathUtil.method_8(this.var_214.mMovieClip.am_Time,"--",ScreenArmory.const_9,ScreenArmory.const_17);
                  this.var_516.Hide();
                  this.var_268.Hide();
                  this.var_268.PlayAnimation("Ready");
               }
            }
            _loc22_ = const_159 - 1;
            this.var_246[_loc22_].Hide();
            method_14(this.var_246[0].mMovieClip.am_ButtonHolder.am_Button);
            _loc23_ = 0;
            while(_loc23_ < const_159 - 1)
            {
               this.var_246[_loc23_].Show();
               _loc23_++;
            }
            _loc23_ = 1;
            while(_loc23_ <= const_159)
            {
               _loc34_ = _loc23_ - 1;
               _loc35_ = this.var_246[_loc34_];
               if(_loc23_ > _loc17_)
               {
                  _loc35_.PlayAnimation("Disabled");
                  if(_loc23_ == 1)
                  {
                     method_12(_loc35_.mMovieClip.am_ButtonHolder.am_Button,_loc21_.iconName);
                     _loc35_.mMovieClip.am_ButtonHolder.filters = [const_112];
                     _loc35_.Show();
                  }
               }
               else if(_loc23_ == 1)
               {
                  method_12(_loc35_.mMovieClip.am_ButtonHolder.am_Button,_loc21_.iconName);
                  _loc35_.mMovieClip.am_ButtonHolder.filters = [];
                  _loc35_.Show();
               }
               else
               {
                  _loc35_.PlayAnimation("Active");
                  if(_loc23_ >= _loc22_)
                  {
                     this.var_246[_loc22_].Show();
                  }
                  else
                  {
                     this.var_246[_loc22_].Hide();
                  }
               }
               _loc23_++;
            }
            _loc23_ = 0;
            while(_loc23_ < const_446)
            {
               if(_loc23_ < _loc17_ - 1)
               {
                  this.var_1116[_loc23_].Show();
               }
               else
               {
                  this.var_1116[_loc23_].Hide();
               }
               _loc23_++;
            }
            if(_loc17_ == class_10.const_105)
            {
               this.var_1508.Show();
            }
            else
            {
               this.var_1508.Hide();
            }
         }
         _loc29_ = var_1.mBuildingInfo.GetOwnedBuildingByName("Tome");
         var_1.UpdateBuildingUpgradePanel(this.var_1870.mMovieClip,_loc29_,this.var_1713);
         if(var_1.mAbilityBook.mStatus == class_45.const_191)
         {
            this.var_1713.Hide();
            if(_loc29_.rank < class_9.const_214)
            {
               MathUtil.method_8(this.var_1870.mMovieClip.am_Message,"Cannot upgrade while training an Ability",ScreenArmory.const_137,ScreenArmory.const_169);
            }
         }
         if(var_1.mAbilityBook.mStatus == class_45.const_191)
         {
            this.var_1561.Hide();
            this.var_214.Hide();
            this.var_179.Show();
            this.var_871.Show();
            this.var_417.mMovieClip.am_Time.visible = true;
            if(this.var_1167)
            {
               this.var_723.Show();
               this.var_1222.Hide();
               this.var_449.Show();
               if(this.var_449.var_175 == 1)
               {
                  this.var_449.PlayAnimation("Warning");
               }
            }
            else
            {
               this.var_723.Hide();
               this.var_1222.Show();
               this.var_449.PlayAnimation("Ready");
               this.var_449.Hide();
            }
            this.var_1804.EnableButton();
         }
         else
         {
            this.var_723.Hide();
            this.var_871.Hide();
            this.var_1222.Hide();
            this.var_449.PlayAnimation("Ready");
            this.var_449.Hide();
         }
         if(var_1.mAbilityBook.mStatus != class_45.const_29)
         {
            this.var_516.DisableButton("Inactive");
         }
      }
      
      public function OnInitDisplay(param1:String) : void
      {
         var _loc3_:Vector.<class_33> = null;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         if(param1 == "Paladin")
         {
            this.var_1404 = const_713;
            this.var_672 = const_609;
            this.var_1015 = const_701;
         }
         else if(param1 == "Rogue")
         {
            this.var_1404 = const_669;
            this.var_672 = const_656;
            this.var_1015 = const_657;
         }
         else if(param1 == "Mage")
         {
            this.var_1404 = const_643;
            this.var_672 = const_614;
            this.var_1015 = const_776;
         }
         this.var_254 = !!var_1.mAbilityBook.mAbilityResearch ? var_1.mAbilityBook.mAbilityResearch : null;
         this.var_429 = -1;
         this.method_332(this.var_429);
         var_1.mAbilityBook.setCurrent();
         this.var_1167 = false;
         this.var_268.Hide();
         this.var_268.PlayAnimation("Ready");
         var_1.screenHudTooltip.HideTooltip(true);
         if(!var_1.screenInteractiveTutorial.CheckCompletedTutorials(class_89.const_331))
         {
            this.var_60.Show();
            _loc3_ = new Vector.<class_33>();
            _loc3_.push(this.var_395[8]);
            _loc3_.push(this.var_516);
            _loc3_.push(this.var_1804);
            _loc3_.push(var_1.screenHudTop.mSpellbookIcon);
            var_1.screenInteractiveTutorial.SetTutorial(class_89.const_331,this,this.var_60,_loc3_);
         }
      }
      
      private function method_1176() : void
      {
         var _loc1_:uint = 0;
         while(_loc1_ < const_65)
         {
            this.var_395[_loc1_].Hide();
            _loc1_++;
         }
      }
      
      private function method_1485() : void
      {
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            this.var_841 = new Vector.<class_10>();
            return;
         }
         var _loc2_:String = this.var_672[this.var_528];
         if(_loc2_ == "Master")
         {
            this.var_1398 = true;
            this.var_841 = var_1.mAbilityBook.getMasterSpells();
         }
         else
         {
            this.var_1398 = false;
            this.var_841 = var_1.mAbilityBook.getSpellsByCategory(_loc2_,false);
         }
      }
      
      private function method_404() : void
      {
         var _loc2_:class_33 = null;
         var _loc3_:MovieClip = null;
         var _loc1_:uint = 0;
         while(_loc1_ < const_285)
         {
            _loc2_ = this.var_605[_loc1_];
            _loc2_.PlayAnimation(class_129.const_380);
            _loc3_ = _loc2_.mMovieClip.am_IconHolder;
            method_12(_loc3_,this.var_1404[_loc1_]);
            _loc1_++;
         }
         this.var_605[this.var_528].PlayAnimation(class_129.const_225);
         MathUtil.method_2(this.var_1546.mMovieClip.am_CategoryName,this.var_1015[this.var_528]);
      }
      
      private function method_1530(param1:MouseEvent, param2:uint) : void
      {
         MathUtil.method_2(var_2.am_Header,this.var_1015[param2]);
         if(this.var_528 == param2)
         {
            this.var_605[param2].PlayAnimation(class_129.const_225);
            return;
         }
         this.var_605[param2].PlayAnimation(class_129.const_817);
         this.var_1955[param2].PlayAnimation("Glare");
      }
      
      private function method_1526(param1:MouseEvent, param2:uint) : void
      {
         MathUtil.method_2(var_2.am_Header,this.var_1015[this.var_528]);
         if(this.var_528 == param2)
         {
            this.var_605[param2].PlayAnimation(class_129.const_225);
            return;
         }
         this.var_605[param2].PlayAnimation(class_129.const_380);
      }
      
      private function method_1376(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         if(param2 != this.var_528)
         {
            var_16 = 0;
         }
         this.var_429 = -1;
         this.method_332(this.var_429);
         this.var_528 = param2;
         Refresh();
      }
      
      private function method_332(param1:int) : void
      {
         var _loc2_:uint = 0;
         while(_loc2_ < const_65)
         {
            this.var_395[_loc2_].mMovieClip.am_Selector.visible = false;
            _loc2_++;
         }
         if(param1 != -1)
         {
            this.var_395[param1].mMovieClip.am_Selector.visible = true;
         }
      }
      
      private function method_1641(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         var _loc4_:uint = var_16 * const_65;
         var _loc5_:class_10 = this.var_877[param2];
         if(param1.ctrlKey && !var_1.screenInteractiveTutorial.mCurrentTutorialIdx)
         {
            var_1.screenSpellbook.LinkAbilityInChat(_loc5_);
            return;
         }
         if(this.var_429 == param2 + _loc4_)
         {
            return;
         }
         this.var_429 = param2 + _loc4_;
         this.var_254 = _loc5_;
         this.method_332(param2);
         if((Boolean(!!_loc3_ ? _loc3_.GetPowerFromAbilityType(_loc5_) : null)) && null != this.var_2721)
         {
            this.method_1330(null,param2);
            this.var_2721 = null;
         }
         else
         {
            Refresh();
         }
      }
      
      private function method_1847(param1:MouseEvent, param2:uint) : void
      {
         if(!param1.ctrlKey)
         {
            return;
         }
         var _loc3_:class_10 = this.var_254;
         var _loc4_:PowerType = class_14.powerTypesDict[_loc3_.abilityName + (param2 + 1)];
         var _loc5_:class_10;
         if(_loc5_ = var_1.screenSpellbook.GetAbilityTypeFromPowerType(_loc4_))
         {
            var_1.screenSpellbook.LinkAbilityInChat(_loc5_,_loc5_.rank);
         }
      }
      
      private function method_1118(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:class_10 = !!this.var_254 ? this.var_254 : (this.var_429 != -1 ? this.var_877[this.var_429] : null);
         if(!_loc3_)
         {
            return;
         }
      }
      
      private function method_1458(param1:MouseEvent, param2:uint) : void
      {
         this.var_246[param2].mMovieClip.am_Selector.visible = false;
         var_1.screenHudTooltip.HideTooltip();
      }
      
      private function method_1713(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:uint = var_16 * const_65;
         var _loc4_:class_10 = this.var_877[param2];
         var _loc5_:uint = uint(var_1.mAbilityBook.GetCurrRankByAbilityID(_loc4_.abilityID));
         var _loc6_:PowerType;
         if(!(_loc6_ = class_14.powerTypesDict[!!_loc5_ ? _loc4_.abilityName + _loc5_ : _loc4_.abilityName]))
         {
            return;
         }
         var_1.screenHudTooltip.ShowPowerTooltip(var_1.clientEnt,_loc6_,683.4,635.4);
         if(this.var_429 == param2 + _loc3_)
         {
            return;
         }
         this.var_395[param2].mMovieClip.am_Highlighter.visible = true;
         this.var_1692[param2].PlayAnimation("Glare");
      }
      
      private function method_1114(param1:MouseEvent, param2:uint) : void
      {
         this.var_395[param2].mMovieClip.am_Highlighter.visible = false;
         var_1.screenHudTooltip.HideTooltip();
      }
      
      public function Train(param1:MouseEvent, param2:Boolean = false) : void
      {
         var _loc11_:uint = 0;
         var _loc12_:Packet = null;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_ || !var_1.CanSendPacket())
         {
            return;
         }
         var _loc4_:class_10;
         if(!(_loc4_ = !!this.var_254 ? this.var_254 : this.var_877[this.var_429]))
         {
            return;
         }
         if(var_1.mAbilityBook.mStatus != class_45.const_29)
         {
            return;
         }
         var _loc5_:uint = _loc4_.abilityID;
         var _loc6_:uint;
         if((_loc6_ = uint(var_1.mAbilityBook.GetCurrRankByAbilityID(_loc5_))) >= class_10.const_105)
         {
            return;
         }
         var _loc7_:uint = uint(_loc6_ + 1);
         var _loc8_:class_10;
         if(!(_loc8_ = class_10.method_352(_loc4_.abilityName,_loc7_)))
         {
            return;
         }
         var _loc9_:class_9 = var_1.mBuildingInfo.GetOwnedBuildingByName("Tome");
         var _loc10_:uint = 0;
         if(_loc9_)
         {
            _loc10_ = _loc9_.rank;
         }
         if(_loc7_ > _loc10_)
         {
            return;
         }
         if(!param2 && _loc3_.currGold < _loc8_.var_129)
         {
            var_1.screenGoldShort.Display(_loc8_.var_129,_loc8_.var_365,class_93.const_441,_loc8_);
         }
         else
         {
            if(_loc3_.currGold >= _loc8_.var_129)
            {
               param2 = false;
            }
            var_1.mAbilityBook.mStatus = class_45.const_191;
            var_1.mAbilityBook.mAbilityResearch = _loc8_;
            var_1.mAbilityBook.mAbilityResearchFinishTime = var_1.mServerGameTime + _loc8_.upgradeTime;
            _loc11_ = 0;
            if(!param2)
            {
               _loc3_.GainMoney(-_loc8_.var_129,false);
            }
            (_loc12_ = new Packet(LinkUpdater.const_1077)).method_20(class_10.const_83,_loc5_);
            _loc12_.method_20(class_10.const_665,_loc7_);
            _loc12_.method_15(param2);
            var_1.serverConn.SendPacket(_loc12_);
            this.var_417.BeginHealthMode("Progress",2);
            Refresh();
         }
      }
      
      override public function OnTickScreen() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:int = 0;
         var _loc3_:class_10 = null;
         var _loc4_:Packet = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(var_1.mAbilityBook.mStatus == class_45.const_191)
         {
            _loc1_ = uint(var_1.mAbilityBook.mAbilityResearchFinishTime);
            _loc2_ = _loc1_ - var_1.mServerGameTime;
            if(_loc2_ < 0)
            {
               _loc2_ = 0;
            }
            this.var_417.mHealthPerc = 1 - _loc2_ / var_1.mAbilityBook.mAbilityResearch.upgradeTime;
            MathUtil.method_2(this.var_179.mMovieClip.am_Progress.am_Time,Game.method_70(_loc2_));
            MathUtil.method_2(this.var_871.mMovieClip.am_Idols,Game.method_229(_loc2_));
         }
         if(Boolean(var_1.mAbilityBook.CheckForDoneResearch()) && Boolean(mWindow.mbCompleted))
         {
            _loc3_ = var_1.mAbilityBook.mAbilityResearch;
            this.var_417.mHealthPerc = 0;
            this.var_417.BeginHealthMode("Progress",2);
            var_1.mAbilityBook.GiveNewRank();
            var_1.mAbilityBook.RebuildHotbar();
            _loc4_ = new Packet(LinkUpdater.const_1205);
            var_1.serverConn.SendPacket(_loc4_);
            this.var_1167 = false;
            Refresh();
         }
      }
      
      private function method_1786(param1:MouseEvent) : void
      {
         this.var_1167 = true;
         Refresh();
      }
      
      private function method_1501(param1:MouseEvent) : void
      {
         if(!var_1.CanSendPacket())
         {
            return;
         }
         this.var_1167 = false;
         var_1.mAbilityBook.mStatus = class_45.const_29;
         var_1.mAbilityBook.mAbilityResearch = null;
         var_1.mAbilityBook.mAbilityResearchFinishTime = 0;
         this.var_417.mHealthPerc = 0;
         var _loc2_:Packet = new Packet(LinkUpdater.const_1129);
         var_1.serverConn.SendPacket(_loc2_);
         Refresh();
      }
      
      private function method_1293(param1:MouseEvent) : void
      {
         this.var_1167 = false;
         Refresh();
      }
      
      private function method_1124(param1:MouseEvent) : void
      {
         var _loc5_:uint = 0;
         var _loc6_:class_33 = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         var _loc2_:int = var_1.mAbilityBook.mAbilityResearchFinishTime - var_1.mServerGameTime;
         var _loc3_:uint = Game.method_257(_loc2_);
         if(var_1.mMammothIdols < _loc3_)
         {
            var_1.screenBuyIdols.Display(_loc3_ - var_1.mMammothIdols);
            return;
         }
         if(var_1.mAbilityBook.mAbilityResearch.abilityID == this.var_254.abilityID)
         {
            _loc5_ = uint(var_1.mAbilityBook.GetCurrRankByAbilityID(var_1.mAbilityBook.mAbilityResearch.abilityID));
            (_loc6_ = this.var_765[_loc5_]).Show();
            _loc6_.PlayAnimation("Activate",class_33.const_14);
         }
         this.var_417.BeginHealthMode("Progress",2);
         this.var_1804.DisableButton("Inactive");
         var _loc4_:Packet;
         (_loc4_ = new Packet(LinkUpdater.const_1111)).method_9(_loc3_);
         var_1.serverConn.SendPacket(_loc4_);
      }
      
      private function method_1372(param1:MouseEvent) : void
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
         if(!(_loc4_ = _loc3_.GetOwnedBuildingByName("Tome")))
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
      
      private function method_1330(param1:PowerType, param2:uint) : void
      {
         if(param2 >= this.var_395.length)
         {
            return;
         }
         var _loc3_:class_33 = this.var_395[param2];
         var _loc4_:class_33 = this.var_246[0];
         if(!_loc3_ || !_loc4_)
         {
            return;
         }
         var _loc5_:Rectangle = _loc3_.mMovieClip.am_IconHolder.getBounds(mWindow.mMovieClip);
         method_68(param1.iconName,_loc5_.x,_loc5_.y,_loc4_.mMovieClip.am_ButtonHolder,250,class_137.method_113,this.method_1196,false);
      }
      
      private function method_1196() : void
      {
         Refresh();
      }
   }
}
