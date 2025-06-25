package
{
   import flash.utils.Dictionary;
   
   public class BuffType
   {
      
      public static const const_48:uint = 3;
      
      public static const const_163:Vector.<Number> = new Vector.<Number>(const_48,true);
      
      public static const const_368:Vector.<uint> = new Vector.<uint>(const_48,true);
      
      public static var var_1869:BuffType;
      
      public static const const_53:uint = 1 << 0;
      
      public static const const_60:uint = 1 << 1;
      
      public static const const_57:uint = 1 << 2;
      
      public static const const_63:uint = 1 << 3;
      
      public static const const_64:uint = 1 << 4;
      
      public static const const_49:uint = 1 << 5;
      
      public static const const_54:uint = 1 << 6;
      
      public static const const_66:uint = 1 << 7;
      
      public static const const_61:uint = 1 << 8;
      
      public static const const_70:uint = 1 << 9;
      
      public static const const_51:uint = 1 << 10;
      
      public static const const_52:uint = 1 << 11;
      
      public static const const_67:uint = 1 << 12;
      
      public static const const_55:uint = 1 << 13;
      
      public static const const_932:uint = 14;
      
      public static const const_624:Array = [const_52,const_70,const_60,const_64,const_53,const_63,const_54,const_66,const_57,const_49,const_51,const_67,const_61,const_55];
      
      public static const const_1049:Array = [const_51,const_52,const_60,const_64,const_53,const_63,const_55,const_70,const_54,const_66,const_57,const_49,const_67,const_61];
      
      public static const const_1274:Array = [const_55,const_60,const_64,const_53,const_63,const_54,const_66,const_57,const_49,const_51,const_52,const_70,const_67,const_61];
      
      public static const const_1100:Array = [const_61,const_70,const_60,const_64,const_53,const_63,const_54,const_66,const_57,const_49,const_51,const_52,const_67,const_55];
      
      public static const const_1275:Array = [const_70,const_60,const_64,const_53,const_63,const_54,const_66,const_57,const_49,const_61,const_51,const_52,const_67,const_55];
      
      public static const const_986:Array = [const_67,const_60,const_64,const_53,const_63,const_54,const_66,const_57,const_49,const_51,const_52,const_70,const_61,const_55];
      
      public static const const_1210:Array = [const_67,const_60,const_64,const_53,const_63,const_54,const_66,const_57,const_49,const_51,const_52,const_70,const_61,const_55];
      
      public static const const_1056:Array = [const_70,const_53,const_54,const_60,const_64,const_63,const_61,const_66,const_57,const_49,const_51,const_52,const_67,const_55];
      
      public static const const_1268:Array = [const_70,const_60,const_64,const_53,const_63,const_54,const_66,const_57,const_49,const_52,const_55,const_51,const_67,const_61];
      
      public static const const_1025:Array = [const_67,const_60,const_64,const_53,const_63,const_54,const_66,const_57,const_49,const_51,const_52,const_70,const_61,const_55];
      
      public static var var_709:BuffType = null;
      
      {
         const_163[0] = 0.375;
         const_163[1] = 0.625;
         const_163[2] = 1;
         const_368[0] = 0;
         const_368[1] = 100;
         const_368[2] = 150;
      }
      
      internal var buffID:uint;
      
      internal var buffName:String;
      
      internal var var_774:Boolean;
      
      internal var var_454:uint;
      
      internal var var_2446:Boolean;
      
      internal var magicDamage:Number = 0;
      
      internal var meleeDamage:Number = 0;
      
      internal var var_1597:Number = 0;
      
      internal var var_1322:Number = 0;
      
      internal var var_915:Number = 0;
      
      internal var var_1086:Number = 0;
      
      internal var var_2700:Number = 0;
      
      internal var var_663:Number = 0;
      
      internal var var_1446:Number = 0;
      
      internal var var_491:Number = 0;
      
      internal var var_2477:String;
      
      internal var var_2894:Number = 0;
      
      internal var var_2362:Number = 0;
      
      internal var speedChange:Number = 0;
      
      internal var var_2397:Number = 0;
      
      internal var var_772:Number = 0;
      
      internal var var_635:uint = 0;
      
      internal var var_1679:uint = 0;
      
      internal var var_668:Boolean = false;
      
      internal var var_953:Boolean = false;
      
      internal var bDisabled:Boolean = false;
      
      internal var var_1961:Boolean = false;
      
      internal var var_876:Boolean = false;
      
      internal var var_2802:Boolean = false;
      
      internal var bUntargetable:Boolean = false;
      
      internal var var_2050:Boolean = false;
      
      internal var var_2548:Boolean = false;
      
      internal var var_2775:Boolean = false;
      
      internal var var_2684:Boolean = false;
      
      internal var var_2620:Boolean = false;
      
      internal var var_2648:Boolean = false;
      
      internal var var_2250:Boolean = false;
      
      internal var var_2845:Boolean = false;
      
      internal var var_2403:Boolean = false;
      
      internal var var_753:Boolean = false;
      
      internal var var_2499:Boolean = false;
      
      internal var var_1035:GfxType = null;
      
      internal var var_2424:Boolean = false;
      
      internal var var_221:String;
      
      internal var var_1378:Boolean = false;
      
      internal var var_1063:String = null;
      
      internal var var_306:Vector.<GfxType> = null;
      
      internal var var_247:Vector.<GfxType> = null;
      
      internal var var_932:uint = 0;
      
      internal var var_1235:uint = 0;
      
      internal var var_2125:String = null;
      
      internal var var_2287:String = null;
      
      internal var stackCount:uint = 1;
      
      internal var var_2473:Boolean = false;
      
      internal var var_2950:int = 0;
      
      internal var var_1708:Boolean = false;
      
      internal var var_1627:Boolean = false;
      
      internal var var_1268:Boolean = false;
      
      internal var var_1061:Boolean = false;
      
      internal var var_2019:Boolean = false;
      
      internal var var_2494:Boolean = false;
      
      internal var var_956:uint = 0;
      
      internal var var_2192:uint = 0;
      
      internal var var_2789:Boolean = false;
      
      internal var var_611:String = null;
      
      internal var var_1251:int = 0;
      
      internal var var_2632:Boolean;
      
      internal var var_2030:Boolean = false;
      
      internal var var_2859:Boolean = false;
      
      internal var var_2728:String = null;
      
      internal var var_76:uint = 0;
      
      public function BuffType()
      {
         super();
      }
      
      public static function method_505(param1:XML) : void
      {
         method_18(param1,class_14.buffTypes,class_14.buffTypesDict,false);
      }
      
      public static function method_476(param1:XML) : void
      {
         method_18(param1,class_14.buffTypes,class_14.buffTypesDict,true);
         var_709 = class_14.buffTypesDict["DismissPet"];
         if(!var_709)
         {
            class_24.method_7("DismissPet buff must exist, but was not found");
         }
         var_1869 = class_14.buffTypesDict["PowerSurge"];
         if(!var_1869)
         {
            class_24.method_7("POWER_SURGE_BUFF must exist");
         }
      }
      
      public static function method_553(param1:XML, param2:Boolean) : BuffType
      {
         var _loc4_:XML = null;
         var _loc5_:String = null;
         var _loc6_:Number = NaN;
         var _loc7_:Array = null;
         var _loc8_:Array = null;
         var _loc9_:GfxType = null;
         var _loc10_:GfxType = null;
         var _loc11_:Vector.<GfxType> = null;
         var _loc12_:int = 0;
         var _loc13_:uint = 0;
         var _loc14_:Number = NaN;
         var _loc15_:uint = 0;
         var _loc16_:String = null;
         var _loc17_:Array = null;
         var _loc18_:String = null;
         var _loc19_:String = null;
         var _loc20_:GfxType = null;
         var _loc21_:int = 0;
         var _loc3_:BuffType = new BuffType();
         _loc3_.buffName = param1.attribute("BuffName");
         _loc3_.var_2446 = param2;
         for each(_loc4_ in param1.*)
         {
            if((_loc5_ = String(_loc4_.name().toString())) == "BuffID")
            {
               _loc3_.buffID = uint(_loc4_);
            }
            else if(_loc5_ == "Attack")
            {
               _loc3_.var_774 = MathUtil.method_50(_loc4_);
            }
            else if(_loc5_ == "Duration")
            {
               _loc3_.var_454 = uint(_loc4_);
            }
            else if(_loc5_ == "StackCount")
            {
               _loc3_.stackCount = uint(_loc4_);
            }
            else if(_loc5_ == "RangedOverride")
            {
               _loc3_.var_2125 = _loc4_.toString();
            }
            else if(_loc5_ == "MeleeOverride")
            {
               _loc3_.var_2287 = _loc4_.toString();
            }
            else if(_loc5_ == "MagicDamage")
            {
               _loc3_.magicDamage = Number(_loc4_);
            }
            else if(_loc5_ == "MeleeDamage")
            {
               _loc3_.meleeDamage = Number(_loc4_);
            }
            else if(_loc5_ == "MagicDefense")
            {
               if((_loc6_ = Number(_loc4_)) < -1 || _loc6_ >= 1)
               {
                  class_24.method_7("Magic Defense outside of valid range -1 to .99:" + _loc3_.buffName + ": " + _loc6_);
               }
               else
               {
                  _loc3_.var_1597 = Number(_loc4_);
               }
            }
            else if(_loc5_ == "MeleeDefense")
            {
               if((_loc6_ = Number(_loc4_)) < -1 || _loc6_ >= 1)
               {
                  class_24.method_7("Melee Defense outside of valid range -1 to .99:" + _loc3_.buffName + ": " + _loc6_);
               }
               else
               {
                  _loc3_.var_1322 = Number(_loc4_);
               }
            }
            else if(_loc5_ == "DoTDamage")
            {
               _loc3_.var_772 = Number(_loc4_);
            }
            else if(_loc5_ == "DoTTickLength")
            {
               _loc3_.var_635 = uint(_loc4_);
            }
            else if(_loc5_ == "VampPercent")
            {
               _loc3_.var_2894 = Number(_loc4_);
            }
            else if(_loc5_ == "RageCostChange")
            {
               _loc3_.var_2362 = Number(_loc4_);
            }
            else if(_loc5_ == "SpeedChange")
            {
               _loc3_.speedChange = Number(_loc4_);
            }
            else if(_loc5_ == "AggroChange")
            {
               _loc3_.var_2397 = Number(_loc4_);
            }
            else if(_loc5_ == "RemoveOnDamage")
            {
               _loc3_.var_2473 = MathUtil.method_50(_loc4_);
            }
            else if(_loc5_ == "KingdomOnly")
            {
               _loc3_.var_2477 = _loc4_.toString();
            }
            else if(_loc5_ == "BuffIcon")
            {
               _loc7_ = _loc4_.toString().split(",");
               _loc3_.method_1328(_loc7_);
            }
            else if(_loc5_ == "EntTint")
            {
               _loc8_ = _loc4_.toString().split("+");
               _loc3_.var_932 = uint(_loc8_[0]);
               if(_loc8_.length > 1)
               {
                  _loc3_.var_1235 = uint(_loc8_[1]);
               }
            }
            else if(_loc5_ == "GfxType")
            {
               if(_loc10_ = GfxType.method_53(_loc4_,null))
               {
                  if(_loc11_ = GfxType.method_321(_loc10_,_loc4_))
                  {
                     _loc3_.var_2789 = true;
                     _loc12_ = int(_loc11_.length);
                     _loc3_.var_306 = new Vector.<GfxType>(const_48 * _loc12_,true);
                     _loc13_ = 0;
                     while(_loc13_ < _loc12_)
                     {
                        _loc14_ = _loc11_[_loc13_].animScale;
                        _loc15_ = 0;
                        while(_loc15_ < const_48)
                        {
                           (_loc10_ = !!_loc15_ ? _loc11_[_loc13_].GetDuplicate() : _loc11_[_loc13_]).animScale = _loc14_ * const_163[_loc15_];
                           _loc3_.var_306[_loc13_ * const_48 + _loc15_] = _loc10_;
                           if(_loc9_ = GfxType.method_368(_loc10_,_loc4_))
                           {
                              if(!_loc3_.var_247)
                              {
                                 _loc3_.var_247 = new Vector.<GfxType>(const_48 * _loc12_,true);
                              }
                              _loc3_.var_247[_loc13_ * const_48 + _loc15_] = _loc9_;
                              _loc9_.animScale *= const_163[_loc15_];
                           }
                           _loc15_++;
                        }
                        _loc13_++;
                     }
                  }
                  else
                  {
                     _loc3_.var_306 = new Vector.<GfxType>(const_48,true);
                     _loc15_ = 0;
                     while(_loc15_ < const_48)
                     {
                        _loc10_ = !!_loc15_ ? GfxType.method_53(_loc4_,null) : _loc10_;
                        _loc10_.animScale *= const_163[_loc15_];
                        _loc3_.var_306[_loc15_] = _loc10_;
                        if(_loc9_ = GfxType.method_368(_loc10_,_loc4_))
                        {
                           if(!_loc3_.var_247)
                           {
                              _loc3_.var_247 = new Vector.<GfxType>(3,true);
                           }
                           _loc3_.var_247[_loc15_] = _loc9_;
                           _loc9_.animScale *= const_163[_loc15_];
                        }
                        _loc15_++;
                     }
                  }
               }
            }
            else if(_loc5_ == "Effect")
            {
               _loc17_ = (_loc16_ = _loc4_.toString()).split(",");
               for each(_loc18_ in _loc17_)
               {
                  if(_loc18_ == "Disabled")
                  {
                     _loc3_.bDisabled = true;
                  }
                  else if(_loc18_ == "Confused")
                  {
                     _loc3_.var_1961 = true;
                  }
                  else if(_loc18_ == "Distracted")
                  {
                     _loc3_.var_876 = true;
                  }
                  else if(_loc18_ == "Invisible")
                  {
                     _loc3_.var_2802 = true;
                  }
                  else if(_loc18_ == "Untargetable")
                  {
                     _loc3_.bUntargetable = true;
                  }
                  else if(_loc18_ == "Stealthed")
                  {
                     _loc3_.var_2050 = true;
                  }
                  else if(_loc18_ == "Invulnerable")
                  {
                     _loc3_.var_2548 = true;
                  }
                  else if(_loc18_ == "MagicImmune")
                  {
                     _loc3_.var_2775 = true;
                  }
                  else if(_loc18_ == "MeleeImmune")
                  {
                     _loc3_.var_2684 = true;
                  }
                  else if(_loc18_ == "Mounted")
                  {
                     _loc3_.var_1378 = true;
                  }
                  else if(_loc18_ == "Petted")
                  {
                     _loc3_.var_1063 = _loc3_.buffName;
                  }
                  else if(_loc18_ == "Stunned")
                  {
                     _loc3_.var_668 = true;
                     if(_loc3_.var_221)
                     {
                        class_24.method_7("Can\'t have multiple immunity effects on a single buff:" + _loc3_.buffName + ": " + _loc18_ + ", " + _loc3_.var_221);
                     }
                     _loc3_.var_221 = _loc18_;
                  }
                  else if(_loc18_ == "Frozen")
                  {
                     _loc3_.var_953 = true;
                     if(_loc3_.var_221)
                     {
                        class_24.method_7("Can\'t have multiple immunity effects on a single buff:" + _loc3_.buffName + ": " + _loc18_ + ", " + _loc3_.var_221);
                     }
                     _loc3_.var_221 = _loc18_;
                  }
                  else if(_loc18_ == "Rooted")
                  {
                     if(_loc3_.var_221)
                     {
                        class_24.method_7("Can\'t have multiple immunity effects on a single buff:" + _loc3_.buffName + ": " + _loc18_ + ", " + _loc3_.var_221);
                     }
                     _loc3_.var_221 = _loc18_;
                  }
                  else if(_loc18_ == "IceRooted")
                  {
                     _loc3_.var_2648 = true;
                     if(_loc3_.var_221)
                     {
                        class_24.method_7("Can\'t have multiple immunity effects on a single buff:" + _loc3_.buffName + ": " + _loc18_ + ", " + _loc3_.var_221);
                     }
                     _loc3_.var_221 = _loc18_;
                  }
                  else if(_loc18_ == "Chilled")
                  {
                     _loc3_.var_2250 = true;
                  }
                  else if(_loc18_ == "Chilblains")
                  {
                     _loc3_.var_2845 = true;
                  }
                  else if(_loc18_ == "Poisoned")
                  {
                     _loc3_.var_2403 = true;
                  }
                  else
                  {
                     class_24.method_7("Unrecognized Effect in " + _loc3_.buffName + ": " + _loc18_);
                  }
               }
            }
            else if(_loc5_ == "BuffLoc")
            {
               if((_loc19_ = _loc4_.toString()) == "Chest")
               {
                  _loc3_.var_1627 = true;
               }
               else if(_loc19_ == "Head")
               {
                  _loc3_.var_1708 = true;
               }
               else if(_loc19_ == "FeetBack")
               {
                  _loc3_.var_1061 = true;
               }
               else if(_loc19_ == "ChestBack")
               {
                  _loc3_.var_1627 = true;
                  _loc3_.var_1061 = true;
               }
               else if(_loc19_ == "HeadBack")
               {
                  _loc3_.var_1708 = true;
                  _loc3_.var_1061 = true;
               }
               else if(_loc19_ == "Tick")
               {
                  _loc3_.var_1268 = true;
                  _loc3_.var_1627 = true;
               }
               else if(_loc19_ == "Feet")
               {
                  _loc3_.var_1061 = false;
               }
               else if(_loc19_ == "Socket")
               {
                  _loc3_.var_1061 = false;
                  _loc3_.var_2019 = true;
               }
               else
               {
                  class_24.method_7("Unrecognized BuffLoc in " + _loc3_.buffName + ": " + _loc19_);
               }
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc3_.buffName + ": " + _loc5_);
            }
         }
         if(_loc3_.var_635)
         {
            _loc3_.var_1679 = _loc3_.var_454 / _loc3_.var_635;
         }
         if(_loc3_.var_1268)
         {
            if(_loc3_.var_306)
            {
               for each(_loc20_ in _loc3_.var_306)
               {
                  _loc20_.bFireAndForget = true;
               }
            }
            if(_loc3_.var_247)
            {
               for each(_loc20_ in _loc3_.var_247)
               {
                  _loc20_.bFireAndForget = true;
               }
            }
         }
         if(_loc3_.var_1061)
         {
            _loc3_.var_247 = _loc3_.var_306;
            _loc3_.var_306 = null;
         }
         if(!_loc3_.var_772 && _loc3_.var_454 && _loc3_.var_2446)
         {
            _loc3_.var_2632 = true;
         }
         if(_loc3_.buffName == "ShadowTendril")
         {
            _loc3_.var_221 = null;
         }
         if(_loc3_.buffName.indexOf("SentinelForm") == 0)
         {
            _loc3_.var_2499 = true;
            _loc3_.var_753 = true;
            _loc3_.var_956 = 190;
         }
         if(_loc3_.buffName.indexOf("IceArmor") == 0)
         {
            _loc3_.var_753 = true;
            _loc3_.var_956 = 277;
         }
         if(_loc3_.buffName == "Haunted")
         {
            _loc3_.var_663 = -0.4;
         }
         if(_loc3_.buffName == "Blinded")
         {
            _loc3_.var_1446 = 0.25;
         }
         else if(_loc3_.buffName == "PetFairyBlind")
         {
            _loc3_.var_1446 = 0.5;
         }
         else if(_loc3_.buffName == "PetCrowBlind")
         {
            _loc3_.var_1446 = 0.5;
         }
         if(_loc3_.buffName == "EyeOfTheStorm")
         {
            _loc3_.var_753 = true;
            _loc3_.var_663 = 0.5;
         }
         if(_loc3_.buffName == "Awareness")
         {
            _loc3_.var_663 = 0.03;
         }
         if(_loc3_.buffName.indexOf("SeekingBlades") == 0)
         {
            _loc3_.var_753 = true;
            _loc3_.var_956 = 111;
         }
         if(_loc3_.buffName.indexOf("Pyromania") == 0)
         {
            _loc3_.var_753 = true;
            _loc3_.var_956 = 800;
            _loc3_.var_611 = "EndPyromania";
            _loc3_.var_1251 = 5;
         }
         if(_loc3_.buffName.indexOf("ShadowArmor") == 0)
         {
            _loc3_.var_753 = true;
            _loc3_.var_956 = 625;
            _loc3_.var_2192 = 3000;
         }
         if(_loc3_.buffName == "RuneStealth")
         {
            _loc3_.var_663 = 1;
         }
         if(_loc3_.buffName.indexOf("DetShield") == 0)
         {
            _loc21_ = int(_loc3_.buffName.substring(9));
            _loc3_.var_753 = true;
            _loc3_.var_611 = "DetShieldDetonate" + _loc21_;
            _loc3_.var_1251 = 5;
            _loc3_.var_1035 = new GfxType();
            _loc3_.var_1035.var_29 = "SFX_2.swf";
            _loc3_.var_1035.animScale = 0.8;
            _loc3_.var_1035.bFireAndForget = true;
            _loc3_.var_1035.animClass = "a_Ping_Barrier";
         }
         if(_loc3_.buffName.indexOf("SentinelForm") == 0)
         {
            _loc3_.var_611 = "EndSentinelForm";
            _loc3_.var_1251 = 6;
         }
         if(_loc3_.buffName.indexOf("IceArmor") == 0)
         {
            _loc3_.var_611 = "EndFrostArmor";
            _loc3_.var_1251 = 6;
         }
         if(_loc3_.buffName == "SeekingBlades")
         {
            _loc3_.var_611 = "EndSeekingBlades";
            _loc3_.var_1251 = 6;
         }
         if(_loc3_.buffName == "ProcMassiveTimeBuff" || _loc3_.buffName == "ProcHealTimeBuff")
         {
            _loc3_.var_2424 = true;
         }
         if(_loc3_.var_1961 || _loc3_.bDisabled || _loc3_.var_876 || _loc3_.var_668 || _loc3_.var_953 || _loc3_.speedChange < 0)
         {
            _loc3_.var_2620 = true;
         }
         if(!_loc3_.buffName.indexOf("GiftUndead") || !_loc3_.buffName.indexOf("LichLeadership"))
         {
            _loc3_.var_2859 = true;
         }
         if(_loc3_.buffName == "LightningStorm")
         {
            _loc3_.var_491 = 0.1;
         }
         if(_loc3_.buffName == "PetMonkeyHaste")
         {
            _loc3_.var_491 = 0.1;
         }
         if(_loc3_.buffName == "Frigid" || _loc3_.buffName == "RuneEnfeeble")
         {
            _loc3_.var_491 = -0.15;
         }
         if(_loc3_.buffName == "Fatigued")
         {
            _loc3_.var_491 = -0.3;
         }
         if(_loc3_.buffName.indexOf("PainEaterRank") == 0)
         {
            switch(int(_loc3_.buffName.substring(13)))
            {
               case 1:
                  _loc3_.var_491 = 0.01;
                  break;
               case 2:
                  _loc3_.var_491 = 0.02;
                  break;
               case 3:
                  _loc3_.var_491 = 0.04;
                  break;
               case 4:
                  _loc3_.var_491 = 0.06;
                  break;
               case 5:
                  _loc3_.var_491 = 0.1;
            }
         }
         if(_loc3_.buffName.indexOf("HeroismRank") == 0)
         {
            switch(int(_loc3_.buffName.substring(11)))
            {
               case 1:
                  _loc3_.var_915 = 0.02;
                  break;
               case 2:
                  _loc3_.var_915 = 0.05;
                  break;
               case 3:
                  _loc3_.var_915 = 0.09;
                  break;
               case 4:
                  _loc3_.var_915 = 0.14;
                  break;
               case 5:
                  _loc3_.var_915 = 0.2;
            }
         }
         if(_loc3_.buffName.indexOf("SoulReaver") >= 0 || _loc3_.buffName.indexOf("GhostBlade") >= 0)
         {
            _loc3_.var_2030 = true;
         }
         if(_loc3_.buffName == "DismissPet")
         {
            _loc3_.var_2494 = true;
         }
         return _loc3_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary, param4:Boolean) : void
      {
         var _loc5_:XML = null;
         var _loc6_:BuffType = null;
         for each(_loc5_ in param1.*)
         {
            if((_loc6_ = method_553(_loc5_,param4)).buffID)
            {
               if(param2[_loc6_.buffID])
               {
                  class_24.method_7("Multiple buffs with ID: " + _loc6_.buffID);
               }
               if(param3[_loc6_.buffName])
               {
                  class_24.method_7("Multiple buffs with name: " + _loc6_.buffName);
               }
               if(!_loc6_.stackCount)
               {
                  class_24.method_7("Stack count must be non-zero: " + _loc6_.buffName);
               }
               if(Boolean(_loc6_.var_635) && _loc6_.var_454 != _loc6_.var_635 * _loc6_.var_1679)
               {
                  class_24.method_7("Buff TickLength must divide evenly into duration: " + _loc6_.buffName);
               }
               param2[_loc6_.buffID] = _loc6_;
               param3[_loc6_.buffName] = _loc6_;
            }
         }
      }
      
      public static function method_2103(param1:Buff, param2:Buff) : Number
      {
         return method_339(param1) - method_339(param2);
      }
      
      public static function method_339(param1:Buff) : Number
      {
         var _loc2_:BuffType = param1.type;
         var _loc3_:Number = 0;
         if(param1.var_176)
         {
            if(_loc2_.bUntargetable)
            {
               _loc3_ += 10000;
            }
            if(_loc2_.var_2050)
            {
               _loc3_ += 9999;
            }
            if(_loc2_.var_668)
            {
               _loc3_ += 999;
            }
            if(_loc2_.var_953)
            {
               _loc3_ += 998;
            }
            if(_loc2_.bDisabled)
            {
               _loc3_ += 997;
            }
            if(param1.method_351() > 1)
            {
               _loc3_ += 996;
            }
            if(_loc2_.var_772 != 0)
            {
               _loc3_ += 995;
            }
            if(_loc2_.var_876)
            {
               _loc3_ += 994;
            }
         }
         return _loc3_;
      }
      
      public static function method_1811(param1:uint) : String
      {
         var _loc2_:String = null;
         switch(param1)
         {
            case const_53:
               _loc2_ = "a_StatusIcon_AttackDown";
               break;
            case const_60:
               _loc2_ = "a_StatusIcon_DefenseDown";
               break;
            case const_57:
               _loc2_ = "a_StatusIcon_SpeedDown";
               break;
            case const_63:
               _loc2_ = "a_StatusIcon_AttackUp";
               break;
            case const_64:
               _loc2_ = "a_StatusIcon_DefenseUp";
               break;
            case const_49:
               _loc2_ = "a_StatusIcon_SpeedUp";
               break;
            case const_54:
               _loc2_ = "a_StatusIcon_Immobile";
               break;
            case const_66:
               _loc2_ = "a_StatusIcon_Stagger";
               break;
            case const_61:
               _loc2_ = "a_StatusIcon_Bleeding";
               break;
            case const_70:
               _loc2_ = "a_StatusIcon_Poisoned";
               break;
            case const_51:
               _loc2_ = "a_StatusIcon_Scorched";
               break;
            case const_52:
               _loc2_ = "a_StatusIcon_Burned";
               break;
            case const_67:
               _loc2_ = "a_StatusIcon_Ignite";
               break;
            case const_55:
               _loc2_ = "a_StatusIcon_Chilblains";
         }
         return _loc2_;
      }
      
      public function method_1328(param1:Array) : void
      {
         var _loc2_:String = null;
         this.var_76 = 0;
         for each(_loc2_ in param1)
         {
            switch(_loc2_)
            {
               case "a_StatusIcon_AttackDown":
                  this.var_76 |= const_53;
                  break;
               case "a_StatusIcon_DefenseDown":
                  this.var_76 |= const_60;
                  break;
               case "a_StatusIcon_SpeedDown":
                  this.var_76 |= const_57;
                  break;
               case "a_StatusIcon_AttackUp":
                  this.var_76 |= const_63;
                  break;
               case "a_StatusIcon_DefenseUp":
                  this.var_76 |= const_64;
                  break;
               case "a_StatusIcon_SpeedUp":
                  this.var_76 |= const_49;
                  break;
               case "a_StatusIcon_Immobile":
                  this.var_76 |= const_54;
                  break;
               case "a_StatusIcon_Stagger":
                  this.var_76 |= const_66;
                  break;
               case "a_StatusIcon_Bleeding":
                  this.var_76 |= const_61;
                  break;
               case "a_StatusIcon_Poisoned":
                  this.var_76 |= const_70;
                  break;
               case "a_StatusIcon_Scorched":
                  this.var_76 |= const_51;
                  break;
               case "a_StatusIcon_Burned":
                  this.var_76 |= const_52;
                  break;
               case "a_StatusIcon_Ignited":
                  this.var_76 |= const_67;
                  break;
               case "a_StatusIcon_Chilblains":
                  this.var_76 |= const_55;
                  break;
            }
         }
      }
   }
}
