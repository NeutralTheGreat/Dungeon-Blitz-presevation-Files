package
{
   import flash.display.MovieClip;
   import flash.geom.Point;
   import flash.utils.Dictionary;
   
   public class class_97
   {
       
      
      internal var var_1:Game;
      
      internal var var_336:Dictionary;
      
      internal var var_626:Vector.<class_33>;
      
      internal var var_1721:MovieClip;
      
      public function class_97(param1:Game)
      {
         super();
         this.var_1 = param1;
         this.var_336 = new Dictionary();
         this.var_626 = new Vector.<class_33>();
      }
      
      public function method_1936() : void
      {
         var _loc1_:String = null;
         var _loc2_:class_33 = null;
         for(_loc1_ in this.var_336)
         {
            _loc2_ = this.var_336[_loc1_];
            _loc2_.method_42();
            _loc2_.DestroyUIMovieClip();
            delete this.var_336[_loc1_];
         }
         this.var_336 = null;
         this.var_626 = null;
         this.var_1 = null;
      }
      
      public function method_1799() : void
      {
         var _loc1_:class_33 = null;
         for each(_loc1_ in this.var_626)
         {
            _loc1_.method_42();
         }
         this.var_626.length = 0;
      }
      
      public function method_290(param1:String, param2:Point = null) : void
      {
         var _loc4_:MovieClip = null;
         var _loc5_:class_33 = null;
         var _loc6_:int = 0;
         var _loc7_:String = null;
         var _loc8_:int = 0;
         if(DevSettings.flags & DevSettings.DEVFLAG_NO_GRAPHICS)
         {
            return;
         }
         if(!this.var_1721)
         {
            this.var_1721 = class_4.method_16("a_TutorialOverlay");
            _loc6_ = this.var_1721.numChildren - 1;
            while(_loc6_ >= 0)
            {
               if(_loc4_ = this.var_1721.getChildAt(_loc6_) as MovieClip)
               {
                  if(_loc7_ = _loc4_.name)
                  {
                     (_loc5_ = new class_33(this.var_1,_loc4_)).method_42();
                     this.var_336[_loc7_] = _loc5_;
                  }
               }
               _loc6_--;
            }
         }
         var _loc3_:class_33 = this.var_336[param1];
         if(_loc3_)
         {
            if((_loc8_ = this.var_626.indexOf(_loc3_)) == -1)
            {
               this.var_626.push(_loc3_);
            }
            if(param2)
            {
               _loc3_.method_141(class_33.const_494);
               _loc3_.mMovieClip.x = param2.x;
               _loc3_.mMovieClip.y = param2.y;
            }
            else if(param1 == "am_WhiteOut")
            {
               _loc3_.method_141(class_33.const_298);
            }
            else
            {
               _loc3_.method_141(class_33.const_344);
            }
            _loc3_.PlayAnimation("Ready");
         }
      }
      
      public function method_187(param1:String) : void
      {
         var _loc2_:class_33 = this.var_336[param1];
         if(_loc2_)
         {
            _loc2_.PlayAnimation("Remove");
         }
      }
      
      public function SetAnimation(param1:String, param2:String) : void
      {
         var _loc3_:class_33 = this.var_336[param1];
         if(_loc3_)
         {
            _loc3_.PlayAnimation(param2);
         }
      }
      
      public function method_1976() : void
      {
         var _loc1_:class_33 = null;
         var _loc2_:class_139 = null;
         var _loc3_:int = int(this.var_626.length - 1);
         while(_loc3_ >= 0)
         {
            _loc1_ = this.var_626[_loc3_];
            _loc1_.TickMovieClip();
            this.method_927(_loc1_,false);
            if(_loc1_.mbCompleted)
            {
               _loc2_ = _loc1_.mActiveTimeline;
               if(Boolean(_loc2_) && _loc2_.name == "Remove")
               {
                  this.var_626.splice(_loc3_,1);
                  this.method_927(_loc1_,true);
                  _loc1_.method_42();
               }
            }
            _loc3_--;
         }
      }
      
      public function method_927(param1:class_33, param2:Boolean) : void
      {
         if(Boolean(param1.mMovieClip.parent) && param1.mMovieClip.parent == this.var_1.var_272)
         {
            if(param2)
            {
               this.method_187("am_ArrowGoLeft");
               this.method_187("am_ArrowGoRight");
            }
            else
            {
               if(param1.mMovieClip.x < -this.var_1.levelLayer.x)
               {
                  if(!class_33(this.var_336["am_ArrowGoLeft"]).mbVisible)
                  {
                     this.method_290("am_ArrowGoLeft");
                  }
               }
               else if(class_33(this.var_336["am_ArrowGoLeft"]).mbVisible)
               {
                  this.method_187("am_ArrowGoLeft");
               }
               if(param1.mMovieClip.x > -this.var_1.levelLayer.x + Camera.SCREEN_WIDTH)
               {
                  if(!class_33(this.var_336["am_ArrowGoRight"]).mbVisible)
                  {
                     this.method_290("am_ArrowGoRight");
                  }
               }
               else if(class_33(this.var_336["am_ArrowGoRight"]).mbVisible)
               {
                  this.method_187("am_ArrowGoRight");
               }
            }
         }
      }
   }
}
