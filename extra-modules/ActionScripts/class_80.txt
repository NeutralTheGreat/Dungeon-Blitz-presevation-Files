package
{
   import flash.events.MouseEvent;
   
   public class class_80 extends class_32
   {
       
      
      internal var var_2833:uint;
      
      internal var var_2673:String;
      
      internal var var_2518:String;
      
      internal var var_700:class_33;
      
      public function class_80(param1:Game)
      {
         super(param1,"a_DialogBox",null);
         var_15 = true;
         mbHideOnClear = false;
      }
      
      override public function OnCreateScreen() : void
      {
         method_10(var_2.am_YesButton,this.method_1080);
         method_10(var_2.am_NoButton,this.method_1167);
         this.var_700 = method_5(var_2.am_CheckBox,this.method_1850);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_700 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         MathUtil.method_2(var_2.am_DialogText,this.var_2673);
         this.var_700.mMovieClip.am_CheckMark.visible = var_1.bIgnoreStrangerInvites;
      }
      
      public function OnInitDisplay(param1:String, param2:uint, param3:String) : void
      {
         this.var_2833 = param2;
         this.var_2673 = param1;
         this.var_2518 = param3;
      }
      
      private function method_967(param1:Boolean) : void
      {
         if(!var_1.CanSendPacket())
         {
            return;
         }
         var _loc2_:Packet = new Packet(LinkUpdater.PKTTYPE_QUERYMESSAGE_ANSWER);
         _loc2_.method_9(this.var_2833);
         _loc2_.method_26(this.var_2518);
         _loc2_.method_15(param1);
         var_1.serverConn.SendPacket(_loc2_);
      }
      
      private function method_1167(param1:MouseEvent) : void
      {
         this.method_967(false);
         Hide();
      }
      
      private function method_1080(param1:MouseEvent) : void
      {
         this.method_967(true);
         Hide();
      }
      
      public function method_1850(param1:MouseEvent) : void
      {
         var_1.bIgnoreStrangerInvites = !var_1.bIgnoreStrangerInvites;
         this.var_700.mMovieClip.am_CheckMark.visible = var_1.bIgnoreStrangerInvites;
      }
   }
}
