package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.net.URLRequest;
   import flash.net.navigateToURL;
   import flash.ui.Keyboard;
   
   public class ScreenLogin
   {
       
      
      internal var var_1:Game;
      
      internal var var_49:MovieClip;
      
      internal var var_1622:class_33 = null;
      
      internal var var_1628:class_33 = null;
      
      internal var var_337:class_33 = null;
      
      internal var var_331:MovieClip = null;
      
      internal var var_1376:Boolean = false;
      
      public function ScreenLogin(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1769() : void
      {
         if(this.var_49)
         {
            this.var_1622.DestroyUIMovieClip();
            this.var_1622 = null;
            this.var_1628.DestroyUIMovieClip();
            this.var_1628 = null;
            this.var_337.DestroyUIMovieClip();
            this.var_337 = null;
            this.var_331 = null;
            this.var_49.am_Forgot.removeEventListener(MouseEvent.CLICK,this.method_613);
         }
         if(Boolean(this.var_49) && Boolean(this.var_49.parent))
         {
            this.var_49.parent.removeChild(this.var_49);
         }
         this.var_49 = null;
         this.var_1 = null;
      }
      
      public function Hide() : void
      {
         this.var_1.method_158(this.var_49);
      }
      
      public function method_40() : Boolean
      {
         return Boolean(this.var_49) && this.var_49.visible;
      }
      
      public function Display() : void
      {
         if(!this.var_49)
         {
            this.var_49 = class_4.method_16("a_LoginSplash",true);
            this.var_49.visible = false;
            this.var_1622 = new class_33(this.var_1,this.var_49.am_LoginButton);
            this.var_1622.BecomeButton("Ready","Over","Click",this.method_1482,false);
            this.var_1628 = new class_33(this.var_1,this.var_49.am_CancelLogin);
            this.var_1628.BecomeButton("Ready","Over","Click",this.method_1661,false);
            this.var_337 = new class_33(this.var_1,this.var_49.am_SavePass);
            this.var_337.BecomeButton("Ready","Over","Click",this.method_411);
            this.var_331 = this.var_337.mMovieClip.am_CheckMark;
            this.var_49.am_Forgot.addEventListener(MouseEvent.CLICK,this.method_613);
            MathUtil.method_2(this.var_49.am_Email,"");
            MathUtil.method_2(this.var_49.am_Password,"");
         }
         if(!this.var_49.visible)
         {
            this.var_1.method_127();
            this.var_49.visible = true;
            this.var_1.var_89.addChildAt(this.var_49,0);
         }
         var _loc1_:Object = this.var_1.var_164.data;
         if(_loc1_.dbUserEmail)
         {
            MathUtil.method_2(this.var_49.am_Email,_loc1_.dbUserEmail);
         }
         else
         {
            MathUtil.method_2(this.var_49.am_Email,"");
            this.var_1.main.stage.focus = this.var_49.am_Email;
         }
         this.var_331.visible = true;
         if(_loc1_.dbPassHash)
         {
            this.var_1376 = true;
            MathUtil.method_2(this.var_49.am_Password,"************");
            this.var_49.am_Password.selectable = false;
            this.var_49.am_Password.tabEnabled = false;
         }
         else
         {
            this.var_1376 = false;
            MathUtil.method_2(this.var_49.am_Password,"");
            this.var_49.am_Password.selectable = true;
            this.var_49.am_Password.tabEnabled = true;
            if(_loc1_.dbUserEmail)
            {
               this.var_1.main.stage.focus = this.var_49.am_Password;
            }
         }
      }
      
      public function method_613(param1:MouseEvent) : void
      {
         if(this.var_1.method_47())
         {
            return;
         }
         navigateToURL(new URLRequest("http://www.dungeonblitz.com/lostpw"),"_blank");
      }
      
      public function method_411(param1:MouseEvent) : void
      {
         var _loc2_:Object = null;
         if(this.var_1.method_47())
         {
            return;
         }
         if(!this.var_331.visible)
         {
            this.var_331.visible = true;
         }
         else
         {
            this.var_331.visible = false;
            this.var_49.am_Password.selectable = true;
            this.var_49.am_Password.tabEnabled = true;
            if(this.var_1376)
            {
               MathUtil.method_2(this.var_49.am_Password,"");
            }
            this.var_1376 = false;
            _loc2_ = this.var_1.var_164.data;
            _loc2_.dbPassHash = "";
            try
            {
               this.var_1.var_164.flush();
            }
            catch(error:Error)
            {
            }
         }
      }
      
      public function method_1774() : void
      {
         if(!this.var_49 || !this.var_49.visible)
         {
            return;
         }
         this.var_1622.TickMovieClip();
         this.var_1628.TickMovieClip();
         this.var_337.TickMovieClip();
      }
      
      public function method_54(param1:int) : Boolean
      {
         if(this.method_40() && !this.var_1.method_47())
         {
            if(param1 == Keyboard.ENTER)
            {
               this.method_805();
               return true;
            }
            if(param1 == Keyboard.ESCAPE)
            {
               this.method_646();
               return true;
            }
         }
         return false;
      }
      
      public function method_1482(param1:MouseEvent) : void
      {
         if(!this.var_1.method_47())
         {
            this.method_805();
         }
      }
      
      public function method_1661(param1:MouseEvent) : void
      {
         if(!this.var_1.method_47())
         {
            this.method_646();
         }
      }
      
      private function method_646() : void
      {
         if(this.var_1.var_1198)
         {
            this.var_1.var_273.Display();
         }
         else
         {
            this.var_1.var_341.Display();
         }
      }
      
      private function method_805() : void
      {
         var _loc1_:String = String(this.var_49.am_Email.text);
         var _loc2_:String = String(this.var_49.am_Password.text);
         var _loc3_:Boolean = this.var_331.visible;
         if(!_loc1_ || _loc1_.indexOf(" ") != -1 || _loc1_.indexOf("@") == -1 || _loc1_.indexOf(".") == -1)
         {
            this.var_1.var_94.method_71("You must enter a valid email address",true);
            return;
         }
         var _loc4_:String = this.var_1376 ? String(this.var_1.var_164.data.dbPassHash) : Crypto.method_164("#bmg#" + _loc2_);
         this.var_1.method_267(_loc1_,_loc4_,_loc3_,false);
      }
   }
}
