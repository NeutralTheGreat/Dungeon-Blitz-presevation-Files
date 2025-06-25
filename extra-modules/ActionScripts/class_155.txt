package
{
   import flash.display.BitmapData;
   import flash.display.Graphics;
   import flash.display.Sprite;
   import flash.display.StageQuality;
   import flash.filters.GlowFilter;
   import flash.geom.Matrix;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   
   public class class_155
   {
      
      private static const const_670:Sprite = new Sprite();
      
      private static const const_520:Matrix = new Matrix();
      
      private static const const_177:TextField = new TextField();
      
      private static const const_463:Sprite = new Sprite();
      
      private static const const_351:uint = 5;
      
      private static const const_154:Vector.<uint> = new Vector.<uint>(const_351,true);
      
      private static const const_182:Vector.<uint> = new Vector.<uint>(const_351,true);
      
      private static const const_273:Vector.<uint> = new Vector.<uint>(const_351,true);
      
      {
         const_177.textColor = 16777215;
         const_177.scaleX = 1.5;
         const_177.scaleY = 1.5;
         const_177.filters = [new GlowFilter(0,1,4,4,10)];
         const_463.addChild(const_177);
         const_154[0] = 0;
         const_182[0] = 16777215;
         const_273[0] = 0;
         const_154[1] = 25;
         const_182[1] = 65280;
         const_273[1] = 0.2;
         const_154[2] = 50;
         const_182[2] = 16776960;
         const_273[2] = 0.4;
         const_154[3] = 100;
         const_182[3] = 16711680;
         const_273[3] = 0.6;
         const_154[4] = 200;
         const_182[4] = 8388736;
         const_273[4] = 0.8;
      }
      
      public function class_155()
      {
         super();
      }
      
      public static function method_1187(param1:BitmapData, param2:uint, param3:String, param4:Rectangle) : void
      {
         if(param2 < const_154[0])
         {
            return;
         }
         var _loc5_:uint = const_351 - 1;
         while(Boolean(_loc5_) && param2 < const_154[_loc5_])
         {
            _loc5_--;
         }
         var _loc6_:Graphics;
         (_loc6_ = const_670.graphics).clear();
         _loc6_.lineStyle(2,0);
         _loc6_.beginFill(const_182[_loc5_],0.3);
         if(param4)
         {
            _loc6_.drawRect(param4.x,param4.y,param4.width,param4.height);
         }
         else
         {
            _loc6_.drawRect(0,0,param1.width,param1.height);
         }
         _loc6_.endFill();
         param1.drawWithQuality(const_670,null,null,null,null,false,StageQuality.LOW);
         const_177.text = String(param2) + " ms, " + param3;
         if(!param4)
         {
            param1.drawWithQuality(const_463,null,null,null,null,false,StageQuality.LOW);
         }
         else
         {
            const_520.tx = param4.x;
            const_520.ty = param4.y;
            param1.drawWithQuality(const_463,const_520,null,null,null,false,StageQuality.LOW);
         }
      }
   }
}
