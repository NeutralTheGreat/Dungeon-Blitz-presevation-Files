package
{
   import flash.events.MouseEvent;
   import flash.text.TextField;
   
   public class class_96 extends class_32
   {
      
      private static const const_1387:Number = 1 / (20 * 60);
      
      private static const const_623:uint = 180;
       
      
      private var var_1045:Boolean;
      
      private var var_2339:class_9;
      
      private var var_2162:TextField;
      
      private var var_190:class_33;
      
      private var var_1891:class_33;
      
      private var var_1476:class_33;
      
      private var var_1960:class_33;
      
      private var var_1720:class_33;
      
      private var var_449:class_33;
      
      private var var_1393:class_33;
      
      private var var_2312:class_33;
      
      public function class_96(param1:Game)
      {
         super(param1,"a_ScreenUpgrading","am_Panel");
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_1891 = method_1(var_2.am_UpgradeInfo);
         this.var_2162 = var_2.am_UpgradePanel.am_Idols;
         this.var_1476 = method_1(var_2.am_CancelPanel);
         method_10(var_2.am_CancelPanel.am_NeverMind,this.method_650);
         method_10(var_2.am_CancelPanel.am_CancelTraining,this.CancelUpgrade);
         this.var_1720 = method_10(var_2.am_UpgradePanel.am_UpgradeNow,this.method_1621);
         this.var_190 = method_17(this.var_1891.mMovieClip.am_Progress,"Progress",0);
         this.var_1960 = method_5(var_2.am_Cancel,this.method_650);
         method_23(var_2.am_Close);
         this.var_2312 = method_1(var_2.am_TrainingIcon);
         this.var_1393 = method_1(var_2.am_ButtonCover);
         this.var_449 = method_1(var_2.am_WarningAnim);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1476 = null;
         this.var_190 = null;
         this.var_1891 = null;
         this.var_1960 = null;
         this.var_2339 = null;
         this.var_2162 = null;
         this.var_1720 = null;
         this.var_449 = null;
         this.var_1393 = null;
         this.var_2312 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         if(this.var_1045)
         {
            this.var_1476.Show();
            this.var_1960.Hide();
            this.var_449.Show();
            if(this.var_449.var_175 == 1)
            {
               this.var_449.PlayAnimation("Warning");
            }
         }
         else
         {
            this.var_1476.Hide();
            this.var_1960.Show();
            this.var_449.PlayAnimation("Ready");
            this.var_449.Hide();
         }
         this.var_1720.EnableButton();
      }
      
      override public function OnTickScreen() : void
      {
         var _loc1_:int = int(var_1.mBuildingInfo.mWorkerEndtime);
         var _loc2_:int = _loc1_ - var_1.mServerGameTime;
         if(_loc2_ < 0)
         {
            _loc2_ = 0;
         }
         var _loc3_:int = int(this.var_2339.upgradeTime);
         var _loc4_:Number = 1 - _loc2_ / _loc3_;
         this.var_190.mHealthPerc = _loc4_;
         var _loc5_:uint = uint(_loc2_);
         MathUtil.method_2(this.var_190.mMovieClip.am_Time,Game.method_70(_loc5_));
         if(!this.var_1393.mbVisible)
         {
            if(_loc5_ <= const_623)
            {
               this.var_1393.Show();
            }
         }
         else if(_loc5_ > const_623)
         {
            this.var_1393.Hide();
         }
         if(!this.var_1045)
         {
            MathUtil.method_2(this.var_2162,Game.method_229(_loc5_));
         }
      }
      
      public function OnInitDisplay(param1:class_9) : void
      {
         if(!param1)
         {
            Hide();
         }
         method_12(this.var_2312.mMovieClip,param1.var_1861);
         MathUtil.method_2(this.var_1891.mMovieClip.am_Name,param1.displayName);
         this.var_2339 = param1;
         this.var_1045 = false;
      }
      
      private function method_650(param1:MouseEvent) : void
      {
         this.var_1045 = !this.var_1045;
         Refresh();
      }
      
      private function CancelUpgrade(param1:MouseEvent) : void
      {
         var_1.mBuildingInfo.CancelUpgrade();
         Hide();
      }
      
      private function method_1621(param1:MouseEvent) : void
      {
         if(!var_1.CanSendPacket())
         {
            return;
         }
         var _loc2_:int = var_1.mBuildingInfo.mWorkerEndtime - var_1.mServerGameTime;
         var _loc3_:uint = Game.method_257(_loc2_);
         if(var_1.mMammothIdols < _loc3_)
         {
            var_1.screenBuyIdols.Display(_loc3_ - var_1.mMammothIdols);
            return;
         }
         this.var_1720.DisableButton("Inactive");
         var _loc4_:Packet;
         (_loc4_ = new Packet(LinkUpdater.const_1187)).method_9(_loc3_);
         var_1.serverConn.SendPacket(_loc4_);
      }
   }
}
