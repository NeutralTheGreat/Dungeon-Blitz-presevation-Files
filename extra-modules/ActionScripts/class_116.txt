package
{
   public class class_116
   {
      
      private static const const_1186:String = "While this event is in place all gold will be doubled world wide";
      
      private static const const_961:String = "While this event is in place all gear drops will be doubled world wide";
      
      private static const const_1009:String = "While this event is in place all material drops will be doubled world wide";
      
      private static const const_1212:String = "While this event is in place all XP gained will be doubled world wide";
      
      private static const const_1062:String = "While this event is in place all pet XP gained will be doubled world wide";
      
      internal static const const_1177:Array = ["a_NewsGoldIcon","Double Gold Event",const_1186,"http://www.dungeonblitz.com/",1387602000];
      
      internal static const const_980:Array = ["a_NewsGearIcon","Double Gear Event",const_961,"http://www.dungeonblitz.com/",1387602000];
      
      internal static const const_1011:Array = ["a_NewsMatsIcon","Double Material Event",const_1009,"http://www.dungeonblitz.com/",1387602000];
      
      internal static const const_1301:Array = ["a_NewsXPIcon","Double XP Event",const_1212,"http://www.dungeonblitz.com/",1387602000];
      
      internal static const const_926:Array = ["a_NewsPetXPIcon","Double Pet XP Event",const_1062,"http://www.dungeonblitz.com/",1387602000];
      
      internal static var var_911:Array = new Array();
      
      {
         var_911[1] = const_1177;
         var_911[2] = const_980;
         var_911[3] = const_1011;
         var_911[4] = const_1301;
         var_911[5] = const_926;
      }
      
      internal var var_1:Game;
      
      internal var var_2682:String;
      
      internal var mExternalURL:String;
      
      internal var var_1001:String;
      
      internal var mTooltip:String;
      
      internal var mTimeEnd:uint;
      
      public function class_116(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_690(param1:String, param2:String, param3:String, param4:String, param5:uint) : void
      {
         this.var_2682 = param1;
         this.mExternalURL = param2;
         this.var_1001 = param3;
         this.mTooltip = param4;
         this.mTimeEnd = param5;
      }
   }
}
