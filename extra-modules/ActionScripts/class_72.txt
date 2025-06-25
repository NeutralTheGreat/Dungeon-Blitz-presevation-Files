package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.MovieClip;
   import flash.display.PixelSnapping;
   import flash.display.Sprite;
   import flash.display.StageQuality;
   import flash.geom.Matrix;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   
   public class class_72
   {
      
      internal static var var_1236:Array = new Array();
      
      internal static var var_970:uint = 0;
      
      internal static var var_1506:Boolean = false;
      
      internal static var var_1112:MovieClip;
      
      internal static var var_1744:Sprite;
       
      
      internal var var_1:Game;
      
      internal var var_62:Sprite;
      
      internal var var_1916:SuperAnimInstance;
      
      internal var var_2727:Number;
      
      internal var var_514:Number = 5;
      
      internal var var_2225:Number = 0;
      
      internal var var_847:Number = 200;
      
      internal var var_1053:Number = 400;
      
      internal var var_2061:Number = 0;
      
      internal var var_2642:Boolean = false;
      
      internal var var_784:int = 0;
      
      internal var scale:Number = 1;
      
      internal var var_1344:Boolean = false;
      
      public function class_72(param1:Game, param2:String, param3:Number, param4:Number, param5:uint, param6:Number, param7:Boolean, param8:MovieClip = null, param9:SuperAnimInstance = null, param10:uint = 0)
      {
         super();
         this.var_1 = param1;
         this.var_2727 = this.var_1.mTimeThisTick;
         this.scale = param6;
         if(param8)
         {
            param8.mouseChildren = false;
            param8.mouseEnabled = false;
            this.var_62 = param8;
            this.var_1916 = param9;
            this.var_62.scaleX = this.var_62.scaleY = this.scale;
            this.var_62.x = 0;
            this.var_62.y = 0;
         }
         else
         {
            this.var_62 = new Sprite();
            this.var_62.mouseChildren = false;
            this.var_62.mouseEnabled = false;
            this.var_62.addChild(this.method_1943(param2,this.scale,param5));
         }
         this.var_62.x = param3;
         this.var_62.y = param4;
         if(param7)
         {
            this.var_1.var_272.addChild(this.var_62);
         }
         else
         {
            this.var_1.var_89.addChild(this.var_62);
         }
         this.var_2061 = param10;
      }
      
      public function method_1943(param1:String, param2:Number, param3:uint) : Bitmap
      {
         var _loc7_:TextField = null;
         var _loc8_:Rectangle = null;
         var _loc9_:Matrix = null;
         var _loc10_:Number = NaN;
         var _loc4_:BitmapData = null;
         var _loc5_:String = null;
         if(param1.length < 6 && param2 < 2)
         {
            _loc5_ = param1 + ":" + param2 + ":" + param3;
            _loc4_ = var_1236[_loc5_];
            this.var_1344 = false;
         }
         else
         {
            this.var_1344 = true;
         }
         if(!_loc4_)
         {
            if(!var_1112)
            {
               var_1112 = class_4.method_16("a_ScoreFloater");
               var_1744 = new Sprite();
               var_1744.addChild(var_1112);
            }
            (_loc7_ = var_1112["am_FloatText"]).textColor = param3;
            _loc7_.x = 0;
            _loc7_.y = 0;
            _loc7_.width = 0;
            _loc7_.height = 0;
            _loc7_.scaleX = param2 * this.var_1.main.overallScale;
            _loc7_.scaleY = param2 * this.var_1.main.overallScale;
            _loc7_.autoSize = TextFieldAutoSize.LEFT;
            _loc7_.wordWrap = false;
            MathUtil.method_2(_loc7_,param1);
            _loc7_.autoSize = TextFieldAutoSize.LEFT;
            _loc7_.antiAliasType = "advanced";
            _loc7_.autoSize = TextFieldAutoSize.LEFT;
            _loc8_ = _loc7_.getBounds(var_1112.parent);
            (_loc9_ = new Matrix()).tx = -_loc8_.x;
            _loc9_.ty = -_loc8_.y;
            _loc10_ = 4 * this.var_1.main.overallScale;
            (_loc4_ = new BitmapData(_loc7_.width + _loc10_,_loc7_.height + _loc10_,true,0)).drawWithQuality(var_1744,_loc9_,null,null,null,true,StageQuality.HIGH);
            if(!this.var_1344)
            {
               var_1236[_loc5_] = _loc4_;
               var_970 += _loc4_.height * _loc4_.width * 4;
            }
         }
         var _loc6_:Bitmap = new Bitmap(_loc4_,PixelSnapping.ALWAYS,true);
         _loc6_.scaleX = _loc6_.scaleY = 1 / this.var_1.main.overallScale;
         _loc6_.x = int(-_loc6_.width / 2);
         _loc6_.y = int(-_loc6_.height / 1.2);
         return _loc6_;
      }
      
      public function method_963() : void
      {
         var _loc1_:Bitmap = null;
         if(this.var_1344)
         {
            _loc1_ = this.var_62.getChildAt(0) as Bitmap;
            _loc1_.bitmapData.dispose();
         }
         if(this.var_1916)
         {
            this.var_1916.DestroySuperAnimInstance();
         }
         this.var_1916 = null;
         if(Boolean(this.var_62) && Boolean(this.var_62.parent))
         {
            this.var_62.parent.removeChild(this.var_62);
         }
         this.var_62 = null;
         this.var_1 = null;
      }
      
      public function method_1939() : Boolean
      {
         var _loc1_:Number = this.var_1.mTimeThisTick - this.var_2727 - this.var_2061;
         if(_loc1_ < this.var_2061)
         {
            return true;
         }
         if(_loc1_ > this.var_847)
         {
            this.var_62.alpha = 1 - (_loc1_ - this.var_847) / (this.var_1053 - this.var_847);
         }
         this.var_62.y -= this.var_1.TIMESTEP * this.var_514;
         this.var_514 -= this.var_2225 * this.var_1.TIMESTEP;
         if(this.var_2642)
         {
            ++this.var_784;
            if(this.var_784 >= 6)
            {
               this.var_62.scaleX = this.var_62.scaleY = 1;
            }
            else if(this.var_784 == 5)
            {
               this.var_62.scaleX = this.var_62.scaleY = 1.7 / 1.3;
            }
            else if(this.var_784 == 4)
            {
               this.var_62.scaleX = this.var_62.scaleY = 2.11 / 1.3;
            }
            else if(this.var_784 == 3)
            {
               this.var_62.scaleX = this.var_62.scaleY = 2.5 / 1.3;
            }
            else if(this.var_784 == 2)
            {
               this.var_62.scaleX = this.var_62.scaleY = 1.75 / 1.3;
            }
            else if(this.var_784 == 1)
            {
               this.var_62.scaleX = this.var_62.scaleY = 1 / 1.3;
            }
         }
         if(this.var_514 < 0)
         {
            this.var_514 = 0;
         }
         return _loc1_ <= this.var_1053;
      }
   }
}
