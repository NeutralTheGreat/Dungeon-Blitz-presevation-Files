package
{
   import flash.display.Bitmap;
   import flash.display.DisplayObject;
   import flash.geom.Matrix;
   import flash.geom.Rectangle;
   
   public class MagicObject
   {
       
      
      internal var var_51:Bitmap;
      
      internal var dObj:DisplayObject;
      
      internal var var_2589:uint;
      
      internal var var_1751:Boolean;
      
      internal var var_716:Matrix;
      
      internal var var_1766:Boolean;
      
      internal var var_2857:Boolean;
      
      internal var var_2771:Boolean;
      
      internal var var_741:Rectangle;
      
      internal var var_2961:Boolean;
      
      internal var var_1967:String = null;
      
      internal var var_2848:String;
      
      public function MagicObject()
      {
         super();
      }
      
      public function method_1477() : void
      {
         if(this.var_51)
         {
            if(this.var_51.bitmapData)
            {
               this.var_51.bitmapData.dispose();
               this.var_51.bitmapData = null;
            }
            if(this.var_51.parent)
            {
               this.var_51.parent.removeChild(this.var_51);
            }
            this.var_51 = null;
         }
         this.dObj = null;
         this.var_741 = null;
         this.var_51 = null;
         this.var_716 = null;
         this.var_2848 = null;
      }
   }
}
