package
{
   import flash.display.GraphicsSolidFill;
   import flash.display.IGraphicsData;
   import flash.display.MovieClip;
   import flash.text.TextField;
   
   public class class_101 extends class_32
   {
      
      private static const const_583:uint = 0;
      
      private static const const_793:uint = 1;
      
      private static const const_696:uint = 2;
      
      private static const const_1007:uint = 3;
      
      public static const const_558:int = 3;
      
      public static const const_770:int = 5;
      
      private static const const_660:uint = 197;
      
      private static const const_388:uint = 223;
      
      private static const const_653:uint = 249;
      
      private static const const_326:uint = 11;
      
      public static const const_523:int = 0;
      
      public static const const_436:int = 1;
      
      public static const RUNESLOT_PROC1:int = 2;
      
      public static const RUNESLOT_PROC2:int = 3;
      
      public static const const_1389:int = 4;
      
      public static const const_547:uint = 0;
      
      public static const const_825:uint = 1;
      
      public static const const_573:uint = 2;
       
      
      public var var_1985:class_33;
      
      public var mTreasureMapDetails:class_33;
      
      private var var_1068:class_33;
      
      private var var_1152:class_33;
      
      private var var_1141:class_33;
      
      private var var_750:class_33;
      
      private var var_2003:class_33;
      
      private var var_1297:class_33;
      
      private var var_730:class_33;
      
      public var var_701:class_33;
      
      private var var_2275:class_33;
      
      private var var_1788:Vector.<class_33>;
      
      private var var_892:Vector.<class_33>;
      
      public var mGearEquippedTooltip:class_33;
      
      private var var_2416:class_33;
      
      private var var_1731:Vector.<class_33>;
      
      private var var_1008:Vector.<class_33>;
      
      public var var_1531:class_33;
      
      public var mSignetDetails2Desc:class_33;
      
      public var mSignetDetails2Stat:class_33;
      
      public var mSignetDetails2Desc2Stat:class_33;
      
      public var var_1671:class_33;
      
      public var var_1733:class_33;
      
      public var mCharmTooltip:class_33;
      
      private var var_1160:class_33;
      
      private var mCharmTooltipProp1:class_33;
      
      private var mCharmTooltipProp2:class_33;
      
      private var mCharmTooltipProp3:class_33;
      
      private var var_1210:class_33;
      
      private var var_1261:class_33;
      
      private var var_1665:class_33;
      
      private var var_1694:class_33;
      
      private var var_1275:class_33;
      
      private var var_2141:class_33;
      
      private var var_1953:class_33;
      
      private var var_627:class_33;
      
      private var var_806:class_33;
      
      private var var_1930:class_33;
      
      private var var_1847:class_33;
      
      private var var_657:class_33;
      
      private var var_2242:Vector.<uint>;
      
      private var var_2147:Vector.<uint>;
      
      public function class_101(param1:Game)
      {
         super(param1,"a_ScreenHudTooltip",null);
         var_15 = true;
         mbHideOnClear = false;
         var_101 = false;
      }
      
      public static function method_37(param1:String, param2:String = null, param3:String = null) : uint
      {
         if(param2 && param1 == "M" && param2 == class_12.const_205)
         {
            return ScreenArmory.const_315;
         }
         if(param3 && param1 == "M" && (param3 == class_18.const_384 || param3 == class_18.const_322))
         {
            return ScreenArmory.const_315;
         }
         if(param1 == "L")
         {
            return ScreenArmory.const_23;
         }
         if(param1 == "R")
         {
            return ScreenArmory.const_22;
         }
         if(param1 == "U")
         {
            return ScreenArmory.const_315;
         }
         if(param1 == "Missing")
         {
            return ScreenArmory.const_9;
         }
         return ScreenArmory.const_24;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc3_:uint = 0;
         var _loc6_:MovieClip = null;
         this.var_1531 = method_27(var_2.am_SignetDetails);
         this.mSignetDetails2Stat = method_27(var_2.am_SignetDetails2Stat);
         this.mSignetDetails2Desc2Stat = method_27(var_2.am_SignetDetails2Desc2Stat);
         this.var_1671 = method_27(var_2.am_MasterLockedDetails);
         this.var_1733 = method_27(var_2.am_MasterUnlockedDetails);
         this.mSignetDetails2Desc = method_27(var_2.am_SignetDetails2Desc);
         this.var_1985 = method_27(var_2.am_BuffDetails);
         this.mTreasureMapDetails = method_27(var_2.am_TreasureMapDetails);
         this.var_750 = method_27(var_2.am_ConsumableTooltip);
         this.var_2003 = method_1(var_2.am_ConsumableTooltip.am_Base);
         this.var_1297 = method_27(var_2.am_HudPowerDetails);
         this.var_730 = method_27(var_2.am_SpellBookPowerDetails);
         this.var_1068 = method_27(var_2.am_SimpleTooltip);
         this.var_1152 = method_27(var_2.am_BasicItem);
         this.var_1141 = method_27(var_2.am_BasicDescription);
         this.var_1210 = method_27(var_2.am_LockboxTooltip);
         this.var_1261 = method_27(var_2.am_DyeTooltip);
         this.var_1665 = method_1(var_2.am_DyeTooltip.am_SmallBottle);
         this.var_1694 = method_1(var_2.am_DyeTooltip.am_LargeBottle);
         this.var_1275 = method_1(var_2.am_PotionDetails);
         this.var_2141 = method_1(var_2.am_PotionDetails.am_ActiveWrapper.am_ItemIconHolder);
         this.var_1953 = method_1(var_2.am_PotionDetails.am_NextWrapper.am_ItemIconHolder);
         this.var_627 = method_27(var_2.am_PetDetails);
         this.var_806 = method_17(this.var_627.mMovieClip.am_Progress,"Progress",0);
         this.var_1930 = method_1(this.var_627.mMovieClip.am_Base);
         this.var_1847 = method_1(this.var_627.mMovieClip.am_MaxLevel);
         var _loc1_:MovieClip = var_2.am_ItemDetail;
         this.var_701 = method_27(_loc1_);
         this.var_2275 = method_1(_loc1_.am_Base);
         var _loc2_:MovieClip = var_2.am_ItemDetailEquipped;
         this.mGearEquippedTooltip = method_27(_loc2_);
         this.var_2416 = method_1(_loc2_.am_Base);
         this.var_1788 = new Vector.<class_33>(const_558,true);
         this.var_1731 = new Vector.<class_33>(const_558,true);
         _loc3_ = 0;
         while(_loc3_ < const_558)
         {
            _loc6_ = _loc1_["am_GemIcon" + (_loc3_ + 1)] as MovieClip;
            this.var_1788[_loc3_] = method_1(_loc6_);
            _loc6_ = _loc2_["am_GemIcon" + (_loc3_ + 1)] as MovieClip;
            this.var_1731[_loc3_] = method_1(_loc6_);
            _loc3_++;
         }
         this.var_892 = new Vector.<class_33>(const_770,true);
         this.var_892[const_523] = method_1(_loc1_.am_PowerRune);
         this.var_892[const_436] = method_1(_loc1_.am_SupportRune);
         this.var_892[RUNESLOT_PROC1] = method_1(_loc1_.am_ProcRune1);
         this.var_892[RUNESLOT_PROC2] = method_1(_loc1_.am_ProcRune2);
         this.var_1008 = new Vector.<class_33>(const_770,true);
         this.var_1008[const_523] = method_1(_loc2_.am_PowerRune);
         this.var_1008[const_436] = method_1(_loc2_.am_SupportRune);
         this.var_1008[RUNESLOT_PROC1] = method_1(_loc2_.am_ProcRune1);
         this.var_1008[RUNESLOT_PROC2] = method_1(_loc2_.am_ProcRune2);
         this.mCharmTooltip = method_27(var_2.am_CharmDetail);
         this.var_1160 = method_1(var_2.am_CharmDetail.am_Base);
         this.mCharmTooltipProp1 = method_1(var_2.am_CharmDetail.am_PrimaryColor);
         this.mCharmTooltipProp2 = method_1(var_2.am_CharmDetail.am_SecondaryColor);
         this.mCharmTooltipProp3 = method_1(var_2.am_CharmDetail.am_TertiaryColor);
         var _loc4_:MovieClip = class_4.method_16("a_RewardTypeIcon_DyeSmall");
         var _loc5_:MovieClip = class_4.method_16("a_RewardTypeIcon_DyeLarge");
         this.var_2242 = this.method_558(_loc4_.am_DyeSwap);
         this.var_2147 = this.method_558(_loc5_.am_DyeSwap);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1985 = null;
         this.mTreasureMapDetails = null;
         this.var_2242 = null;
         this.var_2147 = null;
         this.var_657 = null;
         this.var_750 = null;
         this.var_2003 = null;
         this.var_1297 = null;
         this.var_730 = null;
         this.var_1068 = null;
         this.var_1152 = null;
         this.var_1141 = null;
         this.var_627 = null;
         this.var_806 = null;
         this.var_1930 = null;
         this.var_1847 = null;
         this.var_1210 = null;
         this.var_1261 = null;
         this.var_1665 = null;
         this.var_1694 = null;
         this.var_1531 = null;
         this.mSignetDetails2Desc = null;
         this.mSignetDetails2Stat = null;
         this.mSignetDetails2Desc2Stat = null;
         this.var_1671 = null;
         this.var_1733 = null;
         this.var_1275 = null;
         this.var_2141 = null;
         this.var_1953 = null;
         this.var_701 = null;
         this.var_2275 = null;
         this.mGearEquippedTooltip = null;
         this.var_2416 = null;
         this.var_1788 = null;
         this.var_892 = null;
         this.var_1731 = null;
         this.var_1008 = null;
         this.mCharmTooltip = null;
         this.var_1160 = null;
         this.mCharmTooltipProp1 = null;
         this.mCharmTooltipProp2 = null;
         this.mCharmTooltipProp3 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         if(this.var_1985.mbVisible)
         {
            this.var_1985.Hide(true);
         }
         if(this.mTreasureMapDetails.mbVisible)
         {
            this.mTreasureMapDetails.Hide(true);
         }
         if(this.var_627.mbVisible)
         {
            this.var_627.Hide(true);
         }
         if(this.mCharmTooltip.mbVisible)
         {
            this.mCharmTooltip.Hide(true);
         }
         if(this.var_1152.mbVisible)
         {
            this.var_1152.Hide(true);
         }
         if(this.var_1141.mbVisible)
         {
            this.var_1141.Hide(true);
         }
         if(this.var_701.mbVisible)
         {
            this.var_701.Hide(true);
         }
         if(this.mGearEquippedTooltip.mbVisible)
         {
            this.mGearEquippedTooltip.Hide(true);
         }
         if(this.var_1297.mbVisible)
         {
            this.var_1297.Hide(true);
         }
         if(this.var_730.mbVisible)
         {
            this.var_730.Hide(true);
         }
         if(this.var_1210.mbVisible)
         {
            this.var_1210.Hide(true);
         }
         if(this.var_1275.mbVisible)
         {
            this.var_1275.Hide(true);
         }
         if(this.var_1068.mbVisible)
         {
            this.var_1068.Hide(true);
         }
         if(this.var_1531.mbVisible)
         {
            this.var_1531.Hide(true);
         }
         if(this.mSignetDetails2Desc.mbVisible)
         {
            this.mSignetDetails2Desc.Hide(true);
         }
         if(this.mSignetDetails2Stat.mbVisible)
         {
            this.mSignetDetails2Stat.Hide(true);
         }
         if(this.mSignetDetails2Desc2Stat.mbVisible)
         {
            this.mSignetDetails2Desc2Stat.Hide(true);
         }
         if(this.var_1671.mbVisible)
         {
            this.var_1671.Hide(true);
         }
         if(this.var_1733.mbVisible)
         {
            this.var_1733.Hide(true);
         }
         if(this.var_750.mbVisible)
         {
            this.var_750.Hide(true);
         }
         if(this.var_1261.mbVisible)
         {
            this.var_1261.Hide(true);
         }
      }
      
      public function OnInitDisplay(param1:class_153 = null) : void
      {
         this.ShowBigTooltip(null,true);
      }
      
      public function ShowBigTooltip(param1:class_33, param2:Boolean = false) : void
      {
         var _loc3_:Boolean = param1 != null || param2;
         this.HideTooltip(_loc3_);
         if(param1)
         {
            param1.Show();
         }
         this.var_657 = param1;
      }
      
      public function HideTooltip(param1:Boolean = false) : void
      {
         if(this.var_657)
         {
            if(this.var_657.mbVisible)
            {
               this.var_657.Hide(param1);
            }
         }
         if(this.var_701.mbVisible)
         {
            this.var_701.Hide(param1);
         }
         if(this.mGearEquippedTooltip.mbVisible)
         {
            this.mGearEquippedTooltip.Hide(param1);
         }
      }
      
      private function method_90(param1:class_33) : void
      {
         this.HideTooltip(true);
         if(!param1.mbVisible)
         {
            param1.Show();
         }
         this.var_657 = param1;
      }
      
      public function ShowLockboxTooltip(param1:Number = 0, param2:Number = 0) : void
      {
         var _loc3_:MovieClip = this.var_1210.mMovieClip;
         _loc3_.x = param1;
         _loc3_.y = param2;
         this.method_90(this.var_1210);
      }
      
      public function ShowSimpleTooltip(param1:String, param2:Number = 0, param3:Number = 0) : void
      {
         var _loc4_:MovieClip;
         (_loc4_ = this.var_1068.mMovieClip).x = param2;
         _loc4_.y = param3;
         MathUtil.method_2(_loc4_.am_Name,param1);
         this.method_90(this.var_1068);
      }
      
      public function ShowBasicItemTooltip(param1:String, param2:String, param3:String, param4:Number = 0, param5:Number = 0) : void
      {
         var _loc6_:MovieClip;
         (_loc6_ = this.var_1152.mMovieClip).x = param4;
         _loc6_.y = param5;
         MathUtil.method_8(_loc6_.am_Name,param1,method_37(param3));
         MathUtil.method_2(_loc6_.am_Type,param2);
         this.method_90(this.var_1152);
      }
      
      public function ShowBasicDescriptionTooltip(param1:String, param2:String, param3:String, param4:String, param5:Number = 0, param6:Number = 0) : void
      {
         var _loc7_:MovieClip;
         (_loc7_ = this.var_1141.mMovieClip).x = param5;
         _loc7_.y = param6;
         MathUtil.method_8(_loc7_.am_Name,param1,method_37(param3));
         MathUtil.method_2(_loc7_.am_Type,param2);
         MathUtil.method_2(_loc7_.am_Desc,param4,true);
         this.method_90(this.var_1141);
      }
      
      public function ShowDyeTooltip(param1:class_21, param2:Number = 0, param3:Number = 0) : void
      {
         var _loc6_:class_33 = null;
         var _loc4_:MovieClip;
         (_loc4_ = this.var_1261.mMovieClip).x = param2;
         _loc4_.y = param3;
         var _loc5_:String = param1.var_8;
         MathUtil.method_8(_loc4_.am_Name,param1.displayName,method_37(_loc5_));
         if(_loc5_ == "L")
         {
            _loc6_ = this.var_1694;
            this.var_1665.Hide();
         }
         else
         {
            _loc6_ = this.var_1665;
            this.var_1694.Hide();
         }
         _loc6_.Show();
         this.SkinDyeIcon(param1,_loc6_.mMovieClip.am_DyeSwap);
         this.method_90(this.var_1261);
      }
      
      public function ShowPotionTooltip(param1:class_3, param2:class_103, param3:Number = 0, param4:Number = 0) : void
      {
         var _loc5_:MovieClip;
         (_loc5_ = this.var_1275.mMovieClip).x = param3;
         _loc5_.y = param4;
         MathUtil.method_8(_loc5_.am_Name,param1.displayName,method_37(param1.var_8,class_12.const_205));
         MathUtil.method_2(_loc5_.am_Desc,param1.description,true);
         method_12(this.var_2141.mMovieClip,param1.iconName);
         if(!param2)
         {
            method_14(this.var_1953.mMovieClip);
            MathUtil.method_2(_loc5_.am_NextCount,"");
         }
         else
         {
            method_12(this.var_1953.mMovieClip,param2.consumableType.iconName);
            if(param2.consumableType == param1)
            {
               MathUtil.method_2(_loc5_.am_NextCount,"x" + param2.method_915());
            }
            else
            {
               MathUtil.method_2(_loc5_.am_NextCount,"x" + param2.method_943());
            }
         }
         this.method_90(this.var_1275);
      }
      
      public function ShowMountTooltip(param1:class_20, param2:Number = 0, param3:Number = 0) : void
      {
         var _loc4_:MovieClip;
         (_loc4_ = this.var_750.mMovieClip).x = param2;
         _loc4_.y = param3;
         MathUtil.method_8(_loc4_.am_Name,param1.displayName,method_37(param1.var_255));
         var _loc5_:String = param1.description;
         MathUtil.method_2(_loc4_.am_Desc,_loc5_,true);
         this.method_710(_loc5_,_loc4_.am_UseCase,this.var_2003);
         MathUtil.method_2(_loc4_.am_Type,"Mount");
         MathUtil.method_2(_loc4_.am_UseCase,"Use: Increases movement speed by 40% while mounted");
         this.method_90(this.var_750);
      }
      
      public function ShowConsumableTooltip(param1:class_3, param2:Number = 0, param3:Number = 0, param4:String = null, param5:Boolean = false) : void
      {
         var _loc6_:MovieClip;
         (_loc6_ = this.var_750.mMovieClip).x = param2;
         _loc6_.y = param3;
         if(param4)
         {
            MathUtil.method_8(_loc6_.am_Name,param4,method_37(param1.var_8,class_12.const_205));
         }
         else
         {
            MathUtil.method_8(_loc6_.am_Name,param1.displayName,method_37(param1.var_8,class_12.const_205));
         }
         var _loc7_:String = param1.description;
         MathUtil.method_2(_loc6_.am_Desc,_loc7_,true);
         this.method_710(_loc7_,_loc6_.am_UseCase,this.var_2003);
         var _loc8_:String = param1.method_73();
         MathUtil.method_2(_loc6_.am_Type,_loc8_);
         var _loc9_:String = param1.type;
         if(!param5 && _loc9_ == "Potion" && Boolean(var_1.clientEnt.mCurrPotion))
         {
            _loc9_ = var_1.clientEnt.mNextPotion == param1 ? "Potion_Unequip" : "Potion_Queue";
         }
         else if(!param5 && _loc9_ == "PetFood" && !var_1.mEggPetInfo.mActivePet)
         {
            _loc9_ = "PetFood_NoPet";
         }
         var _loc10_:String = String(class_3.var_477[_loc9_]);
         MathUtil.method_2(_loc6_.am_UseCase,_loc10_,true);
         this.method_90(this.var_750);
      }
      
      private function method_710(param1:String, param2:TextField, param3:class_33) : void
      {
         var _loc4_:uint = 0;
         var _loc9_:String = null;
         if(!param1)
         {
            return;
         }
         var _loc5_:uint = 0;
         var _loc6_:* = false;
         var _loc7_:uint = uint(param1.length);
         var _loc8_:String = "<";
         _loc4_ = 0;
         while(_loc4_ < _loc7_)
         {
            if((_loc9_ = param1.charAt(_loc4_)) == _loc8_)
            {
               _loc8_ = _loc8_ == "<" ? ">" : "<";
               _loc6_ = !_loc6_;
            }
            else if(!_loc6_)
            {
               _loc5_++;
            }
            _loc4_++;
         }
         if(_loc5_ < 52)
         {
            param2.y = 76.65;
            param3.PlayAnimation("Single");
         }
         else if(_loc5_ < 104)
         {
            param2.y = 91.65;
            param3.PlayAnimation("Double");
         }
         else
         {
            param2.y = 112.65;
            param3.PlayAnimation("Triple");
         }
      }
      
      public function ShowPetTooltip(param1:class_87, param2:Boolean = false, param3:Number = 0, param4:Number = 0) : void
      {
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc11_:uint = 0;
         var _loc14_:Number = NaN;
         var _loc15_:int = 0;
         var _loc16_:int = 0;
         var _loc17_:String = null;
         var _loc5_:MovieClip;
         (_loc5_ = this.var_627.mMovieClip).x = param3;
         _loc5_.y = param4;
         var _loc6_:class_7 = param1.mPetType;
         MathUtil.method_8(_loc5_.am_Name,_loc6_.displayName,method_37(_loc6_.var_255));
         var _loc7_:Boolean;
         if(!(_loc7_ = _loc6_.var_1977 || _loc6_.var_1698 || _loc6_.var_2057 || _loc6_.var_2394))
         {
            this.var_1930.PlayAnimation("Single");
         }
         else
         {
            this.var_1930.PlayAnimation("Double");
         }
         var _loc8_:Boolean = false;
         if(param2 || param1 == var_1.mEggPetInfo.mActivePet)
         {
            _loc9_ = _loc10_ = _loc11_ = ScreenArmory.const_106;
            _loc8_ = true;
         }
         else if(var_1.mEggPetInfo.mRestingPetList.indexOf(param1) >= 0)
         {
            _loc10_ = ScreenArmory.const_106;
            _loc9_ = _loc11_ = ScreenArmory.const_9;
         }
         else
         {
            _loc9_ = _loc10_ = _loc11_ = ScreenArmory.const_9;
         }
         var _loc12_:PowerType = class_14.powerTypesDict[_loc6_.var_1138];
         var _loc13_:String = "";
         if(_loc12_)
         {
            _loc13_ = _loc12_.description;
         }
         if(!_loc7_)
         {
            MathUtil.method_8(_loc5_.am_Additional1,"Equip Bonus: " + param1.method_518(_loc8_),_loc10_);
            MathUtil.method_8(_loc5_.am_Additional2,"Use: " + _loc13_,_loc11_);
            MathUtil.method_8(_loc5_.am_Additional3,"",_loc9_);
         }
         else
         {
            MathUtil.method_8(_loc5_.am_Additional1,"Active Bonus: " + param1.method_938(_loc8_),_loc9_);
            MathUtil.method_8(_loc5_.am_Additional2,"Equip Bonus: " + param1.method_518(_loc8_),_loc10_);
            MathUtil.method_8(_loc5_.am_Additional3,"Use: " + _loc13_,_loc11_);
         }
         if(param1 == var_1.mEggPetInfo.mTrainingPet)
         {
            _loc5_.am_XPText.visible = false;
            _loc5_.am_TrainingText.visible = true;
            MathUtil.method_2(_loc5_.am_TrainingText,"Currently training");
            MathUtil.method_2(_loc5_.am_Level,"Level " + param1.var_23);
            this.var_806.BeginHealthMode("Progress",1);
            this.var_806.mHealthPerc = 1;
         }
         else
         {
            _loc5_.am_XPText.visible = true;
            _loc5_.am_TrainingText.visible = false;
            if(param1.var_23 == class_7.const_35)
            {
               this.var_806.Hide();
               MathUtil.method_2(_loc5_.am_Level,"");
               this.var_1847.Show();
               _loc5_.am_XPText.visible = false;
            }
            else
            {
               this.var_806.Show();
               this.var_806.BeginHealthMode("Progress",1);
               _loc14_ = param1.method_324();
               this.var_806.mHealthPerc = _loc14_;
               MathUtil.method_2(_loc5_.am_Level,"Level " + param1.var_23);
               this.var_1847.Hide();
               _loc15_ = param1.var_110 - class_7.method_154(param1.var_23 - 1);
               _loc16_ = int(class_7.method_154(param1.var_23));
               _loc17_ = "";
               if(param1.var_23 != class_7.const_35)
               {
                  _loc17_ = " / " + MathUtil.method_29(_loc16_);
               }
               if(param1.var_110 < _loc16_)
               {
                  MathUtil.method_2(_loc5_.am_XPText,MathUtil.method_29(param1.var_110) + _loc17_);
               }
               else
               {
                  MathUtil.method_2(_loc5_.am_XPText,"<font color=\'#00CCFF\'>" + MathUtil.method_29(param1.var_110) + "</font>" + _loc17_,true);
               }
            }
         }
         this.method_90(this.var_627);
      }
      
      public function ShowGearTooltip(param1:Entity, param2:uint, param3:Boolean = false, param4:class_42 = null, param5:Number = 0, param6:Number = 0) : void
      {
         var _loc8_:class_42 = null;
         var _loc11_:MovieClip = null;
         var _loc12_:class_33 = null;
         var _loc13_:class_33 = null;
         var _loc14_:Vector.<class_33> = null;
         var _loc15_:Vector.<class_33> = null;
         var _loc29_:uint = 0;
         var _loc30_:uint = 0;
         if(!param1)
         {
            return;
         }
         var _loc7_:Array = var_1.mOwnedGear;
         if(param4)
         {
            _loc8_ = param4;
         }
         else
         {
            _loc8_ = _loc7_[param2];
         }
         if(!_loc8_)
         {
            return;
         }
         var _loc9_:EntType = param1.entType;
         var _loc10_:GearType = _loc8_.gearType;
         if(param3)
         {
            _loc29_ = uint(EntType.method_87(_loc10_.type));
            _loc30_ = param1.mEquipGear[_loc29_];
            if(!(_loc8_ = _loc7_[_loc30_]))
            {
               return;
            }
            if(param2 == _loc30_)
            {
               return;
            }
            _loc10_ = _loc8_.gearType;
            _loc14_ = this.var_1008;
            _loc15_ = this.var_1731;
            _loc11_ = this.mGearEquippedTooltip.mMovieClip;
            _loc12_ = this.mGearEquippedTooltip;
            _loc13_ = this.var_2416;
         }
         else
         {
            _loc14_ = this.var_892;
            _loc15_ = this.var_1788;
            _loc11_ = this.var_701.mMovieClip;
            _loc12_ = this.var_701;
            _loc13_ = this.var_2275;
         }
         _loc11_.x = param5;
         _loc11_.y = param6;
         var _loc16_:String = _loc10_.var_8;
         MathUtil.method_8(_loc11_.am_GearName,_loc10_.displayName,method_37(_loc16_));
         MathUtil.method_2(_loc11_.am_GearType,GearType.method_395(_loc9_.className,_loc10_.type));
         var _loc17_:uint = _loc10_.method_377(param1.mExpLevel);
         var _loc18_:uint = _loc10_.method_121("Attack",_loc17_);
         var _loc19_:uint = _loc10_.method_121("Expertise",_loc17_);
         var _loc20_:uint = _loc10_.method_121("Armor",_loc17_);
         var _loc21_:Array = new Array();
         if(_loc18_)
         {
            _loc21_.push("+" + _loc18_ + " Attack");
         }
         if(_loc19_)
         {
            _loc21_.push("+" + _loc19_ + " Expertise");
         }
         if(_loc20_)
         {
            _loc21_.push("+" + _loc20_ + " Defense");
         }
         var _loc22_:uint = 0;
         while(_loc22_ < 3)
         {
            MathUtil.method_2(_loc11_["am_StatLine" + (_loc22_ + 1)],_loc21_[_loc22_]);
            _loc22_++;
         }
         this.method_1120(param1,this,_loc11_,_loc10_,_loc14_);
         method_52(_loc11_.am_ItemIcon,var_1.RenderGear(Game.const_404,_loc10_,0.75,param1,_loc8_.var_295,_loc8_.var_307));
         var _loc23_:MovieClip = _loc15_[0].mMovieClip.am_IconHolder;
         var _loc24_:MovieClip = _loc15_[1].mMovieClip.am_IconHolder;
         var _loc25_:MovieClip = _loc15_[2].mMovieClip.am_IconHolder;
         var _loc26_:class_64 = _loc8_.var_189;
         var _loc27_:class_64 = _loc8_.var_196;
         var _loc28_:class_64 = _loc8_.var_187;
         if(_loc26_)
         {
            _loc26_.method_78(this,_loc23_);
         }
         else
         {
            method_14(_loc23_);
         }
         if(_loc27_)
         {
            _loc27_.method_78(this,_loc24_);
         }
         else
         {
            method_14(_loc24_);
         }
         if(_loc28_)
         {
            _loc28_.method_78(this,_loc25_);
         }
         else
         {
            method_14(_loc25_);
         }
         _loc13_.PlayAnimation(_loc16_);
         if(this.var_657 != this.var_701)
         {
            if(this.var_657 != this.mGearEquippedTooltip)
            {
               this.HideTooltip(true);
            }
         }
         _loc12_.Show();
         this.var_657 = _loc12_;
      }
      
      public function ShowCharmTooltip(param1:class_64, param2:Number = 0, param3:Number = 0) : void
      {
         var _loc4_:MovieClip;
         (_loc4_ = this.mCharmTooltip.mMovieClip).x = param2;
         _loc4_.y = param3;
         var _loc5_:class_1 = param1.var_13;
         var _loc6_:class_1 = param1.method_115();
         if(param1.method_118())
         {
            this.var_1160.PlayAnimation("Triple");
            this.mCharmTooltipProp1.PlayAnimation(_loc5_.var_1321);
            this.mCharmTooltipProp2.PlayAnimation(_loc5_.var_1560);
            this.mCharmTooltipProp3.PlayAnimation(_loc5_.var_1510);
            MathUtil.method_8(_loc4_.am_Name,_loc5_.displayName,ScreenArmory.const_23);
            MathUtil.method_2(_loc4_.am_PrimaryStat,_loc5_.var_1327);
            MathUtil.method_2(_loc4_.am_SecondaryStat,_loc5_.var_1397);
            MathUtil.method_2(_loc4_.am_TertiaryStat,_loc5_.var_1617);
         }
         else if(param1.method_124())
         {
            this.var_1160.PlayAnimation("Double");
            this.mCharmTooltipProp1.PlayAnimation(_loc5_.var_1482);
            this.mCharmTooltipProp2.PlayAnimation(_loc5_.var_1353);
            this.mCharmTooltipProp3.PlayAnimation("Ready");
            MathUtil.method_8(_loc4_.am_Name,_loc5_.displayName,ScreenArmory.const_22);
            MathUtil.method_2(_loc4_.am_PrimaryStat,_loc5_.var_1339);
            MathUtil.method_2(_loc4_.am_SecondaryStat,_loc5_.var_1513);
            MathUtil.method_2(_loc4_.am_TertiaryStat,"");
         }
         else if(!_loc6_)
         {
            this.var_1160.PlayAnimation("Single");
            this.mCharmTooltipProp1.PlayAnimation(_loc5_.var_115);
            this.mCharmTooltipProp2.PlayAnimation("Ready");
            this.mCharmTooltipProp3.PlayAnimation("Ready");
            MathUtil.method_8(_loc4_.am_Name,param1.method_49(),ScreenArmory.const_24);
            MathUtil.method_2(_loc4_.am_PrimaryStat,_loc5_.var_203);
            MathUtil.method_2(_loc4_.am_SecondaryStat,"");
            MathUtil.method_2(_loc4_.am_TertiaryStat,"");
         }
         else
         {
            this.var_1160.PlayAnimation("Double");
            this.mCharmTooltipProp1.PlayAnimation(_loc5_.var_115);
            this.mCharmTooltipProp2.PlayAnimation(_loc6_.var_115);
            this.mCharmTooltipProp3.PlayAnimation("Ready");
            MathUtil.method_2(_loc4_.am_PrimaryStat,_loc5_.var_203);
            MathUtil.method_2(_loc4_.am_SecondaryStat,param1.method_171());
            MathUtil.method_2(_loc4_.am_TertiaryStat,"");
            if(param1.var_8 == class_64.const_341)
            {
               MathUtil.method_8(_loc4_.am_Name,param1.method_49(),ScreenArmory.const_22);
            }
            else if(param1.var_8 == class_64.const_312)
            {
               MathUtil.method_8(_loc4_.am_Name,param1.method_49(),ScreenArmory.const_23);
            }
         }
         this.method_90(this.mCharmTooltip);
      }
      
      public function ShowSpellbookTooltip(param1:Entity, param2:PowerType, param3:class_10, param4:Number = 0, param5:Number = 0) : void
      {
         var _loc10_:* = false;
         var _loc6_:MovieClip = this.var_730.mMovieClip;
         var _loc7_:class_10;
         var _loc8_:Boolean = (Boolean(_loc7_ = var_1.mAbilityBook.mAbilityResearch)) && _loc7_.abilityName == param3.abilityName;
         var _loc9_:Boolean;
         if(_loc9_ = !param3.var_223 && Boolean(var_1.mAbilityBook.IsTrained(param3)) || param3.var_223 && param1.var_85.method_245() >= param3.var_90)
         {
            MathUtil.method_2(_loc6_.am_Notice,"");
            _loc10_ = param1.hudPowers[param3.var_90] == param2;
            if(!param3.var_223)
            {
               if(_loc10_)
               {
                  MathUtil.method_2(_loc6_.am_UseCase,"Equipped");
               }
               else
               {
                  MathUtil.method_2(_loc6_.am_UseCase,"Click to equip this ability");
               }
            }
            else if(_loc10_)
            {
               MathUtil.method_2(_loc6_.am_UseCase,"This ability is automatically equipped");
            }
            else
            {
               MathUtil.method_2(_loc6_.am_UseCase,"Requires " + Game.method_226(param3.className) + " discipline");
            }
         }
         else if(Boolean(_loc7_) && param3.abilityName == _loc7_.abilityName)
         {
            MathUtil.method_2(_loc6_.am_Notice,"");
            MathUtil.method_2(_loc6_.am_UseCase,"Currently training");
         }
         else
         {
            if(!param3.var_223)
            {
               MathUtil.method_2(_loc6_.am_Notice,"Train this ability at your Tome of Power");
            }
            else
            {
               MathUtil.method_2(_loc6_.am_Notice,"Learn this ability in your Talent Tree");
            }
            MathUtil.method_2(_loc6_.am_UseCase,"");
         }
         this.method_459(this.var_730,param1,param2,const_547,false,param4,param5);
      }
      
      public function ShowTalentAbilityTooltip(param1:Entity, param2:PowerType, param3:String, param4:Number = 0, param5:Number = 0) : void
      {
         var _loc6_:MovieClip = this.var_730.mMovieClip;
         MathUtil.method_2(_loc6_.am_Notice,param3);
         MathUtil.method_2(_loc6_.am_UseCase,"");
         this.method_459(this.var_730,param1,param2,const_547,false,param4,param5);
      }
      
      public function ShowTalentstoneTooltip(param1:class_17, param2:uint = 1, param3:Number = 0, param4:Number = 0) : void
      {
         var _loc6_:class_33 = null;
         if(!param1)
         {
            return;
         }
         var _loc5_:Array;
         if(!(_loc5_ = param1.description))
         {
            return;
         }
         var _loc7_:* = _loc5_.length > 2;
         var _loc8_:*;
         if(_loc8_ = _loc5_[0].length > 52)
         {
            _loc6_ = _loc7_ ? this.mSignetDetails2Desc2Stat : this.mSignetDetails2Desc;
         }
         else
         {
            _loc6_ = _loc7_ ? this.mSignetDetails2Desc : this.var_1531;
         }
         var _loc9_:MovieClip;
         (_loc9_ = _loc6_.mMovieClip).x = param3;
         _loc9_.y = param4;
         switch(_loc5_.length)
         {
            case 3:
               class_83.method_751(_loc9_.am_Desc3,_loc5_[2],param2);
            case 2:
               class_83.method_751(_loc9_.am_Desc2,_loc5_[1],param2);
            case 1:
               MathUtil.method_2(_loc9_.am_Desc,_loc5_[0]);
         }
         MathUtil.method_2(_loc9_.am_Name,param1.displayName + " Talentstone");
         MathUtil.method_2(_loc9_.am_PointsRequired,"");
         this.method_90(_loc6_);
      }
      
      public function ShowPowerTooltip(param1:Entity, param2:PowerType, param3:Number = 0, param4:Number = 0, param5:uint = 0, param6:Boolean = false) : void
      {
         var _loc7_:class_87 = null;
         var _loc8_:class_20 = null;
         if(!param1 || !param2)
         {
            return;
         }
         if(param2.var_749)
         {
            if(param2 == PowerType.var_836)
            {
               this.ShowBasicDescriptionTooltip("Dismiss","Pet","M","Dismisses your pet from the battle field",param3,param4);
            }
            else if(_loc7_ = !!param1 ? param1.mEquipPet : null)
            {
               this.ShowPetTooltip(_loc7_,false,param3,param4);
            }
         }
         else if(param2 == PowerType.var_824)
         {
            this.ShowBasicDescriptionTooltip("Dismount","Mount","M","Hop off of your majestic mount",param3,param4);
         }
         else if(param2.var_1439)
         {
            if(_loc8_ = !!param1 ? param1.mEquipMount : null)
            {
               this.ShowMountTooltip(_loc8_,param3,param4);
            }
         }
         else
         {
            this.method_459(this.var_1297,param1,param2,param5,param6,param3,param4);
         }
      }
      
      private function method_459(param1:class_33, param2:Entity, param3:PowerType, param4:uint, param5:Boolean, param6:Number = 0, param7:Number = 0) : void
      {
         var _loc12_:uint = 0;
         var _loc13_:uint = 0;
         var _loc8_:MovieClip;
         (_loc8_ = param1.mMovieClip).x = param6;
         _loc8_.y = param7;
         var _loc9_:uint;
         var _loc10_:String = (_loc9_ = uint(param3.var_7)) < 5 ? "M" : (_loc9_ < 10 ? "R" : "L");
         var _loc11_:class_10;
         if(!(_loc11_ = class_14.var_704[param3.basePowerName]))
         {
            MathUtil.method_8(_loc8_.am_Name,param3.displayName,method_37(_loc10_));
         }
         else if(!(_loc12_ = uint(var_1.mAbilityBook.GetCurrRankByAbilityID(_loc11_.abilityID))))
         {
            if(_loc9_ == 1)
            {
               MathUtil.method_8(_loc8_.am_Name,param3.displayName + " (Available for training)",method_37(_loc10_));
            }
            else
            {
               MathUtil.method_8(_loc8_.am_Name,param3.displayName,ScreenArmory.const_9);
            }
         }
         else if(_loc9_ <= _loc12_)
         {
            MathUtil.method_8(_loc8_.am_Name,param3.displayName,method_37(_loc10_));
         }
         else if(_loc9_ == _loc12_ + 1)
         {
            MathUtil.method_8(_loc8_.am_Name,param3.displayName + " (Available for training)",method_37(_loc10_));
         }
         else
         {
            MathUtil.method_8(_loc8_.am_Name,param3.displayName,ScreenArmory.const_9);
         }
         if(_loc9_)
         {
            MathUtil.method_8(_loc8_.am_Type,"Rank " + _loc9_,ScreenArmory.const_106);
         }
         else if(param3 == PowerType.var_824)
         {
            MathUtil.method_8(_loc8_.am_Type,"Mount",ScreenArmory.const_106);
         }
         else if(param4 == const_573)
         {
            MathUtil.method_8(_loc8_.am_Type,"Toggle",ScreenArmory.const_106);
         }
         else if(param4 == const_825)
         {
            MathUtil.method_8(_loc8_.am_Type,"Discipline Ability",ScreenArmory.const_106);
         }
         else
         {
            MathUtil.method_8(_loc8_.am_Type,"Untrained",ScreenArmory.const_9);
         }
         if(!param5)
         {
            MathUtil.method_2(_loc8_.am_Desc,param3.method_349(param2));
         }
         else
         {
            MathUtil.method_2(_loc8_.am_Desc,param3.method_349(param2,null,true,var_1.mAbilityBook,param2.var_18),true);
         }
         if(param3.var_219)
         {
            if(param3.var_535 > param3.manaCost)
            {
               MathUtil.method_2(_loc8_.am_Additional,"Discipline Mana Required: " + param3.var_535);
            }
            else if(param3.manaCost == 0)
            {
               if(_loc13_ = param3.coolDownTime / 1000)
               {
                  MathUtil.method_2(_loc8_.am_Additional,"Cooldown: " + _loc13_ + " seconds");
               }
               else
               {
                  MathUtil.method_2(_loc8_.am_Additional,"Instant");
               }
            }
            else
            {
               MathUtil.method_2(_loc8_.am_Additional,"Discipline Mana Cost: " + param3.manaCost);
            }
         }
         else if(param3.var_535 > param3.manaCost)
         {
            MathUtil.method_2(_loc8_.am_Additional,"Mana Required: " + param3.var_535);
         }
         else if(param3.manaCost == 0)
         {
            MathUtil.method_2(_loc8_.am_Additional,"");
         }
         else
         {
            MathUtil.method_2(_loc8_.am_Additional,"Mana Cost: " + param3.manaCost);
         }
         this.method_90(param1);
      }
      
      private function method_1120(param1:Entity, param2:class_32, param3:MovieClip, param4:GearType, param5:Vector.<class_33>) : void
      {
         var _loc14_:String = null;
         var _loc15_:class_17 = null;
         var _loc16_:String = null;
         var _loc17_:String = null;
         var _loc18_:String = null;
         var _loc6_:PowerType = !!param4.var_1062 ? param1.method_1677(param4.var_1062) : null;
         var _loc7_:MagicType = !!param4.var_1197 ? class_14.magicTypesDict[param4.var_1197] : null;
         var _loc8_:PowerType = !!param4.var_100 ? class_14.powerTypesDict[param4.var_100] : null;
         var _loc9_:MovieClip = param5[const_523].mMovieClip;
         var _loc10_:MovieClip = param5[const_436].mMovieClip;
         var _loc11_:MovieClip = param5[RUNESLOT_PROC1].mMovieClip;
         var _loc12_:MovieClip = param5[RUNESLOT_PROC2].mMovieClip;
         if(!_loc6_)
         {
            MathUtil.method_2(param3.am_PowerTypeName,"");
            _loc9_.am_ButtonHolder.am_Button.removeChildren();
            _loc9_.visible = false;
            _loc11_.y = const_660 + const_326;
            param3.am_ProcTypeName1.y = const_660;
            _loc12_.y = const_388 + const_326;
            param3.am_ProcTypeName2.y = const_388;
         }
         else
         {
            _loc14_ = "Rune" + _loc6_.powerName;
            _loc15_ = class_14.var_274[_loc14_];
            _loc16_ = "-";
            if(Boolean(_loc15_) && Boolean(_loc15_.description))
            {
               _loc16_ = String(_loc15_.description[0]);
            }
            MathUtil.method_2(param3.am_PowerTypeName,_loc16_);
            param2.method_12(_loc9_.am_ButtonHolder.am_Button,_loc6_.iconName);
            _loc9_.visible = true;
            _loc11_.y = const_388 + const_326;
            param3.am_ProcTypeName1.y = const_388;
            _loc12_.y = const_653 + const_326;
            param3.am_ProcTypeName2.y = const_653;
         }
         _loc10_.visible = false;
         if(!_loc7_)
         {
            MathUtil.method_2(param3.am_MagicTypeName,"");
            _loc10_.am_RuneHolder.removeChildren();
         }
         else
         {
            _loc17_ = this.method_821(1,_loc7_.description);
            _loc18_ = this.method_821(2,_loc7_.description);
            MathUtil.method_2(param3.am_MagicTypeLine1,_loc17_);
            MathUtil.method_2(param3.am_MagicTypeLine2,_loc18_);
            param2.method_12(_loc10_.am_RuneHolder,_loc7_.runeIcon);
         }
         if(!_loc8_)
         {
            MathUtil.method_2(param3.am_ProcTypeName1,"");
            _loc11_.am_RuneHolder.removeChildren();
         }
         else
         {
            MathUtil.method_2(param3.am_ProcTypeName1,_loc8_.method_349(param1));
            param2.method_12(_loc11_.am_RuneHolder,_loc8_.runeIcon);
         }
         if(!(!!param4.procRune2 ? class_14.powerTypesDict[param4.procRune2] : null))
         {
            MathUtil.method_2(param3.am_ProcTypeName2,"");
            _loc12_.am_RuneHolder.removeChildren();
            _loc12_.visible = false;
         }
         else
         {
            MathUtil.method_2(param3.am_ProcTypeName2,null.method_349(param1));
            param2.method_12(_loc12_.am_RuneHolder,null.runeIcon);
            _loc12_.visible = true;
         }
      }
      
      public function SkinEquipmentIcon(param1:GearType, param2:class_33) : void
      {
         var _loc3_:MovieClip = param2.mMovieClip;
         var _loc4_:MovieClip = _loc3_.am_IconHolder.am_Button;
         if(!param1)
         {
            method_14(_loc4_);
            _loc3_.am_RarityMagic.visible = false;
            _loc3_.am_RarityRare.visible = false;
            _loc3_.am_RarityLegendary.visible = false;
            _loc3_.am_IconHolder.visible = false;
            return;
         }
         var _loc5_:SuperAnimInstance = var_1.RenderGear(Game.const_95,param1,0.43);
         _loc3_.am_IconHolder.visible = true;
         method_52(_loc4_,_loc5_);
         var _loc6_:String;
         if((_loc6_ = param1.var_8) == "M")
         {
            _loc3_.am_RarityMagic.visible = true;
            _loc3_.am_RarityRare.visible = false;
            _loc3_.am_RarityLegendary.visible = false;
         }
         else if(_loc6_ == "R")
         {
            _loc3_.am_RarityMagic.visible = false;
            _loc3_.am_RarityRare.visible = true;
            _loc3_.am_RarityLegendary.visible = false;
         }
         else
         {
            _loc3_.am_RarityMagic.visible = false;
            _loc3_.am_RarityRare.visible = false;
            _loc3_.am_RarityLegendary.visible = true;
         }
      }
      
      private function method_558(param1:MovieClip) : Vector.<uint>
      {
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:GraphicsSolidFill = null;
         var _loc2_:Vector.<uint> = new Vector.<uint>(const_1007,true);
         var _loc3_:Vector.<IGraphicsData> = param1.graphics.readGraphicsData();
         var _loc4_:uint = 0;
         var _loc8_:uint = _loc3_.length;
         _loc5_ = 0;
         for(; _loc5_ < _loc8_; _loc5_++)
         {
            if(_loc7_ = _loc3_[_loc5_] as GraphicsSolidFill)
            {
               if(_loc4_ == 3)
               {
                  break;
               }
               if((_loc6_ = _loc7_.color) == 14352384)
               {
                  _loc2_[const_793] = _loc5_;
                  _loc4_++;
               }
               else if(_loc6_ == 16734039)
               {
                  _loc2_[const_583] = _loc5_;
                  _loc4_++;
               }
               else if(_loc6_ == 7798784)
               {
                  _loc2_[const_696] = _loc5_;
                  _loc4_++;
                  continue;
               }
            }
         }
         return _loc2_;
      }
      
      public function SkinDyeIcon(param1:class_21, param2:MovieClip) : void
      {
         var _loc3_:Vector.<IGraphicsData> = param2.graphics.readGraphicsData();
         var _loc4_:Vector.<uint> = param1.var_8 == "L" ? this.var_2147 : this.var_2242;
         (_loc3_[_loc4_[const_793]] as GraphicsSolidFill).color = param1.color;
         (_loc3_[_loc4_[const_583]] as GraphicsSolidFill).color = param1.var_935;
         (_loc3_[_loc4_[const_696]] as GraphicsSolidFill).color = param1.var_209;
         param2.removeChildren();
         param2.graphics.clear();
         param2.graphics.drawGraphicsData(_loc3_);
      }
      
      private function method_821(param1:int, param2:String) : String
      {
         var _loc3_:Array = param2.split(", ");
         if(param1 - 1 < _loc3_.length && param1 - 1 >= 0)
         {
            return _loc3_[param1 - 1];
         }
         return "";
      }
   }
}
