package
{
   import flash.utils.Dictionary;
   
   public class class_17
   {
       
      
      internal var var_382:uint;
      
      internal var var_61:String;
      
      internal var displayName:String;
      
      internal var description:Array;
      
      internal var var_444:String;
      
      internal var var_660:Object;
      
      internal var var_2737:Array;
      
      internal var var_2018:Object;
      
      internal var var_1472:class_40;
      
      internal var var_2725:String;
      
      internal var var_1741:String;
      
      internal var iconName:String;
      
      internal var var_2599:String;
      
      internal var statValue:Number;
      
      internal var var_593:String;
      
      internal var var_2404:Boolean = false;
      
      internal var var_2874:Boolean = false;
      
      public function class_17()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_872,class_14.var_274);
      }
      
      public static function method_649(param1:XML, param2:class_17) : class_17
      {
         var _loc4_:Array = null;
         var _loc5_:Array = null;
         var _loc6_:Array = null;
         var _loc7_:Array = null;
         var _loc8_:Array = null;
         var _loc9_:Array = null;
         var _loc10_:String = null;
         var _loc11_:String = null;
         var _loc12_:int = 0;
         var _loc13_:int = 0;
         var _loc14_:Boolean = false;
         var _loc15_:XML = null;
         var _loc16_:String = null;
         var _loc17_:String = null;
         var _loc18_:String = null;
         var _loc19_:String = null;
         var _loc20_:String = null;
         var _loc21_:String = null;
         var _loc22_:String = null;
         var _loc23_:String = null;
         var _loc24_:String = null;
         var _loc25_:class_38 = null;
         var _loc26_:String = null;
         var _loc27_:class_39 = null;
         var _loc3_:class_17 = new class_17();
         _loc3_.var_61 = param1.attribute("PowerModName");
         for each(_loc15_ in param1.*)
         {
            if((_loc16_ = String(_loc15_.name().toString())) == "ModID")
            {
               _loc3_.var_382 = uint(_loc15_);
            }
            else if(_loc16_ == "ModName")
            {
               _loc3_.var_61 = _loc15_.toString();
            }
            else if(_loc16_ == "DisplayName")
            {
               _loc3_.displayName = _loc15_.toString();
            }
            else if(_loc16_ == "Description")
            {
               _loc17_ = _loc15_.toString();
               _loc3_.description = !!_loc17_ ? _loc17_.split("@") : null;
               _loc14_ = true;
            }
            else if(_loc16_ == "ModType")
            {
               _loc3_.var_444 = _loc15_.toString();
            }
            else if(_loc16_ == "BuffName")
            {
               _loc4_ = (_loc18_ = _loc15_.toString()).split(",");
            }
            else if(_loc16_ == "BuffProperty")
            {
               _loc5_ = (_loc19_ = _loc15_.toString()).split(",");
            }
            else if(_loc16_ == "BuffValue")
            {
               _loc6_ = (_loc20_ = _loc15_.toString()).split(",");
            }
            else if(_loc16_ == "PowerName")
            {
               _loc7_ = (_loc21_ = _loc15_.toString()).split(",");
            }
            else if(_loc16_ == "PowerProperty")
            {
               _loc8_ = (_loc22_ = _loc15_.toString()).split(",");
            }
            else if(_loc16_ == "PowerValue")
            {
               _loc9_ = (_loc23_ = _loc15_.toString()).split(",");
            }
            else if(_loc16_ == "ProcName")
            {
               _loc10_ = _loc15_.toString();
            }
            else if(_loc16_ == "ProcChance")
            {
               _loc11_ = _loc15_.toString();
            }
            else if(_loc16_ == "SelfProperty")
            {
               _loc3_.var_2725 = _loc15_.toString();
            }
            else if(_loc16_ == "SelfValue")
            {
               _loc3_.var_1741 = _loc15_.toString();
            }
            else if(_loc16_ == "IconName")
            {
               _loc3_.iconName = _loc15_.toString();
            }
            else if(_loc16_ == "StatProperty")
            {
               _loc3_.var_2599 = _loc15_.toString();
            }
            else if(_loc16_ == "StatValue")
            {
               _loc3_.statValue = Number(_loc15_);
            }
            else if(_loc16_ == "ComboMod")
            {
               _loc3_.var_593 = _loc15_.toString();
               if(_loc3_.var_593 == _loc3_.var_61)
               {
                  class_24.method_7("PowerModType can not have itself as a ComboMod: " + _loc3_.var_61);
               }
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc3_.var_61 + ": " + _loc16_);
            }
         }
         if(_loc3_.var_444 == "Buff")
         {
            if(Boolean(_loc4_) && Boolean(_loc5_) && Boolean(_loc6_))
            {
               if(_loc5_.length != _loc6_.length)
               {
                  class_24.method_7("Buff Value length must match Buff Property length for " + _loc3_.var_61);
               }
               _loc3_.var_660 = new Object();
               _loc3_.var_2737 = new Array();
               _loc12_ = 0;
               while(_loc12_ < _loc4_.length)
               {
                  _loc24_ = String(_loc4_[_loc12_]);
                  _loc25_ = new class_38(_loc24_);
                  _loc13_ = 0;
                  while(_loc13_ < _loc5_.length)
                  {
                     _loc25_.add(_loc5_[_loc13_],_loc6_[_loc13_]);
                     _loc25_.mOrder.push(_loc5_[_loc13_]);
                     _loc13_++;
                  }
                  _loc3_.var_660[_loc24_] = _loc25_;
                  _loc3_.var_2737.push(_loc24_);
                  _loc12_++;
               }
            }
            else
            {
               class_24.method_7("Modtype: Buff is missing required buff fields to mod for " + _loc3_.var_61);
            }
         }
         else if(_loc3_.var_444 == "Power")
         {
            if(Boolean(_loc7_) && Boolean(_loc8_) && Boolean(_loc9_))
            {
               if(_loc8_.length != _loc8_.length)
               {
                  class_24.method_7("Power Value length must match Power Property length for " + _loc3_.var_61);
               }
               _loc3_.var_2018 = new Object();
               _loc12_ = 0;
               while(_loc12_ < _loc7_.length)
               {
                  _loc26_ = String(_loc7_[_loc12_]);
                  _loc27_ = new class_39(_loc26_);
                  _loc13_ = 0;
                  while(_loc13_ < _loc8_.length)
                  {
                     _loc27_.add(_loc8_[_loc13_],_loc9_);
                     _loc13_++;
                  }
                  _loc3_.var_2018[_loc26_] = _loc27_;
                  _loc12_++;
               }
            }
            else
            {
               class_24.method_7("Modtype: Power is missing required power fields to mod for " + _loc3_.var_61);
            }
         }
         else if(_loc3_.var_444 == "Proc")
         {
            if(Boolean(_loc11_) && Boolean(_loc10_))
            {
               _loc3_.var_1472 = new class_40(_loc3_.var_61,_loc10_,_loc11_);
            }
            else
            {
               class_24.method_7("Modtype: Proc is missing required proc fields to mod for " + _loc3_.var_61);
            }
         }
         else if(_loc3_.var_444 != "Self")
         {
            if(_loc3_.var_444 != "Stat")
            {
               if(_loc3_.var_444 != "WTF")
               {
                  if(_loc3_.var_444 != "Ability")
                  {
                     if(_loc3_.var_444 != "Other")
                     {
                        class_24.method_7("Unknown ModType for " + _loc3_.var_61);
                     }
                  }
               }
            }
         }
         if(!_loc14_)
         {
            _loc3_.description = param2.description;
         }
         if(_loc3_.var_61 == "RuneSoulReaver")
         {
            _loc3_.var_593 = "ComboRuneSoulReaver";
         }
         if(_loc3_.var_61 == "RuneGhostBlade")
         {
            _loc3_.var_593 = "ComboRuneGhostBlade";
         }
         if(!_loc3_.var_61.indexOf("BloodBond"))
         {
            _loc3_.var_2404 = true;
            _loc3_.var_593 = "ComboBloodBond";
         }
         if(!_loc3_.var_61.indexOf("RuneSummonGhoul") || !_loc3_.var_61.indexOf("RuneSummonRangedGhoul"))
         {
            _loc3_.var_2404 = true;
         }
         if(!_loc3_.var_61.indexOf("HealingBoon"))
         {
            _loc3_.var_593 = "ComboHealingBoon";
         }
         if(!_loc3_.var_61.indexOf("Fortify"))
         {
            _loc3_.var_593 = "ComboFortify";
         }
         if(!_loc3_.var_61.indexOf("FaithArmor"))
         {
            _loc3_.var_593 = "ComboFaithArmor";
         }
         if(_loc3_.var_61 == "ComboBloodBond" || _loc3_.var_61 == "ComboHealingBoon" || _loc3_.var_61 == "ComboFortify" || _loc3_.var_61 == "ComboFaithArmor")
         {
            _loc3_.var_2874 = true;
         }
         return _loc3_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary) : void
      {
         var _loc4_:class_17 = null;
         var _loc5_:XML = null;
         var _loc6_:class_17 = null;
         for each(_loc5_ in param1.*)
         {
            _loc4_ = _loc6_ = method_649(_loc5_,_loc4_);
            if(_loc6_.var_382)
            {
               if(param2[_loc6_.var_382])
               {
                  class_24.method_7("Multiple PowerID with ID: " + _loc6_.var_382);
               }
               if(param3[_loc6_.var_61])
               {
                  class_24.method_7("Multiple PowerMod with name: " + _loc6_.var_61);
               }
               param2[_loc6_.var_382] = _loc6_;
               param3[_loc6_.var_61] = _loc6_;
            }
         }
      }
   }
}
