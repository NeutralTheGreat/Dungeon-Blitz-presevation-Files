package
{
   public class class_71
   {
       
      
      internal var var_1:Game;
      
      internal var var_146:class_33;
      
      internal var var_2153:Boolean = false;
      
      public function class_71(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1599() : void
      {
         if(this.var_146)
         {
            this.var_146.method_42();
            this.var_146.DestroyUIMovieClip();
            this.var_146 = null;
         }
         this.var_1 = null;
      }
      
      public function Hide() : void
      {
         if(this.var_146)
         {
            this.var_146.method_42();
         }
      }
      
      public function method_1156() : void
      {
         if(this.var_2153)
         {
            if(!this.var_146)
            {
               this.var_146 = new class_33(this.var_1,class_4.method_16("a_FocusLostSplash"));
               this.var_146.PlayAnimation("Ready");
               this.var_146.method_141(class_33.const_344);
            }
            if(this.var_146.var_387 & class_33.const_80)
            {
               this.var_146.PlayAnimation("Ready");
            }
            if(!this.var_146.mbVisible)
            {
               this.var_146.method_141(class_33.const_344);
            }
            this.var_146.TickMovieClip();
         }
         else if(Boolean(this.var_146) && this.var_146.mbVisible)
         {
            if(!(this.var_146.var_387 & class_33.const_80))
            {
               this.var_146.PlayAnimation("Ready",class_33.const_80);
            }
            if(this.var_146.mbCompleted)
            {
               this.var_146.method_42();
            }
            this.var_146.TickMovieClip();
         }
      }
   }
}
