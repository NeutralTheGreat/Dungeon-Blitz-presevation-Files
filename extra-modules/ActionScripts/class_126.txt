package
{
   import flash.display.MovieClip;
   
   public class class_126 extends class_32
   {
       
      
      public function class_126(param1:Game)
      {
         super(param1,"a_ScreenFanfare",null);
         var_15 = true;
         var_45 = "FadeIn";
         var_87 = "FadeOut";
         var_92 = 10;
      }
      
      public function OnInitDisplay(param1:String, param2:String) : void
      {
         var _loc3_:MovieClip = mWindow.mMovieClip.am_Information;
         MathUtil.method_2(_loc3_.am_Name,param1);
         method_12(_loc3_.am_IconHolder,param2);
      }
   }
}
