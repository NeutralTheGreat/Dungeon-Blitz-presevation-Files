package
{
   import flash.geom.Point;
   import flash.utils.Dictionary;
   
   public class Brain
   {
      
      public static const AGGRO_RADIUS:uint = 250;
      
      private static const MAX_PER_SIDE:uint = 3;
      
      private static const const_1048:uint = 7;
      
      public static const const_194:int = 20;
      
      public static const const_606:uint = 250;
      
      public static const const_807:uint = 2000;
      
      public static const const_1200:uint = 450;
      
      public static const const_1130:uint = 600;
      
      private static const const_982:Boolean = Boolean(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT || DevSettings.flags & DevSettings.DEVFLAG_STANDALONE_CLIENT);
       
      
      internal var var_1:Game;
      
      internal var e:Entity;
      
      internal var spawnSurface:class_37 = null;
      
      internal var homeLoc:Point = null;
      
      internal var target:Entity = null;
      
      internal var var_1151:Point = null;
      
      internal var mTargetRange:Number = 0;
      
      internal var var_938:Dictionary;
      
      internal var var_792:Dictionary;
      
      internal var mostHatedEnt:Entity;
      
      internal var var_878:int;
      
      internal var var_2933:uint;
      
      internal var mTetherState:Class;
      
      internal var var_1265:Dictionary = null;
      
      internal var var_119:class_167 = null;
      
      internal var pausedStateClass:Class = null;
      
      internal var bAnnoyedInsteadOfAggro:Boolean = false;
      
      internal var mAggroRadius:Number = 0;
      
      public var var_2907:Boolean = false;
      
      public var bDeepSleep:Boolean = false;
      
      public var var_2750:uint = 0;
      
      public var var_2827:Boolean = false;
      
      public function Brain(param1:Game, param2:Entity)
      {
         super();
         this.var_1 = param1;
         this.e = param2;
         this.homeLoc = new Point(this.e.physPosX,this.e.physPosY);
         this.var_792 = new Dictionary();
         this.ClearHateList();
      }
      
      public function method_1106() : void
      {
         this.var_1 = null;
         this.e = null;
         this.spawnSurface = null;
         this.homeLoc = null;
         this.var_1151 = null;
         this.target = null;
         this.var_938 = null;
         this.var_792 = null;
         this.mostHatedEnt = null;
         this.var_1265 = null;
         this.var_119.DestroyState();
         this.var_119 = null;
      }
      
      public function method_275() : void
      {
         if(DevSettings.flags & DevSettings.DEVFLAG_PERFORMANCETEST)
         {
            this.var_119 = new class_168(this.e);
         }
         else if(DevSettings.flags & DevSettings.DEVFLAG_DUMBMONSTERS)
         {
            this.var_119 = new class_169(this.e);
         }
         else if(this.e.behaviorType.var_844)
         {
            if(this.e.behaviorType.var_2602)
            {
               this.var_119 = new class_170(this.e);
            }
            else
            {
               this.var_119 = new class_176(this.e);
            }
         }
         else if(this.e.behaviorType.var_2937)
         {
            this.var_119 = new class_177(this.e);
         }
         else if(Boolean(this.e.entType.dramaAnim) || this.e.cue && this.e.cue.dramaAnim)
         {
            this.var_119 = new class_173(this.e);
         }
         else if(this.e.behaviorType.var_1080)
         {
            this.var_119 = new class_175(this.e);
         }
         else
         {
            this.var_119 = new class_172(this.e);
         }
         this.var_119.EnterState(true);
         this.var_1265 = new Dictionary();
         this.var_1265[this.var_119.var_786] = 1;
         if(this.e.behaviorType.bFollowSpawner || this.e.behaviorType.var_2112)
         {
            this.mTetherState = class_172;
         }
         else
         {
            this.mTetherState = class_171;
         }
         this.bAnnoyedInsteadOfAggro = Boolean(this.e.cue) && Boolean(this.e.cue.room) && Boolean(this.e.cue.room.bSlowAggroRoom);
         if(this.bAnnoyedInsteadOfAggro)
         {
            this.mAggroRadius = 0.8 * AGGRO_RADIUS;
         }
         else if(this.e.behaviorType.var_969)
         {
            this.mAggroRadius = 2 * AGGRO_RADIUS;
         }
         else
         {
            this.mAggroRadius = AGGRO_RADIUS;
         }
      }
      
      public function method_2078() : void
      {
         this.e.TeleportTo(this.homeLoc.x,this.homeLoc.y);
      }
      
      public function ClearHateList() : void
      {
         this.var_938 = new Dictionary();
         this.mostHatedEnt = null;
         this.var_878 = -1;
         if(!this.var_1.level.bInstanced)
         {
            this.var_792 = new Dictionary();
         }
      }
      
      public function FindClosestEnemy(param1:Boolean) : Entity
      {
         var _loc5_:Entity = null;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc2_:Entity = null;
         var _loc3_:Number = Number.MAX_VALUE;
         var _loc4_:Array = this.var_1.GatherEntities(this.e,this.e.physPosX,this.e.physPosY,this.mAggroRadius,this.mAggroRadius,Game.ENEMY);
         for each(_loc5_ in _loc4_)
         {
            if(!(!param1 && _loc5_.combatState.var_414))
            {
               _loc6_ = _loc5_.physPosX - this.e.physPosX;
               _loc7_ = _loc5_.physPosY - this.e.physPosY;
               if((_loc8_ = _loc6_ * _loc6_ + _loc7_ * _loc7_) < _loc3_)
               {
                  _loc3_ = _loc8_;
                  _loc2_ = _loc5_;
               }
            }
         }
         return _loc2_;
      }
      
      public function method_356() : void
      {
         var _loc1_:String = null;
         var _loc2_:Entity = null;
         var _loc3_:Entity = null;
         var _loc4_:int = 0;
         var _loc5_:Entity = null;
         this.mostHatedEnt = null;
         this.var_878 = -1;
         if(this.var_2827)
         {
            if(this.e.behaviorType.var_1279)
            {
               _loc2_ = this.var_1.GetEntFromID(this.e.summonerId);
               if(_loc2_)
               {
                  _loc3_ = _loc2_.combatState.var_1201;
                  if(_loc3_)
                  {
                     if(_loc3_.bIAmValid && _loc3_.entState != Entity.const_6)
                     {
                        this.mostHatedEnt = _loc3_;
                        this.var_878 = 999;
                        return;
                     }
                     _loc2_.combatState.var_1201 = null;
                  }
               }
            }
         }
         for(_loc1_ in this.var_938)
         {
            if((_loc4_ = int(this.var_938[_loc1_])) > this.var_878)
            {
               if(!(_loc5_ = this.var_1.GetEntFromID(int(_loc1_))) || !_loc5_.bIAmValid || _loc5_.entState == Entity.const_6)
               {
                  delete this.var_938[_loc1_];
               }
               else
               {
                  this.var_878 = _loc4_;
                  this.mostHatedEnt = _loc5_;
               }
            }
         }
      }
      
      private function method_919(param1:Entity) : Boolean
      {
         if(!param1 || !param1.bIAmValid)
         {
            return false;
         }
         if(param1.entState == Entity.const_6)
         {
            return false;
         }
         if(!param1.method_156())
         {
            return false;
         }
         if(param1.behaviorType.var_752)
         {
            return false;
         }
         if(this.e.behaviorType.var_752)
         {
            return false;
         }
         if(this.e.brain.bDeepSleep)
         {
            return false;
         }
         if(this.e.team == param1.team)
         {
            return false;
         }
         return true;
      }
      
      public function AddHate(param1:Entity, param2:int, param3:Boolean) : void
      {
         var _loc7_:Entity = null;
         if(param1 && param1.behaviorType && Boolean(param1.summonerId))
         {
            if(param1.behaviorType.var_2393)
            {
               param1 = this.var_1.GetEntFromID(param1.summonerId);
            }
            else if(param1.behaviorType.var_1563)
            {
               if((Boolean(_loc7_ = this.var_1.GetEntFromID(param1.summonerId))) && !_loc7_.summonerId)
               {
                  this.AddHate(_loc7_,1,false);
               }
            }
         }
         if(!this.method_919(param1))
         {
            return;
         }
         if(Boolean(param2) && !this.e.behaviorType.var_2203)
         {
            this.var_792[param1.id] = 1;
            if(param1.summonerId)
            {
               this.var_792[param1.summonerId] = 1;
            }
         }
         if(this.e.behaviorType.var_1608)
         {
            param3 = false;
         }
         var _loc4_:int = int(this.var_938[param1.id]) + param2;
         this.var_938[param1.id] = _loc4_;
         this.var_2933 = this.var_1.mTimeThisTick;
         var _loc5_:* = this.mostHatedEnt != null;
         if(param2 < 0)
         {
            this.method_356();
         }
         else if(_loc4_ > this.var_878)
         {
            this.var_878 = _loc4_;
            this.mostHatedEnt = param1;
         }
         if(param3 && !_loc5_ && Boolean(this.e.cue))
         {
            this.CallForHelp(param1);
         }
         if(!!this.e.cue ? this.e.cue.room as Room : null)
         {
            if(!null.var_1118)
            {
               null.method_547();
            }
            if(this.e.var_2685 && !null.var_241)
            {
               null.method_307();
            }
         }
      }
      
      public function method_1292(param1:Entity) : void
      {
         if(this.method_919(param1) && !this.e.behaviorType.var_2203)
         {
            this.var_792[param1.id] = 1;
         }
      }
      
      public function CallForHelp(param1:Entity) : void
      {
         var _loc3_:Entity = null;
         var _loc2_:Array = this.var_1.GatherEntities(this.e,this.e.physPosX,this.e.physPosY,Camera.SCREEN_WIDTH,Camera.PLAY_SCREEN_HEIGHT,Game.FRIEND);
         for each(_loc3_ in _loc2_)
         {
            if(_loc3_.brain && _loc3_.currRoom == this.e.currRoom && this.e != _loc3_ && (_loc3_.cue && _loc3_.cue.aggroTeamID && _loc3_.cue.aggroTeamID == this.e.cue.aggroTeamID))
            {
               _loc3_.brain.AddHate(param1,0,false);
            }
         }
      }
      
      public function UpdateTargetRange() : void
      {
         var _loc1_:int = 0;
         var _loc2_:int = 0;
         var _loc3_:int = 0;
         var _loc6_:Entity = null;
         var _loc7_:* = false;
         var _loc8_:int = 0;
         var _loc11_:Brain = null;
         var _loc4_:PowerType = this.e.GetMeleePower();
         if(this.e.behaviorType.bDefaultToRanged || !_loc4_)
         {
            _loc2_ = int(const_1048);
            _loc1_ = const_1200 + this.e.entType.width * 0.5;
         }
         else
         {
            _loc2_ = int(MAX_PER_SIDE);
            _loc1_ = this.target.entType.width * 0.5 + _loc4_.method_63(this.e) - 5;
         }
         var _loc5_:Dictionary = new Dictionary();
         for each(_loc6_ in this.var_1.entities)
         {
            _loc11_ = _loc6_.brain;
            if(!(_loc6_ == this.e || !_loc11_ || _loc11_.target != this.target || _loc6_.entState == Entity.const_6))
            {
               _loc3_ = Math.round(_loc11_.mTargetRange / const_194) * const_194;
               _loc5_[_loc3_] = true;
            }
         }
         _loc7_ = this.e.physPosX < this.target.physPosX;
         _loc8_ = _loc1_ / (_loc2_ + 1);
         if(_loc7_)
         {
            _loc1_ = -_loc1_;
         }
         else
         {
            _loc8_ = -_loc8_;
         }
         this.mTargetRange = _loc1_;
         var _loc9_:Boolean = false;
         var _loc10_:uint = 0;
         while(_loc10_ < _loc2_)
         {
            _loc3_ = Math.round(this.mTargetRange / const_194) * const_194;
            if(!_loc5_[_loc3_])
            {
               _loc9_ = true;
               break;
            }
            this.mTargetRange += _loc8_;
            _loc10_++;
         }
         if(_loc9_)
         {
            return;
         }
         _loc1_ = -_loc1_;
         _loc8_ = -_loc8_;
         this.mTargetRange = _loc1_;
         _loc10_ = 0;
         while(_loc10_ < _loc2_)
         {
            _loc3_ = Math.round(this.mTargetRange / const_194) * const_194;
            if(!_loc5_[_loc3_])
            {
               _loc9_ = true;
               break;
            }
            this.mTargetRange += _loc8_;
            _loc10_++;
         }
         if(!_loc9_)
         {
            this.mTargetRange = -_loc1_ + -_loc8_ * Math.random() * 0.5;
         }
      }
      
      public function FirePowers() : void
      {
         var _loc2_:PowerType = null;
         var _loc6_:PowerType = null;
         var _loc7_:uint = 0;
         var _loc8_:uint = 0;
         var _loc9_:Vector.<Entity> = null;
         var _loc1_:CombatState = this.e.combatState;
         if(_loc1_.var_1278 || _loc1_.var_1488 || _loc1_.mActivePower || Boolean(this.e.currEmote))
         {
            return;
         }
         var _loc3_:uint = this.e.hudPowers.length;
         var _loc4_:Number = !!this.target ? Math.abs(this.target.physPosX - this.e.physPosX) : 0;
         var _loc5_:uint = 0;
         for(; _loc5_ < _loc3_; _loc5_++)
         {
            _loc2_ = this.e.hudPowers[_loc5_];
            if(_loc1_.method_414(_loc2_))
            {
               if(_loc2_.var_1600 || _loc2_.var_6 == PowerType.const_32)
               {
                  if(!this.e.maxSpeed)
                  {
                     continue;
                  }
                  if(_loc4_ < 350)
                  {
                     continue;
                  }
               }
               else if(_loc2_.var_6 == PowerType.TARGETMETHOD_MELEE || _loc2_.var_6 == PowerType.const_46)
               {
                  if((_loc2_.var_820 || _loc2_.var_1571) && !this.e.maxSpeed)
                  {
                     continue;
                  }
                  if(!this.target)
                  {
                     continue;
                  }
                  _loc7_ = !!(_loc6_ = this.e.GetMeleePower()) ? _loc6_.method_63(this.e) : 0;
                  _loc8_ = _loc2_.method_63(this.e);
                  if(_loc7_ > _loc8_)
                  {
                     _loc8_ = _loc7_;
                  }
                  if(_loc4_ > _loc8_ + this.target.entType.width * 0.5)
                  {
                     continue;
                  }
               }
               else if(_loc2_.var_851)
               {
                  _loc9_ = this.var_1.GetSummonedCreatures(this.e.id,_loc2_);
                  if(_loc2_.var_1629 <= _loc9_.length)
                  {
                     this.e.combatState.method_433(_loc2_,1000);
                  }
               }
               this.e.combatState.method_51(_loc2_,false);
               break;
            }
         }
      }
      
      public function method_419(param1:Point) : void
      {
         this.var_1151.x = param1.x;
         this.var_1151.y = param1.y;
      }
      
      public function ChangeTarget(param1:Entity) : void
      {
         if(this.target == param1)
         {
            return;
         }
         this.target = param1;
         if(this.target)
         {
            this.UpdateTargetRange();
         }
      }
      
      public function Think() : void
      {
         var _loc3_:uint = 0;
         var _loc4_:Entity = null;
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         var _loc7_:Boolean = false;
         var _loc8_:Boolean = false;
         var _loc9_:Boolean = false;
         if(Boolean(this.mostHatedEnt) && (!this.mostHatedEnt.bIAmValid || !this.mostHatedEnt.method_156() || this.mostHatedEnt.entState == Entity.const_6))
         {
            this.method_356();
         }
         if(Boolean(this.target) && (!this.target.bIAmValid || this.target.entState == Entity.const_6))
         {
            this.ChangeTarget(null);
            this.method_356();
         }
         var _loc1_:Class = null;
         if((this.e.InActiveCutScene() || this.mostHatedEnt && this.mostHatedEnt.InActiveCutScene()) && const_982 && this.var_119.var_786 != "CutScene")
         {
            _loc1_ = class_174;
            this.pausedStateClass = Object(this.var_119).constructor;
         }
         else
         {
            _loc1_ = this.var_119.TickState();
         }
         if(_loc1_)
         {
            _loc3_ = uint(this.var_1265[this.var_119.var_786]);
            this.var_119.ExitState(_loc3_ == 1);
            this.var_119.DestroyState();
            this.var_119 = new _loc1_(this.e) as class_167;
            _loc3_ = uint(this.var_1265[this.var_119.var_786]);
            this.var_119.EnterState(!_loc3_);
            this.var_1265[this.var_119.var_786] = _loc3_ + 1;
         }
         if(this.var_2907)
         {
            this.e.bRunning = false;
         }
         if(this.e.combatState.var_683 || this.e.combatState.var_445)
         {
            this.e.bRunning = false;
            this.e.bLeft = this.e.var_2252;
            this.e.bBackpedal = this.e.var_2079;
         }
         var _loc2_:ActivePower = this.e.combatState.mActivePower;
         if(Boolean(_loc2_) && (_loc2_.powerType.var_2895 || !_loc2_.var_54))
         {
            this.e.bRunning = false;
         }
         if(this.e.summonerId && this.e.behaviorType.bFollowSpawner && !this.e.behaviorType.var_844 && (!this.e.behaviorType.var_2807 || !this.e.combatState.mActivePower || this.e.combatState.mActivePower.var_344))
         {
            if(_loc4_ = this.var_1.GetEntFromID(this.e.summonerId))
            {
               _loc5_ = this.e.physPosX - _loc4_.physPosX;
               _loc6_ = this.e.physPosY - _loc4_.physPosY;
               if(this.e.entState == Entity.const_399)
               {
                  if(_loc5_ >= -200 && _loc5_ <= 200)
                  {
                     this.e.bRunning = false;
                  }
                  else
                  {
                     this.e.bRunning = true;
                     this.e.bLeft = _loc5_ > 0;
                  }
               }
            }
         }
         if(this.e.currEmote)
         {
            this.e.bRunning = false;
            this.e.bFiring = false;
         }
         if(Boolean(this.e.var_353) && this.e.entType.var_832)
         {
            if(Boolean(this.target) && this.var_119.var_786 != "Melee")
            {
               this.method_563(this.target.physPosY - (this.target.entType.height - 40),false);
            }
            else
            {
               this.e.bJumping = false;
               this.e.bDropping = false;
            }
         }
         if(this.e.bGotoLocation)
         {
            if(_loc8_ = (_loc7_ = Boolean(this.mostHatedEnt) && Boolean(this.e.var_2749 & Flags.CANCEL_ON_AGGRO) && !this.e.InActiveCutScene()) || this.CloseEnoughToStop(this.e.velocity.x,this.e.physPosX,this.e.gotoLocationX))
            {
               this.e.bRunning = false;
            }
            else
            {
               this.e.bRunning = true;
               this.e.bBackpedal = false;
               this.e.bLeft = this.e.physPosX > this.e.gotoLocationX;
            }
            _loc9_ = true;
            if(this.e.gotoLocationY)
            {
               _loc9_ = this.method_563(this.e.gotoLocationY,_loc7_);
            }
            if(_loc8_ && _loc9_)
            {
               this.e.gotoLocationX = 0;
               this.e.gotoLocationY = 0;
               this.e.bGotoLocation = false;
            }
         }
         if(DevSettings.flags & DevSettings.DEVFLAG_SHOWBEHAVIOR)
         {
            this.e.method_436((this.bDeepSleep ? "DS: " : "") + this.var_119.var_786,0);
         }
      }
      
      public function method_563(param1:Number, param2:Boolean) : Boolean
      {
         var _loc4_:* = false;
         var _loc3_:Boolean = param2 || this.CloseEnoughToStop(this.e.velocity.y,this.e.physPosY,param1);
         if(_loc3_)
         {
            this.e.bJumping = false;
            this.e.bDropping = false;
         }
         else
         {
            _loc4_ = this.e.physPosY > param1;
            this.e.bJumping = _loc4_;
            this.e.bDropping = !_loc4_;
         }
         return _loc3_;
      }
      
      public function CloseEnoughToStop(param1:Number, param2:Number, param3:Number) : Boolean
      {
         var _loc4_:Number;
         if((_loc4_ = param1 * param1 * 0.5) < 5)
         {
            _loc4_ = 5;
         }
         var _loc5_:Number;
         return (_loc5_ = Math.abs(param2 - param3)) <= _loc4_;
      }
   }
}
