package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   
   public class class_68 extends class_32
   {
       
      
      internal var var_298:MovieClip;
      
      internal var var_1147:class_33;
      
      internal var var_2017:uint;
      
      internal var var_399:String;
      
      internal var var_391:Vector.<class_33>;
      
      internal var var_376:Vector.<class_33>;
      
      internal var var_373:Vector.<class_33>;
      
      internal var var_2211:class_33;
      
      internal var var_2245:Vector.<GearType>;
      
      internal var var_2282:Vector.<class_42>;
      
      public function class_68(param1:Game)
      {
         super(param1,"a_InspectWindow","am_InspectWrapper");
      }
      
      public static function method_2007(param1:MovieClip, param2:String) : void
      {
         if(param2 == "Rogue")
         {
            param1.am_PaladinIcon.visible = false;
            param1.am_MageIcon.visible = false;
            param1.am_RogueIcon.visible = true;
         }
         else if(param2 == "Paladin")
         {
            param1.am_PaladinIcon.visible = true;
            param1.am_MageIcon.visible = false;
            param1.am_RogueIcon.visible = false;
         }
         else
         {
            param1.am_PaladinIcon.visible = false;
            param1.am_MageIcon.visible = true;
            param1.am_RogueIcon.visible = false;
         }
      }
      
      override public function OnCreateScreen() : void
      {
         method_23(var_2.am_Exit);
         method_5(var_2.am_Examine,this.method_1235);
         method_5(var_2.am_Invite,this.method_1486);
         method_5(var_2.am_Whisper,this.method_1720);
         this.var_2211 = method_5(var_2.am_Join,this.method_1341);
         this.var_298 = mWindow.mMovieClip.am_GearInfo;
         this.var_1147 = method_1(this.var_298.am_DetailPanel);
         this.var_1147.Hide();
         var _loc1_:MovieClip = this.var_298.am_SlotsMage;
         this.var_391 = new Vector.<class_33>(EntType.MAX_SLOTS,true);
         this.var_391[EntType.SWORD_SLOT] = method_3(_loc1_.am_Sword,EntType.SWORD_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_391[EntType.SHIELD_SLOT] = method_3(_loc1_.am_Shield,EntType.SHIELD_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_391[EntType.HAT_SLOT] = method_3(_loc1_.am_Hat,EntType.HAT_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_391[EntType.ARMOR_SLOT] = method_3(_loc1_.am_Armor,EntType.ARMOR_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_391[EntType.GLOVES_SLOT] = method_3(_loc1_.am_Gloves,EntType.GLOVES_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_391[EntType.BOOTS_SLOT] = method_3(_loc1_.am_Boots,EntType.BOOTS_SLOT,this.method_58,this.method_61,this.method_62);
         _loc1_ = this.var_298.am_SlotsRogue;
         this.var_376 = new Vector.<class_33>(EntType.MAX_SLOTS,true);
         this.var_376[EntType.SWORD_SLOT] = method_3(_loc1_.am_Sword,EntType.SWORD_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_376[EntType.SHIELD_SLOT] = method_3(_loc1_.am_Shield,EntType.SHIELD_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_376[EntType.HAT_SLOT] = method_3(_loc1_.am_Hat,EntType.HAT_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_376[EntType.ARMOR_SLOT] = method_3(_loc1_.am_Armor,EntType.ARMOR_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_376[EntType.GLOVES_SLOT] = method_3(_loc1_.am_Gloves,EntType.GLOVES_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_376[EntType.BOOTS_SLOT] = method_3(_loc1_.am_Boots,EntType.BOOTS_SLOT,this.method_58,this.method_61,this.method_62);
         _loc1_ = this.var_298.am_SlotsPaladin;
         this.var_373 = new Vector.<class_33>(EntType.MAX_SLOTS,true);
         this.var_373[EntType.SWORD_SLOT] = method_3(_loc1_.am_Sword,EntType.SWORD_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_373[EntType.SHIELD_SLOT] = method_3(_loc1_.am_Shield,EntType.SHIELD_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_373[EntType.HAT_SLOT] = method_3(_loc1_.am_Hat,EntType.HAT_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_373[EntType.ARMOR_SLOT] = method_3(_loc1_.am_Armor,EntType.ARMOR_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_373[EntType.GLOVES_SLOT] = method_3(_loc1_.am_Gloves,EntType.GLOVES_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_373[EntType.BOOTS_SLOT] = method_3(_loc1_.am_Boots,EntType.BOOTS_SLOT,this.method_58,this.method_61,this.method_62);
         this.var_2245 = new Vector.<GearType>(EntType.MAX_SLOTS,true);
         this.var_2282 = new Vector.<class_42>(EntType.MAX_SLOTS,true);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_2211 = null;
         this.var_298 = null;
         this.var_1147 = null;
         this.var_391 = null;
         this.var_376 = null;
         this.var_373 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:Entity = var_1.GetEntFromID(this.var_2017);
         if(!_loc1_)
         {
            return;
         }
         this.var_399 = _loc1_.entType.entName;
         this.var_298.visible = false;
         var _loc2_:String = _loc1_.entType.className;
         MathUtil.method_2(var_2.am_Header,this.var_399);
         MathUtil.method_2(var_2.am_Class,(!!_loc1_.mMasterClass ? _loc1_.mMasterClass : _loc2_) + ", Level " + _loc1_.mExpLevel);
         var _loc4_:uint = 1;
         while(_loc4_ < EntType.MAX_SLOTS)
         {
            if(_loc2_ == "Mage")
            {
               this.var_391[_loc4_].Show();
               this.var_376[_loc4_].Hide();
               this.var_373[_loc4_].Hide();
            }
            else if(_loc2_ == "Rogue")
            {
               this.var_391[_loc4_].Hide();
               this.var_376[_loc4_].Show();
               this.var_373[_loc4_].Hide();
            }
            else
            {
               this.var_391[_loc4_].Hide();
               this.var_376[_loc4_].Hide();
               this.var_373[_loc4_].Show();
            }
            _loc4_++;
         }
         this.var_2211.Show();
      }
      
      private function method_1415(param1:Entity, param2:int, param3:Vector.<class_33>) : void
      {
         var _loc10_:class_64 = null;
         var _loc11_:class_64 = null;
         var _loc12_:class_64 = null;
         var _loc13_:class_21 = null;
         var _loc14_:class_21 = null;
         var _loc15_:class_42 = null;
         var _loc4_:EntTypeGear;
         var _loc5_:GearType = !!(_loc4_ = param1.entType.equippedGear[param2]) ? class_14.gearTypesDict[_loc4_.gearName] : null;
         var _loc7_:MovieClip;
         var _loc6_:class_33;
         var _loc8_:MovieClip = (_loc7_ = (_loc6_ = param3[param2]).mMovieClip).am_IconHolder.am_Button;
         var _loc9_:MovieClip = _loc7_.am_Watermark;
         while(_loc8_.numChildren)
         {
            _loc8_.removeChildAt(0);
         }
         this.var_2245[param2] = _loc5_;
         if(!_loc5_ || _loc5_.var_884)
         {
            _loc9_.visible = true;
         }
         else
         {
            _loc9_.visible = false;
            method_52(_loc8_,var_1.RenderGear(Game.const_95,_loc5_,0.43,param1));
         }
         if(_loc4_)
         {
            if(!_loc5_)
            {
               return;
            }
            _loc10_ = !!_loc4_.var_432 ? class_64.method_56(_loc4_.var_432) : null;
            _loc11_ = !!_loc4_.var_501 ? class_64.method_56(_loc4_.var_501) : null;
            _loc12_ = !!_loc4_.var_486 ? class_64.method_56(_loc4_.var_486) : null;
            _loc13_ = class_14.var_194[_loc4_.var_644];
            _loc14_ = class_14.var_194[_loc4_.var_705];
            _loc15_ = new class_42(_loc5_,_loc10_,_loc11_,_loc12_,_loc13_,_loc14_,false);
            this.var_2282[param2] = _loc15_;
         }
      }
      
      private function method_1235(param1:MouseEvent) : void
      {
         var _loc3_:String = null;
         var _loc4_:Vector.<class_33> = null;
         var _loc5_:uint = 0;
         var _loc2_:Entity = var_1.GetEntFromID(this.var_2017);
         if(!_loc2_)
         {
            Hide();
            return;
         }
         if(this.var_298.visible)
         {
            this.var_298.visible = false;
         }
         else
         {
            this.var_298.visible = true;
            MathUtil.method_2(this.var_298.am_StatMelee,String(_loc2_.meleeDamage));
            MathUtil.method_2(this.var_298.am_StatMagic,String(_loc2_.magicDamage));
            MathUtil.method_2(this.var_298.am_StatHealth,String(_loc2_.maxHP));
            MathUtil.method_2(this.var_298.am_StatArmor,String(_loc2_.armorClass));
            _loc3_ = _loc2_.entType.className;
            _loc4_ = _loc3_ == "Mage" ? this.var_391 : (_loc3_ == "Rogue" ? this.var_376 : this.var_373);
            _loc5_ = 1;
            while(_loc5_ < EntType.MAX_SLOTS)
            {
               this.method_1415(_loc2_,_loc5_,_loc4_);
               _loc5_++;
            }
         }
      }
      
      private function method_58(param1:MouseEvent, param2:uint) : void
      {
         var _loc4_:class_42 = null;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         if(param1.ctrlKey)
         {
            _loc4_ = this.var_2282[param2];
            var_1.screenArmory.LinkGearInChat(0,_loc4_);
         }
      }
      
      private function method_61(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:MovieClip = this.var_1147.mMovieClip;
         var _loc5_:EntType = _loc3_.entType;
         var _loc6_:GearType = this.var_2245[param2];
         ScreenArmory.method_1229(_loc6_,_loc4_.am_GearName);
         ScreenArmory.method_1818(_loc5_,_loc6_,_loc4_.am_GearType);
         this.var_1147.Show();
      }
      
      private function method_62(param1:MouseEvent, param2:uint) : void
      {
         this.var_1147.Hide();
      }
      
      private function method_1486(param1:MouseEvent) : void
      {
         if(this.var_399)
         {
            var_1.screenChat.TryToProcessChatAsLocalCommand("/invite " + this.var_399);
         }
      }
      
      private function method_1720(param1:MouseEvent) : void
      {
         if(this.var_399)
         {
            var_1.screenChat.BeginChat("/tell " + this.var_399 + " ");
         }
      }
      
      private function method_2077(param1:MouseEvent) : void
      {
         if(this.var_399)
         {
            var_1.screenChat.TryToProcessChatAsLocalCommand("/acceptfriend " + this.var_399);
         }
      }
      
      private function method_1341(param1:MouseEvent) : void
      {
         if(this.var_399)
         {
            var_1.screenChat.TryToProcessChatAsLocalCommand("/join " + this.var_399);
         }
      }
      
      private function method_2046(param1:MouseEvent) : void
      {
         if(this.var_399)
         {
            var_1.screenChat.TryToProcessChatAsLocalCommand("/friend " + this.var_399);
         }
      }
      
      public function OnInitDisplay(param1:uint) : void
      {
         this.var_2017 = param1;
      }
   }
}
