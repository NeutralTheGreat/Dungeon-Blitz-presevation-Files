package
{
   import flash.display.DisplayObject;
   import flash.display.LoaderInfo;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.filters.GlowFilter;
   import flash.system.ApplicationDomain;
   import flash.utils.Dictionary;
   import flash.utils.getQualifiedClassName;
   
   public class class_88 extends class_32
   {
      
      public static const const_269:uint = 7;
      
      private static const const_904:GlowFilter = new GlowFilter(5592473,1,6,6,1.8,2);
      
      private static const const_1071:GlowFilter = new GlowFilter(16777215,1,10,10,1.8,2);
       
      
      internal var var_980:String;
      
      internal var var_1195:int;
      
      internal var var_2541:class_33;
      
      internal var var_2119:Vector.<class_33>;
      
      internal var var_685:Vector.<MovieClip>;
      
      internal var var_886:Dictionary;
      
      public function class_88(param1:Game)
      {
         super(param1,"a_HouseSwap",null);
         var_45 = "FadeIn";
         var_15 = true;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc6_:Class = null;
         var _loc7_:Sprite = null;
         var _loc8_:DisplayObject = null;
         var _loc9_:String = null;
         var _loc10_:String = null;
         var _loc11_:String = null;
         var _loc12_:Array = null;
         var _loc13_:Vector.<String> = null;
         var _loc14_:int = 0;
         this.var_2119 = new Vector.<class_33>(const_269,true);
         this.var_685 = new Vector.<MovieClip>(const_269,true);
         var _loc2_:uint = 0;
         while(_loc2_ < const_269)
         {
            this.var_685[_loc2_] = var_2["am_Swap" + (_loc2_ + 1)];
            this.var_2119[_loc2_] = method_3(this.var_685[_loc2_],_loc2_,this.method_1150,this.method_1468,this.method_1920);
            _loc2_++;
         }
         this.var_2541 = method_10(var_2.am_BuyButton,this.method_1820);
         this.var_886 = new Dictionary();
         var _loc3_:String = "a_AllSwapsWrapper";
         var _loc5_:ApplicationDomain;
         var _loc4_:LoaderInfo;
         if((_loc5_ = (_loc4_ = ResourceManager.const_40[var_1.level.levelFileName]).applicationDomain).hasDefinition(_loc3_))
         {
            _loc7_ = new (_loc6_ = _loc5_.getDefinition(_loc3_) as Class)();
            _loc14_ = 0;
            while(_loc14_ < _loc7_.numChildren)
            {
               _loc8_ = _loc7_.getChildAt(_loc14_);
               if((_loc12_ = (_loc9_ = getQualifiedClassName(_loc8_)).split("_")).length > 3 && _loc12_[1] == "Swap")
               {
                  _loc10_ = String(_loc12_[2]);
                  _loc11_ = String(_loc12_[3]);
                  if(!(_loc13_ = this.var_886[_loc10_]))
                  {
                     _loc13_ = new Vector.<String>();
                     this.var_886[_loc10_] = _loc13_;
                  }
                  _loc13_.push(_loc11_);
               }
               _loc14_++;
            }
            this.method_740(this.var_886[this.var_980]);
         }
      }
      
      public function method_740(param1:Vector.<String>) : void
      {
         var _loc5_:int = 0;
         while(_loc5_ < const_269)
         {
            if(Boolean(param1) && _loc5_ < param1.length)
            {
               this.method_899(this.var_685[_loc5_],param1[_loc5_],"1000");
            }
            else
            {
               this.method_899(this.var_685[_loc5_],"","");
            }
            _loc5_++;
         }
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_2541 = null;
         this.var_2119 = null;
         this.var_980 = null;
         this.var_886 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
      }
      
      public function OnInitDisplay() : void
      {
         this.method_651();
         this.method_740(this.var_886[this.var_980]);
         this.var_1195 = -1;
         Refresh();
      }
      
      public function method_899(param1:MovieClip, param2:String, param3:String) : void
      {
         MathUtil.method_2(param1.am_Name,param2);
         MathUtil.method_2(param1.am_Cost,param3);
      }
      
      private function method_1468(param1:MouseEvent, param2:uint) : void
      {
         if(param2 != this.var_1195)
         {
            this.var_685[param2].filters = [const_904];
         }
      }
      
      private function method_1920(param1:MouseEvent, param2:uint) : void
      {
         if(param2 != this.var_1195)
         {
            this.var_685[param2].filters = [];
         }
      }
      
      private function method_1150(param1:MouseEvent, param2:uint) : void
      {
         this.method_651();
         this.var_1195 = param2;
         this.var_685[param2].filters = [const_1071];
         Refresh();
      }
      
      private function method_651() : void
      {
         var _loc1_:int = 0;
         while(_loc1_ < const_269)
         {
            this.var_685[_loc1_].filters = [];
            _loc1_++;
         }
      }
      
      private function method_1820(param1:MouseEvent) : void
      {
         if(this.var_1195 == -1 || this.var_980 == null)
         {
            return;
         }
         var _loc2_:String = String(this.var_886[this.var_980][this.var_1195]);
         var_1.ChangeHouseArt(this.var_980,_loc2_);
         var_1.SetSwapCategory(null,null);
         Refresh();
      }
   }
}
