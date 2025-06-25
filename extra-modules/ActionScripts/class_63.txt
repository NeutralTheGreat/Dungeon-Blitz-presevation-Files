package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.external.ExternalInterface;
   import flash.net.URLRequest;
   import flash.net.URLRequestMethod;
   import flash.net.URLVariables;
   import flash.net.navigateToURL;
   import flash.text.TextField;
   
   public class class_63 extends class_32
   {
      
      private static const const_161:uint = 5;
      
      private static const const_162:Vector.<uint> = new Vector.<uint>(const_161 + 1,true);
      
      private static const const_166:Vector.<uint> = new Vector.<uint>(const_161 + 1,true);
      
      private static const const_361:uint = 8;
      
      private static const const_103:Vector.<uint> = new Vector.<uint>(const_361,true);
      
      private static const const_121:Vector.<uint> = new Vector.<uint>(const_361,true);
      
      private static const const_122:Vector.<Number> = new Vector.<Number>(const_361,true);
      
      private static const const_116:Vector.<String> = new Vector.<String>(const_361,true);
      
      {
         const_162[0] = 0;
         const_166[0] = 0;
         const_162[1] = 1;
         const_166[1] = 1;
         const_162[2] = 2;
         const_166[2] = 6;
         const_162[3] = 3;
         const_166[3] = 7;
         const_162[4] = 4;
         const_166[4] = 4;
         const_162[5] = 5;
         const_166[5] = 5;
         const_103[0] = 50;
         const_103[1] = 105;
         const_103[2] = 180;
         const_103[3] = 375;
         const_122[0] = 2.99;
         const_122[1] = 5.99;
         const_122[2] = 9.99;
         const_122[3] = 19.99;
         const_121[0] = 30;
         const_121[1] = 60;
         const_121[2] = 100;
         const_121[3] = 200;
         const_116[0] = "9QQNJJH7RGZTQ";
         const_116[1] = "34D5DGPVPKNDW";
         const_116[2] = "YQJR84UHXP6P2";
         const_116[3] = "BMDSGRY5C4FEL";
         const_103[4] = 1000;
         const_103[5] = 2050;
         const_103[6] = 220;
         const_103[7] = 480;
         const_122[4] = 49.99;
         const_122[5] = 99.99;
         const_122[6] = 11.99;
         const_122[7] = 24.99;
         const_121[4] = 500;
         const_121[5] = 1000;
         const_121[6] = 120;
         const_121[7] = 250;
         const_116[4] = "YAPMVT7PBQGJE";
         const_116[5] = "YAGXMFQJEZR5J";
         const_116[6] = "WUPTFRTXUZL24";
         const_116[7] = "5TWEH5VL9H82Y";
      }
      
      internal var var_1895:uint;
      
      internal var var_2633:Boolean;
      
      internal var var_1383:Vector.<TextField>;
      
      internal var var_2010:Vector.<TextField>;
      
      internal var var_1756:Vector.<MovieClip>;
      
      internal var var_2357:class_33;
      
      internal var var_2552:MovieClip;
      
      internal var var_2463:MovieClip;
      
      public function class_63(param1:Game)
      {
         super(param1,"a_MammothIdolWindow","am_Panel");
         var_15 = true;
         var_45 = "FadeIn";
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:MovieClip = null;
         this.var_1383 = new Vector.<TextField>(const_161,true);
         this.var_2010 = new Vector.<TextField>(const_161,true);
         this.var_1756 = new Vector.<MovieClip>(const_161,true);
         var _loc2_:uint = 0;
         while(_loc2_ < const_161)
         {
            _loc1_ = var_2["am_Cell" + (_loc2_ + 1)];
            this.var_1383[_loc2_] = _loc1_.am_Price;
            this.var_2010[_loc2_] = _loc1_.am_IdolCount;
            this.var_1756[_loc2_] = _loc1_.am_KredIcon;
            method_117(_loc1_,_loc2_,this.method_1165);
            _loc2_++;
         }
         this.var_2552 = var_2.am_TitleBuy;
         this.var_2463 = var_2.am_TitleNotEnough;
         this.var_2357 = method_5(var_2.am_EarnFreeIdols,this.method_1009);
         method_23(var_2.am_Exit);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1383 = null;
         this.var_2010 = null;
         this.var_2552 = null;
         this.var_2463 = null;
         this.var_2357 = null;
      }
      
      private function method_988(param1:uint) : uint
      {
         var _loc2_:uint = !!var_1.mbShowHigher ? uint(param1 + 1) : param1;
         return this.var_2633 ? const_166[_loc2_] : const_162[_loc2_];
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc2_:uint = 0;
         var _loc1_:uint = 0;
         while(_loc1_ < const_161)
         {
            _loc2_ = this.method_988(_loc1_);
            if(var_1.clientKongID)
            {
               this.var_1756[_loc1_].visible = true;
               MathUtil.method_2(this.var_1383[_loc1_],String(const_121[_loc2_]));
            }
            else
            {
               this.var_1756[_loc1_].visible = false;
               MathUtil.method_2(this.var_1383[_loc1_],"$" + String(const_122[_loc2_]));
            }
            MathUtil.method_2(this.var_2010[_loc1_],String(const_103[_loc2_]));
            _loc1_++;
         }
         if(this.var_1895)
         {
            MathUtil.method_2(var_2.am_Title,"You need " + this.var_1895 + " more Mammoth Idol" + (this.var_1895 > 1 ? "s" : ""));
         }
         else
         {
            MathUtil.method_2(var_2.am_Title,"Purchase Mammoth Idols");
         }
         this.var_2357.Hide();
      }
      
      public function OnInitDisplay(param1:uint, param2:Boolean = false) : void
      {
         this.var_1895 = param1;
         this.var_2633 = param2;
      }
      
      private function method_1009(param1:MouseEvent) : void
      {
         if(ExternalInterface.available && Boolean(var_1.clientFacebookID))
         {
            ExternalInterface.call("JSStartEarn");
         }
      }
      
      private function method_1165(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:uint = this.method_988(param2);
         if(ExternalInterface.available && Boolean(var_1.clientFacebookID))
         {
            ExternalInterface.call("JSStartOrder","BuyIdols" + _loc3_ + ":" + var_1.clientUserID);
         }
         else if(ExternalInterface.available && Boolean(var_1.clientKongID))
         {
            ExternalInterface.call("JSStartOrder","buyidols" + _loc3_ + ":" + var_1.clientUserID);
         }
         else
         {
            this.method_1131(_loc3_);
            Hide();
         }
      }
      
      public function method_1131(param1:uint) : void
      {
         var _loc2_:uint = uint(var_1.clientUserID);
         var _loc3_:uint = uint(var_1.clientUserID);
         var _loc4_:uint = uint(var_1.mServerGameTime);
         var _loc5_:String = Crypto.method_164("#b#" + _loc2_ + "#m#" + _loc4_ + "#g#" + _loc3_ + "#i#");
         var _loc6_:URLRequest;
         (_loc6_ = new URLRequest("https://www.paypal.com/cgi-bin/webscr")).method = URLRequestMethod.POST;
         _loc6_.data = new URLVariables();
         _loc6_.data.cmd = "_s-xclick";
         _loc6_.data.custom = _loc2_ + ":" + _loc4_ + ":" + _loc3_ + ":" + _loc5_;
         _loc6_.data.hosted_button_id = const_116[param1];
         navigateToURL(_loc6_,"_blank");
      }
   }
}
