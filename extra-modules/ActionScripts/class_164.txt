package
{
   import flash.geom.Point;
   
   public class class_164 extends class_130
   {
      
      public static const const_844:int = 20;
      
      public static const const_506:int = -15;
       
      
      internal var var_2873:Number = 0;
      
      internal var var_1890:Number = 0;
      
      internal var var_2254:uint = 0;
      
      internal var var_2779:Boolean = true;
      
      public function class_164(param1:Number, param2:Number, param3:Number, param4:Number, param5:Entity, param6:PowerType, param7:uint, param8:Boolean, param9:uint = 0, param10:Boolean = false, param11:int = 20, param12:int = -15)
      {
         super(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10);
         if(param6.basePowerName == "FlameAxe")
         {
            this.var_2779 = false;
         }
         var _loc13_:Number = param3 - param1;
         this.var_1890 = param12;
         this.var_2873 = _loc13_ > 0 ? param11 : -param11;
         this.var_2254 = var_1.mTimeThisTick;
      }
      
      override public function TickMissile() : Boolean
      {
         var _loc7_:Entity = null;
         var _loc8_:Number = NaN;
         var _loc9_:Array = null;
         var _loc10_:Boolean = false;
         var _loc11_:Entity = null;
         var _loc12_:Number = NaN;
         var _loc13_:Number = NaN;
         var _loc14_:class_37 = null;
         var _loc15_:class_37 = null;
         var _loc16_:Array = null;
         var _loc17_:uint = 0;
         var _loc18_:* = false;
         var _loc1_:Boolean = false;
         var _loc2_:class_37 = null;
         var _loc3_:Point = new Point(0,-1);
         if(var_1718 > 0)
         {
            return false;
         }
         if(!var_19.bIAmValid)
         {
            method_106(var_11.x,var_11.y,null,false);
            return false;
         }
         var _loc4_:uint = var_1.mTimeThisTick - this.var_2254;
         this.var_2254 = var_1.mTimeThisTick;
         this.var_1890 += Entity.GRAVITY * var_1.TIMESTEP;
         var _loc5_:Point = new Point(this.var_2873 * var_1.TIMESTEP,this.var_1890 * var_1.TIMESTEP);
         var _loc6_:Point = new Point(var_11.x + _loc5_.x,var_11.y + _loc5_.y);
         if(var_536)
         {
            _loc7_ = null;
            _loc8_ = Camera.SCREEN_WIDTH * 0.5;
            _loc9_ = this.var_2779 ? var_1.GatherEntities(var_19,var_11.x,var_11.y,_loc8_,_loc8_,power.damageMultFull < 0 ? Game.FRIEND : Game.ENEMY) : null;
            _loc10_ = PowerType.method_432(power,var_19);
            for each(_loc11_ in _loc9_)
            {
               if(_loc11_ != var_19)
               {
                  if(!(!_loc11_.method_156() || _loc11_.behaviorType.var_1225 || _loc11_.behaviorType.var_1723))
                  {
                     if(!(_loc11_.behaviorType.var_1094 && !_loc10_))
                     {
                        if(CombatState.method_255(var_11,_loc5_,_loc11_))
                        {
                           _loc7_ = _loc11_;
                           _loc1_ = true;
                           _loc6_.x = var_11.x * 0.3 + _loc11_.appearPosX * 0.7;
                           _loc6_.y = var_11.y;
                           break;
                        }
                     }
                  }
               }
            }
            if(!_loc1_)
            {
               if((_loc14_ = var_1.collMan.getFloorCollision(0,var_11.x,var_11.y,_loc5_,_loc6_,null,_loc3_,null,CollisionManager.HARD_FLOOR,0)) != null)
               {
                  _loc2_ = _loc14_;
               }
               if(_loc2_ != null)
               {
                  _loc1_ = true;
               }
            }
            _loc12_ = Number(var_11.x);
            _loc13_ = Number(var_11.y);
            if(!var_378 && !_loc1_ && Point.distance(var_11.add(_loc5_),var_502) > var_1858)
            {
               var_378 = true;
               _loc12_ = Number(var_638.x);
               _loc13_ = Number(var_638.y);
            }
            if(var_378)
            {
               if((_loc15_ = var_1.collMan.getFloorCollision(0,var_11.x,var_11.y,_loc5_,_loc6_,null,_loc3_,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0)) != null)
               {
                  _loc2_ = _loc15_;
               }
               if(_loc2_ != null)
               {
                  _loc1_ = true;
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
            if(_loc1_ || var_1.mTimeThisTick - var_1456 > var_2413)
            {
               if(power.aoeRadius)
               {
                  _loc16_ = var_1.GatherEntities(var_19,var_11.x,var_11.y,power.aoeRadius,power.aoeRadius,power.damageMultFull < 0 ? Game.FRIEND : Game.ENEMY);
               }
               else if(_loc7_)
               {
                  _loc16_ = new Array(_loc7_);
               }
               else
               {
                  _loc16_ = new Array();
               }
               _loc18_ = (_loc17_ = uint(var_19.combatState.FireThisPower(power,var_11,_loc16_,var_743,0,var_1448,0,null,0,var_249))) > 0;
               method_106(var_11.x,var_11.y,!!_loc2_ ? new Point(-_loc3_.x,-_loc3_.y) : _loc5_,_loc18_);
               if(localMissileID)
               {
                  var_1.linkUpdater.WriteProjectileExplode(var_19,localMissileID,var_11.x,var_11.y,_loc18_);
               }
               if(var_19.debugPowerGfx)
               {
                  power.DrawDebugRange(var_19.debugPowerGfx,var_19,var_11,0);
               }
            }
         }
         return true;
      }
   }
}
