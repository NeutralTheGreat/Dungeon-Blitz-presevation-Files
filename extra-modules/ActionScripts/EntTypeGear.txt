package
{
   public class EntTypeGear
   {
       
      
      internal var gearName:String;
      
      internal var var_432:uint;
      
      internal var var_501:uint;
      
      internal var var_486:uint;
      
      internal var var_644:uint;
      
      internal var var_705:uint;
      
      internal var var_2432:String;
      
      public function EntTypeGear(param1:String, param2:uint, param3:uint, param4:uint, param5:uint = 0, param6:uint = 0)
      {
         super();
         this.gearName = param1;
         this.var_432 = param2;
         this.var_501 = param3;
         this.var_486 = param4;
         this.var_644 = param5;
         this.var_705 = param6;
         this.var_2432 = method_172(this.gearName,this.var_432,this.var_501,this.var_486,this.var_644,this.var_705);
      }
      
      public static function method_172(param1:String, param2:uint, param3:uint, param4:uint, param5:uint, param6:uint) : String
      {
         return param1 + ":" + String(param2) + ":" + String(param3) + ":" + String(param4) + ":" + String(param5) + ":" + String(param6);
      }
      
      public function method_875() : void
      {
         this.var_2432 = method_172(this.gearName,this.var_432,this.var_501,this.var_486,this.var_644,this.var_705);
      }
   }
}
