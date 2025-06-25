package
{
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.geom.ColorTransform;
   import flash.utils.Dictionary;
   import flash.utils.getQualifiedClassName;
   
   public class DayNightManager
   {
      
      public static const const_73:uint = 1;
      
      public static const const_342:uint = 2;
      
      public static const const_340:uint = 3;
      
      public static const const_383:uint = 4;
      
      private static const const_645:uint = 20000;
      
      private static const const_934:uint = 50000;
      
      public static const const_268:Dictionary = new Dictionary();
      
      private static const TIME_OF_DAY_LIST:Array = [const_73,const_73,const_73,const_73,const_73,const_73,const_73,const_73];
      
      private static const TIME_OF_DAY_COUNT:uint = TIME_OF_DAY_LIST.length;
      
      private static const const_1149:uint = 7200;
      
      private static const TIME_PER_CYCLE:uint = const_1149 / TIME_OF_DAY_COUNT;
      
      public static const const_518:uint = const_73;
      
      private static const const_318:Dictionary = new Dictionary();
      
      private static const const_345:Dictionary = new Dictionary();
      
      {
         const_268["Day"] = const_73;
         const_268["Night"] = const_342;
         const_268["Morning"] = const_383;
         const_268["Evening"] = const_340;
         const_318[const_342] = 7829435;
         const_345[const_342] = 2368569;
         const_318[const_340] = 10075033;
         const_345[const_340] = 5618517;
         const_318[const_383] = 10075033;
         const_345[const_383] = 5618517;
      }
      
      internal var var_1:Game;
      
      internal var var_205:Soundscape;
      
      internal var var_2611:String;
      
      internal var var_2812:uint;
      
      internal var var_2072:uint;
      
      internal var var_2230:Boolean;
      
      internal var var_1078:uint = 1;
      
      public function DayNightManager(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1179() : void
      {
         this.var_205 = null;
         this.var_1 = null;
      }
      
      public function method_1547() : void
      {
         var _loc1_:uint = this.var_1.mServerGameTime / TIME_PER_CYCLE;
         var _loc2_:uint = _loc1_ % TIME_OF_DAY_COUNT;
         var _loc3_:uint = uint(TIME_OF_DAY_LIST[_loc2_]);
         var _loc4_:uint;
         if((_loc4_ = this.var_1.level.bInstanced ? const_518 : _loc3_) != this.var_1078)
         {
            this.var_1078 = _loc4_;
            this.method_1268(this.var_1078);
         }
         var _loc5_:String;
         if(!(_loc5_ = Boolean(this.var_1.clientEnt) && Boolean(this.var_1.clientEnt.currRoom) ? this.var_1.clientEnt.currRoom.var_1143 : null) && Boolean(this.var_1.level))
         {
            _loc5_ = this.var_1.level.var_1143;
         }
         if(_loc5_ != this.var_2611 || this.var_2812 != this.var_1078)
         {
            this.method_1101(_loc5_,this.var_1078);
         }
         this.method_1395();
      }
      
      public function method_1268(param1:uint) : void
      {
         var _loc2_:MagicObject = null;
         for each(_loc2_ in this.var_1.var_171.var_410)
         {
            if(!_loc2_.var_2857)
            {
               this.var_1.var_171.method_364(_loc2_);
               this.method_581(_loc2_.dObj,param1);
               if(_loc2_.var_1751)
               {
                  this.var_1.var_171.method_193(_loc2_,true);
               }
            }
         }
         this.method_581(this.var_1.level.var_59,param1);
         if(this.var_1.var_107)
         {
            this.var_1.var_107.method_120();
         }
      }
      
      private function method_1857(param1:MovieClip, param2:uint) : void
      {
         var _loc3_:int = param1.currentFrame;
         if(param2 == const_342)
         {
            param1.gotoAndStop("Night");
         }
         else if(param2 == const_340)
         {
            param1.gotoAndStop("Evening");
         }
         else if(param2 == const_383)
         {
            param1.gotoAndStop("Morning");
         }
         else
         {
            param1.gotoAndStop("Day");
         }
         if(_loc3_ != param1.currentFrame)
         {
            param1.transform.colorTransform = new ColorTransform();
         }
      }
      
      public function method_581(param1:DisplayObject, param2:uint) : void
      {
         var _loc5_:Number = NaN;
         var _loc6_:Number = NaN;
         var _loc7_:Number = NaN;
         if(!param1)
         {
            return;
         }
         var _loc3_:uint = uint(const_318[param2]);
         if(!_loc3_)
         {
            param1.transform.colorTransform = new ColorTransform();
         }
         else
         {
            if(Boolean(param1.name) && !param1.name.indexOf("am_ParallaxHorizon"))
            {
               _loc3_ = uint(const_345[param2]);
            }
            _loc5_ = ((_loc3_ & 16711680) >> 16) / 256;
            _loc6_ = ((_loc3_ & 65280) >> 8) / 256;
            _loc7_ = (_loc3_ & 255) / 256;
            param1.transform.colorTransform = new ColorTransform(_loc5_,_loc6_,_loc7_,1,0,0,0,0);
         }
         var _loc4_:String;
         if(!(_loc4_ = getQualifiedClassName(param1)).indexOf("a_Circadian"))
         {
            this.method_1857(param1 as MovieClip,param2);
         }
      }
      
      public function method_1101(param1:String, param2:uint) : void
      {
         var _loc3_:Soundscape = null;
         if(param1)
         {
            _loc3_ = SoundConfig.method_745(param1,param2);
            if(!_loc3_)
            {
               _loc3_ = SoundConfig.method_745(param1,const_518);
            }
         }
         this.var_2611 = param1;
         this.var_2812 = param2;
         if(_loc3_ == this.var_205)
         {
            return;
         }
         this.var_205 = _loc3_;
         if(Boolean(this.var_205) && Boolean(this.var_205.intro))
         {
            SoundManager.method_748(Main.const_108,this.var_205.intro,this.var_205.introVol);
         }
         this.method_747();
         this.method_576();
         if(this.var_205)
         {
            this.var_2072 = this.var_1.mTimeThisTick + (!!this.var_205.intro ? 5000 : 0);
         }
      }
      
      public function method_576() : void
      {
         if(Boolean(this.var_205) && Boolean(this.var_205.loop))
         {
            SoundManager.method_103(Main.const_108,this.var_205.loop,this.var_205.loopVol);
         }
         this.var_2230 = true;
      }
      
      public function method_747() : void
      {
         SoundManager.method_103(Main.const_108,null);
         this.var_2230 = false;
      }
      
      public function method_1395() : void
      {
         if(!this.var_205 || !this.var_2230)
         {
            return;
         }
         var _loc1_:uint = this.var_1.mTimeThisTick;
         if(_loc1_ < this.var_2072)
         {
            return;
         }
         var _loc2_:Vector.<class_31> = this.var_205.var_1451;
         var _loc3_:uint = _loc2_.length;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:int = Math.random() * this.var_205.var_1451.length;
         var _loc5_:Number = Math.random() * 0.3 + 0.3;
         var _loc6_:class_31 = this.var_205.var_1451[_loc4_];
         SoundManager.method_748(Main.const_108,_loc6_.soundName,_loc5_ * _loc6_.vol);
         this.var_2072 = _loc1_ + const_645 + Math.random() * (const_934 - const_645);
      }
   }
}
