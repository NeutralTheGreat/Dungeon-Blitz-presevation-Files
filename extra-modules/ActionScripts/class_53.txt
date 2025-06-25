package
{
   import flash.events.IOErrorEvent;
   import flash.events.SecurityErrorEvent;
   import flash.net.URLLoader;
   import flash.net.URLRequest;
   import flash.net.URLRequestHeader;
   import flash.net.URLRequestMethod;
   
   public class class_53
   {
      
      private static const const_1080:String = "http://api.gameanalytics.com";
      
      private static const const_1035:String = "1";
      
      private static const const_215:Object = new Object();
      
      private static const const_249:Object = new Object();
      
      private static const const_147:Object = new Object();
      
      private static var var_1850:String;
      
      private static var var_2300:String;
       
      
      public function class_53()
      {
         super();
      }
      
      public static function method_125(param1:String, param2:String, param3:uint, param4:String) : void
      {
         var_1850 = param1;
         var_2300 = param2;
         var _loc5_:Date;
         var _loc6_:String = (_loc5_ = new Date()).time + "x" + uint(Math.random() * 1000000);
         const_215["session_id"] = const_249["session_id"] = const_147["session_id"] = _loc6_;
         const_215["user_id"] = const_249["user_id"] = const_147["user_id"] = param4;
         const_215["build"] = const_249["build"] = const_147["build"] = String(param3);
      }
      
      public static function method_79(param1:String, param2:uint) : void
      {
         const_215["event_id"] = param1;
         const_215["value"] = param2;
         method_207("design",const_215);
      }
      
      public static function method_524(param1:String) : void
      {
         const_249["event_id"] = param1;
         method_207("quality",const_249);
      }
      
      public static function method_721(param1:String, param2:uint, param3:String) : void
      {
         const_147["event_id"] = param1;
         const_147["amount"] = param2;
         const_147["currency"] = param3;
         method_207("business",const_147);
      }
      
      private static function method_207(param1:String, param2:Object) : void
      {
         if(!var_1850)
         {
            return;
         }
         var _loc3_:String = JSON.stringify(param2);
         var _loc4_:String = Crypto.MD5(_loc3_ + var_2300);
         var _loc5_:URLRequest;
         (_loc5_ = new URLRequest(const_1080 + "/" + const_1035 + "/" + var_1850 + "/" + param1)).data = _loc3_;
         _loc5_.method = URLRequestMethod.POST;
         _loc5_.requestHeaders = [new URLRequestHeader("Authorization",_loc4_)];
         var _loc6_:URLLoader;
         (_loc6_ = new URLLoader()).addEventListener(IOErrorEvent.IO_ERROR,method_1509);
         _loc6_.addEventListener(SecurityErrorEvent.SECURITY_ERROR,method_1063);
         _loc6_.load(_loc5_);
      }
      
      private static function method_1509(param1:IOErrorEvent) : void
      {
         class_24.method_19("GA-IOError: " + param1.text);
      }
      
      private static function method_1063(param1:SecurityErrorEvent) : void
      {
         class_24.method_19("GA-SecurityError: " + param1.text);
      }
   }
}
