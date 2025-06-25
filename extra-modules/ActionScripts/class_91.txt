package
{
   import flash.net.FileReference;
   import flash.utils.Dictionary;
   
   public class class_91
   {
      
      public static const const_1123:uint = 5000;
      
      public static const const_863:uint = 5000;
       
      
      public var var_1:Game;
      
      public var var_669:Vector.<class_142>;
      
      public var var_97:class_142;
      
      public var var_1615:Dictionary;
      
      public function class_91(param1:Game)
      {
         super();
         this.var_1 = param1;
         this.var_669 = new Vector.<class_142>();
      }
      
      public function method_973() : void
      {
         if(this.var_97)
         {
            this.var_97.method_327();
         }
         this.var_97 = new class_142(this.var_1,this.var_1.clientEnt);
         this.var_669.push(this.var_97);
      }
      
      public function method_1855() : void
      {
         if(this.var_97)
         {
            this.var_97.method_327();
         }
         this.method_1225();
      }
      
      public function method_81() : void
      {
         if(this.var_97)
         {
            this.var_97.method_81();
         }
      }
      
      public function method_142(param1:Entity, param2:PowerType, param3:int, param4:Boolean = false, param5:int = 0) : void
      {
         this.method_81();
         if(Boolean(param2) && param2.powerID == 0)
         {
            param2 = null;
         }
         if(this.var_97)
         {
            this.var_97.method_142(param1,param2,param3,param4,param5);
         }
      }
      
      public function method_499(param1:Entity, param2:PowerType) : void
      {
         this.method_81();
         if(this.var_97)
         {
            this.var_97.method_499(param1,param2);
         }
      }
      
      public function method_175(param1:PowerType, param2:Entity, param3:Entity, param4:int, param5:Boolean = true, param6:Boolean = true) : void
      {
         this.method_81();
         if(this.var_97)
         {
            this.var_97.method_175(param1,param2,param3,param4,param5,param6);
         }
      }
      
      public function method_410(param1:PowerType, param2:Entity, param3:Entity) : void
      {
         this.method_81();
         if(this.var_97)
         {
            this.var_97.method_410(param1,param2,param3);
         }
      }
      
      public function method_1108() : void
      {
         if(this.var_97)
         {
            this.var_97.method_513();
         }
      }
      
      public function method_2079() : void
      {
         var _loc1_:FileReference = new FileReference();
         var _loc2_:* = new Date().toLocaleString();
         var _loc3_:RegExp = /:/g;
         _loc2_ = _loc2_.replace(_loc3_,"-");
         _loc2_ = "Dungeon Blitz Playtest Metrics " + _loc2_ + ".txt";
         _loc1_.save(this.method_1895(),_loc2_);
      }
      
      private function method_1895() : String
      {
         var _loc3_:class_142 = null;
         var _loc4_:class_157 = null;
         this.var_1615 = new Dictionary();
         var _loc1_:* = new String();
         var _loc2_:* = new String();
         _loc1_ += "Summary Data by MasterClass: \r\n------------------\r\n\r\n";
         _loc2_ += "Individual Session Data: \r\n------------------\r\n\r\n";
         for each(_loc3_ in this.var_669)
         {
            this.method_1754(_loc3_);
            _loc2_ += _loc3_.method_1659() + "\r\n------------------\r\n\r\n";
         }
         for each(_loc4_ in this.var_1615)
         {
            _loc1_ += _loc4_.method_1719();
         }
         _loc1_ += "\r\n------------------\r\n\r\n";
         return _loc1_ + _loc2_;
      }
      
      private function method_2037() : String
      {
         if(this.var_97)
         {
            this.var_97.method_327();
         }
         var _loc1_:class_142 = !!this.var_97 ? this.var_97 : (this.var_669.length > 0 ? this.var_669[this.var_669.length - 1] : null);
         var _loc2_:String = null;
         if(_loc1_)
         {
            _loc2_ = _loc1_.method_1451();
         }
         return _loc2_;
      }
      
      public function method_1225() : void
      {
         var _loc2_:Packet = null;
         if(!this.var_1.CanSendPacket())
         {
            return;
         }
         var _loc1_:class_142 = null;
         if(this.var_97)
         {
            _loc1_ = this.var_97;
         }
         else if(this.var_669.length > 0)
         {
            this.var_669[this.var_669.length - 1];
         }
         if(_loc1_)
         {
            if(_loc1_.var_2733 && this.var_1.mTimeThisTick - _loc1_.var_904 >= const_863 && _loc1_.var_476 > 0)
            {
               this.var_97.method_327();
               _loc2_ = new Packet(LinkUpdater.const_1208);
               _loc1_.method_479(_loc2_);
               this.var_1.serverConn.SendPacket(_loc2_);
            }
         }
      }
      
      private function method_1754(param1:class_142) : void
      {
         if(!param1 || !param1.var_481)
         {
            return;
         }
         if(!this.var_1615[param1.var_481])
         {
            this.var_1615[param1.var_481] = new class_157(this.var_1,param1.var_481);
         }
         var _loc2_:class_157 = this.var_1615[param1.var_481];
         _loc2_.method_1925(param1);
      }
      
      public function method_548(param1:uint, param2:uint, param3:uint, param4:uint, param5:uint, param6:uint, param7:uint, param8:uint) : void
      {
         if(this.var_97)
         {
            this.var_97.method_548(param1,param2,param3,param4,param5,param6,param7,param8);
         }
      }
   }
}
