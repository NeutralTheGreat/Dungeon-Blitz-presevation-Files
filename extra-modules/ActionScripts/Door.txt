package
{
   import flash.geom.Rectangle;
   
   public class Door
   {
      
      private static var STATE_ITERATOR:uint = 0;
      
      public static const DOORSTATE_CLOSED:uint = STATE_ITERATOR++;
      
      public static const DOORSTATE_STATIC:uint = STATE_ITERATOR++;
      
      public static const DOORSTATE_MISSION:uint = STATE_ITERATOR++;
      
      public static const DOORSTATE_MISSIONREPEAT:uint = STATE_ITERATOR++;
      
      public static const DOORSTATE_LOCKED:uint = STATE_ITERATOR++;
      
      public static const const_632:uint = 2 * Camera.SCREEN_WIDTH;
      
      public static const const_62:uint = 200;
       
      
      internal var posX:Number;
      
      internal var posY:Number;
      
      internal var var_443:Rectangle;
      
      internal var bFacingLeft:Boolean;
      
      internal var doorID:uint;
      
      internal var localTarget:String;
      
      internal var var_2504:String;
      
      internal var var_2280:Number = 0;
      
      internal var var_2285:Number = 0;
      
      internal var var_2326:Boolean = false;
      
      internal var var_1260:String = null;
      
      internal var doorState:uint;
      
      internal var var_2671:uint = 0;
      
      internal var var_517:class_33 = null;
      
      internal var bDisabled:Boolean = false;
      
      public function Door(param1:String, param2:Number, param3:Number, param4:Rectangle, param5:uint, param6:String, param7:Boolean = false)
      {
         this.doorState = DOORSTATE_CLOSED;
         super();
         this.posX = param2;
         this.posY = param3;
         this.var_443 = param4;
         this.doorID = param5;
         this.localTarget = param6;
         this.var_2504 = param1;
         this.bFacingLeft = param7;
         if(this.doorID >= class_11.const_1218)
         {
            this.bDisabled = true;
         }
      }
      
      public function method_791() : void
      {
         if(this.var_517)
         {
            this.var_517.method_42();
            this.var_517.DestroyUIMovieClip();
            this.var_517 = null;
         }
         this.var_443 = null;
         this.localTarget = null;
      }
   }
}
