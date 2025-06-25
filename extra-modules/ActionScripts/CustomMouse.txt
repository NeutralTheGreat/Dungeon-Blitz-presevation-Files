package
{
   import flash.display.BitmapData;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.display.StageQuality;
   import flash.geom.Matrix;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.ui.Mouse;
   import flash.ui.MouseCursor;
   import flash.ui.MouseCursorData;
   
   public class CustomMouse
   {
       
      
      internal var var_1:Game;
      
      internal var var_2002:String;
      
      internal var var_2669:Boolean;
      
      public function CustomMouse(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1856() : void
      {
         this.var_1 = null;
      }
      
      public function method_66(param1:String) : void
      {
         var _loc2_:MovieClip = class_4.method_16(param1);
         var _loc3_:Sprite = new Sprite();
         _loc3_.addChild(_loc2_);
         var _loc4_:Rectangle = _loc2_.getBounds(_loc3_);
         var _loc5_:Matrix = new Matrix(1,0,0,1,-_loc4_.x,-_loc4_.y);
         var _loc6_:BitmapData;
         (_loc6_ = new BitmapData(32,32,true,0)).drawWithQuality(_loc3_,_loc5_,null,null,null,false,StageQuality.HIGH);
         var _loc7_:MouseCursorData = new MouseCursorData();
         var _loc8_:Vector.<BitmapData>;
         (_loc8_ = new Vector.<BitmapData>(1,true))[0] = _loc6_;
         _loc7_.hotSpot = new Point(-_loc4_.x,-_loc4_.y);
         _loc7_.data = _loc8_;
         Mouse.registerCursor(param1,_loc7_);
      }
      
      public function method_2003() : void
      {
         if(!this.var_2669)
         {
            if(!this.var_1.method_1004())
            {
               return;
            }
            this.var_2669 = true;
         }
         var _loc1_:String = this.var_1.method_1416();
         if(_loc1_ != this.var_2002)
         {
            this.var_2002 = _loc1_;
            Mouse.cursor = !!this.var_2002 ? this.var_2002 : MouseCursor.AUTO;
         }
      }
   }
}
