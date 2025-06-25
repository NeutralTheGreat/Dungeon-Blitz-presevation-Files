package
{
   import flash.display.DisplayObject;
   import flash.display.LoaderInfo;
   import flash.display.MovieClip;
   import flash.display.Stage;
   import flash.net.URLRequest;
   import flash.system.Security;
   import flash.utils.ByteArray;
   import flash.utils.Dictionary;
   import flash.utils.getTimer;
   
   public class ResourceManager
   {
      
      private static var var_1405:Vector.<class_34> = new Vector.<class_34>();
      
      private static var var_1820:Dictionary = new Dictionary();
      
      public static const const_40:Dictionary = new Dictionary();
      
      private static const const_477:Dictionary = new Dictionary();
      
      private static var var_1352:String;
      
      private static var var_1132:Dictionary = new Dictionary();
      
      private static var var_1896:Dictionary = new Dictionary();
      
      private static const const_627:Dictionary = new Dictionary();
      
      private static var var_747:uint;
      
      public static var var_1542:class_34;
      
      private static var var_504:Vector.<String>;
      
      private static var var_2264:uint;
      
      public static var var_777:uint;
      
      public static var var_1575:uint;
      
      private static var var_882:uint;
      
      private static const const_1253:uint = 6;
      
      private static var var_1289:uint;
      
      private static var var_1131:Vector.<uint>;
      
      private static var var_1372:Vector.<uint>;
      
      private static var var_2011:Vector.<Function>;
      
      private static var var_1681:Vector.<class_34>;
      
      public static const const_812:uint = 1;
      
      public static const const_774:uint = 2;
      
      public static const const_416:uint = 3;
      
      public static const const_622:uint = 4;
      
      public static const const_639:uint = 5;
      
      private static const const_565:String = "masterFileList.xml";
      
      private static const const_496:String = "devSettings.xml";
      
      public static const const_192:String = "Required";
      
      public static const const_512:String = "Init";
      
      public static var var_547:uint = 0;
      
      private static const const_954:uint = 10000;
      
      private static const const_886:uint = 30000;
      
      private static const const_1293:uint = 5000;
      
      private static const const_960:uint = 5000;
       
      
      public function ResourceManager()
      {
         super();
      }
      
      public static function method_125(param1:Array) : void
      {
         var _loc2_:String = null;
         var_504 = new Vector.<String>();
         var_504.push(const_192);
         var_504.push(const_512);
         for each(_loc2_ in param1)
         {
            var_504.push(_loc2_);
         }
         var_504.fixed = true;
         var_2264 = var_504.length;
      }
      
      public static function method_41(param1:String, param2:Function) : void
      {
         const_477[param1] = param2;
      }
      
      public static function method_2102(param1:String, param2:Function) : void
      {
         const_627[param1] = param2;
      }
      
      public static function method_497(param1:String) : void
      {
         var_747 = var_504.indexOf(param1);
      }
      
      public static function method_149(param1:String) : Boolean
      {
         var _loc2_:int = var_504.indexOf(param1);
         return var_747 > _loc2_;
      }
      
      public static function method_2011(param1:String) : void
      {
         var _loc2_:class_34 = null;
         for each(_loc2_ in var_1405)
         {
            if(_loc2_.var_296 == param1 || _loc2_.fileName == param1)
            {
               if(_loc2_.var_296 == class_34.const_288)
               {
                  _loc2_.var_192.unload();
                  const_40[_loc2_.fileName] = null;
               }
               _loc2_.method_336();
            }
         }
      }
      
      private static function method_776(param1:class_34) : void
      {
         var _loc3_:XML = null;
         var _loc4_:String = null;
         var _loc5_:String = null;
         var _loc6_:String = null;
         var _loc7_:String = null;
         var _loc8_:String = null;
         var _loc9_:uint = 0;
         var _loc2_:XML = param1.method_515();
         for each(_loc3_ in _loc2_.*)
         {
            _loc4_ = String(_loc3_.name());
            _loc5_ = _loc3_.attribute("Name");
            _loc6_ = _loc3_.attribute("Version");
            _loc7_ = _loc3_.attribute("Stage");
            _loc8_ = _loc3_.attribute("Size");
            _loc9_ = uint(_loc8_) * 1024;
            var_1896[_loc5_] = _loc9_;
            var_1132[_loc5_] = _loc6_;
            if(_loc4_ != "Level")
            {
               method_143(_loc5_,_loc7_);
            }
            else if(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT)
            {
               method_143(_loc5_,"Level");
            }
         }
      }
      
      private static function method_854(param1:class_34) : void
      {
         var _loc2_:LoaderInfo = param1.var_192.contentLoaderInfo;
         var _loc3_:MovieClip = _loc2_.content as MovieClip;
         _loc3_.gotoAndStop(1);
         if(_loc3_.numChildren)
         {
            class_24.method_7("Imported Swfs cannot have any children on the stage, change the layer to a guide: " + param1.fileName);
         }
         const_40[param1.fileName] = _loc2_;
      }
      
      private static function method_654(param1:class_34) : void
      {
         var _loc6_:ByteArray = null;
         var _loc7_:uint = 0;
         var _loc8_:uint = 0;
         var _loc9_:XML = null;
         var _loc10_:String = null;
         var _loc11_:Function = null;
         var _loc12_:uint = 0;
         var _loc13_:uint = 0;
         var _loc2_:ByteArray = param1.method_1280();
         var _loc3_:uint = uint(_loc2_.readInt());
         var _loc4_:uint = uint(_loc2_.readInt());
         var _loc5_:uint = 0;
         while(_loc5_ < _loc4_)
         {
            _loc6_ = new ByteArray();
            _loc7_ = uint(_loc2_.readInt());
            _loc6_.length = _loc7_;
            _loc8_ = 0;
            while(_loc8_ < _loc7_)
            {
               _loc12_ = uint(_loc8_ & 7);
               _loc13_ = _loc2_.readUnsignedByte();
               _loc6_[_loc8_] = _loc13_ ^ _loc3_ & 255;
               _loc3_ = uint(_loc3_ << 32 - _loc12_ | _loc3_ >>> _loc12_);
               _loc8_++;
            }
            _loc6_.uncompress();
            _loc10_ = String((_loc9_ = new XML(_loc6_)).name().toString());
            if((_loc11_ = const_477[_loc10_]) == null)
            {
               class_24.method_7("Unknown XML type, all handlers must be registered before loading begins: " + param1.fileName);
            }
            _loc11_(_loc9_);
            _loc5_++;
         }
      }
      
      private static function method_969(param1:class_34) : void
      {
         var _loc2_:XML = param1.method_515();
         var _loc3_:String = String(_loc2_.name().toString());
         var _loc4_:Function;
         if((_loc4_ = const_477[_loc3_]) == null)
         {
            class_24.method_7("Unknown XML type, all handlers must be registered before loading begins: " + param1.fileName);
         }
         _loc4_(_loc2_);
      }
      
      private static function method_675(param1:class_34) : void
      {
         var _loc2_:Function = const_627[param1.var_2038];
         if(_loc2_ == null)
         {
            class_24.method_7("Unknown Miscellaneous File, all handlers must be registered before loading begins: " + param1.fileName);
         }
         _loc2_(param1);
      }
      
      public static function method_466(param1:String, param2:uint = 0) : URLRequest
      {
         var _loc3_:String = param1;
         if(param2)
         {
            _loc3_ += "?v=" + param2;
         }
         var _loc4_:String;
         if(!(_loc4_ = var_1352))
         {
            return new URLRequest(_loc3_);
         }
         var _loc5_:String;
         if(_loc5_ = String(var_1132[param1]))
         {
            _loc4_ += _loc5_ + "/";
         }
         return new URLRequest(_loc4_ + _loc3_);
      }
      
      public static function method_783() : void
      {
         var _loc1_:uint = 0;
         var _loc5_:class_34 = null;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc8_:class_34 = null;
         var _loc9_:uint = 0;
         var _loc10_:uint = 0;
         var _loc11_:uint = 0;
         var _loc12_:uint = 0;
         if(var_1289)
         {
            _loc6_ = uint(getTimer());
            _loc7_ = 0;
            while(_loc7_ < var_1289)
            {
               if((_loc8_ = var_1681[_loc7_]).var_828 == const_416)
               {
                  _loc9_ = var_1372[_loc7_];
                  if((_loc10_ = uint(_loc8_.method_515())) != _loc9_)
                  {
                     if(_loc9_)
                     {
                        var_2011[_loc7_]();
                     }
                     var_1372[_loc7_] = _loc10_;
                  }
                  var_1131[_loc7_] = _loc6_;
                  _loc8_.var_828 = const_622;
               }
               else if(_loc6_ - var_1131[_loc7_] >= 1000)
               {
                  _loc8_.method_336();
                  _loc8_.method_335();
                  var_1131[_loc7_] = _loc6_;
               }
               _loc7_++;
            }
         }
         if(var_747 >= var_2264 || Boolean(var_1542))
         {
            return;
         }
         var _loc2_:uint = uint(getTimer());
         var _loc3_:Boolean = true;
         var _loc4_:String = var_504[var_747];
         for each(_loc5_ in var_1405)
         {
            if(_loc5_.var_1650 == _loc4_)
            {
               _loc1_ = _loc5_.var_828;
               if(_loc1_ == const_812)
               {
                  if(var_882 + _loc5_.var_1237 <= const_1253)
                  {
                     _loc5_.method_335();
                     var_882 += _loc5_.var_1237;
                  }
                  _loc3_ = false;
               }
               else if(_loc1_ == const_774)
               {
                  _loc12_ = (_loc11_ = !!_loc5_.var_1649 ? const_886 : const_954) + const_1293 * _loc5_.var_1473;
                  if(_loc2_ - _loc5_.var_1426 >= _loc12_)
                  {
                     ++var_547;
                     _loc5_.method_336();
                     _loc5_.method_335();
                  }
                  _loc3_ = false;
               }
               else if(_loc1_ == const_639)
               {
                  if(_loc2_ - _loc5_.var_1426 >= const_960)
                  {
                     ++var_547;
                     _loc5_.method_336();
                     _loc5_.method_335();
                  }
                  _loc3_ = false;
               }
               else if(_loc1_ == const_416)
               {
                  method_762(_loc5_);
                  _loc5_.var_828 = const_622;
                  var_882 -= _loc5_.var_1237;
                  _loc3_ = false;
               }
            }
         }
         if(_loc3_)
         {
            ++var_747;
         }
      }
      
      public static function method_762(param1:class_34) : void
      {
         var currResource:class_34 = param1;
         try
         {
            method_873(currResource);
         }
         catch(e:Error)
         {
            var_1542 = currResource;
         }
      }
      
      public static function method_873(param1:class_34) : void
      {
         if(param1.fileName == const_565)
         {
            method_776(param1);
         }
         else if(param1.fileName == const_496)
         {
            DevSettings.method_1539(param1);
         }
         else if(param1.var_296 == class_34.const_288)
         {
            method_854(param1);
         }
         else if(param1.var_296 == class_34.const_338)
         {
            method_654(param1);
         }
         else if(param1.var_296 == class_34.const_792 || param1.var_296 == class_34.const_359)
         {
            method_675(param1);
         }
         else if(DevSettings.flags)
         {
            method_969(param1);
         }
      }
      
      public static function method_471(param1:String) : class_34
      {
         return var_1820[param1];
      }
      
      public static function method_143(param1:String, param2:String) : void
      {
         if(method_471(param1))
         {
            return;
         }
         var _loc3_:uint = uint(var_1896[param1]);
         if(!_loc3_)
         {
            _loc3_ = 4096;
         }
         var _loc4_:class_34 = new class_34(param1,_loc3_,param2);
         var_1405.push(_loc4_);
         var_1820[param1] = _loc4_;
         var_777 += _loc4_.var_1295;
      }
      
      public static function method_1913(param1:String, param2:String) : void
      {
         var_1132[const_496] = param1;
         var_1132[const_565] = param1;
         var_1352 = param2;
         method_497(const_192);
         method_143(const_565,const_192);
         if(DevSettings.flags & DevSettings.DEVFLAG_ADDXMLDEVSETTINGS)
         {
            method_143(const_496,const_192);
         }
      }
      
      public static function method_2027(param1:String) : void
      {
         var_1352 = param1;
      }
      
      public static function method_2122(param1:String, param2:Function) : void
      {
         if(!var_1289)
         {
            var_1131 = new Vector.<uint>();
            var_1372 = new Vector.<uint>();
            var_2011 = new Vector.<Function>();
            var_1681 = new Vector.<class_34>();
         }
         var_1681.push(new class_34(param1,1,"None"));
         var_2011.push(param2);
         var_1131.push(0);
         var_1372.push(0);
         ++var_1289;
      }
      
      public static function method_1544(param1:Stage, param2:String, param3:String, param4:String) : String
      {
         var _loc5_:String;
         if(!(_loc5_ = param1.loaderInfo.url).indexOf("http://" + param2) || !_loc5_.indexOf("http://" + param3))
         {
            Security.allowDomain("http://" + param2);
            Security.allowDomain("http://" + param3);
            return "http://" + param3 + param4;
         }
         if(!_loc5_.indexOf("https://" + param2) || !_loc5_.indexOf("https://" + param3))
         {
            Security.allowDomain("https://" + param2);
            Security.allowDomain("https://" + param3);
            return "https://" + param3 + param4;
         }
         class_24.method_7("Failed to load the Swf");
         return null;
      }
      
      public static function method_1071(param1:DisplayObject) : String
      {
         var _loc2_:String = String(param1.loaderInfo.parameters.fv);
         if(!_loc2_)
         {
            class_24.method_7("Failed Swf loading");
         }
         return _loc2_;
      }
   }
}
