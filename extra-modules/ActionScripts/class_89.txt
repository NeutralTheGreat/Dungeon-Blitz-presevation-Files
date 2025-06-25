package
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.utils.Dictionary;
   
   public class class_89 extends class_32
   {
      
      public static const const_331:uint = 1 << 0;
      
      public static const const_272:uint = 1 << 1;
      
      public static const const_138:uint = 1 << 2;
      
      public static const const_281:uint = 1 << 3;
      
      public static const const_263:uint = 1 << 4;
      
      public static const const_261:uint = 1 << 5;
      
      public static const const_352:uint = 1 << 6;
      
      private static const const_290:Dictionary = new Dictionary();
      
      private static const const_1143:String = "_Wait";
      
      private static const const_1285:uint = const_1143.length;
      
      private static const const_1163:String = "ArrowAnimation";
      
      private static const const_903:uint = const_1163.length;
      
      {
         const_290[const_272] = Game.const_372;
         const_290[const_281] = Game.const_414;
         const_290[const_138] = Game.const_502;
         const_290[const_263] = Game.const_552;
      }
      
      private var var_649:class_32;
      
      internal var mCurrentTutorialIdx:uint;
      
      private var var_450:uint;
      
      private var var_852:uint;
      
      private var var_462:class_33;
      
      private var var_541:class_33;
      
      private var var_508:Vector.<class_33>;
      
      private var var_2269:uint;
      
      private var var_1396:uint;
      
      private var var_2850:Boolean = false;
      
      private var var_428:Function;
      
      public function class_89(param1:Game)
      {
         super(param1,"a_ScreenInteractiveTutorial","am_Panel");
         var_15 = true;
         mbHideOnClear = false;
      }
      
      override public function OnDestroyScreen() : void
      {
         this.method_535();
         this.var_462 = null;
         this.var_508 = null;
         if(this.var_541)
         {
            this.var_541.DestroyUIMovieClip();
         }
         this.var_541 = null;
         this.var_649 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:String = null;
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         if(!this.var_462)
         {
            return;
         }
         if(this.var_450 == this.var_852)
         {
            this.method_345();
         }
         else
         {
            _loc1_ = String(this.var_462.mMovieClip.currentLabels[this.var_450].name);
            this.var_462.PlayAnimation(_loc1_);
            _loc2_ = uint(const_903 + String(this.var_450).length + const_1285);
            _loc3_ = uint(_loc1_.substr(_loc2_,_loc1_.length));
            if(_loc3_)
            {
               this.var_2269 = _loc3_;
               this.var_1396 = var_1.mTimeThisTick;
            }
         }
      }
      
      override public function OnTickScreen() : void
      {
         if(Boolean(this.var_649) && !this.var_649.mbVisible)
         {
            if(this.var_450 >= this.var_852 - 1)
            {
               this.method_345();
            }
            else
            {
               this.method_417();
            }
         }
         if(Boolean(this.var_1396) && var_1.mTimeThisTick - this.var_1396 > this.var_2269)
         {
            this.method_767();
         }
         if(this.var_2850 && this.var_462.mbCompleted)
         {
            this.method_345();
         }
      }
      
      private function method_345() : void
      {
         var_1.screenNotification.ShowNotification(class_46.const_722,"Tutorial Complete","M",false);
         if(this.mCurrentTutorialIdx)
         {
            var_1.mTutorialsCompletedList |= this.mCurrentTutorialIdx;
         }
         var _loc1_:uint = uint(const_290[this.mCurrentTutorialIdx]);
         if(_loc1_)
         {
            var_1.SetNewTutorialStage(_loc1_);
         }
         if(this.mCurrentTutorialIdx == const_261 && !(var_1.mAlertState & Game.const_421))
         {
            var_1.UpdateAlert(Game.const_421);
         }
         this.method_417();
      }
      
      private function method_417() : void
      {
         this.method_535();
         this.var_450 = 0;
         this.var_852 = 0;
         this.mCurrentTutorialIdx = 0;
         this.var_462.Hide();
         this.var_462 = null;
         this.var_2269 = 0;
         this.var_1396 = 0;
         if(this.var_541)
         {
            this.var_541.DestroyUIMovieClip();
         }
         this.var_541 = null;
         var _loc1_:MovieClip = this.var_649.mWindow.mMovieClip["am_GlobalUpgradePanel"] as MovieClip;
         if(_loc1_)
         {
            _loc1_.alpha = 1;
         }
         this.var_649 = null;
         Hide();
      }
      
      public function SetTutorial(param1:uint, param2:class_32, param3:class_33, param4:Vector.<class_33>) : void
      {
         if(!param3 || !param4 || !param2)
         {
            return;
         }
         if(this.var_649)
         {
            if(this.var_450 >= this.var_852 - 1)
            {
               this.method_345();
            }
            else
            {
               this.method_417();
            }
         }
         this.mCurrentTutorialIdx = param1;
         this.var_462 = param3;
         this.var_649 = param2;
         var _loc5_:MovieClip;
         if(_loc5_ = this.var_649.mWindow.mMovieClip["am_GlobalUpgradePanel"] as MovieClip)
         {
            _loc5_.alpha = 0;
         }
         this.var_508 = param4;
         this.var_508.fixed = true;
         this.method_1535();
         this.var_852 = this.var_462.mMovieClip.currentLabels.length;
         this.var_450 = 0;
         this.var_2850 = this.var_450 == this.var_852;
         Display();
         Refresh();
      }
      
      private function method_1535() : void
      {
         var _loc2_:class_33 = null;
         this.var_428 = this.method_1671(this.method_1157,[this.mCurrentTutorialIdx]);
         var _loc1_:MovieClip = this.var_462.mMovieClip.am_ConfirmButton;
         if(_loc1_)
         {
            if(this.var_541)
            {
               this.var_541.DestroyUIMovieClip();
               this.var_541 = null;
            }
            this.var_541 = method_5(_loc1_,this.var_428);
         }
         var _loc3_:uint = !!this.var_508 ? this.var_508.length : 0;
         var _loc4_:uint = 0;
         while(_loc4_ < _loc3_)
         {
            _loc2_ = this.var_508[_loc4_];
            if(_loc2_.var_1230)
            {
               _loc2_.mMovieClip.addEventListener(MouseEvent.CLICK,this.var_428,false,0);
               _loc2_.mMovieClip.addEventListener(MouseEvent.RIGHT_CLICK,this.var_428,false,0);
            }
            else
            {
               _loc2_.mMovieClip.addEventListener(MouseEvent.MOUSE_DOWN,this.var_428,false,0);
               _loc2_.mMovieClip.addEventListener(MouseEvent.RIGHT_MOUSE_DOWN,this.var_428,false,0);
            }
            _loc4_++;
         }
      }
      
      private function method_535() : void
      {
         var _loc1_:class_33 = null;
         var _loc2_:uint = !!this.var_508 ? this.var_508.length : 0;
         var _loc3_:uint = 0;
         while(_loc3_ < _loc2_)
         {
            _loc1_ = this.var_508[_loc3_];
            if(_loc1_.var_1230)
            {
               _loc1_.mMovieClip.removeEventListener(MouseEvent.CLICK,this.var_428,false);
               _loc1_.mMovieClip.removeEventListener(MouseEvent.RIGHT_CLICK,this.var_428,false);
            }
            else
            {
               _loc1_.mMovieClip.removeEventListener(MouseEvent.MOUSE_DOWN,this.var_428,false);
               _loc1_.mMovieClip.removeEventListener(MouseEvent.RIGHT_MOUSE_DOWN,this.var_428,false);
            }
            _loc3_++;
         }
         this.var_508 = null;
         this.var_428 = null;
      }
      
      private function method_1157(param1:MouseEvent, param2:uint) : void
      {
         if(this.mCurrentTutorialIdx == param2)
         {
            this.method_767();
         }
      }
      
      private function method_767() : void
      {
         if(!this.var_462)
         {
            return;
         }
         this.var_1396 = 0;
         this.var_450 = this.var_450 == this.var_852 ? this.var_852 : uint(this.var_450 + 1);
         Refresh();
      }
      
      public function method_134() : Boolean
      {
         return !!this.var_649 ? true : false;
      }
      
      public function method_2015() : uint
      {
         return this.mCurrentTutorialIdx;
      }
      
      private function method_1671(param1:Function, param2:Array) : Function
      {
         var callbackFunction:Function = param1;
         var parameters:Array = param2;
         return function(param1:Event):void
         {
            callbackFunction.apply(null,[param1].concat(parameters));
         };
      }
      
      public function CheckCompletedTutorials(param1:uint = 0) : Boolean
      {
         var _loc3_:class_10 = null;
         var _loc4_:class_10 = null;
         var _loc5_:int = 0;
         var _loc6_:Boolean = false;
         if(var_1.mTutorialsCompletedList & param1)
         {
            return true;
         }
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return false;
         }
         if(!param1 || param1 == const_331)
         {
            _loc3_ = this.GetTutorialAbility();
            _loc4_ = var_1.mAbilityBook.mAbilityResearch;
            if(_loc3_ && var_1.mAbilityBook.GetCurrRankByAbilityID(_loc3_.abilityID) || _loc4_ && _loc4_.abilityID == _loc3_.abilityID && var_1.mAbilityBook.mStatus != class_45.const_29)
            {
               var_1.mTutorialsCompletedList |= const_331;
            }
         }
         if(!param1 || param1 == const_272)
         {
            if(_loc2_.hudPowers[3])
            {
               var_1.mTutorialsCompletedList |= const_272;
            }
         }
         if(!param1 || param1 == const_352)
         {
            if(var_1.mCraftTalentData.craftXP)
            {
               var_1.mTutorialsCompletedList |= const_352;
            }
         }
         if(!param1 || param1 == const_138)
         {
            if(Boolean(var_1.mCraftTalentData.craftXP) || Boolean(var_1.mMagicForgeStatus.GetCurrentlyCrafting()))
            {
               var_1.mTutorialsCompletedList |= const_138;
            }
         }
         if(!param1 || param1 == const_263)
         {
            _loc5_ = var_1.mMasterClassTower.GetPointsByIndex(1) + var_1.mMasterClassTower.GetPointsByIndex(2) + var_1.mMasterClassTower.GetPointsByIndex(3);
            if(var_1.mMasterClassTower.mStatus == class_66.const_200 || Boolean(_loc5_))
            {
               var_1.mTutorialsCompletedList |= const_263;
            }
         }
         if(!param1 || param1 == const_261)
         {
            if(!_loc2_.var_85.method_599() || Boolean(var_1.mAlertState & Game.const_421))
            {
               var_1.mTutorialsCompletedList |= const_261;
            }
         }
         if(!param1 || param1 == const_281)
         {
            if((_loc6_ = var_1.mEggPetInfo.mEggStatus == class_81.const_131 || var_1.mEggPetInfo.mEggStatus == class_81.const_319) || Boolean(var_1.mEggPetInfo.mOwnedPets.length))
            {
               var_1.mTutorialsCompletedList |= const_281;
            }
         }
         return Boolean(param1 & var_1.mTutorialsCompletedList);
      }
      
      public function GetTutorialAbility() : class_10
      {
         var _loc2_:class_10 = null;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return null;
         }
         switch(_loc1_.entType.className)
         {
            case "Paladin":
               _loc2_ = class_14.var_704["GroupHoT"];
               break;
            case "Rogue":
               _loc2_ = class_14.var_704["ReduceArmor"];
               break;
            case "Mage":
               _loc2_ = class_14.var_704["IceStorm"];
         }
         return _loc2_;
      }
   }
}
