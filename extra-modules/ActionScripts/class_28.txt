package
{
   import flash.geom.Matrix;
   import flash.geom.Point;
   
   public class class_28
   {
       
      
      internal var var_2034:uint;
      
      internal var var_900:Vector.<class_25>;
      
      internal var var_2381:Point;
      
      internal var var_1807:Point;
      
      internal var var_1813:Point;
      
      internal var var_2388:Matrix;
      
      public function class_28(param1:uint)
      {
         super();
         this.var_2034 = param1;
         this.var_900 = new Vector.<class_25>();
      }
      
      public function method_655() : void
      {
         var _loc1_:class_25 = null;
         this.var_2381 = null;
         this.var_1807 = null;
         this.var_1813 = null;
         this.var_2388 = null;
         for each(_loc1_ in this.var_900)
         {
            _loc1_.method_796();
         }
         this.var_900 = null;
      }
   }
}
