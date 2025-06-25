package
{
   import flash.display.MovieClip;
   import flash.utils.getTimer;
   
   public class ScreenTransfer
   {
      
      private static const TIME_BEFORE_SHOW:uint = 1500;
       
      
      internal var var_1:Game;
      
      internal var var_161:MovieClip;
      
      internal var var_2226:int = 0;
      
      internal var var_2474:Boolean = true;
      
      internal var var_2962:String = null;
      
      public function ScreenTransfer(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1197() : void
      {
         if(Boolean(this.var_161) && Boolean(this.var_161.parent))
         {
            this.var_161.parent.removeChild(this.var_161);
         }
         this.var_161 = null;
         this.var_1 = null;
      }
      
      public function Hide() : void
      {
         this.var_1.method_158(this.var_161);
      }
      
      public function method_253() : void
      {
         var _loc4_:* = null;
         var _loc1_:uint = uint(getTimer() - this.var_2226);
         if(Boolean(this.var_161) && _loc1_ > TIME_BEFORE_SHOW)
         {
            this.var_161.alpha = 1;
         }
         this.var_1.main.var_147.alpha = Math.max(0.5,1 - _loc1_ / TIME_BEFORE_SHOW);
         var _loc2_:int = 0;
         var _loc3_:int = int(this.var_1.level.method_2001());
         if(!ResourceManager.method_149("Required"))
         {
            _loc2_ = 0;
         }
         else if(ResourceManager.method_149("Game"))
         {
            _loc2_ = 80 + Math.round(_loc3_ * 0.2);
         }
         else
         {
            _loc2_ = 80 * (ResourceManager.var_1575 / ResourceManager.var_777);
         }
         this.var_161.am_Progress.gotoAndStop(_loc2_);
         if(ResourceManager.var_1542)
         {
            _loc4_ = "Load Failed: " + ResourceManager.var_1542.var_2038;
         }
         else if(!_loc2_)
         {
            _loc4_ = "Loading...";
         }
         else if(_loc2_ < 100)
         {
            _loc4_ = "Loading..." + _loc2_ + "%";
         }
         else
         {
            _loc4_ = "Connecting to World...";
         }
         if(ResourceManager.var_547)
         {
            _loc4_ += " (R=" + ResourceManager.var_547 + ")";
         }
         MathUtil.method_2(this.var_161.am_LoadingText,_loc4_);
      }
      
      public function Display() : void
      {
         var _loc1_:uint = 0;
         if(!this.var_161)
         {
            this.var_161 = class_4.method_16("a_LoadingScreen");
            this.var_161.am_Progress.gotoAndStop(0);
            this.var_161.visible = false;
         }
         if(!this.var_161.visible)
         {
            _loc1_ = uint(this.var_1.edgeLayer.numChildren);
            this.var_1.edgeLayer.addChildAt(this.var_161,_loc1_ > 1 ? _loc1_ - 2 : 0);
            this.var_161.visible = true;
         }
         if(this.var_2474)
         {
            this.var_161.alpha = 1;
            this.var_2226 = -TIME_BEFORE_SHOW;
            this.var_2474 = false;
         }
         else
         {
            this.var_161.alpha = 0;
            this.var_2226 = getTimer();
         }
         MathUtil.method_2(this.var_161.am_LoadingText,"Loading...");
      }
   }
}
