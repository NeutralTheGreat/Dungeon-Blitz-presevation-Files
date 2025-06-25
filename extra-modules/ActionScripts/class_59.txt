package
{
   public class class_59 extends class_32
   {
       
      
      internal var var_2188:Boolean;
      
      internal var var_1942:class_33;
      
      public function class_59(param1:Game)
      {
         super(param1,"a_LevelUp",null);
         var_45 = "FadeIn";
         var_87 = "Break";
         var_92 = 1600;
         var_15 = true;
         mbHideOnClear = false;
         var_101 = false;
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_1942 = method_1(var_2.am_Break);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1942 = null;
      }
      
      public function OnInitDisplay() : void
      {
         this.var_2188 = true;
         this.var_1942.PlayAnimation("Ready");
      }
      
      override public function OnTickScreen() : void
      {
         var _loc1_:class_139 = null;
         var _loc2_:String = null;
         if(this.var_2188)
         {
            _loc1_ = mWindow.mActiveTimeline;
            _loc2_ = !!_loc1_ ? _loc1_.name : null;
            if(_loc2_ == var_87)
            {
               this.var_1942.PlayAnimation("Break");
               this.var_2188 = false;
            }
         }
      }
   }
}
