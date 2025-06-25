package
{
   import flash.utils.Dictionary;
   
   public class class_157
   {
       
      
      public var var_1:Game;
      
      public var mMasterClass:String;
      
      public var var_2267:uint = 0;
      
      public var var_143:uint = 0;
      
      public var var_2281:uint = 0;
      
      public var var_2396:Number = 0;
      
      public var var_2395:Number = 0;
      
      public var var_2221:Number = 0;
      
      public var var_2101:Number = 0;
      
      public var var_2037:Number = 0;
      
      public var var_2029:Number = 0;
      
      public var var_2220:Number = 0;
      
      public var var_2074:Number = 0;
      
      public var var_2161:Number = 0;
      
      public var var_2087:Number = 0;
      
      public var var_2315:Number = 0;
      
      public var var_2428:Number = 0;
      
      public var var_2239:Number = 0;
      
      public var var_2268:Number = 0;
      
      public var var_2338:Number = 0;
      
      public var var_2174:Number = 0;
      
      public var var_2299:Number = 0;
      
      public var var_1486:Dictionary;
      
      public var var_2862:int = 0;
      
      public function class_157(param1:Game, param2:String)
      {
         super();
         this.var_1 = param1;
         this.mMasterClass = param2;
         this.var_1486 = new Dictionary();
      }
      
      public function method_1925(param1:class_142) : void
      {
         if(param1.var_481 != this.mMasterClass)
         {
            return;
         }
         ++this.var_2862;
         var _loc2_:uint = this.var_143;
         var _loc3_:uint = param1.var_474;
         var _loc4_:uint = !!param1.var_483 ? param1.var_483 : this.var_1.mTimeThisTick;
         this.var_2267 += _loc4_ - param1.var_904;
         this.var_143 += _loc3_;
         if(Boolean(_loc3_) && Boolean(this.var_143))
         {
            this.var_2281 = (_loc2_ * this.var_2281 + _loc3_ * _loc3_) / this.var_143;
            this.var_2396 = (_loc2_ * this.var_2396 + _loc3_ * (1000 * (param1.var_952 + param1.var_1273) / param1.var_474 / param1.meleeDamage)) / this.var_143;
            this.var_2395 = (_loc2_ * this.var_2395 + _loc3_ * (1000 * (param1.var_476 + param1.var_880) / param1.var_474 / param1.meleeDamage)) / this.var_143;
            this.var_2221 = (_loc2_ * this.var_2221 + _loc3_ * param1.var_476) / this.var_143;
            this.var_2101 = (_loc2_ * this.var_2101 + _loc3_ * param1.var_952) / this.var_143;
            this.var_2037 += param1.var_476;
            this.var_2029 = (_loc2_ * this.var_2029 + _loc3_ * param1.var_688) / this.var_143;
            this.var_2220 = (_loc2_ * this.var_2220 + _loc3_ * param1.var_2892) / this.var_143;
            this.var_2074 = (_loc2_ * this.var_2074 + _loc3_ * param1.var_1294) / this.var_143;
            this.var_2161 = (_loc2_ * this.var_2161 + _loc3_ * param1.var_1087) / this.var_143;
            this.var_2087 = (_loc2_ * this.var_2087 + _loc3_ * param1.var_1517) / this.var_143;
            this.var_2315 = (_loc2_ * this.var_2315 + _loc3_ * param1.var_1532) / this.var_143;
            this.var_2428 = (_loc2_ * this.var_2428 + _loc3_ * param1.var_1578) / this.var_143;
            this.var_2239 = (_loc2_ * this.var_2239 + _loc3_ * param1.var_1338) / this.var_143;
            this.var_2268 = (_loc2_ * this.var_2268 + _loc3_ * param1.var_1512) / this.var_143;
            this.var_2338 = (_loc2_ * this.var_2338 + _loc3_ * param1.var_1300) / this.var_143;
            this.var_2174 = (_loc2_ * this.var_2174 + _loc3_ * param1.var_1224) / this.var_143;
            this.var_2299 = (_loc2_ * this.var_2299 + _loc3_ * param1.var_1245) / this.var_143;
         }
         this.method_1255(param1.var_222);
      }
      
      private function method_1255(param1:Dictionary) : void
      {
         var _loc2_:class_166 = null;
         var _loc3_:class_166 = null;
         for each(_loc2_ in param1)
         {
            if(!this.var_1486[_loc2_.var_1059])
            {
               this.var_1486[_loc2_.var_1059] = new class_166(_loc2_.var_1693);
            }
            _loc3_ = this.var_1486[_loc2_.var_1059];
            _loc3_.method_1734(_loc2_);
         }
      }
      
      public function method_1719() : String
      {
         var _loc2_:class_166 = null;
         var _loc1_:* = new String();
         _loc1_ += "Summary for " + this.mMasterClass + ": \r\n\r\n";
         _loc1_ += "totalPlaytime: " + this.var_2267.toString() + "\r\n";
         _loc1_ += "totalCombatTime: " + this.var_143 + "\r\n";
         _loc1_ += "avgCombatTime: " + this.var_2281 + "\r\n";
         _loc1_ += "avgBaseDPS: " + this.var_2396 + "\r\n";
         _loc1_ += "avgFinalDPS: " + this.var_2395 + "\r\n";
         _loc1_ += "avgDamageDealt: " + this.var_2221 + "\r\n";
         _loc1_ += "avgBaseDamageDealt: " + this.var_2101 + "\r\n";
         _loc1_ += "avgDamageReceived: " + this.var_2029 + "\r\n";
         _loc1_ += "avgDamageResisted: " + this.var_2220 + "\r\n";
         _loc1_ += "avgHealingDealt: " + this.var_2074 + "\r\n";
         _loc1_ += "avgHealingReceived: " + this.var_2161 + "\r\n";
         _loc1_ += "avgManaGain: " + this.var_2087 + "\r\n";
         _loc1_ += "avgManaSpent: " + this.var_2315 + "\r\n";
         _loc1_ += "avgManaWasted: " + this.var_2428 + "\r\n";
         _loc1_ += "avgMasterGain: " + this.var_2239 + "\r\n";
         _loc1_ += "avgMasterSpent: " + this.var_2268 + "\r\n";
         _loc1_ += "avgMasterWasted: " + this.var_2338 + "\r\n";
         _loc1_ += "avgKills: " + this.var_2174 + "\r\n";
         _loc1_ += "avgDeaths: " + this.var_2299 + "\r\n";
         _loc1_ += "\r\n\r\n\r\n";
         _loc1_ += "Power Use: \r\n\r\n";
         for each(_loc2_ in this.var_1486)
         {
            _loc1_ += _loc2_.var_1059 + ": \r\n";
            _loc1_ += "Times Used: " + _loc2_.var_322 + "\r\n";
            if(Boolean(_loc2_.var_563) || Boolean(_loc2_.var_236) || Boolean(_loc2_.var_201))
            {
               _loc1_ += "Total Kills: " + _loc2_.var_563 + "\r\n";
            }
            if(Boolean(_loc2_.var_236) || Boolean(_loc2_.var_201))
            {
               _loc1_ += "Average Damage: " + (_loc2_.var_236 + _loc2_.var_201) / _loc2_.var_322 + "\r\n";
            }
            if(Boolean(_loc2_.var_236) || Boolean(_loc2_.var_201))
            {
               _loc1_ += "% of total damage: " + 100 * (_loc2_.var_236 + _loc2_.var_201) / this.var_2037 + "\r\n";
            }
            if(Boolean(_loc2_.var_960) || Boolean(_loc2_.var_951))
            {
               _loc1_ += "Average Base Damage: " + (_loc2_.var_960 + _loc2_.var_951) / _loc2_.var_322 + "\r\n";
            }
            if(Boolean(_loc2_.var_550) || Boolean(_loc2_.var_201))
            {
               _loc1_ += "Average Healing: " + (_loc2_.var_550 + _loc2_.var_768) / _loc2_.var_322 + "\r\n";
            }
            if(_loc2_.var_814)
            {
               _loc1_ += "Mana Spent: " + _loc2_.var_814;
            }
            _loc1_ += "\r\n\r\n";
         }
         return _loc1_;
      }
   }
}
