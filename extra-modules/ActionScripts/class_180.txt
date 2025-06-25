package
{
   import flash.utils.Dictionary;
   
   public class class_180 extends class_167
   {
      
      private static const const_733:uint = 3000;
       
      
      internal var var_637:uint;
      
      internal var var_1520:uint;
      
      internal var fireTiming:Vector.<uint>;
      
      internal var var_2688:uint;
      
      public function class_180(param1:Entity, param2:String = "RoomActive")
      {
         var _loc4_:String = null;
         var _loc5_:Array = null;
         var _loc6_:uint = 0;
         super(param1,param2);
         this.var_637 = var_1.mTimeThisTick;
         if(Boolean(e.cue) && Boolean(e.cue.waitToAggro))
         {
            this.var_637 += e.cue.waitToAggro;
         }
         this.var_1520 = const_733;
         var _loc3_:Dictionary = !!e.cue ? e.cue.parsedParams : null;
         if(_loc3_)
         {
            if(_loc4_ = String(_loc3_["fireTiming"]))
            {
               _loc5_ = _loc4_.split(",");
               this.fireTiming = new Vector.<uint>();
               for each(_loc6_ in _loc5_)
               {
                  this.fireTiming.push(this.var_637 + _loc6_);
               }
            }
            this.var_1520 = uint(_loc3_["fireCycle"]);
            if(!this.var_1520)
            {
               this.var_1520 = const_733;
            }
         }
         if(!this.fireTiming)
         {
            this.fireTiming = new Vector.<uint>();
            this.fireTiming.push(this.var_637);
         }
         this.fireTiming.fixed = true;
         this.var_2688 = this.fireTiming.length;
      }
      
      override public function DestroyState() : void
      {
         this.fireTiming = null;
         super.DestroyState();
      }
      
      override public function TickState() : Class
      {
         var _loc5_:CombatState = null;
         var _loc1_:uint = uint(var_1.mTimeThisTick);
         if(_loc1_ < this.var_637)
         {
            return null;
         }
         var _loc2_:PowerType = e.GetRangedPower();
         if(!_loc2_)
         {
            return null;
         }
         if(!e.currRoom || !e.currRoom.playersInRoom)
         {
            return class_172;
         }
         var _loc3_:Boolean = false;
         var _loc4_:uint = 0;
         while(_loc4_ < this.var_2688)
         {
            if(_loc1_ >= this.fireTiming[_loc4_])
            {
               _loc3_ = true;
               this.fireTiming[_loc4_] += this.var_1520;
            }
            _loc4_++;
         }
         if(_loc3_)
         {
            (_loc5_ = e.combatState).method_749(_loc2_);
            _loc5_.method_51(_loc2_,true);
         }
         e.bFiring = false;
         return null;
      }
   }
}
