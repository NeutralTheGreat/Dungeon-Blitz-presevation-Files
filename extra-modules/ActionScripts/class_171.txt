package
{
   public class class_171 extends class_167
   {
      
      private static const const_1221:uint = 5;
      
      public static const const_675:uint = class_178.const_535 - 200;
       
      
      private var var_2293:Number;
      
      private var var_2438:Number;
      
      private var var_1688:uint;
      
      public function class_171(param1:Entity, param2:String = "Tether")
      {
         super(param1,param2);
         this.var_2293 = e.physPosX;
         this.var_2438 = e.physPosY;
         this.var_1688 = var_1.mTimeThisTick;
      }
      
      override public function EnterState(param1:Boolean) : void
      {
         e.behaviorSpeedMod = 1.5;
         e.RecalculateSpeed();
         e.brain.ClearHateList();
         var_1.linkUpdater.WriteChangeMaxSpeed(e);
      }
      
      override public function TickState() : Class
      {
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         if(brain.bDeepSleep)
         {
            return class_172;
         }
         var _loc1_:Number = e.physPosX - brain.homeLoc.x;
         var _loc2_:Number = e.velocity.x * e.velocity.x * 0.5;
         var _loc3_:Number = const_1221 + _loc2_;
         if(_loc1_ >= -_loc3_ && _loc1_ <= _loc3_)
         {
            return class_172;
         }
         if(brain.mostHatedEnt)
         {
            if(_loc1_ > const_675 || _loc1_ < -const_675)
            {
               e.TeleportTo(brain.homeLoc.x,brain.homeLoc.y);
               return class_172;
            }
            return class_178;
         }
         var _loc4_:uint = uint(var_1.mTimeThisTick);
         if(!e.maxSpeed)
         {
            this.var_1688 = _loc4_;
         }
         else if(_loc4_ - this.var_1688 >= 2000)
         {
            _loc5_ = Math.abs(e.physPosX - this.var_2293);
            _loc6_ = Math.abs(e.physPosY - this.var_2438);
            if(_loc5_ <= 10 && _loc6_ <= 10)
            {
               e.TeleportTo(brain.homeLoc.x,brain.homeLoc.y);
               return class_172;
            }
            this.var_2293 = e.physPosX;
            this.var_2438 = e.physPosY;
            this.var_1688 = _loc4_;
         }
         e.bFiring = false;
         e.bRunning = true;
         e.bLeft = _loc1_ > 0;
         e.bBackpedal = false;
         return null;
      }
      
      override public function ExitState(param1:Boolean) : void
      {
         e.bRunning = false;
         e.behaviorSpeedMod = 1;
         e.RecalculateSpeed();
         var_1.linkUpdater.WriteChangeMaxSpeed(e);
      }
   }
}
