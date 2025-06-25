package
{
   public class class_166
   {
       
      
      public var var_1059:String;
      
      public var var_1693:PowerType;
      
      public var var_322:int = 0;
      
      public var var_1164:int = 0;
      
      public var var_236:int = 0;
      
      public var var_550:int = 0;
      
      public var var_960:int = 0;
      
      public var var_1529:int = 0;
      
      public var var_201:int = 0;
      
      public var var_768:int = 0;
      
      public var var_951:int = 0;
      
      public var var_1317:int = 0;
      
      public var var_563:int = 0;
      
      public var var_814:int = 0;
      
      public function class_166(param1:PowerType)
      {
         super();
         this.var_1693 = param1;
         this.var_1059 = this.var_1693.powerName;
      }
      
      public function method_1538(param1:uint) : void
      {
         ++this.var_322;
      }
      
      public function method_175(param1:int, param2:Boolean, param3:Boolean, param4:Boolean, param5:Boolean) : void
      {
         if(param1 != 0 && param5 && !param3)
         {
            ++this.var_1164;
         }
         if(param2)
         {
            if(param3)
            {
               if(param4)
               {
                  this.var_1317 += param1;
               }
               else
               {
                  this.var_1529 += param1;
               }
            }
            else if(param4)
            {
               this.var_768 += param1;
            }
            else
            {
               this.var_550 += param1;
            }
         }
         else if(param3)
         {
            if(param4)
            {
               this.var_951 += param1;
            }
            else
            {
               this.var_960 += param1;
            }
         }
         else if(param4)
         {
            this.var_201 += param1;
         }
         else
         {
            this.var_236 += param1;
         }
      }
      
      public function method_1423(param1:int) : void
      {
         this.var_814 += param1;
      }
      
      public function method_1912() : void
      {
         ++this.var_563;
      }
      
      public function method_1734(param1:class_166) : void
      {
         this.var_322 += param1.var_322;
         this.var_1164 += param1.var_1164;
         this.var_236 += param1.var_236;
         this.var_550 += param1.var_550;
         this.var_960 += param1.var_960;
         this.var_1529 += param1.var_1529;
         this.var_201 += param1.var_201;
         this.var_768 += param1.var_768;
         this.var_951 += param1.var_951;
         this.var_1317 += param1.var_1317;
         this.var_563 += param1.var_563;
         this.var_814 += param1.var_814;
      }
      
      public function method_479(param1:Packet) : void
      {
         param1.method_9(this.var_1693.powerID);
         param1.method_24(this.var_322);
         param1.method_24(this.var_1164);
         param1.method_24(this.var_236);
         param1.method_24(this.var_550);
         param1.method_24(this.var_201);
         param1.method_24(this.var_768);
         param1.method_24(this.var_563);
         param1.method_24(this.var_814);
      }
   }
}
