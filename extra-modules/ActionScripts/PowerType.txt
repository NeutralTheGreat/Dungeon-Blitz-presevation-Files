package
{
   import flash.display.MovieClip;
   import flash.geom.Point;
   import flash.utils.Dictionary;
   
   public class PowerType
   {
      
      public static const const_1414:uint = 0;
      
      public static const const_1400:uint = 1;
      
      public static const const_1372:uint = 2;
      
      public static const const_1401:uint = 3;
      
      public static const const_1417:uint = 4;
      
      public static const const_423:uint = 7;
      
      private static const const_784:Vector.<String> = Vector.<String>(["VigilLightningFront","VigilFlame","VigilFlameUp","VigilFlameDown","VigilLightningDown","VigilPoisonFront","NephitSpire","NephitStorm","SpikeTrapMelee","WarlockStorm","MimicSpire","BoneGolemStorm","BoneGolemStormOffset","DefectorIceMeteor","DreamSpire","PhantomVine","EmperorBlast","FirePitMelee"]);
      
      public static const TARGETMETHOD_MELEE:uint = 1;
      
      public static const TARGETMETHOD_RANGED:uint = 2;
      
      public static const TARGETMETHOD_PIERCING:uint = 3;
      
      public static const TARGETMETHOD_PROJECTILE:uint = 4;
      
      public static const TARGETMETHOD_PBAOE:uint = 5;
      
      public static const TARGETMETHOD_SELF:uint = 6;
      
      public static const TARGETMETHOD_FRIEND:uint = 7;
      
      public static const TARGETMETHOD_GROUP:uint = 8;
      
      public static const TARGETMETHOD_GROUPANDSELF:uint = 9;
      
      public static const TARGETMETHOD_RANGEDAOE:uint = 10;
      
      public static const const_99:uint = 11;
      
      public static const const_32:uint = 12;
      
      public static const const_275:uint = 13;
      
      public static const const_130:uint = 14;
      
      public static const const_46:uint = 15;
      
      public static const const_111:uint = 16;
      
      public static const const_201:uint = 17;
      
      public static const const_232:uint = 18;
      
      public static const const_424:uint = 19;
      
      public static const const_304:uint = 20;
      
      public static const const_113:uint = 21;
      
      public static const const_921:uint = 22;
      
      public static const const_568:uint = 23;
      
      public static const const_89:uint = 24;
      
      public static const const_517:uint = 25;
      
      public static const const_248:uint = 26;
      
      public static const const_259:uint = 27;
      
      public static const const_96:uint = 28;
      
      public static const const_473:uint = 29;
      
      public static const const_698:uint = 30;
      
      public static const ANIMSOURCE_FEET:uint = 1;
      
      public static const const_778:uint = 2;
      
      public static const ANIMSOURCE_GROUND:uint = 3;
      
      public static const const_440:uint = 4;
      
      public static const ANIMSOURCE_CENTER:uint = 5;
      
      public static const ANIMSOURCE_FIRESOCKET:uint = 6;
      
      public static const ANIMSOURCE_TARGETFEET:uint = 7;
      
      public static const const_293:uint = 8;
      
      public static const ANIMSOURCE_TARGETCENTER:uint = 9;
      
      public static const const_671:uint = 10;
      
      public static const const_559:uint = 11;
      
      public static const const_219:uint = 12;
      
      public static const const_564:uint = 13;
      
      public static const DAMAGETYPE_PHYSICAL:String = "Physical";
      
      public static const DAMAGETYPE_LIGHTNING:String = "Lightning";
      
      public static const DAMAGETYPE_FIRE:String = "Fire";
      
      public static const DAMAGETYPE_HOLY:String = "Holy";
      
      public static const DAMAGETYPE_ENERGY:String = "Energy";
      
      public static const const_755:String = "Death";
      
      public static const const_714:String = "Ice";
      
      public static const const_673:String = "Life";
      
      public static const const_804:String = "Air";
      
      public static const const_740:String = "Earth";
      
      public static const const_1336:int = 0;
      
      public static const const_872:int = 1;
      
      public static const const_537:int = 2;
      
      public static var var_511:PowerType = null;
      
      public static var var_440:PowerType = null;
      
      public static var var_824:PowerType = null;
      
      public static var var_315:PowerType = null;
      
      public static var var_836:PowerType = null;
      
      {
         const_784.fixed = true;
      }
      
      internal var powerID:uint;
      
      internal var powerName:String;
      
      internal var basePowerName:String = "";
      
      internal var var_7:int;
      
      internal var var_2956:Boolean;
      
      internal var var_6:uint;
      
      internal var var_2605:uint;
      
      internal var displayName:String;
      
      internal var iconName:String;
      
      internal var description:String = "";
      
      internal var var_1499:String = "";
      
      internal var var_136:String;
      
      internal var var_2130:String;
      
      internal var var_801:Boolean = false;
      
      internal var var_108:Vector.<uint>;
      
      internal var var_287:uint = 0;
      
      internal var var_125:uint;
      
      internal var var_653:uint;
      
      internal var var_713:uint = 0;
      
      internal var var_1653:GfxType = null;
      
      internal var var_942:Vector.<GfxType> = null;
      
      internal var var_2321:GfxType = null;
      
      internal var var_457:uint;
      
      internal var var_2187:Boolean = false;
      
      internal var var_2888:Boolean = false;
      
      internal var var_1232:Vector.<GfxType> = null;
      
      internal var var_1700:Vector.<GfxType> = null;
      
      internal var var_318:uint;
      
      internal var var_352:Vector.<GfxType> = null;
      
      internal var var_2204:GfxType = null;
      
      internal var var_625:GfxType = null;
      
      internal var var_1418:GfxType = null;
      
      internal var var_1169:Vector.<class_43>;
      
      internal var var_1454:String = null;
      
      internal var var_2103:String = null;
      
      internal var var_2347:String = null;
      
      internal var var_402:String;
      
      private var var_1634:uint;
      
      public var var_507:int;
      
      public var var_127:int;
      
      internal var var_1571:int;
      
      internal var var_820:Vector.<int>;
      
      internal var aoeRadius:uint;
      
      internal var var_375:Vector.<uint>;
      
      internal var coolDownTime:uint;
      
      internal var manaCost:uint;
      
      internal var var_1517:uint;
      
      internal var var_535:uint;
      
      internal var var_219:Boolean = false;
      
      internal var var_2327:Number = 0;
      
      internal var var_630:Vector.<Number>;
      
      internal var damageMultFull:Number = 0;
      
      internal var var_157:String = null;
      
      internal var var_381:Vector.<String> = null;
      
      internal var var_437:Vector.<String> = null;
      
      internal var var_851:Vector.<Array> = null;
      
      internal var var_1629:uint = 0;
      
      internal var var_1962:uint = 0;
      
      internal var var_2346:String = null;
      
      internal var var_543:String = null;
      
      internal var var_2808:String = null;
      
      internal var runeIcon:String = null;
      
      internal var var_879:Boolean = false;
      
      internal var var_2323:Boolean = false;
      
      internal var var_1989:Number = 0;
      
      internal var var_347:String;
      
      internal var var_698:String;
      
      internal var var_1668:int;
      
      internal var var_1591:Vector.<int>;
      
      internal var var_1743:int;
      
      internal var var_1474:Vector.<int>;
      
      internal var var_1075:uint = 0;
      
      internal var var_1212:uint = 0;
      
      internal var var_275:Boolean = false;
      
      internal var var_1735:Boolean = false;
      
      internal var bIsProjectile:Boolean = false;
      
      internal var var_301:Boolean = false;
      
      internal var var_470:Boolean = false;
      
      internal var var_749:Boolean = false;
      
      internal var var_2786:Boolean = false;
      
      internal var var_2486:Boolean = false;
      
      internal var var_1789:Boolean = false;
      
      internal var var_2895:Boolean = true;
      
      internal var var_2846:Boolean = false;
      
      internal var var_2273:Boolean = false;
      
      internal var var_2049:Boolean = false;
      
      internal var var_2042:Boolean = false;
      
      internal var var_2927:Boolean = false;
      
      internal var var_2475:Boolean = false;
      
      internal var var_1427:Boolean = false;
      
      internal var var_1600:Boolean = false;
      
      internal var var_1801:Boolean = false;
      
      internal var var_2674:Boolean = false;
      
      internal var var_1439:Boolean = false;
      
      internal var var_2369:Boolean = false;
      
      internal var var_1759:Boolean = false;
      
      internal var var_2451:Boolean = false;
      
      internal var var_2690:Boolean = false;
      
      internal var var_2629:Boolean = false;
      
      internal var var_2510:Boolean = false;
      
      internal var var_2793:Boolean = false;
      
      internal var var_2553:Boolean = false;
      
      internal var var_2616:Boolean = false;
      
      internal var var_1682:Boolean = false;
      
      internal var var_2943:Boolean = false;
      
      internal var var_2414:Boolean = false;
      
      internal var var_1612:int = 0;
      
      internal var var_646:uint = 0;
      
      internal var var_2900:Boolean = false;
      
      internal var var_93:String = null;
      
      internal var var_1551:Boolean = false;
      
      internal var var_1774:String = null;
      
      internal var var_1689:Boolean = false;
      
      internal var var_2554:Boolean = false;
      
      internal var var_1867:Boolean = false;
      
      internal var var_2770:Boolean = false;
      
      internal var var_2063:Boolean = false;
      
      internal var var_2511:Boolean = false;
      
      internal var var_2585:String = null;
      
      internal var var_2426:Boolean = false;
      
      internal var var_2586:Boolean = false;
      
      internal var var_2520:Boolean = false;
      
      internal var var_2513:Boolean = false;
      
      public function PowerType()
      {
         this.var_108 = new Vector.<uint>();
         this.var_1169 = new Vector.<class_43>();
         this.var_630 = new Vector.<Number>();
         super();
      }
      
      public static function method_505(param1:XML) : void
      {
         method_18(param1,class_14.powerTypes,class_14.powerTypesDict,false);
      }
      
      public static function method_476(param1:XML) : void
      {
         method_18(param1,class_14.powerTypes,class_14.powerTypesDict,true);
         var_511 = class_14.powerTypesDict["SummonPet"];
         if(!var_511)
         {
            class_24.method_7("Summon Pet power must exist, but none was found!");
         }
         var_440 = class_14.powerTypesDict["SummonMount"];
         if(!var_440)
         {
            class_24.method_7("Summon Mount power must exist, but none was found!");
         }
         var_824 = class_14.powerTypesDict["Dismount"];
         if(!var_824)
         {
            class_24.method_7("Dismount power must exist, but none was found!");
         }
         var_315 = class_14.powerTypesDict["VanityPet"];
         if(!var_315)
         {
            class_24.method_7("Vanity Pet power must exist, but none was found!");
         }
         var_836 = class_14.powerTypesDict["DismissPet"];
         if(!var_836)
         {
            class_24.method_7("Dismiss Pet power must exist, but none was found!");
         }
      }
      
      private static function method_210(param1:String) : uint
      {
         if(param1 == "Feet")
         {
            return ANIMSOURCE_FEET;
         }
         if(param1 == "Head")
         {
            return const_778;
         }
         if(param1 == "Ground")
         {
            return ANIMSOURCE_GROUND;
         }
         if(param1 == "TargetPos")
         {
            return const_440;
         }
         if(param1 == "Center")
         {
            return ANIMSOURCE_CENTER;
         }
         if(param1 == "Socket")
         {
            return ANIMSOURCE_FIRESOCKET;
         }
         if(param1 == "TargetFeet")
         {
            return ANIMSOURCE_TARGETFEET;
         }
         if(param1 == "TargetHead")
         {
            return const_293;
         }
         if(param1 == "TargetCenter")
         {
            return ANIMSOURCE_TARGETCENTER;
         }
         if(param1 == "AttackFeet")
         {
            return const_671;
         }
         if(param1 == "Pet")
         {
            return const_559;
         }
         if(param1 == "TargetHit")
         {
            return const_219;
         }
         if(param1 == "MouseFeet")
         {
            return const_564;
         }
         class_24.method_7("Unknown Anim Source Name:" + param1);
         return 0;
      }
      
      public static function method_771(param1:XML, param2:Boolean) : PowerType
      {
         var _loc4_:XML = null;
         var _loc6_:String = null;
         var _loc7_:String = null;
         var _loc8_:Array = null;
         var _loc9_:uint = 0;
         var _loc10_:String = null;
         var _loc11_:Array = null;
         var _loc12_:String = null;
         var _loc13_:Array = null;
         var _loc14_:String = null;
         var _loc15_:String = null;
         var _loc16_:Array = null;
         var _loc17_:String = null;
         var _loc18_:String = null;
         var _loc19_:Array = null;
         var _loc20_:Vector.<uint> = null;
         var _loc21_:String = null;
         var _loc22_:Array = null;
         var _loc23_:Vector.<int> = null;
         var _loc24_:String = null;
         var _loc25_:Array = null;
         var _loc26_:Vector.<int> = null;
         var _loc27_:String = null;
         var _loc28_:Vector.<Array> = null;
         var _loc29_:Array = null;
         var _loc30_:String = null;
         var _loc31_:String = null;
         var _loc32_:Array = null;
         var _loc33_:String = null;
         var _loc34_:String = null;
         var _loc35_:Array = null;
         var _loc36_:uint = 0;
         var _loc37_:Array = null;
         var _loc38_:uint = 0;
         var _loc39_:uint = 0;
         var _loc40_:String = null;
         var _loc41_:uint = 0;
         var _loc42_:GfxType = null;
         var _loc43_:Vector.<GfxType> = null;
         var _loc44_:GfxType = null;
         var _loc45_:Vector.<GfxType> = null;
         var _loc46_:GfxType = null;
         var _loc47_:Vector.<GfxType> = null;
         var _loc48_:Array = null;
         var _loc49_:Number = NaN;
         var _loc50_:Array = null;
         var _loc51_:uint = 0;
         var _loc52_:Array = null;
         var _loc53_:Array = null;
         var _loc54_:int = 0;
         var _loc55_:GfxType = null;
         var _loc56_:String = null;
         var _loc57_:String = null;
         var _loc58_:uint = 0;
         var _loc3_:PowerType = new PowerType();
         _loc3_.powerName = param1.attribute("PowerName");
         _loc3_.var_2956 = param2;
         for each(_loc4_ in param1.*)
         {
            if((_loc6_ = String(_loc4_.name().toString())) == "PowerID")
            {
               _loc3_.powerID = uint(_loc4_);
            }
            else if(_loc6_ == "FireAnimSource")
            {
               _loc3_.var_318 = method_210(_loc4_.toString());
            }
            else if(_loc6_ == "HitAnimSource")
            {
               _loc3_.var_2605 = method_210(_loc4_.toString());
            }
            else if(_loc6_ == "DisplayName")
            {
               _loc3_.displayName = _loc4_.toString();
            }
            else if(_loc6_ == "BasePowerName")
            {
               _loc3_.basePowerName = _loc4_.toString();
            }
            else if(_loc6_ == "IconName")
            {
               _loc3_.iconName = _loc4_.toString();
            }
            else if(_loc6_ == "Description")
            {
               _loc3_.description = _loc4_.toString();
            }
            else if(_loc6_ == "UpgradeDescription")
            {
               _loc3_.var_1499 = _loc4_.toString();
            }
            else if(_loc6_ == "FireSound")
            {
               _loc3_.var_1454 = _loc4_.toString();
            }
            else if(_loc6_ == "HitSound")
            {
               _loc3_.var_2103 = _loc4_.toString();
            }
            else if(_loc6_ == "ProjSound")
            {
               _loc3_.var_2347 = _loc4_.toString();
            }
            else if(_loc6_ == "DamageType")
            {
               _loc3_.var_402 = _loc4_.toString();
            }
            else if(_loc6_ == "CastImpulse")
            {
               _loc3_.var_1571 = int(_loc4_);
            }
            else if(_loc6_ == "Range")
            {
               _loc3_.var_1634 = uint(_loc4_);
            }
            else if(_loc6_ == "RecoverTime")
            {
               _loc3_.var_125 = uint(_loc4_);
            }
            else if(_loc6_ == "ShakeTime")
            {
               _loc3_.var_713 = uint(_loc4_);
            }
            else if(_loc6_ == "ReleaseTime")
            {
               _loc3_.var_653 = uint(_loc4_);
            }
            else if(_loc6_ == "CoolDownTime")
            {
               _loc3_.coolDownTime = uint(_loc4_);
            }
            else if(_loc6_ == "SpawnLimit")
            {
               _loc3_.var_1629 = uint(_loc4_);
            }
            else if(_loc6_ == "SpawnDuration")
            {
               _loc3_.var_1962 = uint(_loc4_);
            }
            else if(_loc6_ == "AggroBonus")
            {
               _loc3_.var_2327 = Number(_loc4_);
            }
            else if(_loc6_ == "ProcModifier")
            {
               _loc3_.var_1989 = Number(_loc4_);
            }
            else if(_loc6_ == "ComboName")
            {
               _loc3_.var_543 = _loc4_.toString();
            }
            else if(_loc6_ == "PowerGroup")
            {
               _loc3_.var_157 = _loc4_.toString();
            }
            else if(_loc6_ == "SwooshChange")
            {
               _loc3_.var_2346 = _loc4_.toString();
            }
            else if(_loc6_ == "ProcName")
            {
               _loc3_.var_2808 = _loc4_.toString();
            }
            else if(_loc6_ == "RuneIcon")
            {
               _loc3_.runeIcon = _loc4_.toString();
            }
            else if(_loc6_ == "FromMasterMana")
            {
               _loc3_.var_219 = MathUtil.method_50(_loc4_);
            }
            else if(_loc6_ == "ManaCost")
            {
               if((_loc8_ = (_loc7_ = _loc4_.toString()).split(",")).length > 1)
               {
                  _loc3_.var_1517 = uint(_loc8_[1]);
               }
               _loc3_.manaCost = uint(_loc8_[0]);
            }
            else if(_loc6_ == "ManaRequirement")
            {
               _loc9_ = uint(_loc4_);
               _loc3_.var_535 = _loc9_;
            }
            else if(_loc6_ == "CastAnimSource")
            {
               if((_loc11_ = (_loc10_ = _loc4_.toString()).split(":")).length > 1 && _loc11_[0] == "L")
               {
                  _loc10_ = String(_loc11_[1]);
                  _loc3_.var_2187 = true;
               }
               _loc11_ = _loc10_.split(",");
               _loc3_.var_457 = method_210(_loc11_[0]);
               if(_loc11_.length > 1 && _loc11_[1] == "Top")
               {
                  _loc3_.var_2888 = true;
               }
            }
            else if(_loc6_ == "AddTargetBuff")
            {
               if((_loc12_ = _loc4_.toString()).indexOf(":") >= 0)
               {
                  if(!_loc12_.indexOf("Random:"))
                  {
                     _loc3_.var_2414 = true;
                     _loc12_ = _loc12_.substr(7);
                  }
                  else if(!_loc12_.indexOf("First:"))
                  {
                     _loc3_.var_2369 = true;
                     _loc12_ = _loc12_.substr(6);
                  }
                  else if(!_loc12_.indexOf("Last:"))
                  {
                     _loc3_.var_2273 = true;
                     _loc12_ = _loc12_.substr(5);
                  }
                  else if(!_loc12_.indexOf("Sequence:"))
                  {
                     _loc3_.var_1759 = true;
                     _loc12_ = _loc12_.substr(9);
                  }
                  else if(!_loc12_.indexOf("FirstTarget:"))
                  {
                     _loc3_.var_2451 = true;
                     _loc12_ = _loc12_.substr(12);
                  }
               }
               _loc3_.var_381 = new Vector.<String>();
               _loc13_ = _loc12_.toString().split(",");
               for each(_loc14_ in _loc13_)
               {
                  _loc3_.var_381.push(_loc14_);
               }
               _loc3_.var_381.fixed = true;
            }
            else if(_loc6_ == "AddSelfBuff")
            {
               if(!(_loc15_ = _loc4_.toString()).indexOf("First:"))
               {
                  _loc3_.var_1682 = true;
                  _loc15_ = _loc15_.substr(6);
               }
               else if(!_loc15_.indexOf("OnDamage:"))
               {
                  _loc3_.var_2063 = true;
                  _loc15_ = _loc15_.substr(9);
               }
               _loc3_.var_437 = new Vector.<String>();
               _loc16_ = _loc15_.toString().split(",");
               for each(_loc17_ in _loc16_)
               {
                  _loc3_.var_437.push(_loc17_);
               }
               _loc3_.var_437.fixed = true;
            }
            else if(_loc6_ == "AoERadius")
            {
               if((_loc19_ = (_loc18_ = _loc4_.toString()).split(",")).length <= 1)
               {
                  _loc3_.aoeRadius = uint(_loc18_);
               }
               else
               {
                  _loc20_ = new Vector.<uint>();
                  for each(_loc21_ in _loc19_)
                  {
                     _loc20_.push(uint(_loc21_));
                  }
                  _loc20_.fixed = true;
                  _loc3_.aoeRadius = _loc20_[0];
                  _loc3_.var_375 = _loc20_;
               }
            }
            else if(_loc6_ == "MissileVelocityX")
            {
               _loc22_ = _loc4_.toString().split(",");
               _loc23_ = new Vector.<int>();
               if(_loc22_.length <= 1)
               {
                  _loc3_.var_1668 = int(_loc4_.toString());
               }
               else
               {
                  for each(_loc24_ in _loc22_)
                  {
                     _loc23_.push(int(_loc24_));
                  }
                  _loc23_.fixed = true;
                  _loc3_.var_1668 = _loc23_[0];
                  _loc3_.var_1591 = _loc23_;
               }
            }
            else if(_loc6_ == "MissileVelocityY")
            {
               _loc25_ = _loc4_.toString().split(",");
               _loc26_ = new Vector.<int>();
               if(_loc25_.length <= 1)
               {
                  _loc3_.var_1743 = int(_loc4_.toString());
               }
               else
               {
                  for each(_loc27_ in _loc25_)
                  {
                     _loc26_.push(int(_loc27_));
                  }
                  _loc26_.fixed = true;
                  _loc3_.var_1743 = _loc26_[0];
                  _loc3_.var_1474 = _loc26_;
               }
            }
            else if(_loc6_ == "SpawnedMonsters")
            {
               _loc28_ = new Vector.<Array>();
               _loc29_ = _loc4_.toString().split("|");
               for each(_loc30_ in _loc29_)
               {
                  _loc28_.push(_loc30_.split(","));
               }
               _loc28_.fixed = true;
               _loc3_.var_851 = _loc28_;
            }
            else if(_loc6_ == "CastAnim")
            {
               if((_loc32_ = (_loc31_ = _loc4_.toString()).split(":")).length > 1 && _loc32_[0] == "L")
               {
                  _loc31_ = String(_loc32_[1]);
                  _loc3_.var_801 = true;
               }
               _loc32_ = _loc31_.split(",");
               _loc3_.var_136 = _loc32_[0];
               if(_loc32_.length > 1)
               {
                  _loc3_.var_2130 = _loc32_[1];
               }
            }
            else if(_loc6_ == "TargetMethod")
            {
               if((_loc33_ = _loc4_.toString()) == "Melee")
               {
                  _loc3_.var_6 = TARGETMETHOD_MELEE;
               }
               else if(_loc33_ == "Ranged")
               {
                  _loc3_.var_6 = TARGETMETHOD_RANGED;
               }
               else if(_loc33_ == "Piercing")
               {
                  _loc3_.var_6 = TARGETMETHOD_PIERCING;
               }
               else if(_loc33_ == "PBAoE")
               {
                  _loc3_.var_6 = TARGETMETHOD_PBAOE;
               }
               else if(_loc33_ == "Self")
               {
                  _loc3_.var_6 = TARGETMETHOD_SELF;
               }
               else if(_loc33_ == "Friend")
               {
                  _loc3_.var_6 = TARGETMETHOD_FRIEND;
               }
               else if(_loc33_ == "Group")
               {
                  _loc3_.var_6 = TARGETMETHOD_GROUP;
               }
               else if(_loc33_ == "GroupAndSelf")
               {
                  _loc3_.var_6 = TARGETMETHOD_GROUPANDSELF;
               }
               else if(_loc33_ == "RangedAoE")
               {
                  _loc3_.var_6 = TARGETMETHOD_RANGEDAOE;
               }
               else if(_loc33_ == "Wave")
               {
                  _loc3_.var_6 = const_99;
               }
               else if(_loc33_ == "Charge")
               {
                  _loc3_.var_6 = const_32;
               }
               else if(_loc33_ == "Mouse")
               {
                  _loc3_.var_6 = const_275;
               }
               else if(_loc33_ == "MouseFeetEveryone")
               {
                  _loc3_.var_6 = const_232;
               }
               else if(_loc33_ == "Blast")
               {
                  _loc3_.var_6 = const_130;
               }
               else if(_loc33_ == "Cleave")
               {
                  _loc3_.var_6 = const_46;
               }
               else if(_loc33_ == "Nova")
               {
                  _loc3_.var_6 = const_111;
               }
               else if(_loc33_ == "Beam")
               {
                  _loc3_.var_6 = const_201;
               }
               else if(_loc33_ == "GroupPet")
               {
                  _loc3_.var_6 = const_424;
               }
               else if(_loc33_ == "Drain")
               {
                  _loc3_.var_6 = const_304;
               }
               else if(_loc33_ == "Pillar")
               {
                  _loc3_.var_6 = const_113;
               }
               else if(_loc33_ == "Other")
               {
                  _loc3_.var_6 = const_921;
               }
               else if(_loc33_ == "Parallel")
               {
                  _loc3_.var_6 = const_568;
               }
               else if(_loc33_ == "RangedStrike")
               {
                  _loc3_.var_6 = const_89;
               }
               else if(_loc33_ == "GroupAndSummoner")
               {
                  _loc3_.var_6 = const_517;
               }
               else if(_loc33_ == "Aura")
               {
                  _loc3_.var_6 = const_248;
               }
               else if(_loc33_ == "AuraFriend")
               {
                  _loc3_.var_6 = const_259;
               }
               else if(_loc33_ == "RangedAoEFriend")
               {
                  _loc3_.var_6 = const_96;
               }
               else if(_loc33_ == "Summoner")
               {
                  _loc3_.var_6 = const_473;
               }
               else if(_loc33_ == "UndeadPet")
               {
                  _loc3_.var_6 = const_698;
               }
               else if(_loc33_ == "LobbedAoE")
               {
                  _loc3_.var_6 = TARGETMETHOD_RANGEDAOE;
                  _loc3_.var_1612 = const_537;
               }
               else if(_loc33_ == "LobbedMonster")
               {
                  _loc3_.var_6 = TARGETMETHOD_RANGEDAOE;
                  _loc3_.var_1612 = const_537;
                  _loc3_.var_275 = true;
               }
               else if(_loc33_ == "RangedAoEEveryone")
               {
                  _loc3_.var_6 = TARGETMETHOD_RANGEDAOE;
                  _loc3_.var_1867 = true;
                  _loc3_.var_1759 = true;
               }
               else if(_loc33_ == "AuraEveryone")
               {
                  _loc3_.var_6 = const_248;
                  _loc3_.var_1867 = true;
                  _loc3_.var_1759 = true;
                  _loc3_.var_1735 = true;
               }
               else if(_loc33_ == "Mount")
               {
                  _loc3_.var_6 = TARGETMETHOD_SELF;
                  _loc3_.var_1439 = true;
               }
               else if(_loc33_ == "Pet")
               {
                  _loc3_.var_6 = TARGETMETHOD_SELF;
                  _loc3_.var_749 = true;
               }
               else if(_loc33_ == "MeleeCombo")
               {
                  _loc3_.var_6 = TARGETMETHOD_MELEE;
                  _loc3_.var_1075 = 2;
               }
               else if(_loc33_ == "MeleePunch")
               {
                  _loc3_.var_6 = TARGETMETHOD_MELEE;
                  _loc3_.var_1075 = 1;
               }
               else if(_loc33_ == "Projectile")
               {
                  _loc3_.var_6 = TARGETMETHOD_PROJECTILE;
                  _loc3_.var_275 = true;
               }
               else if(_loc33_ == "ProjectilePlayer")
               {
                  _loc3_.var_6 = TARGETMETHOD_PROJECTILE;
               }
               else if(_loc33_ == "ProjectileCombo")
               {
                  _loc3_.var_6 = TARGETMETHOD_PROJECTILE;
                  _loc3_.var_1212 = 2;
                  _loc3_.var_1801 = true;
               }
               else if(_loc33_ == "VanityPet")
               {
                  _loc3_.var_6 = const_473;
                  _loc3_.var_2513 = true;
               }
               else
               {
                  class_24.method_7("Unknown Target Method Name:" + _loc33_);
               }
            }
            else if(_loc6_ == "CastSound")
            {
               if(_loc34_ = _loc4_.toString())
               {
                  _loc36_ = 0;
                  _loc38_ = (_loc37_ = _loc34_.split("]").join("[").split("[")).length;
                  _loc39_ = 0;
                  while(_loc39_ < _loc38_)
                  {
                     if(_loc40_ = String(_loc37_[_loc39_]))
                     {
                        if(_loc41_ = uint(_loc40_))
                        {
                           _loc36_ += _loc41_;
                        }
                        else if(_loc40_.indexOf("$") == -1)
                        {
                           _loc3_.var_1169.push(new class_43(_loc40_,null,_loc36_));
                        }
                        else
                        {
                           _loc35_ = _loc40_.split("$");
                           _loc3_.var_1169.push(new class_43(_loc35_.join(""),_loc35_.join("_female"),_loc36_));
                        }
                     }
                     _loc39_++;
                  }
               }
            }
            else if(_loc6_ == "CastGfx")
            {
               if(_loc42_ = GfxType.method_53(_loc4_,null))
               {
                  if(_loc43_ = GfxType.method_321(_loc42_,_loc4_))
                  {
                     _loc3_.var_942 = _loc43_;
                  }
                  else
                  {
                     _loc3_.var_942 = new Vector.<GfxType>(1,true);
                     _loc3_.var_942[0] = _loc42_;
                     _loc3_.var_2321 = GfxType.method_368(_loc42_,_loc4_);
                  }
                  _loc3_.var_1653 = _loc3_.var_942[0];
               }
            }
            else if(_loc6_ == "ProjGfx")
            {
               _loc3_.var_625 = GfxType.method_53(_loc4_,null);
               if(_loc3_.var_625)
               {
                  _loc3_.var_1418 = GfxType.method_1733(_loc3_.var_625,_loc4_);
               }
            }
            else if(_loc6_ == "HitGfx")
            {
               if(_loc44_ = GfxType.method_53(_loc4_,null))
               {
                  if(_loc45_ = GfxType.method_321(_loc44_,_loc4_))
                  {
                     _loc3_.var_1232 = _loc45_;
                  }
                  else if(_loc45_ = GfxType.method_1518(_loc44_,_loc4_))
                  {
                     _loc3_.var_1700 = _loc45_;
                  }
                  else
                  {
                     _loc3_.var_1232 = new Vector.<GfxType>(1,true);
                     _loc3_.var_1232[0] = _loc44_;
                  }
               }
            }
            else if(_loc6_ == "FireGfx")
            {
               if(_loc46_ = GfxType.method_53(_loc4_,null))
               {
                  if(_loc47_ = GfxType.method_321(_loc46_,_loc4_))
                  {
                     _loc3_.var_352 = _loc47_;
                  }
                  else
                  {
                     _loc3_.var_352 = new Vector.<GfxType>(1,true);
                     _loc3_.var_352[0] = _loc46_;
                     _loc3_.var_2204 = GfxType.method_368(_loc46_,_loc4_);
                  }
               }
            }
            else if(_loc6_ == "BaseDamageMult")
            {
               _loc48_ = _loc4_.toString().split(",");
               for each(_loc49_ in _loc48_)
               {
                  _loc3_.var_630.push(_loc49_);
                  _loc3_.damageMultFull += _loc49_;
               }
               _loc3_.var_630.fixed = true;
            }
            else if(_loc6_ == "CastTime")
            {
               _loc50_ = _loc4_.toString().split(",");
               for each(_loc51_ in _loc50_)
               {
                  _loc3_.var_108.push(_loc51_);
                  _loc3_.var_287 += _loc51_;
               }
               _loc3_.var_108.fixed = true;
            }
            else if(_loc6_ == "CenterOffset")
            {
               _loc52_ = _loc4_.toString().split(",");
               _loc3_.var_507 = int(_loc52_[0]);
               if(_loc52_.length > 1)
               {
                  _loc3_.var_127 = int(_loc52_[1]);
               }
            }
            else if(_loc6_ == "FireImpulse")
            {
               if(!_loc3_.var_820)
               {
                  _loc3_.var_820 = new Vector.<int>();
               }
               _loc53_ = _loc4_.toString().split(",");
               for each(_loc54_ in _loc53_)
               {
                  _loc3_.var_820.push(_loc54_);
               }
               _loc3_.var_820.fixed = true;
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc3_.powerName + ": " + _loc6_);
            }
         }
         if(_loc3_.var_625)
         {
            _loc3_.var_625.var_527 = true;
            if(_loc3_.var_1418)
            {
               _loc3_.var_1418.var_527 = true;
            }
            if(_loc3_.var_352)
            {
               for each(_loc55_ in _loc3_.var_352)
               {
                  _loc55_.var_527 = true;
               }
            }
         }
         if(!_loc3_.var_535)
         {
            _loc3_.var_535 = _loc3_.manaCost;
         }
         _loc3_.var_1169.fixed = true;
         if(!_loc3_.var_108.length)
         {
            _loc3_.var_108.push(0);
            _loc3_.var_108.fixed = true;
         }
         if(!_loc3_.var_630.length)
         {
            _loc3_.var_630.push(0);
            _loc3_.var_630.fixed = true;
         }
         _loc3_.var_301 = !_loc3_.powerName.indexOf("Proc");
         _loc3_.bIsProjectile = _loc3_.var_1612 || _loc3_.var_6 == TARGETMETHOD_PROJECTILE || _loc3_.var_6 == const_568 || _loc3_.powerName.indexOf("WildFire") == 0 || _loc3_.powerName.indexOf("DaggerFlurry") == 0 || _loc3_.powerName.indexOf("DarkChi") == 0 || _loc3_.powerName.indexOf("FlameAxe") == 0 || _loc3_.powerName.indexOf("PetDragonRed") == 0;
         _loc3_.var_1735 = _loc3_.var_6 == TARGETMETHOD_RANGED || _loc3_.var_6 == TARGETMETHOD_SELF || _loc3_.var_6 == TARGETMETHOD_FRIEND || _loc3_.var_6 == const_304;
         _loc3_.var_2846 = _loc3_.bIsProjectile || _loc3_.var_6 == TARGETMETHOD_PIERCING || _loc3_.var_6 == TARGETMETHOD_RANGEDAOE || _loc3_.var_6 == const_275 || _loc3_.var_6 == const_32 || _loc3_.var_6 == const_201 || _loc3_.var_6 == const_232 || _loc3_.var_6 == const_89 || _loc3_.var_6 == const_96 || _loc3_.powerName.indexOf("FlameSpout") == 0 || _loc3_.powerName.indexOf("MoltenFist") == 0;
         _loc3_.var_1427 = _loc3_.var_6 == TARGETMETHOD_RANGEDAOE || _loc3_.var_6 == const_275 || _loc3_.var_6 == const_89 || _loc3_.var_6 == const_96;
         _loc3_.var_2786 = _loc3_.var_6 == const_99;
         _loc3_.var_2486 = _loc3_.var_6 == const_46 || _loc3_.var_6 == const_130;
         _loc3_.var_1789 = _loc3_.var_6 == const_99 || _loc3_.var_6 == const_130 || _loc3_.var_6 == const_46 || _loc3_.var_6 == const_111 || _loc3_.var_6 == const_32 || _loc3_.var_6 == const_113;
         _loc3_.var_2042 = _loc3_.var_6 == const_130 || _loc3_.var_6 == const_111 || _loc3_.var_6 == const_113;
         _loc3_.var_2511 = _loc3_.var_318 == ANIMSOURCE_TARGETFEET || _loc3_.var_318 == const_293 || _loc3_.var_318 == ANIMSOURCE_TARGETCENTER || _loc3_.var_457 == const_219;
         if(_loc3_.var_301)
         {
            if((_loc56_ = _loc3_.powerName) == "ProcFire")
            {
               _loc3_.var_879 = true;
               _loc3_.var_470 = true;
            }
            else if(_loc56_ == "ProcIce")
            {
               _loc3_.var_879 = true;
               _loc3_.var_470 = true;
            }
            else if(_loc56_ == "ProcDeath")
            {
               _loc3_.var_879 = true;
               _loc3_.var_470 = true;
            }
            else if(_loc56_ == "ProcLife")
            {
               _loc3_.var_879 = true;
               _loc3_.var_470 = true;
            }
            else if(_loc56_ == "ProcEarth")
            {
               _loc3_.var_879 = true;
               _loc3_.var_470 = true;
            }
            else if(_loc56_ == "ProcAir")
            {
               _loc3_.var_879 = true;
               _loc3_.var_470 = true;
            }
            else if(_loc56_ == "ProcHeal")
            {
               _loc3_.var_2323 = true;
               _loc3_.var_470 = true;
            }
            else if(_loc56_ == "ProcHealTime")
            {
               _loc3_.var_2323 = true;
               _loc3_.var_470 = true;
            }
            else if(_loc56_ == "ProcMassive")
            {
               _loc3_.var_470 = true;
            }
            else if(_loc56_ == "ProcMassiveTime")
            {
               _loc3_.var_470 = true;
            }
         }
         var _loc5_:String = _loc3_.powerName;
         if(!_loc3_.basePowerName)
         {
            _loc3_.basePowerName = _loc3_.powerName;
         }
         else
         {
            if(_loc3_.powerName.lastIndexOf("10") > 0)
            {
               _loc3_.var_7 = 10;
               _loc57_ = _loc5_.substr(0,_loc5_.length - 2);
            }
            else
            {
               _loc3_.var_7 = int(_loc5_.substr(_loc5_.length - 1));
               if(_loc3_.var_7)
               {
                  _loc57_ = _loc5_.substr(0,_loc5_.length - 1);
               }
               else
               {
                  _loc57_ = _loc3_.powerName;
               }
            }
            if(_loc57_ != _loc3_.basePowerName)
            {
               class_24.method_7("Power " + _loc3_.powerName + " has a BasePowerName that doesn\'t match the format \'Powername + Powerlevel\'");
            }
         }
         if(_loc3_.basePowerName == "Warcry")
         {
            _loc3_.var_2049 = true;
         }
         if(_loc3_.basePowerName == "JumpSlam")
         {
            _loc3_.var_2049 = true;
            _loc3_.var_1427 = true;
         }
         if(!_loc3_.powerName.indexOf("PitLordSmash"))
         {
            _loc3_.var_1427 = true;
         }
         if(_loc3_.powerName == "DragonPounce" || _loc3_.powerName == "GriffonPounce")
         {
            _loc3_.var_1600 = true;
         }
         if(!_loc3_.powerName.indexOf("WyrmPounce"))
         {
            _loc3_.var_1600 = true;
         }
         if(_loc3_.powerName == "DragonTripleShot" || _loc3_.powerName == "DragonMeteorShot")
         {
            _loc3_.var_2674 = true;
            _loc3_.var_1600 = true;
         }
         if(_loc3_.powerName == "HumanCyclone" || _loc3_.powerName == "DogCyclone" || _loc3_.powerName == "DemonCyclone")
         {
            _loc3_.var_1600 = true;
         }
         if(!_loc3_.powerName.indexOf("VigilLightningFront"))
         {
            _loc3_.var_2042 = true;
         }
         if(_loc3_.powerName == "EmberExplosion" || _loc3_.powerName == "GoblinCannonballExplode" || _loc3_.powerName == "KillSelfInternal" || _loc3_.powerName == "Detonate" || _loc3_.powerName == "GoblinCannonballProxy")
         {
            _loc3_.var_2475 = true;
         }
         if(!_loc3_.var_2513 && !_loc3_.basePowerName.indexOf("Pet"))
         {
            if(!_loc3_.basePowerName.indexOf("PetDjinn"))
            {
               _loc3_.var_2793 = true;
            }
            else if(!_loc3_.basePowerName.indexOf("PetSprite") || !_loc3_.basePowerName.indexOf("PetPhoenix") || !_loc3_.basePowerName.indexOf("PetDragonBone") || !_loc3_.basePowerName.indexOf("PetCrow"))
            {
               _loc3_.var_2616 = true;
            }
            else
            {
               _loc3_.var_2553 = true;
            }
         }
         if(_loc3_.basePowerName == "PermafrostClone")
         {
            _loc3_.var_2629 = true;
         }
         if(_loc3_.basePowerName == "PermafrostClone" || _loc3_.basePowerName == "PolarSentry" || _loc3_.basePowerName == "HailstoneEmbrace" || _loc3_.basePowerName == "EndFrostArmor" || _loc3_.basePowerName == "FrostArmorMelee" || _loc3_.basePowerName == "FrostArmorRanged" || _loc3_.basePowerName == "ShadowBlade" || _loc3_.basePowerName == "SeekingBlades" || _loc3_.basePowerName == "EndSeekingBlades" || _loc3_.basePowerName == "MistWalk" || _loc3_.basePowerName == "Defiance" || _loc3_.basePowerName == "Barrier" || _loc3_.basePowerName == "SentinelForm" || _loc3_.basePowerName == "EndSentinelForm" || _loc3_.basePowerName == "SFMelee" || _loc3_.basePowerName == "SFMeleeCombo" || _loc3_.basePowerName == "SFRanged" || _loc3_.basePowerName == "Flamethrower" || _loc3_.basePowerName == "FlamethrowerROR" || _loc3_.basePowerName == "Pyromania" || _loc3_.basePowerName == "EndPyromania" || _loc3_.basePowerName == "SummonDragonSoul" || _loc3_.basePowerName == "WildFire" || _loc3_.basePowerName == "SoulReaver" || _loc3_.basePowerName == "GhostBlade" || _loc3_.basePowerName == "SoulShatter" || _loc3_.basePowerName == "ShadowLegion" || _loc3_.basePowerName == "ShadowArmor" || _loc3_.basePowerName == "ShadowStep" || _loc3_.basePowerName == "ShadowStepClose" || _loc3_.basePowerName == "SummonGhoul" || _loc3_.basePowerName == "PlagueBattalion" || _loc3_.basePowerName == "SummonRangedGhoul" || _loc3_.basePowerName == "Sanctum" || _loc3_.basePowerName == "SanctumCombo" || _loc3_.basePowerName == "CleansingLight" || _loc3_.basePowerName == "LeoneanAura" || _loc3_.basePowerName == "LeapStrike" || _loc3_.basePowerName == "Berserker" || _loc3_.basePowerName == "Sacrifice" || _loc3_.basePowerName == "LightningBomb")
         {
            if(!_loc3_.var_219)
            {
               class_24.method_7("Does not match internal validation list of Master Mana powers, should be true: " + _loc3_.basePowerName + ". Check that BasePowerName is set in Excel file.");
            }
         }
         else if(_loc3_.var_219)
         {
            class_24.method_7("Does not match internal validation list of Master Mana powers, should be false: " + _loc3_.basePowerName + ". Check that BasePowerName is set in Excel file.");
         }
         if(_loc3_.basePowerName == "FlamethrowerROR")
         {
            _loc3_.var_2690 = true;
         }
         if(_loc3_.basePowerName == "FlameFieldTrail")
         {
            _loc3_.var_2510 = true;
         }
         if(_loc3_.basePowerName == "DragonSoulShot")
         {
            _loc3_.var_1801 = false;
         }
         if(_loc3_.basePowerName == "FlameSpout")
         {
            _loc3_.var_1789 = false;
         }
         if(_loc3_.basePowerName == "IceSpike")
         {
            _loc3_.var_1682 = true;
            _loc3_.var_93 = "RuneIceSpike";
         }
         if(_loc3_.basePowerName == "MistWalkClose")
         {
            if(_loc3_.var_7 >= 10)
            {
               _loc3_.var_93 = "DashArmor75";
            }
            else if(_loc3_.var_7 >= 9)
            {
               _loc3_.var_93 = "DashArmor65";
            }
            else if(_loc3_.var_7 >= 7)
            {
               _loc3_.var_93 = "DashArmor60";
            }
            else if(_loc3_.var_7 >= 4)
            {
               _loc3_.var_93 = "DashArmor55";
            }
            else
            {
               _loc3_.var_93 = "DashArmor50";
            }
         }
         if(_loc3_.basePowerName == "Cleave")
         {
            if(_loc3_.var_7 >= 10)
            {
               _loc3_.var_93 = "Phalanx";
            }
            else if(_loc3_.var_7 >= 9)
            {
               _loc3_.var_93 = "Phalanx35";
            }
            else if(_loc3_.var_7 >= 5)
            {
               _loc3_.var_93 = "Phalanx25";
            }
            else
            {
               _loc3_.var_93 = "DashArmor50";
            }
         }
         if(_loc3_.basePowerName == "SteelCyclone")
         {
            if(_loc3_.var_7 >= 9)
            {
               _loc3_.var_93 = "DashArmor50";
            }
            else if(_loc3_.var_7 >= 6)
            {
               _loc3_.var_93 = "DashArmor25";
            }
         }
         if(_loc3_.basePowerName == "JuggernautCharge")
         {
            if(_loc3_.var_7 >= 4)
            {
               _loc3_.var_93 = "SentinelArmor";
            }
            else
            {
               _loc3_.var_93 = "Phalanx";
            }
         }
         if(_loc3_.basePowerName == "Shockwave")
         {
            _loc3_.var_93 = "SentinelArmor";
         }
         if(_loc3_.basePowerName == "ShieldFlurryStrike")
         {
            _loc3_.var_93 = "Phalanx";
         }
         if(_loc3_.basePowerName == "VitalStrike")
         {
            if(_loc3_.var_7 >= 10)
            {
               _loc3_.var_93 = "DashArmor60";
            }
            else if(_loc3_.var_7 >= 5)
            {
               _loc3_.var_93 = "DashArmor45";
            }
            else if(_loc3_.var_7 >= 3)
            {
               _loc3_.var_93 = "DashArmor25";
            }
         }
         if(_loc3_.basePowerName == "Assassinate")
         {
            if(_loc3_.var_7 >= 10)
            {
               _loc3_.var_93 = "DashArmor60";
            }
            else if(_loc3_.var_7 >= 7)
            {
               _loc3_.var_93 = "DashArmor45";
            }
            else if(_loc3_.var_7 >= 4)
            {
               _loc3_.var_93 = "DashArmor25";
            }
         }
         if(_loc3_.basePowerName == "PoisonLance")
         {
            if(_loc3_.var_7 >= 10)
            {
               _loc3_.var_93 = "DashArmor50";
            }
            else if(_loc3_.var_7 >= 8)
            {
               _loc3_.var_93 = "DashArmor25";
            }
            else if(_loc3_.var_7 >= 4)
            {
               _loc3_.var_93 = "DashArmor10";
            }
         }
         if(_loc3_.basePowerName == "FlameStrike")
         {
            _loc3_.var_1551 = true;
            _loc3_.var_1774 = "FireFieldTrail";
            if(_loc3_.var_7)
            {
               _loc3_.var_1774 += _loc3_.var_7;
            }
         }
         if(_loc3_.basePowerName == "GhostBlade")
         {
            if(_loc3_.var_7 >= 10)
            {
               _loc3_.var_698 = "GhostBlade10";
            }
            else if(_loc3_.var_7 >= 9)
            {
               _loc3_.var_698 = "GhostBlade9";
            }
            else if(_loc3_.var_7 >= 7)
            {
               _loc3_.var_698 = "GhostBlade7";
            }
            else if(_loc3_.var_7 >= 6)
            {
               _loc3_.var_698 = "GhostBlade6";
            }
            else if(_loc3_.var_7 >= 4)
            {
               _loc3_.var_698 = "GhostBlade4";
            }
            else
            {
               _loc3_.var_698 = "GhostBlade1";
            }
         }
         if(_loc3_.basePowerName == "SoulReaver")
         {
            _loc3_.var_698 = "SoulReaverSelf" + _loc3_.var_7;
         }
         if(_loc3_.basePowerName == "CelestialLanceCombo" || _loc3_.basePowerName == "DivineWordCombo" || _loc3_.basePowerName == "SanctumCombo")
         {
            _loc3_.var_2770 = true;
         }
         if(_loc3_.basePowerName == "CelestialLance")
         {
            _loc3_.var_2520 = true;
         }
         if(_loc3_.basePowerName == "ProcCriticalHit")
         {
            _loc3_.var_2554 = true;
         }
         if(_loc3_.basePowerName == "ProcDevour" || _loc3_.basePowerName == "ProcAlways75PctHeal" || _loc3_.basePowerName == "ProcLifethirstSelf")
         {
            _loc3_.var_2426 = true;
         }
         if(_loc3_.basePowerName == "ProcHealSummoner")
         {
            _loc3_.var_2426 = true;
            _loc3_.var_2586 = true;
         }
         if(_loc3_.var_301 || _loc3_.basePowerName == "FireFieldTrail" || _loc3_.basePowerName == "HailstoneEmbrace" || _loc3_.basePowerName == "GrantFrostArmor" || _loc3_.basePowerName == "EndFrostArmor" || _loc3_.basePowerName == "HailstonePulse" || _loc3_.basePowerName == "EndSeekingBlades" || _loc3_.basePowerName == "EndSentinelForm" || _loc3_.basePowerName == "EndPyromania" || _loc3_.basePowerName == "PolarSentry" || _loc3_.basePowerName == "Assassinate" || _loc3_.basePowerName == "FrostArmorIce" || _loc3_.basePowerName == "ShadowTendril" || _loc3_.basePowerName == "ShadowLegion" || _loc3_.basePowerName == "FrostArmorRanged" || _loc3_.basePowerName == "LightningBombExplode" || _loc3_.basePowerName == "LightningBombExplodeTwo" || _loc3_.basePowerName == "CelestialLanceCombo" || _loc3_.basePowerName == "ShadowStep" || _loc3_.basePowerName == "DetShieldDetonate" || _loc3_.basePowerName == "LeapStrike" || _loc3_.basePowerName == "Fury" || _loc3_.basePowerName == "PainEater" || _loc3_.basePowerName == "FireShield" || _loc3_.basePowerName == "Heroism" || _loc3_.basePowerName == "Vigor" || _loc3_.basePowerName == "Blaze" || _loc3_.basePowerName == "InfestationSpawn" || _loc3_.basePowerName == "InfestationSpawnKing" || _loc3_.basePowerName == "VerdictROR" || _loc3_.basePowerName == "VerdictHeal" || _loc3_.basePowerName == "VerdictHealMelee" || _loc3_.basePowerName == "FountainOfLifeCombo" || _loc3_.basePowerName == "DivineWord" || _loc3_.basePowerName == "SummonGhoul" || _loc3_.basePowerName == "SummonRangedGhoul" || _loc3_.basePowerName == "PlagueBattalion")
         {
            _loc3_.var_1689 = true;
         }
         if(const_784.indexOf(_loc3_.basePowerName) != -1)
         {
            _loc3_.var_275 = true;
         }
         if(_loc3_.var_275 && _loc3_.damageMultFull <= 0)
         {
            class_24.method_7("Challenge power must deal positive damage: " + _loc3_.powerName);
         }
         if(_loc3_.var_1989 > 1)
         {
            _loc3_.var_1989 = 1;
         }
         _loc3_.var_347 = _loc3_.powerName;
         if(_loc3_.basePowerName == "LeapStrike" || _loc3_.basePowerName == "ShieldFlurry" || _loc3_.basePowerName == "Juggernaut" || _loc3_.basePowerName == "MistWalk" || _loc3_.basePowerName == "Assassinate" || _loc3_.basePowerName == "SeekingBlades" || _loc3_.basePowerName == "ShadowStep")
         {
            _loc3_.var_347 = _loc3_.var_543;
         }
         if(_loc3_.basePowerName == "CleavingBlows")
         {
            _loc3_.var_347 = _loc3_.var_437[0];
         }
         if(_loc3_.basePowerName == "Meteor")
         {
            _loc3_.var_347 = _loc3_.var_381[0];
         }
         if(_loc3_.basePowerName == "PermafrostClone")
         {
            _loc58_ = uint(_loc3_.powerName.substr(_loc3_.basePowerName.length));
            _loc3_.var_347 = "PermafrostCloneExplode" + _loc58_;
         }
         if(_loc3_.basePowerName == "SummonDragonSoul")
         {
            _loc58_ = uint(_loc3_.powerName.substr(_loc3_.basePowerName.length));
            _loc3_.var_347 = "DragonSoulShot" + _loc58_;
         }
         if(_loc3_.basePowerName == "Decoy")
         {
            _loc58_ = uint(_loc3_.powerName.substr(_loc3_.basePowerName.length));
            _loc3_.var_347 = "DecoyExplode" + _loc58_;
         }
         if(_loc3_.basePowerName == "Verdict")
         {
            _loc58_ = uint(_loc3_.powerName.substr(_loc3_.basePowerName.length));
            _loc3_.var_347 = "VerdictROR" + _loc58_;
         }
         if(_loc3_.basePowerName == "FountainOfLife")
         {
            _loc58_ = uint(_loc3_.powerName.substr(_loc3_.basePowerName.length));
            _loc3_.var_347 = "FountainOfLifeCombo" + _loc58_;
         }
         if(_loc3_.basePowerName == "Pyromania")
         {
            _loc58_ = uint(_loc3_.powerName.substr(_loc3_.basePowerName.length));
            _loc3_.var_347 = "FlamethrowerROR" + _loc58_;
         }
         return _loc3_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary, param4:Boolean) : void
      {
         var _loc5_:XML = null;
         var _loc6_:PowerType = null;
         for each(_loc5_ in param1.*)
         {
            if((_loc6_ = method_771(_loc5_,param4)).powerID)
            {
               if(param3[_loc6_.powerName])
               {
                  class_24.method_7("Multiple powers with name: " + _loc6_.powerName);
               }
               if(param2[_loc6_.powerID])
               {
                  class_24.method_7("Multiple powers with ID: " + _loc6_.powerID);
               }
               if(_loc6_.var_457 == ANIMSOURCE_TARGETFEET || _loc6_.var_457 == const_293 || _loc6_.var_457 == ANIMSOURCE_TARGETCENTER || _loc6_.var_457 == const_219)
               {
                  class_24.method_7("Power cast anim cannot source at the target: " + _loc6_.powerName);
               }
               if(Boolean(_loc6_.var_352) && !_loc6_.var_352[0].bFireAndForget)
               {
                  class_24.method_7("FireGfx must be FireAndForget: " + _loc6_.powerName);
               }
               if(Boolean(_loc6_.var_625) && _loc6_.var_625.bFireAndForget)
               {
                  class_24.method_7("ProjGfx cannot be FireAndForget: " + _loc6_.powerName);
               }
               if(_loc6_.var_6 == TARGETMETHOD_PROJECTILE && !_loc6_.var_625)
               {
                  class_24.method_7("Projectile must have ProjGfx: " + _loc6_.powerName);
               }
               if(Boolean(_loc6_.var_1212) && !_loc6_.var_1418)
               {
                  class_24.method_7("Ranged combo fireball must have a double version: " + _loc6_.powerName);
               }
               if(_loc6_.var_507 && _loc6_.var_6 != TARGETMETHOD_MELEE && _loc6_.var_6 != TARGETMETHOD_PBAOE && _loc6_.var_6 != const_130 && _loc6_.var_6 != const_46 && _loc6_.var_6 != const_111)
               {
                  class_24.method_7("CenterOffsetX not yet supported for that target type: " + _loc6_.powerName);
               }
               if(_loc6_.var_127 && _loc6_.var_6 != TARGETMETHOD_RANGEDAOE && _loc6_.var_6 != TARGETMETHOD_PBAOE && _loc6_.var_6 != const_275 && _loc6_.var_6 != const_99 && _loc6_.var_6 != const_130 && _loc6_.var_6 != const_111 && _loc6_.var_6 != const_232 && _loc6_.var_6 != const_89 && _loc6_.var_6 != const_96)
               {
                  class_24.method_7("CenterOffsetY not yet supported for that target type: " + _loc6_.powerName);
               }
               if((_loc6_.var_6 == const_111 || _loc6_.var_6 == const_113) && (!_loc6_.var_375 || _loc6_.var_375.length != _loc6_.var_108.length))
               {
                  class_24.method_7("Nova radius list must match the cast time list in length: " + _loc6_.powerName);
               }
               if(Boolean(_loc6_.var_851) && !_loc6_.var_1629)
               {
                  class_24.method_7("Powers with SpawnedMonsters must have a SpawnLimit: " + _loc6_.powerName);
               }
               if(_loc6_.var_301 && (Boolean(_loc6_.manaCost) || Boolean(_loc6_.var_287) || Boolean(_loc6_.var_125)))
               {
                  class_24.method_7("ProcPowers must not have a manaCost, castTime, or recoverTime: " + _loc6_.powerName);
               }
               if(_loc6_.var_6 != TARGETMETHOD_RANGEDAOE && _loc6_.var_6 != const_99 && _loc6_.var_457 == ANIMSOURCE_GROUND && _loc6_.var_6 != const_113 && _loc6_.var_6 != const_89 && _loc6_.var_6 != const_96)
               {
                  class_24.method_7("CastAnimSource can only be Ground with Wave or RangedAoE powers: " + _loc6_.powerName);
               }
               if(_loc6_.var_6 != TARGETMETHOD_RANGEDAOE && _loc6_.var_6 != const_99 && _loc6_.var_318 == ANIMSOURCE_GROUND && _loc6_.var_6 != const_113 && _loc6_.var_6 != const_89 && _loc6_.var_6 != const_96)
               {
                  class_24.method_7("FireAnimSource can only be Ground with Wave or RangedAoE powers: " + _loc6_.powerName);
               }
               if(_loc6_.var_275 && Boolean(_loc6_.var_437))
               {
                  class_24.method_7("ChallengePower cannot have a SelfBuff property: " + _loc6_.powerName);
               }
               if(_loc6_.var_275 && Boolean(_loc6_.var_851))
               {
                  class_24.method_7("ChallengePower cannot have SpawnedMonsters: " + _loc6_.powerName);
               }
               if(_loc6_.var_275 && Boolean(_loc6_.var_2808))
               {
                  class_24.method_7("ChallengePower cannot have a Proc attached: " + _loc6_.powerName);
               }
               if(_loc6_.manaCost >= Math.pow(2,const_423) && _loc6_.var_219)
               {
                  class_24.method_7("Power " + _loc6_.powerName + " cost more master mana than allocated. Increment MAXMANA_BITSTOSEND");
               }
               if(_loc6_.var_6 == const_89 && !_loc6_.aoeRadius)
               {
                  class_24.method_7("Power " + _loc6_.powerName + " needs a nonzero value as a single target melee radius in its AoE field");
               }
               param2[_loc6_.powerID] = _loc6_;
               param3[_loc6_.powerName] = _loc6_;
            }
         }
      }
      
      public static function method_432(param1:PowerType, param2:Entity) : Boolean
      {
         if(!param2)
         {
            return false;
         }
         return (param1 == param2.var_280 || param1 == param2.var_353) && !param2.var_99;
      }
      
      public function method_63(param1:Entity) : uint
      {
         var _loc2_:uint = 0;
         if(this.var_6 == TARGETMETHOD_MELEE || this.var_6 == const_32 || this.var_6 == const_46)
         {
            return Math.round(param1.entType.width * 0.5 + this.var_1634 * (1 + param1.totalMods.var_1492));
         }
         _loc2_ = !!this.var_1634 ? this.var_1634 : this.aoeRadius;
         return Math.round(_loc2_ * (1 + param1.totalMods.var_1492));
      }
      
      public function DrawDebugRange(param1:MovieClip, param2:Entity, param3:Point, param4:uint, param5:Entity = null) : void
      {
         var _loc6_:uint = this.method_63(param2);
         var _loc7_:int = param2.bFacingLeft() ? int(-this.var_507) : this.var_507;
         param1.graphics.clear();
         if(Boolean(this.var_1634) && Boolean(this.aoeRadius))
         {
            if(this.var_6 == TARGETMETHOD_MELEE || this.var_6 == const_32 || this.var_6 == const_46)
            {
               param1.graphics.beginFill(204,0.2);
               param1.graphics.drawRect(param2.appearPosX + _loc7_ + _loc6_,param2.appearPosY - param2.entType.height,this.aoeRadius,param2.entType.height);
               param1.graphics.endFill();
               param1.graphics.beginFill(204,0.2);
               param1.graphics.drawRect(param2.appearPosX + _loc7_ - _loc6_ - this.aoeRadius,param2.appearPosY - param2.entType.height,this.aoeRadius,param2.entType.height);
               param1.graphics.endFill();
            }
            else if(param5 && this.var_6 == const_248 || this.var_6 == const_259)
            {
               param1.graphics.beginFill(204,0.2);
               param1.graphics.drawRect(param5.var_10 - this.aoeRadius,param5.var_12 - this.aoeRadius,this.aoeRadius * 2,this.aoeRadius * 2);
               param1.graphics.endFill();
            }
            else
            {
               param1.graphics.beginFill(204,0.2);
               if(this.var_6 == const_232)
               {
                  param1.graphics.drawRect(param3.x - this.aoeRadius,param3.y + this.var_127,this.aoeRadius * 2,-this.var_127);
               }
               else
               {
                  param1.graphics.drawRect(param3.x - this.aoeRadius,param3.y - this.aoeRadius + this.var_127,this.aoeRadius * 2,this.aoeRadius * 2);
               }
               param1.graphics.endFill();
            }
         }
         var _loc8_:uint;
         var _loc9_:uint = !!(_loc8_ = param4 % 3) ? (_loc8_ == 2 ? 13421568 : 52224) : 13369344;
         param1.graphics.beginFill(_loc9_,0.4);
         if(this.var_6 == TARGETMETHOD_MELEE || this.var_6 == const_32 || this.var_6 == const_46)
         {
            param1.graphics.drawRect(param2.appearPosX - _loc6_ + _loc7_,param2.appearPosY - param2.entType.height,_loc6_ * 2,param2.entType.height);
         }
         else if(this.var_6 == const_130)
         {
            param1.graphics.drawRect(param2.var_10 - this.aoeRadius + _loc7_,param2.var_12 - this.aoeRadius + this.var_127,this.aoeRadius * 2,this.aoeRadius * 2);
         }
         else if(this.var_6 == TARGETMETHOD_PBAOE)
         {
            param1.graphics.drawRect(param2.var_10 - this.aoeRadius + _loc7_,param2.var_12 - this.aoeRadius + this.var_127,this.aoeRadius * 2,this.aoeRadius * 2);
         }
         else if(this.var_6 == const_111)
         {
            param1.graphics.drawRect(param3.x - this.var_375[param4] + _loc7_,param3.y - this.aoeRadius + this.var_127,this.var_375[param4] * 2,this.aoeRadius * 2);
         }
         else if(this.var_6 == const_113)
         {
            param1.graphics.drawRect(param3.x - this.aoeRadius + _loc7_,param3.y - this.var_375[param4] + this.var_127,this.aoeRadius * 2,this.var_375[param4] * 2);
         }
         else if(this.var_6 == TARGETMETHOD_PROJECTILE)
         {
            param1.graphics.drawRect(param3.x - _loc6_,param3.y - _loc6_,_loc6_ * 2,_loc6_ * 2);
         }
         else if(this.var_6 == TARGETMETHOD_RANGEDAOE || this.var_6 == const_89 || Boolean(const_96))
         {
            param1.graphics.drawRect(param3.x - _loc6_,param3.y - _loc6_,_loc6_ * 2,_loc6_ * 2);
         }
         else
         {
            param1.graphics.drawRect(param2.appearPosX - _loc6_,param2.appearPosY - _loc6_,_loc6_ * 2,_loc6_ * 2);
         }
         param1.graphics.endFill();
         if(this.var_507)
         {
            param1.graphics.beginFill(52224,0.2);
            param1.graphics.drawRect(param2.appearPosX + _loc7_ - 5,param2.appearPosY - param2.entType.height,10,param2.entType.height);
            param1.graphics.endFill();
         }
         if(this.var_127)
         {
            param1.graphics.beginFill(52224,0.2);
            param1.graphics.drawRect(param2.appearPosX + _loc7_ - param2.entType.width * 0.5,param2.appearPosY + this.var_127 - 5,param2.entType.width,10);
            param1.graphics.endFill();
         }
      }
      
      private function method_358(param1:int, param2:Number, param3:Number) : Number
      {
         var _loc4_:int = Math.round((this.damageMultFull + param3) * param1);
         if(param2)
         {
            _loc4_ += Math.ceil(param2 * _loc4_);
         }
         return _loc4_;
      }
      
      private function method_1344(param1:BuffType, param2:int) : Number
      {
         var _loc3_:Number = param1.var_772 * param2;
         return Math.round(_loc3_);
      }
      
      public function method_349(param1:Entity, param2:class_42 = null, param3:Boolean = false, param4:class_45 = null, param5:class_44 = null) : String
      {
         var _loc21_:uint = 0;
         var _loc22_:EntTypeGear = null;
         var _loc23_:String = null;
         var _loc24_:GearType = null;
         var _loc25_:uint = 0;
         var _loc26_:uint = 0;
         var _loc27_:PowerType = null;
         var _loc28_:PowerType = null;
         var _loc29_:class_10 = null;
         var _loc30_:uint = 0;
         var _loc31_:PowerType = null;
         var _loc32_:String = null;
         var _loc33_:uint = 0;
         var _loc34_:PowerType = null;
         var _loc35_:int = 0;
         var _loc36_:* = null;
         var _loc37_:* = null;
         var _loc6_:*;
         if(!(_loc6_ = param3 ? this.var_1499 : this.description) || !param1)
         {
            return "";
         }
         var _loc7_:int = param1.meleeDamage;
         var _loc8_:int = param1.magicDamage;
         var _loc9_:Number = Number(param1.var_719[this.var_157]);
         if(!!param2 ? param2.gearType : null)
         {
            _loc21_ = uint(EntType.method_87(null.type));
            if(_loc22_ = param1.entType.equippedGear[_loc21_])
            {
               if(_loc24_ = !!(_loc23_ = _loc22_.gearName) ? class_14.gearTypesDict[_loc23_] : null)
               {
                  _loc26_ = _loc24_.method_377(param1.mExpLevel);
                  _loc7_ -= _loc24_.method_121("Attack",_loc26_);
                  _loc8_ -= _loc24_.method_121("Expertise",_loc26_);
               }
               _loc25_ = uint(null.method_377(param1.mExpLevel));
               _loc7_ += null.method_121("Attack",_loc25_);
               _loc8_ += null.method_121("Expertise",_loc25_);
            }
         }
         var _loc11_:Number = 0;
         var _loc12_:int = 0;
         var _loc13_:Boolean = false;
         if(this.powerName == this.var_347)
         {
            if(param5)
            {
               _loc11_ = param5.method_102(param1,this.basePowerName,"BaseDamageMult");
            }
            _loc12_ = this.method_358(_loc7_,_loc9_,_loc11_);
            _loc13_ = true;
         }
         else if(_loc27_ = class_14.powerTypesDict[this.var_347])
         {
            if(param5)
            {
               _loc11_ = param5.method_102(param1,_loc27_.basePowerName,"BaseDamageMult");
            }
            _loc12_ = _loc27_.method_358(_loc7_,_loc9_,_loc11_);
         }
         if(_loc12_ < 0)
         {
            _loc12_ *= -1;
         }
         var _loc14_:BuffType = null;
         if(this.var_381)
         {
            _loc14_ = class_14.buffTypesDict[this.var_381[0]];
         }
         else if(this.var_437)
         {
            _loc14_ = class_14.buffTypesDict[this.var_437[0]];
         }
         var _loc15_:int = 0;
         var _loc16_:Number = 0;
         if(_loc14_)
         {
            _loc16_ = _loc14_.var_454 * 0.001;
            if((_loc15_ = this.method_1344(_loc14_,_loc8_)) < 0)
            {
               _loc15_ *= -1;
            }
         }
         if(_loc14_)
         {
            if(_loc14_.var_1378)
            {
               _loc6_ += " (Increases travel speed by 40%)";
            }
            else if(_loc14_.var_1063)
            {
               _loc28_ = class_14.powerTypesDict[_loc14_.var_1063];
               _loc6_ += _loc28_.description;
            }
         }
         var _loc17_:uint = 0;
         var _loc18_:Boolean = false;
         if(Boolean(param4) && param3)
         {
            _loc29_ = class_14.var_704[this.basePowerName];
            _loc30_ = 0;
            if(_loc29_)
            {
               _loc30_ = param4.GetCurrRankByAbilityID(_loc29_.abilityID);
            }
            if(_loc30_)
            {
               _loc31_ = class_14.powerTypesDict[this.basePowerName + _loc30_];
            }
            if(_loc31_)
            {
               if(_loc13_)
               {
                  _loc17_ = _loc31_.method_358(_loc7_,_loc9_,_loc11_);
               }
               else if(_loc34_ = class_14.powerTypesDict[_loc31_.var_347])
               {
                  if(param5)
                  {
                     _loc11_ = param5.method_102(param1,_loc34_.basePowerName,"BaseDamageMult");
                  }
                  _loc17_ = _loc34_.method_358(_loc7_,_loc9_,_loc11_);
               }
            }
            _loc32_ = this.powerName.substr(this.basePowerName.length);
            if((_loc33_ = uint(_loc32_)) > _loc30_)
            {
               _loc18_ = true;
            }
         }
         var _loc20_:uint;
         var _loc19_:Array;
         if(_loc20_ = (_loc19_ = _loc6_.split("#")).length)
         {
            _loc35_ = 0;
            while(_loc35_ < _loc20_)
            {
               if(_loc19_[_loc35_] == "dmg")
               {
                  _loc19_[_loc35_] = MathUtil.method_29(_loc12_);
               }
               else if(_loc19_[_loc35_] == "dot")
               {
                  _loc19_[_loc35_] = MathUtil.method_29(_loc15_);
               }
               else if(_loc19_[_loc35_] == "dur")
               {
                  _loc19_[_loc35_] = MathUtil.method_29(_loc16_);
               }
               else if(_loc19_[_loc35_] == "olddmg")
               {
                  _loc36_ = "<font color=\'#00CCFF\'>\n(Current: " + MathUtil.method_29(_loc17_) + ", Improved: " + MathUtil.method_29(_loc12_) + ")</font>";
                  _loc37_ = "<font color=\'#00CCFF\'>\n(Current: " + MathUtil.method_29(_loc17_) + ")</font>";
                  if(_loc18_)
                  {
                     _loc19_[_loc35_] = _loc36_;
                  }
                  else
                  {
                     _loc19_[_loc35_] = _loc37_;
                  }
               }
               _loc35_++;
            }
            _loc6_ = _loc19_.join("");
         }
         return _loc6_;
      }
      
      public function method_2053(param1:Entity) : String
      {
         if(!param1)
         {
            return "";
         }
         var _loc2_:PowerType = !!param1.mEquipPet ? param1.mEquipPet.var_1693 : null;
         if(!_loc2_)
         {
            return "";
         }
         return _loc2_.description;
      }
      
      public function method_1137(param1:Boolean = false) : uint
      {
         var _loc2_:PowerType = null;
         if(!this.var_646 || param1)
         {
            this.var_646 = 0;
            _loc2_ = this;
            while(_loc2_)
            {
               if(_loc2_.var_653)
               {
                  this.var_646 += _loc2_.var_653;
               }
               else
               {
                  this.var_646 += _loc2_.var_287;
                  this.var_646 += _loc2_.var_125;
               }
               if(_loc2_.var_543)
               {
                  _loc2_ = class_14.powerTypesDict[_loc2_.var_543];
               }
               else
               {
                  _loc2_ = null;
               }
            }
         }
         return this.var_646;
      }
      
      public function method_1773(param1:Entity) : Number
      {
         var _loc2_:String = null;
         var _loc3_:Number = CombatState.const_1097;
         if(param1 && param1.entType && Boolean(this.var_402))
         {
            _loc2_ = param1.entType.var_328;
            if(_loc2_ == this.var_402)
            {
               _loc3_ = CombatState.const_1254;
            }
            else if(_loc2_ == const_804 && this.var_402 == const_740 || _loc2_ == const_740 && this.var_402 == const_804 || _loc2_ == const_755 && this.var_402 == const_673 || _loc2_ == const_673 && this.var_402 == const_755 || _loc2_ == DAMAGETYPE_FIRE && this.var_402 == const_714 || _loc2_ == const_714 && this.var_402 == DAMAGETYPE_FIRE)
            {
               _loc3_ = CombatState.const_970;
            }
         }
         return _loc3_;
      }
   }
}
