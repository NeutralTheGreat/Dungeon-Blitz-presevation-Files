package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.filters.GlowFilter;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   
   public class class_83 extends class_32
   {
      
      public static const const_492:uint = 1;
      
      public static const const_602:uint = 2;
      
      public static const const_74:uint = 30;
      
      private static const const_943:uint = 35;
      
      public static const const_15:uint = 3;
      
      private static const const_39:uint = 14;
      
      private static const const_1261:String = "am_Path";
      
      private static const const_927:uint = const_1261.length;
      
      private static const const_732:String = "Disabled";
      
      private static const const_487:String = "Pending";
      
      private static const const_114:uint = 2;
      
      private static const const_454:uint = 1;
      
      private static const const_447:uint = 0;
      
      private static const const_1113:uint = 6978655;
      
      private static const const_859:uint = 12569273;
      
      private static const const_891:GlowFilter = new GlowFilter(5555953,1,5,5,2,3);
      
      public static const const_601:Vector.<Vector.<uint>> = method_632();
      
      private static const const_719:int = 0;
      
      private static const const_611:int = 1;
      
      private static const const_686:int = 2;
      
      private static const const_104:uint = 0;
      
      private static const const_301:uint = 1;
      
      private static const const_481:uint = 2;
       
      
      public var var_60:class_33;
      
      private var var_1458:class_33;
      
      private var var_2680:class_33;
      
      private var var_338:Vector.<class_33>;
      
      private var var_765:Vector.<class_33>;
      
      private var var_1533:Vector.<class_156>;
      
      private var var_165:Vector.<uint>;
      
      private var var_35:class_118;
      
      private var var_1394:class_33;
      
      private var var_594:class_22;
      
      private var var_642:int;
      
      private var var_565:int;
      
      private var var_1970:Vector.<class_33>;
      
      private var var_358:Vector.<Vector.<class_33>>;
      
      private var var_2304:Vector.<Vector.<class_33>>;
      
      private var var_606:uint = 0;
      
      private var var_1587:uint = 0;
      
      private var var_1437:class_33;
      
      private var var_1457:class_33;
      
      private var var_2140:class_33;
      
      private var var_488:Vector.<Object>;
      
      private var var_1000:int = -1;
      
      private var var_888:int = 0;
      
      private var var_253:Vector.<Vector.<uint>>;
      
      public function class_83(param1:Game)
      {
         super(param1,"a_SigilWindow2","am_Panel");
      }
      
      public static function method_751(param1:TextField, param2:String, param3:int) : void
      {
         var _loc4_:Array;
         var _loc5_:int = int((_loc4_ = param2.split(",")).length);
         var _loc6_:* = "<font color=\'#00CCFF\'>" + _loc4_[0] + "</font>";
         var _loc7_:int = 1;
         while(_loc7_ < _loc5_)
         {
            if(_loc7_ == param3)
            {
               _loc6_ += "<font color=\'#00CCFF\'> [" + _loc4_[_loc7_] + " ]</font>";
            }
            else
            {
               _loc6_ += "<font color=\'#999999\'>" + _loc4_[_loc7_] + "</font>";
            }
            _loc7_++;
         }
         MathUtil.method_2(param1,_loc6_,true);
      }
      
      public static function method_406(param1:String) : String
      {
         return param1.charAt(0).toUpperCase() + param1.substr(1).toLowerCase();
      }
      
      private static function method_632() : Vector.<Vector.<uint>>
      {
         var _loc2_:Vector.<uint> = null;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc1_:Vector.<Vector.<uint>> = new Vector.<Vector.<uint>>();
         _loc1_.push(Vector.<uint>([2,3]));
         _loc1_.push(Vector.<uint>([1,5]));
         _loc1_.push(Vector.<uint>([1,4]));
         _loc1_.push(Vector.<uint>([3,6]));
         _loc1_.push(Vector.<uint>([2,7]));
         _loc1_.push(Vector.<uint>([4,7]));
         _loc1_.push(Vector.<uint>([5,6,8,10]));
         _loc1_.push(Vector.<uint>([7,9]));
         _loc1_.push(Vector.<uint>([8,10,11]));
         _loc1_.push(Vector.<uint>([7,9]));
         _loc1_.push(Vector.<uint>([9,12,13]));
         _loc1_.push(Vector.<uint>([11,15]));
         _loc1_.push(Vector.<uint>([11,14]));
         _loc1_.push(Vector.<uint>([13,16]));
         _loc1_.push(Vector.<uint>([12,17]));
         _loc1_.push(Vector.<uint>([14,17]));
         _loc1_.push(Vector.<uint>([15,16,18,20]));
         _loc1_.push(Vector.<uint>([17,19]));
         _loc1_.push(Vector.<uint>([18,20,21]));
         _loc1_.push(Vector.<uint>([17,19]));
         _loc1_.push(Vector.<uint>([19,22,23]));
         _loc1_.push(Vector.<uint>([21,25]));
         _loc1_.push(Vector.<uint>([21,24]));
         _loc1_.push(Vector.<uint>([23,26]));
         _loc1_.push(Vector.<uint>([22,27]));
         _loc1_.push(Vector.<uint>([24,27]));
         _loc1_.push(Vector.<uint>([25,26,28,30]));
         _loc1_.push(Vector.<uint>([27,29]));
         _loc1_.push(Vector.<uint>([28,30]));
         _loc1_.push(Vector.<uint>([27,29]));
         _loc1_.fixed = true;
         for each(_loc2_ in _loc1_)
         {
            _loc3_ = _loc2_.length;
            _loc4_ = 0;
            while(_loc4_ < _loc3_)
            {
               --_loc2_[_loc4_];
               _loc4_++;
            }
            _loc2_.fixed = true;
         }
         return _loc1_;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:MovieClip = null;
         var _loc2_:uint = 0;
         var _loc5_:MovieClip = null;
         var _loc6_:class_156 = null;
         var _loc9_:String = null;
         var _loc10_:int = 0;
         var _loc11_:uint = 0;
         var _loc12_:uint = 0;
         var _loc13_:MovieClip = null;
         var _loc14_:Vector.<class_33> = null;
         var _loc15_:Vector.<class_33> = null;
         var _loc16_:uint = 0;
         var _loc17_:MovieClip = null;
         this.method_715();
         var _loc3_:MovieClip = var_2.am_NodeGroup;
         this.var_338 = new Vector.<class_33>(const_74,true);
         this.var_765 = new Vector.<class_33>(const_74,true);
         var _loc4_:int = 0;
         while(_loc4_ < const_74)
         {
            _loc2_ = uint(_loc4_ + 1);
            _loc1_ = _loc3_["am_Node" + _loc2_] as MovieClip;
            this.var_338[_loc4_] = method_3(_loc1_,_loc4_,this.method_1056,this.method_894,this.method_1046);
            this.var_765[_loc4_] = method_1(_loc1_.am_NodeAnimationGroup);
            this.var_765[_loc4_].Hide();
            _loc4_++;
         }
         this.var_1533 = new Vector.<class_156>();
         var _loc7_:MovieClip = var_2.am_PathGroup;
         _loc4_ = 0;
         while(_loc4_ < const_943)
         {
            _loc10_ = (_loc9_ = (_loc5_ = _loc7_.getChildAt(_loc4_) as MovieClip).name).lastIndexOf("_");
            _loc11_ = uint(_loc9_.slice(const_927,_loc10_));
            _loc12_ = uint(_loc9_.substr(_loc9_.lastIndexOf("_") + 1));
            _loc6_ = new class_156(_loc11_ - 1,_loc12_ - 1,method_1(_loc5_));
            this.var_1533.push(_loc6_);
            _loc4_++;
         }
         this.var_1970 = new Vector.<class_33>(const_39,true);
         this.var_358 = new Vector.<Vector.<class_33>>(const_39,true);
         this.var_2304 = new Vector.<Vector.<class_33>>(const_39,true);
         var _loc8_:MovieClip = var_2.am_SignetGroup;
         _loc4_ = 0;
         while(_loc4_ < const_39)
         {
            _loc13_ = _loc8_["am_Signets" + _loc4_] as MovieClip;
            _loc14_ = new Vector.<class_33>(const_15,true);
            _loc15_ = new Vector.<class_33>(const_15,true);
            _loc16_ = 0;
            while(_loc16_ < const_15)
            {
               (_loc17_ = _loc13_["am_Signet" + _loc16_] as MovieClip).am_Highlighter.visible = false;
               _loc14_[_loc16_] = method_3(_loc17_,_loc4_ * const_15 + _loc16_,this.method_1256,this.method_629,this.method_1021);
               _loc15_[_loc16_] = method_1(_loc17_.am_GlareAnim);
               _loc16_++;
            }
            this.var_1970[_loc4_] = method_1(_loc13_.am_LockAnimation);
            this.var_2304[_loc4_] = _loc15_;
            this.var_358[_loc4_] = _loc14_;
            _loc4_++;
         }
         this.var_1394 = method_17(var_2.am_Shelves.am_TalentMeter,"Progress",20);
         this.var_2140 = method_1(var_2.am_Portrait);
         this.var_1437 = method_10(var_2.am_ApplyButton,this.method_1112);
         this.var_1457 = method_10(var_2.am_UndoButton,this.method_1342);
         method_10(var_2.am_RespecPanel.am_RespecButton,this.method_1428);
         this.var_1458 = method_1(var_2.am_RespecPanel);
         this.var_2680 = method_10(var_2.am_RespecIcon,null,this.method_1975,this.method_1450);
         var_2.am_RespecCount.mouseEnabled = false;
         method_23(var_2.am_Exit);
         this.var_60 = method_1(var_2.am_TutorialInteraction);
         this.var_60.Hide();
         var_2.cacheAsBitmap = true;
      }
      
      public function method_715() : void
      {
         this.var_165 = new Vector.<uint>(const_74,true);
         this.method_653();
      }
      
      override public function OnDestroyScreen() : void
      {
         var _loc2_:class_156 = null;
         var _loc3_:Vector.<uint> = null;
         var _loc4_:uint = 0;
         this.var_338 = null;
         this.var_165 = null;
         this.var_1394 = null;
         this.var_1437 = null;
         this.var_1457 = null;
         this.var_765 = null;
         this.var_594 = null;
         this.var_1970 = null;
         this.var_2140 = null;
         this.var_1458 = null;
         this.var_2680 = null;
         this.var_60 = null;
         this.var_35.method_213();
         this.var_35 = null;
         var _loc1_:uint = 0;
         while(_loc1_ < const_39)
         {
            _loc4_ = 0;
            while(_loc4_ < const_15)
            {
               this.var_358[_loc1_][_loc4_] = null;
               _loc4_++;
            }
            this.var_358[_loc1_] = null;
            _loc1_++;
         }
         this.var_358 = null;
         for each(_loc2_ in this.var_1533)
         {
            _loc2_.Destroy();
         }
         this.var_1533 = null;
         for each(_loc3_ in this.var_253)
         {
            _loc3_ = null;
         }
         this.var_253 = null;
         this.var_488 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc7_:class_156 = null;
         var _loc8_:class_33 = null;
         var _loc9_:uint = 0;
         var _loc11_:uint = 0;
         var _loc12_:PowerType = null;
         var _loc13_:uint = 0;
         var _loc14_:class_148 = null;
         var _loc15_:MovieClip = null;
         var _loc16_:class_17 = null;
         var _loc17_:* = false;
         var _loc18_:* = false;
         var _loc19_:Boolean = false;
         var _loc20_:class_148 = null;
         var _loc21_:uint = 0;
         var _loc22_:uint = 0;
         var _loc23_:Boolean = false;
         var _loc24_:class_33 = null;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:String = _loc1_.mMasterClass;
         this.var_2140.PlayAnimation(_loc2_);
         var _loc3_:uint = uint(this.var_35.method_231());
         var _loc4_:uint = this.var_35.method_98();
         MathUtil.method_2(var_2.am_ClassName,method_406(_loc2_));
         MathUtil.method_2(var_2.am_TalentPoints,String(_loc3_));
         this.var_1394.mHealthPerc = _loc4_ / (class_118.const_1246 + class_118.const_195);
         this.var_165 = new Vector.<uint>(const_74,true);
         var _loc6_:uint = 0;
         for(; _loc6_ < const_74; _loc6_++)
         {
            if(this.method_173(_loc6_))
            {
               if(_loc12_ = this.method_456(_loc6_))
               {
                  method_12(this.var_338[_loc6_].mMovieClip.am_IconHolder,_loc12_.iconName);
               }
               if(_loc13_ = _loc6_ / 10 * 20)
               {
                  if(_loc4_ < _loc13_)
                  {
                     this.method_1502(_loc6_);
                     continue;
                  }
                  if(this.var_35.method_93(_loc6_ - 2).IsEmpty())
                  {
                     this.method_978(_loc6_);
                     continue;
                  }
               }
               this.method_978(_loc6_);
            }
            else
            {
               _loc14_ = this.var_35.method_93(_loc6_);
               _loc15_ = this.var_338[_loc6_].mMovieClip.am_Holder;
               if(_loc14_.IsEmpty())
               {
                  method_14(_loc15_);
                  continue;
               }
               _loc16_ = _loc14_.method_333();
               method_12(_loc15_,_loc16_.iconName);
            }
            this.var_165[_loc6_] = const_114;
            for each(_loc11_ in const_601[_loc6_])
            {
               if(this.var_165[_loc11_] != const_114)
               {
                  this.var_165[_loc11_] = const_454;
               }
            }
         }
         for each(_loc7_ in this.var_1533)
         {
            _loc17_ = this.var_165[_loc7_.var_2430] == const_114;
            _loc18_ = this.var_165[_loc7_.var_2139] == const_114;
            if(!_loc17_ || !_loc18_)
            {
               _loc7_.var_1097.Hide();
            }
            else
            {
               if(this.var_35.HasPendingNodeType(_loc7_.var_2430) || this.var_35.HasPendingNodeType(_loc7_.var_2139))
               {
                  _loc7_.var_1097.PlayAnimation(const_487);
               }
               else
               {
                  _loc7_.var_1097.PlayAnimation(class_129.const_197);
               }
               _loc7_.var_1097.Show();
            }
         }
         _loc9_ = 0;
         _loc6_ = 0;
         while(_loc6_ < const_74)
         {
            _loc8_ = this.var_338[_loc6_];
            _loc19_ = this.method_173(_loc6_);
            if(this.var_165[_loc6_] == const_114)
            {
               if(!_loc19_)
               {
                  _loc8_.mMovieClip.am_Count.visible = false;
                  _loc8_.mMovieClip.am_Counter.visible = true;
                  _loc21_ = (_loc20_ = this.var_35.method_93(_loc6_)).GetPointsSpent();
                  _loc22_ = this.var_35.method_430(_loc6_);
                  if(_loc23_ = Boolean(_loc20_.method_520()))
                  {
                     MathUtil.method_2(_loc8_.mMovieClip.am_Counter.am_Count2,"<font color=\"#00CC33\">" + _loc21_ + "</font>" + "/" + _loc22_,true);
                  }
                  else
                  {
                     MathUtil.method_2(_loc8_.mMovieClip.am_Counter.am_Count2,_loc21_ + "/" + _loc22_,true);
                  }
               }
               if(_loc6_ == 0)
               {
                  _loc8_.PlayAnimation(class_129.const_197);
               }
               else if(_loc19_)
               {
                  _loc9_++;
                  if(this.method_931(_loc6_))
                  {
                     _loc8_.PlayAnimation(const_487);
                     if(_loc9_ - 1 == this.var_1587)
                     {
                        (_loc24_ = this.var_765[_loc6_]).PlayAnimation("Unlock",class_33.const_14);
                        _loc24_.Show();
                        ++this.var_1587;
                     }
                  }
                  else
                  {
                     _loc8_.PlayAnimation(class_129.const_197);
                  }
               }
               else if(this.var_35.HasPendingNodeType(_loc6_))
               {
                  _loc8_.PlayAnimation(const_487);
               }
               else
               {
                  _loc8_.PlayAnimation(class_129.const_197);
               }
            }
            else if(this.var_165[_loc6_] == const_454)
            {
               if(!_loc19_)
               {
                  _loc8_.mMovieClip.am_Count.visible = true;
                  _loc8_.mMovieClip.am_Counter.visible = false;
                  MathUtil.method_8(_loc8_.mMovieClip.am_Count,String(this.var_35.method_430(_loc6_)),ScreenArmory.const_11,ScreenArmory.const_47);
                  _loc8_.PlayAnimation("Inactive");
               }
               else
               {
                  _loc8_.PlayAnimation(const_732);
               }
            }
            else
            {
               if(!_loc19_)
               {
                  _loc8_.mMovieClip.am_Count.visible = true;
                  _loc8_.mMovieClip.am_Counter.visible = false;
                  MathUtil.method_8(_loc8_.mMovieClip.am_Count,String(this.var_35.method_430(_loc6_)),const_1113,const_859);
               }
               _loc8_.PlayAnimation(const_732);
            }
            _loc6_++;
         }
         this.method_1359(_loc1_,this.var_35.method_98());
         if(this.var_488.length)
         {
            this.var_1437.Show();
            this.var_1457.Show();
         }
         else
         {
            this.var_1437.Hide();
            this.var_1457.Hide();
         }
         var _loc10_:uint = uint(var_1.mRespecStoneCount);
         if(_loc1_.var_85.method_599() || !_loc10_)
         {
            this.var_1458.Hide();
            MathUtil.method_2(var_2.am_RespecCount,"x" + _loc10_);
         }
         else
         {
            this.var_1458.Show();
            MathUtil.method_2(this.var_1458.mMovieClip.am_RespecCount,"x" + _loc10_);
         }
         if(Boolean(this.var_888) && this.var_1000 >= 0)
         {
            if(this.var_888 == const_611)
            {
               this.method_894(null,this.var_1000);
            }
            else if(this.var_888 == const_686)
            {
               this.method_629(null,this.var_1000);
            }
         }
      }
      
      private function method_1359(param1:Entity, param2:uint) : void
      {
         var _loc6_:uint = 0;
         var _loc7_:class_33 = null;
         var _loc8_:class_33 = null;
         var _loc9_:MovieClip = null;
         var _loc10_:uint = 0;
         var _loc11_:class_22 = null;
         var _loc12_:class_17 = null;
         var _loc3_:uint = param2 / class_118.const_195;
         var _loc4_:Vector.<class_22> = class_14.var_368[param1.mMasterClass];
         var _loc5_:uint = 0;
         while(_loc5_ < const_39)
         {
            if(_loc5_ > this.var_606 && _loc5_ <= _loc3_)
            {
               (_loc7_ = this.var_1970[_loc5_]).PlayAnimation("Unlock",class_33.const_14);
               _loc7_.Show();
            }
            _loc6_ = 0;
            while(_loc6_ < const_15)
            {
               _loc9_ = (_loc8_ = this.var_358[_loc5_][_loc6_]).mMovieClip.am_Holder;
               if(this.method_468(_loc5_,_loc6_) != const_104)
               {
                  method_14(_loc9_);
                  _loc8_.mMovieClip.am_Selector.visible = false;
               }
               else
               {
                  _loc8_.PlayAnimation(_loc5_ <= _loc3_ ? "Ready" : "Inactive");
                  _loc8_.mMovieClip.am_Selector.visible = this.var_594 && _loc5_ == this.var_565 && _loc6_ == this.var_642;
                  _loc10_ = uint(_loc5_ * const_15 + _loc6_ + 1);
                  _loc11_ = _loc4_[_loc10_];
                  _loc12_ = class_14.var_274[_loc11_.var_548 + 1];
                  method_12(_loc8_.mMovieClip.am_Holder,_loc12_.iconName);
               }
               _loc6_++;
            }
            _loc5_++;
         }
         if(_loc3_ < const_39)
         {
            this.var_606 = _loc3_;
         }
      }
      
      private function method_451() : void
      {
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc8_:class_148 = null;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:uint = this.var_35.method_98();
         var _loc3_:uint = 0;
         this.var_165 = new Vector.<uint>(const_74,true);
         var _loc4_:uint = 0;
         for(; _loc4_ < const_74; _loc4_++)
         {
            if(this.method_173(_loc4_))
            {
               if((Boolean(_loc7_ = 2 * _loc4_)) && (_loc2_ < _loc7_ || this.var_35.method_93(_loc4_ - 2).IsEmpty()))
               {
                  continue;
               }
               _loc3_++;
            }
            else if((_loc8_ = this.var_35.method_93(_loc4_)).IsEmpty())
            {
               continue;
            }
            this.var_165[_loc4_] = const_114;
            for each(_loc6_ in const_601[_loc4_])
            {
               if(this.var_165[_loc6_] != const_114)
               {
                  this.var_165[_loc6_] = const_454;
               }
            }
         }
         this.var_1587 = _loc3_;
         var _loc5_:uint;
         if((_loc5_ = _loc2_ / 5) < const_39)
         {
            this.var_606 = _loc5_;
         }
      }
      
      override public function Hide() : void
      {
         var _loc2_:uint = 0;
         var _loc1_:uint = 0;
         while(_loc1_ < const_39)
         {
            _loc2_ = 0;
            while(_loc2_ < const_15)
            {
               if(this.var_253[_loc1_][_loc2_] == const_301)
               {
                  this.var_253[_loc1_][_loc2_] = const_104;
               }
               _loc2_++;
            }
            _loc1_++;
         }
         super.Hide();
      }
      
      public function OnInitDisplay(param1:String) : void
      {
         var _loc5_:class_148 = null;
         var _loc6_:class_148 = null;
         var _loc7_:Vector.<class_33> = null;
         var _loc2_:Entity = var_1.clientEnt;
         var _loc3_:class_118 = !!_loc2_ ? _loc2_.var_85 : null;
         if(!_loc3_)
         {
            return;
         }
         this.var_35 = new class_118(var_1);
         var _loc4_:uint = 0;
         while(_loc4_ < class_118.const_43)
         {
            _loc5_ = _loc3_.var_58[_loc4_];
            (_loc6_ = this.var_35.var_58[_loc4_]).mNodeType = _loc5_.mNodeType;
            _loc6_.mPointsSpent = _loc5_.mPointsSpent;
            _loc6_.var_1307 = _loc5_.var_1307;
            _loc4_++;
         }
         this.var_488 = new Vector.<Object>();
         this.method_644();
         this.var_606 = this.var_35.method_98() / 5;
         this.var_1394.BeginHealthMode("Progress",20);
         if(!var_1.screenInteractiveTutorial.CheckCompletedTutorials(class_89.const_261) && Boolean(this.var_35.method_231()))
         {
            this.var_60.Show();
            (_loc7_ = new Vector.<class_33>()).push(this.var_358[0][0]);
            _loc7_.push(this.var_358[0][1]);
            _loc7_.push(this.var_358[0][2]);
            _loc7_.push(this.var_338[1]);
            _loc7_.push(this.var_338[2]);
            _loc7_.push(this.var_1437);
            _loc7_.push(this.var_1457);
            var_1.screenInteractiveTutorial.SetTutorial(class_89.const_261,this,this.var_60,_loc7_);
         }
      }
      
      private function method_1502(param1:uint) : void
      {
         this.var_338[param1].mMovieClip.am_Lock.visible = true;
      }
      
      private function method_978(param1:uint) : void
      {
         this.var_338[param1].mMovieClip.am_Lock.visible = false;
      }
      
      private function method_456(param1:uint) : PowerType
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return null;
         }
         var _loc3_:String = _loc2_.mMasterClass;
         if(param1 == 0)
         {
            return _loc2_.method_38(_loc3_,4);
         }
         if(param1 == 10)
         {
            return _loc2_.method_38(_loc3_,5);
         }
         if(param1 == 20)
         {
            return _loc2_.method_38(_loc3_,6);
         }
         return null;
      }
      
      private function method_1112(param1:MouseEvent) : void
      {
         var _loc4_:class_33 = null;
         var _loc5_:class_148 = null;
         var _loc6_:uint = 0;
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_ || !var_1.CanSendPacket())
         {
            return;
         }
         var _loc3_:uint = 1;
         while(_loc3_ < const_74)
         {
            _loc4_ = this.var_765[_loc3_];
            if(this.method_173(_loc3_))
            {
               if(this.method_931(_loc3_))
               {
                  _loc4_.PlayAnimation("Unlock",class_33.const_14);
               }
            }
            else if((_loc5_ = this.var_35.method_93(_loc3_)).HasPendingNodeType() || Boolean(_loc5_.method_520()))
            {
               _loc4_.PlayAnimation("Activate",class_33.const_14);
            }
            _loc4_.Show();
            _loc3_++;
         }
         this.var_35.method_338();
         if(_loc2_.var_85)
         {
            _loc2_.var_85.method_213();
         }
         _loc3_ = 0;
         while(_loc3_ < const_39)
         {
            _loc6_ = 0;
            while(_loc6_ < const_15)
            {
               if(this.var_253[_loc3_][_loc6_] == const_301)
               {
                  this.var_253[_loc3_][_loc6_] = const_481;
               }
               _loc6_++;
            }
            _loc3_++;
         }
         _loc2_.var_85 = this.var_35.method_272();
         _loc2_.var_85.method_840(this.var_488);
         var_1.mAbilityBook.DefaultMasterRanks(this.var_35,_loc2_.mMasterClass);
         this.var_488 = new Vector.<Object>();
         _loc2_.ResetEntType(_loc2_.entType);
         Refresh();
      }
      
      private function method_1265() : void
      {
         var _loc3_:uint = 0;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_ || !var_1.CanSendPacket())
         {
            return;
         }
         if(_loc1_.var_85)
         {
            _loc1_.var_85.method_213();
         }
         this.var_35.method_338();
         this.var_488 = new Vector.<Object>();
         var _loc2_:int = 0;
         while(_loc2_ < const_39)
         {
            _loc3_ = 0;
            while(_loc3_ < const_15)
            {
               if(this.var_253[_loc2_][_loc3_] == const_301)
               {
                  this.var_253[_loc2_][_loc3_] = const_481;
               }
               _loc3_++;
            }
            _loc2_++;
         }
         _loc1_.var_85 = this.var_35.method_272();
         _loc1_.var_85.method_840(this.var_488);
         this.method_451();
      }
      
      private function method_1056(param1:MouseEvent, param2:uint) : void
      {
         var _loc4_:class_33 = null;
         var _loc5_:class_17 = null;
         var _loc6_:class_10 = null;
         var _loc7_:uint = 0;
         var _loc8_:uint = 0;
         var _loc9_:Object = null;
         var _loc10_:class_33 = null;
         var _loc11_:MovieClip = null;
         var _loc12_:Rectangle = null;
         var _loc13_:int = 0;
         if(this.method_173(param2))
         {
            if(param1.ctrlKey)
            {
               if(_loc6_ = var_1.screenSpellbook.GetAbilityTypeFromPowerType(this.method_456(param2)))
               {
                  var_1.screenSpellbook.LinkAbilityInChat(_loc6_,_loc6_.rank);
               }
            }
            return;
         }
         if(this.var_165[param2] == const_447)
         {
            return;
         }
         var _loc3_:class_148 = this.var_35.method_93(param2);
         if(!_loc3_)
         {
            return;
         }
         if(this.var_35.method_231() <= 0)
         {
            return;
         }
         if(_loc3_.IsEmpty())
         {
            if(this.var_594)
            {
               _loc8_ = (_loc7_ = this.var_35.method_98()) / class_118.const_195;
               if(this.var_565 <= _loc8_)
               {
                  (_loc9_ = new Object()).nodeIndex = param2;
                  _loc9_.actionType = const_492;
                  _loc9_.signetGroup = this.var_565;
                  _loc9_.signetIndex = this.var_642;
                  this.var_488.push(_loc9_);
                  _loc3_.Socket(this.var_594,this.var_565 * const_15 + this.var_642);
                  (_loc4_ = this.var_765[param2]).PlayAnimation("Activate",class_33.const_14);
                  _loc4_.Show();
                  _loc5_ = class_14.var_274[this.var_594.var_548 + 1];
                  _loc12_ = (_loc11_ = (_loc10_ = this.var_358[this.var_565][this.var_642]).mMovieClip).getBounds(mWindow.mMovieClip);
                  method_68(_loc5_.iconName,_loc12_.x,_loc12_.y,this.var_338[param2].mMovieClip,300,null,null,true);
                  this.method_570(this.var_565,this.var_642);
                  this.var_565 = -1;
                  this.var_642 = -1;
                  this.var_594 = null;
               }
            }
         }
         else
         {
            if(param1.ctrlKey && !var_1.screenInteractiveTutorial.mCurrentTutorialIdx)
            {
               if(_loc5_ = _loc3_.method_333())
               {
                  this.method_633(_loc5_);
               }
               return;
            }
            if(this.var_165[param2] == const_114)
            {
               if(this.var_35.method_676(param2))
               {
                  if(this.var_35.method_231())
                  {
                     (_loc9_ = new Object()).nodeIndex = param2;
                     _loc9_.actionType = const_602;
                     this.var_488.push(_loc9_);
                     _loc3_.method_460();
                     (_loc4_ = this.var_765[param2]).PlayAnimation("Allocate",class_33.const_14);
                     _loc4_.Show();
                     _loc5_ = _loc3_.method_333();
                     _loc13_ = int(_loc3_.GetPointsSpent());
                     this.method_507(_loc5_,_loc13_);
                  }
               }
            }
         }
         Refresh();
      }
      
      private function method_894(param1:MouseEvent, param2:uint) : void
      {
         var _loc4_:PowerType = null;
         var _loc5_:int = 0;
         var _loc6_:String = null;
         var _loc7_:class_148 = null;
         var _loc8_:class_17 = null;
         var _loc9_:int = 0;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         this.var_338[param2].mMovieClip.filters = [const_891];
         this.var_888 = const_611;
         this.var_1000 = param2;
         if(this.method_173(param2))
         {
            _loc4_ = this.method_456(param2);
            if(this.var_165[param2] == const_114)
            {
               var_1.screenHudTooltip.ShowPowerTooltip(_loc3_,_loc4_,681,633.25);
            }
            else if((_loc5_ = param2 * 2 - this.var_35.method_98()) <= 0)
            {
               var_1.screenHudTooltip.ShowTalentAbilityTooltip(_loc3_,_loc4_,"Requires a connecting slot to be filled.",681,614);
            }
            else
            {
               _loc6_ = _loc5_ == 1 ? " more talent point." : " more talent points.";
               var_1.screenHudTooltip.ShowTalentAbilityTooltip(_loc3_,_loc4_,"Requires " + _loc5_ + _loc6_,681,614);
            }
         }
         else
         {
            if((_loc7_ = this.var_35.method_93(param2)).IsEmpty())
            {
               this.method_1673(this.var_165[param2] == const_447);
               return;
            }
            _loc8_ = _loc7_.method_333();
            _loc9_ = int(_loc7_.GetPointsSpent());
            this.method_507(_loc8_,_loc9_);
         }
      }
      
      private function method_507(param1:class_17, param2:int = 1) : void
      {
         var _loc6_:* = false;
         var _loc7_:* = false;
         if(!param1)
         {
            return;
         }
         var _loc4_:uint = 630;
         var _loc5_:Array;
         if(_loc5_ = param1.description)
         {
            _loc6_ = _loc5_.length > 2;
            if(_loc7_ = _loc5_[0].length > 52)
            {
               _loc4_ = _loc6_ ? 630 : 650;
            }
            else
            {
               _loc4_ = _loc6_ ? 650 : 670;
            }
         }
         var_1.screenHudTooltip.ShowTalentstoneTooltip(param1,param2,681,_loc4_);
      }
      
      private function method_1673(param1:Boolean) : void
      {
         if(param1)
         {
            var_1.screenHudTooltip.ShowBasicDescriptionTooltip("Locked Socket","Socket","M","Requires a connecting socket to be filled.",681.95,659);
         }
         else if(!this.var_35.method_231())
         {
            var_1.screenHudTooltip.ShowBasicDescriptionTooltip("Empty Socket","Socket","M","Earn more Talents Points to slot new Talentstones.",681.95,659);
         }
         else if(this.var_594)
         {
            var_1.screenHudTooltip.ShowBasicDescriptionTooltip("Empty Socket","Socket","M","Click to slot selected Talentstone.",681.95,659);
         }
         else
         {
            var_1.screenHudTooltip.ShowBasicDescriptionTooltip("Empty Socket","Socket","M","Select a Talentstone to put here.",681.95,659);
         }
      }
      
      private function method_1046(param1:MouseEvent, param2:uint) : void
      {
         this.var_1000 = -1;
         this.var_888 = const_719;
         this.var_338[param2].mMovieClip.filters = [];
         var_1.screenHudTooltip.HideTooltip();
      }
      
      private function method_1256(param1:MouseEvent, param2:uint) : void
      {
         var _loc9_:class_22 = null;
         var _loc10_:class_17 = null;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:uint = param2 % const_15;
         var _loc5_:uint = uint(param2 / const_15);
         var _loc6_:uint;
         var _loc7_:uint = (_loc6_ = this.var_35.method_98()) / class_118.const_195;
         if(_loc5_ > _loc7_)
         {
            this.var_358[_loc5_][_loc4_].PlayAnimation("Inactive");
            if(!param1.ctrlKey)
            {
               return;
            }
         }
         var _loc8_:Vector.<class_22> = class_14.var_368[_loc3_.mMasterClass];
         if(param1.ctrlKey && !var_1.screenInteractiveTutorial.mCurrentTutorialIdx)
         {
            _loc9_ = _loc8_[param2 + 1];
            _loc10_ = class_14.var_274[_loc9_.var_548 + 1];
            this.method_633(_loc10_);
            return;
         }
         this.var_594 = _loc8_[param2 + 1];
         this.var_565 = _loc5_;
         this.var_642 = _loc4_;
         Refresh();
      }
      
      public function method_633(param1:class_17) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:* = "{" + class_127.const_8[6] + ":";
         _loc3_ += param1.var_382.toString();
         _loc3_ += "}";
         var_1.screenChat.AddItemInfoToChatEntry("[" + param1.displayName + "]",_loc3_);
      }
      
      private function method_629(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         this.var_888 = const_686;
         this.var_1000 = param2;
         var _loc4_:uint = Math.floor(param2 / const_15);
         var _loc5_:uint = param2 % const_15;
         var _loc6_:class_33;
         (_loc6_ = this.var_358[_loc4_][_loc5_]).mMovieClip.am_Highlighter.visible = true;
         var _loc7_:uint;
         var _loc8_:uint = (_loc7_ = this.var_35.method_98()) / class_118.const_195;
         if(_loc4_ <= _loc8_ && this.method_468(_loc4_,_loc5_) == const_104)
         {
            this.var_2304[_loc4_][_loc5_].PlayAnimation("Glare");
         }
         else
         {
            _loc6_.PlayAnimation("Inactive");
         }
         var _loc9_:Vector.<class_22>;
         var _loc10_:class_22 = (_loc9_ = class_14.var_368[_loc3_.mMasterClass])[param2 + 1];
         var _loc11_:class_17 = class_14.var_274[_loc10_.var_548 + 1];
         this.method_507(_loc11_);
      }
      
      private function method_1021(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:uint = Math.floor(param2 / const_15);
         var _loc4_:uint = param2 % const_15;
         this.var_1000 = -1;
         this.var_888 = const_719;
         var _loc5_:class_33;
         (_loc5_ = this.var_358[_loc3_][_loc4_]).mMovieClip.am_Highlighter.visible = false;
         var _loc6_:uint;
         var _loc7_:uint = (_loc6_ = this.var_35.method_98()) / class_118.const_195;
         if(_loc3_ > _loc7_)
         {
            _loc5_.PlayAnimation("Inactive");
         }
         var_1.screenHudTooltip.HideTooltip();
      }
      
      private function method_1975(param1:MouseEvent) : void
      {
         var_1.screenHudTooltip.ShowBasicDescriptionTooltip("Respec Stone","Consumable","M","Create the Respec Stone in your forge to reset all your talent stones.",703,630);
      }
      
      private function method_1450(param1:MouseEvent) : void
      {
         var_1.screenHudTooltip.HideTooltip();
      }
      
      private function method_1342(param1:MouseEvent) : void
      {
         var _loc2_:Object = this.var_488.pop();
         if(!_loc2_)
         {
            return;
         }
         var _loc3_:class_148 = this.var_35.method_93(_loc2_.nodeIndex);
         if(!_loc3_)
         {
            return;
         }
         if(_loc2_.actionType == const_492)
         {
            _loc3_.method_478();
            this.method_1674(_loc2_.signetGroup,_loc2_.signetIndex);
         }
         else if(_loc2_.actionType == const_602)
         {
            _loc3_.method_1317();
         }
         this.var_565 = -1;
         this.var_642 = -1;
         this.var_594 = null;
         Refresh();
      }
      
      private function method_173(param1:uint) : Boolean
      {
         return !(param1 % 10);
      }
      
      private function method_931(param1:uint) : Boolean
      {
         var _loc2_:uint = param1 / 10 * 20;
         var _loc3_:uint = this.var_35.method_98();
         return this.var_35.HasPendingNodeType(param1 - 2) && _loc2_ <= _loc3_;
      }
      
      private function method_1428(param1:MouseEvent) : void
      {
         var_1.screenRespecConfirm.Display();
      }
      
      public function RespecTalentTree() : void
      {
         var _loc4_:uint = 0;
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_ || !var_1.CanSendPacket())
         {
            return;
         }
         if(!_loc1_.var_85.method_1304())
         {
            return;
         }
         var _loc2_:uint = 0;
         while(_loc2_ < const_39)
         {
            _loc4_ = 0;
            while(_loc4_ < const_15)
            {
               this.var_253[_loc2_][_loc4_] = const_104;
               _loc4_++;
            }
            _loc2_++;
         }
         --var_1.mRespecStoneCount;
         _loc1_.var_85.method_213();
         this.var_35.method_213();
         this.var_35 = new class_118(var_1);
         _loc1_.var_85 = this.var_35.method_272();
         this.var_488 = new Vector.<Object>();
         this.var_1587 = 0;
         this.var_606 = 0;
         this.var_594 = null;
         this.var_642 = -1;
         this.var_565 = -1;
         this.var_1394.BeginHealthMode("Progress",20);
         Refresh();
         _loc1_.ResetEntType(var_1.clientEnt.entType);
         var _loc3_:Packet = new Packet(LinkUpdater.const_1089);
         var_1.serverConn.SendPacket(_loc3_);
      }
      
      private function method_653() : void
      {
         this.var_253 = new Vector.<Vector.<uint>>(const_39,true);
         var _loc1_:uint = 0;
         while(_loc1_ < const_39)
         {
            this.var_253[_loc1_] = Vector.<uint>([const_104,const_104,const_104]);
            _loc1_++;
         }
      }
      
      private function method_468(param1:uint, param2:uint) : uint
      {
         return this.var_253[param1][param2];
      }
      
      private function method_570(param1:uint, param2:uint) : void
      {
         this.var_253[param1][param2] = const_301;
      }
      
      private function method_1674(param1:uint, param2:uint) : void
      {
         this.var_253[param1][param2] = const_104;
      }
      
      private function method_644() : void
      {
         var _loc5_:class_148 = null;
         this.method_653();
         var _loc1_:uint = 0;
         var _loc2_:int = 0;
         var _loc3_:int = 0;
         var _loc4_:Vector.<class_148> = this.var_35.method_1384();
         for each(_loc5_ in _loc4_)
         {
            if(_loc5_.mNodeType)
            {
               _loc1_ = _loc5_.mNodeType.mNodeID - 1;
               _loc3_ = _loc1_ % const_15;
               _loc2_ = Math.floor(_loc1_ / const_15);
               this.var_253[_loc2_][_loc3_] = const_481;
            }
         }
      }
      
      public function method_2026() : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         if(!this.var_165)
         {
            this.method_715();
         }
      }
      
      private function method_1034(param1:Boolean, param2:Boolean = true) : class_148
      {
         var _loc3_:class_148 = null;
         var _loc6_:uint = 0;
         var _loc7_:Boolean = false;
         var _loc4_:Vector.<class_148> = new Vector.<class_148>();
         var _loc5_:class_148 = null;
         _loc6_ = 0;
         while(_loc6_ < const_74)
         {
            if(!(_loc7_ = this.method_173(_loc6_)) && this.var_165[_loc6_] != const_447)
            {
               _loc3_ = this.var_35.method_93(_loc6_);
               if(this.var_35.method_676(_loc6_))
               {
                  if(!_loc5_)
                  {
                     _loc5_ = _loc3_;
                  }
                  if(_loc3_.IsEmpty() == param1)
                  {
                     _loc4_.push(_loc3_);
                  }
               }
            }
            _loc6_++;
         }
         if(_loc4_.length > 0)
         {
            return _loc4_[Math.floor(Math.random() * _loc4_.length)];
         }
         if(!param2)
         {
            _loc5_ = null;
         }
         return _loc5_;
      }
      
      private function method_1190(param1:class_148, param2:Boolean) : Boolean
      {
         var _loc4_:Vector.<uint> = null;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc8_:uint = 0;
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc11_:Vector.<class_22> = null;
         var _loc12_:class_22 = null;
         var _loc3_:Entity = var_1.clientEnt;
         var _loc7_:Boolean = false;
         if(!_loc3_)
         {
            return false;
         }
         _loc4_ = new Vector.<uint>();
         _loc5_ = param2 ? this.var_606 - 1 : 0;
         while(_loc5_ <= this.var_606)
         {
            _loc6_ = 0;
            while(_loc6_ < const_15)
            {
               if(this.method_468(_loc5_,_loc6_) == const_104)
               {
                  _loc4_.push(_loc5_ * const_15 + _loc6_);
               }
               _loc6_++;
            }
            _loc5_++;
         }
         if(_loc4_.length > 0)
         {
            _loc8_ = _loc4_[Math.floor(Math.random() * _loc4_.length)];
            _loc9_ = Math.floor(_loc8_ / const_15);
            _loc10_ = _loc8_ % const_15;
            _loc12_ = (_loc11_ = class_14.var_368[_loc3_.mMasterClass])[_loc8_ + 1];
            param1.Socket(_loc12_,_loc8_);
            this.method_570(_loc9_,_loc10_);
            _loc7_ = true;
         }
         return _loc7_;
      }
   }
}
