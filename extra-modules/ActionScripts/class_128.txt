package
{
   public class class_128 extends class_32
   {
       
      
      internal var var_2525:uint;
      
      public function class_128(param1:Game)
      {
         super(param1,"a_PetFloaterSimple","am_Panel");
         var_15 = true;
         var_45 = "FadeIn";
         var_87 = "FadeOut";
         var_92 = 1500;
         var_112 = true;
         var_101 = false;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:class_7 = class_14.var_224[this.var_2525];
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:PowerType = class_14.powerTypesDict[_loc1_.var_1138];
         if(!_loc2_)
         {
            return;
         }
         MathUtil.method_2(var_2.am_Name,_loc1_.displayName);
         var _loc3_:String = "a_StoreIcon" + _loc2_.iconName.replace("a_PetIcon_","");
         method_12(var_2.am_IconHolder,_loc3_);
      }
      
      public function OnInitDisplay(param1:uint) : void
      {
         this.var_2525 = param1;
      }
   }
}
