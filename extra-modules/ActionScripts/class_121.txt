package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   
   public class class_121 extends class_32
   {
      
      private static const const_265:uint = 173;
      
      private static const const_280:uint = 46;
       
      
      public var var_1969:Boolean;
      
      private var var_972:Boolean;
      
      private var var_955:uint;
      
      private var var_334:int;
      
      private var var_1771:class_33;
      
      private var var_1252:Vector.<class_33>;
      
      private var var_1538:Vector.<class_33>;
      
      private var var_650:Vector.<class_33>;
      
      private var var_503:Vector.<class_33>;
      
      private var var_75:Vector.<Vector.<class_21>>;
      
      private var var_202:class_21;
      
      private var var_204:class_21;
      
      private var var_185:Vector.<Vector.<class_33>>;
      
      private var var_2067:class_33;
      
      private var var_2205:class_33;
      
      private var var_558:Vector.<Vector.<class_33>>;
      
      private var var_1464:class_33;
      
      private var var_1647:class_33;
      
      private var var_1408:class_138;
      
      private var var_1437:class_33;
      
      public function class_121(param1:Game)
      {
         super(param1,"a_DyeWindow",null);
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc14_:uint = 0;
         var _loc15_:MovieClip = null;
         var _loc1_:uint = EntType.MAX_SLOTS;
         this.var_503 = new Vector.<class_33>(_loc1_,true);
         this.var_503[EntType.SWORD_SLOT] = method_3(var_2.am_Sword,EntType.SWORD_SLOT,null);
         this.var_503[EntType.SHIELD_SLOT] = method_3(var_2.am_Shield,EntType.SHIELD_SLOT,null);
         this.var_503[EntType.HAT_SLOT] = method_3(var_2.am_Hat,EntType.HAT_SLOT,null);
         this.var_503[EntType.ARMOR_SLOT] = method_3(var_2.am_Armor,EntType.ARMOR_SLOT,null);
         this.var_503[EntType.GLOVES_SLOT] = method_3(var_2.am_Gloves,EntType.GLOVES_SLOT,null);
         this.var_503[EntType.BOOTS_SLOT] = method_3(var_2.am_Boots,EntType.BOOTS_SLOT,null);
         this.var_185 = new Vector.<Vector.<class_33>>(_loc1_,true);
         this.var_558 = new Vector.<Vector.<class_33>>(_loc1_,true);
         var _loc2_:Vector.<class_33> = new Vector.<class_33>(2,true);
         _loc2_[0] = method_3(var_2.am_Sword1,EntType.SWORD_SLOT * _loc1_ + 0,this.method_96,this.method_86,this.method_88);
         _loc2_[1] = method_3(var_2.am_Sword2,EntType.SWORD_SLOT * _loc1_ + 1,this.method_96,this.method_86,this.method_88);
         this.var_185[EntType.SWORD_SLOT] = _loc2_;
         var _loc3_:Vector.<class_33> = new Vector.<class_33>(2,true);
         _loc3_[0] = method_1(var_2["am_ApplyAnim" + 0] as MovieClip);
         _loc3_[1] = method_1(var_2["am_ApplyAnim" + 1] as MovieClip);
         this.var_558[EntType.SWORD_SLOT] = _loc3_;
         var _loc4_:Vector.<class_33>;
         (_loc4_ = new Vector.<class_33>(2,true))[0] = method_3(var_2.am_Shield1,EntType.SHIELD_SLOT * _loc1_ + 0,this.method_96,this.method_86,this.method_88);
         _loc4_[1] = method_3(var_2.am_Shield2,EntType.SHIELD_SLOT * _loc1_ + 1,this.method_96,this.method_86,this.method_88);
         this.var_185[EntType.SHIELD_SLOT] = _loc4_;
         var _loc5_:Vector.<class_33>;
         (_loc5_ = new Vector.<class_33>(2,true))[0] = method_1(var_2["am_ApplyAnim" + 2] as MovieClip);
         _loc5_[1] = method_1(var_2["am_ApplyAnim" + 3] as MovieClip);
         this.var_558[EntType.SHIELD_SLOT] = _loc5_;
         var _loc6_:Vector.<class_33>;
         (_loc6_ = new Vector.<class_33>(2,true))[0] = method_3(var_2.am_Hat1,EntType.HAT_SLOT * _loc1_ + 0,this.method_96,this.method_86,this.method_88);
         _loc6_[1] = method_3(var_2.am_Hat2,EntType.HAT_SLOT * _loc1_ + 1,this.method_96,this.method_86,this.method_88);
         this.var_185[EntType.HAT_SLOT] = _loc6_;
         var _loc7_:Vector.<class_33>;
         (_loc7_ = new Vector.<class_33>(2,true))[0] = method_1(var_2["am_ApplyAnim" + 4] as MovieClip);
         _loc7_[1] = method_1(var_2["am_ApplyAnim" + 5] as MovieClip);
         this.var_558[EntType.HAT_SLOT] = _loc7_;
         var _loc8_:Vector.<class_33>;
         (_loc8_ = new Vector.<class_33>(2,true))[0] = method_3(var_2.am_Armor1,EntType.ARMOR_SLOT * _loc1_ + 0,this.method_96,this.method_86,this.method_88);
         _loc8_[1] = method_3(var_2.am_Armor2,EntType.ARMOR_SLOT * _loc1_ + 1,this.method_96,this.method_86,this.method_88);
         this.var_185[EntType.ARMOR_SLOT] = _loc8_;
         var _loc9_:Vector.<class_33>;
         (_loc9_ = new Vector.<class_33>(2,true))[0] = method_1(var_2["am_ApplyAnim" + 6] as MovieClip);
         _loc9_[1] = method_1(var_2["am_ApplyAnim" + 7] as MovieClip);
         this.var_558[EntType.ARMOR_SLOT] = _loc9_;
         var _loc10_:Vector.<class_33>;
         (_loc10_ = new Vector.<class_33>(2,true))[0] = method_3(var_2.am_Gloves1,EntType.GLOVES_SLOT * _loc1_ + 0,this.method_96,this.method_86,this.method_88);
         _loc10_[1] = method_3(var_2.am_Gloves2,EntType.GLOVES_SLOT * _loc1_ + 1,this.method_96,this.method_86,this.method_88);
         this.var_185[EntType.GLOVES_SLOT] = _loc10_;
         var _loc11_:Vector.<class_33>;
         (_loc11_ = new Vector.<class_33>(2,true))[0] = method_1(var_2["am_ApplyAnim" + 8] as MovieClip);
         _loc11_[1] = method_1(var_2["am_ApplyAnim" + 9] as MovieClip);
         this.var_558[EntType.GLOVES_SLOT] = _loc11_;
         var _loc12_:Vector.<class_33>;
         (_loc12_ = new Vector.<class_33>(2,true))[0] = method_3(var_2.am_Boots1,EntType.BOOTS_SLOT * _loc1_ + 0,this.method_96,this.method_86,this.method_88);
         _loc12_[1] = method_3(var_2.am_Boots2,EntType.BOOTS_SLOT * _loc1_ + 1,this.method_96,this.method_86,this.method_88);
         this.var_185[EntType.BOOTS_SLOT] = _loc12_;
         var _loc13_:Vector.<class_33>;
         (_loc13_ = new Vector.<class_33>(2,true))[0] = method_1(var_2["am_ApplyAnim" + 10] as MovieClip);
         _loc13_[1] = method_1(var_2["am_ApplyAnim" + 11] as MovieClip);
         this.var_558[EntType.BOOTS_SLOT] = _loc13_;
         this.var_2067 = method_5(var_2.am_Shirt,this.method_1434,this.method_772,this.method_369);
         this.var_2205 = method_5(var_2.am_Pants,this.method_1534,this.method_648,this.method_369);
         this.var_1464 = method_1(var_2.am_ApplyAnimShirt);
         this.var_1647 = method_1(var_2.am_ApplyAnimPants);
         var _loc16_:MovieClip;
         var _loc17_:uint = (_loc16_ = var_2.am_ContainerGroup).numChildren / 2;
         this.var_1252 = new Vector.<class_33>(_loc17_,true);
         this.var_1538 = new Vector.<class_33>(_loc17_,true);
         this.var_650 = new Vector.<class_33>(_loc17_,true);
         _loc14_ = 0;
         while(_loc14_ < _loc17_)
         {
            this.var_1252[_loc14_] = method_3(_loc16_["am_Dye" + (_loc14_ + 1)] as MovieClip,_loc14_ + 1,this.method_1613,this.method_1425,this.method_1953);
            this.var_1538[_loc14_] = method_5(_loc16_["am_EmptyBottle" + (_loc14_ + 1)] as MovieClip,null,this.method_1253,this.method_369);
            (_loc15_ = var_2["am_Contact" + _loc14_] as MovieClip).mouseChildren = false;
            _loc15_.mouseEnabled = false;
            _loc15_.stop();
            this.var_650[_loc14_] = method_1(_loc15_);
            _loc14_++;
         }
         this.var_1408 = method_21(var_2.am_EarnedGold);
         this.var_1771 = method_1(var_2.am_PaperDollHolder);
         this.var_1437 = method_5(var_2.am_Apply,this.OnApplyDyes);
         method_23(var_2.am_Close);
         this.var_1969 = true;
      }
      
      override public function OnDestroyScreen() : void
      {
         this.method_341(false);
         this.var_1252 = null;
         this.var_650 = null;
         this.var_1538 = null;
         this.var_558 = null;
         this.var_1464 = null;
         this.var_1647 = null;
         this.var_503 = null;
         this.var_1771.mMovieClip.removeChildren();
         this.var_1771 = null;
         this.var_185[EntType.SWORD_SLOT] = null;
         this.var_185[EntType.SHIELD_SLOT] = null;
         this.var_185[EntType.HAT_SLOT] = null;
         this.var_185[EntType.ARMOR_SLOT] = null;
         this.var_185[EntType.GLOVES_SLOT] = null;
         this.var_185[EntType.BOOTS_SLOT] = null;
         this.var_185 = null;
         this.var_75[EntType.SWORD_SLOT] = null;
         this.var_75[EntType.SHIELD_SLOT] = null;
         this.var_75[EntType.HAT_SLOT] = null;
         this.var_75[EntType.ARMOR_SLOT] = null;
         this.var_75[EntType.GLOVES_SLOT] = null;
         this.var_75[EntType.BOOTS_SLOT] = null;
         this.var_75 = null;
         this.var_2067 = null;
         this.var_2205 = null;
         this.var_202 = null;
         this.var_204 = null;
         this.var_1408 = null;
         this.var_1437 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         if(this.var_1969)
         {
            this.method_1523();
         }
         if(this.var_972)
         {
            this.method_1571();
         }
         var_37 = true;
      }
      
      override public function Hide() : void
      {
         this.method_341(false);
         super.Hide();
      }
      
      override public function RefreshPaperDoll() : void
      {
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:String = this.GetPaperDollType();
         if(!_loc2_)
         {
            return;
         }
         EntType.method_57(_loc2_,"DyeUI");
         if(mPaperDoll)
         {
            mPaperDoll.ResetEntType(EntType.method_48("PaperDoll","DyeUI"));
         }
         else
         {
            mPaperDoll = new Entity(var_1,"DyeUI:PaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,_loc1_.mExpLevel,0,null,_loc1_.var_85.method_272(),_loc1_.mMasterClass,_loc1_.var_329,_loc1_.mEquipPet,_loc1_.mCurrPotion);
         }
         this.var_1771.mMovieClip.addChild(mPaperDoll.gfx.m_TheDO);
      }
      
      private function GetPaperDollType() : String
      {
         var _loc6_:EntTypeGear = null;
         var _loc7_:class_21 = null;
         var _loc8_:class_21 = null;
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc11_:String = null;
         var _loc2_:Entity = var_1.clientEnt;
         var _loc3_:EntType = _loc2_.entType;
         var _loc4_:* = (_loc4_ = (_loc4_ = "<EntType EntName=\"PaperDoll\" parent=\"Player:" + _loc3_.entName + "\">") + "<GfxType>") + ("<AnimScale>" + 1.75 + "</AnimScale>");
         if(_loc3_.gfxType.var_522)
         {
            _loc4_ += "<FlipAnim>False</FlipAnim>";
         }
         if(_loc3_.className == "Rogue")
         {
            _loc4_ += "<BaseAnim>Relaxed</BaseAnim>";
         }
         _loc4_ += "</GfxType>";
         if(this.var_202)
         {
            _loc4_ += "<ShirtColor>" + this.var_202.color + "</ShirtColor>";
         }
         if(this.var_204)
         {
            _loc4_ += "<PantColor>" + this.var_204.color + "</PantColor>";
         }
         _loc4_ += "<EquippedGear>";
         var _loc5_:int = 1;
         while(_loc5_ < EntType.MAX_SLOTS)
         {
            if(_loc6_ = _loc3_.equippedGear[_loc5_])
            {
               _loc7_ = this.var_75[_loc5_][0];
               _loc8_ = this.var_75[_loc5_][1];
               if(!(!_loc7_ && !_loc8_))
               {
                  _loc9_ = !!_loc7_ ? _loc7_.var_57 : _loc6_.var_644;
                  _loc10_ = !!_loc8_ ? _loc8_.var_57 : _loc6_.var_705;
                  _loc11_ = EntType.method_523(_loc5_);
                  _loc4_ += "<" + _loc11_ + ">" + EntTypeGear.method_172(_loc6_.gearName,_loc6_.var_432,_loc6_.var_501,_loc6_.var_486,_loc9_,_loc10_) + "</" + _loc11_ + ">";
               }
            }
            _loc5_++;
         }
         return _loc4_ + "</EquippedGear></EntType>";
      }
      
      public function OnInitDisplay() : void
      {
         this.var_955 = 0;
         this.var_334 = -1;
         this.var_75 = new Vector.<Vector.<class_21>>(EntType.MAX_SLOTS,true);
         this.var_75[EntType.SWORD_SLOT] = new Vector.<class_21>(2,true);
         this.var_75[EntType.SHIELD_SLOT] = new Vector.<class_21>(2,true);
         this.var_75[EntType.HAT_SLOT] = new Vector.<class_21>(2,true);
         this.var_75[EntType.ARMOR_SLOT] = new Vector.<class_21>(2,true);
         this.var_75[EntType.GLOVES_SLOT] = new Vector.<class_21>(2,true);
         this.var_75[EntType.BOOTS_SLOT] = new Vector.<class_21>(2,true);
         this.method_1274();
         this.method_1869();
         this.var_972 = true;
         MathUtil.method_2(var_2.am_CharacterName,var_1.clientEntName);
         this.var_1408.SetText("--");
         this.var_1969 = true;
         if(!(var_1.mAlertState & Game.const_501))
         {
            var_1.UpdateAlert(Game.const_501);
         }
         if(var_1.mTutorialStage == Game.const_270)
         {
            var_1.SetNewTutorialStage(Game.const_476);
         }
      }
      
      private function method_1571() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc3_:class_21 = null;
         var _loc4_:MovieClip = null;
         var _loc9_:class_42 = null;
         var _loc10_:uint = 0;
         var _loc11_:Boolean = false;
         var _loc12_:class_21 = null;
         if(!var_1.clientEnt)
         {
            return;
         }
         var _loc5_:Boolean = false;
         this.var_955 = 0;
         _loc1_ = 1;
         while(_loc1_ < EntType.MAX_SLOTS)
         {
            _loc2_ = 0;
            while(_loc2_ < 2)
            {
               _loc3_ = this.var_75[_loc1_][_loc2_];
               _loc4_ = this.var_185[_loc1_][_loc2_].mMovieClip;
               _loc9_ = var_1.mOwnedGear[var_1.clientEnt.mEquipGear[_loc1_]];
               _loc10_ = 0;
               if(_loc9_)
               {
                  if(_loc12_ = _loc2_ == 0 ? _loc9_.var_295 : _loc9_.var_307)
                  {
                     _loc10_ = _loc12_.var_57;
                  }
               }
               _loc11_ = false;
               if(Boolean(_loc3_) && _loc3_.var_57 != _loc10_)
               {
                  ++this.var_955;
                  _loc5_ = true;
                  _loc11_ = true;
               }
               this.method_536(_loc3_,_loc4_,_loc11_);
               _loc2_++;
            }
            _loc1_++;
         }
         var _loc6_:Boolean = false;
         if(Boolean(this.var_202) && this.var_202.color != var_1.clientEnt.entType.shirtColor)
         {
            _loc5_ = true;
            _loc6_ = true;
         }
         this.method_536(this.var_202,this.var_2067.mMovieClip,_loc6_);
         var _loc7_:Boolean = false;
         if(Boolean(this.var_204) && this.var_204.color != var_1.clientEnt.entType.pantColor)
         {
            _loc5_ = true;
            _loc7_ = true;
         }
         this.method_536(this.var_204,this.var_2205.mMovieClip,_loc7_);
         if(_loc5_)
         {
            this.var_1437.EnableButton();
         }
         else
         {
            this.var_1437.DisableButton("Inactive");
         }
         var _loc8_:uint = Entity.const_655[var_1.clientEnt.mExpLevel] * this.var_955;
         this.var_1408.SetText(MathUtil.method_29(_loc8_));
         this.var_972 = false;
      }
      
      private function method_536(param1:class_21, param2:MovieClip, param3:Boolean) : void
      {
         var _loc4_:MovieClip = null;
         if(!param1)
         {
            param2.am_IconSmall.visible = false;
            param2.am_IconLarge.visible = false;
            param2.am_PendingIcon.visible = false;
            return;
         }
         if(param1.var_8 != "L")
         {
            _loc4_ = param2.am_IconSmall;
            param2.am_IconLarge.visible = false;
         }
         else
         {
            _loc4_ = param2.am_IconLarge;
            param2.am_IconSmall.visible = false;
         }
         _loc4_.visible = true;
         param2.am_PendingIcon.visible = param3;
         var_1.screenHudTooltip.SkinDyeIcon(param1,_loc4_.am_DyeSwap);
      }
      
      private function method_1869() : void
      {
         var _loc2_:uint = 0;
         var _loc4_:class_33 = null;
         var _loc5_:Vector.<uint> = null;
         var _loc6_:uint = 0;
         var _loc7_:class_42 = null;
         var _loc8_:GearType = null;
         var _loc9_:class_21 = null;
         var _loc10_:class_21 = null;
         var _loc1_:Entity = var_1.clientEnt;
         var _loc3_:uint = EntType.MAX_SLOTS;
         if(!_loc1_)
         {
            _loc2_ = 1;
            while(_loc2_ < _loc3_)
            {
               (_loc4_ = this.var_503[_loc2_]).mMovieClip.am_IconHolder.removeChildren();
               _loc4_.DisableButton("Inactive");
               this.var_75[_loc2_][0] = null;
               this.var_75[_loc2_][1] = null;
               _loc2_++;
            }
            this.var_202 = null;
            this.var_204 = null;
         }
         else
         {
            _loc5_ = _loc1_.mEquipGear;
            _loc2_ = 1;
            while(_loc2_ < _loc3_)
            {
               _loc8_ = !!(_loc7_ = !!(_loc6_ = _loc1_.mEquipGear[_loc2_]) ? var_1.mOwnedGear[_loc6_] : null) ? _loc7_.gearType : null;
               _loc4_ = this.var_503[_loc2_];
               var_1.screenHudTooltip.SkinEquipmentIcon(_loc8_,_loc4_);
               if(_loc8_)
               {
                  _loc4_.EnableButton();
                  this.var_185[_loc2_][0].EnableButton();
                  this.var_185[_loc2_][1].EnableButton();
                  this.var_75[_loc2_][0] = _loc7_.var_295;
                  this.var_75[_loc2_][1] = _loc7_.var_307;
               }
               else
               {
                  _loc4_.DisableButton("Inactive");
                  this.var_185[_loc2_][0].DisableButton("Inactive");
                  this.var_185[_loc2_][1].DisableButton("Inactive");
                  this.var_75[_loc2_][0] = null;
                  this.var_75[_loc2_][1] = null;
               }
               _loc9_ = class_14.var_949[_loc1_.entType.shirtColor];
               _loc10_ = class_14.var_949[_loc1_.entType.pantColor];
               this.var_202 = _loc9_;
               this.var_204 = _loc10_;
               _loc2_++;
            }
         }
      }
      
      private function method_1274() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:class_33 = null;
         var _loc3_:uint = this.var_650.length;
         _loc1_ = 0;
         while(_loc1_ < _loc3_)
         {
            _loc2_ = this.var_650[_loc1_];
            _loc2_.PlayAnimation("MouseOver");
            _loc2_.Hide();
            _loc1_++;
         }
      }
      
      public function OnApplyDyes(param1:MouseEvent, param2:Boolean = false) : void
      {
         var _loc5_:Packet = null;
         var _loc6_:uint = 0;
         var _loc7_:class_21 = null;
         var _loc8_:class_21 = null;
         var _loc9_:* = false;
         var _loc10_:* = false;
         var _loc11_:class_21 = null;
         var _loc12_:class_21 = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         var _loc3_:uint = this.var_955 * Entity.const_655[var_1.clientEnt.mExpLevel];
         var _loc4_:uint = this.var_955 * Entity.const_1016[var_1.clientEnt.mExpLevel];
         if(!param2 && var_1.clientEnt.currGold < _loc3_)
         {
            var_1.screenGoldShort.Display(_loc3_,_loc4_,class_93.const_538,null);
         }
         else
         {
            if(!param2)
            {
               var_1.clientEnt.GainMoney(-_loc3_,false);
            }
            (_loc5_ = new Packet(LinkUpdater.const_1175)).method_9(var_1.clientEntID);
            _loc6_ = 1;
            while(_loc6_ < EntType.MAX_SLOTS)
            {
               _loc11_ = this.var_75[_loc6_][0];
               _loc12_ = this.var_75[_loc6_][1];
               if(!_loc11_ && !_loc12_)
               {
                  _loc5_.method_15(false);
               }
               else
               {
                  _loc5_.method_15(true);
                  _loc5_.method_20(class_21.const_50,!!_loc11_ ? _loc11_.var_57 : 0);
                  _loc5_.method_20(class_21.const_50,!!_loc12_ ? _loc12_.var_57 : 0);
               }
               _loc6_++;
            }
            _loc5_.method_15(param2);
            _loc7_ = this.var_202;
            _loc8_ = this.var_204;
            _loc9_ = _loc7_ != null;
            _loc10_ = _loc8_ != null;
            _loc5_.method_15(_loc9_);
            if(_loc9_)
            {
               _loc5_.method_20(class_21.const_50,_loc7_.var_57);
            }
            _loc5_.method_15(_loc10_);
            if(_loc10_)
            {
               _loc5_.method_20(class_21.const_50,_loc8_.var_57);
            }
            var_1.serverConn.SendPacket(_loc5_);
            this.var_1408.SetText("--");
            this.var_1437.DisableButton("Inactive");
            this.method_1407();
            Refresh();
         }
      }
      
      private function method_1407() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc3_:class_33 = null;
         var _loc5_:class_21 = null;
         var _loc6_:class_42 = null;
         var _loc7_:uint = 0;
         if(!var_1.clientEnt)
         {
            return;
         }
         var _loc4_:uint = EntType.MAX_SLOTS;
         _loc1_ = 1;
         while(_loc1_ < _loc4_)
         {
            _loc2_ = 0;
            while(_loc2_ < 2)
            {
               if(!this.var_75[_loc1_][_loc2_])
               {
                  _loc3_ = this.var_558[_loc1_][_loc2_];
                  if(_loc3_.mbVisible)
                  {
                     _loc3_.Hide();
                  }
               }
               else
               {
                  _loc5_ = this.var_75[_loc1_][_loc2_];
                  _loc6_ = var_1.mOwnedGear[var_1.clientEnt.mEquipGear[_loc1_]];
                  _loc7_ = 0;
                  if(_loc2_ == 0 && _loc6_ && Boolean(_loc6_.var_295))
                  {
                     _loc7_ = _loc6_.var_295.var_57;
                  }
                  if(_loc2_ == 1 && _loc6_ && Boolean(_loc6_.var_307))
                  {
                     _loc7_ = _loc6_.var_307.var_57;
                  }
                  if(Boolean(_loc5_) && _loc5_.var_57 != _loc7_)
                  {
                     _loc3_ = this.var_558[_loc1_][_loc2_];
                     _loc3_.Show();
                     _loc3_.PlayAnimation("Allocate",class_33.const_14);
                  }
               }
               _loc2_++;
            }
            _loc1_++;
         }
         if(!this.var_202 || this.var_202.color == var_1.clientEnt.entType.shirtColor)
         {
            this.var_1464.Hide();
         }
         else
         {
            this.var_1464.Show();
            this.var_1464.PlayAnimation("Allocate",class_33.const_14);
         }
         if(!this.var_204 || this.var_204.color == var_1.clientEnt.entType.pantColor)
         {
            this.var_1647.Hide();
         }
         else
         {
            this.var_1647.Show();
            this.var_1647.PlayAnimation("Allocate",class_33.const_14);
         }
      }
      
      private function method_1434(param1:MouseEvent) : void
      {
         var _loc3_:class_21 = null;
         if(!var_1.clientEnt)
         {
            return;
         }
         if(this.var_334 < 0)
         {
            return;
         }
         var _loc2_:class_21 = class_14.var_686[this.var_334];
         if(!_loc2_)
         {
            return;
         }
         if(this.var_202 != _loc2_)
         {
            this.var_202 = _loc2_;
         }
         else
         {
            _loc3_ = class_14.var_949[var_1.clientEnt.entType.shirtColor];
            this.var_202 = _loc3_;
         }
         this.method_772(param1);
         this.var_972 = true;
         Refresh();
      }
      
      private function method_772(param1:MouseEvent) : void
      {
         if(!this.var_202)
         {
            return;
         }
         var_1.screenHudTooltip.ShowBasicItemTooltip(this.var_202.displayName,"Dye",this.var_202.var_8,const_265,const_280);
      }
      
      private function method_1534(param1:MouseEvent) : void
      {
         var _loc3_:class_21 = null;
         if(!var_1.clientEnt)
         {
            return;
         }
         if(this.var_334 < 0)
         {
            return;
         }
         var _loc2_:class_21 = class_14.var_686[this.var_334];
         if(!_loc2_)
         {
            return;
         }
         if(this.var_204 != _loc2_)
         {
            this.var_204 = _loc2_;
         }
         else
         {
            _loc3_ = class_14.var_949[var_1.clientEnt.entType.pantColor];
            this.var_204 = _loc3_;
         }
         this.method_648(param1);
         this.var_972 = true;
         Refresh();
      }
      
      private function method_648(param1:MouseEvent) : void
      {
         if(!this.var_204)
         {
            return;
         }
         var_1.screenHudTooltip.ShowBasicItemTooltip(this.var_204.displayName,"Dye",this.var_204.var_8,const_265,const_280);
      }
      
      private function method_96(param1:MouseEvent, param2:uint) : void
      {
         var _loc7_:uint = 0;
         var _loc8_:class_42 = null;
         if(!var_1.clientEnt)
         {
            return;
         }
         if(this.var_334 < 0)
         {
            return;
         }
         var _loc3_:uint = uint(param2 / EntType.MAX_SLOTS);
         var _loc4_:uint = param2 % EntType.MAX_SLOTS;
         var _loc5_:class_21;
         if(!(_loc5_ = class_14.var_686[this.var_334]))
         {
            return;
         }
         var _loc6_:class_21;
         if(!(_loc6_ = this.var_75[_loc3_][_loc4_]) || _loc6_.var_57 != _loc5_.var_57)
         {
            this.var_75[_loc3_][_loc4_] = _loc5_;
         }
         else
         {
            _loc8_ = !!(_loc7_ = uint(var_1.clientEnt.mEquipGear[_loc3_])) ? var_1.mOwnedGear[_loc7_] : null;
            this.var_75[_loc3_][_loc4_] = !!_loc4_ ? _loc8_.var_307 : _loc8_.var_295;
         }
         this.method_86(param1,param2);
         this.var_972 = true;
         Refresh();
      }
      
      private function method_86(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:uint = uint(param2 / EntType.MAX_SLOTS);
         var _loc4_:uint = param2 % EntType.MAX_SLOTS;
         var _loc5_:class_21;
         if(!(_loc5_ = this.var_75[_loc3_][_loc4_]))
         {
            return;
         }
         var_1.screenHudTooltip.ShowBasicItemTooltip(_loc5_.displayName,"Dye",_loc5_.var_8,const_265,const_280);
      }
      
      private function method_88(param1:MouseEvent, param2:uint) : void
      {
         this.method_369(param1);
      }
      
      private function method_369(param1:MouseEvent) : void
      {
         var_1.screenHudTooltip.HideTooltip();
      }
      
      private function method_1613(param1:MouseEvent, param2:uint) : void
      {
         var _loc4_:class_21 = null;
         if(param1.ctrlKey)
         {
            if(!(_loc4_ = class_14.var_686[param2]))
            {
               return;
            }
            this.method_1574(_loc4_);
            return;
         }
         if(this.var_334 > -1)
         {
            this.var_650[this.var_334 - 1].Hide();
         }
         var _loc3_:class_33 = this.var_650[param2 - 1];
         _loc3_.PlayAnimation("Selected");
         _loc3_.Show();
         if(this.var_334 != param2)
         {
            this.var_334 = param2;
         }
      }
      
      private function method_1425(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:class_21 = class_14.var_686[param2];
         var_1.screenHudTooltip.ShowBasicItemTooltip(_loc3_.displayName,"Dye",_loc3_.var_8,const_265,const_280);
         var _loc4_:class_33;
         if(!(_loc4_ = this.var_650[param2 - 1]).mbVisible)
         {
            _loc4_.Show();
         }
         if(param2 != this.var_334)
         {
            if(_loc4_.mActiveTimeline.name != "MouseOver")
            {
               _loc4_.PlayAnimation("MouseOver");
            }
         }
      }
      
      private function method_1953(param1:MouseEvent, param2:uint) : void
      {
         var_1.screenHudTooltip.HideTooltip();
         var _loc3_:class_33 = this.var_650[param2 - 1];
         if(param2 != this.var_334)
         {
            if(_loc3_.mbVisible)
            {
               _loc3_.Hide();
            }
         }
      }
      
      private function method_341(param1:Boolean) : void
      {
         var_2.am_ContainerGroup.cacheAsBitmap = param1;
      }
      
      private function method_1523() : void
      {
         var _loc1_:class_21 = null;
         var _loc2_:uint = 0;
         var _loc4_:class_33 = null;
         this.method_341(false);
         var _loc5_:Array = class_14.var_686;
         var _loc6_:uint = this.var_1252.length;
         _loc2_ = 0;
         while(_loc2_ < _loc6_)
         {
            _loc1_ = _loc5_[_loc2_ + 1];
            if(_loc1_)
            {
               if(!var_1.mOwnedDyes[_loc1_.var_57])
               {
                  this.var_1252[_loc2_].Hide();
                  this.var_1538[_loc2_].Show();
               }
               else
               {
                  _loc4_ = this.var_1252[_loc2_];
                  var_1.screenHudTooltip.SkinDyeIcon(_loc1_,_loc4_.mMovieClip.am_DyeSwap);
                  _loc4_.Show();
                  this.var_1538[_loc2_].Hide();
               }
            }
            _loc2_++;
         }
         this.var_1969 = false;
         this.method_341(true);
      }
      
      public function method_1588() : void
      {
         this.var_972 = true;
         Refresh();
      }
      
      public function method_1574(param1:class_21) : void
      {
         var _loc2_:* = "{" + class_127.const_8[8] + ":";
         _loc2_ += String(param1.var_57);
         _loc2_ += "}";
         var_1.screenChat.AddItemInfoToChatEntry("[" + param1.displayName + "]",_loc2_);
      }
      
      private function method_1253(param1:MouseEvent) : void
      {
         var_1.screenHudTooltip.ShowBasicDescriptionTooltip("Empty Bottle","Dye","Missing","Slay monsters to find dye bottles, then use them to dye your gear different colors",const_265,const_280 - 40);
      }
   }
}
