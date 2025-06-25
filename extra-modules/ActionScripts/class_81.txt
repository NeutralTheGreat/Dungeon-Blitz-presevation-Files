package
{
   public class class_81
   {
      
      public static const const_892:uint = 3;
      
      public static const const_516:uint = 0;
      
      public static const const_131:uint = 1;
      
      public static const const_319:uint = 2;
      
      public static const const_251:uint = 0;
      
      public static const const_107:uint = 1;
      
      public static const const_474:uint = 2;
       
      
      internal var var_1:Game;
      
      internal var var_1233:Vector.<uint>;
      
      internal var mIncubatingEggID:uint;
      
      internal var var_1179:uint;
      
      internal var mActivePet:class_87;
      
      internal var mRestingPetList:Vector.<class_87>;
      
      internal var mOwnedPets:Vector.<class_87>;
      
      internal var mOwnedPetsHash:Array;
      
      internal var mEggStatus:uint;
      
      internal var mPetTrainingStatus:uint;
      
      internal var var_2987:uint;
      
      internal var mTrainingPet:class_87;
      
      internal var var_943:uint;
      
      internal var mEggResetEndTime:uint;
      
      internal var mbAskingForEggs:Boolean;
      
      public function class_81(param1:Game)
      {
         super();
         this.var_1 = param1;
         this.var_1233 = new Vector.<uint>(class_16.const_1290,true);
         this.mIncubatingEggID = 0;
         this.var_1179 = 0;
         this.mActivePet = null;
         this.mRestingPetList = new Vector.<class_87>(const_892,true);
         this.mOwnedPets = new Vector.<class_87>();
         this.mTrainingPet = null;
         this.var_943 = 0;
         this.mOwnedPetsHash = new Array();
         this.mPetTrainingStatus = const_251;
         this.mEggStatus = const_516;
         this.mEggResetEndTime = 0;
      }
      
      public function method_1900() : void
      {
         var _loc1_:String = null;
         this.var_1 = null;
         this.var_1233 = null;
         this.mRestingPetList = null;
         this.mOwnedPets = null;
         for each(_loc1_ in this.mOwnedPetsHash)
         {
         }
         _loc1_ = null;
         this.mOwnedPetsHash = null;
      }
      
      public function SetEggData(param1:uint, param2:uint) : void
      {
         var _loc3_:class_7 = class_14.var_224[param1];
         if(!_loc3_)
         {
            return;
         }
         this.mIncubatingEggID = param1;
         this.var_1179 = param2;
         if(!this.mIncubatingEggID)
         {
            this.mEggStatus = const_516;
         }
         else if(Boolean(this.mIncubatingEggID) && Boolean(param2))
         {
            this.mEggStatus = const_131;
         }
         else
         {
            this.mEggStatus = const_319;
         }
      }
      
      public function SetRestingPetData(param1:class_87, param2:uint) : void
      {
         this.mRestingPetList[param2] = param1;
      }
      
      public function SetActivePetData(param1:class_87) : void
      {
         this.mActivePet = param1;
      }
      
      public function method_1548(param1:class_87, param2:uint) : void
      {
         this.mTrainingPet = param1;
         this.var_943 = param2;
         if(param2 == 0)
         {
            this.mPetTrainingStatus = const_474;
         }
         else
         {
            this.mPetTrainingStatus = const_107;
         }
      }
      
      public function method_976(param1:Vector.<uint>) : void
      {
         var _loc3_:class_16 = null;
         var _loc2_:uint = 0;
         while(_loc2_ < param1.length)
         {
            this.var_1233[_loc2_] = param1[_loc2_];
            _loc3_ = class_14.var_212[this.var_1233[_loc2_]];
            _loc2_++;
         }
      }
      
      public function PickEgg(param1:uint) : uint
      {
         return this.var_1233[param1];
      }
      
      public function method_1474(param1:uint, param2:uint, param3:uint, param4:Boolean) : void
      {
         var _loc8_:String = null;
         var _loc9_:int = 0;
         var _loc10_:Boolean = false;
         var _loc5_:class_7;
         if(!(_loc5_ = class_14.var_224[param1]))
         {
            return;
         }
         if(!param4)
         {
            _loc8_ = "Pet:" + _loc5_.var_310;
            this.var_1.screenNotification.ShowNotification(class_46.const_561,_loc5_.displayName,_loc5_.var_255,true,null,_loc8_);
         }
         var _loc6_:uint = 0;
         if(param3 != 1 && param3 - 1 < class_7.const_164.length)
         {
            _loc6_ = uint(class_7.const_164[param3 - 1]);
         }
         var _loc7_:class_87 = new class_87(this.var_1,_loc5_,param3,_loc6_,param2);
         this.method_713(_loc7_);
         this.var_1.mEggPetInfo.method_588();
         this.var_1179 = 0;
         this.mIncubatingEggID = 0;
         this.mEggStatus = const_516;
         if(this.var_1.clientEnt)
         {
            _loc9_ = this.mRestingPetList.indexOf(null);
            _loc10_ = false;
            if(!this.mActivePet)
            {
               this.var_1.clientEnt.ChangePet(_loc7_);
               this.SetActivePetData(_loc7_);
               _loc10_ = true;
            }
            else if(_loc9_ >= 0)
            {
               this.SetRestingPetData(_loc7_,_loc9_);
               this.var_1.clientEnt.ChangeRestingPets(_loc9_,_loc7_);
               _loc10_ = true;
            }
            if(_loc10_)
            {
               this.SendPetInfoToServer();
            }
         }
         if(this.var_1.screenBarn.mbVisible)
         {
            this.var_1.screenBarn.Refresh();
         }
      }
      
      public function method_713(param1:class_87) : void
      {
         this.mOwnedPets.push(param1);
         if(this.mOwnedPetsHash[param1.mPetType.var_104])
         {
            this.mOwnedPetsHash[param1.mPetType.var_104][param1.var_670] = param1;
         }
         else
         {
            this.mOwnedPetsHash[param1.mPetType.var_104] = new Array();
            this.mOwnedPetsHash[param1.mPetType.var_104][param1.var_670] = param1;
         }
      }
      
      public function method_2091(param1:uint) : uint
      {
         var _loc2_:Array = this.mOwnedPetsHash[param1];
         var _loc3_:uint = 0;
         if(_loc2_)
         {
            _loc3_ = _loc2_.length;
         }
         return _loc3_;
      }
      
      public function GetNewestPetDataByID(param1:uint) : class_87
      {
         var _loc2_:Array = this.mOwnedPetsHash[param1];
         if(Boolean(_loc2_) && Boolean(_loc2_.length))
         {
            return _loc2_[_loc2_.length - 1];
         }
         return null;
      }
      
      public function GetPetDataByIDIteration(param1:uint, param2:uint) : class_87
      {
         if(this.mOwnedPetsHash[param1])
         {
            return this.mOwnedPetsHash[param1][param2];
         }
         return null;
      }
      
      public function TrainPet(param1:class_87, param2:Boolean = false) : void
      {
         var _loc3_:class_81 = this.var_1.mEggPetInfo;
         if(_loc3_.mPetTrainingStatus != class_81.const_251)
         {
            return;
         }
         var _loc4_:uint = class_7.method_154(param1.var_23);
         if(param1.var_110 < _loc4_)
         {
            return;
         }
         var _loc5_:uint = uint(param1.var_23 + 1);
         this.mTrainingPet = param1;
         this.var_943 = this.var_1.mServerGameTime + class_7.method_516(_loc5_);
         this.mPetTrainingStatus = const_107;
         if(this.mTrainingPet == this.var_1.mEggPetInfo.mActivePet)
         {
            this.var_1.mEggPetInfo.SetActivePetData(null);
         }
         if(this.mTrainingPet == this.var_1.mEggPetInfo.mRestingPetList[class_7.const_220])
         {
            this.var_1.mEggPetInfo.SetRestingPetData(null,class_7.const_220);
         }
         if(this.mTrainingPet == this.var_1.mEggPetInfo.mRestingPetList[class_7.const_199])
         {
            this.var_1.mEggPetInfo.SetRestingPetData(null,class_7.const_199);
         }
         if(this.mTrainingPet == this.var_1.mEggPetInfo.mRestingPetList[class_7.const_187])
         {
            this.var_1.mEggPetInfo.SetRestingPetData(null,class_7.const_187);
         }
         this.var_1.screenArmory.Refresh();
         var _loc6_:Packet;
         (_loc6_ = new Packet(LinkUpdater.const_1114)).method_20(class_7.const_19,param1.mPetType.var_104);
         _loc6_.method_9(param1.var_670);
         _loc6_.method_20(class_7.const_75,_loc5_);
         _loc6_.method_15(param2);
         this.var_1.serverConn.SendPacket(_loc6_);
      }
      
      public function method_1600() : void
      {
         if(!this.mTrainingPet)
         {
            return;
         }
         if(this.mTrainingPet.var_23 == class_7.const_35)
         {
            return;
         }
         ++this.mTrainingPet.var_23;
         this.mTrainingPet = null;
         this.var_943 = 0;
         this.mPetTrainingStatus = const_251;
      }
      
      public function PetTrainCancel() : void
      {
         this.mTrainingPet = null;
         this.var_943 = 0;
         this.mPetTrainingStatus = const_251;
      }
      
      public function HatchEggCancel() : void
      {
         this.mIncubatingEggID = 0;
         this.var_1179 = 0;
         this.mEggStatus = const_251;
      }
      
      public function method_1937(param1:uint) : void
      {
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:Boolean = false;
         if(!this.mActivePet)
         {
            return;
         }
         var _loc2_:uint = this.mActivePet.var_110;
         if(_loc2_ < 4294967295 - param1)
         {
            _loc3_ = this.mActivePet.var_110;
            this.mActivePet.var_110 += param1;
            _loc4_ = uint(class_7.const_164[this.mActivePet.var_23]);
            _loc5_ = _loc3_ < _loc4_ && this.mActivePet.var_110 > _loc4_;
            if(Boolean(param1) && _loc5_)
            {
               this.var_1.screenNotification.ShowNotification(class_46.const_343,this.mActivePet.mPetType.displayName + " is ready to train","M",false);
            }
         }
      }
      
      public function SendPetInfoToServer() : void
      {
         var _loc1_:Packet = new Packet(LinkUpdater.const_1209);
         var _loc2_:class_87 = this.mActivePet;
         var _loc3_:class_87 = this.mRestingPetList[class_7.const_220];
         var _loc4_:class_87 = this.mRestingPetList[class_7.const_199];
         var _loc5_:class_87 = this.mRestingPetList[class_7.const_187];
         var _loc6_:uint = !!_loc2_ ? _loc2_.mPetType.var_104 : 0;
         var _loc7_:uint = !!_loc2_ ? _loc2_.var_670 : 0;
         var _loc8_:uint = !!_loc3_ ? _loc3_.mPetType.var_104 : 0;
         var _loc9_:uint = !!_loc3_ ? _loc3_.var_670 : 0;
         var _loc10_:uint = !!_loc4_ ? _loc4_.mPetType.var_104 : 0;
         var _loc11_:uint = !!_loc4_ ? _loc4_.var_670 : 0;
         var _loc12_:uint = !!_loc5_ ? _loc5_.mPetType.var_104 : 0;
         var _loc13_:uint = !!_loc5_ ? _loc5_.var_670 : 0;
         _loc1_.method_20(class_7.const_19,_loc6_);
         _loc1_.method_9(_loc7_);
         _loc1_.method_20(class_7.const_19,_loc8_);
         _loc1_.method_9(_loc9_);
         _loc1_.method_20(class_7.const_19,_loc10_);
         _loc1_.method_9(_loc11_);
         _loc1_.method_20(class_7.const_19,_loc12_);
         _loc1_.method_9(_loc13_);
         this.var_1.serverConn.SendPacket(_loc1_);
      }
      
      public function method_588() : void
      {
         this.mOwnedPets.sort(this.method_1121);
         this.var_1.screenArmory.Refresh();
         this.var_1.screenBarn.var_1302 = true;
         this.var_1.screenBarn.Refresh();
      }
      
      public function method_1121(param1:class_87, param2:class_87) : Number
      {
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         var _loc3_:int = 0;
         if(param1 == this.mActivePet)
         {
            _loc3_ = -1;
         }
         else if(param2 == this.mActivePet)
         {
            _loc3_ = 1;
         }
         else
         {
            _loc4_ = this.mRestingPetList.indexOf(param1);
            _loc5_ = this.mRestingPetList.indexOf(param2);
            if(_loc4_ >= 0)
            {
               if(_loc5_ < 0)
               {
                  _loc3_ = -1;
               }
               else if(_loc5_ < _loc4_)
               {
                  _loc3_ = 1;
               }
               else
               {
                  _loc3_ = -1;
               }
            }
            else if(_loc5_ >= 0)
            {
               _loc3_ = 1;
            }
         }
         if(!_loc3_)
         {
            _loc3_ = param2.var_23 - param1.var_23;
         }
         return _loc3_;
      }
      
      public function method_2119(param1:class_87, param2:class_87) : Number
      {
         return param2.var_23 - param1.var_23;
      }
      
      public function method_891(param1:uint) : void
      {
         this.mEggResetEndTime = param1;
      }
      
      public function method_1321() : void
      {
         if(!this.mTrainingPet)
         {
            return;
         }
         var _loc1_:class_7 = this.mTrainingPet.mPetType;
         var _loc2_:String = "Pet:" + _loc1_.var_310;
         this.var_1.screenNotification.ShowNotification(class_46.const_343,_loc1_.displayName + " Rank " + (this.mTrainingPet.var_23 + 1),_loc1_.var_255,true,null,_loc2_);
      }
      
      public function method_1133() : void
      {
         this.var_1.screenNotification.ShowNotification(class_46.const_561,"A new Pet is hatching in the Barn!");
      }
   }
}
