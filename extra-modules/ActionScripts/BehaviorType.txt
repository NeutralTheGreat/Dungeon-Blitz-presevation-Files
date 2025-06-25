package
{
   import flash.net.registerClassAlias;
   import flash.utils.ByteArray;
   import flash.utils.getQualifiedClassName;
   
   public class BehaviorType
   {
      
      public static var bInitialized:Boolean;
      
      public static const behaviorTypes:Array = new Array();
      
      public static const const_1319:Array = [];
      
      {
         method_592();
      }
      
      public var var_1241:String;
      
      public var bNoPhysics:Boolean;
      
      public var var_696:Boolean;
      
      public var var_53:Boolean;
      
      public var bNoCombat:Boolean;
      
      public var var_881:Boolean;
      
      public var var_2918:Boolean;
      
      public var var_2937:Boolean;
      
      public var var_534:Boolean;
      
      public var bNoAutoFace:Boolean;
      
      public var bNoPursueTarget:Boolean;
      
      public var bDefaultToRanged:Boolean;
      
      public var bFollowSpawner:Boolean;
      
      public var bFastSleepChecks:Boolean;
      
      public var var_969:Boolean;
      
      public var bRoomAggroRadius:Boolean;
      
      public var bSlowOnTheUptake:Boolean;
      
      public var bSkipSpawnState:Boolean;
      
      public var var_1267:Boolean;
      
      public var var_2668:Boolean;
      
      public var var_2565:Boolean;
      
      public var var_1832:Boolean;
      
      public var var_1939:Boolean;
      
      public var var_1608:Boolean;
      
      public var var_752:Boolean;
      
      public var var_983:Boolean;
      
      public var var_1023:Boolean;
      
      public var var_72:Boolean;
      
      public var var_995:Boolean;
      
      public var var_1536:Boolean;
      
      public var bUntargetable:Boolean;
      
      public var var_1124:Boolean;
      
      public var var_1225:Boolean;
      
      public var var_1094:Boolean;
      
      public var var_844:Boolean;
      
      public var var_988:Boolean;
      
      public var var_2117:Boolean;
      
      public var var_1723:Boolean;
      
      public var var_2602:Boolean;
      
      public var var_2200:Boolean;
      
      public var var_2543:Boolean;
      
      public var var_332:Boolean;
      
      public var var_1080:Boolean;
      
      public var var_2135:Boolean;
      
      public var var_1279:Boolean;
      
      public var var_679:Boolean;
      
      public var var_2906:Boolean = false;
      
      public var var_2765:Boolean = false;
      
      public var var_2393:Boolean = false;
      
      public var var_1563:Boolean = false;
      
      public var var_533:Boolean = false;
      
      public var var_1643:Boolean = false;
      
      public var var_2731:Boolean = false;
      
      public var var_2754:Boolean = false;
      
      public var var_2807:Boolean = false;
      
      public var var_2112:Boolean = false;
      
      public var var_2303:Boolean = false;
      
      public var var_2203:Boolean = false;
      
      public function BehaviorType(param1:String = null)
      {
         super();
         if(param1)
         {
            behaviorTypes[param1] = this;
            this.var_1241 = param1;
         }
      }
      
      public static function TweakBehavior(param1:BehaviorType, param2:Array) : BehaviorType
      {
         var _loc4_:Boolean = false;
         var _loc5_:Boolean = false;
         var _loc6_:String = null;
         if(!param1)
         {
            return param1;
         }
         var _loc3_:BehaviorType = param1;
         for(_loc6_ in param2)
         {
            if(_loc6_ in _loc3_)
            {
               _loc4_ = Boolean(_loc3_[_loc6_]);
               if((_loc5_ = Boolean(param2[_loc6_])) != _loc4_)
               {
                  if(_loc3_.var_1241.indexOf("Custom_") != 0)
                  {
                     _loc3_ = _loc3_.method_1823();
                  }
                  _loc3_[_loc6_] = _loc5_;
               }
            }
            else
            {
               class_24.method_19("Tried to tweak a behavior, but \'" + _loc6_ + "\' is not a behavior flag");
            }
         }
         return _loc3_;
      }
      
      public static function method_367(param1:String) : BehaviorType
      {
         var _loc2_:BehaviorType = behaviorTypes[param1];
         return !!_loc2_ ? _loc2_ : behaviorTypes["Null"];
      }
      
      public static function method_592() : void
      {
         var _loc1_:BehaviorType = null;
         _loc1_ = new BehaviorType("Null");
         _loc1_ = new BehaviorType("NPC");
         _loc1_.var_53 = true;
         _loc1_.bNoCombat = true;
         _loc1_.var_1939 = true;
         _loc1_.var_2117 = true;
         _loc1_ = new BehaviorType("NPCDummy");
         _loc1_.bNoAutoFace = true;
         _loc1_.bUntargetable = true;
         _loc1_.var_53 = true;
         _loc1_.bNoCombat = true;
         _loc1_.var_1939 = true;
         _loc1_ = new BehaviorType("GoblinCannon");
         _loc1_.bNoAutoFace = true;
         _loc1_.var_53 = true;
         _loc1_.bUntargetable = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_ = new BehaviorType("FireField");
         _loc1_.bNoAutoFace = true;
         _loc1_.var_53 = true;
         _loc1_.bUntargetable = true;
         _loc1_.var_983 = true;
         _loc1_.var_534 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_1267 = true;
         _loc1_.var_752 = true;
         _loc1_.var_332 = true;
         _loc1_.var_1080 = true;
         _loc1_.var_533 = true;
         _loc1_ = new BehaviorType("PermafrostClone");
         _loc1_.var_53 = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_.var_983 = true;
         _loc1_.var_332 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_534 = true;
         _loc1_.var_1080 = true;
         _loc1_.var_2543 = true;
         _loc1_.var_2135 = true;
         _loc1_.var_533 = true;
         _loc1_ = new BehaviorType("Decoy");
         _loc1_.var_53 = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_.var_983 = true;
         _loc1_.var_332 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_534 = true;
         _loc1_.var_1080 = true;
         _loc1_.var_2135 = true;
         _loc1_.var_533 = true;
         _loc1_.var_72 = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_1723 = true;
         _loc1_ = new BehaviorType("FrostWardTotem");
         _loc1_.bNoAutoFace = true;
         _loc1_.var_53 = true;
         _loc1_.bUntargetable = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_.var_983 = true;
         _loc1_.bFastSleepChecks = true;
         _loc1_.var_534 = true;
         _loc1_.var_533 = true;
         _loc1_.var_332 = true;
         _loc1_ = new BehaviorType("Barrier");
         _loc1_.bNoAutoFace = true;
         _loc1_.bNoPhysics = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_.var_983 = true;
         _loc1_.bFastSleepChecks = true;
         _loc1_.var_1124 = true;
         _loc1_ = new BehaviorType("FrostClone");
         _loc1_.bUntargetable = true;
         _loc1_ = new BehaviorType("TreasureChest");
         _loc1_.bNoCombat = true;
         _loc1_.var_1225 = true;
         _loc1_.bNoPhysics = true;
         _loc1_.var_1832 = true;
         _loc1_.var_2117 = true;
         _loc1_ = new BehaviorType("Chest");
         _loc1_.bNoCombat = true;
         _loc1_.var_1225 = true;
         _loc1_.bNoPhysics = true;
         _loc1_ = new BehaviorType("DramaTargetable");
         _loc1_.var_1124 = true;
         _loc1_ = new BehaviorType("DramaTargetablePreferRanged");
         _loc1_.var_1124 = true;
         _loc1_.var_696 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_ = new BehaviorType("PreferRanged");
         _loc1_.var_696 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_ = new BehaviorType("PrefRangedNoReq");
         _loc1_.var_696 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_53 = true;
         _loc1_ = new BehaviorType("CaveGnome");
         _loc1_.var_696 = true;
         _loc1_.bNoPhysics = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_53 = true;
         _loc1_.var_969 = true;
         _loc1_.var_983 = true;
         _loc1_ = new BehaviorType("Spawner");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.bNoPursueTarget = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_1608 = true;
         _loc1_ = new BehaviorType("LarvaSpawner");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_881 = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.bNoPursueTarget = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_ = new BehaviorType("DesertLarva");
         _loc1_.var_72 = true;
         _loc1_ = new BehaviorType("SandWorm");
         _loc1_.var_881 = true;
         _loc1_.var_72 = true;
         _loc1_ = new BehaviorType("BeehiveSpawner");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.bNoPursueTarget = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_ = new BehaviorType("SpawnerNephit");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_.bSkipSpawnState = false;
         _loc1_.bNoPursueTarget = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_1608 = true;
         _loc1_.bUntargetable = true;
         _loc1_.var_72 = true;
         _loc1_.var_53 = true;
         _loc1_ = new BehaviorType("NephitEye");
         _loc1_.bNoPhysics = true;
         _loc1_.var_72 = true;
         _loc1_.var_995 = true;
         _loc1_.bNoAutoFace = true;
         _loc1_ = new BehaviorType("ServantSpawner");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_53 = true;
         _loc1_.var_995 = true;
         _loc1_.var_72 = true;
         _loc1_.bSkipSpawnState = false;
         _loc1_.bRoomAggroRadius = true;
         _loc1_.bNoPursueTarget = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_1608 = true;
         _loc1_ = new BehaviorType("Switch");
         _loc1_.var_53 = true;
         _loc1_.var_995 = true;
         _loc1_.bNoCombat = true;
         _loc1_.var_1094 = true;
         _loc1_.bNoPhysics = true;
         _loc1_ = new BehaviorType("PowerMarker");
         _loc1_.bNoPhysics = true;
         _loc1_.bUntargetable = true;
         _loc1_.var_53 = true;
         _loc1_.var_72 = true;
         _loc1_.bNoCombat = true;
         _loc1_ = new BehaviorType("PowerMarkerCombat");
         _loc1_.bNoPhysics = true;
         _loc1_.bUntargetable = true;
         _loc1_.var_53 = true;
         _loc1_.var_72 = true;
         _loc1_ = new BehaviorType("Poltergeist");
         _loc1_.var_53 = true;
         _loc1_ = new BehaviorType("Aura");
         _loc1_.bNoPhysics = true;
         _loc1_.var_72 = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_53 = true;
         _loc1_.bUntargetable = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_ = new BehaviorType("DragonPortal");
         _loc1_.bNoPhysics = true;
         _loc1_.var_72 = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_53 = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_.var_1124 = true;
         _loc1_ = new BehaviorType("SandWorm");
         _loc1_.bNoPhysics = true;
         _loc1_.var_72 = true;
         _loc1_ = new BehaviorType("SandWormSubmerge");
         _loc1_.bNoPhysics = true;
         _loc1_.bUntargetable = true;
         _loc1_.var_72 = true;
         _loc1_ = new BehaviorType("Spark");
         _loc1_.bNoPhysics = true;
         _loc1_.var_72 = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_53 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_ = new BehaviorType("Revivable");
         _loc1_.var_995 = true;
         _loc1_ = new BehaviorType("RevivableRanged");
         _loc1_.var_995 = true;
         _loc1_.var_696 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_ = new BehaviorType("Mushroom");
         _loc1_.bNoPhysics = true;
         _loc1_.var_72 = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_53 = true;
         _loc1_.var_1124 = true;
         _loc1_ = new BehaviorType("DarkOrbType");
         _loc1_.bNoPhysics = true;
         _loc1_.var_72 = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_53 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.bUntargetable = true;
         _loc1_ = new BehaviorType("SpikeTrap");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.bUntargetable = true;
         _loc1_.var_53 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_534 = true;
         _loc1_.var_752 = true;
         _loc1_ = new BehaviorType("BannerBearer");
         _loc1_.bSlowOnTheUptake = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_ = new BehaviorType("MineShaft");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.bNoPursueTarget = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_1608 = true;
         _loc1_ = new BehaviorType("NoFall");
         _loc1_.var_696 = true;
         _loc1_ = new BehaviorType("Homing");
         _loc1_.bFastSleepChecks = true;
         _loc1_ = new BehaviorType("Trap");
         _loc1_.bUntargetable = true;
         _loc1_.bNoPhysics = true;
         _loc1_ = new BehaviorType("FollowPet");
         _loc1_.bFollowSpawner = true;
         _loc1_.bFastSleepChecks = true;
         _loc1_.var_969 = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.var_1023 = true;
         _loc1_.var_72 = true;
         _loc1_.var_988 = true;
         _loc1_.var_1536 = true;
         _loc1_.var_1279 = true;
         _loc1_ = new BehaviorType("ScalingFollowPet");
         _loc1_.bFollowSpawner = true;
         _loc1_.bFastSleepChecks = true;
         _loc1_.var_969 = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.var_1023 = true;
         _loc1_.var_72 = true;
         _loc1_.var_988 = true;
         _loc1_.var_1536 = true;
         _loc1_.var_1279 = true;
         _loc1_.var_533 = true;
         _loc1_.var_332 = true;
         _loc1_.var_1563 = true;
         _loc1_ = new BehaviorType("UndeadPet");
         _loc1_.bFollowSpawner = true;
         _loc1_.bFastSleepChecks = true;
         _loc1_.var_969 = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.var_1023 = true;
         _loc1_.var_72 = true;
         _loc1_.var_988 = true;
         _loc1_.var_1536 = true;
         _loc1_.var_1279 = true;
         _loc1_.var_679 = true;
         _loc1_.var_533 = true;
         _loc1_.var_332 = true;
         _loc1_.var_1563 = true;
         _loc1_ = new BehaviorType("UndeadPetRanged");
         _loc1_.bFollowSpawner = true;
         _loc1_.bFastSleepChecks = true;
         _loc1_.var_969 = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.var_1023 = true;
         _loc1_.var_72 = true;
         _loc1_.var_988 = true;
         _loc1_.var_1536 = true;
         _loc1_.var_1279 = true;
         _loc1_.var_679 = true;
         _loc1_.var_533 = true;
         _loc1_.var_332 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_1563 = true;
         _loc1_ = new BehaviorType("Parrot");
         _loc1_.bNoCombat = true;
         _loc1_.var_53 = true;
         _loc1_.bUntargetable = true;
         _loc1_ = new BehaviorType("LittlePet");
         _loc1_.bUntargetable = true;
         _loc1_.bFollowSpawner = true;
         _loc1_.bFastSleepChecks = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.var_72 = true;
         _loc1_.var_844 = true;
         _loc1_ = new BehaviorType("WanderingPet");
         _loc1_.bUntargetable = true;
         _loc1_.var_72 = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.bNoCombat = true;
         _loc1_.var_53 = true;
         _loc1_.var_844 = true;
         _loc1_.var_2602 = true;
         _loc1_ = new BehaviorType("Chains");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoCombat = true;
         _loc1_.var_1094 = true;
         _loc1_ = new BehaviorType("Smashable");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoCombat = true;
         _loc1_.var_53 = true;
         _loc1_ = new BehaviorType("Dummy");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_988 = true;
         _loc1_ = new BehaviorType("HomeDummy");
         _loc1_.bNoPhysics = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.var_53 = true;
         _loc1_.var_2303 = true;
         _loc1_.bNoCombat = true;
         _loc1_.var_2765 = true;
         _loc1_.var_2203 = true;
         _loc1_ = new BehaviorType("Bush");
         _loc1_.bNoPhysics = true;
         _loc1_.var_53 = true;
         _loc1_.var_752 = true;
         _loc1_.var_1939 = true;
         _loc1_ = new BehaviorType("Kraken");
         _loc1_.var_969 = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_72 = true;
         _loc1_ = new BehaviorType("Wisp");
         _loc1_.var_696 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_72 = true;
         _loc1_ = new BehaviorType("Ember");
         _loc1_.var_72 = true;
         _loc1_ = new BehaviorType("DragonSoul");
         _loc1_.var_696 = true;
         _loc1_.bUntargetable = true;
         _loc1_.bFollowSpawner = true;
         _loc1_.bFastSleepChecks = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.var_72 = true;
         _loc1_.var_844 = true;
         _loc1_.var_2200 = true;
         _loc1_.var_332 = true;
         _loc1_ = new BehaviorType("PolarSentry");
         _loc1_.var_53 = true;
         _loc1_.bSkipSpawnState = true;
         _loc1_.var_332 = true;
         _loc1_.var_533 = true;
         _loc1_.var_881 = true;
         _loc1_.var_72 = true;
         _loc1_.bNoPhysics = true;
         _loc1_.var_1023 = true;
         _loc1_.var_533 = true;
         _loc1_.bNoPursueTarget = true;
         _loc1_.bFollowSpawner = true;
         _loc1_.var_1563 = true;
         _loc1_ = new BehaviorType("ActivePet");
         _loc1_.bUntargetable = true;
         _loc1_.var_2393 = true;
         _loc1_.var_332 = true;
         _loc1_.var_1643 = true;
         _loc1_.var_881 = true;
         _loc1_.var_72 = true;
         _loc1_.bNoPursueTarget = true;
         _loc1_.bFollowSpawner = false;
         _loc1_.var_2112 = true;
         _loc1_ = new BehaviorType("SingleTargetPet");
         _loc1_.bUntargetable = true;
         _loc1_.var_2393 = true;
         _loc1_.var_332 = true;
         _loc1_.var_1643 = true;
         _loc1_.var_881 = true;
         _loc1_.var_72 = true;
         _loc1_.bNoPursueTarget = true;
         _loc1_.bFollowSpawner = true;
         _loc1_.var_2731 = true;
         _loc1_.var_2754 = true;
         _loc1_.var_2807 = true;
         _loc1_ = new BehaviorType("DecoyPet");
         _loc1_.var_1643 = true;
         _loc1_.var_881 = true;
         _loc1_.var_72 = true;
         _loc1_.bNoPursueTarget = true;
         _loc1_.var_53 = true;
         _loc1_.bRoomAggroRadius = true;
         _loc1_.var_332 = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.var_534 = true;
         _loc1_.var_1080 = true;
         _loc1_.var_2135 = true;
         _loc1_.var_72 = true;
         _loc1_.var_2112 = true;
         _loc1_ = new BehaviorType("CombatSwitch");
         _loc1_.var_72 = true;
         _loc1_.var_1094 = true;
         _loc1_.bNoPhysics = true;
         _loc1_.bFastSleepChecks = true;
         _loc1_ = new BehaviorType("VigilStraight");
         _loc1_.bNoPhysics = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_1267 = true;
         _loc1_.var_534 = true;
         _loc1_.var_53 = true;
         _loc1_.var_752 = true;
         _loc1_.bUntargetable = true;
         _loc1_ = new BehaviorType("VigilWaterfall");
         _loc1_.bNoPhysics = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_1267 = true;
         _loc1_.var_2668 = true;
         _loc1_.var_534 = true;
         _loc1_.var_53 = true;
         _loc1_.var_752 = true;
         _loc1_.bUntargetable = true;
         _loc1_ = new BehaviorType("VigilFountain");
         _loc1_.bNoPhysics = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_1267 = true;
         _loc1_.var_2565 = true;
         _loc1_.var_534 = true;
         _loc1_.var_53 = true;
         _loc1_.var_752 = true;
         _loc1_.bUntargetable = true;
         _loc1_ = new BehaviorType("VigilTarget");
         _loc1_.bNoPhysics = true;
         _loc1_.bDefaultToRanged = true;
         _loc1_.bNoAutoFace = true;
         _loc1_.var_53 = true;
         _loc1_.bUntargetable = true;
         _loc1_.bRoomAggroRadius = true;
      }
      
      public function method_1823() : BehaviorType
      {
         var _loc1_:ByteArray = new ByteArray();
         registerClassAlias(getQualifiedClassName(BehaviorType),BehaviorType);
         _loc1_.writeObject(this);
         _loc1_.position = 0;
         var _loc2_:BehaviorType = _loc1_.readObject() as BehaviorType;
         _loc2_.var_1241 = "Custom_" + this.var_1241;
         return _loc2_;
      }
   }
}
