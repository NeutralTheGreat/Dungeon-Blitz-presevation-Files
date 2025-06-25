package
{
   public class EntType
   {
      
      public static const ARMOR_SLOT:uint = 1;
      
      public static const GLOVES_SLOT:uint = 2;
      
      public static const BOOTS_SLOT:uint = 3;
      
      public static const HAT_SLOT:uint = 4;
      
      public static const SWORD_SLOT:uint = 5;
      
      public static const SHIELD_SLOT:uint = 6;
      
      public static const MAX_SLOTS:uint = 7;
      
      public static const const_238:uint = 9;
      
      public static const const_1366:uint = 4;
      
      public static const const_283:uint = 7;
      
      public static const const_330:uint = 8;
      
      public static const const_697:uint = 0;
      
      public static const const_362:uint = 1;
      
      public static const const_102:uint = 2;
      
      public static const const_109:uint = 3;
      
      public static const const_123:uint = 4;
      
      public static const const_92:uint = 5;
      
      public static const const_257:uint = 6;
      
      public static const const_157:Vector.<String> = new Vector.<String>(const_257,true);
      
      public static const const_247:Vector.<Number> = new Vector.<Number>(const_257,true);
      
      public static const const_267:Vector.<Number> = new Vector.<Number>(const_257,true);
      
      public static const const_227:Vector.<Number> = new Vector.<Number>(const_257,true);
      
      public static const const_132:Vector.<Array> = new Vector.<Array>(const_257,true);
      
      public static const const_754:Array = [0,320,352,368,386,405,424,445,466,489,512,537,562,590,618,648,679,711,746,782,819,859,900,943,989,1036,1086,1138,1193,1251,1311,1374,1440,1509,1582,1658,1738,1821,1909,2001,2097,2198,2304,2415,2531,2653,2780,2914,3054,3201,3355];
      
      public static const COLOR_SKIN:String = "0xC7A36D";
      
      public static const COLOR_SKIN_DARK:String = "0xA9854F";
      
      public static const SKIN_DARKER_DELTA:uint = 12;
      
      public static const COLOR_HAIR:String = "0x53879C";
      
      public static const COLOR_HAIR_DARK:String = "0x003366";
      
      public static const HAIR_DARKER_DELTA:uint = 13;
      
      public static const COLOR_SHIRT:String = "0x506060";
      
      public static const COLOR_SHIRT_DARK:String = "0x304040";
      
      public static const SHIRT_DARKER_DELTA:uint = 13;
      
      public static const COLOR_PANTS:String = "0x616263";
      
      public static const COLOR_PANTS_DARK:String = "0x414243";
      
      public static const PANTS_DARKER_DELTA:uint = 12;
      
      public static const CHAR_COLOR_BITSTOSEND:uint = 24;
      
      public static const PALADIN_OPTIONS_FILE:String = "Animation_Paladin.swf";
      
      public static const MAGE_OPTIONS_FILE:String = "Animation_Mage.swf";
      
      public static const ROGUE_OPTIONS_FILE:String = "Animation_Rogue.swf";
      
      public static var dynamicEntTypes:Array = new Array();
      
      {
         const_157[const_697] = "None";
         const_157[const_362] = "Pet";
         const_157[const_102] = "Minion";
         const_157[const_109] = "Lieutenant";
         const_157[const_123] = "MiniBoss";
         const_157[const_92] = "Boss";
         const_247[const_102] = 0.08;
         const_247[const_109] = 0.2;
         const_247[const_123] = 0.2;
         const_247[const_92] = 1;
         const_267[const_102] = 0;
         const_267[const_109] = 0.01;
         const_267[const_123] = 0.01;
         const_267[const_92] = 0.01;
         const_227[const_102] = 0.2;
         const_227[const_109] = 0.6;
         const_227[const_123] = 0.8;
         const_227[const_92] = 2;
         const_132[const_362] = [0,407,444,463,484,505,528,552,577,603,631,659,689,721,754,789,825,864,903,945,989,1035,1083,1134,1186,1242,1300,1361,1426,1492,1562,1636,1713,1794,1879,1968,2061,2159,2260,2367,2480,2598,2721,2850,2986,3128,3277,3433,3597,3769,3948];
         const_132[const_102] = [0,242,283,305,349,376,404,434,466,500,537,561,587,615,643,673,703,737,771,807,845,883,925,969,1013,1061,1111,1163,1219,1275,1335,1399,1465,1535,1607,1683,1763,1847,1934,2025,2123,2223,2329,2439,2555,2677,2805,2939,3079,3227,3381];
         const_132[const_109] = [0,371,433,467,535,575,618,663,712,763,818,855,893,935,977,1022,1068,1117,1169,1223,1279,1338,1400,1465,1533,1604,1679,1757,1840,1926,2016,2111,2210,2314,2423,2537,2657,2782,2913,3051,3196,3347,3506,3672,3846,4029,4220,4421,4631,4852,5083];
         const_132[const_123] = [0,408,476,513,588,632,679,728,782,838,898,938,981,1026,1072,1121,1172,1226,1282,1341,1403,1467,1536,1607,1681,1759,1841,1927,2018,2111,2210,2314,2423,2537,2656,2781,2912,3050,3193,3344,3503,3668,3842,4024,4215,4415,4625,4845,5075,5317,5570];
         const_132[const_92] = [0,457,534,575,658,707,760,815,875,938,1005,1050,1098,1148,1200,1254,1311,1371,1434,1500,1569,1640,1717,1796,1879,1966,2058,2153,2254,2359,2469,2585,2707,2834,2967,3106,3253,3406,3566,3734,3912,4096,4290,4493,4706,4930,5164,5409,5666,5936,6219];
      }
      
      internal var var_2508:Boolean = false;
      
      internal var entName:String = null;
      
      internal var parentEntType:String = null;
      
      internal var var_1606:XML = null;
      
      internal var displayName:String;
      
      internal var width:uint;
      
      internal var height:uint;
      
      internal var var_1449:Array = null;
      
      internal var gfxType:GfxType = null;
      
      internal var var_2241:Boolean = false;
      
      internal var meleePower:String = null;
      
      internal var rangedPower:String = null;
      
      internal var var_1200:Array;
      
      internal var meleeDamage:Number = 0;
      
      internal var var_1044:Number = 0;
      
      internal var var_939:Number = 0;
      
      internal var armorClass:Number = 0;
      
      internal var var_251:Number = 0;
      
      internal var var_562:String = null;
      
      internal var var_855:uint = 0;
      
      internal var var_782:uint = 0;
      
      internal var shirtColor:uint = 0;
      
      internal var pantColor:uint = 0;
      
      internal var var_760:String = null;
      
      internal var var_857:String = null;
      
      internal var var_769:String = null;
      
      internal var var_779:String = null;
      
      internal var var_439:String = null;
      
      internal var var_2836:Number = 1;
      
      internal var var_1635:String = null;
      
      internal var var_1452:String = null;
      
      internal var var_738:String = null;
      
      internal var var_1350:String = null;
      
      internal var var_1570:String = null;
      
      internal var var_1623:String = null;
      
      internal var var_248:String;
      
      internal var var_103:String;
      
      internal var var_1594:Number = 0;
      
      internal var var_1817:Number = 1;
      
      internal var var_2198:Number = 0;
      
      internal var var_1036:Number = 0;
      
      internal var var_1109:Number = 0;
      
      internal var var_2809:Boolean;
      
      internal var var_2604:Boolean;
      
      internal var var_2783:Boolean;
      
      internal var var_328:String;
      
      internal var sleepAnim:String = null;
      
      internal var dramaAnim:String = null;
      
      internal var var_2215:GfxType = null;
      
      internal var equippedGear:Vector.<EntTypeGear>;
      
      internal var var_832:Boolean = false;
      
      internal var var_2516:Boolean = false;
      
      internal var var_138:uint;
      
      internal var var_106:String;
      
      internal var baseLevel:uint;
      
      internal var var_1767:uint;
      
      internal var var_2509:String;
      
      internal var var_2884:String;
      
      internal var var_2940:String;
      
      internal var var_2930:String;
      
      internal var var_620:Boolean = false;
      
      internal var var_1685:Boolean = false;
      
      internal var className:String = "";
      
      internal var var_2677:Boolean = false;
      
      internal var var_2928:Boolean = false;
      
      internal var var_1336:Number = 0;
      
      internal var var_2538:Boolean = false;
      
      internal var var_2238:Boolean = false;
      
      internal var var_913:Boolean = false;
      
      internal var bPassiveTurnToFace:Boolean = true;
      
      public function EntType()
      {
         this.var_1200 = new Array();
         this.equippedGear = new Vector.<EntTypeGear>(MAX_SLOTS,true);
         super();
         this.var_1449 = new Array();
      }
      
      public static function method_30(param1:XML) : void
      {
         class_14.entTypesXMLs.push(param1);
         method_584();
      }
      
      public static function method_584() : void
      {
         var _loc1_:EntType = null;
         var _loc2_:XML = null;
         var _loc3_:XML = null;
         for each(_loc2_ in class_14.entTypesXMLs)
         {
            for each(_loc3_ in _loc2_.*)
            {
               _loc1_ = new EntType();
               _loc1_.entName = _loc3_.attribute("EntName");
               if(_loc1_.entName == "")
               {
                  class_24.method_7("Nameless Enttype - possibly a typo in this entype or the previous one");
               }
               _loc1_.parentEntType = _loc3_.attribute("parent");
               _loc1_.var_1606 = _loc3_;
               if(class_14.entTypes[_loc1_.entName])
               {
                  class_24.method_7("Duplicate Ent Type for ent named: " + _loc1_.entName);
               }
               class_14.entTypes[_loc1_.entName] = _loc1_;
            }
         }
      }
      
      public static function method_370(param1:uint, param2:Number) : uint
      {
         var _loc3_:uint = uint((param1 & 16711680) >> 16);
         var _loc4_:uint = uint((param1 & 65280) >> 8);
         var _loc5_:uint = uint(param1 & 255);
         var _loc6_:Array;
         (_loc6_ = MathUtil.method_1971(_loc3_,_loc4_,_loc5_))[2] = Math.max(_loc6_[2] - param2,0);
         var _loc7_:Array = MathUtil.method_1652(_loc6_[0],_loc6_[1],_loc6_[2]);
         return MathUtil.method_1546(_loc7_[0],_loc7_[1],_loc7_[2]);
      }
      
      public static function method_97(param1:String, param2:String, param3:Number, param4:Vector.<EntTypeGear>, param5:String, param6:String, param7:String, param8:String, param9:String, param10:uint, param11:uint, param12:uint, param13:uint) : String
      {
         var _loc15_:EntTypeGear = null;
         var _loc16_:GearType = null;
         var _loc14_:* = (_loc14_ = (_loc14_ = (_loc14_ = (_loc14_ = (_loc14_ = (_loc14_ = (_loc14_ = (_loc14_ = (_loc14_ = "<EntType EntName=\'" + param1 + "\' parent=\'" + param2 + "\'>") + ("<HairColor>" + param10 + "</HairColor>")) + ("<SkinColor>" + param11 + "</SkinColor>")) + ("<ShirtColor>" + param12 + "</ShirtColor>")) + ("<PantColor>" + param13 + "</PantColor>")) + ("<GenderSet>" + param5 + "</GenderSet>")) + ("<HeadSet>" + param6 + "</HeadSet>")) + ("<HairSet>" + param7 + "</HairSet>")) + ("<MouthSet>" + param8 + "</MouthSet>")) + ("<FaceSet>" + param9 + "</FaceSet>");
         if(param3)
         {
            _loc14_ += "<CustomScale>" + param3 + "</CustomScale>";
         }
         if(param4)
         {
            _loc14_ += "<EquippedGear>";
            for each(_loc15_ in param4)
            {
               if(_loc15_ && Boolean(_loc15_.gearName))
               {
                  if(_loc16_ = class_14.gearTypesDict[_loc15_.gearName])
                  {
                     _loc14_ += "<" + _loc16_.type + ">" + _loc15_.var_2432 + "</" + _loc16_.type + ">";
                  }
               }
            }
            _loc14_ += "</EquippedGear>";
         }
         return _loc14_ + "</EntType>";
      }
      
      public static function method_683(param1:String, param2:String, param3:String, param4:String, param5:uint, param6:uint, param7:uint, param8:uint, param9:Number, param10:String, param11:String) : String
      {
         var _loc12_:uint = EntType.method_370(param5,HAIR_DARKER_DELTA);
         var _loc13_:uint = EntType.method_370(param6,SKIN_DARKER_DELTA);
         var _loc14_:uint = EntType.method_370(param7,SHIRT_DARKER_DELTA);
         var _loc15_:uint = EntType.method_370(param8,PANTS_DARKER_DELTA);
         var _loc16_:String = "<GfxType>";
         if(param9)
         {
            _loc16_ += "<AnimScale>" + param9 + "</AnimScale>";
         }
         _loc16_ = (_loc16_ = (_loc16_ = (_loc16_ = (_loc16_ = (_loc16_ = (_loc16_ = (_loc16_ += "<ColorSwap>" + EntType.COLOR_HAIR + "=0x" + param5.toString(16) + "</ColorSwap>") + ("<ColorSwap7>" + EntType.COLOR_HAIR_DARK + "=0x" + _loc12_.toString(16) + "</ColorSwap7>")) + ("<ColorSwap2>" + EntType.COLOR_SKIN + "=0x" + param6.toString(16) + "</ColorSwap2>")) + ("<ColorSwap3>" + EntType.COLOR_SKIN_DARK + "=0x" + _loc13_.toString(16) + "</ColorSwap3>")) + ("<ColorSwap4>" + EntType.COLOR_SHIRT + "=0x" + param7.toString(16) + "</ColorSwap4>")) + ("<ColorSwap5>" + EntType.COLOR_SHIRT_DARK + "=0x" + _loc14_.toString(16) + "</ColorSwap5>")) + ("<ColorSwap8>" + EntType.COLOR_PANTS + "=0x" + param8.toString(16) + "</ColorSwap8>")) + ("<ColorSwap9>" + EntType.COLOR_PANTS_DARK + "=0x" + _loc15_.toString(16) + "</ColorSwap9>");
         var _loc17_:String = EntType.PALADIN_OPTIONS_FILE;
         if(param10 == "Mage")
         {
            _loc17_ = EntType.MAGE_OPTIONS_FILE;
         }
         else if(param10 == "Rogue")
         {
            _loc17_ = EntType.ROGUE_OPTIONS_FILE;
         }
         if(param11)
         {
            _loc16_ += "<CustomArt>" + _loc17_ + "/" + param11 + "</CustomArt>";
         }
         return (_loc16_ = (_loc16_ = (_loc16_ = (_loc16_ += "<CustomArt2>" + _loc17_ + "/" + param1 + "</CustomArt2>") + ("<CustomArt3>" + _loc17_ + "/" + param2 + "</CustomArt3>")) + ("<CustomArt4>" + _loc17_ + "/" + param3 + "</CustomArt4>")) + ("<CustomArt5>" + _loc17_ + "/" + param4 + "</CustomArt5>")) + "</GfxType>";
      }
      
      public static function method_57(param1:String, param2:String) : void
      {
         var _loc3_:XML = new XML(param1);
         var _loc4_:EntType;
         (_loc4_ = new EntType()).entName = _loc3_.attribute("EntName");
         _loc4_.parentEntType = _loc3_.attribute("parent");
         _loc4_.var_1606 = _loc3_;
         dynamicEntTypes[param2 + ":" + _loc4_.entName] = _loc4_;
      }
      
      public static function method_48(param1:String, param2:String = null) : EntType
      {
         var _loc5_:EntType = null;
         var _loc3_:String = !!param2 ? param2 + ":" + param1 : param1;
         var _loc4_:EntType;
         if(!(_loc4_ = class_14.entTypes[_loc3_]))
         {
            _loc4_ = dynamicEntTypes[_loc3_];
         }
         if(Boolean(_loc4_) && !_loc4_.var_2508)
         {
            if(_loc4_.parentEntType != null && _loc4_.parentEntType != "" && _loc4_.parentEntType.toLowerCase() != "none")
            {
               if((_loc5_ = method_48(_loc4_.parentEntType)) != null)
               {
                  _loc4_.method_1595(_loc5_);
               }
            }
            method_828(_loc4_);
            _loc4_.var_2508 = true;
            _loc4_.gfxType = _loc4_.method_60();
         }
         return _loc4_;
      }
      
      public static function method_828(param1:EntType) : EntType
      {
         var _loc4_:XML = null;
         var _loc5_:String = null;
         var _loc7_:String = null;
         var _loc8_:Array = null;
         var _loc9_:String = null;
         var _loc10_:String = null;
         var _loc11_:XML = null;
         var _loc12_:String = null;
         var _loc13_:Array = null;
         var _loc14_:EntTypeGear = null;
         var _loc15_:GfxType = null;
         var _loc16_:Number = NaN;
         var _loc2_:XML = param1.var_1606;
         var _loc3_:Number = 0;
         for each(_loc4_ in _loc2_.*)
         {
            if((_loc7_ = String(_loc4_.name())) == "DisplayName")
            {
               param1.displayName = _loc4_;
            }
            else if(_loc7_ == "HitPoints")
            {
               param1.var_939 = Number(_loc4_);
            }
            else if(_loc7_ == "ArmorClass")
            {
               param1.armorClass = Number(_loc4_);
            }
            else if(_loc7_ == "MeleeDamage")
            {
               param1.meleeDamage = Number(_loc4_);
            }
            else if(_loc7_ == "MagicDamage")
            {
               param1.var_1044 = Number(_loc4_);
            }
            else if(_loc7_ == "Speed")
            {
               param1.var_251 = Number(_loc4_);
            }
            else if(_loc7_ == "Width")
            {
               param1.width = uint(_loc4_);
            }
            else if(_loc7_ == "Height")
            {
               param1.height = uint(_loc4_);
            }
            else if(_loc7_ == "Behavior")
            {
               param1.var_562 = _loc4_.toString();
            }
            else if(_loc7_ == "SoundDeathRattle")
            {
               param1.var_1635 = _loc4_;
            }
            else if(_loc7_ == "SoundBloodied")
            {
               param1.var_1452 = _loc4_;
            }
            else if(_loc7_ == "SoundHitGrunt")
            {
               param1.var_738 = _loc4_;
            }
            else if(_loc7_ == "SoundJump")
            {
               param1.var_1350 = _loc4_;
            }
            else if(_loc7_ == "SoundActivate")
            {
               param1.var_1570 = _loc4_;
            }
            else if(_loc7_ == "SoundGrumble")
            {
               param1.var_1623 = _loc4_;
            }
            else if(_loc7_ == "Realm")
            {
               param1.var_106 = _loc4_.toString();
            }
            else if(_loc7_ == "Kingdom")
            {
               param1.var_103 = _loc4_.toString();
            }
            else if(_loc7_ == "Element")
            {
               param1.var_328 = _loc4_.toString();
            }
            else if(_loc7_ == "Level")
            {
               param1.baseLevel = uint(_loc4_);
            }
            else if(_loc7_ == "GroupLevel")
            {
               param1.var_1767 = uint(_loc4_);
            }
            else if(_loc7_ == "RewardClass")
            {
               param1.var_248 = _loc4_.toString();
            }
            else if(_loc7_ == "ItemDropChance")
            {
               param1.var_2198 = Number(_loc4_.toString());
            }
            else if(_loc7_ == "HealthDropRatio")
            {
               param1.var_1109 = Number(_loc4_);
            }
            else if(_loc7_ == "GoldDrop")
            {
               _loc8_ = _loc4_.toString().split(",");
               param1.var_1594 = Number(_loc8_[0]);
               if(_loc8_.length > 1)
               {
                  param1.var_1817 = Number(_loc8_[1]);
               }
            }
            else if(_loc7_ == "Flying")
            {
               param1.var_832 = MathUtil.method_50(_loc4_);
            }
            else if(_loc7_ == "MeleePower")
            {
               param1.meleePower = _loc4_.toString();
            }
            else if(_loc7_ == "RangedPower")
            {
               param1.rangedPower = _loc4_.toString();
            }
            else if(_loc7_ == "Powers")
            {
               param1.var_1200 = _loc4_.toString().split(",");
            }
            else if(_loc7_ == "ExpMult")
            {
               param1.var_1036 = Number(_loc4_);
            }
            else if(_loc7_ == "HairColor")
            {
               param1.var_855 = uint(_loc4_);
            }
            else if(_loc7_ == "SkinColor")
            {
               param1.var_782 = uint(_loc4_);
            }
            else if(_loc7_ == "ShirtColor")
            {
               param1.shirtColor = uint(_loc4_);
            }
            else if(_loc7_ == "PantColor")
            {
               param1.pantColor = uint(_loc4_);
            }
            else if(_loc7_ == "HeadSet")
            {
               param1.var_760 = _loc4_.toString();
            }
            else if(_loc7_ == "HairSet")
            {
               param1.var_857 = _loc4_.toString();
            }
            else if(_loc7_ == "MouthSet")
            {
               param1.var_769 = _loc4_.toString();
            }
            else if(_loc7_ == "FaceSet")
            {
               param1.var_779 = _loc4_.toString();
            }
            else if(_loc7_ == "GenderSet")
            {
               param1.var_439 = _loc4_.toString();
            }
            else if(_loc7_ == "SleepAnim")
            {
               param1.sleepAnim = _loc4_.toString();
            }
            else if(_loc7_ == "DramaAnim")
            {
               param1.dramaAnim = _loc4_.toString();
            }
            else if(_loc7_ == "CustomScale")
            {
               param1.var_2836 = Number(_loc4_);
            }
            else if(_loc7_ == "DevStatus")
            {
               _loc3_++;
            }
            else if(_loc7_ == "GfxType")
            {
               param1.var_1449.push(_loc4_);
            }
            else if(_loc7_ == "ReactPct")
            {
               param1.var_1336 = Number(_loc4_);
            }
            else if(_loc7_ == "PassiveTurnToFace")
            {
               param1.bPassiveTurnToFace = MathUtil.method_50(_loc4_);
            }
            else if(_loc7_ == "GenderFix")
            {
               if((_loc9_ = _loc4_.toString()) != "Male" && _loc9_ != "Female")
               {
                  class_24.method_7("Unknown Gender Fix Field: " + _loc9_);
               }
               param1.var_439 = _loc9_;
            }
            else if(_loc7_ == "EntRank")
            {
               if((_loc10_ = _loc4_.toString()) == "Pet")
               {
                  param1.var_138 = const_362;
               }
               else if(_loc10_ == "Minion")
               {
                  param1.var_138 = const_102;
               }
               else if(_loc10_ == "Lieutenant")
               {
                  param1.var_138 = const_109;
               }
               else if(_loc10_ == "MiniBoss")
               {
                  param1.var_138 = const_123;
               }
               else if(_loc10_ == "Boss")
               {
                  param1.var_138 = const_92;
               }
            }
            else if(_loc7_ == "EquippedGear")
            {
               for each(_loc11_ in _loc4_.*)
               {
                  _loc12_ = String(_loc11_.name());
                  _loc13_ = _loc11_.toString().split(":");
                  _loc14_ = new EntTypeGear(_loc13_[0],_loc13_[1],_loc13_[2],_loc13_[3],_loc13_[4],_loc13_[5]);
                  if(_loc12_ == "Armor")
                  {
                     param1.equippedGear[ARMOR_SLOT] = _loc14_;
                  }
                  else if(_loc12_ == "Gloves")
                  {
                     param1.equippedGear[GLOVES_SLOT] = _loc14_;
                  }
                  else if(_loc12_ == "Boots")
                  {
                     param1.equippedGear[BOOTS_SLOT] = _loc14_;
                  }
                  else if(_loc12_ == "Hat")
                  {
                     param1.equippedGear[HAT_SLOT] = _loc14_;
                  }
                  else if(_loc12_ == "Sword")
                  {
                     param1.equippedGear[SWORD_SLOT] = _loc14_;
                  }
                  else if(_loc12_ == "Shield")
                  {
                     param1.equippedGear[SHIELD_SLOT] = _loc14_;
                  }
                  else
                  {
                     class_24.method_7("Unrecognized Property in " + param1.entName + ": " + _loc12_);
                  }
               }
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + param1.entName + ": " + _loc7_);
            }
         }
         if((_loc5_ = param1.entName) == "Paladin" || _loc5_ == "StarterPaladin")
         {
            param1.className = "Paladin";
         }
         else if(_loc5_ == "Rogue" || _loc5_ == "StarterRogue")
         {
            param1.className = "Rogue";
         }
         else if(_loc5_ == "Mage" || _loc5_ == "StarterMage")
         {
            param1.className = "Mage";
         }
         if(!param1.var_328)
         {
            switch(param1.var_103)
            {
               case "Infernal":
                  param1.var_328 = "Air";
                  break;
               case "Undead":
                  param1.var_328 = "Death";
                  break;
               case "Mythic":
                  param1.var_328 = "Ice";
                  break;
               case "Trog":
                  param1.var_328 = "Earth";
                  break;
               case "Draconic":
                  param1.var_328 = "Fire";
                  break;
               case "Sylvan":
                  param1.var_328 = "Life";
                  break;
               default:
                  param1.var_328 = null;
            }
         }
         if(!_loc5_.indexOf("RockHulkBase") || !_loc5_.indexOf("DevourerBase") || !_loc5_.indexOf("Craft") || !_loc5_.indexOf("NPCMoai") || !_loc5_.indexOf("NPCIronStatue") || !_loc5_.indexOf("NPCVillager09") || !_loc5_.indexOf("NPCTitus") || !_loc5_.indexOf("NPCAnna") || !_loc5_.indexOf("NPCOldMan") || !_loc5_.indexOf("NPCSwampOldMan") || !_loc5_.indexOf("NPCOldMan") || !_loc5_.indexOf("NPCVillager07") || !_loc5_.indexOf("NPCSwampVillager07") || !_loc5_.indexOf("NPCOldMan") || !_loc5_.indexOf("NPCElric") || !_loc5_.indexOf("NPCRuggedVillager04") || !_loc5_.indexOf("NPCRuggedVillager03") || !_loc5_.indexOf("NPCCaptain"))
         {
            param1.bPassiveTurnToFace = false;
         }
         if(_loc5_ == "EmberBush")
         {
            param1.var_2940 = "EmberBushFire";
         }
         if(_loc5_ == "ScarabLarva" || _loc5_ == "ScarabLarvaSpawnBasic" || _loc5_ == "ScarabLarvaSpawn")
         {
            param1.var_2930 = "LarvaPoisonCloud";
         }
         if(_loc5_ == "IntroKraken" || !_loc5_.indexOf("CaveVigil") || _loc5_ == "LarvaSpawner")
         {
            param1.var_2677 = true;
         }
         if(_loc5_ == "DragonBase")
         {
            param1.var_1336 = 0.05;
         }
         if(!_loc5_.indexOf("OasisWarlock"))
         {
            (_loc15_ = new GfxType()).animClass = "a_WarlockOrb";
            _loc15_.var_29 = "SFX_1.swf";
            _loc15_.animScale = 0.5;
            param1.var_2215 = _loc15_;
         }
         if(_loc5_ == "DragonSoul")
         {
            param1.var_2516 = true;
         }
         param1.var_2538 = param1.var_138 == const_102;
         param1.var_2238 = param1.var_138 == const_92 || param1.var_138 == const_123 || param1.entName == "FireBomb";
         param1.method_686();
         var _loc6_:int = _loc5_.indexOf("Hard");
         param1.var_913 = _loc6_ >= 0 && _loc6_ == _loc5_.length - 4;
         if(param1.var_138 != const_92 || param1.var_248 == "RandomItem")
         {
            param1.var_2884 = param1.var_106;
         }
         else if(!param1.var_913)
         {
            param1.var_2509 = param1.entName;
         }
         else
         {
            param1.var_2509 = param1.entName.substr(0,param1.entName.length - 4);
         }
         param1.var_2809 = param1.var_103 && param1.var_106 && param1.var_1767 && param1.var_248 && param1.var_248 != "ExpAndGold" && param1.var_248 != "NoLoot" && param1.var_248 != "HealthOnly";
         param1.var_2604 = param1.var_103 && param1.var_106 && param1.var_1767 && param1.var_248 && param1.var_248 != "ExpAndGold" && param1.var_248 != "NoLoot" && param1.var_248 != "HealthOnly";
         param1.var_2783 = param1.var_103 && param1.var_106 && param1.var_1767 && param1.var_248 && param1.var_248 != "ExpAndGold" && param1.var_248 != "NoLoot" && param1.var_248 != "HealthOnly";
         if(param1.baseLevel && param1.var_1036 || param1.var_248 == "HealthOnly")
         {
            _loc16_ = const_227[param1.var_138];
            if(!param1.var_1109)
            {
               param1.var_1109 = _loc16_;
            }
            else
            {
               param1.var_1109 = _loc16_ * param1.var_1109;
            }
         }
         return param1;
      }
      
      public static function method_87(param1:String) : int
      {
         var _loc2_:int = 0;
         var _loc3_:String = param1.toUpperCase();
         if(_loc3_ == "ARMOR")
         {
            _loc2_ = int(EntType.ARMOR_SLOT);
         }
         else if(_loc3_ == "SWORD")
         {
            _loc2_ = int(EntType.SWORD_SLOT);
         }
         else if(_loc3_ == "SHIELD")
         {
            _loc2_ = int(EntType.SHIELD_SLOT);
         }
         else if(_loc3_ == "BOOTS")
         {
            _loc2_ = int(EntType.BOOTS_SLOT);
         }
         else if(_loc3_ == "GLOVES")
         {
            _loc2_ = int(EntType.GLOVES_SLOT);
         }
         else if(_loc3_ == "HAT")
         {
            _loc2_ = int(EntType.HAT_SLOT);
         }
         return _loc2_;
      }
      
      public static function method_523(param1:int) : String
      {
         var _loc2_:String = null;
         if(param1 == EntType.ARMOR_SLOT)
         {
            _loc2_ = "Armor";
         }
         else if(param1 == EntType.GLOVES_SLOT)
         {
            _loc2_ = "Gloves";
         }
         else if(param1 == EntType.BOOTS_SLOT)
         {
            _loc2_ = "Boots";
         }
         else if(param1 == EntType.HAT_SLOT)
         {
            _loc2_ = "Hat";
         }
         else if(param1 == EntType.SWORD_SLOT)
         {
            _loc2_ = "Sword";
         }
         else if(param1 == EntType.SHIELD_SLOT)
         {
            _loc2_ = "Shield";
         }
         return _loc2_;
      }
      
      public function method_1595(param1:EntType) : void
      {
         var _loc3_:* = undefined;
         this.displayName = param1.displayName;
         this.var_939 = param1.var_939;
         this.meleeDamage = param1.meleeDamage;
         this.var_1044 = param1.var_1044;
         this.armorClass = param1.armorClass;
         this.var_251 = param1.var_251;
         this.var_562 = param1.var_562;
         this.className = param1.className;
         this.var_1635 = param1.var_1635;
         this.var_738 = param1.var_738;
         this.var_1350 = param1.var_1350;
         this.var_1570 = param1.var_1570;
         this.var_1623 = param1.var_1623;
         this.var_1452 = param1.var_1452;
         this.width = param1.width;
         this.height = param1.height;
         this.var_1036 = param1.var_1036;
         this.var_1594 = param1.var_1594;
         this.var_1817 = param1.var_1817;
         this.sleepAnim = param1.sleepAnim;
         this.dramaAnim = param1.dramaAnim;
         this.var_855 = param1.var_855;
         this.var_782 = param1.var_782;
         this.shirtColor = param1.shirtColor;
         this.pantColor = param1.pantColor;
         this.var_760 = param1.var_760;
         this.var_857 = param1.var_857;
         this.var_769 = param1.var_769;
         this.var_779 = param1.var_779;
         this.var_439 = param1.var_439;
         this.var_1336 = param1.var_1336;
         this.bPassiveTurnToFace = param1.bPassiveTurnToFace;
         for(_loc3_ in param1.equippedGear)
         {
            this.equippedGear[_loc3_] = param1.equippedGear[_loc3_];
         }
         this.var_1449 = param1.var_1449.concat();
      }
      
      public function method_686() : void
      {
         this.var_620 = this.var_439 == "Female" || this.className == "Mage" && this.var_439 != "Male";
         this.var_1685 = this.className == "Mage" && !this.var_620 || this.className == "Paladin" && this.var_620;
         if(this.var_620 && this.className == "Rogue")
         {
            this.var_738 = "snd_hurt_mage_01|snd_hurt_mage_02|snd_hurt_mage_03|snd_silence|snd_silence|snd_silence";
         }
         else if(!this.var_620 && this.className == "Mage")
         {
            this.var_738 = "snd_hurt_mage_01_male|snd_hurt_mage_02_male|snd_hurt_mage_03_male|snd_silence|snd_silence|snd_silence";
         }
         else if(this.var_620 && this.className == "Paladin")
         {
            this.var_738 = "snd_hurt_paladin_01_female|snd_hurt_paladin_02_female|snd_hurt_paladin_03_female|snd_silence|snd_silence|snd_silence";
         }
      }
      
      public function method_60() : GfxType
      {
         var _loc1_:class_21 = null;
         var _loc2_:XML = null;
         var _loc4_:XML = null;
         var _loc5_:* = undefined;
         var _loc6_:String = null;
         var _loc7_:EntTypeGear = null;
         var _loc8_:GearType = null;
         var _loc9_:int = 0;
         var _loc3_:GfxType = new GfxType();
         for each(_loc4_ in this.var_1449)
         {
            GfxType.method_53(_loc4_,_loc3_);
         }
         if(Boolean(this.var_760) && Boolean(this.var_857) && Boolean(this.var_769) && Boolean(this.var_779))
         {
            _loc6_ = EntType.method_683(this.var_760,this.var_857,this.var_769,this.var_779,this.var_855,this.var_782,this.shirtColor,this.pantColor,this.var_2836,this.className,this.var_439);
            GfxType.method_53(new XML(_loc6_),_loc3_);
         }
         for(_loc5_ in this.equippedGear)
         {
            if(_loc7_ = this.equippedGear[_loc5_])
            {
               if(_loc8_ = class_14.gearTypesDict[_loc7_.gearName])
               {
                  _loc9_ = EntType.method_87(_loc8_.type);
                  _loc2_ = this.var_1685 && Boolean(_loc8_.var_1303) ? _loc8_.var_1303 : _loc8_.var_582;
                  GfxType.method_53(_loc2_,_loc3_,_loc9_);
                  if(_loc7_.var_644)
                  {
                     _loc1_ = class_14.var_194[_loc7_.var_644];
                     if(_loc1_)
                     {
                        _loc3_.colorSwaps.unshift(new ColorSwap(13693168,_loc1_.var_935,_loc5_));
                        _loc3_.colorSwaps.unshift(new ColorSwap(8438000,_loc1_.color,_loc5_));
                        _loc3_.colorSwaps.unshift(new ColorSwap(28896,_loc1_.var_209,_loc5_));
                     }
                  }
                  if(_loc7_.var_705)
                  {
                     _loc1_ = class_14.var_194[_loc7_.var_705];
                     if(_loc1_)
                     {
                        _loc3_.colorSwaps.unshift(new ColorSwap(16751001,_loc1_.var_935,_loc5_));
                        _loc3_.colorSwaps.unshift(new ColorSwap(11534336,_loc1_.color,_loc5_));
                        _loc3_.colorSwaps.unshift(new ColorSwap(6291456,_loc1_.var_209,_loc5_));
                     }
                  }
               }
            }
         }
         _loc3_.method_1289();
         this.var_2241 = true;
         return _loc3_;
      }
   }
}
