package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   
   public class class_107 extends class_32
   {
      
      private static const const_41:uint = 15;
      
      private static const const_265:Number = 669.4;
      
      private static const const_280:Number = 491.35;
      
      public static const const_736:Number = 20;
       
      
      public var mbFromLockBox:Boolean;
      
      private var var_482:Vector.<class_12>;
      
      private var var_2149:class_138;
      
      private var var_869:Vector.<class_138>;
      
      private var var_1089:Vector.<class_33>;
      
      private var var_1312:Vector.<class_33>;
      
      private var var_1163:Vector.<class_33>;
      
      private var var_1249:Vector.<class_33>;
      
      private var var_837:Vector.<class_138>;
      
      private var var_1524:Vector.<class_138>;
      
      private var var_1038:Vector.<class_33>;
      
      public var mTempOwnedChangeLog:Vector.<Boolean>;
      
      public function class_107(param1:Game)
      {
         super(param1,"a_ScreenRoyalSigilStore",null);
         var_15 = true;
      }
      
      public static function method_484(param1:class_12) : String
      {
         var _loc3_:class_3 = null;
         var _loc2_:String = param1.type;
         if(_loc2_ == "RespecStone" || _loc2_ == "CharmRemover")
         {
            _loc2_ = "Charm";
         }
         else if(_loc2_ == "Consumable")
         {
            _loc3_ = class_14.var_303[param1.var_257];
            _loc2_ = _loc3_.method_73();
         }
         return _loc2_;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:uint = 0;
         this.var_869 = new Vector.<class_138>(const_41,true);
         this.var_1312 = new Vector.<class_33>(const_41,true);
         this.var_1163 = new Vector.<class_33>(const_41,true);
         this.var_837 = new Vector.<class_138>(const_41,true);
         this.var_1038 = new Vector.<class_33>(const_41,true);
         this.var_1089 = new Vector.<class_33>(const_41,true);
         this.var_1249 = new Vector.<class_33>(const_41,true);
         this.var_1524 = new Vector.<class_138>(const_41,true);
         this.mTempOwnedChangeLog = new Vector.<Boolean>(const_41,true);
         _loc1_ = 0;
         while(_loc1_ < const_41)
         {
            this.var_869[_loc1_] = method_21(var_2["am_Cost" + _loc1_] as TextField);
            this.var_1163[_loc1_] = method_1(var_2["am_MouseOver" + _loc1_] as MovieClip);
            this.var_1038[_loc1_] = method_1(var_2["am_Icon" + _loc1_] as MovieClip);
            this.var_837[_loc1_] = method_21(var_2["am_Name" + _loc1_] as TextField);
            this.var_1089[_loc1_] = method_1(var_2["am_CostIcon" + _loc1_] as MovieClip);
            this.var_1312[_loc1_] = method_3(var_2["am_Contact" + _loc1_] as MovieClip,_loc1_,this.method_1212,this.method_549,this.HideTooltip);
            this.var_1249[_loc1_] = method_1(var_2["am_SoldIcon" + _loc1_] as MovieClip);
            this.var_1524[_loc1_] = method_21(var_2["am_Type" + _loc1_] as TextField);
            _loc1_++;
         }
         this.var_2149 = method_92(var_2.am_OwnedSigilCount);
         method_10(var_2.am_Close,this.method_1248);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.method_847();
         this.var_869 = null;
         this.var_837 = null;
         this.var_1038 = null;
         this.var_1163 = null;
         this.var_1312 = null;
         this.var_482 = null;
         this.var_1089 = null;
         this.var_2149 = null;
         this.var_1249 = null;
         this.var_1524 = null;
      }
      
      override public function Hide() : void
      {
         this.method_847();
         super.Hide();
      }
      
      private function method_847() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:MovieClip = null;
         _loc1_ = 0;
         while(_loc1_ < const_41)
         {
            _loc2_ = this.var_1038[_loc1_].mMovieClip.am_MaskIconHolder;
            method_14(_loc2_);
            _loc1_++;
         }
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:uint = 0;
         var _loc3_:class_12 = null;
         var _loc4_:String = null;
         var _loc5_:class_33 = null;
         var _loc6_:MovieClip = null;
         var _loc7_:MovieClip = null;
         var _loc8_:String = null;
         var _loc9_:TextField = null;
         var _loc10_:class_20 = null;
         var _loc11_:class_7 = null;
         var _loc12_:class_3 = null;
         var _loc2_:uint = this.var_482.length;
         _loc1_ = 0;
         while(_loc1_ < const_41)
         {
            if(_loc1_ < _loc2_)
            {
               _loc3_ = this.var_482[_loc1_];
               if(this.method_723(_loc3_) || this.mTempOwnedChangeLog[_loc1_])
               {
                  this.var_1249[_loc1_].Show();
                  this.var_1312[_loc1_].Hide();
               }
               else
               {
                  this.var_1249[_loc1_].Hide();
                  this.var_1312[_loc1_].Show();
               }
               _loc6_ = (_loc5_ = this.var_1038[_loc1_]).mMovieClip.am_ItemIconHolder;
               _loc7_ = _loc5_.mMovieClip.am_MaskIconHolder;
               switch(_loc3_.type)
               {
                  case class_12.const_279:
                     _loc4_ = (_loc10_ = class_14.var_362[_loc3_.var_257]).var_255;
                     _loc6_.visible = false;
                     method_14(_loc7_);
                     _loc7_.addChild(class_41.method_168(_loc10_,0,0,58,58,var_1.main.overallScale));
                     _loc7_.visible = true;
                     MathUtil.method_8(this.var_837[_loc1_].mTextField,_loc10_.displayName,class_101.method_37(_loc4_,_loc3_.type));
                     break;
                  case class_12.include:
                     _loc4_ = (_loc11_ = class_14.var_233[_loc3_.var_257]).var_255;
                     _loc6_.visible = false;
                     method_14(_loc7_);
                     _loc7_.addChild(class_41.method_85(_loc11_,0,0,58,58,var_1.main.overallScale));
                     _loc7_.visible = true;
                     MathUtil.method_8(this.var_837[_loc1_].mTextField,_loc11_.displayName,class_101.method_37(_loc4_,_loc3_.type));
                     break;
                  case class_12.const_205:
                     _loc4_ = (_loc12_ = class_14.var_303[_loc3_.var_257]).var_8;
                     _loc7_.visible = false;
                     method_12(_loc6_,_loc3_.iconName);
                     _loc6_.visible = true;
                     MathUtil.method_8(this.var_837[_loc1_].mTextField,_loc3_.displayName,class_101.method_37(_loc4_,_loc3_.type));
                     break;
                  default:
                     _loc4_ = "M";
                     _loc7_.visible = false;
                     method_12(_loc6_,_loc3_.iconName);
                     _loc6_.visible = true;
                     MathUtil.method_8(this.var_837[_loc1_].mTextField,_loc3_.displayName,class_101.method_37(_loc4_,_loc3_.type));
               }
               this.var_1038[_loc1_].Show();
               _loc8_ = method_484(_loc3_);
               this.var_1524[_loc1_].SetText(_loc8_);
               this.var_869[_loc1_].SetText(String(_loc3_.var_795));
               _loc9_ = this.var_869[_loc1_].mTextField;
               if(_loc3_.var_795 > var_1.mLockboxData.mRoyalSigils)
               {
                  _loc9_.textColor = ScreenArmory.const_137;
               }
               else
               {
                  _loc9_.textColor = ScreenArmory.const_24;
               }
               this.var_869[_loc1_].TickTextField();
               this.var_1089[_loc1_].mMovieClip.x = _loc9_.x + _loc9_.width - _loc9_.textWidth - const_736;
               this.var_1089[_loc1_].Show();
            }
            else
            {
               this.var_869[_loc1_].SetText("");
               this.var_837[_loc1_].SetText("");
               this.var_1089[_loc1_].Hide();
               this.var_1038[_loc1_].Hide();
               this.var_1524[_loc1_].SetText("");
               this.var_1249[_loc1_].Hide();
            }
            _loc1_++;
         }
         this.var_2149.var_213 = var_1.mLockboxData.mRoyalSigils;
      }
      
      public function OnInitDisplay() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc3_:class_12 = null;
         if(var_1.screenMenu.mbVisible)
         {
            var_1.screenMenu.Hide();
         }
         this.mbFromLockBox = false;
         if(!this.var_482)
         {
            this.var_482 = new Vector.<class_12>();
            _loc2_ = class_14.var_1626.length;
            _loc1_ = 1;
            while(_loc1_ < _loc2_)
            {
               _loc3_ = class_14.var_1626[_loc1_];
               if(_loc3_)
               {
                  this.var_482.push(_loc3_);
               }
               _loc1_++;
            }
         }
         _loc1_ = 0;
         while(_loc1_ < const_41)
         {
            this.mTempOwnedChangeLog[_loc1_] = false;
            _loc1_++;
         }
         this.method_1709();
         this.HideTooltip();
         if(!(var_1.mAlertState & Game.const_443))
         {
            var_1.UpdateAlert(Game.const_443);
         }
         if(var_1.mTutorialStage == Game.const_287 || var_1.mTutorialStage == Game.const_230 || var_1.mTutorialStage == Game.const_302)
         {
            var_1.SetNewTutorialStage(Game.const_410);
         }
      }
      
      private function method_1709() : void
      {
         var _loc1_:uint = 0;
         _loc1_ = 0;
         while(_loc1_ < const_41)
         {
            this.var_1163[_loc1_].Hide();
            _loc1_++;
         }
      }
      
      private function method_1212(param1:MouseEvent, param2:uint) : void
      {
         if(!var_1.clientEnt)
         {
            return;
         }
         if(param2 >= this.var_482.length)
         {
            return;
         }
         var _loc3_:class_12 = this.var_482[param2];
         if(this.method_723(_loc3_))
         {
            return;
         }
         var _loc4_:uint = _loc3_.var_795;
         if(!_loc3_.var_1579 && var_1.mLockboxData.mRoyalSigils < _loc4_)
         {
            return;
         }
         if(_loc3_.var_1579 && var_1.clientEnt.currGold < _loc4_)
         {
            return;
         }
         mbHideOnClear = false;
         var_1.screenRoyalSigilStore.mbHideOnClear = false;
         var_1.screenRoyalSigilStorePrompt.Display(_loc3_,param2);
         mbHideOnClear = true;
         var_1.screenRoyalSigilStore.mbHideOnClear = true;
         var_1.screenHudTooltip.HideTooltip(true);
      }
      
      private function method_549(param1:MouseEvent, param2:uint) : void
      {
         var _loc5_:class_20 = null;
         var _loc6_:class_7 = null;
         var _loc7_:class_87 = null;
         var _loc8_:class_1 = null;
         var _loc9_:class_64 = null;
         var _loc10_:class_3 = null;
         if(param2 >= this.var_482.length)
         {
            return;
         }
         var _loc3_:class_12 = this.var_482[param2];
         var _loc4_:String = _loc3_.type;
         switch(_loc4_)
         {
            case class_12.const_279:
               _loc5_ = class_14.var_362[_loc3_.var_257];
               var_1.screenHudTooltip.ShowMountTooltip(_loc5_,const_265,const_280);
               break;
            case class_12.include:
               _loc6_ = class_14.var_233[_loc3_.var_257];
               _loc7_ = new class_87(var_1,_loc6_,1,0,0);
               var_1.screenHudTooltip.ShowPetTooltip(_loc7_,true,const_265,const_280);
               _loc7_.method_1460();
               break;
            default:
               if(_loc4_ == "RespecStone")
               {
                  _loc8_ = class_14.var_142["RespecStone"];
                  _loc9_ = new class_64(_loc8_);
                  var_1.screenHudTooltip.ShowCharmTooltip(_loc9_,const_265,const_280);
                  break;
               }
               if(_loc4_ == "CharmRemover")
               {
                  _loc8_ = class_14.var_142["CharmRemover"];
                  _loc9_ = new class_64(_loc8_);
                  var_1.screenHudTooltip.ShowCharmTooltip(_loc9_,const_265,const_280);
                  break;
               }
               if(_loc10_ = class_14.var_303[_loc3_.var_257])
               {
                  var_1.screenHudTooltip.ShowConsumableTooltip(_loc10_,const_265,const_280,_loc3_.displayName,true);
               }
               break;
         }
         this.var_1163[param2].Show();
      }
      
      private function HideTooltip(param1:MouseEvent = null, param2:uint = 0) : void
      {
         if(param2 < this.var_482.length)
         {
            this.var_1163[param2].Hide();
         }
         var_1.screenHudTooltip.HideTooltip();
      }
      
      private function method_723(param1:class_12) : Boolean
      {
         var _loc2_:class_20 = null;
         var _loc3_:class_7 = null;
         if(param1.var_2505)
         {
            if(param1.type == class_12.const_279)
            {
               _loc2_ = class_14.var_362[param1.var_257];
               if(var_1.mOwnedMounts[_loc2_.var_197])
               {
                  return true;
               }
            }
            else if(param1.type == class_12.include)
            {
               _loc3_ = class_14.var_233[param1.var_257];
               if(var_1.mEggPetInfo.mOwnedPetsHash[_loc3_.var_104])
               {
                  return true;
               }
            }
         }
         return false;
      }
      
      public function method_1248(param1:MouseEvent = null) : void
      {
         this.Hide();
         if(this.mbFromLockBox)
         {
            var_1.screenLockBox.Display();
         }
         this.mbFromLockBox = false;
      }
   }
}
