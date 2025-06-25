package
{
   import flash.events.MouseEvent;
   
   public class class_78 extends class_32
   {
      
      private static const const_750:Number = 132.8;
      
      private static const const_406:Number = 155.7;
      
      private static const const_711:Number = 180.7;
       
      
      internal var var_725:uint;
      
      internal var var_25:class_64;
      
      internal var var_1453:uint;
      
      internal var var_616:class_33;
      
      internal var var_987:Boolean;
      
      internal var var_1177:class_33;
      
      internal var var_1189:class_33;
      
      internal var var_346:class_33;
      
      internal var var_198:class_33;
      
      internal var var_123:class_33;
      
      internal var var_291:class_33;
      
      public function class_78(param1:Game)
      {
         super(param1,"a_Popup_Socket","am_PromptPanel");
         var_15 = true;
         var_45 = "FadeIn";
      }
      
      public static function method_416(param1:class_32, param2:uint, param3:uint, param4:class_64) : Boolean
      {
         var _loc6_:Entity;
         var _loc5_:Game;
         if(!(_loc6_ = (_loc5_ = param1.var_1).clientEnt) || !_loc5_.CanSendPacket())
         {
            return false;
         }
         var _loc7_:class_42;
         if(!(_loc7_ = _loc5_.mOwnedGear[param2]))
         {
            return false;
         }
         var _loc8_:class_114;
         if(!(_loc8_ = _loc5_.mOwnedCharms[param4.method_75()]))
         {
            return false;
         }
         if(!param3)
         {
            return false;
         }
         var _loc9_:GearType = _loc7_.gearType;
         var _loc10_:uint = uint(GearType.var_603[_loc9_.var_8]);
         var _loc11_:uint = param4.method_75();
         _loc6_.method_1915(param2,param4,param3);
         var _loc12_:Packet;
         (_loc12_ = new Packet(LinkUpdater.const_773)).method_9(_loc6_.id);
         _loc12_.method_20(GearType.GEARTYPE_BITSTOSEND,param2);
         _loc12_.method_20(GearType.const_176,_loc10_);
         _loc12_.method_20(class_64.const_101,_loc11_);
         _loc12_.method_20(class_1.const_765,param3);
         _loc5_.serverConn.SendPacket(_loc12_);
         _loc5_.screenArmory.Refresh();
         param1.method_265("Collapse");
         return true;
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_1177 = method_23(var_2.am_Cancel);
         this.var_1189 = method_10(var_2.am_Socket,this.method_1798);
         this.var_616 = method_1(var_2.am_CharmHolder);
         this.var_346 = method_1(var_2.am_Base);
         this.var_198 = method_1(var_2.am_PrimaryColor);
         this.var_123 = method_1(var_2.am_SecondaryColor);
         this.var_291 = method_1(var_2.am_TertiaryColor);
         method_23(var_2.am_Exit);
         var_2.am_TertiaryStat.mouseEnabled = false;
      }
      
      override public function OnDestroyScreen() : void
      {
         method_14(this.var_616.mMovieClip.am_IconHolder);
         this.var_198 = null;
         this.var_123 = null;
         this.var_291 = null;
         this.var_346 = null;
         this.var_616 = null;
         this.var_25 = null;
         this.var_1177 = null;
         this.var_1189 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         if(!this.var_25)
         {
            return;
         }
         this.var_25.method_78(this,this.var_616.mMovieClip.am_IconHolder);
         var _loc1_:class_1 = this.var_25.method_115();
         if(this.var_25.method_118())
         {
            this.var_346.PlayAnimation("TriStat");
            this.var_291.Show();
            this.var_123.Show();
            this.var_198.PlayAnimation(this.var_25.var_13.var_1321);
            this.var_123.PlayAnimation(this.var_25.var_13.var_1560);
            this.var_291.PlayAnimation(this.var_25.var_13.var_1510);
            MathUtil.method_8(var_2.am_Name,this.var_25.var_13.displayName,ScreenArmory.const_23);
            MathUtil.method_2(var_2.am_PrimaryStat,this.var_25.var_13.var_1327);
            MathUtil.method_2(var_2.am_SecondaryStat,this.var_25.var_13.var_1397);
            MathUtil.method_2(var_2.am_TertiaryStat,this.var_25.var_13.var_1617);
            this.var_1177.mMovieClip.y = const_711;
            this.var_1189.mMovieClip.y = const_711;
         }
         else if(this.var_25.method_124())
         {
            this.var_346.PlayAnimation("DualStat");
            this.var_291.Hide();
            this.var_123.Show();
            this.var_198.PlayAnimation(this.var_25.var_13.var_1482);
            this.var_123.PlayAnimation(this.var_25.var_13.var_1353);
            MathUtil.method_8(var_2.am_Name,this.var_25.var_13.displayName,ScreenArmory.const_22);
            MathUtil.method_2(var_2.am_PrimaryStat,this.var_25.var_13.var_1339);
            MathUtil.method_2(var_2.am_SecondaryStat,this.var_25.var_13.var_1513);
            MathUtil.method_2(var_2.am_TertiaryStat,"");
            this.var_1177.mMovieClip.y = const_406;
            this.var_1189.mMovieClip.y = const_406;
         }
         else if(!_loc1_)
         {
            this.var_346.PlayAnimation("SingleStat");
            this.var_123.Hide();
            this.var_291.Hide();
            MathUtil.method_8(var_2.am_Name,this.var_25.method_49(),ScreenArmory.const_24);
            MathUtil.method_2(var_2.am_PrimaryStat,this.var_25.var_13.var_203);
            MathUtil.method_2(var_2.am_SecondaryStat,"");
            MathUtil.method_2(var_2.am_TertiaryStat,"");
            this.var_1177.mMovieClip.y = const_750;
            this.var_1189.mMovieClip.y = const_750;
            this.var_198.PlayAnimation(this.var_25.var_13.var_115);
         }
         else
         {
            this.var_346.PlayAnimation("DualStat");
            this.var_291.Hide();
            this.var_123.Show();
            this.var_123.PlayAnimation(_loc1_.var_115);
            this.var_198.PlayAnimation(this.var_25.var_13.var_115);
            MathUtil.method_2(var_2.am_PrimaryStat,this.var_25.var_13.var_203);
            MathUtil.method_2(var_2.am_SecondaryStat,this.var_25.method_171());
            MathUtil.method_2(var_2.am_TertiaryStat,"");
            this.var_1177.mMovieClip.y = const_406;
            this.var_1189.mMovieClip.y = const_406;
            if(this.var_25.var_8 == class_64.const_341)
            {
               MathUtil.method_8(var_2.am_Name,this.var_25.method_49(),ScreenArmory.const_22);
            }
            else if(this.var_25.var_8 == class_64.const_312)
            {
               MathUtil.method_8(var_2.am_Name,this.var_25.method_49(),ScreenArmory.const_23);
            }
         }
         this.var_987 = false;
      }
      
      public function OnInitDisplay(param1:class_64, param2:uint, param3:uint) : void
      {
         this.var_25 = param1;
         this.var_725 = param2;
         this.var_1453 = param3;
      }
      
      public function method_1798(param1:MouseEvent) : void
      {
         if(!this.var_987 && method_416(this,this.var_725,this.var_1453,this.var_25))
         {
            this.var_987 = true;
         }
      }
   }
}
