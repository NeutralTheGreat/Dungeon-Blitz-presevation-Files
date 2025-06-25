package
{
   import flash.events.MouseEvent;
   
   public class class_125 extends class_32
   {
       
      
      public function class_125(param1:Game)
      {
         super(param1,"a_ScreenRespecConfirm","am_Panel");
         var_15 = true;
      }
      
      override public function OnCreateScreen() : void
      {
         method_10(var_2.am_Yes,this.method_1594);
         method_10(var_2.am_No,this.method_1540);
         method_23(var_2.am_Close);
      }
      
      override public function OnRefreshScreen() : void
      {
         MathUtil.method_2(var_2.am_RespecCount,"x" + 1);
      }
      
      private function method_1594(param1:MouseEvent) : void
      {
         var_1.screenSigil.RespecTalentTree();
         Hide();
      }
      
      private function method_1540(param1:MouseEvent) : void
      {
         Hide();
      }
   }
}
