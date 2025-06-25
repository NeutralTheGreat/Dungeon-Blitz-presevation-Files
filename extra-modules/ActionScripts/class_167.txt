package
{
   public class class_167
   {
       
      
      internal var var_1:Game;
      
      internal var e:Entity;
      
      internal var brain:Brain;
      
      internal var var_786:String;
      
      public function class_167(param1:Entity, param2:String)
      {
         super();
         this.e = param1;
         this.brain = this.e.brain;
         this.var_786 = param2;
         this.var_1 = param1.var_1;
      }
      
      public function DestroyState() : void
      {
         this.e = null;
         this.brain = null;
         this.var_1 = null;
      }
      
      public function EnterState(param1:Boolean) : void
      {
      }
      
      public function ExitState(param1:Boolean) : void
      {
      }
      
      public function TickState() : Class
      {
         return null;
      }
   }
}
