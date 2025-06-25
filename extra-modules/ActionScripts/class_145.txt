package
{
   public class class_145
   {
       
      
      internal var var_2649:int;
      
      internal var var_2699:int;
      
      internal var var_2707:int;
      
      internal var var_2591:int;
      
      internal var var_1833:String;
      
      internal var room:Room;
      
      internal var id:int;
      
      public function class_145(param1:String, param2:int, param3:int, param4:int, param5:int, param6:Room, param7:int)
      {
         super();
         this.var_2649 = param2;
         this.var_2699 = param3;
         this.var_2707 = param2 + param4;
         this.var_2591 = param3 + param5;
         this.var_1833 = param1;
         this.room = param6;
         this.id = param7;
      }
      
      public function method_1465() : void
      {
         this.room = null;
      }
      
      public function method_810(param1:int, param2:int) : Boolean
      {
         return param1 >= this.var_2649 && param1 <= this.var_2707 && param2 >= this.var_2699 && param2 <= this.var_2591;
      }
   }
}
