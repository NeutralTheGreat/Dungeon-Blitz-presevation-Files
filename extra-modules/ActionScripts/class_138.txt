package
{
   import flash.text.AntiAliasType;
   import flash.text.TextField;
   import flash.text.TextFormat;
   
   public class class_138
   {
       
      
      private var var_1:Game;
      
      public var mTextField:TextField;
      
      private var var_1037:String;
      
      private var var_2436:String;
      
      public var mbVisible:Boolean;
      
      public var var_213:int;
      
      public var var_2444:String;
      
      public var var_258:int;
      
      private var var_2547:int;
      
      private var var_770:Number;
      
      private var var_2249:Number;
      
      private var var_1837:Boolean;
      
      public function class_138(param1:Game, param2:TextField)
      {
         super();
         this.var_1 = param1;
         this.var_1037 = param2.text;
         this.var_2436 = this.var_1037;
         this.mbVisible = param2.visible;
         this.mTextField = param2;
         this.mTextField.mouseEnabled = false;
         param2.embedFonts = true;
         param2.antiAliasType = AntiAliasType.ADVANCED;
         var _loc3_:TextFormat = param2.getTextFormat();
         param2.defaultTextFormat = _loc3_;
         param2.setTextFormat(_loc3_);
      }
      
      public function method_1593() : void
      {
         this.mTextField = null;
         this.var_1 = null;
      }
      
      public function Hide() : void
      {
         this.mTextField.visible = false;
         this.mbVisible = false;
      }
      
      public function Show() : void
      {
         this.mTextField.visible = true;
         this.mbVisible = true;
      }
      
      public function method_878(param1:Number, param2:String = "") : void
      {
         this.var_2444 = param2;
         this.var_2249 = param1 * Game.TARGETFPS;
         this.method_1810();
      }
      
      public function SetText(param1:String) : void
      {
         this.var_1037 = !!param1 ? param1 : "";
         this.var_258 = 0;
         this.var_213 = 0;
         this.var_1837 = false;
      }
      
      public function method_1810() : void
      {
         this.var_258 = int.MIN_VALUE;
         this.var_1837 = true;
      }
      
      public function TickTextField() : void
      {
         if(this.var_258 != this.var_213)
         {
            if(!this.var_2249)
            {
               this.var_258 = this.var_213;
            }
            else if(this.var_1837)
            {
               this.var_258 = this.var_213;
               this.var_1837 = false;
            }
            else if(!this.var_770 || this.var_2547 != this.var_213)
            {
               this.var_770 = (this.var_213 - this.var_258) / this.var_2249;
               this.var_2547 = this.var_213;
            }
            else if(this.var_770 > 0)
            {
               this.var_258 += int(this.var_770 * this.var_1.TIMESTEP) + 1;
               if(this.var_258 >= this.var_213)
               {
                  this.var_258 = this.var_213;
                  this.var_770 = 0;
               }
            }
            else
            {
               this.var_258 += int(this.var_770 * this.var_1.TIMESTEP) - 1;
               if(this.var_258 <= this.var_213)
               {
                  this.var_258 = this.var_213;
                  this.var_770 = 0;
               }
            }
            this.var_1037 = MathUtil.method_29(this.var_258) + this.var_2444;
         }
         if(this.var_1037 != this.var_2436)
         {
            this.var_2436 = this.var_1037;
            this.mTextField.text = this.var_1037;
         }
      }
   }
}
