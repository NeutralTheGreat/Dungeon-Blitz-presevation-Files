package
{
   public class class_140
   {
       
      
      internal var powerNodeTypeID:uint;
      
      internal var modValue:Vector.<Number>;
      
      public function class_140(param1:uint, param2:Vector.<Number>)
      {
         super();
         this.powerNodeTypeID = param1;
         this.modValue = param2;
      }
      
      public function GetValueByProp(param1:String, param2:String) : Number
      {
         var _loc4_:class_38 = null;
         var _loc5_:Array = null;
         var _loc6_:int = 0;
         var _loc7_:String = null;
         var _loc3_:class_17 = class_14.var_872[this.powerNodeTypeID];
         if(_loc3_.var_660.hasOwnProperty(param1))
         {
            _loc5_ = (_loc4_ = _loc3_.var_660[param1]).mOrder;
            _loc6_ = 0;
            while(_loc6_ < _loc5_.length)
            {
               _loc7_ = String(_loc5_[_loc6_]);
               if(param2 == _loc7_ && _loc6_ < this.modValue.length)
               {
                  return this.modValue[_loc6_];
               }
               _loc6_++;
            }
         }
         return 0;
      }
   }
}
