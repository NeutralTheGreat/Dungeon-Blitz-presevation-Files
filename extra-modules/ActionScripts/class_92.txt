package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   
   public class class_92 extends class_32
   {
       
      
      private var var_1437:class_33;
      
      private var var_1889:class_33;
      
      private var var_1334:class_33;
      
      private var var_521:Vector.<class_33>;
      
      private var var_2026:Boolean = false;
      
      private var var_82:Array;
      
      private var var_1175:Array;
      
      private const const_1425:String = "---";
      
      private var var_1877:Boolean;
      
      public function class_92(param1:Game)
      {
         var _loc3_:int = 0;
         super(param1,"a_ScreenKeybind","am_Panel");
         var_15 = true;
         this.var_82 = new Array(Game.const_79);
         this.var_82[Game.const_153] = 0;
         this.var_82[Game.const_151] = 1;
         this.var_82[Game.const_158] = 2;
         this.var_82[Game.const_188] = 3;
         this.var_82[Game.COMMAND_SPELL1] = 4;
         this.var_82[Game.COMMAND_SPELL2] = 5;
         this.var_82[Game.COMMAND_SPELL3] = 6;
         this.var_82[Game.COMMAND_SPELL4] = 7;
         this.var_82[Game.COMMAND_SPELL5] = 8;
         this.var_82[Game.COMMAND_SPELL6] = 9;
         this.var_82[Game.const_401] = 23;
         this.var_82[Game.const_317] = 24;
         this.var_82[Game.const_328] = 15;
         this.var_82[Game.const_346] = 12;
         this.var_82[Game.const_367] = 16;
         this.var_82[Game.const_364] = 13;
         this.var_82[Game.const_357] = 17;
         this.var_82[Game.const_314] = 19;
         this.var_82[Game.const_329] = 18;
         this.var_82[Game.const_321] = 14;
         this.var_82[Game.const_320] = 20;
         this.var_82[Game.const_277] = 11;
         this.var_82[Game.const_274] = 10;
         this.var_82[Game.const_458] = 21;
         this.var_82[Game.const_430] = 22;
         this.var_82[Game.const_574] = 25;
         this.var_1175 = new Array(Game.const_79);
         var _loc2_:int = 0;
         while(_loc2_ < this.var_1175.length)
         {
            _loc3_ = this.var_82.indexOf(_loc2_);
            if(_loc3_ != -1)
            {
               this.var_1175[_loc2_] = _loc3_;
            }
            _loc2_++;
         }
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_521 = new Vector.<class_33>(Game.const_79,true);
         var _loc1_:MovieClip = var_2.am_BindingGroup;
         var _loc2_:uint = 0;
         while(_loc2_ < Game.const_79)
         {
            this.var_521[_loc2_] = method_3(_loc1_["am_Binding" + _loc2_] as MovieClip,_loc2_,this.method_1463);
            _loc2_++;
         }
         this.var_1437 = method_5(var_2.am_Apply,this.method_1707);
         this.var_1889 = method_5(var_2.am_Default,this.method_1228);
         this.var_1334 = method_23(var_2.am_Exit);
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_521 = null;
         this.var_1437 = null;
         this.var_1334 = null;
         this.var_1889 = null;
      }
      
      override public function OnClearScreen() : void
      {
         var_1.mKeybindManager.mbStatePickKey = false;
         var_1.mKeybindManager.mActiveCommand = 0;
         if(this.var_2026)
         {
            var_1.mKeybindManager.ClearBuffer();
         }
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:TextField = null;
         var _loc2_:uint = 0;
         while(_loc2_ < Game.const_79)
         {
            _loc1_ = this.var_521[_loc2_].mMovieClip.am_Text;
            _loc1_.textColor = ScreenArmory.const_11;
            MathUtil.method_2(_loc1_,var_1.mKeybindManager.FetchKeyFromCommand(this.var_1175[_loc2_]));
            _loc2_++;
         }
         this.method_498();
      }
      
      public function OnInitDisplay() : void
      {
         var_1.mKeybindManager.WriteIntoBuffer();
         this.var_2026 = true;
         this.var_1877 = false;
         var_1.mKeybindManager.SetContext(var_1.CONTEXT_NORMAL);
      }
      
      private function method_1463(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:TextField = this.var_521[param2].mMovieClip.am_Text;
         _loc3_.textColor = 16729156;
         var _loc4_:int = int(this.var_1175[param2]);
         MathUtil.method_2(_loc3_,"??");
         this.method_292("Press Key for " + var_1.mKeybindManager.GetReadableCommands(_loc4_));
         this.method_1702();
         var_1.mKeybindManager.mbStatePickKey = true;
         var_1.mKeybindManager.mActiveCommand = _loc4_;
      }
      
      private function method_1702() : void
      {
         var _loc2_:class_33 = null;
         var _loc1_:uint = 0;
         while(_loc1_ < Game.const_79)
         {
            _loc2_ = this.var_521[_loc1_];
            _loc2_.DisableButton("Nothing");
            _loc2_.ClearAnimation();
            _loc1_++;
         }
         this.var_1437.DisableButton("Nothing");
         this.var_1889.DisableButton("Nothing");
         this.var_1334.DisableButton("Nothing");
      }
      
      public function method_498() : void
      {
         var _loc2_:class_33 = null;
         var _loc1_:uint = 0;
         while(_loc1_ < Game.const_79)
         {
            _loc2_ = this.var_521[_loc1_];
            _loc2_.EnableButton();
            _loc1_++;
         }
         if(this.var_1877)
         {
            this.var_1437.EnableButton();
         }
         else
         {
            this.var_1437.DisableButton("Inactive");
         }
         this.var_1889.EnableButton();
         this.var_1334.EnableButton();
      }
      
      public function method_1089(param1:int, param2:int) : void
      {
         var _loc3_:int = int(this.var_82[param1]);
         var _loc4_:TextField;
         (_loc4_ = this.var_521[_loc3_].mMovieClip.am_Text).textColor = ScreenArmory.const_11;
         MathUtil.method_2(_loc4_,var_1.mKeybindManager.GetReadableKey(param2));
         if(param2 == 255)
         {
            this.method_292("Keybind Erased");
         }
         else
         {
            this.method_292("Key Rebinded");
         }
         this.var_1877 = true;
         this.method_498();
      }
      
      private function method_1707(param1:MouseEvent) : void
      {
         var _loc6_:int = 0;
         var _loc7_:Boolean = false;
         if(!var_1.CanSendPacket())
         {
            return;
         }
         var_1.mKeybindManager.saveBufferIntoReal();
         this.var_2026 = false;
         var _loc2_:Packet = new Packet(LinkUpdater.const_1014);
         var _loc3_:Vector.<Object> = var_1.mKeybindManager.GenerateServerPacket();
         var _loc4_:* = !var_1.mKeybindManager.mbDefault;
         var _loc5_:String = "";
         _loc2_.method_15(_loc4_);
         _loc5_ += _loc4_ ? "1" : "0";
         if(_loc4_)
         {
            _loc6_ = 0;
            while(_loc6_ < _loc3_.length)
            {
               _loc7_ = Boolean(_loc3_[_loc6_]["exists"]);
               _loc2_.method_15(_loc7_);
               _loc5_ += _loc7_ ? "1" : "0";
               if(_loc7_)
               {
                  _loc2_.method_1860(_loc3_[_loc6_]["key"]);
                  _loc5_ += _loc3_[_loc6_]["key"];
               }
               _loc6_++;
            }
         }
         var_1.serverConn.SendPacket(_loc2_);
         var_1.mKeybindManager.ClearServerPacket();
         this.UpdateHotbarKeys();
         Hide();
      }
      
      public function UpdateHotbarKeys() : void
      {
         var _loc1_:class_108 = var_1.mKeybindManager;
         var _loc2_:Vector.<class_153> = var_1.screenHud.mPowerButtons;
         MathUtil.method_2(_loc2_[0].keyClip.am_KeyBindText,_loc1_.FetchKeyFromCommand(Game.COMMAND_SPELL1));
         MathUtil.method_2(_loc2_[1].keyClip.am_KeyBindText,_loc1_.FetchKeyFromCommand(Game.COMMAND_SPELL2));
         MathUtil.method_2(_loc2_[2].keyClip.am_KeyBindText,_loc1_.FetchKeyFromCommand(Game.COMMAND_SPELL3));
         MathUtil.method_2(_loc2_[3].keyClip.am_KeyBindText,_loc1_.FetchKeyFromCommand(Game.COMMAND_SPELL4));
         MathUtil.method_2(_loc2_[4].keyClip.am_KeyBindText,_loc1_.FetchKeyFromCommand(Game.COMMAND_SPELL5));
         MathUtil.method_2(_loc2_[5].keyClip.am_KeyBindText,_loc1_.FetchKeyFromCommand(Game.COMMAND_SPELL6));
         MathUtil.method_2(_loc2_[6].keyClip.am_KeyBindText,_loc1_.FetchKeyFromCommand(Game.const_277));
         MathUtil.method_2(_loc2_[7].keyClip.am_KeyBindText,_loc1_.FetchKeyFromCommand(Game.const_274));
      }
      
      private function method_1228(param1:MouseEvent) : void
      {
         var _loc3_:TextField = null;
         var_1.mKeybindManager.WriteDefaultsIntoBuffer();
         var _loc2_:uint = 0;
         while(_loc2_ < Game.const_79)
         {
            _loc3_ = this.var_521[_loc2_].mMovieClip.am_Text;
            _loc3_.textColor = ScreenArmory.const_11;
            MathUtil.method_2(_loc3_,var_1.mKeybindManager.FetchKeyFromCommand(this.var_1175[_loc2_],true));
            _loc2_++;
         }
         this.var_1877 = true;
         this.method_498();
      }
      
      private function method_2146(param1:MouseEvent) : void
      {
      }
      
      public function method_292(param1:String) : void
      {
         MathUtil.method_2(var_2.am_Message,param1);
      }
      
      public function method_1556(param1:int) : void
      {
         var _loc3_:TextField = null;
         var _loc2_:uint = 0;
         while(_loc2_ < Game.const_79)
         {
            _loc3_ = this.var_521[_loc2_].mMovieClip.am_Text;
            if(_loc3_.text == var_1.mKeybindManager.GetReadableKey(param1))
            {
               _loc3_.text = this.const_1425;
            }
            _loc2_++;
         }
      }
   }
}
