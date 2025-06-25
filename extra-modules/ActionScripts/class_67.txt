package
{
   import flash.events.MouseEvent;
   import flash.external.ExternalInterface;
   import flash.net.URLRequest;
   import flash.net.navigateToURL;
   
   public class class_67 extends class_32
   {
       
      
      private var var_2709:Boolean;
      
      public function class_67(param1:Game)
      {
         super(param1,"a_CrashWindow",null);
         var_15 = true;
         mbHideOnClear = false;
      }
      
      override public function OnCreateScreen() : void
      {
         method_5(var_2.am_Refresh,this.method_1866);
      }
      
      override public function OnRefreshScreen() : void
      {
         if(this.var_2709)
         {
            MathUtil.method_2(var_2.am_Title,"Lost Connection");
            MathUtil.method_2(var_2.am_Text,"Connection to the\nserver has been lost!");
         }
         else
         {
            MathUtil.method_2(var_2.am_Title,"Client Error");
            MathUtil.method_2(var_2.am_Text,"How embarrassing,\nI swear this never happens!");
         }
      }
      
      public function OnInitDisplay(param1:Boolean = false) : void
      {
         this.var_2709 = param1;
      }
      
      private function method_1866(param1:MouseEvent) : void
      {
         var _loc2_:String = "http://www.dungeonblitz.com";
         if(var_1.clientFacebookID)
         {
            _loc2_ = "http://apps.facebook.com/dungeonblitz/";
         }
         else if(var_1.clientKongID)
         {
            _loc2_ = "http://www.kongregate.com/games/BlueMammoth/dungeon-blitz";
         }
         navigateToURL(new URLRequest(_loc2_),"_top");
         if(ExternalInterface.available)
         {
            ExternalInterface.call("JSRefreshGame");
         }
      }
   }
}
