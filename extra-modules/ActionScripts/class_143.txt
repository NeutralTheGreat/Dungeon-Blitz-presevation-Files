package
{
   import flash.display.Sprite;
   import flash.geom.Point;
   
   public class class_143
   {
      
      public static const PRESSED_JUMP:uint = 1;
      
      public static const RELEASED_JUMP:uint = 2;
      
      public static const PRESSED_DROP:uint = 3;
      
      public static const RELEASED_DROP:uint = 4;
      
      public static const PRESSED_FIRE:uint = 5;
      
      public static const RELEASED_FIRE:uint = 6;
       
      
      internal var var_1:Game;
      
      internal var var_48:Entity;
      
      internal var var_418:Camera;
      
      internal var var_1051:Number = 0;
      
      internal var var_896:Number = 0;
      
      public function class_143(param1:Game, param2:Entity)
      {
         super();
         this.var_1 = param1;
         this.var_48 = param2;
         this.var_418 = new Camera(param1,param2);
      }
      
      public function method_1489() : void
      {
         this.var_418.method_1964();
         this.var_418 = null;
         this.var_48 = null;
         this.var_1 = null;
      }
      
      public function method_375(param1:Point) : Point
      {
         var _loc2_:Main = this.var_1.main;
         var _loc3_:Sprite = this.var_1.levelLayer;
         var _loc4_:Number = 1 / _loc2_.overallScale;
         param1.x = _loc2_.mouseX * _loc4_ - _loc3_.x;
         param1.y = _loc2_.mouseY * _loc4_ - _loc3_.y;
         return param1;
      }
      
      public function method_550() : void
      {
         if(this.var_1.var_406.indexOf(Game.const_151) != -1)
         {
            if(this.var_896 == 0)
            {
               this.var_896 = this.var_1.mTimeThisTick;
            }
         }
         else
         {
            this.var_896 = 0;
         }
         if(this.var_1.var_406.indexOf(Game.const_153) != -1)
         {
            if(this.var_1051 == 0)
            {
               this.var_1051 = this.var_1.mTimeThisTick;
            }
         }
         else
         {
            this.var_1051 = 0;
         }
         if(this.var_1051 == 0 && this.var_896 == 0)
         {
            this.var_48.bRunning = false;
         }
         else if(this.var_1051 == 0 && this.var_896 > 0)
         {
            this.var_48.bLeft = false;
            this.var_48.bBackpedal = false;
            this.var_48.bRunning = true;
         }
         else if(this.var_1051 > 0 && this.var_896 == 0)
         {
            this.var_48.bLeft = true;
            this.var_48.bBackpedal = false;
            this.var_48.bRunning = true;
         }
         else if(this.var_1051 > this.var_896)
         {
            this.var_48.bLeft = true;
            this.var_48.bBackpedal = true;
            this.var_48.bRunning = true;
         }
         else
         {
            this.var_48.bLeft = false;
            this.var_48.bBackpedal = true;
            this.var_48.bRunning = true;
         }
         if(this.var_48.var_1787 > this.var_1.mTimeThisTick)
         {
            if(this.var_48.var_687 != this.var_48.bLeft)
            {
               this.var_48.bBackpedal = true;
            }
            else
            {
               this.var_48.bBackpedal = false;
            }
         }
      }
      
      public function Jump() : void
      {
         this.var_48.var_471.push(PRESSED_JUMP);
      }
      
      public function method_727() : void
      {
         this.var_48.var_471.push(RELEASED_JUMP);
      }
      
      public function Drop() : void
      {
         this.var_48.var_471.push(PRESSED_DROP);
      }
      
      public function method_725() : void
      {
         this.var_48.var_471.push(RELEASED_DROP);
      }
      
      public function Fire() : void
      {
         this.var_48.var_471.push(PRESSED_FIRE);
      }
      
      public function method_674() : void
      {
         this.var_48.var_471.push(RELEASED_FIRE);
      }
   }
}
