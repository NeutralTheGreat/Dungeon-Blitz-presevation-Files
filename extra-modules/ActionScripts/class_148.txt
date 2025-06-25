package
{
   public class class_148
   {
       
      
      internal var mNodeType:class_22;
      
      internal var mPointsSpent:uint;
      
      internal var var_1307:int;
      
      private var var_468:class_22;
      
      private var var_305:uint;
      
      private var var_2991:int;
      
      public function class_148(param1:class_22, param2:uint)
      {
         super();
         this.mNodeType = param1;
         this.mPointsSpent = param2;
         this.var_468 = null;
         this.var_305 = 0;
      }
      
      public function IsEmpty() : Boolean
      {
         if(!this.mNodeType && !this.var_468)
         {
            return true;
         }
         return false;
      }
      
      public function Socket(param1:class_22, param2:int) : void
      {
         if(this.mNodeType)
         {
            return;
         }
         this.var_468 = param1;
         this.method_460();
      }
      
      public function method_338() : void
      {
         if(this.var_468)
         {
            this.mNodeType = this.var_468;
            this.var_468 = null;
         }
         if(this.var_305)
         {
            this.mPointsSpent += this.var_305;
            this.var_305 = 0;
         }
      }
      
      public function method_478() : void
      {
         this.mNodeType = null;
         this.var_468 = null;
         this.method_1987();
      }
      
      public function method_333() : class_17
      {
         var _loc1_:uint = this.mPointsSpent + this.var_305;
         if(this.var_468)
         {
            return class_14.var_274[this.var_468.var_548 + _loc1_];
         }
         if(this.mNodeType)
         {
            return class_14.var_274[this.mNodeType.var_548 + _loc1_];
         }
         return null;
      }
      
      public function method_1301() : void
      {
         this.var_305 = 0;
      }
      
      public function method_1987() : void
      {
         this.var_305 = 0;
         this.mPointsSpent = 0;
      }
      
      public function method_520() : uint
      {
         return this.var_305;
      }
      
      public function HasPendingNodeType() : Boolean
      {
         return Boolean(this.var_468);
      }
      
      public function method_460() : void
      {
         ++this.var_305;
      }
      
      public function method_1317() : void
      {
         --this.var_305;
      }
      
      public function GetPointsSpent() : uint
      {
         return this.mPointsSpent + this.var_305;
      }
      
      public function DestroyTalentSlot() : void
      {
         this.mNodeType = null;
         this.mPointsSpent = 0;
         this.var_1307 = -1;
         this.var_468 = null;
         this.var_305 = 0;
      }
   }
}
