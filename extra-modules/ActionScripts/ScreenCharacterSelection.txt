package
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.ui.Keyboard;
   
   public class ScreenCharacterSelection
   {
       
      
      internal var var_1:Game;
      
      internal var var_28:MovieClip;
      
      internal var var_400:String;
      
      internal var var_1329:String;
      
      internal var var_70:Entity;
      
      internal var var_2534:Boolean = false;
      
      internal var var_37:Boolean = false;
      
      internal var var_1625:class_33 = null;
      
      internal var var_1477:class_33 = null;
      
      internal var var_1638:class_33 = null;
      
      internal var var_708:class_33 = null;
      
      public function ScreenCharacterSelection(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1064() : void
      {
         if(this.var_28)
         {
            this.var_1625.DestroyUIMovieClip();
            this.var_1625 = null;
            this.var_1638.DestroyUIMovieClip();
            this.var_1638 = null;
            this.var_1477.DestroyUIMovieClip();
            this.var_1477 = null;
            this.var_708.DestroyUIMovieClip();
            this.var_708 = null;
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_28.am_CharOption1);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_28.am_CharOption2);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_28.am_CharOption3);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_28.am_CharOption4);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_28.am_CharOption5);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_28.am_CharOption6);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_28.am_CharOption7);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_28.am_CharOption8);
         }
         if(Boolean(this.var_28) && Boolean(this.var_28.parent))
         {
            this.var_28.parent.removeChild(this.var_28);
         }
         this.var_28 = null;
         this.var_1 = null;
      }
      
      public function Hide() : void
      {
         this.var_1.method_158(this.var_28);
         if(this.var_70)
         {
            this.var_70.DestroyEntity(false);
         }
         this.var_70 = null;
         this.var_37 = false;
      }
      
      public function method_40() : Boolean
      {
         return Boolean(this.var_28) && this.var_28.visible;
      }
      
      public function Display() : void
      {
         var _loc3_:MovieClip = null;
         var _loc4_:Object = null;
         if(!this.var_28)
         {
            this.var_28 = class_4.method_16("a_IntroSplash",true);
            this.var_28.visible = false;
            this.var_1625 = new class_33(this.var_1,this.var_28.am_PlayButton);
            this.var_1625.BecomeButton("Ready","Over","Click",this.method_1077,false);
            this.var_1638 = new class_33(this.var_1,this.var_28.am_ChangeChar);
            this.var_1638.BecomeButton("Ready","Over","Click",this.method_1288,false);
            this.var_1477 = new class_33(this.var_1,this.var_28.am_CreateChar);
            this.var_1477.BecomeButton("Ready","Over","Click",this.method_1648,false);
            this.var_708 = new class_33(this.var_1,this.var_28.am_NotMyAccount);
            this.var_708.BecomeButton("Ready","Over","Click",this.method_1642,false);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_28.am_CharOption1,this.method_153);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_28.am_CharOption2,this.method_153);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_28.am_CharOption3,this.method_153);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_28.am_CharOption4,this.method_153);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_28.am_CharOption5,this.method_153);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_28.am_CharOption6,this.method_153);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_28.am_CharOption7,this.method_153);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_28.am_CharOption8,this.method_153);
            MathUtil.method_2(this.var_28.am_Name,"");
            MathUtil.method_2(this.var_28.am_LevelClass,"");
         }
         if(!this.var_28.visible)
         {
            this.var_1.method_127();
            this.var_28.visible = true;
            this.var_1.var_89.addChildAt(this.var_28,0);
         }
         var _loc1_:uint = 0;
         while(_loc1_ < Game.const_207)
         {
            _loc3_ = this.var_28.getChildByName("am_CharOption" + (_loc1_ + 1)) as MovieClip;
            _loc3_.filters = [Game.const_515];
            _loc3_.visible = false;
            _loc3_.gotoAndStop(1);
            _loc1_++;
         }
         this.var_28.am_DataLoading.visible = false;
         this.var_28.am_ChangeChar.visible = true;
         this.var_28.am_CreateChar.alpha = 1;
         var _loc2_:Array = this.var_1.var_1306;
         if(_loc2_)
         {
            this.var_400 = _loc2_[0];
            MathUtil.method_2(this.var_28.am_Name,this.var_400);
            MathUtil.method_2(this.var_28.am_LevelClass,"Level " + Entity.method_1630(uint(_loc2_[2])) + " " + _loc2_[1]);
            this.UpdatePaperDoll(this.var_400);
         }
         else if(Boolean((_loc4_ = this.var_1.var_164.data).dbCharName) && Boolean(_loc4_.dbCharLevel) && Boolean(_loc4_.dbCharClass))
         {
            this.var_400 = _loc4_.dbCharName;
            MathUtil.method_2(this.var_28.am_Name,this.var_400);
            MathUtil.method_2(this.var_28.am_LevelClass,"Level " + _loc4_.dbCharLevel + " " + _loc4_.dbCharClass);
            EntType.method_57(_loc4_.dbEntType,"Player");
            this.UpdatePaperDoll(this.var_400);
         }
         else
         {
            this.var_400 = null;
            MathUtil.method_2(this.var_28.am_Name,"");
            MathUtil.method_2(this.var_28.am_LevelClass,"");
         }
         if(this.var_1.var_934)
         {
            this.var_708.Hide();
         }
         if(Boolean(this.var_1.var_355) && !this.var_1.var_1125)
         {
            this.method_1875(this.var_1.var_355);
            if(!this.var_400 && Boolean(this.var_1.var_355.length))
            {
               this.method_959(0);
            }
         }
      }
      
      public function method_1875(param1:Vector.<Object>) : void
      {
         var _loc4_:MovieClip = null;
         var _loc5_:Object = null;
         var _loc2_:uint = param1.length;
         var _loc3_:uint = 0;
         while(_loc3_ < Game.const_207)
         {
            (_loc4_ = this.var_28.getChildByName("am_CharOption" + (_loc3_ + 1)) as MovieClip).visible = true;
            if(_loc3_ >= _loc2_)
            {
               _loc4_.alpha = 0.5;
               _loc4_.gotoAndStop(1);
               MathUtil.method_2(_loc4_.am_CharName,"");
               MathUtil.method_2(_loc4_.am_CharLevel,"");
            }
            else
            {
               _loc5_ = param1[_loc3_];
               MathUtil.method_2(_loc4_.am_CharName,_loc5_.name);
               MathUtil.method_2(_loc4_.am_CharLevel,_loc5_.level);
               if(this.var_400 == _loc5_.name)
               {
                  _loc4_.filters = [class_51.const_71,Game.const_621];
               }
               if(_loc5_.className == "Mage")
               {
                  _loc4_.gotoAndStop(2);
               }
               else if(_loc5_.className == "Paladin")
               {
                  _loc4_.gotoAndStop(3);
               }
               else
               {
                  _loc4_.gotoAndStop(4);
               }
               _loc4_.alpha = 1;
            }
            _loc3_++;
         }
         this.var_28.am_ChangeChar.visible = false;
         if(_loc2_ >= Game.const_207)
         {
            this.var_28.am_CreateChar.alpha = 0.5;
         }
      }
      
      public function method_959(param1:uint) : void
      {
         var _loc4_:MovieClip = null;
         var _loc5_:String = null;
         var _loc6_:Packet = null;
         if(!this.var_1.var_355)
         {
            return;
         }
         var _loc2_:Object = this.var_1.var_355[param1];
         var _loc3_:uint = 0;
         while(_loc3_ < Game.const_207)
         {
            _loc4_ = this.var_28.getChildByName("am_CharOption" + (_loc3_ + 1)) as MovieClip;
            if(param1 != _loc3_)
            {
               _loc4_.filters = [Game.const_515];
            }
            else
            {
               _loc5_ = String(_loc2_.name);
               if(this.var_1.var_2129[_loc5_])
               {
                  this.UpdatePaperDoll(_loc5_);
               }
               else
               {
                  (_loc6_ = new Packet(LinkUpdater.const_840)).method_26(_loc5_);
                  this.var_1.serverConn.SendPacket(_loc6_);
                  this.var_1.var_2129[_loc5_] = true;
               }
               _loc4_.filters = [class_51.const_71,Game.const_621];
               MathUtil.method_2(this.var_28.am_Name,_loc5_);
               MathUtil.method_2(this.var_28.am_LevelClass,"Level " + _loc2_.level + " " + _loc2_.className);
               this.var_400 = _loc5_;
            }
            _loc3_++;
         }
      }
      
      public function method_153(param1:MouseEvent) : void
      {
         var _loc4_:MovieClip = null;
         if(this.var_1.method_47())
         {
            return;
         }
         var _loc2_:MovieClip = param1.target as MovieClip;
         if(_loc2_.alpha < 1)
         {
            return;
         }
         var _loc3_:uint = 0;
         while(_loc3_ < Game.const_207)
         {
            if((_loc4_ = this.var_28.getChildByName("am_CharOption" + (_loc3_ + 1)) as MovieClip).hitTestPoint(param1.stageX,param1.stageY))
            {
               this.method_959(_loc3_);
               break;
            }
            _loc3_++;
         }
      }
      
      public function method_1642(param1:MouseEvent) : void
      {
         if(this.var_1.method_47())
         {
            return;
         }
         if(Boolean(this.var_708) && !this.var_708.mbVisible)
         {
            return;
         }
         if(this.var_1.serverConn)
         {
            this.var_1.serverConn.method_205();
         }
         this.var_1.serverConn = null;
         this.var_1.var_164.clear();
         this.var_1.var_273.Display();
      }
      
      public function method_1648(param1:MouseEvent) : void
      {
         var _loc2_:uint = 0;
         if(this.var_1.method_47())
         {
            return;
         }
         if(this.var_1.var_355)
         {
            _loc2_ = this.var_1.var_355.length;
            if(_loc2_ >= Game.const_207)
            {
               this.var_1.var_94.method_71("You cannot create more than eight characters",true);
               return;
            }
            if(_loc2_ >= this.var_1.loginMaxChars)
            {
               this.var_1.tooltip.TriggerTooltip(class_19.method_254("NewCharPremiumReact"));
               return;
            }
         }
         this.var_1.var_1125 = null;
         this.method_405(true,false);
      }
      
      public function method_1288(param1:MouseEvent) : void
      {
         if(this.var_1.method_47())
         {
            return;
         }
         this.var_1.var_1125 = null;
         this.method_405(false,false);
      }
      
      public function method_54(param1:int) : Boolean
      {
         if(this.method_40() && !this.var_1.method_47())
         {
            if(param1 == Keyboard.ENTER)
            {
               this.method_603();
               return true;
            }
         }
         return false;
      }
      
      public function method_1077(param1:MouseEvent) : void
      {
         if(!this.var_1.method_47())
         {
            this.method_603();
         }
      }
      
      public function method_603() : void
      {
         if(!this.var_400)
         {
            this.var_1.var_94.method_71("Must choose a character",true);
            return;
         }
         this.var_1.var_1125 = this.var_400;
         this.method_405(false,false);
      }
      
      private function method_405(param1:Boolean, param2:Boolean) : void
      {
         this.var_1.var_612 = param1;
         this.var_1.var_1198 = param2;
         if(this.var_1.serverConn)
         {
            return;
         }
         var _loc3_:* = null;
         var _loc4_:String = null;
         var _loc5_:Object;
         if(Boolean((_loc5_ = this.var_1.var_164.data).dbUserEmail) && Boolean(_loc5_.dbPassHash))
         {
            _loc3_ = String(_loc5_.dbUserEmail);
            _loc4_ = String(_loc5_.dbPassHash);
         }
         else if(this.var_1.clientFacebookID)
         {
            _loc3_ = "fbnoemail" + this.var_1.clientFacebookID + "@dungeonblitz.com";
            _loc4_ = Crypto.method_164("#bmg#" + this.var_1.clientFacebookID + "^nonsense^");
         }
         else if(this.var_1.clientKongID)
         {
            _loc3_ = "kongnoemail" + this.var_1.clientKongID + "@dungeonblitz.com";
            _loc4_ = Crypto.method_164("#bmg#" + this.var_1.clientKongID + "^nonsense^");
         }
         else
         {
            _loc3_ = String(_loc5_.dbUserEmail);
         }
         this.var_1.method_267(_loc3_,_loc4_,true,false);
      }
      
      public function UpdatePaperDoll(param1:String) : void
      {
         if(Boolean(this.var_70) && this.var_1329 != param1)
         {
            this.var_70.DestroyEntity(false);
            this.var_70 = null;
         }
         this.var_1329 = param1;
         this.var_37 = true;
      }
      
      public function RefreshPaperDoll() : void
      {
         var _loc3_:Array = null;
         var _loc4_:Vector.<EntTypeGear> = null;
         var _loc5_:uint = 0;
         var _loc6_:String = null;
         var _loc7_:uint = 0;
         var _loc8_:GearType = null;
         if(!this.var_28 || !this.var_28.visible)
         {
            return;
         }
         this.var_1625.TickMovieClip();
         this.var_1638.TickMovieClip();
         this.var_1477.TickMovieClip();
         this.var_708.TickMovieClip();
         if(!this.var_37)
         {
            return;
         }
         if(!this.var_2534 && !ResourceManager.method_149("Login"))
         {
            this.var_28.am_DataLoading.visible = true;
            return;
         }
         this.var_2534 = true;
         this.var_28.am_DataLoading.visible = false;
         if(!EntType.dynamicEntTypes["Player:" + this.var_1329])
         {
            _loc3_ = this.var_1.var_1306;
            if(!_loc3_ || _loc3_[0] != this.var_1329)
            {
               return;
            }
            _loc4_ = new Vector.<EntTypeGear>();
            _loc5_ = 12;
            while(_loc5_ <= 17)
            {
               if(_loc8_ = !!(_loc7_ = uint(_loc3_[_loc5_])) ? class_14.gearTypes[_loc7_] : null)
               {
                  _loc4_.push(new EntTypeGear(_loc8_.gearName,0,0,0));
               }
               _loc5_++;
            }
            _loc6_ = EntType.method_97(_loc3_[0],_loc3_[1],0,_loc4_,_loc3_[8],_loc3_[10],_loc3_[9],_loc3_[11],_loc3_[7],_loc3_[3],_loc3_[6],_loc3_[5],_loc3_[4]);
            EntType.method_57(_loc6_,"Player");
         }
         var _loc1_:* = "<EntType EntName=\"PaperDoll\" parent=\"Player:" + this.var_1329 + "\"><GfxType><AnimScale>1.8</AnimScale><Shadow></Shadow></GfxType></EntType>";
         EntType.method_57(_loc1_,"CharSelectUI");
         if(!this.var_70)
         {
            this.var_70 = new Entity(this.var_1,"CharSelectUI:PaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,0,0,null,null,null,null,null,null);
         }
         else
         {
            this.var_70.ResetEntType(EntType.method_48("PaperDoll","CharSelectUI"));
         }
         var _loc2_:Sprite = this.var_70.gfx.m_TheDO;
         if(_loc2_.scaleX > 0)
         {
            _loc2_.scaleX = -_loc2_.scaleX;
         }
         this.var_28.am_PaperDollHolder.addChild(_loc2_);
         this.var_37 = false;
      }
   }
}
