package
{
   public class class_54 extends class_32
   {
       
      
      internal var var_725:uint;
      
      internal var var_2631:String;
      
      public function class_54(param1:Game)
      {
         super(param1,"a_GearFloaterMagic","am_Panel");
         var_15 = true;
         var_45 = "FadeIn";
         var_87 = "FadeOut";
         var_92 = 1500;
         var_112 = true;
         var_101 = false;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:Entity = var_1.clientEnt;
         var _loc2_:GearType = class_14.var_421[String(this.var_725) + this.var_2631];
         if(!_loc1_ || !_loc2_)
         {
            return;
         }
         MathUtil.method_2(var_2.am_Name,_loc2_.displayName);
         MathUtil.method_2(var_2.am_Type,"New " + GearType.method_395(_loc1_.entType.className,_loc2_.type));
         method_52(var_2.am_IconHolder,var_1.RenderGear(Game.const_95,_loc2_,1));
      }
      
      public function OnInitDisplay(param1:uint, param2:String) : void
      {
         this.var_725 = param1;
         this.var_2631 = param2;
      }
   }
}
