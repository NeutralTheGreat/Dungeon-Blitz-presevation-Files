package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.geom.Rectangle;
   
   public class class_110 extends class_32
   {
      
      private static const const_43:uint = 4;
       
      
      private var var_1748:Boolean;
      
      private var var_2936:class_33;
      
      private var var_110:class_138;
      
      private var mActivePet:class_87;
      
      private var var_1104:class_33;
      
      private var var_794:class_33;
      
      private var var_2197:class_33;
      
      private var var_531:class_33;
      
      private var var_681:Vector.<class_33>;
      
      private var var_1187:Vector.<class_138>;
      
      private var var_447:Vector.<class_103>;
      
      public function class_110(param1:Game)
      {
         super(param1,"a_ScreenPetFood",null);
         var_15 = true;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:MovieClip = null;
         this.var_681 = new Vector.<class_33>(const_43,true);
         this.var_1187 = new Vector.<class_138>(const_43,true);
         _loc1_ = 0;
         while(_loc1_ < const_43)
         {
            _loc2_ = var_2["am_Slot" + _loc1_] as MovieClip;
            this.var_681[_loc1_] = method_3(_loc2_,_loc1_,this.method_1223,this.method_1257,this.HideTooltip);
            this.var_1187[_loc1_] = method_21(_loc2_.am_Quantity);
            _loc1_++;
         }
         this.var_447 = new Vector.<class_103>();
         this.var_1104 = method_1(var_2.am_LevelUp);
         this.var_794 = method_1(var_2.am_ParticleBurst);
         this.var_794.mMovieClip.mouseChildren = false;
         this.var_794.mMovieClip.mouseEnabled = false;
         this.var_2197 = method_1(var_2.am_Locator);
         this.var_531 = method_1(var_2.am_XPFloaterAnim);
         this.var_531.mMovieClip.mouseChildren = false;
         this.var_531.mMovieClip.mouseEnabled = false;
         this.var_2936 = method_5(var_2.am_PetInfo,null,this.method_1911,this.HideTooltip);
         this.var_110 = method_21(var_2.am_XPText);
         method_23(var_2.am_Close);
         method_23(var_2.am_BoneIcon);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_681 = null;
         this.var_1187 = null;
         this.var_447 = null;
         this.var_1104 = null;
         this.var_794 = null;
         this.var_2197 = null;
         this.var_110 = null;
         this.mActivePet = null;
         this.var_531 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc2_:uint = 0;
         var _loc4_:class_103 = null;
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         var _loc7_:String = null;
         var _loc1_:* = this.mActivePet.var_23 == class_7.const_35;
         var _loc3_:uint = this.var_447.length;
         _loc2_ = 0;
         while(_loc2_ < const_43)
         {
            if(_loc2_ >= _loc3_)
            {
               method_14(this.var_681[_loc2_].mMovieClip.am_ItemIconHolder);
               this.var_1187[_loc2_].SetText("");
            }
            else if((Boolean(_loc4_ = this.var_447[_loc2_])) && Boolean(_loc4_.stackCount))
            {
               method_12(this.var_681[_loc2_].mMovieClip.am_ItemIconHolder,_loc4_.consumableType.iconName);
               this.var_1187[_loc2_].SetText("x" + _loc4_.stackCount);
               if(_loc1_)
               {
                  this.var_681[_loc2_].mMovieClip.filters = [class_50.const_112];
               }
               else
               {
                  this.var_681[_loc2_].mMovieClip.filters = [];
               }
            }
            else
            {
               method_14(this.var_681[_loc2_].mMovieClip.am_ItemIconHolder);
               this.var_1187[_loc2_].SetText("");
            }
            _loc2_++;
         }
         if(_loc1_)
         {
            this.var_110.SetText("");
         }
         else
         {
            _loc5_ = this.mActivePet.var_110 - class_7.method_154(this.mActivePet.var_23 - 1);
            _loc6_ = int(class_7.method_154(this.mActivePet.var_23));
            _loc7_ = "";
            if(this.mActivePet.var_23 != class_7.const_35)
            {
               _loc7_ = " / " + MathUtil.method_29(_loc6_);
            }
            if(this.mActivePet.var_110 < _loc6_)
            {
               MathUtil.method_2(this.var_110.mTextField,MathUtil.method_29(this.mActivePet.var_110) + _loc7_);
            }
            else
            {
               MathUtil.method_2(this.var_110.mTextField,"<font color=\'#00CCFF\'>" + MathUtil.method_29(this.mActivePet.var_110) + "</font>" + _loc7_,true);
            }
         }
      }
      
      public function OnInitDisplay(param1:class_87) : void
      {
         this.method_1306();
         this.var_1104.Hide(true);
         this.var_794.Hide(true);
         this.var_1748 = false;
         this.var_531.Hide(true);
         this.mActivePet = param1;
      }
      
      private function method_1223(param1:MouseEvent, param2:uint) : void
      {
         if(param2 >= this.var_447.length)
         {
            return;
         }
         var _loc3_:class_103 = this.var_447[param2];
         if(!_loc3_ || !_loc3_.stackCount)
         {
            return;
         }
         if(!this.mActivePet || !this.mActivePet.method_1533())
         {
            return;
         }
         if(_loc3_.consumableType.consumableID == class_3.var_1829)
         {
            if(this.mActivePet.var_23 < class_7.const_35)
            {
               this.var_1748 = true;
            }
            ++this.mActivePet.var_23;
         }
         this.method_1010(param2);
         if(!this.var_531.mbVisible)
         {
            this.var_531.Show();
         }
         this.var_531.ClearAnimation();
         this.var_531.PlayAnimation("Float",class_33.const_14);
         MathUtil.method_2(this.var_531.mMovieClip.am_Wrapper.am_Amount,"+" + MathUtil.method_29(_loc3_.consumableType.var_2821) + "XP");
         var _loc4_:Packet;
         (_loc4_ = new Packet(LinkUpdater.const_789)).method_20(class_3.const_69,_loc3_.consumableType.consumableID);
         var_1.serverConn.SendPacket(_loc4_);
         if(SoundConfig.var_199)
         {
            SoundManager.Play(SoundConfig.var_199);
         }
         var_1.screenArmory.Refresh();
      }
      
      private function method_1257(param1:MouseEvent, param2:uint) : void
      {
         if(param2 >= this.var_447.length)
         {
            return;
         }
         var _loc3_:class_103 = this.var_447[param2];
         if(!_loc3_ || !_loc3_.stackCount)
         {
            return;
         }
         var _loc4_:class_3 = _loc3_.consumableType;
         var_1.screenHudTooltip.ShowBasicDescriptionTooltip(_loc4_.displayName,"Pet Food",_loc4_.var_8,_loc4_.description,302.15,185.75);
      }
      
      private function method_1911(param1:MouseEvent) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:class_87 = _loc2_.mEquipPet;
         if(!_loc3_)
         {
            return;
         }
         var_1.screenHudTooltip.ShowPetTooltip(_loc3_,false,712.55,150);
      }
      
      private function HideTooltip(param1:MouseEvent, param2:uint = 0) : void
      {
         var_1.screenHudTooltip.HideTooltip(true);
      }
      
      private function method_1010(param1:uint) : void
      {
         var _loc2_:class_3 = this.var_447[param1].consumableType;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:MovieClip = this.var_681[param1].mMovieClip;
         var _loc4_:Rectangle = _loc3_.getBounds(mWindow.mMovieClip);
         var _loc5_:MovieClip = this.var_2197.mMovieClip;
         method_68(_loc2_.iconName,_loc4_.x,_loc4_.y,_loc5_,250,class_137.method_113,this.method_1512);
      }
      
      private function method_1512() : void
      {
         if(this.var_1748)
         {
            this.var_1104.Show();
            this.var_1104.ClearAnimation();
            this.var_1104.PlayAnimation("FadeIn",class_33.const_14);
            this.var_1748 = false;
         }
         this.var_794.Show();
         this.var_794.ClearAnimation();
         this.var_794.PlayAnimation("Burst",class_33.const_14);
         Refresh();
      }
      
      private function method_1306() : void
      {
         var _loc1_:class_103 = null;
         var _loc3_:uint = 0;
         this.var_447.length = 0;
         var _loc2_:Array = var_1.mOwnedConsumables;
         var _loc4_:uint = _loc2_.length;
         _loc3_ = 0;
         while(_loc3_ < _loc4_)
         {
            _loc1_ = _loc2_[_loc3_];
            if(_loc1_ && _loc1_.stackCount && _loc1_.consumableType.type == "PetFood")
            {
               this.var_447.push(_loc1_);
            }
            _loc3_++;
         }
      }
   }
}
