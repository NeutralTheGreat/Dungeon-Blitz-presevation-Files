package
{
   import flash.media.Sound;
   import flash.media.SoundChannel;
   import flash.media.SoundTransform;
   
   public class class_149
   {
       
      
      internal var var_2705:uint;
      
      internal var var_2390:Number = 0;
      
      internal var var_1946:Number = 0;
      
      internal var var_1637:Sound;
      
      internal var var_739:SoundChannel;
      
      internal var var_2255:String;
      
      internal var var_2702:Number = 0;
      
      internal var var_919:Number = 0;
      
      internal var var_370:Number = 0;
      
      internal var var_825:SoundChannel;
      
      public function class_149(param1:uint, param2:Number, param3:Number)
      {
         super();
         this.var_2705 = param1;
         this.var_2390 = param2;
         this.var_1946 = param3;
      }
      
      public function method_487() : void
      {
         if(!this.var_739)
         {
            return;
         }
         if(!this.var_1946)
         {
            this.var_739.stop();
         }
         else
         {
            if(this.var_825)
            {
               this.var_825.stop();
            }
            this.var_825 = this.var_739;
         }
         this.var_1637 = null;
         this.var_739 = null;
      }
      
      public function method_816() : void
      {
         if(this.var_2255)
         {
            SoundManager.method_103(this.var_2705,this.var_2255,this.var_2702);
         }
      }
      
      public function method_1616() : void
      {
         var _loc1_:SoundTransform = null;
         var _loc2_:Number = NaN;
         if(this.var_919 < this.var_370 && this.var_739 && this.var_1637 && this.var_1637.bytesLoaded >= this.var_1637.bytesTotal)
         {
            this.var_919 += this.var_2390;
            if(this.var_919 > this.var_370)
            {
               this.var_919 = this.var_370;
            }
            this.var_739.soundTransform.volume = this.var_919 * this.var_370;
         }
         if(this.var_825)
         {
            _loc1_ = this.var_825.soundTransform;
            _loc2_ = _loc1_.volume - this.var_1946;
            if(_loc2_ <= this.var_1946)
            {
               this.var_825.stop();
               this.var_825 = null;
            }
            else
            {
               _loc1_.volume = _loc2_;
               this.var_825.soundTransform = _loc1_;
            }
         }
      }
   }
}
