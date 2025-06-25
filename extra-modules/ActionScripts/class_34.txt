package
{
   import flash.display.Loader;
   import flash.events.Event;
   import flash.events.HTTPStatusEvent;
   import flash.events.IOErrorEvent;
   import flash.events.ProgressEvent;
   import flash.events.SecurityErrorEvent;
   import flash.net.URLLoader;
   import flash.net.URLLoaderDataFormat;
   import flash.system.ApplicationDomain;
   import flash.system.LoaderContext;
   import flash.utils.ByteArray;
   import flash.utils.getTimer;
   
   public class class_34
   {
      
      public static const const_664:String = "XML";
      
      public static const const_288:String = "SWF";
      
      public static const const_338:String = "SWZ";
      
      public static const const_359:String = "PBJ";
      
      public static const const_792:String = "MISC";
       
      
      internal var fileName:String;
      
      internal var var_296:String;
      
      internal var var_1650:String;
      
      internal var var_2038:String;
      
      internal var var_1295:uint;
      
      internal var var_2945:uint;
      
      internal var var_1237:uint;
      
      internal var var_1649:uint;
      
      internal var startTime:uint;
      
      internal var var_1426:uint;
      
      internal var var_2939:uint;
      
      internal var var_192:Loader;
      
      internal var var_182:URLLoader;
      
      internal var var_1473:uint;
      
      internal var var_828:uint = 1;
      
      public function class_34(param1:String, param2:uint, param3:String)
      {
         super();
         this.fileName = param1;
         this.var_2945 = param2;
         this.var_1295 = param2;
         this.var_1650 = param3;
         if(param2 >= 524288)
         {
            this.var_1237 = 3;
         }
         else if(param2 >= 262144)
         {
            this.var_1237 = 2;
         }
         else
         {
            this.var_1237 = 1;
         }
         var _loc4_:String;
         if((_loc4_ = this.fileName.substr(-3,3).toUpperCase()) == const_288)
         {
            this.var_296 = const_288;
         }
         else if(_loc4_ == const_338)
         {
            this.var_296 = const_338;
         }
         else if(_loc4_ == const_664)
         {
            this.var_296 = const_664;
         }
         else if(_loc4_ == const_359)
         {
            this.var_296 = const_359;
         }
         else
         {
            this.var_296 = const_792;
         }
         var _loc5_:Array = this.fileName.split("/");
         var _loc6_:String;
         var _loc7_:Array = !!(_loc6_ = String(_loc5_[_loc5_.length - 1])) ? _loc6_.split(".") : ["Unknown"];
         this.var_2038 = _loc7_[0];
      }
      
      public function method_336() : void
      {
         if(this.var_182)
         {
            try
            {
               this.var_182.close();
            }
            catch(e:Error)
            {
            }
            this.var_182.removeEventListener(HTTPStatusEvent.HTTP_STATUS,this.method_301);
            this.var_182.removeEventListener(IOErrorEvent.IO_ERROR,this.method_152);
            this.var_182.removeEventListener(ProgressEvent.PROGRESS,this.method_283);
            this.var_182.removeEventListener(SecurityErrorEvent.SECURITY_ERROR,this.method_152);
            this.var_182.removeEventListener(Event.COMPLETE,this.method_386);
            this.var_182 = null;
         }
         else if(this.var_192)
         {
            try
            {
               this.var_192.close();
            }
            catch(e:Error)
            {
            }
            this.var_192.contentLoaderInfo.removeEventListener(HTTPStatusEvent.HTTP_STATUS,this.method_301);
            this.var_192.contentLoaderInfo.removeEventListener(IOErrorEvent.IO_ERROR,this.method_152);
            this.var_192.contentLoaderInfo.removeEventListener(ProgressEvent.PROGRESS,this.method_283);
            this.var_192.contentLoaderInfo.removeEventListener(SecurityErrorEvent.SECURITY_ERROR,this.method_152);
            this.var_192.contentLoaderInfo.removeEventListener(Event.COMPLETE,this.method_386);
            this.var_192 = null;
         }
         ++this.var_1473;
         this.var_828 = ResourceManager.const_812;
      }
      
      public function method_335() : void
      {
         var _loc1_:ApplicationDomain = null;
         var _loc2_:LoaderContext = null;
         this.var_1426 = this.startTime = getTimer();
         this.var_828 = ResourceManager.const_774;
         if(this.var_296 == const_288)
         {
            this.var_192 = new Loader();
            this.var_192.contentLoaderInfo.addEventListener(HTTPStatusEvent.HTTP_STATUS,this.method_301);
            this.var_192.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR,this.method_152);
            this.var_192.contentLoaderInfo.addEventListener(ProgressEvent.PROGRESS,this.method_283);
            this.var_192.contentLoaderInfo.addEventListener(SecurityErrorEvent.SECURITY_ERROR,this.method_152);
            this.var_192.contentLoaderInfo.addEventListener(Event.COMPLETE,this.method_386);
            if(this.var_1650 == "Lib" || this.var_1650 == "Core" || this.var_1650 == ResourceManager.const_192)
            {
               _loc1_ = ApplicationDomain.currentDomain;
            }
            else
            {
               _loc1_ = new ApplicationDomain(ApplicationDomain.currentDomain);
            }
            _loc2_ = new LoaderContext(false,_loc1_);
            this.var_192.load(ResourceManager.method_466(this.fileName,this.var_1473),_loc2_);
         }
         else
         {
            this.var_182 = new URLLoader();
            if(this.var_296 == const_338 || this.var_296 == const_359)
            {
               this.var_182.dataFormat = URLLoaderDataFormat.BINARY;
            }
            this.var_182.addEventListener(HTTPStatusEvent.HTTP_STATUS,this.method_301);
            this.var_182.addEventListener(IOErrorEvent.IO_ERROR,this.method_152);
            this.var_182.addEventListener(ProgressEvent.PROGRESS,this.method_283);
            this.var_182.addEventListener(SecurityErrorEvent.SECURITY_ERROR,this.method_152);
            this.var_182.addEventListener(Event.COMPLETE,this.method_386);
            this.var_182.load(ResourceManager.method_466(this.fileName,this.var_1473));
         }
      }
      
      public function method_1280() : ByteArray
      {
         return this.var_182.data as ByteArray;
      }
      
      public function method_515() : XML
      {
         return new XML(this.var_182.data);
      }
      
      private function method_386(param1:Event) : void
      {
         this.var_828 = ResourceManager.const_416;
      }
      
      private function method_301(param1:HTTPStatusEvent) : void
      {
         this.var_2939 = param1.status;
      }
      
      private function method_283(param1:ProgressEvent) : void
      {
         ResourceManager.var_1575 -= this.var_1649;
         ResourceManager.var_777 -= this.var_1295;
         this.var_1295 = param1.bytesTotal;
         this.var_1649 = param1.bytesLoaded;
         ResourceManager.var_1575 += this.var_1649;
         ResourceManager.var_777 += this.var_1295;
         this.var_1426 = getTimer();
      }
      
      private function method_152(param1:Event) : void
      {
         this.var_1426 = getTimer();
         this.var_828 = ResourceManager.const_639;
      }
   }
}
