package
{
   public class class_173 extends class_172
   {
       
      
      internal var var_2867:uint;
      
      internal var var_2713:uint;
      
      internal var var_1656:uint;
      
      internal var var_1543:Class;
      
      public function class_173(param1:Entity, param2:String = "Drama")
      {
         super(param1,param2);
         var _loc3_:String = Boolean(e.cue) && Boolean(e.cue.dramaAnim) ? String(e.cue.dramaAnim) : String(e.entType.dramaAnim);
         this.var_2713 = var_1.mTimeThisTick + 0;
      }
      
      override public function DestroyState() : void
      {
         this.var_1543 = null;
         super.DestroyState();
      }
      
      override public function TickState() : Class
      {
         var _loc1_:uint = uint(var_1.mTimeThisTick);
         if(_loc1_ < this.var_2713)
         {
            return null;
         }
         if(!this.var_1543)
         {
            this.var_1543 = super.TickState();
         }
         if(!this.var_1656 && Boolean(this.var_1543))
         {
            this.var_1656 = _loc1_ + this.var_2867;
            e.entState = Entity.const_78;
            e.BeginActive();
         }
         if(Boolean(this.var_1656) && _loc1_ >= this.var_1656)
         {
            return this.var_1543;
         }
         return null;
      }
      
      override public function EnterState(param1:Boolean) : void
      {
         super.EnterState(param1);
         e.entState = Entity.const_467;
         e.BeginDrama();
      }
   }
}
