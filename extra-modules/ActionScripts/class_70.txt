package
{
   import flash.events.MouseEvent;
   
   public class class_70 extends class_32
   {
       
      
      private var var_1652:class_33;
      
      private var var_1928:class_33;
      
      private var var_2942:class_33;
      
      private var var_2597:class_33;
      
      private var var_2483:class_33;
      
      private var var_1795:class_138;
      
      private var var_1761:class_138;
      
      private var var_2612:class_33;
      
      private var var_2651:class_33;
      
      private var var_1619:class_33;
      
      public var mPotionContainer:class_33;
      
      private var var_706:class_138;
      
      private var var_2916:uint;
      
      private var var_2902:uint;
      
      public function class_70(param1:Game)
      {
         super(param1,"a_HudTopRight",null);
         var_15 = true;
         mbHideOnClear = false;
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_2483 = method_5(var_2.am_Menu,this.method_1417);
         this.var_1652 = method_5(var_2.am_SoundOn,this.method_1222);
         this.var_1928 = method_5(var_2.am_SoundOff,this.method_1183);
         this.var_2942 = method_5(var_2.am_AddIdols,this.method_1639);
         this.var_2597 = method_5(var_2.am_Tutorial,this.method_1608);
         this.var_1795 = method_92(var_2.am_Gold);
         this.var_1795.mTextField.mouseEnabled = false;
         this.var_1761 = method_92(var_2.am_Idols);
         this.var_1761.mTextField.mouseEnabled = false;
         this.var_2612 = method_5(var_2.am_IdolMatte,null,this.method_600,this.method_760);
         this.var_2651 = method_5(var_2.am_GoldMatte,null,this.method_600,this.method_760);
         this.mPotionContainer = method_5(var_2.am_PotionContainer,null,this.ShowPotionTooltip,this.HideTooltip);
         this.var_1619 = method_17(var_2.am_PotionContainer.am_PotionBattery,"Progress",0);
         this.var_706 = method_21(var_2.am_PotionContainer.am_PercentLeft);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1652 = null;
         this.var_1928 = null;
         this.var_1795 = null;
         this.var_1761 = null;
         this.var_2597 = null;
         this.var_2483 = null;
         this.mPotionContainer = null;
         this.var_1619 = null;
         this.var_706 = null;
         this.var_2612 = null;
         this.var_2651 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc3_:class_103 = null;
         if(SoundManager.var_804)
         {
            this.var_1652.Hide();
            this.var_1928.Show();
         }
         else
         {
            this.var_1652.Show();
            this.var_1928.Hide();
         }
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:class_3 = var_1.clientEnt.mCurrPotion;
         if(!_loc2_)
         {
            if(this.mPotionContainer.mbVisible)
            {
               this.mPotionContainer.Hide();
               this.var_1619.Hide();
               this.var_706.Hide();
            }
         }
         else
         {
            if(!this.mPotionContainer.mbVisible)
            {
               this.mPotionContainer.Show();
               this.var_1619.Show();
               this.var_706.Show();
            }
            _loc3_ = var_1.mOwnedConsumables[_loc2_.consumableID];
            if(_loc3_)
            {
               this.var_706.SetText(_loc3_.method_906() + "%");
            }
         }
      }
      
      public function OnInitDisplay(param1:Entity) : void
      {
         this.var_706.Hide();
         var _loc2_:class_3 = param1.mCurrPotion;
         if(_loc2_)
         {
            this.var_2916 = _loc2_.consumableID;
         }
         var _loc3_:class_3 = param1.mNextPotion;
         if(_loc3_)
         {
            this.var_2902 = _loc3_.consumableID;
         }
      }
      
      override public function OnTickScreen() : void
      {
         var _loc3_:uint = 0;
         var _loc4_:class_103 = null;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         if(!var_1.bSuppressGoldDisplay)
         {
            this.var_1795.var_213 = _loc1_.currGold;
         }
         this.var_1761.var_213 = var_1.mMammothIdols;
         var _loc2_:Number = 0;
         if(var_1.clientEnt.mCurrPotion)
         {
            _loc3_ = uint(var_1.clientEnt.mCurrPotion.consumableID);
            if(_loc4_ = var_1.mOwnedConsumables[_loc3_])
            {
               _loc2_ = _loc4_.method_578();
            }
            this.var_1619.mHealthPerc = _loc2_;
         }
      }
      
      private function method_1608(param1:MouseEvent) : void
      {
         var _loc2_:class_32 = null;
         var _loc3_:class_33 = null;
         for each(_loc2_ in var_1.mUIManager.mActiveScreens)
         {
            _loc3_ = _loc2_.var_656;
            if(_loc3_)
            {
               if(_loc3_.mbVisible)
               {
                  _loc3_.Hide();
                  break;
               }
               _loc3_.Show();
               break;
            }
         }
      }
      
      private function method_1639(param1:MouseEvent) : void
      {
         var_1.screenBuyIdols.Toggle(0);
      }
      
      private function method_1417(param1:MouseEvent) : void
      {
         var_1.screenMenu.Toggle();
      }
      
      private function method_1222(param1:MouseEvent) : void
      {
         SoundManager.method_401(true);
         var_1.StoreGameInfo();
         Refresh();
      }
      
      private function method_1183(param1:MouseEvent) : void
      {
         SoundManager.method_401(false);
         var_1.StoreGameInfo();
         Refresh();
      }
      
      private function ShowPotionTooltip(param1:MouseEvent) : void
      {
         if(!var_1.clientEnt)
         {
            return;
         }
         var _loc2_:class_3 = var_1.clientEnt.mCurrPotion;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:class_103 = var_1.mOwnedConsumables[_loc2_.consumableID];
         if(!_loc3_)
         {
            return;
         }
         if(!_loc3_.stackCount)
         {
            return;
         }
         this.var_706.Show();
         this.var_706.SetText(_loc3_.method_906() + "%");
         var _loc4_:class_3;
         var _loc5_:class_103 = !!(_loc4_ = var_1.clientEnt.mNextPotion) ? var_1.mOwnedConsumables[_loc4_.consumableID] : null;
         var_1.screenHudTooltip.ShowPotionTooltip(_loc2_,_loc5_,330,6);
      }
      
      private function HideTooltip(param1:MouseEvent) : void
      {
         var_1.screenHudTooltip.HideTooltip(true);
         this.var_706.Hide();
      }
      
      private function method_600(param1:MouseEvent) : void
      {
      }
      
      private function method_760(param1:MouseEvent) : void
      {
      }
   }
}
