package
{
   public class class_175 extends class_167
   {
       
      
      internal var var_544:uint = 0;
      
      public function class_175(param1:Entity, param2:String = "FireConstantly")
      {
         super(param1,param2);
      }
      
      override public function TickState() : Class
      {
         brain.target = e;
         if(!e.behaviorType.bNoAutoFace && !e.combatState.mActivePower)
         {
            e.bBackpedal = false;
            e.bLeft = e.physPosX > brain.target.physPosX;
         }
         e.bFiring = true;
         e.bRunning = false;
         brain.FirePowers();
         return null;
      }
   }
}
