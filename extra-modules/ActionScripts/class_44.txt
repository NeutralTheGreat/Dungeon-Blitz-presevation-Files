package
{
   import flash.utils.Dictionary;
   
   public class class_44
   {
       
      
      public var var_1:Game;
      
      public var ownEnt:Entity;
      
      public var var_3003:int;
      
      public var var_2994:int;
      
      public var var_2977:int;
      
      public var var_3000:int;
      
      public var var_539:Object;
      
      public var var_2418:Object;
      
      public var var_567:Object;
      
      public var var_907:Object;
      
      public var var_1582:Object;
      
      public var var_766:Object;
      
      public var var_1030:Object;
      
      public var var_1256:Array;
      
      public var var_1007:Array;
      
      public var var_1927:Vector.<uint>;
      
      public function class_44(param1:Game, param2:class_118, param3:Entity)
      {
         super();
         this.var_1 = param1;
         this.method_1788(param2,param3);
      }
      
      public function method_577() : void
      {
         var _loc1_:Dictionary = null;
         var _loc2_:Object = null;
         var _loc3_:Object = null;
         var _loc4_:Array = null;
         for each(_loc1_ in this.var_539)
         {
            for each(_loc4_ in _loc1_)
            {
               _loc4_ = null;
            }
            _loc1_ = null;
         }
         this.var_539 = null;
         this.var_2418 = null;
         for each(_loc2_ in this.var_567)
         {
            _loc2_ = null;
         }
         this.var_567 = null;
         for each(_loc3_ in this.var_907)
         {
            _loc3_ = null;
         }
         this.var_907 = null;
         this.var_1582 = null;
         this.var_766 = null;
         this.var_1030 = null;
         this.var_1256 = null;
         this.var_1007 = null;
         this.var_1927 = null;
      }
      
      public function method_1788(param1:class_118, param2:Entity) : void
      {
         var _loc3_:String = null;
         var _loc4_:Vector.<class_148> = null;
         var _loc5_:Vector.<class_22> = null;
         var _loc6_:int = 0;
         var _loc7_:class_148 = null;
         var _loc8_:class_22 = null;
         var _loc9_:class_17 = null;
         var _loc10_:Vector.<EntTypeGear> = null;
         var _loc11_:EntTypeGear = null;
         var _loc12_:Vector.<uint> = null;
         var _loc13_:String = null;
         var _loc14_:GearType = null;
         var _loc15_:String = null;
         var _loc16_:uint = 0;
         this.method_577();
         this.var_567 = new Object();
         this.var_539 = new Object();
         this.var_2418 = new Object();
         this.var_907 = new Object();
         this.var_1582 = new Object();
         this.var_766 = new Object();
         this.var_1030 = new Object();
         this.var_1256 = new Array();
         this.var_1007 = new Array();
         this.var_1927 = new Vector.<uint>();
         if(!param2)
         {
            return;
         }
         if(param1)
         {
            _loc3_ = param2.mMasterClass;
            _loc4_ = param1.var_58;
            if(_loc5_ = class_14.var_368[_loc3_])
            {
               _loc6_ = 0;
               while(_loc6_ < _loc4_.length)
               {
                  if(_loc7_ = _loc4_[_loc6_])
                  {
                     _loc9_ = !!(_loc8_ = _loc7_.mNodeType) ? class_14.var_274[_loc8_.var_548 + _loc7_.mPointsSpent] : null;
                     this.method_306(_loc9_);
                  }
                  _loc6_++;
               }
            }
         }
         if(param2)
         {
            _loc10_ = param2.entType.equippedGear;
            for each(_loc11_ in _loc10_)
            {
               if(_loc13_ = !!_loc11_ ? _loc11_.gearName : null)
               {
                  _loc9_ = !!(_loc15_ = !!(_loc14_ = class_14.gearTypesDict[_loc13_]) ? "Rune" + _loc14_.var_1062 : null) ? class_14.var_274[_loc15_] : null;
                  this.method_306(_loc9_);
               }
            }
            if(_loc12_ = param2.var_1283)
            {
               for each(_loc16_ in _loc12_)
               {
                  _loc9_ = !!_loc16_ ? class_14.var_872[_loc16_] : null;
                  this.method_306(_loc9_);
               }
            }
         }
      }
      
      private function method_1863(param1:class_17) : void
      {
         var _loc2_:String = null;
         var _loc3_:String = null;
         var _loc4_:Dictionary = null;
         var _loc5_:String = null;
         var _loc8_:Object = null;
         var _loc9_:String = null;
         var _loc10_:Object = null;
         var _loc11_:Dictionary = null;
         var _loc12_:Array = null;
         var _loc13_:Object = null;
         var _loc14_:String = null;
         var _loc15_:Object = null;
         var _loc16_:Object = null;
         var _loc17_:Object = null;
         var _loc18_:class_40 = null;
         var _loc19_:String = null;
         var _loc20_:String = null;
         var _loc21_:String = null;
         var _loc22_:String = null;
         var _loc23_:Number = NaN;
         var _loc24_:Number = NaN;
         if(!param1)
         {
            return;
         }
         var _loc6_:uint = param1.var_382;
         var _loc7_:String;
         if((_loc7_ = param1.var_444) == "Buff")
         {
            _loc8_ = param1.var_660;
            for(_loc9_ in _loc8_)
            {
               _loc10_ = _loc8_[_loc9_].mBuffProperty;
               this.var_2418[_loc9_] = _loc8_[_loc9_].mOrder;
               for(_loc3_ in _loc10_)
               {
                  _loc2_ = String(_loc10_[_loc3_]);
                  if(this.var_539.hasOwnProperty(_loc9_))
                  {
                     if((_loc4_ = this.var_539[_loc9_])[_loc3_])
                     {
                        _loc5_ = String(this.var_539[_loc9_][_loc3_][_loc6_]);
                        if(_loc4_[_loc3_][_loc6_])
                        {
                           _loc4_[_loc3_][_loc6_] = this.method_291(_loc5_,_loc2_);
                        }
                        else
                        {
                           _loc4_[_loc3_][_loc6_] = _loc2_;
                        }
                     }
                     else
                     {
                        _loc4_[_loc3_] = new Array();
                        _loc4_[_loc3_][_loc6_] = _loc2_;
                     }
                  }
                  else
                  {
                     _loc11_ = new Dictionary();
                     (_loc12_ = new Array())[_loc6_] = _loc2_;
                     _loc11_[_loc3_] = _loc12_;
                     this.var_539[_loc9_] = _loc11_;
                  }
               }
            }
         }
         else if(_loc7_ == "Power")
         {
            _loc13_ = param1.var_2018;
            for(_loc14_ in _loc13_)
            {
               _loc15_ = _loc13_[_loc14_].mAbilityProperty;
               for(_loc3_ in _loc15_)
               {
                  _loc2_ = String(_loc15_[_loc3_]);
                  if(this.var_567.hasOwnProperty(_loc14_))
                  {
                     if((_loc16_ = this.var_567[_loc14_]).hasOwnProperty(_loc3_))
                     {
                        _loc5_ = String(this.var_567[_loc14_][_loc3_]);
                        _loc16_[_loc3_] = this.method_291(_loc5_,_loc2_);
                     }
                     else
                     {
                        _loc16_[_loc3_] = _loc2_;
                     }
                  }
                  else
                  {
                     (_loc17_ = new Object())[_loc3_] = _loc2_;
                     this.var_567[_loc14_] = _loc17_;
                  }
               }
            }
         }
         else if(_loc7_ == "Proc")
         {
            _loc19_ = (_loc18_ = param1.var_1472).var_2811;
            _loc2_ = _loc18_.var_2823;
            if(this.var_907.hasOwnProperty(_loc19_))
            {
               this.var_907[_loc19_] = this.method_291(this.var_907[_loc19_],_loc2_);
            }
            else
            {
               this.var_907[_loc19_] = _loc2_;
            }
         }
         else if(_loc7_ == "Self")
         {
            _loc20_ = param1.var_2725;
            _loc21_ = param1.var_1741;
            if(this.var_1582.hasOwnProperty(_loc20_))
            {
               _loc21_ = this.method_291(this.var_1582[_loc20_],_loc21_);
            }
            this.var_1582[_loc20_] = _loc21_;
         }
         else if(_loc7_ == "Stat")
         {
            _loc22_ = param1.var_2599;
            _loc23_ = param1.statValue;
            if(this.var_766.hasOwnProperty(_loc22_))
            {
               _loc23_ = this.var_766[_loc22_] + _loc23_;
            }
            this.var_766[_loc22_] = _loc23_;
         }
         else if(_loc7_ == "WTF" || _loc7_ == "Other")
         {
            _loc24_ = Number(param1.var_1741);
            if(isNaN(_loc24_))
            {
               this.var_1030[param1.var_61] = param1.var_1741;
            }
            else
            {
               this.var_1030[param1.var_61] = !!this.var_1030[param1.var_61] ? this.var_1030[param1.var_61] + _loc24_ : _loc24_;
            }
         }
         else if(_loc7_ == "Ability")
         {
            this.var_1256.push(param1.var_61);
         }
      }
      
      private function method_291(param1:String, param2:String) : String
      {
         var _loc5_:String = null;
         var _loc6_:String = null;
         var _loc3_:Number = Number(param1);
         var _loc4_:Number = Number(param2);
         if(param1.indexOf(":") == -1 && param2.indexOf(":") == -1)
         {
            if(!isNaN(_loc3_) && !isNaN(_loc4_))
            {
               return String(_loc3_ + _loc4_);
            }
            return param1 + "," + param2;
         }
         if(param1.indexOf(":") == -1 != (param2.indexOf(":") == -1))
         {
            return param1 + "," + param2;
         }
         var _loc7_:Array = param1.split(":");
         var _loc8_:Array = param2.split(":");
         _loc3_ = Number(_loc7_[1]);
         _loc4_ = Number(_loc8_[1]);
         _loc5_ = String(_loc7_[0]);
         _loc6_ = String(_loc8_[0]);
         if(!isNaN(_loc3_) && !isNaN(_loc4_) && _loc5_ == _loc6_)
         {
            return _loc5_ + ":" + String(_loc3_ + _loc4_);
         }
         return param1 + "," + param2;
      }
      
      public function method_1670(param1:Entity, param2:String, param3:String, param4:uint) : Number
      {
         var _loc6_:String = null;
         var _loc7_:Array = null;
         var _loc8_:String = null;
         var _loc9_:Number = NaN;
         this.ownEnt = param1;
         var _loc5_:Number = 0;
         if(Boolean(this.var_539[param2]) && Boolean(this.var_539[param2][param3][param4]))
         {
            if((_loc7_ = (_loc6_ = String(this.var_539[param2][param3][param4])).split(":")).length > 1)
            {
               _loc8_ = String(_loc7_[0]);
               _loc9_ = Number(_loc7_[1]);
               _loc5_ = this.method_823(_loc8_,_loc9_);
            }
            else
            {
               _loc5_ = Number(_loc6_);
            }
         }
         return _loc5_;
      }
      
      private function method_823(param1:String, param2:Number) : Number
      {
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         if(!param1 || isNaN(param2))
         {
            return 0;
         }
         switch(param1)
         {
            case "MP":
               return 0;
            case "RP":
               _loc6_ = (_loc5_ = class_22.method_1160(this.ownEnt.mMasterClass,"Magic")) / 2;
               return this.ownEnt.magicDamage / _loc6_ * param2;
            case "AP":
               return this.ownEnt.meleeDamage * param2;
            case "AR":
               return this.ownEnt.armorClass * param2;
            default:
               return 0;
         }
      }
      
      public function method_64(param1:String) : Number
      {
         if(this.var_766)
         {
            return this.var_766.hasOwnProperty(param1) ? Number(this.var_766[param1]) : 0;
         }
         return 0;
      }
      
      public function method_492(param1:Vector.<String>, param2:String, param3:String) : Vector.<String>
      {
         var _loc4_:String = null;
         var _loc5_:Object = null;
         var _loc6_:Object = null;
         var _loc7_:Array = null;
         var _loc8_:int = 0;
         var _loc9_:Array = null;
         var _loc10_:Array = null;
         var _loc11_:String = null;
         var _loc12_:String = null;
         var _loc13_:int = 0;
         if(param3 == "AddTargetBuff" || param3 == "AddSelfBuff")
         {
            _loc5_ = this.var_567;
            if(param1 == null)
            {
               param1 = new Vector.<String>();
            }
            if(Boolean(_loc5_) && _loc5_.hasOwnProperty(param2))
            {
               if((_loc6_ = _loc5_[param2]).hasOwnProperty(param3))
               {
                  _loc4_ = String(_loc6_[param3]);
               }
               if(_loc4_)
               {
                  _loc7_ = _loc4_.split(",");
                  _loc8_ = 0;
                  while(_loc8_ < _loc7_.length)
                  {
                     if(!((_loc9_ = _loc7_[_loc8_].split(":"))[0] != "Append" && _loc9_[0] != "Replace"))
                     {
                        if(_loc9_.length >= 2)
                        {
                           if(_loc9_[0] == "Append")
                           {
                              param1.push(_loc9_[1]);
                           }
                           if(_loc9_[0] == "Replace")
                           {
                              if((_loc10_ = _loc9_[1].split("=")).length >= 2)
                              {
                                 _loc11_ = String(_loc10_[0]);
                                 _loc12_ = String(_loc10_[1]);
                                 _loc13_ = 0;
                                 while(_loc13_ < param1.length)
                                 {
                                    if(param1[_loc13_] == _loc11_)
                                    {
                                       param1[_loc13_] = _loc12_;
                                    }
                                    _loc13_++;
                                 }
                              }
                           }
                        }
                     }
                     _loc8_++;
                  }
               }
            }
         }
         return param1;
      }
      
      public function method_102(param1:Entity, param2:String, param3:String) : Number
      {
         var _loc5_:String = null;
         var _loc7_:Object = null;
         var _loc8_:Array = null;
         var _loc9_:String = null;
         var _loc10_:Number = NaN;
         this.ownEnt = param1;
         var _loc4_:Number = 0;
         var _loc6_:Object;
         if((Boolean(_loc6_ = this.var_567)) && _loc6_.hasOwnProperty(param2))
         {
            if((_loc7_ = _loc6_[param2]).hasOwnProperty(param3))
            {
               _loc5_ = String(_loc7_[param3]);
            }
            if(_loc5_)
            {
               if((_loc8_ = _loc5_.split(":")).length > 1)
               {
                  _loc9_ = String(_loc8_[0]);
                  _loc10_ = Number(_loc8_[1]);
                  _loc4_ = this.method_823(_loc9_,_loc10_);
               }
               else
               {
                  _loc4_ = Number(_loc5_);
               }
            }
         }
         return _loc4_;
      }
      
      public function method_101(param1:Entity, param2:BuffType) : Vector.<class_140>
      {
         var _loc3_:Vector.<Number> = null;
         var _loc7_:String = null;
         var _loc8_:uint = 0;
         var _loc9_:class_17 = null;
         var _loc10_:Object = null;
         var _loc11_:int = 0;
         var _loc12_:class_140 = null;
         var _loc13_:String = null;
         var _loc14_:Number = NaN;
         var _loc4_:Vector.<class_140> = new Vector.<class_140>();
         var _loc5_:Array;
         if(!(_loc5_ = this.var_1007))
         {
            return null;
         }
         var _loc6_:Array = class_14.var_872;
         for(_loc7_ in _loc5_)
         {
            _loc8_ = uint(_loc7_);
            if((_loc9_ = _loc6_[_loc8_]).var_444 == "Buff" && _loc9_.var_660.hasOwnProperty(param2.buffName))
            {
               _loc10_ = _loc9_.var_660[param2.buffName];
               _loc3_ = new Vector.<Number>();
               _loc11_ = 0;
               while(_loc11_ < _loc9_.var_660[param2.buffName].mOrder.length)
               {
                  _loc13_ = String(_loc9_.var_660[param2.buffName].mOrder[_loc11_]);
                  _loc14_ = this.method_1670(param1,param2.buffName,_loc13_,_loc8_);
                  _loc3_.push(_loc14_);
                  _loc11_++;
               }
               _loc12_ = new class_140(_loc8_,_loc3_);
               _loc4_.push(_loc12_);
            }
         }
         if(_loc4_.length > 0)
         {
            return _loc4_;
         }
         return null;
      }
      
      private function method_306(param1:class_17) : void
      {
         var _loc2_:class_17 = null;
         if(!param1)
         {
            return;
         }
         if(param1.var_2874 && Boolean(this.var_1007[param1.var_382]))
         {
            return;
         }
         if(param1.var_2404)
         {
            this.var_1927.push(param1.var_382);
         }
         this.var_1007[param1.var_382] = !!this.var_1007[param1.var_382] ? this.var_1007[param1.var_382] + 1 : 1;
         this.method_1863(param1);
         if(param1.var_593)
         {
            _loc2_ = class_14.var_274[param1.var_593];
            this.method_306(_loc2_);
         }
      }
      
      public function method_1479(param1:Vector.<String>, param2:String, param3:String) : Vector.<String>
      {
         var _loc4_:String = null;
         var _loc5_:Object = null;
         var _loc6_:Object = null;
         var _loc7_:Array = null;
         var _loc8_:int = 0;
         if(param3 == "ProcOnHit")
         {
            _loc5_ = this.var_567;
            if(param1 == null)
            {
               param1 = new Vector.<String>();
            }
            if(Boolean(_loc5_) && _loc5_.hasOwnProperty(param2))
            {
               if((_loc6_ = _loc5_[param2]).hasOwnProperty(param3))
               {
                  if(_loc4_ = String(_loc6_[param3]))
                  {
                     _loc7_ = _loc4_.split(",");
                     _loc8_ = 0;
                     while(_loc8_ < _loc7_.length)
                     {
                        if(param1.indexOf(_loc7_[_loc8_]) < 0)
                        {
                           param1.push(_loc7_[_loc8_]);
                        }
                        _loc8_++;
                     }
                  }
               }
            }
         }
         return param1;
      }
   }
}
