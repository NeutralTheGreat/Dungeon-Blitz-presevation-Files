package
{
   import flash.display.Bitmap;
   import flash.display.Graphics;
   import flash.display.MovieClip;
   
   public class class_46 extends class_32
   {
      
      private static const const_34:uint = 4;
      
      private static const const_1370:uint = 4500;
      
      private static const const_1019:int = -50;
      
      private static const const_917:int = 0;
      
      public static const const_1339:uint = 0;
      
      public static const const_828:uint = 1;
      
      public static const const_211:uint = 2;
      
      public static const const_586:uint = 3;
      
      public static const const_561:uint = 4;
      
      public static const const_343:uint = 5;
      
      public static const const_629:uint = 6;
      
      public static const const_692:uint = 7;
      
      public static const const_381:uint = 8;
      
      public static const const_726:uint = 9;
      
      public static const const_761:uint = 10;
      
      public static const const_720:uint = 11;
      
      public static const const_647:uint = 12;
      
      public static const const_772:uint = 13;
      
      public static const const_722:uint = 14;
      
      public static const const_588:uint = 15;
      
      public static const const_546:uint = 16;
      
      public static const const_532:uint = 17;
      
      public static const const_353:uint = 18;
      
      public static const const_572:uint = 19;
      
      private static const const_1216:Number = 37;
      
      private static const const_822:Number = 16;
       
      
      private var var_560:Vector.<class_33>;
      
      private var var_1308:Vector.<class_33>;
      
      private var var_1975:Vector.<class_33>;
      
      private var var_1356:Vector.<class_33>;
      
      private var var_998:Vector.<class_33>;
      
      private var var_944:Vector.<class_33>;
      
      private var var_992:Vector.<class_33>;
      
      private var var_976:Vector.<class_33>;
      
      private var var_2592:MovieClip;
      
      private var var_2546:MovieClip;
      
      private var var_791:Array;
      
      private var var_1406:Array;
      
      private var var_96:uint = 0;
      
      private var var_2437:uint = 0;
      
      public function class_46(param1:Game)
      {
         super(param1,"a_ScreenNotification",null);
         var_15 = true;
         mbHideOnClear = false;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc2_:MovieClip = null;
         var _loc3_:MovieClip = null;
         this.var_560 = new Vector.<class_33>(const_34,true);
         this.var_1308 = new Vector.<class_33>(const_34,true);
         this.var_1975 = new Vector.<class_33>(const_34,true);
         this.var_1356 = new Vector.<class_33>(const_34,true);
         this.var_998 = new Vector.<class_33>(const_34,true);
         this.var_944 = new Vector.<class_33>(const_34,true);
         this.var_992 = new Vector.<class_33>(const_34,true);
         this.var_976 = new Vector.<class_33>(const_34,true);
         var _loc1_:uint = 0;
         while(_loc1_ < const_34)
         {
            _loc2_ = var_2["am_Panel" + _loc1_] as MovieClip;
            this.var_560[_loc1_] = method_1(_loc2_);
            this.var_560[_loc1_].mMovieClip.mouseChildren = false;
            this.var_560[_loc1_].mMovieClip.mouseEnabled = false;
            this.var_560[_loc1_].Hide();
            _loc3_ = _loc2_.am_Panel;
            this.var_1308[_loc1_] = method_1(_loc3_);
            this.var_1975[_loc1_] = method_1(_loc3_.am_MaterialType);
            this.var_1356[_loc1_] = method_1(_loc3_.am_New);
            this.var_998[_loc1_] = method_1(_loc3_.am_Online);
            this.var_944[_loc1_] = method_1(_loc3_.am_Offline);
            this.var_992[_loc1_] = method_1(_loc3_.am_IconBase);
            this.var_976[_loc1_] = method_1(_loc3_.am_Tinker);
            _loc1_++;
         }
         this.var_2437 = this.var_560[0].mMovieClip.y;
         this.var_791 = [0,0,0,0];
         this.var_1406 = new Array();
         this.var_2592 = class_4.method_16("a_RewardTypeIcon_DyeSmall");
         this.var_2546 = class_4.method_16("a_RewardTypeIcon_DyeLarge");
         Hide();
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_560 = null;
         this.var_1308 = null;
         this.var_1975 = null;
         this.var_1356 = null;
         this.var_791 = null;
         this.var_1406 = null;
         this.var_998 = null;
         this.var_944 = null;
         this.var_992 = null;
         this.var_976 = null;
         this.var_2592 = null;
         this.var_2546 = null;
      }
      
      public function ShowNotification(param1:uint, param2:String, param3:String = "M", param4:Boolean = true, param5:String = null, param6:String = null, param7:class_64 = null, param8:class_21 = null) : void
      {
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc13_:String = null;
         var _loc14_:Array = null;
         var _loc20_:MovieClip = null;
         var _loc21_:MovieClip = null;
         var _loc22_:Bitmap = null;
         var _loc23_:Boolean = false;
         var _loc24_:class_20 = null;
         var _loc25_:class_7 = null;
         var _loc26_:class_137 = null;
         var _loc27_:uint = 0;
         Display();
         if(param3 == "R")
         {
            _loc9_ = ScreenArmory.const_22;
            _loc10_ = ScreenArmory.const_814;
         }
         else if(param3 == "L")
         {
            _loc9_ = ScreenArmory.const_23;
            _loc10_ = ScreenArmory.const_672;
         }
         else if(param3 == "U")
         {
            _loc9_ = ScreenArmory.const_315;
            _loc10_ = ScreenArmory.const_1125;
         }
         else
         {
            _loc9_ = ScreenArmory.const_24;
            _loc10_ = ScreenArmory.const_455;
         }
         var _loc11_:class_33;
         (_loc11_ = this.var_560[this.var_96]).mMovieClip.y = this.var_2437;
         this.var_791[this.var_96] = var_1.mTimeThisTick + 4500;
         var _loc12_:class_33 = this.var_1308[this.var_96];
         var _loc15_:String = param2;
         if(param1 == const_720)
         {
            this.var_998[this.var_96].Show();
            this.var_944[this.var_96].Hide();
            this.var_992[this.var_96].Hide();
            this.var_976[this.var_96].Hide();
         }
         else if(param1 == const_647)
         {
            this.var_998[this.var_96].Hide();
            this.var_944[this.var_96].Show();
            this.var_992[this.var_96].Hide();
            this.var_976[this.var_96].Hide();
         }
         else if(param1 == const_722)
         {
            this.var_998[this.var_96].Hide();
            this.var_944[this.var_96].Hide();
            this.var_992[this.var_96].Hide();
            this.var_976[this.var_96].Show();
            _loc15_ = "   " + param2;
         }
         else
         {
            this.var_998[this.var_96].Hide();
            this.var_944[this.var_96].Hide();
            this.var_992[this.var_96].Show();
            this.var_976[this.var_96].Hide();
            _loc13_ = !!param6 ? param6 : this.method_733(param1);
            if((Boolean(_loc14_ = !!param6 ? param6.split(":") : null)) && _loc14_.length != 2)
            {
               _loc14_ = null;
            }
            _loc15_ = " " + param2;
         }
         var _loc16_:MovieClip = _loc12_.mMovieClip.am_IconHolder;
         if(param1 == const_211 && Boolean(param7))
         {
            _loc20_ = param7.method_1842();
            _loc16_.removeChildren();
            _loc16_.addChild(_loc20_);
         }
         else if(param1 == const_532 || param1 == const_546 || param1 == const_353 && param8)
         {
            _loc21_ = class_4.method_16(param8.var_8 == "L" ? "a_RewardTypeIcon_DyeLarge" : "a_RewardTypeIcon_DyeSmall");
            var_1.screenHudTooltip.SkinDyeIcon(param8,_loc21_.am_DyeSwap);
            _loc16_.removeChildren();
            _loc16_.addChild(_loc21_);
         }
         else if(param1 == const_572)
         {
            _loc16_.removeChildren();
            method_12(_loc16_,this.method_733(param1));
         }
         else if(_loc14_)
         {
            method_14(_loc16_);
            _loc23_ = false;
            if(_loc14_[0] == "Mount")
            {
               if(_loc24_ = class_14.var_362[_loc14_[1]])
               {
                  _loc22_ = class_41.method_168(_loc24_,2,2,44,44,var_1.main.overallScale);
                  _loc16_.addChild(_loc22_);
                  _loc23_ = true;
               }
            }
            else if(_loc14_[0] == "Pet")
            {
               if(_loc25_ = class_14.var_233[_loc14_[1]])
               {
                  _loc22_ = class_41.method_85(_loc25_,2,2,44,44,var_1.main.overallScale);
                  _loc16_.addChild(_loc22_);
                  _loc23_ = true;
               }
            }
            if(!_loc23_)
            {
               method_12(_loc16_,_loc13_);
            }
         }
         else if(_loc13_)
         {
            method_12(_loc16_,_loc13_);
         }
         else
         {
            method_14(_loc16_);
         }
         MathUtil.method_8(_loc12_.mMovieClip.am_Message,_loc15_,_loc9_,_loc10_);
         _loc12_.mMovieClip.am_Message.width = _loc12_.mMovieClip.am_Message.textWidth + 25;
         var _loc17_:Graphics;
         (_loc17_ = _loc12_.mMovieClip.am_MatteHolder.graphics).clear();
         _loc17_.beginFill(0,0.75);
         _loc17_.drawRoundRect(0,0,_loc12_.mMovieClip.am_Message.textWidth + 80,const_1216,const_822,const_822);
         _loc17_.endFill();
         if(param4)
         {
            this.var_1356[this.var_96].Show();
         }
         else
         {
            this.var_1356[this.var_96].Hide();
         }
         var _loc18_:class_33 = this.var_1975[this.var_96];
         if(param5)
         {
            _loc18_.Show();
            _loc18_.PlayAnimation(param5);
         }
         else
         {
            _loc18_.Hide();
         }
         _loc11_.Show();
         _loc11_.PlayAnimation("FadeIn");
         var _loc19_:int = 0;
         while(_loc19_ < const_34)
         {
            if(_loc26_ = this.var_1406[_loc19_])
            {
               _loc26_.ForceComplete();
            }
            if(_loc19_ != this.var_96)
            {
               if((_loc11_ = this.var_560[_loc19_]).mbVisible)
               {
                  _loc27_ = (this.var_96 - _loc19_ + const_34) % const_34;
                  this.var_1406[_loc19_] = method_909(_loc11_.mMovieClip,_loc11_.mMovieClip.x,this.var_2437 + _loc27_ * const_1019,250,class_137.method_113);
                  this.var_791[_loc19_] += const_917;
               }
            }
            _loc19_++;
         }
         this.var_96 = (this.var_96 + 1) % const_34;
         mWindow.mMovieClip.mouseChildren = false;
         mWindow.mMovieClip.mouseEnabled = false;
      }
      
      override public function OnTickScreen() : void
      {
         var _loc4_:class_33 = null;
         var _loc1_:Boolean = true;
         var _loc2_:uint = uint(var_1.mTimeThisTick);
         var _loc3_:int = 0;
         while(_loc3_ < const_34)
         {
            _loc4_ = this.var_560[_loc3_];
            if(this.var_791[_loc3_])
            {
               _loc1_ = false;
               if(_loc2_ >= this.var_791[_loc3_])
               {
                  _loc4_.PlayAnimation("FadeOut");
                  this.var_791[_loc3_] = 0;
               }
            }
            else if(!_loc4_.mbCompleted)
            {
               _loc1_ = false;
            }
            else if(_loc4_.mbVisible)
            {
               _loc4_.Hide();
               this.var_1406[_loc3_] = null;
            }
            _loc3_++;
         }
         if(_loc1_)
         {
            Hide();
            this.var_96 = 0;
         }
      }
      
      public function method_733(param1:uint) : String
      {
         var _loc2_:String = null;
         switch(param1)
         {
            case const_828:
               _loc2_ = "a_NotificationIcon_Gear";
               break;
            case const_211:
               _loc2_ = "a_NotificationIcon_Charm";
               break;
            case const_586:
               _loc2_ = "a_NotificationIcon_Ability";
               break;
            case const_561:
               _loc2_ = "a_NotificationIcon_Pet";
               break;
            case const_343:
               _loc2_ = "a_NotificationIcon_PetRank";
               break;
            case const_629:
               _loc2_ = "a_NotificationIcon_Housing";
               break;
            case const_692:
               _loc2_ = "a_NotificationIcon_TalentPoint";
               break;
            case const_726:
               _loc2_ = "a_NotificationIcon_Material";
               break;
            case const_761:
               _loc2_ = "a_NotificationIcon_Mount";
               break;
            case const_381:
               _loc2_ = "a_NotificationIcon_FriendRequest";
               break;
            case const_772:
               _loc2_ = "a_NewEggsIcon";
               break;
            case const_588:
               _loc2_ = "a_Lockbox02";
               break;
            case const_546:
               _loc2_ = "a_DyeBottleBig";
               break;
            case const_532:
               _loc2_ = "a_DyeBottleSmall";
               break;
            case const_353:
               _loc2_ = "a_Icon_PotionGearFind";
               break;
            case const_572:
               _loc2_ = "a_Icon_LockboxKey";
         }
         return _loc2_;
      }
      
      override public function OnClearScreen() : void
      {
         var _loc2_:class_33 = null;
         var _loc3_:MovieClip = null;
         var _loc1_:uint = 0;
         while(_loc1_ < const_34)
         {
            _loc2_ = this.var_1308[_loc1_];
            _loc3_ = _loc2_.mMovieClip.am_IconHolder;
            method_14(_loc3_);
            _loc1_++;
         }
      }
   }
}
