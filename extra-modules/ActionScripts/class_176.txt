package
{
   public class class_176 extends class_167
   {
      
      public static const const_1102:int = 200;
      
      public static const const_846:int = 250;
      
      public static const const_918:int = 120;
      
      public static const const_855:int = 200;
      
      public static const const_1051:int = 30;
      
      public static const const_848:int = 250;
      
      public static const const_1082:int = 5;
       
      
      internal var var_1361:uint = 0;
      
      public function class_176(param1:Entity, param2:String = "FloatingPetFollow")
      {
         super(param1,param2);
      }
      
      override public function TickState() : Class
      {
         var _loc12_:* = false;
         var _loc1_:Entity = var_1.GetEntFromID(e.summonerId);
         if(!_loc1_ || !_loc1_.bIAmValid)
         {
            return null;
         }
         var _loc2_:uint = uint(var_1.mTimeThisTick);
         if(_loc2_ >= this.var_1361)
         {
            this.var_1361 = _loc2_ + (!!e.behaviorType.bSlowOnTheUptake ? 4000 : 2000);
            e.bLeft = e.physPosX > _loc1_.physPosX;
         }
         var _loc3_:Number = e.physPosX - _loc1_.physPosX;
         var _loc4_:Number = e.physPosY - _loc1_.physPosY;
         var _loc5_:Number = _loc3_ > 0 ? _loc3_ : -_loc3_;
         var _loc6_:Number = _loc4_ > 0 ? _loc4_ : -_loc4_;
         if((_loc5_ >= 600 || _loc6_ >= 400) && !var_1.PointOnScreenWithinDist(e.physPosX,e.physPosY,0,0))
         {
            e.TeleportTo(_loc1_.physPosX,_loc1_.physPosY);
            return null;
         }
         var _loc7_:Number = _loc1_.maxSpeed;
         if(_loc5_ > const_848)
         {
            _loc7_ += const_1082;
         }
         if(e.maxSpeed != _loc7_)
         {
            e.maxSpeed = _loc7_;
         }
         var _loc8_:*;
         var _loc9_:Number = (_loc8_ = _loc1_.combatState.var_270 != null) ? const_855 : const_918;
         var _loc10_:Number = _loc8_ ? const_846 : const_1102;
         if(e.bRunning)
         {
            _loc10_ -= const_1051;
         }
         if(_loc3_ >= -_loc10_ && _loc3_ <= _loc10_)
         {
            e.bRunning = false;
         }
         else
         {
            e.bRunning = true;
            e.bLeft = _loc3_ > 0;
         }
         var _loc11_:int;
         if(!(_loc11_ = _loc1_.physPosY - _loc9_) || Boolean(brain.CloseEnoughToStop(e.velocity.y,e.physPosY,_loc11_)))
         {
            e.bJumping = false;
            e.bDropping = false;
         }
         else
         {
            _loc12_ = e.physPosY > _loc11_;
            e.bJumping = _loc12_;
            e.bDropping = !_loc12_;
         }
         return null;
      }
   }
}
