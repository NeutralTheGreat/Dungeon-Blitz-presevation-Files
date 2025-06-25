package
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.display.StageAlign;
   import flash.display.StageScaleMode;
   import flash.events.Event;
   import flash.utils.Dictionary;
   
   public class DungeonBlitz extends MovieClip
   {
       
      
      internal var var_2324:Main;
      
      internal var var_2228:Sprite;
      
      internal var var_2489:String;
      
      public function DungeonBlitz()
      {
         super();
         if(stage)
         {
            this.method_861();
         }
         else
         {
            addEventListener(Event.ADDED_TO_STAGE,this.method_861);
         }
      }
      
      public static function method_594() : void
      {
         GfxType.method_125(method_787());
         SuperAnimData.method_125(method_696(),["Animation_Psychophage.swf","Animation_Nephit.swf"],["a__AnimationPetSprite","a__Idol2Animation","a__SpikeTrap","a__WallOfWinter","a__FrozenWardTotem"]);
      }
      
      private static function method_696() : Dictionary
      {
         var _loc1_:Dictionary = new Dictionary();
         _loc1_["a_Cape"] = EntType.HAT_SLOT;
         _loc1_["a_Choker"] = EntType.HAT_SLOT;
         _loc1_["a_Hat"] = EntType.HAT_SLOT;
         _loc1_["a_HatBack"] = EntType.HAT_SLOT;
         _loc1_["a_Mantle"] = EntType.HAT_SLOT;
         _loc1_["a_MantleBack"] = EntType.HAT_SLOT;
         _loc1_["a_Focus"] = EntType.SHIELD_SLOT;
         _loc1_["a_Offhand"] = EntType.SHIELD_SLOT;
         _loc1_["a_Shield"] = EntType.SHIELD_SLOT;
         _loc1_["a_ShieldBack"] = EntType.SHIELD_SLOT;
         _loc1_["a_ShieldSide"] = EntType.SHIELD_SLOT;
         _loc1_["a_ShieldSideBack"] = EntType.SHIELD_SLOT;
         _loc1_["a_ShieldSwoosh01"] = EntType.SHIELD_SLOT;
         _loc1_["a_ShootEffect"] = EntType.SHIELD_SLOT;
         _loc1_["a_Hand"] = EntType.GLOVES_SLOT;
         _loc1_["a_Hand1"] = EntType.GLOVES_SLOT;
         _loc1_["a_Hand2"] = EntType.GLOVES_SLOT;
         _loc1_["a_Hand3"] = EntType.GLOVES_SLOT;
         _loc1_["a_Hand4"] = EntType.GLOVES_SLOT;
         _loc1_["a_Hand5"] = EntType.GLOVES_SLOT;
         _loc1_["a_Hand02"] = EntType.GLOVES_SLOT;
         _loc1_["a_Hand03"] = EntType.GLOVES_SLOT;
         _loc1_["a_Hand04"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandFist1"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandFist2"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandFist3"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandFist4"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandFist4R"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandFist5R"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandFistback"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandL"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandL2"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandL3"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandL4"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandL5"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandL6"] = EntType.GLOVES_SLOT;
         _loc1_["a_HandR"] = EntType.GLOVES_SLOT;
         _loc1_["a_LArm"] = EntType.GLOVES_SLOT;
         _loc1_["a_LArmL"] = EntType.GLOVES_SLOT;
         _loc1_["a_LArmL2"] = EntType.GLOVES_SLOT;
         _loc1_["a_LArmL3"] = EntType.GLOVES_SLOT;
         _loc1_["a_LArmR"] = EntType.GLOVES_SLOT;
         _loc1_["a_LArmR2"] = EntType.GLOVES_SLOT;
         _loc1_["a_Belt"] = EntType.ARMOR_SLOT;
         _loc1_["a_Shoulder"] = EntType.ARMOR_SLOT;
         _loc1_["a_Skirt"] = EntType.ARMOR_SLOT;
         _loc1_["a_ULeg"] = EntType.ARMOR_SLOT;
         _loc1_["a_Torso"] = EntType.ARMOR_SLOT;
         _loc1_["a_Torso2"] = EntType.ARMOR_SLOT;
         _loc1_["a_TorsoSide"] = EntType.ARMOR_SLOT;
         _loc1_["a_UArm"] = EntType.ARMOR_SLOT;
         _loc1_["a_UArm02"] = EntType.ARMOR_SLOT;
         _loc1_["a_UArmL"] = EntType.ARMOR_SLOT;
         _loc1_["a_UArmLBack"] = EntType.ARMOR_SLOT;
         _loc1_["a_UArmR"] = EntType.ARMOR_SLOT;
         _loc1_["a_UArmRF"] = EntType.ARMOR_SLOT;
         _loc1_["a_UArmRMelee"] = EntType.ARMOR_SLOT;
         _loc1_["a_ULegL"] = EntType.ARMOR_SLOT;
         _loc1_["a_ULegL2"] = EntType.ARMOR_SLOT;
         _loc1_["a_ULegR"] = EntType.ARMOR_SLOT;
         _loc1_["a_Waist"] = EntType.ARMOR_SLOT;
         _loc1_["a_Waist2"] = EntType.ARMOR_SLOT;
         _loc1_["a_WaistRun"] = EntType.ARMOR_SLOT;
         _loc1_["a_WaistSide"] = EntType.ARMOR_SLOT;
         _loc1_["a_Leg"] = EntType.ARMOR_SLOT;
         _loc1_["a_Leg02"] = EntType.ARMOR_SLOT;
         _loc1_["a_Foot01"] = EntType.BOOTS_SLOT;
         _loc1_["a_Foot02"] = EntType.BOOTS_SLOT;
         _loc1_["a_Foot03"] = EntType.BOOTS_SLOT;
         _loc1_["a_Foot04"] = EntType.BOOTS_SLOT;
         _loc1_["a_FootFront"] = EntType.BOOTS_SLOT;
         _loc1_["a_FootL"] = EntType.BOOTS_SLOT;
         _loc1_["a_FootR"] = EntType.BOOTS_SLOT;
         _loc1_["a_Foot1"] = EntType.BOOTS_SLOT;
         _loc1_["a_Foot2"] = EntType.BOOTS_SLOT;
         _loc1_["a_Foot3"] = EntType.BOOTS_SLOT;
         _loc1_["a_Foot4"] = EntType.BOOTS_SLOT;
         _loc1_["a_LLeg"] = EntType.BOOTS_SLOT;
         _loc1_["a_LLeg1"] = EntType.BOOTS_SLOT;
         _loc1_["a_LLeg2"] = EntType.BOOTS_SLOT;
         _loc1_["a_LLeg3"] = EntType.BOOTS_SLOT;
         _loc1_["a_LLegDeath"] = EntType.BOOTS_SLOT;
         _loc1_["a_LLegFront"] = EntType.BOOTS_SLOT;
         _loc1_["a_LLegL"] = EntType.BOOTS_SLOT;
         _loc1_["a_LLegR"] = EntType.BOOTS_SLOT;
         _loc1_["a_ToeHeelUp"] = EntType.BOOTS_SLOT;
         _loc1_["a_ToeL"] = EntType.BOOTS_SLOT;
         _loc1_["a_ToeR"] = EntType.BOOTS_SLOT;
         _loc1_["a_Spark"] = EntType.SWORD_SLOT;
         _loc1_["a_Sword"] = EntType.SWORD_SLOT;
         _loc1_["a_SwordGrip"] = EntType.SWORD_SLOT;
         return _loc1_;
      }
      
      private static function method_787() : Array
      {
         var _loc1_:Array = new Array();
         _loc1_["AbSkin"] = 15123652;
         _loc1_["AbSkinDk"] = 12940918;
         _loc1_["AbTrim"] = 3368448;
         _loc1_["CySkinLt"] = 12549269;
         _loc1_["CySkin"] = 9198444;
         _loc1_["CySkinDk"] = 5058874;
         _loc1_["CyArmorLt"] = 16776960;
         _loc1_["CyArmor"] = 11776768;
         _loc1_["CyArmorDk"] = 7697664;
         _loc1_["CyHair"] = 10040064;
         _loc1_["CyCloth"] = 3302962;
         _loc1_["CyClothDk"] = 2048031;
         _loc1_["DrSkin"] = 9182236;
         _loc1_["DrSkinDk"] = 5050127;
         _loc1_["DrBelly"] = 13404712;
         _loc1_["DrBellyDk"] = 8410649;
         _loc1_["DrWing"] = 15124636;
         _loc1_["DrWingDk"] = 12560001;
         _loc1_["DrFur"] = 13421772;
         _loc1_["DrFurDk"] = 10066329;
         _loc1_["DvSkin"] = 39168;
         _loc1_["DvSkinDk"] = 26112;
         _loc1_["GhSkin"] = 11197155;
         _loc1_["GhSkinDk"] = 8825523;
         _loc1_["GhTrim"] = 3754061;
         _loc1_["GoSkin"] = 5020057;
         _loc1_["GoSkinDk"] = 3765107;
         _loc1_["GoMantle"] = 16514043;
         _loc1_["GoMantleDk"] = 13224393;
         _loc1_["GoArmor"] = 3435316;
         _loc1_["GoArmorDk"] = 2642472;
         _loc1_["LzSkin"] = 12566386;
         _loc1_["LzSkinDk"] = 6842415;
         _loc1_["MaSkin"] = 16706228;
         _loc1_["MaSkinDk"] = 11567362;
         _loc1_["MaHairLt"] = 5474204;
         _loc1_["MaHair"] = 13158;
         _loc1_["PaBoots"] = 9136438;
         _loc1_["PaBootsDk"] = 6572838;
         _loc1_["PaHair"] = 13158;
         _loc1_["PaHairLt"] = 5474204;
         _loc1_["PaPants"] = 2957585;
         _loc1_["PaPantsLt"] = 4009238;
         _loc1_["PaLoin"] = 5832704;
         _loc1_["PaLoinDk"] = 3932160;
         _loc1_["PaGloves"] = 8802330;
         _loc1_["PaSuit"] = 5267552;
         _loc1_["PaSuitDk"] = 3162176;
         _loc1_["PaSkin"] = 13083501;
         _loc1_["PaSkinDk"] = 11109711;
         _loc1_["PcBlueLt"] = 13693168;
         _loc1_["PcBlue"] = 8438000;
         _loc1_["PcBlueDk"] = 28896;
         _loc1_["PcRed"] = 11534336;
         _loc1_["PcRedDk"] = 6291456;
         _loc1_["PcPale"] = 15790240;
         _loc1_["PcSuit"] = 5267552;
         _loc1_["PcSuitDk"] = 3162176;
         _loc1_["PcPants"] = 6382179;
         _loc1_["PcPantsDk"] = 4276803;
         _loc1_["PsSkinLt"] = 10040217;
         _loc1_["PsSkin"] = 6697830;
         _loc1_["PsSkinDk"] = 6684723;
         _loc1_["PsIris"] = 16711680;
         _loc1_["PsIrisDk"] = 10027008;
         _loc1_["PsWhite"] = 15462874;
         _loc1_["PsWhiteDk"] = 10140493;
         _loc1_["RgCloakLt"] = 6710886;
         _loc1_["RgCloak"] = 4473924;
         _loc1_["RgCloakDk"] = 3355443;
         _loc1_["RgCloakVDk"] = 2500134;
         _loc1_["RhSkinLt"] = 10724259;
         _loc1_["RhSkin"] = 9276813;
         _loc1_["RhSkinDk"] = 6840930;
         _loc1_["RhEyes"] = 2740196;
         _loc1_["RhTeeth"] = 16777215;
         _loc1_["RhTongue"] = 15510957;
         _loc1_["RhMouth"] = 6890014;
         _loc1_["RpSkin"] = 8413023;
         _loc1_["RpSkinDk"] = 5060921;
         _loc1_["RpBelly"] = 11764868;
         _loc1_["RpBellyDk"] = 9201511;
         _loc1_["RpStripes"] = 16777011;
         _loc1_["RpStripesDk"] = 16759603;
         _loc1_["RpEye"] = 16762214;
         _loc1_["RpEyeDk"] = 13732116;
         _loc1_["RpFringe"] = 3023394;
         _loc1_["DmArmorLt"] = 14213092;
         _loc1_["DmArmor"] = 10662591;
         _loc1_["DmArmorDk"] = 7108224;
         _loc1_["DmArmorTrim"] = 6515829;
         _loc1_["DmArmorTrimDk"] = 4936281;
         _loc1_["DmFur"] = 13421772;
         _loc1_["DmFurDk"] = 9211020;
         _loc1_["DmFurTrim"] = 5855577;
         _loc1_["DmFurTrimDk"] = 3162945;
         _loc1_["DmCloth"] = 5834760;
         _loc1_["DmHorn"] = 3618362;
         _loc1_["DmHornDk"] = 2500134;
         _loc1_["DmBone"] = 14269069;
         _loc1_["DmBoneDk"] = 8416595;
         _loc1_["HmCloth"] = 11711392;
         _loc1_["HmClothDk"] = 15066830;
         _loc1_["HmClothTrim"] = 7539467;
         _loc1_["HmClothTrimDk"] = 5834760;
         _loc1_["HmArmorLt"] = 14282239;
         _loc1_["HmArmor"] = 10662591;
         _loc1_["HmArmorDk"] = 7108224;
         _loc1_["HmArmorTrim"] = 6515829;
         _loc1_["HmArmorTrimDk"] = 4936281;
         _loc1_["HmCoatLt"] = 10914412;
         _loc1_["HmCoat"] = 8416083;
         _loc1_["HmCoatDk"] = 6706498;
         _loc1_["HmCoatTrim"] = 14275000;
         _loc1_["HmCoatTrimDk"] = 10064770;
         _loc1_["HmHorn"] = 14269069;
         _loc1_["HmHornDk"] = 7561546;
         _loc1_["HmHoof"] = 4210752;
         _loc1_["HmHoofDk"] = 3026478;
         _loc1_["SkSkin"] = 16706228;
         _loc1_["SkSkinDk"] = 11567362;
         _loc1_["SpBigLt"] = 6710886;
         _loc1_["SpBig"] = 3355443;
         _loc1_["SpBigDk"] = 2500134;
         _loc1_["SpBigBelly"] = 6890014;
         _loc1_["SpBigBellyDk"] = 4199442;
         _loc1_["Sp1SkinLt"] = 5782886;
         _loc1_["Sp1Skin"] = 4665682;
         _loc1_["Sp1SkinDk"] = 3614272;
         _loc1_["Sp2SkinLt"] = 4541757;
         _loc1_["Sp2Skin"] = 6779740;
         _loc1_["Sp2SkinDk"] = 9017722;
         _loc1_["TrSkinLt"] = 5388312;
         _loc1_["TrSkin"] = 6965536;
         _loc1_["TrSkinDk"] = 9005109;
         _loc1_["VgSkin"] = 11776768;
         _loc1_["VgSkinDk"] = 7697664;
         _loc1_["gWhite"] = 16777215;
         _loc1_["gWhiteDk"] = 10065033;
         _loc1_["gBeige"] = 14664838;
         _loc1_["gBeigeDk"] = 11573865;
         _loc1_["gGray"] = 5066061;
         _loc1_["gGrayDk"] = 2500134;
         _loc1_["gPurple"] = 5844927;
         _loc1_["gPurpleDk"] = 3217766;
         _loc1_["gPaleRed"] = 14232877;
         _loc1_["gPaleRedDk"] = 10883602;
         _loc1_["gPaleOrange"] = 14398976;
         _loc1_["gPaleOrangeDk"] = 14251776;
         _loc1_["gPaleBlue"] = 12382718;
         _loc1_["gPaleBlueDk"] = 1871101;
         _loc1_["gDeepRed"] = 9175040;
         _loc1_["gDeepRedDk"] = 4194304;
         _loc1_["gPink"] = 16744319;
         _loc1_["gPinkDk"] = 11556695;
         _loc1_["gGold"] = 15121202;
         _loc1_["gGoldDk"] = 10058785;
         _loc1_["gPaleGreen"] = 5341281;
         _loc1_["gPaleGreenDk"] = 2506030;
         _loc1_["gDeepBlue"] = 277626;
         _loc1_["gDeepBlueDk"] = 207181;
         _loc1_["gBronze"] = 16764031;
         _loc1_["gBronzeDk"] = 10906647;
         _loc1_["gPaleBrown"] = 10053964;
         _loc1_["gPaleBrownDk"] = 6175266;
         _loc1_["gSilver"] = 14014399;
         _loc1_["gSilverDk"] = 9079932;
         return _loc1_;
      }
      
      public function method_861(param1:Event = null) : void
      {
         var _loc2_:String = null;
         var _loc3_:String = null;
         DevSettings.method_275();
         stage.scaleMode = StageScaleMode.NO_SCALE;
         stage.align = StageAlign.TOP_LEFT;
         this.var_2228 = new Sprite();
         addChild(this.var_2228);
         if(!(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
         {
            _loc2_ = ResourceManager.method_1071(root);
            _loc3_ = ResourceManager.method_1544(stage,"www.dungeonblitz.com","db.bmgstatic.com","/p/");
         }
         this.var_2489 = !!(DevSettings.flags & DevSettings.DEVFLAG_ADDXMLDEVSETTINGS) ? ResourceManager.const_512 : ResourceManager.const_192;
         addEventListener(Event.ENTER_FRAME,this.method_916);
         method_594();
         class_23.method_1579(Camera.SCREEN_WIDTH * 0.5,Camera.PLAY_SCREEN_HEIGHT,0,4,100);
         class_4.method_125("UI_General_Click_Button_Soft");
         this.method_1059();
         ResourceManager.method_125(["Login","Lib","Core","Game","Level"]);
         this.method_1557();
         class_14.method_1668();
         ResourceManager.method_1913(root.loaderInfo.parameters.fv,_loc3_);
      }
      
      private function method_916(param1:Event) : void
      {
         ResourceManager.method_783();
         if(ResourceManager.method_149(this.var_2489))
         {
            this.method_1466();
            removeEventListener(Event.ENTER_FRAME,this.method_916);
         }
      }
      
      private function method_1466() : void
      {
         this.var_2324 = new Main();
         this.var_2228.addChild(this.var_2324);
         this.var_2324.Init();
      }
      
      private function method_1557() : void
      {
         ResourceManager.method_41("EntTypes",EntType.method_30);
         ResourceManager.method_41("GearTypes",GearType.method_30);
         ResourceManager.method_41("PlayerPowerTypes",PowerType.method_476);
         ResourceManager.method_41("MonsterPowerTypes",PowerType.method_505);
         ResourceManager.method_41("PlayerBuffTypes",BuffType.method_476);
         ResourceManager.method_41("MonsterBuffTypes",BuffType.method_505);
         ResourceManager.method_41("CharmTypes",class_1.method_30);
         ResourceManager.method_41("MaterialTypes",class_8.method_30);
         ResourceManager.method_41("MagicTypes",MagicType.method_30);
         ResourceManager.method_41("MountTypes",class_20.method_30);
         ResourceManager.method_41("PetTypes",class_7.method_30);
         ResourceManager.method_41("MissionTypes",class_13.method_30);
         ResourceManager.method_41("MissionGroups",class_5.method_30);
         ResourceManager.method_41("DoorTypes",class_11.method_30);
         ResourceManager.method_41("TooltipTypes",class_19.method_30);
         ResourceManager.method_41("DyeTypes",class_21.method_30);
         ResourceManager.method_41("LevelTypes",class_2.method_30);
         ResourceManager.method_41("SoundConfig",SoundConfig.method_30);
         ResourceManager.method_41("NodeTypes",class_22.method_30);
         ResourceManager.method_41("AbilityTypes",class_10.method_30);
         ResourceManager.method_41("PowerModTypes",class_17.method_30);
         ResourceManager.method_41("BuildingTypes",class_9.method_30);
         ResourceManager.method_41("EggTypes",class_16.method_30);
         ResourceManager.method_41("StatueTypes",class_6.method_30);
         ResourceManager.method_41("LockboxTypes",class_15.method_30);
         ResourceManager.method_41("RoyalStoreTypes",class_12.method_30);
         ResourceManager.method_41("ConsumableTypes",class_3.method_30);
         ResourceManager.method_41("RewardpackTypes",class_18.method_30);
      }
      
      private function method_1059() : void
      {
         CollisionManager.method_77(CollisionManager.RED_LINE,CollisionManager.SOFT_FLOOR);
         CollisionManager.method_77(CollisionManager.CYAN_LINE,CollisionManager.HARD_FLOOR);
         CollisionManager.method_77(CollisionManager.WHITE_LINE,CollisionManager.TRIGGER_BOUNDARY);
         CollisionManager.method_77(CollisionManager.BLUE_LINE,CollisionManager.HARD_FLOOR | Game.const_140);
         CollisionManager.method_77(CollisionManager.MAGENTA_LINE,CollisionManager.SOFT_FLOOR | Game.const_140);
         CollisionManager.method_77(CollisionManager.GREEN_LINE,Game.const_140 | Game.const_391);
         CollisionManager.method_77(CollisionManager.YELLOW_LINE,Game.const_152);
         CollisionManager.method_77(CollisionManager.const_1140,Game.const_152 | Game.const_413);
         CollisionManager.method_77(CollisionManager.BLACK_LINE,Game.const_237 | Game.const_391);
         CollisionManager.method_77(CollisionManager.const_1109,Game.const_160);
         CollisionManager.method_77(CollisionManager.const_1132,Game.const_160);
         CollisionManager.method_77(CollisionManager.const_1224,Game.const_160 | Game.const_469);
         CollisionManager.method_77(CollisionManager.const_882,Game.const_160 | Game.const_682);
         CollisionManager.method_77(CollisionManager.const_1215,Game.const_250);
      }
   }
}
