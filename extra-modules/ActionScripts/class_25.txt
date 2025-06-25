package
{
   import flash.geom.Matrix;
   
   public class class_25
   {
       
      
      internal var className:String;
      
      internal var frame:int;
      
      internal var var_1320:Matrix;
      
      internal var var_2320:Number;
      
      internal var var_1263:Vector.<class_25>;
      
      internal var var_2440:int;
      
      internal var var_1866:Boolean;
      
      internal var var_2639:Boolean;
      
      public function class_25(param1:String, param2:String, param3:Matrix, param4:Number)
      {
         super();
         this.className = param1;
         this.var_1320 = param3;
         this.var_2320 = param4;
         this.frame = 1;
         if(!param1.indexOf("Whole"))
         {
            this.var_2639 = true;
         }
         else if(!param1.indexOf("a_Head"))
         {
            this.var_1866 = true;
         }
         this.var_2440 = SuperAnimData.var_2126[param1];
      }
      
      public function method_796() : void
      {
         var _loc1_:class_25 = null;
         this.var_1320 = null;
         if(this.var_1263)
         {
            for each(_loc1_ in this.var_1263)
            {
               _loc1_.method_796();
            }
            this.var_1263 = null;
         }
      }
   }
}
