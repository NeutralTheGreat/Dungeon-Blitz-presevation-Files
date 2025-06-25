package
{
   public class class_174 extends class_167
   {
       
      
      public function class_174(param1:Entity, param2:String = "CutScene")
      {
         super(param1,param2);
      }
      
      override public function EnterState(param1:Boolean) : void
      {
         e.bRunning = false;
         e.bFiring = false;
         e.bUntargetable = true;
         var_1.linkUpdater.WriteEntityUntargetable(e.id,true);
      }
      
      override public function TickState() : Class
      {
         if(Boolean(e.bRunning) && e.entState != Entity.const_78)
         {
            e.entState = Entity.const_78;
            e.BeginActive();
         }
         if(e.InActiveCutScene())
         {
            return null;
         }
         var _loc1_:Class = brain.pausedStateClass;
         brain.pausedStateClass = null;
         if(_loc1_ == class_173 && e.cue && Boolean(e.cue.dramaAnim))
         {
            return class_172;
         }
         return _loc1_;
      }
      
      override public function ExitState(param1:Boolean) : void
      {
         e.bUntargetable = false;
         var_1.linkUpdater.WriteEntityUntargetable(e.id,false);
      }
   }
}
