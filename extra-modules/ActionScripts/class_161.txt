package
{
   import flash.geom.Point;
   
   public class class_161
   {
      
      private static const const_1383:Number = 5;
       
      
      internal var var_1:Game;
      
      internal var var_2897:String;
      
      internal var var_778:SuperAnimInstance;
      
      internal var var_475:Vector.<class_37>;
      
      private var bDisabled:Boolean;
      
      public function class_161(param1:Game, param2:String, param3:SuperAnimInstance)
      {
         super();
         this.var_1 = param1;
         this.bDisabled = false;
         this.var_778 = param3;
         this.var_2897 = param2;
      }
      
      public function method_1053() : void
      {
         this.var_778 = null;
         this.var_475 = null;
      }
      
      public function method_1259() : Boolean
      {
         var _loc2_:Point = null;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:class_37 = null;
         if(this.bDisabled)
         {
            return false;
         }
         var _loc1_:Point = !!this.var_778.m_Seq.var_314 ? this.var_778.m_Seq.var_314.var_1813 : null;
         if(_loc1_ != null && Boolean(this.var_475))
         {
            _loc2_ = this.var_778.m_TheDO.transform.matrix.transformPoint(_loc1_);
            _loc3_ = this.var_475.length;
            _loc4_ = 0;
            while(_loc4_ < _loc3_)
            {
               _loc5_ = this.var_475[_loc4_];
               _loc5_.var_2952 = _loc5_.startX;
               _loc5_.var_2955 = _loc5_.startY;
               _loc5_.startX = _loc5_.var_2610 + _loc2_.x;
               _loc5_.startY = _loc5_.var_2708 + _loc2_.y;
               _loc5_.endX = _loc5_.var_2493 + _loc2_.x;
               _loc5_.endY = _loc5_.var_2826 + _loc2_.y;
               _loc4_++;
            }
         }
         return true;
      }
      
      public function method_2097(param1:Vector.<class_37>) : void
      {
         var _loc7_:class_37 = null;
         this.var_475 = param1;
         var _loc2_:class_28 = this.var_778.m_Seq.var_30.var_604[0];
         if(!_loc2_)
         {
            _loc2_ = this.var_778.m_Seq.var_30.method_242(0);
         }
         var _loc3_:Point = _loc2_.var_1813;
         var _loc4_:Point = this.var_778.m_TheDO.transform.matrix.transformPoint(_loc3_);
         var _loc5_:uint = this.var_475.length;
         var _loc6_:uint = 0;
         while(_loc6_ < _loc5_)
         {
            _loc7_ = this.var_475[_loc6_];
            _loc7_.var_2610 = _loc7_.startX - _loc4_.x;
            _loc7_.var_2708 = _loc7_.startY - _loc4_.y;
            _loc7_.var_2493 = _loc7_.endX - _loc4_.x;
            _loc7_.var_2826 = _loc7_.endY - _loc4_.y;
            _loc6_++;
         }
      }
      
      public function method_2062() : void
      {
         var _loc1_:uint = this.var_475.length;
         var _loc2_:uint = 0;
         while(_loc2_ < _loc1_)
         {
            this.var_475[_loc2_].bDisabled = true;
            _loc2_++;
         }
         this.bDisabled = true;
      }
      
      public function method_2006() : void
      {
         var _loc1_:uint = this.var_475.length;
         var _loc2_:uint = 0;
         while(_loc2_ < _loc1_)
         {
            this.var_475[_loc2_].bDisabled = false;
            _loc2_++;
         }
         this.bDisabled = false;
      }
   }
}
