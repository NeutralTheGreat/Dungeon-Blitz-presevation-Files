package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   
   public class class_85 extends class_32
   {
      
      private static const const_757:Array = [50000,375000,625000];
       
      
      private var var_895:Vector.<class_33>;
      
      private var var_869:Vector.<class_138>;
      
      private var var_2519:class_33;
      
      private var var_1800:class_138;
      
      public function class_85(param1:Game)
      {
         super(param1,"a_ScreenLockBoxBuyTroves",null);
         var_15 = true;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = class_131.const_576.length;
         this.var_895 = new Vector.<class_33>(_loc2_,true);
         _loc1_ = 0;
         while(_loc1_ < _loc2_)
         {
            this.var_895[_loc1_] = method_117(var_2["am_BuyTroves" + _loc1_] as MovieClip,_loc1_,this.method_994);
            _loc1_++;
         }
         this.var_2519 = method_1(var_2.am_PanelBase);
         this.var_1800 = method_21(var_2.am_HeaderMsg);
         this.var_869 = new Vector.<class_138>(_loc2_,true);
         _loc1_ = 0;
         while(_loc1_ < _loc2_)
         {
            this.var_869[_loc1_] = method_21(var_2["am_Cost" + _loc1_] as TextField);
            _loc1_++;
         }
         method_23(var_2.am_Close);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_895 = null;
         this.var_2519 = null;
         this.var_1800 = null;
         this.var_869 = null;
      }
      
      public function OnInitDisplay(param1:Boolean) : void
      {
         if(param1)
         {
            this.var_1800.SetText("YOU RAN OUT OF TREASURE TROVES!");
         }
         else
         {
            this.var_1800.SetText("BUY TREASURE TROVE?");
         }
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:Entity = var_1.clientEnt;
         var _loc2_:uint = const_757.length;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            if(_loc1_.currGold < const_757[_loc3_])
            {
               this.var_895[_loc3_].DisableButton("Ready");
               this.var_895[_loc3_].mMovieClip.filters = [class_50.const_112];
               MathUtil.method_8(this.var_869[_loc3_].mTextField,this.var_869[_loc3_].mTextField.text,ScreenArmory.const_137,ScreenArmory.const_169);
            }
            else
            {
               this.var_895[_loc3_].EnableButton();
               this.var_895[_loc3_].mMovieClip.filters = [];
               MathUtil.method_8(this.var_869[_loc3_].mTextField,this.var_869[_loc3_].mTextField.text,ScreenArmory.const_24,ScreenArmory.const_455);
            }
            _loc3_++;
         }
      }
      
      private function method_994(param1:MouseEvent, param2:uint) : void
      {
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(param2 >= class_131.const_576.length)
         {
            return;
         }
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:uint = class_131.const_576[param2];
         var _loc5_:uint = class_131.const_1179[param2];
         if(_loc3_.currGold < _loc5_)
         {
            return;
         }
         var _loc6_:Packet;
         (_loc6_ = new Packet(LinkUpdater.const_1164)).method_20(class_15.const_300,var_1.mLockboxData.mLockboxID);
         _loc6_.method_9(param2);
         var_1.serverConn.SendPacket(_loc6_);
         Hide();
      }
   }
}
