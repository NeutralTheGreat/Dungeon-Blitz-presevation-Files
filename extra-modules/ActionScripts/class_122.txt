package
{
   public class class_122
   {
      
      public static const PRECISION_FIX_OFFSET:int = 2;
       
      
      internal var var_1:Game;
      
      internal var e:Entity;
      
      internal var var_914:int;
      
      internal var var_950:int;
      
      internal var var_1794:int;
      
      internal var var_556:Boolean = true;
      
      internal var var_1667:Boolean = false;
      
      internal var var_2778:Boolean = false;
      
      internal var var_1792:Number = 0;
      
      internal var var_2090:Number = 0;
      
      internal var var_1281:uint = 0;
      
      internal var var_873:Number = 0;
      
      internal var var_885:Number = 0;
      
      public function class_122(param1:Game, param2:Entity)
      {
         super();
         this.var_1 = param1;
         this.e = param2;
      }
      
      public function method_1998() : void
      {
         this.e = null;
         this.var_1 = null;
      }
      
      public function method_550() : void
      {
         var _loc2_:Number = NaN;
         var _loc1_:Number = this.var_1.mTimeThisTick;
         if(Boolean(DevSettings.flags & DevSettings.DEVFLAG_SHOWENTITYGHOST) && this.e.id >= 1000000000)
         {
            this.e.UpdatePos(this.var_914,this.var_950);
            return;
         }
         if(this.e.entState == Entity.const_6)
         {
            this.var_1281 = 0;
            this.e.var_282.x = 0;
            this.e.var_282.y = 0;
            return;
         }
         if(this.var_2090 + this.var_1281 <= _loc1_)
         {
            this.var_1281 = 0;
            this.e.var_282.x = 0;
            this.e.var_282.y = 0;
         }
         if(this.var_2090 < this.var_1792)
         {
            if(this.var_556)
            {
               this.e.TeleportTo(this.var_914,this.var_950 - PRECISION_FIX_OFFSET);
               this.e.var_282.x = 0;
               this.e.var_282.y = 0;
               this.var_556 = false;
            }
            else
            {
               this.var_873 = this.var_914 - this.e.physPosX;
               this.var_885 = this.var_950 - this.e.physPosY - PRECISION_FIX_OFFSET;
               if(Math.abs(this.var_873) > 256 || Math.abs(this.var_885) > 128)
               {
                  this.e.TeleportTo(this.var_914,this.var_950 - PRECISION_FIX_OFFSET);
               }
               else
               {
                  if(this.var_873 > -1 && this.var_873 < 1)
                  {
                     this.var_873 = 0;
                  }
                  if(this.var_885 > -1 && this.var_885 < 1)
                  {
                     this.var_885 = 0;
                  }
                  this.var_1281 = Boolean(this.var_873) || Boolean(this.var_885) ? uint(4 * LinkUpdater.MIN_TIME_BETWEEN_UPDATES) : 0;
                  if(this.var_1281)
                  {
                     _loc2_ = 1000 / (Game.TARGETFPS * this.var_1281);
                     this.e.var_282.x = _loc2_ * this.var_873;
                     this.e.var_282.y = _loc2_ * this.var_885;
                  }
               }
            }
            this.e.velocity.x = this.var_1794 * LinkUpdater.VELOCITY_DEFLATE;
            this.var_2090 = this.var_1792;
         }
      }
   }
}
