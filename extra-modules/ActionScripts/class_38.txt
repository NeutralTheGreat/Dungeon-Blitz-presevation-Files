package
{
   public class class_38
   {
       
      
      internal var mBuffProperty:Object;
      
      internal var mOrder:Array;
      
      internal var var_1388:String;
      
      public function class_38(param1:String)
      {
         super();
         this.mBuffProperty = new Object();
         this.var_1388 = param1;
         this.mOrder = new Array();
      }
      
      public function method_2104() : void
      {
         this.mBuffProperty = null;
         this.mOrder = null;
      }
      
      public function add(param1:String, param2:String) : void
      {
         this.mBuffProperty[param1] = param2;
      }
   }
}
