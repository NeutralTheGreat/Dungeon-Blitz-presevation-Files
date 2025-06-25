package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.MovieClip;
   import flash.display.PixelSnapping;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.geom.Point;
   import flash.system.Capabilities;
   import flash.system.System;
   import flash.utils.getTimer;
   
   public class Main extends Sprite
   {
      
      public static const const_206:Number = 30;
      
      public static const const_607:Number = 4;
      
      public static const const_715:Number = 100;
      
      public static const const_77:uint = SoundManager.method_712(0.01,0.07);
      
      public static const const_108:uint = SoundManager.method_712(0.04,0);
      
      public static var var_1468:Number = -1000;
      
      public static var var_1954:Number = -1001;
      
      public static var var_1876:int = 31;
      
      public static const const_1249:uint = 7498;
       
      
      private var var_2717:Number;
      
      internal var var_2975:int = 0;
      
      internal var var_2210:Connection = null;
      
      internal var var_523:Vector.<Game>;
      
      internal var var_2363:uint = 0;
      
      internal var var_2392:String = null;
      
      internal var resourceMonitor:ResourceMonitorUtil;
      
      internal var overallScale:Number = 0;
      
      internal var var_2243:Number = 0;
      
      internal var var_982:Number = 0;
      
      internal var var_2825:Number = 0;
      
      internal var var_1976:Boolean = false;
      
      internal var var_147:Bitmap;
      
      internal var var_860:uint = 0;
      
      internal var var_903:uint = 0;
      
      internal var var_374:Bitmap;
      
      internal var var_2289:Number = 0;
      
      internal var var_2792:Number = 0;
      
      internal var var_2102:Boolean = false;
      
      internal var var_2219:int = 0;
      
      internal var var_2618:uint = 0;
      
      internal var var_1765:Number = 0;
      
      internal var var_2349:Number = 1000;
      
      internal var var_2588:uint = 0;
      
      internal var var_1860:uint = 0;
      
      internal var var_2617:uint = 0;
      
      internal var var_2801:uint = 0;
      
      internal var w:int = 0;
      
      public function Main()
      {
         this.var_2717 = !!(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT) ? 0 : 1;
         super();
      }
      
      public function Init() : void
      {
         SuperAnimData.aaMain = this;
         a_LocalText.funcRef = this.method_1832;
         stage.frameRate = const_206;
         if(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT)
         {
            this.var_2210 = new Connection(null);
            this.var_2210.method_403("127.0.0.1",const_1249);
            addEventListener(Event.ENTER_FRAME,this.method_1324);
         }
         addEventListener(Event.ENTER_FRAME,this.method_1284);
         addEventListener(Event.ACTIVATE,this.method_1812);
         addEventListener(Event.DEACTIVATE,this.method_1481);
         this.method_1634();
         this.method_561(stage.stageWidth,stage.stageHeight);
         stage.addEventListener(Event.RESIZE,this.method_1897);
         this.var_523 = new Vector.<Game>();
         var _loc1_:int = 0;
         while(_loc1_ < this.var_2717)
         {
            this.var_523.push(new Game(this));
            _loc1_++;
         }
         var _loc2_:String = Capabilities.version;
         var _loc3_:Array = _loc2_.split(" ");
         if(_loc3_.length > 1)
         {
            _loc3_ = _loc3_[1].split(",");
            this.var_2219 = int(_loc3_[0]);
         }
         if(this.var_2219 >= 11 && stage.frameRate != const_715)
         {
            stage.frameRate = const_715;
         }
      }
      
      public function method_1634() : void
      {
         this.var_147 = new Bitmap(null,PixelSnapping.ALWAYS,false);
         addChild(this.var_147);
         if(DevSettings.flags & DevSettings.DEVFLAG_SHOWRESOURCEMONITOR)
         {
            this.CreateResourceMonitor();
         }
      }
      
      public function CreateResourceMonitor() : void
      {
         if(this.resourceMonitor)
         {
            return;
         }
         this.resourceMonitor = new ResourceMonitorUtil();
         this.resourceMonitor.mouseChildren = false;
         this.resourceMonitor.mouseEnabled = false;
         this.resourceMonitor.x = Camera.SCREEN_WIDTH - this.resourceMonitor.width;
         stage.addChild(this.resourceMonitor);
         this.resourceMonitor.method_104("fps",const_206,3,16763938);
         this.resourceMonitor.method_104("low",const_206,1,16737894);
         this.resourceMonitor.method_104("mem",500,2,52479);
         this.resourceMonitor.method_104("sbmp",250,2,16777215);
         this.resourceMonitor.method_104("bbmp",250,2,16755455);
         this.resourceMonitor.method_104("mcbmp",250,2,16777130);
         this.resourceMonitor.method_104("tbmp",250,2,16755370);
         this.resourceMonitor.method_104("ents",100,2,13400063);
         this.resourceMonitor.method_104("scale",100,2,16742399);
         this.resourceMonitor.method_104("bSent",1000,1,7812010);
         this.resourceMonitor.method_104("bRec",1000,1,11189077);
      }
      
      public function method_2008(param1:BitmapData) : void
      {
         var _loc2_:Bitmap = new Bitmap(param1,PixelSnapping.NEVER,true);
         _loc2_.x = int(this.w % 500);
         _loc2_.y = int(this.w / 500) * 100;
         stage.addChild(_loc2_);
         this.w += _loc2_.width;
      }
      
      public function method_1761() : void
      {
         if(this.resourceMonitor)
         {
            this.resourceMonitor.x = parent.x + (Camera.SCREEN_WIDTH * this.overallScale - this.resourceMonitor.width);
         }
      }
      
      public function method_561(param1:int, param2:int) : void
      {
         var _loc3_:Number = NaN;
         var _loc7_:int = 0;
         var _loc8_:int = 0;
         if(!param1 || !param2)
         {
            return;
         }
         var _loc4_:Number = Camera.SCREEN_WIDTH / Camera.SCREEN_HEIGHT;
         if(param1 < param2 * _loc4_)
         {
            _loc3_ = param1 / (Camera.SCREEN_WIDTH + var_1876 * 2);
         }
         else
         {
            _loc3_ = param2 / (Camera.SCREEN_HEIGHT + var_1876 * 2);
         }
         var _loc5_:Number = Camera.SCREEN_WIDTH * _loc3_;
         var _loc6_:int = int(_loc5_ / 6) * 6;
         _loc3_ = Number(_loc6_) / Camera.SCREEN_WIDTH;
         if(_loc3_ > 1.25 && !(DevSettings.flags & DevSettings.const_1124))
         {
            _loc3_ = 1.25;
         }
         if(_loc3_ < 0.125)
         {
            _loc3_ = 0.125;
         }
         if(_loc3_ != this.overallScale)
         {
            _loc7_ = Math.ceil(Camera.SCREEN_WIDTH * _loc3_);
            _loc8_ = Math.ceil(Camera.PLAY_SCREEN_HEIGHT * _loc3_);
            this.overallScale = _loc3_;
            this.var_2243 = this.overallScale;
            this.var_982 = this.overallScale;
            this.var_2825 = this.overallScale;
            if(this.var_147.bitmapData)
            {
               this.var_147.bitmapData.dispose();
            }
            this.var_147.bitmapData = new BitmapData(_loc7_,_loc8_,false);
            this.var_147.bitmapData.fillRect(this.var_147.bitmapData.rect,4737365);
            if(this.var_374)
            {
               removeChild(this.var_374);
               if(this.var_374.bitmapData)
               {
                  this.var_374.bitmapData.dispose();
               }
               this.var_374 = null;
               this.var_903 = 0;
               this.var_860 = 0;
               this.var_147.alpha = 1;
            }
            this.var_2102 = true;
         }
         parent.x = int((param1 - Camera.SCREEN_WIDTH * this.overallScale) * 0.5);
         parent.y = int((param2 - Camera.SCREEN_HEIGHT * this.overallScale) * 0.5);
         this.var_2792 = this.var_2289;
         this.method_1761();
      }
      
      public function method_987(param1:Point) : Point
      {
         var _loc2_:Number = 1 / this.overallScale;
         var _loc3_:Number = stage.stageWidth * 0.5 - Camera.SCREEN_WIDTH * this.overallScale * 0.5;
         param1.x = (stage.mouseX - _loc3_) * _loc2_;
         param1.y = (stage.mouseY - parent.y) * _loc2_;
         return param1;
      }
      
      private function method_1284(param1:Event) : void
      {
         var startOfTicks:int;
         var i:int;
         var afterAllTicks:int;
         var totalTickTime:int;
         var realFrameRate:Number;
         var currGame:Game = null;
         var bKeepTicking:Boolean = false;
         var mainTimeNow:uint = 0;
         var timeSinceLastTick:uint = 0;
         var mainTimeStep:Number = NaN;
         var timeSinceFPSUpdate:Number = NaN;
         var entCount:uint = 0;
         var magicCacheCount:uint = 0;
         var magicTilerCount:uint = 0;
         var FPS:Number = NaN;
         var flashTargetFrameRate:Number = NaN;
         var ev:Event = param1;
         if(this.var_2289 > this.var_2792)
         {
            this.method_561(stage.stageWidth,stage.stageHeight);
         }
         ResourceManager.method_783();
         class_41.method_1358();
         SoundManager.method_1017();
         startOfTicks = getTimer();
         i = int(this.var_523.length - 1);
         while(i >= 0)
         {
            currGame = this.var_523[i];
            if(!DevSettings.flags || Boolean(DevSettings.flags & DevSettings.DEVFLAG_MASTER_CLIENT))
            {
               bKeepTicking = currGame.method_1636();
            }
            else
            {
               bKeepTicking = currGame.method_789();
            }
            if(!bKeepTicking)
            {
               try
               {
                  currGame.method_571();
               }
               catch(error:Error)
               {
                  currGame.method_297(error);
               }
               this.var_523.splice(i,1);
            }
            i--;
         }
         afterAllTicks = getTimer();
         totalTickTime = afterAllTicks - startOfTicks;
         if(this.resourceMonitor)
         {
            mainTimeNow = uint(getTimer());
            timeSinceLastTick = uint(mainTimeNow - this.var_2618);
            mainTimeStep = timeSinceLastTick * 0.001 * Game.TARGETFPS;
            if(mainTimeStep > this.var_1765)
            {
               this.var_1765 = mainTimeStep;
            }
            if(mainTimeStep < this.var_2349)
            {
               this.var_2349 = mainTimeStep;
            }
            ++this.var_1860;
            this.var_2618 = mainTimeNow;
            timeSinceFPSUpdate = afterAllTicks - this.var_2588;
            if(timeSinceFPSUpdate > 1000)
            {
               entCount = 0;
               magicCacheCount = 0;
               magicTilerCount = 0;
               for each(currGame in this.var_523)
               {
                  if(currGame.var_171)
                  {
                     magicCacheCount += currGame.var_171.var_1522;
                  }
                  if(currGame.entities)
                  {
                     entCount += currGame.entities.length;
                  }
                  if(currGame.var_107)
                  {
                     magicTilerCount += currGame.var_107.var_1881;
                  }
               }
               FPS = this.var_1860 * 1000 / timeSinceFPSUpdate;
               this.resourceMonitor.method_107("fps",FPS);
               this.resourceMonitor.method_107("low",Game.TARGETFPS / this.var_1765);
               this.resourceMonitor.method_107("mem",Math.round(System.totalMemory / 10485.76) / 100);
               this.resourceMonitor.method_107("sbmp",SuperAnimData.var_263 * 4 / (1024 * 1024));
               this.resourceMonitor.method_107("bbmp",SuperAnimData.var_665 * 4 / (1024 * 1024));
               this.resourceMonitor.method_107("mcbmp",magicCacheCount * 4 / (1024 * 1024));
               this.resourceMonitor.method_107("tbmp",magicTilerCount * 4 / (1024 * 1024));
               this.resourceMonitor.method_107("ents",entCount);
               this.resourceMonitor.method_107("scale",this.overallScale * 100);
               this.resourceMonitor.method_107("bSent",this.var_2617);
               this.resourceMonitor.method_107("bRec",this.var_2801);
               this.resourceMonitor.method_1035();
               this.var_2801 = 0;
               this.var_2617 = 0;
               this.var_1860 = 0;
               this.var_1765 = 0;
               this.var_2349 = 1000;
               this.var_2588 = afterAllTicks;
            }
         }
         realFrameRate = 1000 / (totalTickTime + 15);
         realFrameRate = Math.floor(realFrameRate) - 1;
         if(this.var_2219 < 11)
         {
            flashTargetFrameRate = stage.frameRate;
            if(flashTargetFrameRate > realFrameRate)
            {
               flashTargetFrameRate = realFrameRate;
            }
            else if(flashTargetFrameRate < const_206)
            {
               flashTargetFrameRate += 1;
            }
            flashTargetFrameRate = realFrameRate;
            if(flashTargetFrameRate > const_206)
            {
               flashTargetFrameRate = const_206;
            }
            if(flashTargetFrameRate < const_607)
            {
               flashTargetFrameRate = const_607;
            }
            if(flashTargetFrameRate != stage.frameRate)
            {
               stage.frameRate = flashTargetFrameRate;
            }
         }
      }
      
      private function method_1897(param1:Event) : void
      {
         this.var_2289 = getTimer();
      }
      
      private function method_1812(param1:Event) : void
      {
         Main.var_1468 = getTimer();
      }
      
      private function method_1481(param1:Event) : void
      {
         Main.var_1954 = getTimer();
      }
      
      private function method_1324(param1:Event) : void
      {
         var pkt:Packet = null;
         var mapID:uint = 0;
         var levelName:String = null;
         var internalName:String = null;
         var mapLevel:uint = 0;
         var baseLevel:uint = 0;
         var monsterBonusLevel:uint = 0;
         var momentParams:String = null;
         var alterParams:String = null;
         var isInstanced:Boolean = false;
         var newGame:Game = null;
         var mapToRemoveID:uint = 0;
         var i:int = 0;
         var game:Game = null;
         var ev:Event = param1;
         var packetList:Vector.<Packet> = this.var_2210.method_918();
         loop0:
         for each(pkt in packetList)
         {
            switch(pkt.type)
            {
               case LinkUpdater.PKTTYPE_GAME_TO_MASTER_PORT:
                  this.var_2392 = pkt.method_13();
                  this.var_2363 = pkt.method_91();
                  break;
               case LinkUpdater.PKTTYPE_GAME_TO_MASTER_START_LEVEL:
                  mapID = pkt.method_4();
                  levelName = pkt.method_13();
                  internalName = pkt.method_13();
                  mapLevel = pkt.method_6(Entity.MAX_CHAR_LEVEL_BITS);
                  baseLevel = pkt.method_6(Entity.MAX_CHAR_LEVEL_BITS);
                  monsterBonusLevel = pkt.method_4();
                  momentParams = pkt.method_13();
                  alterParams = pkt.method_13();
                  isInstanced = pkt.method_11();
                  newGame = new Game(this);
                  newGame.mBonusLevels = monsterBonusLevel;
                  newGame.method_282(0,levelName,mapLevel,baseLevel,internalName,momentParams,alterParams,isInstanced);
                  newGame.var_2334 = mapID;
                  newGame.levelLayer.visible = false;
                  this.var_523.push(newGame);
                  break;
               case LinkUpdater.PKTTYPE_GAME_TO_MASTER_END_LEVEL:
                  mapToRemoveID = pkt.method_4();
                  i = 0;
                  while(i < this.var_523.length)
                  {
                     game = this.var_523[i];
                     if(game.var_2334 == mapToRemoveID)
                     {
                        try
                        {
                           game.method_571();
                        }
                        catch(error:Error)
                        {
                           game.method_297(error);
                        }
                        this.var_523.splice(i,1);
                        continue loop0;
                     }
                     i++;
                  }
                  break;
            }
         }
      }
      
      public function method_1832(param1:MovieClip) : void
      {
         class_4.method_276(param1);
      }
   }
}
