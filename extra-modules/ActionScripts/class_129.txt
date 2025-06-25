package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   import flash.utils.Dictionary;
   
   public class class_129 extends class_32
   {
      
      private static const const_285:uint = 4;
      
      private static const const_65:uint = 13;
      
      public static const const_817:String = "Over";
      
      public static const const_225:String = "Selected";
      
      public static const const_380:String = "Deselected";
      
      public static const const_197:String = "Active";
      
      private static const const_42:Dictionary = new Dictionary();
      
      {
         const_42["Mage"] = 0;
         const_42["Rogue"] = 0;
         const_42["Paladin"] = 0;
         const_42["Frostwarden"] = 1;
         const_42["Executioner"] = 1;
         const_42["Sentinel"] = 1;
         const_42["Flameseer"] = 2;
         const_42["Shadowwalker"] = 2;
         const_42["Justicar"] = 2;
         const_42["Necromancer"] = 3;
         const_42["Soulthief"] = 3;
         const_42["Templar"] = 3;
      }
      
      private var var_60:class_33;
      
      private var var_605:Vector.<class_33>;
      
      private var var_1955:Vector.<class_33>;
      
      private var var_2983:int;
      
      private var var_2971:Boolean;
      
      private var var_395:Vector.<class_33>;
      
      private var var_1640:Vector.<class_33>;
      
      private var var_1154:Vector.<class_33>;
      
      private var var_1880:TextField;
      
      private var var_834:class_33;
      
      private var var_1199:class_10;
      
      private var var_528:uint;
      
      private var var_1596:int;
      
      private var var_1404:Vector.<String>;
      
      private var var_1541:Vector.<class_33>;
      
      private var var_672:Vector.<String>;
      
      private var var_1015:Vector.<String>;
      
      private var var_841:Vector.<class_10>;
      
      private var var_2214:Boolean = false;
      
      private var var_2212:class_33;
      
      public function class_129(param1:Game)
      {
         super(param1,"a_ScreenSpellbook","am_Panel");
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc4_:MovieClip = null;
         var _loc5_:MovieClip = null;
         var _loc1_:MovieClip = var_2.am_SlotGroup;
         this.var_1154 = new Vector.<class_33>(const_65,true);
         this.var_395 = new Vector.<class_33>(const_65,true);
         this.var_1640 = new Vector.<class_33>(const_65,true);
         var _loc2_:uint = 0;
         while(_loc2_ < const_65)
         {
            _loc4_ = _loc1_["am_Slot" + _loc2_] as MovieClip;
            this.var_1640[_loc2_] = method_1(_loc4_.am_New);
            this.var_1154[_loc2_] = method_17(_loc4_.am_Progress,"Progress",8);
            this.var_395[_loc2_] = method_3(_loc4_,_loc2_,this.method_1641,this.method_1378,this.method_1516);
            _loc2_++;
         }
         var _loc3_:MovieClip = var_2.am_TabGroup;
         this.var_605 = new Vector.<class_33>(const_285,true);
         this.var_1955 = new Vector.<class_33>(const_285,true);
         this.var_1541 = new Vector.<class_33>(const_285,true);
         _loc2_ = 0;
         while(_loc2_ < const_285)
         {
            _loc5_ = _loc3_["am_Tab" + _loc2_] as MovieClip;
            this.var_1541[_loc2_] = method_1(_loc5_.am_New);
            this.var_605[_loc2_] = method_3(_loc5_,_loc2_,this.method_1376,this.method_1530,this.method_1526);
            this.var_1955[_loc2_] = method_1(_loc5_.am_GlareAnim);
            _loc2_++;
         }
         this.var_528 = 0;
         this.var_2212 = method_1(var_2.am_ComingSoon);
         this.var_60 = method_1(var_2.am_TutorialInteraction);
         this.var_60.Hide();
         method_23(var_2.am_Exit);
         var_2.cacheAsBitmap = true;
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_605 = null;
         this.var_395 = null;
         this.var_1404 = null;
         this.var_1154 = null;
         this.var_834 = null;
         this.var_672 = null;
         this.var_1015 = null;
         this.var_841 = null;
         this.var_1199 = null;
         this.var_1880 = null;
         this.var_1955 = null;
         this.var_1640 = null;
         this.var_1541 = null;
         this.var_60 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc7_:class_33 = null;
         var _loc8_:MovieClip = null;
         var _loc9_:class_10 = null;
         var _loc10_:PowerType = null;
         var _loc11_:String = null;
         var _loc12_:Boolean = false;
         var _loc13_:Boolean = false;
         var _loc14_:uint = 0;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         this.method_404();
         this.method_1176();
         this.method_1184();
         this.method_1485();
         var _loc2_:String = this.var_672[this.var_528];
         var _loc3_:Boolean = class_50.method_454(_loc2_);
         if(!_loc3_)
         {
            this.var_2212.Hide();
            var_44 = Math.ceil(this.var_841.length / const_65);
            var _loc4_:uint = var_16 * const_65;
            var _loc5_:class_10 = var_1.mAbilityBook.mAbilityResearch;
            var _loc6_:uint = 0;
            while(_loc6_ < const_65)
            {
               if(_loc4_ + _loc6_ < this.var_841.length)
               {
                  (_loc7_ = this.var_395[_loc6_]).Show();
                  (_loc8_ = _loc7_.mMovieClip).am_Selector.visible = false;
                  _loc8_.am_PendingNote.visible = false;
                  this.var_1640[_loc6_].Hide();
                  _loc9_ = this.var_841[_loc6_ + _loc4_];
                  _loc10_ = class_14.powerTypesDict[_loc9_.abilityName];
                  method_12(_loc8_.am_IconHolder,_loc10_.iconName);
                  if(var_1.mAbilityBook.mHotbarList.indexOf(_loc9_) != -1)
                  {
                     _loc8_.am_Equipped.visible = true;
                  }
                  else
                  {
                     _loc8_.am_Equipped.visible = false;
                  }
                  if(!(_loc11_ = _loc9_.type))
                  {
                     _loc8_.am_MasterFrame.visible = false;
                  }
                  else if(_loc9_.var_223)
                  {
                     _loc8_.am_MasterFrame.visible = true;
                  }
                  else
                  {
                     _loc8_.am_MasterFrame.visible = false;
                  }
                  _loc12_ = !_loc9_.var_223 && Boolean(var_1.mAbilityBook.IsTrained(_loc9_)) || _loc9_.var_223 && _loc1_.var_85.method_245() >= _loc9_.var_90 && _loc9_.className.toLowerCase() == _loc1_.mMasterClass;
                  _loc13_ = false;
                  if(_loc5_)
                  {
                     if(_loc5_.abilityName == _loc9_.abilityName)
                     {
                        _loc13_ = true;
                     }
                  }
                  if(_loc13_)
                  {
                     _loc7_.PlayAnimation(const_197);
                     this.var_1199 = _loc9_;
                     this.var_834 = this.var_1154[_loc6_];
                     this.var_1880 = this.var_834.mMovieClip.am_Time;
                     if(var_1.mAbilityBook.mStatus != class_45.const_223)
                     {
                        this.var_834.Show();
                     }
                     else
                     {
                        this.var_1640[_loc6_].Show();
                        _loc8_.am_PendingNote.visible = true;
                        this.var_834.Hide();
                     }
                     MathUtil.method_8(_loc8_.am_Name,_loc10_.displayName,ScreenArmory.const_11,ScreenArmory.const_47);
                     MathUtil.method_8(_loc8_.am_Type,"",ScreenArmory.const_106,ScreenArmory.const_417);
                  }
                  else if(_loc12_)
                  {
                     _loc7_.PlayAnimation(const_197);
                     this.var_1154[_loc6_].Hide();
                     _loc14_ = uint(var_1.mAbilityBook.mAbilityListTrainedRanks[_loc9_.abilityID]);
                     MathUtil.method_8(_loc8_.am_Type,!!_loc14_ ? "Rank " + _loc14_ : "Rank 1",ScreenArmory.const_106,ScreenArmory.const_417);
                     MathUtil.method_8(_loc8_.am_Name,_loc10_.displayName,ScreenArmory.const_11,ScreenArmory.const_47);
                  }
                  else
                  {
                     _loc7_.PlayAnimation("Inactive");
                     this.var_1154[_loc6_].Hide();
                     _loc14_ = uint(var_1.mAbilityBook.mAbilityListTrainedRanks[_loc9_.abilityID]);
                     MathUtil.method_8(_loc8_.am_Type,!!_loc14_ ? "Rank " + _loc14_ : "Untrained",ScreenArmory.const_9,ScreenArmory.const_17);
                     MathUtil.method_8(_loc8_.am_Name,_loc10_.displayName,ScreenArmory.const_9,ScreenArmory.const_17);
                  }
               }
               _loc6_++;
            }
            return;
         }
         this.var_2212.Show();
      }
      
      override public function OnTickScreen() : void
      {
         var _loc2_:uint = 0;
         var _loc3_:int = 0;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         if(this.var_1199)
         {
            _loc2_ = uint(var_1.mAbilityBook.mAbilityResearchFinishTime);
            _loc3_ = _loc2_ - var_1.mServerGameTime;
            if(_loc3_ < 0)
            {
               _loc3_ = 0;
            }
            this.var_834.mHealthPerc = 1 - _loc3_ / var_1.mAbilityBook.mAbilityResearch.upgradeTime;
            if(this.var_1880.visible)
            {
               MathUtil.method_2(this.var_834.mMovieClip.am_Time,Game.method_70(_loc3_));
            }
            if(!this.var_2214 && var_1.mAbilityBook.mStatus == class_45.const_223)
            {
               this.var_1596 = const_42[this.var_1199.className];
               this.var_2214 = true;
               Refresh();
            }
         }
      }
      
      public function OnInitDisplay(param1:String) : void
      {
         var _loc4_:Vector.<class_33> = null;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         if(param1 == "Paladin")
         {
            this.var_1404 = class_50.const_713;
            this.var_672 = class_50.const_609;
            this.var_1015 = class_50.const_701;
         }
         else if(param1 == "Rogue")
         {
            this.var_1404 = class_50.const_669;
            this.var_672 = class_50.const_656;
            this.var_1015 = class_50.const_657;
         }
         else if(param1 == "Mage")
         {
            this.var_1404 = class_50.const_643;
            this.var_672 = class_50.const_614;
            this.var_1015 = class_50.const_776;
         }
         this.var_2214 = false;
         var_1.mAbilityBook.setCurrent();
         if(Boolean(var_1.mAbilityBook.mAbilityResearch) && var_1.mAbilityBook.mStatus == class_45.const_223)
         {
            this.var_1596 = const_42[var_1.mAbilityBook.mAbilityResearch.className];
         }
         else
         {
            this.var_1596 = -1;
         }
         var_1.screenHudTooltip.HideTooltip(true);
         var _loc3_:class_10 = var_1.screenInteractiveTutorial.GetTutorialAbility();
         if(!var_1.screenInteractiveTutorial.CheckCompletedTutorials(class_89.const_272) && _loc3_ && Boolean(var_1.mAbilityBook.GetCurrRankByAbilityID(_loc3_.abilityID)))
         {
            this.var_528 = 0;
            this.var_60.Show();
            (_loc4_ = new Vector.<class_33>()).push(this.var_395[6]);
            var_1.screenInteractiveTutorial.SetTutorial(class_89.const_272,this,this.var_60,_loc4_);
         }
      }
      
      private function method_1485() : void
      {
         var _loc2_:String = null;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            this.var_841 = new Vector.<class_10>();
         }
         else
         {
            _loc2_ = this.var_672[this.var_528];
            this.var_841 = var_1.mAbilityBook.getSpellsByCategory(_loc2_);
         }
      }
      
      private function method_1184() : void
      {
         if(this.var_1199)
         {
            this.var_1199 = null;
            this.var_834 = null;
            this.var_1880 = null;
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
      
      private function method_404() : void
      {
         var _loc2_:class_33 = null;
         var _loc1_:uint = 0;
         while(_loc1_ < const_285)
         {
            _loc2_ = this.var_605[_loc1_];
            _loc2_.PlayAnimation(const_380);
            method_12(_loc2_.mMovieClip.am_IconHolder,this.var_1404[_loc1_]);
            this.var_1541[_loc1_].Hide();
            _loc1_++;
         }
         if(this.var_1596 != -1)
         {
            this.var_1541[this.var_1596].Show();
         }
         this.var_605[this.var_528].PlayAnimation(const_225);
         MathUtil.method_2(var_2.am_Header,this.var_1015[this.var_528]);
      }
      
      private function method_1530(param1:MouseEvent, param2:uint) : void
      {
         MathUtil.method_2(var_2.am_Header,this.var_1015[param2]);
         if(this.var_528 == param2)
         {
            this.var_605[param2].PlayAnimation(const_225);
            return;
         }
         this.var_605[param2].PlayAnimation(const_817);
      }
      
      private function method_1526(param1:MouseEvent, param2:uint) : void
      {
         MathUtil.method_2(var_2.am_Header,this.var_1015[this.var_528]);
         if(this.var_528 == param2)
         {
            this.var_605[param2].PlayAnimation(const_225);
            return;
         }
         this.var_605[param2].PlayAnimation(const_380);
      }
      
      private function method_1376(param1:MouseEvent, param2:uint) : void
      {
         this.var_528 = param2;
         Refresh();
      }
      
      private function method_1641(param1:MouseEvent, param2:uint) : void
      {
         var _loc7_:MovieClip = null;
         var _loc8_:Rectangle = null;
         var _loc9_:class_10 = null;
         var _loc10_:PowerType = null;
         var _loc11_:Vector.<Entity> = null;
         var _loc12_:int = 0;
         var _loc13_:Entity = null;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:uint = var_16 * const_65;
         var _loc5_:class_10 = this.var_841[param2 + _loc4_];
         if(param1.ctrlKey && !var_1.screenInteractiveTutorial.mCurrentTutorialIdx)
         {
            this.LinkAbilityInChat(_loc5_);
            return;
         }
         var _loc6_:Boolean;
         if(_loc6_ = !_loc5_.var_223 && Boolean(var_1.mAbilityBook.IsTrained(_loc5_)) || _loc5_.var_223 && _loc3_.var_85.method_245() >= _loc5_.var_90)
         {
            if(_loc5_.var_90 > 0 && _loc5_.var_90 < 4)
            {
               if(!(_loc9_ = var_1.mAbilityBook.mHotbarList[_loc5_.var_90]))
               {
                  var_1.mAbilityBook.SetAbilities(_loc5_.var_90,class_14.var_478[_loc5_.abilityID]);
                  _loc8_ = (_loc7_ = this.var_395[param2].mMovieClip).getBounds(mWindow.mMovieClip);
                  var_1.screenHud.PlayPowerToHotbar(_loc8_.x,_loc8_.y,_loc5_,_loc3_);
               }
               else if(var_1.mAbilityBook.mHotbarList[_loc5_.var_90].abilityName != _loc5_.abilityName)
               {
                  _loc10_ = var_1.clientEnt.GetPowerFromAbilityType(var_1.mAbilityBook.mHotbarList[_loc5_.var_90]);
                  _loc11_ = var_1.GetSummonedCreatures(var_1.clientEntID,_loc10_);
                  _loc12_ = 0;
                  while(_loc12_ < _loc11_.length)
                  {
                     (_loc13_ = _loc11_[_loc12_]).var_1459 = var_1.mTimeThisTick - (_loc10_.var_1962 + 5000);
                     _loc12_++;
                  }
                  var_1.mAbilityBook.SetAbilities(_loc5_.var_90,class_14.var_478[_loc5_.abilityID]);
                  _loc8_ = (_loc7_ = this.var_395[param2].mMovieClip).getBounds(mWindow.mMovieClip);
                  var_1.screenHud.PlayPowerToHotbar(_loc8_.x,_loc8_.y,_loc5_,_loc3_);
               }
            }
         }
      }
      
      private function method_1378(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:uint = var_16 * const_65;
         var _loc5_:class_10 = this.var_841[param2 + _loc4_];
         var _loc6_:PowerType;
         if(!(_loc6_ = _loc3_.GetPowerFromAbilityType(_loc5_)))
         {
            return;
         }
         var _loc8_:MovieClip;
         var _loc7_:MovieClip;
         (_loc8_ = (_loc7_ = this.var_395[param2].mMovieClip).am_Selector).visible = true;
         var_1.screenHudTooltip.ShowSpellbookTooltip(_loc3_,_loc6_,_loc5_,681.4,614.5);
      }
      
      private function method_1516(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:MovieClip;
         (_loc4_ = this.var_395[param2].mMovieClip).am_Selector.visible = false;
         var_1.screenHudTooltip.HideTooltip();
      }
      
      public function LinkAbilityInChat(param1:class_10, param2:uint = 0) : void
      {
         var _loc5_:uint = 0;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_ || !param1)
         {
            return;
         }
         var _loc4_:PowerType = _loc3_.GetPowerFromAbilityType(param1);
         if(!param2)
         {
            _loc5_ = uint(var_1.mAbilityBook.mAbilityListTrainedRanks[param1.abilityID]);
         }
         else
         {
            _loc5_ = param2;
         }
         _loc5_ = Math.max(_loc5_,1);
         var _loc6_:* = (_loc6_ = (_loc6_ = (_loc6_ = "{" + class_127.const_8[5]) + (":" + param1.abilityName)) + (":" + _loc5_.toString())) + "}";
         var_1.screenChat.AddItemInfoToChatEntry("[" + _loc4_.displayName + " - Rank " + _loc5_.toString() + "]",_loc6_);
      }
      
      public function GetAbilityTypeFromPowerType(param1:PowerType) : class_10
      {
         var _loc2_:* = param1.basePowerName;
         if(param1.var_7)
         {
            _loc2_ += param1.var_7;
         }
         else
         {
            _loc2_ += "1";
         }
         return class_14.var_1101[_loc2_];
      }
   }
}
