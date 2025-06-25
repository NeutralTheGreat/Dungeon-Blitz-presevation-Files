package
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.geom.Point;
   
   public class Camera
   {
      
      public static var SCREEN_WIDTH:Number = 1152;
      
      public static const SCREEN_HEIGHT:Number = 768;
      
      public static const PLAY_SCREEN_HEIGHT:Number = 668;
      
      private static const MOVEZONE_RIGHT_BASE:Number = 420;
      
      private static const MOVEZONE_LEFT_BASE:Number = 200;
      
      private static const const_925:Number = 260;
      
      private static const const_800:Number = 5;
      
      private static const const_603:Number = 160;
      
      private static const const_604:uint = 100;
      
      private static const const_676:uint = 80;
      
      private static const const_295:Number = 3000;
      
      private static const const_798:int = 349;
      
      private static const const_746:Number = 50;
      
      private static const const_674:Number = 150;
      
      private static const const_585:Number = 250;
      
      public static var leftDot:MovieClip = null;
      
      public static var rightDot:MovieClip = null;
      
      public static var meDot:MovieClip = null;
      
      public static var leftDotS:MovieClip = null;
      
      public static var rightDotS:MovieClip = null;
      
      public static var meDotS:MovieClip = null;
      
      public static var doodleSurface:Sprite = null;
      
      public static var var_404:Point = null;
      
      public static var var_1314:uint = Room.const_243;
      
      public static var var_1133:uint = Room.const_243;
       
      
      internal var var_1:Game;
      
      internal var var_48:Entity;
      
      internal var var_556:Boolean = false;
      
      internal var var_81:Point;
      
      internal var var_557:Number = 0;
      
      internal var var_524:Number = 0;
      
      internal var var_1227:Number;
      
      internal var var_2089:Number;
      
      internal var var_2997:Number = 0;
      
      internal var var_316:Boolean = false;
      
      internal var var_839:Number = 0;
      
      internal var var_2985:Number = 0;
      
      internal var var_2729:String;
      
      internal var var_2372:Number = 100;
      
      internal var var_2401:Number;
      
      public function Camera(param1:Game, param2:Entity)
      {
         super();
         this.var_1 = param1;
         this.var_48 = param2;
         this.var_81 = new Point();
      }
      
      public function method_1964() : void
      {
         this.var_81 = null;
         this.var_48 = null;
         this.var_1 = null;
      }
      
      public function method_2095() : void
      {
         var _loc1_:Number = (MOVEZONE_RIGHT_BASE + MOVEZONE_LEFT_BASE) / 4;
         if(this.var_316)
         {
            this.var_81.x = this.var_48.gfx.m_TheDO.x - (SCREEN_WIDTH - _loc1_);
         }
         else
         {
            this.var_81.x = this.var_48.gfx.m_TheDO.x - _loc1_;
         }
      }
      
      public function method_1102() : void
      {
         var _loc1_:Point = this.var_1.main.method_987(class_36.const_803);
         if(_loc1_.y >= const_674 && _loc1_.y <= Camera.PLAY_SCREEN_HEIGHT)
         {
            if(this.var_316)
            {
               if(_loc1_.x >= SCREEN_WIDTH - const_746)
               {
                  this.method_161();
               }
            }
            else if(_loc1_.x <= const_746)
            {
               this.method_161();
            }
         }
      }
      
      public function method_1582() : void
      {
         var _loc1_:Point = this.var_1.main.method_987(class_36.const_803);
         if(_loc1_.y >= const_674 && _loc1_.y <= Camera.PLAY_SCREEN_HEIGHT)
         {
            if(this.var_316)
            {
               if(_loc1_.x >= SCREEN_WIDTH - const_585)
               {
                  this.method_161();
               }
            }
            else if(_loc1_.x <= const_585)
            {
               this.method_161();
            }
         }
      }
      
      private function method_1924(param1:Number, param2:Number) : uint
      {
         var _loc3_:uint = 0;
         var _loc4_:class_37 = null;
         var _loc5_:Number = param2 - 1;
         var _loc6_:Point = class_36.const_952;
         var _loc7_:Point = class_36.CAMERAZONETEST_POINT2;
         var _loc8_:Point;
         (_loc8_ = class_36.CAMERAZONETEST_POINT3).x = 0;
         _loc8_.y = const_295;
         if(!(_loc4_ = this.var_1.collMan.getFloorCollision(0,param1,_loc5_,_loc8_,_loc6_,null,_loc7_,null,Game.const_250,0,CollisionManager.const_258)) || !_loc4_.var_941)
         {
            return 0;
         }
         _loc3_ = uint(_loc4_.var_941);
         _loc8_.x = 0;
         _loc8_.y = -const_295;
         if(!(_loc4_ = this.var_1.collMan.getFloorCollision(0,param1,_loc5_,_loc8_,_loc6_,null,_loc7_,null,Game.const_250,0,CollisionManager.const_258)) || _loc4_.var_941 != _loc3_)
         {
            return 0;
         }
         _loc8_.x = const_295;
         _loc8_.y = 0;
         if(!(_loc4_ = this.var_1.collMan.getFloorCollision(0,param1,_loc5_,_loc8_,_loc6_,null,_loc7_,null,Game.const_250,0,CollisionManager.const_258)) || _loc4_.var_941 != _loc3_)
         {
            return 0;
         }
         _loc8_.x = -const_295;
         _loc8_.y = 0;
         if(!(_loc4_ = this.var_1.collMan.getFloorCollision(0,param1,_loc5_,_loc8_,_loc6_,null,_loc7_,null,Game.const_250,0,CollisionManager.const_258)) || _loc4_.var_941 != _loc3_)
         {
            return 0;
         }
         return _loc3_;
      }
      
      public function method_161() : void
      {
         this.var_316 = !this.var_316;
      }
      
      public function method_1438(param1:Point) : void
      {
         var_404 = param1;
         this.var_557 = 0;
         this.var_524 = 0;
      }
      
      public function method_1073() : void
      {
         var _loc23_:class_37 = null;
         var _loc37_:Point = null;
         var _loc38_:Number = NaN;
         var _loc40_:Number = NaN;
         var _loc49_:Point = null;
         var _loc54_:Number = NaN;
         var _loc55_:Point = null;
         var _loc56_:Point = null;
         var _loc57_:class_37 = null;
         var _loc58_:Point = null;
         var _loc59_:class_37 = null;
         var _loc60_:Number = NaN;
         var _loc61_:Number = NaN;
         var _loc62_:Number = NaN;
         var _loc63_:Number = NaN;
         var _loc64_:Number = NaN;
         var _loc1_:Number = this.var_48.physPosX;
         var _loc2_:Room = this.var_48.currRoom;
         if(Boolean(_loc2_) && (_loc2_.var_113 != var_1314 || _loc2_.var_1207 != var_1133))
         {
            var_1314 = _loc2_.var_113;
            var_1133 = _loc2_.var_1207;
            this.method_1438(_loc2_.var_1082[var_1133]);
         }
         if(var_404)
         {
            if(var_404.x < _loc1_ && !this.var_316)
            {
               this.method_161();
            }
            else if(var_404.x > _loc1_ && this.var_316)
            {
               this.method_161();
            }
         }
         var _loc3_:Number = this.var_2401;
         if(this.var_48.physPosY > this.var_2401 || this.var_48.currSurface || this.var_556)
         {
            _loc3_ = this.var_48.physPosY;
            this.var_2401 = _loc3_;
         }
         _loc3_ = this.var_48.physPosY;
         var _loc4_:Boolean = false;
         var _loc5_:Point = new Point();
         var _loc6_:Number = this.var_81.x;
         var _loc7_:Number = this.var_81.y;
         if(this.var_556)
         {
            this.var_557 = 0;
            this.var_524 = 0;
            _loc54_ = (MOVEZONE_RIGHT_BASE + MOVEZONE_LEFT_BASE) / 4;
            if(this.var_316)
            {
               this.var_81.x = _loc1_ - (SCREEN_WIDTH - _loc54_);
            }
            else
            {
               this.var_81.x = _loc1_ - _loc54_;
            }
            _loc4_ = true;
         }
         if(_loc1_ < this.var_81.x)
         {
            this.method_161();
            this.var_81.x = _loc1_ - (SCREEN_WIDTH - const_798);
            _loc4_ = true;
         }
         else if(_loc1_ > this.var_81.x + SCREEN_WIDTH)
         {
            this.method_161();
            this.var_81.x = _loc1_ - const_798;
            _loc4_ = true;
         }
         var _loc8_:Number = this.var_2372 - this.var_81.x;
         if(!this.var_48.bFacingLeft() && !this.var_316)
         {
            this.var_1227 = Math.min(MOVEZONE_LEFT_BASE,_loc8_);
         }
         else if(this.var_48.bFacingLeft() && this.var_316)
         {
            this.var_1227 = Math.min(MOVEZONE_LEFT_BASE,SCREEN_WIDTH - _loc8_);
         }
         else
         {
            this.var_1227 = 0;
            this.var_2372 = _loc1_;
         }
         this.var_2372 = _loc1_;
         this.var_2089 = MOVEZONE_RIGHT_BASE;
         if(this.var_316)
         {
            this.var_2089 = SCREEN_WIDTH - this.var_1227;
            this.var_1227 = SCREEN_WIDTH - MOVEZONE_RIGHT_BASE;
         }
         var _loc9_:int = int(this.method_1924(_loc1_,_loc3_));
         var _loc10_:Point;
         (_loc10_ = new Point(this.var_81.x,this.var_81.y)).x = Math.min(_loc10_.x,_loc1_ - this.var_1227);
         _loc10_.x = Math.max(_loc10_.x,_loc1_ - this.var_2089);
         var _loc11_:Point = new Point(0,0);
         var _loc12_:Number = _loc3_;
         var _loc13_:Point = new Point(0,const_925);
         if(this.var_1.collMan.getFloorCollision(0,_loc1_,_loc12_,_loc13_,_loc11_,null,_loc5_,null,CollisionManager.HARD_FLOOR | CollisionManager.SOFT_FLOOR,0,_loc9_))
         {
            _loc12_ = _loc11_.y;
         }
         var _loc14_:Point = new Point(_loc10_.x - _loc1_,0);
         var _loc15_:class_37;
         if((Boolean(_loc15_ = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc12_,_loc14_,_loc11_,null,_loc5_,null,Game.const_152,0,_loc9_))) && Boolean(_loc15_.type & Game.const_413))
         {
            _loc10_.x = _loc11_.x;
         }
         else
         {
            _loc55_ = new Point(_loc10_.x + SCREEN_WIDTH - _loc1_,0);
            if(this.var_1.collMan.getFloorCollision(0,_loc1_,_loc12_,_loc55_,_loc11_,null,_loc5_,null,Game.const_152,0,_loc9_))
            {
               _loc10_.x = _loc11_.x - SCREEN_WIDTH;
               _loc56_ = new Point(_loc10_.x - _loc1_,0);
               if((Boolean(_loc57_ = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc12_,_loc56_,_loc11_,null,_loc5_,null,Game.const_152,0,_loc9_))) && Boolean(_loc57_.type & Game.const_413))
               {
                  _loc10_.x = _loc11_.x;
               }
            }
            else
            {
               _loc58_ = new Point(_loc10_.x - _loc1_,0);
               if(_loc59_ = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc12_,_loc58_,_loc11_,null,_loc5_,null,Game.const_152,0,_loc9_))
               {
                  _loc10_.x = _loc11_.x;
                  _loc55_.x = _loc10_.x + SCREEN_WIDTH - _loc1_;
                  if(this.var_1.collMan.getFloorCollision(0,_loc1_,_loc12_,_loc55_,_loc11_,null,_loc5_,null,Game.const_152,0,_loc9_))
                  {
                     _loc10_.x = _loc11_.x - SCREEN_WIDTH;
                  }
               }
            }
         }
         if(_loc1_ - _loc10_.x <= MOVEZONE_RIGHT_BASE)
         {
            this.var_316 = false;
         }
         if(_loc1_ - _loc10_.x >= SCREEN_WIDTH - MOVEZONE_RIGHT_BASE)
         {
            this.var_316 = true;
         }
         if(DevSettings.flags & DevSettings.DEVFLAG_SHOWWORLDCOLLISION)
         {
            if(!doodleSurface)
            {
               doodleSurface = new Sprite();
               this.var_1.levelLayer.addChild(doodleSurface);
            }
            doodleSurface.graphics.clear();
         }
         var _loc16_:Number = _loc3_ - const_800;
         var _loc17_:Point = new Point(0,const_603 + const_800);
         var _loc18_:Point = new Point();
         var _loc19_:class_37 = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc16_,_loc17_,_loc18_,null,_loc5_,null,Game.const_140,0,_loc9_);
         var _loc20_:Number = _loc16_ + _loc17_.y;
         var _loc21_:uint = Game.const_469;
         if(!_loc19_)
         {
            _loc17_.y += const_603;
            if(_loc19_ = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc16_,_loc17_,_loc18_,null,_loc5_,null,Game.const_160,0,_loc9_))
            {
               _loc20_ = _loc16_ + _loc17_.y - const_676;
            }
         }
         var _loc22_:Number = _loc20_ - PLAY_SCREEN_HEIGHT;
         var _loc24_:Point = new Point();
         var _loc25_:Point = new Point(0,-PLAY_SCREEN_HEIGHT);
         if(_loc23_ = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc3_,_loc25_,_loc24_,null,_loc5_,null,Game.const_237,0,_loc9_))
         {
            if(_loc24_.y > _loc22_)
            {
               _loc22_ = _loc24_.y;
            }
         }
         var _loc26_:Number = MOVEZONE_LEFT_BASE;
         var _loc27_:Number = SCREEN_WIDTH - MOVEZONE_LEFT_BASE;
         var _loc28_:Number = PLAY_SCREEN_HEIGHT + PLAY_SCREEN_HEIGHT;
         var _loc29_:Point = new Point(0,_loc28_);
         var _loc30_:Point = new Point();
         var _loc31_:class_37 = this.var_1.collMan.getFloorCollision(0,_loc10_.x + _loc26_,_loc22_,_loc29_,_loc30_,null,_loc5_,null,Game.const_140,0,_loc9_);
         var _loc32_:Number = _loc22_ + _loc29_.y;
         var _loc33_:Point = new Point(0,_loc28_);
         var _loc34_:Point = new Point();
         var _loc35_:class_37 = this.var_1.collMan.getFloorCollision(0,_loc10_.x + _loc27_,_loc22_,_loc33_,_loc34_,null,_loc5_,null,Game.const_140,0,_loc9_);
         var _loc36_:Number = _loc22_ + _loc33_.y;
         if(Boolean(_loc19_) || Boolean(_loc31_) || Boolean(_loc35_))
         {
            _loc60_ = _loc32_;
            if(_loc36_ > _loc60_)
            {
               _loc60_ = _loc36_;
            }
            if(_loc20_ > _loc60_)
            {
               _loc60_ = _loc20_;
            }
            _loc10_.y = _loc60_ - PLAY_SCREEN_HEIGHT + const_676;
            if(_loc10_.y > _loc3_ - const_604)
            {
               _loc10_.y = _loc3_ - const_604;
            }
            _loc21_ = 0;
         }
         if(DevSettings.flags & DevSettings.DEVFLAG_SHOWWORLDCOLLISION)
         {
            if(!leftDot)
            {
               leftDotS = class_4.method_16("a_Dot");
               rightDotS = class_4.method_16("a_Dot");
               meDotS = class_4.method_16("a_Dot");
               leftDot = class_4.method_16("a_Dot");
               rightDot = class_4.method_16("a_Dot");
               meDot = class_4.method_16("a_Dot");
               this.var_1.levelLayer.addChild(leftDotS);
               this.var_1.levelLayer.addChild(rightDotS);
               this.var_1.levelLayer.addChild(meDotS);
               this.var_1.levelLayer.addChild(leftDot);
               this.var_1.levelLayer.addChild(rightDot);
               this.var_1.levelLayer.addChild(meDot);
            }
            doodleSurface.graphics.lineStyle(3,16766720,1,false);
            doodleSurface.graphics.moveTo(_loc1_,_loc16_);
            doodleSurface.graphics.lineTo(_loc1_,_loc20_);
            doodleSurface.graphics.moveTo(_loc10_.x + _loc26_,_loc22_);
            doodleSurface.graphics.lineTo(_loc10_.x + _loc26_,_loc22_ + _loc28_);
            doodleSurface.graphics.moveTo(_loc10_.x + _loc27_,_loc22_);
            doodleSurface.graphics.lineTo(_loc10_.x + _loc27_,_loc22_ + _loc28_);
            doodleSurface.graphics.beginFill(204,0.2);
            leftDot.x = _loc10_.x + _loc26_;
            leftDot.y = _loc32_;
            rightDot.x = _loc10_.x + _loc27_;
            rightDot.y = _loc36_;
            meDot.x = _loc1_;
            meDot.y = _loc20_;
         }
         var _loc39_:Point = new Point();
         _loc25_ = new Point(0,-PLAY_SCREEN_HEIGHT);
         _loc38_ = _loc3_;
         if(_loc23_ = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc38_,_loc25_,_loc39_,null,_loc5_,null,Game.const_237,0,_loc9_))
         {
            if(_loc39_.y > _loc10_.y)
            {
               _loc10_.y = _loc39_.y;
            }
         }
         _loc25_ = new Point(0,-PLAY_SCREEN_HEIGHT);
         _loc38_ = _loc3_;
         if(_loc23_ = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc38_,_loc25_,_loc39_,null,_loc5_,null,Game.const_237 | Game.const_140,0,_loc9_))
         {
            _loc38_ = _loc39_.y + 1;
         }
         else
         {
            _loc38_ = _loc3_ - PLAY_SCREEN_HEIGHT;
         }
         _loc37_ = new Point(0,PLAY_SCREEN_HEIGHT * 4);
         _loc23_ = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc38_,_loc37_,_loc39_,null,_loc5_,null,Game.const_237 | Game.const_140,0,_loc9_);
         if(_loc23_ = this.var_1.collMan.getFloorCollision(0,_loc1_,_loc38_,_loc37_,_loc39_,null,_loc5_,null,Game.const_160,0,_loc9_))
         {
            _loc61_ = _loc10_.x + SCREEN_WIDTH / 2;
            _loc62_ = _loc38_ + _loc37_.y / 2;
            _loc25_ = new Point(0,-PLAY_SCREEN_HEIGHT);
            _loc38_ = _loc62_;
            if(_loc23_ = this.var_1.collMan.getFloorCollision(0,_loc61_,_loc38_,_loc25_,_loc39_,null,_loc5_,null,Game.const_391,0,_loc9_))
            {
               _loc38_ = _loc39_.y + 1;
            }
            else
            {
               _loc38_ = _loc3_ - PLAY_SCREEN_HEIGHT;
            }
            _loc37_ = new Point(0,PLAY_SCREEN_HEIGHT * 4);
            _loc23_ = this.var_1.collMan.getFloorCollision(0,_loc61_,_loc38_,_loc37_,_loc39_,null,_loc5_,null,Game.const_391,0,_loc9_);
            if(_loc23_ = this.var_1.collMan.getFloorCollision(0,_loc61_,_loc38_,_loc37_,_loc39_,null,_loc5_,null,Game.const_160,0,_loc9_))
            {
               _loc10_.y = _loc39_.y - PLAY_SCREEN_HEIGHT;
               _loc21_ = _loc23_.type;
            }
         }
         if(DevSettings.flags & DevSettings.DEVFLAG_SHOWWORLDCOLLISION)
         {
            doodleSurface.graphics.lineStyle(10,6710886,1,false);
            doodleSurface.graphics.moveTo(_loc61_,_loc38_);
            doodleSurface.graphics.lineTo(_loc61_ + _loc37_.x,_loc38_ + _loc37_.y);
            if(_loc23_)
            {
               doodleSurface.graphics.lineStyle(12,6710886,1,false);
               doodleSurface.graphics.moveTo(_loc39_.x,_loc39_.y);
               doodleSurface.graphics.lineTo(_loc39_.x - 15,_loc39_.y - 15);
               doodleSurface.graphics.lineTo(_loc39_.x + 15,_loc39_.y - 15);
               doodleSurface.graphics.lineTo(_loc39_.x,_loc39_.y);
            }
         }
         if(_loc21_ & Game.const_469)
         {
            if((_loc40_ = _loc3_ - 350) < _loc10_.y)
            {
               _loc10_.y = _loc40_;
            }
         }
         else if(!(_loc21_ & Game.const_682))
         {
            if((_loc40_ = _loc3_ - 120) < _loc10_.y)
            {
               _loc10_.y = _loc40_;
            }
         }
         this.var_81.x = _loc10_.x;
         this.var_81.y = _loc10_.y;
         if(this.var_48.var_1122)
         {
            this.var_81.x = _loc6_;
            this.var_81.y = _loc7_;
         }
         if(var_404)
         {
            this.var_81.x = var_404.x - SCREEN_WIDTH / 2;
            this.var_81.y = var_404.y - PLAY_SCREEN_HEIGHT;
         }
         var _loc43_:Number = 700;
         var _loc44_:Number = 700;
         if(var_404)
         {
            _loc43_ *= 5;
            _loc44_ *= 5;
         }
         var _loc45_:Number = (_loc6_ - this.var_81.x) / this.var_1.TIMESTEP;
         var _loc46_:Number = (_loc7_ - this.var_81.y) / this.var_1.TIMESTEP;
         var _loc47_:Number = 1000 / Game.TARGETFPS;
         if(Math.abs(_loc45_) > 20 && !this.var_557)
         {
            this.var_557 = _loc43_;
         }
         this.var_557 -= _loc47_;
         if(this.var_557 <= 0)
         {
            this.var_557 = 0;
         }
         if(Math.abs(_loc46_) > 20 && !this.var_524)
         {
            this.var_524 = _loc44_;
         }
         this.var_524 -= _loc47_;
         if(this.var_524 <= 0)
         {
            this.var_524 = 0;
         }
         var _loc48_:Boolean = false;
         if(this.var_556)
         {
            this.var_557 = 0;
            this.var_524 = 0;
            this.var_556 = false;
            _loc48_ = true;
         }
         var _loc50_:Point;
         (_loc50_ = new Point(0,0)).x = (-this.var_81.x - this.var_1.levelLayer.x) * (this.var_557 / _loc43_);
         _loc50_.y = (-this.var_81.y - this.var_1.levelLayer.y) * (this.var_524 / _loc44_);
         if(var_404)
         {
            if((_loc63_ = -this.var_81.x - this.var_1.levelLayer.x) < 0)
            {
               _loc63_ *= -1;
            }
            if(_loc63_ < 1.5)
            {
               _loc50_.x = 0;
            }
            if((_loc64_ = -this.var_81.y - this.var_1.levelLayer.y) < 0)
            {
               _loc64_ *= -1;
            }
            if(_loc64_ < 1.5)
            {
               _loc50_.y = 0;
            }
         }
         _loc49_ = new Point(-this.var_81.x - _loc50_.x,-this.var_81.y - _loc50_.y);
         this.method_1469(_loc49_);
         this.var_1.levelLayer.x = _loc49_.x;
         this.var_1.levelLayer.y = _loc49_.y;
         var _loc51_:Number;
         var _loc52_:Number = (_loc51_ = this.var_1.main.overallScale) * this.var_1.levelLayer.x;
         var _loc53_:Number = _loc51_ * this.var_1.levelLayer.y;
         _loc52_ = Math.floor(_loc52_ + 0.3786);
         _loc53_ = Math.floor(_loc53_ + 0.3786);
         _loc52_ /= _loc51_;
         _loc53_ /= _loc51_;
         this.var_1.levelLayer.x = _loc52_;
         this.var_1.levelLayer.y = _loc53_;
      }
      
      public function method_1469(param1:Point) : void
      {
         var _loc2_:Number = 0;
         if(this.var_839 <= 0)
         {
            return;
         }
         if(this.var_839 == 2)
         {
            _loc2_ += 5;
         }
         else if(this.var_839 == 1)
         {
            _loc2_ -= 3;
         }
         else if(this.var_839 >= 3)
         {
            if(this.var_839 % 2 == 1)
            {
               _loc2_ -= 7;
            }
            else
            {
               _loc2_ += 7;
            }
         }
         param1.y += _loc2_;
         --this.var_839;
      }
      
      public function method_237(param1:String, param2:Number = 0) : void
      {
         this.var_2729 = param1;
         this.var_839 = this.var_2729 == "Slam" ? 3 : param2;
      }
   }
}
