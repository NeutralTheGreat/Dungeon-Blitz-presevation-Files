package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.utils.Dictionary;
   
   public class class_52 extends class_32
   {
      
      private static const const_149:uint = 4;
      
      public static const const_216:uint = 3;
      
      private static const const_687:Vector.<uint> = Vector.<uint>([0,4,5,6]);
      
      private static const const_911:Vector.<String> = Vector.<String>(["sentinel","justicar","templar"]);
      
      private static const const_1005:Vector.<String> = Vector.<String>(["executioner","shadowwalker","soulthief"]);
      
      private static const const_984:Vector.<String> = Vector.<String>(["flameseer","frostwarden","necromancer"]);
      
      private static const const_1204:Vector.<String> = Vector.<String>(["Sentinel","Justicar","Templar"]);
      
      private static const const_1067:Vector.<String> = Vector.<String>(["Viperblade","Shadowstalker","Soulthief"]);
      
      private static const const_910:Vector.<String> = Vector.<String>(["Flameseer","Frostbringer","Necromancer"]);
      
      private static const const_963:Vector.<String> = Vector.<String>(["Blessed by the Storm Gods, you draw enemy wrath upon your impregnable form and focus the tempest until you become the Lightning Avatar and smite all who stand before you.","With righteous fury from the Flame of Justice coursing through your body, you leap into the fray, a blaze of attacks swirling through the enemy ranks.","Infused with the Numinous Essence, you shine a searing, sacred light into the darkest places, healing the worthy and inflicting blinding agony upon the wicked."]);
      
      private static const const_1139:Vector.<String> = Vector.<String>(["You have forsaken all safety for the Pure Death; you know the perfect strike, the incurable venom, the hidden cut that dooms your chosen foe to certain annihilation.","You have sacrificed yourself to the Shadow Court, becoming a deadly trickster who strikes from afar, appears everywhere at once, and terrorizes enemies from the darkness.","You have mastered the heresies of the Codex Carnifex; you know that true pain comes with the death of the soul and that true victory takes a foe’s life force as your dark reward."]);
      
      private static const const_1174:Vector.<String> = Vector.<String>(["Touched by an Essence of Fire, you throw caution to the wind with every explosive inferno you unleash upon the enemy, incinerating all but leaving you vulnerable among the ashes.","Channeling the Eternal Winter, your icy conjurations keep the enemy hordes at bay and protect you from harm while a frozen doom descends upon all who oppose you.","Tainted by the Curse of Undeath, you fear no foe, raising armies of hungry ghouls to feast upon your unfortunate enemies, your own power and immortal essence grows with every victim they claim."]);
      
      public static const const_31:Dictionary = new Dictionary();
      
      public static const const_45:Dictionary = new Dictionary();
      
      private static const const_899:Vector.<Number> = Vector.<Number>([21,226,432]);
      
      {
         const_31["mage"] = const_984;
         const_31["paladin"] = const_911;
         const_31["rogue"] = const_1005;
         const_31["mageDisplay"] = const_910;
         const_31["paladinDisplay"] = const_1204;
         const_31["rogueDisplay"] = const_1067;
         const_31["mageDesc"] = const_1174;
         const_31["paladinDesc"] = const_963;
         const_31["rogueDesc"] = const_1139;
         const_45["sentinel"] = 0;
         const_45["justicar"] = 0;
         const_45["templar"] = 0;
         const_45["paladin"] = 0;
         const_45["executioner"] = 1;
         const_45["shadowwalker"] = 1;
         const_45["soulthief"] = 1;
         const_45["rogue"] = 1;
         const_45["flameseer"] = 2;
         const_45["frostwarden"] = 2;
         const_45["necromancer"] = 2;
         const_45["mage"] = 2;
      }
      
      public var var_2522:Boolean;
      
      private var mMasterClass:String;
      
      private var var_2941:uint;
      
      private var var_1558:Vector.<String>;
      
      private var var_2356:Vector.<String>;
      
      private var var_2201:Vector.<String>;
      
      private var var_560:Vector.<class_33>;
      
      private var var_1184:Vector.<class_33>;
      
      private var var_1349:Vector.<class_33>;
      
      private var var_1364:Vector.<class_33>;
      
      private var var_1605:Vector.<class_33>;
      
      private var var_1569:Vector.<class_33>;
      
      private var var_1389:Vector.<class_33>;
      
      public function class_52(param1:Game)
      {
         super(param1,"a_ScreenClassSelect",null);
         var_15 = true;
      }
      
      override public function OnCreateScreen() : void
      {
         var _loc1_:MovieClip = null;
         var _loc2_:MovieClip = null;
         var _loc4_:uint = 0;
         var _loc5_:MovieClip = null;
         var _loc6_:uint = 0;
         var _loc7_:class_33 = null;
         this.var_560 = new Vector.<class_33>(const_216,true);
         this.var_1184 = new Vector.<class_33>(const_216,true);
         this.var_1349 = new Vector.<class_33>(const_216,true);
         this.var_1364 = new Vector.<class_33>(const_216,true);
         this.var_1605 = new Vector.<class_33>();
         this.var_1569 = new Vector.<class_33>();
         this.var_1389 = new Vector.<class_33>();
         var _loc3_:uint = 0;
         while(_loc3_ < const_216)
         {
            _loc1_ = var_2["am_Panel" + _loc3_] as MovieClip;
            this.var_560[_loc3_] = method_1(_loc1_);
            this.var_1184[_loc3_] = method_1(_loc1_.am_Portrait);
            this.var_1349[_loc3_] = method_117(_loc1_.am_ChangeButton,_loc3_,this.method_687);
            this.var_1364[_loc3_] = method_117(_loc1_.am_KeepButton,_loc3_,this.method_687);
            _loc2_ = _loc1_.am_AbilityIconGroup;
            _loc4_ = 0;
            while(_loc4_ < const_149)
            {
               _loc5_ = _loc2_["am_AbilityIcon" + _loc4_] as MovieClip;
               _loc6_ = _loc3_ * const_149 + _loc4_;
               this.var_1569.push(method_3(_loc5_,_loc3_ * const_149 + _loc4_,null,this.method_1868,this.method_1238));
               this.var_1605.push(method_1(_loc5_.am_GlareAnim));
               (_loc7_ = method_1(_loc5_.am_Selector)).Hide();
               this.var_1389.push(_loc7_);
               _loc4_++;
            }
            _loc3_++;
         }
         this.var_1605.fixed;
         this.var_1569.fixed;
         this.var_1389.fixed;
         method_10(this.var_560[0].mMovieClip.am_Close,this.method_1041);
         var_2.cacheAsBitmap = true;
      }
      
      override public function OnDestroyScreen() : void
      {
         this.var_560 = null;
         this.var_1184 = null;
         this.var_1349 = null;
         this.var_1364 = null;
         this.var_1558 = null;
         this.var_2356 = null;
         this.var_2201 = null;
         this.var_1605 = null;
         this.var_1569 = null;
      }
      
      override public function OnRefreshScreen() : void
      {
         var _loc1_:MovieClip = null;
         var _loc2_:String = null;
         var _loc3_:PowerType = null;
         var _loc4_:class_10 = null;
         var _loc6_:uint = 0;
         var _loc7_:uint = 0;
         var _loc5_:uint = 0;
         while(_loc5_ < const_216)
         {
            _loc1_ = this.var_560[_loc5_].mMovieClip;
            _loc2_ = this.var_1558[_loc5_];
            this.var_1184[_loc5_].PlayAnimation(_loc2_);
            if(this.mMasterClass == _loc2_)
            {
               this.var_1364[_loc5_].Show();
               this.var_1349[_loc5_].Hide();
            }
            else
            {
               this.var_1364[_loc5_].Hide();
               this.var_1349[_loc5_].Show();
            }
            MathUtil.method_2(_loc1_.am_ClassName,this.var_2356[_loc5_]);
            MathUtil.method_2(_loc1_.am_ClassDescription,this.var_2201[_loc5_]);
            _loc6_ = 0;
            while(_loc6_ < const_149)
            {
               if(_loc4_ = class_14.var_526[_loc2_ + const_687[_loc6_]])
               {
                  _loc3_ = class_14.powerTypesDict[_loc4_.abilityName + 1];
                  if(_loc3_)
                  {
                     _loc7_ = _loc5_ * const_149 + _loc6_;
                     method_12(this.var_1569[_loc7_].mMovieClip.am_IconHolder.am_Button,_loc3_.iconName);
                  }
               }
               _loc6_++;
            }
            _loc5_++;
         }
      }
      
      public function OnInitDisplay() : void
      {
         var _loc2_:String = null;
         var _loc1_:Entity = var_1.clientEnt;
         if(_loc1_)
         {
            _loc2_ = _loc1_.entType.className.toLowerCase();
            this.mMasterClass = _loc1_.mMasterClass;
            this.var_1558 = const_31[_loc2_];
            this.var_2356 = const_31[_loc2_ + "Display"];
            this.var_2201 = const_31[_loc2_ + "Desc"];
            this.var_2941 = const_45[_loc2_];
         }
         var_1.screenHudTooltip.HideTooltip(true);
         if(this.var_2522)
         {
            var_656.Show();
            this.var_2522 = false;
         }
      }
      
      private function method_687(param1:MouseEvent, param2:uint) : void
      {
         var _loc6_:Entity = null;
         var _loc7_:int = 0;
         var _loc8_:Packet = null;
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_ || !var_1.CanSendPacket())
         {
            return;
         }
         var _loc4_:String = _loc3_.entType.className;
         var _loc5_:String;
         if(!(_loc5_ = this.var_1558[param2]) || const_31[_loc4_.toLowerCase()].indexOf(_loc5_) < 0)
         {
            return;
         }
         for each(_loc6_ in var_1.entities)
         {
            if(Boolean(_loc6_.cue) && _loc6_.cue.characterName == "Special_ClassTower")
            {
               _loc6_.method_397(Entity.const_282);
               break;
            }
         }
         var_1.bWaitingForChangeMasterClassResponse = true;
         _loc7_ = Game.method_766(_loc5_);
         (_loc8_ = new Packet(LinkUpdater.const_767)).method_9(var_1.clientEntID);
         _loc8_.method_20(Game.const_209,_loc7_);
         var_1.serverConn.SendPacket(_loc8_);
         var_1.screenClassTowers.Display();
         Hide();
      }
      
      private function method_1041(param1:MouseEvent) : void
      {
         Hide();
         if(Boolean(var_1.clientEnt) && var_1.clientEnt.getTowerLevel() > 0)
         {
            var_1.screenClassTowers.Display();
         }
      }
      
      private function method_1868(param1:MouseEvent, param2:uint) : void
      {
         var _loc3_:Entity = var_1.clientEnt;
         if(!_loc3_)
         {
            return;
         }
         var _loc4_:uint = uint(param2 / const_149);
         var _loc5_:String = this.var_1558[_loc4_];
         var _loc6_:class_10;
         if(!(_loc6_ = class_14.var_526[_loc5_ + const_687[param2 % const_149]]))
         {
            return;
         }
         var _loc7_:PowerType;
         if(!(_loc7_ = _loc3_.GetPowerFromAbilityType(_loc6_)))
         {
            return;
         }
         var_1.screenHudTooltip.ShowPowerTooltip(_loc3_,_loc7_,406,const_899[_loc4_],class_101.const_825);
         this.var_1605[param2].PlayAnimation("Glare");
         this.var_1389[param2].Show();
      }
      
      private function method_1238(param1:MouseEvent, param2:uint) : void
      {
         var_1.screenHudTooltip.HideTooltip(true);
         this.var_1389[param2].Hide();
      }
   }
}
