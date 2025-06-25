package
{
   import flash.display.MovieClip;
   
   public class class_100 extends class_32
   {
      
      private static const const_1196:Number = 1 / (Game.TARGETFPS * 2);
      
      private static const const_605:String = "Raising your combat level to match teammates: ";
      
      private static const const_751:String = "Lowering your combat level to match teammates: ";
       
      
      private var var_267:int;
      
      private var var_761:int;
      
      private var var_1938:Number;
      
      private var var_770:Number;
      
      private var var_1034:MovieClip;
      
      private var var_1413:MovieClip;
      
      private var var_1430:MovieClip;
      
      private var var_1471:MovieClip;
      
      public function class_100(param1:Game)
      {
         super(param1,"a_FloaterSlugline",null);
         var_15 = true;
         var_45 = "FadeIn";
         var_92 = 2500;
         var_112 = true;
         var_101 = false;
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_1034 = var_2.am_CombatLevel;
         this.var_1413 = var_2.am_DungeonLevel;
         this.var_1430 = this.var_1034.am_ArrowUp;
         this.var_1471 = this.var_1034.am_ArrowDown;
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_1034 = null;
         this.var_1413 = null;
         this.var_1430 = null;
         this.var_1471 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc5_:uint = 0;
         var _loc1_:Entity = var_1.clientEnt;
         var _loc2_:Level = var_1.level;
         if(!_loc1_ || !_loc2_)
         {
            return;
         }
         var _loc3_:String = _loc2_.internalName;
         var _loc4_:String = Level.method_73(_loc3_);
         MathUtil.method_2(var_2.am_Name.am_Text,_loc4_);
         if(!_loc2_.bInstanced || !_loc4_)
         {
            this.var_1034.visible = false;
            this.var_1413.visible = false;
            this.var_761 = 0;
            this.var_267 = 0;
         }
         else
         {
            this.var_267 = !!var_1.mBonusLevels ? _loc1_.mExpLevel : _loc1_.var_64;
            this.var_761 = _loc1_.var_64;
            this.var_1938 = this.var_267;
            if(this.var_267 != _loc1_.var_64)
            {
               if(this.var_267 == this.var_761)
               {
                  this.var_1430.visible = false;
                  this.var_1471.visible = false;
                  this.var_770 = 0;
               }
               else
               {
                  this.var_770 = const_1196 * (this.var_761 - this.var_267);
                  if(this.var_770 >= 0)
                  {
                     this.var_1430.visible = true;
                     this.var_1471.visible = false;
                     MathUtil.method_2(var_2.am_CombatLevel.am_Text,const_605 + this.var_267);
                  }
                  else
                  {
                     this.var_1430.visible = false;
                     this.var_1471.visible = true;
                     MathUtil.method_2(var_2.am_CombatLevel.am_Text,const_751 + this.var_267);
                  }
               }
               this.var_1034.visible = true;
            }
            else
            {
               this.var_1034.visible = false;
            }
            _loc5_ = var_1.mBonusLevels + _loc2_.mapLevel;
            MathUtil.method_2(this.var_1413.am_Text,"Dungeon Level: " + _loc5_);
            this.var_1413.visible = true;
         }
      }
      
      override public function OnTickScreen() : void
      {
         if(!this.var_770)
         {
            return;
         }
         this.var_1938 += this.var_770 * var_1.TIMESTEP;
         this.var_267 = uint(this.var_1938);
         if(this.var_770 < 0)
         {
            if(this.var_267 < this.var_761)
            {
               this.var_770 = 0;
               this.var_267 = this.var_761;
            }
            MathUtil.method_2(var_2.am_CombatLevel.am_Text,const_751 + this.var_267);
         }
         else
         {
            if(this.var_267 > this.var_761)
            {
               this.var_770 = 0;
               this.var_267 = this.var_761;
            }
            MathUtil.method_2(var_2.am_CombatLevel.am_Text,const_605 + this.var_267);
         }
      }
   }
}
