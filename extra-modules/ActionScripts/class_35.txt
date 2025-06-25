package
{
   import flash.utils.Dictionary;
   
   public class class_35
   {
      
      public static const const_379:Dictionary = method_911();
       
      
      internal var var_160:String;
      
      internal var displayName:String;
      
      internal var var_1701:Vector.<class_13>;
      
      internal var var_1886:Vector.<class_13>;
      
      public function class_35(param1:String)
      {
         super();
         this.var_160 = param1;
         this.displayName = const_379[this.var_160];
         this.var_1701 = new Vector.<class_13>();
         this.var_1886 = new Vector.<class_13>();
      }
      
      private static function method_911() : Dictionary
      {
         var _loc3_:String = null;
         var _loc1_:Dictionary = new Dictionary();
         _loc1_["CaptainFink"] = "Captain Fink";
         _loc1_["Anna"] = "Anna";
         _loc1_["AnnaOutside"] = "Anna";
         _loc1_["NR_QuestAnna01"] = "Anna";
         _loc1_["NR_QuestAnna02"] = "Anna";
         _loc1_["NR_QuestAnna03"] = "Anna";
         _loc1_["NR_Mayor01"] = "Mayor Ristas";
         _loc1_["NR_VillageSoldier"] = "Lost Militiaman";
         _loc1_["NR_CartGuy"] = "Otto";
         _loc1_["NR_Villager02"] = "Jarvis";
         _loc1_["NR_Villager03"] = "Jerdus";
         _loc1_["NR_Hermit"] = "Herman";
         _loc1_["SRN_Mayor01"] = "Alderman Abbod";
         _loc1_["Dane"] = "Dane";
         _loc1_["SRN_Mayor02"] = "Affric";
         _loc1_["Kenelm"] = "Kenelm";
         _loc1_["SRN_Mayor03"] = "Gehrin";
         _loc1_["Odem"] = "Odem";
         _loc1_["Ield"] = "Ield";
         _loc1_["Palok"] = "Palok";
         _loc1_["Rose"] = "Rose";
         _loc1_["Sugh"] = "Sugh";
         _loc1_["Gran"] = "Headwoman Gran";
         _loc1_["Gretta"] = "Gretta";
         _loc1_["BT_Greeter"] = "Richan";
         _loc1_["BT_Warden"] = "Warden Maximilian";
         _loc1_["BT_Mayor01"] = "Steward of Felbridge";
         _loc1_["BT_SubWarden"] = "Sub-Warden Gunter";
         _loc1_["CH_Mayor01"] = "Captain Gar";
         _loc1_["CH_Mayor02"] = "Yagarah";
         _loc1_["CH_Scout"] = "Yagarah";
         _loc1_["CH_Villager01"] = "Jothren";
         _loc1_["CH_Villager02"] = "Renlin";
         _loc1_["CH_Villager03"] = "Arliss";
         _loc1_["OMM_Scout01"] = "Shamar";
         _loc1_["OMM_Mayor01"] = "Adohi";
         _loc1_["OMM_Moai01"] = "Onyx Moai";
         _loc1_["OMM_Moai02"] = "Jade Moai";
         _loc1_["OMM_Moai03"] = "Stone Moai";
         _loc1_["OMM_Statue01"] = "Iron Statue";
         _loc1_["OMM_Villager01"] = "Ormos";
         _loc1_["OMM_Villager02"] = "Amilie";
         _loc1_["OMM_Villager03"] = "Keenai";
         _loc1_["EG_Scout01"] = "Wildbark";
         _loc1_["EG_Mayor01"] = "Longroot";
         _loc1_["EG_Villager01"] = "Oak";
         _loc1_["EG_Villager02"] = "River";
         _loc1_["EG_Villager03"] = "Briarbranch";
         _loc1_["AC_Mayor01"] = "Butcher\'s Boy";
         _loc1_["AC_Titus01"] = "Titus";
         _loc1_["AC_Titus02"] = "Titus";
         _loc1_["AC_Titus03"] = "Titus";
         _loc1_["AC_Villager03"] = "Kessa";
         _loc1_["AC_Villager04"] = "Laina";
         _loc1_["AC_Villager05"] = "Reishi";
         _loc1_["SD_Titus01"] = "Titus";
         _loc1_["SD_Titus02"] = "Titus";
         _loc1_["SD_Acolyte01"] = "Omshi";
         _loc1_["SD_Acolyte02"] = "Hontai";
         _loc1_["SD_Slave01"] = "Zib";
         _loc1_["SD_Nomad01"] = "Alzrebi";
         _loc1_["SD_Mayor01"] = "Kenken";
         _loc1_["SD_Matron01"] = "Ivetta";
         _loc1_["SD_Gladiator01"] = "Zumwalt";
         _loc1_["SD_Chief01"] = "Gzarek";
         _loc1_["SD_Emissary02"] = "Gzagg";
         _loc1_["SD_Jackal01"] = "Rathbone";
         _loc1_["SD_Jackal02"] = "Rathbone";
         _loc1_["VH_Odin01"] = "Odryn";
         _loc1_["VH_FabMab01"] = "Ma Mab";
         _loc1_["VH_FabMab02"] = "Ma Mab";
         _loc1_["VH_Jackal02"] = "Rathbone";
         _loc1_["VH_Skitts01"] = "Skitts";
         _loc1_["VH_Vagrant01"] = "The Mushroom Man";
         _loc1_["VH_Rebel01"] = "Hank the Tank";
         _loc1_["VH_Rebel02"] = "Finn";
         _loc1_["VH_Monk01"] = "Odo";
         _loc1_["VH_TheName"] = "Plaseebo";
         _loc1_["SD_Sage01"] = "Siggin";
         _loc1_["KP_Steward"] = "Innkeeper";
         _loc1_["NR_Researcher"] = "Researcher";
         _loc1_["SD_OgreMagus"] = "Ogre Magus";
         _loc1_["SD_MeanGoblin"] = "Frikig";
         _loc1_["SD_NiceGoblin"] = "Gigrik";
         _loc1_["SD_Savant"] = "Savant";
         var _loc2_:Vector.<String> = new Vector.<String>();
         for(_loc3_ in _loc1_)
         {
            _loc2_.push(_loc3_);
         }
         for each(_loc3_ in _loc2_)
         {
            _loc1_[_loc3_ + "Hard"] = _loc1_[_loc3_];
         }
         return _loc1_;
      }
      
      public static function method_820(param1:String, param2:Array, param3:Dictionary) : class_35
      {
         var _loc4_:class_35;
         if(!(_loc4_ = param3[param1]))
         {
            if(!(_loc4_ = new class_35(param1)).displayName)
            {
               class_24.method_7("ContactType: No display name defined for contact: " + param1);
            }
            param2.push(_loc4_);
            param3[param1] = _loc4_;
         }
         return _loc4_;
      }
   }
}
