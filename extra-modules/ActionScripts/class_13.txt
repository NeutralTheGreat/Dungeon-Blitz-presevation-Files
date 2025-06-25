package
{
   import flash.utils.Dictionary;
   
   public class class_13
   {
      
      public static const const_1259:uint = 0;
      
      public static const const_578:uint = 1;
      
      public static const const_785:uint = 2;
      
      public static const const_619:uint = 3;
      
      public static const const_802:uint = 4;
      
      public static const const_735:uint = 5;
      
      public static const const_841:uint = 100;
      
      public static const const_584:uint = 200;
      
      public static const const_1070:uint = 300;
      
      public static const const_949:uint = 3;
      
      public static const const_544:uint = 1;
      
      public static const const_831:uint = 2;
      
      public static const const_426:uint = 3;
      
      public static const const_1403:uint = 4;
      
      public static const const_118:uint = 5;
      
      public static const const_1151:uint = 232;
      
      public static const const_944:uint = 142;
      
      public static const const_557:uint = 271;
      
      private static const const_1170:Array = [0,10,24,38,52,71,92,114,141,175,211,253,303,360,426,500,589,693,807,943,1103,1288,1497,1747,2029,2353,2734,3165,3670,4251,4923,5696,6587,7621,8808,10182,11760,13585,15685,18111,20898,24116,27819,32085,37002,42667,49187,56702,65347,75308,86780];
      
      private static const const_1250:Array = [0,43,84,123,163,204,244,284,329,375,421,473,526,579,645,706,774,850,927,1011,1103,1197,1306,1416,1535,1662,1805,1950,2111,2282,2462,2658,2872,3096,3337,3603,3880,4183,4503,4851,5224,5625,6053,6516,7007,7542,8113,8729,9381,10087,10847];
      
      private static const const_916:Array = [0,2,5,8,10,14,18,23,28,35,42,51,61,72,85,100,118,139,161,189,221,258,299,349,406,471,547,633,734,850,985,1139,1317,1524,1762,2036,2352,2717,3137,3622,4180,4823,5564,6417,7400,8533,9837,11340,13069,15062,17356];
      
      private static const const_1287:Array = [0,9,17,25,33,41,49,57,66,75,84,95,105,116,129,141,155,170,185,202,221,239,261,283,307,332,361,390,422,456,492,532,574,619,667,721,776,837,901,970,1045,1125,1211,1303,1401,1508,1623,1746,1876,2017,2169];
      
      public static var var_1022:uint = 0;
       
      
      internal var var_525:String;
      
      internal var missionID:uint;
      
      internal var var_1775:Boolean;
      
      internal var var_2676:uint;
      
      internal var var_908:uint;
      
      internal var var_1478:uint;
      
      internal var var_134:String;
      
      internal var var_431:String;
      
      internal var var_186:String;
      
      internal var var_231:uint;
      
      internal var var_2319:String;
      
      internal var var_2869:String;
      
      internal var var_160:String;
      
      internal var var_319:String;
      
      internal var var_1323:String;
      
      internal var var_2734:Vector.<Vector.<class_13>>;
      
      internal var var_2110:String;
      
      internal var var_1577:uint;
      
      internal var var_1572:uint;
      
      internal var var_2898:String;
      
      internal var var_2893:String;
      
      internal var var_2908:String;
      
      internal var displayName:String;
      
      internal var var_2116:String;
      
      internal var var_2550:String;
      
      internal var description:String;
      
      internal var var_2858:String;
      
      internal var var_2530:String;
      
      internal var var_1490:String;
      
      internal var var_2739:String;
      
      internal var var_2742:String;
      
      internal var var_2425:String;
      
      internal var var_2309:String;
      
      internal var var_2136:String;
      
      internal var var_2814:Boolean;
      
      public function class_13()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_238,class_14.var_42,class_14.var_1391);
      }
      
      public static function method_974(param1:XML) : class_13
      {
         var _loc5_:XML = null;
         var _loc6_:String = null;
         var _loc7_:String = null;
         var _loc8_:Array = null;
         var _loc9_:String = null;
         var _loc10_:int = 0;
         var _loc11_:int = 0;
         var _loc2_:String = null;
         var _loc3_:String = null;
         var _loc4_:class_13 = new class_13();
         for each(_loc5_ in param1.*)
         {
            if((_loc6_ = String(_loc5_.name().toString())) == "MissionID")
            {
               _loc4_.missionID = uint(_loc5_);
            }
            else if(_loc6_ == "MissionName")
            {
               _loc4_.var_525 = _loc5_.toString();
            }
            else if(_loc6_ == "DisplayName")
            {
               _loc4_.displayName = _loc5_.toString();
            }
            else if(_loc6_ == "TrackerText")
            {
               _loc4_.var_2116 = _loc5_.toString();
            }
            else if(_loc6_ == "TrackerReturn")
            {
               _loc4_.var_2550 = _loc5_.toString();
            }
            else if(_loc6_ == "Description")
            {
               _loc4_.description = _loc5_.toString();
            }
            else if(_loc6_ == "MageReward")
            {
               _loc4_.var_2908 = _loc5_.toString();
            }
            else if(_loc6_ == "RogueReward")
            {
               _loc4_.var_2893 = _loc5_.toString();
            }
            else if(_loc6_ == "PaladinReward")
            {
               _loc4_.var_2898 = _loc5_.toString();
            }
            else if(_loc6_ == "ISayOnAccept")
            {
               _loc4_.var_2425 = _loc5_.toString();
            }
            else if(_loc6_ == "ISayOnComplete")
            {
               _loc4_.var_2309 = _loc5_.toString();
            }
            else if(_loc6_ == "ISayOnReturn")
            {
               _loc4_.var_2136 = _loc5_.toString();
            }
            else if(_loc6_ == "PreReqText")
            {
               _loc4_.var_2858 = _loc5_.toString();
            }
            else if(_loc6_ == "OfferText")
            {
               _loc4_.var_2530 = _loc5_.toString();
            }
            else if(_loc6_ == "ActiveText")
            {
               _loc4_.var_1490 = _loc5_.toString();
            }
            else if(_loc6_ == "ReturnText")
            {
               _loc4_.var_2742 = _loc5_.toString();
            }
            else if(_loc6_ == "PraiseText")
            {
               _loc4_.var_2739 = _loc5_.toString();
            }
            else if(_loc6_ == "Achievement")
            {
               _loc4_.var_1775 = MathUtil.method_50(_loc5_.toString());
            }
            else if(_loc6_ == "AchievementPoints")
            {
               _loc4_.var_2676 = uint(_loc5_);
            }
            else if(_loc6_ == "MissionLevel")
            {
               _loc4_.var_1478 = uint(_loc5_.toString());
            }
            else if(_loc6_ == "CompleteCount")
            {
               _loc4_.var_908 = uint(_loc5_.toString());
            }
            else if(_loc6_ == "Dungeon")
            {
               _loc4_.var_134 = _loc5_.toString();
            }
            else if(_loc6_ == "ExpReward")
            {
               _loc2_ = _loc5_.toString();
            }
            else if(_loc6_ == "GoldReward")
            {
               _loc3_ = _loc5_.toString();
            }
            else if(_loc6_ == "ContactName")
            {
               _loc4_.var_160 = _loc5_.toString();
            }
            else if(_loc6_ == "ReturnName")
            {
               _loc4_.var_319 = _loc5_.toString();
            }
            else if(_loc6_ == "ProgressIcon")
            {
               _loc4_.var_2319 = _loc5_.toString();
            }
            else if(_loc6_ == "ProgressText")
            {
               _loc4_.var_2869 = _loc5_.toString();
            }
            else if(_loc6_ == "ActiveTarget")
            {
               _loc4_.var_1323 = _loc5_.toString();
            }
            else if(_loc6_ == "PreReqMissions")
            {
               _loc4_.var_2110 = _loc5_.toString();
            }
            else if(_loc6_ == "ZoneSet")
            {
               _loc8_ = (_loc7_ = _loc5_.toString()).split(",");
               _loc4_.var_431 = _loc8_[0];
               if(_loc8_.length > 1)
               {
                  _loc4_.var_186 = _loc8_[1];
               }
            }
            else if(_loc6_ == "Priority")
            {
               _loc10_ = (_loc9_ = _loc5_.toString()).indexOf("+");
               _loc11_ = _loc9_.indexOf("-");
               if(!_loc9_.indexOf("Side"))
               {
                  _loc4_.var_231 = const_841;
               }
               else if(!_loc9_.indexOf("Dungeon"))
               {
                  _loc4_.var_231 = const_584;
               }
               else if(!_loc9_.indexOf("Story"))
               {
                  _loc4_.var_231 = const_1070;
               }
               else
               {
                  class_24.method_7("Unrecognized Mission Priority for " + _loc4_.var_525 + ": " + _loc9_);
               }
               if(_loc10_ != -1 && _loc11_ != -1)
               {
                  class_24.method_7("Mission Priority can\'t have + and -, " + _loc4_.var_525 + ": " + _loc9_);
               }
               else if(_loc10_ != -1)
               {
                  _loc4_.var_231 += _loc9_.length - _loc10_;
               }
               else if(_loc11_ != -1)
               {
                  _loc4_.var_231 -= _loc9_.length - _loc11_;
               }
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc4_.var_525 + ": " + _loc6_);
            }
         }
         if(_loc4_.var_431)
         {
            _loc4_.var_2814 = _loc4_.var_431.indexOf("Hard") >= 0;
         }
         if(_loc2_ == "M")
         {
            _loc4_.var_1577 = const_1170[_loc4_.var_1478];
         }
         else if(_loc2_ == "L")
         {
            _loc4_.var_1577 = const_916[_loc4_.var_1478];
         }
         else
         {
            _loc4_.var_1577 = 0;
         }
         if(_loc3_ == "M")
         {
            _loc4_.var_1572 = const_1250[_loc4_.var_1478];
         }
         else if(_loc3_ == "L")
         {
            _loc4_.var_1572 = const_1287[_loc4_.var_1478];
         }
         else
         {
            _loc4_.var_1572 = 0;
         }
         return _loc4_;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary, param4:Dictionary) : void
      {
         var _loc5_:XML = null;
         var _loc6_:class_35 = null;
         var _loc7_:Array = null;
         var _loc8_:Dictionary = null;
         var _loc9_:class_13 = null;
         var _loc10_:class_13 = null;
         var _loc11_:String = null;
         var _loc12_:Vector.<Vector.<class_13>> = null;
         var _loc13_:Array = null;
         var _loc14_:String = null;
         var _loc15_:Array = null;
         var _loc16_:Vector.<class_13> = null;
         var _loc17_:String = null;
         var _loc18_:class_13 = null;
         var_1022 = 0;
         for each(_loc5_ in param1.*)
         {
            if((_loc10_ = method_974(_loc5_)).missionID)
            {
               if(param3[_loc10_.var_525])
               {
                  class_24.method_7("Multiple missions with name: " + _loc10_.var_525);
               }
               if(param2[_loc10_.missionID])
               {
                  class_24.method_7("Multiple missions with ID: " + _loc10_.missionID);
               }
               if(_loc10_.var_1775 && !_loc10_.var_2676)
               {
                  class_24.method_7("Achievement was not assigned achievement points: " + _loc10_.var_525);
               }
               if(_loc10_.missionID != var_1022 + 1)
               {
                  class_24.method_7("MissionIDs must be ascending by 1, starting with 1: " + _loc10_.missionID);
               }
               param2[_loc10_.missionID] = _loc10_;
               param3[_loc10_.var_525] = _loc10_;
               if(_loc10_.var_134)
               {
                  param4[_loc10_.var_134] = _loc10_;
               }
               var_1022 = _loc10_.missionID;
            }
         }
         _loc7_ = class_14.var_2123;
         _loc8_ = class_14.var_999;
         for each(_loc9_ in param2)
         {
            if(_loc11_ = String(_loc9_.var_2110))
            {
               _loc12_ = new Vector.<Vector.<class_13>>();
               _loc13_ = _loc11_.split("|");
               for each(_loc14_ in _loc13_)
               {
                  _loc15_ = _loc14_.split(",");
                  _loc16_ = new Vector.<class_13>();
                  for each(_loc17_ in _loc15_)
                  {
                     if(!(_loc18_ = param3[_loc17_]))
                     {
                        class_24.method_7("Unknown pre-req mission name: " + _loc17_);
                     }
                     _loc16_.push(_loc18_);
                  }
                  _loc16_.fixed = true;
                  _loc12_.push(_loc16_);
               }
               _loc12_.fixed = true;
               _loc9_.var_2734 = _loc12_;
               _loc9_.var_2110 = null;
            }
            if(_loc9_.var_319)
            {
               (_loc6_ = class_35.method_820(_loc9_.var_319,_loc7_,_loc8_)).var_1701.push(_loc9_);
            }
            if(_loc9_.var_160)
            {
               (_loc6_ = class_35.method_820(_loc9_.var_160,_loc7_,_loc8_)).var_1886.push(_loc9_);
            }
         }
      }
      
      public function method_224(param1:uint) : String
      {
         if(param1 == const_578)
         {
            return this.var_2858;
         }
         if(param1 == const_785)
         {
            return this.var_2530;
         }
         if(param1 == const_619)
         {
            return this.var_1490;
         }
         if(param1 == const_735)
         {
            return this.var_2739;
         }
         if(param1 == const_802)
         {
            return this.var_2742;
         }
         return null;
      }
   }
}
