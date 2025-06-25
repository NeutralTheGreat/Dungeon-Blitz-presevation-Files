package
{
   public class class_182 extends class_167
   {
      
      private static const const_1320:Number = 0.5;
      
      private static const const_591:uint = 4000;
      
      private static const const_1291:uint = 8000;
       
      
      internal var var_2536:uint;
      
      public function class_182(param1:Entity, param2:String = "Victory")
      {
         super(param1,param2);
         var _loc3_:uint = const_591 + Math.random() * (const_1291 - const_591);
         this.var_2536 = var_1.mTimeThisTick + _loc3_;
      }
      
      override public function TickState() : Class
      {
         if(brain.mostHatedEnt)
         {
            return class_178;
         }
         e.bFiring = false;
         e.bRunning = false;
         if(var_1.mTimeThisTick < this.var_2536)
         {
            return null;
         }
         return brain.mTetherState;
      }
   }
}
