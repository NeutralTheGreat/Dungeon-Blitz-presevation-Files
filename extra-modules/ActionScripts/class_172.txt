package
{
   public class class_172 extends class_167
   {
      
      private static const const_587:uint = 2000;
       
      
      internal var var_2086:uint;
      
      internal var var_2512:Boolean;
      
      internal var var_2866:Boolean;
      
      public function class_172(param1:Entity, param2:String = "Sleep")
      {
         super(param1,param2);
         this.var_2086 = var_1.mTimeThisTick + Math.random() * const_587;
         this.var_2512 = e.behaviorType.bFastSleepChecks;
         this.var_2866 = Boolean(e.behaviorType.bRoomAggroRadius) || e.summonerId && !e.behaviorType.bFollowSpawner || Boolean(e.cue) && Boolean(e.cue.bDoNotAutoSpawn);
      }
      
      override public function TickState() : Class
      {
         var _loc3_:Entity = null;
         var _loc4_:Entity = null;
         var _loc1_:BehaviorType = e.behaviorType;
         if(e.behaviorType.bNoCombat)
         {
            return null;
         }
         if(brain.bDeepSleep)
         {
            return null;
         }
         if(_loc1_.var_1080)
         {
            return class_175;
         }
         if(_loc1_.var_534 && e.currRoom && Boolean(e.currRoom.playersInRoom))
         {
            return class_180;
         }
         if(brain.mostHatedEnt)
         {
            return class_179;
         }
         if(this.var_2866 && e.currRoom && Boolean(e.currRoom.playersInRoom))
         {
            _loc3_ = e.currRoom.GetTarget();
            if(_loc3_)
            {
               brain.AddHate(_loc3_,0,false);
            }
         }
         var _loc2_:uint = uint(var_1.mTimeThisTick);
         if(this.var_2512 || _loc2_ - this.var_2086 >= const_587)
         {
            if(_loc4_ = brain.FindClosestEnemy(false))
            {
               if(brain.bAnnoyedInsteadOfAggro)
               {
                  brain.AddHate(_loc4_,0,false);
                  return class_181;
               }
               brain.AddHate(_loc4_,0,true);
               return class_179;
            }
            this.var_2086 = _loc2_;
         }
         return null;
      }
      
      override public function EnterState(param1:Boolean) : void
      {
         brain.ClearHateList();
         e.combatState.ResetCooldownsAndImmunity();
         e.entState = Entity.const_399;
         if(e.cue)
         {
            e.bLeft = e.cue.IsFacingLeft();
         }
         e.bFiring = false;
         e.bRunning = false;
         e.BeginSleep();
      }
   }
}
