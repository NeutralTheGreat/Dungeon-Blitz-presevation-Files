package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   
   public class class_115 extends class_32
   {
       
      
      private var var_156:class_12;
      
      private var var_2630:uint;
      
      private var var_1982:class_33;
      
      private var var_2065:class_33;
      
      private var var_2071:class_138;
      
      private var var_2328:class_138;
      
      private var var_1555:class_138;
      
      public function class_115(param1:Game)
      {
         super(param1,"a_ScreenRoyalSigilStorePrompt",null);
         var_15 = true;
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_1982 = method_1(var_2.am_Icon);
         this.var_2065 = method_1(var_2.am_CostIcon);
         this.var_1555 = method_21(var_2.am_Cost);
         this.var_2071 = method_21(var_2.am_Name);
         this.var_2328 = method_21(var_2.am_Type);
         method_5(var_2.am_NeverMind,this.method_1497);
         method_5(var_2.am_Buy,this.method_994);
         method_23(var_2.am_Close);
         var_2.cacheAsBitmap = true;
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1982 = null;
         this.var_2065 = null;
         this.var_1555 = null;
         this.var_2071 = null;
         this.var_156 = null;
         this.var_2328 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:String = null;
         var _loc2_:MovieClip = null;
         var _loc3_:MovieClip = null;
         var _loc4_:TextField = null;
         var _loc5_:class_20 = null;
         var _loc6_:class_7 = null;
         var _loc7_:class_3 = null;
         if(!this.var_156)
         {
            Hide();
         }
         else
         {
            _loc2_ = this.var_1982.mMovieClip.am_ItemIconHolder;
            _loc3_ = this.var_1982.mMovieClip.am_MaskIconHolder;
            switch(this.var_156.type)
            {
               case class_12.const_279:
                  _loc1_ = (_loc5_ = class_14.var_362[this.var_156.var_257]).var_255;
                  _loc2_.visible = false;
                  method_14(_loc3_);
                  _loc3_.addChild(class_41.method_168(_loc5_,0,0,58,58,var_1.main.overallScale));
                  _loc3_.visible = true;
                  break;
               case class_12.include:
                  _loc1_ = (_loc6_ = class_14.var_233[this.var_156.var_257]).var_255;
                  _loc2_.visible = false;
                  method_14(_loc3_);
                  _loc3_.addChild(class_41.method_85(_loc6_,0,0,58,58,var_1.main.overallScale));
                  _loc3_.visible = true;
                  break;
               case class_12.const_205:
                  _loc1_ = (_loc7_ = class_14.var_303[this.var_156.var_257]).var_8;
                  _loc3_.visible = false;
                  method_12(_loc2_,this.var_156.iconName);
                  _loc2_.visible = true;
                  break;
               default:
                  _loc1_ = "M";
                  _loc3_.visible = false;
                  method_12(_loc2_,this.var_156.iconName);
                  _loc2_.visible = true;
            }
            MathUtil.method_8(this.var_2071.mTextField,this.var_156.displayName,class_101.method_37(_loc1_,this.var_156.type));
            this.var_2328.SetText(class_107.method_484(this.var_156));
            this.var_1555.SetText(String(this.var_156.var_795));
            this.var_1555.TickTextField();
            _loc4_ = this.var_1555.mTextField;
            this.var_2065.mMovieClip.x = _loc4_.x + _loc4_.width - _loc4_.textWidth - class_107.const_736;
         }
      }
      
      public function OnInitDisplay(param1:class_12, param2:uint) : void
      {
         this.var_156 = param1;
         this.var_2630 = param2;
      }
      
      private function method_1497(param1:MouseEvent) : void
      {
         Hide();
      }
      
      private function method_994(param1:MouseEvent) : void
      {
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(!var_1.clientEnt)
         {
            return;
         }
         if(!this.var_156.var_1579 && var_1.mLockboxData.mRoyalSigils < this.var_156.var_795)
         {
            return;
         }
         if(this.var_156.var_1579 && var_1.clientEnt.currGold < this.var_156.var_795)
         {
            return;
         }
         var _loc2_:Packet = new Packet(LinkUpdater.const_1219);
         _loc2_.method_20(class_12.const_753,this.var_156.var_865);
         var_1.serverConn.SendPacket(_loc2_);
         if(this.var_156.type == class_12.const_279 || this.var_156.type == class_12.include)
         {
            var_1.screenRoyalSigilStore.mTempOwnedChangeLog[this.var_2630] = true;
         }
         var_1.screenRoyalSigilStore.Refresh();
         Hide();
      }
   }
}
