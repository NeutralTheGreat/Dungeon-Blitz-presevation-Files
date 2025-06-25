package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   
   public class class_95 extends class_32
   {
      
      private static const const_400:uint = 3000;
      
      private static const const_826:uint = 8000;
      
      private static const const_615:uint = 20000;
      
      private static const const_1017:uint = const_826 - const_400;
      
      private static const const_1188:uint = const_615 - const_400;
      
      public static const const_837:uint = 300;
       
      
      public var var_787:uint;
      
      private var var_190:class_33;
      
      private var var_1599:class_33;
      
      private var var_1534:class_33;
      
      private var mBurst1:class_33;
      
      private var mBurst2:class_33;
      
      private var var_1739:class_33;
      
      private var var_1117:class_33;
      
      private var var_2171:class_33;
      
      private var var_2439:class_138;
      
      public function class_95(param1:Game)
      {
         super(param1,"a_RespawnWindow","am_RespawnPanel");
         var_15 = true;
         mbHideOnClear = false;
         var_45 = "FadeIn";
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_1599 = method_5(var_2.am_Respawn,this.method_1792);
         this.var_1534 = method_5(var_2.am_ReviveAtPortal,this.method_1272);
         this.mBurst1 = method_1(var_2.am_Burst1);
         this.mBurst2 = method_1(var_2.am_Burst2);
         this.var_1739 = method_1(var_2.am_Hearts);
         this.var_190 = method_17(var_2.am_ReviveProgress,"Progress",0);
         var _loc1_:MovieClip = var_2.am_ResPotionWrapper;
         this.var_1117 = method_1(_loc1_);
         this.var_2171 = method_5(_loc1_.am_Drink,this.method_1215);
         this.var_2439 = method_21(_loc1_.am_Count);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1599 = null;
         this.var_1534 = null;
         this.mBurst1 = null;
         this.mBurst2 = null;
         this.var_1739 = null;
         this.var_190 = null;
         this.var_1117 = null;
         this.var_2171 = null;
         this.var_2439 = null;
      }
      
      private function method_1792(param1:MouseEvent) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_ || _loc2_.entState != Entity.const_6)
         {
            return;
         }
         var _loc3_:uint = !!var_1.InHardMode() ? const_615 : const_826;
         var _loc4_:int;
         if((_loc4_ = var_1.mTimeThisTick - _loc2_.var_217) < _loc3_)
         {
            return;
         }
         if(!var_1.CanSendPacket() || Boolean(this.var_787))
         {
            return;
         }
         var _loc5_:Packet;
         (_loc5_ = new Packet(LinkUpdater.PKTTYPE_REQUEST_RESPAWN)).method_15(false);
         var_1.serverConn.SendPacket(_loc5_);
         this.var_787 = var_1.mTimeThisTick;
         method_265("Collapse");
      }
      
      public function method_1215(param1:MouseEvent) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_ || _loc2_.entState != Entity.const_6)
         {
            return;
         }
         if(!var_1.mOwnedConsumables[class_3.var_1959] || var_1.mOwnedConsumables[class_3.var_1959].stackCount == 0)
         {
            var_1.screenChat.ReadUnsafeStatusText("You are out of resurrection potions.");
            return;
         }
         if(!var_1.CanSendPacket() || Boolean(this.var_787))
         {
            return;
         }
         var _loc3_:Packet = new Packet(LinkUpdater.PKTTYPE_REQUEST_RESPAWN);
         _loc3_.method_15(true);
         var_1.serverConn.SendPacket(_loc3_);
         this.var_787 = var_1.mTimeThisTick;
         method_265("Collapse");
      }
      
      private function method_1272(param1:MouseEvent) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_ || _loc2_.entState != Entity.const_6)
         {
            return;
         }
         var _loc3_:Door = var_1.level.GetDoorFromID(const_837);
         if(!_loc3_)
         {
            return;
         }
         var_1.OpenDoor(_loc3_);
      }
      
      public function OnInitDisplay() : void
      {
         var _loc1_:class_3 = null;
         var _loc2_:uint = 0;
         this.var_190.BeginHealthMode("Progress",0);
         this.var_1599.DisableButton("Inactive");
         this.mBurst1.ClearAnimation();
         this.mBurst2.ClearAnimation();
         this.var_1739.PlayAnimation("Off");
         if(var_1.level.internalName == "BridgeTownHard")
         {
            this.var_1534.Show();
            this.var_1117.Hide();
         }
         else if(!var_1.level.bInstanced)
         {
            this.var_1534.Hide();
            this.var_1117.Hide();
         }
         else
         {
            this.var_1534.Hide();
            this.var_1117.Show();
            _loc1_ = class_14.var_303["Resurrection"];
            _loc2_ = 0;
            if(var_1.mOwnedConsumables[_loc1_.consumableID])
            {
               _loc2_ = uint(var_1.mOwnedConsumables[_loc1_.consumableID].stackCount);
            }
            if(!_loc2_)
            {
               this.var_1117.Hide();
            }
            else
            {
               this.var_2171.EnableButton();
               this.var_2439.SetText("x" + _loc2_);
            }
         }
      }
      
      override public function OnTickScreen() : void
      {
         var _loc1_:Entity = var_1.clientEnt;
         var _loc2_:uint = !!_loc1_ ? uint(var_1.mTimeThisTick - _loc1_.var_217) : 0;
         var _loc3_:uint = !!var_1.InHardMode() ? const_1188 : const_1017;
         var _loc4_:Number;
         if((_loc4_ = (_loc2_ - const_400) / _loc3_) >= 1 && this.var_1599.var_1027)
         {
            this.var_190.PlayAnimation("Glow",class_33.const_36);
            this.mBurst1.PlayAnimation("Emit");
            this.mBurst2.PlayAnimation("Emit");
            this.var_1599.EnableButton();
            this.var_1739.PlayAnimation("On");
         }
         this.var_190.mHealthPerc = _loc4_;
      }
      
      public function method_1865() : void
      {
         var _loc1_:Entity = var_1.clientEnt;
         var _loc2_:Boolean = Boolean(_loc1_) && _loc1_.entState == Entity.const_6;
         var _loc3_:Boolean = _loc2_ && !this.var_787 && var_1.mTimeThisTick - _loc1_.var_217 >= const_400;
         if(_loc3_)
         {
            if(!mbVisible)
            {
               Display();
            }
         }
         else if(mbVisible)
         {
            Hide();
         }
      }
   }
}
