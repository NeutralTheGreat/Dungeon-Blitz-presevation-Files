package
{
   public class class_6
   {
      
      public static const const_1118:uint = uint(EntType.COLOR_HAIR);
      
      public static const const_1110:uint = uint(EntType.COLOR_SKIN);
      
      public static const const_1181:uint = uint(EntType.COLOR_SHIRT);
      
      public static const const_1279:uint = uint(EntType.COLOR_PANTS);
      
      public static const const_1000:Number = 1.5;
      
      public static var var_1148:Vector.<GfxType> = new Vector.<GfxType>();
      
      public static var var_1677:Boolean = false;
       
      
      internal var gfxType:GfxType;
      
      internal var var_2341:uint;
      
      internal var var_2623:uint;
      
      internal var displayName:String;
      
      internal var className:String;
      
      internal var var_2462:String;
      
      internal var var_2443:String;
      
      internal var var_2594:String;
      
      internal var var_2529:String;
      
      internal var var_2573:String;
      
      internal var var_2507:int;
      
      internal var var_2813:int;
      
      internal var var_2581:int;
      
      internal var var_2622:int;
      
      internal var var_2574:int;
      
      internal var var_2469:int;
      
      internal var var_2763:String;
      
      internal var var_2542:uint;
      
      internal var var_2229:Boolean;
      
      internal var var_2490:int;
      
      internal var var_2767:int;
      
      internal var var_1646:String;
      
      public function class_6()
      {
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.var_661);
      }
      
      public static function method_887(param1:XML) : class_6
      {
         var _loc3_:XML = null;
         var _loc4_:GfxType = null;
         var _loc5_:String = null;
         var _loc2_:class_6 = new class_6();
         _loc2_.var_2623 = param1.attribute("StatueName");
         for each(_loc3_ in param1.*)
         {
            if((_loc5_ = String(_loc3_.name().toString())) == "StatueID")
            {
               _loc2_.var_2341 = uint(_loc3_);
            }
            else if(_loc5_ == "DisplayName")
            {
               _loc2_.displayName = _loc3_.toString();
            }
            else if(_loc5_ == "Class")
            {
               _loc2_.className = _loc3_.toString();
            }
            else if(_loc5_ == "Gender")
            {
               _loc2_.var_2462 = _loc3_.toString();
            }
            else if(_loc5_ == "Headset")
            {
               _loc2_.var_2443 = _loc3_.toString();
            }
            else if(_loc5_ == "Hairset")
            {
               _loc2_.var_2594 = _loc3_.toString();
            }
            else if(_loc5_ == "Mouthset")
            {
               _loc2_.var_2529 = _loc3_.toString();
            }
            else if(_loc5_ == "Faceset")
            {
               _loc2_.var_2573 = _loc3_.toString();
            }
            else if(_loc5_ == "Armor")
            {
               _loc2_.var_2507 = uint(_loc3_);
            }
            else if(_loc5_ == "Gloves")
            {
               _loc2_.var_2813 = uint(_loc3_);
            }
            else if(_loc5_ == "Boots")
            {
               _loc2_.var_2581 = uint(_loc3_);
            }
            else if(_loc5_ == "Hat")
            {
               _loc2_.var_2622 = uint(_loc3_);
            }
            else if(_loc5_ == "Sword")
            {
               _loc2_.var_2574 = uint(_loc3_);
            }
            else if(_loc5_ == "Shield")
            {
               _loc2_.var_2469 = uint(_loc3_);
            }
            else if(_loc5_ == "AnimationPose")
            {
               _loc2_.var_2763 = _loc3_.toString();
            }
            else if(_loc5_ == "AnimationFrame")
            {
               _loc2_.var_2542 = uint(_loc3_);
            }
            else if(_loc5_ == "FlipAnimation")
            {
               _loc2_.var_2229 = MathUtil.method_50(_loc3_);
            }
            else if(_loc5_ == "XOffset")
            {
               _loc2_.var_2490 = uint(_loc3_);
            }
            else if(_loc5_ == "YOffset")
            {
               _loc2_.var_2767 = uint(_loc3_);
            }
            else if(_loc5_ == "FlavorText")
            {
               _loc2_.var_1646 = _loc3_.toString();
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc2_.var_2623 + ": " + _loc5_);
            }
         }
         _loc4_ = new GfxType();
         return _loc2_;
      }
      
      public static function method_18(param1:XML, param2:Array) : void
      {
         var _loc4_:XML = null;
         var _loc5_:class_6 = null;
         for each(_loc4_ in param1.*)
         {
            if((_loc5_ = method_887(_loc4_)).var_2341)
            {
               param2[_loc5_.var_2341] = _loc5_;
            }
         }
      }
      
      public static function method_1052(param1:uint) : GfxType
      {
         var _loc5_:String = null;
         var _loc2_:class_6 = class_14.var_661[param1];
         if(!_loc2_)
         {
            return null;
         }
         var _loc3_:GfxType = new GfxType();
         _loc3_.var_1598 = true;
         _loc3_.var_522 = _loc2_.var_2229;
         _loc3_.var_177 = 10;
         var _loc4_:Number = const_1000;
         if(_loc2_.className == "Mage")
         {
            _loc3_.var_29 = EntType.MAGE_OPTIONS_FILE;
            _loc5_ = "Gfx_Mage_1.swf";
         }
         else if(_loc2_.className == "Rogue")
         {
            _loc3_.var_29 = EntType.ROGUE_OPTIONS_FILE;
            _loc5_ = "Gfx_Rogue_1.swf";
            _loc3_.var_918 = true;
         }
         else
         {
            _loc3_.var_29 = EntType.PALADIN_OPTIONS_FILE;
            _loc5_ = "Gfx_Paladin_1.swf";
            _loc4_ *= 0.68182;
         }
         var _loc6_:String = EntType.method_683(_loc2_.var_2443,_loc2_.var_2594,_loc2_.var_2529,_loc2_.var_2573,const_1118,const_1110,const_1181,const_1279,_loc4_,_loc2_.className,_loc2_.var_2462);
         GfxType.method_53(new XML(_loc6_),_loc3_);
         var _loc7_:GearType = class_14.gearTypes[_loc2_.var_2507];
         var _loc8_:GearType = class_14.gearTypes[_loc2_.var_2813];
         var _loc9_:GearType = class_14.gearTypes[_loc2_.var_2581];
         var _loc10_:GearType = class_14.gearTypes[_loc2_.var_2622];
         var _loc11_:GearType = class_14.gearTypes[_loc2_.var_2574];
         var _loc12_:GearType = class_14.gearTypes[_loc2_.var_2469];
         if(_loc7_)
         {
            GfxType.method_53(_loc7_.var_582,_loc3_,EntType.ARMOR_SLOT);
         }
         if(_loc8_)
         {
            GfxType.method_53(_loc8_.var_582,_loc3_,EntType.GLOVES_SLOT);
         }
         if(_loc9_)
         {
            GfxType.method_53(_loc9_.var_582,_loc3_,EntType.BOOTS_SLOT);
         }
         if(_loc10_)
         {
            GfxType.method_53(_loc10_.var_582,_loc3_,EntType.HAT_SLOT);
         }
         if(_loc11_)
         {
            GfxType.method_53(_loc11_.var_582,_loc3_,EntType.SWORD_SLOT);
         }
         if(_loc12_)
         {
            GfxType.method_53(_loc12_.var_582,_loc3_,EntType.SHIELD_SLOT);
         }
         return _loc3_;
      }
   }
}
