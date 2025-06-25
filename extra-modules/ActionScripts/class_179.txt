package
{
   public class class_179 extends class_167
   {
      
      private static const const_816:uint = 500;
      
      private static const const_865:uint = 1500;
       
      
      internal var var_637:uint;
      
      internal var var_2665:Boolean;
      
      public function class_179(param1:Entity, param2:String = "Alerted")
      {
         super(param1,param2);
         var _loc3_:uint = Math.random() * const_865;
         if(_loc3_ < const_816)
         {
            _loc3_ = const_816;
         }
         if(e.behaviorType.bSkipSpawnState)
         {
            _loc3_ = 0;
         }
         if(Boolean(e.cue) && Boolean(e.cue.waitToAggro))
         {
            _loc3_ = uint(e.cue.waitToAggro);
         }
         this.var_637 = var_1.mTimeThisTick + _loc3_;
         this.var_2665 = Boolean(e.cue) && Boolean(e.cue.waitToAggro);
      }
      
      override public function TickState() : Class
      {
         if(e.currHP < e.maxHP && !this.var_2665)
         {
            return class_178;
         }
         if(var_1.mTimeThisTick >= this.var_637)
         {
            return class_178;
         }
         return null;
      }
      
      override public function EnterState(param1:Boolean) : void
      {
         if(!e.behaviorType.bNoAutoFace && Boolean(brain.mostHatedEnt))
         {
            e.bLeft = brain.mostHatedEnt.physPosX < e.physPosX;
         }
         if(e.cue && e.cue.sayOnAlert && (param1 || !var_1.level.bInstanced))
         {
            e.StartSkit(e.cue.sayOnAlert,false,brain.mostHatedEnt);
         }
      }
      
      override public function ExitState(param1:Boolean) : void
      {
         var _loc2_:int = 0;
         if((param1 || !var_1.level.bInstanced) && e.cue && Boolean(e.cue.sayOnActivate))
         {
            e.StartSkit(e.cue.sayOnActivate,false,brain.mostHatedEnt);
         }
         if(param1 && !e.targetOffsetY && !e.behaviorType.bNoPhysics)
         {
            _loc2_ = 0;
            if(e.yOffsetToSimulateZ < Entity.YOFFSET_RANGE_HIGH)
            {
               _loc2_ = int(Math.random() * Entity.YOFFSET_RANGE_HIGH) - 1;
            }
            else if(e.yOffsetToSimulateZ > Entity.YOFFSET_RANGE_LOW)
            {
               _loc2_ = int(Math.random() * Entity.YOFFSET_RANGE_LOW) + 1;
            }
            if(_loc2_)
            {
               e.targetOffsetY = _loc2_;
               var_1.linkUpdater.WriteChangeOffsetY(e);
            }
         }
         e.entState = Entity.const_78;
         e.BeginActive();
      }
   }
}
