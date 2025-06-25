package
{
   import flash.events.MouseEvent;
   import flash.external.ExternalInterface;
   import flash.net.URLRequest;
   import flash.net.navigateToURL;
   
   public class ScreenLevelComplete extends class_32
   {
      
      private static const const_1371:uint = 10;
      
      private static const const_749:Array = ["Ready","Half","One","OneHalf","Two","TwoHalf","Three","ThreeHalf","Four","FourHalf","Five"];
       
      
      private const const_1426:Number = 0.015;
      
      private const const_1428:Number = 0.35;
      
      private const const_554:String = "Progress";
      
      private const const_435:String = "Pulse";
      
      private const const_1213:Number = 1;
      
      private var var_493:Number = 0;
      
      private var var_1305:class_33;
      
      private var var_1444:class_33;
      
      private var var_1584:class_33;
      
      private var var_1589:class_33;
      
      private var var_1525:class_33;
      
      private var var_2108:class_33;
      
      private var var_1379:class_33;
      
      private var var_1438:uint;
      
      private var var_1206:uint;
      
      private var var_1691:uint;
      
      private var var_1980:uint;
      
      private var var_2001:uint;
      
      private var var_1827:uint;
      
      private var var_1998:uint;
      
      private var var_1402:uint;
      
      private var var_2777:uint;
      
      private var var_2664:class_33;
      
      private var var_1678:class_33;
      
      private var var_1839:String;
      
      private var var_1202:String;
      
      private var var_945:uint;
      
      public function ScreenLevelComplete(param1:Game)
      {
         super(param1,"a_DungeonComplete_Bronze","am_Panel");
         var_45 = "FadeIn";
         mbHideOnClear = false;
      }
      
      public static function method_559(param1:uint) : String
      {
         var _loc2_:uint = param1 % 10;
         var _loc3_:uint = param1 % 100 / 10;
         if(_loc3_ == 1)
         {
            return "th";
         }
         if(_loc2_ == 1)
         {
            return "st";
         }
         if(_loc2_ == 2)
         {
            return "nd";
         }
         if(_loc2_ == 3)
         {
            return "rd";
         }
         return "th";
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_2664 = method_1(var_2.am_BasePlate);
         method_10(var_2.am_Leave,this.method_1319);
         method_5(var_2.am_Ranks,this.method_1888);
         this.var_2108 = method_5(var_2.am_Share,this.method_1861);
         this.var_1379 = method_1(var_2.am_StarRating);
         this.var_1305 = method_17(var_2.am_KillsProgress.am_Fill,"Progress",0);
         this.var_1444 = method_17(var_2.am_AccuracyProgress.am_Fill,"Progress",0);
         this.var_1584 = method_17(var_2.am_DeathsProgress.am_Fill,"Progress",0);
         this.var_1589 = method_17(var_2.am_TreasureProgress.am_Fill,"Progress",0);
         this.var_1525 = method_17(var_2.am_TimeProgress.am_Fill,"Progress",0);
         this.var_1678 = method_1(var_2.am_DreadHeader);
         this.var_2108.Hide();
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_2108 = null;
         this.var_1379 = null;
         this.var_1305 = null;
         this.var_1444 = null;
         this.var_1584 = null;
         this.var_1589 = null;
         this.var_1525 = null;
         this.var_1678 = null;
         this.var_2664 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         this.var_1438 = 0;
         this.var_1379.PlayAnimation(const_749[this.var_1438]);
         MathUtil.method_2(var_2.am_MapName,this.var_1202);
         MathUtil.method_2(var_2.am_Rank,MathUtil.method_29(this.var_1206) + method_559(this.var_1206));
         this.method_1119();
      }
      
      override public function OnTickScreen() : void
      {
         var _loc1_:* = false;
         var _loc2_:uint = 0;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc8_:uint = 0;
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc11_:uint = 0;
         var _loc12_:uint = 0;
         if(this.var_493 < this.const_1213)
         {
            this.var_493 += this.const_1426 * var_1.TIMESTEP;
            _loc1_ = this.var_493 >= this.const_1213;
            if(_loc1_)
            {
               this.var_493 = this.const_1213;
            }
            _loc2_ = this.var_945 * 40000;
            _loc3_ = this.var_945 * 20000;
            _loc4_ = this.var_945 * 20000;
            _loc5_ = this.var_945 * 10000;
            _loc6_ = this.var_945 * 10000;
            _loc7_ = Math.min(this.var_1980,Math.round(_loc2_ * this.var_493));
            _loc8_ = Math.min(this.var_2001,Math.round(_loc3_ * this.var_493));
            _loc9_ = Math.min(this.var_1827,Math.round(_loc4_ * this.var_493));
            _loc10_ = Math.min(this.var_1998,Math.round(_loc5_ * this.var_493));
            _loc11_ = _loc1_ ? this.var_1402 : uint(Math.min(this.var_1402,Math.round(_loc6_ * this.var_493)));
            _loc12_ = _loc7_ + _loc8_ + _loc9_ + _loc10_ + _loc11_;
            this.var_1305.mHealthPerc = _loc7_ / _loc2_;
            this.var_1444.mHealthPerc = _loc8_ / _loc3_;
            this.var_1584.mHealthPerc = _loc9_ / _loc4_;
            this.var_1589.mHealthPerc = _loc10_ / _loc5_;
            this.var_1525.mHealthPerc = _loc11_ / _loc6_;
            if(this.var_1379.mbCompleted && this.var_1438 < this.var_1691)
            {
               this.var_1379.PlayAnimation(const_749[++this.var_1438]);
            }
            if(_loc1_)
            {
               if(this.var_1980 >= _loc2_)
               {
                  this.var_1305.PlayAnimation(this.const_435);
               }
               if(this.var_2001 >= _loc3_)
               {
                  this.var_1444.PlayAnimation(this.const_435);
               }
               if(this.var_1827 >= _loc4_)
               {
                  this.var_1584.PlayAnimation(this.const_435);
               }
               if(this.var_1998 >= _loc5_)
               {
                  this.var_1589.PlayAnimation(this.const_435);
               }
               if(this.var_1402 >= _loc6_)
               {
                  this.var_1525.PlayAnimation(this.const_435);
               }
            }
            MathUtil.method_2(var_2.am_KillsScore,MathUtil.method_29(_loc7_,true));
            MathUtil.method_2(var_2.am_AccuracyScore,MathUtil.method_29(_loc8_,true));
            MathUtil.method_2(var_2.am_DeathsScore,MathUtil.method_29(_loc9_,true));
            MathUtil.method_2(var_2.am_TreasureScore,MathUtil.method_29(_loc10_,true));
            if(!_loc1_)
            {
               MathUtil.method_2(var_2.am_TimeScore,MathUtil.method_29(_loc11_,true),true);
            }
            else
            {
               MathUtil.method_2(var_2.am_TimeScore,"<font color=\'#3FFF3F\'>" + MathUtil.method_29(_loc11_,true) + "</font>",true);
            }
            MathUtil.method_2(var_2.am_TotalScore,MathUtil.method_29(_loc12_,true));
         }
      }
      
      public function OnInitDisplay(param1:uint, param2:uint, param3:uint, param4:uint, param5:uint, param6:uint, param7:uint, param8:uint, param9:Boolean) : void
      {
         this.var_1839 = var_1.level.internalName;
         this.var_945 = param2;
         this.var_1202 = Level.method_73(this.var_1839);
         if(!this.var_1202)
         {
            this.var_1202 = "Dungeon Complete!";
         }
         this.var_1206 = param3;
         this.var_1691 = param1;
         this.var_1980 = param4;
         this.var_2001 = param5;
         this.var_1827 = param6;
         this.var_1998 = param7;
         this.var_1402 = param8;
         this.var_2777 = param4 + param5 + param6 + param7 + param8;
         if(!param9)
         {
            this.var_1678.Hide();
         }
         else
         {
            this.var_1678.Show();
         }
         if(!this.var_1691 && !this.var_1980 && !this.var_2001 && !this.var_1827 && !this.var_1998 && !this.var_1402 && !this.var_945)
         {
            this.var_1202 = !!this.var_1206 ? "Time Has Expired" : "Uh Oh, Level Error Occured";
            this.var_1206 = 0;
            this.var_1839 = null;
         }
         if(SoundConfig.var_1705)
         {
            SoundManager.Play(SoundConfig.var_1705);
         }
      }
      
      private function method_1119() : void
      {
         this.var_493 = 0;
         this.var_1305.BeginHealthMode(this.const_554,0);
         this.var_1444.BeginHealthMode(this.const_554,0);
         this.var_1584.BeginHealthMode(this.const_554,0);
         this.var_1589.BeginHealthMode(this.const_554,0);
         this.var_1525.BeginHealthMode(this.const_554,0);
      }
      
      private function method_1888(param1:MouseEvent) : void
      {
         var _loc2_:String = "http://www.dungeonblitz.com/rankings/";
         var _loc3_:String = Level.method_1476(this.var_1839);
         if(_loc3_)
         {
            _loc2_ += _loc3_ + "/";
         }
         navigateToURL(new URLRequest(_loc2_),"_blank");
      }
      
      private function method_1861(param1:MouseEvent) : void
      {
         if(ExternalInterface.available && Boolean(var_1.clientFacebookID))
         {
            ExternalInterface.call("JSShareScore",this.var_1202,this.var_2777,this.var_1206,this.var_1691);
         }
      }
      
      private function method_1319(param1:MouseEvent) : void
      {
         Hide();
         var_1.OpenDoor(new Door("ExitMission",0,0,null,2,null));
      }
   }
}
