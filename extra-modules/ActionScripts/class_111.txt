package
{
   public class class_111
   {
      
      internal static const const_509:uint = 0;
      
      internal static const const_286:uint = 1;
      
      internal static const const_264:uint = 2;
      
      internal static const const_1101:uint = 511;
      
      internal static const const_432:uint = 9;
       
      
      internal var var_1:Game;
      
      internal var status:uint;
      
      internal var primary:uint;
      
      internal var secondary:uint;
      
      internal var var_2316:uint;
      
      internal var var_2675:uint;
      
      internal var endtime:uint;
      
      internal var var_8:uint;
      
      internal var usedlist:uint;
      
      internal var var_2434:Boolean;
      
      public function class_111(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function CanReroll() : Boolean
      {
         return this.primary && this.var_8 && this.status == class_111.const_264 && this.usedlist < class_111.const_1101;
      }
      
      public function CanAccept() : Boolean
      {
         return Boolean(this.primary) && this.status == class_111.const_264;
      }
      
      public function FreeForge() : void
      {
         this.status = class_111.const_509;
         this.primary = 0;
         this.secondary = 0;
         this.var_2316 = 0;
         this.endtime = 0;
         this.var_8 = 0;
         this.usedlist = 0;
      }
      
      public function RetreiveCharm() : class_64
      {
         var _loc1_:class_1 = class_14.var_767[this.primary];
         return new class_64(_loc1_,this.secondary,this.var_8);
      }
      
      public function GetCurrentlyCrafting() : class_1
      {
         return class_14.var_767[this.primary];
      }
   }
}
