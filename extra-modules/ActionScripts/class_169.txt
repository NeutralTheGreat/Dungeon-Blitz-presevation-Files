package
{
   public class class_169 extends class_167
   {
       
      
      public function class_169(param1:Entity, param2:String = "Dumb")
      {
         super(param1,param2);
      }
      
      override public function TickState() : Class
      {
         return null;
      }
      
      override public function EnterState(param1:Boolean) : void
      {
         e.entState = Entity.const_78;
      }
   }
}
