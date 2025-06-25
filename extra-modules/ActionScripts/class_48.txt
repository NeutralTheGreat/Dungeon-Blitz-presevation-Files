package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.external.ExternalInterface;
   import flash.net.URLRequest;
   import flash.net.navigateToURL;
   import flash.text.StyleSheet;
   import flash.text.TextField;
   
   public class class_48 extends class_32
   {
      
      private static const const_1281:String = "\'The perfect flash MMO\'<br/>-<a href=\'http://mmoreporter.com/2012/03/29/mmo-reporter-episode-72-why-do-i-like-dungeon-blitz/\'>MMOReporter.com </a><br/><br/>\'The fact that it\'s a free to play game only makes me feel happier\'<br/>-<a href=\'http://vgvee.com/2012/04/dungeon-blitz-the-review/\'>VGVee.com </a>";
      
      private static const const_995:String = "\'I can\'t wait to continue playing\'<br/>-<a href=\'http://www.gamexplain.com/article-714-1333038975-dungeon-blitz-initial-impressions.html\'>Gamexplain.com </a><br/><br/>\'Whether you play in short bursts or sink chunks of time, this is your game\'<br/>-<a href=\'http://www.mmohunter.com/dungeon-blitz.html\'>MMOHunter.com </a>";
      
      private static const const_1393:uint = 480;
      
      private static const const_1323:uint = 350;
       
      
      internal var var_1986:class_33;
      
      internal var var_1935:class_33;
      
      internal var var_339:MovieClip;
      
      internal var var_2367:MovieClip;
      
      internal var var_2262:MovieClip;
      
      public function class_48(param1:Game)
      {
         super(param1,"a_LinkBar",null);
         var_15 = true;
         mbHideOnClear = false;
      }
      
      override public function OnCreateScreen() : void
      {
         method_10(var_2.am_News,this.method_1760);
         method_10(var_2.am_Forums,this.method_1619);
         method_10(var_2.am_About,this.method_1329);
         method_10(var_2.am_Contact,this.method_1001);
         this.var_1986 = method_10(var_2.am_Like,this.method_1174);
         this.var_1935 = method_10(var_2.am_Invite,this.method_1486);
         this.var_339 = var_2.am_AboutBox;
         this.var_2367 = this.var_339.am_AboutMatte;
         method_10(this.var_339.am_OK,this.method_1573);
         method_10(this.var_339.am_BlueMammoth,this.method_1377);
         var _loc1_:MovieClip = this.var_339.am_YouTubeVid;
         method_10(_loc1_,this.method_1783);
         this.var_2262 = _loc1_.am_Image;
         var _loc2_:StyleSheet = new StyleSheet();
         _loc2_.setStyle("a:link",{"color":"#7FFFFF"});
         _loc2_.setStyle("a:hover",{
            "color":"#7FFFFF",
            "textDecoration":"underline"
         });
         _loc2_.setStyle("a:active",{
            "color":"#CFFFFF",
            "textDecoration":"underline"
         });
         var _loc3_:TextField = this.var_339.am_Reviews1;
         _loc3_.styleSheet = _loc2_;
         MathUtil.method_2(_loc3_,const_1281,true);
         _loc3_ = this.var_339.am_Reviews2;
         _loc3_.styleSheet = _loc2_;
         MathUtil.method_2(_loc3_,const_995,true);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.method_270();
         this.var_1986 = null;
         this.var_1935 = null;
         this.var_339 = null;
         this.var_2367 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         if(var_1.mbPageIsLiked)
         {
            this.var_1986.Hide();
            this.var_1935.Show();
         }
         else
         {
            this.var_1986.Show();
            this.var_1935.Hide();
         }
         this.var_2367.visible = var_1.gameState != Game.STATE_PLAY;
         var _loc1_:Number = Number(var_1.main.overallScale);
         var _loc2_:Number = _loc1_ > 1 ? 1 / _loc1_ : 1;
         this.var_2262.scaleX = _loc2_;
         this.var_2262.scaleY = _loc2_;
      }
      
      public function OnInitDisplay() : void
      {
         this.method_270();
         if(var_1.clientKongID)
         {
            var_1.mbPageIsLiked = true;
         }
      }
      
      private function method_270() : void
      {
         this.var_339.visible = false;
      }
      
      private function method_1977() : void
      {
         this.var_339.visible = true;
      }
      
      public function method_54(param1:int) : Boolean
      {
         if(mbVisible && this.var_339 && this.var_339.visible && param1 == Game.const_240)
         {
            this.method_270();
            return true;
         }
         return false;
      }
      
      private function method_1760(param1:MouseEvent) : void
      {
         var _loc2_:String = !!var_1.clientFacebookID ? "http://www.facebook.com/DungeonBlitz" : "http://www.dungeonblitz.com/news/";
         navigateToURL(new URLRequest(_loc2_),"_blank");
      }
      
      private function method_1619(param1:MouseEvent) : void
      {
         var _loc2_:String = !!var_1.clientKongID ? "http://www.kongregate.com/forums/211-dungeon-blitz" : "http://www.dungeonblitz.com/forums/";
         navigateToURL(new URLRequest(_loc2_),"_blank");
      }
      
      private function method_1001(param1:MouseEvent) : void
      {
         navigateToURL(new URLRequest("http://www.bluemammoth.com/contact/"),"_blank");
      }
      
      private function method_1377(param1:MouseEvent) : void
      {
         navigateToURL(new URLRequest("http://www.bluemammoth.com/"),"_blank");
      }
      
      private function method_1783(param1:MouseEvent) : void
      {
         navigateToURL(new URLRequest("http://www.youtube.com/watch?v=She67udLfSA"),"_blank");
      }
      
      private function method_1329(param1:MouseEvent) : void
      {
         if(this.var_339.visible)
         {
            this.method_270();
         }
         else
         {
            this.method_1977();
         }
      }
      
      private function method_1573(param1:MouseEvent) : void
      {
         this.method_270();
      }
      
      private function method_1174(param1:MouseEvent) : void
      {
         navigateToURL(new URLRequest("http://www.facebook.com/DungeonBlitz"),"_blank");
         if(var_1.clientFacebookID)
         {
            var_1.mbPageIsLiked = true;
         }
         Refresh();
      }
      
      private function method_1486(param1:MouseEvent) : void
      {
         if(ExternalInterface.available)
         {
            ExternalInterface.call("JSInviteFriend");
         }
      }
   }
}
