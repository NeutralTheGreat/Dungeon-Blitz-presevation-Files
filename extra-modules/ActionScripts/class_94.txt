package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.ui.Keyboard;
   
   public class class_94
   {
       
      
      internal var var_1:Game;
      
      internal var var_1749:Boolean;
      
      internal var var_88:MovieClip;
      
      internal var var_966:class_33 = null;
      
      public function class_94(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1258() : void
      {
         if(this.var_88)
         {
            this.var_966.DestroyUIMovieClip();
            this.var_966 = null;
         }
         if(Boolean(this.var_88) && Boolean(this.var_88.parent))
         {
            this.var_88.parent.removeChild(this.var_88);
         }
         this.var_88 = null;
         this.var_1 = null;
      }
      
      public function Hide() : void
      {
         this.var_1.method_158(this.var_88);
      }
      
      public function method_40() : Boolean
      {
         return Boolean(this.var_88) && this.var_88.visible;
      }
      
      public function method_54(param1:int) : Boolean
      {
         if(this.method_40() && this.var_1749)
         {
            if(param1 == Keyboard.ESCAPE || param1 == Keyboard.ENTER)
            {
               this.Hide();
               return true;
            }
         }
         return false;
      }
      
      public function method_1983() : void
      {
         if(!this.var_88 || !this.var_88.visible)
         {
            return;
         }
         this.var_966.TickMovieClip();
      }
      
      public function method_71(param1:String, param2:Boolean = false) : void
      {
         if(!this.var_88)
         {
            this.var_88 = class_4.method_16("a_LoginInfoSplash",true);
            this.var_88.x = 0.5 * (Camera.SCREEN_WIDTH - this.var_88.width);
            this.var_88.y = 0.5 * (Camera.SCREEN_HEIGHT - this.var_88.height);
            this.var_88.visible = false;
            this.var_966 = new class_33(this.var_1,this.var_88.am_StatusClose);
            this.var_966.BecomeButton("Ready","Over","Click",this.method_1361,false);
         }
         if(!this.var_88.visible)
         {
            this.var_88.visible = true;
            this.var_1.var_89.addChild(this.var_88);
         }
         this.var_1749 = param2;
         if(this.var_1749)
         {
            this.var_966.Show();
         }
         else
         {
            this.var_966.Hide();
         }
         MathUtil.method_2(this.var_88.am_Status,param1);
      }
      
      public function method_1361(param1:MouseEvent) : void
      {
         if(this.method_40() && this.var_1749)
         {
            this.Hide();
         }
      }
   }
}
