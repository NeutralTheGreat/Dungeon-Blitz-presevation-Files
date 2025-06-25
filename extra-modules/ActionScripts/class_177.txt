package
{
   public class class_177 extends class_172
   {
      
      private static const const_1160:uint = 3000;
       
      
      internal var var_1830:uint = 0;
      
      public function class_177(param1:Entity, param2:String = "Patrol")
      {
         super(param1,param2);
      }
      
      override public function TickState() : Class
      {
         var _loc1_:uint = 0;
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         if(brain.spawnSurface)
         {
            _loc1_ = uint(var_1.mTimeThisTick);
            _loc2_ = e.maxSpeed * e.maxSpeed * 0.5;
            _loc3_ = brain.spawnSurface.startX + _loc2_;
            _loc4_ = brain.spawnSurface.endX - _loc2_;
            if(Boolean(e.bLeft) && e.physPosX <= _loc3_ || !e.bLeft && e.physPosX >= _loc4_)
            {
               e.bRunning = false;
               if(!this.var_1830)
               {
                  this.var_1830 = _loc1_ + const_1160;
               }
               else if(_loc1_ >= this.var_1830)
               {
                  e.bLeft = !e.bLeft;
                  e.bRunning = true;
                  this.var_1830 = 0;
               }
            }
            if(e.currSurface != brain.spawnSurface)
            {
               e.SetCurrSurface(brain.spawnSurface);
               e.UpdatePos(e.startPhysPosX,e.startPhysPosY);
            }
         }
         return super.TickState();
      }
      
      override public function EnterState(param1:Boolean) : void
      {
         super.EnterState(param1);
         e.behaviorSpeedMod = 0.5;
         e.RecalculateSpeed();
         var_1.linkUpdater.WriteChangeMaxSpeed(e);
         e.bRunning = true;
      }
      
      override public function ExitState(param1:Boolean) : void
      {
         e.behaviorSpeedMod = 1;
         e.RecalculateSpeed();
         var_1.linkUpdater.WriteChangeMaxSpeed(e);
         e.bRunning = false;
         super.ExitState(param1);
      }
   }
}
