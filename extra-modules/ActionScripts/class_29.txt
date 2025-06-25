package
{
   import flash.display.FrameLabel;
   import flash.display.MovieClip;
   import flash.system.ApplicationDomain;
   import flash.utils.Dictionary;
   
   public class class_29
   {
      
      private static const const_498:Dictionary = new Dictionary();
       
      
      internal var var_1:Game;
      
      public function class_29(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public static function method_2117(param1:String, param2:String) : Boolean
      {
         var _loc3_:Object = ResourceManager.const_40[param1];
         if(!_loc3_)
         {
            return false;
         }
         var _loc4_:ApplicationDomain;
         if(!(_loc4_ = _loc3_.applicationDomain).hasDefinition(param2))
         {
            return false;
         }
         return true;
      }
      
      public static function method_765(param1:String, param2:String, param3:String) : class_30
      {
         return const_498[param2 + "/" + param1 + ":" + param3];
      }
      
      public static function method_602(param1:String, param2:String, param3:String, param4:String) : class_30
      {
         var _loc7_:MovieClip = null;
         var _loc9_:Vector.<uint> = null;
         var _loc10_:String = null;
         var _loc11_:String = null;
         var _loc12_:uint = 0;
         var _loc13_:uint = 0;
         var _loc14_:uint = 0;
         var _loc15_:uint = 0;
         var _loc16_:uint = 0;
         var _loc17_:FrameLabel = null;
         var _loc18_:ApplicationDomain = null;
         var _loc19_:Class = null;
         var _loc5_:String = param2 + "/" + param1 + ":" + param4;
         var _loc6_:class_30;
         if(!(_loc6_ = const_498[_loc5_]))
         {
            _loc6_ = new class_30(param1,param2);
            const_498[_loc5_] = _loc6_;
         }
         var _loc8_:Object;
         if(!(_loc8_ = ResourceManager.const_40[param2]))
         {
            _loc7_ = new MovieClip();
            class_24.method_19("Could not find animation file: " + param2);
         }
         else if(!(_loc18_ = _loc8_.applicationDomain).hasDefinition(param3))
         {
            _loc7_ = new MovieClip();
            class_24.method_19("Could not find " + param3 + " in file: " + param2);
         }
         else
         {
            _loc7_ = new (_loc19_ = _loc18_.getDefinition(param3) as Class)();
            MathUtil.method_235(_loc7_);
         }
         for each(_loc17_ in _loc7_.scenes[0].labels)
         {
            if(!(_loc11_ = String(_loc17_.name)).indexOf("Loop"))
            {
               _loc13_ = uint(_loc17_.frame);
            }
            else if(!_loc11_.indexOf("Recover"))
            {
               _loc14_ = uint(_loc17_.frame);
            }
            else if(!_loc11_.indexOf("End"))
            {
               _loc15_ = uint(_loc17_.frame);
            }
            else if(!_loc11_.indexOf("Free"))
            {
               _loc16_ = uint(_loc17_.frame);
            }
            else if(!_loc11_.indexOf("RunEnd"))
            {
               if(!_loc9_)
               {
                  _loc9_ = new Vector.<uint>();
               }
               _loc9_.push(_loc17_.frame);
            }
            else
            {
               if(_loc10_)
               {
                  _loc6_.method_856(_loc10_,_loc7_,_loc12_,_loc15_,_loc13_,_loc14_,_loc16_,_loc9_,param4);
               }
               _loc10_ = _loc11_;
               _loc12_ = uint(_loc17_.frame);
               _loc13_ = 0;
               _loc14_ = 0;
               _loc15_ = 0;
               _loc16_ = 0;
               _loc9_ = null;
            }
         }
         _loc6_.method_856(_loc10_,_loc7_,_loc12_,_loc15_,_loc13_,_loc14_,_loc16_,_loc9_,param4);
         return _loc6_;
      }
      
      public function method_2099() : void
      {
         this.var_1 = null;
      }
   }
}
