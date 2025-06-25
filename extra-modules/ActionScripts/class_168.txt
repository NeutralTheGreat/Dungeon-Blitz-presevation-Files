package
{
   public class class_168 extends class_167
   {
       
      
      internal var var_2861:uint = 0;
      
      public function class_168(param1:Entity, param2:String = "PerfTest")
      {
         super(param1,param2);
      }
      
      override public function TickState() : Class
      {
         e.bRunning = true;
         if(e.physPosX <= 300)
         {
            e.bLeft = false;
         }
         else if(e.physPosX >= 1110)
         {
            e.bLeft = true;
         }
         e.bFiring = true;
         var _loc1_:uint = uint(var_1.mTimeThisTick);
         if(_loc1_ - this.var_2861 > 2000)
         {
            e.bJumping = !e.bJumping;
            if(Math.random() > 0.7)
            {
               e.bLeft = !e.bLeft;
               e.bJumping = !e.bJumping;
            }
            this.var_2861 = _loc1_;
         }
         return null;
      }
      
      override public function EnterState(param1:Boolean) : void
      {
         brain.ChangeTarget(var_1.clientEnt);
      }
   }
}
