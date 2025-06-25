package
{
   import flash.display.JointStyle;
   import flash.display.Shape;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import flash.text.TextFormat;
   
   public class ResourceMonitorUtil extends Sprite
   {
       
      
      private var var_2935:uint = 16777215;
      
      private var var_2954:Number = 0.25;
      
      private var var_2903:uint = 0;
      
      private var var_2881:Number = 0.25;
      
      private var var_2929:uint = 10027008;
      
      private var var_2877:Number = 0.5;
      
      private var var_2795:Boolean = true;
      
      private var var_2879:Boolean = true;
      
      private var var_2917:TextFormat;
      
      private var var_1226:Array;
      
      private var var_2904:Array;
      
      private var var_1121:int = 20;
      
      private var var_2006:Sprite;
      
      private var var_1043:Sprite;
      
      private var var_609:Sprite;
      
      private var var_833:Shape;
      
      private var _width:int = 150;
      
      private var var_2044:int = 60;
      
      private var var_1411:int = 0;
      
      private var var_2540:Boolean = false;
      
      public function ResourceMonitorUtil()
      {
         this.var_2917 = new TextFormat("Courier",10,16777215);
         this.var_1226 = new Array();
         this.var_2904 = new Array();
         super();
         this.mouseEnabled = false;
         this.mouseChildren = false;
         this.var_2006 = new Sprite();
         this.addChild(this.var_2006);
         this.var_1043 = new Sprite();
         this.var_2006.addChild(this.var_1043);
         this.var_609 = new Sprite();
         this.addChild(this.var_609);
         this.var_833 = new Shape();
         this.var_609.addChild(this.var_833);
      }
      
      public static function method_2086(param1:int, param2:int = 2) : Number
      {
         return Number((param1 / (1024 * 1024)).toFixed(param2));
      }
      
      public function method_104(param1:String, param2:Number, param3:int, param4:int) : void
      {
         this.var_2540 = true;
         visible = true;
         var _loc5_:class_163 = new class_163();
         this.var_1226[param1] = _loc5_;
         _loc5_._label = param1;
         _loc5_.var_2722 = param2;
         _loc5_.var_2654 = param3;
         _loc5_.var_2551 = param4;
         _loc5_.var_367 = new Array();
         _loc5_.var_732 = new Shape();
         this.var_609.addChildAt(_loc5_.var_732,0);
         var _loc6_:TextField;
         (_loc6_ = new TextField()).defaultTextFormat = new TextFormat("Courier",10,param4,true);
         _loc6_.autoSize = TextFieldAutoSize.LEFT;
         _loc6_.multiline = false;
         _loc6_.wordWrap = false;
         _loc6_.selectable = false;
         _loc5_.var_1769 = _loc6_;
         _loc6_.text = "";
         _loc6_.y = this.var_1411;
         this.var_1411 += 12;
         this.var_2006.addChild(_loc6_);
      }
      
      public function method_1035() : void
      {
         var _loc1_:class_163 = null;
         if(!this.var_2540)
         {
            return;
         }
         this.width = this._width;
         for each(_loc1_ in this.var_1226)
         {
            _loc1_.var_367.push(_loc1_._valThisTick);
            if(_loc1_.var_367.length > this.var_1121)
            {
               _loc1_.var_367.splice(0,1);
            }
            _loc1_.var_2913 = this.method_1127(_loc1_);
         }
         this.var_1043.graphics.clear();
         this.var_1043.graphics.clear();
         this.var_1043.graphics.beginFill(this.var_2903,this.var_2881);
         this.var_1043.graphics.drawRect(0,0,this._width,this.var_1411 + 5);
         this.var_1043.graphics.endFill();
         if(this.var_2879)
         {
            for each(_loc1_ in this.var_1226)
            {
               _loc1_.var_1769.text = _loc1_._label;
               _loc1_.var_1769.appendText(" ");
               _loc1_.var_1769.appendText(_loc1_._valThisTick.toFixed());
            }
         }
         var _loc2_:Number = this._width / this.var_1121;
         this.var_609.graphics.clear();
         this.var_609.y = this.var_1411 + 5;
         this.var_609.graphics.beginFill(this.var_2929,this.var_2877);
         this.var_609.graphics.drawRect(0,0,this._width,this.var_2044);
         this.var_609.graphics.endFill();
         this.var_833.graphics.clear();
         this.var_833.visible = this.var_2795;
         if(!this.var_2795)
         {
            return;
         }
         var _loc3_:int = 0;
         while(_loc3_ < this.var_1121)
         {
            this.var_833.graphics.lineStyle(1,this.var_2935,this.var_2954,false,"normal","none",JointStyle.MITER);
            this.var_833.graphics.moveTo(_loc3_ * _loc2_,0);
            this.var_833.graphics.lineTo(_loc3_ * _loc2_,this.var_2044);
            this.var_833.graphics.endFill();
            _loc3_++;
         }
         for each(_loc1_ in this.var_1226)
         {
            this.method_1901(_loc1_);
         }
         dispatchEvent(new Event(Event.CHANGE));
      }
      
      public function method_107(param1:String, param2:Number) : void
      {
         this.var_1226[param1]._valThisTick = param2;
      }
      
      private function method_1127(param1:class_163) : Number
      {
         var _loc2_:Number = 0;
         var _loc3_:int = 0;
         while(_loc3_ < param1.var_367.length)
         {
            _loc2_ += param1.var_367[_loc3_];
            _loc3_++;
         }
         return param1.var_367.length > 0 ? _loc2_ / param1.var_367.length : 0;
      }
      
      private function method_1901(param1:class_163) : void
      {
         var _loc5_:Number = NaN;
         if(!param1.var_732)
         {
            return;
         }
         var _loc2_:Number = this._width / this.var_1121;
         var _loc3_:int = this.var_2044;
         param1.var_732.graphics.clear();
         param1.var_732.graphics.lineStyle(param1.var_2654,param1.var_2551,1,false,"normal","none",JointStyle.MITER);
         var _loc4_:int = 0;
         while(_loc4_ < param1.var_367.length)
         {
            _loc5_ = -(param1.var_367[_loc4_] / param1.var_2722) + 1;
            if(_loc4_ == 0)
            {
               param1.var_732.graphics.moveTo(_loc2_ * _loc4_ + _loc2_ * (this.var_1121 - param1.var_367.length),_loc5_ * _loc3_);
            }
            else
            {
               param1.var_732.graphics.lineTo(_loc2_ * _loc4_ + _loc2_ * (this.var_1121 - param1.var_367.length),_loc5_ * _loc3_);
            }
            _loc4_++;
         }
         param1.var_732.graphics.endFill();
      }
      
      override public function set width(param1:Number) : void
      {
         this._width = param1;
      }
      
      override public function get width() : Number
      {
         return this._width;
      }
   }
}
