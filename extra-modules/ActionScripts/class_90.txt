package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   
   public class class_90 extends class_32
   {
       
      
      private var var_895:Vector.<class_33>;
      
      private var var_2519:class_33;
      
      private var var_1800:class_138;
      
      public function class_90(param1:Game)
      {
         super(param1,"a_ScreenLockBoxBuyKeys",null);
         var_15 = true;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = class_131.const_356.length;
         this.var_895 = new Vector.<class_33>(_loc2_,true);
         _loc1_ = 0;
         while(_loc1_ < _loc2_)
         {
            this.var_895[_loc1_] = method_117(var_2["am_BuyKeys" + _loc1_] as MovieClip,_loc1_,this.method_994);
            _loc1_++;
         }
         this.var_2519 = method_1(var_2.am_PanelBase);
         this.var_1800 = method_21(var_2.am_HeaderMsg);
         method_23(var_2.am_Close);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_895 = null;
         this.var_2519 = null;
         this.var_1800 = null;
      }
      
      public function OnInitDisplay(param1:Boolean) : void
      {
         if(param1)
         {
            this.var_1800.SetText("YOU RAN OUT OF DRAGON KEYS!");
         }
         else
         {
            this.var_1800.SetText("BUY DRAGON KEYS?");
         }
      }
      
      private function method_994(param1:MouseEvent, param2:uint) : void
      {
         if(param2 >= class_131.const_356.length)
         {
            return;
         }
         var _loc3_:uint = class_131.const_356[param2];
         var _loc4_:uint = class_131.const_1059[param2];
         if(var_1.mMammothIdols < _loc4_)
         {
            var_1.screenBuyIdols.Display(_loc4_ - var_1.mMammothIdols,true);
            return;
         }
         var_1.mLockboxData.BuyLockboxKeys(param2);
         Hide();
      }
   }
}
