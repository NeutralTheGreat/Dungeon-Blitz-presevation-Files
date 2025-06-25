package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   
   public class class_109 extends class_32
   {
      
      private static const const_1247:uint = 129;
      
      private static const const_633:uint = 144;
      
      private static const const_964:uint = 169;
      
      private static const const_1227:String = "Replace and Destroy this charm?";
      
      private static const const_1147:String = "Remove and Recover this charm?";
      
      private static const const_1074:String = "With this Charm below";
      
      private static const const_1063:String = "Using the Charm Remover";
       
      
      internal var var_725:uint;
      
      internal var var_25:class_64;
      
      internal var var_83:class_64;
      
      internal var var_1453:uint;
      
      internal var var_616:class_33;
      
      internal var mIconHolder2:class_33;
      
      internal var var_1422:class_33;
      
      internal var var_346:class_33;
      
      internal var var_198:class_33;
      
      internal var var_123:class_33;
      
      internal var var_291:class_33;
      
      internal var mPanel2:class_33;
      
      internal var mBaseWindow2:class_33;
      
      internal var mPrimaryColor2:class_33;
      
      internal var mSecondaryColor2:class_33;
      
      internal var mTertiaryColor2:class_33;
      
      internal var var_987:Boolean;
      
      public function class_109(param1:Game)
      {
         super(param1,"a_Popup_Replace","am_PromptPanel");
         var_15 = true;
         var_45 = "FadeIn";
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:MovieClip = var_2.am_CharmPanel1;
         var _loc2_:MovieClip = var_2.am_CharmPanel2;
         this.var_616 = method_1(_loc1_.am_CharmHolder);
         this.mIconHolder2 = method_1(_loc2_.am_CharmHolder);
         this.var_346 = method_1(_loc1_.am_Base);
         this.var_198 = method_1(_loc1_.am_PrimaryColor);
         this.var_123 = method_1(_loc1_.am_SecondaryColor);
         this.var_291 = method_1(_loc1_.am_TertiaryColor);
         this.mBaseWindow2 = method_1(_loc2_.am_Base);
         this.mPrimaryColor2 = method_1(_loc2_.am_PrimaryColor);
         this.mSecondaryColor2 = method_1(_loc2_.am_SecondaryColor);
         this.mTertiaryColor2 = method_1(_loc2_.am_TertiaryColor);
         this.var_1422 = method_1(_loc1_);
         this.mPanel2 = method_1(_loc2_);
         method_10(_loc2_.am_Base.am_Replace,this.method_1373);
         method_23(_loc2_.am_Base.am_Cancel);
         method_23(var_2.am_Exit);
         _loc1_.am_TertiaryStat.mouseEnabled = false;
         _loc2_.am_TertiaryStat.mouseEnabled = false;
      }
      
      override public function OnDestroyScreen() : void
      {
         method_14(this.var_616.mMovieClip.am_IconHolder);
         method_14(this.mIconHolder2.mMovieClip.am_IconHolder);
         this.var_616 = null;
         this.mIconHolder2 = null;
         this.var_25 = null;
         this.var_83 = null;
         this.var_198 = null;
         this.var_123 = null;
         this.var_346 = null;
         this.mBaseWindow2 = null;
         this.mPrimaryColor2 = null;
         this.mSecondaryColor2 = null;
         this.mTertiaryColor2 = null;
         this.var_1422 = null;
         this.mPanel2 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         if(!this.var_25 || !this.var_83)
         {
            return;
         }
         var _loc1_:MovieClip = this.var_1422.mMovieClip;
         this.var_83.method_78(this,this.var_616.mMovieClip.am_IconHolder);
         var _loc2_:class_1 = this.var_83.method_115();
         if(this.var_25.method_379())
         {
            MathUtil.method_2(var_2.am_CharmPanel1.am_HeaderText,const_1147);
            MathUtil.method_2(var_2.am_CharmPanel2.am_HeaderText,const_1063);
         }
         else
         {
            MathUtil.method_2(var_2.am_CharmPanel1.am_HeaderText,const_1227);
            MathUtil.method_2(var_2.am_CharmPanel2.am_HeaderText,const_1074);
         }
         if(this.var_83.method_118())
         {
            this.var_346.PlayAnimation("TriStat");
            this.var_291.Show();
            this.var_123.Show();
            this.var_198.PlayAnimation(this.var_83.var_13.var_1321);
            this.var_123.PlayAnimation(this.var_83.var_13.var_1560);
            this.var_291.PlayAnimation(this.var_83.var_13.var_1510);
            MathUtil.method_8(_loc1_.am_Name,this.var_83.var_13.displayName,ScreenArmory.const_23);
            MathUtil.method_2(_loc1_.am_PrimaryStat,this.var_83.var_13.var_1327);
            MathUtil.method_2(_loc1_.am_SecondaryStat,this.var_83.var_13.var_1397);
            MathUtil.method_2(_loc1_.am_TertiaryStat,this.var_83.var_13.var_1617);
            this.mPanel2.mMovieClip.y = const_964;
         }
         else if(this.var_83.method_124())
         {
            this.var_346.PlayAnimation("DualStat");
            this.var_291.Hide();
            this.var_123.Show();
            this.var_198.PlayAnimation(this.var_83.var_13.var_1482);
            this.var_123.PlayAnimation(this.var_83.var_13.var_1353);
            MathUtil.method_8(_loc1_.am_Name,this.var_83.var_13.displayName,ScreenArmory.const_22);
            MathUtil.method_2(_loc1_.am_PrimaryStat,this.var_83.var_13.var_1339);
            MathUtil.method_2(_loc1_.am_SecondaryStat,this.var_83.var_13.var_1513);
            MathUtil.method_2(_loc1_.am_TertiaryStat,"");
            this.mPanel2.mMovieClip.y = const_633;
         }
         else if(!_loc2_)
         {
            this.var_346.PlayAnimation("SingleStat");
            this.var_123.Hide();
            this.var_291.Hide();
            this.var_198.PlayAnimation(this.var_83.var_13.var_115);
            MathUtil.method_8(_loc1_.am_Name,this.var_83.method_49(),ScreenArmory.const_24);
            MathUtil.method_2(_loc1_.am_PrimaryStat,this.var_83.var_13.var_203);
            MathUtil.method_2(_loc1_.am_SecondaryStat,"");
            MathUtil.method_2(_loc1_.am_TertiaryStat,"");
            this.mPanel2.mMovieClip.y = const_1247;
         }
         else
         {
            this.var_346.PlayAnimation("DualStat");
            this.var_291.Hide();
            this.var_123.Show();
            this.var_123.PlayAnimation(_loc2_.var_115);
            this.var_198.PlayAnimation(this.var_83.var_13.var_115);
            MathUtil.method_2(_loc1_.am_PrimaryStat,this.var_83.var_13.var_203);
            MathUtil.method_2(_loc1_.am_SecondaryStat,this.var_83.method_171());
            MathUtil.method_2(_loc1_.am_TertiaryStat,"");
            this.mPanel2.mMovieClip.y = const_633;
            if(this.var_83.var_8 == class_64.const_341)
            {
               MathUtil.method_8(_loc1_.am_Name,this.var_83.method_49(),ScreenArmory.const_22);
            }
            else if(this.var_83.var_8 == class_64.const_312)
            {
               MathUtil.method_8(_loc1_.am_Name,this.var_83.method_49(),ScreenArmory.const_23);
            }
         }
         _loc1_ = this.mPanel2.mMovieClip;
         this.var_25.method_78(this,this.mIconHolder2.mMovieClip.am_IconHolder);
         _loc2_ = this.var_25.method_115();
         if(this.var_25.method_118())
         {
            this.mBaseWindow2.PlayAnimation("TriStat");
            MathUtil.method_8(_loc1_.am_Name,this.var_25.var_13.displayName,ScreenArmory.const_23);
            MathUtil.method_2(_loc1_.am_PrimaryStat,this.var_25.var_13.var_1327);
            MathUtil.method_2(_loc1_.am_SecondaryStat,this.var_25.var_13.var_1397);
            MathUtil.method_2(_loc1_.am_TertiaryStat,this.var_25.var_13.var_1617);
            this.mSecondaryColor2.Show();
            this.mTertiaryColor2.Show();
            this.mPrimaryColor2.PlayAnimation(this.var_25.var_13.var_1321);
            this.mSecondaryColor2.PlayAnimation(this.var_25.var_13.var_1560);
            this.mTertiaryColor2.PlayAnimation(this.var_25.var_13.var_1510);
         }
         else if(this.var_25.method_124())
         {
            this.mBaseWindow2.PlayAnimation("DualStat");
            MathUtil.method_8(_loc1_.am_Name,this.var_25.var_13.displayName,ScreenArmory.const_22);
            MathUtil.method_2(_loc1_.am_PrimaryStat,this.var_25.var_13.var_1339);
            MathUtil.method_2(_loc1_.am_SecondaryStat,this.var_25.var_13.var_1513);
            MathUtil.method_2(_loc1_.am_TertiaryStat,"");
            this.mSecondaryColor2.Show();
            this.mTertiaryColor2.Hide();
            this.mPrimaryColor2.PlayAnimation(this.var_25.var_13.var_1482);
            this.mSecondaryColor2.PlayAnimation(this.var_25.var_13.var_1353);
         }
         else if(!_loc2_)
         {
            this.mBaseWindow2.PlayAnimation("SingleStat");
            this.mPrimaryColor2.PlayAnimation(this.var_25.var_13.var_115);
            this.mSecondaryColor2.Hide();
            this.mTertiaryColor2.Hide();
            MathUtil.method_8(_loc1_.am_Name,this.var_25.method_49(),ScreenArmory.const_24);
            MathUtil.method_2(_loc1_.am_PrimaryStat,this.var_25.var_13.var_203);
            MathUtil.method_2(_loc1_.am_SecondaryStat,"");
            MathUtil.method_2(_loc1_.am_TertiaryStat,"");
         }
         else
         {
            this.mBaseWindow2.PlayAnimation("DualStat");
            this.mPrimaryColor2.PlayAnimation(this.var_25.var_13.var_115);
            this.mTertiaryColor2.Hide();
            this.mSecondaryColor2.Show();
            this.mSecondaryColor2.PlayAnimation(_loc2_.var_115);
            MathUtil.method_2(_loc1_.am_PrimaryStat,this.var_25.var_13.var_203);
            MathUtil.method_2(_loc1_.am_SecondaryStat,this.var_25.method_171());
            MathUtil.method_2(_loc1_.am_TertiaryStat,"");
            if(this.var_25.var_8 == class_64.const_341)
            {
               MathUtil.method_8(_loc1_.am_Name,this.var_25.method_49(),ScreenArmory.const_22);
            }
            else if(this.var_25.var_8 == class_64.const_312)
            {
               MathUtil.method_8(_loc1_.am_Name,this.var_25.method_49(),ScreenArmory.const_23);
            }
         }
         this.var_987 = false;
      }
      
      public function OnInitDisplay(param1:class_64, param2:uint, param3:uint, param4:class_64) : void
      {
         this.var_25 = param1;
         this.var_725 = param2;
         this.var_1453 = param3;
         this.var_83 = param4;
      }
      
      public function method_1373(param1:MouseEvent) : void
      {
         if(!this.var_987 && class_78.method_416(this,this.var_725,this.var_1453,this.var_25))
         {
            this.var_987 = true;
         }
      }
   }
}
