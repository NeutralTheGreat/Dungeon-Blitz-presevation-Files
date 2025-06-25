package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   
   public class class_120 extends class_32
   {
      
      private static const const_360:uint = 4;
       
      
      private var var_1491:class_33;
      
      private var var_1642:Vector.<class_33>;
      
      private var var_1504:Vector.<class_138>;
      
      private var var_551:Vector.<class_103>;
      
      public function class_120(param1:Game)
      {
         super(param1,"a_ScreenCatalyst",null);
         var_15 = true;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:MovieClip = null;
         this.var_1642 = new Vector.<class_33>(const_360,true);
         this.var_1504 = new Vector.<class_138>(const_360,true);
         _loc1_ = 0;
         while(_loc1_ < const_360)
         {
            _loc2_ = var_2["am_Slot" + _loc1_] as MovieClip;
            this.var_1642[_loc1_] = method_3(_loc2_,_loc1_,this.method_1697,this.method_1617,this.HideTooltip);
            this.var_1504[_loc1_] = method_21(_loc2_.am_Quantity);
            _loc1_++;
         }
         this.var_551 = new Vector.<class_103>();
         this.var_1491 = method_5(var_2.am_Remove,this.method_1891,this.method_1723,this.HideTooltip);
         method_23(var_2.am_Close);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1491 = null;
         this.var_1642 = null;
         this.var_1504 = null;
         this.var_551 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:uint = 0;
         var _loc3_:class_103 = null;
         var _loc2_:uint = this.var_551.length;
         _loc1_ = 0;
         while(_loc1_ < const_360)
         {
            if(_loc1_ >= _loc2_)
            {
               method_14(this.var_1642[_loc1_].mMovieClip.am_ItemIconHolder);
               this.var_1504[_loc1_].SetText("");
            }
            else
            {
               _loc3_ = this.var_551[_loc1_];
               method_12(this.var_1642[_loc1_].mMovieClip.am_ItemIconHolder,_loc3_.consumableType.iconName);
               this.var_1504[_loc1_].SetText("x" + _loc3_.stackCount);
            }
            _loc1_++;
         }
      }
      
      public function OnInitDisplay() : void
      {
         this.method_1242();
      }
      
      private function method_1891(param1:MouseEvent) : void
      {
         Hide();
         var_1.screenForge.ClearCatalyst();
      }
      
      private function method_1723(param1:MouseEvent) : void
      {
         var_1.screenHudTooltip.ShowSimpleTooltip("Remove Catalyst",583.05,412.95);
      }
      
      private function method_1697(param1:MouseEvent, param2:uint) : void
      {
         if(param2 >= this.var_551.length)
         {
            return;
         }
         var _loc3_:class_103 = this.var_551[param2];
         if(!_loc3_ || !_loc3_.stackCount)
         {
            return;
         }
         Hide();
         var_1.screenForge.SetCatalyst(_loc3_.consumableType);
      }
      
      private function method_1617(param1:MouseEvent, param2:uint) : void
      {
         if(param2 >= this.var_551.length)
         {
            return;
         }
         var _loc3_:class_103 = this.var_551[param2];
         if(!_loc3_ || !_loc3_.stackCount)
         {
            return;
         }
         var _loc4_:class_3 = _loc3_.consumableType;
         var_1.screenHudTooltip.ShowBasicDescriptionTooltip(_loc4_.displayName,"Catalyst",_loc4_.var_8,_loc4_.description,583.05,412.95);
      }
      
      private function HideTooltip(param1:MouseEvent, param2:uint = 0) : void
      {
         var_1.screenHudTooltip.HideTooltip(true);
      }
      
      private function method_1242() : void
      {
         var _loc1_:class_103 = null;
         var _loc3_:uint = 0;
         this.var_551.length = 0;
         var _loc2_:Array = var_1.mOwnedConsumables;
         var _loc4_:uint = _loc2_.length;
         _loc3_ = 0;
         while(_loc3_ < _loc4_)
         {
            _loc1_ = _loc2_[_loc3_];
            if(_loc1_ && _loc1_.stackCount && _loc1_.consumableType.type == "Catalyst")
            {
               this.var_551.push(_loc1_);
            }
            _loc3_++;
         }
      }
   }
}
