package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.utils.Dictionary;
   
   public class class_69 extends class_32
   {
      
      private static const const_1330:uint = 50;
      
      private static const const_224:uint = 3;
      
      private static const const_542:Dictionary = new Dictionary();
      
      public static const const_94:Dictionary = new Dictionary();
      
      {
         const_542["Paladin"] = class_9.var_1616;
         const_542["Rogue"] = class_9.var_1618;
         const_542["Mage"] = class_9.var_1357;
         const_94["frostwarden"] = "Frostbringer";
         const_94["flameseer"] = "Flameseer";
         const_94["necromancer"] = "Necromancer";
         const_94["sentinel"] = "Sentinel";
         const_94["justicar"] = "Justicar";
         const_94["templar"] = "Templar";
         const_94["soulthief"] = "Soulthief";
         const_94["shadowwalker"] = "Shadowstalker";
         const_94["executioner"] = "Viperblade";
      }
      
      public var var_60:class_33;
      
      private var var_2150:class_33;
      
      private var var_1753:class_33;
      
      private var var_2818:class_33;
      
      private var var_605:Vector.<class_33>;
      
      private var var_1184:Vector.<class_33>;
      
      private var var_2353:uint;
      
      private var mMasterClass:String;
      
      private var var_569:class_33;
      
      private var var_1385:class_33;
      
      private var var_664:class_33;
      
      private var var_1645:class_33;
      
      private var var_1873:class_33;
      
      private var var_964:class_33;
      
      private var var_1238:class_33;
      
      private var var_1045:Boolean;
      
      private var var_1134:class_33;
      
      private var var_1324:class_33;
      
      private var var_1545:class_33;
      
      private var var_617:class_33;
      
      private var var_1018:class_33;
      
      private var mTooltip:class_33;
      
      private var var_449:class_33;
      
      private var var_261:class_33;
      
      private var var_1580:class_33;
      
      private var var_1144:Vector.<class_33>;
      
      public function class_69(param1:Game)
      {
         super(param1,"a_ScreenClassTower","am_Panel");
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc3_:MovieClip = null;
         var _loc1_:MovieClip = var_2.am_ClassTabs;
         this.var_605 = new Vector.<class_33>(const_224,true);
         this.var_1184 = new Vector.<class_33>(const_224,true);
         this.var_1144 = new Vector.<class_33>(const_224,true);
         var _loc2_:int = 0;
         while(_loc2_ < const_224)
         {
            this.var_605[_loc2_] = method_3(_loc1_["am_ClassTab" + _loc2_] as MovieClip,_loc2_,this.method_687,this.method_1854,this.method_1198);
            _loc3_ = this.var_605[_loc2_].mMovieClip;
            this.var_1184[_loc2_] = method_1(_loc3_.am_Portrait);
            this.var_1144[_loc2_] = method_1(_loc3_.am_Selector);
            _loc2_++;
         }
         this.var_1753 = method_17(var_2.am_Progress,"Progress",0.5);
         this.var_1753.BeginHealthMode("Progress",0.5);
         this.var_2818 = method_5(var_2.am_LockAnimation,null,this.method_1758,this.method_1314);
         this.var_2150 = method_1(var_2.am_Illustration);
         this.var_261 = method_1(var_2.am_Notice);
         this.var_1873 = method_1(mWindow.mMovieClip.am_GlobalUpgradePanel);
         this.var_1645 = method_10(mWindow.mMovieClip.am_GlobalUpgradePanel.am_Upgrade,this.method_1100);
         this.var_1134 = method_1(var_2.am_SpeedUpPanel);
         this.var_1324 = method_10(var_2.am_SpeedUpPanel.am_SpeedUp,this.method_1410);
         this.var_1545 = method_1(var_2.am_TrainTalentPanel);
         this.var_664 = method_10(var_2.am_TrainTalentPanel.am_TrainTalent,this.TrainTalentPoint);
         this.mTooltip = method_1(var_2.am_Tooltip);
         this.mTooltip.Hide();
         this.var_617 = method_1(var_2.am_ResearchProgressPanel);
         this.var_964 = method_5(var_2.am_Cancel,this.method_650);
         this.var_1238 = method_17(this.var_617.mMovieClip.am_Progress,"Progress",2);
         this.var_1018 = method_1(var_2.am_CancelPanel);
         method_10(var_2.am_CancelPanel.am_CancelTraining,this.method_1013);
         method_10(var_2.am_CancelPanel.am_NeverMind,this.method_650);
         this.var_449 = method_1(var_2.am_WarningAnim);
         this.var_569 = method_1(var_2.am_BuildingTooLow);
         this.var_1385 = method_1(var_2.am_TalentsMastered);
         this.var_1580 = method_1(var_2.am_TalentProgHeader);
         this.var_60 = method_1(var_2.am_TutorialInteraction);
         this.var_60.Hide();
         method_23(var_2.am_Close);
         var_2.cacheAsBitmap = true;
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1753 = null;
         this.var_664 = null;
         this.var_2150 = null;
         this.var_1645 = null;
         this.var_1873 = null;
         this.var_1134 = null;
         this.var_1324 = null;
         this.var_617 = null;
         this.var_1238 = null;
         this.var_1018 = null;
         this.var_964 = null;
         this.var_449 = null;
         this.mTooltip = null;
         this.var_1545 = null;
         this.var_605 = null;
         this.var_1184 = null;
         this.var_1144 = null;
         this.var_261 = null;
         this.var_569 = null;
         this.var_1385 = null;
         this.var_1580 = null;
         this.var_60 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc5_:class_33 = null;
         var _loc6_:class_33 = null;
         var _loc15_:int = 0;
         var _loc16_:String = null;
         var _loc17_:MovieClip = null;
         var _loc18_:Array = null;
         var _loc19_:uint = 0;
         var _loc20_:uint = 0;
         var _loc21_:MovieClip = null;
         var _loc22_:uint = 0;
         var _loc23_:uint = 0;
         var _loc24_:uint = 0;
         var _loc25_:String = null;
         var _loc26_:class_9 = null;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:class_66 = var_1.mMasterClassTower;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:String = _loc1_.mMasterClass;
         if(!_loc3_)
         {
            var_1.screenMasterClassSelection.Display();
            return;
         }
         this.mMasterClass = _loc3_;
         this.var_2353 = class_9.method_472(this.mMasterClass);
         var _loc4_:String = _loc1_.entType.className.toLowerCase();
         var _loc7_:Vector.<String> = class_52.const_31[_loc4_];
         var _loc8_:Vector.<String> = class_52.const_31[_loc4_ + "Display"];
         if(_loc7_)
         {
            _loc15_ = 0;
            while(_loc15_ < const_224)
            {
               _loc5_ = this.var_605[_loc15_];
               _loc16_ = _loc8_[_loc15_];
               _loc17_ = _loc5_.mMovieClip;
               MathUtil.method_2(_loc17_.am_Level,String(var_1.mMasterClassTower.GetPointsByMC(_loc7_[_loc15_])));
               MathUtil.method_2(_loc17_.am_ClassName,_loc16_);
               (_loc6_ = this.var_1184[_loc15_]).PlayAnimation(_loc7_[_loc15_]);
               _loc15_++;
            }
         }
         var _loc9_:class_9;
         if(!(_loc9_ = this.method_256(this.var_2353)))
         {
            return;
         }
         var _loc10_:class_9 = class_9.method_132(_loc9_);
         this.var_2150.PlayAnimation(this.mMasterClass);
         var _loc11_:uint = class_66.method_251(_loc3_);
         var _loc12_:uint = uint(var_1.mMasterClassTower.GetPointsByIndex(_loc11_));
         this.var_1753.mHealthPerc = _loc12_ / 50;
         this.var_2818.PlayAnimation(_loc9_.rank.toString());
         if(_loc2_.mStatus == class_66.const_200)
         {
            this.var_1134.Show();
            this.var_617.Show();
            this.var_1580.Show();
            this.var_261.Hide();
            this.var_1545.Hide();
            this.var_569.Hide();
            this.var_1385.Hide();
            if(!this.var_1045)
            {
               this.var_964.Show();
               this.var_1018.Hide();
               this.var_449.PlayAnimation("Ready");
               this.var_449.Hide();
            }
            else
            {
               this.var_964.Hide();
               this.var_1018.Show();
               this.var_449.Show();
               if(this.var_449.var_175 == 1)
               {
                  this.var_449.PlayAnimation("Warning");
               }
            }
            _loc18_ = [class_50.const_112];
            for each(_loc6_ in this.var_1184)
            {
               _loc6_.mMovieClip.filters = _loc18_;
            }
            _loc19_ = var_1.mMasterClassTower.mEndtime - var_1.mServerGameTime;
            MathUtil.method_2(this.var_1134.mMovieClip.am_Idols,Game.method_229(_loc19_));
            MathUtil.method_2(this.var_617.mMovieClip.am_Name,"Talent Point - " + const_94[this.mMasterClass]);
            method_12(this.var_617.mMovieClip.am_IconHolder,"a_TalentPointIcon");
            if(this.var_1045)
            {
               this.var_1018.Show();
               this.var_964.Hide();
            }
            else
            {
               this.var_1018.Hide();
               this.var_964.Show();
            }
         }
         else
         {
            this.var_964.Hide();
            this.var_1018.Hide();
            this.var_1134.Hide();
            this.var_617.Hide();
            this.var_1545.Show();
            this.var_261.Show();
            this.var_449.PlayAnimation("Ready");
            this.var_449.Hide();
            MathUtil.method_2(this.var_1238.mMovieClip.am_Time,"");
            MathUtil.method_2(this.var_617.mMovieClip.am_Name,"");
            method_14(this.var_617.mMovieClip.am_IconHolder);
            for each(_loc6_ in this.var_1184)
            {
               _loc6_.mMovieClip.filters = [];
            }
            _loc20_ = uint(var_1.mMasterClassTower.GetPointsByMC(this.mMasterClass));
            _loc21_ = this.var_1545.mMovieClip;
            if((_loc22_ = uint(_loc12_ + 1)) > class_66.const_495)
            {
               MathUtil.method_8(_loc21_.am_Gold,"--",ScreenArmory.const_9,ScreenArmory.const_17);
               MathUtil.method_8(_loc21_.am_Time,"--",ScreenArmory.const_9,ScreenArmory.const_17);
               this.var_664.Hide();
               this.var_1580.Hide();
               this.var_1385.Show();
               this.var_569.Hide();
               this.var_261.Hide();
            }
            else
            {
               _loc23_ = _loc9_.rank * 5;
               if(Boolean(_loc20_) && _loc20_ == _loc23_)
               {
                  MathUtil.method_8(_loc21_.am_Gold,"--",ScreenArmory.const_9,ScreenArmory.const_17);
                  MathUtil.method_8(_loc21_.am_Time,"--",ScreenArmory.const_9,ScreenArmory.const_17);
                  this.var_664.Hide();
                  this.var_261.Hide();
                  if(!this.var_569.mbVisible)
                  {
                     _loc24_ = uint(_loc9_.displayName.indexOf(" Level"));
                     _loc25_ = _loc9_.displayName.substr(0,_loc24_);
                     MathUtil.method_2(this.var_569.mMovieClip.am_Notice.am_Text,"Requires: " + _loc25_ + " Level " + (_loc9_.rank + 1));
                     this.var_569.PlayAnimation("Warning");
                     this.var_569.Show();
                  }
               }
               else
               {
                  MathUtil.method_8(_loc21_.am_Time,Game.method_70(class_66.const_527[_loc22_],true),ScreenArmory.const_11,ScreenArmory.const_47);
                  MathUtil.method_8(_loc21_.am_Gold,MathUtil.method_29(class_66.const_553[_loc22_]),ScreenArmory.const_11,ScreenArmory.const_47);
                  this.var_664.Show();
                  this.var_664.EnableButton();
                  this.var_569.Hide();
               }
               this.var_1385.Hide();
               this.var_1580.Show();
            }
         }
         _loc9_ = var_1.mBuildingInfo.GetBuildingByMasterClass(_loc3_);
         var_1.UpdateBuildingUpgradePanel(this.var_1873.mMovieClip,_loc9_,this.var_1645);
         if(_loc2_.mStatus == class_66.const_200)
         {
            this.var_1645.Hide();
            this.var_664.DisableButton("Inactive");
            if(_loc9_.rank < class_9.const_214)
            {
               MathUtil.method_8(this.var_1873.mMovieClip.am_Message,"Cannot upgrade while training a Talent Point",ScreenArmory.const_137,ScreenArmory.const_169);
            }
         }
         else if(var_1.mBuildingInfo.mStatus != class_105.const_29)
         {
            this.var_1645.Hide();
            if((Boolean(_loc26_ = var_1.mBuildingInfo.GetCurrentBuilding())) && _loc26_.var_242 == _loc9_.var_242)
            {
               this.var_664.DisableButton("Inactive");
            }
         }
         var _loc13_:uint = uint(_loc9_.displayName.indexOf(" Level"));
         var _loc14_:String = _loc9_.displayName.substr(0,_loc13_);
         MathUtil.method_2(var_2.am_Header,_loc14_);
         MathUtil.method_2(var_2.am_Level,String(_loc9_.rank));
         this.var_1324.EnableButton();
      }
      
      public function OnInitDisplay() : void
      {
         var _loc2_:Vector.<class_33> = null;
         this.var_1045 = false;
         var _loc1_:uint = 0;
         while(_loc1_ < const_224)
         {
            this.var_1144[_loc1_].Hide();
            _loc1_++;
         }
         this.var_569.Hide();
         if(!var_1.screenInteractiveTutorial.CheckCompletedTutorials(class_89.const_263))
         {
            this.var_60.Show();
            _loc2_ = new Vector.<class_33>();
            _loc2_.push(this.var_664);
            _loc2_.push(this.var_1324);
            var_1.screenInteractiveTutorial.SetTutorial(class_89.const_263,this,this.var_60,_loc2_);
         }
      }
      
      private function method_256(param1:uint) : class_9
      {
         var _loc3_:class_9 = null;
         var _loc2_:Dictionary = var_1.mBuildingInfo.mData;
         for each(_loc3_ in _loc2_)
         {
            if(_loc3_.var_208 == param1)
            {
               return _loc3_;
            }
         }
         return null;
      }
      
      private function method_2088(param1:Entity) : Vector.<uint>
      {
         var _loc2_:String = param1.entType.className;
         if(_loc2_ == "Paladin")
         {
            return class_9.var_1616;
         }
         if(_loc2_ == "Rogue")
         {
            return class_9.var_1618;
         }
         return class_9.var_1357;
      }
      
      private function method_1410(param1:MouseEvent) : void
      {
         if(!var_1.CanSendPacket())
         {
            return;
         }
         var _loc2_:int = var_1.mMasterClassTower.mEndtime - var_1.mServerGameTime;
         var _loc3_:uint = Game.method_257(_loc2_);
         if(var_1.mMammothIdols < _loc3_)
         {
            var_1.screenBuyIdols.Display(_loc3_ - var_1.mMammothIdols);
            return;
         }
         this.var_1324.DisableButton("Inactive");
         var _loc4_:Packet;
         (_loc4_ = new Packet(LinkUpdater.const_1284)).method_9(_loc3_);
         var_1.serverConn.SendPacket(_loc4_);
      }
      
      private function method_650(param1:MouseEvent) : void
      {
         this.var_1045 = !this.var_1045;
         Refresh();
      }
      
      private function method_1013(param1:MouseEvent) : void
      {
         this.var_1045 = false;
         var_1.mMasterClassTower.ClearResearch();
         Refresh();
      }
      
      private function method_1854(param1:MouseEvent, param2:uint) : void
      {
         this.var_1144[param2].Show();
      }
      
      private function method_1198(param1:MouseEvent, param2:uint) : void
      {
         this.var_1144[param2].Hide();
      }
      
      private function method_687(param1:MouseEvent, param2:uint) : void
      {
         if(var_1.mMasterClassTower.mStatus == class_66.const_200)
         {
            return;
         }
         Hide();
         var_1.screenMasterClassSelection.Display();
      }
      
      public function TrainTalentPoint(param1:MouseEvent, param2:Boolean = false) : void
      {
         var _loc10_:class_9 = null;
         var _loc11_:uint = 0;
         var _loc12_:uint = 0;
         var _loc13_:uint = 0;
         var _loc14_:uint = 0;
         var _loc15_:Packet = null;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_ || !var_1.CanSendPacket())
         {
            return;
         }
         if(!var_1.mBuildingInfo)
         {
            return;
         }
         if(var_1.mMasterClassTower.mStatus != class_66.const_185)
         {
            return;
         }
         if(var_1.mBuildingInfo.mWorkerBuildingID)
         {
            if((Boolean(_loc10_ = class_14.var_278[var_1.mBuildingInfo.mWorkerBuildingID])) && _loc10_.type == "Tower")
            {
               return;
            }
         }
         var _loc4_:class_105 = var_1.mBuildingInfo;
         var _loc5_:String = _loc3_.mMasterClass;
         var _loc6_:uint = class_66.method_251(_loc5_);
         var _loc7_:String = _loc4_.method_238(_loc5_);
         var _loc8_:uint = _loc4_.mData[_loc7_].rank * class_66.const_948;
         var _loc9_:uint = uint(var_1.mMasterClassTower.GetPointsByIndex(_loc6_));
         if(Boolean(_loc6_) && _loc9_ < _loc8_)
         {
            _loc12_ = (_loc11_ = uint(class_66.const_527[_loc9_ + 1])) + var_1.mServerGameTime;
            _loc13_ = uint(class_66.const_553[_loc9_ + 1]);
            _loc14_ = uint(class_66.const_1002[_loc9_ + 1]);
            if(!param2 && _loc3_.currGold < _loc13_)
            {
               var_1.screenGoldShort.Display(_loc13_,_loc14_,class_93.const_577,_loc6_);
            }
            else
            {
               var_1.mMasterClassTower.SetCurrentResearch(_loc6_,_loc12_);
               if(!param2)
               {
                  _loc3_.GainMoney(-_loc13_,false);
               }
               (_loc15_ = new Packet(LinkUpdater.const_1044)).method_20(class_66.const_571,_loc6_);
               _loc15_.method_15(param2);
               var_1.serverConn.SendPacket(_loc15_);
            }
         }
         this.var_1238.BeginHealthMode("Progress",2);
         Refresh();
      }
      
      override public function OnTickScreen() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:int = 0;
         var _loc3_:uint = 0;
         var _loc4_:int = 0;
         var _loc5_:Packet = null;
         if(!var_1.mMasterClassTower || !var_1.CanSendPacket())
         {
            return;
         }
         if(var_1.mMasterClassTower.mStatus == class_66.const_200)
         {
            _loc1_ = uint(var_1.mMasterClassTower.mEndtime);
            _loc2_ = _loc1_ - var_1.mServerGameTime;
            if(_loc2_ < 0)
            {
               _loc2_ = 0;
            }
            MathUtil.method_8(this.var_1238.mMovieClip.am_Time,Game.method_70(_loc2_),ScreenArmory.const_11,ScreenArmory.const_47);
            MathUtil.method_8(var_2.am_Gold2,"--",ScreenArmory.const_9,ScreenArmory.const_17);
            MathUtil.method_2(this.var_1134.mMovieClip.am_Idols,Game.method_229(_loc2_));
            this.var_1238.mHealthPerc = 1 - _loc2_ / class_66.method_1210(var_1.mMasterClassTower.GetPointsByIndex(var_1.mMasterClassTower.mCurrentResearchIndex) + 1);
         }
         if(var_1.mBuildingInfo.mStatus == class_105.const_339)
         {
            _loc3_ = uint(var_1.mBuildingInfo.mWorkerEndtime);
            if((_loc4_ = _loc3_ - var_1.mServerGameTime) < 0)
            {
               _loc4_ = 0;
            }
            MathUtil.method_8(var_2.am_Time,Game.method_70(_loc4_),ScreenArmory.const_11,ScreenArmory.const_47);
            MathUtil.method_8(var_2.am_Gold,"--",ScreenArmory.const_9,ScreenArmory.const_17);
         }
         if(var_1.mMasterClassTower.mStatus == class_66.const_534 && Boolean(mWindow.mbCompleted))
         {
            var_1.mMasterClassTower.GiveNewResearchPoint();
            _loc5_ = new Packet(LinkUpdater.const_987);
            var_1.serverConn.SendPacket(_loc5_);
            this.var_1045 = false;
            Refresh();
         }
      }
      
      private function method_1100(param1:MouseEvent) : void
      {
         var _loc6_:class_9 = null;
         var _loc2_:Entity = var_1.clientEnt;
         var _loc3_:class_105 = var_1.mBuildingInfo;
         if(!_loc2_)
         {
            return;
         }
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_9;
         if(!(_loc4_ = _loc3_.GetBuildingByMasterClass(_loc2_.mMasterClass)))
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
            var_1.screenUpgrading.Display(_loc6_);
            Hide();
         }
      }
      
      private function method_1758(param1:MouseEvent) : void
      {
         var _loc2_:class_9 = this.method_256(this.var_2353);
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:uint = class_66.method_251(this.mMasterClass);
         var _loc4_:uint;
         if((_loc4_ = uint(var_1.mMasterClassTower.GetPointsByIndex(_loc3_))) >= _loc2_.rank * 5)
         {
            MathUtil.method_8(this.mTooltip.mMovieClip.am_Text,"Requires Building Level " + (_loc2_.rank + 1),ScreenArmory.const_137,ScreenArmory.const_169);
         }
         else
         {
            MathUtil.method_8(this.mTooltip.mMovieClip.am_Text,"Requires Building Level " + (_loc2_.rank + 1),ScreenArmory.const_11,ScreenArmory.const_47);
         }
         this.mTooltip.Show();
      }
      
      private function method_1314(param1:MouseEvent) : void
      {
         this.mTooltip.Hide();
         Refresh();
      }
   }
}
