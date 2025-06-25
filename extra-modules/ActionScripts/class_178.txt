package
{
   public class class_178 extends class_167
   {
      
      private static const const_768:uint = 1000;
      
      private static const const_613:uint = 400;
      
      public static const const_535:uint = 2000;
       
      
      internal var var_2460:Boolean = true;
      
      public function class_178(param1:Entity, param2:String = "Pursuit")
      {
         super(param1,param2);
      }
      
      override public function EnterState(param1:Boolean) : void
      {
         if(brain.target)
         {
            brain.UpdateTargetRange();
         }
      }
      
      override public function TickState() : Class
      {
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         if(brain.target != brain.mostHatedEnt)
         {
            brain.ChangeTarget(brain.mostHatedEnt);
         }
         if(!brain.target)
         {
            return !!e.behaviorType.bSkipSpawnState ? brain.mTetherState : class_182;
         }
         if(e.behaviorType.bNoPursueTarget)
         {
            return !!e.behaviorType.bDefaultToRanged ? class_184 : class_183;
         }
         if(this.var_2460)
         {
            this.var_2460 = false;
            if(Math.abs(brain.target.physPosX - e.physPosX) <= Math.abs(brain.mTargetRange))
            {
               return !!e.behaviorType.bDefaultToRanged ? class_184 : class_183;
            }
         }
         if(!e.cue || e.cue.room != e.currRoom)
         {
            if((_loc4_ = brain.homeLoc.x - e.physPosX) > const_535 || _loc4_ < -const_535)
            {
               return brain.mTetherState;
            }
            if((_loc5_ = brain.target.physPosX - e.physPosX) > const_768 || _loc5_ < -const_768)
            {
               return brain.mTetherState;
            }
            if((_loc6_ = brain.target.physPosY - e.physPosY) > const_613 || _loc6_ < -const_613)
            {
               return brain.mTetherState;
            }
         }
         if(!e.behaviorType.bNoAutoFace && !e.combatState.mActivePower)
         {
            e.bLeft = e.physPosX > brain.target.physPosX;
         }
         else if(e.bBackpedal)
         {
            e.bLeft = !e.bLeft;
         }
         var _loc1_:Number = e.velocity.x * e.velocity.x * 0.5;
         var _loc2_:Number = brain.target.physPosX + brain.mTargetRange;
         var _loc3_:* = e.physPosX >= _loc2_;
         if(_loc3_)
         {
            if(!e.bLeft)
            {
               e.bBackpedal = true;
               e.bLeft = true;
            }
            else
            {
               e.bBackpedal = false;
            }
            e.bRunning = e.physPosX - _loc2_ - _loc1_ > 0;
         }
         else
         {
            if(e.bLeft)
            {
               e.bBackpedal = true;
               e.bLeft = false;
            }
            else
            {
               e.bBackpedal = false;
            }
            e.bRunning = _loc2_ - _loc1_ - e.physPosX > 0;
         }
         if(!e.bRunning)
         {
            return !!e.behaviorType.bDefaultToRanged ? class_184 : class_183;
         }
         e.bFiring = true;
         brain.FirePowers();
         return null;
      }
   }
}
