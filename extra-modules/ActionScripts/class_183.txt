package
{
   public class class_183 extends class_167
   {
       
      
      internal var var_544:uint = 0;
      
      public function class_183(param1:Entity, param2:String = "Melee")
      {
         super(param1,param2);
      }
      
      override public function TickState() : Class
      {
         if(brain.target != brain.mostHatedEnt)
         {
            brain.ChangeTarget(brain.mostHatedEnt);
         }
         if(!brain.target)
         {
            return !!e.behaviorType.bSkipSpawnState ? brain.mTetherState : class_182;
         }
         var _loc1_:PowerType = e.GetMeleePower();
         var _loc2_:int = brain.target.entType.width * 0.5 + (!!_loc1_ ? _loc1_.method_63(e) : 0);
         var _loc3_:Number = Math.abs(brain.target.physPosX - e.physPosX);
         var _loc4_:*;
         if(!(_loc4_ = _loc3_ > _loc2_))
         {
            this.var_544 = 0;
         }
         else if(!this.var_544)
         {
            this.var_544 = var_1.mTimeThisTick + (!!e.behaviorType.bSlowOnTheUptake ? Brain.const_807 : Brain.const_606);
         }
         else if(var_1.mTimeThisTick >= this.var_544)
         {
            return class_178;
         }
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
