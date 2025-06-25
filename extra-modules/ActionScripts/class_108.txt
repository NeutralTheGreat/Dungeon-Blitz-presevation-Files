package
{
   import flash.ui.Keyboard;
   import flash.utils.Dictionary;
   
   public class class_108
   {
      
      internal static const UNBOUNDKEY:int = 255;
      
      public static const const_595:uint = 1 << 0;
      
      public static const const_1277:uint = 1 << 1;
       
      
      internal var var_990:int;
      
      private var var_74:int;
      
      private var var_1272:int;
      
      private var var_67:Array;
      
      private var var_169:Dictionary;
      
      private var var_1702:Array;
      
      private var var_975:Array;
      
      private var var_1518:Array;
      
      private var mDefault2:Array;
      
      private var var_1156:Vector.<String>;
      
      private var var_9:Vector.<String>;
      
      public var mbStatePickKey:Boolean = false;
      
      public var mActiveCommand:int = 0;
      
      public var var_2960:Boolean = false;
      
      private var var_1158:Vector.<Object>;
      
      public var mbDefault:Boolean = false;
      
      public function class_108(param1:int)
      {
         super();
         this.var_990 = param1;
         this.method_1885();
         this.var_67 = new Array();
         this.var_74 = -1;
         this.var_1702 = new Array();
         this.var_975 = new Array();
         this.var_1156 = new Vector.<String>(this.var_990 + 1);
         this.var_1156[0] = "";
         this.var_1158 = new Vector.<Object>();
      }
      
      public function method_31(param1:int, param2:int = -1) : int
      {
         var _loc3_:int = this.var_74;
         if(param2 != -1)
         {
            _loc3_ = param2;
         }
         var _loc4_:Array = this.var_67[_loc3_]["map"];
         var _loc5_:Array = this.var_67[_loc3_]["map2"];
         var _loc6_:uint;
         if(!(_loc6_ = uint(_loc4_[param1])) && Boolean(_loc5_))
         {
            _loc6_ = uint(_loc5_[param1]);
         }
         return _loc6_;
      }
      
      public function FetchKeyFromCommand(param1:int, param2:Boolean = false, param3:Boolean = false) : String
      {
         var _loc4_:Array = null;
         var _loc5_:Array = null;
         var _loc6_:int = 0;
         if(param2)
         {
            if(!param3)
            {
               _loc4_ = this.var_169["map"];
            }
            else
            {
               _loc4_ = this.var_169["map2"];
            }
            _loc5_ = this.var_169["exceptions"];
         }
         else
         {
            if(!param3)
            {
               _loc4_ = this.var_67[this.var_74]["map"];
            }
            else
            {
               _loc4_ = this.var_67[this.var_74]["map2"];
            }
            _loc5_ = this.var_67[this.var_74]["exceptions"];
         }
         if(param1 == 255)
         {
            return "---";
         }
         if(param1 > 0 && param1 <= this.var_990)
         {
            _loc6_ = 0;
            while(_loc6_ < _loc4_.length)
            {
               if(_loc5_.indexOf(_loc6_) <= -1)
               {
                  if(this.var_975.indexOf(_loc6_) <= -1)
                  {
                     if(_loc4_[_loc6_] == param1)
                     {
                        return this.GetReadableKey(_loc6_);
                     }
                  }
               }
               _loc6_++;
            }
         }
         return "---";
      }
      
      public function method_2113(param1:int, param2:Boolean = false, param3:Boolean = false) : int
      {
         var _loc4_:Array = null;
         var _loc5_:Array = null;
         var _loc6_:int = 0;
         if(param2)
         {
            if(!param3)
            {
               _loc4_ = this.var_169["map"];
            }
            else
            {
               _loc4_ = this.var_169["map2"];
            }
            _loc5_ = this.var_169["exceptions"];
         }
         else
         {
            if(!param3)
            {
               _loc4_ = this.var_67[this.var_74]["map"];
            }
            else
            {
               _loc4_ = this.var_67[this.var_74]["map2"];
            }
            _loc5_ = this.var_67[this.var_74]["exceptions"];
         }
         if(param1 > 0 && param1 <= this.var_990)
         {
            _loc6_ = 0;
            while(_loc6_ < _loc4_.length)
            {
               if(_loc5_.indexOf(_loc6_) <= -1)
               {
                  if(_loc4_[_loc6_] == param1)
                  {
                     return _loc6_;
                  }
               }
               _loc6_++;
            }
         }
         return UNBOUNDKEY;
      }
      
      public function method_1805(param1:int) : Boolean
      {
         if(this.var_1702.indexOf(param1) > -1)
         {
            return false;
         }
         return true;
      }
      
      public function method_32(param1:int, param2:int, param3:Boolean = true, param4:Boolean = false, param5:Boolean = false) : int
      {
         var _loc6_:Array = null;
         var _loc7_:int = 0;
         if(param4)
         {
            _loc6_ = this.var_169["map"];
         }
         else
         {
            _loc6_ = this.var_67[this.var_74]["map"];
         }
         if(!_loc6_)
         {
            return _loc7_;
         }
         if(!param3)
         {
            this.method_848(param2);
         }
         if(param5)
         {
            this.var_975[param1] = param2;
         }
         var _loc8_:uint = 0;
         while(_loc8_ < this.var_975.length)
         {
            if(this.var_975[_loc8_] == param2 && param1 != _loc8_)
            {
               delete this.var_975[_loc8_];
            }
            _loc8_++;
         }
         if(!(this.var_67[this.var_74]["flags"] & const_595))
         {
            _loc7_ = this.method_1959(param1,param4);
         }
         _loc6_[param2] = param1;
         return _loc7_;
      }
      
      public function method_2094(param1:int, param2:int, param3:Boolean = true, param4:Boolean = false) : int
      {
         var _loc5_:Array = null;
         var _loc6_:int = 0;
         if(param4)
         {
            _loc5_ = this.var_169["map2"];
         }
         else
         {
            _loc5_ = this.var_67[this.var_74]["map2"];
         }
         if(!_loc5_)
         {
            return _loc6_;
         }
         if(!param3)
         {
            this.method_848(param2);
         }
         if(!(this.var_67[this.var_74]["flags"] & const_595))
         {
            _loc6_ = this.method_1945(param1,param4);
         }
         _loc5_[param2] = param1;
         return _loc6_;
      }
      
      private function method_1959(param1:int, param2:Boolean = false) : int
      {
         var _loc3_:Array = null;
         var _loc4_:Array = null;
         var _loc5_:String = null;
         if(param1 == class_108.UNBOUNDKEY)
         {
            return 0;
         }
         if(param2)
         {
            _loc3_ = this.var_169["map"];
            _loc4_ = this.var_169["exceptions"];
         }
         else
         {
            _loc3_ = this.var_67[this.var_74]["map"];
            _loc4_ = this.var_67[this.var_74]["exceptions"];
         }
         for(_loc5_ in _loc3_)
         {
            if(_loc4_.indexOf(int(_loc5_)) <= -1)
            {
               if(this.var_975.indexOf(int(_loc5_)) <= -1)
               {
                  if(param1 == _loc3_[_loc5_])
                  {
                     if(this.var_1518[_loc5_] == param1)
                     {
                        delete _loc3_[_loc5_];
                        return 0;
                     }
                     _loc3_[_loc5_] = 255;
                     return int(_loc5_);
                  }
               }
            }
         }
         return 0;
      }
      
      private function method_1945(param1:int, param2:Boolean = false) : int
      {
         var _loc3_:Array = null;
         var _loc4_:Array = null;
         var _loc5_:String = null;
         if(param1 == class_108.UNBOUNDKEY)
         {
            return 0;
         }
         if(param2)
         {
            _loc3_ = this.var_169["map2"];
            _loc4_ = this.var_169["exceptions"];
         }
         else
         {
            _loc3_ = this.var_67[this.var_74]["map2"];
            _loc4_ = this.var_67[this.var_74]["exceptions"];
         }
         for(_loc5_ in _loc3_)
         {
            if(_loc4_.indexOf(int(_loc5_)) <= -1)
            {
               if(param1 == _loc3_[_loc5_])
               {
                  if(this.mDefault2[_loc5_] == param1)
                  {
                     delete _loc3_[_loc5_];
                     return 0;
                  }
                  _loc3_[_loc5_] = 255;
                  return int(_loc5_);
               }
            }
         }
         return 0;
      }
      
      public function method_2016(param1:uint, param2:Boolean = false, param3:Boolean = false) : void
      {
         var _loc4_:Array = null;
         if(param1 == UNBOUNDKEY)
         {
            return;
         }
         if(param2)
         {
            if(!param3)
            {
               _loc4_ = this.var_169["map"];
            }
            else
            {
               _loc4_ = this.var_169["map2"];
            }
         }
         else if(!param3)
         {
            _loc4_ = this.var_67[this.var_74]["map"];
         }
         else
         {
            _loc4_ = this.var_67[this.var_74]["map2"];
         }
         if(_loc4_)
         {
            delete _loc4_[param1];
         }
      }
      
      private function method_848(param1:int) : void
      {
         var _loc2_:Array = this.var_67[this.var_74]["exceptions"];
         _loc2_.push(param1);
         this.var_1702.push(param1);
      }
      
      public function method_181(param1:int) : void
      {
         this.var_1702.push(param1);
      }
      
      public function method_794(param1:uint = 0) : int
      {
         ++this.var_74;
         var _loc2_:Dictionary = new Dictionary();
         var _loc3_:Array = new Array();
         var _loc4_:Array = new Array();
         _loc2_["map"] = _loc3_;
         _loc2_["exceptions"] = _loc4_;
         _loc2_["flags"] = param1;
         this.var_67.push(_loc2_);
         return this.var_74;
      }
      
      public function SetContext(param1:int) : void
      {
         if(this.var_74 >= 0 && this.var_74 < this.var_67.length)
         {
            this.var_74 = param1;
         }
      }
      
      public function method_1424(param1:int) : void
      {
         this.var_1272 = param1;
         this.var_1518 = this.var_67[this.var_1272]["map"].slice();
         if(this.var_67[this.var_1272]["map2"])
         {
            this.mDefault2 = this.var_67[this.var_1272]["map2"].slice();
         }
         this.mbDefault = true;
      }
      
      public function GenerateServerPacket() : Vector.<Object>
      {
         var _loc5_:String = null;
         var _loc6_:int = 0;
         var _loc7_:int = 0;
         var _loc8_:Object = null;
         this.mbDefault = true;
         var _loc1_:Array = this.var_67[this.var_1272]["map"];
         var _loc2_:Array = this.var_67[this.var_1272]["exceptions"];
         var _loc3_:Vector.<int> = new Vector.<int>(this.var_990 + 1);
         var _loc4_:Vector.<Boolean> = new Vector.<Boolean>(this.var_990 + 1);
         _loc6_ = 1;
         while(_loc6_ < _loc4_.length)
         {
            _loc4_[_loc6_] = false;
            _loc6_++;
         }
         for(_loc5_ in _loc1_)
         {
            if(int(_loc5_) != 255)
            {
               if(_loc1_[int(_loc5_)] <= this.var_990 + 1)
               {
                  if(_loc1_[int(_loc5_)] != undefined)
                  {
                     if(_loc2_.indexOf(int(_loc5_)) <= -1)
                     {
                        if((_loc7_ = int(_loc1_[int(_loc5_)])) < _loc4_.length)
                        {
                           _loc4_[_loc7_] = true;
                        }
                        if(_loc7_ != this.var_1518[int(_loc5_)])
                        {
                           _loc3_[_loc7_] = int(_loc5_);
                        }
                     }
                  }
               }
            }
         }
         _loc6_ = 1;
         while(_loc6_ < _loc3_.length)
         {
            if(_loc3_[_loc6_] != 0)
            {
               (_loc8_ = new Object())["exists"] = true;
               _loc8_["key"] = _loc3_[_loc6_];
               this.var_1158.push(_loc8_);
               this.mbDefault = false;
            }
            else if(!_loc4_[_loc6_] && this.var_1518.indexOf(_loc6_) > -1)
            {
               this.mbDefault = false;
               (_loc8_ = new Object())["exists"] = true;
               _loc8_["key"] = class_108.UNBOUNDKEY;
               this.var_1158.push(_loc8_);
               this.mbDefault = false;
            }
            else
            {
               (_loc8_ = new Object())["exists"] = false;
               this.var_1158.push(_loc8_);
            }
            _loc6_++;
         }
         return this.var_1158;
      }
      
      public function ClearServerPacket() : void
      {
         this.var_1158.length = 0;
      }
      
      public function method_44(param1:String, param2:int) : void
      {
         if(param2 < this.var_1156.length)
         {
            this.var_1156[param2] = param1;
         }
      }
      
      public function GetReadableCommands(param1:int) : String
      {
         if(param1 < this.var_1156.length)
         {
            return this.var_1156[param1];
         }
         return "";
      }
      
      public function GetReadableKey(param1:int) : String
      {
         if(param1 < this.var_9.length)
         {
            return this.var_9[param1];
         }
         return "";
      }
      
      private function method_1885() : void
      {
         this.var_9 = new Vector.<String>(256);
         this.var_9[Keyboard.LEFT] = "[LEFT]";
         this.var_9[Keyboard.RIGHT] = "[RIGHT]";
         this.var_9[Keyboard.UP] = "[UP]";
         this.var_9[Keyboard.DOWN] = "[DOWN]";
         this.var_9[Keyboard.SPACE] = "[SPACE]";
         this.var_9[Keyboard.A] = "A";
         this.var_9[Keyboard.B] = "B";
         this.var_9[Keyboard.C] = "C";
         this.var_9[Keyboard.D] = "D";
         this.var_9[Keyboard.E] = "E";
         this.var_9[Keyboard.F] = "F";
         this.var_9[Keyboard.G] = "G";
         this.var_9[Keyboard.H] = "H";
         this.var_9[Keyboard.I] = "I";
         this.var_9[Keyboard.J] = "J";
         this.var_9[Keyboard.K] = "K";
         this.var_9[Keyboard.L] = "L";
         this.var_9[Keyboard.M] = "M";
         this.var_9[Keyboard.N] = "N";
         this.var_9[Keyboard.O] = "O";
         this.var_9[Keyboard.P] = "P";
         this.var_9[Keyboard.Q] = "Q";
         this.var_9[Keyboard.R] = "R";
         this.var_9[Keyboard.S] = "S";
         this.var_9[Keyboard.T] = "T";
         this.var_9[Keyboard.U] = "U";
         this.var_9[Keyboard.V] = "V";
         this.var_9[Keyboard.W] = "W";
         this.var_9[Keyboard.X] = "X";
         this.var_9[Keyboard.Y] = "Y";
         this.var_9[Keyboard.Z] = "Z";
         this.var_9[Keyboard.NUMBER_0] = "0";
         this.var_9[Keyboard.NUMBER_1] = "1";
         this.var_9[Keyboard.NUMBER_2] = "2";
         this.var_9[Keyboard.NUMBER_3] = "3";
         this.var_9[Keyboard.NUMBER_4] = "4";
         this.var_9[Keyboard.NUMBER_5] = "5";
         this.var_9[Keyboard.NUMBER_6] = "6";
         this.var_9[Keyboard.NUMBER_7] = "7";
         this.var_9[Keyboard.NUMBER_8] = "8";
         this.var_9[Keyboard.NUMBER_9] = "9";
         this.var_9[Keyboard.BACKSPACE] = "[Backspace]";
         this.var_9[Keyboard.TAB] = "[Tab]";
         this.var_9[Keyboard.SEMICOLON] = ";";
         this.var_9[Keyboard.EQUAL] = "=";
         this.var_9[Keyboard.COMMA] = ",";
         this.var_9[Keyboard.MINUS] = "-";
         this.var_9[Keyboard.PERIOD] = ".";
         this.var_9[Keyboard.BACKQUOTE] = "`";
         this.var_9[Keyboard.LEFTBRACKET] = "[";
         this.var_9[Keyboard.RIGHTBRACKET] = "]";
         this.var_9[Keyboard.QUOTE] = "\'";
         this.var_9[Keyboard.NUMPAD_0] = "NUM_0";
         this.var_9[Keyboard.NUMPAD_1] = "NUM_1";
         this.var_9[Keyboard.NUMPAD_2] = "NUM_2";
         this.var_9[Keyboard.NUMPAD_3] = "NUM_3";
         this.var_9[Keyboard.NUMPAD_4] = "NUM_4";
         this.var_9[Keyboard.NUMPAD_5] = "NUM_5";
         this.var_9[Keyboard.NUMPAD_6] = "NUM_6";
         this.var_9[Keyboard.NUMPAD_7] = "NUM_7";
         this.var_9[Keyboard.NUMPAD_8] = "NUM_8";
         this.var_9[Keyboard.NUMPAD_9] = "NUM_9";
         this.var_9[Keyboard.NUMPAD_MULTIPLY] = "*";
         this.var_9[Keyboard.NUMPAD_ADD] = "+";
         this.var_9[Keyboard.NUMPAD_SUBTRACT] = "-";
         this.var_9[Keyboard.NUMPAD_DECIMAL] = ".";
         this.var_9[Keyboard.NUMPAD_DIVIDE] = "/";
         this.var_9[Keyboard.PAGE_UP] = "[Page Up]";
         this.var_9[Keyboard.PAGE_DOWN] = "[Page Down]";
         this.var_9[Keyboard.END] = "[End]";
         this.var_9[Keyboard.HOME] = "[Home]";
         this.var_9[Keyboard.INSERT] = "[Insert]";
         this.var_9[Keyboard.DELETE] = "[Delete]";
         this.var_9[144] = "[Num Lock]";
         this.var_9[145] = "[Scroll Lock]";
         this.var_9[19] = "[Pause]";
         this.var_9[Keyboard.F1] = "F1";
         this.var_9[Keyboard.F2] = "F2";
         this.var_9[Keyboard.F3] = "F3";
         this.var_9[Keyboard.F4] = "F4";
         this.var_9[Keyboard.F5] = "F5";
         this.var_9[Keyboard.F6] = "F6";
         this.var_9[Keyboard.F7] = "F7";
         this.var_9[Keyboard.F8] = "F8";
         this.var_9[Keyboard.F9] = "F9";
         this.var_9[Keyboard.F10] = "F10";
         this.var_9[Keyboard.F11] = "F11";
         this.var_9[Keyboard.F12] = "F12";
         this.var_9[Keyboard.F13] = "F13";
         this.var_9[Keyboard.F14] = "F14";
         this.var_9[Keyboard.F15] = "F15";
         this.var_9[126] = "F16";
         this.var_9[255] = "---";
         this.var_9[Keyboard.SHIFT] = "[SHIFT]";
         this.var_9[Keyboard.ALTERNATE] = "[ALT]";
         this.var_9[Keyboard.CONTROL] = "[CTRL]";
         this.var_9[Keyboard.CAPS_LOCK] = "[Caps Lock]";
         this.var_9[Keyboard.SLASH] = "/";
         this.var_9[Keyboard.BACKSLASH] = "\\";
      }
      
      public function WriteIntoBuffer() : void
      {
         var _loc4_:Array = null;
         var _loc1_:Dictionary = new Dictionary();
         var _loc2_:Array = this.var_67[this.var_74]["map"].slice();
         var _loc3_:Array = this.var_67[this.var_74]["exceptions"].slice();
         if(this.var_67[this.var_74]["map2"])
         {
            _loc4_ = this.var_67[this.var_74]["map2"].slice();
            _loc1_["map2"] = _loc4_;
         }
         _loc1_["map"] = _loc2_;
         _loc1_["exceptions"] = _loc3_;
         this.var_169 = _loc1_;
      }
      
      public function saveBufferIntoReal() : void
      {
         this.var_67[this.var_74] = this.var_169;
      }
      
      public function ClearBuffer() : void
      {
         this.var_169 = null;
      }
      
      public function WriteDefaultsIntoBuffer() : void
      {
         this.var_169["map"] = this.var_1518.slice();
         if(this.mDefault2)
         {
            this.var_169["map2"] = this.mDefault2.slice();
         }
         this.var_169["exceptions"] = this.var_67[this.var_74]["exceptions"].slice();
      }
      
      public function method_907(param1:uint, param2:int = -1) : uint
      {
         var _loc3_:uint = uint(this.method_31(param1));
         if(param1 == Keyboard.NUMPAD_0 && this.method_31(Keyboard.NUMBER_0,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMBER_0,param2));
         }
         if(param1 == Keyboard.NUMPAD_1 && this.method_31(Keyboard.NUMBER_1,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMBER_1,param2));
         }
         if(param1 == Keyboard.NUMPAD_2 && this.method_31(Keyboard.NUMBER_2,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMBER_2,param2));
         }
         if(param1 == Keyboard.NUMPAD_3 && this.method_31(Keyboard.NUMBER_3,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMBER_3,param2));
         }
         if(param1 == Keyboard.NUMPAD_4 && this.method_31(Keyboard.NUMBER_4,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMBER_4,param2));
         }
         if(param1 == Keyboard.NUMPAD_5 && this.method_31(Keyboard.NUMBER_5,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMBER_5,param2));
         }
         if(param1 == Keyboard.NUMPAD_6 && this.method_31(Keyboard.NUMBER_6,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMBER_6,param2));
         }
         if(param1 == Keyboard.NUMPAD_7 && this.method_31(Keyboard.NUMBER_7,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMBER_7,param2));
         }
         if(param1 == Keyboard.NUMPAD_8 && this.method_31(Keyboard.NUMBER_8,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMBER_8,param2));
         }
         if(param1 == Keyboard.NUMPAD_9 && this.method_31(Keyboard.NUMBER_9,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMBER_9,param2));
         }
         if(param1 == Keyboard.NUMBER_0 && this.method_31(Keyboard.NUMPAD_0,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMPAD_0,param2));
         }
         if(param1 == Keyboard.NUMBER_1 && this.method_31(Keyboard.NUMPAD_1,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMPAD_1,param2));
         }
         if(param1 == Keyboard.NUMBER_2 && this.method_31(Keyboard.NUMPAD_2,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMPAD_2,param2));
         }
         if(param1 == Keyboard.NUMBER_3 && this.method_31(Keyboard.NUMPAD_3,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMPAD_3,param2));
         }
         if(param1 == Keyboard.NUMBER_4 && this.method_31(Keyboard.NUMPAD_4,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMPAD_4,param2));
         }
         if(param1 == Keyboard.NUMBER_5 && this.method_31(Keyboard.NUMPAD_5,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMPAD_5,param2));
         }
         if(param1 == Keyboard.NUMBER_6 && this.method_31(Keyboard.NUMPAD_6,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMPAD_6,param2));
         }
         if(param1 == Keyboard.NUMBER_7 && this.method_31(Keyboard.NUMPAD_7,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMPAD_7,param2));
         }
         if(param1 == Keyboard.NUMBER_8 && this.method_31(Keyboard.NUMPAD_8,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMPAD_8,param2));
         }
         if(param1 == Keyboard.NUMBER_9 && this.method_31(Keyboard.NUMPAD_9,param2) && (!_loc3_ || _loc3_ == 255))
         {
            _loc3_ = uint(this.method_31(Keyboard.NUMPAD_9,param2));
         }
         return _loc3_;
      }
   }
}
