package
{
   import flash.display.Sprite;
   import flash.geom.Point;
   
   public class class_130
   {
      
      internal static const FUDGEFACTOR:Number = 0.00001;
      
      private static const const_883:Number = 20;
      
      private static const const_1265:uint = 2000;
       
      
      internal var var_2712:Number;
      
      internal var var_11:Point;
      
      internal var var_559:Number = 0;
      
      internal var var_638:Point;
      
      internal var velocity:Point;
      
      internal var var_502:Point;
      
      internal var var_1:Game;
      
      internal var gfx:SuperAnimInstance = null;
      
      internal var var_378:Boolean;
      
      internal var var_1456:Number;
      
      internal var var_19:Entity;
      
      internal var var_1718:Number = 0;
      
      internal var var_1858:Number = 0;
      
      internal var remoteMissileID:uint = 0;
      
      internal var localMissileID:uint = 0;
      
      internal var power:PowerType;
      
      internal var var_1448:Boolean;
      
      internal var var_536:Boolean;
      
      internal var var_249:uint;
      
      internal var var_743:Boolean;
      
      internal var var_2413:uint = 0;
      
      public function class_130(param1:Number, param2:Number, param3:Number, param4:Number, param5:Entity, param6:PowerType, param7:uint, param8:Boolean, param9:uint = 0, param10:Boolean = false)
      {
         super();
         this.var_19 = param5;
         this.var_1 = this.var_19.var_1;
         this.power = param6;
         this.var_1448 = param8;
         this.var_502 = new Point(param1,param2);
         this.var_11 = new Point(this.var_502.x,this.var_502.y);
         this.var_638 = new Point(param3,param4);
         this.var_2712 = const_883;
         this.var_2413 = const_1265;
         this.var_249 = param9;
         this.var_743 = param10;
         this.gfx = new SuperAnimInstance(this.var_1,this.var_1448 ? this.power.var_1418 : this.power.var_625,this.var_19.var_24 != null);
         this.gfx.m_TheDO.x = this.var_11.x;
         this.gfx.m_TheDO.y = this.var_11.y;
         if(param6.powerName == "NephitRanged")
         {
            this.var_1.playerEntLayer.addChild(this.gfx.m_TheDO);
         }
         else
         {
            this.var_1.playerEntLayer.addChildAt(this.gfx.m_TheDO,this.var_1.playerEntLayer.getChildIndex(this.var_19.gfx.m_TheDO));
         }
         if(this.power.var_2347)
         {
            this.var_1.method_82(this.power.var_2347,this.var_502.x,this.var_502.y);
         }
         this.velocity = this.var_638.subtract(this.var_502);
         this.var_1858 = this.velocity.length - FUDGEFACTOR;
         this.var_378 = false;
         this.var_1456 = this.var_1.mTimeThisTick;
         if(this.var_19.var_20 & Entity.LOCAL)
         {
            this.localMissileID = param7;
         }
         else
         {
            this.remoteMissileID = param7;
         }
         this.var_536 = !this.remoteMissileID && !param6.var_275 || param6.var_275 && this.remoteMissileID || Boolean(DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT);
      }
      
      public function method_770() : void
      {
         this.var_11 = null;
         this.var_638 = null;
         this.velocity = null;
         this.var_502 = null;
         if(this.gfx)
         {
            this.gfx.DestroySuperAnimInstance();
            this.gfx = null;
         }
         this.var_19 = null;
         this.power = null;
         this.var_1 = null;
      }
      
      public function method_106(param1:int, param2:int, param3:Point, param4:Boolean) : void
      {
         var _loc5_:GfxType = null;
         var _loc6_:SuperAnimInstance = null;
         var _loc7_:PowerType = null;
         if(!param3)
         {
            param3 = new Point(this.velocity.x,this.velocity.y);
            param3.normalize(1);
         }
         if(Boolean(this.var_19.var_20 & Entity.PLAYER) && !this.power.var_1689)
         {
            if(param4)
            {
               ++this.var_1.level.var_1096;
            }
            ++this.var_1.level.var_728;
         }
         if(this.gfx)
         {
            this.gfx.DestroySuperAnimInstance();
            this.gfx = null;
         }
         if(this.power.var_1454)
         {
            this.var_1.method_82(this.power.var_1454,param1,param2);
         }
         if(this.power.var_352)
         {
            _loc5_ = this.power.var_352[uint(Math.random() * this.power.var_352.length)];
            (_loc6_ = new SuperAnimInstance(this.var_1,_loc5_,this.var_19.var_24 != null)).m_TheDO.x = param1;
            _loc6_.m_TheDO.y = param2;
            _loc6_.m_TheDO.rotation = MathUtil.method_222(this.var_559,param3,360);
            this.var_1.playerEntLayer.addChild(_loc6_.m_TheDO);
         }
         if(this.power.basePowerName == "VerdictROR" && this.var_19 == this.var_1.clientEnt)
         {
            if(_loc7_ = class_14.powerTypesDict["VerdictHeal" + this.power.var_7])
            {
               this.var_19.combatState.method_46(_loc7_,null,new Point(param1,param2));
            }
         }
         this.var_1718 = this.var_1.mTimeThisTick;
      }
      
      public function TickMissile() : Boolean
      {
         var _loc9_:Entity = null;
         var _loc10_:Number = NaN;
         var _loc11_:Array = null;
         var _loc12_:Boolean = false;
         var _loc13_:Entity = null;
         var _loc14_:Number = NaN;
         var _loc15_:Number = NaN;
         var _loc16_:class_37 = null;
         var _loc17_:class_37 = null;
         var _loc18_:Array = null;
         var _loc19_:uint = 0;
         var _loc20_:* = false;
         var _loc21_:Point = null;
         var _loc22_:ActivePower = null;
         var _loc23_:int = 0;
         var _loc1_:Boolean = false;
         var _loc2_:class_37 = null;
         var _loc3_:Point = new Point(0,-1);
         if(this.var_1718 > 0)
         {
            return false;
         }
         if(!this.var_19.bIAmValid)
         {
            this.method_106(this.var_11.x,this.var_11.y,null,false);
            return false;
         }
         var _loc4_:Point;
         (_loc4_ = new Point(this.velocity.x,this.velocity.y)).normalize(this.var_1.TIMESTEP * this.var_2712);
         var _loc5_:Point = new Point(this.var_11.x + _loc4_.x,this.var_11.y + _loc4_.y);
         if(this.var_536)
         {
            _loc9_ = null;
            _loc10_ = Camera.SCREEN_WIDTH * 0.5;
            _loc11_ = this.var_1.GatherEntities(this.var_19,this.var_11.x,this.var_11.y,_loc10_,_loc10_,this.power.damageMultFull < 0 ? Game.FRIEND : Game.ENEMY);
            _loc12_ = PowerType.method_432(this.power,this.var_19);
            for each(_loc13_ in _loc11_)
            {
               if(_loc13_ != this.var_19)
               {
                  if(!(!_loc13_.method_156() || _loc13_.behaviorType.var_1225 || _loc13_.behaviorType.var_1723))
                  {
                     if(!(_loc13_.behaviorType.var_1094 && !_loc12_))
                     {
                        if(CombatState.method_255(this.var_11,_loc4_,_loc13_))
                        {
                           _loc9_ = _loc13_;
                           _loc1_ = true;
                           _loc5_.x = this.var_11.x * 0.3 + _loc13_.appearPosX * 0.7;
                           _loc5_.y = this.var_11.y;
                           break;
                        }
                     }
                  }
               }
            }
            if(!_loc1_)
            {
               if(_loc16_ = this.var_1.collMan.getFloorCollision(0,this.var_11.x,this.var_11.y,_loc4_,_loc5_,null,_loc3_,null,CollisionManager.HARD_FLOOR,0))
               {
                  _loc2_ = _loc16_;
               }
               if(_loc2_)
               {
                  _loc1_ = true;
               }
            }
            _loc14_ = this.var_11.x;
            _loc15_ = this.var_11.y;
            if(!this.var_378 && !_loc1_ && Point.distance(this.var_11.add(_loc4_),this.var_502) > this.var_1858)
            {
               this.var_378 = true;
               _loc14_ = this.var_638.x;
               _loc15_ = this.var_638.y;
            }
            if(this.var_378)
            {
               if(_loc17_ = this.var_1.collMan.getFloorCollision(0,_loc14_,_loc15_,_loc4_,_loc5_,null,_loc3_,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0))
               {
                  _loc2_ = _loc17_;
               }
               if(_loc2_)
               {
                  _loc1_ = true;
               }
            }
         }
         this.var_11.x = _loc5_.x;
         this.var_11.y = _loc5_.y;
         _loc4_.normalize(1);
         var _loc6_:Number = 1;
         var _loc7_:Number;
         if((_loc7_ = MathUtil.method_222(this.var_559,_loc4_,360)) >= 180)
         {
            _loc7_ -= 180;
            _loc6_ = -1;
         }
         var _loc8_:Sprite;
         (_loc8_ = this.gfx.m_TheDO).x = this.var_11.x;
         _loc8_.y = this.var_11.y;
         _loc8_.rotation = _loc7_;
         _loc8_.scaleY = _loc6_;
         if(this.var_536)
         {
            if(_loc1_ || this.var_1.mTimeThisTick - this.var_1456 > this.var_2413)
            {
               if(this.power.aoeRadius)
               {
                  _loc18_ = this.var_1.GatherEntities(this.var_19,this.var_11.x,this.var_11.y,this.power.aoeRadius,this.power.aoeRadius,this.power.damageMultFull < 0 ? Game.FRIEND : Game.ENEMY);
               }
               else if(_loc9_)
               {
                  _loc18_ = new Array(_loc9_);
               }
               else
               {
                  _loc18_ = new Array();
               }
               _loc20_ = (_loc19_ = this.var_19.combatState.FireThisPower(this.power,this.var_11,_loc18_,this.var_743,0,this.var_1448,0,null,0,this.var_249)) > 0;
               this.method_106(this.var_11.x,this.var_11.y,!!_loc2_ ? new Point(-_loc3_.x,-_loc3_.y) : _loc4_,_loc20_);
               if(this.localMissileID)
               {
                  this.var_1.linkUpdater.WriteProjectileExplode(this.var_19,this.localMissileID,this.var_11.x,this.var_11.y,_loc20_);
               }
               if(this.var_19.debugPowerGfx)
               {
                  this.power.DrawDebugRange(this.var_19.debugPowerGfx,this.var_19,this.var_11,0);
               }
               if(Boolean(_loc2_) && this.power.powerName.indexOf("FrostArmorRanged") == 0)
               {
                  (_loc21_ = new Point(_loc3_.x,_loc3_.y)).normalize(1);
                  if(_loc4_.y < 0)
                  {
                     _loc21_.y = Math.abs(_loc21_.y);
                  }
                  else
                  {
                     _loc21_.y = -1 * Math.abs(_loc21_.y);
                  }
                  if(_loc4_.x < 0)
                  {
                     _loc21_.x = Math.abs(_loc21_.x);
                  }
                  else
                  {
                     _loc21_.x = -1 * Math.abs(_loc21_.x);
                  }
                  _loc23_ = 1;
                  if(this.power.var_7 >= 10)
                  {
                     _loc23_ = 10;
                  }
                  else if(this.power.var_7 >= 7)
                  {
                     _loc23_ = 7;
                  }
                  else if(this.power.var_7 >= 5)
                  {
                     _loc23_ = 5;
                  }
                  else if(this.power.var_7 >= 2)
                  {
                     _loc23_ = 2;
                  }
                  if(_loc21_.y < -1 * Math.abs(_loc21_.x))
                  {
                     _loc22_ = this.var_19.combatState.method_46(class_14.powerTypesDict["FrostArmorIce" + _loc23_],null,new Point(this.var_11.x,this.var_11.y));
                  }
                  else
                  {
                     _loc22_ = this.var_19.combatState.method_46(class_14.powerTypesDict["FrostArmorIceWall" + _loc23_],null,new Point(this.var_11.x,this.var_11.y));
                  }
                  _loc22_.var_1894 = _loc21_;
               }
            }
         }
         return true;
      }
   }
}
