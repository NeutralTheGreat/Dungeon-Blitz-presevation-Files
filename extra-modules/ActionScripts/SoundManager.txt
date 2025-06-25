package
{
   import flash.events.IOErrorEvent;
   import flash.events.SecurityErrorEvent;
   import flash.media.Sound;
   import flash.media.SoundChannel;
   import flash.media.SoundLoaderContext;
   import flash.media.SoundMixer;
   import flash.media.SoundTransform;
   import flash.system.ApplicationDomain;
   import flash.utils.Dictionary;
   
   public class SoundManager
   {
      
      private static const const_652:Dictionary = new Dictionary();
      
      private static const const_742:Dictionary = new Dictionary();
      
      public static var var_804:Boolean;
      
      public static var var_597:Number = 0;
      
      private static const const_710:SoundTransform = new SoundTransform(var_597);
      
      private static var var_510:Vector.<class_149> = new Vector.<class_149>();
       
      
      public function SoundManager()
      {
         super();
      }
      
      public static function SetSoundVolume(param1:Number) : void
      {
         var_597 = param1;
         const_710.volume = param1;
      }
      
      public static function method_401(param1:Boolean) : void
      {
         var _loc2_:class_149 = null;
         if(param1 == var_804)
         {
            return;
         }
         var_804 = param1;
         SoundMixer.soundTransform = new SoundTransform(param1 ? 0 : 1);
         for each(_loc2_ in var_510)
         {
            if(!param1)
            {
               _loc2_.method_816();
            }
            else
            {
               _loc2_.method_487();
            }
         }
      }
      
      public static function method_920(param1:uint) : Number
      {
         var _loc2_:class_149 = var_510[param1];
         return !!_loc2_ ? _loc2_.var_370 : 0;
      }
      
      public static function method_712(param1:Number, param2:Number) : uint
      {
         var _loc3_:uint = var_510.length;
         var _loc4_:class_149 = new class_149(_loc3_,param1,param2);
         var_510.push(_loc4_);
         return _loc3_;
      }
      
      public static function method_218(param1:uint, param2:Number) : void
      {
         var _loc6_:SoundTransform = null;
         var _loc3_:class_149 = var_510[param1];
         if(!_loc3_)
         {
            return;
         }
         if(_loc3_.var_370 == param2)
         {
            return;
         }
         var _loc4_:Number = _loc3_.var_370;
         _loc3_.var_370 = param2;
         var _loc5_:SoundChannel = _loc3_.var_739;
         if(param2 <= 0)
         {
            _loc3_.method_487();
         }
         else if(_loc4_ <= 0)
         {
            _loc3_.method_816();
         }
         else if(_loc5_)
         {
            (_loc6_ = _loc5_.soundTransform).volume = _loc3_.var_919 * param2;
            _loc5_.soundTransform = _loc6_;
         }
      }
      
      public static function method_1017() : void
      {
         var _loc1_:class_149 = null;
         for each(_loc1_ in var_510)
         {
            _loc1_.method_1616();
         }
      }
      
      public static function method_103(param1:uint, param2:String, param3:Number = 1) : void
      {
         var _loc4_:class_149;
         if(!(_loc4_ = var_510[param1]))
         {
            return;
         }
         _loc4_.method_487();
         _loc4_.var_2255 = param2;
         _loc4_.var_2702 = param3;
         if(!param2 || _loc4_.var_370 <= 0 || var_804)
         {
            return;
         }
         var _loc5_:Sound = method_311(param2);
         var _loc6_:SoundChannel;
         if(!(_loc6_ = method_185(_loc5_,0,true)))
         {
            return;
         }
         _loc6_.soundTransform = new SoundTransform(!!_loc4_.var_2390 ? param3 * _loc4_.var_370 : 0);
         _loc4_.var_1637 = _loc5_;
         _loc4_.var_739 = _loc6_;
      }
      
      public static function method_748(param1:uint, param2:String, param3:Number = 1) : void
      {
         var _loc4_:class_149;
         if(!(_loc4_ = var_510[param1]) || _loc4_.var_370 <= 0 || var_804)
         {
            return;
         }
         var _loc5_:Sound = method_311(param2);
         var _loc6_:SoundChannel;
         if(_loc6_ = method_185(_loc5_,0,false))
         {
            _loc6_.soundTransform = new SoundTransform(param3 * _loc4_.var_370);
         }
      }
      
      public static function Play(param1:String, param2:Number = 1, param3:Boolean = false, param4:Number = 0) : SoundChannel
      {
         var _loc9_:String = null;
         var _loc10_:Sound = null;
         var _loc11_:SoundChannel = null;
         var _loc12_:ApplicationDomain = null;
         var _loc13_:Class = null;
         if(var_597 <= 0 || var_804)
         {
            return null;
         }
         var _loc5_:Array = param1.split("|");
         var _loc6_:uint = uint(Math.random() * _loc5_.length);
         param1 = String(_loc5_[_loc6_]);
         var _loc7_:SoundChannel = null;
         var _loc8_:Array = param1.split(",");
         for each(_loc9_ in _loc8_)
         {
            if(_loc9_ != "snd_silence")
            {
               if(!(_loc10_ = const_652[_loc9_]))
               {
                  if(!(_loc12_ = ApplicationDomain.currentDomain).hasDefinition(_loc9_))
                  {
                     method_596(_loc9_);
                     continue;
                  }
                  _loc10_ = new (_loc13_ = _loc12_.getDefinition(_loc9_) as Class)();
                  const_652[_loc9_] = _loc10_;
               }
               if(_loc11_ = method_185(_loc10_,param4,param3))
               {
                  if(param2 != 1)
                  {
                     _loc11_.soundTransform = new SoundTransform(var_597 * param2);
                  }
                  else
                  {
                     _loc11_.soundTransform = const_710;
                  }
                  _loc7_ = _loc11_;
               }
            }
         }
         return _loc7_;
      }
      
      private static function method_596(param1:String) : void
      {
         class_24.method_19("SoundManager: Could not find sound: " + param1);
      }
      
      public static function method_155(param1:SoundChannel) : SoundChannel
      {
         if(param1)
         {
            param1.stop();
         }
         return null;
      }
      
      private static function method_311(param1:String) : Sound
      {
         var _loc2_:Sound = const_742[param1];
         if(!_loc2_)
         {
            _loc2_ = new Sound(ResourceManager.method_466("mp3/" + param1),new SoundLoaderContext(3000));
            _loc2_.addEventListener(IOErrorEvent.IO_ERROR,method_763);
            _loc2_.addEventListener(SecurityErrorEvent.SECURITY_ERROR,method_763);
            const_742[param1] = _loc2_;
         }
         return _loc2_;
      }
      
      private static function method_763(param1:IOErrorEvent) : void
      {
         class_24.method_19(param1.text);
      }
      
      private static function method_185(param1:Sound, param2:uint, param3:Boolean) : SoundChannel
      {
         var _loc4_:SoundChannel = null;
         try
         {
            _loc4_ = param1.play(param2,param3 ? 9999 : 0);
         }
         catch(e:Error)
         {
         }
         return _loc4_;
      }
   }
}
