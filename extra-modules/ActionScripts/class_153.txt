package
{
   import flash.display.Bitmap;
   import flash.display.MovieClip;
   
   public class class_153
   {
       
      
      internal var var_434:PowerType;
      
      internal var var_714:Boolean = false;
      
      internal var var_1161:Boolean = false;
      
      internal var keyClip:MovieClip;
      
      internal var keyAnim:class_33;
      
      internal var buttonClip:MovieClip;
      
      internal var var_2274:MovieClip;
      
      internal var var_220:Bitmap;
      
      public function class_153(param1:MovieClip, param2:class_33, param3:MovieClip, param4:MovieClip)
      {
         super();
         this.keyClip = param1;
         this.keyAnim = param2;
         this.buttonClip = param3;
         this.var_2274 = param4;
      }
      
      public function method_1066() : void
      {
         this.keyClip = null;
         this.buttonClip = null;
         this.var_434 = null;
         this.var_2274 = null;
         this.keyAnim.DestroyUIMovieClip();
         this.keyAnim = null;
         this.method_431();
      }
      
      public function method_431() : void
      {
         if(this.var_220)
         {
            if(this.var_220.bitmapData)
            {
               this.var_220.bitmapData.dispose();
               this.var_220.bitmapData = null;
            }
            this.var_220 = null;
         }
      }
   }
}
