package
{
   public class class_106 extends class_32
   {
       
      
      internal var var_2662:uint;
      
      public function class_106(param1:Game)
      {
         super(param1,"a_MountFloaterSimple","am_Panel");
         var_15 = true;
         var_45 = "FadeIn";
         var_87 = "FadeOut";
         var_92 = 1500;
         var_112 = true;
         var_101 = false;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:class_20 = class_14.var_464[this.var_2662];
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:PowerType = PowerType.var_440;
         MathUtil.method_2(var_2.am_Name,_loc1_.displayName);
         var _loc3_:String = "a_StoreIcon" + _loc2_.iconName.replace("a_MountIcon_","");
         method_12(var_2.am_IconHolder,_loc3_);
      }
      
      public function OnInitDisplay(param1:uint) : void
      {
         this.var_2662 = param1;
      }
   }
}
