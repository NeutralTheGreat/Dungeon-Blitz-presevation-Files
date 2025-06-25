package
{
   import flash.geom.Point;
   import flash.utils.Dictionary;
   
   public class Buff
   {
      
      public static const const_885:Number = 1.5;
      
      public static const const_1202:Number = 0.85;
      
      public static const const_1128:int = -200;
       
      
      internal var var_1:Game;
      
      internal var var_4:Entity;
      
      internal var var_47:Vector.<class_141>;
      
      internal var var_1737:Vector.<class_140>;
      
      internal var gfxType:GfxType;
      
      internal var var_1624:GfxType;
      
      internal var var_176:SuperAnimInstance;
      
      internal var var_283:SuperAnimInstance;
      
      internal var type:BuffType;
      
      internal var startTime:uint;
      
      internal var var_1399:uint;
      
      private var var_1011:uint;
      
      private var var_561:uint = 0;
      
      private var var_1070:uint;
      
      private var var_1209:uint;
      
      internal var var_619:int;
      
      internal var var_590:int;
      
      internal var var_1114:Boolean = false;
      
      internal var var_2996:SuperAnimInstance;
      
      internal var var_1663:uint = 0;
      
      internal var var_666:uint = 0;
      
      internal var var_2638:uint = 0;
      
      internal var var_2325:uint = 0;
      
      internal var var_830:int = 0;
      
      internal var var_1590:int = 0;
      
      internal var var_771:int = 0;
      
      internal var var_1211:Entity;
      
      internal var var_2005:PowerType;
      
      internal var var_1420:Entity;
      
      internal var var_2932:uint = 2000;
      
      public function Buff(param1:Entity, param2:BuffType, param3:int = 0, param4:Vector.<class_140> = null)
      {
         this.var_47 = new Vector.<class_141>();
         super();
         this.var_4 = param1;
         this.var_1 = param1.var_1;
         this.type = param2;
         this.var_619 = param3;
         this.var_590 = 0;
         this.var_1737 = param4;
         var _loc5_:uint = this.var_4.entType.height;
         this.var_666 = BuffType.const_48 - 1;
         while(Boolean(this.var_666) && _loc5_ <= BuffType.const_368[this.var_666])
         {
            --this.var_666;
         }
         if(this.type.var_306)
         {
            this.gfxType = this.type.var_306[this.var_666];
         }
         if(this.type.var_247)
         {
            this.var_1624 = this.type.var_247[this.var_666];
         }
         if(!this.type.var_1268)
         {
            this.method_971();
         }
         if((Boolean(this.type.var_932) || Boolean(this.type.var_1235)) && Boolean(this.var_4.gfx))
         {
            if(this.type.buffName == "FrostShock")
            {
               this.var_4.gfx.method_627(this.type.var_932,this.type.var_1235);
            }
            this.var_4.gfx.method_325(this.type.var_932,this.type.var_1235);
         }
         if(param2.var_2192)
         {
            this.var_1663 = this.var_1.mTimeThisTick + param2.var_2192;
         }
      }
      
      private function method_971() : void
      {
         var _loc1_:int = 0;
         var _loc2_:int = 0;
         if(this.type.var_2789)
         {
            _loc1_ = !!this.type.var_306 ? int(this.type.var_306.length) : (!!this.type.var_247 ? int(this.type.var_247.length) : 0);
            if(_loc1_)
            {
               _loc2_ = Math.floor(Math.random() * _loc1_ / BuffType.const_48);
               this.gfxType = !!this.type.var_306 ? this.type.var_306[_loc2_ * BuffType.const_48 + this.var_666] : null;
               this.var_1624 = !!this.type.var_247 ? this.type.var_247[_loc2_ * BuffType.const_48 + this.var_666] : null;
            }
         }
         if(this.gfxType)
         {
            if(this.gfxType.var_927)
            {
               this.var_4.gfx.method_366(this.gfxType);
            }
            else
            {
               this.var_176 = new SuperAnimInstance(this.var_1,this.gfxType,this.var_4.var_24 != null);
               this.var_1.playerEntLayer.addChildAt(this.var_176.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.var_4.gfx.m_TheDO) + 1);
            }
         }
         if(this.var_1624)
         {
            this.var_283 = new SuperAnimInstance(this.var_1,this.var_1624,this.var_4.var_24 != null);
            this.var_1.playerEntLayer.addChildAt(this.var_283.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.var_4.gfx.m_TheDO));
         }
      }
      
      public function method_1095() : Boolean
      {
         var _loc11_:uint = 0;
         var _loc12_:Number = NaN;
         var _loc13_:int = 0;
         var _loc14_:int = 0;
         var _loc15_:GfxType = null;
         var _loc16_:SuperAnimInstance = null;
         var _loc17_:Number = NaN;
         var _loc18_:Number = NaN;
         var _loc19_:GfxType = null;
         var _loc20_:SuperAnimInstance = null;
         var _loc21_:Number = NaN;
         var _loc22_:Number = NaN;
         var _loc23_:Number = NaN;
         var _loc24_:Packet = null;
         var _loc25_:PowerType = null;
         var _loc26_:Number = NaN;
         var _loc1_:Number = this.method_59("Duration");
         var _loc2_:Number = this.method_59("DoTDamage");
         var _loc3_:Number = this.method_59("DoTTickLeft");
         if(this.type.var_2030 && (!this.var_4.var_38 || this.var_4.team != Entity.GOODGUY))
         {
            if(!this.var_1211 || !this.var_1211.bIAmValid || this.var_1211.entState == Entity.const_6)
            {
               if(!this.var_4.var_38)
               {
                  this.method_534();
               }
               return false;
            }
         }
         var _loc4_:Number = this.type.var_1679;
         if(this.type.var_635)
         {
            _loc4_ = (this.type.var_454 + _loc1_) / (this.type.var_635 + _loc3_);
         }
         var _loc5_:uint = this.var_1.mTimeThisTick;
         var _loc6_:Number = 0;
         if(this.type.var_2620)
         {
            _loc6_ = this.var_4.var_571;
         }
         var _loc8_:uint = this.type.var_454 * 1 + _loc1_;
         this.var_4.combatState.var_1157 &= 4294967295;
         if(Boolean(this.type.var_635 + _loc3_) && (!_loc4_ || this.var_1399 < _loc4_))
         {
            if((_loc11_ = this.var_2638 + (this.type.var_635 + _loc3_) * (1 + this.var_2325)) <= _loc5_)
            {
               if(this.type.var_1268)
               {
                  this.method_971();
               }
               ++this.var_1399;
               ++this.var_2325;
               if(!this.var_4.var_38)
               {
                  _loc12_ = !!_loc4_ ? (this.type.var_772 + _loc2_) / _loc4_ : this.type.var_772 + _loc2_;
                  if((_loc13_ = Math.round(_loc12_ * this.var_561) * this.method_351()) < 0)
                  {
                     _loc13_ += Math.floor((this.var_4.var_237 + this.var_4.combatState.var_546) * _loc13_);
                     _loc14_ = this.var_4.currHP - this.var_4.maxHP;
                     if(_loc13_ < _loc14_)
                     {
                        _loc13_ = _loc14_ < 0 ? _loc14_ : 0;
                     }
                  }
                  else
                  {
                     _loc13_ = Math.round(_loc13_ * const_885);
                  }
                  if(this.type.buffName == "MistEffect" || this.type.var_2250)
                  {
                     (_loc15_ = new GfxType()).var_29 = "SFX_3.swf";
                     _loc15_.bFireAndForget = true;
                     if(!this.var_4.var_1170)
                     {
                        _loc15_.animClass = "a_FrostArmorWorldMist" + int(Math.random() * 5);
                        _loc16_ = new SuperAnimInstance(this.var_1,_loc15_,true);
                        if(this.var_4.bFacingLeft())
                        {
                           _loc16_.m_TheDO.scaleX = -1;
                        }
                        this.var_1.playerEntLayer.addChildAt(_loc16_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.var_4.gfx.m_TheDO) + 1);
                        _loc18_ = -(_loc17_ = 30) + Math.random() * (_loc17_ - -_loc17_);
                        _loc16_.m_TheDO.x = this.var_4.var_10 + _loc18_;
                        _loc16_.m_TheDO.y = this.var_4.appearPosY + Math.random() * 15;
                     }
                  }
                  if(this.type.buffName == "Blink")
                  {
                     (_loc19_ = new GfxType()).var_29 = "SFX_3.swf";
                     _loc19_.bFireAndForget = true;
                     _loc19_.animClass = "a_FrostParticles";
                     (_loc20_ = new SuperAnimInstance(this.var_1,_loc19_,true)).m_TheDO.scaleX = 0.3;
                     _loc20_.m_TheDO.scaleY = 0.3;
                     _loc20_.m_TheDO.rotation = 90;
                     _loc20_.m_TheDO.alpha = 0.75;
                     if(this.var_4.bFacingLeft())
                     {
                        _loc20_.m_TheDO.scaleX *= -1;
                     }
                     this.var_1.playerEntLayer.addChildAt(_loc20_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.var_4.gfx.m_TheDO) + 1);
                     _loc21_ = Math.random() * -50;
                     _loc23_ = -(_loc22_ = 50) + Math.random() * (_loc22_ - -_loc22_);
                     _loc20_.m_TheDO.x = this.var_4.var_10 + _loc21_;
                     _loc20_.m_TheDO.y = this.var_4.var_12 + _loc23_;
                  }
                  if(Boolean(this.var_4.var_1028) && _loc13_ > 0)
                  {
                     if((_loc13_ -= Math.ceil(_loc13_ * this.var_4.var_1028)) < 0)
                     {
                        _loc13_ = 0;
                     }
                  }
                  if(_loc13_ > 0 && this.var_4.combatState.method_924(false))
                  {
                     _loc13_ = 0;
                  }
                  if(_loc13_)
                  {
                     Game.var_172.method_175(class_14.powerTypes[this.var_1209],this.var_1.GetEntFromID(this.var_1070),this.var_4,_loc13_,true,false);
                     _loc13_ *= this.method_1572(_loc13_);
                     this.var_4.combatState.method_294(this.var_1.GetEntFromID(this.var_1070),_loc13_,null,this.var_1209);
                     if(!this.var_4.behaviorType.var_2303)
                     {
                        (_loc24_ = new Packet(LinkUpdater.PKTTYPE_BUFF_TICK_DOT)).method_9(this.var_4.id);
                        _loc24_.method_9(this.var_1070);
                        _loc24_.method_9(this.var_1209);
                        _loc24_.method_24(_loc13_);
                        this.var_1.serverConn.SendPacket(_loc24_);
                     }
                  }
               }
               if(this.var_2005 && this.var_1420 && this.var_1.clientEntID == this.var_1420.id)
               {
                  this.var_1420.combatState.method_46(this.var_2005,null,new Point(this.var_4.physPosX,this.var_4.physPosY));
               }
            }
         }
         if(this.type.var_772 > 0)
         {
            this.var_4.combatState.method_81();
         }
         this.UpdatePos(this.var_4.appearPosX,this.var_4.appearPosY);
         if(this.type.var_454 + _loc1_ && _loc5_ >= _loc9_ && !this.var_4.var_38)
         {
            if(this.type.buffName.indexOf("DetShield") == 0)
            {
               if(Boolean(this.var_4) && Boolean(this.var_4.combatState.var_651))
               {
                  _loc25_ = class_14.powerTypesDict["DetShieldDetonate" + this.var_4.combatState.var_651];
                  this.var_4.combatState.method_46(_loc25_,null,new Point(this.var_4.var_10,this.var_4.var_12));
               }
            }
            this.method_534();
            return false;
         }
         if(Boolean(this.type.var_956) && !this.var_4.InActiveCutScene())
         {
            _loc26_ = this.method_59("DrainMasterManaInterval");
            if(this.var_1.mTimeThisTick > this.var_1663 && this.var_1.mTimeThisTick - this.var_1663 >= this.type.var_956 + _loc26_)
            {
               Game.var_172.method_142(this.var_4,class_14.powerTypes[this.var_1209],-1,true,this.var_4.var_31);
               this.var_1663 = this.var_1.mTimeThisTick;
               --this.var_4.var_31;
               if(this.var_4.var_31 <= 0)
               {
                  this.var_4.var_31 = 0;
               }
               if(this.var_4.id == this.var_1.clientEntID)
               {
                  this.var_1.method_114(this.var_4.var_31);
               }
            }
         }
         return true;
      }
      
      public function method_1572(param1:int) : Number
      {
         var _loc2_:Number = 1;
         if(this.type.var_2403 && Boolean(this.var_4.combatState.var_1032))
         {
            _loc2_ += this.method_59("BleedMultiplier");
         }
         if(this.var_4.combatState.var_1033)
         {
            _loc2_ += this.method_59("BoundMultiplier");
         }
         return _loc2_;
      }
      
      public function UpdatePos(param1:Number, param2:Number) : void
      {
         var _loc3_:Point = null;
         if(Boolean(this.var_176) && Boolean(this.var_176.m_TheDO))
         {
            this.var_176.m_TheDO.x = param1;
            this.var_176.m_TheDO.y = param2;
            if(this.type.var_668 || this.type.var_876 || this.type.var_1708)
            {
               this.var_176.m_TheDO.y -= this.var_4.entType.height;
            }
            else if(this.type.var_1627)
            {
               this.var_176.m_TheDO.y -= this.var_4.entType.height * 0.5;
            }
            else if(this.type.var_2019)
            {
               if(this.var_4.combatState.mActivePower)
               {
                  _loc3_ = this.var_4.method_219(new Point(param1,param2),this.var_4.combatState.mActivePower.powerType.var_136);
                  this.var_176.m_TheDO.x = _loc3_.x;
                  this.var_176.m_TheDO.y = _loc3_.y;
               }
            }
         }
         if(Boolean(this.var_283) && Boolean(this.var_283.m_TheDO))
         {
            this.var_283.m_TheDO.x = param1;
            this.var_283.m_TheDO.y = param2;
            if(this.type.var_668 || this.type.var_876 || this.type.var_1708)
            {
               this.var_283.m_TheDO.y -= this.var_4.entType.height;
            }
            else if(this.type.var_1627)
            {
               this.var_283.m_TheDO.y -= this.var_4.entType.height * 0.5;
            }
            else if(this.type.var_2019)
            {
               if(this.var_4.combatState.mActivePower)
               {
                  _loc3_ = this.var_4.method_219(new Point(param1,param2),this.var_4.combatState.mActivePower.powerType.var_136);
                  this.var_176.m_TheDO.x = _loc3_.x;
                  this.var_176.m_TheDO.y = _loc3_.y;
               }
            }
         }
      }
      
      public function method_351() : uint
      {
         var _loc1_:int = this.method_59("StackCount");
         return this.var_1011 > this.type.stackCount + _loc1_ ? uint(this.type.stackCount + _loc1_) : this.var_1011;
      }
      
      private function method_917(param1:uint, param2:Boolean) : class_141
      {
         var _loc3_:int = 0;
         var _loc5_:class_141 = null;
         var _loc4_:int = int(this.var_47.length);
         _loc3_ = 0;
         while(_loc3_ < _loc4_)
         {
            if((_loc5_ = this.var_47[_loc3_]).entID == param1)
            {
               if(param2)
               {
                  this.var_47.splice(_loc3_,1);
               }
               return _loc5_;
            }
            _loc3_++;
         }
         return null;
      }
      
      public function method_1559(param1:uint, param2:uint, param3:uint, param4:uint, param5:uint) : void
      {
         var _loc8_:int = 0;
         var _loc9_:Dictionary = null;
         var _loc10_:uint = 0;
         var _loc6_:class_141;
         if(!(_loc6_ = this.method_917(param1,false)))
         {
            _loc6_ = new class_141(param1,this.type.buffID,0,param4);
            this.var_47.push(_loc6_);
            this.var_2638 = this.var_1.mTimeThisTick;
         }
         _loc6_.var_342 = param4;
         this.var_1070 = param1;
         this.var_1209 = param4;
         if(this.type.var_2424)
         {
            _loc8_ = Math.ceil(this.var_561 * this.var_1399 / this.type.var_1679);
            this.var_561 += param3 - _loc8_;
            _loc6_.stackCount = 1;
            this.var_1011 = 1;
            if(param5)
            {
               this.var_771 = class_142.const_551[param5];
            }
         }
         else
         {
            _loc6_.stackCount += param2;
            this.var_1011 += param2;
            if(param3 > this.var_561)
            {
               this.var_561 = param3;
               if(param5)
               {
                  this.var_771 = class_142.const_551[param5];
               }
            }
         }
         if(!param5 && !this.var_771)
         {
            this.var_771 = 0;
         }
         this.var_1399 = 0;
         var _loc7_:uint = this.startTime;
         this.startTime = this.var_1.mTimeThisTick;
         if(Boolean(this.type.var_221) && !(this.var_4.var_20 & Entity.PLAYER))
         {
            if((_loc10_ = uint((_loc9_ = this.var_4.combatState.var_1654)[this.type.var_221])) == 1)
            {
               this.startTime -= this.type.var_454 * 0.5;
            }
            else if(_loc10_ == 2)
            {
               this.startTime -= this.type.var_454 * 0.75;
            }
            else if(_loc10_ >= 3)
            {
               this.startTime -= this.type.var_454;
            }
            _loc9_[this.type.var_221] = _loc10_ + 1;
            if(_loc7_ > this.startTime)
            {
               this.startTime = _loc7_;
            }
         }
         if(this.type.var_2728)
         {
            this.var_2005 = class_14.powerTypesDict[this.type.var_2728];
            this.var_1420 = this.var_1.GetEntFromID(param1);
         }
      }
      
      public function method_1515(param1:uint) : Boolean
      {
         var _loc3_:class_141 = null;
         var _loc2_:class_141 = this.method_917(param1,true);
         if(_loc2_)
         {
            this.var_1011 -= _loc2_.stackCount;
            if(!this.var_47.length)
            {
               this.method_258();
               return true;
            }
            if(_loc2_.entID == this.var_1070)
            {
               _loc3_ = this.var_47[this.var_47.length - 1];
               this.var_1070 = _loc3_.entID;
               this.var_1209 = _loc3_.var_342;
            }
         }
         return false;
      }
      
      public function method_534() : void
      {
         var _loc1_:class_141 = null;
         for each(_loc1_ in this.var_47)
         {
            this.var_1.linkUpdater.method_1837(this.var_4,_loc1_.entID,this.type.buffID);
         }
      }
      
      public function method_258() : void
      {
         var _loc1_:class_141 = null;
         var _loc2_:class_141 = null;
         var _loc3_:PowerType = null;
         var _loc4_:ActivePower = null;
         var _loc5_:int = 0;
         var _loc6_:class_141 = null;
         var _loc7_:PowerType = null;
         var _loc8_:PowerType = null;
         if(this.var_4.hudPowers)
         {
            if(this.type.var_611)
            {
               this.var_4.method_993(class_14.powerTypesDict[this.type.var_611]);
            }
            if(this.type.buffName.indexOf("ShadowArmor") == 0)
            {
               this.var_4.method_354(false,true);
            }
         }
         if(this.type.buffName.indexOf("LightningBomb") == 0)
         {
            if(Boolean(this.var_1.clientEnt) && this.var_4.entState == Entity.const_6)
            {
               for each(_loc2_ in this.var_47)
               {
                  if(_loc2_.entID == this.var_1.clientEntID)
                  {
                     _loc3_ = !!_loc2_.var_342 ? class_14.powerTypes[_loc2_.var_342] : null;
                     if(_loc3_)
                     {
                        _loc5_ = _loc3_.var_7;
                        if(this.var_830 >= 3 || this.var_830 >= 2 && _loc5_ < 10 || this.var_830 >= 1 && _loc5_ < 5)
                        {
                           _loc4_ = this.var_1.clientEnt.combatState.method_46(class_14.powerTypesDict["LightningBombExplodeTwo" + _loc3_.var_7],this.var_4,new Point(this.var_4.physPosX,this.var_4.physPosY));
                        }
                        else
                        {
                           _loc4_ = this.var_1.clientEnt.combatState.method_46(class_14.powerTypesDict["LightningBombExplode" + _loc3_.var_7],this.var_4,new Point(this.var_4.physPosX,this.var_4.physPosY));
                        }
                        if(_loc4_)
                        {
                           _loc4_.var_830 = this.var_830 + 1;
                        }
                        break;
                     }
                  }
               }
            }
         }
         if(this.type.buffName.indexOf("Infested") == 0)
         {
            if(Boolean(this.var_1.clientEnt) && this.var_4.entState == Entity.const_6)
            {
               if(this.var_47.length)
               {
                  if((_loc6_ = this.var_47[0]).entID == this.var_1.clientEntID)
                  {
                     if(_loc7_ = !!_loc6_.var_342 ? class_14.powerTypes[_loc6_.var_342] : null)
                     {
                        _loc8_ = class_14.powerTypesDict["InfestationSpawn" + _loc7_.var_7];
                        if(_loc7_.var_7 >= 10 && this.var_4.entType.var_138 >= EntType.const_109)
                        {
                           _loc8_ = class_14.powerTypesDict["InfestationSpawnKing"];
                        }
                        if(_loc8_)
                        {
                           this.var_1.clientEnt.combatState.method_46(_loc8_,this.var_4,new Point(this.var_4.physPosX,this.var_4.physPosY));
                        }
                     }
                  }
               }
            }
         }
         if(Boolean(this.type.var_932) && Boolean(this.var_4.gfx))
         {
            this.var_4.gfx.method_1026();
         }
         if(this.gfxType && this.gfxType.var_927 && Boolean(this.var_4.gfx))
         {
            this.var_4.gfx.method_366(null);
         }
         if(this.var_176 && this.var_176.m_Seq && !this.type.var_1268)
         {
            this.var_176.m_Seq.method_131();
         }
         this.var_176 = null;
         if(this.var_283 && this.var_283.m_Seq && !this.type.var_1268)
         {
            this.var_283.m_Seq.method_131();
         }
         this.var_283 = null;
         for each(_loc1_ in this.var_47)
         {
            _loc1_.method_1687();
         }
         this.var_47 = null;
         this.gfxType = null;
         this.var_1624 = null;
         this.type = null;
         this.var_4 = null;
         this.var_1 = null;
         this.var_1211 = null;
         this.var_1420 = null;
         this.var_2005 = null;
      }
      
      public function method_357(param1:int) : int
      {
         if(!this.var_619)
         {
            return param1;
         }
         if(this.var_590 + param1 > this.var_619)
         {
            this.var_1114 = true;
            return this.var_619 - this.var_590;
         }
         this.var_590 += param1;
         return param1;
      }
      
      public function method_1467() : void
      {
         this.var_1114 = false;
         this.var_590 = 0;
      }
      
      public function method_59(param1:String) : Number
      {
         var _loc3_:int = 0;
         var _loc2_:Number = 0;
         if(this.var_1737)
         {
            _loc3_ = 0;
            while(_loc3_ < this.var_1737.length)
            {
               _loc2_ += this.var_1737[_loc3_].GetValueByProp(this.type.buffName,param1);
               _loc3_++;
            }
         }
         return _loc2_;
      }
   }
}
