package
{
   public class class_98 extends class_32
   {
       
      
      internal var var_863:uint;
      
      public function class_98(param1:Game)
      {
         super(param1,"a_QuestItemFloaterSimple","am_Panel");
         var_15 = true;
         var_45 = "FadeIn";
         var_87 = "FadeOut";
         var_92 = 1500;
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
         MathUtil.method_2(var_2.am_Name,_loc1_.var_2869);
         method_12(var_2.am_IconHolder,_loc1_.var_2319);
      }
      
      public function OnInitDisplay(param1:uint) : void
      {
         this.var_863 = param1;
      }
   }
}
