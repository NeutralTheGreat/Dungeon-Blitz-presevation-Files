package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   
   public class class_58 extends class_32
   {
      
      private static const const_923:uint = 400;
      
      public static const const_56:uint = 8;
      
      private static const const_728:uint = 2000;
      
      private static const const_764:Number = 633;
      
      private static const const_667:Number = 630;
      
      private static const const_744:Number = 630;
       
      
      internal var var_2217:class_33;
      
      internal var var_729:class_33;
      
      private var var_909:Vector.<class_33>;
      
      private var var_1528:Vector.<class_33>;
      
      internal var var_755:class_33;
      
      internal var var_1790:class_33;
      
      internal var var_1670:Boolean = false;
      
      internal var mPowerButtons:Vector.<class_153>;
      
      internal var var_645:class_33;
      
      private var var_2747:int = -1;
      
      private var var_864:class_153;
      
      private var var_2351:class_10;
      
      public var var_2091:Boolean = false;
      
      public var var_2062:Boolean = false;
      
      private var var_1988:Boolean;
      
      private var var_2442:int = -1;
      
      private var var_2752:int = -1;
      
      private var var_2515:int = -1;
      
      private var var_2803:int = -1;
      
      private var var_1793:int = -1;
      
      private var var_2844:int = -1;
      
      private var var_2237:uint = 0;
      
      public function class_58(param1:Game)
      {
         super(param1,"a_Hud",null);
         var_15 = true;
         mbHideOnClear = false;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:MovieClip = null;
         var _loc2_:String = null;
         var _loc3_:MovieClip = null;
         var _loc4_:class_33 = null;
         var _loc5_:MovieClip = null;
         var _loc12_:class_33 = null;
         var _loc13_:class_33 = null;
         var_2.am_LevelText.mouseEnabled = false;
         var_2.am_LevelXP.visible = false;
         var_2.am_LevelXP.mouseEnabled = false;
         var_2.am_XPAdd.visible = false;
         var_2.am_XPAdd.mouseEnabled = false;
         var_2.am_HPText.visible = false;
         var_2.am_HPText.mouseEnabled = false;
         var_2.am_ManaText.visible = false;
         var_2.am_ManaText.mouseEnabled = false;
         var_2.am_TempHPText.visible = false;
         var_2.am_TempHPText.mouseEnabled = false;
         var _loc6_:MovieClip = var_2.am_XPBar;
         var _loc7_:MovieClip;
         (_loc7_ = var_2.am_XPContact).addEventListener(MouseEvent.ROLL_OVER,this.method_951);
         _loc7_.addEventListener(MouseEvent.ROLL_OUT,this.method_758);
         this.var_755 = method_17(_loc6_,"Exp",0);
         var _loc8_:MovieClip;
         (_loc8_ = var_2.am_HPBar).addEventListener(MouseEvent.ROLL_OVER,this.method_741);
         _loc8_.addEventListener(MouseEvent.ROLL_OUT,this.method_852);
         this.var_2217 = method_17(_loc8_,"Health",2);
         var _loc9_:MovieClip;
         (_loc9_ = var_2.am_ManaBar).addEventListener(MouseEvent.ROLL_OVER,this.method_657);
         _loc9_.addEventListener(MouseEvent.ROLL_OUT,this.method_717);
         this.var_729 = method_17(_loc9_,"Mana",2);
         this.var_1790 = method_17(_loc8_.am_TempHP,"TempHP",2);
         var _loc10_:MovieClip;
         (_loc10_ = var_2.am_ClassManaBar).addEventListener(MouseEvent.ROLL_OVER,this.method_1890);
         _loc10_.addEventListener(MouseEvent.ROLL_OUT,this.method_1230);
         this.var_645 = new class_33(var_1,_loc10_);
         this.var_645.BeginHealthMode("Mana",2);
         var_2.am_ClassManaText.visible = false;
         var_2.am_ClassManaText.mouseEnabled = false;
         this.var_909 = new Vector.<class_33>(const_56,true);
         this.var_1528 = new Vector.<class_33>(const_56,true);
         this.mPowerButtons = new Vector.<class_153>(const_56);
         _loc5_ = var_2.am_PowerButtons;
         var _loc11_:uint = 0;
         while(_loc11_ < const_56)
         {
            _loc2_ = String(_loc11_ + 1);
            _loc1_ = _loc5_["am_Key" + _loc2_];
            _loc1_.addEventListener(MouseEvent.MOUSE_OVER,this.method_979);
            _loc1_.addEventListener(MouseEvent.MOUSE_OUT,this.method_835);
            var_1.UIBasicButton_CreateBasicButton(_loc1_,this.method_1261,null,false,true);
            (_loc4_ = new class_33(var_1,_loc1_)).PlayAnimation("LowMojo");
            _loc4_.TickMovieClip();
            (_loc12_ = method_1(_loc1_.am_Selector)).Hide();
            this.var_1528[_loc11_] = _loc12_;
            MathUtil.method_2(_loc1_.am_KeyBindText,_loc2_);
            _loc13_ = method_17(_loc1_.am_Cooldown,"Cooldown",0);
            this.var_909[_loc11_] = _loc13_;
            _loc3_ = _loc1_.am_ButtonHolder.am_Button;
            this.mPowerButtons[_loc11_] = new class_153(_loc1_,_loc4_,_loc3_,_loc3_.am_BlankIcon);
            _loc11_++;
         }
         var_2.am_CacheIcon.mouseEnabled = false;
         var_2.am_CacheIcon.mouseChildren = false;
      }
      
      override public function OnDestroyScreen() : void
      {
         var _loc1_:MovieClip = null;
         var _loc2_:class_153 = null;
         var _loc3_:uint = 0;
         while(_loc3_ < const_56)
         {
            _loc2_ = this.mPowerButtons[_loc3_];
            _loc1_ = _loc2_.keyClip;
            _loc1_.removeEventListener(MouseEvent.MOUSE_OVER,this.method_979);
            _loc1_.removeEventListener(MouseEvent.MOUSE_OUT,this.method_835);
            var_1.UIBasicButton_DestroyBasicButton(_loc1_);
            _loc2_.method_1066();
            this.mPowerButtons[_loc3_] = null;
            _loc3_++;
         }
         this.mPowerButtons = null;
         var _loc4_:MovieClip = var_2.am_HPBar;
         var _loc5_:MovieClip = var_2.am_ManaBar;
         var _loc6_:MovieClip = var_2.am_XPContact;
         _loc4_.removeEventListener(MouseEvent.ROLL_OVER,this.method_741);
         _loc4_.removeEventListener(MouseEvent.ROLL_OUT,this.method_852);
         _loc5_.removeEventListener(MouseEvent.ROLL_OVER,this.method_657);
         _loc5_.removeEventListener(MouseEvent.ROLL_OUT,this.method_717);
         _loc6_.removeEventListener(MouseEvent.ROLL_OVER,this.method_951);
         _loc6_.removeEventListener(MouseEvent.ROLL_OUT,this.method_758);
         this.var_2217 = null;
         this.var_729 = null;
         this.var_1790 = null;
         this.var_755 = null;
         this.var_2351 = null;
         this.var_909 = null;
         this.var_1528 = null;
         this.var_864 = null;
      }
      
      public function OnInitDisplay() : void
      {
         this.var_1988 = false;
      }
      
      public function method_741(param1:MouseEvent) : void
      {
         var_2.am_HPText.visible = true;
         if(this.var_1670)
         {
            var_2.am_TempHPText.visible = true;
         }
         param1.stopPropagation();
      }
      
      public function method_852(param1:MouseEvent) : void
      {
         var_2.am_HPText.visible = false;
         var_2.am_TempHPText.visible = false;
         param1.stopPropagation();
      }
      
      public function method_951(param1:MouseEvent) : void
      {
         var_2.am_LevelXP.visible = true;
         param1.stopPropagation();
      }
      
      public function method_758(param1:MouseEvent) : void
      {
         var_2.am_LevelXP.visible = false;
         param1.stopPropagation();
      }
      
      public function method_657(param1:MouseEvent) : void
      {
         var_2.am_ManaText.visible = true;
         param1.stopPropagation();
      }
      
      public function method_717(param1:MouseEvent) : void
      {
         var_2.am_ManaText.visible = false;
         param1.stopPropagation();
      }
      
      public function method_54(param1:int) : Boolean
      {
         if(var_1.screenKeybind.mbVisible)
         {
            return false;
         }
         if(param1 >= Game.COMMAND_SPELL1 && param1 < Game.COMMAND_SPELL1 + const_56)
         {
            this.method_769(param1 - Game.COMMAND_SPELL1 + 1);
            return true;
         }
         return false;
      }
      
      public function method_1266(param1:int) : void
      {
         var _loc2_:MovieClip = null;
         if(param1 > 0)
         {
            _loc2_ = var_2.am_XPAdd;
            _loc2_.visible = true;
            MathUtil.method_2(_loc2_.am_Text,"+" + param1.toString() + " xp");
            this.var_2237 = var_1.mTimeThisTick;
         }
      }
      
      override public function OnTickScreen() : void
      {
         var _loc11_:class_33 = null;
         var _loc12_:class_153 = null;
         var _loc13_:class_139 = null;
         var _loc16_:uint = 0;
         var _loc17_:Number = NaN;
         var _loc18_:PowerType = null;
         var _loc19_:Number = NaN;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:int = _loc1_.currHP;
         if(_loc2_ < 0)
         {
            _loc2_ = 0;
         }
         this.var_2217.mHealthPerc = _loc2_ / _loc1_.maxHP;
         if(_loc2_ != this.var_2442 || this.var_2752 != _loc1_.maxHP)
         {
            this.var_2752 = _loc1_.maxHP;
            this.var_2442 = _loc2_;
            MathUtil.method_2(var_2.am_HPText,_loc2_ + "/" + _loc1_.maxHP);
         }
         var _loc3_:int = _loc1_.combatState.var_1797;
         if(_loc3_)
         {
            if(_loc3_ <= 0)
            {
               _loc3_ = 0;
               this.var_1670 = false;
               var_2.am_TempHPText.visible = false;
            }
            else
            {
               this.var_1670 = true;
               if(var_2.am_HPText.visible)
               {
                  var_2.am_TempHPText.visible = true;
               }
            }
            this.var_1790.mHealthPerc = _loc3_ / _loc1_.combatState.var_2043;
            if(_loc3_ != this.var_2844)
            {
               this.var_2844 = _loc3_;
               MathUtil.method_2(var_2.am_TempHPText,MathUtil.method_29(_loc3_));
            }
         }
         else
         {
            this.var_1790.mHealthPerc = 0;
            this.var_1670 = false;
            var_2.am_TempHPText.visible = false;
         }
         var _loc4_:Number = _loc1_.var_228;
         var _loc5_:Number = _loc1_.var_1785;
         if(_loc4_ < _loc5_)
         {
            if(!this.var_729.var_564)
            {
               this.var_729.BeginHealthMode("Mana",2);
            }
            this.var_729.mHealthPerc = _loc4_ / _loc5_;
         }
         else if(this.var_729.var_564 || this.var_729.mbCompleted)
         {
            this.var_729.PlayAnimation("Glow");
         }
         if(_loc4_ != this.var_2515)
         {
            this.var_2515 = _loc4_;
            MathUtil.method_2(var_2.am_ManaText,_loc4_ + "/" + _loc5_);
         }
         if(var_2.am_XPAdd.visible)
         {
            _loc16_ = uint(var_1.mTimeThisTick);
            if(this.var_2237 + const_728 <= _loc16_)
            {
               var_2.am_XPAdd.visible = false;
            }
            else
            {
               if((_loc17_ = 1.2 - (_loc16_ - this.var_2237) / const_728) < 0)
               {
                  _loc17_ = 0;
               }
               else if(_loc17_ > 1)
               {
                  _loc17_ = 1;
               }
               var_2.am_XPAdd.alpha = _loc17_;
            }
         }
         var _loc6_:uint = uint(Entity.EXPERIENCE_TABLE[_loc1_.mExpLevel]);
         var _loc7_:uint = Entity.EXPERIENCE_TABLE[_loc1_.mExpLevel + 1] - _loc6_;
         var _loc8_:uint = uint(_loc1_.var_859 - _loc6_);
         if(this.var_2803 != _loc8_ || this.var_1793 != _loc1_.mExpLevel)
         {
            MathUtil.method_2(var_2.am_LevelXP,MathUtil.method_29(_loc8_) + " / " + MathUtil.method_29(_loc7_));
            this.var_2803 = _loc8_;
         }
         if(this.var_755.mbCompleted || this.var_755.var_564)
         {
            if(!this.var_755.var_564)
            {
               this.var_755.BeginHealthMode("Exp",0);
            }
            this.var_755.mHealthPerc = _loc8_ / _loc7_;
         }
         if(this.var_1793 != _loc1_.mExpLevel)
         {
            if(this.var_1793 != -1)
            {
               this.var_755.PlayAnimation("Level");
            }
            MathUtil.method_2(var_2.am_LevelText,_loc1_.mExpLevel.toString());
            this.var_1793 = _loc1_.mExpLevel;
         }
         var _loc9_:Number = _loc1_.var_31;
         var _loc10_:Number = _loc1_.const_156;
         if(_loc9_ <= _loc10_)
         {
            if(!this.var_645.var_564)
            {
               this.var_645.BeginHealthMode("Mana",2);
            }
            this.var_645.mHealthPerc = _loc9_ / _loc10_;
         }
         else if(this.var_645.var_564 || this.var_645.mbCompleted)
         {
            this.var_645.PlayAnimation("Glow");
         }
         this.var_645.TickMovieClip();
         if(_loc9_ != this.var_2747)
         {
            this.var_2747 = _loc9_;
            MathUtil.method_2(var_2.am_ClassManaText,int(_loc9_) + "/" + _loc10_);
         }
         var _loc14_:uint = 0;
         while(_loc14_ < const_56)
         {
            (_loc11_ = (_loc12_ = this.mPowerButtons[_loc14_]).keyAnim).TickMovieClip();
            if(_loc11_.mbCompleted)
            {
               if((Boolean(_loc13_ = _loc11_.mActiveTimeline)) && _loc13_.name == "BackUp")
               {
                  _loc11_.PlayAnimation("Ready");
               }
            }
            _loc14_++;
         }
         var _loc15_:uint = 1;
         while(_loc15_ < EntType.const_238)
         {
            this.method_1566(_loc15_,_loc1_.hudPowers[_loc15_]);
            _loc15_++;
         }
         if(this.var_1988)
         {
            if(this.var_864)
            {
               if(_loc18_ = this.var_864.var_434)
               {
                  _loc19_ = _loc18_.var_749 ? const_667 : (_loc18_.var_1439 ? const_744 : const_764);
                  var_1.screenHudTooltip.ShowPowerTooltip(var_1.clientEnt,this.var_864.var_434,682,_loc19_,class_101.const_573);
               }
            }
         }
      }
      
      private function method_1890(param1:MouseEvent) : void
      {
         var_2.am_ClassManaText.visible = true;
         param1.stopPropagation();
      }
      
      private function method_1230(param1:MouseEvent) : void
      {
         var_2.am_ClassManaText.visible = false;
         param1.stopPropagation();
      }
      
      public function method_1505() : void
      {
         var _loc3_:class_153 = null;
         var _loc4_:PowerType = null;
         var _loc5_:MovieClip = null;
         if(!var_2)
         {
            return;
         }
         var _loc1_:Number = Number(var_1.main.overallScale);
         var _loc2_:uint = 1;
         while(_loc2_ < EntType.const_238)
         {
            _loc3_ = this.mPowerButtons[_loc2_ - 1];
            if(_loc3_.var_220)
            {
               if(!(!(_loc4_ = _loc3_.var_434) || !_loc4_.powerName))
               {
                  (_loc5_ = _loc3_.buttonClip).removeChildAt(0);
                  _loc3_.method_431();
                  if((_loc4_ == PowerType.var_511 || _loc4_ == PowerType.var_315) && var_1.clientEnt && Boolean(var_1.clientEnt.mEquipPet))
                  {
                     _loc3_.var_220 = class_41.method_85(var_1.clientEnt.mEquipPet.mPetType,2,2,44,44,_loc1_,_loc3_.keyClip.scaleX);
                  }
                  else if(_loc4_ == PowerType.var_440 && var_1.clientEnt && Boolean(var_1.clientEnt.mEquipMount))
                  {
                     _loc3_.var_220 = class_41.method_168(var_1.clientEnt.mEquipMount,2,2,44,44,_loc1_,_loc3_.keyClip.scaleX);
                  }
                  else
                  {
                     _loc3_.var_220 = class_4.method_639(var_1,_loc4_.iconName,_loc3_.keyClip.scaleX);
                  }
                  _loc5_.addChild(_loc3_.var_220);
               }
            }
            _loc2_++;
         }
      }
      
      public function method_1566(param1:int, param2:PowerType) : void
      {
         var _loc10_:MovieClip = null;
         var _loc11_:ActivePower = null;
         var _loc12_:Number = NaN;
         var _loc13_:* = false;
         var _loc14_:uint = 0;
         var _loc15_:Boolean = false;
         var _loc16_:uint = 0;
         var _loc17_:uint = 0;
         var _loc18_:uint = 0;
         var _loc19_:class_33 = null;
         var _loc20_:int = 0;
         var _loc21_:int = 0;
         var _loc22_:Boolean = false;
         var _loc23_:Number = NaN;
         var _loc24_:Vector.<Entity> = null;
         var _loc25_:int = 0;
         var _loc26_:Buff = null;
         var _loc3_:Entity = var_1.clientEnt;
         var _loc4_:int = int(var_1.mTimeThisTick);
         var _loc5_:class_153;
         var _loc6_:MovieClip = (_loc5_ = this.mPowerButtons[param1 - 1]).keyClip;
         var _loc7_:class_33 = _loc5_.keyAnim;
         if(param1 == EntType.const_330 && Boolean(_loc3_.combatState.var_270))
         {
            param2 = class_14.powerTypesDict["Dismount"];
         }
         if(param1 == EntType.const_283 && (_loc3_.combatState.var_724 || _loc3_.combatState.var_823))
         {
            param2 = class_14.powerTypesDict["DismissPet"];
         }
         var _loc8_:PowerType;
         if((_loc8_ = param2) != _loc5_.var_434 || this.var_2091 && param1 == EntType.const_283 || this.var_2062 && param1 == EntType.const_330)
         {
            (_loc10_ = _loc5_.buttonClip).removeChildAt(0);
            _loc5_.method_431();
            if(!_loc8_ || !_loc8_.iconName)
            {
               _loc10_.addChild(_loc5_.var_2274);
               this.var_909[param1 - 1].Show();
            }
            else if((_loc8_ == PowerType.var_511 || _loc8_ == PowerType.var_315) && Boolean(_loc3_.mEquipPet))
            {
               _loc5_.var_220 = class_41.method_85(_loc3_.mEquipPet.mPetType,2,2,44,44,var_1.main.overallScale,_loc5_.keyClip.scaleX);
               _loc10_.addChild(_loc5_.var_220);
               this.var_2091 = false;
            }
            else if(_loc8_ == PowerType.var_440 && Boolean(_loc3_.mEquipMount))
            {
               _loc5_.var_220 = class_41.method_168(_loc3_.mEquipMount,2,2,44,44,var_1.main.overallScale,_loc5_.keyClip.scaleX);
               _loc10_.addChild(_loc5_.var_220);
               this.var_2062 = false;
            }
            else
            {
               _loc5_.var_220 = class_4.method_639(var_1,_loc8_.iconName,_loc5_.keyClip.scaleX);
               _loc10_.addChild(_loc5_.var_220);
            }
            _loc5_.var_434 = _loc8_;
            _loc5_.var_714 = param1 > const_56;
            _loc7_.PlayAnimation("LowMojo");
         }
         if(!param2 || !_loc3_.var_234 && param2.powerID != _loc3_.combatState.var_1853)
         {
            _loc6_.am_Toggle.visible = false;
         }
         else if(Boolean(_loc3_.var_234) && _loc3_.var_234.indexOf(param2) != -1)
         {
            _loc6_.am_Toggle.visible = true;
         }
         else if(_loc3_.combatState.var_1853 == param2.powerID)
         {
            _loc6_.am_Toggle.visible = true;
         }
         else
         {
            _loc6_.am_Toggle.visible = false;
         }
         var _loc9_:Boolean = false;
         if(!_loc8_ && this.var_909[param1 - 1].mbVisible)
         {
            _loc9_ = true;
            _loc8_ = param2;
         }
         if(Boolean(_loc8_) && (param1 <= const_56 || _loc9_))
         {
            _loc11_ = _loc3_.combatState.mActivePower;
            _loc12_ = 1 + _loc3_.combatState.var_1083;
            _loc13_ = _loc3_.var_228 >= int(_loc8_.var_535 * _loc12_);
            _loc14_ = uint(_loc3_.combatState.var_114[_loc8_.powerID]);
            _loc15_ = Boolean(_loc11_) && _loc11_.powerType == _loc8_;
            _loc17_ = (_loc16_ = uint(_loc3_.combatState.var_114[_loc8_.powerID])) > _loc4_ ? uint(_loc16_ - _loc4_) : 0;
            _loc18_ = _loc8_.coolDownTime;
            _loc19_ = this.var_909[param1 - 1];
            _loc20_ = _loc4_ - _loc14_;
            _loc21_ = !!_loc8_.coolDownTime ? int(_loc8_.coolDownTime) : int(_loc8_.method_1137());
            _loc22_ = (_loc22_ = !!_loc18_ ? _loc4_ < _loc16_ : _loc20_ < _loc21_) || _loc15_;
            if(Boolean(_loc14_) && _loc20_ < _loc21_)
            {
               _loc23_ = !!_loc18_ ? (_loc18_ - _loc17_) / _loc18_ : _loc20_ / _loc21_;
               this.var_909[param1 - 1].mHealthPerc = _loc23_;
               _loc19_.Show();
            }
            else
            {
               _loc19_.Hide();
            }
            if(_loc8_.var_219 || _loc3_.combatState.var_39 || Boolean(_loc3_.combatState.var_1853))
            {
               _loc13_ = _loc3_.combatState.method_414(_loc8_);
            }
            if(_loc8_.var_851)
            {
               if(!_loc22_)
               {
                  _loc24_ = var_1.GetSummonedCreatures(_loc3_.id,_loc8_);
                  _loc25_ = 0;
                  if(_loc3_.var_18)
                  {
                     _loc25_ = _loc3_.var_18.method_102(_loc3_,_loc8_.basePowerName,"SpawnLimit");
                  }
                  if(_loc8_.var_1629 + _loc25_ <= _loc24_.length)
                  {
                     _loc22_ = false;
                     _loc13_ = false;
                  }
               }
               if(_loc22_ && !_loc15_)
               {
                  _loc22_ = false;
                  _loc13_ = false;
               }
            }
            if(_loc8_.var_698)
            {
               if(!_loc22_)
               {
                  if(_loc26_ = _loc3_.combatState.method_135(class_14.buffTypesDict[_loc8_.var_698]))
                  {
                     _loc22_ = false;
                     _loc13_ = false;
                  }
               }
               if(_loc22_ && !_loc15_)
               {
                  _loc22_ = false;
                  _loc13_ = false;
               }
            }
            if(_loc5_.var_714)
            {
               if(_loc22_)
               {
                  _loc5_.var_714 = false;
                  _loc5_.var_1161 = true;
                  _loc7_.PlayAnimation("Cooldown");
               }
               else if(!_loc13_)
               {
                  _loc5_.var_714 = false;
                  _loc5_.var_1161 = false;
                  _loc7_.PlayAnimation("LowMojo");
               }
            }
            else if(!_loc13_ && !_loc22_ && _loc5_.var_1161)
            {
               _loc5_.var_714 = false;
               _loc5_.var_1161 = false;
               _loc7_.PlayAnimation("LowMojo");
            }
            else if(_loc13_ && !_loc22_)
            {
               _loc5_.var_714 = true;
               _loc5_.var_1161 = false;
               _loc7_.PlayAnimation("BackUp");
            }
         }
      }
      
      public function method_769(param1:int) : void
      {
         var _loc4_:class_33 = null;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:class_153 = this.mPowerButtons[param1 - 1];
         if(!_loc3_ || !_loc3_.var_714)
         {
            return;
         }
         if(_loc2_.method_252(_loc3_.var_434))
         {
            (_loc4_ = _loc3_.keyAnim).PlayAnimation("Cooldown");
            _loc3_.var_714 = false;
            _loc3_.var_1161 = true;
         }
      }
      
      private function method_835(param1:MouseEvent) : void
      {
         var _loc3_:class_153 = null;
         var _loc2_:MovieClip = param1.currentTarget as MovieClip;
         var _loc4_:uint = 0;
         while(_loc4_ < const_56)
         {
            _loc3_ = this.mPowerButtons[_loc4_];
            if(_loc3_.keyClip == _loc2_)
            {
               this.var_1528[_loc4_].Hide();
               break;
            }
            _loc4_++;
         }
         this.var_1988 = false;
         var_1.screenHudTooltip.HideTooltip(true);
         param1.stopPropagation();
      }
      
      private function method_979(param1:MouseEvent) : void
      {
         var _loc4_:class_153 = null;
         var _loc6_:PowerType = null;
         var _loc7_:Number = NaN;
         var _loc2_:MovieClip = param1.currentTarget as MovieClip;
         var _loc5_:uint = 0;
         while(_loc5_ < const_56)
         {
            if((_loc4_ = this.mPowerButtons[_loc5_]).keyClip == _loc2_)
            {
               this.var_1528[_loc5_].Show();
               this.var_864 = _loc4_;
               this.var_1988 = true;
               break;
            }
            _loc5_++;
         }
         if(this.var_864)
         {
            if(_loc6_ = this.var_864.var_434)
            {
               _loc7_ = _loc6_.var_749 ? const_667 : (_loc6_.var_1439 ? const_744 : const_764);
               var_1.screenHudTooltip.ShowPowerTooltip(var_1.clientEnt,this.var_864.var_434,682,_loc7_,class_101.const_573);
            }
         }
         else
         {
            var_1.screenHudTooltip.HideTooltip(true);
         }
         param1.stopPropagation();
      }
      
      private function method_1261(param1:MouseEvent) : void
      {
         var _loc2_:class_153 = null;
         var _loc5_:PowerType = null;
         var _loc6_:class_10 = null;
         var _loc3_:MovieClip = param1.currentTarget as MovieClip;
         var _loc4_:uint = 0;
         while(_loc4_ < const_56)
         {
            _loc2_ = this.mPowerButtons[_loc4_];
            if(_loc2_.keyClip == _loc3_)
            {
               if(param1.ctrlKey && Boolean(_loc2_.var_434))
               {
                  if((_loc5_ = _loc2_.var_434) == PowerType.var_836 || _loc5_.basePowerName == "SummonPet" || _loc5_.basePowerName == "VanityPet")
                  {
                     if(var_1.clientEnt.mEquipPet)
                     {
                        var_1.screenArmory.LinkPetInChat(0,var_1.clientEnt.mEquipPet);
                     }
                     break;
                  }
                  if(_loc5_ == PowerType.var_824 || _loc5_.basePowerName.indexOf("Mount") != -1)
                  {
                     if(var_1.clientEnt.mEquipMount)
                     {
                        var_1.screenArmory.LinkMountInChat(0,var_1.clientEnt.mEquipMount);
                     }
                     break;
                  }
                  if(_loc6_ = var_1.screenSpellbook.GetAbilityTypeFromPowerType(_loc5_))
                  {
                     var_1.screenSpellbook.LinkAbilityInChat(_loc6_,_loc6_.rank);
                  }
                  break;
               }
               this.method_769(_loc4_ + 1);
               break;
            }
            _loc4_++;
         }
         param1.stopPropagation();
      }
      
      public function PlayPowerToHotbar(param1:Number, param2:Number, param3:class_10, param4:Entity) : void
      {
         var _loc7_:Packet = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         this.var_2351 = param3;
         var _loc5_:PowerType = class_14.powerTypesDict[param3.abilityName];
         var _loc6_:MovieClip = this.mPowerButtons[param3.var_90 - 1].buttonClip;
         method_68(_loc5_.iconName,param1,param2,_loc6_,const_923,class_137.method_113,this.method_1236);
         if(class_45.method_461(param3.abilityID) && var_1.mAbilityBook.GetCurrRankByAbilityID(param3.abilityID) == 1)
         {
            var_1.mAbilityBook.mJustGotTutorialAbility = false;
         }
         else
         {
            param4.var_228 = 0;
            _loc7_ = new Packet(LinkUpdater.const_1239);
            var_1.serverConn.SendPacket(_loc7_);
         }
      }
      
      private function method_1236() : void
      {
         var _loc1_:PowerType = class_14.powerTypesDict[this.var_2351.abilityName];
         if(_loc1_)
         {
            var_1.mAbilityBook.RebuildHotbar();
         }
         var_1.screenSpellbook.Refresh();
      }
   }
}
