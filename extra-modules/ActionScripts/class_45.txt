package
{
   public class class_45
   {
      
      private static const const_1346:uint = 3;
      
      internal static const const_29:uint = 0;
      
      internal static const const_191:uint = 1;
      
      internal static const const_223:uint = 2;
      
      internal static const const_1234:uint = 17;
      
      internal static const const_1066:uint = 9;
      
      internal static const const_1238:uint = 25;
       
      
      internal var var_1:Game;
      
      internal var var_789:Array;
      
      internal var mAbilityListTrainedRanks:Array;
      
      internal var var_1013:Vector.<class_10>;
      
      internal var mHotbarList:Vector.<class_10>;
      
      internal var var_989:Vector.<class_10>;
      
      internal var mStatus:uint;
      
      internal var mAbilityResearch:class_10;
      
      internal var mAbilityResearchFinishTime:int;
      
      internal var mJustGotTutorialAbility:Boolean = false;
      
      public function class_45(param1:Game)
      {
         super();
         this.mStatus = const_29;
         this.var_1 = param1;
         this.var_1013 = new Vector.<class_10>();
         this.var_789 = new Array();
         this.mHotbarList = new Vector.<class_10>(4);
         this.mAbilityResearch = null;
         this.mAbilityResearchFinishTime = 0;
         this.mAbilityListTrainedRanks = new Array();
      }
      
      public static function method_461(param1:uint) : Boolean
      {
         return param1 == const_1234 || param1 == const_1066 || param1 == const_1238;
      }
      
      public function method_1185() : void
      {
         this.var_789 = null;
         this.var_1013 = null;
         this.mHotbarList = null;
         this.var_1 = null;
      }
      
      public function SetAbilities(param1:int, param2:class_10) : Boolean
      {
         if(!param2)
         {
            return false;
         }
         if(!this.IsTrained(param2))
         {
            return false;
         }
         if(param1 < 1 || param1 > 3)
         {
            return false;
         }
         if(param1 == 3 && param2.var_90 != 3)
         {
            return false;
         }
         this.mHotbarList[param1] = param2;
         return true;
      }
      
      public function RebuildHotbar() : void
      {
         var _loc3_:Packet = null;
         var _loc4_:int = 0;
         var _loc5_:Boolean = false;
         var _loc1_:Entity = this.var_1.clientEnt;
         if(!_loc1_ || !this.var_1.CanSendPacket())
         {
            return;
         }
         _loc1_.ResetEntType(_loc1_.entType);
         var _loc2_:int = this.method_1751();
         if(_loc2_)
         {
            _loc3_ = new Packet(LinkUpdater.const_929);
            _loc4_ = 1;
            while(_loc4_ < this.mHotbarList.length)
            {
               _loc5_ = !!(_loc2_ & 1 << _loc4_ - 1) ? true : false;
               _loc3_.method_15(_loc5_);
               if(_loc5_)
               {
                  _loc3_.method_20(class_10.const_83,this.mHotbarList[_loc4_].abilityID);
               }
               _loc4_++;
            }
            this.var_1.serverConn.SendPacket(_loc3_);
         }
      }
      
      public function method_1859(param1:uint, param2:uint) : void
      {
         var _loc3_:class_10 = class_10.method_591(param1,param2);
         if(_loc3_)
         {
            this.var_789[param1] = _loc3_;
            if(param2 > class_10.const_105)
            {
               param2 = class_10.const_105;
            }
            this.mAbilityListTrainedRanks[_loc3_.abilityID] = param2;
         }
      }
      
      public function method_1311(param1:String) : void
      {
         var _loc2_:class_10 = null;
         this.var_1013 = new Vector.<class_10>();
         for each(_loc2_ in class_14.var_478)
         {
            if(_loc2_.var_1911 == param1)
            {
               this.var_1013.push(_loc2_);
            }
         }
         this.var_1013.sort(class_10.method_1363);
      }
      
      public function getSpellsByCategory(param1:String, param2:Boolean = true, param3:Boolean = false, param4:int = 0) : Vector.<class_10>
      {
         var _loc6_:class_10 = null;
         param1 = !!param1 ? param1.toLowerCase() : "";
         var _loc5_:Vector.<class_10> = new Vector.<class_10>();
         for each(_loc6_ in this.var_1013)
         {
            if(_loc6_.className.toLowerCase() == param1 && (param2 || !_loc6_.var_223) && (param3 || !_loc6_.var_2189) && (!param4 || _loc6_.var_90 == param4))
            {
               _loc5_.push(_loc6_);
            }
         }
         return _loc5_;
      }
      
      public function getMasterSpells(param1:Boolean = false) : Vector.<class_10>
      {
         var _loc3_:class_10 = null;
         var _loc2_:Vector.<class_10> = new Vector.<class_10>();
         for each(_loc3_ in this.var_1013)
         {
            if(_loc3_.var_223 && (param1 || !_loc3_.var_2189) && !class_50.method_454(_loc3_.className))
            {
               _loc2_.push(_loc3_);
            }
         }
         return _loc2_;
      }
      
      public function IsTrained(param1:class_10) : Boolean
      {
         return this.var_789[param1.abilityID];
      }
      
      public function setCurrent() : void
      {
         this.var_989 = new Vector.<class_10>(4);
         this.var_989[1] = this.mHotbarList[1];
         this.var_989[2] = this.mHotbarList[2];
         this.var_989[3] = this.mHotbarList[3];
      }
      
      public function method_1751() : int
      {
         var _loc2_:int = 0;
         if(!this.var_989)
         {
            return 0;
         }
         var _loc1_:* = 0;
         _loc2_ = 1;
         while(_loc2_ < this.var_989.length)
         {
            if(this.var_989[_loc2_] != this.mHotbarList[_loc2_])
            {
               _loc1_ |= 1 << _loc2_ - 1;
            }
            _loc2_++;
         }
         return _loc1_;
      }
      
      public function ReceiveAbilityResearchDone(param1:uint) : void
      {
         var _loc2_:PowerType = null;
         var _loc3_:String = null;
         this.mStatus = class_45.const_223;
         if(Boolean(this.mAbilityResearch) && Boolean(this.var_1.clientEnt))
         {
            _loc2_ = this.var_1.clientEnt.GetPowerFromAbilityType(this.mAbilityResearch);
            _loc3_ = "M";
            if(this.mAbilityResearch.rank == 10)
            {
               _loc3_ = "L";
            }
            else if(this.mAbilityResearch.rank >= 5)
            {
               _loc3_ = "R";
            }
            this.var_1.screenNotification.ShowNotification(class_46.const_586,_loc2_.displayName + " - [Rank " + this.mAbilityResearch.rank + "]",_loc3_);
         }
      }
      
      public function CheckForDoneResearch() : Boolean
      {
         return this.mStatus == class_45.const_223;
      }
      
      public function GetCurrRankByAbilityID(param1:uint) : uint
      {
         return this.mAbilityListTrainedRanks[param1];
      }
      
      public function GiveNewRank() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         if(this.mAbilityResearch)
         {
            _loc1_ = this.mAbilityResearch.abilityID;
            _loc2_ = this.mAbilityResearch.rank;
            if(method_461(_loc1_) && _loc2_ == 1)
            {
               this.mJustGotTutorialAbility = true;
               this.var_1.clientEnt.var_228 = Entity.const_429;
            }
            this.var_789[_loc1_] = this.mAbilityResearch;
            this.mAbilityListTrainedRanks[_loc1_] = this.mAbilityResearch.rank;
         }
         this.mStatus = class_45.const_29;
         this.var_1.mAbilityBook.mAbilityResearch = null;
         this.var_1.mAbilityBook.mAbilityResearchFinishTime = 0;
         if(this.var_1.screenTome.mbVisible)
         {
            this.var_1.screenTome.Refresh();
         }
      }
      
      public function DefaultMasterRanks(param1:class_118, param2:String) : void
      {
         var _loc4_:class_10 = null;
         if(!param1 || !param2)
         {
            return;
         }
         var _loc3_:uint = param1.method_245(param2);
         switch(_loc3_)
         {
            case 6:
               if((Boolean(_loc4_ = class_14.var_526[param2.toLowerCase() + 6])) && !this.mAbilityListTrainedRanks[_loc4_.abilityID])
               {
                  this.var_789[_loc4_.abilityID] = _loc4_;
                  this.mAbilityListTrainedRanks[_loc4_.abilityID] = 1;
               }
            case 5:
               if((Boolean(_loc4_ = class_14.var_526[param2.toLowerCase() + 5])) && !this.mAbilityListTrainedRanks[_loc4_.abilityID])
               {
                  this.var_789[_loc4_.abilityID] = _loc4_;
                  this.mAbilityListTrainedRanks[_loc4_.abilityID] = 1;
                  break;
               }
         }
         if((Boolean(_loc4_ = class_14.var_526[param2.toLowerCase() + 4])) && !this.mAbilityListTrainedRanks[_loc4_.abilityID])
         {
            this.var_789[_loc4_.abilityID] = _loc4_;
            this.mAbilityListTrainedRanks[_loc4_.abilityID] = 1;
         }
      }
   }
}
