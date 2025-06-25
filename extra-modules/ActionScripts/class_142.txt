package
{
   import flash.utils.Dictionary;
   
   public class class_142
   {
      
      public static const const_551:Array = [1,480,528,552,579,607,636,667,699,733,768,805,843,885,927,972,1018,1067,1119,1173,1229,1288,1350,1415,1483,1554,1629,1707,1790,1876,1966,2061,2160,2264,2373,2487,2607,2732,2863,3001,3146,3297,3456,3622,3796,3979,4170,4371,4581,4802,5033];
       
      
      public var var_1:Game;
      
      public var var_134:String;
      
      public var var_2733:Boolean = false;
      
      public var className:String;
      
      public var var_481:String;
      
      public var var_904:uint = 0;
      
      public var var_483:uint = 0;
      
      public var var_476:int = 0;
      
      public var var_952:int = 0;
      
      public var var_1273:int = 0;
      
      public var var_880:int = 0;
      
      public var var_688:int = 0;
      
      public var var_1332:int = 0;
      
      public var var_2892:int = 0;
      
      public var var_1294:int = 0;
      
      public var var_1087:int = 0;
      
      public var var_2555:int = 0;
      
      public var var_2562:int = 0;
      
      public var var_2815:int = 0;
      
      public var var_2447:int = 0;
      
      public var level:int = 0;
      
      public var var_2921:int = 0;
      
      public var maxHP:int = 0;
      
      public var meleeDamage:int = 0;
      
      public var var_2849:int = 0;
      
      public var var_2706:int = 0;
      
      public var var_2579:Number = 0;
      
      public var var_2710:Number = 0;
      
      public var var_1517:int = 0;
      
      public var var_1532:int = 0;
      
      public var var_1578:int = 0;
      
      public var var_1338:int = 0;
      
      public var var_1512:int = 0;
      
      public var var_1300:int = 0;
      
      public var var_222:Dictionary;
      
      public var var_474:uint = 0;
      
      public var var_2368:uint = 0;
      
      public var var_1245:int = 0;
      
      public var var_1224:int = 0;
      
      public var var_2501:int = 1;
      
      public var var_1585:Number = 1;
      
      public var var_2539:uint = 0;
      
      public var var_805:String;
      
      public var var_1691:uint;
      
      public var var_945:uint;
      
      public var var_1206:uint;
      
      public var var_1980:uint;
      
      public var var_2001:uint;
      
      public var var_1827:uint;
      
      public var var_1998:uint;
      
      public var var_1402:uint;
      
      public function class_142(param1:Game, param2:Entity)
      {
         this.var_222 = new Dictionary();
         this.var_805 = new String();
         super();
         this.var_1 = param1;
         if(this.var_1.level)
         {
            this.var_134 = this.var_1.level.internalName;
            this.var_2733 = this.var_1.level.bInstanced && this.var_1.level.internalName != "CraftTown";
         }
         this.var_904 = this.var_1.mTimeThisTick;
         this.var_483 = 0;
         this.method_95("Session Start.");
         if(param2)
         {
            this.className = param2.entType.className;
            this.var_481 = param2.mMasterClass;
            this.level = param2.var_64;
            this.var_2921 = param2.baseMaxHP;
            this.maxHP = param2.maxHP;
            this.meleeDamage = param2.meleeDamage;
            this.var_2849 = param2.magicDamage;
            this.var_2706 = param2.armorClass;
            this.var_2579 = param2.var_1337;
            this.var_2710 = param2.var_667 + param2.var_640;
            this.method_95("Session MasterClass: " + this.var_481 + ", Location: " + this.var_134);
         }
         this.method_513();
      }
      
      public function method_327() : void
      {
         this.method_513();
         if(!this.var_483)
         {
            this.var_483 = this.var_1.mTimeThisTick;
            this.method_95("Session End.");
         }
      }
      
      public function method_513() : void
      {
         var _loc1_:int = this.var_1.var_2142 + 1;
         var _loc2_:uint = uint(this.var_1.mTimeThisTick - this.var_2539);
         var _loc3_:uint = uint(this.var_1.mTimeThisTick - this.var_904);
         if(_loc3_)
         {
            this.var_1585 = (this.var_2501 * _loc2_ + this.var_1585 * (_loc3_ - _loc2_)) / _loc3_;
         }
         this.var_2501 = _loc1_;
         this.var_2539 = this.var_1.mTimeThisTick;
      }
      
      public function method_81() : void
      {
         var _loc1_:uint = this.var_1.mTimeThisTick;
         var _loc2_:uint = uint(_loc1_ - this.var_2368);
         if(_loc2_ < class_91.const_1123)
         {
            this.var_474 += _loc2_;
         }
         else
         {
            this.method_95("Combat End.",this.var_2368);
            this.method_95("Combat Start.");
         }
         this.var_2368 = _loc1_;
      }
      
      public function method_499(param1:Entity, param2:PowerType) : void
      {
         if(!param2)
         {
            return;
         }
         if(param1 != this.var_1.clientEnt)
         {
            return;
         }
         if(!this.var_222[param2.powerName])
         {
            this.var_222[param2.powerName] = new class_166(param2);
         }
         var _loc3_:class_166 = this.var_222[param2.powerName];
         _loc3_.method_1538(this.var_1.mTimeThisTick);
         this.method_95("Player used power " + param2.powerName);
      }
      
      public function method_175(param1:PowerType, param2:Entity, param3:Entity, param4:int, param5:Boolean, param6:Boolean = false) : void
      {
         var _loc12_:Boolean = false;
         var _loc13_:class_166 = null;
         if(!param1 || param4 == 0)
         {
            return;
         }
         var _loc7_:Boolean = true;
         var _loc8_:Boolean = true;
         var _loc9_:Entity = this.var_1.clientEnt;
         var _loc10_:* = param4 < 0;
         if(param3 == _loc9_)
         {
            if(param5)
            {
               if(_loc10_)
               {
                  this.var_2562 += -param4;
               }
               else
               {
                  this.var_1332 += param4;
               }
            }
            else if(_loc10_)
            {
               this.var_1087 += -param4;
            }
            else
            {
               this.var_688 += param4;
            }
            if(_loc8_)
            {
               this.method_95("Player received " + (_loc10_ ? -param4 + " health " : param4 + " damage ") + "from " + (!!param2 ? param2.entType.entName : "No Source") + " with " + param1.powerName);
            }
         }
         var _loc11_:Boolean;
         if((_loc11_ = Boolean(param2) && Boolean(param2.summonerId) && this.var_1.GetEntFromID(param2.summonerId) == _loc9_) && Boolean(param2.var_99))
         {
            param1 = param2.var_99;
         }
         if(param2 == _loc9_ || _loc11_)
         {
            _loc12_ = Boolean(param3) && _loc9_.team != param3.team && param3.team != Entity.NEUTRAL;
            if(_loc11_)
            {
               if(_loc10_ && !_loc12_)
               {
                  if(param5)
                  {
                     this.var_2815 += -param4;
                  }
                  else
                  {
                     this.var_2447 += -param4;
                  }
               }
               else if(!_loc10_ && _loc12_)
               {
                  if(param5)
                  {
                     this.var_1273 += param4;
                  }
                  else
                  {
                     this.var_880 += param4;
                  }
               }
            }
            else if(_loc10_ && !_loc12_)
            {
               if(param5)
               {
                  this.var_2555 += -param4;
               }
               else
               {
                  this.var_1294 += -param4;
               }
            }
            else if(!_loc10_ && _loc12_)
            {
               if(param5)
               {
                  this.var_952 += param4;
               }
               else
               {
                  this.var_476 += param4;
               }
            }
            else
            {
               _loc8_ = false;
               _loc7_ = false;
            }
            if(_loc7_)
            {
               if(!this.var_222[param1.powerName])
               {
                  this.var_222[param1.powerName] = new class_166(param1);
               }
               (_loc13_ = this.var_222[param1.powerName]).method_175(param4,_loc10_,param5,_loc11_,param6);
            }
            if(_loc8_)
            {
               if(param5)
               {
                  this.method_95((_loc11_ ? "Player Pet" : "Player") + " " + (_loc10_ ? "Healed" : "Dealt") + " " + param4 + " base damage on target " + (!!param3 ? param3.entType.entName : "None") + " with " + param1.powerName);
               }
               else
               {
                  this.method_95((_loc11_ ? "Player Pet" : "Player") + " " + (_loc10_ ? "Healed" : "Dealt") + " " + param4 + " final damage on target " + (!!param3 ? param3.entType.entName : "None") + " with " + param1.powerName);
               }
            }
         }
      }
      
      public function method_142(param1:Entity, param2:PowerType, param3:int, param4:Boolean = false, param5:int = 0) : void
      {
         var _loc7_:class_166 = null;
         if(!param3)
         {
            return;
         }
         if(param1 != this.var_1.clientEnt)
         {
            return;
         }
         var _loc6_:int = param5 + param3;
         if(param4)
         {
            if(param3 > 0)
            {
               this.var_1338 += param3;
            }
            else
            {
               this.var_1512 += param3;
            }
            if(_loc6_ > 100)
            {
               this.var_1300 += _loc6_ - 100;
            }
         }
         else
         {
            if(param3 > 0)
            {
               this.var_1517 += param3;
            }
            else
            {
               this.var_1532 += param3;
            }
            if(_loc6_ > 80)
            {
               this.var_1578 += _loc6_ - 80;
            }
         }
         if(param3 < 0 && Boolean(param2))
         {
            if(!this.var_222[param2.powerName])
            {
               this.var_222[param2.powerName] = new class_166(param2);
            }
            (_loc7_ = this.var_222[param2.powerName]).method_1423(Math.abs(param3));
         }
         this.method_95((param4 ? "Master Mana" : "Mana") + " change: " + param3 + " from source power: " + (!!param2 ? param2.displayName : "None") + ". New value: " + (param4 ? param1.var_31 : param1.var_228));
      }
      
      public function method_410(param1:PowerType, param2:Entity, param3:Entity) : void
      {
         var _loc6_:Boolean = false;
         var _loc7_:class_166 = null;
         var _loc4_:Entity = this.var_1.clientEnt;
         if(param3 == _loc4_)
         {
            ++this.var_1245;
            this.method_95("Player killed by " + (!!param2 ? param2.entType.entName : "No SourceEnt") + " power: " + (!!param1 ? param1.powerName : "No PowerType"));
            return;
         }
         if(!param1 || !param3)
         {
            return;
         }
         var _loc5_:Boolean;
         if((_loc5_ = Boolean(param2) && Boolean(param2.summonerId) && this.var_1.GetEntFromID(param2.summonerId) == _loc4_) && Boolean(param2.var_99))
         {
            param1 = param2.var_99;
         }
         if(param2 == _loc4_ || _loc5_)
         {
            if(!(_loc6_ = _loc4_.team != param3.team && param3.team != Entity.NEUTRAL))
            {
               return;
            }
            ++this.var_1224;
            this.method_95("Enemy " + param3.entType.entName + " killed by power: " + param1.powerName);
            if(!this.var_222[param1.powerName])
            {
               this.var_222[param1.powerName] = new class_166(param1);
            }
            (_loc7_ = this.var_222[param1.powerName]).method_1912();
         }
      }
      
      public function method_95(param1:String, param2:uint = 0) : void
      {
         var _loc3_:uint = !!param2 ? param2 : this.var_1.mTimeThisTick;
         if(!this.var_805)
         {
            this.var_805 = new String();
         }
         if(param1)
         {
            this.var_805 += _loc3_ + ": " + param1;
            this.var_805 += "\r\n";
         }
      }
      
      public function method_1659() : String
      {
         var _loc1_:* = new String();
         var _loc2_:uint = !!this.var_483 ? this.var_483 : this.var_1.mTimeThisTick;
         _loc1_ += "Master Class: " + this.var_481 + "\r\n";
         _loc1_ += "Dungeon: " + this.var_134 + "\r\n";
         _loc1_ += "Play Time: " + (_loc2_ - this.var_904) + "\r\n";
         _loc1_ += "Time in Combat: " + this.var_474 + "\r\n";
         _loc1_ += "Average Group Size: " + this.var_1585 + "\r\n";
         _loc1_ += "baseDPS: " + 1000 * (this.var_952 + this.var_1273) / this.var_474 / this.meleeDamage + "\r\n";
         _loc1_ += "finalDPS: " + 1000 * (this.var_476 + this.var_880) / this.var_474 / this.meleeDamage + "\r\n";
         _loc1_ += "Total damage dealt (Player): " + this.var_476 + "\r\n";
         _loc1_ += "Total damage dealt (Pets): " + this.var_880 + "\r\n";
         _loc1_ += "Total base damage dealt (Player): " + this.var_952 + "\r\n";
         _loc1_ += "Total base damage dealt (Pets): " + this.var_1273 + "\r\n";
         _loc1_ += "Number of Kills: " + this.var_1224 + "\r\n";
         _loc1_ += "Healing Dealt: " + this.var_1294 + "\r\n";
         _loc1_ += "Damage Received: " + this.var_688 + "\r\n";
         _loc1_ += "Damage Resisted: " + (this.var_1332 - this.var_688) + "\r\n";
         _loc1_ += "Number of Deaths: " + this.var_1245 + "\r\n";
         _loc1_ += "Healing Received: " + this.var_1087 + "\r\n";
         _loc1_ += "Mana Gained: " + this.var_1517 + "\r\n";
         _loc1_ += "Mana Spent: " + this.var_1532 + "\r\n";
         _loc1_ += "Mana Wasted: " + this.var_1578 + "\r\n";
         _loc1_ += "Master Mana Gained: " + this.var_1338 + "\r\n";
         _loc1_ += "Master Mana Spent: " + this.var_1512 + "\r\n";
         _loc1_ += "Master Mana Wasted: " + this.var_1300 + "\r\n";
         _loc1_ += "Primary Damage Stat: " + this.meleeDamage + "\r\n";
         _loc1_ += "Max HP: " + this.maxHP + "\r\n";
         _loc1_ += "----- \r\n";
         return _loc1_ + this.var_805;
      }
      
      public function method_1451() : String
      {
         var _loc3_:class_166 = null;
         var _loc1_:* = new String();
         var _loc2_:uint = !!this.var_483 ? this.var_483 : this.var_1.mTimeThisTick;
         _loc1_ += "Master Class: " + this.var_481 + "\r\n";
         _loc1_ += "Dungeon: " + this.var_134 + "\r\n";
         _loc1_ += "Play Time: " + (_loc2_ - this.var_904) + "\r\n";
         _loc1_ += "Time in Combat: " + this.var_474 + "\r\n";
         _loc1_ += "Average Group Size: " + this.var_1585 + "\r\n";
         _loc1_ += "DPS: " + 1000 * (this.var_952 + this.var_1273) / this.var_474 / this.meleeDamage + "\r\n";
         _loc1_ += "Total damage dealt (Player): " + this.var_476 + "\r\n";
         _loc1_ += "Total damage dealt (Pets): " + this.var_880 + "\r\n";
         _loc1_ += "Number of Kills: " + this.var_1224 + "\r\n";
         _loc1_ += "Healing Dealt: " + this.var_1294 + "\r\n";
         _loc1_ += "Damage Received: " + this.var_688 + "\r\n";
         _loc1_ += "Damage Resisted: " + (this.var_1332 - this.var_688) + "\r\n";
         _loc1_ += "Number of Deaths: " + this.var_1245 + "\r\n";
         _loc1_ += "Healing Received: " + this.var_1087 + "\r\n";
         _loc1_ += "Mana Gained: " + this.var_1517 + "\r\n";
         _loc1_ += "Mana Spent: " + this.var_1532 + "\r\n";
         _loc1_ += "Mana Wasted: " + this.var_1578 + "\r\n";
         _loc1_ += "Master Mana Gained: " + this.var_1338 + "\r\n";
         _loc1_ += "Master Mana Spent: " + this.var_1512 + "\r\n";
         _loc1_ += "Master Mana Wasted: " + this.var_1300 + "\r\n";
         _loc1_ += "Primary Damage Stat: " + this.meleeDamage + "\r\n";
         _loc1_ += "Max HP: " + this.maxHP + "\r\n";
         _loc1_ += "\r\n";
         for each(_loc3_ in this.var_222)
         {
            _loc1_ += _loc3_.var_1059 + ": \r\n";
            _loc1_ += "Times Used: " + _loc3_.var_322 + "\r\n";
            if(Boolean(_loc3_.var_563) || Boolean(_loc3_.var_236) || Boolean(_loc3_.var_201))
            {
               _loc1_ += "Total Kills: " + _loc3_.var_563 + "\r\n";
            }
            if(Boolean(_loc3_.var_236) || Boolean(_loc3_.var_201))
            {
               _loc1_ += "Average Damage: " + (_loc3_.var_236 + _loc3_.var_201) / _loc3_.var_322 + "\r\n";
            }
            if(Boolean(_loc3_.var_236) || Boolean(_loc3_.var_201))
            {
               _loc1_ += "% of total damage: " + 100 * (_loc3_.var_236 + _loc3_.var_201) / this.var_476 + "\r\n";
            }
            if(Boolean(_loc3_.var_550) || Boolean(_loc3_.var_201))
            {
               _loc1_ += "Average Healing: " + (_loc3_.var_550 + _loc3_.var_768) / _loc3_.var_322 + "\r\n";
            }
            _loc1_ += "\r\n";
         }
         return _loc1_;
      }
      
      public function method_479(param1:Packet) : void
      {
         var _loc4_:class_166 = null;
         var _loc2_:uint = !!this.var_483 ? this.var_483 : this.var_1.mTimeThisTick;
         var _loc3_:int = int(const_551[this.level]);
         if(_loc3_ == 0)
         {
            _loc3_ = 1;
         }
         param1.method_20(Game.const_209,Game.method_766(this.var_481));
         param1.method_9(this.level);
         param1.method_9(_loc2_ - this.var_904);
         param1.method_9(this.var_474);
         param1.method_24(this.var_476);
         param1.method_24(this.var_880);
         param1.method_24(_loc3_);
         param1.method_24(this.var_1224);
         param1.method_24(this.var_1294);
         param1.method_24(this.var_688);
         param1.method_24(this.var_1332 - this.var_688);
         param1.method_24(this.var_1245);
         param1.method_24(this.var_1087);
         param1.method_24(this.meleeDamage);
         param1.method_24(this.var_2849);
         param1.method_24(this.var_2706);
         param1.method_24(this.var_2579 * 1000);
         param1.method_24(this.var_2710 * 1000);
         param1.method_24(this.maxHP);
         param1.method_24(1000 * this.var_1585);
         param1.method_20(class_119.const_228,this.var_1691);
         param1.method_9(this.var_1206);
         param1.method_9(this.var_1980);
         param1.method_9(this.var_2001);
         param1.method_9(this.var_1827);
         param1.method_9(this.var_1998);
         param1.method_9(this.var_1402);
         for each(_loc4_ in this.var_222)
         {
            param1.method_15(true);
            _loc4_.method_479(param1);
         }
         param1.method_15(false);
      }
      
      public function method_548(param1:uint, param2:uint, param3:uint, param4:uint, param5:uint, param6:uint, param7:uint, param8:uint) : void
      {
         this.var_1691 = param1;
         this.var_945 = param2;
         this.var_1206 = param3;
         this.var_1980 = param4;
         this.var_2001 = param5;
         this.var_1827 = param6;
         this.var_1998 = param7;
         this.var_1402 = param8;
      }
   }
}
