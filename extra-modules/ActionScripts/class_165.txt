package
{
   import flash.geom.Point;
   
   public class class_165 extends class_130
   {
       
      
      internal var var_2311:Vector.<Entity>;
      
      internal var var_2124:int = 0;
      
      public function class_165(param1:Number, param2:Number, param3:Number, param4:Number, param5:Entity, param6:PowerType, param7:uint, param8:Boolean, param9:uint = 0, param10:Boolean = false)
      {
         super(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10);
         this.var_2311 = new Vector.<Entity>();
         var_1.playerEntLayer.setChildIndex(gfx.m_TheDO,var_1.playerEntLayer.numChildren - 1);
      }
      
      override public function TickMissile() : Boolean
      {
         var _loc7_:Entity = null;
         var _loc8_:Number = NaN;
         var _loc9_:Array = null;
         var _loc10_:Entity = null;
         var _loc11_:Number = NaN;
         var _loc12_:Number = NaN;
         var _loc13_:class_37 = null;
         var _loc14_:class_37 = null;
         var _loc15_:Array = null;
         var _loc16_:int = 0;
         var _loc17_:int = 0;
         var _loc18_:Entity = null;
         var _loc19_:* = false;
         var _loc1_:Boolean = false;
         var _loc2_:class_37 = null;
         var _loc3_:Point = new Point(0,-1);
         var _loc4_:Boolean = false;
         if(var_1718 > 0)
         {
            return false;
         }
         if(!var_19.bIAmValid)
         {
            method_106(var_11.x,var_11.y,null,false);
            return false;
         }
         var _loc5_:Point;
         (_loc5_ = new Point(velocity.x,velocity.y)).normalize(var_1.TIMESTEP * 20);
         var _loc6_:Point = new Point(var_11.x + _loc5_.x,var_11.y + _loc5_.y);
         if(var_536)
         {
            _loc7_ = null;
            _loc8_ = Camera.SCREEN_WIDTH * 0.5;
            _loc9_ = var_1.GatherEntities(var_19,var_11.x,var_11.y,_loc8_,_loc8_,power.damageMultFull < 0 ? Game.FRIEND : Game.ENEMY);
            for each(_loc10_ in _loc9_)
            {
               if(_loc10_ != var_19)
               {
                  if(!(!_loc10_.method_156() || _loc10_.behaviorType.var_1225 || _loc10_.behaviorType.var_1723))
                  {
                     if(CombatState.method_255(var_11,_loc5_,_loc10_))
                     {
                        _loc7_ = _loc10_;
                        _loc1_ = true;
                        break;
                     }
                  }
               }
            }
            if(!_loc1_)
            {
               if((_loc13_ = var_1.collMan.getFloorCollision(0,var_11.x,var_11.y,_loc5_,_loc6_,null,_loc3_,null,CollisionManager.HARD_FLOOR,0)) != null)
               {
                  _loc2_ = _loc13_;
               }
               if(_loc2_ != null)
               {
                  _loc1_ = true;
                  _loc4_ = true;
               }
            }
            _loc11_ = Number(var_11.x);
            _loc12_ = Number(var_11.y);
            if(!var_378 && !_loc1_ && Point.distance(var_11.add(_loc5_),var_502) > var_1858)
            {
               var_378 = true;
               _loc11_ = Number(var_638.x);
               _loc12_ = Number(var_638.y);
            }
            if(var_378)
            {
               if((_loc14_ = var_1.collMan.getFloorCollision(0,_loc11_,_loc12_,_loc5_,_loc6_,null,_loc3_,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0)) != null)
               {
                  _loc2_ = _loc14_;
               }
               if(_loc2_ != null)
               {
                  _loc1_ = true;
                  _loc4_ = true;
               }
            }
         }
         var_11.x = _loc6_.x;
         var_11.y = _loc6_.y;
         _loc5_.normalize(1);
         var_559 = MathUtil.method_222(var_559,_loc5_,360);
         gfx.m_TheDO.x = var_11.x;
         gfx.m_TheDO.y = var_11.y;
         gfx.m_TheDO.rotation = var_559;
         if(var_536)
         {
            if(_loc1_ || var_1.mTimeThisTick - var_1456 > 2000)
            {
               if(power.aoeRadius)
               {
                  _loc15_ = var_1.GatherEntities(var_19,var_11.x,var_11.y,power.aoeRadius,power.aoeRadius,power.damageMultFull < 0 ? Game.FRIEND : Game.ENEMY);
               }
               else if(_loc7_)
               {
                  _loc15_ = new Array(_loc7_);
               }
               else
               {
                  _loc15_ = new Array();
               }
               _loc17_ = int(_loc15_.length);
               _loc16_ = 0;
               while(_loc16_ < _loc17_)
               {
                  if(_loc18_ = _loc15_[_loc16_])
                  {
                     if(this.var_2311.indexOf(_loc18_) < 0)
                     {
                        ++this.var_2124;
                        this.var_2311.push(_loc18_);
                     }
                     else
                     {
                        _loc15_.splice(_loc16_,1);
                        _loc16_--;
                     }
                  }
                  _loc16_++;
               }
               var_19.combatState.FireThisPower(power,var_11,_loc15_,var_743,0,var_1448,0,null,0,var_249);
               if(_loc4_ || var_1.mTimeThisTick - var_1456 > 2000)
               {
                  _loc19_ = _loc7_ != null;
                  method_106(var_11.x,var_11.y,!!_loc2_ ? new Point(-_loc3_.x,-_loc3_.y) : _loc5_,this.var_2124 > 0);
                  if(localMissileID)
                  {
                     var_1.linkUpdater.WriteProjectileExplode(var_19,localMissileID,var_11.x,var_11.y,_loc19_);
                  }
                  if(var_19.debugPowerGfx)
                  {
                     power.DrawDebugRange(var_19.debugPowerGfx,var_19,var_11,0);
                  }
               }
            }
         }
         return true;
      }
   }
}
