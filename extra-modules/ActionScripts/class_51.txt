package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.filters.BitmapFilterQuality;
   import flash.filters.GlowFilter;
   import flash.ui.Keyboard;
   
   public class class_51
   {
      
      public static const const_71:GlowFilter = new GlowFilter(7792093,1,10,10,10,BitmapFilterQuality.LOW);
       
      
      internal var var_1:Game;
      
      internal var var_40:MovieClip;
      
      internal var var_1105:Boolean = false;
      
      internal var var_168:String = null;
      
      internal var var_675:String = null;
      
      internal var var_452:Vector.<Entity>;
      
      internal var var_422:MovieClip;
      
      internal var var_380:MovieClip;
      
      internal var var_415:MovieClip;
      
      internal var var_416:MovieClip;
      
      internal var var_364:MovieClip;
      
      internal var var_401:MovieClip;
      
      internal var var_174:class_33;
      
      internal var var_2445:Boolean = false;
      
      public function class_51(param1:Game)
      {
         var _loc2_:String = null;
         var _loc3_:String = null;
         var _loc4_:String = null;
         this.var_452 = new Vector.<Entity>();
         super();
         this.var_1 = param1;
         if(!this.var_2445)
         {
            _loc2_ = "<EntType EntName=\"StarterPaladin\"><GfxType><AnimScale>1.4</AnimScale><AnimFile>Animation_Paladin.swf</AnimFile><AnimClass>a__Animation</AnimClass></GfxType></EntType>";
            _loc3_ = "<EntType EntName=\"StarterMage\"><GfxType><AnimScale>2.0</AnimScale><AnimFile>Animation_Mage.swf</AnimFile><AnimClass>a__Animation</AnimClass></GfxType></EntType>";
            _loc4_ = "<EntType EntName=\"StarterRogue\"><GfxType><AnimScale>2.0</AnimScale><AnimFile>Animation_Rogue.swf</AnimFile><AnimClass>a__Animation</AnimClass><CustomArt>Animation_Rogue.swf/NoHat</CustomArt></GfxType></EntType>";
            EntType.method_57(_loc2_,"CharCreateUI");
            EntType.method_57(_loc3_,"CharCreateUI");
            EntType.method_57(_loc4_,"CharCreateUI");
            this.var_2445 = false;
         }
      }
      
      public function method_1821() : void
      {
         var _loc1_:Entity = null;
         for each(_loc1_ in this.var_452)
         {
            _loc1_.DestroyEntity(false);
         }
         this.var_452 = null;
         if(this.var_40)
         {
            this.var_422.removeEventListener(MouseEvent.ROLL_OVER,this.method_797);
            this.var_422.removeEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_422.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_912);
            this.var_422 = null;
            this.var_380.removeEventListener(MouseEvent.ROLL_OVER,this.method_757);
            this.var_380.removeEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_380.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_863);
            this.var_380 = null;
            this.var_415.removeEventListener(MouseEvent.ROLL_OVER,this.method_808);
            this.var_415.removeEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_415.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_692);
            this.var_415 = null;
            this.var_416.removeEventListener(MouseEvent.ROLL_OVER,this.method_569);
            this.var_416.removeEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_416.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_845);
            this.var_416 = null;
            this.var_364.removeEventListener(MouseEvent.ROLL_OVER,this.method_871);
            this.var_364.removeEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_364.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_610);
            this.var_364 = null;
            this.var_401.removeEventListener(MouseEvent.ROLL_OVER,this.method_958);
            this.var_401.removeEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_401.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_556);
            this.var_401 = null;
         }
         if(Boolean(this.var_40) && Boolean(this.var_40.parent))
         {
            this.var_40.parent.removeChild(this.var_40);
         }
         this.var_40 = null;
         this.var_1 = null;
      }
      
      public function Hide() : void
      {
         var _loc1_:Entity = null;
         this.var_1.method_158(this.var_40);
         for each(_loc1_ in this.var_452)
         {
            _loc1_.DestroyEntity(false);
         }
         this.var_452.length = 0;
         this.var_1105 = false;
      }
      
      public function method_40() : Boolean
      {
         return Boolean(this.var_40) && this.var_40.visible;
      }
      
      private function method_797(param1:MouseEvent) : void
      {
         this.var_675 = "Paladin";
         this.var_168 = null;
         this.method_162();
         param1.stopPropagation();
      }
      
      private function method_757(param1:MouseEvent) : void
      {
         this.var_675 = "PaladinFem";
         this.var_168 = null;
         this.method_162();
         param1.stopPropagation();
      }
      
      private function method_808(param1:MouseEvent) : void
      {
         this.var_675 = "Rogue";
         this.var_168 = null;
         this.method_162();
         param1.stopPropagation();
      }
      
      private function method_569(param1:MouseEvent) : void
      {
         this.var_675 = "RogueFem";
         this.var_168 = null;
         this.method_162();
         param1.stopPropagation();
      }
      
      private function method_871(param1:MouseEvent) : void
      {
         this.var_675 = "Mage";
         this.var_168 = null;
         this.method_162();
         param1.stopPropagation();
      }
      
      private function method_958(param1:MouseEvent) : void
      {
         this.var_675 = "MageMale";
         this.var_168 = null;
         this.method_162();
         param1.stopPropagation();
      }
      
      private function method_99(param1:MouseEvent) : void
      {
         if(!this.var_168)
         {
            this.var_675 = null;
         }
         this.method_162();
         param1.stopPropagation();
      }
      
      private function method_912(param1:MouseEvent) : void
      {
         this.var_168 = "Paladin";
         this.method_223();
         param1.stopPropagation();
      }
      
      private function method_863(param1:MouseEvent) : void
      {
         this.var_168 = "PaladinFem";
         this.method_223();
         param1.stopPropagation();
      }
      
      private function method_692(param1:MouseEvent) : void
      {
         this.var_168 = "Rogue";
         this.method_223();
         param1.stopPropagation();
      }
      
      private function method_845(param1:MouseEvent) : void
      {
         this.var_168 = "RogueFem";
         this.method_223();
         param1.stopPropagation();
      }
      
      private function method_610(param1:MouseEvent) : void
      {
         this.var_168 = "Mage";
         this.method_223();
         param1.stopPropagation();
      }
      
      private function method_556(param1:MouseEvent) : void
      {
         this.var_168 = "MageMale";
         this.method_223();
         param1.stopPropagation();
      }
      
      public function method_223() : void
      {
         if(!this.var_1105)
         {
            return;
         }
         this.Hide();
         if(this.var_168 == "Paladin")
         {
            this.var_1.var_141.Display("Paladin","Male");
         }
         else if(this.var_168 == "PaladinFem")
         {
            this.var_1.var_141.Display("Paladin","Female");
         }
         else if(this.var_168 == "Rogue")
         {
            this.var_1.var_141.Display("Rogue","Male");
         }
         else if(this.var_168 == "RogueFem")
         {
            this.var_1.var_141.Display("Rogue","Female");
         }
         else if(this.var_168 == "Mage")
         {
            this.var_1.var_141.Display("Mage","Female");
         }
         else if(this.var_168 == "MageMale")
         {
            this.var_1.var_141.Display("Mage","Male");
         }
      }
      
      public function Display() : void
      {
         if(!this.var_40)
         {
            this.var_40 = class_4.method_16("a_ClassSelection_Screen",true);
            this.var_40.visible = false;
            this.var_40.am_MageDesc.mouseEnabled = false;
            this.var_40.am_MageDesc.mouseChildren = false;
            this.var_40.am_PaladinDesc.mouseEnabled = false;
            this.var_40.am_PaladinDesc.mouseChildren = false;
            this.var_40.am_RogueDesc.mouseEnabled = false;
            this.var_40.am_RogueDesc.mouseChildren = false;
            this.var_422 = this.var_40.am_PDH_Paladin;
            this.var_422.addEventListener(MouseEvent.ROLL_OVER,this.method_797);
            this.var_422.addEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_422.addEventListener(MouseEvent.MOUSE_DOWN,this.method_912);
            this.var_422.mouseChildren = false;
            this.var_380 = this.var_40.am_PDH_PaladinFemale;
            this.var_380.addEventListener(MouseEvent.ROLL_OVER,this.method_757);
            this.var_380.addEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_380.addEventListener(MouseEvent.MOUSE_DOWN,this.method_863);
            this.var_380.mouseChildren = false;
            this.var_415 = this.var_40.am_PDH_Rogue;
            this.var_415.addEventListener(MouseEvent.ROLL_OVER,this.method_808);
            this.var_415.addEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_415.addEventListener(MouseEvent.MOUSE_DOWN,this.method_692);
            this.var_415.mouseChildren = false;
            this.var_416 = this.var_40.am_PDH_RogueFemale;
            this.var_416.addEventListener(MouseEvent.ROLL_OVER,this.method_569);
            this.var_416.addEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_416.addEventListener(MouseEvent.MOUSE_DOWN,this.method_845);
            this.var_416.mouseChildren = false;
            this.var_364 = this.var_40.am_PDH_Mage;
            this.var_364.addEventListener(MouseEvent.ROLL_OVER,this.method_871);
            this.var_364.addEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_364.addEventListener(MouseEvent.MOUSE_DOWN,this.method_610);
            this.var_364.mouseChildren = false;
            this.var_401 = this.var_40.am_PDH_MageMale;
            this.var_401.addEventListener(MouseEvent.ROLL_OVER,this.method_958);
            this.var_401.addEventListener(MouseEvent.ROLL_OUT,this.method_99);
            this.var_401.addEventListener(MouseEvent.MOUSE_DOWN,this.method_556);
            this.var_401.mouseChildren = false;
            this.var_174 = new class_33(this.var_1,this.var_40.am_ChangeAccount);
            this.var_174.BecomeButton("Ready","Over","Click",this.method_1431,false);
         }
         if(!this.var_40.visible)
         {
            this.var_1.method_127();
            this.var_40.visible = true;
            this.var_1.var_89.addChildAt(this.var_40,0);
         }
         this.method_162();
         this.var_1105 = false;
         this.var_40.am_DataLoading.visible = true;
         if(this.var_1.serverConn)
         {
            MathUtil.method_2(this.var_174.mMovieClip.am_Text,"Back to Character List");
         }
         else if(this.var_1.var_934)
         {
            this.var_174.Hide();
         }
         else
         {
            MathUtil.method_2(this.var_174.mMovieClip.am_Text,"Login Existing Account");
         }
      }
      
      private function method_913() : void
      {
         if(Boolean(this.var_174) && !this.var_174.mbVisible)
         {
            return;
         }
         if(this.var_1.serverConn)
         {
            this.var_1.var_341.Display();
         }
         else
         {
            this.var_1.var_612 = false;
            this.var_1.var_1198 = true;
            this.var_1.var_479.Display();
         }
      }
      
      public function method_1431(param1:MouseEvent) : void
      {
         if(!this.var_1.method_47())
         {
            this.method_913();
         }
      }
      
      public function method_54(param1:int) : Boolean
      {
         if(this.method_40() && !this.var_1.method_47())
         {
            if(param1 == Keyboard.ESCAPE)
            {
               this.method_913();
               return true;
            }
         }
         return false;
      }
      
      private function method_162() : void
      {
         this.var_40.am_MageDesc.visible = false;
         this.var_40.am_PaladinDesc.visible = false;
         this.var_40.am_RogueDesc.visible = false;
         this.var_422.filters = [];
         this.var_380.filters = [];
         this.var_415.filters = [];
         this.var_416.filters = [];
         this.var_364.filters = [];
         this.var_401.filters = [];
         var _loc1_:String = !!this.var_675 ? this.var_675 : this.var_168;
         if(_loc1_ == "Rogue")
         {
            this.var_40.am_RogueDesc.visible = true;
            this.var_415.filters = [const_71];
         }
         else if(_loc1_ == "RogueFem")
         {
            this.var_40.am_RogueDesc.visible = true;
            this.var_416.filters = [const_71];
         }
         else if(_loc1_ == "Paladin")
         {
            this.var_40.am_PaladinDesc.visible = true;
            this.var_422.filters = [const_71];
         }
         else if(_loc1_ == "PaladinFem")
         {
            this.var_40.am_PaladinDesc.visible = true;
            this.var_380.filters = [const_71];
         }
         else if(_loc1_ == "Mage")
         {
            this.var_40.am_MageDesc.visible = true;
            this.var_364.filters = [const_71];
         }
         else if(_loc1_ == "MageMale")
         {
            this.var_40.am_MageDesc.visible = true;
            this.var_401.filters = [const_71];
         }
      }
      
      public function RefreshPaperDoll() : void
      {
         var _loc1_:Entity = null;
         if(!this.var_40 || !this.var_40.visible)
         {
            return;
         }
         this.var_174.TickMovieClip();
         if(this.var_1105)
         {
            return;
         }
         if(!this.var_1105 && !ResourceManager.method_149(ResourceManager.const_512))
         {
            this.var_40.am_DataLoading.visible = true;
            return;
         }
         this.var_1105 = true;
         this.var_40.am_DataLoading.visible = false;
         EntType.method_57(EntType.method_97("PaladinPaperDoll","CharCreateUI:StarterPaladin",0.85,new Vector.<EntTypeGear>(),null,"Basic","Do01","M01","F01",5320474,12283209,6776672,4206624),"ClassSelectUI");
         EntType.method_57(EntType.method_97("FPaladinPaperDoll","CharCreateUI:StarterPaladin",0.8,new Vector.<EntTypeGear>(),"Female","Basic","FDo01","FM01","FF01",5320474,12283209,6776672,4206624),"ClassSelectUI");
         EntType.method_57(EntType.method_97("RoguePaperDoll","CharCreateUI:StarterRogue",0.81,new Vector.<EntTypeGear>(),null,"MaleHead","Do01","Mouth01","Face01",5977374,12283209,6776672,6710886),"ClassSelectUI");
         EntType.method_57(EntType.method_97("FRoguePaperDoll","CharCreateUI:StarterRogue",0.78,new Vector.<EntTypeGear>(),"Female","FemaleHead","FDo01","FMouth01","FFace01",5977374,12283209,6776672,6710886),"ClassSelectUI");
         EntType.method_57(EntType.method_97("MagePaperDoll","CharCreateUI:StarterMage",0.8,new Vector.<EntTypeGear>(),null,"Head01","Do01","M01","F01",5977374,12283209,6776672,10261889),"ClassSelectUI");
         EntType.method_57(EntType.method_97("MMagePaperDoll","CharCreateUI:StarterMage",0.85,new Vector.<EntTypeGear>(),"Male","Head01","MDo01","MM01","MF01",5977374,12283209,6776672,4012352),"ClassSelectUI");
         _loc1_ = new Entity(this.var_1,"ClassSelectUI:PaladinPaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,0,0,null,null,null,null,null,null);
         _loc1_.gfx.m_TheDO.scaleX = -_loc1_.gfx.m_TheDO.scaleX;
         this.var_422.addChild(_loc1_.gfx.m_TheDO);
         this.var_452.push(_loc1_);
         _loc1_ = new Entity(this.var_1,"ClassSelectUI:FPaladinPaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,0,0,null,null,null,null,null,null);
         _loc1_.gfx.m_TheDO.scaleX = _loc1_.gfx.m_TheDO.scaleX;
         _loc1_.gfx.m_Seq.method_34(Seq.C_EMOTE,"Relaxed",true);
         this.var_380.addChild(_loc1_.gfx.m_TheDO);
         this.var_452.push(_loc1_);
         _loc1_ = new Entity(this.var_1,"ClassSelectUI:RoguePaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,0,0,null,null,null,null,null,null);
         this.var_415.addChild(_loc1_.gfx.m_TheDO);
         this.var_452.push(_loc1_);
         _loc1_ = new Entity(this.var_1,"ClassSelectUI:FRoguePaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,0,0,null,null,null,null,null,null);
         _loc1_.gfx.m_Seq.method_34(Seq.C_EMOTE,"Relaxed",true);
         _loc1_.gfx.m_TheDO.scaleX = -_loc1_.gfx.m_TheDO.scaleX;
         this.var_416.addChild(_loc1_.gfx.m_TheDO);
         this.var_452.push(_loc1_);
         _loc1_ = new Entity(this.var_1,"ClassSelectUI:MagePaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,0,0,null,null,null,null,null,null);
         _loc1_.gfx.m_TheDO.scaleX = -_loc1_.gfx.m_TheDO.scaleX;
         this.var_364.addChild(_loc1_.gfx.m_TheDO);
         this.var_452.push(_loc1_);
         _loc1_ = new Entity(this.var_1,"ClassSelectUI:MMagePaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,0,0,null,null,null,null,null,null);
         _loc1_.gfx.m_Seq.method_34(Seq.C_EMOTE,"Relaxed",true);
         _loc1_.gfx.m_TheDO.scaleX = -_loc1_.gfx.m_TheDO.scaleX;
         this.var_401.addChild(_loc1_.gfx.m_TheDO);
         this.var_452.push(_loc1_);
      }
   }
}
