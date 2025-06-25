package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.DisplayObject;
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import flash.display.PixelSnapping;
   import flash.display.StageQuality;
   import flash.events.MouseEvent;
   import flash.geom.Matrix;
   import flash.geom.Rectangle;
   import flash.system.ApplicationDomain;
   import flash.text.AntiAliasType;
   import flash.text.TextField;
   
   public class class_4
   {
       
      
      internal var var_1:Game;
      
      internal var mActiveScreens:Vector.<class_32>;
      
      internal var var_1240:Vector.<class_32>;
      
      internal var var_981:Boolean = false;
      
      internal var var_1983:Boolean = false;
      
      public function class_4(param1:Game)
      {
         super();
         this.var_1 = param1;
         this.mActiveScreens = new Vector.<class_32>();
         this.var_1240 = new Vector.<class_32>();
      }
      
      public static function method_125(param1:String) : void
      {
         class_33.var_1480 = param1;
      }
      
      public static function method_639(param1:Game, param2:String, param3:Number) : Bitmap
      {
         var _loc4_:Bitmap = new Bitmap(null,PixelSnapping.ALWAYS);
         var _loc5_:MovieClip = method_16(param2);
         var _loc6_:Rectangle = _loc5_.getBounds(_loc5_);
         var _loc7_:Number;
         var _loc8_:Number = (_loc7_ = param1.main.overallScale) * param3;
         var _loc9_:uint = Math.ceil(_loc6_.width * _loc8_);
         var _loc10_:uint;
         if(!(_loc10_ = Math.ceil(_loc6_.height * _loc8_)) || !_loc9_)
         {
            return _loc4_;
         }
         var _loc11_:BitmapData;
         (_loc11_ = new BitmapData(_loc9_,_loc10_,true,0)).drawWithQuality(_loc5_,new Matrix(_loc8_,0,0,_loc8_,-_loc6_.x * _loc8_,-_loc6_.y * _loc8_),null,null,null,false,StageQuality.HIGH);
         _loc4_.bitmapData = _loc11_;
         var _loc12_:Number = 1 / _loc8_;
         _loc4_.x = _loc6_.x * param3;
         _loc4_.y = _loc6_.y * param3;
         _loc4_.scaleX = _loc12_;
         _loc4_.scaleY = _loc12_;
         return _loc4_;
      }
      
      public static function method_16(param1:String, param2:Boolean = false) : MovieClip
      {
         var _loc3_:MovieClip = null;
         var _loc5_:Class = null;
         var _loc4_:ApplicationDomain;
         if(!(_loc4_ = ApplicationDomain.currentDomain).hasDefinition(param1))
         {
            _loc3_ = new MovieClip();
         }
         else
         {
            _loc3_ = new (_loc5_ = _loc4_.getDefinition(param1) as Class)();
         }
         method_276(_loc3_,param2);
         return _loc3_;
      }
      
      public static function method_276(param1:DisplayObjectContainer, param2:Boolean = false) : void
      {
         var _loc3_:TextField = null;
         var _loc4_:DisplayObject = null;
         var _loc5_:DisplayObjectContainer = null;
         if(!param2)
         {
            param1.mouseEnabled = false;
            param1.mouseChildren = false;
         }
         var _loc6_:uint = uint(param1.numChildren);
         var _loc7_:uint = 0;
         while(_loc7_ < _loc6_)
         {
            _loc3_ = (_loc4_ = param1.getChildAt(_loc7_)) as TextField;
            if(_loc3_)
            {
               _loc3_.embedFonts = true;
               _loc3_.antiAliasType = AntiAliasType.ADVANCED;
            }
            else if(_loc5_ = _loc4_ as DisplayObjectContainer)
            {
               method_276(_loc5_,param2);
            }
            _loc7_++;
         }
      }
      
      public function method_1085() : void
      {
         var _loc1_:class_32 = null;
         for each(_loc1_ in this.var_1240)
         {
            _loc1_.method_448();
         }
         this.var_1240 = null;
         this.mActiveScreens = null;
         this.var_1 = null;
      }
      
      private function method_617(param1:MouseEvent) : void
      {
         this.var_981 = true;
         param1.stopPropagation();
      }
      
      private function method_606(param1:MouseEvent) : void
      {
         this.var_981 = false;
         param1.stopPropagation();
      }
      
      private function method_373(param1:MouseEvent) : void
      {
         param1.stopPropagation();
      }
      
      public function method_22(param1:Class) : class_32
      {
         var _loc2_:class_32 = new param1(this.var_1);
         this.var_1240.push(_loc2_);
         _loc2_.var_1450 = this.var_1240.length;
         return _loc2_;
      }
      
      public function method_1338() : void
      {
         this.var_1240.fixed = true;
      }
      
      public function method_990(param1:String) : MovieClip
      {
         var _loc2_:MovieClip = method_16(param1,true);
         _loc2_.addEventListener(MouseEvent.ROLL_OVER,this.method_617);
         _loc2_.addEventListener(MouseEvent.ROLL_OUT,this.method_606);
         _loc2_.addEventListener(MouseEvent.MOUSE_DOWN,this.method_373);
         _loc2_.addEventListener(MouseEvent.RIGHT_MOUSE_DOWN,this.method_373);
         return _loc2_;
      }
      
      public function method_1999(param1:MovieClip) : void
      {
         param1.removeEventListener(MouseEvent.ROLL_OVER,this.method_617);
         param1.removeEventListener(MouseEvent.ROLL_OUT,this.method_606);
         param1.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_373);
         param1.removeEventListener(MouseEvent.RIGHT_MOUSE_DOWN,this.method_373);
      }
      
      public function method_1045() : void
      {
         var _loc1_:class_32 = null;
         var _loc2_:int = int(this.mActiveScreens.length - 1);
         while(_loc2_ >= 0)
         {
            _loc1_ = this.mActiveScreens[_loc2_];
            if(_loc1_.mbHideOnClear)
            {
               _loc1_.Hide();
            }
            _loc2_--;
         }
      }
      
      public function method_249() : void
      {
         var _loc1_:class_32 = null;
         var _loc2_:int = int(this.mActiveScreens.length - 1);
         while(_loc2_ >= 0)
         {
            _loc1_ = this.mActiveScreens[_loc2_];
            _loc1_.method_434();
            _loc2_--;
         }
      }
      
      public function method_1688() : Boolean
      {
         return this.var_1983;
      }
   }
}
