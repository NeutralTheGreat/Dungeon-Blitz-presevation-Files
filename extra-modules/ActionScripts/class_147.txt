package
{
   public class class_147
   {
       
      
      internal var superAnim:SuperAnimInstance;
      
      internal var var_2609:String;
      
      internal var var_2822:Number;
      
      internal var var_2657:Number;
      
      internal var width:Number;
      
      internal var height:Number;
      
      internal var var_2603:String;
      
      public function class_147(param1:SuperAnimInstance, param2:String, param3:Number, param4:Number, param5:Number, param6:Number)
      {
         super();
         this.superAnim = param1;
         this.var_2609 = param2;
         this.var_2822 = param3;
         this.var_2657 = param4;
         this.width = param5;
         this.height = param6;
      }
      
      public function method_720() : void
      {
         this.superAnim.DestroySuperAnimInstance();
         this.superAnim = null;
      }
   }
}
