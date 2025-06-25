package
{
   public class class_181 extends class_167
   {
      
      private static const const_842:uint = 4000;
      
      private static const const_853:uint = 1000;
       
      
      internal var var_2872:uint;
      
      internal var var_2568:uint;
      
      public function class_181(param1:Entity, param2:String = "Annoyed")
      {
         super(param1,param2);
         this.var_2872 = var_1.mTimeThisTick + const_842;
      }
      
      override public function TickState() : Class
      {
         if(!brain.mostHatedEnt)
         {
            return class_172;
         }
         if(e.currHP < e.maxHP)
         {
            return class_179;
         }
         var _loc1_:uint = uint(var_1.mTimeThisTick);
         var _loc2_:Number = e.physPosX - brain.mostHatedEnt.physPosX;
         if(Math.abs(_loc2_) <= brain.mAggroRadius)
         {
            this.var_2568 = _loc1_;
         }
         else if(_loc1_ >= this.var_2568 + const_853)
         {
            brain.ClearHateList();
            return class_172;
         }
         if(_loc1_ >= this.var_2872)
         {
            return class_179;
         }
         e.bBackpedal = false;
         if(!e.behaviorType.bNoAutoFace && Boolean(e.entType.bPassiveTurnToFace))
         {
            e.bLeft = _loc2_ > 0;
         }
         return null;
      }
      
      override public function ExitState(param1:Boolean) : void
      {
         if(brain.mostHatedEnt)
         {
            brain.CallForHelp(brain.mostHatedEnt);
         }
      }
   }
}
