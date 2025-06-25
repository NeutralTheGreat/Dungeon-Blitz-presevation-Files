package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.net.URLRequest;
   import flash.net.navigateToURL;
   
   public class class_132 extends class_32
   {
      
      private static const const_365:Number = 5;
      
      private static const const_845:Number = 10.4;
      
      private static const const_1154:Number = 4.65;
      
      private static const const_864:Number = 571.95;
      
      private static const const_1148:Number = 44.95;
       
      
      internal var var_1422:class_33;
      
      internal var var_1982:class_33;
      
      internal var mExternalURL:class_33;
      
      internal var var_1001:class_138;
      
      internal var mTooltip:class_33;
      
      internal var var_924:class_138;
      
      internal var var_2128:class_138;
      
      internal var var_1888:class_33;
      
      internal var var_1709:class_33;
      
      public function class_132(param1:Game)
      {
         super(param1,"a_NewsHUD","am_Panel");
         mbHideOnClear = false;
         var_1 = param1;
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_1422 = method_1(var_2);
         this.var_1001 = method_21(var_2.am_TopLeftGroup.am_Title);
         this.var_1982 = method_1(var_2.am_TopLeftGroup.am_IconHolder);
         this.var_1888 = method_5(var_2.am_TopLeftGroup,null,this.method_549,this.HideTooltip);
         this.mExternalURL = method_5(var_2.am_ExternalLink,this.method_1752);
         this.mTooltip = method_1(var_2.am_Tooltip);
         this.var_1709 = method_1(var_2.am_Tooltip.am_TimerGroup);
         this.var_2128 = method_21(this.var_1709.mMovieClip.am_TimeLeftText);
         this.var_924 = method_21(var_2.am_Tooltip.am_TooltipText);
         this.var_924.mTextField.wordWrap = true;
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1982 = null;
         this.mExternalURL = null;
         this.var_1001 = null;
         this.mTooltip = null;
         this.var_1888 = null;
         this.var_924 = null;
         this.var_2128 = null;
         this.var_1709 = null;
      }
      
      override public function Refresh() : void
      {
         if(!var_2)
         {
            return;
         }
         var _loc1_:class_116 = var_1.mNewsData;
         method_12(this.var_1982.mMovieClip,_loc1_.var_2682);
         if(_loc1_.mExternalURL)
         {
            this.mExternalURL.Show();
         }
         else
         {
            this.mExternalURL.Hide();
         }
         MathUtil.method_2(this.var_1001.mTextField,_loc1_.var_1001);
         MathUtil.method_2(this.var_924.mTextField,_loc1_.mTooltip);
         if(_loc1_.var_1001)
         {
            this.var_1888.Show();
         }
         else
         {
            this.var_1888.Hide();
         }
      }
      
      override public function OnTickScreen() : void
      {
         if(!this.mTooltip.mbVisible)
         {
            return;
         }
         var _loc1_:int = var_1.mNewsData.mTimeEnd - var_1.mServerGameTime;
         if(_loc1_ < 0)
         {
            _loc1_ = 0;
         }
         MathUtil.method_2(this.var_2128.mTextField,MathUtil.method_1401(_loc1_));
      }
      
      public function method_1752(param1:MouseEvent) : void
      {
         var _loc2_:String = String(var_1.mNewsData.mExternalURL);
         if(_loc2_)
         {
            navigateToURL(new URLRequest(_loc2_),"_blank");
         }
      }
      
      public function method_549(param1:MouseEvent) : void
      {
         if(!var_1.mNewsData.mTooltip)
         {
            return;
         }
         var _loc2_:MovieClip = this.mTooltip.mMovieClip["am_LeftBorder"] as MovieClip;
         var _loc3_:MovieClip = this.mTooltip.mMovieClip["am_RightBorder"] as MovieClip;
         var _loc4_:MovieClip = this.mTooltip.mMovieClip["am_BottomBorder"] as MovieClip;
         var _loc5_:MovieClip = this.mTooltip.mMovieClip["am_Background"] as MovieClip;
         var _loc6_:Number = this.var_924.mTextField.textHeight;
         var _loc7_:Number = this.var_924.mTextField.textHeight + const_365;
         this.var_924.mTextField.height = _loc7_;
         var _loc8_:Number = const_845 + _loc7_ + const_365;
         this.var_1709.mMovieClip.y = _loc8_;
         var _loc9_:Number = _loc8_ + const_1148 + const_365;
         _loc5_.height = _loc9_ + const_365;
         var _loc10_:Number = _loc9_ / const_864;
         _loc2_.scaleY = _loc3_.scaleY = _loc10_;
         _loc4_.y = const_1154 + _loc2_.height;
         this.mTooltip.Show();
      }
      
      public function HideTooltip(param1:MouseEvent) : void
      {
         this.mTooltip.Hide();
      }
   }
}
