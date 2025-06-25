package
{
   public class class_131
   {
      
      public static const const_1242:uint = 10;
      
      public static const const_356:Vector.<uint> = Vector.<uint>([1,10,25]);
      
      public static const const_1059:Vector.<uint> = Vector.<uint>([22,210,470]);
      
      public static const const_576:Vector.<uint> = Vector.<uint>([1,10,25]);
      
      public static const const_1179:Vector.<uint> = Vector.<uint>([50000,375000,625000]);
       
      
      internal var var_1:Game;
      
      internal var mLockboxID:uint = 0;
      
      internal var mLockboxList:Vector.<class_151>;
      
      internal var mOwnedLockboxes:Array;
      
      internal var mUniqueLockboxes:uint = 0;
      
      internal var mLockboxKeys:uint = 0;
      
      internal var mRoyalSigils:uint = 0;
      
      internal var mEarnedSigilsCache:uint = 0;
      
      public function class_131(param1:Game)
      {
         this.mLockboxList = new Vector.<class_151>();
         this.mOwnedLockboxes = new Array();
         super();
         this.var_1 = param1;
      }
      
      public function method_2114() : void
      {
         var _loc1_:class_151 = null;
         for each(_loc1_ in this.mOwnedLockboxes)
         {
            _loc1_.method_777();
         }
         this.mOwnedLockboxes = null;
         this.mLockboxList = null;
      }
      
      public function method_1310(param1:uint, param2:uint, param3:Boolean) : void
      {
         var _loc5_:class_151 = null;
         var _loc6_:String = null;
         var _loc4_:class_15;
         if(_loc4_ = class_14.var_838[param1])
         {
            if(!(_loc5_ = this.mOwnedLockboxes[param1]))
            {
               _loc5_ = new class_151(_loc4_,0);
               this.mOwnedLockboxes[param1] = _loc5_;
               this.mLockboxList.push(_loc5_);
               ++this.mUniqueLockboxes;
            }
            _loc5_.stackCount += param2;
            _loc6_ = param2 == 1 ? "" : " x" + String(param2);
            if(!param3)
            {
               this.var_1.screenNotification.ShowNotification(class_46.const_588,_loc4_.displayName + _loc6_,"L");
            }
            this.var_1.screenArmory.Refresh();
         }
      }
      
      public function method_1303(param1:uint) : void
      {
         this.mLockboxKeys += param1;
      }
      
      public function OpenLockbox(param1:uint) : void
      {
         var _loc4_:uint = 0;
         var _loc2_:class_151 = this.mOwnedLockboxes[param1];
         if(!_loc2_)
         {
            return;
         }
         if(!_loc2_.stackCount)
         {
            return;
         }
         if(!this.mLockboxKeys)
         {
            return;
         }
         --_loc2_.stackCount;
         --this.mLockboxKeys;
         if(!_loc2_.stackCount)
         {
            _loc4_ = 0;
            while(_loc4_ < this.mLockboxList.length)
            {
               if(this.mLockboxList[_loc4_] == _loc2_)
               {
                  this.mLockboxList.splice(_loc4_,1);
                  break;
               }
               _loc4_++;
            }
            _loc2_.method_777();
            this.mOwnedLockboxes[param1] = null;
            --this.mUniqueLockboxes;
         }
         this.var_1.screenArmory.Refresh();
         var _loc3_:Packet = new Packet(LinkUpdater.const_1289);
         _loc3_.method_20(class_15.const_300,param1);
         this.var_1.serverConn.SendPacket(_loc3_);
      }
      
      public function BuyLockboxKeys(param1:uint) : void
      {
         if(!this.var_1.CanSendPacket())
         {
            return;
         }
         var _loc2_:uint = class_131.const_356[param1];
         this.method_1303(_loc2_);
         this.var_1.screenLockBox.method_1978(_loc2_);
         this.var_1.screenLockBox.Refresh();
         var _loc3_:Packet = new Packet(LinkUpdater.const_1115);
         _loc3_.method_9(param1);
         this.var_1.serverConn.SendPacket(_loc3_);
         var _loc4_:String = _loc2_ > 1 ? "Dragon Keys x" : "Dragon Key x";
         this.var_1.screenNotification.ShowNotification(class_46.const_572,_loc4_ + _loc2_,"L");
      }
      
      public function method_1966(param1:uint) : void
      {
         this.mEarnedSigilsCache = param1;
      }
      
      public function method_1459() : uint
      {
         var _loc1_:class_151 = null;
         var _loc2_:int = int(this.mOwnedLockboxes.length - 1);
         while(_loc2_ >= 0)
         {
            _loc1_ = this.mOwnedLockboxes[_loc2_];
            if(Boolean(_loc1_) && Boolean(_loc1_.stackCount))
            {
               return _loc1_.var_286.lockboxID;
            }
            _loc2_--;
         }
         return class_14.var_838[class_14.var_838.length - 1].lockboxID;
      }
      
      public function method_662() : Boolean
      {
         var _loc2_:class_151 = null;
         if(this.var_1.mAlertState & Game.const_186)
         {
            return true;
         }
         var _loc1_:int = int(this.mOwnedLockboxes.length - 1);
         while(_loc1_ >= 0)
         {
            _loc2_ = this.mOwnedLockboxes[_loc1_];
            if(Boolean(_loc2_) && _loc2_.stackCount >= const_1242)
            {
               return true;
            }
            _loc1_--;
         }
         return false;
      }
   }
}
