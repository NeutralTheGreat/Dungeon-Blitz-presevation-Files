package
{
   import flash.display.DisplayObject;
   import flash.display.Sprite;
   import flash.filters.GlowFilter;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.utils.Dictionary;
   
   public class Loot
   {
      
      private static var var_1936:Dictionary = new Dictionary();
      
      private static var var_1945:Dictionary = new Dictionary();
      
      private static var var_1100:Dictionary;
      
      private static const const_1033:int = -26;
      
      private static const const_618:int = -52;
      
      private static const const_562:int = -35;
      
      private static const const_1122:uint = 500;
      
      private static var goldGfxTypes:Vector.<GfxType>;
      
      public static var var_846:GfxType = new GfxType();
      
      public static var var_734:GfxType = new GfxType();
      
      public static const const_1236:int = 2;
      
      {
         method_975();
         method_582();
         var_846.var_29 = "SFX_1.swf";
         var_846.animScale = 1.8;
         var_846.bFireAndForget = true;
         var_846.animClass = "a_HealthLoot";
         var_846.baseAnim = "Appear";
         var_734.var_29 = "SFX_1.swf";
         var_734.animScale = 1.8;
         var_734.bFireAndForget = true;
         var_734.animClass = "a_SoulLoot";
         var_734.baseAnim = "Appear";
      }
      
      internal var var_1:Game;
      
      internal var lootID:uint;
      
      internal var var_11:Point;
      
      internal var var_2614:uint;
      
      internal var superAnim:SuperAnimInstance;
      
      internal var var_2607:Boolean = false;
      
      internal var var_2487:Boolean = false;
      
      internal var var_2535:uint;
      
      internal var gearType:GearType;
      
      internal var materialType:class_8;
      
      internal var var_79:uint;
      
      internal var var_2169:uint;
      
      internal var var_286:class_15;
      
      internal var var_647:class_21;
      
      internal var var_1509:uint;
      
      internal var var_2889:Boolean = false;
      
      public function Loot(param1:Game, param2:uint, param3:Point, param4:GearType, param5:class_8, param6:uint, param7:uint, param8:class_15, param9:class_21, param10:uint = 0)
      {
         var _loc11_:GfxType = null;
         var _loc12_:uint = 0;
         var _loc13_:GfxType = null;
         var _loc14_:Number = NaN;
         var _loc15_:GfxType = null;
         var _loc16_:GfxType = null;
         super();
         this.var_1 = param1;
         this.lootID = param2;
         this.gearType = param4;
         this.materialType = param5;
         this.var_286 = param8;
         this.var_647 = param9;
         this.var_11 = new Point();
         this.var_2614 = this.var_1.mTimeThisTick;
         if(param4)
         {
            this.superAnim = this.var_1.RenderGear(Game.const_1015,param4,1,null,null,null,true);
            this.superAnim.m_TheDO.filters = [new GlowFilter(4279367708)];
         }
         else if(param5)
         {
            if(!(_loc11_ = var_1936[param5.var_537]))
            {
               (_loc11_ = new GfxType()).var_29 = "UI_1.swf";
               _loc11_.animClass = param5.iconName;
               _loc11_.bFireAndForget = true;
               var_1936[param5.var_537] = _loc11_;
            }
            this.superAnim = new SuperAnimInstance(this.var_1,_loc11_,true);
            this.superAnim.m_Seq.method_34(Seq.C_USEPOWER,"Ready",true);
         }
         else if(param6)
         {
            this.var_79 = param6;
            if(this.var_79 <= 40)
            {
               _loc12_ = 0;
            }
            else if(this.var_79 <= 65)
            {
               _loc12_ = 1;
            }
            else if(this.var_79 <= 113)
            {
               _loc12_ = 2;
            }
            else if(this.var_79 <= 160)
            {
               _loc12_ = 3;
            }
            else if(this.var_79 <= 260)
            {
               _loc12_ = 4;
            }
            else if(this.var_79 <= 452)
            {
               _loc12_ = 5;
            }
            else
            {
               _loc12_ = 6;
            }
            this.superAnim = new SuperAnimInstance(this.var_1,goldGfxTypes[_loc12_],true);
            this.superAnim.m_Seq.method_34(Seq.C_USEPOWER,"Appear",true);
         }
         else if(this.var_286)
         {
            if(!(_loc13_ = var_1945[this.var_286.var_1375]))
            {
               (_loc13_ = new GfxType()).var_29 = "UI_2.swf";
               _loc13_.animClass = this.var_286.var_2810;
               _loc13_.bFireAndForget = true;
               _loc13_.animScale = 1;
               var_1945[this.var_286.var_1375] = _loc13_;
            }
            this.superAnim = new SuperAnimInstance(this.var_1,_loc13_,true);
            this.superAnim.m_Seq.method_34(Seq.C_USEPOWER,"Ready",true);
         }
         else if(Boolean(param10) && this.var_1.clientEnt.combatState.var_2036)
         {
            this.var_1509 = param10;
            this.superAnim = new SuperAnimInstance(this.var_1,var_734,true);
            this.var_2889 = true;
            this.superAnim.method_325(6684774);
            this.superAnim.m_Seq.method_34(Seq.C_USEPOWER,"Appear",true);
            _loc14_ = 1.4;
            if(this.var_1.clientEnt)
            {
               _loc14_ *= this.var_1509 / this.var_1.clientEnt.const_156;
            }
            if(_loc14_ > 1)
            {
               _loc14_ = 1;
            }
            if(_loc14_ < 0.45)
            {
               _loc14_ = 0.45;
            }
            this.superAnim.m_TheDO.scaleX = this.superAnim.m_TheDO.scaleY = _loc14_;
         }
         else if(this.var_647)
         {
            if(_loc15_ = var_1100[this.var_647.var_8])
            {
               _loc16_ = _loc15_.GetDuplicate();
            }
            if(_loc16_)
            {
               _loc16_.colorSwaps.push(new ColorSwap(16734039,this.var_647.var_935,0));
               _loc16_.colorSwaps.push(new ColorSwap(14352384,this.var_647.color,0));
               _loc16_.colorSwaps.push(new ColorSwap(7798784,this.var_647.var_209,0));
            }
            this.superAnim = new SuperAnimInstance(this.var_1,_loc16_,true);
            this.superAnim.m_Seq.method_34(Seq.C_USEPOWER,"Ready",true);
         }
         else
         {
            this.var_2169 = param7;
            this.superAnim = new SuperAnimInstance(this.var_1,var_846,true);
            this.superAnim.m_Seq.method_34(Seq.C_USEPOWER,"Appear",true);
            _loc14_ = 1.4;
            if(this.var_1.clientEnt)
            {
               _loc14_ *= this.var_2169 / this.var_1.clientEnt.maxHP;
            }
            if(_loc14_ > 1)
            {
               _loc14_ = 1;
            }
            if(_loc14_ < 0.45)
            {
               _loc14_ = 0.45;
            }
            this.superAnim.m_TheDO.scaleX = this.superAnim.m_TheDO.scaleY = _loc14_;
         }
         this.var_11.x = param3.x;
         this.var_11.y = param3.y;
         this.superAnim.m_TheDO.x = this.var_11.x;
         this.superAnim.m_TheDO.y = this.var_11.y;
         if(this.materialType)
         {
            this.superAnim.m_TheDO.x += const_1033;
            this.superAnim.m_TheDO.y += const_618;
         }
         this.var_1.playerEntLayer.addChild(this.superAnim.m_TheDO);
      }
      
      public static function method_975() : void
      {
         var_1100 = new Dictionary();
         var _loc1_:GfxType = new GfxType();
         _loc1_.var_29 = "UI_1.swf";
         _loc1_.animClass = "a_DyeBottleBig";
         _loc1_.baseAnim = "Ready";
         _loc1_.animScale = 0.3;
         _loc1_.bFireAndForget = true;
         var_1100["L"] = _loc1_;
         var _loc2_:GfxType = new GfxType();
         _loc2_.var_29 = "UI_1.swf";
         _loc2_.animClass = "a_DyeBottleSmall";
         _loc2_.baseAnim = "Ready";
         _loc2_.animScale = 0.3;
         _loc2_.bFireAndForget = true;
         var_1100["R"] = _loc2_;
         var_1100["M"] = _loc2_;
      }
      
      public static function method_582() : void
      {
         goldGfxTypes = new Vector.<GfxType>();
         var _loc1_:GfxType = new GfxType();
         _loc1_.var_29 = "SFX_1.swf";
         _loc1_.animClass = "a_GoldLoot00";
         _loc1_.baseAnim = "Appear";
         _loc1_.animScale = 0.95;
         _loc1_.bFireAndForget = true;
         goldGfxTypes.push(_loc1_);
         _loc1_ = new GfxType();
         _loc1_.var_29 = "SFX_1.swf";
         _loc1_.animClass = "a_GoldLoot01";
         _loc1_.baseAnim = "Appear";
         _loc1_.animScale = 1;
         _loc1_.bFireAndForget = true;
         goldGfxTypes.push(_loc1_);
         _loc1_ = new GfxType();
         _loc1_.var_29 = "SFX_1.swf";
         _loc1_.animClass = "a_GoldLoot02";
         _loc1_.baseAnim = "Appear";
         _loc1_.animScale = 1.05;
         _loc1_.bFireAndForget = true;
         goldGfxTypes.push(_loc1_);
         _loc1_ = new GfxType();
         _loc1_.var_29 = "SFX_1.swf";
         _loc1_.animClass = "a_GoldLoot03";
         _loc1_.baseAnim = "Appear";
         _loc1_.animScale = 1.1;
         _loc1_.bFireAndForget = true;
         goldGfxTypes.push(_loc1_);
         _loc1_ = new GfxType();
         _loc1_.var_29 = "SFX_1.swf";
         _loc1_.animClass = "a_GoldLoot04";
         _loc1_.baseAnim = "Appear";
         _loc1_.animScale = 1.15;
         _loc1_.bFireAndForget = true;
         goldGfxTypes.push(_loc1_);
         _loc1_ = new GfxType();
         _loc1_.var_29 = "SFX_1.swf";
         _loc1_.animClass = "a_GoldLoot05";
         _loc1_.baseAnim = "Appear";
         _loc1_.animScale = 1.2;
         _loc1_.bFireAndForget = true;
         goldGfxTypes.push(_loc1_);
         _loc1_ = new GfxType();
         _loc1_.var_29 = "SFX_1.swf";
         _loc1_.animClass = "a_GoldLoot06";
         _loc1_.baseAnim = "Appear";
         _loc1_.animScale = 1.25;
         _loc1_.bFireAndForget = true;
         goldGfxTypes.push(_loc1_);
         goldGfxTypes.fixed = true;
      }
      
      public function method_1300() : Boolean
      {
         var _loc3_:uint = 0;
         var _loc4_:Number = NaN;
         var _loc5_:Sprite = null;
         var _loc6_:Sprite = null;
         var _loc7_:Sprite = null;
         var _loc8_:String = null;
         var _loc9_:Packet = null;
         var _loc10_:Rectangle = null;
         var _loc11_:EntType = null;
         var _loc12_:Number = NaN;
         var _loc13_:Number = NaN;
         var _loc1_:Entity = this.var_1.clientEnt;
         var _loc2_:uint = this.var_1.mTimeThisTick;
         if(this.var_2607)
         {
            if(!this.materialType && !this.var_286 && !this.var_647)
            {
               return !this.superAnim.m_bFinished;
            }
            _loc3_ = uint(_loc2_ - this.var_2535);
            if((_loc4_ = _loc3_ / const_1122) > 1)
            {
               this.superAnim.DestroySuperAnimInstance();
               return false;
            }
            if(this.materialType)
            {
               (_loc5_ = this.superAnim.m_TheDO).y = this.var_11.y + const_618 + const_562 * _loc4_;
               _loc5_.scaleX = 0.8 * (1 - _loc4_);
               _loc5_.scaleY = 0.8 * (1 - _loc4_);
            }
            if(this.var_286)
            {
               (_loc6_ = this.superAnim.m_TheDO).y = this.var_11.y + const_562 * _loc4_;
               _loc6_.scaleX = 0.8 * (1 - _loc4_);
               _loc6_.scaleY = 0.8 * (1 - _loc4_);
            }
            if(this.var_647)
            {
               (_loc7_ = this.superAnim.m_TheDO).y = this.var_11.y + const_562 * _loc4_;
               _loc7_.scaleX = 0.8 * (1 - _loc4_);
               _loc7_.scaleY = 0.8 * (1 - _loc4_);
            }
            return true;
         }
         if(this.var_2487)
         {
            if(!this.var_1.CanSendPacket())
            {
               return true;
            }
            if(_loc2_ - this.var_2614 < 350)
            {
               return true;
            }
            if(this.gearType)
            {
               _loc8_ = SoundConfig.var_1818;
            }
            else if(this.materialType)
            {
               _loc8_ = SoundConfig.var_1818;
            }
            else if(this.var_79)
            {
               _loc8_ = SoundConfig.var_2154;
            }
            else if(this.var_2169)
            {
               _loc8_ = SoundConfig.var_2158;
            }
            if(_loc8_)
            {
               SoundManager.Play(_loc8_,1);
            }
            (_loc9_ = new Packet(LinkUpdater.PKTTYPE_PICKUP_LOOTDROP)).method_9(this.lootID);
            this.var_1.serverConn.SendPacket(_loc9_);
            if(this.var_1509)
            {
               Game.var_172.method_142(_loc1_,null,this.var_1509,true,_loc1_.var_31);
               _loc1_.var_31 += this.var_1509;
               if(_loc1_.var_31 > _loc1_.const_156)
               {
                  _loc1_.var_31 = _loc1_.const_156;
               }
               this.var_1.method_114(_loc1_.var_31);
            }
            if(!this.materialType && !this.var_286 && !this.var_647)
            {
               this.superAnim.m_Seq.method_108();
            }
            this.var_2607 = true;
            this.var_2535 = _loc2_;
         }
         else
         {
            _loc10_ = this.superAnim.m_TheDO.getBounds(this.var_1.levelLayer as DisplayObject);
            _loc11_ = _loc1_.entType;
            _loc12_ = _loc1_.appearPosY;
            if((_loc13_ = _loc1_.appearPosX - _loc11_.width * 0.5) <= _loc10_.x + _loc10_.width && _loc13_ + _loc11_.width >= _loc10_.x && _loc12_ - _loc11_.height <= _loc10_.y + _loc10_.height && _loc12_ >= _loc10_.y)
            {
               this.var_2487 = true;
            }
         }
         return true;
      }
      
      public function method_946() : void
      {
         this.gearType = null;
         this.materialType = null;
         this.var_11 = null;
         this.superAnim.DestroySuperAnimInstance();
         this.superAnim = null;
         this.var_1 = null;
      }
   }
}
