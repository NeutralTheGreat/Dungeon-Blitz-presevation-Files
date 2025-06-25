package
{
   public class PowerGroup
   {
       
      
      public var var_1:Game;
      
      public var var_2766:ActivePower;
      
      public var var_973:PowerType;
      
      public var var_2824:uint = 0;
      
      public var var_1740:uint = 0;
      
      public var var_1290:Vector.<Entity>;
      
      public var var_1335:int = 0;
      
      public function PowerGroup(param1:Game, param2:ActivePower, param3:PowerType)
      {
         super();
         this.var_1 = param1;
         this.var_2766 = param2;
         this.var_973 = param3;
         if(Boolean(this.var_973) && Boolean(this.var_973.var_108))
         {
            if(this.var_973.var_108.length > 1)
            {
               this.var_1740 = this.var_973.var_108[1];
            }
            else
            {
               this.var_1740 = this.var_973.var_108[0];
            }
         }
      }
      
      public function method_1629(param1:Entity) : Boolean
      {
         if(Boolean(this.var_1740) && this.var_1.mTimeThisTick >= this.var_2824)
         {
            this.var_1290 = new Vector.<Entity>();
            this.var_2824 = this.var_1.mTimeThisTick + this.var_1740;
         }
         else if(!this.var_1290)
         {
            this.var_1290 = new Vector.<Entity>();
         }
         var _loc2_:Boolean = false;
         if(this.var_1290.indexOf(param1) < 0)
         {
            this.var_1290.push(param1);
            _loc2_ = true;
         }
         return _loc2_;
      }
      
      public function method_587(param1:ActivePower) : void
      {
         param1.var_157 = this;
         ++this.var_1335;
      }
      
      public function method_1817() : void
      {
         --this.var_1335;
         if(this.var_1335 <= 0)
         {
            this.method_1005();
         }
      }
      
      public function method_1005() : void
      {
         this.var_2766 = null;
         this.var_1290 = null;
         this.var_973 = null;
         this.var_1 = null;
      }
   }
}
