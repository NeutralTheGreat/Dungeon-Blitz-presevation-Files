package
{
   import flash.display.BitmapData;
   import flash.display.MovieClip;
   
   public class class_159
   {
       
      
      internal var var_2944:String;
      
      internal var var_1287:Number;
      
      internal var var_1208:Number;
      
      internal var var_586:Number;
      
      internal var var_2759:Number;
      
      internal var var_2842:Number;
      
      internal var var_509:BitmapData;
      
      internal var var_2055:MovieClip;
      
      public function class_159(param1:String, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:MovieClip)
      {
         super();
         this.var_2944 = param1;
         this.var_1287 = param2;
         this.var_1208 = param3;
         this.var_586 = param4;
         this.var_2759 = param5;
         this.var_2842 = param6;
         this.var_2055 = param7;
      }
      
      public function method_1696() : void
      {
         this.var_2055 = null;
         if(this.var_509)
         {
            this.var_509.dispose();
            this.var_509 = null;
         }
      }
   }
}
