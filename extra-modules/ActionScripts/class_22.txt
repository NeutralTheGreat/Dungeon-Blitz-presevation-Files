package
{
   import flash.utils.Dictionary;
   
   public class class_22
   {
      
      public static const const_856:uint = 42;
       
      
      internal var mNodeID:uint;
      
      internal var var_548:String;
      
      public function class_22(param1:uint, param2:String)
      {
         super();
         this.mNodeID = param1;
         this.var_548 = param2;
      }
      
      public static function method_1160(param1:String, param2:String) : int
      {
         var _loc5_:int = 0;
         var _loc6_:class_22 = null;
         var _loc3_:int = 0;
         var _loc4_:Vector.<class_22>;
         if(_loc4_ = class_14.var_368[param1])
         {
            _loc5_ = 0;
            while(_loc5_ < _loc4_.length)
            {
               if((_loc6_ = _loc4_[_loc5_]).var_548.indexOf(param2) > -1)
               {
                  _loc3_ += class_14.var_274[_loc6_.var_548].statValue;
               }
               _loc5_++;
            }
         }
         return _loc3_;
      }
      
      public static function method_30(param1:XML) : void
      {
         class_22.method_18(param1,class_14.var_368);
      }
      
      public static function method_18(param1:XML, param2:Dictionary) : void
      {
         var _loc4_:XML = null;
         var _loc5_:uint = 0;
         var _loc6_:XML = null;
         var _loc7_:String = null;
         var _loc8_:String = null;
         var _loc9_:Vector.<class_22> = null;
         var _loc10_:class_22 = null;
         var _loc3_:uint = uint(const_856 + 1);
         param2["templar"] = new Vector.<class_22>(_loc3_,true);
         param2["justicar"] = new Vector.<class_22>(_loc3_,true);
         param2["sentinel"] = new Vector.<class_22>(_loc3_,true);
         param2["flameseer"] = new Vector.<class_22>(_loc3_,true);
         param2["frostwarden"] = new Vector.<class_22>(_loc3_,true);
         param2["necromancer"] = new Vector.<class_22>(_loc3_,true);
         param2["shadowwalker"] = new Vector.<class_22>(_loc3_,true);
         param2["executioner"] = new Vector.<class_22>(_loc3_,true);
         param2["soulthief"] = new Vector.<class_22>(_loc3_,true);
         for each(_loc4_ in param1.*)
         {
            _loc5_ = uint(_loc4_.attribute("NodeID"));
            for each(_loc6_ in _loc4_.*)
            {
               _loc7_ = String(_loc6_.name().toString());
               _loc8_ = _loc6_.toString();
               _loc9_ = param2[_loc7_.toLowerCase()];
               _loc10_ = new class_22(_loc5_,_loc8_);
               _loc9_[_loc5_] = _loc10_;
            }
         }
      }
   }
}
