package
{
   import flash.display.MovieClip;
   import flash.events.*;
   import flash.filters.DropShadowFilter;
   import flash.geom.ColorTransform;
   import flash.geom.Point;
   import flash.text.StyleSheet;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   
   public class class_104
   {
      
      public static const const_983:Number = 300;
      
      public static const const_888:Number = 700;
      
      private static var var_2155:uint = 0;
      
      private static var var_2422:uint = 14211288;
      
      private static var var_2355:uint = 3675407;
      
      private static var var_2183:uint = 9558973;
      
      private static var var_2383:uint = 2956300;
      
      private static var var_2371:uint = 14533209;
      
      private static var var_2379:uint = 2956300;
      
      private static var var_2232:uint = 5882589;
      
      private static var var_2223:uint = 0;
      
      private static var var_2272:uint = 15239304;
       
      
      internal var var_1:Game;
      
      internal var var_43:MovieClip = null;
      
      internal var var_2196:Number = 0;
      
      internal var var_361:Number = 0;
      
      internal var var_2988:Number = 0;
      
      internal var var_2967:Number = 0;
      
      internal var var_2915:Number = 0;
      
      internal var var_1730:String;
      
      internal var var_978:Boolean;
      
      internal var var_411:Number;
      
      internal var var_740:Number;
      
      internal var var_497:String;
      
      internal var var_2190:Number;
      
      internal var var_2099:Boolean = false;
      
      internal var var_1494:int;
      
      internal var var_2686:int;
      
      public function class_104(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1744() : void
      {
         if(Boolean(this.var_43) && Boolean(this.var_43.parent))
         {
            this.var_43.parent.removeChild(this.var_43);
         }
         this.var_43 = null;
         this.var_1 = null;
      }
      
      public function TriggerTooltip(param1:String) : void
      {
         var _loc2_:int = 0;
         var _loc4_:String = null;
         if(!param1)
         {
            return;
         }
         var _loc3_:Array = param1.split("$");
         this.var_978 = false;
         this.var_411 = var_2155;
         this.var_740 = var_2422;
         this.var_361 = 10000;
         this.var_2190 = 0;
         _loc2_ = 0;
         while(_loc2_ < _loc3_.length - 1)
         {
            if((_loc4_ = _loc3_[_loc2_] as String) == "NOW")
            {
               this.var_978 = true;
            }
            else if(_loc4_ == "REACT")
            {
               this.UntriggerTooltip();
               this.var_978 = true;
               this.var_361 = 2000;
               this.var_411 = var_2223;
               this.var_740 = var_2272;
               this.var_2190 = -40;
            }
            else if(_loc4_ == "MAPDUNGEON")
            {
               this.var_978 = true;
               this.var_411 = var_2355;
               this.var_740 = var_2183;
            }
            else if(_loc4_ == "MAPTEAMMATE")
            {
               this.var_978 = true;
               this.var_411 = var_2383;
               this.var_740 = var_2371;
            }
            else if(_loc4_ == "MAPLANDMARK")
            {
               this.var_978 = true;
               this.var_411 = var_2379;
               this.var_740 = var_2232;
            }
            _loc2_++;
         }
         this.var_497 = _loc3_[_loc3_.length - 1];
      }
      
      public function UntriggerTooltip() : void
      {
         this.var_497 = null;
      }
      
      public function method_1543() : void
      {
         var _loc1_:Number = this.var_1.mTimeThisTick;
         if(Boolean(this.var_497) && this.var_1494 == 0)
         {
            this.var_1494 = this.var_1.mTimeThisTick;
         }
         else if(!this.var_497)
         {
            this.var_1494 = 0;
         }
         var _loc2_:Number = this.var_978 ? 0 : const_983;
         if(Boolean(this.var_1494) && this.var_1494 <= _loc1_ - _loc2_)
         {
            this.var_2099 = true;
         }
         if(this.var_2099)
         {
            if(Boolean(this.var_497) && this.var_497 != this.var_1730)
            {
               this.var_2915 = _loc1_;
               if(this.var_497)
               {
                  this.method_549(this.var_497,this.var_411);
               }
            }
            else if(this.var_497 == null)
            {
               if(this.var_1730)
               {
                  this.var_361 = this.var_1.mTimeThisTick - this.var_2196;
               }
            }
            this.var_1730 = this.var_497;
         }
         this.method_754(false);
         if(Boolean(this.var_43) && this.var_43.visible)
         {
            this.var_2686 = _loc1_;
         }
         if(this.var_2686 < _loc1_ - const_888)
         {
            this.var_2099 = false;
         }
      }
      
      public function method_549(param1:String, param2:Number) : void
      {
         param1 = StringUtils.method_80(param1);
         param1 = ChatBubble.method_464(param1);
         this.var_2196 = this.var_1.mTimeThisTick;
         if(!this.var_43)
         {
            this.var_43 = class_4.method_16("a_Tooltip");
            this.var_43.filters = [new DropShadowFilter(2,45,0,2,3,3)];
            this.var_43.alpha = 0.1;
         }
         this.var_1.var_245.addChild(this.var_43);
         var _loc3_:TextField = this.var_43.getChildByName("am_Text") as TextField;
         var _loc4_:MovieClip = this.var_43.getChildByName("am_Background") as MovieClip;
         _loc3_.x = 0;
         _loc3_.y = 0;
         _loc3_.width = 0;
         _loc3_.height = 0;
         _loc3_.autoSize = TextFieldAutoSize.LEFT;
         _loc3_.styleSheet = new StyleSheet();
         _loc3_.wordWrap = false;
         _loc3_.text = param1;
         _loc3_.antiAliasType = "advanced";
         _loc3_.width += 1;
         _loc3_.autoSize = TextFieldAutoSize.NONE;
         if(_loc3_.width < 30)
         {
            _loc3_.width = 30;
         }
         else if(_loc3_.width > 150)
         {
            _loc3_.width = 150;
         }
         _loc3_.wordWrap = true;
         _loc3_.autoSize = TextFieldAutoSize.LEFT;
         _loc3_.y = -_loc3_.height;
         _loc3_.x = 0;
         _loc4_.gotoAndStop(1);
         _loc4_.y = _loc3_.y;
         _loc4_.x = _loc3_.x;
         _loc4_.width = _loc3_.width;
         _loc4_.height = _loc3_.height;
         _loc3_.autoSize = TextFieldAutoSize.NONE;
         _loc3_.text = param1;
         _loc3_.textColor = param2;
         _loc3_.wordWrap = true;
         this.var_43.visible = true;
         var _loc5_:Number = ((this.var_740 & 16711680) >> 16) / 256;
         var _loc6_:Number = ((this.var_740 & 65280) >> 8) / 256;
         var _loc7_:Number = (this.var_740 & 255) / 256;
         _loc4_.transform.colorTransform = new ColorTransform(_loc5_,_loc6_,_loc7_,1,0,0,0,0);
         this.method_754(true);
      }
      
      public function method_754(param1:Boolean) : void
      {
         if(!this.var_43 || !this.var_43.visible)
         {
            return;
         }
         var _loc3_:MovieClip = this.var_43.getChildByName("am_Background") as MovieClip;
         if(param1)
         {
            this.var_43.x = (this.var_1.main.stage.mouseX - this.var_1.main.parent.x) / this.var_1.main.overallScale;
            this.var_43.y = (this.var_1.main.stage.mouseY - this.var_1.main.parent.y) / this.var_1.main.overallScale;
            this.var_43.x += this.var_2190;
            this.var_43.y -= 15;
         }
         _loc3_.gotoAndStop(1);
         var _loc4_:Point = new Point(0,0);
         var _loc5_:Point;
         (_loc5_ = new Point()).x = Camera.SCREEN_WIDTH * 0.5;
         _loc5_.y = Camera.SCREEN_HEIGHT * 0.5;
         var _loc6_:Point;
         if((_loc6_ = (_loc6_ = new Point(this.var_43.x,this.var_43.y)).subtract(_loc5_)).x < Camera.SCREEN_WIDTH * -0.5 + this.var_43.width / 2)
         {
            _loc4_.x = Camera.SCREEN_WIDTH * -0.5 + this.var_43.width / 2;
            this.var_43.x = _loc5_.x + _loc4_.x;
         }
         else if(_loc6_.x > Camera.SCREEN_WIDTH * 0.5 - this.var_43.width / 2)
         {
            _loc4_.x = Camera.SCREEN_WIDTH * 0.5 - this.var_43.width / 2;
            this.var_43.x = _loc5_.x + _loc4_.x;
         }
         if(_loc6_.y < Camera.SCREEN_HEIGHT * -0.5 + this.var_43.height)
         {
            _loc4_.y = Camera.SCREEN_HEIGHT * -0.5 + this.var_43.height;
            this.var_43.y = _loc5_.y + _loc4_.y;
         }
         else if(_loc6_.y > Camera.SCREEN_HEIGHT * 0.5)
         {
            _loc4_.y = Camera.SCREEN_HEIGHT * 0.5;
            this.var_43.y = _loc5_.y + _loc4_.y;
         }
         _loc3_.gotoAndStop(1);
         var _loc7_:Number = this.var_1.mTimeThisTick - this.var_2196;
         var _loc8_:Number = 0;
         var _loc9_:Number = this.var_361;
         if(_loc7_ <= 1000)
         {
            _loc8_ = 0;
         }
         if(_loc7_ <= 100)
         {
            if((_loc8_ = 0.2 + 0.8 * (_loc7_ / 100)) < this.var_43.alpha)
            {
               _loc8_ = this.var_43.alpha;
            }
         }
         else if(_loc7_ <= _loc9_)
         {
            _loc8_ = 1;
         }
         else if(_loc7_ <= _loc9_ + 250)
         {
            if((_loc8_ = 1 - (_loc7_ - _loc9_) / 250) < 0.5)
            {
               _loc8_ = 0;
            }
         }
         this.var_43.alpha = _loc8_;
         if(_loc8_ <= 0)
         {
            this.var_43.visible = false;
            this.var_43.parent.removeChild(this.var_43);
            this.var_497 = null;
            this.var_1730 = null;
         }
      }
   }
}
