package
{
   public class CutScene
   {
      
      public static const const_973:uint = 250;
       
      
      internal var var_1:Game;
      
      internal var room:Room;
      
      internal var var_2382:uint;
      
      internal var var_1901:uint;
      
      internal var var_2078:uint;
      
      internal var var_1697:uint;
      
      internal var var_1659:Boolean = false;
      
      internal var var_2133:Boolean = false;
      
      internal var var_631:Array;
      
      internal var var_1064:int;
      
      public function CutScene(param1:Game, param2:Room)
      {
         super();
         this.var_1 = param1;
         this.room = param2;
      }
      
      public function method_932() : void
      {
         this.var_631 = null;
         this.room = null;
         this.var_1 = null;
      }
      
      public function method_441(param1:Array, param2:Boolean, param3:Boolean = false) : void
      {
         var _loc4_:Packet = null;
         this.var_631 = param1;
         this.var_1064 = 0;
         this.var_2078 = 0;
         this.var_1659 = param2;
         this.var_2382 = this.var_1.mTimeThisTick;
         this.var_1901 = 0;
         this.var_1697 = 0;
         if(this.var_1659)
         {
            this.var_2133 = true;
         }
         else
         {
            if(this.room.var_1052)
            {
               this.method_502();
            }
            (_loc4_ = new Packet(LinkUpdater.const_683)).method_9(this.room.var_113);
            _loc4_.method_15(param3);
            this.var_1.serverConn.SendPacket(_loc4_);
            this.room.method_572(param3);
         }
      }
      
      public function method_502() : void
      {
         var _loc1_:Packet = null;
         if(this.var_1659)
         {
            this.var_2133 = false;
         }
         else
         {
            _loc1_ = new Packet(LinkUpdater.const_762);
            _loc1_.method_9(this.room.var_113);
            this.var_1.serverConn.SendPacket(_loc1_);
            this.room.method_752();
         }
         this.var_2382 = 0;
         this.var_1901 = this.var_1.mTimeThisTick;
         this.var_1697 = this.room.mRoomTick;
      }
      
      public function method_761() : void
      {
         var _loc1_:a_Cue = null;
         var _loc2_:String = null;
         var _loc3_:Boolean = false;
         var _loc4_:String = null;
         var _loc5_:Array = null;
         var _loc6_:int = 0;
         var _loc7_:int = 0;
         var _loc8_:String = null;
         var _loc9_:String = null;
         var _loc10_:uint = 0;
         var _loc11_:Number = NaN;
         var _loc12_:String = null;
         var _loc13_:String = null;
         var _loc14_:String = null;
         var _loc15_:Entity = null;
         var _loc16_:Boolean = false;
         if(this.var_2133 || !this.var_1659 && this.room.var_1052)
         {
            _loc3_ = false;
            while(!_loc3_)
            {
               _loc5_ = (_loc4_ = String(this.var_631[this.var_1064])).split(" ");
               _loc6_ = int(_loc5_[0]) * const_973;
               if((_loc7_ = this.var_2078 + _loc6_) < this.var_1.mTimeThisTick - this.var_2382)
               {
                  _loc8_ = String(_loc5_[1]);
                  _loc9_ = String(_loc5_[2]);
                  if(_loc8_ == "Camera")
                  {
                     this.room.var_1207 = _loc9_ == "Free" ? Room.const_243 : uint(_loc9_);
                     this.var_1.linkUpdater.method_1227(this.room.var_113,this.room.var_1207);
                  }
                  else if(_loc8_ == "Shake")
                  {
                     _loc10_ = uint(_loc9_);
                     this.room.method_237(_loc10_);
                     this.var_1.linkUpdater.method_1765(this.room.var_113,_loc10_);
                  }
                  else if(_loc8_ == "Sound")
                  {
                     _loc11_ = 1;
                     _loc12_ = String(_loc9_);
                     if(_loc5_.length > 3)
                     {
                        _loc11_ = Number(_loc5_[3]);
                     }
                     this.room.HookPlaySound(_loc12_,_loc11_);
                  }
                  else if(_loc8_ == "SpawnCue")
                  {
                     _loc1_ = this.method_384(_loc9_);
                     if(_loc1_)
                     {
                        this.room.SpawnCue(_loc1_);
                     }
                  }
                  else if(_loc8_ == "RemoveCue")
                  {
                     _loc1_ = this.method_384(_loc9_);
                     if(_loc1_)
                     {
                        this.room.RemoveCue(_loc1_);
                     }
                  }
                  else if(_loc8_ == "FirePower")
                  {
                     _loc2_ = String(_loc5_[3]);
                     _loc1_ = this.method_384(_loc9_);
                     if(_loc1_)
                     {
                        this.room.CueHookFirePower(_loc1_,_loc2_,null);
                     }
                  }
                  else if(_loc8_ == "QuickFirePower")
                  {
                     _loc2_ = String(_loc5_[3]);
                     _loc1_ = this.method_384(_loc9_);
                     if(_loc1_)
                     {
                        this.room.CueHookQuickFirePower(_loc1_,_loc2_,null);
                     }
                  }
                  else if(_loc8_ == "End")
                  {
                     this.var_1064 = this.var_631.length;
                  }
                  else
                  {
                     _loc13_ = _loc5_.slice(2).join(" ");
                     if(_loc8_ == "Player")
                     {
                        this.room.method_1845(_loc13_);
                     }
                     else
                     {
                        _loc14_ = "am_" + _loc8_;
                        if(_loc15_ = this.room.method_35(_loc14_))
                        {
                           _loc15_.StartSkit(_loc13_,false,this.room.GetTarget());
                        }
                        else
                        {
                           _loc16_ = _loc5_.length <= 3 || _loc5_[3].toUpperCase() != "RECOVER";
                           this.room.HookAnimate(_loc14_,_loc9_,_loc16_);
                        }
                     }
                  }
                  ++this.var_1064;
                  this.var_2078 = _loc7_;
                  if(this.var_1064 >= this.var_631.length)
                  {
                     _loc3_ = true;
                     this.method_502();
                  }
               }
               else
               {
                  _loc3_ = true;
               }
            }
         }
      }
      
      private function method_384(param1:String) : a_Cue
      {
         var _loc2_:a_Cue = this.room.method_851("am_" + param1);
         return !!_loc2_ ? _loc2_ : this.room.method_851(param1);
      }
   }
}
