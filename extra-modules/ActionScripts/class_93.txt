package
{
   import flash.events.MouseEvent;
   
   public class class_93 extends class_32
   {
      
      public static const const_178:uint = 1;
      
      public static const const_577:uint = 2;
      
      public static const const_441:uint = 3;
      
      public static const const_563:uint = 4;
      
      public static const const_507:uint = 5;
      
      public static const const_538:uint = 6;
       
      
      internal var var_2339:class_9;
      
      internal var var_2912:class_10;
      
      internal var var_2899:uint;
      
      internal var var_2887:uint = 0;
      
      internal var var_320:uint = 0;
      
      internal var var_2880:uint = 0;
      
      internal var var_1742:uint = 0;
      
      internal var var_2847:class_87;
      
      public function class_93(param1:Game)
      {
         super(param1,"a_ScreenGoldShort","am_Panel");
         var_15 = true;
      }
      
      override public function OnCreateScreen() : void
      {
         method_10(var_2.am_SpendIdols,this.method_1784);
         method_23(var_2.am_Close);
      }
      
      public function OnInitDisplay(param1:uint, param2:uint, param3:uint, param4:Object) : void
      {
         var _loc5_:String = null;
         var _loc6_:String = null;
         this.var_320 = param3;
         this.var_2880 = param1;
         this.var_1742 = param2;
         if(this.var_320 == const_178)
         {
            _loc5_ = "Upgrade Building";
            _loc6_ = "How would you like to pay to begin your upgrade?";
            this.var_2339 = class_9(param4);
         }
         if(this.var_320 == const_577)
         {
            _loc5_ = "Train Talent Point";
            _loc6_ = "How would you like to pay to begin your training?";
            this.var_2899 = uint(param4);
         }
         if(this.var_320 == const_441)
         {
            _loc5_ = "Train Ability Rank";
            _loc6_ = "How would you like to pay to begin your training?";
            this.var_2912 = class_10(param4);
         }
         if(this.var_320 == const_563)
         {
            _loc5_ = "Hatch Egg";
            _loc6_ = "How would you like to pay for the egg?";
            this.var_2887 = uint(param4);
         }
         if(this.var_320 == const_507)
         {
            _loc5_ = "Train Pet";
            _loc6_ = "How would you like to pay to begin the training?";
            this.var_2847 = class_87(param4);
         }
         if(this.var_320 == const_538)
         {
            _loc5_ = "Dye Gear";
            _loc6_ = "How would you like to pay to dye your gear?";
         }
         MathUtil.method_2(var_2.am_Header,_loc5_);
         MathUtil.method_2(var_2.am_Message,_loc6_);
         MathUtil.method_2(var_2.am_Idols,MathUtil.method_29(this.var_1742));
         MathUtil.method_2(var_2.am_Gold,MathUtil.method_29(param1));
      }
      
      private function method_1784(param1:MouseEvent) : void
      {
         var _loc2_:class_9 = null;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         if(var_1.mMammothIdols < this.var_1742)
         {
            var_1.screenBuyIdols.Display(this.var_1742 - var_1.mMammothIdols);
            return;
         }
         if(this.var_320 == const_178)
         {
            _loc2_ = var_1.mBuildingInfo.UpgradeBuilding(this.var_2339,true);
            if(_loc2_)
            {
               var_1.screenUpgrading.Display(_loc2_);
               Hide();
            }
         }
         if(this.var_320 == const_577)
         {
            var_1.screenClassTowers.TrainTalentPoint(new MouseEvent(MouseEvent.CLICK),true);
            var_1.screenTome.Refresh();
            Hide();
         }
         if(this.var_320 == const_441)
         {
            var_1.screenTome.Train(new MouseEvent(MouseEvent.CLICK),true);
            var_1.screenTome.Refresh();
            Hide();
         }
         if(this.var_320 == const_563)
         {
            var_1.screenBarn.TrainOrHatchClicked(new MouseEvent(MouseEvent.CLICK),true);
            var_1.screenBarn.Refresh();
            Hide();
         }
         if(this.var_320 == const_507)
         {
            var_1.mEggPetInfo.TrainPet(this.var_2847,true);
            var_1.screenBarn.Refresh();
            var_1.screenBarn.ResetSelectors();
            Hide();
         }
         if(this.var_320 == const_538)
         {
            var_1.screenDyeGear.OnApplyDyes(new MouseEvent(MouseEvent.CLICK),true);
            var_1.screenDyeGear.Refresh();
            Hide();
         }
      }
      
      private function method_2021(param1:MouseEvent) : void
      {
         Hide();
      }
   }
}
