package
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.geom.Rectangle;
   
   public class class_152
   {
       
      
      internal var var_1223:MovieClip;
      
      internal var var_1772:MovieClip;
      
      internal var var_1041:MovieClip;
      
      internal var var_117:MovieClip;
      
      internal var var_1479:Boolean;
      
      internal var var_1620:Boolean;
      
      internal var var_2751:Boolean = false;
      
      internal var var_1773:Function;
      
      private var var_149:uint;
      
      private var var_490:uint;
      
      internal var var_173:uint = 0;
      
      internal var var_707:Number;
      
      internal var var_2745:Number = 3;
      
      public function class_152(param1:MovieClip, param2:MovieClip, param3:MovieClip, param4:uint, param5:Function)
      {
         super();
         this.var_1223 = param1;
         this.var_1772 = param2;
         this.var_1041 = param3;
         this.var_117 = this.var_1041.am_ScrollButton;
         this.var_173 = param4;
         this.var_149 = this.var_173;
         this.var_1773 = param5;
         var _loc6_:Rectangle = this.var_1041.getBounds(this.var_1041);
         this.var_707 = _loc6_.height + _loc6_.y * 2;
         this.var_1223.addEventListener(MouseEvent.MOUSE_DOWN,this.method_934);
         this.var_1772.addEventListener(MouseEvent.MOUSE_DOWN,this.method_580);
         this.var_117.addEventListener(MouseEvent.MOUSE_DOWN,this.method_889);
         this.var_1041.addEventListener(MouseEvent.MOUSE_DOWN,this.method_926);
         this.var_1223.addEventListener(Event.REMOVED_FROM_STAGE,this.method_688);
      }
      
      public function method_2137() : void
      {
         this.var_1223.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_934);
         this.var_1772.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_580);
         this.var_117.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_889);
         this.var_1041.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_926);
         this.var_1223.removeEventListener(Event.REMOVED_FROM_STAGE,this.method_688);
         this.var_1223 = null;
         this.var_1772 = null;
         this.var_117 = null;
         this.var_1041 = null;
         this.var_1773 = null;
      }
      
      public function method_2012(param1:int) : void
      {
         this.var_173 = param1;
         this.method_107();
      }
      
      public function method_984(param1:uint) : void
      {
         this.var_490 = param1;
         this.method_107(true);
      }
      
      public function method_2069() : void
      {
         this.var_149 = this.var_173;
         this.method_107();
      }
      
      public function method_1158() : void
      {
         this.var_149 = this.var_490 < this.var_173 ? this.var_173 : this.var_490;
         this.method_107();
      }
      
      public function method_2106() : void
      {
         if(this.var_1620)
         {
            this.var_2751 = true;
         }
         else
         {
            this.method_1158();
         }
      }
      
      private function method_107(param1:Boolean = false) : void
      {
         var _loc3_:Number = NaN;
         var _loc2_:Number = this.var_490 <= this.var_173 ? this.var_707 : this.var_707 * (this.var_173 / this.var_490);
         if(_loc2_ < this.var_2745)
         {
            _loc2_ = this.var_2745;
         }
         else if(_loc2_ > this.var_707)
         {
            _loc2_ = this.var_707;
         }
         this.var_117.height = _loc2_;
         if(!this.var_1479)
         {
            if(this.var_490 <= this.var_173)
            {
               this.var_117.y = 0;
            }
            else
            {
               _loc3_ = this.var_707 - this.var_117.height;
               this.var_117.y = _loc3_ * ((this.var_149 - this.var_173) / (this.var_490 - this.var_173));
            }
         }
         if(!param1)
         {
            this.var_1773(this.var_149 - this.var_173);
         }
      }
      
      private function method_934(param1:MouseEvent) : void
      {
         if(this.var_149 > this.var_173)
         {
            --this.var_149;
            this.method_107();
         }
      }
      
      private function method_580(param1:MouseEvent) : void
      {
         if(this.var_149 < this.var_490)
         {
            ++this.var_149;
            this.method_107();
         }
      }
      
      private function method_889(param1:MouseEvent) : void
      {
         this.var_1479 = true;
         this.var_117.startDrag(false,new Rectangle(this.var_117.x,0,0,this.var_707 - this.var_117.height));
         this.var_117.stage.addEventListener(MouseEvent.MOUSE_UP,this.method_539,false,0,true);
         this.var_117.stage.addEventListener(MouseEvent.MOUSE_MOVE,this.method_868,false,0,true);
      }
      
      private function method_539(param1:MouseEvent = null) : void
      {
         if(this.var_1479)
         {
            this.var_1479 = false;
            this.var_117.stopDrag();
            this.var_117.stage.removeEventListener(MouseEvent.MOUSE_UP,this.method_539);
            this.var_117.stage.removeEventListener(MouseEvent.MOUSE_MOVE,this.method_868);
         }
      }
      
      private function method_868(param1:MouseEvent) : void
      {
         this.method_1606();
      }
      
      private function method_1606() : void
      {
         var _loc1_:Number = this.var_707 - this.var_117.height;
         if(_loc1_ < 1)
         {
            return;
         }
         var _loc2_:Number = this.var_117.y / _loc1_;
         if(_loc2_ > 1)
         {
            _loc2_ = 1;
         }
         else if(_loc2_ < 0)
         {
            _loc2_ = 0;
         }
         var _loc3_:Number = this.var_173;
         var _loc4_:Number = this.var_490;
         this.var_149 = Math.round(_loc2_ * (_loc4_ - _loc3_)) + _loc3_;
         this.var_1773(this.var_149 - this.var_173);
      }
      
      private function method_540(param1:MouseEvent = null) : void
      {
         if(this.var_1620)
         {
            this.var_1620 = false;
            this.var_117.stage.removeEventListener(MouseEvent.MOUSE_UP,this.method_540);
            this.var_2751 = false;
         }
      }
      
      private function method_688(param1:Event) : void
      {
         this.method_540();
         this.method_539();
      }
      
      private function method_926(param1:MouseEvent) : void
      {
         var _loc4_:int = 0;
         if(!this.var_1620)
         {
            this.var_1620 = true;
            this.var_117.stage.addEventListener(MouseEvent.MOUSE_UP,this.method_540,false,0,true);
         }
         if(this.var_1479)
         {
            return;
         }
         var _loc2_:Number = param1.localY;
         var _loc3_:Number = this.var_707 - this.var_117.height;
         if(_loc3_ < 1)
         {
            return;
         }
         if(_loc2_ > this.var_117.y + this.var_117.height)
         {
            this.var_149 += 5;
            _loc4_ = this.var_490 < this.var_173 ? int(this.var_173) : int(this.var_490);
            if(this.var_149 > _loc4_)
            {
               this.var_149 = _loc4_;
            }
            this.method_107();
         }
         else if(_loc2_ < this.var_117.y)
         {
            this.var_149 -= 5;
            if(this.var_149 < this.var_173)
            {
               this.var_149 = this.var_173;
            }
            this.method_107();
         }
      }
   }
}
