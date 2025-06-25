package
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   
   public class class_124 extends class_32
   {
       
      
      internal var var_2179:MovieClip;
      
      internal var var_2431:MovieClip;
      
      internal var var_1968:class_33;
      
      internal var var_1758:class_33;
      
      internal var var_700:class_33;
      
      internal var var_1539:class_33;
      
      internal var var_1496:class_33;
      
      public function class_124(param1:Game)
      {
         super(param1,"a_Menu","am_MenuWrapper");
         var_15 = true;
      }
      
      override public function OnCreateScreen() : void
      {
         method_23(var_2.am_Exit);
         method_23(var_2.am_Close);
         method_5(var_2.am_Keybindings,this.method_1037);
         this.var_1968 = method_5(var_2.am_ProfaneFilter,this.method_1962);
         this.var_1539 = method_17(var_2.am_SoundProg,"Progress",0);
         this.var_2179 = method_313(var_2.am_SoundSlider,this.method_1679,this.method_1951,0.05);
         this.var_1496 = method_17(var_2.am_MusicProg,"Progress",0);
         this.var_2431 = method_313(var_2.am_MusicSlider,this.method_1313,this.method_1057,0.05);
         this.var_1758 = method_5(var_2.am_FloaterFilter,this.method_1683);
         this.var_700 = method_5(var_2.am_InviteOption,this.method_1275);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_2179 = null;
         this.var_2431 = null;
         this.var_1968 = null;
         this.var_1539 = null;
         this.var_1496 = null;
         this.var_1758 = null;
         this.var_700 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         this.var_1968.mMovieClip.am_CheckMark.visible = var_1.bProfaneFilter;
         this.var_1758.mMovieClip.am_CheckMark.visible = var_1.bShowGroupFloaters;
         this.var_700.mMovieClip.am_CheckMark.visible = var_1.bIgnoreStrangerInvites;
         var _loc1_:Number = SoundManager.var_597;
         class_136.method_330(this.var_2179,_loc1_);
         this.var_1539.mHealthPerc = _loc1_;
         var _loc2_:Number = SoundManager.method_920(Main.const_77);
         class_136.method_330(this.var_2431,_loc2_);
         this.var_1496.mHealthPerc = _loc2_;
      }
      
      override public function OnClearScreen() : void
      {
         var_1.screenLinkBar.Hide();
      }
      
      public function OnInitDisplay() : void
      {
         var_1.screenLinkBar.Display();
      }
      
      public function method_1962(param1:Event) : void
      {
         var_1.bProfaneFilter = !var_1.bProfaneFilter;
         this.var_1968.mMovieClip.am_CheckMark.visible = var_1.bProfaneFilter;
         var_1.StoreGameInfo();
      }
      
      public function method_1683(param1:Event) : void
      {
         var_1.bShowGroupFloaters = !var_1.bShowGroupFloaters;
         this.var_1758.mMovieClip.am_CheckMark.visible = var_1.bShowGroupFloaters;
         var_1.StoreGameInfo();
      }
      
      public function method_1275(param1:Event) : void
      {
         var_1.bIgnoreStrangerInvites = !var_1.bIgnoreStrangerInvites;
         this.var_700.mMovieClip.am_CheckMark.visible = var_1.bIgnoreStrangerInvites;
      }
      
      public function method_1679(param1:Number) : void
      {
         SoundManager.SetSoundVolume(param1);
         SoundManager.method_218(Main.const_108,param1);
         var_1.StoreGameInfo();
      }
      
      public function method_1313(param1:Number) : void
      {
         SoundManager.method_218(Main.const_77,param1);
         var_1.StoreGameInfo();
      }
      
      public function method_1951(param1:Number) : void
      {
         SoundManager.SetSoundVolume(param1);
         SoundManager.method_218(Main.const_108,param1);
         this.var_1539.mHealthPerc = param1;
         this.var_1539.TickMovieClip();
      }
      
      public function method_1057(param1:Number) : void
      {
         SoundManager.method_218(Main.const_77,param1);
         this.var_1496.mHealthPerc = param1;
         this.var_1496.TickMovieClip();
      }
      
      public function method_1037(param1:MouseEvent) : void
      {
         var_1.screenKeybind.Display();
      }
   }
}
