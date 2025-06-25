package
{
   import flash.geom.Point;
   
   public class class_37
   {
      
      public static const const_439:uint = 1 << 0;
      
      public static const const_464:uint = 1 << 1;
      
      public static const const_782:uint = 1 << 2;
      
      public static const const_704:uint = 1 << 3;
      
      public static const const_786:uint = 1 << 4;
      
      public static const const_706:uint = 1 << 5;
      
      public static const const_638:uint = 1 << 6;
       
      
      internal var var_2610:Number;
      
      internal var var_2708:Number;
      
      internal var var_2493:Number;
      
      internal var var_2826:Number;
      
      internal var var_2952:Number;
      
      internal var var_2955:Number;
      
      internal var startX:Number;
      
      internal var startY:Number;
      
      internal var endX:Number;
      
      internal var endY:Number;
      
      internal var var_2914:Boolean;
      
      internal var type:uint;
      
      internal var room:Room;
      
      internal var bDisabled:Boolean;
      
      internal var var_120:uint;
      
      internal var var_573:Vector.<String>;
      
      internal var var_941:int;
      
      internal var var_2286:int;
      
      internal var var_2886:Point;
      
      public function class_37(param1:Point, param2:Point, param3:uint, param4:uint, param5:Vector.<String>, param6:Room, param7:int, param8:uint)
      {
         super();
         this.startX = param1.x;
         this.startY = param1.y;
         this.endX = param2.x;
         this.endY = param2.y;
         this.type = param3;
         this.var_120 = param4;
         this.var_573 = param5;
         this.room = param6;
         this.var_941 = param7;
         this.var_2286 = param8;
      }
      
      public function method_1778() : void
      {
         this.var_573 = null;
         this.room = null;
         this.var_2886 = null;
      }
   }
}
