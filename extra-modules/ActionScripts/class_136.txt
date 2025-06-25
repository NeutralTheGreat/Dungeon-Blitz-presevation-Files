package
{
   import flash.display.MovieClip;
   import flash.events.*;
   
   public class class_136
   {
      
      internal static var var_783:MovieClip;
       
      
      public function class_136()
      {
         super();
      }
      
      public static function method_305(param1:MouseEvent) : void
      {
         var _loc3_:Function = null;
         var _loc4_:Function = null;
         var _loc2_:MovieClip = var_783;
         if(_loc2_)
         {
            _loc2_.removeEventListener(MouseEvent.MOUSE_MOVE,method_508);
            if(_loc2_.db_SliderCommitCallback)
            {
               _loc3_ = _loc2_.db_SliderCommitCallback;
               _loc4_ = _loc2_.db_ReadSlider;
               _loc3_(_loc4_(_loc2_));
            }
            var_783 = null;
         }
      }
      
      public static function method_874(param1:MouseEvent) : void
      {
      }
      
      public static function method_755(param1:MouseEvent) : void
      {
         method_305(param1);
         var _loc2_:MovieClip = param1.target as MovieClip;
         _loc2_.removeEventListener(MouseEvent.MOUSE_MOVE,method_508);
         if(var_783)
         {
            var_783 = null;
         }
      }
      
      public static function method_508(param1:MouseEvent) : void
      {
         var _loc3_:Function = null;
         var _loc4_:Function = null;
         var _loc2_:MovieClip = param1.target as MovieClip;
         method_388(_loc2_,param1.localX,param1.localY);
         if(_loc2_.db_SliderChangeCallback)
         {
            _loc3_ = _loc2_.db_SliderChangeCallback;
            _loc4_ = _loc2_.db_ReadSlider;
            _loc3_(_loc4_(_loc2_));
         }
      }
      
      public static function method_372(param1:MouseEvent) : void
      {
         var _loc3_:Function = null;
         var _loc4_:Function = null;
         var _loc2_:MovieClip = param1.target as MovieClip;
         var_783 = _loc2_;
         _loc2_.addEventListener(MouseEvent.MOUSE_MOVE,method_508);
         method_388(_loc2_,param1.localX,param1.localY);
         if(_loc2_.db_SliderChangeCallback)
         {
            _loc3_ = _loc2_.db_SliderChangeCallback;
            _loc4_ = _loc2_.db_ReadSlider;
            _loc3_(_loc4_(_loc2_));
         }
      }
      
      public static function method_388(param1:MovieClip, param2:Number, param3:Number) : void
      {
         var _loc4_:Function = null;
         var _loc5_:Number = NaN;
         param1.am_Knob.x = Math.min(Math.max(param2,param1.am_KnobStart.x),param1.am_KnobEnd.x);
         param1.am_Knob.y = Math.min(Math.max(param3,param1.am_KnobStart.y),param1.am_KnobEnd.y);
         if(param1.db_Snap)
         {
            _loc5_ = (_loc4_ = param1.db_ReadSlider)(param1);
            _loc5_ = Math.round(_loc5_ / param1.db_Snap) * param1.db_Snap;
            method_330(param1,_loc5_);
         }
      }
      
      public static function method_330(param1:MovieClip, param2:Number) : void
      {
         param1.am_Knob.x = param1.am_KnobStart.x + (param1.am_KnobEnd.x - param1.am_KnobStart.x) * param2;
         param1.am_Knob.y = param1.am_KnobStart.y + (param1.am_KnobEnd.y - param1.am_KnobStart.y) * param2;
      }
      
      public static function method_1320(param1:MovieClip) : Number
      {
         var _loc2_:Number = (param1.am_Knob.x - param1.am_KnobStart.x) / (param1.am_KnobEnd.x - param1.am_KnobStart.x);
         return Math.max(Math.min(_loc2_,1),0);
      }
      
      public static function method_1995(param1:MovieClip) : Number
      {
         var _loc2_:Number = (param1.am_Knob.y - param1.am_KnobStart.y) / (param1.am_KnobEnd.y - param1.am_KnobStart.y);
         return Math.max(Math.min(_loc2_,1),0);
      }
      
      public static function method_1078(param1:MovieClip, param2:Function, param3:Function, param4:Number = 0, param5:Boolean = false) : void
      {
         param1.mouseChildren = false;
         param1.am_KnobStart.visible = false;
         param1.am_KnobEnd.visible = false;
         param1.db_SliderCommitCallback = param2;
         param1.db_SliderChangeCallback = param3;
         param1.db_Snap = param4;
         param1.db_ReadSlider = param5 ? method_1995 : method_1320;
         param1.addEventListener(MouseEvent.MOUSE_UP,method_305);
         param1.addEventListener(MouseEvent.ROLL_OVER,method_874);
         param1.addEventListener(MouseEvent.ROLL_OUT,method_755);
         param1.addEventListener(MouseEvent.MOUSE_DOWN,method_372);
         param1.addEventListener(MouseEvent.RIGHT_MOUSE_DOWN,method_372);
      }
      
      public static function method_1536(param1:MovieClip) : void
      {
         param1.filters = [];
         param1.db_SliderCommitCallback = null;
         param1.db_SliderChangeCallback = null;
         param1.db_ReadSlider = null;
         param1.removeEventListener(MouseEvent.MOUSE_UP,method_305);
         param1.removeEventListener(MouseEvent.ROLL_OVER,method_874);
         param1.removeEventListener(MouseEvent.ROLL_OUT,method_755);
         param1.removeEventListener(MouseEvent.MOUSE_DOWN,method_372);
         param1.removeEventListener(MouseEvent.RIGHT_MOUSE_DOWN,method_372);
      }
   }
}
