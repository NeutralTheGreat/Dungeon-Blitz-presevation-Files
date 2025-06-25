package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   
   public class class_79 extends class_32
   {
      
      private static const const_292:uint = 4000;
      
      private static const const_478:uint = 2000;
       
      
      internal var var_1926:class_33;
      
      internal var var_764:MovieClip;
      
      internal var var_1906:uint;
      
      internal var var_1811:class_33;
      
      internal var var_1254:class_33;
      
      internal var var_1103:class_33;
      
      internal var var_1110:class_33;
      
      internal var var_1907:class_33;
      
      internal var var_1747:class_33;
      
      internal var var_1661:class_33;
      
      internal var var_1992:class_33;
      
      internal var var_1956:class_33;
      
      internal var var_1993:class_33;
      
      internal var mSpellbookIcon:class_33;
      
      public function class_79(param1:Game)
      {
         super(param1,"a_HudTop",null);
         var_15 = true;
         mbHideOnClear = false;
      }
      
      override public function OnCreateScreen() : void
      {
         var_2.am_SocialNotify.visible = false;
         var_2.am_SocialNotify.mouseEnabled = false;
         var_2.am_SocialNotify.mouseChildren = false;
         var_2.am_SocialCount.mouseEnabled = false;
         var_2.am_SocialCount.mouseChildren = false;
         this.var_1926 = method_5(var_2.am_Inventory,this.method_1511);
         this.var_764 = var_2.am_GearNotify;
         this.var_764.visible = false;
         this.var_764.mouseEnabled = false;
         this.var_764.mouseChildren = false;
         this.var_1811 = method_5(var_2.am_Sigil,this.method_1506);
         method_5(var_2.am_Social,this.method_1220);
         this.mSpellbookIcon = method_5(var_2.am_Spellbook,this.method_1870);
         this.var_1254 = method_5(var_2.am_GoHome,this.method_1357);
         this.var_1907 = method_17(this.var_1254.mMovieClip.am_Cooldown,"Cooldown",0);
         this.var_1103 = method_5(var_2.am_GoLeave,this.method_1982);
         this.var_1747 = method_17(this.var_1103.mMovieClip.am_Cooldown,"Cooldown",0);
         this.var_1110 = method_5(var_2.am_GoLeaveDungeon,this.method_1446);
         this.var_1661 = method_17(this.var_1110.mMovieClip.am_Cooldown,"Cooldown",0);
         this.var_1992 = method_5(var_2.am_LeaveGroup,this.method_1498);
         this.var_1956 = method_5(var_2.am_GroupUnlocked,this.method_1031);
         this.var_1993 = method_5(var_2.am_GroupLocked,this.method_1364);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1926 = null;
         this.var_764 = null;
         this.mSpellbookIcon = null;
         this.var_1811 = null;
         this.var_1254 = null;
         this.var_1103 = null;
         this.var_1110 = null;
         this.var_1907 = null;
         this.var_1747 = null;
         this.var_1661 = null;
         this.var_1992 = null;
         this.var_1956 = null;
         this.var_1993 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         this.var_1254.Hide();
         this.var_1103.Hide();
         this.var_1110.Hide();
         this.var_1907.Hide();
         this.var_1747.Hide();
         this.var_1661.Hide();
         var _loc1_:Level = var_1.level;
         var _loc3_:String = _loc1_.internalName;
         var _loc5_:Boolean;
         var _loc4_:Boolean;
         if((_loc5_ = !(_loc4_ = Boolean(_loc3_) && !_loc3_.indexOf("CraftTown")) && _loc1_.bInstanced) && !_loc4_)
         {
            if(_loc3_ != "TutorialBoat")
            {
               this.var_1110.Show();
            }
         }
         else if(_loc4_)
         {
            this.var_1103.Show();
         }
         else if(Boolean(var_1.mMissionInfoList[class_13.const_118]) || _loc3_ != "NewbieRoad")
         {
            this.var_1254.Show();
         }
         if(Boolean(var_1.clientEnt) && Boolean(var_1.clientEnt.mMasterClass))
         {
            this.var_1811.Show();
         }
         else
         {
            this.var_1811.Hide();
         }
         this.var_1992.Hide();
         this.var_1956.Hide();
         this.var_1993.Hide();
         if(Boolean(var_1.groupmates) && Boolean(var_1.groupmates.length))
         {
            this.var_1992.Show();
            if(var_1.bAmGroupLeader)
            {
               if(var_1.bGroupIsLocked)
               {
                  this.var_1993.Show();
               }
               else
               {
                  this.var_1956.Show();
               }
            }
         }
      }
      
      override public function OnTickScreen() : void
      {
         var _loc4_:Number = NaN;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:uint = _loc1_.combatState.method_1503();
         var _loc3_:class_33 = null;
         if(this.var_1254.mbVisible)
         {
            _loc3_ = this.var_1907;
         }
         else if(this.var_1103.mbVisible)
         {
            _loc3_ = this.var_1747;
         }
         else if(this.var_1110.mbVisible)
         {
            _loc3_ = this.var_1661;
         }
         if(_loc3_)
         {
            if(_loc2_ < const_292)
            {
               _loc4_ = 0;
               if(_loc2_ > const_478)
               {
                  _loc4_ = (_loc2_ - const_478) / (const_292 - const_478);
               }
               _loc3_.Show();
               _loc3_.mHealthPerc = _loc4_;
            }
            else
            {
               _loc3_.Hide();
            }
         }
      }
      
      private function method_1506(param1:MouseEvent) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         if(!var_1.screenSigil.mbVisible && Boolean(var_1.bWaitingForChangeMasterClassResponse))
         {
            return;
         }
         if(_loc2_.mMasterClass)
         {
            var_1.screenSigil.Toggle(_loc2_.mMasterClass);
         }
      }
      
      public function method_1730(param1:Vector.<Friend>) : void
      {
         var _loc3_:Friend = null;
         if(!var_2)
         {
            return;
         }
         var _loc2_:int = 0;
         for each(_loc3_ in param1)
         {
            if(_loc3_.bOnline || _loc3_.var_276)
            {
               _loc2_++;
            }
         }
         MathUtil.method_2(var_2.am_SocialCount.am_Text,String(_loc2_));
      }
      
      public function method_1660() : void
      {
         if(!var_2)
         {
            return;
         }
         ++this.var_1906;
         this.var_764.visible = true;
         MathUtil.method_2(this.var_764.am_Text,String(this.var_1906));
         this.var_1926.PlayAnimation("New",class_33.const_36);
      }
      
      public function ResetNewInventoryCount() : void
      {
         this.var_1906 = 0;
         this.var_764.visible = false;
         this.var_1926.PlayAnimation("Ready");
      }
      
      private function method_1511(param1:MouseEvent) : void
      {
         var_1.screenArmory.Toggle();
      }
      
      private function method_1220(param1:MouseEvent) : void
      {
         var_1.screenFriend.Toggle();
      }
      
      private function method_1870(param1:MouseEvent) : void
      {
         if(!var_1.clientEnt)
         {
            return;
         }
         var_1.screenSpellbook.Toggle(var_1.clientEnt.entType.className);
      }
      
      private function method_1357(param1:MouseEvent) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(Boolean(_loc2_) && _loc2_.combatState.method_123(const_292))
         {
            var_1.OpenDoor(new Door("GoHome",0,0,null,class_11.const_759,null));
         }
      }
      
      private function method_1446(param1:MouseEvent) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         var _loc3_:Level = var_1.level;
         if(!_loc3_.internalName)
         {
            return;
         }
         var _loc4_:*;
         var _loc5_:Boolean = !(_loc4_ = !_loc3_.internalName.indexOf("CraftTown")) && _loc3_.bInstanced;
         if(_loc2_ && _loc2_.combatState.method_123(const_292) && _loc5_)
         {
            var_1.OpenDoor(new Door("ExitDungeon",0,0,null,0,null));
         }
      }
      
      private function method_1982(param1:MouseEvent) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         var _loc3_:Level = var_1.level;
         if(!_loc3_.internalName)
         {
            return;
         }
         var _loc4_:*;
         var _loc5_:Boolean = !(_loc4_ = !_loc3_.internalName.indexOf("CraftTown")) && _loc3_.bInstanced;
         if(_loc2_ && _loc2_.combatState.method_123(const_292) && !_loc5_)
         {
            var_1.OpenDoor(new Door("LeaveHome",0,0,null,0,null));
         }
      }
      
      private function method_1498(param1:MouseEvent) : void
      {
         var_1.screenChat.TryToProcessChatAsLocalCommand("/Quit");
      }
      
      private function method_1031(param1:MouseEvent) : void
      {
         var_1.screenChat.TryToProcessChatAsLocalCommand("/Lock");
      }
      
      private function method_1364(param1:MouseEvent) : void
      {
         var_1.screenChat.TryToProcessChatAsLocalCommand("/Unlock");
      }
   }
}
