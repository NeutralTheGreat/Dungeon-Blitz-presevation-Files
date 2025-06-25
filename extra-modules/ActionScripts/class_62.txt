package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.utils.Dictionary;
   
   public class class_62 extends class_32
   {
       
      
      internal var var_1120:Dictionary;
      
      internal var var_633:class_33;
      
      internal var var_2202:String;
      
      public function class_62(param1:Game)
      {
         super(param1,"a_TutorialWalkthrough","am_Holder");
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:String = null;
         var _loc2_:MovieClip = null;
         var _loc3_:MovieClip = null;
         this.var_1120 = new Dictionary();
         while(var_2.numChildren)
         {
            _loc2_ = var_2.removeChildAt(0) as MovieClip;
            if(_loc2_)
            {
               _loc1_ = _loc2_.name;
               if(_loc1_)
               {
                  this.var_1120[_loc1_] = method_1(_loc2_);
                  _loc3_ = _loc2_.am_Panel;
                  _loc3_.mouseChildren = true;
                  method_10(_loc3_.am_Done,this.method_1491);
               }
            }
         }
      }
      
      override public function OnDestroyScreen() : void
      {
         var _loc1_:String = null;
         for each(_loc1_ in this.var_1120)
         {
            delete this.var_1120[_loc1_];
         }
         this.var_1120 = null;
         this.var_633 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:MovieClip = null;
         if(this.var_633)
         {
            _loc1_ = this.var_633.mMovieClip;
            if(_loc1_.parent)
            {
               _loc1_.parent.removeChild(_loc1_);
            }
            this.var_633.Hide();
         }
         this.var_633 = this.var_1120[this.var_2202];
         if(this.var_633)
         {
            var_2.addChild(this.var_633.mMovieClip);
            this.var_633.PlayAnimation("Ready");
            this.var_633.Show();
         }
      }
      
      public function OnInitDisplay(param1:String) : void
      {
         this.var_2202 = param1;
      }
      
      private function method_1491(param1:MouseEvent) : void
      {
         method_119();
         if(this.var_2202 == "am_Forge")
         {
            var_1.screenForge.Display();
         }
      }
   }
}
