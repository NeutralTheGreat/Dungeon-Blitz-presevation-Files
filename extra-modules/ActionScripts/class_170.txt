package
{
   import flash.geom.Point;
   
   public class class_170 extends class_167
   {
      
      public static const const_700:int = 4000;
      
      public static const const_850:int = 9000;
      
      public static const const_628:int = 100;
      
      public static const const_1195:int = 250;
      
      public static const const_1162:int = const_1195 - const_628;
      
      public static const const_1006:int = 100;
      
      public static const const_1084:int = 300;
       
      
      internal var var_1361:uint = 0;
      
      internal var var_1255:int;
      
      internal var var_1019:int;
      
      internal var var_2053:int;
      
      internal var var_2376:int;
      
      internal var var_1852:Boolean;
      
      internal var var_1963:Boolean;
      
      public function class_170(param1:Entity, param2:String = "WanderingPet")
      {
         super(param1,param2);
         var _loc3_:Point = new Point(0,4000);
         var _loc4_:Point = new Point(e.appearPosX + _loc3_.x,e.appearPosY + _loc3_.y);
         var _loc5_:class_37 = var_1.collMan.getFloorCollision(0,e.appearPosX,e.appearPosY + 1,_loc3_,_loc4_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0);
         this.var_2053 = Math.max(_loc5_.endY,_loc5_.startY) - const_1006;
         this.var_2376 = this.var_2053 - const_1084;
      }
      
      override public function TickState() : Class
      {
         var _loc3_:int = 0;
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         var _loc6_:* = false;
         var _loc7_:* = false;
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         var _loc1_:Entity = var_1.clientEnt;
         if(e.bSmackingAWallOrCeiling)
         {
            if(e.bLeftFacing)
            {
               this.var_1963 = true;
            }
            else
            {
               this.var_1852 = true;
            }
         }
         var _loc2_:uint = uint(var_1.mTimeThisTick);
         if(_loc2_ >= this.var_1361)
         {
            _loc3_ = Math.random() * (const_850 - const_700) + const_700;
            this.var_1361 = _loc2_ + _loc3_;
            _loc4_ = this.method_1299();
            _loc5_ = Math.random();
            _loc6_ = Math.random() > 0.5;
            _loc7_ = Math.random() > 0.5;
            _loc8_ = _loc6_ ? _loc5_ * _loc4_ : _loc5_ * _loc4_ * -1;
            _loc9_ = _loc7_ ? (1 - _loc5_) * _loc4_ : (1 - _loc5_) * _loc4_ * -1;
            this.var_1255 = e.physPosX + _loc8_;
            this.var_1019 = e.physPosY + _loc9_;
            if(this.var_1963 && e.physPosX > this.var_1255)
            {
               this.var_1255 = _loc8_ > 0 ? int(e.physPosX + _loc8_) : int(e.physPosX - _loc8_);
            }
            else if(this.var_1852 && e.physPosX < this.var_1255)
            {
               this.var_1255 = _loc8_ > 0 ? int(e.physPosX - _loc8_) : int(e.physPosX + _loc8_);
            }
            if(this.var_1852 || this.var_1963)
            {
               this.var_1852 = false;
               this.var_1963 = false;
            }
            if(this.var_1019 > this.var_2053 || this.var_1019 < this.var_2376)
            {
               this.var_1019 = e.physPosY - _loc9_;
            }
            else if(this.var_1019 < this.var_2376)
            {
               this.var_1019 = e.physPosY + _loc9_;
            }
            e.gotoLocationX = this.var_1255;
            e.gotoLocationY = this.var_1019;
            e.bGotoLocation = true;
         }
         return null;
      }
      
      public function method_1299() : Number
      {
         return Math.random() * const_1162 + const_628;
      }
      
      public function method_2029() : Number
      {
         return 2 * Math.PI * Math.random();
      }
   }
}
