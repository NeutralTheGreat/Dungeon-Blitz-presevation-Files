package
{
   import flash.utils.Dictionary;
   
   public class SoundConfig
   {
      
      public static var var_1705:String;
      
      public static var var_199:String;
      
      public static var var_1818:String;
      
      public static var var_2154:String;
      
      public static var var_2158:String;
      
      public static var var_1728:String;
      
      public static var var_2478:String;
      
      public static var var_1948:String;
      
      public static var var_1947:String;
      
      public static var var_1987:String;
      
      public static var var_1704:String;
      
      public static var var_1784:String;
      
      public static var var_1849:String;
      
      public static var var_2774:String;
      
      public static var var_2557:String;
      
      public static var var_2593:String;
      
      public static var var_2479:String;
      
      public static var var_2819:String;
      
      public static var var_2643:String;
      
      public static var var_1687:String;
      
      public static var var_2166:String;
      
      public static var var_2340:String;
      
      public static var var_2016:String;
      
      public static var var_2350:String;
      
      public static var var_2165:String;
      
      public static var var_2271:String;
      
      public static var var_2317:String;
      
      public static var var_2407:String;
      
      public static var var_1716:String;
      
      public static var var_1949:String;
      
      public static var var_1844:String;
      
      public static var var_1734:String;
      
      public static var var_1750:String;
      
      public static var var_1782:String;
      
      public static var var_1662:String;
      
      public static var var_2595:String;
      
      public static var var_2804:String;
      
      public static var var_2492:String;
      
      public static var var_2572:String;
      
      public static var var_2571:String;
      
      public static var var_2464:String;
      
      public static var var_2834:String;
      
      public static var var_2757:String;
      
      public static var var_2780:String;
      
      public static var var_2497:String;
      
      public static var var_2556:String;
      
      public static var var_2563:String;
      
      public static var var_1973:String;
      
      private static var var_1442:Dictionary = new Dictionary();
       
      
      public function SoundConfig()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         var _loc2_:XML = null;
         var _loc3_:String = null;
         var _loc4_:String = null;
         var _loc5_:Soundscape = null;
         var _loc6_:Array = null;
         var _loc7_:XML = null;
         var _loc8_:String = null;
         var _loc9_:Array = null;
         var _loc10_:String = null;
         var _loc11_:class_31 = null;
         for each(_loc2_ in param1.*)
         {
            _loc3_ = String(_loc2_.name().toString());
            _loc4_ = _loc2_.toString();
            if(_loc3_ == "LevelComplete")
            {
               var_1705 = _loc4_;
            }
            else if(_loc3_ == "ChangeGear")
            {
               var_199 = _loc4_;
            }
            else if(_loc3_ == "PickUpGear")
            {
               var_1818 = _loc4_;
            }
            else if(_loc3_ == "PickUpGold")
            {
               var_2154 = _loc4_;
            }
            else if(_loc3_ == "PickUpHealth")
            {
               var_2158 = _loc4_;
            }
            else if(_loc3_ == "CompleteAchievement")
            {
               var_1728 = _loc4_;
            }
            else if(_loc3_ == "CompleteMission")
            {
               var_2478 = _loc4_;
            }
            else if(_loc3_ == "GetMission")
            {
               var_1948 = _loc4_;
            }
            else if(_loc3_ == "LevelUp")
            {
               var_1947 = _loc4_;
            }
            else if(_loc3_ == "Teleport")
            {
               var_1987 = _loc4_;
            }
            else if(_loc3_ == "Revive")
            {
               var_1704 = _loc4_;
            }
            else if(_loc3_ == "HealthLow")
            {
               var_1784 = _loc4_;
            }
            else if(_loc3_ == "HealthCritical")
            {
               var_1849 = _loc4_;
            }
            else if(_loc3_ == "MeleeMiss")
            {
               var_2774 = _loc4_;
            }
            else if(_loc3_ == "MeleeHit")
            {
               var_2557 = _loc4_;
            }
            else if(_loc3_ == "MeleeBackMiss")
            {
               var_2593 = _loc4_;
            }
            else if(_loc3_ == "MeleeBackHit")
            {
               var_2479 = _loc4_;
            }
            else if(_loc3_ == "MeleeThreeHit")
            {
               var_2819 = _loc4_;
            }
            else if(_loc3_ == "MeleeThreeMiss")
            {
               var_2643 = _loc4_;
            }
            else if(_loc3_ == "Plummet")
            {
               var_1687 = _loc4_;
            }
            else if(_loc3_ == "IntroMusic")
            {
               var_1662 = _loc4_;
            }
            else if(_loc3_ == "RunPaladin")
            {
               var_2166 = _loc4_;
            }
            else if(_loc3_ == "RunMage")
            {
               var_2340 = _loc4_;
            }
            else if(_loc3_ == "RunRogue")
            {
               var_2016 = _loc4_;
            }
            else if(_loc3_ == "RunWater")
            {
               var_2350 = _loc4_;
            }
            else if(_loc3_ == "RunMetal")
            {
               var_2165 = _loc4_;
            }
            else if(_loc3_ == "RunWood")
            {
               var_2271 = _loc4_;
            }
            else if(_loc3_ == "RunPuddle")
            {
               var_2317 = _loc4_;
            }
            else if(_loc3_ == "RunRopeBridge")
            {
               var_2407 = _loc4_;
            }
            else if(_loc3_ == "LandOnGeneral")
            {
               var_1716 = _loc4_;
            }
            else if(_loc3_ == "LandOnWater")
            {
               var_1949 = _loc4_;
            }
            else if(_loc3_ == "LandOnMetal")
            {
               var_1844 = _loc4_;
            }
            else if(_loc3_ == "LandOnWood")
            {
               var_1734 = _loc4_;
            }
            else if(_loc3_ == "LandOnPuddle")
            {
               var_1750 = _loc4_;
            }
            else if(_loc3_ == "LandOnRopeBridge")
            {
               var_1782 = _loc4_;
            }
            else if(_loc3_ == "StorePurchase")
            {
               var_2595 = _loc4_;
            }
            else if(_loc3_ == "StoreConsider")
            {
               var_2804 = _loc4_;
            }
            else if(_loc3_ == "ForgeOpen")
            {
               var_2492 = _loc4_;
            }
            else if(_loc3_ == "ForgeSelect")
            {
               var_2572 = _loc4_;
            }
            else if(_loc3_ == "ForgeCraft")
            {
               var_2571 = _loc4_;
            }
            else if(_loc3_ == "ForgeEmerge")
            {
               var_2464 = _loc4_;
            }
            else if(_loc3_ == "ForgeLevelUp")
            {
               var_2834 = _loc4_;
            }
            else if(_loc3_ == "TrainSkill")
            {
               var_2757 = _loc4_;
            }
            else if(_loc3_ == "Vengeance")
            {
               var_2780 = _loc4_;
            }
            else if(_loc3_ == "VengeanceEnd")
            {
               var_2497 = _loc4_;
            }
            else if(_loc3_ == "GearBreak")
            {
               var_2556 = _loc4_;
            }
            else if(_loc3_ == "GearRepair")
            {
               var_2563 = _loc4_;
            }
            else if(_loc3_ == "NewGroupmate")
            {
               var_1973 = _loc4_;
            }
            else if(_loc3_ == "Soundscape")
            {
               (_loc5_ = new Soundscape()).loop = _loc2_.attribute("loop");
               if("@loopVol" in _loc2_)
               {
                  _loc5_.loopVol = Number(_loc2_.attribute("loopVol"));
               }
               _loc5_.intro = _loc2_.attribute("intro");
               if("@introVol" in _loc2_)
               {
                  _loc5_.introVol = Number(_loc2_.attribute("introVol"));
               }
               _loc6_ = String(_loc2_.attribute("name")).split(":");
               _loc5_.name = _loc6_[0];
               if(_loc6_.length <= 1)
               {
                  _loc5_.var_1805 = DayNightManager.const_73;
               }
               else
               {
                  _loc5_.var_1805 = DayNightManager.const_268[_loc6_[1]];
                  if(!_loc5_.var_1805)
                  {
                     class_24.method_7("Unrecognized TimeOfDay in SoundConfig - " + _loc5_.name + ":" + _loc6_[1]);
                  }
               }
               for each(_loc7_ in _loc2_.*)
               {
                  if((_loc10_ = String(_loc7_.name().toString())) == "Sound")
                  {
                     (_loc11_ = new class_31()).cycle = _loc7_.attribute("cycle");
                     _loc11_.soundName = _loc7_.toString();
                     if("@vol" in _loc7_)
                     {
                        _loc11_.vol = Number(_loc7_.attribute("vol"));
                     }
                     _loc5_.var_1451.push(_loc11_);
                  }
                  else
                  {
                     class_24.method_7("Unrecognized Property in SoundConfig " + _loc5_.name + ": " + _loc10_);
                  }
               }
               _loc8_ = _loc5_.name.toLowerCase();
               if(!(_loc9_ = var_1442[_loc8_]))
               {
                  _loc9_ = new Array();
                  var_1442[_loc8_] = _loc9_;
               }
               _loc9_[_loc5_.var_1805] = _loc5_;
            }
            else
            {
               class_24.method_7("Unknown Sound Property: " + _loc3_);
            }
         }
      }
      
      public static function method_745(param1:String, param2:uint) : Soundscape
      {
         var _loc3_:String = param1.toLowerCase();
         var _loc4_:Array;
         return !!(_loc4_ = var_1442[_loc3_]) ? _loc4_[param2] : null;
      }
   }
}
