package
{
   public class class_47 extends class_32
   {
       
      
      internal var var_2805:uint;
      
      public function class_47(param1:Game)
      {
         super(param1,"a_MaterialFloaterSimple","am_Panel");
         var_15 = true;
         var_45 = "FadeIn";
         var_87 = "FadeOut";
         var_92 = 1500;
         var_112 = true;
         var_101 = false;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:class_8 = class_14.var_629[this.var_2805];
         if(!_loc1_)
         {
            return;
         }
         if(_loc1_.var_139 == "M")
         {
            MathUtil.method_8(var_2.am_Name,_loc1_.displayName,ScreenArmory.const_24);
         }
         else if(_loc1_.var_139 == "R")
         {
            MathUtil.method_8(var_2.am_Name,_loc1_.displayName,ScreenArmory.const_22);
         }
         else if(_loc1_.var_139 == "L")
         {
            MathUtil.method_8(var_2.am_Name,_loc1_.displayName,ScreenArmory.const_23);
         }
         method_12(var_2.am_IconHolder,_loc1_.iconName);
      }
      
      public function OnInitDisplay(param1:uint) : void
      {
         this.var_2805 = param1;
      }
   }
}
