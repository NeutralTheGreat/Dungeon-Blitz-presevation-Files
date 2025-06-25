package
{
   import flash.display.MovieClip;
   import flash.filters.GlowFilter;
   import flash.geom.ColorTransform;
   import flash.geom.Matrix;
   import flash.text.StyleSheet;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   
   public class ChatBubble
   {
      
      private static const const_748:int = 150;
       
      
      internal var var_34:MovieClip;
      
      internal var var_2456:uint = 0;
      
      internal var var_678:uint = 0;
      
      internal var var_1:Game;
      
      internal var var_19:Entity;
      
      internal var var_866:int = 1;
      
      internal var scale:Number = 1;
      
      internal var scaleX:Number = 1;
      
      internal var scaleY:Number = 1;
      
      internal var width:Number;
      
      internal var height:Number;
      
      internal var var_361:int = 3000;
      
      internal var var_1490:String;
      
      internal var var_2698:Number;
      
      internal var var_2831:Number;
      
      internal var var_2909:Number;
      
      internal var var_2502:Number = 200;
      
      internal var var_2514:Number = 30;
      
      internal var var_1796:Array = null;
      
      public function ChatBubble(param1:Entity)
      {
         super();
         this.var_19 = param1;
         this.var_1 = this.var_19.var_1;
      }
      
      public static function method_464(param1:String) : String
      {
         var _loc2_:String = param1;
         var _loc3_:RegExp = /\[b\](.*?)\[\/b\]/gi;
         var _loc4_:RegExp = /\[i\](.*?)\[\/i\]/gi;
         var _loc5_:RegExp = /\[S(.*?)\](.*?)\[\/S\]/gi;
         var _loc6_:Array = new Array(_loc3_,_loc4_,_loc5_);
         var _loc7_:Array = new Array("<b>$1</b>","<i>$1</i>","<font size=\'$1\'>$2</font>");
         var _loc8_:int = 0;
         while(_loc8_ < _loc6_.length)
         {
            _loc2_ = _loc2_.replace(_loc6_[_loc8_],_loc7_[_loc8_]);
            _loc8_++;
         }
         return _loc2_;
      }
      
      public function method_1793() : void
      {
         if(Boolean(this.var_34) && Boolean(this.var_34.parent))
         {
            this.var_34.parent.removeChild(this.var_34);
         }
         this.var_34 = null;
         this.var_19 = null;
         this.var_1 = null;
      }
      
      public function method_1804(param1:String) : String
      {
         var _loc3_:Array = null;
         var _loc4_:String = null;
         var _loc2_:String = null;
         if(!this.var_1796)
         {
            this.var_1796 = new Array();
         }
         if(param1.length > 2 && param1.charAt(0) == "[")
         {
            _loc3_ = param1.split("]");
            _loc4_ = (_loc4_ = (_loc4_ = String(_loc3_[0])).slice(1)).toLowerCase();
            param1 = String(_loc3_[1]);
            param1 = StringUtils.method_80(param1);
            _loc2_ = String(this.var_1796[_loc4_]);
         }
         if(_loc2_ == null)
         {
            _loc2_ = String(this.var_1796["normal"]);
         }
         if(_loc2_ != null)
         {
            param1 = _loc2_ + param1 + "</font>";
         }
         return param1;
      }
      
      public function method_1105() : void
      {
         this.var_34 = class_4.method_16("a_ChatBubble");
         this.var_34.visible = false;
         var _loc1_:TextField = this.var_34.getChildByName("am_ChatTextBox") as TextField;
         var _loc2_:MovieClip = this.var_34.getChildByName("am_ChatBack") as MovieClip;
         var _loc3_:MovieClip = this.var_34.getChildByName("am_ChatPtr") as MovieClip;
         this.var_2698 = _loc1_.width;
         this.var_2831 = _loc1_.height;
         this.var_2909 = _loc3_.height;
      }
      
      public function method_328(param1:String) : void
      {
         var _loc2_:String = "";
         param1 = StringUtils.method_80(param1);
         if(param1.length > const_748)
         {
            param1 = param1.slice(0,const_748).concat("...");
         }
         this.var_361 = Entity.const_642 + param1.length * Entity.const_833;
         if(param1 == "")
         {
            if(this.var_34 && this.var_34.visible && this.var_678 < this.var_361)
            {
               this.var_678 = this.var_361;
            }
            return;
         }
         this.var_1490 = param1;
         this.var_678 = 0;
         this.var_2456 = this.var_1.mTimeThisTick;
         if(param1.length > 2 && param1.charAt(0) == "^")
         {
            _loc2_ = param1.charAt(1);
            _loc2_ = _loc2_.toLowerCase();
            param1 = param1.slice(2);
            param1 = StringUtils.method_80(param1);
         }
         param1 = this.method_1804(param1);
         if(this.var_19.entType.var_1623)
         {
            this.var_1.method_82(this.var_19.entType.var_1623,this.var_19.physPosX,this.var_19.physPosY);
         }
         param1 = method_464(param1);
         if(!this.var_34)
         {
            this.method_1105();
         }
         this.var_1.var_781.addChild(this.var_34);
         var _loc5_:TextField;
         (_loc5_ = this.var_34.getChildByName("am_ChatTextBox") as TextField).x = 0;
         _loc5_.y = 0;
         _loc5_.width = 0;
         _loc5_.height = 0;
         _loc5_.autoSize = TextFieldAutoSize.LEFT;
         _loc5_.styleSheet = new StyleSheet();
         _loc5_.wordWrap = false;
         _loc5_.text = param1;
         _loc5_.antiAliasType = "advanced";
         _loc5_.width += 10;
         _loc5_.autoSize = TextFieldAutoSize.NONE;
         if(_loc5_.width < this.var_2514)
         {
            _loc5_.width = this.var_2514;
         }
         else if(_loc5_.width > this.var_2502)
         {
            _loc5_.width = this.var_2502;
         }
         _loc5_.wordWrap = true;
         _loc5_.autoSize = TextFieldAutoSize.LEFT;
         _loc5_.height = _loc5_.height;
         _loc5_.width = _loc5_.width;
         _loc5_.y = -_loc5_.height + 0.3;
         _loc5_.x = -(_loc5_.width / 2);
         this.width = _loc5_.width;
         this.height = _loc5_.height;
         _loc5_.autoSize = TextFieldAutoSize.NONE;
         _loc5_.text = param1;
         _loc5_.wordWrap = true;
         if(_loc2_ == "t")
         {
            this.var_866 = 2;
         }
         else if(_loc2_ == "e")
         {
            this.var_866 = 3;
         }
         else if(_loc2_ == "s")
         {
            this.var_866 = 3;
            this.scale = 1.6;
         }
         else if(_loc2_ == "w")
         {
            this.var_866 = 1;
            this.scale = 0.75;
         }
         else if(_loc2_ == "b")
         {
            this.var_866 = 4;
            this.scale = 1.6;
         }
         else
         {
            this.var_866 = 1;
         }
         var _loc6_:MovieClip = this.var_34.getChildByName("am_ChatBack") as MovieClip;
         var _loc7_:MovieClip = this.var_34.getChildByName("am_ChatPtr") as MovieClip;
         _loc6_.gotoAndStop(1);
         _loc6_.transform.matrix = new Matrix();
         _loc7_.gotoAndStop(1);
         _loc7_.transform.matrix = new Matrix();
         _loc6_.y = _loc5_.y;
         _loc6_.x = _loc5_.x;
         this.scaleX = this.width / this.var_2698;
         this.scaleY = this.height / this.var_2831;
         _loc6_.gotoAndStop(this.var_866);
         _loc7_.gotoAndStop(this.var_866);
         _loc6_.am_ChatInternal.scaleX = this.scaleX;
         _loc6_.am_ChatInternal.scaleY = this.scaleY;
         var _loc8_:* = (0 & 16711680) >> 16;
         var _loc9_:* = (0 & 65280) >> 8;
         var _loc10_:* = 0 & 255;
         if(_loc6_)
         {
            _loc6_.transform.colorTransform = new ColorTransform(1,1,1,1,_loc8_,_loc9_,_loc10_,0);
         }
         if(_loc7_)
         {
            _loc7_.transform.colorTransform = new ColorTransform(1,1,1,1,_loc8_,_loc9_,_loc10_,0);
         }
         this.var_34.filters = [new GlowFilter(11701805,1,5,5,10)];
         this.var_34.visible = true;
         this.var_34.scaleX = this.scale;
         this.var_34.scaleY = this.scale;
         this.method_901();
      }
      
      public function method_901() : void
      {
         var _loc24_:TextField = null;
         if(!this.var_34 || !this.var_34.visible)
         {
            return;
         }
         if(!this.var_1.mUIManager || !this.var_1.mUIManager.method_1688())
         {
            this.var_678 += this.var_1.TIMESTEP * 1000 / Number(Game.TARGETFPS);
         }
         var _loc1_:Boolean = this.var_19 && this.var_1.clientEnt && Boolean(this.var_1.clientEnt.var_518) && this.var_1.clientEnt.var_518 == this.var_19.id;
         var _loc2_:Boolean = this.var_19 && this.var_1.clientEnt && Boolean(this.var_1.clientEnt.var_518) && this.var_1.clientEntID == this.var_19.id;
         if(_loc1_ || _loc2_)
         {
            if(this.var_678 < this.var_361 && this.var_678 > this.var_361 - 200)
            {
               this.var_678 = this.var_361 - 200;
            }
         }
         this.var_34.x = this.var_19.appearPosX + 10;
         this.var_34.y = this.var_19.appearPosY - this.var_19.entType.height - 50;
         if(this.var_19.var_694)
         {
            this.var_34.y -= 75;
         }
         if(this.var_19.combatState.var_39 == class_14.powerTypesDict["SentinelForm1"].powerID)
         {
            this.var_34.y -= 55;
         }
         if(this.var_19.var_599 != Entity.const_282)
         {
            this.var_34.y -= Entity.const_836;
         }
         var _loc5_:Boolean = true;
         var _loc6_:Number = 0;
         var _loc7_:Boolean = false;
         var _loc8_:Boolean = false;
         var _loc13_:Number = -this.var_1.levelLayer.x + this.width / 2 + 25;
         var _loc14_:Number = -this.var_1.levelLayer.x - this.width / 2 + Camera.SCREEN_WIDTH - 25;
         if(this.var_34.x < _loc13_)
         {
            if(this.var_34.x < _loc13_ - this.width / 2)
            {
               _loc8_ = true;
            }
            if((_loc6_ = this.var_34.x - _loc13_) < -(this.width / 2 - 16))
            {
               _loc6_ = -(this.width / 2 - 16);
            }
            this.var_34.x = _loc13_;
         }
         else if(this.var_34.x > _loc14_)
         {
            if(this.var_34.x > _loc14_ + this.width / 2)
            {
               _loc7_ = true;
            }
            if((_loc6_ = this.var_34.x - _loc14_) > this.width / 2 - 16)
            {
               _loc6_ = this.width / 2 - 16;
            }
            this.var_34.x = _loc14_;
         }
         var _loc15_:Number = 0;
         if(Boolean(this.var_19) && this.var_1.var_641.method_40())
         {
            _loc15_ = this.var_1.var_641.var_330.height;
         }
         var _loc16_:Number = -this.var_1.levelLayer.y + _loc15_ + this.height + 6;
         var _loc17_:Number = -this.var_1.levelLayer.y - _loc15_ + Camera.PLAY_SCREEN_HEIGHT - 6;
         if(this.var_34.y < _loc16_)
         {
            this.var_34.y = _loc16_;
         }
         else if(this.var_34.y > _loc17_)
         {
            this.var_34.y = _loc17_;
         }
         var _loc18_:MovieClip;
         (_loc18_ = this.var_34.getChildByName("am_ChatPtr") as MovieClip).transform.matrix = new Matrix();
         if(_loc8_)
         {
            _loc18_.rotation = 90;
            _loc18_.x = -this.width / 2 + 3;
            _loc18_.y = -this.height / 2;
         }
         else if(_loc7_)
         {
            _loc18_.rotation = -90;
            _loc18_.x = this.width / 2 - 3;
            _loc18_.y = -this.height / 2;
         }
         else
         {
            _loc18_.x = _loc6_;
         }
         var _loc19_:Number = this.var_1.mTimeThisTick - this.var_2456;
         var _loc20_:Number = this.var_678;
         var _loc21_:Number = 0;
         var _loc22_:Number = this.var_361;
         var _loc23_:class_26;
         if((Boolean(_loc23_ = this.var_19.gfx.m_Seq.var_30)) && _loc23_.var_1802 == class_127.var_1566)
         {
            if((_loc24_ = this.var_34.getChildByName("am_ChatTextBox") as TextField).text == class_127.var_1825)
            {
               _loc22_ = 1000000000;
            }
         }
         if(_loc19_ <= 100)
         {
            _loc21_ = 0.2 + 0.8 * (_loc19_ / 100);
         }
         else if(_loc20_ <= _loc22_)
         {
            _loc21_ = 1;
         }
         else if(_loc20_ <= _loc22_ + 500)
         {
            _loc21_ = 1 - (_loc20_ - _loc22_) / 500;
         }
         this.var_34.alpha = _loc21_;
         if(_loc21_ <= 0)
         {
            this.var_34.visible = false;
         }
      }
   }
}
