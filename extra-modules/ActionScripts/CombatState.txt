package
{
   import flash.geom.Point;
   import flash.utils.Dictionary;
   
   public class CombatState
   {
      
      private static const REGEN_AMOUNT:Number = 0.1;
      
      private static const const_1217:Number = 0.01;
      
      private static const REGEN_INTERVAL:uint = 500;
      
      public static const const_1248:Number = 0.2;
      
      public static const const_998:Number = 0.5;
      
      public static const const_1282:Number = 1;
      
      public static const const_1060:Number = 1.5;
      
      public static const const_970:Number = 1;
      
      public static const const_1097:Number = 0;
      
      public static const const_1254:Number = -0.5;
      
      public static const const_560:Number = 0.1;
      
      public static const const_466:Number = 0.1;
      
      public static const const_260:Number = 0.15;
      
      public static const const_126:Number = 0.1;
      
      public static const const_136:Number = 0.1;
      
      public static const const_556:Number = 0.1;
      
      public static const const_569:Number = 0.15;
      
      public static const const_548:Number = 0.05;
      
      public static const const_386:Number = 0.75;
      
      public static const const_332:Number = -0.75;
      
      public static const const_299:Number = 0.75;
      
      public static const const_354:Number = -0.75;
      
      public static const const_1349:Number = 0.5;
      
      public static const CANREGEN_TIME:uint = 6000 - REGEN_INTERVAL;
      
      private static const const_1146:Boolean = Boolean(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT || DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT);
      
      public static const const_1228:uint = 3000;
      
      public static const const_737:uint = 6;
      
      public static const const_135:Vector.<Number> = new Vector.<Number>(const_737 + 1,true);
      
      public static const const_1075:uint = 1500;
      
      public static var var_1005:GfxType = new GfxType();
      
      private static var var_2075:Number = 10;
      
      {
         const_135[0] = 0;
         const_135[1] = 1.25;
         const_135[2] = 0.8;
         const_135[3] = 0.6;
         const_135[4] = 0.3;
         const_135[5] = 0.15;
         const_135[6] = 0.1;
         var_1005.var_29 = "SFX_1.swf";
         var_1005.animScale = 0.45;
         var_1005.bFireAndForget = true;
         var_1005.animClass = "a_ProtectHitReact";
      }
      
      internal var var_1:Game;
      
      internal var var_3:Entity;
      
      internal var var_2145:Number;
      
      internal var var_2313:Number;
      
      internal var var_2051:uint;
      
      internal var var_1995:Number = 1;
      
      internal var var_937:uint = 0;
      
      internal var var_1435:uint = 0;
      
      internal var var_1660:int = 10;
      
      internal var masterDangerRegenInterval:uint = 0;
      
      internal var var_1392:Boolean = false;
      
      internal var var_1146:Number = 0;
      
      internal var var_2951:Number = 0;
      
      internal var var_1586:Number = 0;
      
      internal var var_2163:uint = 0;
      
      internal var var_2715:uint = 0;
      
      internal var var_2036:Boolean = false;
      
      internal var var_1201:Entity = null;
      
      private var var_2361:uint;
      
      internal var var_2173:Boolean = false;
      
      internal var var_1299:PowerType = null;
      
      internal var var_2531:uint = 0;
      
      internal var mActivePower:ActivePower = null;
      
      internal var var_554:Vector.<ActivePower> = null;
      
      internal var var_1937:Boolean = true;
      
      internal var var_1900:uint = 0;
      
      internal var currMeleeCombo:uint = 0;
      
      internal var var_2624:uint = 0;
      
      internal var var_1502:uint = 0;
      
      internal var var_813:uint = 1;
      
      internal var var_114:Dictionary;
      
      internal var var_1654:Dictionary;
      
      internal var var_84:Vector.<Buff>;
      
      internal var var_372:Vector.<SuperAnimInstance>;
      
      internal var var_2579:Number = 0;
      
      internal var var_663:Number = 0;
      
      internal var var_39:int = 0;
      
      internal var var_498:int = 0;
      
      internal var var_545:Boolean = false;
      
      internal var var_1853:int = 0;
      
      internal var var_555:Boolean = true;
      
      internal var var_288:Number = 0;
      
      internal var var_495:Number = 0;
      
      internal var var_360:Number = 0;
      
      internal var var_292:Number = 0;
      
      internal var var_1057:Dictionary;
      
      internal var var_577:Dictionary;
      
      internal var var_540:Number = 0;
      
      internal var var_2405:Number = 0;
      
      internal var var_984:Number = 0;
      
      internal var var_546:Number = 0;
      
      internal var var_1083:Number = 0;
      
      internal var var_1651:String = null;
      
      internal var var_1823:String = null;
      
      internal var var_270:String = null;
      
      internal var var_724:String = null;
      
      internal var var_823:Boolean = false;
      
      internal var var_683:Boolean = false;
      
      internal var var_2291:Boolean = false;
      
      internal var var_445:Boolean = false;
      
      internal var var_1488:Boolean = false;
      
      internal var var_1278:Boolean = false;
      
      internal var var_1559:Boolean = false;
      
      internal var var_414:Boolean = false;
      
      internal var var_2218:Boolean = false;
      
      internal var var_1421:Boolean = false;
      
      internal var var_840:Number = 0;
      
      internal var var_1923:Boolean = false;
      
      internal var var_1905:Boolean = false;
      
      internal var var_1819:Boolean = false;
      
      internal var var_1298:Boolean = false;
      
      internal var var_1033:int = 0;
      
      internal var var_2246:Boolean = false;
      
      internal var var_1710:Number = 0;
      
      internal var var_1674:Number = 0;
      
      internal var var_1797:Number = 0;
      
      internal var var_2043:Number = 0;
      
      internal var var_651:int = 0;
      
      internal var var_1139:Number = 1;
      
      internal var var_2151:Boolean = false;
      
      internal var var_1102:Boolean = false;
      
      internal var var_1515:Boolean = false;
      
      internal var var_1091:int = 0;
      
      internal var var_963:Boolean = false;
      
      internal var var_1171:Boolean = false;
      
      internal var var_1999:Boolean = false;
      
      internal var var_931:int = 0;
      
      internal var var_598:int = 0;
      
      internal var var_552:int = 0;
      
      internal var var_576:int = 0;
      
      internal var var_2689:Boolean = false;
      
      internal var var_1181:Number = 0;
      
      internal var var_1556:Number = 0;
      
      internal var var_1192:Number = 0;
      
      internal var var_1738:Number = 0;
      
      internal var var_2146:Boolean = false;
      
      internal var var_1981:int = 0;
      
      internal var var_1786:int = 0;
      
      internal var var_1032:int = 0;
      
      internal var var_2045:int = 0;
      
      internal var var_1313:Boolean = false;
      
      internal var var_1957:Boolean = false;
      
      internal var var_2111:int = 0;
      
      internal var var_2069:Boolean = false;
      
      internal var var_1234:int = 0;
      
      internal var var_1857:GfxType = null;
      
      internal var var_2953:Number = 0;
      
      internal var var_2114:Boolean = false;
      
      internal var var_2096:Boolean = false;
      
      internal var var_1188:uint = 0;
      
      internal var var_1815:uint = 0;
      
      internal var var_2195:Number = 0;
      
      internal var var_1483:Number = 0;
      
      internal var var_1557:Number = 0;
      
      internal var var_1433:int = 0;
      
      internal var var_1310:int = 0;
      
      internal var var_1455:int = 0;
      
      internal var var_1521:Number = 0;
      
      internal var var_1527:Number = 0;
      
      internal var var_1644:Number = 0;
      
      internal var var_1204:Number = 0;
      
      internal var var_1669:Boolean = false;
      
      internal var var_1414:Number = 0;
      
      internal var var_1093:Number = 0;
      
      internal var var_2566:uint = 0;
      
      internal var var_1424:Number = 0;
      
      internal var var_1311:Number = 0;
      
      internal var var_1410:Number = 0;
      
      internal var var_1595:Number = 0;
      
      internal var var_1574:String;
      
      internal var var_1567:Number = 0;
      
      internal var var_923:Number = 0;
      
      internal var var_971:Number = 0;
      
      internal var var_1428:Number = 0;
      
      internal var var_2168:Boolean = false;
      
      internal var var_2400:Boolean = false;
      
      internal var var_2279:Boolean = false;
      
      internal var var_2419:Boolean = false;
      
      internal var var_2798:Boolean = false;
      
      internal var var_2470:Boolean = false;
      
      internal var var_2227:Boolean = false;
      
      internal var var_2122:Boolean = false;
      
      internal var var_1176:uint;
      
      internal var var_1157:uint;
      
      internal var var_1910:Boolean = false;
      
      internal var var_354:Array;
      
      public function CombatState(param1:Entity)
      {
         super();
         this.var_2145 = param1.appearPosX;
         this.var_2313 = param1.appearPosY;
         this.var_3 = param1;
         this.var_1 = this.var_3.var_1;
         this.var_114 = new Dictionary();
         this.var_1654 = new Dictionary();
         this.var_1057 = new Dictionary();
         this.var_577 = new Dictionary();
         this.var_84 = new Vector.<Buff>();
         this.var_372 = new Vector.<SuperAnimInstance>();
         this.var_554 = new Vector.<ActivePower>();
      }
      
      public static function method_255(param1:Point, param2:Point, param3:Entity) : Boolean
      {
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:Number = param3.entType.width;
         var _loc10_:Number = param3.entType.height;
         if(_loc9_ < _loc10_)
         {
            _loc4_ = _loc9_ * 0.5;
            _loc5_ = param3.appearPosX;
            _loc6_ = param3.appearPosY - _loc4_;
            _loc7_ = 0;
            _loc8_ = -_loc10_ + _loc9_;
         }
         else
         {
            _loc4_ = _loc10_ * 0.5;
            _loc5_ = param3.appearPosX - _loc9_ * 0.5 + _loc4_;
            _loc6_ = param3.var_12;
            _loc7_ = _loc9_ - _loc10_;
            _loc8_ = 0;
         }
         return MathUtil.method_1246(param1.x,param1.y,param2.x,param2.y,var_2075,_loc5_,_loc6_,_loc7_,_loc8_,_loc4_);
      }
      
      public function method_1206() : void
      {
         var _loc1_:Buff = null;
         var _loc2_:SuperAnimInstance = null;
         var _loc3_:ActivePower = null;
         for each(_loc1_ in this.var_84)
         {
            _loc1_.method_258();
         }
         this.var_84 = null;
         this.var_1574 = null;
         for each(_loc2_ in this.var_372)
         {
            _loc2_.DestroySuperAnimInstance();
         }
         this.var_372 = null;
         this.var_1057 = null;
         this.var_577 = null;
         this.var_114 = null;
         this.var_1654 = null;
         this.var_354 = null;
         if(this.mActivePower)
         {
            this.mActivePower.method_129();
         }
         this.mActivePower = null;
         for each(_loc3_ in this.var_554)
         {
            _loc3_.method_129();
         }
         this.var_554 = null;
         this.var_1299 = null;
         this.var_3 = null;
         this.var_1 = null;
      }
      
      public function method_135(param1:BuffType) : Buff
      {
         var _loc2_:Buff = null;
         for each(_loc2_ in this.var_84)
         {
            if(param1 == _loc2_.type)
            {
               return _loc2_;
            }
         }
         return null;
      }
      
      public function AddBuff(param1:BuffType, param2:Entity, param3:uint, param4:uint, param5:int = 1, param6:Vector.<class_140> = null, param7:int = 0, param8:Entity = null) : void
      {
         var _loc11_:PowerType = null;
         var _loc12_:Entity = null;
         var _loc9_:Boolean;
         if((_loc9_ = Entity.method_574(param2,this.var_3)) && !param1.var_774 || !_loc9_ && param1.var_774)
         {
            return;
         }
         if(param1.var_2859 && (!this.var_3.behaviorType || !this.var_3.behaviorType.var_679))
         {
            return;
         }
         if(param1.var_774 && this.var_2151)
         {
            return;
         }
         if(param1.buffName.indexOf("DetShield") == 0)
         {
            if(this.var_651)
            {
               _loc11_ = class_14.powerTypesDict["DetShieldDetonate" + this.var_651];
               this.method_51(_loc11_,false);
               this.RemoveBuff(class_14.buffTypesDict["DetShield" + this.var_651]);
            }
         }
         if(param1.var_611)
         {
            this.var_3.method_1138(class_14.powerTypesDict[param1.var_611],param1.var_1251);
         }
         var _loc10_:uint = param2.id;
         this.var_1.linkUpdater.method_1262(this.var_3,_loc10_,param1.buffID,param3,param4,param5,param6);
         this.method_522(param1,_loc10_,param5,param3,param4,param6,param7,param8);
         if(param1.buffName == "Prey")
         {
            if(_loc12_ = !!param2.summonerId ? this.var_1.GetEntFromID(param2.summonerId) : param2)
            {
               if(Boolean(_loc12_.combatState.var_1201) && Boolean(_loc12_.combatState.var_1201.combatState))
               {
                  _loc12_.combatState.var_1201.combatState.RemoveBuff(param1);
               }
               _loc12_.combatState.var_1201 = this.var_3;
               _loc12_.method_1658();
            }
         }
      }
      
      public function RemoveAllBuffs() : void
      {
         var _loc2_:Buff = null;
         var _loc1_:int = int(this.var_84.length - 1);
         while(_loc1_ >= 0)
         {
            _loc2_ = this.var_84[_loc1_];
            this.RemoveBuff(_loc2_.type);
            _loc1_--;
         }
      }
      
      public function RemoveBuff(param1:BuffType) : void
      {
         var _loc2_:Buff = this.method_135(param1);
         if(_loc2_)
         {
            _loc2_.method_534();
            _loc2_.method_258();
            this.var_84.splice(this.var_84.indexOf(_loc2_),1);
            this.var_555 = true;
         }
      }
      
      public function method_522(param1:BuffType, param2:uint, param3:uint, param4:uint, param5:uint, param6:Vector.<class_140>, param7:int = 0, param8:Entity = null) : void
      {
         var _loc12_:PowerType = null;
         var _loc13_:int = 0;
         var _loc14_:int = 0;
         var _loc15_:Number = NaN;
         var _loc16_:int = 0;
         var _loc17_:Number = NaN;
         var _loc18_:int = 0;
         var _loc19_:uint = 0;
         var _loc9_:Entity;
         var _loc10_:int = !!(_loc9_ = this.var_1.GetEntFromID(param2)) ? _loc9_.var_64 : 0;
         var _loc11_:Buff;
         if(!(_loc11_ = this.method_135(param1)))
         {
            _loc13_ = !!(_loc12_ = class_14.powerTypes[param5]) ? _loc12_.var_7 : 0;
            if(!param1.buffName.indexOf("Retribution"))
            {
               _loc15_ = this.var_3.magicDamage * 10;
               if(_loc13_ >= 10)
               {
                  _loc15_ = 1.55 * this.var_3.magicDamage * 10;
               }
               else if(_loc13_ >= 9)
               {
                  _loc15_ = 1.3 * this.var_3.magicDamage * 10;
               }
               else if(_loc13_ >= 6)
               {
                  _loc15_ = 1.3 * this.var_3.magicDamage * 9;
               }
               else if(_loc13_ >= 5)
               {
                  _loc15_ = 1.23 * this.var_3.magicDamage * 9;
               }
               else if(_loc13_ >= 4)
               {
                  _loc15_ = 1 * this.var_3.magicDamage * 9;
               }
               else if(_loc13_ >= 2)
               {
                  _loc15_ = this.var_3.magicDamage * 7;
               }
               else if(_loc13_ >= 1)
               {
                  _loc15_ = 0.8 * this.var_3.magicDamage * 7;
               }
               _loc11_ = new Buff(this.var_3,param1,_loc15_,param6);
            }
            else if(param1.buffName == "Thorns")
            {
               _loc11_ = new Buff(this.var_3,param1,this.var_3.magicDamage * 10,param6);
            }
            else if(param1.buffName == "Absorb")
            {
               _loc11_ = new Buff(this.var_3,param1,this.var_3.maxHP / 2,param6);
            }
            else if(param1.buffName.indexOf("DetShield") == 0)
            {
               _loc16_ = int(param1.buffName.substring(9));
               _loc17_ = 4;
               if(_loc16_ >= 10)
               {
                  _loc17_ = 6;
               }
               else if(_loc16_ >= 8)
               {
                  _loc17_ = 5.5;
               }
               else if(_loc16_ >= 6)
               {
                  _loc17_ = 5;
               }
               else if(_loc16_ >= 4)
               {
                  _loc17_ = 4.5;
               }
               if(this.var_2168)
               {
                  _loc17_ += 0.8;
               }
               _loc18_ = Math.floor(this.var_3.magicDamage * _loc17_);
               _loc11_ = new Buff(this.var_3,param1,_loc18_,param6);
            }
            else if(param1.buffName.indexOf("PlagueStackLimit") == 0)
            {
               _loc19_ = 3;
               if(_loc13_ >= 10)
               {
                  _loc19_ = 5;
               }
               else if(_loc13_ >= 5)
               {
                  _loc19_ = 4;
               }
               _loc11_ = new Buff(this.var_3,param1,_loc19_,param6);
            }
            else
            {
               _loc11_ = new Buff(this.var_3,param1,0,param6);
            }
            if(_loc14_ = param1.var_2950 + _loc11_.method_59("Durability"))
            {
               if(_loc9_)
               {
                  _loc11_.var_1590 = _loc14_ * _loc9_.magicDamage;
               }
            }
            if(param1.var_2030)
            {
               if(param8)
               {
                  _loc11_.var_1211 = param8;
               }
               else if(param1.var_774)
               {
                  _loc11_.var_1211 = _loc9_;
               }
            }
            if(this.var_1.clientEntID != this.var_3.id)
            {
               if(param1.buffName.indexOf("IceArmor") == 0)
               {
                  this.var_3.method_262(true,true,_loc13_);
               }
               if(param1.buffName.indexOf("SentinelForm") == 0)
               {
                  this.var_3.method_247(true,true,_loc13_);
               }
               if(param1.buffName.indexOf("SeekingBlades") == 0)
               {
                  this.var_3.method_391(true,true);
               }
               if(param1.buffName.indexOf("ShadowArmor") == 0)
               {
                  this.var_3.method_354(true,true,_loc13_);
               }
            }
            this.var_84.push(_loc11_);
            this.var_555 = true;
         }
         _loc11_.method_1559(param2,param3,param4,param5,_loc10_);
         if(param1.stackCount > 1)
         {
            this.var_555 = true;
         }
         _loc11_.method_1467();
         if(param7)
         {
            _loc11_.var_830 = param7;
         }
      }
      
      public function method_1278(param1:BuffType, param2:uint) : void
      {
         var _loc3_:Buff = this.method_135(param1);
         if(_loc3_)
         {
            if(_loc3_.method_1515(param2))
            {
               this.var_84.splice(this.var_84.indexOf(_loc3_),1);
               this.var_555 = true;
               if(this.var_1.clientEntID != this.var_3.id)
               {
                  if(param1.buffName.indexOf("IceArmor") == 0)
                  {
                     this.var_3.method_262(false,true);
                  }
                  if(param1.buffName.indexOf("SentinelForm") == 0)
                  {
                     this.var_3.method_247(false,true);
                  }
                  if(param1.buffName.indexOf("SeekingBlades") == 0)
                  {
                     this.var_3.method_391(false,true);
                  }
                  if(param1.buffName.indexOf("Pyromania") == 0)
                  {
                     this.var_3.method_475(false,true);
                  }
                  if(param1.buffName.indexOf("ShadowArmor") == 0)
                  {
                     this.var_3.method_354(false,true);
                  }
               }
            }
         }
      }
      
      public function method_841() : void
      {
         var _loc3_:BuffType = null;
         var _loc4_:Buff = null;
         var _loc5_:BuffType = null;
         var _loc1_:Vector.<BuffType> = new Vector.<BuffType>();
         var _loc2_:int = int(this.var_84.length - 1);
         while(_loc2_ >= 0)
         {
            if((Boolean(_loc5_ = (_loc4_ = this.var_84[_loc2_]).type)) && _loc5_.var_1378)
            {
               _loc1_.push(_loc5_);
            }
            _loc2_--;
         }
         for each(_loc3_ in _loc1_)
         {
            this.RemoveBuff(_loc3_);
         }
      }
      
      public function method_2127() : void
      {
         var _loc3_:BuffType = null;
         var _loc4_:Buff = null;
         var _loc5_:BuffType = null;
         var _loc1_:Vector.<BuffType> = new Vector.<BuffType>();
         var _loc2_:int = int(this.var_84.length - 1);
         while(_loc2_ >= 0)
         {
            if((Boolean(_loc5_ = (_loc4_ = this.var_84[_loc2_]).type)) && Boolean(_loc5_.var_1063))
            {
               _loc1_.push(_loc5_);
            }
            _loc2_--;
         }
         for each(_loc3_ in _loc1_)
         {
            this.RemoveBuff(_loc3_);
         }
      }
      
      private function method_322() : void
      {
         var _loc1_:String = null;
         var _loc8_:Buff = null;
         var _loc11_:Object = null;
         var _loc12_:String = null;
         var _loc13_:Object = null;
         var _loc14_:String = null;
         var _loc15_:Number = NaN;
         var _loc16_:BuffType = null;
         var _loc17_:Boolean = false;
         var _loc18_:class_141 = null;
         var _loc19_:Number = NaN;
         var _loc20_:Number = NaN;
         var _loc21_:Number = NaN;
         var _loc22_:Number = NaN;
         var _loc23_:Number = NaN;
         var _loc24_:Number = NaN;
         var _loc25_:Number = NaN;
         var _loc26_:Number = NaN;
         var _loc27_:Number = NaN;
         var _loc28_:Number = NaN;
         var _loc29_:Number = NaN;
         var _loc30_:String = null;
         var _loc31_:uint = 0;
         var _loc32_:Number = NaN;
         var _loc33_:Number = NaN;
         var _loc34_:Number = NaN;
         var _loc35_:Number = NaN;
         var _loc36_:Number = NaN;
         var _loc37_:class_141 = null;
         var _loc38_:PowerType = null;
         if(!this.var_555)
         {
            return;
         }
         var _loc2_:Boolean = this.var_1278;
         var _loc3_:Boolean = this.var_1559;
         var _loc4_:String = this.var_270;
         var _loc5_:String = this.var_724;
         var _loc6_:Boolean = this.var_823;
         var _loc7_:uint = this.var_1176;
         this.var_1176 = 0;
         this.var_288 = 0;
         this.var_495 = 0;
         this.var_360 = 0;
         this.var_292 = 0;
         this.var_540 = 0;
         this.var_2405 = 0;
         this.var_984 = 0;
         this.var_546 = 0;
         this.var_1083 = 0;
         this.var_1651 = null;
         this.var_1823 = null;
         this.var_270 = null;
         this.var_724 = null;
         this.var_683 = false;
         this.var_2291 = false;
         this.var_445 = false;
         this.var_1488 = false;
         this.var_1278 = false;
         this.var_1559 = false;
         this.var_414 = false;
         this.var_2218 = false;
         this.var_1421 = false;
         this.var_1923 = false;
         this.var_1905 = false;
         this.var_1819 = false;
         this.var_823 = false;
         this.var_840 = 0;
         for(_loc1_ in this.var_1057)
         {
            delete this.var_1057[_loc1_];
         }
         for(_loc1_ in this.var_577)
         {
            delete this.var_577[_loc1_];
         }
         this.var_1298 = false;
         this.var_1033 = 0;
         this.var_2246 = false;
         this.var_1710 = 0;
         this.var_1674 = 0;
         this.var_1797 = 0;
         this.var_2043 = 0;
         this.var_651 = 0;
         this.var_1139 = 1;
         this.var_2151 = false;
         this.var_1102 = false;
         this.var_1515 = false;
         this.var_1999 = false;
         this.var_1091 = 0;
         this.var_963 = false;
         this.var_1171 = false;
         this.var_931 = 0;
         this.var_598 = 0;
         this.var_552 = 0;
         this.var_576 = 0;
         this.var_2689 = false;
         this.var_1234 = 0;
         this.var_1181 = 0;
         this.var_1556 = 0;
         this.var_1192 = 0;
         this.var_1738 = 0;
         this.var_2146 = false;
         this.var_1981 = 0;
         this.var_1786 = 0;
         this.var_1032 = 0;
         this.var_2045 = 0;
         this.var_1313 = false;
         this.var_2069 = false;
         this.var_1957 = false;
         this.var_2111 = 0;
         this.var_1857 = null;
         this.var_2953 = 0;
         this.var_2096 = false;
         this.var_2114 = false;
         this.var_1188 = 0;
         this.var_1815 = 0;
         this.var_2195 = 0;
         this.var_1483 = 0;
         this.var_1557 = 0;
         this.var_1433 = 0;
         this.var_1310 = 0;
         this.var_1455 = 0;
         this.var_1521 = 0;
         this.var_1527 = 0;
         this.var_1644 = 0;
         this.var_1204 = 0;
         this.var_1669 = false;
         this.var_1414 = 0;
         this.var_1093 = 0;
         this.var_1424 = 0;
         this.var_1311 = 0;
         this.var_1410 = 0;
         this.var_1595 = 0;
         this.var_1574 = null;
         this.var_1567 = 0;
         this.var_923 = 0;
         this.var_971 = 0;
         this.var_1428 = 0;
         this.var_2168 = false;
         this.var_2400 = false;
         this.var_2419 = false;
         this.var_2279 = false;
         this.var_2798 = false;
         this.var_2470 = false;
         this.var_2227 = false;
         if(this.var_3.var_18)
         {
            _loc11_ = this.var_3.var_18.var_1030;
            for(_loc12_ in _loc11_)
            {
               _loc13_ = _loc11_[_loc12_];
               _loc14_ = String(_loc13_);
               _loc15_ = Number(_loc13_);
               if(_loc12_.indexOf("ContactPoison") == 0)
               {
                  this.var_2195 += _loc15_;
               }
               else if(_loc12_.indexOf("Pounce") == 0)
               {
                  this.var_1483 += _loc15_;
               }
               else if(_loc12_.indexOf("IgniteCrit") == 0)
               {
                  this.var_1557 += _loc15_;
               }
               else if(_loc12_.indexOf("Fury") == 0)
               {
                  this.var_1433 += int(_loc15_);
               }
               else if(_loc12_.indexOf("PainEater") == 0)
               {
                  this.var_1310 += int(_loc15_);
               }
               else if(_loc12_.indexOf("FireShield") == 0)
               {
                  this.var_1455 += int(_loc15_);
               }
               else if(_loc12_.indexOf("Heroism") == 0)
               {
                  this.var_1521 += _loc15_;
               }
               else if(_loc12_.indexOf("Vigor") == 0)
               {
                  this.var_1527 += _loc15_;
               }
               else if(_loc12_.indexOf("Dominate") == 0)
               {
                  this.var_1644 += _loc15_;
               }
               else if(_loc12_.indexOf("SentinelArmor") == 0)
               {
                  this.var_1204 += _loc15_;
               }
               else if(_loc12_.indexOf("Blaze") == 0)
               {
                  this.var_1414 += _loc15_;
               }
               else if(_loc12_.indexOf("Harmony") == 0)
               {
                  this.var_1093 += _loc15_;
               }
               else if(_loc12_.indexOf("Conserve") == 0)
               {
                  this.var_1424 += _loc15_;
               }
               else if(_loc12_.indexOf("ShadowRefuge") == 0)
               {
                  this.var_1311 += _loc15_;
               }
               else if(_loc12_.indexOf("Taunt") == 0)
               {
                  this.var_984 += _loc15_;
               }
               else if(_loc12_.indexOf("TwistHex") == 0)
               {
                  this.var_1410 += _loc15_;
               }
               else if(_loc12_.indexOf("WindCloak") == 0)
               {
                  this.var_1595 += _loc15_;
               }
               else if(_loc12_.indexOf("MinionMaster") == 0)
               {
                  this.var_1574 = _loc14_;
               }
               else if(_loc12_.indexOf("CurseCrit") == 0)
               {
                  this.var_1567 += _loc15_;
               }
               else if(_loc12_.indexOf("CurseArmor") == 0)
               {
                  this.var_923 += _loc15_;
               }
               else if(_loc12_.indexOf("CurseSword") == 0)
               {
                  this.var_971 += _loc15_;
               }
               else if(_loc12_.indexOf("ClutchHeal") == 0)
               {
                  this.var_1428 += _loc15_;
               }
               switch(_loc12_)
               {
                  case "RuneBarrier":
                     this.var_2168 = true;
                     break;
                  case "RuneShadowBlade":
                     this.var_2400 = true;
                     break;
                  case "RuneShadowArmor":
                     this.var_2419 = true;
                     break;
                  case "RuneFlamethrower":
                     this.var_2279 = true;
                     break;
                  case "RuneDecoy":
                     this.var_2798 = true;
                     break;
                  case "RunePermafrostClone":
                     this.var_2470 = true;
                     break;
                  case "RuneLeapStrike":
                     this.var_2227 = true;
                     break;
               }
            }
         }
         for each(_loc8_ in this.var_84)
         {
            _loc16_ = _loc8_.type;
            _loc17_ = false;
            for each(_loc18_ in _loc8_.var_47)
            {
               if(_loc18_.entID == this.var_1.clientEntID)
               {
                  _loc17_ = true;
                  break;
               }
            }
            _loc19_ = _loc8_.method_59("MagicDamage");
            _loc20_ = _loc8_.method_59("MeleeDamage");
            _loc21_ = _loc8_.method_59("MagicDefense");
            _loc22_ = _loc8_.method_59("MeleeDefense");
            _loc23_ = _loc8_.method_59("SpeedChange");
            _loc24_ = _loc8_.method_59("AggroChange");
            _loc25_ = _loc8_.method_59("HasteBonus");
            _loc26_ = _loc8_.method_59("ProcChance");
            _loc27_ = _loc8_.method_59("Recovery");
            _loc28_ = _loc8_.method_59("TargetDodgeChance");
            _loc29_ = 1 - this.var_3.var_1065;
            _loc30_ = _loc16_.var_2477;
            _loc31_ = _loc8_.method_351();
            if(_loc30_)
            {
               _loc32_ = Number(this.var_1057[_loc30_]);
               _loc33_ = Number(this.var_577[_loc30_]);
               _loc34_ = _loc16_.var_1597 * _loc31_ + _loc21_ * _loc31_;
               _loc35_ = _loc16_.var_1322 * _loc31_ + _loc22_ * _loc31_;
               this.var_1057[_loc30_] = !!_loc32_ ? _loc32_ + _loc34_ : _loc34_;
               this.var_577[_loc30_] = !!_loc33_ ? _loc33_ + _loc35_ : _loc35_;
            }
            else
            {
               if(_loc16_.var_774 && Boolean(_loc29_))
               {
                  this.var_288 += (_loc16_.magicDamage + _loc19_) * _loc31_ * _loc29_;
                  this.var_495 += (_loc16_.meleeDamage + _loc20_) * _loc31_ * _loc29_;
                  this.var_360 += (_loc16_.var_1597 + _loc21_) * _loc31_ * _loc29_;
                  this.var_292 += (_loc16_.var_1322 + _loc22_) * _loc31_ * _loc29_;
                  this.var_840 += (_loc16_.var_491 + _loc25_) * _loc31_ * _loc29_;
                  this.var_1181 += (_loc16_.var_1086 + _loc26_) * _loc31_ * _loc29_;
                  this.var_1556 += _loc16_.var_2700 * _loc31_ * _loc29_;
                  this.var_1192 += _loc16_.var_663 * _loc31_ * _loc29_;
                  this.var_546 += (_loc16_.var_915 + _loc27_) * _loc31_ * _loc29_;
               }
               else
               {
                  this.var_288 += (_loc16_.magicDamage + _loc19_) * _loc31_;
                  this.var_495 += (_loc16_.meleeDamage + _loc20_) * _loc31_;
                  this.var_360 += (_loc16_.var_1597 + _loc21_) * _loc31_;
                  this.var_292 += (_loc16_.var_1322 + _loc22_) * _loc31_;
                  this.var_840 += (_loc16_.var_491 + _loc25_) * _loc31_;
                  this.var_1181 += (_loc16_.var_1086 + _loc26_) * _loc31_;
                  this.var_1556 += _loc16_.var_2700 * _loc31_;
                  this.var_1192 += _loc16_.var_663 * _loc31_;
                  this.var_546 += (_loc16_.var_915 + _loc27_) * _loc31_;
               }
               this.var_683 = this.var_683 || _loc16_.var_668;
               this.var_445 = this.var_445 || _loc16_.var_953;
               this.var_1488 = this.var_1488 || _loc16_.bDisabled;
               this.var_1278 = this.var_1278 || _loc16_.var_1961;
               this.var_1559 = this.var_1559 || _loc16_.var_876;
               this.var_2218 = this.var_2218 || _loc16_.var_2802;
               this.var_1421 = this.var_1421 || _loc16_.bUntargetable;
               this.var_1923 = this.var_1923 || _loc16_.var_2548;
               this.var_1905 = this.var_1905 || _loc16_.var_2684;
               this.var_1819 = this.var_1819 || _loc16_.var_2775;
               this.var_414 = this.var_414 || _loc16_.var_2050;
               this.var_823 = this.var_823 || _loc16_.var_2494;
               if(_loc16_.var_2125)
               {
                  this.var_1651 = _loc16_.var_2125;
               }
               if(_loc16_.var_2287)
               {
                  this.var_1823 = _loc16_.var_2287;
               }
               if((Boolean(_loc16_.speedChange) || Boolean(_loc23_)) && !_loc16_.var_1378)
               {
                  _loc36_ = _loc16_.speedChange * _loc31_ + _loc23_ * _loc31_;
                  if(_loc16_.speedChange < 0)
                  {
                     if(_loc36_ > -1 && Boolean(_loc29_))
                     {
                        _loc36_ *= _loc29_;
                     }
                     this.var_540 = _loc36_ < this.var_540 ? _loc36_ : this.var_540;
                  }
                  else if(this.var_540 >= 0)
                  {
                     this.var_540 = _loc36_ > this.var_540 ? _loc36_ : this.var_540;
                  }
               }
               if(_loc16_.var_1378 && Boolean(this.var_3.mEquipMount))
               {
                  this.var_270 = this.var_3.mEquipMount.var_566;
                  if(_loc16_.speedChange)
                  {
                     this.var_2405 = _loc16_.speedChange;
                  }
               }
               if(_loc16_.var_1063)
               {
                  this.var_724 = _loc16_.var_1063;
               }
               if(Boolean(_loc16_.var_2397) || Boolean(_loc24_))
               {
                  this.var_984 += _loc16_.var_2397 * _loc31_ + _loc24_ * _loc31_;
               }
               if(_loc16_.var_2362)
               {
                  this.var_1083 += _loc16_.var_2362 * _loc31_;
               }
               if(_loc16_.var_1446)
               {
                  this.var_1738 += (_loc16_.var_1446 + _loc28_) * _loc31_;
               }
               if(_loc16_.var_753)
               {
                  this.var_1298 = true;
               }
               if(_loc16_.var_774)
               {
                  ++this.var_2111;
               }
               this.var_1102 = this.var_1102 || _loc16_.var_2648;
               this.var_1515 = this.var_1515 || _loc16_.var_2250;
               this.var_1999 = this.var_1999 || _loc16_.var_2845;
               if(_loc16_.var_2403)
               {
                  this.var_1091 += _loc8_.method_351();
               }
               this.var_1313 = this.var_1313 || _loc16_.var_2499;
               this.var_1176 |= _loc8_.type.var_76;
               switch(_loc16_.buffName)
               {
                  case "Staggered":
                     this.var_2291 = true;
                     break;
                  case "Bound":
                     this.var_1033 = _loc31_;
                     break;
                  case "LifeWard":
                     this.var_2246 = true;
                     break;
                  case "Thorns":
                     this.var_1674 += _loc8_.var_619 - _loc8_.var_590;
                     break;
                  case "Sacred":
                     this.var_2151 = true;
                     break;
                  case "Cursed":
                     this.var_963 = true;
                     break;
                  case "MinorCurse":
                     this.var_1171 = true;
                     break;
                  case "SeekingBlades":
                     if(_loc8_ && _loc8_.var_47 && _loc8_.var_47.length > 0)
                     {
                        _loc37_ = _loc8_.var_47[_loc8_.var_47.length - 1];
                        _loc38_ = class_14.powerTypes[_loc37_.var_342];
                        this.var_931 = _loc38_.var_7;
                     }
                     break;
                  case "Retribution":
                  case "Retribution1":
                  case "Retribution7":
                     if(_loc8_ && _loc8_.var_47 && _loc8_.var_47.length > 0)
                     {
                        _loc37_ = _loc8_.var_47[_loc8_.var_47.length - 1];
                        _loc38_ = class_14.powerTypes[_loc37_.var_342];
                        this.var_552 = _loc38_.var_7;
                     }
                     this.var_1710 += _loc8_.var_619 - _loc8_.var_590;
                     break;
                  case "Haunted":
                     this.var_2689 = true;
                     break;
                  case "Ignite":
                     this.var_1234 = _loc31_;
                     break;
                  case "Doomed":
                     this.var_1139 = -1;
                     break;
                  case "Berserk":
                     this.var_2146 = true;
                     break;
                  case "Flammable":
                     this.var_1981 = _loc31_;
                     break;
                  case "Scorched":
                     this.var_1786 = _loc31_;
                     break;
                  case "Bleeding":
                     this.var_1032 = _loc31_;
                     break;
                  case "Burned":
                     this.var_2045 = _loc31_;
                     break;
                  case "HealingBane":
                     if(this.var_1139 > 0)
                     {
                        this.var_1139 *= 0.5;
                     }
                     break;
                  case "FrostShock":
                     this.var_1957 = true;
                     break;
                  case "IceArmor":
                     this.var_2069 = true;
                     break;
                  case "FireBrand":
                  case "FireBrandRank1":
                  case "FireBrandRank3":
                  case "FireBrandRank6":
                  case "FireBrandRank8":
                     if(_loc8_ && _loc8_.var_47 && _loc8_.var_47.length > 0)
                     {
                        _loc37_ = _loc8_.var_47[_loc8_.var_47.length - 1];
                        _loc38_ = class_14.powerTypes[_loc37_.var_342];
                        this.var_598 = _loc38_.var_7;
                     }
                     break;
                  case "Weakened":
                     this.var_2096 = true;
                     break;
                  case "Enfeeble":
                  case "Enfeeble30":
                  case "Enfeeble45":
                  case "Enfeeble60":
                     this.var_2114 = true;
                     break;
                  case "SigilSentinelArmor":
                     this.var_1669 = true;
                     this.var_360 += this.var_1204;
                     this.var_292 += this.var_1204;
                     break;
                  case "PlagueStackLimit":
                     this.var_1815 += _loc8_.var_619 - _loc8_.var_590;
               }
               if(_loc16_.buffName.indexOf("ShadowArmor") == 0)
               {
                  if(this.var_2419)
                  {
                     this.var_360 += 0.1;
                     this.var_292 += 0.1;
                  }
                  if(_loc8_ && _loc8_.var_47 && _loc8_.var_47.length > 0)
                  {
                     _loc37_ = _loc8_.var_47[_loc8_.var_47.length - 1];
                     _loc38_ = class_14.powerTypes[_loc37_.var_342];
                     this.var_576 = _loc38_.var_7;
                  }
               }
               else if(_loc16_.buffName.indexOf("PlagueBattalion") == 0)
               {
                  if(_loc8_ && _loc8_.var_47 && _loc8_.var_47.length > 0)
                  {
                     _loc37_ = _loc8_.var_47[_loc8_.var_47.length - 1];
                     _loc38_ = class_14.powerTypes[_loc37_.var_342];
                     this.var_1188 = _loc38_.var_7;
                  }
               }
               else if(_loc16_.buffName.indexOf("DetShield") == 0)
               {
                  if(_loc8_ && _loc8_.var_47 && _loc8_.var_47.length > 0)
                  {
                     _loc37_ = _loc8_.var_47[_loc8_.var_47.length - 1];
                     _loc38_ = class_14.powerTypes[_loc37_.var_342];
                     this.var_651 = _loc38_.var_7;
                  }
                  this.var_2043 = _loc8_.var_619;
                  if(!_loc8_.var_1114)
                  {
                     this.var_1797 += _loc8_.var_619 - _loc8_.var_590;
                  }
               }
               if(_loc16_.var_1035)
               {
                  this.var_1857 = _loc16_.var_1035;
               }
            }
         }
         this.var_555 = false;
         if(Boolean(this.var_3.var_20 & Entity.PLAYER) || Boolean(this.var_3.summonerId))
         {
            if(this.var_495 > const_299)
            {
               this.var_495 = const_299;
            }
            if(this.var_288 > const_299)
            {
               this.var_288 = const_299;
            }
            if(this.var_292 > const_386)
            {
               this.var_292 = const_386;
            }
            if(this.var_360 > const_386)
            {
               this.var_360 = const_386;
            }
         }
         if(this.var_495 < const_354)
         {
            this.var_495 = const_354;
         }
         if(this.var_288 < const_354)
         {
            this.var_288 = const_354;
         }
         if(this.var_360 < const_332)
         {
            this.var_360 = const_332;
         }
         if(this.var_292 < const_332)
         {
            this.var_292 = const_332;
         }
         var _loc9_:* = this.var_1278 != _loc2_;
         var _loc10_:* = this.var_1559 != _loc3_;
         if(this.var_683 || this.var_445 || _loc9_ || _loc10_)
         {
            if(Boolean(this.var_3.gfx) && Boolean(this.var_3.gfx.m_Seq))
            {
               this.var_3.gfx.m_Seq.method_428();
            }
            if(this.mActivePower)
            {
               this.mActivePower.method_640();
            }
            this.mActivePower = null;
         }
         if((_loc9_ || _loc10_) && Boolean(this.var_3.brain))
         {
            this.var_3.brain.ClearHateList();
            if(_loc9_ && this.var_3.team != Entity.NEUTRAL)
            {
               this.var_3.team = this.var_3.team == Entity.GOODGUY ? Entity.BADGUY : Entity.GOODGUY;
            }
         }
         if(this.var_270 != _loc4_ && (_loc4_ == null || this.var_270 == null))
         {
            this.var_3.method_1088(EntType.method_48(this.var_270));
         }
         if(this.var_724 != _loc5_)
         {
            this.var_3.method_2002(EntType.method_48(this.var_724));
         }
         if(Boolean(this.var_3.gfx) && Boolean(this.var_3.gfx.m_TheDO))
         {
            this.var_3.gfx.m_TheDO.alpha = this.var_414 ? 0.5 : 1;
         }
         this.var_3.RecalculateSpeed();
         if(!this.var_823 && _loc6_)
         {
            this.var_3.method_343();
         }
         if(this.var_1176 != _loc7_)
         {
            this.var_1910 = true;
         }
      }
      
      public function method_1200(param1:Number, param2:Number = 0) : Boolean
      {
         var _loc3_:Number = Math.random();
         var _loc4_:Number = this.var_3.var_1086 * (1 + this.var_1181 + param2) * param1;
         return _loc3_ < _loc4_;
      }
      
      public function method_72(param1:PowerType, param2:Entity, param3:Point, param4:int, param5:uint) : void
      {
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         if(!param1 || !param1.var_301)
         {
            return;
         }
         var _loc6_:Number = 0;
         if(param1.var_879)
         {
            _loc6_ = param1.method_1773(param2);
         }
         if(param1.powerName == "ProcMassive")
         {
            _loc6_ = const_1248;
         }
         if(param1.powerName == "ProcMassiveTime")
         {
            _loc6_ = const_998;
         }
         if(param1.powerName == "ProcHeal")
         {
            _loc6_ = const_1282;
         }
         if(param1.powerName == "ProcHealTime")
         {
            _loc6_ = const_1060;
         }
         if(param1.var_470)
         {
            param4 *= 1 + _loc6_ + this.var_3.var_667 + this.var_3.var_640;
         }
         if(param1.var_2426)
         {
            _loc8_ = this.var_3.meleeDamage * (1 + this.var_495 + this.var_3.totalMods.meleeDamage);
            _loc9_ = this.var_3.magicDamage * (1 + this.var_288 + this.var_3.totalMods.magicDamage);
            param4 *= _loc9_ / _loc8_;
         }
         var _loc7_:ActivePower;
         (_loc7_ = new ActivePower(this.var_1,param1,this.var_3,param2,param3,0,0,0,false)).var_803 = param4;
         _loc7_.var_249 = param5;
         _loc7_.method_243();
         _loc7_.method_129();
      }
      
      public function ResetCooldownsAndImmunity() : void
      {
         this.var_114 = new Dictionary();
         this.var_1654 = new Dictionary();
      }
      
      private function method_1910(param1:PowerType) : Entity
      {
         var _loc5_:class_133 = null;
         var _loc6_:Entity = null;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         var _loc10_:Number = NaN;
         var _loc11_:Number = NaN;
         var _loc2_:Entity = this.var_3;
         var _loc3_:Number = this.var_3.currHP / this.var_3.maxHP;
         var _loc4_:Number = param1.method_63(this.var_3);
         for each(_loc5_ in this.var_1.groupmates)
         {
            if(!(!(_loc6_ = this.var_1.GetPlayerEntFromEntName(_loc5_.charName)) || _loc6_.currHP <= 0))
            {
               if((_loc7_ = _loc6_.currHP / _loc6_.maxHP) <= _loc3_)
               {
                  _loc8_ = Math.abs(_loc6_.var_10 - this.var_3.var_10);
                  _loc9_ = Math.abs(_loc6_.var_12 - this.var_3.var_12);
                  _loc10_ = _loc6_.entType.width * 0.5 + this.var_3.entType.width * 0.5;
                  _loc11_ = _loc6_.entType.height * 0.5 + this.var_3.entType.height * 0.5;
                  if(_loc8_ <= _loc4_ + _loc10_ && _loc9_ <= _loc4_ + _loc11_)
                  {
                     _loc3_ = _loc7_;
                     _loc2_ = _loc6_;
                  }
               }
            }
         }
         return _loc2_;
      }
      
      private function method_1513(param1:PowerType) : Entity
      {
         var _loc8_:Entity = null;
         var _loc9_:Number = NaN;
         var _loc10_:Boolean = false;
         var _loc11_:Number = NaN;
         var _loc2_:Entity = null;
         var _loc3_:Number = 0;
         var _loc4_:Boolean = false;
         var _loc5_:Boolean = this.var_3.bFacingLeft();
         var _loc6_:uint = param1.damageMultFull < 0 ? Game.FRIEND : Game.ENEMY;
         var _loc7_:Array = this.var_1.GatherEntities(this.var_3,this.var_3.var_10,this.var_3.var_12,Camera.SCREEN_WIDTH,Camera.SCREEN_HEIGHT * 0.25,_loc6_);
         for each(_loc8_ in _loc7_)
         {
            if(!(Boolean(this.var_3.var_20 & Entity.PLAYER) && !this.var_1.PointOnScreenWithinDist(_loc8_.var_10,_loc8_.var_12,_loc8_.entType.width * 0.5,_loc8_.entType.height * 0.5)))
            {
               if(_loc8_.id == this.var_3.var_485)
               {
                  _loc2_ = _loc8_;
                  break;
               }
               _loc10_ = (_loc9_ = _loc8_.appearPosX - this.var_3.appearPosX) <= 0 && _loc5_ || _loc9_ >= 0 && !_loc5_;
               _loc11_ = _loc9_ >= 0 ? _loc9_ : -_loc9_;
               if(_loc10_ && (!_loc2_ || _loc11_ > _loc3_))
               {
                  _loc4_ = _loc10_;
                  _loc2_ = _loc8_;
                  _loc3_ = _loc11_;
               }
            }
         }
         return _loc2_;
      }
      
      private function method_1322(param1:PowerType) : Entity
      {
         var _loc6_:Array = null;
         var _loc14_:Entity = null;
         var _loc15_:Number = NaN;
         var _loc16_:Number = NaN;
         var _loc17_:Number = NaN;
         var _loc18_:Number = NaN;
         var _loc19_:Boolean = false;
         var _loc20_:* = false;
         var _loc21_:int = 0;
         var _loc2_:PowerType = this.var_3.GetMeleePower();
         var _loc3_:Number = param1.method_63(this.var_3);
         var _loc4_:Number = !!_loc2_ ? _loc2_.method_63(this.var_3) : 0;
         var _loc5_:uint = param1.damageMultFull < 0 ? Game.FRIEND : Game.ENEMY;
         if(param1.var_6 == PowerType.TARGETMETHOD_MELEE || param1.var_6 == PowerType.const_46)
         {
            _loc6_ = this.var_1.GatherEntities(this.var_3,this.var_3.var_10,this.var_3.var_12,_loc3_,this.var_3.entType.height * 0.5,_loc5_ | Game.MELEEABLE | Game.INTENTIONAL_MELEE);
         }
         else
         {
            _loc6_ = this.var_1.GatherEntities(this.var_3,this.var_3.var_10,this.var_3.var_12,_loc3_,_loc3_,_loc5_);
         }
         var _loc7_:Entity = null;
         var _loc8_:Number = 0;
         var _loc9_:Boolean = false;
         var _loc10_:Boolean = false;
         var _loc11_:Number = _loc4_ * _loc4_;
         var _loc12_:Boolean = this.var_3.bFacingLeft();
         var _loc13_:Boolean = param1.var_6 == PowerType.const_46 && param1.var_820 && Boolean(param1.var_108) && param1.var_108.length > 1;
         for each(_loc14_ in _loc6_)
         {
            if(!(Boolean(this.var_3.var_20 & Entity.PLAYER) && !this.var_1.PointOnScreenWithinDist(_loc14_.var_10,_loc14_.var_12,_loc14_.entType.width * 0.5,_loc14_.entType.height * 0.5)))
            {
               _loc15_ = _loc14_.var_10 - this.var_3.var_10;
               _loc16_ = _loc14_.var_12 - this.var_3.var_12;
               _loc17_ = _loc15_ * _loc15_;
               _loc18_ = _loc16_ * _loc16_ + _loc17_;
               _loc19_ = _loc15_ <= 0 && _loc12_ || _loc15_ >= 0 && !_loc12_;
               _loc20_ = _loc17_ <= _loc11_;
               _loc21_ = !!_loc7_ ? _loc14_.entType.var_138 - _loc7_.entType.var_138 : 1;
               if((_loc19_ || !_loc13_) && _loc21_ >= 0)
               {
                  if(Boolean(_loc21_) || (_loc20_ && !_loc9_ || _loc19_ && !_loc10_ || _loc18_ < _loc8_))
                  {
                     _loc7_ = _loc14_;
                     _loc9_ = _loc20_;
                     _loc10_ = _loc19_;
                     _loc8_ = _loc18_;
                  }
               }
            }
         }
         return _loc7_;
      }
      
      public function method_656(param1:PowerType) : Entity
      {
         var _loc6_:Array = null;
         var _loc14_:Entity = null;
         var _loc15_:Number = NaN;
         var _loc16_:Number = NaN;
         var _loc17_:Number = NaN;
         var _loc18_:Number = NaN;
         var _loc19_:Boolean = false;
         var _loc20_:* = false;
         if(this.var_3.brain)
         {
            if(param1.var_6 == PowerType.const_32)
            {
               return this.var_3.brain.target;
            }
            if(this.var_3.behaviorType.var_2731)
            {
               return this.method_1322(param1);
            }
         }
         if(param1.var_6 == PowerType.TARGETMETHOD_FRIEND)
         {
            return this.method_1910(param1);
         }
         if(param1.var_6 == PowerType.const_32 || param1.basePowerName == "LeapStrike")
         {
            return this.method_1513(param1);
         }
         if(param1.var_6 == PowerType.const_201)
         {
            return null;
         }
         var _loc2_:PowerType = this.var_3.GetMeleePower();
         var _loc3_:Number = param1.method_63(this.var_3);
         var _loc4_:Number = !!_loc2_ ? _loc2_.method_63(this.var_3) : 0;
         var _loc5_:uint = param1.damageMultFull < 0 ? Game.FRIEND : Game.ENEMY;
         if(param1.var_6 == PowerType.const_248 || param1.var_6 == PowerType.const_259)
         {
            _loc5_ = Game.FRIEND;
         }
         else if(param1.var_1867)
         {
            _loc5_ = 0;
         }
         if(param1.var_6 == PowerType.TARGETMETHOD_MELEE || param1.var_6 == PowerType.const_46)
         {
            _loc6_ = this.var_1.GatherEntities(this.var_3,this.var_3.var_10,this.var_3.var_12,_loc3_,this.var_3.entType.height * 0.5,_loc5_ | Game.MELEEABLE | Game.INTENTIONAL_MELEE);
         }
         else
         {
            _loc6_ = this.var_1.GatherEntities(this.var_3,this.var_3.var_10,this.var_3.var_12,_loc3_,_loc3_,_loc5_);
         }
         var _loc7_:Entity = null;
         var _loc8_:Number = 0;
         var _loc9_:Boolean = false;
         var _loc10_:Boolean = false;
         var _loc11_:Number = _loc4_ * _loc4_;
         var _loc12_:Boolean = this.var_3.bFacingLeft();
         var _loc13_:Boolean = param1.var_6 == PowerType.const_46 && param1.var_820 && Boolean(param1.var_108) && param1.var_108.length > 1;
         for each(_loc14_ in _loc6_)
         {
            if(!(Boolean(this.var_3.var_20 & Entity.PLAYER) && !this.var_1.PointOnScreenWithinDist(_loc14_.var_10,_loc14_.var_12,_loc14_.entType.width * 0.5,_loc14_.entType.height * 0.5)))
            {
               if(_loc14_.id == this.var_3.var_485)
               {
                  _loc7_ = _loc14_;
                  break;
               }
               if(_loc14_.id == this.var_3.var_1812)
               {
                  _loc7_ = _loc14_;
                  break;
               }
               _loc15_ = _loc14_.var_10 - this.var_3.var_10;
               _loc16_ = _loc14_.var_12 - this.var_3.var_12;
               _loc17_ = _loc15_ * _loc15_;
               _loc18_ = _loc16_ * _loc16_ + _loc17_;
               _loc19_ = _loc15_ <= 0 && _loc12_ || _loc15_ >= 0 && !_loc12_;
               _loc20_ = _loc17_ <= _loc11_;
               if((_loc19_ || !_loc13_) && (!_loc7_ || _loc20_ && !_loc9_ || _loc19_ && !_loc10_ || _loc18_ < _loc8_))
               {
                  _loc7_ = _loc14_;
                  _loc9_ = _loc20_;
                  _loc10_ = _loc19_;
                  _loc8_ = _loc18_;
               }
            }
         }
         return _loc7_;
      }
      
      public function method_678(param1:PowerType) : Boolean
      {
         if(this.method_51(param1,false))
         {
            this.mActivePower.method_299(this.var_3.var_38 != null);
            this.mActivePower.method_243();
            this.mActivePower.method_129();
            this.mActivePower = null;
            return true;
         }
         return false;
      }
      
      public function method_51(param1:PowerType, param2:Boolean, param3:uint = 0, param4:Point = null) : Boolean
      {
         var _loc12_:int = 0;
         var _loc13_:* = false;
         var _loc14_:Point = null;
         var _loc15_:* = false;
         var _loc16_:Boolean = false;
         var _loc17_:* = false;
         var _loc18_:Boolean = false;
         var _loc19_:int = 0;
         var _loc20_:uint = 0;
         if(this.var_3.entState == Entity.const_6 || this.var_683 || this.var_445)
         {
            return false;
         }
         if(Boolean(this.mActivePower) && Boolean(param4))
         {
            return false;
         }
         var _loc5_:uint = this.var_1.mTimeThisTick;
         if(Boolean(this.mActivePower) || !this.method_414(param1))
         {
            this.var_1299 = param1;
            this.var_2531 = _loc5_ + 600;
            _loc12_ = 0;
            if(this.var_3.var_18)
            {
               _loc12_ = this.var_3.var_18.method_102(this.var_3,param1.basePowerName,"ManaCost");
            }
            if(this.var_39 && param1.var_219 && param1.manaCost + _loc12_ > this.var_3.var_31)
            {
               if(this.var_39 == class_14.powerTypesDict["HailstoneEmbrace1"])
               {
                  this.var_3.method_262(false,false);
               }
               else if(this.var_39 == class_14.powerTypesDict["SentinelForm1"])
               {
                  this.var_3.method_247(false,false);
               }
            }
            return false;
         }
         var _loc6_:PowerType = class_14.powerTypesDict["Dismount"];
         if(this.var_270 && _loc6_ != param1 && !param1.var_749)
         {
            this.method_678(_loc6_);
            this.method_322();
            if(this.var_270)
            {
               return false;
            }
         }
         if(this.var_39)
         {
            if(this.var_39 == class_14.powerTypesDict["SentinelForm1"].powerID)
            {
               if(Boolean(param1.var_136) && param1.var_136.indexOf("Melee") >= 0)
               {
                  if(!(_loc13_ = this.var_1.mTimeThisTick - this.var_1900 <= 250) || this.currMeleeCombo >= param1.var_1075)
                  {
                     this.currMeleeCombo = 0;
                  }
                  else
                  {
                     ++this.currMeleeCombo;
                  }
                  if(this.currMeleeCombo == 1)
                  {
                     param1 = class_14.powerTypesDict["SFMeleeCombo" + param1.var_7];
                  }
                  this.var_1900 = _loc5_ + param1.var_287 + param1.var_125;
               }
            }
         }
         if(param2 && Boolean(this.var_3.var_24))
         {
            _loc15_ = (_loc14_ = this.var_3.var_24.method_375(class_36.const_1198)).x < this.var_3.appearPosX;
            if(this.var_3.bFacingLeft() != _loc15_)
            {
               this.var_3.bBackpedal = !this.var_3.bBackpedal;
            }
         }
         var _loc7_:Entity = param1.var_6 == PowerType.TARGETMETHOD_SELF ? this.var_3 : this.method_656(param1);
         if(param1.var_1735 && !_loc7_)
         {
            return false;
         }
         var _loc8_:Point = this.var_3.method_1973(class_36.QUEUEPOWER_POINT2);
         if(Boolean(this.var_3.var_24) || this.var_3.behaviorType && this.var_3.behaviorType.var_2754)
         {
            _loc16_ = this.var_3.bFacingLeft();
            if(Boolean(_loc7_) && _loc7_ != this.var_3)
            {
               this.var_3.var_687 = _loc7_.appearPosX < this.var_3.appearPosX;
            }
            else if(!param1.var_1735 && param2)
            {
               this.var_3.var_687 = _loc8_.x < this.var_3.appearPosX;
            }
            else
            {
               this.var_3.var_687 = _loc16_;
            }
            this.var_3.var_1787 = _loc5_ + param1.var_287 + param1.var_125 + 800;
            if(this.var_3.var_687 != _loc16_)
            {
               this.var_3.bBackpedal = !this.var_3.bBackpedal;
            }
         }
         if(param1.var_136 == "Melee")
         {
            if(!(_loc17_ = this.var_1.mTimeThisTick - this.var_1900 <= 250) || this.currMeleeCombo >= param1.var_1075)
            {
               this.currMeleeCombo = 0;
            }
            else
            {
               ++this.currMeleeCombo;
            }
            this.var_1900 = _loc5_ + param1.var_287 + param1.var_125;
         }
         else if(param1.var_136 == "Shoot")
         {
            if(!(_loc18_ = this.var_1.mTimeThisTick - this.var_2624 <= 250 && (param1.powerName.indexOf("MeteorROR") == -1 && param1.basePowerName != "FlamethrowerROR")) || this.var_1502 >= param1.var_1212)
            {
               this.var_1502 = 0;
            }
            else
            {
               ++this.var_1502;
            }
            this.var_2624 = _loc5_ + param1.var_287 + param1.var_125;
         }
         var _loc9_:Point = new Point(_loc8_.x,_loc8_.y);
         if(!param2 && (param1.var_6 == PowerType.TARGETMETHOD_RANGEDAOE || param1.var_6 == PowerType.const_99 || param1.var_6 == PowerType.const_32 || param1.var_6 == PowerType.const_113 || param1.var_6 == PowerType.const_89 || param1.var_6 == PowerType.const_96))
         {
            if(param1.basePowerName == "PermafrostCloneExplode" || param1.basePowerName == "JusticeFist")
            {
               _loc9_ = new Point(this.var_3.physPosX,this.var_3.physPosY);
            }
            else if(_loc7_)
            {
               _loc9_ = new Point(_loc7_.physPosX,_loc7_.physPosY);
               if(param1.var_6 == PowerType.const_32)
               {
                  _loc19_ = (this.var_3.entType.width + _loc7_.entType.width) * 0.5;
                  _loc9_.x += this.var_3.physPosX < _loc7_.physPosX ? -_loc19_ : _loc19_;
               }
            }
            else
            {
               _loc20_ = param1.method_63(this.var_3);
               _loc9_ = new Point(this.var_3.physPosX,this.var_3.physPosY);
               if(param1.var_6 == PowerType.const_32)
               {
                  _loc9_.x += this.var_3.bFacingLeft() ? -(Camera.SCREEN_WIDTH * 0.5) : Camera.SCREEN_WIDTH * 0.5;
               }
               else
               {
                  _loc9_.x += this.var_3.bFacingLeft() ? -_loc20_ : _loc20_;
               }
            }
         }
         if(param4)
         {
            _loc9_.x = param4.x;
            _loc9_.y = param4.y;
         }
         if(param1.basePowerName == "LeapStrike")
         {
            if(_loc7_)
            {
               _loc9_.x = _loc7_.var_10;
               _loc9_.y = _loc7_.var_12;
            }
            else
            {
               _loc9_.x = this.var_3.bFacingLeft() ? this.var_3.var_10 - 350 : this.var_3.var_10 + 350;
               _loc9_.y = this.var_3.appearPosY;
            }
         }
         var _loc10_:uint = param1.bIsProjectile ? this.var_813++ : 0;
         if(this.var_3.id == this.var_1.clientEntID)
         {
            this.var_1.linkUpdater.method_541(this.var_3);
         }
         this.mActivePower = new ActivePower(this.var_1,param1,this.var_3,_loc7_,_loc9_,_loc10_,this.currMeleeCombo,this.var_1502,false);
         this.mActivePower.var_2532 = _loc5_ + param3;
         var _loc11_:int = 0;
         if(this.var_3.var_18)
         {
            _loc11_ = this.var_3.var_18.method_102(this.var_3,param1.basePowerName,"CooldownTime");
         }
         this.var_114[param1.powerID] = _loc5_ + param1.coolDownTime + _loc11_;
         if(this.var_3.var_20 & Entity.LOCAL && !param1.var_219 && param1.manaCost >= 15)
         {
            if(this.var_1424)
            {
               this.var_1435 += this.var_1424;
            }
            if(this.var_1527)
            {
               this.method_72(class_14.powerTypesDict["ProcAlwaysFullHeal"],this.var_3,new Point(this.var_3.physPosX,this.var_3.physPosY),this.var_1527 * this.var_3.magicDamage,param1.powerID);
            }
         }
         return true;
      }
      
      public function method_414(param1:PowerType) : Boolean
      {
         var _loc2_:int = 0;
         if(this.var_3.var_18)
         {
            _loc2_ = this.var_3.var_18.method_102(this.var_3,param1.basePowerName,"ManaCost");
         }
         if(!this.var_3.brain && param1.var_219 && this.var_3.var_31 < param1.var_535 + _loc2_)
         {
            return false;
         }
         var _loc3_:Number = 1 + this.var_1083;
         if(!this.var_3.brain && this.var_3.var_228 < int(_loc3_ * (param1.var_535 + _loc2_)) && !param1.var_219 && !param1.var_749)
         {
            return false;
         }
         var _loc4_:uint;
         if((_loc4_ = this.var_1.mTimeThisTick) < this.var_114[param1.powerID])
         {
            return false;
         }
         var _loc5_:PowerType;
         if((_loc5_ = class_14.powerTypesDict["SentinelForm1"]) && this.var_39 == _loc5_.powerID && (param1 == this.var_3.hudPowers[1] || param1 == this.var_3.hudPowers[2] || param1 == this.var_3.hudPowers[3] || param1.var_1439 || param1.var_749))
         {
            return false;
         }
         if(this.var_1204 && !this.var_1669 && param1.basePowerName == "SentinelForm")
         {
            this.AddBuff(class_14.buffTypesDict["SigilSentinelArmor"],this.var_3,this.var_3.magicDamage,param1.powerID);
         }
         return true;
      }
      
      public function method_924(param1:Boolean) : Boolean
      {
         if(this.var_1923)
         {
            return true;
         }
         return param1 ? this.var_1905 : this.var_1819;
      }
      
      private function method_1192(param1:PowerType, param2:Entity, param3:Boolean, param4:uint, param5:Boolean, param6:uint, param7:Boolean, param8:int, param9:uint, param10:int = 0) : void
      {
         var _loc16_:Vector.<class_140> = null;
         var _loc26_:BuffType = null;
         var _loc27_:int = 0;
         var _loc28_:int = 0;
         var _loc29_:Number = NaN;
         var _loc30_:Number = NaN;
         var _loc31_:Boolean = false;
         var _loc32_:Boolean = false;
         var _loc33_:BuffType = null;
         var _loc34_:int = 0;
         var _loc35_:EntType = null;
         var _loc36_:String = null;
         var _loc37_:Number = NaN;
         var _loc38_:Number = NaN;
         var _loc39_:Number = NaN;
         var _loc40_:Number = NaN;
         var _loc41_:int = 0;
         var _loc42_:Entity = null;
         var _loc43_:int = 0;
         var _loc44_:Boolean = false;
         var _loc45_:Number = NaN;
         var _loc46_:int = 0;
         var _loc47_:Number = NaN;
         var _loc48_:int = 0;
         var _loc49_:Number = NaN;
         var _loc50_:Number = NaN;
         var _loc51_:String = null;
         var _loc52_:BuffType = null;
         var _loc53_:class_134 = null;
         var _loc54_:Boolean = false;
         var _loc55_:int = 0;
         var _loc56_:Vector.<String> = null;
         var _loc57_:BuffType = null;
         var _loc58_:Number = NaN;
         var _loc59_:Number = NaN;
         var _loc60_:Vector.<PowerType> = null;
         var _loc61_:int = 0;
         var _loc62_:PowerType = null;
         var _loc63_:String = null;
         var _loc64_:PowerType = null;
         var _loc65_:int = 0;
         var _loc66_:PowerType = null;
         var _loc67_:BuffType = null;
         var _loc68_:PowerType = null;
         var _loc69_:* = false;
         var _loc70_:uint = 0;
         var _loc71_:Entity = null;
         var _loc72_:Vector.<class_140> = null;
         var _loc73_:Buff = null;
         var _loc11_:uint = param1.var_630.length;
         var _loc12_:Number = param4 < _loc11_ ? param1.var_630[param4] : param1.var_630[0];
         var _loc13_:CombatState = param2.combatState;
         if(param2 != this.var_3 && _loc13_.method_924(param1.var_402 == PowerType.DAMAGETYPE_PHYSICAL))
         {
            return;
         }
         var _loc14_:Number = 1 + this.var_3.totalMods.var_1680;
         var _loc15_:uint = this.var_1.mTimeThisTick;
         var _loc17_:uint = uint(this.var_3.magicDamage);
         var _loc18_:Number = 0;
         if(this.var_3.var_18)
         {
            _loc18_ = this.var_3.var_18.method_102(this.var_3,param1.basePowerName,"BaseDamageMult");
         }
         _loc12_ += _loc18_;
         var _loc19_:Boolean = false;
         var _loc20_:int = 0;
         if(param1.powerName.indexOf("LightningBombExplode") == 0)
         {
            _loc20_ = param8;
            param8 = 0;
         }
         if(param1.powerName == "Avalanche10")
         {
            if(_loc13_.var_1102)
            {
               _loc26_ = class_14.buffTypesDict["FreezeSpire10"];
               if(this.var_3.var_18)
               {
                  _loc16_ = this.var_3.var_18.method_101(this.var_3,_loc26_);
               }
               _loc13_.AddBuff(_loc26_,this.var_3,_loc17_,param1.powerID,1,_loc16_);
            }
         }
         var _loc21_:int = 0;
         if(param8)
         {
            if((_loc21_ = _loc12_ * param8) < 0)
            {
               if(param1.var_2586)
               {
                  _loc21_ = Math.floor((1 + param2.var_237 + param2.combatState.var_546) * _loc21_);
               }
               _loc27_ = param2.currHP - param2.maxHP;
               if(_loc21_ < _loc27_)
               {
                  _loc21_ = _loc27_ < 0 ? _loc27_ : 0;
               }
            }
         }
         else if(_loc12_ > 0)
         {
            _loc28_ = !!_loc20_ ? _loc20_ : this.var_3.meleeDamage;
            _loc21_ = Math.round(_loc12_ * _loc28_);
            Game.var_172.method_175(param1,this.var_3,param2,_loc21_,true);
            if(_loc21_)
            {
               if(_loc21_ -= param2.armorClass)
               {
                  _loc39_ = this.method_1393(_loc21_,param1,param2);
                  _loc21_ *= _loc39_;
               }
               _loc29_ = param2.combatState.var_292;
               _loc21_ = Math.ceil(_loc21_ * (1 - _loc29_));
               if((_loc30_ = param2.combatState.method_1552(param1)) > 1)
               {
                  _loc30_ = 1;
               }
               _loc21_ = Math.ceil(_loc21_ * (1 - _loc30_));
               _loc31_ = false;
               if(param1.var_136 == "Melee" && this.currMeleeCombo > 1 && this.currMeleeCombo == param1.var_1075)
               {
                  _loc21_ *= 2;
                  _loc14_ *= 2;
                  _loc31_ = true;
               }
               if(param7)
               {
                  _loc21_ *= 2;
                  _loc14_ *= 2;
               }
               if(!param1.var_2786)
               {
                  if(param6 > const_737)
                  {
                     _loc21_ = 0;
                  }
                  else
                  {
                     _loc40_ = const_135[param6];
                     _loc21_ *= _loc40_;
                  }
               }
               _loc32_ = _loc13_.var_445 || _loc13_.var_1102 || _loc13_.var_1515 || _loc13_.var_1999;
               _loc33_ = class_14.buffTypesDict["Chilblains"];
               if((param1.basePowerName == "FrostBlast" || param1.basePowerName == "FrigidComet") && param1.var_7 >= 5)
               {
                  if(_loc32_)
                  {
                     if(this.var_3.var_18)
                     {
                        _loc16_ = this.var_3.var_18.method_101(this.var_3,_loc33_);
                     }
                     _loc13_.AddBuff(_loc33_,this.var_3,this.var_3.magicDamage,param1.powerID,1,_loc16_);
                  }
               }
               else if(param1.basePowerName == "GlacialSpear")
               {
                  _loc41_ = 1;
                  if(_loc32_)
                  {
                     if(param1.var_7 >= 10)
                     {
                        _loc41_ = 5;
                     }
                     else if(param1.var_7 >= 8)
                     {
                        _loc41_ = 4;
                     }
                     else if(param1.var_7 >= 5)
                     {
                        _loc41_ = 3;
                     }
                     else if(param1.var_7 >= 3)
                     {
                        _loc41_ = 2;
                     }
                     if(this.var_3.var_18)
                     {
                        _loc16_ = this.var_3.var_18.method_101(this.var_3,_loc33_);
                     }
                     _loc13_.AddBuff(_loc33_,this.var_3,this.var_3.magicDamage,param1.powerID,_loc41_,_loc16_);
                  }
               }
               else if(param1.basePowerName == "IceSpike")
               {
                  _loc41_ = 0;
                  if(param1.var_7 >= 10)
                  {
                     _loc41_ = 2;
                  }
                  else if(param1.var_7 >= 5)
                  {
                     _loc41_ = 1;
                  }
                  if(Boolean(_loc41_) && _loc32_)
                  {
                     if(this.var_3.var_18)
                     {
                        _loc16_ = this.var_3.var_18.method_101(this.var_3,_loc33_);
                     }
                     _loc13_.AddBuff(_loc33_,this.var_3,this.var_3.magicDamage,param1.powerID,_loc41_,_loc16_);
                  }
               }
               else if(param1.basePowerName == "IceNova")
               {
                  _loc41_ = 0;
                  if(param1.var_7 >= 8)
                  {
                     _loc41_ = 2;
                  }
                  else if(param1.var_7 >= 5)
                  {
                     _loc41_ = 1;
                  }
                  if(Boolean(_loc41_) && _loc32_)
                  {
                     if(this.var_3.var_18)
                     {
                        _loc16_ = this.var_3.var_18.method_101(this.var_3,_loc33_);
                     }
                     _loc13_.AddBuff(_loc33_,this.var_3,this.var_3.magicDamage,param1.powerID,_loc41_,_loc16_);
                  }
               }
               else if(param1.basePowerName == "PermafrostCloneExplode")
               {
                  _loc42_ = this.var_1.GetEntFromID(this.var_3.summonerId);
                  _loc41_ = 0;
                  if(param1.var_7 >= 10)
                  {
                     _loc41_ = 3;
                  }
                  else if(param1.var_7 >= 7)
                  {
                     _loc41_ = 2;
                  }
                  else if(param1.var_7 >= 5)
                  {
                     _loc41_ = 1;
                  }
                  if(_loc42_ && _loc41_ && _loc32_)
                  {
                     if(_loc42_.var_18)
                     {
                        _loc16_ = _loc42_.var_18.method_101(_loc42_,_loc33_);
                     }
                     _loc13_.AddBuff(_loc33_,_loc42_,_loc42_.magicDamage,param1.powerID,_loc41_,_loc16_);
                  }
               }
               _loc34_ = 0;
               if(param3)
               {
                  _loc43_ = int(param1.manaCost);
                  if(Boolean(this.mActivePower) && Boolean(this.mActivePower.var_912))
                  {
                     _loc43_ = this.mActivePower.var_912;
                  }
                  if(param1.basePowerName == "HeartSeeker" && param1.var_7 >= 8 || param1.basePowerName == "DarkChi" && param1.var_7 >= 10)
                  {
                     _loc13_.AddBuff(class_14.buffTypesDict["Dazed"],this.var_3,this.var_3.magicDamage,param1.powerID,1);
                  }
                  if(param1 == this.var_3.var_280 || param1 == this.var_3.var_353)
                  {
                     _loc34_ = _loc21_ * 2;
                  }
                  else if(_loc43_ <= 20)
                  {
                     _loc34_ = _loc21_ * 1;
                  }
                  else if(_loc43_ <= 40)
                  {
                     _loc34_ = _loc21_ * 0.5;
                  }
                  else
                  {
                     _loc34_ = _loc21_ * 0.25;
                  }
                  if(this.var_576)
                  {
                     if(this.var_576 >= 9)
                     {
                        _loc34_ *= 1;
                     }
                     else if(this.var_576 >= 6)
                     {
                        _loc34_ *= 0.9;
                     }
                     else if(this.var_576 >= 3)
                     {
                        _loc34_ *= 0.8;
                     }
                     else
                     {
                        _loc34_ *= 0.7;
                     }
                  }
                  if(param1.var_219)
                  {
                     _loc34_ *= 0.75;
                  }
               }
               if((_loc36_ = (_loc35_ = param2.entType).entName) == "IntroDummy1")
               {
                  _loc21_ = param7 || _loc31_ ? _loc21_ * 2 : 1;
               }
               else if(_loc36_ == "IntroDummy2")
               {
                  _loc21_ = param1.manaCost == 20 ? _loc21_ * 2 : 1;
               }
               else if(_loc36_ == "IntroDummy3")
               {
                  _loc21_ = param1.manaCost == 30 ? _loc21_ * 2 : 1;
               }
               _loc37_ = (_loc37_ = param2.combatState.var_663) + param2.combatState.var_1192;
               _loc38_ = (_loc38_ = 0) + this.var_1738;
               if(param1.var_301)
               {
                  _loc37_ = 0;
                  _loc38_ = 0;
               }
               if(Boolean(_loc37_) || _loc38_ && !param1.var_275)
               {
                  if(_loc38_ > Math.random() || _loc37_ > Math.random())
                  {
                     this.method_72(class_14.powerTypesDict["ProcGlancingBlow"],param2,new Point(param2.physPosX,param2.physPosY),(_loc21_ + _loc34_) / 2,param1.powerID);
                     param2.combatState.method_1960(this.var_1298);
                     _loc21_ = 0;
                     _loc34_ = 0;
                     _loc19_ = true;
                  }
               }
               if(this.var_931 && !param1.var_275 && !param1.var_301)
               {
                  _loc44_ = param1 == this.var_3.var_280 || param1 == this.var_3.var_353;
                  _loc45_ = 0;
                  if(this.var_931 >= 10)
                  {
                     _loc45_ = _loc44_ ? 1 : 0.5;
                  }
                  else if(this.var_931 >= 9)
                  {
                     _loc45_ = _loc44_ ? 0.9 : 0.4;
                  }
                  else if(this.var_931 >= 7)
                  {
                     _loc45_ = _loc44_ ? 0.85 : 0.35;
                  }
                  else if(this.var_931 >= 5)
                  {
                     _loc45_ = _loc44_ ? 0.8 : 0.3;
                  }
                  else
                  {
                     _loc45_ = _loc44_ ? 0.75 : 0.25;
                  }
                  _loc46_ = _loc21_ + _loc21_ * _loc45_;
                  this.method_72(class_14.powerTypesDict["ProcCriticalHit"],param2,new Point(param2.physPosX,param2.physPosY),_loc46_ + _loc34_,param1.powerID);
                  _loc21_ = 0;
                  _loc34_ = 0;
                  _loc19_ = true;
               }
               _loc21_ += _loc34_;
            }
            if(_loc21_ < 1 && !_loc19_)
            {
               _loc21_ = 1;
            }
         }
         else if(_loc12_ < 0)
         {
            _loc21_ = (_loc21_ = (_loc21_ = Math.round(_loc12_ * this.var_3.magicDamage)) + Math.floor(this.var_3.totalMods.magicDamage * _loc21_)) + Math.floor(this.var_288 * _loc21_);
            _loc47_ = !!this.var_3.var_719[param1.var_157] ? Number(this.var_3.var_719[param1.var_157]) : 0;
            _loc21_ += Math.floor((_loc47_ + param2.var_237 + param2.combatState.var_546) * _loc21_);
            if(Boolean(this.var_1428) && param2.currHP < param2.maxHP * 0.2)
            {
               _loc21_ *= 1 + this.var_1428;
            }
            _loc48_ = param2.currHP - param2.maxHP;
            if(_loc21_ >= 0)
            {
               _loc21_ = -1;
            }
            if(_loc21_ < _loc48_)
            {
               _loc21_ = _loc48_ < 0 ? _loc48_ : 0;
            }
         }
         var _loc22_:Boolean;
         if((_loc22_ = Entity.method_574(this.var_3,param2)) && _loc21_ < 0 || !_loc22_ && _loc21_ > 0)
         {
            return;
         }
         if(this.var_3.method_622())
         {
            _loc49_ = Number(Game.const_1078[this.var_3.var_1523]);
            if(this.var_3.entType.var_913)
            {
               _loc49_ += Game.const_1085;
            }
            _loc21_ = Math.round(_loc21_ * _loc49_);
         }
         if(Boolean(param1.var_1517) && param5)
         {
            _loc50_ = _loc14_ * param1.var_1517;
            Game.var_172.method_142(this.var_3,param1,_loc50_,false,this.var_3.var_228);
            this.var_3.var_228 += _loc50_;
            if(this.var_3.var_228 > this.var_3.var_1785)
            {
               this.var_3.var_228 = this.var_3.var_1785;
            }
         }
         if(param2.behaviorType.var_2918)
         {
            _loc21_ = 0;
         }
         param2.combatState.method_294(this.var_3,_loc21_,param1,param1.powerID);
         if(_loc21_ > 0)
         {
            this.method_81();
         }
         var _loc23_:Boolean = param7 || _loc31_;
         this.var_1.linkUpdater.method_1092(this.var_3,param1,param2,_loc21_,param9,param4,_loc23_);
         var _loc24_:Vector.<String> = !!param1.var_381 ? param1.var_381.slice() : null;
         if(param1.var_1759 && _loc24_ && _loc24_.length > param4)
         {
            _loc24_ = _loc24_.slice(param4,param4 + 1);
         }
         if(this.var_3.var_18)
         {
            _loc24_ = this.var_3.var_18.method_492(_loc24_,param1.basePowerName,"AddTargetBuff");
         }
         if(_loc24_)
         {
            if(!param1.var_2414 && (!param1.var_2451 || param6 == 1))
            {
               for each(_loc51_ in _loc24_)
               {
                  if(_loc52_ = class_14.buffTypesDict[_loc51_])
                  {
                     if((!param1.var_1801 || param7) && (!param1.var_2273 || param4 == param1.var_108.length - 1) && (!param1.var_2369 || param4 == 0))
                     {
                        if(this.var_3.var_18)
                        {
                           _loc16_ = this.var_3.var_18.method_101(this.var_3,_loc52_);
                        }
                        _loc17_ = uint(this.var_3.magicDamage);
                        _loc53_ = this.var_3.totalMods;
                        _loc17_ *= 1 + _loc53_.magicDamage + this.var_288;
                        if(!(_loc54_ = _loc52_.var_668 || _loc52_.var_953) || !param2.entType.var_2238)
                        {
                           if(_loc52_.var_2424)
                           {
                              _loc17_ = uint(param8);
                           }
                           param2.combatState.AddBuff(_loc52_,this.var_3,_loc17_,param1.powerID,1,_loc16_,param10);
                        }
                     }
                  }
               }
            }
            else if(param1.var_2414)
            {
               _loc55_ = Math.random() * _loc24_.length;
               _loc51_ = _loc24_[_loc55_];
               if((_loc52_ = class_14.buffTypesDict[_loc51_]) && (!param1.var_1801 || param7) && (!param1.var_2273 || param4 == param1.var_108.length - 1) && (!param1.var_2369 || param4 == 0))
               {
                  if(this.var_3.var_18)
                  {
                     _loc16_ = this.var_3.var_18.method_101(this.var_3,_loc52_);
                  }
                  _loc17_ = uint(this.var_3.magicDamage);
                  if(!(_loc54_ = _loc52_.var_668 || _loc52_.var_953) || !param2.entType.var_2238)
                  {
                     param2.combatState.AddBuff(_loc52_,this.var_3,_loc17_,param1.powerID,1,_loc16_);
                  }
               }
            }
         }
         if(_loc21_ > 0 && param1.var_2063 && (!param1.var_1682 || !param4))
         {
            _loc56_ = !!param1.var_437 ? param1.var_437.slice() : null;
            if(this.var_3.var_18)
            {
               _loc56_ = this.var_3.var_18.method_492(_loc56_,param1.basePowerName,"AddSelfBuff");
            }
            if(_loc56_)
            {
               for each(_loc51_ in _loc56_)
               {
                  if(_loc57_ = class_14.buffTypesDict[_loc51_])
                  {
                     if(this.var_3.var_18)
                     {
                        _loc16_ = this.var_3.var_18.method_101(this.var_3,_loc57_);
                     }
                     _loc17_ = uint(this.var_3.magicDamage);
                     this.var_3.combatState.AddBuff(_loc57_,this.var_3,_loc17_,param1.powerID,1,_loc16_,0,param2);
                  }
               }
            }
         }
         if(this.var_3.var_1553 && (!param1.var_301 || param1.var_2554) && _loc21_ > 0)
         {
            _loc58_ = param1.var_1989;
            _loc59_ = 0;
            if(param7 || _loc31_)
            {
               _loc58_ = 1;
            }
            else if(_loc58_)
            {
               if(Boolean(this.var_1557) && Boolean(_loc13_.var_1234))
               {
                  _loc59_ += this.var_1557;
               }
               if(Boolean(this.var_1644) && (_loc13_.var_683 || _loc13_.var_2291))
               {
                  _loc59_ += this.var_1644;
               }
               if(Boolean(this.var_1567) && _loc13_.var_963)
               {
                  _loc59_ += this.var_1567;
               }
            }
            if(this.method_1200(_loc58_,_loc59_))
            {
               _loc60_ = this.var_3.var_1553;
               _loc61_ = 0;
               while(_loc61_ < _loc60_.length)
               {
                  if((_loc62_ = _loc60_[_loc61_]).var_2323)
                  {
                     this.method_72(_loc62_,this.var_3,new Point(param2.physPosX,param2.physPosY),_loc21_ / 2,param1.powerID);
                  }
                  else
                  {
                     this.method_72(_loc62_,param2,new Point(param2.physPosX,param2.physPosY),_loc21_ / 2,param1.powerID);
                  }
                  _loc61_++;
               }
            }
         }
         if(param1.basePowerName == "VampStrike" || param1.basePowerName == "ShadowScythe")
         {
            this.method_72(class_14.powerTypesDict["ProcAlwaysFullHeal"],this.var_3,new Point(param2.physPosX,param2.physPosY),_loc21_,param1.powerID);
         }
         else if(param1.basePowerName == "Devour")
         {
            this.method_72(class_14.powerTypesDict["ProcDevour"],this.var_3,new Point(param2.physPosX,param2.physPosY),_loc21_,param1.powerID);
         }
         else if(param1.basePowerName == "Reaper")
         {
            this.method_72(class_14.powerTypesDict["ProcAlways75PctHeal"],this.var_3,new Point(param2.physPosX,param2.physPosY),_loc21_,param1.powerID);
         }
         else if(param1.basePowerName == "Lifethirst")
         {
            this.method_72(class_14.powerTypesDict["ProcLifethirstSelf"],this.var_3,new Point(param2.physPosX,param2.physPosY),_loc21_,param1.powerID);
            if(param1.var_7 >= 10)
            {
               this.method_72(class_14.powerTypesDict["ProcLifethirstPets10"],this.var_3,new Point(param2.physPosX,param2.physPosY),_loc21_,param1.powerID);
            }
            else if(param1.var_7 >= 7)
            {
               this.method_72(class_14.powerTypesDict["ProcLifethirstPets7"],this.var_3,new Point(param2.physPosX,param2.physPosY),_loc21_,param1.powerID);
            }
            else if(param1.var_7 >= 4)
            {
               this.method_72(class_14.powerTypesDict["ProcLifethirstPets4"],this.var_3,new Point(param2.physPosX,param2.physPosY),_loc21_,param1.powerID);
            }
         }
         var _loc25_:Vector.<String> = new Vector.<String>();
         if(param1.var_2585)
         {
            _loc25_.push(param1.var_2585);
         }
         if((_loc25_ = this.var_3.var_18.method_1479(_loc25_,param1.basePowerName,"ProcOnHit")).length > 0)
         {
            for each(_loc63_ in _loc25_)
            {
               if(_loc64_ = class_14.powerTypesDict[_loc63_])
               {
                  this.method_72(_loc64_,this.var_3,new Point(param2.physPosX,param2.physPosY),_loc21_,param1.powerID);
               }
            }
         }
         if(_loc21_ > 0)
         {
            if(this.var_598 > 0)
            {
               _loc65_ = param7 ? 2 : 1;
               if(this.var_3.var_18)
               {
                  _loc16_ = this.var_3.var_18.method_101(this.var_3,class_14.buffTypesDict["Scorched"]);
               }
               param2.combatState.AddBuff(class_14.buffTypesDict["Scorched"],this.var_3,this.var_3.magicDamage,param1.powerID,_loc65_,_loc16_);
            }
            if(this.var_1414 && _loc13_.var_2045 && param1.var_402 == "Fire")
            {
               this.method_46(class_14.powerTypesDict["Blaze" + this.var_1414],param2,new Point(param2.physPosX,param2.physPosY),true);
            }
         }
         if(param1.basePowerName == "FrostArmorRanged" && this.var_3.id == this.var_1.clientEntID)
         {
            if(param1.var_7 >= 10)
            {
               _loc66_ = class_14.powerTypesDict["FrostArmorIce10"];
            }
            else if(param1.var_7 >= 7)
            {
               _loc66_ = class_14.powerTypesDict["FrostArmorIce7"];
            }
            else if(param1.var_7 >= 5)
            {
               _loc66_ = class_14.powerTypesDict["FrostArmorIce5"];
            }
            else if(param1.var_7 >= 2)
            {
               _loc66_ = class_14.powerTypesDict["FrostArmorIce2"];
            }
            else
            {
               _loc66_ = class_14.powerTypesDict["FrostArmorIce1"];
            }
            this.method_46(_loc66_,null,new Point(param2.appearPosX,param2.appearPosY));
         }
         if(Boolean(this.var_1188) && _loc22_)
         {
            _loc67_ = class_14.buffTypesDict["Plagued" + this.var_1188];
            _loc68_ = class_14.powerTypesDict["PlagueBattalion" + this.var_1188];
            _loc71_ = (Boolean(_loc70_ = (_loc69_ = !this.var_3.summonerId) ? this.var_3.id : this.var_3.summonerId)) && _loc70_ == this.var_1.clientEntID ? this.var_1.GetEntFromID(_loc70_) : null;
            if(_loc67_ && _loc68_ && _loc71_ && (_loc69_ || _loc71_.combatState.var_1815))
            {
               if(!_loc69_)
               {
                  if(_loc73_ = _loc71_.combatState.method_135(class_14.buffTypesDict["PlagueStackLimit"]))
                  {
                     _loc73_.method_357(1);
                  }
                  _loc71_.combatState.var_555 = true;
               }
               if(_loc71_.var_18)
               {
                  _loc72_ = _loc71_.var_18.method_101(_loc71_,_loc67_);
               }
               param2.combatState.AddBuff(_loc67_,_loc71_,_loc71_.magicDamage,_loc68_.powerID,1,_loc72_);
               this.RemoveBuff(class_14.buffTypesDict["PlagueBattalion"]);
               this.var_1188 = 0;
            }
         }
      }
      
      public function method_1393(param1:int, param2:PowerType, param3:Entity) : Number
      {
         var _loc4_:EntType = null;
         var _loc5_:CombatState = null;
         var _loc6_:Number = NaN;
         var _loc7_:int = 0;
         var _loc9_:Number = NaN;
         var _loc10_:Number = NaN;
         var _loc11_:Number = NaN;
         var _loc12_:Number = NaN;
         var _loc14_:Number = NaN;
         var _loc15_:String = null;
         var _loc16_:Number = NaN;
         var _loc17_:Number = NaN;
         var _loc18_:Number = NaN;
         var _loc19_:Number = NaN;
         var _loc20_:Number = NaN;
         var _loc21_:Number = NaN;
         var _loc22_:Number = NaN;
         var _loc23_:Number = NaN;
         var _loc24_:Number = NaN;
         var _loc25_:Number = NaN;
         var _loc26_:int = 0;
         var _loc27_:Number = NaN;
         var _loc28_:Number = NaN;
         var _loc29_:Number = NaN;
         var _loc30_:Number = NaN;
         var _loc31_:int = 0;
         var _loc32_:int = 0;
         var _loc33_:Number = NaN;
         var _loc34_:Number = NaN;
         var _loc35_:Number = NaN;
         var _loc36_:Number = NaN;
         _loc4_ = param3.entType;
         _loc5_ = param3.combatState;
         _loc6_ = 1;
         _loc7_ = 0;
         var _loc8_:class_134 = this.var_3.totalMods;
         _loc6_ = (_loc6_ += _loc8_.meleeDamage) + this.var_495;
         if(_loc9_ = Number(this.var_3.var_1562[_loc4_.var_106]))
         {
            _loc6_ += _loc9_;
         }
         if(_loc10_ = Number(this.var_3.var_65[_loc4_.var_328 + "Slay"]))
         {
            _loc6_ += _loc10_;
         }
         if(_loc11_ = Number(this.var_3.var_719[param2.var_157]))
         {
            _loc6_ += _loc11_;
         }
         if(_loc12_ = Number(param3.var_1516[this.var_3.entType.var_106]))
         {
            _loc6_ -= _loc12_;
         }
         var _loc13_:String = this.var_3.entType.var_103;
         if(_loc14_ = Number(param3.combatState.var_577[_loc13_]))
         {
            _loc6_ -= _loc14_;
         }
         _loc15_ = this.var_3.entType.var_328;
         if(_loc16_ = Number(param3.combatState.var_577[_loc15_]))
         {
            _loc6_ -= _loc16_;
         }
         if(_loc17_ = Number(param3.var_66["Resist" + _loc15_]))
         {
            _loc6_ -= _loc17_;
         }
         if(this.var_2146)
         {
            _loc18_ = 1 - this.var_3.currHP / this.var_3.maxHP;
            _loc19_ = 1.175;
            _loc6_ += _loc18_ * _loc19_;
         }
         if((Boolean(_loc5_.var_1981) || Boolean(_loc5_.var_1786)) && (param2.var_402 == PowerType.DAMAGETYPE_FIRE || this.var_598))
         {
            _loc20_ = 0.1;
            _loc21_ = 0.01;
            if(this.var_598)
            {
               if(this.var_598 >= 10)
               {
                  _loc21_ = 0.0205;
               }
               else if(this.var_598 >= 5)
               {
                  _loc21_ = 0.0175;
               }
               else if(this.var_598 >= 4)
               {
                  _loc21_ = 0.015;
               }
               else if(this.var_598 >= 2)
               {
                  _loc21_ = 0.0125;
               }
            }
            if(this.var_2279 && param2.basePowerName == "FlamethrowerROR")
            {
               _loc20_ *= 1.1;
               _loc21_ *= 1.1;
            }
            _loc6_ = (_loc6_ += _loc20_ * _loc5_.var_1981) + _loc21_ * _loc5_.var_1786;
         }
         if(param2.basePowerName == "QuickStrike" && (Boolean(_loc5_.var_1091) || Boolean(_loc5_.var_1032)))
         {
            _loc33_ = 0;
            if(param2.var_7 >= 10)
            {
               _loc33_ = 0.15;
            }
            else if(param2.var_7 >= 7)
            {
               _loc33_ = 0.1;
            }
            else if(param2.var_7 >= 3)
            {
               _loc33_ = 0.05;
            }
            _loc6_ += _loc33_;
         }
         if(param2.basePowerName == "PolarSentryStrike")
         {
            _loc22_ = 0;
            if(_loc5_.var_445)
            {
               _loc22_ += 1.5;
            }
            else if(_loc5_.var_1102)
            {
               _loc22_ += 1;
            }
            else if(_loc5_.var_1515)
            {
               _loc22_ += 0.5;
            }
            if(param2.var_7 < 10)
            {
               if(param2.var_7 >= 5)
               {
                  _loc22_ *= 0.75;
               }
               else
               {
                  _loc22_ *= 0.5;
               }
            }
            _loc6_ += _loc22_;
         }
         if(this.var_1957 && (param2.basePowerName == "FrostArmorIce" || param2.basePowerName == "FrostArmorMelee" || param2.basePowerName == "FrostArmorIceWall"))
         {
            if(param2.var_7 >= 10)
            {
               _loc6_ += 1;
            }
            else if(param2.var_7 >= 5)
            {
               _loc6_ += 0.5;
            }
         }
         if(_loc5_.var_1234)
         {
            _loc23_ = 0.05;
            if(param2.basePowerName == "LeapStrikeClose")
            {
               if(this.var_2227)
               {
                  _loc6_ += _loc23_ * _loc5_.var_1234;
               }
               if(param2.var_7 >= 10)
               {
                  _loc6_ += 0.8;
               }
               else if(param2.var_7 >= 8)
               {
                  _loc6_ += 0.75;
               }
               else if(param2.var_7 >= 5)
               {
                  _loc6_ += 0.7;
               }
               else
               {
                  _loc6_ += 0.65;
               }
            }
            else if(param2.basePowerName == "JusticeFist")
            {
               if(param2.var_7 >= 9)
               {
                  _loc23_ = 0.25;
               }
               else if(param2.var_7 >= 8)
               {
                  _loc23_ = 0.2;
               }
               else if(param2.var_7 >= 6)
               {
                  _loc23_ = 0.15;
               }
               else if(param2.var_7 >= 4)
               {
                  _loc23_ = 0.1;
               }
               _loc6_ += _loc23_;
            }
            else if(param2.basePowerName == "FuriousAssault")
            {
               if(param2.var_7 >= 10)
               {
                  _loc23_ = 0.25;
               }
               else if(param2.var_7 >= 8)
               {
                  _loc23_ = 0.2;
               }
               else if(param2.var_7 >= 7)
               {
                  _loc23_ = 0.15;
               }
               else if(param2.var_7 >= 4)
               {
                  _loc23_ = 0.1;
               }
               _loc6_ += _loc23_;
            }
            else if(param2.basePowerName == "LightningStorm")
            {
               if(param2.var_7 >= 10)
               {
                  _loc23_ = 0.5;
               }
               else if(param2.var_7 >= 7)
               {
                  _loc23_ = 0.25;
               }
               else
               {
                  _loc23_ = 0;
               }
               _loc6_ += _loc23_;
            }
         }
         if((_loc5_.var_2096 || _loc5_.var_2114) && param2.basePowerName == "Enfeeble")
         {
            if(param2.var_7 >= 9)
            {
               _loc6_ += 0.5;
            }
            else if(param2.var_7 >= 7)
            {
               _loc6_ += 0.25;
            }
         }
         if(param2.basePowerName == "DeathBlowOld")
         {
            _loc24_ = (param3.maxHP - param3.currHP) / param3.maxHP;
            _loc25_ = param2.var_7 >= 10 ? 1 : 0.5;
            _loc26_ = _loc24_ * _loc25_ * this.var_3.meleeDamage;
            _loc6_ += _loc26_ / param1;
         }
         if(param2.basePowerName == "Reaper" && Boolean(_loc5_.var_1033))
         {
            _loc27_ = 0;
            if(param2.var_7 >= 10)
            {
               _loc27_ = 0.2;
            }
            else if(param2.var_7 >= 9)
            {
               _loc27_ = 0.15;
            }
            else if(param2.var_7 >= 7)
            {
               _loc27_ = 0.1;
            }
            else if(param2.var_7 >= 5)
            {
               _loc27_ = 0.05;
            }
            else
            {
               _loc27_ = 0.02;
            }
            _loc6_ += _loc27_;
         }
         if(param2.basePowerName == "PainBender" && Boolean(_loc5_.var_1033))
         {
            _loc28_ = 0;
            if(param2.var_7 >= 10)
            {
               _loc28_ = 0.75;
            }
            else if(param2.var_7 >= 9)
            {
               _loc28_ = 0.6;
            }
            else if(param2.var_7 >= 7)
            {
               _loc28_ = 0.45;
            }
            else if(param2.var_7 >= 4)
            {
               _loc28_ = 0.3;
            }
            else
            {
               _loc28_ = 0.15;
            }
            _loc6_ += _loc28_;
         }
         if(param2.basePowerName == "Devour")
         {
            _loc29_ = 0;
            if(_loc5_.var_1033)
            {
               if(param2.var_7 >= 10)
               {
                  _loc29_ += 0.15;
               }
               else if(param2.var_7 >= 7)
               {
                  _loc29_ += 0.1;
               }
               else if(param2.var_7 >= 4)
               {
                  _loc29_ += 0.05;
               }
            }
            if(_loc5_.var_1091)
            {
               if(param2.var_7 >= 10)
               {
                  _loc29_ += 0.15;
               }
               else if(param2.var_7 >= 8)
               {
                  _loc29_ += 0.1;
               }
               else if(param2.var_7 >= 5)
               {
                  _loc29_ += 0.05;
               }
            }
            _loc6_ += _loc29_;
         }
         if(param2.basePowerName == "ShadowBlade")
         {
            _loc30_ = 0.5 * this.var_3.meleeDamage;
            if(param2.var_7 >= 10)
            {
               _loc31_ = 10;
            }
            else if(param2.var_7 >= 8)
            {
               _loc31_ = 8;
            }
            else if(param2.var_7 >= 7)
            {
               _loc31_ = 7;
            }
            else if(param2.var_7 >= 6)
            {
               _loc31_ = 6;
            }
            else if(param2.var_7 >= 5)
            {
               _loc31_ = 5;
            }
            else if(param2.var_7 >= 4)
            {
               _loc31_ = 4;
            }
            else
            {
               _loc31_ = 3;
            }
            if(_loc32_ = _loc5_.var_1032 > _loc31_ ? _loc31_ : _loc5_.var_1032)
            {
               if(this.var_2400)
               {
                  _loc30_ *= 1.1;
               }
               _loc7_ += _loc30_ * _loc32_;
            }
         }
         if(param2.basePowerName == "SeverStrike" && Boolean(_loc5_.var_1091))
         {
            _loc33_ = 0;
            if(param2.var_7 >= 6)
            {
               _loc33_ = 0.15;
            }
            else if(param2.var_7 >= 3)
            {
               _loc33_ = 0.1;
            }
            _loc7_ += _loc33_ * this.var_3.meleeDamage;
         }
         if(param2.basePowerName == "Desecrate")
         {
            if(_loc34_ = !!param3.combatState.var_84 ? param3.combatState.var_84.length : 0)
            {
               if(param2.var_7 >= 10)
               {
                  _loc35_ = 2.5;
                  _loc34_ *= 0.5;
               }
               else if(param2.var_7 >= 9)
               {
                  _loc35_ = 2.25;
                  _loc34_ *= 0.45;
               }
               else if(param2.var_7 >= 8)
               {
                  _loc35_ = 2;
                  _loc34_ *= 0.4;
               }
               else if(param2.var_7 >= 7)
               {
                  _loc35_ = 1.8;
                  _loc34_ *= 0.36;
               }
               else if(param2.var_7 >= 6)
               {
                  _loc35_ = 1.6;
                  _loc34_ *= 0.32;
               }
               else if(param2.var_7 >= 5)
               {
                  _loc35_ = 1.4;
                  _loc34_ *= 0.28;
               }
               else if(param2.var_7 >= 4)
               {
                  _loc35_ = 1.2;
                  _loc34_ *= 0.24;
               }
               else
               {
                  _loc35_ = 1;
                  _loc34_ *= 0.2;
               }
               if(_loc34_ > _loc35_)
               {
                  _loc34_ = _loc35_;
               }
               _loc7_ += _loc34_ * this.var_3.magicDamage * (1 + this.var_288 + this.var_3.totalMods.magicDamage);
            }
         }
         if(param2.basePowerName == "BansheeWail")
         {
            _loc36_ = !!param3.combatState.var_84 ? param3.combatState.var_84.length : 0;
            _loc35_ = 0;
            if(_loc36_)
            {
               if(param2.var_7 >= 10)
               {
                  _loc35_ = 3;
                  _loc36_ *= 0.6;
               }
               else if(param2.var_7 >= 9)
               {
                  _loc35_ = 2.5;
                  _loc36_ *= 0.5;
               }
               else if(param2.var_7 >= 8)
               {
                  _loc35_ = 2.25;
                  _loc36_ *= 0.45;
               }
               else if(param2.var_7 >= 7)
               {
                  _loc35_ = 2;
                  _loc36_ *= 0.4;
               }
               else if(param2.var_7 >= 6)
               {
                  _loc35_ = 1.8;
                  _loc36_ *= 0.36;
               }
               else if(param2.var_7 >= 5)
               {
                  _loc35_ = 1.65;
                  _loc36_ *= 0.33;
               }
               else if(param2.var_7 >= 4)
               {
                  _loc35_ = 1.4;
                  _loc36_ *= 0.28;
               }
               else
               {
                  _loc35_ = 1.25;
                  _loc36_ *= 0.25;
               }
               if(_loc36_ > _loc35_)
               {
                  _loc36_ = _loc35_;
               }
               _loc7_ += _loc36_ * this.var_3.magicDamage * (1 + this.var_288 + this.var_3.totalMods.magicDamage);
            }
         }
         if(this.var_1093 && this.var_2566 >= this.var_1.mTimeThisTick && !param2.var_219 && param2.manaCost >= 15)
         {
            _loc6_ += this.var_1093;
         }
         if(Boolean(this.var_1483) && (_loc5_.var_540 < 0 || _loc5_.var_445))
         {
            _loc6_ += this.var_1483;
         }
         if(Boolean(this.var_1410) && Boolean(_loc5_.var_1033))
         {
            _loc6_ += this.var_1410;
         }
         if(this.var_963 && param3.behaviorType && param3.behaviorType.var_679)
         {
            _loc6_ -= 0.2;
         }
         if(param3.combatState.var_963 && this.var_3.behaviorType && this.var_3.behaviorType.var_679)
         {
            _loc6_ += 0.05;
         }
         if(this.var_963 && Boolean(_loc5_.var_971))
         {
            _loc6_ -= _loc5_.var_971;
         }
         if(param3.combatState.var_963 && Boolean(this.var_923))
         {
            _loc6_ += this.var_923;
         }
         if(this.var_1171 && param3.behaviorType && param3.behaviorType.var_679)
         {
            _loc6_ -= 0.04;
         }
         if(param3.combatState.var_1171 && this.var_3.behaviorType && this.var_3.behaviorType.var_679)
         {
            _loc6_ += 0.01;
         }
         if(this.var_1171 && Boolean(_loc5_.var_971))
         {
            _loc6_ -= _loc5_.var_971 / 5;
         }
         if(param3.combatState.var_1171 && Boolean(this.var_923))
         {
            _loc6_ += this.var_923 / 5;
         }
         if((_loc6_ += _loc7_ / param1) < 0)
         {
            _loc6_ = 0;
         }
         return _loc6_;
      }
      
      public function method_294(param1:Entity, param2:int, param3:PowerType, param4:uint) : void
      {
         var _loc5_:Number = NaN;
         var _loc6_:int = 0;
         var _loc7_:Buff = null;
         var _loc8_:BuffType = null;
         var _loc9_:CombatState = null;
         if(this.var_3.brain && param1 && this.var_3 != param1 && Boolean(param2))
         {
            _loc5_ = 1 + param1.totalMods.var_1318 + param1.combatState.var_984 + (!!param3 ? param3.var_2327 : 0);
            this.var_3.brain.AddHate(param1,param2 * _loc5_,true);
         }
         else if(this.var_3.brain && param1 && this.var_3 != param1 && (this.var_3.brain.mostHatedEnt && (param3.basePowerName == "HateBeacon" || param3.basePowerName == "PetDjinn") || param3.basePowerName == "HatePulse"))
         {
            _loc5_ = 1 + param1.totalMods.var_1318 + param1.combatState.var_984 + (!!param3 ? param3.var_2327 : 0);
            this.var_3.brain.AddHate(param1,10000 * _loc5_,true);
         }
         this.var_3.TakeDamage(param2,false,param1,param3,param4);
         if(!this.var_3.var_38 && param3 && (!param3.var_301 || param3.basePowerName == "ProcGlancingBlow") && param2 > 0)
         {
            _loc6_ = int(this.var_84.length - 1);
            while(_loc6_ >= 0)
            {
               _loc8_ = (_loc7_ = this.var_84[_loc6_]).type;
               if(Boolean(_loc7_.var_1590) && param2 > 0)
               {
                  _loc7_.var_1590 -= param2;
               }
               if(_loc8_.var_2473 && _loc7_.var_1590 <= 0 && this.var_1.mTimeThisTick - _loc7_.startTime >= const_1075)
               {
                  this.RemoveBuff(_loc7_.type);
               }
               _loc6_--;
            }
         }
         if(!this.var_3.var_38 && Boolean(param3))
         {
            if(param3 == class_14.powerTypesDict["PetPhoenix"])
            {
               this.method_304(5,true,true);
            }
            if(param3.basePowerName == "CleansingLight")
            {
               this.method_304(5,true,true);
            }
         }
         if(Boolean(param3) && param2 > 0)
         {
            this.var_3.var_1875 = true;
            if(param1)
            {
               this.var_3.var_1897 += param2;
               this.var_3.var_2692 = this.var_3.appearPosX < param1.appearPosX ? -1 : 1;
            }
            if(this.var_3.var_20 & Entity.LOCAL)
            {
               if(Boolean(this.var_1310) && this.var_3.currHP < this.var_3.maxHP * 0.2)
               {
                  this.method_46(class_14.powerTypesDict["PainEater" + this.var_1310],this.var_3,new Point(this.var_3.physPosX,this.var_3.physPosY),true);
               }
               if(Boolean(this.var_1521) && this.var_3.currHP < this.var_3.maxHP * 0.2)
               {
                  this.method_46(class_14.powerTypesDict["Heroism" + this.var_1521],this.var_3,new Point(this.var_3.physPosX,this.var_3.physPosY),true);
               }
            }
         }
         if(param2 > 0)
         {
            this.method_81();
            if(param1)
            {
               param1.combatState.method_81();
            }
         }
         if(param3 && !param3.bIsProjectile && !param3.var_1689 && param1 && Boolean(param1.var_20 & Entity.PLAYER))
         {
            if(!(_loc9_ = param1.combatState).var_1937)
            {
               ++this.var_1.level.var_1096;
               ++this.var_1.level.var_728;
               _loc9_.var_1937 = true;
            }
         }
      }
      
      public function method_225(param1:PowerType, param2:SuperAnimInstance, param3:uint, param4:Entity, param5:Point, param6:uint) : void
      {
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:Point = null;
         var _loc10_:Point = null;
         var _loc11_:CollisionManager = null;
         var _loc12_:class_37 = null;
         var _loc13_:class_37 = null;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         var _loc16_:Point = null;
         var _loc17_:Point = null;
         var _loc18_:Number = NaN;
         var _loc19_:Number = NaN;
         var _loc20_:Number = NaN;
         switch(param3)
         {
            case PowerType.ANIMSOURCE_FEET:
               param2.m_TheDO.x = this.var_3.appearPosX;
               param2.m_TheDO.y = this.var_3.appearPosY;
               break;
            case PowerType.const_778:
               param2.m_TheDO.x = this.var_3.appearPosX;
               param2.m_TheDO.y = this.var_3.appearPosY - this.var_3.entType.height;
               break;
            case PowerType.const_671:
               param2.m_TheDO.x = this.var_3.appearPosX + (this.var_3.bFacingLeft() ? -param1.var_507 : param1.var_507);
               param2.m_TheDO.y = this.var_3.appearPosY;
               break;
            case PowerType.const_440:
               param2.m_TheDO.x = param5.x;
               param2.m_TheDO.y = param5.y;
               break;
            case PowerType.const_559:
               param2.m_TheDO.x = !!this.var_3.var_183 ? this.var_3.var_183.var_10 : this.var_3.var_10;
               param2.m_TheDO.y = !!this.var_3.var_183 ? this.var_3.var_183.var_12 : this.var_3.var_12;
               break;
            case PowerType.ANIMSOURCE_GROUND:
               _loc7_ = param5.x;
               _loc8_ = param5.y;
               _loc9_ = new Point();
               _loc10_ = new Point();
               _loc11_ = this.var_1.collMan;
               if(param1.var_6 == PowerType.const_99)
               {
                  _loc18_ = !!param6 ? param1.aoeRadius * 1.6 : this.var_3.entType.width;
                  _loc19_ = this.var_3.bFacingLeft() ? -1 : 1;
                  _loc7_ += _loc19_ * _loc18_;
               }
               _loc12_ = _loc11_.getFloorCollision(0,_loc7_,_loc8_ + 1,new Point(0,-202),_loc9_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,CollisionManager.SEARCHFLAG_UPWARD_INCLUDE_SOFT);
               _loc13_ = _loc11_.getFloorCollision(0,_loc7_,_loc8_ - 1,new Point(0,202),_loc10_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0);
               _loc14_ = !!_loc12_ ? Math.abs(_loc9_.y - _loc8_) : 10000;
               if((_loc15_ = !!_loc13_ ? Math.abs(_loc10_.y - _loc8_) : 10000) <= 200 && _loc15_ <= _loc14_)
               {
                  param5.x = _loc10_.x;
                  param5.y = _loc10_.y;
               }
               else if(_loc14_ <= 200 && _loc14_ <= _loc15_)
               {
                  param5.x = _loc9_.x;
                  param5.y = _loc9_.y;
               }
               param2.m_TheDO.x = param5.x;
               param2.m_TheDO.y = param5.y;
               if(!param1.powerName.indexOf("FirePillar") || !param1.powerName.indexOf("GoblinFlames"))
               {
                  param2.m_TheDO.scaleY = param6 < 4 ? 0.4 + param6 * 0.3 : 1.3 - (param6 - 4) * 0.3;
               }
               if(param1.basePowerName == "Avalanche")
               {
                  param2.m_TheDO.scaleX = Math.abs(param2.m_TheDO.scaleY = 1 - param6 * 0.1);
                  if(this.var_3.bFacingLeft())
                  {
                     param2.m_TheDO.scaleX *= -1;
                  }
               }
               break;
            case PowerType.ANIMSOURCE_CENTER:
               param2.m_TheDO.x = this.var_3.var_10;
               param2.m_TheDO.y = this.var_3.var_12;
               break;
            case PowerType.ANIMSOURCE_FIRESOCKET:
               _loc16_ = this.var_3.method_219(param5,param1.var_136);
               param2.m_TheDO.x = _loc16_.x;
               param2.m_TheDO.y = _loc16_.y;
               break;
            case PowerType.ANIMSOURCE_TARGETFEET:
               if(param4)
               {
                  param2.m_TheDO.x = param4.appearPosX;
                  param2.m_TheDO.y = param4.appearPosY;
               }
               else if(param5)
               {
                  param2.m_TheDO.x = param5.x;
                  param2.m_TheDO.y = param5.y;
               }
               break;
            case PowerType.const_293:
               if(param4)
               {
                  param2.m_TheDO.x = param4.appearPosX;
                  param2.m_TheDO.y = param4.appearPosY - param4.entType.height;
               }
               else if(param5)
               {
                  param2.m_TheDO.x = param5.x;
                  param2.m_TheDO.y = param5.y - this.var_3.entType.height;
               }
               break;
            case PowerType.ANIMSOURCE_TARGETCENTER:
               if(param4)
               {
                  param2.m_TheDO.x = param4.var_10;
                  param2.m_TheDO.y = param4.var_12;
               }
               else if(param5)
               {
                  param2.m_TheDO.x = param5.x;
                  param2.m_TheDO.y = param5.y - this.var_3.entType.height / 2;
               }
               break;
            case PowerType.const_219:
               if(param4)
               {
                  param2.m_TheDO.x = param4.var_10;
                  if(_loc16_ = this.var_3.method_219(param5,param1.var_136))
                  {
                     param2.m_TheDO.y = _loc16_.y;
                  }
                  else
                  {
                     param2.m_TheDO.y = this.var_3.var_12;
                  }
                  _loc20_ = param4.appearPosY - param4.entType.height;
                  if(param2.m_TheDO.y < _loc20_)
                  {
                     param2.m_TheDO.y = _loc20_;
                     break;
                  }
                  if(param2.m_TheDO.y > param4.appearPosY)
                  {
                     param2.m_TheDO.y = param4.appearPosY;
                  }
                  break;
               }
               if(param5)
               {
                  param2.m_TheDO.x = param5.x;
                  param2.m_TheDO.y = param5.y - this.var_3.entType.height / 2;
               }
               break;
            case PowerType.const_564:
               _loc17_ = this.method_139(new Point(param5.x,param5.y));
               param2.m_TheDO.y = _loc17_.y;
               param2.m_TheDO.x = _loc17_.x;
         }
      }
      
      public function method_2045(param1:SuperAnimInstance, param2:PowerType, param3:Point) : void
      {
         var _loc4_:Number = NaN;
         var _loc5_:Number = NaN;
         if(param2.var_6 == PowerType.const_201)
         {
            _loc5_ = (_loc4_ = Math.sqrt(Math.pow(param3.x - param1.m_TheDO.x,2) + Math.pow(param3.y - param1.m_TheDO.y,2))) / param2.method_63(this.var_3);
            param1.m_TheDO.scaleY = _loc5_;
         }
      }
      
      public function method_2041(param1:SuperAnimInstance) : void
      {
         param1.m_TheDO.scaleX = 1;
         param1.m_TheDO.scaleY = 1;
      }
      
      public function method_512(param1:SuperAnimInstance, param2:PowerType, param3:Point) : void
      {
         var _loc4_:Point = null;
         if(param2.var_6 == PowerType.TARGETMETHOD_PIERCING || param2.basePowerName == "CrimsonShot" || param2.var_6 == PowerType.const_201)
         {
            (_loc4_ = new Point(param3.x - param1.m_TheDO.x,param3.y - param1.m_TheDO.y)).normalize(1);
            param1.m_TheDO.rotation = MathUtil.method_222(0,_loc4_,360);
         }
      }
      
      public function method_884(param1:PowerType, param2:Entity, param3:uint) : void
      {
         var _loc4_:GfxType = null;
         var _loc5_:String = null;
         var _loc6_:String = null;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:SuperAnimInstance = null;
         var _loc10_:String = null;
         var _loc11_:SuperAnimInstance = null;
         var _loc12_:GfxType = null;
         var _loc13_:Number = NaN;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         var _loc16_:SuperAnimInstance = null;
         var _loc17_:SuperAnimInstance = null;
         _loc4_ = null;
         if(param1.var_1232)
         {
            _loc4_ = param1.var_1232[uint(Math.random() * param1.var_1232.length)];
         }
         else if(param1.var_1700)
         {
            _loc4_ = param1.var_1700[param3 % param1.var_1700.length];
         }
         if(Boolean(_loc4_) && (!param1.var_2927 || !param3))
         {
            _loc9_ = new SuperAnimInstance(this.var_1,_loc4_,this.var_3.var_24 != null);
            this.method_225(param1,_loc9_,param1.var_2605,param2,null,0);
            if(this.var_3.appearPosX > param2.appearPosX || this.var_3 == param2 && !this.var_3.bFacingLeft())
            {
               _loc9_.m_TheDO.scaleX = -1;
            }
            if(!(_loc10_ = param1.powerName).indexOf("ReduceArmor") || !_loc10_.indexOf("Enfeeble") || !_loc10_.indexOf("TouchHeal") || param1.var_301)
            {
               this.var_1.playerEntLayer.addChild(_loc9_.m_TheDO);
            }
            else
            {
               this.var_1.playerEntLayer.addChildAt(_loc9_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(param2.gfx.m_TheDO) + 1);
            }
            param2.combatState.var_372.push(_loc9_);
         }
         if(param1.var_2103)
         {
            this.var_1.method_82(param1.var_2103,this.var_3.var_10,this.var_3.var_12);
         }
         _loc5_ = this.var_3.entType.var_103;
         _loc6_ = this.var_3.entType.var_328;
         _loc7_ = Number(param2.combatState.var_577[_loc5_]);
         _loc8_ = Number(param2.combatState.var_577[_loc6_]);
         if(Boolean(_loc7_) || Boolean(_loc8_))
         {
            _loc11_ = new SuperAnimInstance(this.var_1,var_1005,this.var_3.var_24 != null);
            this.method_225(param1,_loc11_,PowerType.ANIMSOURCE_TARGETCENTER,param2,null,0);
            this.var_1.playerEntLayer.addChildAt(_loc11_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(param2.gfx.m_TheDO) + 1);
            param2.combatState.var_372.push(_loc11_);
         }
         if(param2.combatState.var_2069)
         {
            (_loc12_ = new GfxType()).var_29 = "SFX_3.swf";
            _loc13_ = 0.4;
            _loc14_ = 0.7;
            _loc15_ = _loc13_ + Math.random() * (_loc14_ - _loc13_);
            _loc12_.animScale = _loc15_;
            _loc12_.bFireAndForget = true;
            _loc12_.animClass = "a_FrostBeamHitReact_0" + int(Math.random() * 3 + 1);
            _loc16_ = new SuperAnimInstance(this.var_1,_loc12_,this.var_3.var_24 != null);
            this.method_225(param1,_loc16_,PowerType.const_219,param2,null,0);
            if(param2.var_10 > this.var_3.var_10)
            {
               _loc16_.m_TheDO.scaleX *= -1;
            }
            _loc16_.m_TheDO.rotation = Math.random() * 360;
            this.var_1.playerEntLayer.addChildAt(_loc16_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(param2.gfx.m_TheDO) + 1);
            param2.combatState.var_372.push(_loc16_);
         }
         else if(param2.combatState.var_1857)
         {
            _loc17_ = new SuperAnimInstance(this.var_1,param2.combatState.var_1857,this.var_3.var_24 != null);
            this.method_225(param1,_loc17_,PowerType.ANIMSOURCE_TARGETCENTER,param2,null,0);
            if(param2.var_10 > this.var_3.var_10)
            {
               _loc17_.m_TheDO.scaleX *= -1;
            }
            this.var_1.playerEntLayer.addChildAt(_loc17_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(param2.gfx.m_TheDO) + 1);
            param2.combatState.var_372.push(_loc17_);
         }
      }
      
      public function FireThisPower(param1:PowerType, param2:Point, param3:Array, param4:Boolean, param5:uint, param6:Boolean, param7:uint, param8:Dictionary, param9:int, param10:uint, param11:PowerGroup = null, param12:int = 0) : uint
      {
         var _loc13_:uint = 0;
         var _loc14_:Boolean = false;
         var _loc15_:Entity = null;
         var _loc16_:Vector.<class_140> = null;
         var _loc17_:Vector.<String> = null;
         var _loc18_:Boolean = false;
         var _loc19_:String = null;
         var _loc20_:BuffType = null;
         var _loc21_:uint = 0;
         var _loc22_:Number = NaN;
         var _loc23_:Number = NaN;
         var _loc24_:int = 0;
         var _loc25_:Array = null;
         var _loc26_:Vector.<Entity> = null;
         var _loc27_:int = 0;
         var _loc28_:int = 0;
         var _loc29_:int = 0;
         var _loc30_:Point = null;
         var _loc31_:uint = 0;
         var _loc32_:uint = 0;
         var _loc33_:String = null;
         var _loc34_:* = false;
         var _loc35_:* = false;
         var _loc36_:* = false;
         var _loc37_:* = false;
         var _loc38_:* = false;
         var _loc39_:* = false;
         var _loc40_:Boolean = false;
         var _loc41_:* = false;
         var _loc42_:* = false;
         var _loc43_:* = false;
         var _loc44_:* = false;
         var _loc45_:* = false;
         var _loc46_:* = false;
         var _loc47_:Array = null;
         var _loc48_:Entity = null;
         var _loc49_:uint = 0;
         var _loc50_:Point = null;
         var _loc51_:* = null;
         var _loc52_:Point = null;
         var _loc53_:BuffType = null;
         _loc13_ = param7;
         _loc14_ = PowerType.method_432(param1,this.var_3);
         for each(_loc15_ in param3)
         {
            if(Boolean(_loc15_.method_156()) && (!param8 || !param8[_loc15_.id]))
            {
               if(!(Boolean(param11) && !param11.method_1629(_loc15_)))
               {
                  if(!(_loc15_.behaviorType.var_1094 && !_loc14_))
                  {
                     this.method_884(param1,_loc15_,param5);
                     if(!param1.var_275 || Boolean(_loc15_.var_20 & Entity.LOCAL))
                     {
                        _loc13_++;
                        this.method_1192(param1,_loc15_,param4,param5,_loc13_ == 1,_loc13_,param6,param9,param10,param12);
                        if(Boolean(this.var_1433) && _loc15_.currHP <= 0)
                        {
                           this.method_46(class_14.powerTypesDict["Fury" + this.var_1433],this.var_3,new Point(this.var_3.physPosX,this.var_3.physPosY),true);
                        }
                     }
                  }
               }
            }
         }
         if(param1.basePowerName == "ShadowScythe")
         {
            this.var_3.var_351 = Entity.const_461;
         }
         _loc16_ = new Vector.<class_140>();
         _loc17_ = !!param1.var_437 ? param1.var_437.slice() : null;
         if(this.var_3.var_18)
         {
            _loc17_ = this.var_3.var_18.method_492(_loc17_,param1.basePowerName,"AddSelfBuff");
         }
         if(_loc17_ && (!param1.var_1682 || !param5) && !param1.var_2063)
         {
            for each(_loc19_ in _loc17_)
            {
               if(_loc20_ = class_14.buffTypesDict[_loc19_])
               {
                  _loc21_ = uint(this.var_3.magicDamage);
                  if(this.var_3.var_18)
                  {
                     _loc16_ = this.var_3.var_18.method_101(this.var_3,_loc20_);
                  }
                  this.var_3.combatState.AddBuff(_loc20_,this.var_3,_loc21_,param1.powerID,1,_loc16_);
               }
            }
         }
         _loc18_ = param1 == PowerType.var_511 || param1 == PowerType.var_315;
         if(param1.var_851 && (!param1.var_2629 || param5 == 0) || _loc18_ && this.var_3.mEquipPet)
         {
            if(param1.var_6 == PowerType.TARGETMETHOD_SELF || param1.basePowerName == "PermafrostClone")
            {
               _loc22_ = this.var_3.physPosX;
               _loc23_ = this.var_3.physPosY;
               if(param1.basePowerName == "SummonDragonSoul")
               {
                  if(this.var_3.bFacingLeft())
                  {
                     _loc22_ -= 80;
                  }
                  else
                  {
                     _loc22_ += 80;
                  }
                  _loc23_ += -110 - Math.random() * 20;
               }
               if(!param1.powerName.indexOf("SpawnWasp"))
               {
                  _loc23_ += -110 - Math.random() * 20;
               }
            }
            else
            {
               _loc22_ = param2.x;
               _loc23_ = param2.y;
               if(param1.var_6 == PowerType.TARGETMETHOD_PROJECTILE)
               {
                  _loc30_ = new Point(0,0);
                  if(this.var_1.collMan.getFloorCollision(0,param2.x,param2.y - 150,new Point(0,320),_loc30_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0))
                  {
                     _loc22_ = _loc30_.x;
                     _loc23_ = _loc30_.y;
                  }
               }
            }
            _loc24_ = 0;
            if(this.var_3.var_18)
            {
               _loc24_ = this.var_3.var_18.method_102(this.var_3,param1.basePowerName,"SpawnLimit");
            }
            if(_loc18_)
            {
               if(param1 == PowerType.var_315 && !this.var_3.mEquipPet.mPetType.var_2294)
               {
                  _loc25_ = [];
                  this.RemoveBuff(BuffType.var_709);
               }
               else
               {
                  _loc25_ = ["Pet" + this.var_3.mEquipPet.mPetType.var_310];
               }
            }
            else
            {
               _loc31_ = param1.var_851.length;
               _loc32_ = Math.random() * _loc31_;
               _loc25_ = param1.var_851[_loc32_];
            }
            _loc26_ = this.var_1.GetSummonedCreatures(this.var_3.id,param1);
            _loc27_ = param1.var_1629 + _loc24_ - _loc26_.length;
            if((_loc28_ = int(_loc25_.length)) > _loc27_)
            {
               _loc28_ = _loc27_;
            }
            _loc29_ = 0;
            while(_loc29_ < _loc28_)
            {
               _loc34_ = (_loc33_ = String(_loc25_[_loc29_])) == "DragonSoul";
               _loc35_ = _loc33_ == "PermafrostClone";
               _loc36_ = _loc33_ == "NatureGuard";
               _loc37_ = !_loc33_.indexOf("GhoulGuard");
               _loc38_ = !_loc33_.indexOf("Ghoul2Guard");
               _loc40_ = !(_loc39_ = _loc33_.indexOf("ShadowLegionCloneTwo") == 0) && _loc33_.indexOf("ShadowLegionClone") == 0;
               _loc41_ = _loc33_.indexOf("PolarSentry") >= 0;
               _loc42_ = _loc33_.indexOf("InfestationSpawn") >= 0;
               _loc43_ = _loc33_.indexOf("SummonGuard") >= 0;
               _loc44_ = !_loc33_.indexOf("Decoy");
               _loc45_ = _loc33_.indexOf("Pet") == 0;
               _loc46_ = !_loc33_.indexOf("PetDjinn");
               _loc47_ = EntType.const_132[EntType.const_362];
               if(_loc45_)
               {
                  if(this.var_3.bFacingLeft())
                  {
                     _loc22_ -= 70;
                  }
                  else
                  {
                     _loc22_ += 70;
                  }
                  _loc23_ -= 90;
               }
               else if(_loc36_)
               {
                  _loc49_ = 5;
                  while(_loc49_ <= 50)
                  {
                     if(this.var_3.magicDamage >= _loc47_[_loc49_])
                     {
                        _loc33_ = "NatureGuard" + _loc49_;
                     }
                     _loc49_ += 5;
                  }
               }
               else if(_loc40_ || _loc38_)
               {
                  if(this.var_3.bFacingLeft())
                  {
                     _loc22_ += 60;
                  }
                  else
                  {
                     _loc22_ -= 60;
                  }
                  _loc23_ -= 30;
                  _loc22_ = (_loc50_ = this.method_139(new Point(_loc22_,_loc23_))).x;
                  _loc23_ = _loc50_.y;
               }
               else if(_loc39_ || _loc37_)
               {
                  if(this.var_3.bFacingLeft())
                  {
                     _loc22_ -= 110 - 60 * param5;
                  }
                  else
                  {
                     _loc22_ += 110 - 60 * param5;
                  }
                  _loc23_ -= 30;
                  _loc22_ = (_loc50_ = this.method_139(new Point(_loc22_,_loc23_))).x;
                  _loc23_ = _loc50_.y;
               }
               else if(_loc41_)
               {
                  _loc22_ = (_loc50_ = this.method_139(new Point(_loc22_,_loc23_))).x;
                  _loc23_ = _loc50_.y;
               }
               else if(_loc44_)
               {
                  _loc22_ = (_loc50_ = this.method_139(new Point(_loc22_,_loc23_))).x;
                  _loc23_ = _loc50_.y;
               }
               if(this.var_3.entType.var_913)
               {
                  _loc51_ = _loc33_ + "Hard";
                  if(EntType.method_48(_loc51_))
                  {
                     _loc33_ = _loc51_;
                  }
                  else
                  {
                     class_24.method_19("Spawned Monster: Could not find promoted ent type: " + _loc51_);
                  }
               }
               if(_loc33_ == "FrostWardTotem")
               {
                  _loc22_ = (_loc52_ = this.method_139(new Point(_loc22_,_loc23_))).x;
                  _loc23_ = _loc52_.y + Entity.PULLBACK_DIST;
               }
               if(_loc48_ = new Entity(this.var_1,_loc33_,null,_loc22_,_loc23_ - Entity.PULLBACK_DIST,Entity.LOCAL | Entity.MONSTER,this.var_3.team,0,0,this.var_3.id,param1,null,null,null,null,null))
               {
                  _loc48_.bLeft = this.var_3.bLeft;
                  _loc48_.var_1459 = this.var_1.mTimeThisTick;
                  _loc48_.var_2305 = true;
                  _loc48_.currRoom = this.var_3.currRoom;
                  if(Boolean(this.var_3.brain) && Boolean(this.var_3.brain.target))
                  {
                     _loc48_.brain.AddHate(this.var_3.brain.target,0,false);
                  }
                  if(_loc45_ && Boolean(this.var_3.mEquipPet))
                  {
                     _loc48_.combatState.method_51(this.var_3.mEquipPet.var_1693,false);
                  }
                  if(_loc36_ || _loc40_ || _loc39_ || _loc43_ || _loc42_)
                  {
                     _loc48_.combatState.method_51(class_14.powerTypesDict["MagePetSummon"],false);
                  }
                  if(_loc34_)
                  {
                     _loc48_.combatState.method_51(class_14.powerTypesDict["DragonSoulSummon"],false);
                  }
                  if(_loc37_ || _loc38_)
                  {
                     _loc48_.combatState.method_51(class_14.powerTypesDict["GhoulSummon"],false);
                  }
                  if(_loc35_ && Boolean(param1.var_7))
                  {
                     _loc48_.combatState.method_51(class_14.powerTypesDict["PermafrostCloneExplode" + param1.var_7],false);
                  }
                  if(_loc41_)
                  {
                     _loc48_.combatState.method_51(class_14.powerTypesDict["PolarSentryAppear"],false);
                     _loc48_.combatState.AddBuff(class_14.buffTypesDict["TundraWormBase"],this.var_3,0,param1.powerID);
                  }
                  if(_loc46_)
                  {
                     _loc48_.combatState.AddBuff(class_14.buffTypesDict["PetDjinnInvulnerability"],this.var_3,0,param1.powerID);
                  }
                  if(this.var_3.var_18)
                  {
                     _loc48_.method_1819(this.var_3.var_18.var_1927);
                  }
                  this.var_1.entities.push(_loc48_);
                  if(!_loc33_.indexOf("ShadowLegionClone") && Boolean(this.mActivePower))
                  {
                     _loc48_.entType.gfxType = this.var_3.entType.method_60();
                     _loc48_.var_997 = true;
                     _loc48_.ResetEntType(_loc48_.entType);
                     _loc48_.bLeft = this.mActivePower.var_188;
                     if(this.var_3 == this.var_1.clientEnt)
                     {
                        _loc48_.gfx.method_325(6710886);
                        _loc48_.gfx.var_1854 = 0.8;
                     }
                  }
                  if(_loc40_ || _loc39_)
                  {
                     if(param1.var_7 >= 9)
                     {
                        _loc48_.combatState.AddBuff(class_14.buffTypesDict["AggroBonus120"],this.var_3,this.var_3.magicDamage,param1.powerID);
                     }
                     else if(param1.var_7 >= 8)
                     {
                        _loc48_.combatState.AddBuff(class_14.buffTypesDict["AggroBonus100"],this.var_3,this.var_3.magicDamage,param1.powerID);
                     }
                     else if(param1.var_7 >= 6)
                     {
                        _loc48_.combatState.AddBuff(class_14.buffTypesDict["AggroBonus80"],this.var_3,this.var_3.magicDamage,param1.powerID);
                     }
                     else if(param1.var_7 >= 5)
                     {
                        _loc48_.combatState.AddBuff(class_14.buffTypesDict["AggroBonus60"],this.var_3,this.var_3.magicDamage,param1.powerID);
                     }
                     else if(param1.var_7 >= 3)
                     {
                        _loc48_.combatState.AddBuff(class_14.buffTypesDict["AggroBonus40"],this.var_3,this.var_3.magicDamage,param1.powerID);
                     }
                     else if(param1.var_7 >= 2)
                     {
                        _loc48_.combatState.AddBuff(class_14.buffTypesDict["AggroBonus20"],this.var_3,this.var_3.magicDamage,param1.powerID);
                     }
                  }
                  if(_loc33_.indexOf("Decoy") == 0)
                  {
                     _loc48_.var_997 = true;
                  }
                  if(Boolean(this.var_1574) && _loc48_.behaviorType.var_679)
                  {
                     if(_loc53_ = class_14.buffTypesDict[this.var_1574])
                     {
                        this.AddBuff(_loc53_,this.var_3,this.var_3.magicDamage,param1.powerID,1);
                     }
                  }
               }
               _loc29_++;
            }
         }
         else if(param1 == PowerType.var_315 && !this.var_3.mEquipPet)
         {
            this.RemoveBuff(BuffType.var_709);
         }
         return _loc13_;
      }
      
      public function method_749(param1:PowerType) : void
      {
         this.var_114[param1.powerID] = 0;
      }
      
      public function method_433(param1:PowerType, param2:uint) : void
      {
         this.var_114[param1.powerID] = this.var_1.mTimeThisTick + param2;
      }
      
      public function method_123(param1:uint) : Boolean
      {
         return this.var_1.mTimeThisTick - this.var_2361 >= param1;
      }
      
      public function method_81() : void
      {
         this.var_2361 = this.var_1.mTimeThisTick;
      }
      
      public function method_1503() : uint
      {
         return this.var_1.mTimeThisTick - this.var_2361;
      }
      
      public function method_960() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         var _loc6_:uint = 0;
         var _loc7_:int = 0;
         var _loc8_:SuperAnimInstance = null;
         var _loc9_:ActivePower = null;
         var _loc10_:PowerType = null;
         var _loc11_:int = 0;
         var _loc12_:Point = null;
         var _loc13_:PowerType = null;
         var _loc14_:PowerType = null;
         var _loc15_:Boolean = false;
         var _loc16_:Buff = null;
         var _loc17_:Buff = null;
         var _loc18_:int = 0;
         var _loc19_:Packet = null;
         var _loc20_:GfxType = null;
         var _loc21_:SuperAnimInstance = null;
         var _loc22_:uint = 0;
         _loc1_ = this.var_1.mTimeThisTick;
         _loc2_ = this.var_3.appearPosX - this.var_2145;
         _loc3_ = this.var_3.appearPosY - this.var_2313;
         _loc4_ = int(this.var_372.length - 1);
         while(_loc4_ >= 0)
         {
            if((_loc8_ = this.var_372[_loc4_]).m_bFinished)
            {
               this.var_372.splice(_loc4_,1);
            }
            else
            {
               _loc8_.m_TheDO.x += _loc2_;
               _loc8_.m_TheDO.y += _loc3_;
            }
            _loc4_--;
         }
         this.var_2145 = this.var_3.appearPosX;
         this.var_2313 = this.var_3.appearPosY;
         this.method_322();
         _loc5_ = int(this.var_554.length - 1);
         while(_loc5_ >= 0)
         {
            if(!(_loc9_ = this.var_554[_loc5_]).method_243())
            {
               _loc9_.method_129();
               this.var_554.splice(_loc5_,1);
            }
            _loc5_--;
         }
         if(this.mActivePower)
         {
            if((_loc10_ = this.mActivePower.powerType).damageMultFull > 0 && (_loc10_.manaCost || _loc10_.var_136 != "Melee"))
            {
               this.method_81();
            }
            if(!this.mActivePower.method_243())
            {
               _loc11_ = !!this.mActivePower.var_912 ? this.mActivePower.var_912 : int(this.mActivePower.powerType.manaCost);
               _loc12_ = this.mActivePower.targetPos;
               _loc13_ = this.mActivePower.powerType;
               this.mActivePower.method_129();
               this.mActivePower = null;
               if(_loc13_.var_543)
               {
                  if((Boolean(_loc14_ = class_14.powerTypesDict[_loc13_.var_543])) && this.method_51(_loc14_,false))
                  {
                     this.mActivePower.var_912 = _loc11_;
                     this.mActivePower.var_2314 = true;
                     this.mActivePower.method_299(this.var_3.var_38 != null);
                     if(_loc14_.var_2770 && Boolean(_loc12_))
                     {
                        this.mActivePower.targetPos = _loc12_;
                     }
                  }
               }
            }
            else if(Boolean(this.mActivePower.var_653) && _loc1_ >= this.mActivePower.var_653)
            {
               _loc11_ = this.mActivePower.var_912;
               _loc13_ = this.mActivePower.powerType;
               this.var_554.push(this.mActivePower);
               this.mActivePower = null;
               if(_loc13_.var_543)
               {
                  if((Boolean(_loc14_ = class_14.powerTypesDict[_loc13_.var_543])) && this.method_51(_loc14_,false))
                  {
                     this.mActivePower.var_912 = _loc11_;
                     this.mActivePower.var_2314 = true;
                     this.mActivePower.method_299(this.var_3.var_38 != null);
                  }
               }
            }
         }
         if(this.var_270)
         {
            _loc15_ = !this.method_123(CombatState.const_1228) || this.var_1.level.bInstanced && !this.var_1.level.var_333;
            if(this.var_2173 != _loc15_)
            {
               this.var_2173 = _loc15_;
               this.var_3.RecalculateSpeed();
            }
            if(this.var_683 || this.var_445)
            {
               this.method_841();
               this.method_322();
            }
         }
         _loc6_ = this.var_1157;
         this.var_1157 = 4294967295;
         _loc7_ = int(this.var_84.length - 1);
         while(_loc7_ >= 0)
         {
            if(!(_loc16_ = this.var_84[_loc7_]).method_1095())
            {
               _loc16_.method_258();
               this.var_84.splice(_loc7_,1);
               this.var_555 = true;
            }
            _loc7_--;
         }
         if(this.var_1157 != _loc6_)
         {
            this.var_1910 = true;
         }
         if(!this.mActivePower && this.var_1299 && _loc1_ < this.var_2531)
         {
            this.method_322();
            this.method_51(this.var_1299,false);
            this.var_1299 = null;
         }
         if(!this.var_3.var_38 && this.var_39 && !this.var_545 && (this.var_3.var_31 < this.var_3.GetMeleePower().manaCost || this.var_3.var_31 <= 0 || this.var_3.entState == Entity.const_6))
         {
            if(this.var_39 == class_14.powerTypesDict["SentinelForm1"].powerID)
            {
               this.var_3.combatState.method_46(class_14.powerTypesDict["EndSentinelForm"],this.var_3,new Point(this.var_3.physPosX,this.var_3.physPosY));
               this.var_545 = true;
            }
            else if(this.var_39 == class_14.powerTypesDict["HailstoneEmbrace1"].powerID)
            {
               this.var_3.combatState.method_46(class_14.powerTypesDict["EndFrostArmor"],this.var_3,new Point(this.var_3.physPosX,this.var_3.physPosY));
               this.var_545 = true;
            }
            else if(this.var_39 == class_14.powerTypesDict["SeekingBlades1"].powerID)
            {
               this.var_3.combatState.method_46(class_14.powerTypesDict["EndSeekingBlades"],this.var_3,new Point(this.var_3.physPosX,this.var_3.physPosY));
               this.var_545 = true;
            }
            else if(this.var_39 == class_14.powerTypesDict["Pyromania1"].powerID)
            {
               this.var_3.combatState.method_46(class_14.powerTypesDict["EndPyromania"],this.var_3,new Point(this.var_3.physPosX,this.var_3.physPosY));
               this.var_545 = true;
            }
         }
         if(Boolean(this.var_3.var_20 & Entity.LOCAL) && Boolean(this.var_576) && this.var_3.var_31 <= 0)
         {
            this.RemoveBuff(class_14.buffTypesDict["ShadowArmor" + this.var_576]);
         }
         if(this.var_3.entState == Entity.const_6)
         {
            if(this.mActivePower)
            {
               this.mActivePower.method_640();
               this.mActivePower = null;
            }
            if(this.var_84.length)
            {
               for each(_loc17_ in this.var_84)
               {
                  _loc17_.method_258();
               }
               this.var_84 = new Vector.<Buff>();
               this.var_555 = true;
            }
            this.method_81();
         }
         if(const_1146)
         {
            if(!this.method_1553())
            {
               this.var_2051 = _loc1_;
            }
            else if(_loc1_ - this.var_2051 >= REGEN_INTERVAL)
            {
               if((_loc18_ = !this.var_3.brain ? int(Math.round((REGEN_AMOUNT + this.var_3.var_237 + this.var_546) * this.var_3.maxHP)) : int(Math.round(const_1217 * this.var_3.maxHP))) + this.var_3.currHP > this.var_3.maxHP)
               {
                  _loc18_ = this.var_3.maxHP - this.var_3.currHP;
               }
               if(_loc18_)
               {
                  this.var_3.TakeDamage(-_loc18_,true);
                  if(!this.var_3.behaviorType.var_2303)
                  {
                     (_loc19_ = new Packet(LinkUpdater.const_958)).method_9(this.var_3.id);
                     _loc19_.method_24(_loc18_);
                     this.var_1.serverConn.SendPacket(_loc19_);
                  }
               }
               this.var_2051 = _loc1_;
            }
         }
         if(!this.var_3.var_38)
         {
            if(Boolean(this.var_937) && (!this.mActivePower || this.mActivePower.startTime))
            {
               if(this.masterDangerRegenInterval)
               {
                  if(!this.var_1392 && this.var_3.var_31 < this.var_1660)
                  {
                     this.var_1392 = true;
                     this.AddBuff(class_14.buffTypesDict["FrostShock"],this.var_3,this.var_3.magicDamage,class_14.powerTypesDict["HailstoneEmbrace1"].powerID);
                     (_loc20_ = new GfxType()).var_29 = "SFX_2.swf";
                     _loc20_.bFireAndForget = true;
                     _loc20_.animClass = "a_FrostShock";
                     (_loc21_ = new SuperAnimInstance(this.var_1,_loc20_,true)).m_TheDO.x = this.var_3.appearPosX;
                     _loc21_.m_TheDO.y = this.var_3.appearPosY;
                     this.var_1.playerEntLayer.addChildAt(_loc21_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.var_3.gfx.m_TheDO) + 1);
                  }
                  else if(this.var_1392 && this.var_3.var_31 >= this.var_1660)
                  {
                     this.var_1392 = false;
                     this.RemoveBuff(class_14.buffTypesDict["FrostShock"]);
                  }
               }
               if(!this.var_39 && !this.var_1298 && _loc1_ - this.var_1435 >= this.var_937 && this.var_3.entState != Entity.const_6 && !this.var_3.InActiveCutScene())
               {
                  _loc22_ = this.masterDangerRegenInterval;
                  if(Boolean(this.masterDangerRegenInterval) && Boolean(this.var_3.var_18))
                  {
                     _loc22_ += this.var_3.var_18.method_64("masterDangerRegenInterval");
                  }
                  if(!this.var_1392 || _loc1_ - this.var_1435 >= _loc22_)
                  {
                     Game.var_172.method_142(this.var_3,null,this.var_1995,true,this.var_3.var_31);
                     this.var_3.var_31 += this.var_1995;
                     if(this.var_3.var_31 > this.var_3.const_156)
                     {
                        this.var_3.var_31 = this.var_3.const_156;
                     }
                     else if(this.var_3.var_31 < 0)
                     {
                        this.var_3.var_31 = 0;
                     }
                     this.var_1435 = _loc1_;
                     this.var_1.method_114(this.var_3.var_31);
                  }
               }
            }
         }
      }
      
      private function method_1553() : Boolean
      {
         var _loc1_:Brain = null;
         var _loc2_:BehaviorType = null;
         if(this.var_3.currHP >= this.var_3.maxHP)
         {
            return false;
         }
         if(this.var_3.entState == Entity.const_6)
         {
            return false;
         }
         _loc1_ = this.var_3.brain;
         if(!_loc1_)
         {
            return this.method_123(CANREGEN_TIME);
         }
         _loc2_ = this.var_3.behaviorType;
         if(_loc2_.var_2765)
         {
            return true;
         }
         if(_loc1_.bDeepSleep || Boolean(_loc1_.mostHatedEnt))
         {
            return false;
         }
         if(_loc2_.var_2906)
         {
            return false;
         }
         return true;
      }
      
      public function method_304(param1:int = 5, param2:Boolean = false, param3:Boolean = false) : void
      {
         var _loc4_:BuffType = null;
         var _loc5_:Vector.<BuffType> = null;
         var _loc6_:int = 0;
         var _loc7_:Buff = null;
         var _loc8_:Boolean = false;
         var _loc9_:Boolean = false;
         var _loc10_:Boolean = false;
         _loc5_ = new Vector.<BuffType>();
         _loc6_ = 0;
         for each(_loc7_ in this.var_84)
         {
            if((Boolean(_loc4_ = _loc7_.type)) && _loc4_.var_774)
            {
               _loc8_ = _loc4_.magicDamage < 0 || _loc4_.var_1597 < 0 || _loc4_.meleeDamage < 0 || _loc4_.var_1322 < 0;
               _loc9_ = Boolean(_loc4_.var_772);
               if((_loc10_ = _loc4_.var_1961 || _loc4_.bDisabled || _loc4_.var_876 || _loc4_.var_668 || _loc4_.var_953 || _loc4_.speedChange < 0) || _loc9_ && param2 || _loc8_ && param3)
               {
                  _loc5_.push(_loc4_);
                  _loc6_++;
                  if(Boolean(param1) && _loc6_ >= param1)
                  {
                     break;
                  }
               }
            }
         }
         for each(_loc4_ in _loc5_)
         {
            this.RemoveBuff(_loc4_);
         }
      }
      
      public function method_139(param1:Point) : Point
      {
         var _loc2_:Point = null;
         var _loc3_:Point = null;
         var _loc4_:CollisionManager = null;
         _loc2_ = new Point();
         _loc3_ = new Point();
         var _loc5_:class_37 = (_loc4_ = this.var_1.collMan).getFloorCollision(0,param1.x,param1.y - 1,new Point(0,600),_loc2_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0,0);
         var _loc6_:class_37 = _loc4_.getFloorCollision(0,param1.x,param1.y - 1,new Point(0,-240),_loc3_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0,0);
         return !!_loc2_.y ? _loc2_ : _loc3_;
      }
      
      public function method_1960(param1:Boolean = false) : void
      {
         var _loc2_:PowerType = null;
         var _loc3_:PowerType = null;
         var _loc4_:PowerType = null;
         if(this.var_1586 && !param1 && this.var_1.mTimeThisTick >= this.var_2715)
         {
            if(this.var_1.clientEnt == this.var_3 && this.var_3.mMasterClass == "blademaster")
            {
               _loc2_ = this.var_3.hudPowers[4];
               _loc3_ = this.var_3.hudPowers[5];
               _loc4_ = this.var_3.hudPowers[6];
               this.method_390(_loc2_,this.var_1586);
               this.method_390(_loc3_,this.var_1586);
               this.method_390(_loc4_,this.var_1586);
               if(this.var_2163)
               {
                  this.var_2715 = this.var_1.mTimeThisTick + this.var_2163;
               }
            }
         }
      }
      
      public function method_390(param1:PowerType, param2:Number) : void
      {
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         _loc3_ = uint(this.var_114[param1.powerID]);
         if(_loc3_ > this.var_1.mTimeThisTick)
         {
            _loc4_ = uint(_loc3_ - param1.coolDownTime);
            this.var_114[param1.powerID] = _loc4_ + (1 - param2) * param1.coolDownTime;
         }
      }
      
      public function method_46(param1:PowerType, param2:Entity, param3:Point, param4:Boolean = false) : ActivePower
      {
         var _loc5_:ActivePower = null;
         var _loc6_:int = 0;
         if(param4 && this.var_114[param1.powerID] > this.var_1.mTimeThisTick)
         {
            return null;
         }
         _loc5_ = new ActivePower(this.var_1,param1,this.var_3,param2,param3,0,0,0,false,true);
         this.var_554.push(_loc5_);
         _loc6_ = 0;
         if(this.var_3.var_18)
         {
            _loc6_ = this.var_3.var_18.method_102(this.var_3,param1.basePowerName,"CooldownTime");
         }
         this.var_114[param1.powerID] = this.var_1.mTimeThisTick + param1.coolDownTime + _loc6_;
         return _loc5_;
      }
      
      public function method_2031(param1:PowerType) : ActivePower
      {
         var _loc2_:ActivePower = null;
         _loc2_ = null;
         if(!param1)
         {
            return null;
         }
         for each(_loc2_ in this.var_554)
         {
            if(_loc2_.powerType == param1)
            {
               return _loc2_;
            }
         }
         return null;
      }
      
      public function method_1552(param1:PowerType) : Number
      {
         var _loc2_:Number = NaN;
         _loc2_ = 0;
         if(param1.bIsProjectile && Boolean(this.var_1595))
         {
            _loc2_ += this.var_1595;
         }
         return _loc2_;
      }
   }
}
