package
{
   public class BossFight
   {
      
      public static const const_1145:uint = 0;
      
      public static const const_821:uint = 1;
      
      public static const const_756:uint = 2;
      
      public static const const_810:uint = 3;
      
      public static const const_1233:String = "am_Boss";
      
      public static const const_734:String = "am_Boss2";
       
      
      private var var_1:Game;
      
      private var mRoom:Room;
      
      internal var var_1434:Boolean;
      
      internal var var_2925:uint;
      
      internal var var_2875:uint;
      
      internal var var_1042:uint = 0;
      
      internal var var_1213:uint = 0;
      
      internal var var_812:uint = 0;
      
      public function BossFight(param1:Game, param2:Room)
      {
         super();
         this.var_1 = param1;
         this.mRoom = param2;
      }
      
      public function method_1896() : void
      {
         this.mRoom = null;
         this.var_1 = null;
      }
      
      public function method_1508() : void
      {
         if(this.var_1434)
         {
            this.method_779();
         }
         this.var_1434 = true;
         this.var_2925 = this.var_1.mTimeThisTick;
      }
      
      public function method_779() : void
      {
         this.var_1434 = false;
         this.var_2875 = this.var_1.mTimeThisTick;
      }
      
      public function method_1981() : void
      {
         var _loc7_:Entity = null;
         if(!this.var_1434)
         {
            return;
         }
         var _loc1_:Entity = this.mRoom.method_35(const_1233);
         var _loc2_:Entity = this.mRoom.var_122.bDoubleBossFight ? this.mRoom.method_35(const_734) : null;
         var _loc3_:uint = !!_loc1_ ? _loc1_.id : 0;
         var _loc4_:String = Boolean(_loc1_) && Boolean(_loc1_.cue) ? _loc1_.cue.displayName : null;
         var _loc5_:uint = !!_loc2_ ? _loc2_.id : 0;
         var _loc6_:String = Boolean(_loc2_) && Boolean(_loc2_.cue) ? _loc2_.cue.displayName : null;
         if(this.var_1042 == const_1145)
         {
            this.var_1042 = const_821;
            this.mRoom.HookSetPhase(null);
            if(this.mRoom.var_122.cutSceneStartBoss)
            {
               this.mRoom.method_465(this.mRoom.var_122.cutSceneStartBoss);
               this.var_812 = this.var_1.mTimeThisTick;
            }
            this.mRoom.method_903(_loc3_,_loc4_,_loc5_,_loc6_);
            this.var_1.linkUpdater.method_1369(this.mRoom.var_113,_loc3_,_loc4_,_loc5_,_loc6_);
         }
         else if(this.var_1042 == const_821)
         {
            if(!this.mRoom.var_1052)
            {
               if(this.var_812)
               {
                  this.var_1213 += this.mRoom.var_235.var_1901 - this.var_812;
                  this.var_812 = 0;
               }
               this.var_1042 = const_756;
               if(_loc7_ = this.mRoom.GetTarget())
               {
                  this.mRoom.RoomAggro(_loc7_);
               }
               if(this.mRoom.var_122.bossFightPhase != null)
               {
                  this.mRoom.HookSetPhase(this.mRoom.var_122.bossFightPhase);
               }
            }
         }
         else if(this.var_1042 == const_756)
         {
            if((!_loc1_ || _loc1_.currHP <= 0) && (!_loc2_ || _loc2_.currHP <= 0))
            {
               this.var_1042 = const_810;
               this.mRoom.method_876();
               this.var_1.linkUpdater.method_1986(this.mRoom.var_113);
               if(this.mRoom.var_122.cutSceneDefeatBoss)
               {
                  this.mRoom.method_1762(this.mRoom.var_122.cutSceneDefeatBoss);
                  this.var_812 = this.var_1.mTimeThisTick;
               }
            }
         }
         else if(this.var_1042 == const_810)
         {
            if(!this.mRoom.var_1052)
            {
               if(this.var_812)
               {
                  this.var_1213 += this.mRoom.var_235.var_1901 - this.var_812;
                  this.var_812 = 0;
               }
               this.mRoom.CueKillAllMonsters();
               this.method_779();
            }
         }
         if(!this.mRoom.var_1047 && _loc3_ || !this.mRoom.var_1377 && _loc5_)
         {
            this.mRoom.method_935(_loc3_,_loc4_,_loc5_,_loc6_);
            this.var_1.linkUpdater.method_1286(this.mRoom.var_113,_loc3_,_loc4_,_loc5_,_loc6_);
         }
      }
   }
}
