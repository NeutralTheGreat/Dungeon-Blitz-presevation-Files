package
{
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.net.URLRequest;
   import flash.net.navigateToURL;
   import flash.ui.Keyboard;
   
   public class ScreenNewAccount
   {
       
      
      internal var var_1:Game;
      
      internal var var_55:MovieClip;
      
      internal var var_1384:class_33 = null;
      
      internal var var_1334:class_33 = null;
      
      internal var var_1611:class_33 = null;
      
      internal var var_337:class_33 = null;
      
      internal var var_1296:class_33 = null;
      
      internal var var_1196:class_33 = null;
      
      internal var var_331:MovieClip = null;
      
      internal var var_1259:MovieClip = null;
      
      internal var var_897:MovieClip = null;
      
      internal var var_37:Boolean = false;
      
      internal var var_70:Entity = null;
      
      public function ScreenNewAccount(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1921() : void
      {
         if(this.var_55)
         {
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_55.am_Terms);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_55.am_Privacy);
            this.var_1384.DestroyUIMovieClip();
            this.var_1384 = null;
            this.var_1334.DestroyUIMovieClip();
            this.var_1334 = null;
            this.var_1611.DestroyUIMovieClip();
            this.var_1611 = null;
            this.var_337.DestroyUIMovieClip();
            this.var_337 = null;
            this.var_1296.DestroyUIMovieClip();
            this.var_1296 = null;
            this.var_1196.DestroyUIMovieClip();
            this.var_1196 = null;
            this.var_331 = null;
            this.var_1259 = null;
            this.var_897 = null;
         }
         if(Boolean(this.var_55) && Boolean(this.var_55.parent))
         {
            this.var_55.parent.removeChild(this.var_55);
         }
         this.var_55 = null;
         if(this.var_70)
         {
            this.var_70.DestroyEntity(false);
         }
         this.var_70 = null;
         this.var_1 = null;
      }
      
      public function Hide() : void
      {
         this.var_1.method_158(this.var_55);
         if(this.var_70)
         {
            this.var_70.DestroyEntity(false);
         }
         this.var_70 = null;
         this.var_37 = false;
      }
      
      public function method_40() : Boolean
      {
         return Boolean(this.var_55) && this.var_55.visible;
      }
      
      public function method_1745() : void
      {
         if(!this.var_55)
         {
            this.var_55 = class_4.method_16("a_NewAccountSplash",true);
            this.var_55.visible = false;
            this.var_55.am_Email.maxChars = 320;
            this.var_1384 = new class_33(this.var_1,this.var_55.am_StartButton);
            this.var_1384.BecomeButton("Ready","Over","Click",this.method_1055,false);
            this.var_1334 = new class_33(this.var_1,this.var_55.am_Close);
            this.var_1334.BecomeButton("Ready","Over","Click",this.method_1705,false);
            this.var_1611 = new class_33(this.var_1,this.var_55.am_ChangeAccount);
            this.var_1611.BecomeButton("Ready","Over","Click",this.method_1374,false);
            this.var_337 = new class_33(this.var_1,this.var_55.am_SavePass);
            this.var_337.BecomeButton("Ready","Over","Click",this.method_411);
            this.var_1296 = new class_33(this.var_1,this.var_55.am_AgeValid);
            this.var_1296.BecomeButton("Ready","Over","Click",this.method_1023);
            this.var_1196 = new class_33(this.var_1,this.var_55.am_AgeInvalid);
            this.var_1196.BecomeButton("Ready","Over","Click",this.method_1972);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_55.am_Terms,this.method_1906);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_55.am_Privacy,this.method_1245);
            this.var_331 = this.var_337.mMovieClip.am_CheckMark;
            this.var_1259 = this.var_1296.mMovieClip.am_CheckMark;
            this.var_897 = this.var_1196.mMovieClip.am_CheckMark;
            MathUtil.method_2(this.var_55.am_Email,"");
            MathUtil.method_2(this.var_55.am_Password,"");
            this.var_1259.visible = false;
            this.var_897.visible = false;
         }
         if(!this.var_55.visible)
         {
            this.var_1.method_127();
            this.var_55.visible = true;
            this.var_1.var_89.addChildAt(this.var_55,0);
         }
         var _loc1_:ScreenCharacterCreation = this.var_1.var_141;
         if(Boolean(_loc1_) && Boolean(_loc1_.var_17))
         {
            MathUtil.method_2(this.var_55.am_Name,_loc1_.var_17.am_Name.text);
            MathUtil.method_2(this.var_55.am_LevelClass,"Level 1 " + _loc1_.var_250);
            this.UpdatePaperDoll();
         }
         this.var_1.main.stage.focus = this.var_55.am_Email;
      }
      
      public function method_1906(param1:MouseEvent) : void
      {
         if(this.var_1.method_47())
         {
            return;
         }
         navigateToURL(new URLRequest("http://www.dungeonblitz.com/terms/"),"_blank");
      }
      
      public function method_1245(param1:MouseEvent) : void
      {
         if(this.var_1.method_47())
         {
            return;
         }
         navigateToURL(new URLRequest("http://www.dungeonblitz.com/privacy/"),"_blank");
      }
      
      public function method_1023(param1:MouseEvent) : void
      {
         if(this.var_1.method_47())
         {
            return;
         }
         this.var_1259.visible = true;
         this.var_897.visible = false;
      }
      
      public function method_1972(param1:MouseEvent) : void
      {
         if(this.var_1.method_47())
         {
            return;
         }
         this.var_1259.visible = false;
         this.var_897.visible = true;
      }
      
      public function method_411(param1:MouseEvent) : void
      {
         if(this.var_1.method_47())
         {
            return;
         }
         this.var_331.visible = !this.var_331.visible;
      }
      
      public function method_54(param1:int) : Boolean
      {
         if(this.method_40() && !this.var_1.method_47())
         {
            if(param1 == Keyboard.ENTER)
            {
               this.method_621();
               return true;
            }
         }
         return false;
      }
      
      public function method_1207() : void
      {
         this.Hide();
         this.var_1.var_141.Display(this.var_1.var_141.var_250,this.var_1.var_141.var_216);
      }
      
      public function method_1055(param1:MouseEvent) : void
      {
         if(!this.var_1.method_47())
         {
            this.method_621();
         }
         param1.stopPropagation();
      }
      
      public function method_1374(param1:MouseEvent) : void
      {
         this.Hide();
         this.var_1.var_612 = false;
         this.var_1.var_1198 = true;
         this.var_1.var_479.Display();
         param1.stopPropagation();
      }
      
      public function method_1705(param1:MouseEvent) : void
      {
         this.method_1207();
         param1.stopPropagation();
      }
      
      private function method_1346(param1:String) : Boolean
      {
         if(param1.length > 320)
         {
            return false;
         }
         if(param1.indexOf(" ") != -1)
         {
            return false;
         }
         var _loc2_:Array = param1.split("@");
         if(_loc2_.length != 2)
         {
            return false;
         }
         var _loc3_:String = String(_loc2_[0]);
         var _loc4_:String;
         if((_loc4_ = String(_loc2_[1])).indexOf(".") == -1)
         {
            return false;
         }
         return true;
      }
      
      private function method_621() : void
      {
         if(!this.var_1259.visible && !this.var_897.visible)
         {
            this.var_1.var_94.method_71("You must select your age",true);
            return;
         }
         if(this.var_897.visible)
         {
            this.var_1.var_94.method_71("Only those of age 13 and older can create a new Dungeon Blitz account!",false);
            return;
         }
         var _loc1_:String = String(this.var_55.am_Email.text);
         var _loc2_:String = String(this.var_55.am_Password.text);
         var _loc3_:Boolean = this.var_331.visible;
         if(!this.method_1346(_loc1_))
         {
            this.var_1.var_94.method_71("You must enter a valid email",true);
            return;
         }
         if(_loc1_ == _loc2_)
         {
            this.var_1.var_94.method_71("Email and Password must be different",true);
            return;
         }
         if(_loc2_.length < 6)
         {
            this.var_1.var_94.method_71("Password must be at least 6 characters",true);
            return;
         }
         var _loc4_:String = Crypto.method_164("#bmg#" + _loc2_);
         this.var_1.method_267(_loc1_,_loc4_,_loc3_,true);
      }
      
      private function UpdatePaperDoll() : void
      {
         this.var_37 = true;
      }
      
      public function method_1927() : void
      {
         if(!this.var_55 || !this.var_55.visible)
         {
            return;
         }
         this.var_1384.TickMovieClip();
         this.var_1334.TickMovieClip();
         this.var_1611.TickMovieClip();
         this.var_337.TickMovieClip();
         this.var_1296.TickMovieClip();
         this.var_1196.TickMovieClip();
         var _loc1_:ScreenCharacterCreation = this.var_1.var_141;
         if(!_loc1_ || !_loc1_.var_250 || !_loc1_.var_216 || !this.var_37)
         {
            return;
         }
         var _loc2_:uint = uint(_loc1_.var_130["Hair"]);
         var _loc3_:uint = uint(_loc1_.var_130["Skin"]);
         var _loc4_:uint = uint(_loc1_.var_130["Shirt"]);
         var _loc5_:uint = uint(_loc1_.var_130["Pant"]);
         var _loc6_:String = _loc1_.var_216 == "Female" && _loc1_.var_250 == "Rogue" ? "Female" : "";
         var _loc7_:String = EntType.method_97("PaperDoll","CharCreateUI:Starter" + _loc1_.var_250,1,new Vector.<EntTypeGear>(),_loc6_,_loc1_.var_1346,_loc1_.var_1441,_loc1_.var_1549,_loc1_.var_1592,_loc2_,_loc3_,_loc4_,_loc5_);
         EntType.method_57(_loc7_,"NewAccountUI");
         if(!this.var_70)
         {
            this.var_70 = new Entity(this.var_1,"NewAccountUI:PaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,0,0,null,null,null,null,null,null);
         }
         else
         {
            this.var_70.ResetEntType(EntType.method_48("PaperDoll","NewAccountUI"));
         }
         var _loc8_:DisplayObject;
         if((_loc8_ = this.var_70.gfx.m_TheDO).scaleX > 0)
         {
            _loc8_.scaleX = -_loc8_.scaleX;
         }
         this.var_55.am_PaperDollHolder.addChild(_loc8_);
         this.var_37 = false;
      }
   }
}
