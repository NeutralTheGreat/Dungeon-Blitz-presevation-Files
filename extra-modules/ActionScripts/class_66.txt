package
{
   import flash.utils.Dictionary;
   
   public class class_66
   {
      
      internal static const const_465:uint = 3;
      
      internal static const const_409:uint = 6;
      
      internal static const const_571:uint = 2;
      
      internal static const const_1412:uint = 1;
      
      internal static const const_1410:uint = 2;
      
      internal static const const_1420:uint = 3;
      
      internal static const const_76:Dictionary = new Dictionary();
      
      internal static const const_185:uint = 0;
      
      internal static const const_200:uint = 1;
      
      internal static const const_534:uint = 2;
      
      internal static const const_495:uint = 50;
      
      internal static const const_948:uint = 5;
      
      internal static const const_527:Array = [0,Game.const_181,7200,14400,21600,37800,54000,70200,86400,108000,129600,150750,171900,195750,219600,268500,317400,337500,357600,434850,512100,532575,553050,575175,597300,621200,645100,670900,696700,724575,752450,782550,812650,845150,877650,912750,947850,985775,1023700,1064650,1105600,1149825,1194050,1241800,1289550,1341125,1392700,1448400,1504100,1564275,1624450];
      
      internal static const const_553:Array = [0,0,2805,6300,11187,18009,27133,39230,55492,76352,103326,138087,182677,238420,309610,398435,508501,646504,817051,1028027,1287751,1608088,2000327,2479956,3067822,3781585,4084112,4410841,4763708,5144805,5556389,6000900,6480972,6999450,7559406,8164158,8817291,9522674,10284488,11107247,11995827,12955493,13991932,15111287,16320190,17625805,19035869,20558739,22203438,23979713,25898090];
      
      internal static const const_1002:Array = [0,0,2,4,6,10,14,20,28,37,41,45,51,59,68,80,95,113,122,132,145,161,181,193,204,219,225,231,238,246,254,263,273,283,291,299,308,318,329,340,352,366,380,396,412,431,450,471,494,519,545];
      
      {
         const_76["frostwarden"] = 1;
         const_76["sentinel"] = 1;
         const_76["executioner"] = 1;
         const_76["flameseer"] = 2;
         const_76["justicar"] = 2;
         const_76["shadowwalker"] = 2;
         const_76["necromancer"] = 3;
         const_76["templar"] = 3;
         const_76["soulthief"] = 3;
      }
      
      internal var var_1:Game;
      
      internal var var_403:Vector.<uint>;
      
      internal var mCurrentResearchIndex:uint = 0;
      
      internal var mEndtime:uint;
      
      internal var mStatus:uint;
      
      public function class_66(param1:Game, param2:uint = 0, param3:uint = 0, param4:uint = 0)
      {
         super();
         this.var_403 = new Vector.<uint>(const_465,true);
         this.var_403[0] = param2;
         this.var_403[1] = param3;
         this.var_403[2] = param4;
         this.var_1 = param1;
         this.mStatus = const_185;
         this.mEndtime = 0;
      }
      
      public static function method_251(param1:String) : uint
      {
         if(!const_76[param1])
         {
            return 0;
         }
         return const_76[param1];
      }
      
      public static function method_1210(param1:uint) : uint
      {
         return const_527[param1];
      }
      
      public static function method_2049(param1:uint) : uint
      {
         return const_553[param1];
      }
      
      public function method_995(param1:uint, param2:uint, param3:uint) : void
      {
         this.var_403[0] = param1;
         this.var_403[1] = param2;
         this.var_403[2] = param3;
      }
      
      public function method_1399() : void
      {
         this.var_403 = null;
         this.mCurrentResearchIndex = 0;
         this.mEndtime = 0;
         this.mStatus = 0;
      }
      
      public function GetPointsByIndex(param1:uint) : uint
      {
         if(param1 == 0 || param1 > const_465)
         {
            return 0;
         }
         return this.var_403[param1 - 1];
      }
      
      public function GetPointsByMC(param1:String) : uint
      {
         var _loc2_:uint = method_251(param1);
         return this.GetPointsByIndex(_loc2_);
      }
      
      public function SetCurrentResearch(param1:uint, param2:uint) : void
      {
         this.mCurrentResearchIndex = param1;
         this.mEndtime = param2;
         this.mStatus = const_185;
         if(Boolean(this.mCurrentResearchIndex) && Boolean(this.mEndtime))
         {
            this.mStatus = const_200;
         }
         if(Boolean(this.mCurrentResearchIndex) && !this.mEndtime)
         {
            this.mStatus = const_534;
         }
         if(!this.mCurrentResearchIndex && !this.mEndtime)
         {
            this.mStatus = const_185;
         }
      }
      
      public function GiveNewResearchPoint() : void
      {
         var _loc1_:uint = this.mCurrentResearchIndex - 1;
         if(_loc1_ < 0 || _loc1_ >= const_465)
         {
            return;
         }
         this.mStatus = class_66.const_185;
         this.mEndtime = 0;
         this.mCurrentResearchIndex = 0;
         ++this.var_403[_loc1_];
         if(this.var_403[_loc1_] > const_495)
         {
            this.var_403[_loc1_] = const_495;
         }
         this.var_1.screenClassTowers.Refresh();
      }
      
      public function ClearResearch() : void
      {
         if(!this.var_1.CanSendPacket())
         {
            return;
         }
         this.mStatus = const_185;
         this.mCurrentResearchIndex = 0;
         this.mEndtime = 0;
         var _loc1_:Packet = new Packet(LinkUpdater.const_1220);
         this.var_1.serverConn.SendPacket(_loc1_);
      }
      
      public function method_469() : void
      {
         if(this.var_1.clientEnt)
         {
            this.var_1.screenNotification.ShowNotification(class_46.const_692,"Gained Talent Point - " + Game.method_226(this.var_1.clientEnt.mMasterClass));
         }
      }
   }
}
