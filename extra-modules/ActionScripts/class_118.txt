package
{
   public class class_118
   {
      
      public static const const_43:uint = 27;
      
      public static const const_529:Array = new Array(5,2,3,5,5,3,2,3,2,5,2,3,5,5,3,2,3,2,5,2,3,5,5,3,2,3,2);
      
      public static const const_1304:uint = 90;
      
      public static const const_1246:uint = 65;
      
      public static const const_195:uint = 5;
      
      public static const const_127:uint = 6;
      
      public static const ABILITY6_POINTS_PREREQ:uint = 40;
      
      public static const ABILITY6_NODE_PREREQ:uint = 18;
      
      public static const ABILITY5_POINTS_PREREQ:uint = 20;
      
      public static const ABILITY5_NODE_PREREQ:uint = 8;
       
      
      internal var var_1:Game;
      
      internal var var_58:Vector.<class_148>;
      
      private var var_2964:uint;
      
      private var var_2974:uint;
      
      public function class_118(param1:Game)
      {
         super();
         this.var_1 = param1;
         this.var_58 = new Vector.<class_148>(const_43,true);
         var _loc2_:uint = 0;
         while(_loc2_ < const_43)
         {
            this.var_58[_loc2_] = new class_148(null,0);
            _loc2_++;
         }
      }
      
      public static function method_277(param1:uint) : uint
      {
         var _loc2_:uint = 0;
         var _loc3_:uint = uint(const_529[param1]);
         if(_loc3_ <= 2)
         {
            _loc2_ = 1;
         }
         if(_loc3_ <= 4)
         {
            _loc2_ = 2;
         }
         if(_loc3_ <= 5)
         {
            _loc2_ = 3;
         }
         return _loc2_;
      }
      
      public function method_213() : void
      {
         var _loc1_:uint = 0;
         while(_loc1_ < const_43)
         {
            this.var_58[_loc1_].DestroyTalentSlot();
            _loc1_++;
         }
         this.var_58 = null;
      }
      
      public function method_840(param1:Vector.<Object>) : void
      {
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:Object = null;
         var _loc5_:Packet = new Packet(LinkUpdater.const_1133);
         _loc4_ = 0;
         while(_loc4_ < const_43)
         {
            _loc3_ = this.var_58[_loc4_].mPointsSpent;
            if(_loc3_ > 0 && Boolean(this.var_58[_loc4_].mNodeType))
            {
               _loc5_.method_15(true);
               _loc6_ = method_277(_loc4_);
               _loc2_ = this.var_58[_loc4_].mNodeType.mNodeID;
               _loc5_.method_20(const_127,_loc2_);
               _loc5_.method_20(_loc6_,_loc3_ - 1);
            }
            else
            {
               _loc5_.method_15(false);
            }
            _loc4_++;
         }
         _loc4_ = 0;
         while(_loc4_ < param1.length)
         {
            _loc7_ = param1[_loc4_];
            _loc5_.method_15(true);
            if(_loc7_.actionType == class_83.const_492)
            {
               _loc5_.method_15(true);
               _loc5_.method_20(class_118.const_127,_loc7_.nodeIndex);
               _loc5_.method_20(class_118.const_127,_loc7_.signetGroup);
               _loc5_.method_20(class_118.const_127,_loc7_.signetIndex + 1);
            }
            else
            {
               _loc5_.method_15(false);
               _loc5_.method_20(class_118.const_127,_loc7_.nodeIndex);
            }
            _loc4_++;
         }
         _loc5_.method_15(false);
         this.var_1.serverConn.SendPacket(_loc5_);
      }
      
      public function toString() : String
      {
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc1_:String = "";
         var _loc2_:uint = 0;
         while(_loc2_ < class_118.const_43)
         {
            _loc3_ = uint(_loc2_ + 1);
            _loc4_ = 0;
            if(this.var_58[_loc2_].mNodeType)
            {
               _loc4_ = this.var_58[_loc2_].mNodeType.mNodeID;
            }
            _loc5_ = this.var_58[_loc2_].mPointsSpent;
            _loc1_ += "ID: " + _loc3_ + "(" + _loc4_ + ", " + _loc5_ + ")\n";
            _loc2_++;
         }
         return _loc1_;
      }
      
      public function method_338() : void
      {
         var _loc1_:class_148 = null;
         for each(_loc1_ in this.var_58)
         {
            _loc1_.method_338();
         }
      }
      
      private function method_191(param1:uint) : uint
      {
         if(param1 < 1)
         {
            return 0;
         }
         if(param1 < 10)
         {
            return param1 - 1;
         }
         if(param1 < 20)
         {
            return param1 - 2;
         }
         return param1 - 3;
      }
      
      public function method_1384() : Vector.<class_148>
      {
         return this.var_58;
      }
      
      public function method_93(param1:uint) : class_148
      {
         return this.var_58[this.method_191(param1)];
      }
      
      public function IsEmpty(param1:uint) : Boolean
      {
         return this.var_58[this.method_191(param1)].IsEmpty();
      }
      
      public function method_599() : Boolean
      {
         var _loc2_:class_148 = null;
         var _loc1_:uint = 0;
         while(_loc1_ < const_43)
         {
            _loc2_ = this.var_58[_loc1_];
            if(!_loc2_.IsEmpty())
            {
               return false;
            }
            _loc1_++;
         }
         return true;
      }
      
      public function method_676(param1:uint) : Boolean
      {
         var _loc2_:uint = this.method_191(param1);
         return this.var_58[_loc2_].GetPointsSpent() < const_529[_loc2_];
      }
      
      public function method_231() : int
      {
         return (!!this.var_1.clientEnt ? this.var_1.clientEnt.method_1494() : 0) - this.method_98();
      }
      
      public function method_98() : uint
      {
         var _loc2_:class_148 = null;
         var _loc1_:uint = 0;
         var _loc3_:uint = 0;
         while(_loc3_ < const_43)
         {
            _loc2_ = this.var_58[_loc3_];
            if(!_loc2_.IsEmpty())
            {
               _loc1_ += _loc2_.GetPointsSpent();
            }
            _loc3_++;
         }
         return _loc1_;
      }
      
      public function HasPendingNodeType(param1:uint) : Boolean
      {
         return this.var_58[this.method_191(param1)].HasPendingNodeType();
      }
      
      public function method_2107(param1:uint) : uint
      {
         return this.var_58[this.method_191(param1)].GetPointsSpent();
      }
      
      public function method_430(param1:uint) : uint
      {
         return const_529[this.method_191(param1)];
      }
      
      public function method_496() : void
      {
         var _loc1_:class_148 = null;
         var _loc2_:uint = 0;
         while(_loc2_ < const_43)
         {
            _loc1_ = this.var_58[_loc2_];
            if(_loc1_.HasPendingNodeType())
            {
               _loc1_.method_478();
            }
            else if(_loc1_.method_520())
            {
               _loc1_.method_1301();
            }
            _loc2_++;
         }
      }
      
      public function method_2059() : void
      {
         var _loc1_:class_148 = null;
         var _loc2_:uint = 0;
         while(_loc2_ < const_43)
         {
            _loc1_ = this.var_58[_loc2_];
            _loc1_.method_478();
            _loc2_++;
         }
      }
      
      public function method_272() : class_118
      {
         var _loc3_:class_148 = null;
         var _loc4_:class_22 = null;
         var _loc5_:uint = 0;
         var _loc6_:class_148 = null;
         var _loc1_:class_118 = new class_118(this.var_1);
         var _loc2_:uint = 0;
         while(_loc2_ < this.var_58.length)
         {
            _loc3_ = this.var_58[_loc2_];
            _loc4_ = _loc3_.mNodeType;
            _loc5_ = _loc3_.mPointsSpent;
            _loc6_ = new class_148(_loc4_,_loc5_);
            _loc1_.var_58[_loc2_] = _loc6_;
            _loc2_++;
         }
         return _loc1_;
      }
      
      public function method_245(param1:String = null) : uint
      {
         var _loc2_:uint = 0;
         var _loc3_:uint = this.method_98();
         if(_loc3_ >= ABILITY6_POINTS_PREREQ && !this.method_93(ABILITY6_NODE_PREREQ).IsEmpty())
         {
            _loc2_ = 6;
         }
         else if(_loc3_ >= ABILITY5_POINTS_PREREQ && !this.method_93(ABILITY5_NODE_PREREQ).IsEmpty())
         {
            _loc2_ = 5;
         }
         else if(Boolean(param1) || this.var_1.clientEnt && this.var_1.clientEnt.mMasterClass)
         {
            _loc2_ = 4;
         }
         return _loc2_;
      }
      
      public function method_1304() : Boolean
      {
         return true;
      }
   }
}
