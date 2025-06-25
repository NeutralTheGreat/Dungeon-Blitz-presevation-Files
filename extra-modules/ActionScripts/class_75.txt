package
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.filters.GlowFilter;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   import flash.utils.Dictionary;
   
   public class class_75 extends class_32
   {
      
      private static const const_485:uint = 97;
      
      private static var var_1470:Array = new Array();
      
      private static const const_124:Number = 100;
      
      private static const const_1087:Number = 30;
      
      private static const const_860:Number = 10;
      
      private static const const_1121:uint = 0;
      
      private static const const_1088:uint = 1;
      
      private static const const_1012:uint = 2;
      
      private static const const_13:uint = 6;
      
      private static const const_1379:uint = 10;
      
      private static const const_100:uint = class_86.const_373;
      
      private static const const_128:uint = 3;
      
      private static const const_475:uint = 18;
      
      private static const const_1352:uint = 6;
      
      private static const const_125:uint = 6;
      
      private static const const_1364:uint = 36;
      
      private static const const_398:uint = 100;
      
      private static const const_717:uint = 0;
      
      private static const const_681:uint = 1;
      
      private static const const_741:uint = 2;
      
      private static const const_832:uint = 3;
      
      private static const const_752:uint = 4;
      
      private static const const_769:uint = 5;
      
      private static const const_1311:uint = 6;
      
      private static const const_165:Vector.<String> = new Vector.<String>(const_13,true);
      
      private static const const_145:Dictionary = new Dictionary();
      
      private static const const_198:Dictionary = new Dictionary();
      
      private static const const_620:GlowFilter = new GlowFilter(16777062,1,6,6,10);
      
      private static const const_221:uint = 10;
      
      private static const const_173:uint = 11;
      
      {
         const_165[const_717] = "Infernal";
         const_165[const_681] = "Draconic";
         const_165[const_741] = "Mythic";
         const_165[const_832] = "Sylvan";
         const_165[const_752] = "Trog";
         const_165[const_769] = "Undead";
         const_145["Infernal"] = const_717;
         const_145["Draconic"] = const_681;
         const_145["Mythic"] = const_741;
         const_145["Sylvan"] = const_832;
         const_145["Trog"] = const_752;
         const_145["Undead"] = const_769;
         const_198["M"] = const_1121;
         const_198["R"] = const_1088;
         const_198["L"] = const_1012;
      }
      
      public var var_60:class_33;
      
      private var var_2387:class_33;
      
      private var var_1699:class_33;
      
      private var var_1658:class_138;
      
      private var var_621:class_33;
      
      private var var_639:class_33;
      
      private var var_579:uint;
      
      private var var_921:uint;
      
      private var var_1727:uint;
      
      private var var_41:int;
      
      private var var_116:uint;
      
      internal var var_105:class_3;
      
      private var var_1475:class_33;
      
      private var var_1172:class_33;
      
      private var var_448:class_33;
      
      private var var_1898:class_33;
      
      private var var_1178:class_138;
      
      private var var_607:Boolean;
      
      private var var_624:Boolean;
      
      private var var_887:Boolean;
      
      private var var_2106:class_33;
      
      private var var_1893:uint;
      
      private var var_1104:class_33;
      
      private var var_1497:class_33;
      
      private var var_1485:class_33;
      
      private var var_1155:class_33;
      
      private var var_1277:class_33;
      
      private var var_1123:class_33;
      
      private var var_1382:class_33;
      
      private var var_1365:Vector.<class_33>;
      
      private var var_1755:Vector.<class_33>;
      
      private var var_948:Vector.<class_33>;
      
      private var var_1633:Vector.<TextField>;
      
      private var var_1416:Vector.<uint>;
      
      private var var_158:Vector.<Vector.<Vector.<class_8>>>;
      
      private var var_290:Vector.<Vector.<class_33>>;
      
      private var var_957:Vector.<class_33>;
      
      private var var_438:Rectangle;
      
      private var var_1355:uint;
      
      private var var_1010:Vector.<uint>;
      
      private var var_1342:Vector.<uint>;
      
      private var var_1676:Vector.<Number>;
      
      private var var_1092:Vector.<Vector.<uint>>;
      
      private var var_920:Vector.<Vector.<class_33>>;
      
      private var var_469:Array;
      
      private var var_862:Vector.<Boolean>;
      
      private var var_1919:Vector.<class_33>;
      
      private var var_2332:class_33;
      
      private var var_2435:class_33;
      
      private var var_1610:class_33;
      
      private var var_1912:Vector.<class_33>;
      
      private var var_1239:Vector.<class_33>;
      
      private var var_1437:class_33;
      
      private var var_2007:class_33;
      
      private var var_1799:Vector.<class_33>;
      
      private var var_174:class_33;
      
      private var var_1284:class_33;
      
      private var var_894:class_33;
      
      private var var_684:class_33;
      
      private var var_1056:class_33;
      
      private var var_1072:class_33;
      
      private var var_1581:class_33;
      
      private var var_1409:class_33;
      
      private var var_461:Vector.<class_33>;
      
      private var var_2182:class_138;
      
      private var var_1664:class_33;
      
      private var var_1803:class_33;
      
      private var var_1328:class_33;
      
      private var var_1134:class_33;
      
      private var var_1628:class_33;
      
      private var var_1048:class_33;
      
      private var var_1324:class_33;
      
      private var var_2544:class_33;
      
      private var var_2835:class_33;
      
      private var var_1514:class_33;
      
      private var var_1115:Boolean = false;
      
      private var var_449:class_33;
      
      private var var_261:class_33;
      
      private var var_614:class_33;
      
      private var var_1554:class_33;
      
      private var var_1838:class_33;
      
      private var var_671:class_33;
      
      private var var_1180:class_33;
      
      private var var_1972:class_33;
      
      private var var_2292:Vector.<class_33>;
      
      private var var_1481:Vector.<Boolean>;
      
      private var var_2134:class_33;
      
      public function class_75(param1:Game)
      {
         super(param1,"a_ScreenMagicForge","am_Panel");
      }
      
      public static function method_1028(param1:class_76, param2:class_76) : int
      {
         var _loc3_:class_8 = param1.materialType;
         var _loc4_:class_8 = param2.materialType;
         var _loc5_:uint = class_8.method_220(_loc3_.var_139);
         var _loc6_:uint = class_8.method_220(_loc4_.var_139);
         if(_loc5_ < _loc6_)
         {
            return 1;
         }
         if(_loc5_ > _loc6_)
         {
            return -1;
         }
         var _loc7_:uint = param1.var_181;
         var _loc8_:uint = param2.var_181;
         if(_loc7_ < _loc8_)
         {
            return 1;
         }
         if(_loc7_ > _loc8_)
         {
            return -1;
         }
         return param1.materialType.var_140 < param2.materialType.var_140 ? 1 : -1;
      }
      
      public static function method_1201(param1:class_76, param2:class_76) : int
      {
         var _loc3_:class_8 = param1.materialType;
         var _loc4_:class_8 = param2.materialType;
         var _loc5_:uint = class_8.method_220(_loc3_.var_139);
         var _loc6_:uint = class_8.method_220(_loc4_.var_139);
         if(_loc5_ < _loc6_)
         {
            return 1;
         }
         if(_loc5_ > _loc6_)
         {
            return -1;
         }
         var _loc7_:String = _loc3_.var_103;
         var _loc8_:String = _loc4_.var_103;
         if(_loc7_ == "Infernal")
         {
            return -1;
         }
         if(_loc8_ == "Infernal")
         {
            return 1;
         }
         if(_loc7_ == "Draconic")
         {
            return -1;
         }
         if(_loc8_ == "Draconic")
         {
            return 1;
         }
         if(_loc7_ == "Mythic")
         {
            return -1;
         }
         if(_loc8_ == "Mythic")
         {
            return 1;
         }
         if(_loc7_ == "Sylvan")
         {
            return -1;
         }
         if(_loc8_ == "Sylvan")
         {
            return 1;
         }
         if(_loc7_ == "Trog")
         {
            return -1;
         }
         if(_loc8_ == "Trog")
         {
            return 1;
         }
         return param1.materialType.var_140 < param2.materialType.var_140 ? 1 : -1;
      }
      
      public static function method_337(param1:uint) : uint
      {
         var _loc2_:class_1 = class_14.var_767[param1];
         if(!_loc2_)
         {
            return 0;
         }
         var _loc3_:uint = 0;
         while(_loc3_ < class_64.const_26.length)
         {
            if(_loc2_.var_115 == class_64.const_26[_loc3_])
            {
               return _loc3_;
            }
            _loc3_++;
         }
         return 0;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc13_:MovieClip = null;
         var _loc14_:Vector.<class_33> = null;
         var _loc15_:uint = 0;
         var _loc16_:Rectangle = null;
         var _loc17_:MovieClip = null;
         var _loc18_:MovieClip = null;
         var _loc19_:Vector.<class_33> = null;
         var _loc20_:class_33 = null;
         var_1470[const_485] = new class_76(1,class_14.var_629[const_485]);
         var _loc1_:MovieClip = var_2.am_MaterialLists;
         this.var_1010 = new Vector.<uint>(const_13,true);
         this.var_1342 = new Vector.<uint>(const_13,true);
         this.var_1676 = new Vector.<Number>(const_13,true);
         this.var_920 = new Vector.<Vector.<class_33>>(const_13,true);
         this.var_1092 = new Vector.<Vector.<uint>>(const_13,true);
         var _loc2_:uint = 0;
         while(_loc2_ < const_13)
         {
            _loc13_ = _loc1_["am_List" + _loc2_] as MovieClip;
            _loc14_ = new Vector.<class_33>(const_125,true);
            _loc15_ = 0;
            while(_loc15_ < const_125)
            {
               _loc14_[_loc15_] = method_3(_loc13_["am_Slot" + _loc15_] as MovieClip,_loc2_ * const_125 + _loc15_,this.method_1605,this.method_1331,this.method_1564);
               _loc15_++;
            }
            this.var_920[_loc2_] = _loc14_;
            this.var_1092[_loc2_] = new Vector.<uint>(const_13,true);
            _loc16_ = _loc13_.getBounds(var_2);
            this.var_1676[_loc2_] = _loc16_.y + (_loc16_.height - var_2.am_PageLeft.height) * 0.5;
            _loc2_++;
         }
         this.var_1581 = method_1(_loc1_);
         this.var_671 = method_27(var_2.am_MaterialLists.am_ItemMaterialDetail);
         this.var_671.Hide(true);
         this.var_438 = _loc1_.getBounds(var_2);
         this.var_438.x -= const_398;
         this.var_438.y -= const_398;
         this.var_438.width += const_398 * 2;
         this.var_438.height += const_398 * 2;
         var _loc3_:MovieClip = var_2.am_RealmGroup;
         var _loc4_:MovieClip = var_2.am_RemovalSocketGroup;
         var _loc5_:MovieClip = var_2.am_PagingGroup;
         this.var_1365 = new Vector.<class_33>(const_13,true);
         this.var_1633 = new Vector.<TextField>(const_13,true);
         this.var_1755 = new Vector.<class_33>(const_13,true);
         this.var_948 = new Vector.<class_33>(const_13,true);
         this.var_1919 = new Vector.<class_33>(const_13,true);
         this.var_290 = new Vector.<Vector.<class_33>>(const_13,true);
         this.var_957 = new Vector.<class_33>(const_13,true);
         _loc2_ = 0;
         while(_loc2_ < const_13)
         {
            _loc17_ = _loc3_["am_Realm" + _loc2_] as MovieClip;
            this.var_1365[_loc2_] = method_17(_loc17_.am_Meter,"Progress",0);
            this.var_1755[_loc2_] = method_1(_loc17_.am_TierAnim);
            this.var_948[_loc2_] = method_1(_loc17_.am_MaxedAnim);
            this.var_1633[_loc2_] = _loc17_.am_Tier;
            _loc18_ = _loc17_.am_MaterialGroup;
            _loc19_ = new Vector.<class_33>(const_128,true);
            _loc15_ = 0;
            while(_loc15_ < const_128)
            {
               _loc19_[_loc15_] = method_3(_loc18_["am_Socket" + _loc15_] as MovieClip,_loc2_ * const_475 + _loc15_,this.method_1822);
               _loc15_++;
            }
            this.var_290[_loc2_] = _loc19_;
            this.var_957[_loc2_] = method_1(_loc18_);
            (_loc20_ = method_1(_loc4_["am_Locator" + _loc2_] as MovieClip)).Hide();
            this.var_1919[_loc2_] = _loc20_;
            _loc2_++;
         }
         this.var_1072 = method_1(_loc3_);
         this.var_1072.Hide();
         var _loc6_:MovieClip;
         var _loc7_:MovieClip = (_loc6_ = var_2.am_RecipeGroup).am_Choices;
         this.var_461 = new Vector.<class_33>(class_64.const_217 + class_64.const_422 + class_64.const_524,true);
         _loc2_ = 0;
         while(_loc2_ < class_64.const_217 + class_64.const_422 + class_64.const_524)
         {
            this.var_461[_loc2_] = method_3(_loc7_["am_Recipe" + _loc2_] as MovieClip,_loc2_,this.method_1775,this.method_1487,this.method_1640);
            _loc2_++;
         }
         this.var_1056 = method_1(_loc6_);
         this.var_2182 = method_92(_loc6_.am_LevelSelectText);
         this.var_1803 = method_5(_loc6_.am_IncreaseLevel,this.method_1985);
         this.var_1664 = method_5(_loc6_.am_Decrease,this.method_1340);
         var _loc8_:MovieClip = var_2.am_CurrentCrafting;
         this.var_1134 = method_1(_loc8_.am_SpeedUpPanel);
         this.var_1628 = method_5(_loc8_.am_Cancel,this.method_1135);
         this.var_1048 = method_1(var_2.am_CancelPanel);
         this.var_1328 = method_1(_loc8_.am_CharmPanel);
         this.var_1324 = method_10(this.var_1134.mMovieClip.am_SpeedUp,this.method_1124);
         this.var_2544 = method_10(this.var_1048.mMovieClip.am_CancelTraining,this.method_1501);
         this.var_2835 = method_10(this.var_1048.mMovieClip.am_NeverMind,this.method_1293);
         this.var_1514 = method_17(this.var_1328.mMovieClip.am_Progress,"Progress",2);
         this.var_2134 = method_5(this.var_1328.mMovieClip.am_IconHolder,null,this.method_1883,this.method_1988);
         this.var_174 = method_5(var_2.am_RecipeCharmIcon,this.method_1989,this.method_1928,this.method_1801);
         this.var_1898 = method_1(var_2.am_RecipeLocator);
         this.var_1898.Hide();
         this.var_1485 = method_1(var_2.am_FireAnimation);
         this.var_1155 = method_1(var_2.am_LeftFlameAnim);
         this.var_1277 = method_1(var_2.am_RightFlameAnim);
         this.var_1123 = method_1(var_2.am_CoalsAnim);
         this.var_1382 = method_1(var_2.am_WallGlow);
         this.var_1409 = method_1(_loc8_);
         this.var_614 = method_1(var_2.am_ForgeToggleButton.am_Pulse);
         this.var_449 = method_1(var_2.am_WarningAnim);
         this.var_261 = method_1(var_2.am_Notice);
         this.var_261.mMovieClip.mouseChildren = false;
         this.var_261.mMovieClip.mouseEnabled = false;
         var _loc9_:MovieClip = var_2.am_StatPanel;
         this.var_2106 = method_17(var_2.am_CraftXPProgress,"Progress",0);
         this.var_1497 = method_10(var_2.am_ForgeToggleButton,this.method_1014);
         this.var_1610 = method_27(_loc9_.am_ForgeStatDetails);
         this.var_1912 = new Vector.<class_33>(const_100,true);
         this.var_1239 = new Vector.<class_33>(const_100,true);
         this.var_1799 = new Vector.<class_33>(const_100,true);
         _loc2_ = 0;
         while(_loc2_ < const_100)
         {
            this.var_1912[_loc2_] = method_17(_loc9_["am_Progress" + _loc2_],"Ready",0);
            this.var_1799[_loc2_] = method_17(_loc9_["am_ProgressPending" + _loc2_],"Ready",0);
            this.var_1239[_loc2_] = method_3(_loc9_["am_Plus" + _loc2_],_loc2_,this.method_1406,this.method_774,this.method_812);
            method_3(_loc9_["am_Contact" + _loc2_],_loc2_,null,this.method_774,this.method_812);
            _loc2_++;
         }
         this.var_894 = method_1(_loc9_);
         this.var_1437 = method_10(_loc9_.am_Apply,this.method_1592);
         this.var_2007 = method_10(_loc9_.am_Reset,this.method_1954);
         this.var_1610.Hide(true);
         this.var_1104 = method_1(var_2.am_LevelUp);
         this.var_1104.Hide();
         var _loc10_:MovieClip = _loc9_.am_AllocationAnimGroup;
         this.var_2292 = new Vector.<class_33>(const_100,true);
         _loc2_ = 0;
         while(_loc2_ < const_100)
         {
            this.var_2292[_loc2_] = method_1(_loc10_["am_AllocateAnim" + _loc2_] as MovieClip);
            _loc2_++;
         }
         this.var_1481 = new Vector.<Boolean>(const_100,true);
         var _loc11_:MovieClip = var_2.am_MeterGroup;
         this.var_2332 = method_17(_loc11_.am_RareChance,"Progress",1.25);
         this.var_2435 = method_17(_loc11_.am_LegendaryChance,"Progress",1.25);
         _loc11_.am_MeterTooltip.visible = false;
         this.var_684 = method_5(_loc11_,null,this.method_1568,this.method_1994);
         var _loc12_:MovieClip = var_2.am_CraftGroup;
         this.var_2387 = method_10(_loc12_.am_Craft,this.Craft);
         this.var_1284 = method_1(_loc12_);
         method_5(var_2.am_ArtisanTooltipContact,null,this.method_1429,this.method_1381);
         this.var_1180 = method_27(var_2.am_ArtisanTooltip);
         this.var_1180.Hide(true);
         this.var_1178 = method_92(var_2.am_CraftXP);
         this.var_1554 = method_1(mWindow.mMovieClip.am_GlobalUpgradePanel);
         this.var_1838 = method_10(this.var_1554.mMovieClip.am_Upgrade,this.method_1391);
         this.var_1972 = method_1(var_2.am_MaterialWanring);
         this.var_60 = method_1(var_2.am_TutorialInteraction);
         this.var_60.Hide();
         this.var_1475 = method_10(var_2.am_CatalystButton,this.method_1697,this.method_1022,this.method_1110);
         this.var_1172 = method_1(var_2.am_CatalystButton.am_ItemIconHolder);
         this.var_448 = method_1(var_2.am_ParticleBurst);
         this.var_448.mMovieClip.mouseChildren = false;
         this.var_448.mMovieClip.mouseEnabled = false;
         this.var_1699 = method_10(var_2.am_TinkersSoulIcon,this.method_1748,this.method_1354,this.method_1006);
         this.var_1658 = method_21(var_2.am_TinkerSoulCount);
         this.var_639 = method_1(var_2.am_XPFloaterAnim);
         this.var_639.mMovieClip.mouseChildren = false;
         this.var_639.mMovieClip.mouseEnabled = false;
         this.var_621 = method_1(var_2.am_ParticleBurstTinker);
         this.var_621.mMovieClip.mouseChildren = false;
         this.var_621.mMovieClip.mouseEnabled = false;
         method_23(var_2.am_Close);
         method_208();
      }
      
      override public function OnDestroyScreen() : void
      {
         var _loc2_:uint = 0;
         this.var_1365 = null;
         this.var_1633 = null;
         this.var_1416 = null;
         this.var_1755 = null;
         this.var_948 = null;
         this.var_862 = null;
         this.var_1919 = null;
         this.var_1284 = null;
         this.var_894 = null;
         this.var_684 = null;
         this.var_1056 = null;
         this.var_1072 = null;
         this.var_1581 = null;
         this.var_1409 = null;
         this.var_2106 = null;
         this.var_1497 = null;
         this.var_461 = null;
         this.var_2182 = null;
         this.var_1803 = null;
         this.var_1664 = null;
         this.var_2332 = null;
         this.var_2435 = null;
         this.var_1010 = null;
         this.var_1342 = null;
         this.var_1676 = null;
         this.var_438 = null;
         this.var_469 = null;
         this.var_1912 = null;
         this.var_1799 = null;
         this.var_1239 = null;
         this.var_1610 = null;
         this.var_1485 = null;
         this.var_1155 = null;
         this.var_1277 = null;
         this.var_1123 = null;
         this.var_1382 = null;
         this.var_671 = null;
         this.var_1180 = null;
         this.var_1437 = null;
         this.var_2007 = null;
         this.var_1328 = null;
         this.var_1324 = null;
         this.var_1134 = null;
         this.var_1628 = null;
         this.var_2544 = null;
         this.var_1048 = null;
         this.var_2835 = null;
         this.var_1514 = null;
         this.var_1554 = null;
         this.var_1838 = null;
         this.var_1178 = null;
         this.var_449 = null;
         this.var_261 = null;
         this.var_614 = null;
         this.var_1972 = null;
         this.var_1481 = null;
         this.var_2134 = null;
         this.var_60 = null;
         this.var_2387 = null;
         this.var_1699 = null;
         this.var_1658 = null;
         this.var_621 = null;
         this.var_639 = null;
         this.var_105 = null;
         this.var_1475 = null;
         this.var_1172 = null;
         this.var_448 = null;
         var _loc1_:uint = 0;
         while(_loc1_ < const_13)
         {
            this.var_957[_loc1_] = null;
            this.var_290[_loc1_] = null;
            _loc1_++;
         }
         this.var_957 = null;
         this.var_290 = null;
         _loc1_ = 0;
         while(_loc1_ < const_13)
         {
            this.var_920[_loc1_] = null;
            _loc1_++;
         }
         this.var_920 = null;
         _loc1_ = 0;
         while(_loc1_ < const_13)
         {
            _loc2_ = 0;
            while(_loc2_ < const_128)
            {
               this.var_158[_loc1_][_loc2_] = null;
               _loc2_++;
            }
            this.var_158[_loc1_] = null;
            _loc1_++;
         }
         this.var_158 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc9_:class_33 = null;
         var _loc10_:TextField = null;
         var _loc11_:uint = 0;
         var _loc12_:uint = 0;
         var _loc1_:uint = uint(var_1.mMagicForgeStatus.status);
         this.var_607 = _loc1_ == class_111.const_286;
         this.var_579 = var_1.mCraftTalentData.craftLevel;
         this.var_1727 = var_1.mCraftTalentData.craftXP;
         this.var_1048.Hide();
         if(this.var_607)
         {
            this.var_1409.Show();
            this.var_1056.Hide();
            this.var_1072.Hide();
            this.var_1284.Hide();
            this.var_684.Hide();
            this.method_409();
            this.var_1485.Show();
            this.var_1155.Show();
            this.var_1277.Show();
            this.var_1123.Show();
            this.var_1155.PlayAnimation("Loop",class_33.const_36);
            this.var_1277.PlayAnimation("Loop",class_33.const_36);
            this.var_1123.PlayAnimation("Ready",class_33.const_36);
            this.var_1382.PlayAnimation("LightUp",class_33.const_36);
            this.var_174.Hide();
            this.method_1763();
         }
         else if(this.var_624)
         {
            this.var_1581.Hide();
            this.var_894.Hide();
            this.var_1409.Hide();
            this.var_1056.Show();
            this.var_1072.Show();
            this.var_1284.Hide();
            this.var_684.Hide();
            this.method_409();
            this.var_1485.Hide();
            this.var_1155.Hide();
            this.var_1277.Hide();
            this.var_1123.Hide();
            this.var_1382.PlayAnimation("Ready");
            this.method_424();
            this.var_449.PlayAnimation("Ready");
            this.var_449.Hide();
         }
         else
         {
            this.var_1409.Hide();
            this.var_1056.Hide();
            this.var_1072.Show();
            this.var_1284.Show();
            this.var_684.Show();
            this.var_1475.Show();
            this.var_1485.Hide();
            this.var_1155.Hide();
            this.var_1277.Hide();
            this.var_1123.Hide();
            this.var_1382.PlayAnimation("Ready");
            this.var_174.Show();
            if(this.var_887)
            {
               this.method_836();
            }
            this.var_449.PlayAnimation("Ready");
            this.var_449.Hide();
         }
         if(this.var_887)
         {
            this.var_1056.Hide();
            this.var_1581.Hide();
            this.var_894.Show();
            this.method_1117();
            this.var_261.Hide();
            this.var_614.Hide();
            MathUtil.method_2(var_2.am_Header,"Artisan Skills");
         }
         else
         {
            this.var_894.Hide();
            this.method_836();
            if(!this.var_624)
            {
               this.var_1581.Show();
               MathUtil.method_2(var_2.am_Header,"Crafting Materials");
               for each(_loc9_ in this.var_948)
               {
                  _loc9_.mMovieClip.filters = [];
               }
            }
            else
            {
               this.var_1056.Show();
               MathUtil.method_2(var_2.am_Header,"Select a Recipe");
               for each(_loc9_ in this.var_948)
               {
                  _loc9_.mMovieClip.filters = [class_50.const_112];
               }
               for each(_loc10_ in this.var_1633)
               {
                  MathUtil.method_2(_loc10_,"");
               }
            }
            if(Boolean(var_1.mCraftTalentData.GetTotalPendingPoints()) && this.var_579 != 1)
            {
               if(!this.var_261.mbVisible)
               {
                  this.var_261.PlayAnimation("Notice");
                  this.var_614.PlayAnimation("Pulse",class_33.const_36);
                  this.var_261.Show();
                  this.var_614.Show();
                  MathUtil.method_2(this.var_261.mMovieClip.am_TextWrapper.am_Text,"You did not press the Apply button");
               }
            }
            else if(Boolean(var_1.mCraftTalentData.GetTalentPointsRemaining()) && this.var_579 != 1)
            {
               if(!this.var_261.mbVisible)
               {
                  this.var_261.PlayAnimation("Notice");
                  this.var_614.PlayAnimation("Pulse",class_33.const_36);
                  this.var_261.Show();
                  this.var_614.Show();
                  MathUtil.method_2(this.var_261.mMovieClip.am_TextWrapper.am_Text,"You have unspent Artisan Points");
               }
            }
            else
            {
               this.var_261.Hide();
               this.var_614.Hide();
            }
         }
         var _loc2_:uint = uint(class_86.const_222[this.var_579 - 1]);
         var _loc3_:uint = class_86.const_222[this.var_579] - _loc2_;
         var _loc4_:uint = uint(this.var_1727 - _loc2_);
         this.var_2106.mHealthPerc = Number(_loc4_) / Number(_loc3_);
         MathUtil.method_2(var_2.am_ArtisanLevel,String(var_1.mCraftTalentData.craftLevel));
         if(this.var_1893 != this.var_579)
         {
            this.var_1104.Show();
            this.var_1104.PlayAnimation("FadeIn",class_33.const_14);
            this.var_1893 = this.var_579;
         }
         this.method_998();
         var _loc5_:class_9 = var_1.mBuildingInfo.GetOwnedBuildingByName("Forge");
         var_1.UpdateBuildingUpgradePanel(this.var_1554.mMovieClip,_loc5_,this.var_1838);
         if(this.var_607)
         {
            if(_loc5_.rank < class_9.const_214)
            {
               MathUtil.method_8(this.var_1554.mMovieClip.am_Message,"Cannot upgrade while crafting a Charm",ScreenArmory.const_137,ScreenArmory.const_169);
            }
            this.var_1838.Hide();
         }
         this.var_1324.EnableButton();
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         while(_loc7_ < this.var_158.length)
         {
            _loc11_ = 0;
            while(_loc11_ < this.var_158[_loc7_].length)
            {
               _loc12_ = 0;
               while(_loc12_ < this.var_158[_loc7_][_loc11_].length)
               {
                  _loc6_++;
                  _loc12_++;
               }
               _loc11_++;
            }
            _loc7_++;
         }
         var _loc8_:uint = uint(var_1.mCraftTalentData.GetMaxMats());
         MathUtil.method_2(var_2.am_MaterialCount,_loc6_ + "/" + _loc8_);
      }
      
      private function method_1014(param1:MouseEvent) : void
      {
         if(!this.var_887)
         {
            this.var_887 = true;
            var_44 = 0;
            method_177();
            MathUtil.method_2(this.var_1497.mMovieClip.am_Text,"View Materials");
         }
         else
         {
            this.var_887 = false;
            MathUtil.method_2(this.var_1497.mMovieClip.am_Text,"Artisan Skills");
         }
         Refresh();
      }
      
      private function method_1406(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:class_86 = var_1.mCraftTalentData;
         var _loc4_:uint;
         if((_loc4_ = _loc3_.method_554() + _loc3_.GetTotalPendingPoints()) >= _loc3_.craftLevel)
         {
            return;
         }
         _loc3_.method_1843(param2);
         this.method_726(param2);
         this.var_1481[param2] = true;
         Refresh();
      }
      
      private function method_1592(param1:MouseEvent) : void
      {
         var _loc4_:class_33 = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         var _loc2_:class_86 = var_1.mCraftTalentData;
         _loc2_.method_1307();
         _loc2_.method_1785();
         var _loc3_:uint = 0;
         while(_loc3_ < const_100)
         {
            if(this.var_1481[_loc3_])
            {
               (_loc4_ = this.var_2292[_loc3_]).Show();
               _loc4_.PlayAnimation("Allocate",class_33.const_14);
            }
            _loc3_++;
         }
         this.method_615();
         Refresh();
      }
      
      private function method_1954(param1:MouseEvent) : void
      {
         var _loc2_:class_86 = var_1.mCraftTalentData;
         _loc2_.method_496();
         this.method_615();
         Refresh();
      }
      
      private function method_615() : void
      {
         var _loc1_:uint = 0;
         while(_loc1_ < const_100)
         {
            this.var_1481[_loc1_] = false;
            _loc1_++;
         }
      }
      
      private function method_1117() : void
      {
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc1_:class_86 = var_1.mCraftTalentData;
         var _loc2_:uint = _loc1_.GetTalentPointsRemaining();
         var _loc3_:uint = 0;
         while(_loc3_ < const_100)
         {
            _loc4_ = _loc1_.GetCraftTalentBonus(_loc3_);
            _loc5_ = _loc1_.method_1297(_loc3_);
            _loc6_ = _loc4_ + _loc5_;
            this.var_1912[_loc3_].mHealthPerc = _loc4_ / class_86.const_33;
            this.var_1799[_loc3_].mHealthPerc = _loc6_ / class_86.const_33;
            if(_loc2_ == 0)
            {
               this.var_1239[_loc3_].DisableButton("Inactive");
            }
            else if(_loc4_ >= class_86.const_33 || _loc6_ >= class_86.const_33)
            {
               this.var_1239[_loc3_].DisableButton("Inactive");
            }
            else
            {
               this.var_1239[_loc3_].EnableButton();
            }
            _loc3_++;
         }
         if(_loc1_.GetTotalPendingPoints() > 0)
         {
            this.var_1437.EnableButton();
            this.var_2007.EnableButton();
         }
         else
         {
            this.var_1437.DisableButton("Inactive");
            this.var_2007.DisableButton("Inactive");
         }
         MathUtil.method_2(this.var_894.mMovieClip.am_ArtisanPoints,String(_loc2_));
      }
      
      private function method_424() : void
      {
         var _loc1_:class_1 = null;
         var _loc2_:class_64 = null;
         var _loc3_:String = null;
         var _loc4_:String = null;
         if(this.var_41 == this.var_921)
         {
            this.var_1803.DisableButton("Inactive");
         }
         else
         {
            this.var_1803.EnableButton();
         }
         if(this.var_41 <= 1)
         {
            this.var_1664.DisableButton("Inactive");
         }
         else
         {
            this.var_1664.EnableButton();
         }
         this.var_2182.SetText("Recipe Level: " + this.var_41);
         var _loc5_:uint = 0;
         while(_loc5_ < class_64.const_217 + class_64.const_422 + class_64.const_524)
         {
            _loc3_ = String(class_64.const_26[_loc5_ + 1]);
            _loc4_ = this.var_41 < 10 ? "0" + this.var_41 : String(this.var_41);
            if(this.method_136(_loc5_ + 1))
            {
               _loc4_ = "";
            }
            _loc1_ = class_14.var_142[_loc3_ + _loc4_];
            _loc2_ = new class_64(_loc1_);
            _loc2_.method_78(this,this.var_461[_loc5_].mMovieClip.am_IconHolder);
            this.var_461[_loc5_].mMovieClip.visible = true;
            _loc5_++;
         }
         if(this.var_116)
         {
            _loc3_ = String(class_64.const_26[this.var_116]);
            _loc4_ = this.var_41 < 10 ? "0" + this.var_41 : String(this.var_41);
            if(this.method_136(this.var_116))
            {
               _loc4_ = "";
            }
            _loc1_ = class_14.var_142[_loc3_ + _loc4_];
            _loc2_ = new class_64(_loc1_);
            _loc2_.method_78(this,var_2.am_RecipeCharmIcon.am_Holder);
            MathUtil.method_2(var_2.am_CharmName,_loc1_.displayName);
            MathUtil.method_2(var_2.am_CharmProperty,_loc1_.var_203);
         }
         else
         {
            method_14(var_2.am_RecipeCharmIcon.am_Holder);
         }
      }
      
      private function method_836() : void
      {
         var _loc1_:MovieClip = null;
         var _loc2_:MovieClip = null;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc9_:uint = 0;
         var _loc10_:Vector.<class_76> = null;
         var _loc11_:uint = 0;
         var _loc12_:uint = 0;
         var _loc13_:uint = 0;
         var _loc14_:Vector.<class_33> = null;
         var _loc15_:uint = 0;
         var _loc16_:uint = 0;
         var _loc17_:* = null;
         var _loc18_:class_76 = null;
         var _loc19_:class_8 = null;
         var _loc20_:uint = 0;
         var _loc21_:Vector.<class_8> = null;
         var _loc22_:uint = 0;
         var _loc23_:uint = 0;
         var _loc24_:uint = 0;
         var _loc25_:uint = 0;
         var _loc26_:String = null;
         var _loc27_:String = null;
         var _loc28_:class_1 = null;
         var _loc29_:class_64 = null;
         var _loc30_:uint = 0;
         if(this.var_1010[this.var_1355] != var_16)
         {
            this.var_1010[this.var_1355] = var_16;
            this.var_862[this.var_1355] = true;
         }
         var _loc6_:Number = 0;
         var _loc7_:Number = 0;
         var _loc8_:uint = 0;
         while(_loc8_ < const_13)
         {
            if(this.var_862[_loc8_])
            {
               _loc9_ = this.var_1010[_loc8_];
               _loc12_ = !!(_loc11_ = (_loc10_ = this.method_1231(const_165[_loc8_])).length) ? uint(Math.ceil(_loc11_ / const_125)) : 1;
               if(_loc9_ >= _loc12_)
               {
                  _loc9_ = _loc12_ - 1;
               }
               this.var_1342[_loc8_] = _loc12_;
               _loc13_ = _loc9_ * const_125;
               _loc14_ = this.var_920[_loc8_];
               _loc15_ = 0;
               while(_loc15_ < const_125)
               {
                  _loc1_ = _loc14_[_loc15_].mMovieClip;
                  _loc2_ = _loc1_.am_ItemIconHolder;
                  if(_loc13_ >= _loc11_)
                  {
                     _loc2_.visible = false;
                     _loc1_.am_Quantity.visible = false;
                     this.var_1092[_loc8_][_loc15_] = 0;
                  }
                  else
                  {
                     _loc19_ = (_loc18_ = _loc10_[_loc13_]).materialType;
                     _loc20_ = uint(this.var_469[_loc19_.var_140]);
                     MathUtil.method_2(_loc1_.am_Quantity,String(_loc20_));
                     method_12(_loc2_,_loc18_.materialType.iconName);
                     _loc2_.visible = true;
                     _loc1_.am_Quantity.visible = true;
                     this.var_1092[_loc8_][_loc15_] = _loc19_.var_140;
                  }
                  _loc15_++;
                  _loc13_++;
               }
               _loc16_ = 0;
               _loc17_ = "";
               _loc5_ = 0;
               _loc15_ = 0;
               while(_loc15_ < const_128)
               {
                  if(!(_loc22_ = (_loc21_ = this.var_158[_loc8_][_loc15_]).length))
                  {
                     method_14(this.var_290[_loc8_][_loc15_].mMovieClip.am_Holder);
                  }
                  else
                  {
                     _loc5_ += this.method_510(_loc21_);
                     method_12(this.var_290[_loc8_][_loc15_].mMovieClip.am_Holder,_loc21_[_loc22_ - 1].iconName);
                     _loc16_ |= 1 << _loc15_;
                  }
                  _loc15_++;
               }
               if(!_loc16_)
               {
                  _loc17_ = "M";
                  this.var_957[_loc8_].Hide();
               }
               else
               {
                  if(1 << 0 & _loc16_)
                  {
                     _loc17_ += "M";
                     this.var_290[_loc8_][0].Show();
                  }
                  else
                  {
                     this.var_290[_loc8_][0].Hide();
                  }
                  if(1 << 1 & _loc16_)
                  {
                     _loc17_ += "R";
                     this.var_290[_loc8_][1].Show();
                  }
                  else
                  {
                     this.var_290[_loc8_][1].Hide();
                  }
                  if(1 << 2 & _loc16_)
                  {
                     _loc17_ += "L";
                     this.var_290[_loc8_][2].Show();
                  }
                  else
                  {
                     this.var_290[_loc8_][2].Hide();
                  }
                  this.var_957[_loc8_].Show();
               }
               this.var_957[_loc8_].PlayAnimation(_loc17_);
               _loc3_ = this.method_514(_loc5_);
               if(_loc3_ != this.var_1416[_loc8_])
               {
                  this.var_1755[_loc8_].PlayAnimation("TierUp");
               }
               MathUtil.method_2(this.var_1633[_loc8_],String(_loc3_ - 1));
               this.var_1416[_loc15_] = _loc3_;
               if(_loc3_ == class_8.const_256)
               {
                  this.var_1365[_loc8_].mHealthPerc = 1;
                  this.var_948[_loc8_].PlayAnimation("Maxed",class_33.const_36);
               }
               else
               {
                  _loc23_ = this.method_824(_loc3_ - 1);
                  _loc25_ = uint((_loc24_ = this.method_824(_loc3_)) - _loc23_);
                  this.var_1365[_loc8_].mHealthPerc = (_loc5_ - _loc23_) / _loc25_;
                  this.var_948[_loc8_].PlayAnimation("Ready");
               }
               this.var_862[_loc8_] = false;
            }
            _loc8_++;
         }
         if(this.var_116)
         {
            _loc26_ = String(class_64.const_26[this.var_116]);
            _loc27_ = this.var_41 < 10 ? "0" + this.var_41 : String(this.var_41);
            if(this.method_136(this.var_116))
            {
               _loc27_ = "";
            }
            _loc28_ = class_14.var_142[_loc26_ + _loc27_];
            (_loc29_ = new class_64(_loc28_)).method_78(this,var_2.am_RecipeCharmIcon.am_Holder);
            MathUtil.method_2(var_2.am_CharmName,_loc28_.displayName);
            MathUtil.method_2(var_2.am_CharmProperty,_loc28_.var_203);
            _loc30_ = uint(var_1.mCraftTalentData.GetTimeAfterBonuses(_loc28_));
            MathUtil.method_2(this.var_1284.mMovieClip.am_Time,Game.method_70(_loc30_,true));
         }
         _loc8_ = 0;
         while(_loc8_ < const_13)
         {
            _loc5_ = 0;
            _loc15_ = 0;
            while(_loc15_ < const_128)
            {
               _loc5_ += this.method_510(this.var_158[_loc8_][_loc15_]);
               _loc15_++;
            }
            _loc4_ = this.method_514(_loc5_);
            _loc6_ += class_8.const_1240[_loc4_ - 1];
            _loc7_ += class_8.const_1286[_loc4_ - 1];
            _loc8_++;
         }
         if(!this.var_105)
         {
            method_14(this.var_1172.mMovieClip);
            if(this.method_1747() && !this.var_607 && !this.var_624)
            {
               this.method_1569();
            }
            else
            {
               this.method_409();
            }
         }
         else
         {
            method_12(this.var_1172.mMovieClip,this.var_105.iconName);
            _loc6_ += this.var_105.var_1831;
            _loc7_ += this.var_105.var_1711;
         }
         this.method_1054(_loc6_,_loc7_);
         if(var_44)
         {
            var_44 = this.var_1342[this.var_1355];
         }
      }
      
      private function method_2052(param1:Number, param2:Number) : Number
      {
         var _loc3_:Number = NaN;
         var _loc4_:Number = 0;
         if(var_1.mCraftTalentData)
         {
            _loc4_ = Number(var_1.mCraftTalentData.GetCraftTalentBonus(class_86.const_146));
         }
         _loc3_ = param1 + _loc4_ * param2;
         var _loc5_:*;
         if(_loc5_ = Number(int(_loc3_)) == _loc3_)
         {
            return _loc3_ < 10 ? 291 : 283;
         }
         return _loc3_ < 10 ? 279 : 270;
      }
      
      private function method_1763() : void
      {
         var _loc1_:MovieClip = this.var_1328.mMovieClip;
         var _loc2_:class_1 = var_1.mMagicForgeStatus.GetCurrentlyCrafting();
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:class_64 = new class_64(_loc2_);
         _loc3_.method_78(this,this.var_2134.mMovieClip);
         MathUtil.method_2(_loc1_.am_Name,_loc3_.method_49());
         if(this.var_1115)
         {
            this.var_1048.Show();
            this.var_1628.Hide();
            this.var_449.Show();
            if(this.var_449.var_175 == 1)
            {
               this.var_449.PlayAnimation("Warning");
            }
         }
         else
         {
            this.var_1048.Hide();
            this.var_1628.Show();
            this.var_449.PlayAnimation("Ready");
            this.var_449.Hide();
         }
      }
      
      private function method_1883(param1:MouseEvent) : void
      {
         var _loc2_:class_1 = var_1.mMagicForgeStatus.GetCurrentlyCrafting();
         var _loc3_:class_64 = new class_64(_loc2_);
         var_1.screenHudTooltip.ShowCharmTooltip(_loc3_,740,575);
      }
      
      private function method_1988(param1:MouseEvent) : void
      {
         var_1.screenHudTooltip.HideTooltip();
      }
      
      public function OnInitDisplay() : void
      {
         var _loc3_:Vector.<class_33> = null;
         this.var_921 = var_1.mBuildingInfo.GetOwnedBuildingByName("Forge").rank;
         if(!this.var_921)
         {
            this.var_921 = 1;
         }
         this.var_41 = this.var_921;
         if(!this.var_1893)
         {
            this.var_1893 = var_1.mCraftTalentData.craftLevel;
         }
         var _loc1_:class_111 = var_1.mMagicForgeStatus;
         if(_loc1_.status == class_111.const_286)
         {
            this.var_116 = method_337(_loc1_.primary);
            this.var_624 = false;
            this.var_607 = true;
         }
         else
         {
            this.var_116 = 0;
            this.var_624 = true;
            this.var_607 = false;
         }
         this.var_887 = false;
         MathUtil.method_2(this.var_1497.mMovieClip.am_Text,"Artisan Skills");
         var _loc2_:uint = 0;
         while(_loc2_ < const_13)
         {
            this.var_1010[_loc2_] = 0;
            _loc2_++;
         }
         var_16 = 0;
         var_44 = 0;
         this.var_671.Hide(true);
         this.var_1180.Hide(true);
         this.var_1178.Hide();
         this.var_639.Hide(true);
         this.var_621.Hide(true);
         this.var_448.Hide(true);
         this.var_261.Hide();
         this.var_614.Hide();
         this.method_813();
         if(!var_1.screenInteractiveTutorial.CheckCompletedTutorials(class_89.const_138))
         {
            this.var_60.Show();
            _loc3_ = new Vector.<class_33>();
            _loc3_.push(this.var_461[4]);
            _loc3_.push(this.var_920[4][0]);
            _loc3_.push(this.var_2387);
            _loc3_.push(this.var_1324);
            var_1.screenInteractiveTutorial.SetTutorial(class_89.const_138,this,this.var_60,_loc3_);
         }
      }
      
      override public function OnTickScreen() : void
      {
         var _loc1_:class_1 = null;
         var _loc2_:uint = 0;
         var _loc3_:Number = NaN;
         if(Boolean(var_44) && !this.var_438.contains(var_2.mouseX,var_2.mouseY))
         {
            var_44 = 0;
            method_177();
         }
         if(this.var_607)
         {
            _loc1_ = class_14.var_767[var_1.mMagicForgeStatus.primary];
            _loc2_ = var_1.mMagicForgeStatus.endtime - var_1.mServerGameTime;
            _loc3_ = 1 - _loc2_ / var_1.mCraftTalentData.GetTimeAfterBonuses(_loc1_);
            MathUtil.method_2(this.var_1514.mMovieClip.am_Time,Game.method_70(_loc2_));
            this.var_1514.mHealthPerc = _loc3_;
            if(!this.var_1115)
            {
               MathUtil.method_2(this.var_1134.mMovieClip.am_Idols,Game.method_229(_loc2_));
            }
         }
      }
      
      private function method_1054(param1:Number, param2:Number) : void
      {
         var _loc3_:Number = 0;
         if(var_1.mCraftTalentData)
         {
            _loc3_ = Number(var_1.mCraftTalentData.GetCraftTalentBonus(class_86.const_146));
         }
         var _loc4_:Number = param1 + _loc3_ * class_8.const_968;
         var _loc5_:Number = param2 + _loc3_ * class_8.const_1072;
         var _loc6_:Number = const_1087;
         var _loc7_:Number = const_860;
         var _loc8_:Boolean = false;
         var _loc9_:Boolean = false;
         if(this.var_105)
         {
            if(this.var_105.var_1831)
            {
               _loc8_ = true;
               if((_loc6_ += this.var_105.var_1831) > const_124)
               {
                  _loc6_ = const_124;
               }
               if(_loc4_ > const_124)
               {
                  _loc4_ = const_124;
               }
            }
            if(this.var_105.var_1711)
            {
               _loc9_ = true;
               if((_loc7_ += this.var_105.var_1711) > const_124)
               {
                  _loc7_ = const_124;
               }
               if(_loc5_ > const_124)
               {
                  _loc5_ = const_124;
               }
            }
         }
         MathUtil.method_8(this.var_684.mMovieClip.am_RarePercent,this.method_567(_loc4_,2) + "%",_loc8_ ? 52275 : ScreenArmory.const_24);
         MathUtil.method_8(this.var_684.mMovieClip.am_LegendaryPercent,this.method_567(_loc5_,2) + "%",_loc9_ ? 52275 : ScreenArmory.const_24);
         this.var_2332.mHealthPerc = _loc4_ / _loc6_;
         this.var_2435.mHealthPerc = _loc5_ / _loc7_;
      }
      
      private function method_567(param1:Number, param2:Number) : Number
      {
         var _loc3_:Number = NaN;
         if(param2 >= 0)
         {
            _loc3_ = Math.pow(10,param2);
            return Math.round(param1 * _loc3_) / _loc3_;
         }
         return param1;
      }
      
      public function SetCatalyst(param1:class_3) : void
      {
         if(!param1)
         {
            return;
         }
         this.var_105 = param1;
         if(!this.var_448.mbVisible)
         {
            this.var_448.Show();
         }
         this.var_448.ClearAnimation();
         this.var_448.PlayAnimation("Burst",class_33.const_14);
         Refresh();
      }
      
      public function ClearCatalyst() : void
      {
         this.var_105 = null;
         Refresh();
      }
      
      private function method_1697(param1:MouseEvent) : void
      {
         var_1.screenCatalysts.Display();
      }
      
      private function method_1022(param1:MouseEvent) : void
      {
         if(!this.var_105)
         {
            var_1.screenHudTooltip.ShowSimpleTooltip("Add Catalyst",583.05,412.95);
         }
         else
         {
            var_1.screenHudTooltip.ShowBasicDescriptionTooltip(this.var_105.displayName,"Catalyst",this.var_105.var_8,this.var_105.description,583.05,412.95);
         }
      }
      
      private function method_1110(param1:MouseEvent) : void
      {
         var_1.screenHudTooltip.HideTooltip(true);
      }
      
      private function method_813() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:class_76 = null;
         var _loc3_:Vector.<Vector.<class_8>> = null;
         var _loc4_:uint = 0;
         this.var_469 = new Array();
         if(!var_1.screenInteractiveTutorial.CheckCompletedTutorials(class_89.const_138))
         {
            this.var_469[const_485] = 1;
         }
         else
         {
            for each(_loc2_ in var_1.mOwnedMaterials)
            {
               this.var_469[_loc2_.materialType.var_140] = _loc2_.var_181;
            }
         }
         this.var_1416 = new Vector.<uint>(const_13,true);
         this.var_862 = new Vector.<Boolean>(const_13,true);
         _loc1_ = 0;
         while(_loc1_ < const_13)
         {
            this.var_1416[_loc1_] = 1;
            this.var_862[_loc1_] = true;
            _loc1_++;
         }
         this.var_158 = new Vector.<Vector.<Vector.<class_8>>>(const_13,true);
         _loc1_ = 0;
         while(_loc1_ < const_13)
         {
            _loc3_ = new Vector.<Vector.<class_8>>(const_128,true);
            _loc4_ = 0;
            while(_loc4_ < const_128)
            {
               _loc3_[_loc4_] = new Vector.<class_8>();
               _loc4_++;
            }
            this.var_158[_loc1_] = _loc3_;
            _loc1_++;
         }
         this.var_448.Hide();
         this.var_105 = null;
      }
      
      private function method_510(param1:Vector.<class_8>) : uint
      {
         var _loc3_:class_8 = null;
         var _loc2_:uint = 0;
         for each(_loc3_ in param1)
         {
            _loc2_ += class_8.method_220(_loc3_.var_139);
         }
         return _loc2_;
      }
      
      private function method_824(param1:uint) : uint
      {
         if(param1 == class_8.const_256)
         {
            return this.method_543(class_8.const_256 - 1);
         }
         return this.method_543(param1);
      }
      
      private function method_543(param1:uint) : uint
      {
         var _loc2_:Number = Number(var_1.mCraftTalentData.GetCraftTalentBonus(class_86.const_210));
         return Math.ceil(class_8.const_1040[param1] * (1 - _loc2_ * class_8.const_1024));
      }
      
      private function method_1568(param1:MouseEvent) : void
      {
         this.var_684.mMovieClip.am_MeterTooltip.visible = true;
      }
      
      private function method_1994(param1:MouseEvent) : void
      {
         this.var_684.mMovieClip.am_MeterTooltip.visible = false;
      }
      
      private function method_726(param1:uint) : void
      {
         var _loc2_:uint = uint(var_1.mCraftTalentData.GetCraftTalentBonus(param1));
         var _loc3_:MovieClip = this.var_894.mMovieClip.am_ForgeStatDetails;
         MathUtil.method_2(_loc3_.am_Name,class_86.const_184[param1]);
         MathUtil.method_2(_loc3_.am_Desc,class_86.const_204[param1]);
         MathUtil.method_2(_loc3_.am_Bonus,"Current Level: " + class_86.const_144[param1][_loc2_]);
         if(_loc2_ == class_86.const_33)
         {
            MathUtil.method_2(_loc3_.am_BonusNext,"");
         }
         else
         {
            MathUtil.method_2(_loc3_.am_BonusNext,"Next Level: " + class_86.const_144[param1][_loc2_ + 1]);
         }
      }
      
      private function method_774(param1:MouseEvent, param2:uint) : void
      {
         this.method_726(param2);
         this.var_1610.Show();
      }
      
      private function method_812(param1:MouseEvent, param2:uint) : void
      {
         this.var_1610.Hide();
      }
      
      private function method_1775(param1:MouseEvent, param2:uint) : void
      {
         var _loc5_:String = null;
         var _loc6_:class_1 = null;
         var _loc7_:class_64 = null;
         var _loc3_:uint = uint(param2 + 1);
         var _loc4_:String;
         if(!(_loc4_ = String(class_64.const_26[_loc3_])))
         {
            return;
         }
         if(param1.ctrlKey && !var_1.screenInteractiveTutorial.mCurrentTutorialIdx)
         {
            _loc5_ = this.var_41 < 10 ? _loc4_ + "0" + this.var_41 : _loc4_ + this.var_41;
            if(_loc3_ == const_221)
            {
               _loc5_ = class_64.const_366;
            }
            if(_loc3_ == const_173)
            {
               _loc5_ = class_64.const_323;
            }
            _loc6_ = class_14.var_142[_loc5_];
            _loc7_ = new class_64(_loc6_);
            var_1.screenArmory.LinkCharmInChat(0,_loc7_);
            return;
         }
         this.method_1575(param2);
         this.var_116 = _loc3_;
         this.var_624 = false;
      }
      
      private function method_1487(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:uint = uint(param2 + 1);
         var _loc4_:String;
         if(!(_loc4_ = String(class_64.const_26[_loc3_])))
         {
            return;
         }
         this.var_461[param2].mMovieClip.filters = [const_620];
         var _loc5_:String = String(class_64.const_26[_loc3_]);
         var _loc6_:String = this.var_41 < 10 ? "0" + this.var_41 : String(this.var_41);
         if(this.method_136(_loc3_))
         {
            _loc6_ = "";
         }
         var _loc7_:class_1 = class_14.var_142[_loc5_ + _loc6_];
         var _loc8_:class_64 = new class_64(_loc7_);
         var_1.screenHudTooltip.ShowCharmTooltip(_loc8_,740,575);
      }
      
      private function method_1640(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:uint = uint(param2 + 1);
         var _loc4_:String;
         if(!(_loc4_ = String(class_64.const_26[_loc3_])))
         {
            return;
         }
         this.var_461[param2].mMovieClip.filters = [];
         var_1.screenHudTooltip.HideTooltip();
      }
      
      private function method_1928(param1:MouseEvent) : void
      {
         this.var_174.mMovieClip.filters = [const_620];
         var _loc2_:uint = this.var_116;
         var _loc3_:String = String(class_64.const_26[_loc2_]);
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:String = String(class_64.const_26[this.var_116]);
         var _loc5_:String = this.var_41 < 10 ? "0" + this.var_41 : String(this.var_41);
         if(this.method_136(this.var_116))
         {
            _loc5_ = "";
         }
         var _loc6_:class_1 = class_14.var_142[_loc4_ + _loc5_];
         var _loc7_:class_64 = new class_64(_loc6_);
         var_1.screenHudTooltip.ShowCharmTooltip(_loc7_,740,575);
      }
      
      private function method_1801(param1:MouseEvent) : void
      {
         this.var_174.mMovieClip.filters = [];
         var_1.screenHudTooltip.HideTooltip();
      }
      
      private function method_1989(param1:MouseEvent) : void
      {
         var _loc2_:String = null;
         var _loc3_:String = null;
         var _loc4_:class_1 = null;
         var _loc5_:class_64 = null;
         if(param1.ctrlKey)
         {
            if(!this.var_116)
            {
               return;
            }
            _loc2_ = String(class_64.const_26[this.var_116]);
            _loc3_ = this.var_41 < 10 ? _loc2_ + "0" + this.var_41 : _loc2_ + this.var_41;
            if(this.var_116 == const_221)
            {
               _loc3_ = class_64.const_366;
            }
            if(this.var_116 == const_173)
            {
               _loc3_ = class_64.const_323;
            }
            _loc4_ = class_14.var_142[_loc3_];
            _loc5_ = new class_64(_loc4_);
            var_1.screenArmory.LinkCharmInChat(0,_loc5_);
            return;
         }
         this.method_1851();
         this.var_116 = 0;
         this.var_624 = true;
         this.var_887 = false;
         method_14(var_2.am_RecipeCharmIcon.am_Holder);
      }
      
      public function method_514(param1:uint) : uint
      {
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         while(_loc3_ < class_8.const_256)
         {
            if(param1 < this.method_543(_loc3_))
            {
               break;
            }
            if(_loc2_ < class_8.const_256)
            {
               _loc2_++;
            }
            _loc3_++;
         }
         return _loc2_;
      }
      
      private function method_1493(param1:class_8, param2:MovieClip) : void
      {
         var _loc3_:Rectangle = param2.am_Locator.getBounds(mWindow.mMovieClip);
         var _loc4_:uint = uint(const_145[param1.var_103]);
         var _loc5_:uint = uint(const_198[param1.var_139]);
         var _loc6_:MovieClip = this.var_290[_loc4_][_loc5_].mMovieClip;
         method_68(param1.iconName,_loc3_.x,_loc3_.y,_loc6_,250,class_137.method_113,this.method_300,true);
      }
      
      private function method_1433(param1:class_8, param2:uint) : void
      {
         var _loc3_:uint = uint(const_198[param1.var_139]);
         var _loc4_:class_33;
         var _loc5_:Rectangle = (_loc4_ = this.var_290[param2][_loc3_]).mMovieClip.am_Holder.getBounds(mWindow.mMovieClip);
         var _loc6_:MovieClip = this.var_1919[param2].mMovieClip;
         method_68(param1.iconName,_loc5_.x,_loc5_.y,_loc6_,200,class_137.method_113,this.method_300,true);
      }
      
      private function method_1575(param1:uint) : void
      {
         var _loc2_:uint = uint(param1 + 1);
         var _loc3_:String = String(class_64.const_26[_loc2_]);
         var _loc4_:String = this.var_41 < 10 ? _loc3_ + "0" + this.var_41 : _loc3_ + this.var_41;
         if(_loc2_ == const_221)
         {
            _loc4_ = class_64.const_366;
         }
         if(_loc2_ == const_173)
         {
            _loc4_ = class_64.const_323;
         }
         var _loc5_:class_1 = class_14.var_142[_loc4_];
         var _loc6_:Rectangle = this.var_461[param1].mMovieClip.am_IconHolder.getBounds(mWindow.mMovieClip);
         var _loc7_:MovieClip = this.var_1898.mMovieClip;
         var _loc8_:class_137;
         var _loc9_:MovieClip = (_loc8_ = method_68(_loc5_.iconName,_loc6_.x,_loc6_.y,_loc7_,250,class_137.method_113,this.method_300,true)).method_922() as MovieClip;
         if(!this.method_136(_loc2_))
         {
            _loc9_.am_SecondaryCharm.gotoAndStop(1);
            _loc9_.am_SecondaryCharm.visible = false;
         }
         this.var_461[param1].mMovieClip.visible = false;
      }
      
      private function method_1851() : void
      {
         var _loc1_:uint = this.var_116;
         var _loc2_:String = String(class_64.const_26[_loc1_]);
         var _loc3_:String = this.var_41 < 10 ? _loc2_ + "0" + this.var_41 : _loc2_ + this.var_41;
         if(_loc1_ == const_221)
         {
            _loc3_ = class_64.const_366;
         }
         if(_loc1_ == const_173)
         {
            _loc3_ = class_64.const_323;
         }
         var _loc4_:class_1 = class_14.var_142[_loc3_];
         var _loc5_:MovieClip = this.var_461[_loc1_ - 1].mMovieClip.am_IconHolder;
         var _loc6_:Rectangle = this.var_1898.mMovieClip.getBounds(mWindow.mMovieClip);
         var _loc7_:class_137;
         var _loc8_:MovieClip = (_loc7_ = method_68(_loc4_.iconName,_loc6_.x,_loc6_.y,_loc5_,250,class_137.method_113,this.method_300,true)).method_922() as MovieClip;
         if(!this.method_136(_loc1_))
         {
            _loc8_.am_SecondaryCharm.gotoAndStop(1);
            _loc8_.am_SecondaryCharm.visible = false;
         }
      }
      
      private function method_300() : void
      {
         Refresh();
      }
      
      private function method_1822(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:int = param2 % const_475;
         var _loc4_:uint = uint(param2 / const_475);
         var _loc5_:Vector.<class_8>;
         if(!(_loc5_ = this.var_158[_loc4_][_loc3_]).length)
         {
            return;
         }
         var _loc6_:class_8 = _loc5_.pop();
         this.var_469[_loc6_.var_140] = uint(this.var_469[_loc6_.var_140]) + 1;
         this.var_862[_loc4_] = true;
         this.method_1433(_loc6_,_loc4_);
      }
      
      private function method_1605(param1:MouseEvent, param2:uint) : void
      {
         var _loc15_:uint = 0;
         var _loc16_:uint = 0;
         var _loc17_:Vector.<class_8> = null;
         if(this.var_624 || this.var_607 || this.method_136(this.var_116) && !param1.ctrlKey)
         {
            return;
         }
         var _loc3_:uint = param2 % 6;
         var _loc4_:uint = uint(param2 / const_125);
         var _loc5_:uint;
         if(!(_loc5_ = this.var_1092[_loc4_][_loc3_]))
         {
            return;
         }
         var _loc6_:class_76 = var_1.mOwnedMaterials[_loc5_];
         if(!var_1.screenInteractiveTutorial.CheckCompletedTutorials(class_89.const_138))
         {
            _loc6_ = var_1470[_loc5_];
         }
         if(!_loc6_)
         {
            return;
         }
         var _loc7_:class_8 = _loc6_.materialType;
         if(param1.ctrlKey)
         {
            var_1.screenArmory.LinkMaterialInChat(0,_loc7_);
            return;
         }
         var _loc8_:int;
         if(!(_loc8_ = int(this.var_469[_loc7_.var_140])))
         {
            return;
         }
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         while(_loc10_ < this.var_158.length)
         {
            _loc15_ = 0;
            while(_loc15_ < this.var_158[_loc10_].length)
            {
               _loc16_ = 0;
               while(_loc16_ < this.var_158[_loc10_][_loc15_].length)
               {
                  _loc9_++;
                  _loc16_++;
               }
               _loc15_++;
            }
            _loc10_++;
         }
         var _loc11_:uint = uint(var_1.mCraftTalentData.GetMaxMats());
         if(_loc9_ + 1 > _loc11_)
         {
            this.var_1972.Show();
            this.var_1972.PlayAnimation("Warning",class_33.const_14);
            return;
         }
         var _loc12_:uint = 0;
         var _loc13_:uint = 0;
         while(_loc13_ < const_128)
         {
            if((_loc17_ = this.var_158[_loc4_][_loc13_]).length)
            {
               _loc12_ += this.method_510(_loc17_);
            }
            _loc13_++;
         }
         var _loc14_:uint;
         if((_loc14_ = this.method_514(_loc12_)) == 7)
         {
            return;
         }
         this.var_158[_loc4_][const_198[_loc7_.var_139]].push(_loc7_);
         this.var_469[_loc7_.var_140] = _loc8_ - 1;
         this.var_862[_loc4_] = true;
         this.method_1493(_loc7_,this.var_920[_loc4_][_loc3_].mMovieClip);
      }
      
      private function method_1331(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:uint = uint(param2 / const_125);
         var_16 = this.var_1010[_loc3_];
         var_44 = this.var_1342[_loc3_];
         this.var_1355 = _loc3_;
         method_177();
         var _loc4_:Number = this.var_1676[_loc3_];
         var_731.mMovieClip.y = _loc4_;
         var_810.mMovieClip.y = _loc4_;
         var _loc5_:uint = param2 % 6;
         var _loc6_:uint;
         if(!(_loc6_ = this.var_1092[_loc3_][_loc5_]))
         {
            return;
         }
         var _loc7_:class_76;
         if(!(_loc7_ = var_1.mOwnedMaterials[_loc6_]))
         {
            return;
         }
         var _loc8_:class_8 = _loc7_.materialType;
         var _loc9_:int;
         if(!(_loc9_ = int(this.var_469[_loc8_.var_140])))
         {
            return;
         }
         if(_loc8_.var_139 == "M")
         {
            MathUtil.method_8(this.var_671.mMovieClip.am_Name,_loc8_.displayName,ScreenArmory.const_24);
         }
         else if(_loc8_.var_139 == "R")
         {
            MathUtil.method_8(this.var_671.mMovieClip.am_Name,_loc8_.displayName,ScreenArmory.const_22);
         }
         else if(_loc8_.var_139 == "L")
         {
            MathUtil.method_8(this.var_671.mMovieClip.am_Name,_loc8_.displayName,ScreenArmory.const_23);
         }
         this.var_671.Show();
      }
      
      private function method_1564(param1:MouseEvent, param2:uint) : void
      {
         this.var_671.Hide();
      }
      
      private function method_1231(param1:String) : Vector.<class_76>
      {
         var _loc4_:class_76 = null;
         var _loc5_:class_8 = null;
         var _loc2_:Array = var_1.mOwnedMaterials;
         if(!var_1.screenInteractiveTutorial.CheckCompletedTutorials(class_89.const_138))
         {
            _loc2_ = var_1470;
         }
         var _loc3_:Vector.<class_76> = new Vector.<class_76>();
         for each(_loc4_ in _loc2_)
         {
            _loc5_ = _loc4_.materialType;
            if(Boolean(this.var_469[_loc5_.var_140]) && _loc5_.var_103 == param1)
            {
               _loc3_.push(_loc4_);
            }
         }
         _loc3_.sort(method_1028);
         _loc3_.fixed = true;
         return _loc3_;
      }
      
      private function method_1429(param1:MouseEvent) : void
      {
         var _loc2_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         this.var_1180.Show();
         this.var_1178.Show();
         if(this.var_579 >= class_86.const_369)
         {
            _loc4_ = uint(class_86.const_222[class_86.const_369 - 1]);
            _loc2_ = this.var_1727;
         }
         else
         {
            _loc5_ = uint(class_86.const_222[this.var_579 - 1]);
            _loc4_ = class_86.const_222[this.var_579] - _loc5_;
            _loc2_ = uint(this.var_1727 - _loc5_);
         }
         this.var_1178.SetText(MathUtil.method_29(_loc2_) + " / " + MathUtil.method_29(_loc4_));
         var_1.screenHudTooltip.HideTooltip(true);
      }
      
      private function method_1381(param1:MouseEvent) : void
      {
         this.var_1180.Hide(true);
         this.var_1178.Hide();
      }
      
      private function Craft(param1:MouseEvent) : void
      {
         var _loc11_:uint = 0;
         var _loc12_:uint = 0;
         var _loc13_:class_8 = null;
         var _loc14_:uint = 0;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(!this.var_116)
         {
            return;
         }
         var _loc2_:String = String(class_64.const_26[this.var_116]);
         var _loc3_:String = this.var_41 < 10 ? "0" + this.var_41 : String(this.var_41);
         if(this.method_136(this.var_116))
         {
            _loc3_ = "";
         }
         var _loc4_:class_1;
         if(!(_loc4_ = class_14.var_142[_loc2_ + _loc3_]))
         {
            return;
         }
         if(_loc4_.var_2736)
         {
            return;
         }
         var _loc5_:uint = _loc4_.var_68;
         var _loc6_:uint = uint(var_1.mCraftTalentData.GetTimeAfterBonuses(_loc4_));
         this.var_1115 = false;
         var _loc7_:Array = new Array();
         var _loc8_:uint = 0;
         while(_loc8_ < this.var_158.length)
         {
            _loc11_ = 0;
            while(_loc11_ < this.var_158[_loc8_].length)
            {
               _loc12_ = 0;
               while(_loc12_ < this.var_158[_loc8_][_loc11_].length)
               {
                  _loc14_ = (_loc13_ = this.var_158[_loc8_][_loc11_][_loc12_]).var_140;
                  _loc7_[_loc14_] = (!!_loc7_[_loc14_] ? _loc7_[_loc14_] : 0) + 1;
                  _loc12_++;
               }
               _loc11_++;
            }
            _loc8_++;
         }
         var _loc9_:uint = _loc6_ + var_1.mServerGameTime;
         var_1.mMagicForgeStatus.status = class_111.const_286;
         var_1.mMagicForgeStatus.primary = _loc5_;
         var_1.mMagicForgeStatus.endtime = _loc9_;
         this.var_1514.BeginHealthMode("Progress",2);
         var_1.screenForge.Refresh();
         var _loc10_:Packet;
         (_loc10_ = new Packet(LinkUpdater.const_937)).method_20(class_1.const_254,_loc5_);
         _loc8_ = 0;
         while(_loc8_ < _loc7_.length)
         {
            if(_loc7_[_loc8_])
            {
               var_1.clientEnt.SpendMaterial(_loc8_,_loc7_[_loc8_]);
               _loc10_.method_15(true);
               _loc10_.method_20(class_8.const_658,_loc8_);
               _loc10_.method_20(class_8.const_731,_loc7_[_loc8_]);
            }
            _loc8_++;
         }
         _loc10_.method_15(false);
         _loc10_.method_15(!!this.var_105 ? this.var_105.consumableID == class_3.var_1415 : false);
         _loc10_.method_15(!!this.var_105 ? this.var_105.consumableID == class_3.var_2082 : false);
         _loc10_.method_15(!!this.var_105 ? this.var_105.consumableID == class_3.var_1374 : false);
         _loc10_.method_15(!!this.var_105 ? this.var_105.consumableID == class_3.var_1462 : false);
         var_1.serverConn.SendPacket(_loc10_);
      }
      
      private function method_1135(param1:MouseEvent) : void
      {
         this.var_1115 = true;
         Refresh();
      }
      
      private function method_1124(param1:MouseEvent) : void
      {
         if(!var_1.CanSendPacket())
         {
            return;
         }
         var _loc2_:int = var_1.mMagicForgeStatus.endtime - var_1.mServerGameTime;
         var _loc3_:uint = Game.method_257(_loc2_);
         if(var_1.mMammothIdols < _loc3_)
         {
            var_1.screenBuyIdols.Display(_loc3_ - var_1.mMammothIdols);
            return;
         }
         this.var_1324.DisableButton("Inactive");
         var _loc4_:Packet;
         (_loc4_ = new Packet(LinkUpdater.const_889)).method_9(_loc3_);
         var_1.serverConn.SendPacket(_loc4_);
      }
      
      private function method_1501(param1:MouseEvent) : void
      {
         if(!var_1.CanSendPacket())
         {
            return;
         }
         this.var_1115 = false;
         this.var_607 = false;
         var_1.mMagicForgeStatus.FreeForge();
         this.var_116 = 0;
         this.var_624 = true;
         method_14(var_2.am_RecipeCharmIcon.am_Holder);
         this.method_813();
         var _loc2_:Packet = new Packet(LinkUpdater.const_1192);
         var_1.serverConn.SendPacket(_loc2_);
         Refresh();
      }
      
      private function method_1293(param1:MouseEvent) : void
      {
         this.var_1115 = false;
         Refresh();
      }
      
      private function method_1391(param1:MouseEvent) : void
      {
         var _loc6_:class_9 = null;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:class_105 = var_1.mBuildingInfo;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:class_9;
         if(!(_loc4_ = _loc3_.GetOwnedBuildingByName("Forge")))
         {
            return;
         }
         var _loc5_:class_9;
         if(!(_loc5_ = class_9.method_132(_loc4_)))
         {
            return;
         }
         if(_loc2_.currGold < _loc5_.var_129)
         {
            var_1.screenGoldShort.Display(_loc5_.var_129,_loc5_.var_365,class_93.const_178,_loc4_);
         }
         else if(_loc6_ = _loc3_.UpgradeBuilding(_loc4_))
         {
            Hide();
            var_1.screenUpgrading.Display(_loc6_);
         }
      }
      
      public function method_1747() : Boolean
      {
         if(this.method_1767(this.var_116))
         {
            return false;
         }
         if(Boolean(var_1.mOwnedConsumables[class_3.var_1415]) && Boolean(var_1.mOwnedConsumables[class_3.var_1415].stackCount) || Boolean(var_1.mOwnedConsumables[class_3.var_1374]) && Boolean(var_1.mOwnedConsumables[class_3.var_1374].stackCount) || Boolean(var_1.mOwnedConsumables[class_3.var_1462]) && Boolean(var_1.mOwnedConsumables[class_3.var_1462].stackCount))
         {
            return true;
         }
         return false;
      }
      
      public function method_1569() : void
      {
         this.var_1475.Show();
         this.var_1172.Show();
      }
      
      public function method_409() : void
      {
         this.var_1475.Hide();
         this.var_1172.Hide();
         this.var_448.Hide();
      }
      
      public function method_136(param1:uint) : Boolean
      {
         return param1 == const_221 || param1 == const_173;
      }
      
      public function method_1767(param1:uint) : Boolean
      {
         return param1 == const_221 || param1 == const_173;
      }
      
      public function method_1985(param1:Event) : void
      {
         ++this.var_41;
         if(this.var_41 > this.var_921)
         {
            this.var_41 = this.var_921;
         }
         this.method_424();
      }
      
      public function method_1340(param1:Event) : void
      {
         --this.var_41;
         if(this.var_41 <= 0)
         {
            this.var_41 = 1;
         }
         this.method_424();
      }
      
      private function method_1748(param1:MouseEvent) : void
      {
         if(!var_1.mOwnedConsumables[class_3.var_715] || !var_1.mOwnedConsumables[class_3.var_715].stackCount)
         {
            return;
         }
         if(!this.var_621.mbVisible)
         {
            this.var_621.Show();
         }
         this.var_621.ClearAnimation();
         this.var_621.PlayAnimation("Burst",class_33.const_14);
         if(!this.var_639.mbVisible)
         {
            this.var_639.Show();
         }
         this.var_639.ClearAnimation();
         this.var_639.PlayAnimation("Float",class_33.const_14);
         var _loc2_:class_3 = class_14.var_419[class_3.var_715];
         var _loc3_:uint = _loc2_.var_2720;
         var_1.mCraftTalentData.SetXP(var_1.mCraftTalentData.craftXP + _loc3_);
         var _loc4_:Packet;
         (_loc4_ = new Packet(LinkUpdater.const_789)).method_20(class_3.const_69,class_3.var_715);
         var_1.serverConn.SendPacket(_loc4_);
         Refresh();
      }
      
      private function method_1354(param1:MouseEvent) : void
      {
         var _loc2_:class_3 = class_14.var_303["ForgeXP"];
         if(!_loc2_)
         {
            return;
         }
         var_1.screenHudTooltip.ShowConsumableTooltip(_loc2_,688,600);
      }
      
      private function method_1006(param1:MouseEvent) : void
      {
         var_1.screenHudTooltip.HideTooltip(true);
      }
      
      private function method_998() : void
      {
         var _loc1_:uint = !!var_1.mOwnedConsumables[class_3.var_715] ? uint(var_1.mOwnedConsumables[class_3.var_715].stackCount) : 0;
         if(!_loc1_)
         {
            this.var_1699.Hide();
            this.var_1658.SetText("");
         }
         else
         {
            this.var_1699.Show();
            this.var_1658.SetText(String(_loc1_));
         }
      }
   }
}
