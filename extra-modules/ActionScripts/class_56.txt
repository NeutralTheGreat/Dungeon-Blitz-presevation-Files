package
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.geom.Rectangle;
   import flash.text.*;
   
   public class class_56
   {
      
      private static const const_385:uint = 0;
      
      private static const const_428:uint = 1;
      
      private static const const_530:uint = 2;
      
      private static const const_468:uint = 18;
      
      private static const const_724:String = "<font color=\'#7FFFFF\'>";
      
      private static const const_1172:Vector.<String> = Vector.<String>(["Friends","Guild","Ignore","Zone"]);
      
      private static const const_539:String = "<font color=\'#77AAFF\'>";
      
      private static const const_992:String = "<font color=\'#666666\'>";
       
      
      internal var var_1:Game;
      
      internal var var_26:MovieClip = null;
      
      internal var var_14:MovieClip = null;
      
      internal var var_335:MovieClip = null;
      
      internal var var_574:MovieClip = null;
      
      internal var var_2216:int = 0;
      
      internal var var_2185:int = 0;
      
      internal var var_2302:int = 0;
      
      internal var var_2389:int = 0;
      
      internal var var_2385:Boolean = false;
      
      internal var var_2333:Boolean = false;
      
      internal var var_2257:Boolean = false;
      
      internal var var_2109:Boolean = false;
      
      internal var var_2772:Boolean = false;
      
      public function class_56(param1:Game)
      {
         super();
         this.var_1 = param1;
      }
      
      public function method_1803() : void
      {
         if(this.var_26)
         {
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_26.am_FriendsTab);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_26.am_GuildTab);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_26.am_ZoneTab);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_26.am_IgnoreTab);
            this.method_1849();
            this.method_1704();
            this.method_1403();
            this.method_1830();
            this.var_1.method_1878(this.var_26);
         }
         if(Boolean(this.var_335) && Boolean(this.var_335.parent))
         {
            this.var_335.parent.removeChild(this.var_335);
         }
         this.var_335 = null;
         if(Boolean(this.var_574) && Boolean(this.var_574.parent))
         {
            this.var_574.parent.removeChild(this.var_574);
         }
         this.var_574 = null;
         this.method_458();
         this.var_26 = null;
         this.var_1 = null;
      }
      
      public function Hide() : void
      {
         this.method_126();
         this.var_1.method_158(this.var_26);
      }
      
      public function Toggle() : void
      {
         if(this.method_40())
         {
            this.Hide();
         }
         else
         {
            this.Display();
         }
      }
      
      public function method_40() : Boolean
      {
         return Boolean(this.var_26) && this.var_26.visible;
      }
      
      public function method_1496(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = param1.target as MovieClip;
         this.method_126();
         param1.stopPropagation();
      }
      
      public function Display() : void
      {
         if(!this.var_26)
         {
            this.var_26 = this.var_1.method_1398("a_FriendWindow",this.method_1496);
            this.var_26.scaleX = 1.2;
            this.var_26.scaleY = 1.2;
            this.var_26.x = 370;
            this.var_26.y = 658 - this.var_26.height;
            this.var_26.visible = false;
            this.var_1.UIBasicButton_CreateBasicButton(this.var_26.am_FriendsTab,this.method_1232,null,false,true);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_26.am_GuildTab,this.method_1452,null,false,true);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_26.am_ZoneTab,this.method_1638,null,false,true);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_26.am_IgnoreTab,this.method_1700,null,false,true);
            this.method_278("Friends");
            this.var_574 = class_4.method_16("a_FriendLineGrayBack");
            this.method_486();
         }
         if(!this.var_26.visible)
         {
            this.var_1.method_127();
            this.var_26.visible = true;
            this.var_1.var_89.addChild(this.var_26);
         }
         this.method_489(this.var_1.friendList);
         this.method_392(this.var_1.var_1004);
         this.method_159(this.var_1.var_124);
         this.method_246(this.var_1.var_340);
         this.method_481();
      }
      
      private function method_278(param1:String) : void
      {
         var _loc2_:String = null;
         for each(_loc2_ in const_1172)
         {
            if(_loc2_ != param1)
            {
               this.method_1780(_loc2_);
            }
         }
         this.method_1685(param1);
      }
      
      public function method_458() : void
      {
         if(Boolean(this.var_14) && Boolean(this.var_14.parent))
         {
            this.var_14.parent.removeChild(this.var_14);
         }
         this.var_14 = null;
      }
      
      public function method_486() : void
      {
         this.var_14 = class_4.method_16("a_FriendPopup");
         this.var_14.mouseChildren = true;
         this.var_14.visible = false;
         this.var_26.addChild(this.var_14);
      }
      
      public function method_362(param1:MovieClip) : void
      {
         var _loc2_:int = 0;
         var _loc3_:MovieClip = null;
         _loc2_ = 0;
         while(_loc2_ < param1.numChildren)
         {
            _loc3_ = param1.getChildAt(_loc2_) as MovieClip;
            _loc3_.dyn_Function = null;
            _loc3_.dyn_Friend = null;
            _loc3_.visible = false;
            _loc2_++;
         }
         param1.visible = false;
      }
      
      public function method_33(param1:MovieClip, param2:String, param3:String = "", param4:Function = null, param5:Friend = null) : MovieClip
      {
         var _loc8_:int = 0;
         var _loc6_:MovieClip = null;
         var _loc7_:MovieClip = null;
         _loc8_ = 0;
         while(_loc8_ < param1.numChildren)
         {
            if(!(_loc7_ = param1.getChildAt(_loc8_) as MovieClip).visible)
            {
               _loc6_ = _loc7_;
               break;
            }
            _loc8_++;
         }
         if(!_loc6_)
         {
            (_loc6_ = class_4.method_16("a_FriendPopupOption")).gotoAndStop("Ready");
            _loc6_.y = _loc6_.height * param1.numChildren - 0.5;
            this.var_1.UIBasicButton_CreateBasicButton(_loc6_,this.method_452,null,false,true);
            _loc6_.addEventListener(MouseEvent.ROLL_OVER,this.method_442);
            _loc6_.addEventListener(MouseEvent.ROLL_OUT,this.method_463);
            param1.addChild(_loc6_);
         }
         _loc6_.dyn_Callback = param4;
         _loc6_.dyn_Friend = param5;
         _loc6_.visible = true;
         MathUtil.method_2(_loc6_.am_Text,const_724 + param2 + class_127.var_121,true);
         MathUtil.method_2(_loc6_.am_Keys,const_724 + param3 + class_127.var_121,true);
         return _loc6_;
      }
      
      public function method_442(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = param1.currentTarget as MovieClip;
         if(_loc2_.dyn_Callback != null)
         {
            _loc2_.gotoAndStop("Over");
         }
      }
      
      public function method_463(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = param1.currentTarget as MovieClip;
         if(_loc2_.dyn_Callback != null)
         {
            _loc2_.gotoAndStop("Ready");
         }
      }
      
      public function method_126() : void
      {
         if(this.var_14)
         {
            this.var_14.visible = false;
         }
         this.method_481();
      }
      
      public function method_206(param1:MovieClip, param2:String) : void
      {
         if(!this.var_14 || !this.var_14.parent)
         {
            return;
         }
         var _loc3_:Friend = param1.dyn_Friend as Friend;
         this.method_362(this.var_14);
         this.method_666(this.var_335);
         var _loc4_:Rectangle = param1.getBounds(this.var_14.parent);
         this.var_14.visible = true;
         this.var_14.x = _loc4_.x;
         this.var_14.y = _loc4_.y + _loc4_.height + -1;
         var _loc5_:uint = !!this.var_1.clientEnt ? this.var_1.clientEnt.var_2039 : 0;
         if(param2 == "Friends" && _loc3_.var_276)
         {
            if(Boolean(_loc3_.charName) && _loc3_.var_207 != _loc3_.charName)
            {
               this.method_33(this.var_14,"(" + _loc3_.var_207 + ")");
            }
            this.method_33(this.var_14,"  Accept friend invite","",this.method_425,_loc3_);
            this.method_33(this.var_14,"  Quietly decline","",this.method_455,_loc3_);
         }
         else if(param2 == "Friends" && _loc3_.bOnline)
         {
            if(Boolean(_loc3_.charName) && _loc3_.var_207 != _loc3_.charName)
            {
               this.method_33(this.var_14,"(" + _loc3_.var_207 + ")");
            }
            this.method_33(this.var_14,"  Invite to party","",this.method_188,_loc3_);
            this.method_33(this.var_14,"  Join their party","",this.method_323,_loc3_);
            this.method_33(this.var_14,"  Tell...","",this.method_202,_loc3_);
            this.method_33(this.var_14,"  Goto house","",this.method_312,_loc3_);
         }
         else if(param2 == "Friends")
         {
            this.method_33(this.var_14,"  Unfriend","",this.method_949,_loc3_);
            this.method_33(this.var_14,"  Goto house","",this.method_312,_loc3_);
         }
         else if(param2 == "Guild")
         {
            this.method_33(this.var_14,"  Invite to party","",this.method_188,_loc3_);
            this.method_33(this.var_14,"  Join their party","",this.method_323,_loc3_);
            this.method_33(this.var_14,"  Invite to friend list","",this.method_284,_loc3_);
            this.method_33(this.var_14,"  Tell...","",this.method_202,_loc3_);
            if(_loc5_ == Entity.const_236 && _loc3_.var_289 == Entity.const_309)
            {
               this.method_33(this.var_14,"  Promote to Officer","",this.method_435,_loc3_);
            }
            else if(_loc5_ <= Entity.const_139 && _loc3_.var_289 == Entity.const_308)
            {
               this.method_33(this.var_14,"  Promote to Member","",this.method_435,_loc3_);
            }
            else if(_loc5_ <= Entity.const_139 && _loc3_.var_289 == Entity.const_470)
            {
               this.method_33(this.var_14,"  Promote to Initiate","",this.method_435,_loc3_);
            }
            if(_loc5_ == Entity.const_236 && _loc3_.var_289 == Entity.const_139)
            {
               this.method_33(this.var_14,"  Demote to Member","",this.method_422,_loc3_);
            }
            else if(_loc5_ <= Entity.const_139 && _loc3_.var_289 == Entity.const_309)
            {
               this.method_33(this.var_14,"  Demote to Initiate","",this.method_422,_loc3_);
            }
            else if(_loc5_ <= Entity.const_139 && _loc3_.var_289 == Entity.const_308)
            {
               this.method_33(this.var_14,"  Demote to Silenced","",this.method_422,_loc3_);
            }
            if(_loc5_ <= Entity.const_139 && _loc5_ < _loc3_.var_289)
            {
               this.method_33(this.var_14,"  Remove from guild","",this.method_1282,_loc3_);
            }
         }
         else if(param2 == "Zone")
         {
            this.method_33(this.var_14,"  Invite to party","",this.method_188,_loc3_);
            this.method_33(this.var_14,"  Invite to friend list","",this.method_284,_loc3_);
            this.method_33(this.var_14,"  Ignore","",this.method_449,_loc3_);
            this.method_33(this.var_14,"  Tell...","",this.method_202,_loc3_);
         }
         else if(param2 == "Ignore")
         {
            this.method_33(this.var_14,"Unignore","",this.method_910,_loc3_);
         }
      }
      
      public function method_312(param1:Friend) : void
      {
         var _loc2_:String = null;
         var _loc3_:Boolean = false;
         if(param1.charName)
         {
            _loc3_ = true;
            _loc2_ = param1.charName;
         }
         else
         {
            _loc3_ = false;
            _loc2_ = param1.var_207;
         }
         this.var_1.method_312(_loc2_,_loc3_);
      }
      
      public function method_452(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = param1.target as MovieClip;
         this.method_126();
         var _loc3_:Function = _loc2_.dyn_Callback;
         var _loc4_:Friend = _loc2_.dyn_Friend;
         if(_loc3_ != null)
         {
            _loc3_(_loc4_);
         }
         param1.stopPropagation();
      }
      
      public function method_188(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/invite " + param1.charName);
      }
      
      public function method_323(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/Join " + param1.charName);
      }
      
      public function method_284(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/friend " + param1.charName);
      }
      
      public function method_435(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/guildpromote " + param1.charName);
      }
      
      public function method_422(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/guilddemote " + param1.charName);
      }
      
      public function method_1282(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/guildkick " + param1.charName);
      }
      
      public function method_202(param1:Friend) : void
      {
         this.var_1.screenChat.BeginChat("/tell " + param1.charName + " ");
      }
      
      public function method_449(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/ignore " + param1.charName);
      }
      
      public function method_910(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/ignore " + param1.charName);
      }
      
      public function method_949(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/unfriend " + param1.var_207);
      }
      
      public function method_425(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/acceptfriend " + param1.var_207);
      }
      
      public function method_455(param1:Friend) : void
      {
         this.var_1.screenChat.TryToProcessChatAsLocalCommand("/declinefriend " + param1.var_207);
      }
      
      public function method_1941(param1:MouseEvent) : void
      {
         this.var_1.screenChat.BeginChat("/friend ");
         param1.stopPropagation();
      }
      
      public function method_1169(param1:MouseEvent) : void
      {
         this.var_1.screenChat.BeginChat("/ignore ");
         param1.stopPropagation();
      }
      
      private function method_980(param1:MouseEvent) : void
      {
         this.method_206(param1.target as MovieClip,"Friends");
         param1.stopPropagation();
      }
      
      private function method_890(param1:MouseEvent) : void
      {
         this.method_206(param1.target as MovieClip,"Guild");
         param1.stopPropagation();
      }
      
      private function method_989(param1:MouseEvent) : void
      {
         this.method_206(param1.target as MovieClip,"Zone");
         param1.stopPropagation();
      }
      
      private function method_705(param1:MouseEvent) : void
      {
         this.method_206(param1.target as MovieClip,"Ignore");
         param1.stopPropagation();
      }
      
      public function method_1232(param1:MouseEvent) : void
      {
         this.method_278("Friends");
         this.method_489(this.var_1.friendList);
         param1.stopPropagation();
      }
      
      public function method_1638(param1:MouseEvent) : void
      {
         this.method_278("Zone");
         this.method_392(this.var_1.var_1004);
         param1.stopPropagation();
      }
      
      public function method_1700(param1:MouseEvent) : void
      {
         this.method_278("Ignore");
         this.method_246(this.var_1.var_340);
         param1.stopPropagation();
      }
      
      public function method_1452(param1:MouseEvent) : void
      {
         this.method_278("Guild");
         this.method_159(this.var_1.var_124);
         param1.stopPropagation();
      }
      
      public function method_1780(param1:String) : void
      {
         var _loc2_:MovieClip = this.var_26.getChildByName("am_" + param1 + "Panel") as MovieClip;
         _loc2_.visible = false;
         var _loc3_:MovieClip = this.var_26.getChildByName("am_" + param1 + "Tab") as MovieClip;
         _loc3_.am_Tab.visible = false;
      }
      
      public function method_1685(param1:String) : void
      {
         var _loc2_:MovieClip = this.var_26.getChildByName("am_" + param1 + "Panel") as MovieClip;
         _loc2_.visible = true;
         var _loc3_:MovieClip = this.var_26.getChildByName("am_" + param1 + "Tab") as MovieClip;
         _loc3_.am_Tab.visible = true;
      }
      
      public function method_359(param1:String) : Boolean
      {
         if(!this.var_26 || !this.var_26.visible)
         {
            return false;
         }
         var _loc2_:MovieClip = this.var_26.getChildByName("am_" + param1 + "Panel") as MovieClip;
         return _loc2_.visible;
      }
      
      public function method_481() : void
      {
         if(this.var_335 && !this.var_14.visible && this.var_574 && this.var_574.parent == this.var_335)
         {
            this.var_335.removeChild(this.var_574);
         }
         this.var_335 = null;
      }
      
      public function method_666(param1:MovieClip) : void
      {
         this.var_335 = param1;
         if(Boolean(this.var_335) && !this.var_14.visible)
         {
            this.var_335.addChildAt(this.var_574,0);
         }
      }
      
      public function method_677(param1:MouseEvent) : void
      {
         var _loc2_:MovieClip = param1.target as MovieClip;
         this.method_666(_loc2_);
      }
      
      public function method_585(param1:MouseEvent) : void
      {
         this.method_481();
      }
      
      public function method_363(param1:MovieClip, param2:Function) : void
      {
         var _loc6_:MovieClip = null;
         var _loc3_:int = 0;
         var _loc4_:Number = 0;
         var _loc7_:MovieClip = param1.am_List;
         while(_loc7_.numChildren)
         {
            _loc7_.removeChildAt(0);
         }
         _loc3_ = 0;
         while(_loc3_ < const_468)
         {
            (_loc6_ = class_4.method_16("a_FriendLine")).mouseEnabled = true;
            _loc6_.x = 0;
            _loc6_.y = _loc4_;
            _loc6_.addEventListener(MouseEvent.MOUSE_DOWN,param2);
            _loc6_.addEventListener(MouseEvent.ROLL_OVER,this.method_677);
            _loc6_.addEventListener(MouseEvent.ROLL_OUT,this.method_585);
            _loc7_.addChild(_loc6_);
            _loc6_.dyn_Friend = null;
            _loc6_.visible = false;
            _loc4_ += _loc6_.height;
            _loc3_++;
         }
         var _loc8_:class_152;
         (_loc8_ = new class_152(param1.am_ChatUp,param1.am_ChatDown,param1.am_ChatScroll,const_468,this.method_1749(this.method_1449,[param1]))).method_984(0);
         param1.dyn_scroll = _loc8_;
      }
      
      private function method_1749(param1:Function, param2:Array) : Function
      {
         var method:Function = param1;
         var additionalArguments:Array = param2;
         return function(param1:int):void
         {
            method.apply(null,[param1].concat(additionalArguments));
         };
      }
      
      private function method_1449(param1:int, param2:MovieClip) : void
      {
         if(param2.name == "am_FriendsPanel")
         {
            this.var_2216 = param1;
            this.method_145(this.var_2216,this.var_1.friendList,param2,const_385);
         }
         else if(param2.name == "am_GuildPanel")
         {
            this.var_2185 = param1;
            this.method_145(this.var_2185,this.var_1.var_124,param2,const_530);
         }
         else if(param2.name == "am_IgnorePanel")
         {
            this.var_2389 = param1;
            this.method_145(this.var_2389,this.var_1.var_340,param2,const_428);
         }
         else if(param2.name == "am_ZonePanel")
         {
            this.var_2302 = param1;
            this.method_145(this.var_2302,this.var_1.var_1004,param2,const_385);
         }
      }
      
      public function method_145(param1:int, param2:Vector.<Friend>, param3:MovieClip, param4:uint) : void
      {
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         var _loc7_:String = null;
         var _loc8_:String = null;
         var _loc10_:Friend = null;
         var _loc11_:MovieClip = null;
         var _loc13_:String = null;
         _loc5_ = param1;
         _loc6_ = 0;
         while(_loc5_ < param1 + const_468)
         {
            _loc10_ = _loc5_ < param2.length ? param2[_loc5_] : null;
            _loc11_ = param3.am_List.getChildAt(_loc6_);
            if(_loc10_)
            {
               _loc11_.visible = true;
               _loc11_.dyn_Friend = _loc10_;
               if(param4 == const_428)
               {
                  MathUtil.method_2(_loc11_.am_Name,_loc10_.charName,true);
                  MathUtil.method_2(_loc11_.am_Zone,"",true);
               }
               else if(!_loc10_.bOnline)
               {
                  MathUtil.method_2(_loc11_.am_Name,_loc10_.var_207,true);
                  if(_loc10_.var_276)
                  {
                     MathUtil.method_2(_loc11_.am_Zone,const_539 + "Pending" + class_127.var_121,true);
                  }
                  else
                  {
                     MathUtil.method_2(_loc11_.am_Zone,const_992 + "Offline" + class_127.var_121,true);
                  }
               }
               else
               {
                  _loc7_ = _loc10_.charName + ", Level " + _loc10_.var_2100 + " " + _loc10_.className;
                  _loc8_ = !!_loc10_.var_2659 ? _loc10_.var_2659 : "Online";
                  if(_loc10_.var_276)
                  {
                     _loc7_ = const_539 + _loc7_ + class_127.var_121;
                     _loc8_ = const_539 + "Pending" + class_127.var_121;
                  }
                  if(param4 == const_530)
                  {
                     if(_loc10_.var_289 == Entity.const_236)
                     {
                        _loc13_ = "[L]";
                     }
                     else if(_loc10_.var_289 == Entity.const_139)
                     {
                        _loc13_ = "[O]";
                     }
                     else if(_loc10_.var_289 == Entity.const_309)
                     {
                        _loc13_ = "[M]";
                     }
                     else if(_loc10_.var_289 == Entity.const_308)
                     {
                        _loc13_ = "[I]";
                     }
                     else if(_loc10_.var_289 == Entity.const_470)
                     {
                        _loc13_ = "[S]";
                     }
                     _loc7_ = _loc13_ + " " + _loc7_;
                  }
                  MathUtil.method_2(_loc11_.am_Name,_loc7_,true);
                  MathUtil.method_2(_loc11_.am_Zone,_loc8_,true);
               }
            }
            else
            {
               _loc11_.visible = false;
               _loc11_.dyn_Friend = null;
            }
            _loc5_++;
            _loc6_++;
         }
         var _loc9_:class_152;
         (_loc9_ = param3.dyn_scroll).method_984(param2.length);
      }
      
      public function method_289(param1:MovieClip, param2:Function) : void
      {
         var _loc5_:MovieClip = null;
         var _loc3_:int = 0;
         var _loc4_:MovieClip = param1.am_List;
         _loc3_ = 0;
         while(_loc3_ < _loc4_.numChildren)
         {
            (_loc5_ = _loc4_.getChildAt(_loc3_) as MovieClip).removeEventListener(MouseEvent.MOUSE_DOWN,param2);
            _loc5_.removeEventListener(MouseEvent.ROLL_OVER,this.method_677);
            _loc5_.removeEventListener(MouseEvent.ROLL_OUT,this.method_585);
            _loc3_++;
         }
      }
      
      public function method_1521() : void
      {
         this.method_363(this.var_26.am_FriendsPanel,this.method_980);
         this.var_1.UIBasicButton_CreateBasicButton(this.var_26.am_FriendsPanel.am_AddFriendButton,this.method_1941,class_19.method_254("am_AddFriendButton"));
         this.var_2333 = true;
      }
      
      public function method_489(param1:Vector.<Friend>, param2:Boolean = true) : void
      {
         var _loc5_:Friend = null;
         var _loc6_:Packet = null;
         if(!this.method_359("Friends") || !this.var_1.CanSendPacket())
         {
            return;
         }
         if(!this.var_2333)
         {
            this.method_1521();
         }
         this.method_126();
         if(param2)
         {
            _loc6_ = new Packet(LinkUpdater.const_913);
            this.var_1.serverConn.SendPacket(_loc6_);
         }
         var _loc3_:uint = 0;
         var _loc4_:uint = param1.length;
         for each(_loc5_ in param1)
         {
            if(_loc5_.bOnline)
            {
               _loc3_++;
            }
         }
         if(_loc4_)
         {
            MathUtil.method_2(this.var_26.am_FriendsPanel.am_Count,_loc3_ + " of " + _loc4_ + " friends online.");
         }
         else
         {
            MathUtil.method_2(this.var_26.am_FriendsPanel.am_Count,"");
         }
         this.method_145(this.var_2216,param1,this.var_26.am_FriendsPanel,const_385);
      }
      
      public function method_1849() : void
      {
         this.method_289(this.var_26.am_FriendsPanel,this.method_980);
         this.var_1.UIBasicButton_DestroyBasicButton(this.var_26.am_FriendsPanel.am_AddFriend);
         this.var_2333 = false;
      }
      
      public function method_1680() : void
      {
         this.method_363(this.var_26.am_GuildPanel,this.method_890);
         this.var_2385 = true;
      }
      
      public function method_159(param1:Vector.<Friend>) : void
      {
         if(!this.method_359("Guild"))
         {
            return;
         }
         if(!this.var_2385)
         {
            this.method_1680();
         }
         this.method_126();
         if(Boolean(this.var_1.clientEnt) && Boolean(this.var_1.clientEnt.var_1931))
         {
            MathUtil.method_2(this.var_26.am_GuildPanel.am_GuildName,this.var_1.clientEnt.var_1931);
         }
         else
         {
            MathUtil.method_2(this.var_26.am_GuildPanel.am_GuildName,"You aren\'t in a guild.");
         }
         var _loc2_:uint = param1.length;
         if(!this.var_1.clientEnt || !this.var_1.clientEnt.var_1931)
         {
            MathUtil.method_2(this.var_26.am_GuildPanel.am_Count,"");
         }
         else if(!_loc2_)
         {
            MathUtil.method_2(this.var_26.am_GuildPanel.am_Count,"No members online.");
         }
         else if(_loc2_ == 1)
         {
            MathUtil.method_2(this.var_26.am_GuildPanel.am_Count,"1 member online.");
         }
         else
         {
            MathUtil.method_2(this.var_26.am_GuildPanel.am_Count,_loc2_ + " members online.");
         }
         this.method_145(this.var_2185,param1,this.var_26.am_GuildPanel,const_530);
      }
      
      public function method_1704() : void
      {
         this.method_289(this.var_26.am_GuildPanel,this.method_890);
         this.var_2385 = false;
      }
      
      public function method_1790() : void
      {
         this.method_363(this.var_26.am_ZonePanel,this.method_989);
         this.var_2257 = true;
      }
      
      public function method_392(param1:Vector.<Friend>, param2:Boolean = true) : void
      {
         var _loc4_:Packet = null;
         if(!this.method_359("Zone") || !this.var_1.CanSendPacket())
         {
            return;
         }
         if(!this.var_2257)
         {
            this.method_1790();
         }
         this.method_126();
         if(param2)
         {
            _loc4_ = new Packet(LinkUpdater.const_1302);
            this.var_1.serverConn.SendPacket(_loc4_);
         }
         var _loc3_:uint = param1.length;
         if(!_loc3_)
         {
            MathUtil.method_2(this.var_26.am_ZonePanel.am_Zone,"No players in this area.");
         }
         else if(_loc3_ == 1)
         {
            MathUtil.method_2(this.var_26.am_ZonePanel.am_Zone,"1 player in this area.");
         }
         else
         {
            MathUtil.method_2(this.var_26.am_ZonePanel.am_Zone,_loc3_ + " players in this area.");
         }
         this.method_145(this.var_2302,param1,this.var_26.am_ZonePanel,const_385);
      }
      
      public function method_1403() : void
      {
         this.method_289(this.var_26.am_ZonePanel,this.method_989);
         this.var_2257 = false;
      }
      
      public function method_1764() : void
      {
         this.method_363(this.var_26.am_IgnorePanel,this.method_705);
         this.var_1.UIBasicButton_CreateBasicButton(this.var_26.am_IgnorePanel.am_AddIgnoreButton,this.method_1169,class_19.method_254("am_AddIgnoreButton"));
         this.var_2109 = true;
      }
      
      public function method_246(param1:Vector.<Friend>) : void
      {
         var _loc3_:Packet = null;
         if(!this.method_359("Ignore") || !this.var_1.CanSendPacket())
         {
            return;
         }
         if(!this.var_2109)
         {
            this.method_1764();
         }
         this.method_126();
         if(!this.var_2772)
         {
            _loc3_ = new Packet(LinkUpdater.const_1052);
            this.var_1.serverConn.SendPacket(_loc3_);
            this.var_2772 = true;
         }
         var _loc2_:uint = param1.length;
         if(!_loc2_)
         {
            MathUtil.method_2(this.var_26.am_IgnorePanel.am_Count,"");
         }
         else if(_loc2_ == 1)
         {
            MathUtil.method_2(this.var_26.am_IgnorePanel.am_Count,"You are ignoring 1 player.");
         }
         else
         {
            MathUtil.method_2(this.var_26.am_IgnorePanel.am_Count,"You are ignoring " + _loc2_ + " players.");
         }
         this.method_145(this.var_2389,param1,this.var_26.am_IgnorePanel,const_428);
      }
      
      public function method_1830() : void
      {
         this.method_289(this.var_26.am_IgnorePanel,this.method_705);
         this.var_2109 = false;
      }
   }
}
