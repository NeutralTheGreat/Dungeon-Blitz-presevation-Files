package
{
   import flash.display.Sprite;
   
   public class class_60
   {
      
      public static const const_721:Number = 500;
      
      public static const const_555:uint = 70;
      
      public static const const_419:uint = 50;
       
      
      internal var var_1:Game;
      
      internal var var_167:Sprite;
      
      internal var var_330:Sprite;
      
      internal var var_313:Sprite;
      
      internal var var_2855:uint;
      
      internal var mTimeEnd:uint;
      
      public function class_60(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1351() : void
      {
         if(Boolean(this.var_330) && Boolean(this.var_330.parent))
         {
            this.var_330.parent.removeChild(this.var_330);
         }
         this.var_330 = null;
         if(Boolean(this.var_313) && Boolean(this.var_313.parent))
         {
            this.var_313.parent.removeChild(this.var_313);
         }
         this.var_313 = null;
         if(Boolean(this.var_167) && Boolean(this.var_167.parent))
         {
            this.var_167.parent.removeChild(this.var_167);
         }
         this.var_167 = null;
         this.var_1 = null;
      }
      
      public function Display() : void
      {
         if(!this.var_167)
         {
            this.var_167 = new Sprite();
            this.var_167.visible = false;
            this.var_330 = new Sprite();
            this.var_167.addChild(this.var_330);
            this.var_313 = new Sprite();
            this.var_167.addChild(this.var_313);
            this.var_330.graphics.beginFill(0,1);
            this.var_330.graphics.drawRect(0,0,Camera.SCREEN_WIDTH,10);
            this.var_330.graphics.endFill();
            this.var_313.graphics.beginFill(0,1);
            this.var_313.graphics.drawRect(0,0,Camera.SCREEN_WIDTH,10);
            this.var_313.graphics.endFill();
         }
         if(!this.var_167.visible)
         {
            this.var_167.visible = true;
            this.var_1.edgeLayer.addChildAt(this.var_167,0);
         }
         this.var_2855 = this.var_1.mTimeThisTick;
         this.mTimeEnd = 0;
      }
      
      public function method_253() : void
      {
         if(DevSettings.flags & DevSettings.DEVFLAG_NO_GRAPHICS)
         {
            return;
         }
         var _loc1_:Boolean = this.method_40();
         var _loc2_:Boolean = Boolean(this.var_1.clientEnt) && (this.var_1.clientEnt.InActiveCutScene() || this.var_1.clientEnt.currRoom && this.var_1.clientEnt.currRoom.var_1417);
         if(!_loc1_ && !_loc2_)
         {
            return;
         }
         if(!_loc1_ && _loc2_)
         {
            this.Display();
         }
         var _loc3_:uint = uint(this.var_1.mTimeThisTick - this.var_2855);
         var _loc4_:Number;
         if((_loc4_ = _loc3_ / const_721) > 1)
         {
            _loc4_ = 1;
         }
         var _loc5_:uint = const_555 * _loc4_;
         var _loc6_:uint = const_419 * _loc4_;
         this.var_330.height = _loc5_;
         this.var_313.height = _loc6_;
         this.var_313.y = Camera.PLAY_SCREEN_HEIGHT - _loc6_;
         if(!_loc2_)
         {
            if(!this.mTimeEnd)
            {
               this.mTimeEnd = this.var_1.mTimeThisTick;
            }
            _loc3_ = uint(this.var_1.mTimeThisTick - this.mTimeEnd);
            if((_loc4_ = _loc3_ / const_721) > 1)
            {
               _loc4_ = 1;
            }
            _loc5_ = const_555 - const_555 * _loc4_;
            _loc6_ = const_419 - const_419 * _loc4_;
            this.var_330.height = _loc5_;
            this.var_313.height = _loc6_;
            this.var_313.y = Camera.PLAY_SCREEN_HEIGHT - _loc6_;
            if(_loc5_ < 1 || _loc6_ < 1)
            {
               this.Hide();
            }
         }
      }
      
      public function Hide() : void
      {
         if(this.var_167)
         {
            this.var_167.visible = false;
            if(this.var_167.parent)
            {
               this.var_167.parent.removeChild(this.var_167);
            }
         }
      }
      
      public function method_40() : Boolean
      {
         return Boolean(this.var_167) && this.var_167.visible;
      }
   }
}
