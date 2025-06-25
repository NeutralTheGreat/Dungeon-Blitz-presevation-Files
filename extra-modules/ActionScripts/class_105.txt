package
{
   import flash.utils.Dictionary;
   
   public class class_105
   {
      
      internal static const const_29:uint = 0;
      
      internal static const const_339:uint = 1;
      
      internal static const const_521:uint = 2;
       
      
      internal var var_1:Game;
      
      internal var mData:Dictionary;
      
      internal var mStatus:uint;
      
      internal var mWorkerBuildingID:uint;
      
      internal var mWorkerEndtime:uint;
      
      public function class_105(param1:Game)
      {
         super();
         this.var_1 = param1;
         this.mData = new Dictionary();
      }
      
      public static function method_1596(param1:String) : String
      {
         if(param1 == "Mage")
         {
            return "Frostwarden";
         }
         if(param1 == "Rogue")
         {
            return "Executioner";
         }
         if(param1 == "Paladin")
         {
            return "Sentinel";
         }
         return "";
      }
      
      public static function method_1628(param1:String) : String
      {
         if(param1 == "Mage")
         {
            return "Flameseer";
         }
         if(param1 == "Rogue")
         {
            return "Shadowwalker";
         }
         if(param1 == "Paladin")
         {
            return "Justicar";
         }
         return "";
      }
      
      public static function method_1706(param1:String) : String
      {
         if(param1 == "Mage")
         {
            return "Necromancer";
         }
         if(param1 == "Rogue")
         {
            return "Soulthief";
         }
         if(param1 == "Paladin")
         {
            return "Templar";
         }
         return "";
      }
      
      public static function method_551(param1:uint) : uint
      {
         return uint(param1 / 5) + 1;
      }
      
      public function method_1455() : void
      {
         this.mData = null;
      }
      
      public function method_1430(param1:uint) : void
      {
         this.mData["Keep"] = class_9.method_94("Keep",param1);
      }
      
      public function method_1492(param1:uint) : void
      {
         this.mData["Forge"] = class_9.method_94("Forge",param1);
      }
      
      public function method_2145(param1:uint) : void
      {
         this.mData["Hatchery"] = class_9.method_94("Hatchery",param1);
      }
      
      public function method_1980(param1:uint) : void
      {
         this.mData["Tome"] = class_9.method_94("Tome",param1);
      }
      
      public function method_1728(param1:uint) : void
      {
         this.mData["Barn"] = class_9.method_94("Barn",param1);
      }
      
      public function method_382(param1:String, param2:uint) : void
      {
         param1 = class_83.method_406(param1);
         var _loc3_:String = this.method_238(param1);
         if(_loc3_)
         {
            this.mData[_loc3_] = class_9.method_94(param1 + "Tower",param2);
         }
      }
      
      public function GetOwnedBuildingByName(param1:String) : class_9
      {
         var _loc2_:class_9 = null;
         for each(_loc2_ in this.mData)
         {
            if(param1 == _loc2_.var_242)
            {
               return _loc2_;
            }
         }
         return null;
      }
      
      public function method_256(param1:class_9) : class_9
      {
         var _loc2_:class_9 = null;
         for each(_loc2_ in this.mData)
         {
            if(param1.var_208 == _loc2_.var_208)
            {
               return _loc2_;
            }
         }
         return null;
      }
      
      public function method_2115(param1:class_9) : void
      {
         var _loc3_:String = null;
         var _loc4_:String = null;
         if(!param1)
         {
            return;
         }
         var _loc2_:String = param1.var_242;
         if(param1.type == "Tower")
         {
            _loc3_ = param1.var_242.replace("Tower","");
            if(_loc4_ = this.method_238(_loc3_))
            {
               this.mData[_loc4_] = param1;
            }
         }
         else
         {
            this.mData[param1.var_242] = param1;
         }
      }
      
      public function method_238(param1:String) : String
      {
         var _loc2_:String = "";
         if(!param1)
         {
            return "";
         }
         param1 = param1.toLowerCase();
         if(param1 == "frostwarden" || param1 == "sentinel" || param1 == "executioner")
         {
            _loc2_ = "ClassTowerOne";
         }
         if(param1 == "flameseer" || param1 == "justicar" || param1 == "shadowwalker")
         {
            _loc2_ = "ClassTowerTwo";
         }
         if(param1 == "necromancer" || param1 == "templar" || param1 == "soulthief")
         {
            _loc2_ = "ClassTowerThree";
         }
         return _loc2_;
      }
      
      public function method_1277(param1:uint, param2:uint) : void
      {
         this.mWorkerBuildingID = param1;
         this.mWorkerEndtime = param2;
         this.mStatus = const_29;
         if(Boolean(this.mWorkerBuildingID) && Boolean(this.mWorkerEndtime))
         {
            this.mStatus = const_339;
         }
         if(Boolean(this.mWorkerBuildingID) && !this.mWorkerEndtime)
         {
            this.mStatus = const_521;
         }
      }
      
      public function GetBuildingByMasterClass(param1:String) : class_9
      {
         var _loc2_:String = this.method_238(param1);
         var _loc3_:class_9 = null;
         return this.mData[_loc2_];
      }
      
      public function UpgradeBuilding(param1:class_9, param2:Boolean = false) : class_9
      {
         var _loc3_:Entity = this.var_1.clientEnt;
         if(!_loc3_ || !this.var_1.CanSendPacket())
         {
            return null;
         }
         if(this.mStatus != const_29)
         {
            return null;
         }
         var _loc4_:class_9;
         if(!(_loc4_ = this.method_256(param1)))
         {
            return null;
         }
         var _loc5_:class_9;
         if(!(_loc5_ = class_9.method_132(_loc4_)))
         {
            return null;
         }
         var _loc6_:uint = _loc5_.upgradeTime + this.var_1.mServerGameTime;
         var _loc7_:uint = _loc5_.rank;
         var _loc8_:uint = method_551(_loc3_.mExpLevel);
         if(_loc7_ > _loc8_)
         {
            return null;
         }
         var _loc9_:uint = _loc5_.var_129;
         if(!param2 && _loc3_.currGold < _loc9_)
         {
            return null;
         }
         if(_loc3_.currGold >= _loc9_)
         {
            param2 = false;
         }
         if(param1.type == "Tower")
         {
            this.var_1.mMasterClassTower.ClearResearch();
            this.var_1.screenClassTowers.Refresh();
         }
         this.mStatus = const_339;
         this.mWorkerBuildingID = _loc5_.var_208;
         this.mWorkerEndtime = _loc6_;
         this.var_1.var_163["Scaffolding"] = _loc5_.var_208;
         this.var_1.level.method_194();
         if(this.var_1.var_107)
         {
            this.var_1.var_107.method_120();
         }
         if(!param2)
         {
            _loc3_.GainMoney(-_loc9_,false);
         }
         var _loc10_:Packet;
         (_loc10_ = new Packet(LinkUpdater.const_861)).method_20(class_9.const_129,this.mWorkerBuildingID);
         _loc10_.method_20(class_9.const_28,_loc7_);
         _loc10_.method_15(param2);
         this.var_1.serverConn.SendPacket(_loc10_);
         return _loc5_;
      }
      
      public function method_1421() : void
      {
         var _loc1_:class_9 = this.method_256(class_14.var_278[this.mWorkerBuildingID]);
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:class_9 = class_9.method_132(_loc1_);
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:Entity = this.var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:String = "";
         if(_loc2_.type == "Tower")
         {
            _loc4_ = this.method_238(_loc3_.mMasterClass);
         }
         else
         {
            _loc4_ = _loc2_.var_242;
         }
         var _loc5_:class_9 = this.mData[_loc4_];
         this.mData[_loc4_] = _loc2_;
         this.var_1.var_163["Scaffolding"] = null;
         this.var_1.var_163[_loc2_.type] = _loc2_;
         var _loc6_:String = _loc5_.var_266;
         var _loc7_:String = _loc2_.var_266;
         this.var_1.level.method_506(_loc7_);
         this.var_1.level.method_194();
         this.method_595();
         if(this.var_1.screenUpgrading.mbVisible)
         {
            this.var_1.screenUpgrading.Hide();
            switch(_loc1_.type)
            {
               case "Forge":
                  this.var_1.screenForge.Display();
                  break;
               case "Tower":
                  this.var_1.screenClassTowers.Display();
                  break;
               case "Barn":
                  this.var_1.screenBarn.Display();
                  break;
               case "Tome":
                  if(this.var_1.clientEnt)
                  {
                     this.var_1.screenTome.Display(this.var_1.clientEnt.entType.className);
                     break;
                  }
            }
         }
      }
      
      public function method_595() : void
      {
         this.mStatus = const_29;
         this.mWorkerBuildingID = 0;
         this.mWorkerEndtime = 0;
      }
      
      public function CancelUpgrade() : void
      {
         if(!this.var_1.CanSendPacket())
         {
            return;
         }
         if(!this.mWorkerBuildingID)
         {
            return;
         }
         this.method_595();
         this.var_1.var_163["Scaffolding"] = 0;
         this.var_1.level.method_194();
         if(this.var_1.var_107)
         {
            this.var_1.var_107.method_120();
         }
         var _loc1_:Packet = new Packet(LinkUpdater.const_1032);
         this.var_1.serverConn.SendPacket(_loc1_);
      }
      
      public function GetCurrentBuilding() : class_9
      {
         return this.method_256(class_14.var_278[this.mWorkerBuildingID]);
      }
      
      public function method_469() : void
      {
         var _loc1_:class_9 = this.method_256(class_14.var_278[this.mWorkerBuildingID]);
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:class_9 = class_9.method_132(_loc1_);
         if(!_loc2_)
         {
            return;
         }
         if(_loc2_.rank > 1)
         {
            this.var_1.screenNotification.ShowNotification(class_46.const_629,_loc2_.displayName);
         }
      }
   }
}
