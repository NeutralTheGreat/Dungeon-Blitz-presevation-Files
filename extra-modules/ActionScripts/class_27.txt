package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.Sprite;
   
   public class class_27
   {
       
      
      internal var var_2004:class_26;
      
      internal var var_875:Vector.<Sprite>;
      
      internal var var_575:Vector.<Bitmap>;
      
      public function class_27(param1:class_26)
      {
         super();
         this.var_2004 = param1;
         this.var_575 = new Vector.<Bitmap>(this.var_2004.var_710,true);
         this.var_875 = new Vector.<Sprite>(this.var_2004.var_710,true);
      }
      
      public function method_2073() : void
      {
         this.method_742();
         this.method_647();
         this.var_2004 = null;
         this.var_875 = null;
         this.var_575 = null;
      }
      
      public function method_1490(param1:uint) : uint
      {
         var _loc2_:Bitmap = this.var_575[param1];
         if(!_loc2_)
         {
            return 0;
         }
         var _loc3_:BitmapData = _loc2_.bitmapData;
         var _loc4_:uint = uint(_loc3_.height * _loc3_.width);
         _loc3_.dispose();
         _loc2_.bitmapData = null;
         this.var_575[param1] = null;
         return _loc4_;
      }
      
      public function method_742() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc3_:Bitmap = null;
         _loc2_ = this.var_575.length;
         _loc1_ = 0;
         while(_loc1_ < _loc2_)
         {
            _loc3_ = this.var_575[_loc1_];
            if(_loc3_)
            {
               if(_loc3_.bitmapData)
               {
                  _loc3_.bitmapData.dispose();
                  _loc3_.bitmapData = null;
               }
               this.var_575[_loc1_] = null;
            }
            _loc1_++;
         }
      }
      
      public function method_647() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc3_:Sprite = null;
         _loc2_ = this.var_875.length;
         _loc1_ = 0;
         while(_loc1_ < _loc2_)
         {
            _loc3_ = this.var_875[_loc1_];
            if(_loc3_)
            {
               if(_loc3_.parent)
               {
                  _loc3_.parent.removeChild(_loc3_);
               }
               this.var_875[_loc1_] = null;
            }
            _loc1_++;
         }
      }
   }
}
