package
{
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.geom.Point;
   
   public class class_137
   {
      
      private static const const_408:Number = 1;
       
      
      private var var_1:Game;
      
      private var var_2627:Number;
      
      private var var_2437:Number;
      
      private var var_2714:Number;
      
      private var var_2790:Number;
      
      private var var_493:Number;
      
      private var var_1822:Boolean;
      
      private var var_1696:Function;
      
      private var var_1719:Function;
      
      private var var_2485:Point;
      
      private var var_2758:Point;
      
      private var var_2838:uint;
      
      public var var_484:DisplayObject;
      
      private var var_2577:Boolean;
      
      private var var_2621:Boolean;
      
      public function class_137(param1:Game)
      {
         super();
         this.var_1 = param1;
         this.var_2758 = new Point();
         this.var_2485 = new Point();
      }
      
      public static function method_1396(param1:Number) : Number
      {
         return param1;
      }
      
      public static function method_113(param1:Number) : Number
      {
         return param1 * param1 * (3 - 2 * param1);
      }
      
      public function method_862() : void
      {
         if(this.var_484)
         {
            if(this.var_2621)
            {
               this.var_484.parent.removeChild(this.var_484);
            }
            this.var_484 = null;
         }
         this.var_1 = null;
         this.var_2758 = null;
         this.var_2485 = null;
         this.var_1696 = null;
         this.var_1719 = null;
      }
      
      public function method_922() : DisplayObject
      {
         return this.var_484;
      }
      
      public function ForceComplete() : void
      {
         this.var_1822 = true;
      }
      
      public function method_546(param1:MovieClip, param2:Boolean = true) : void
      {
         this.var_484 = param1;
         this.var_2621 = param2;
      }
      
      public function method_1283(param1:Boolean) : void
      {
         this.var_2577 = param1;
      }
      
      public function method_470(param1:Number, param2:Number, param3:uint, param4:Function, param5:Function) : void
      {
         this.var_493 = 0;
         this.var_2838 = param3;
         this.var_1822 = false;
         if(param4 == null)
         {
            this.var_1696 = method_1396;
         }
         else
         {
            this.var_1696 = param4;
         }
         this.var_1719 = param5;
         this.var_2627 = this.var_484.x;
         this.var_2437 = this.var_484.y;
         this.var_2714 = param1;
         this.var_2790 = param2;
      }
      
      public function method_1931() : Boolean
      {
         var _loc1_:Number = NaN;
         if(this.var_1822)
         {
            return true;
         }
         if(this.var_493 < const_408)
         {
            this.var_493 += this.var_1.TIMESTEP * 1000 / Game.TARGETFPS / this.var_2838;
            if(this.var_493 >= const_408)
            {
               this.var_493 = const_408;
               if(this.var_1719 != null)
               {
                  this.var_1719();
               }
               this.var_1822 = true;
            }
            _loc1_ = this.var_1696(this.var_493);
            if(this.var_2577)
            {
               this.var_484.alpha = 1 - _loc1_;
            }
            this.var_484.x = this.var_2627 * (1 - _loc1_) + this.var_2714 * _loc1_;
            this.var_484.y = this.var_2437 * (1 - _loc1_) + this.var_2790 * _loc1_;
         }
         return false;
      }
   }
}
