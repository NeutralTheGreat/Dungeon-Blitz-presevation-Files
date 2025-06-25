package
{
   public class class_74 extends class_32
   {
       
      
      internal var var_863:uint;
      
      public function class_74(param1:Game)
      {
         super(param1,"a_CompleteQuestFloater","am_Panel");
         var_15 = true;
         var_45 = "FadeIn";
         var_87 = "FadeOut";
         var_92 = 1000;
         var_112 = true;
         var_101 = false;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:class_13 = class_14.var_238[this.var_863];
         if(!_loc1_)
         {
            return;
         }
         MathUtil.method_2(var_2.am_Name,_loc1_.displayName);
         MathUtil.method_2(var_2.am_Gold,!!_loc1_.var_1572 ? String(_loc1_.var_1572) : "");
         MathUtil.method_2(var_2.am_Xp,!!_loc1_.var_1577 ? String(_loc1_.var_1577) : "");
      }
      
      public function OnInitDisplay(param1:uint) : void
      {
         this.var_863 = param1;
      }
   }
}
