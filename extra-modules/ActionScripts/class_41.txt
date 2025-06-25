package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.PixelSnapping;
   import flash.display.Sprite;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.utils.Dictionary;
   
   public class class_41
   {
      
      private static const const_567:Sprite = new Sprite();
      
      private static const const_271:Bitmap = new Bitmap(null,PixelSnapping.AUTO);
      
      private static const const_1004:Point = new Point();
      
      private static const const_226:Rectangle = new Rectangle();
      
      private static const const_1184:uint = 100;
      
      private static const const_801:Dictionary = new Dictionary();
      
      private static const const_699:uint = 30;
      
      private static var var_1108:Vector.<Bitmap> = new Vector.<Bitmap>();
      
      private static var var_785:uint = 0;
       
      
      public function class_41()
      {
         super();
      }
      
      public static function method_860(param1:String, param2:GfxType, param3:Number) : GfxType
      {
         var _loc5_:GfxType = null;
         var _loc4_:String = param1 + param3;
         if(!(_loc5_ = const_801[_loc4_]))
         {
            (_loc5_ = param2.GetDuplicate()).animScale = param3;
            _loc5_.var_947 = "Icon";
            _loc5_.baseAnim = "Icon";
            _loc5_.var_177 = 0.1;
            _loc5_.bFireAndForget = true;
            const_801[param1] = _loc5_;
         }
         return _loc5_;
      }
      
      public static function method_85(param1:class_7, param2:Number, param3:Number, param4:uint, param5:uint, param6:Number, param7:Number = 1) : Bitmap
      {
         var _loc8_:Bitmap = new Bitmap(null,PixelSnapping.AUTO);
         var _loc9_:EntType;
         if(!(_loc9_ = EntType.method_48("Pet" + param1.var_310)))
         {
            class_24.method_19("Missing Pet Entity: Pet" + param1.var_310);
            return _loc8_;
         }
         return method_374(_loc9_,_loc8_,param2,param3,param4,param5,param6,param7);
      }
      
      public static function method_168(param1:class_20, param2:Number, param3:Number, param4:uint, param5:uint, param6:Number, param7:Number = 1) : Bitmap
      {
         var _loc8_:Bitmap = new Bitmap(null,PixelSnapping.AUTO);
         var _loc9_:EntType;
         if(!(_loc9_ = EntType.method_48(param1.var_566)))
         {
            class_24.method_19("Missing Mount Entity: " + param1.var_566);
            return _loc8_;
         }
         return method_374(_loc9_,_loc8_,param2,param3,param4,param5,param6,param7);
      }
      
      private static function method_374(param1:EntType, param2:Bitmap, param3:Number, param4:Number, param5:uint, param6:uint, param7:Number, param8:Number) : Bitmap
      {
         var _loc9_:GfxType = method_860(param1.entName,param1.gfxType,param5 / const_1184 * param8);
         var _loc12_:class_26;
         var _loc11_:class_30;
         var _loc10_:SuperAnimData;
         if(!(_loc12_ = (_loc11_ = (_loc10_ = SuperAnimData.method_939(_loc9_)).var_71).var_69["Icon"]))
         {
            class_24.method_19("Missing Icon Frame for Entity: " + param1.entName);
            return param2;
         }
         var _loc13_:class_28;
         if(!(_loc13_ = _loc12_.var_604[0]))
         {
            _loc13_ = _loc12_.method_242(0);
         }
         var _loc14_:Number = Math.ceil(param5 * param7 * param8);
         var _loc15_:Number = Math.ceil(param6 * param7 * param8);
         var _loc16_:BitmapData = new BitmapData(_loc14_,_loc15_,true,0);
         _loc10_.method_866(_loc12_,_loc13_,const_567,const_271,1);
         const_226.x = -const_271.x;
         const_226.width = _loc14_;
         const_226.y = -const_271.y;
         const_226.height = _loc15_;
         _loc16_.copyPixels(const_271.bitmapData,const_226,const_1004);
         while(const_567.numChildren)
         {
            const_567.removeChildAt(0);
         }
         const_271.bitmapData = null;
         var _loc17_:Number = 1 / (param7 * param8);
         param2.x = param3;
         param2.y = param4;
         param2.scaleX = _loc17_;
         param2.scaleY = _loc17_;
         param2.bitmapData = _loc16_;
         var_1108.push(param2);
         return param2;
      }
      
      public static function method_1358() : void
      {
         var _loc1_:Bitmap = null;
         var _loc2_:int = var_1108.length - 1 - var_785;
         while(_loc2_ >= 0)
         {
            _loc1_ = var_1108[_loc2_];
            if(!_loc1_.parent)
            {
               if(_loc1_.bitmapData)
               {
                  _loc1_.bitmapData.dispose();
                  _loc1_.bitmapData = null;
               }
               var_1108.splice(_loc2_,1);
               _loc2_++;
            }
            _loc2_ -= const_699;
         }
         if(++var_785 >= const_699)
         {
            var_785 = 0;
         }
      }
   }
}
