package
{
   import flash.geom.Point;
   import flash.utils.Dictionary;
   
   public class ActivePower
   {
       
      
      internal var var_1:Game;
      
      internal var var_4:Entity;
      
      internal var var_188:Boolean = false;
      
      internal var powerType:PowerType = null;
      
      internal var var_33:Entity = null;
      
      internal var targetPos:Point = null;
      
      internal var var_2661:Boolean = false;
      
      internal var var_344:Boolean = false;
      
      internal var var_2064:uint = 0;
      
      internal var var_2521:Boolean = false;
      
      private var var_240:Boolean = false;
      
      internal var var_2314:Boolean = false;
      
      internal var startTime:uint = 0;
      
      internal var var_1145:uint = 0;
      
      internal var var_125:uint = 0;
      
      internal var var_653:uint = 0;
      
      internal var var_713:uint = 0;
      
      internal var meleeCombo:uint = 0;
      
      internal var var_674:uint = 0;
      
      internal var var_743:Boolean = false;
      
      internal var var_294:uint = 0;
      
      internal var var_489:SuperAnimInstance = null;
      
      internal var var_435:SuperAnimInstance = null;
      
      internal var var_54:uint = 0;
      
      internal var var_1865:uint = 0;
      
      internal var var_2865:uint;
      
      internal var var_1851:Dictionary;
      
      internal var var_536:Boolean;
      
      internal var var_803:int;
      
      internal var var_249:uint;
      
      internal var var_2532:uint;
      
      internal var var_1894:Point = null;
      
      internal var var_2948:Boolean = false;
      
      internal var var_157:PowerGroup = null;
      
      internal var var_912:int = 0;
      
      internal var var_830:int = 0;
      
      public function ActivePower(param1:Game, param2:PowerType, param3:Entity, param4:Entity, param5:Point, param6:uint, param7:uint, param8:uint, param9:Boolean, param10:Boolean = false)
      {
         var _loc11_:CombatState = null;
         super();
         this.var_1 = param1;
         this.var_4 = param3;
         this.var_33 = param4;
         this.powerType = param2;
         this.var_294 = param6;
         this.meleeCombo = param7;
         this.var_674 = param8;
         this.var_240 = param9;
         this.var_743 = param3.combatState.var_414 && Boolean(param3.var_20 & Entity.PLAYER);
         this.var_2661 = this.var_33 != null;
         this.var_188 = param3.bFacingLeft();
         this.targetPos = param5;
         this.var_2521 = param10;
         if(this.powerType.var_1789)
         {
            this.var_1851 = new Dictionary();
         }
         this.method_299(param9);
         if(!param2.bIsProjectile && !param2.var_301 && !param2.var_1689 && Boolean(this.var_4.var_20 & Entity.PLAYER))
         {
            if(!(_loc11_ = this.var_4.combatState).var_1937)
            {
               ++this.var_1.level.var_728;
            }
            _loc11_.var_1937 = false;
         }
         if(!param9 && param2.var_1551)
         {
            this.var_157 = new PowerGroup(this.var_1,this,class_14.powerTypesDict[param2.var_1774]);
         }
      }
      
      public function method_129() : void
      {
         if(Boolean(this.var_157) && !this.powerType.var_1551)
         {
            this.var_157.method_1817();
         }
         this.var_157 = null;
         if(Boolean(this.var_489) && Boolean(this.var_489.m_Seq))
         {
            this.var_489.m_Seq.method_131();
         }
         this.var_489 = null;
         if(Boolean(this.var_435) && Boolean(this.var_435.m_Seq))
         {
            this.var_435.m_Seq.method_131();
         }
         this.var_435 = null;
         this.var_1851 = null;
         this.var_4 = null;
         this.powerType = null;
         this.var_33 = null;
         this.targetPos = null;
         this.var_1 = null;
      }
      
      public function method_640() : void
      {
         if(Boolean(this.powerType.var_136) && this.powerType.var_801)
         {
            this.var_4.gfx.m_Seq.method_108();
         }
         this.method_129();
      }
      
      public function method_921() : Array
      {
         var _loc1_:Number = NaN;
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc4_:Number = NaN;
         var _loc10_:Array = null;
         var _loc11_:Entity = null;
         var _loc12_:Array = null;
         var _loc13_:Array = null;
         var _loc14_:class_133 = null;
         var _loc15_:Entity = null;
         var _loc16_:Entity = null;
         var _loc17_:Array = null;
         var _loc18_:Entity = null;
         var _loc19_:Entity = null;
         var _loc20_:Array = null;
         var _loc21_:int = 0;
         var _loc22_:Array = null;
         var _loc23_:Boolean = false;
         var _loc24_:Array = null;
         var _loc25_:Entity = null;
         var _loc26_:Entity = null;
         var _loc27_:Boolean = false;
         var _loc28_:String = null;
         var _loc29_:Array = null;
         var _loc30_:Entity = null;
         var _loc31_:class_133 = null;
         var _loc32_:Entity = null;
         var _loc33_:Array = null;
         var _loc34_:Array = null;
         var _loc35_:Entity = null;
         var _loc36_:Point = null;
         var _loc37_:Point = null;
         var _loc38_:Array = null;
         var _loc39_:Array = null;
         var _loc40_:Entity = null;
         var _loc41_:Entity = null;
         var _loc5_:int = this.var_188 ? int(-this.powerType.var_507) : this.powerType.var_507;
         var _loc6_:uint = this.powerType.damageMultFull < 0 ? Game.FRIEND : Game.ENEMY;
         if(this.powerType.var_1867)
         {
            _loc6_ = uint(Game.FRIEND | Game.ENEMY);
         }
         var _loc7_:int = 0;
         if(this.var_4.var_18)
         {
            _loc7_ = this.var_4.var_18.method_102(this.var_4,this.powerType.basePowerName,"AoERadius");
         }
         if(this.powerType.var_6 == PowerType.TARGETMETHOD_SELF)
         {
            return new Array(this.var_4);
         }
         if(this.powerType.var_6 == PowerType.TARGETMETHOD_RANGED || this.powerType.var_6 == PowerType.TARGETMETHOD_FRIEND)
         {
            return new Array(this.var_33);
         }
         if(this.powerType.var_6 == PowerType.const_304)
         {
            return new Array(this.var_33,this.var_4);
         }
         if(this.powerType.basePowerName == "MoltenFist")
         {
            return this.var_1.GatherEntities(this.var_4,this.targetPos.x,this.targetPos.y + this.powerType.var_127,this.powerType.var_375[this.var_54] + _loc7_,this.powerType.var_375[this.var_54] + _loc7_,_loc6_);
         }
         if(this.powerType.basePowerName == "Harm")
         {
            return this.var_1.GatherEntities(this.var_4,this.targetPos.x,this.targetPos.y,this.powerType.var_375[this.var_54] + _loc7_,this.powerType.aoeRadius + _loc7_,_loc6_);
         }
         if(this.powerType.var_6 == PowerType.TARGETMETHOD_RANGEDAOE)
         {
            return this.var_1.GatherEntities(this.var_4,this.targetPos.x,this.targetPos.y + this.powerType.var_127,this.powerType.aoeRadius + _loc7_,this.powerType.aoeRadius + _loc7_,_loc6_);
         }
         if(this.powerType.var_6 == PowerType.const_275)
         {
            return this.var_1.GatherEntities(this.var_4,this.targetPos.x,this.targetPos.y + this.powerType.var_127,this.powerType.aoeRadius,this.powerType.aoeRadius,_loc6_);
         }
         if(this.powerType.var_6 == PowerType.const_232)
         {
            this.targetPos = this.var_4.combatState.method_139(new Point(this.targetPos.x,this.targetPos.y));
            return this.var_1.GatherEntities(this.var_4,this.targetPos.x,this.targetPos.y + this.powerType.var_127,this.powerType.aoeRadius,-this.powerType.var_127,Game.FRIEND | Game.ENEMY);
         }
         if(this.powerType.var_6 == PowerType.const_99)
         {
            return this.var_1.GatherEntities(this.var_4,this.targetPos.x,this.targetPos.y + this.powerType.var_127,this.powerType.aoeRadius,this.powerType.aoeRadius,_loc6_);
         }
         if(this.powerType.var_6 == PowerType.const_130)
         {
            return this.var_1.GatherEntities(this.var_4,this.var_4.var_10 + _loc5_,this.var_4.var_12 + this.powerType.var_127,this.powerType.aoeRadius + _loc7_,this.powerType.aoeRadius + _loc7_,_loc6_);
         }
         if(this.powerType.var_6 == PowerType.TARGETMETHOD_PBAOE)
         {
            return this.var_1.GatherEntities(this.var_4,this.var_4.var_10 + _loc5_,this.var_4.var_12 + this.powerType.var_127,this.powerType.aoeRadius,this.powerType.aoeRadius,_loc6_);
         }
         if(this.powerType.var_6 == PowerType.const_111)
         {
            return this.var_1.GatherEntities(this.var_4,this.var_4.var_10 + _loc5_,this.var_4.var_12 + this.powerType.var_127,this.powerType.var_375[this.var_54] + _loc7_,this.powerType.aoeRadius + _loc7_,_loc6_);
         }
         if(this.powerType.var_6 == PowerType.const_113)
         {
            return this.var_1.GatherEntities(this.var_4,this.targetPos.x,this.targetPos.y + this.powerType.var_127,this.powerType.aoeRadius,this.powerType.var_375[this.var_54],_loc6_);
         }
         if(this.powerType.var_6 == PowerType.const_32)
         {
            return this.var_1.GatherEntities(this.var_4,this.var_4.var_10,this.var_4.var_12,this.powerType.method_63(this.var_4) + this.powerType.aoeRadius,this.var_4.entType.height * 0.5,_loc6_ | Game.MELEEABLE | Game.INTENTIONAL_MELEE);
         }
         if(this.powerType.var_6 == PowerType.const_248)
         {
            _loc11_ = !!this.var_33 ? this.var_33 : this.var_4;
            return this.var_1.GatherEntities(this.var_4,_loc11_.var_10,_loc11_.var_12,this.powerType.aoeRadius,this.powerType.aoeRadius,_loc6_);
         }
         if(this.powerType.var_6 == PowerType.const_259 || this.powerType.var_6 == PowerType.const_96)
         {
            _loc12_ = new Array();
            _loc13_ = new Array();
            for each(_loc14_ in this.var_1.groupmates)
            {
               if((Boolean(_loc15_ = this.var_1.GetPlayerEntFromEntName(_loc14_.charName))) && _loc15_.currHP > 0)
               {
                  _loc13_.push(_loc15_);
               }
            }
            _loc13_.push(this.var_4);
            if(this.powerType.var_6 == PowerType.const_259)
            {
               _loc11_ = !!this.var_33 ? this.var_33 : this.var_4;
               for each(_loc16_ in _loc13_)
               {
                  _loc1_ = Math.abs(_loc16_.var_10 - _loc11_.var_10);
                  _loc2_ = Math.abs(_loc16_.var_12 - _loc11_.var_12);
                  _loc3_ = _loc16_.entType.width * 0.5 + _loc11_.entType.width * 0.5;
                  _loc4_ = _loc16_.entType.height * 0.5 + _loc11_.entType.height * 0.5;
                  if(_loc1_ <= this.powerType.aoeRadius + _loc7_ + _loc3_ && _loc2_ <= this.powerType.aoeRadius + _loc7_ + _loc4_)
                  {
                     _loc12_.push(_loc16_);
                  }
               }
            }
            else if(this.powerType.var_6 == PowerType.const_96)
            {
               for each(_loc16_ in _loc13_)
               {
                  _loc1_ = Math.abs(_loc16_.var_10 - (this.targetPos.x + this.powerType.var_507));
                  _loc2_ = Math.abs(_loc16_.var_12 - (this.targetPos.y + this.powerType.var_127));
                  _loc3_ = _loc16_.entType.width * 0.5;
                  _loc4_ = _loc16_.entType.height * 0.5;
                  if(_loc1_ <= this.powerType.aoeRadius + _loc7_ + _loc3_ && _loc2_ <= this.powerType.aoeRadius + _loc7_ + _loc4_)
                  {
                     _loc12_.push(_loc16_);
                  }
               }
            }
            return _loc12_;
         }
         var _loc8_:uint = this.powerType.method_63(this.var_4);
         if(this.powerType.var_6 == PowerType.TARGETMETHOD_MELEE || this.powerType.var_6 == PowerType.const_46)
         {
            if(this.powerType.aoeRadius)
            {
               return this.var_1.GatherEntities(this.var_4,this.var_4.var_10 + _loc5_,this.var_4.var_12,_loc8_ + this.powerType.aoeRadius,this.var_4.entType.height * 0.5,_loc6_ | Game.MELEEABLE | Game.INTENTIONAL_MELEE);
            }
            if(this.var_33)
            {
               _loc1_ = Math.abs(this.var_33.var_10 - (this.var_4.var_10 + _loc5_));
               _loc2_ = Math.abs(this.var_33.var_12 - this.var_4.var_12);
               _loc3_ = this.var_33.entType.width * 0.5 + this.var_4.entType.width * 0.5;
               _loc4_ = this.var_33.entType.height * 0.5 + this.var_4.entType.height * 0.5;
               if(_loc1_ <= _loc8_ + _loc3_ && _loc2_ <= _loc4_)
               {
                  return new Array(this.var_33);
               }
            }
            _loc17_ = this.var_1.GatherEntities(this.var_4,this.var_4.var_10 + _loc5_,this.var_4.var_12,_loc8_,this.var_4.entType.height * 0.5,_loc6_ | Game.MELEEABLE | Game.INTENTIONAL_MELEE);
            _loc18_ = null;
            if(this.var_4.var_485)
            {
               for each(_loc19_ in _loc17_)
               {
                  if(_loc19_.id == this.var_4.var_485)
                  {
                     _loc18_ = _loc19_;
                     break;
                  }
               }
            }
            if(!_loc18_)
            {
               _loc18_ = this.method_453(_loc17_);
            }
            return !!_loc18_ ? new Array(_loc18_) : new Array();
         }
         if(this.powerType.var_6 == PowerType.const_89)
         {
            if(_loc20_ = this.var_1.GatherEntities(this.var_4,this.targetPos.x,this.targetPos.y + this.powerType.var_127,this.powerType.aoeRadius + _loc7_,this.powerType.aoeRadius + _loc7_,_loc6_))
            {
               if((_loc21_ = !!this.var_33 ? _loc20_.indexOf(this.var_33) : -1) >= 0)
               {
                  return new Array(this.var_33);
               }
               if(!_loc20_.length)
               {
                  return new Array();
               }
               return new Array(_loc20_[0]);
            }
         }
         if(this.powerType.var_6 == PowerType.TARGETMETHOD_GROUP || this.powerType.var_6 == PowerType.TARGETMETHOD_GROUPANDSELF || this.powerType.var_6 == PowerType.const_424 || this.powerType.var_6 == PowerType.const_517)
         {
            _loc22_ = new Array();
            if(this.powerType.var_6 == PowerType.TARGETMETHOD_GROUPANDSELF)
            {
               _loc22_.push(this.var_4);
            }
            if(this.powerType.var_6 == PowerType.const_424)
            {
               _loc24_ = this.var_1.GatherEntities(this.var_4,this.var_4.var_10,this.var_4.var_12,_loc8_,_loc8_,Game.FRIEND);
               for each(_loc25_ in _loc24_)
               {
                  if(_loc25_ != this.var_4 && _loc25_.var_20 & Entity.MONSTER && _loc25_.team == this.var_4.team)
                  {
                     _loc22_.push(_loc25_);
                  }
               }
            }
            if(this.powerType.var_6 == PowerType.const_517)
            {
               if(_loc26_ = this.var_1.GetEntFromID(this.var_4.summonerId))
               {
                  _loc22_.push(_loc26_);
               }
               else
               {
                  _loc22_.push(this.var_4);
               }
            }
            _loc23_ = Boolean(this.var_4.entType) && this.var_4.entType.var_106 == "Pet";
            if(Boolean(this.var_4.brain) && !_loc23_)
            {
               _loc27_ = Boolean(this.var_4.entType) && this.var_4.entType.var_106 == "Wisp";
               _loc28_ = !!this.var_4.entType ? this.var_4.entType.var_106 : null;
               _loc29_ = this.var_1.GatherEntities(this.var_4,this.var_4.var_10,this.var_4.var_12,_loc8_,_loc8_,Game.FRIEND);
               for each(_loc30_ in _loc29_)
               {
                  if(_loc30_ != this.var_4 && _loc30_.entType && (_loc27_ || _loc30_.entType.var_106 == _loc28_))
                  {
                     _loc22_.push(_loc30_);
                  }
               }
               return _loc22_;
            }
            for each(_loc31_ in this.var_1.groupmates)
            {
               if((Boolean(_loc32_ = this.var_1.GetPlayerEntFromEntName(_loc31_.charName))) && _loc32_.currHP > 0)
               {
                  _loc1_ = Math.abs(_loc32_.var_10 - this.var_4.var_10);
                  _loc2_ = Math.abs(_loc32_.var_12 - this.var_4.var_12);
                  _loc3_ = _loc32_.entType.width * 0.5 + this.var_4.entType.width * 0.5;
                  _loc4_ = _loc32_.entType.height * 0.5 + this.var_4.entType.height * 0.5;
                  if(_loc1_ <= _loc8_ + _loc3_ && _loc2_ <= _loc8_ + _loc4_)
                  {
                     _loc22_.push(_loc32_);
                  }
               }
            }
            return _loc22_;
         }
         if(this.powerType.var_6 == PowerType.const_473)
         {
            if((Boolean(_loc26_ = this.var_1.GetEntFromID(this.var_4.summonerId))) && _loc26_.entState != Entity.const_6)
            {
               return new Array(_loc26_);
            }
            return new Array();
         }
         if(this.powerType.var_6 == PowerType.const_698)
         {
            _loc33_ = new Array();
            _loc34_ = this.var_1.GatherEntities(this.var_4,this.var_4.var_10,this.var_4.var_12,_loc8_,_loc8_,Game.FRIEND);
            for each(_loc35_ in _loc34_)
            {
               if(_loc35_ != this.var_4 && _loc35_.var_20 & Entity.MONSTER && _loc35_.team == this.var_4.team && _loc35_.behaviorType.var_679)
               {
                  _loc33_.push(_loc35_);
               }
            }
            return _loc33_;
         }
         if(this.powerType.var_6 == PowerType.TARGETMETHOD_PIERCING)
         {
            _loc36_ = this.var_4.method_186(class_36.const_747);
            (_loc37_ = class_36.GETTARGETPIERCE_POINT2).x = this.targetPos.x - _loc36_.x;
            _loc37_.y = this.targetPos.y - _loc36_.y;
            _loc37_.normalize(this.powerType.method_63(this.var_4));
            _loc38_ = new Array();
            _loc39_ = this.var_1.GatherEntities(this.var_4,this.var_4.appearPosX,this.var_4.appearPosY,_loc8_ + 100,_loc8_ + 100,_loc6_);
            for each(_loc40_ in _loc39_)
            {
               if(CombatState.method_255(_loc36_,_loc37_,_loc40_))
               {
                  _loc38_.push(_loc40_);
               }
            }
            return _loc38_;
         }
         if(this.powerType.var_6 == PowerType.const_201)
         {
            _loc36_ = this.var_4.method_186(class_36.const_747);
            (_loc37_ = class_36.GETTARGETPIERCE_POINT2).x = this.targetPos.x - _loc36_.x;
            _loc37_.y = this.targetPos.y - _loc36_.y;
            _loc37_.normalize(this.powerType.method_63(this.var_4));
            _loc38_ = new Array();
            _loc39_ = this.var_1.GatherEntities(this.var_4,this.var_4.appearPosX,this.var_4.appearPosY,_loc8_ + 100,_loc8_ + 100,_loc6_);
            for each(_loc40_ in _loc39_)
            {
               if(CombatState.method_255(_loc36_,_loc37_,_loc40_))
               {
                  _loc38_.push(_loc40_);
               }
            }
            return !!(_loc41_ = this.method_453(_loc38_)) ? new Array(_loc41_) : new Array();
         }
         var _loc9_:Entity;
         return !!(_loc9_ = this.method_453(_loc38_)) ? new Array(_loc9_) : new Array();
      }
      
      public function method_453(param1:Array) : Entity
      {
         var _loc4_:Entity = null;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc2_:Number = Number.MAX_VALUE;
         var _loc3_:Entity = null;
         for each(_loc4_ in param1)
         {
            _loc5_ = _loc4_.appearPosX - this.var_4.appearPosX;
            _loc6_ = _loc4_.appearPosY - this.var_4.appearPosY;
            if((_loc7_ = _loc5_ * _loc5_ + _loc6_ * _loc6_) < _loc2_)
            {
               _loc2_ = _loc7_;
               _loc3_ = _loc4_;
            }
         }
         return _loc3_;
      }
      
      public function method_299(param1:Boolean) : void
      {
         this.var_240 = param1;
         this.var_536 = !this.var_240 && !this.powerType.var_275 || this.powerType.var_275 && this.var_240 || Boolean(DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT);
      }
      
      private function method_716() : void
      {
         var _loc1_:int = 0;
         var _loc2_:int = 0;
         var _loc3_:Number = NaN;
         var _loc4_:int = 0;
         var _loc5_:Number = NaN;
         if(this.powerType.var_219)
         {
            _loc1_ = int(this.powerType.manaCost);
            Game.var_172.method_142(this.var_4,this.powerType,-_loc1_,true,this.var_4.var_31);
            this.var_4.var_31 -= _loc1_;
            this.var_1.method_114(this.var_4.var_31);
         }
         else if(!this.powerType.var_749)
         {
            _loc2_ = this.powerType.manaCost * 0.25;
            _loc3_ = 1 + this.var_4.combatState.var_1083 + this.var_4.totalMods.var_1724;
            if((_loc4_ = _loc3_ * this.powerType.manaCost) < _loc2_)
            {
               _loc4_ = _loc2_;
            }
            this.var_4.var_228 -= _loc4_;
            Game.var_172.method_142(this.var_4,this.powerType,-_loc4_,false);
            if(Boolean(this.var_4.combatState.var_1146) && !this.var_4.combatState.var_1298)
            {
               _loc5_ = _loc4_ * this.var_4.combatState.var_1146;
               Game.var_172.method_142(this.var_4,this.powerType,_loc5_,true,this.var_4.var_31);
               this.var_4.var_31 += _loc5_;
               if(this.var_4.var_31 > this.var_4.const_156)
               {
                  this.var_4.var_31 = this.var_4.const_156;
               }
               else if(this.var_4.var_31 < 0)
               {
                  this.var_4.var_31 = 0;
               }
               this.var_1.method_114(this.var_4.var_31);
            }
         }
      }
      
      private function method_750(param1:GfxType, param2:Boolean) : void
      {
         var _loc5_:Entity = null;
         var _loc3_:CombatState = this.var_4.combatState;
         var _loc4_:SuperAnimInstance = new SuperAnimInstance(this.var_1,param1,this.var_4.var_24 != null);
         _loc3_.method_225(this.powerType,_loc4_,this.powerType.var_457,this.var_4,this.targetPos,this.var_54);
         _loc3_.method_512(_loc4_,this.powerType,this.targetPos);
         if(this.var_1894)
         {
            this.var_1894.normalize(1);
            _loc4_.m_TheDO.rotation = MathUtil.method_222(0,this.var_1894,360);
         }
         if(this.powerType.basePowerName == "PermafrostCloneExplode")
         {
            if(_loc5_ = this.var_1.GetEntFromID(this.var_4.summonerId))
            {
               this.var_188 = _loc5_.bFacingLeft();
            }
         }
         if(this.var_188)
         {
            _loc4_.m_TheDO.scaleX = -1;
         }
         if(param2)
         {
            if(!this.powerType.var_1653.bFireAndForget)
            {
               this.var_489 = _loc4_;
            }
            if(this.powerType.var_1427)
            {
               this.var_1.playerEntLayer.addChild(_loc4_.m_TheDO);
            }
            else if(this.powerType.var_2510)
            {
               this.var_1.playerEntLayer.addChildAt(_loc4_.m_TheDO,0);
            }
            else
            {
               this.var_1.playerEntLayer.addChildAt(_loc4_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.var_4.gfx.m_TheDO) + 1);
            }
         }
         else
         {
            if(Boolean(this.powerType.var_1653) && !this.powerType.var_1653.bFireAndForget)
            {
               this.var_435 = _loc4_;
            }
            this.var_1.playerEntLayer.addChildAt(_loc4_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.var_4.gfx.m_TheDO));
         }
         if(this.powerType.var_457 != PowerType.ANIMSOURCE_GROUND && this.powerType.var_457 != PowerType.const_564 && this.powerType.var_457 && this.powerType.basePowerName.indexOf("ShadowBlade") && this.powerType.basePowerName != "Assassinate" && this.powerType.basePowerName != "AssassinateClose" && this.powerType.basePowerName != "MistWalk" && this.powerType.basePowerName != "MistWalkClose" && this.powerType.basePowerName != "FrostArmorIce" && this.powerType.basePowerName != "FrostArmorIceWall" && this.powerType.basePowerName != "VerdictHeal" && this.powerType.basePowerName != "VerdictHealMelee" && this.powerType.basePowerName != "BlackStorm" && this.powerType.basePowerName != "ShadowLegion" && this.powerType.basePowerName != "ShadowArmor")
         {
            _loc3_.var_372.push(_loc4_);
         }
      }
      
      public function method_1507() : void
      {
         var _loc1_:GfxType = null;
         var _loc2_:Number = NaN;
         var _loc3_:* = false;
         if(this.powerType.var_136)
         {
            if(this.powerType.var_136 != "Melee")
            {
               this.var_4.gfx.m_Seq.method_34(Seq.C_USEPOWER,this.powerType.var_136,this.powerType.var_801);
            }
            else if(!this.meleeCombo)
            {
               this.var_4.gfx.m_Seq.method_34(Seq.C_USEPOWER,"Melee",this.powerType.var_801);
            }
            else if(this.meleeCombo == 1)
            {
               this.var_4.gfx.m_Seq.method_34(Seq.C_USEPOWER,"MeleeBack",this.powerType.var_801);
            }
            else if(this.meleeCombo == 2)
            {
               this.var_4.gfx.m_Seq.method_34(Seq.C_USEPOWER,"Melee3",this.powerType.var_801);
            }
            else
            {
               this.var_4.gfx.m_Seq.method_34(Seq.C_USEPOWER,"Melee4",this.powerType.var_801);
            }
         }
         if(this.powerType.var_942)
         {
            _loc1_ = this.powerType.var_942[uint(Math.random() * this.powerType.var_942.length)];
            this.method_750(_loc1_,true);
         }
         if(this.powerType.var_2321)
         {
            this.method_750(this.powerType.var_2321,false);
         }
         if(this.powerType.var_1571)
         {
            this.var_4.velocity.x = this.var_188 ? -this.powerType.var_1571 : this.powerType.var_1571;
         }
         if(this.powerType.basePowerName == "DaggerFlurry")
         {
            if(this.targetPos)
            {
               _loc2_ = this.var_4.physPosX;
               _loc3_ = this.targetPos.x - _loc2_ < 0;
               this.var_4.var_1787 = this.var_1.mTimeThisTick + this.powerType.var_287 + this.powerType.var_125 - 200;
               if(_loc3_ && !this.var_188)
               {
                  this.var_4.velocity.x *= -1;
                  this.var_4.var_687 = true;
               }
               else if(!_loc3_ && this.var_188)
               {
                  this.var_4.velocity.x *= -1;
                  this.var_4.var_687 = false;
               }
            }
         }
         if(this.powerType.basePowerName == "Assassinate")
         {
            this.var_4.gfx.method_880(0.1);
            this.var_4.var_997 = true;
         }
         else if(this.powerType.basePowerName == "MistWalk")
         {
            this.var_4.gfx.method_880(0.5);
            this.var_4.var_997 = true;
         }
         else if(this.powerType.basePowerName == "AssassinateClose" || this.powerType.basePowerName == "MistWalkClose")
         {
            this.var_4.gfx.method_1703();
            this.var_4.var_997 = false;
         }
      }
      
      private function method_573(param1:GfxType, param2:Boolean) : void
      {
         var _loc3_:SuperAnimInstance = null;
         var _loc5_:Entity = null;
         var _loc4_:CombatState = this.var_4.combatState;
         if((!this.powerType.var_2049 || this.var_54 == this.powerType.var_108.length - 1) && (!this.powerType.var_2042 || !this.var_54))
         {
            _loc5_ = this.powerType.var_2511 ? this.var_33 : this.var_4;
            _loc3_ = new SuperAnimInstance(this.var_1,param1,this.var_4.var_24 != null);
            _loc4_.method_225(this.powerType,_loc3_,this.powerType.var_318,_loc5_,this.targetPos,this.var_54);
            _loc4_.method_512(_loc3_,this.powerType,this.targetPos);
            if(this.powerType.var_318 != PowerType.ANIMSOURCE_GROUND && this.powerType.var_318 != PowerType.const_440 && this.powerType.var_318 != PowerType.const_559 && this.powerType.var_318 != PowerType.ANIMSOURCE_TARGETCENTER && this.powerType.var_318 != PowerType.ANIMSOURCE_TARGETFEET && this.powerType.var_318 != PowerType.const_293 && this.powerType.var_318 != PowerType.const_219 && this.powerType.basePowerName != "DryadRush" && this.powerType.basePowerName != "GoblinRush" && this.powerType.basePowerName.indexOf("SkeletonFireNova") && this.powerType.basePowerName.indexOf("SkeletonNova") && this.powerType.basePowerName.indexOf("HumanFireNova") && this.powerType.basePowerName.indexOf("HumanNova") && this.powerType.basePowerName.indexOf("IceNova") && this.powerType.basePowerName.indexOf("IceSpike") && this.powerType.basePowerName.indexOf("FireBlast") && this.powerType.basePowerName.indexOf("Stealth") && this.powerType.basePowerName.indexOf("ShadowBlade") && this.powerType.basePowerName.indexOf("SummonGuard") && this.powerType.basePowerName.indexOf("EnemyFireBlast") && this.powerType.basePowerName.indexOf("HumanFireBlast") && this.powerType.basePowerName.indexOf("DryadFireBlast") && this.powerType.basePowerName.indexOf("GhostBlast") && this.powerType.basePowerName.indexOf("FrostBlast") && this.powerType.basePowerName.indexOf("JuggernautCharge") && this.powerType.basePowerName.indexOf("JuggernautClose") && this.powerType.basePowerName.indexOf("Defiance") && this.powerType.basePowerName.indexOf("Shockwave") && this.powerType.basePowerName != "IridescentBurst" && this.powerType.basePowerName != "RollingSmash" && this.powerType.basePowerName != "DecoyExplode" && this.powerType.basePowerName != "LeapStrike" && this.powerType.basePowerName != "LeapStrikeClose" && this.powerType.basePowerName != "Harm")
            {
               _loc4_.var_372.push(_loc3_);
            }
            if(this.var_188 && this.powerType.basePowerName != "Avalanche")
            {
               _loc3_.m_TheDO.scaleX = -1;
            }
            _loc4_.method_512(_loc3_,this.powerType,this.targetPos);
            if(!param2)
            {
               this.var_1.playerEntLayer.addChildAt(_loc3_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.var_4.gfx.m_TheDO));
            }
            else if(this.powerType.var_1427)
            {
               this.var_1.playerEntLayer.addChild(_loc3_.m_TheDO);
            }
            else
            {
               this.var_1.playerEntLayer.addChildAt(_loc3_.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.var_4.gfx.m_TheDO) + 1);
            }
         }
      }
      
      public function method_872() : void
      {
         var _loc5_:Number = NaN;
         var _loc6_:class_37 = null;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:CollisionManager = null;
         var _loc10_:Point = null;
         var _loc11_:Point = null;
         var _loc12_:Point = null;
         var _loc13_:Number = NaN;
         var _loc14_:Number = NaN;
         var _loc15_:class_37 = null;
         var _loc16_:Number = NaN;
         var _loc17_:Point = null;
         var _loc18_:Boolean = false;
         var _loc19_:class_130 = null;
         var _loc20_:int = 0;
         var _loc21_:int = 0;
         var _loc22_:int = 0;
         var _loc23_:int = 0;
         var _loc24_:int = 0;
         var _loc25_:GfxType = null;
         var _loc26_:int = 0;
         var _loc27_:int = 0;
         var _loc28_:Number = NaN;
         var _loc29_:Vector.<Entity> = null;
         var _loc30_:Entity = null;
         var _loc31_:PowerType = null;
         var _loc32_:PowerType = null;
         var _loc33_:int = 0;
         var _loc34_:Number = NaN;
         var _loc35_:uint = 0;
         var _loc36_:int = 0;
         var _loc37_:int = 0;
         var _loc38_:Seq = null;
         var _loc39_:String = null;
         var _loc40_:String = null;
         if(this.powerType.basePowerName == "LeapStrike" && this.var_54 > 0)
         {
            return;
         }
         if(this.powerType.var_6 == PowerType.const_111 && !this.var_54)
         {
            this.targetPos = new Point(this.var_4.var_10,this.var_4.var_12);
         }
         if(this.powerType.var_6 == PowerType.const_99 && !this.var_54)
         {
            this.targetPos = !!this.var_33 ? new Point(this.var_33.physPosX,this.var_33.physPosY) : new Point(this.var_4.physPosX,this.var_4.physPosY);
         }
         if(this.powerType.var_6 == PowerType.const_568)
         {
            _loc5_ = this.var_188 ? -1000 : 1000;
            if(_loc6_ = this.var_4.currSurface)
            {
               _loc7_ = (_loc6_.endY - _loc6_.startY) / (_loc6_.endX - _loc6_.startX);
               _loc8_ = this.var_4.var_12 + _loc5_ * _loc7_;
               this.targetPos = new Point(this.var_4.var_10 + _loc5_,_loc8_);
            }
            else if(this.var_33)
            {
               this.targetPos = new Point(this.var_33.var_10,this.var_33.var_12);
            }
            else
            {
               this.targetPos = new Point(this.var_4.var_10 + _loc5_,this.var_4.var_12);
            }
         }
         if(this.powerType.basePowerName == "Avalanche" && !this.var_54)
         {
            if(this.var_33)
            {
               if(this.var_33.physPosX < this.var_4.physPosX)
               {
                  this.var_4.bLeftFacing = true;
               }
               else if(this.var_33.physPosX > this.var_4.physPosX)
               {
                  this.var_4.bLeftFacing = false;
               }
            }
            _loc9_ = this.var_1.collMan;
            _loc10_ = new Point();
            _loc11_ = new Point();
            _loc12_ = new Point();
            this.targetPos = new Point(this.var_4.physPosX,this.var_4.physPosY);
            _loc13_ = this.targetPos.x;
            _loc14_ = this.targetPos.y;
            if((_loc16_ = !!(_loc15_ = this.var_4.bFacingLeft() ? _loc9_.getFloorCollision(0,_loc13_ - 1,_loc14_,new Point(-1,0),_loc12_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0) : _loc9_.getFloorCollision(0,_loc13_ + 1,_loc14_,new Point(1,0),_loc12_,null,null,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0)) ? Math.abs(_loc12_.x - _loc13_) : 10000) <= 700)
            {
               this.targetPos.x = _loc12_.x;
               this.targetPos.y = _loc12_.y;
            }
         }
         if(Boolean(this.var_489) && !this.powerType.var_2187)
         {
            this.var_489.m_Seq.method_131();
            this.var_489 = null;
         }
         if(Boolean(this.var_435) && !this.powerType.var_2187)
         {
            this.var_435.m_Seq.method_131();
            this.var_435 = null;
         }
         if(this.powerType.var_136)
         {
            if(this.powerType.var_136 == "Shoot" && !this.powerType.var_287 && Boolean(this.targetPos))
            {
               this.var_4.method_1690(this.targetPos.x,this.targetPos.y);
            }
         }
         if(Boolean(this.powerType.var_2130) && Boolean(this.var_2064))
         {
            this.var_4.gfx.m_Seq.method_34(Seq.C_USEPOWER,this.powerType.var_2130,false);
         }
         if(this.powerType.bIsProjectile)
         {
            if(this.targetPos)
            {
               _loc17_ = this.var_4.method_219(new Point(this.targetPos.x,this.targetPos.y),this.powerType.var_136);
               _loc18_ = this.var_674 > 1 && this.var_674 == this.powerType.var_1212;
               if(this.powerType.basePowerName == "DragonSoulShot")
               {
                  _loc17_ = new Point(this.var_4.appearPosX,this.var_4.appearPosY);
               }
               if(this.powerType.basePowerName == "DaggerFlurry")
               {
                  if(this.var_33)
                  {
                     this.targetPos = new Point(this.var_33.var_10,this.var_33.var_12);
                     _loc17_ = this.var_4.method_219(new Point(this.targetPos.x,this.targetPos.y),this.powerType.var_136);
                  }
                  _loc19_ = new class_130(_loc17_.x + (this.var_54 - 1) * 10,_loc17_.y + (this.var_54 - 1) * 10,this.targetPos.x + (this.var_54 - 1) * 40,this.targetPos.y + (this.var_54 - 1) * 40,this.var_4,this.powerType,this.var_294,_loc18_,this.var_249,this.var_743);
                  ++this.var_294;
                  ++this.var_4.combatState.var_813;
               }
               else if(this.powerType.basePowerName == "PetDragonRed")
               {
                  if(this.var_33)
                  {
                     this.targetPos = new Point(this.var_33.var_10,this.var_33.var_12);
                  }
                  _loc20_ = Math.random() * 150 - 75;
                  _loc19_ = new class_130(_loc17_.x,_loc17_.y,this.targetPos.x,this.targetPos.y + _loc20_,this.var_4,this.powerType,this.var_294,_loc18_,this.var_249,this.var_4.combatState.var_414);
               }
               else if(this.powerType.basePowerName == "DarkChi")
               {
                  if(this.var_33)
                  {
                     this.targetPos = new Point(this.var_33.var_10,this.var_33.var_12);
                  }
                  _loc19_ = new class_130(_loc17_.x,_loc17_.y,this.targetPos.x,this.targetPos.y,this.var_4,this.powerType,this.var_294,_loc18_,this.var_249,this.var_4.combatState.var_414);
               }
               else if(!this.powerType.basePowerName.indexOf("HalloweenLobbed"))
               {
                  if(!(_loc21_ = !!this.powerType.var_1591 ? this.powerType.var_1591[this.var_54] : this.powerType.var_1668))
                  {
                     _loc21_ = class_164.const_506;
                  }
                  if(!(_loc22_ = !!this.powerType.var_1474 ? this.powerType.var_1474[this.var_54] : this.powerType.var_1743))
                  {
                     _loc22_ = class_164.const_506;
                  }
                  _loc19_ = new class_164(_loc17_.x,_loc17_.y,_loc17_.x - 500,_loc17_.y,this.var_4,this.powerType,this.var_294,_loc18_,this.var_249,false,_loc21_,_loc22_);
                  this.var_1.var_371.push(_loc19_);
                  this.var_294 = this.var_4.combatState.var_813++;
                  _loc19_ = new class_164(_loc17_.x,_loc17_.y,_loc17_.x + 500,_loc17_.y,this.var_4,this.powerType,this.var_294,_loc18_,this.var_249,false,_loc21_,_loc22_);
               }
               else if(this.powerType.var_1612 == PowerType.const_872)
               {
                  _loc17_.x = this.var_4.var_10;
                  _loc17_.y = this.var_4.var_12;
                  _loc19_ = new class_165(_loc17_.x,_loc17_.y,this.targetPos.x,this.targetPos.y,this.var_4,this.powerType,this.var_294,_loc18_,this.var_249,this.var_4.combatState.var_414);
               }
               else if(this.powerType.var_1612 == PowerType.const_537)
               {
                  if(!(_loc23_ = !!this.powerType.var_1591 ? this.powerType.var_1591[this.var_54] : this.powerType.var_1668))
                  {
                     _loc23_ = class_164.const_844;
                  }
                  if(!(_loc24_ = !!this.powerType.var_1474 ? this.powerType.var_1474[this.var_54] : this.powerType.var_1743))
                  {
                     _loc24_ = class_164.const_506;
                  }
                  _loc19_ = new class_164(_loc17_.x,_loc17_.y,this.targetPos.x,this.targetPos.y,this.var_4,this.powerType,this.var_294,_loc18_,this.var_249,this.var_4.combatState.var_414,_loc23_,_loc24_);
               }
               else
               {
                  _loc19_ = new class_130(_loc17_.x,_loc17_.y,this.targetPos.x,this.targetPos.y,this.var_4,this.powerType,this.var_294,_loc18_,this.var_249,this.var_4.combatState.var_414);
               }
               this.var_1.var_371.push(_loc19_);
            }
         }
         else
         {
            if(this.powerType.var_352)
            {
               _loc25_ = this.powerType.var_352[uint(Math.random() * this.powerType.var_352.length)];
               this.method_573(_loc25_,true);
            }
            if(this.powerType.var_2204)
            {
               this.method_573(this.powerType.var_2204,false);
            }
            if(Boolean(this.powerType.var_1454) && !this.var_54)
            {
               this.var_1.method_82(this.powerType.var_1454,this.var_4.var_10,this.var_4.var_12);
            }
         }
         var _loc1_:Vector.<int> = this.powerType.var_820;
         if(_loc1_)
         {
            if(this.var_54 < _loc1_.length)
            {
               _loc26_ = _loc1_[this.var_54];
               this.var_4.velocity.x = this.var_188 ? -_loc26_ : _loc26_;
            }
         }
         if(this.powerType.basePowerName == "LeapStrike")
         {
            if(Boolean(this.targetPos) && this.var_54 == 0)
            {
               if((_loc27_ = this.targetPos.x - this.var_4.physPosX) < 0 == this.var_4.bLeft)
               {
                  if((_loc28_ = Math.round((this.targetPos.x - this.var_4.physPosX) / this.powerType.var_108[1] * 1000 / Game.TARGETFPS)) > 40)
                  {
                     _loc28_ = 40;
                  }
                  if(_loc28_ < -40)
                  {
                     _loc28_ = -40;
                  }
                  this.var_4.var_91.x = _loc28_;
                  if(!this.var_4.velocity.y)
                  {
                     this.var_4.var_91.y = -10;
                  }
                  if(_loc28_ < 0)
                  {
                     this.var_4.var_687 = true;
                  }
                  else
                  {
                     this.var_4.var_687 = false;
                  }
               }
            }
         }
         var _loc2_:Boolean = false;
         var _loc3_:Boolean = false;
         var _loc4_:PowerType = this.var_4.var_280;
         if(this.powerType == this.var_4.GetRangedPower() || this.powerType == this.var_4.GetMeleePower())
         {
            _loc2_ = true;
         }
         else if(this.var_33 && this.var_33 != this.var_4 && this.powerType.damageMultFull > 0)
         {
            _loc3_ = true;
            _loc2_ = true;
         }
         if(_loc2_)
         {
            if((Boolean(_loc29_ = this.var_1.GetSummonedCreatures(this.var_4.id,class_14.powerTypesDict["SummonDragonSoul"]))) && _loc29_.length > 0)
            {
               _loc33_ = 1;
               if(_loc32_ = (_loc30_ = _loc29_[0]).var_99)
               {
                  _loc33_ = _loc32_.var_7;
               }
               _loc31_ = class_14.powerTypesDict["DragonSoulShot" + _loc33_];
               if(Boolean(_loc30_.brain) && _loc30_.brain.var_2750 <= this.var_1.mTimeThisTick)
               {
                  this.var_294 = this.powerType.bIsProjectile ? this.var_4.combatState.var_813++ : 0;
                  _loc18_ = this.var_674 > 1 && this.powerType == _loc4_ && this.var_674 == _loc4_.var_1212;
                  _loc30_.combatState.method_749(_loc31_);
                  _loc34_ = this.var_4.var_412 + this.var_4.combatState.var_840;
                  _loc35_ = _loc4_.var_125;
                  if(_loc34_)
                  {
                     _loc36_ = int(_loc4_.var_287 + _loc4_.var_125);
                     _loc35_ = uint(_loc37_ = Math.round(_loc36_ / (1 + _loc34_)));
                  }
                  if(_loc3_)
                  {
                     _loc30_.combatState.method_51(_loc31_,true,0,new Point(this.var_33.var_10,this.var_33.var_12));
                  }
                  else
                  {
                     _loc30_.combatState.method_51(_loc31_,true,0,this.targetPos);
                  }
                  _loc30_.brain.var_2750 = this.var_1.mTimeThisTick + _loc35_;
               }
            }
         }
         if(this.powerType.basePowerName == "FlamethrowerROR")
         {
            _loc39_ = !!(_loc38_ = this.var_4.gfx.m_Seq).var_30 ? _loc38_.var_30.var_1802 : null;
            _loc40_ = this.var_4.bRunning && !this.var_4.bJumping ? "BlastRun" : "Blast4";
            if(_loc39_ != _loc40_)
            {
               _loc38_.method_34(Seq.C_USEPOWER,_loc40_,true);
            }
         }
      }
      
      private function method_801() : void
      {
         var _loc1_:PowerType = null;
         if(this.powerType.var_801)
         {
            _loc1_ = !!this.powerType.var_543 ? class_14.powerTypesDict[this.powerType.var_543] : null;
            if(!_loc1_ || !_loc1_.var_136)
            {
               this.var_4.gfx.m_Seq.method_108();
            }
         }
         if(this.var_489)
         {
            this.var_489.m_Seq.method_131();
            this.var_489 = null;
         }
         if(this.var_435)
         {
            this.var_435.m_Seq.method_131();
            this.var_435 = null;
         }
      }
      
      public function method_243() : Boolean
      {
         var _loc2_:Array = null;
         var _loc3_:Boolean = false;
         var _loc4_:Entity = null;
         var _loc5_:Number = NaN;
         var _loc6_:int = 0;
         var _loc7_:int = 0;
         var _loc8_:Packet = null;
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc11_:class_43 = null;
         var _loc12_:String = null;
         var _loc13_:CombatState = null;
         var _loc14_:Array = null;
         var _loc15_:uint = 0;
         var _loc16_:PowerType = null;
         var _loc17_:Packet = null;
         var _loc18_:Entity = null;
         var _loc19_:int = 0;
         var _loc20_:Point = null;
         var _loc21_:ActivePower = null;
         var _loc22_:int = 0;
         var _loc23_:PowerType = null;
         var _loc24_:uint = 0;
         var _loc25_:uint = 0;
         var _loc26_:uint = 0;
         var _loc27_:Array = null;
         var _loc28_:String = null;
         var _loc29_:PowerType = null;
         var _loc30_:* = false;
         var _loc1_:uint = this.var_1.mTimeThisTick;
         if(this.var_2948)
         {
            return false;
         }
         if(this.var_4 && this.var_4.entState == Entity.const_6 && this.powerType.var_2943)
         {
            return false;
         }
         if(Boolean(this.var_33) && !this.var_33.bIAmValid)
         {
            return false;
         }
         if(_loc1_ < this.var_2532)
         {
            return true;
         }
         if(!this.var_4.bFiring && this.powerType.var_2690)
         {
            if(!(this.powerType.basePowerName == "FlamethrowerROR" && this.var_240))
            {
               this.var_4.gfx.m_Seq.method_108();
               return false;
            }
            if(this.var_4.combatState.var_2122)
            {
               this.var_4.combatState.var_2122 = false;
               this.var_4.gfx.m_Seq.method_108();
               return false;
            }
         }
         if(this.powerType.var_6 == PowerType.const_304)
         {
            _loc2_ = this.method_921();
            _loc3_ = false;
            for each(_loc4_ in _loc2_)
            {
               if(_loc4_ && _loc4_.entType != this.var_4.entType)
               {
                  _loc3_ = true;
               }
            }
            if(!_loc3_)
            {
               return false;
            }
            if(this.var_4.bFiring)
            {
               return false;
            }
            if(this.var_4.bJumping)
            {
               return false;
            }
            if(this.var_4.bDropping)
            {
               return false;
            }
            if(this.var_4.bRunning)
            {
               return false;
            }
            if(this.var_4.currSurface == null)
            {
               return false;
            }
            if(this.var_4.var_1875)
            {
               return false;
            }
         }
         if(!this.startTime)
         {
            Game.var_172.method_499(this.var_4,this.powerType);
            this.startTime = _loc1_;
            this.var_54 = 0;
            this.var_1145 = this.startTime + this.powerType.var_108[this.var_54];
            this.var_125 = this.startTime + this.powerType.var_287 + this.powerType.var_125;
            _loc5_ = this.var_4.var_412 + this.var_4.combatState.var_840;
            if((this.powerType == this.var_4.var_280 || this.powerType == this.var_4.var_353) && Boolean(_loc5_))
            {
               _loc6_ = int(this.powerType.var_287 + this.powerType.var_125);
               _loc7_ = Math.round(_loc6_ / (1 + _loc5_));
               this.var_125 = this.startTime + _loc7_;
            }
            this.var_653 = !!this.powerType.var_653 ? this.startTime + this.powerType.var_653 : 0;
            this.var_713 = !!this.powerType.var_713 ? this.startTime + this.powerType.var_713 : 0;
            this.method_1507();
            if(this.var_4.behaviorType.var_1023)
            {
               this.var_4.var_822 = false;
            }
            if(!this.var_240)
            {
               if(this.powerType.var_219)
               {
                  if(this.powerType.manaCost)
                  {
                     _loc8_ = new Packet(LinkUpdater.const_1300);
                     _loc9_ = this.var_4.var_31;
                     _loc8_.method_20(PowerType.const_423,_loc9_);
                     this.var_1.serverConn.SendPacket(_loc8_);
                  }
               }
               this.method_716();
               if(!this.var_2314)
               {
                  this.var_1.linkUpdater.method_1353(this);
               }
            }
         }
         if(this.var_1865 < this.powerType.var_1169.length)
         {
            _loc10_ = uint(_loc1_ - this.startTime);
            _loc11_ = this.powerType.var_1169[this.var_1865];
            if(_loc10_ >= _loc11_.var_2732)
            {
               _loc12_ = Boolean(_loc11_.var_2331) && this.var_4.entType.var_620 ? _loc11_.var_2331 : _loc11_.soundName;
               this.var_1.method_82(_loc12_,this.var_4.var_10,this.var_4.var_12);
               ++this.var_1865;
            }
         }
         if(Boolean(this.var_713) && _loc1_ > this.var_713)
         {
            if(this.var_4.var_24)
            {
               this.var_4.var_24.var_418.method_237("Slam");
            }
            this.var_713 = 0;
         }
         if(this.powerType.basePowerName == "FlamethrowerROR")
         {
            this.var_188 = this.var_4.bFacingLeft();
         }
         if(!this.var_344 && _loc1_ >= this.var_1145)
         {
            this.method_872();
            this.var_344 = true;
            ++this.var_2064;
            _loc13_ = this.var_4.combatState;
            if(!this.powerType.bIsProjectile && this.var_536)
            {
               _loc14_ = this.method_921();
               if(this.powerType.basePowerName == "FlamethrowerROR")
               {
                  if(this.var_4.var_31 < this.powerType.manaCost)
                  {
                     this.var_4.gfx.m_Seq.method_108();
                     return false;
                  }
                  this.method_716();
               }
               if(this.powerType.basePowerName == "FlamethrowerClose")
               {
                  _loc16_ = class_14.powerTypesDict["FlamethrowerROR"];
                  (_loc17_ = new Packet(LinkUpdater.const_694)).method_9(this.var_4.id);
                  _loc17_.method_9(_loc16_.powerID);
                  this.var_1.serverConn.SendPacket(_loc17_);
                  if(this.powerType.var_7 < 5)
                  {
                     this.var_4.combatState.RemoveBuff(class_14.buffTypesDict["FlamethrowerRank1"]);
                  }
                  else if(this.powerType.var_7 < 9)
                  {
                     this.var_4.combatState.RemoveBuff(class_14.buffTypesDict["FlamethrowerRank5"]);
                  }
                  else
                  {
                     this.var_4.combatState.RemoveBuff(class_14.buffTypesDict["FlamethrowerRank9"]);
                  }
                  this.var_4.combatState.RemoveBuff(class_14.buffTypesDict["FlamethrowerROR" + this.powerType.var_7]);
               }
               if(this.powerType.basePowerName == "DetShieldDetonate")
               {
                  this.var_4.combatState.RemoveBuff(class_14.buffTypesDict["DetShield" + this.powerType.var_7]);
               }
               if(this.powerType.powerName.indexOf("LightningBombExplode") == 0 && Boolean(this.var_33))
               {
                  switch(this.var_33.entType.var_138)
                  {
                     case EntType.const_102:
                        this.var_803 = this.var_4.magicDamage * 1;
                        break;
                     case EntType.const_109:
                        this.var_803 = this.var_4.magicDamage * 1.5;
                        break;
                     case EntType.const_123:
                        this.var_803 = this.var_4.magicDamage * 2;
                        break;
                     case EntType.const_92:
                        this.var_803 = this.var_4.magicDamage * 2.5;
                  }
                  this.var_803 *= this.powerType.damageMultFull;
               }
               _loc15_ = _loc13_.FireThisPower(this.powerType,this.targetPos,_loc14_,this.var_743,this.var_54,false,this.var_2865,this.var_1851,this.var_803,this.var_249,this.var_157,this.var_830);
               if(this.powerType.var_2486)
               {
                  this.var_2865 = _loc15_;
               }
               if(this.powerType.var_1789)
               {
                  for each(_loc18_ in _loc14_)
                  {
                     this.var_1851[_loc18_.id] = true;
                  }
               }
               if(this.powerType.basePowerName == "SeekingBlades")
               {
                  this.var_4.method_391(true,this.var_240);
               }
               else if(this.powerType.basePowerName == "EndSeekingBlades")
               {
                  this.var_4.method_391(false,this.var_240);
               }
               if(this.powerType.basePowerName == "ShadowArmor")
               {
                  this.var_4.method_354(true,this.var_240,this.powerType.var_7);
                  if(this.var_4.combatState.var_1311)
                  {
                     _loc19_ = this.var_4.combatState.var_1311 * this.var_4.magicDamage;
                     this.var_4.combatState.method_72(class_14.powerTypesDict["ProcAlwaysFullHeal"],this.var_4,new Point(this.var_4.physPosX,this.var_4.physPosY),_loc19_,this.powerType.powerID);
                  }
                  if(this.powerType.var_7 >= 10)
                  {
                     this.var_4.combatState.method_304();
                  }
               }
               if(this.powerType.basePowerName == "Pyromania")
               {
                  this.var_4.method_475(true,this.var_240,this.powerType.var_7);
               }
               else if(this.powerType.basePowerName == "EndPyromania")
               {
                  this.var_4.method_475(false,this.var_240);
               }
               if(this.powerType.basePowerName == "SecondWind")
               {
                  this.var_4.combatState.method_304();
               }
               if(this.powerType.basePowerName == "FlameStrike")
               {
                  _loc20_ = this.var_4.combatState.method_139(new Point(this.var_4.var_10,this.var_4.var_12));
                  _loc21_ = this.var_4.combatState.method_46(class_14.powerTypesDict["FireFieldTrail" + this.powerType.var_7],null,_loc20_);
                  if(this.powerType.var_1551 && Boolean(this.var_157))
                  {
                     this.var_157.method_587(_loc21_);
                  }
               }
               if(this.powerType.basePowerName == "ShadowTendrilDash")
               {
                  _loc20_ = this.var_4.combatState.method_139(new Point(this.var_4.var_10,this.var_4.var_12));
                  _loc21_ = this.var_4.combatState.method_46(class_14.powerTypesDict["ShadowTendril" + this.powerType.var_7],null,_loc20_);
                  if(this.powerType.var_1551 && Boolean(this.var_157))
                  {
                     this.var_157.method_587(_loc21_);
                  }
               }
               if(this.powerType.basePowerName == "SentinelForm")
               {
                  if(this.var_4.combatState.var_1669)
                  {
                     this.var_4.combatState.RemoveBuff(class_14.buffTypesDict["SigilSentinelArmor"]);
                  }
                  this.var_4.method_247(true,this.var_240,this.powerType.var_7);
               }
               else if(this.powerType.basePowerName == "EndSentinelForm")
               {
                  this.var_4.method_247(false,this.var_240);
               }
               else if(this.powerType.basePowerName == "EndFrostArmor")
               {
                  this.var_4.method_262(false,this.var_240);
               }
            }
            if(this.var_4.behaviorType.var_2200)
            {
               this.var_4.var_822 = false;
            }
            if(this.var_240)
            {
               if(this.var_54 < this.powerType.var_108.length - 1)
               {
                  this.var_1145 += this.powerType.var_108[++this.var_54];
                  this.var_344 = false;
               }
               else
               {
                  this.method_801();
               }
            }
            else
            {
               if(this.var_4.debugPowerGfx)
               {
                  this.powerType.DrawDebugRange(this.var_4.debugPowerGfx,this.var_4,this.targetPos,this.var_54,this.var_33);
               }
               if(_loc13_.var_414 && Boolean(this.powerType.damageMultFull))
               {
                  if(_loc13_.var_576)
                  {
                     _loc13_.RemoveBuff(class_14.buffTypesDict["ShadowArmor" + _loc13_.var_576]);
                  }
               }
               if(this.powerType.powerName == "Dismount")
               {
                  _loc13_.method_841();
               }
               if(this.powerType == PowerType.var_836)
               {
                  this.var_4.method_343();
               }
               if(this.var_54 < this.powerType.var_108.length - 1)
               {
                  this.var_1145 += this.powerType.var_108[++this.var_54];
                  this.var_344 = false;
                  if(Boolean(this.var_33) && this.var_33.entState == Entity.const_6)
                  {
                     this.var_33 = null;
                  }
               }
               else
               {
                  _loc5_ = this.var_4.var_412 + this.var_4.combatState.var_840;
                  _loc22_ = (this.powerType.var_125 + this.powerType.var_287) * 2;
                  if(_loc5_)
                  {
                     _loc22_ = Math.round(_loc22_ / (1 + _loc5_));
                  }
                  if(this.powerType.var_136 == "Melee" && this.meleeCombo > 1 && this.meleeCombo == this.powerType.var_1075)
                  {
                     _loc13_.var_114[this.powerType.powerID] += _loc22_;
                  }
                  if(this.powerType.var_136 == "Shoot" && this.var_674 > 1 && this.var_674 == this.powerType.var_1212)
                  {
                     _loc13_.var_114[this.powerType.powerID] += _loc22_;
                  }
                  if(this.powerType == this.var_4.GetMeleePower())
                  {
                     if((Boolean(_loc23_ = this.var_4.GetRangedPower())) && this.powerType != _loc23_)
                     {
                        _loc25_ = _loc24_ = 800;
                        if(_loc5_)
                        {
                           _loc25_ = Math.round(_loc24_ / (1 + _loc5_));
                        }
                        _loc13_.method_433(_loc23_,_loc25_);
                     }
                  }
                  if(this.powerType.var_2674)
                  {
                     _loc26_ = uint(_loc1_ - this.startTime);
                     _loc27_ = this.var_4.entType.var_1200;
                     for each(_loc28_ in _loc27_)
                     {
                        if((_loc29_ = class_14.powerTypesDict[_loc28_]) != this.powerType && _loc29_.coolDownTime > _loc26_)
                        {
                           _loc13_.method_433(_loc29_,_loc29_.coolDownTime - _loc26_);
                        }
                     }
                  }
                  if(this.powerType.var_2475)
                  {
                     this.var_4.TakeDamage(this.var_4.currHP * 10,true);
                  }
                  if(this.powerType.var_2793)
                  {
                     this.var_4.var_1459 = 0;
                  }
                  this.method_801();
                  if(this.powerType.basePowerName == "PermafrostClone")
                  {
                     this.var_4.combatState.RemoveBuff(class_14.buffTypesDict["Blink"]);
                  }
                  if(this.powerType.basePowerName == "FlameStrike")
                  {
                     if(this.powerType.var_7 >= 8)
                     {
                        this.var_4.combatState.RemoveBuff(class_14.buffTypesDict["FireArmor"]);
                     }
                     else
                     {
                        this.var_4.combatState.RemoveBuff(class_14.buffTypesDict["FireArmor30"]);
                     }
                  }
                  if(this.powerType.basePowerName == "HailstoneEmbrace")
                  {
                     this.var_4.method_262(true,this.var_240,this.powerType.var_7);
                  }
               }
            }
         }
         if(this.powerType.var_6 == PowerType.const_32)
         {
            _loc30_ = this.var_4.physPosX < this.targetPos.x;
            if(this.powerType.basePowerName == "MistWalk")
            {
               if(this.var_33)
               {
                  if(this.var_188 && this.var_4.var_10 < this.var_33.var_10 - (this.var_4.entType.width >> 1) - (this.var_33.entType.width >> 1) - 35)
                  {
                     this.var_125 = 0;
                     this.var_344 = true;
                  }
                  else if(!this.var_188 && this.var_4.var_10 > this.var_33.var_10 + (this.var_33.entType.width >> 1) + (this.var_4.entType.width >> 1) + 35)
                  {
                     this.var_125 = 0;
                     this.var_344 = true;
                  }
               }
               else if(this.var_188 && this.var_4.physPosX - this.var_4.var_2247 < this.targetPos.x)
               {
                  this.var_125 = 0;
                  this.var_344 = true;
               }
               else if(!this.var_188 && this.var_4.physPosX > this.targetPos.x + this.var_4.var_2247)
               {
                  this.var_125 = 0;
                  this.var_344 = true;
               }
            }
            else if(_loc30_ && this.var_188 || !_loc30_ && !this.var_188)
            {
               this.var_125 = 0;
               this.var_344 = true;
            }
         }
         if(this.powerType.basePowerName == "LeapStrike" && ((_loc1_ - this.startTime > 1165 || this.targetPos && _loc1_ - this.startTime > 1000 && Math.abs(this.targetPos.x - this.var_4.physPosX) < 50) && this.var_4.currSurface))
         {
            this.var_125 = 0;
            this.var_344 = true;
         }
         if(this.var_344 && _loc1_ >= this.var_125)
         {
            if(!this.var_4.var_38 && Boolean(this.powerType.var_93))
            {
               this.var_4.combatState.RemoveBuff(class_14.buffTypesDict[this.powerType.var_93]);
            }
            if(this.powerType.basePowerName == "LeapStrike")
            {
               this.var_4.var_91.y = 0;
               this.var_4.var_91.x = 0;
            }
            if(this.powerType.var_6 == PowerType.const_32)
            {
               this.var_4.velocity.x = 0;
            }
            if(this.powerType.basePowerName == "LeapStrikeClose")
            {
               this.var_4.gfx.m_Seq.var_735 = false;
            }
            if(this.var_4.combatState.var_1093 && this.powerType.var_219 && this.powerType.manaCost >= 15)
            {
               this.var_4.combatState.var_2566 = _loc1_ + 3000;
            }
            if(this.powerType.var_2553)
            {
               this.var_4.var_1878 = this.var_1.mTimeThisTick;
            }
            if(this.powerType.var_2616)
            {
               this.var_4.var_822 = true;
            }
            return false;
         }
         return true;
      }
   }
}
