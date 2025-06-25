package
{
   public class class_42
   {
       
      
      internal var gearType:GearType;
      
      internal var var_189:class_64;
      
      internal var var_196:class_64;
      
      internal var var_187:class_64;
      
      internal var var_295:class_21;
      
      internal var var_307:class_21;
      
      internal var var_1814:Boolean;
      
      public function class_42(param1:GearType, param2:class_64, param3:class_64, param4:class_64, param5:class_21, param6:class_21, param7:Boolean)
      {
         super();
         this.gearType = param1;
         this.var_189 = param2;
         this.var_196 = param3;
         this.var_187 = param4;
         this.var_295 = param5;
         this.var_307 = param6;
         this.var_1814 = param7;
      }
      
      public function method_2084() : void
      {
         this.gearType = null;
         if(this.var_189)
         {
            this.var_189.method_266();
            this.var_189 = null;
         }
         if(this.var_196)
         {
            this.var_196.method_266();
            this.var_196 = null;
         }
         if(this.var_187)
         {
            this.var_187.method_266();
            this.var_187 = null;
         }
         this.var_295 = null;
         this.var_307 = null;
      }
      
      public function method_908() : EntTypeGear
      {
         return new EntTypeGear(this.gearType.gearName,!!this.var_189 ? this.var_189.method_75() : 0,!!this.var_196 ? this.var_196.method_75() : 0,!!this.var_187 ? this.var_187.method_75() : 0,!!this.var_295 ? this.var_295.var_57 : 0,!!this.var_307 ? this.var_307.var_57 : 0);
      }
      
      public function method_1528() : String
      {
         return EntTypeGear.method_172(this.gearType.gearName,!!this.var_189 ? this.var_189.method_75() : 0,!!this.var_196 ? this.var_196.method_75() : 0,!!this.var_187 ? this.var_187.method_75() : 0,!!this.var_295 ? this.var_295.var_57 : 0,!!this.var_307 ? this.var_307.var_57 : 0);
      }
   }
}
