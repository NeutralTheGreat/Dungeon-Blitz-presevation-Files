package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.display.StageQuality;
   import flash.events.MouseEvent;
   import flash.system.ApplicationDomain;
   import flash.text.TextField;
   import flash.utils.Dictionary;
   import flash.utils.getQualifiedClassName;
   
   public class class_102 extends class_32
   {
      
      private static const const_1294:uint = 2;
      
      private static const const_235:uint = 0;
      
      private static const const_202:uint = 1;
      
      private static const const_183:String = "Hair";
      
      private static const const_189:String = "Skin";
      
      private static const const_387:Dictionary = new Dictionary();
      
      private static const const_396:String = "Male";
      
      private static const const_350:String = "Female";
      
      private static const const_942:Number = 6;
      
      public static const const_1384:uint = 100;
      
      private static const const_90:Number = -128;
      
      private static const const_148:Dictionary = new Dictionary();
      
      public static const const_18:Dictionary = new Dictionary();
      
      public static const const_3:Dictionary = new Dictionary();
      
      public static const const_5:Dictionary = new Dictionary();
      
      public static const const_2:Dictionary = new Dictionary();
      
      {
         const_387[const_235] = const_183;
         const_387[const_202] = const_189;
         const_148["Paladin_Male"] = EntType.PALADIN_OPTIONS_FILE;
         const_148["Paladin_Female"] = EntType.PALADIN_OPTIONS_FILE;
         const_148["Mage_Female"] = EntType.MAGE_OPTIONS_FILE;
         const_148["Mage_Male"] = EntType.MAGE_OPTIONS_FILE;
         const_148["Rogue_Male"] = EntType.ROGUE_OPTIONS_FILE;
         const_148["Rogue_Female"] = EntType.ROGUE_OPTIONS_FILE;
         const_18["Mage_Female_Head01"] = "Pretty Proportional";
         const_18["Mage_Female_Head02"] = "The Tophat";
         const_18["Mage_Female_Head03"] = "Little Women";
         const_18["Mage_Male_Head01"] = "Lookin\' Good";
         const_18["Mage_Male_Head02"] = "Long And Tall";
         const_18["Mage_Male_Head03"] = "The Pinch";
         const_18["Paladin_Male_Basic"] = "All Around Average";
         const_18["Paladin_Male_Large"] = "Snap Into A Slim Trim";
         const_18["Paladin_Male_Long"] = "Itty Bitty";
         const_18["Paladin_Male_Short"] = "Large And In Charge";
         const_18["Paladin_Female_FBasic"] = "Urban Basics";
         const_18["Paladin_Female_FLarge"] = "Big Girl";
         const_18["Paladin_Female_FLong"] = "Let\'s Get Down To It";
         const_18["Paladin_Female_FShort"] = "The Vogue";
         const_18["Rogue_Male_MaleHead"] = "The Continental";
         const_18["Rogue_Male_MaleHead2"] = "Round And Ready";
         const_18["Rogue_Male_MaleHead3"] = "Bring It In Tight";
         const_18["Rogue_Female_FemaleHead"] = "Sweet Sixteen";
         const_18["Rogue_Female_FemaleHead02"] = "Long Linda";
         const_18["Rogue_Female_FemaleHead03"] = "Witch Doctor\'s Curse";
         const_3["Mage_Female_F01"] = "Highschool Sweetheart";
         const_3["Mage_Female_F02"] = "The Urban Stare";
         const_3["Mage_Female_F03"] = "I\'m Better Than You";
         const_3["Mage_Female_F04"] = "Saucy Bird";
         const_3["Mage_Female_F05"] = "Mean Girl";
         const_3["Mage_Female_F06"] = "Eye Heart U";
         const_3["Mage_Female_F07"] = "Velvet Painting";
         const_3["Mage_Female_F08"] = "Hell Hath No Fury";
         const_3["Mage_Female_F09"] = "Evil Princess";
         const_3["Mage_Female_F10"] = "Into the Sun";
         const_3["Mage_Female_F11"] = "Finger Paint Heroes";
         const_3["Mage_Female_F12"] = "Village Elder";
         const_3["Mage_Female_F13"] = "Jane, Jane Bond";
         const_3["Mage_Female_F14"] = "Mascara Massacre";
         const_3["Mage_Male_MF01"] = "Stay Off My Lawn";
         const_3["Mage_Male_MF02"] = "Die Hard";
         const_3["Mage_Male_MF03"] = "On The Prowl";
         const_3["Mage_Male_MF04"] = "Partied Too Hard";
         const_3["Mage_Male_MF05"] = "Butler Blocks";
         const_3["Mage_Male_MF06"] = "Blank In The Face";
         const_3["Mage_Male_MF07"] = "Such A Good Kid";
         const_3["Mage_Male_MF08"] = "Bake Sale Warlord";
         const_3["Mage_Male_MF09"] = "Death And Taxes";
         const_3["Mage_Male_MF10"] = "The Void";
         const_3["Mage_Male_MF11"] = "Offroad Makeover";
         const_3["Mage_Male_MF12"] = "A Road Well Traveled";
         const_3["Mage_Male_MF13"] = "Dots N\' Spots";
         const_3["Mage_Male_MF14"] = "Spirits Of War";
         const_3["Mage_Male_MF15"] = "Wink Of The Warlock";
         const_3["Paladin_Male_F02"] = "Lets Be Serious";
         const_3["Paladin_Male_F03"] = "The Pretty Boy";
         const_3["Paladin_Male_F04"] = "Whiskey Sour Smile";
         const_3["Paladin_Male_F05"] = "I Don\'t Wanna Ask Again";
         const_3["Paladin_Male_F06"] = "Mean Muggin\'";
         const_3["Paladin_Male_F07"] = "I Apologize For Nothing";
         const_3["Paladin_Male_F01"] = "Which Way Did He Go Doc";
         const_3["Paladin_Male_F08"] = "Big Brow Grit";
         const_3["Paladin_Male_F09"] = "In It To Win It";
         const_3["Paladin_Male_F10"] = "Escape From New York";
         const_3["Paladin_Male_F11"] = "The Bandit";
         const_3["Paladin_Male_F12"] = "It\'s Raining Rockstar";
         const_3["Paladin_Male_F13"] = "Mall Metal Madness";
         const_3["Paladin_Male_F14"] = "Hunting Party";
         const_3["Paladin_Male_F15"] = "No Sunscreen";
         const_3["Paladin_Female_FF01"] = "Long Lashes";
         const_3["Paladin_Female_FF02"] = "Whoa Nelly";
         const_3["Paladin_Female_FF03"] = "Mischiefmaker";
         const_3["Paladin_Female_FF04"] = "The New Girl";
         const_3["Paladin_Female_FF05"] = "Cute As A Button";
         const_3["Paladin_Female_FF06"] = "Pretty Girls Make Plots";
         const_3["Paladin_Female_FF07"] = "Sadiehawkin\'s Bombshell";
         const_3["Paladin_Female_FF08"] = "Puppy Dog Eyes";
         const_3["Paladin_Female_FF09"] = "Momma Ain\'t Happy";
         const_3["Paladin_Female_FF10"] = "Of Mice And Women";
         const_3["Paladin_Female_FF11"] = "Vampiric Me";
         const_3["Paladin_Female_FF12"] = "I Just Wanna Talk";
         const_3["Paladin_Female_FF13"] = "Techno Terra";
         const_3["Rogue_Male_Face01"] = "Why So Serious";
         const_3["Rogue_Male_Face02"] = "Mr. Charisma";
         const_3["Rogue_Male_Face03"] = "Big Brow Business";
         const_3["Rogue_Male_Face04"] = "Winded Watson";
         const_3["Rogue_Male_Face05"] = "The Stare";
         const_3["Rogue_Male_Face06"] = "The Gottfried Squint";
         const_3["Rogue_Male_Face07"] = "Where Are My Glasses";
         const_3["Rogue_Male_Face08"] = "The Expendables";
         const_3["Rogue_Male_Face09"] = "Fright Night";
         const_3["Rogue_Male_Face10"] = "Close Encounters";
         const_3["Rogue_Male_Face11"] = "Three Ring Stare";
         const_3["Rogue_Male_Face12"] = "Get Off Me";
         const_3["Rogue_Male_Face13"] = "I Said Get Off Me";
         const_3["Rogue_Male_Face14"] = "Ain\'t Got No Alibi";
         const_3["Rogue_Female_FFace01"] = "We Need To Talk";
         const_3["Rogue_Female_FFace02"] = "Dungeon Blitzed";
         const_3["Rogue_Female_FFace03"] = "Independent Woman";
         const_3["Rogue_Female_FFace04"] = "The Mistress";
         const_3["Rogue_Female_FFace05"] = "Icing on the Cake";
         const_3["Rogue_Female_FFace06"] = "All Nighter";
         const_3["Rogue_Female_FFace07"] = "Wait Just A Minute";
         const_3["Rogue_Female_FFace08"] = "Nightmare B4 Blitzmas";
         const_3["Rogue_Female_FFace09"] = "Its a Good Day";
         const_3["Rogue_Female_FFace10"] = "Voluptuous Vixen";
         const_3["Rogue_Female_FFace11"] = "The Triclops";
         const_3["Rogue_Female_FFace12"] = "Petite Feet";
         const_3["Rogue_Female_FFace13"] = "Show Girl";
         const_5["Mage_Female_M01"] = "Pucker Up";
         const_5["Mage_Female_M02"] = "Shade Of Bliss";
         const_5["Mage_Female_M03"] = "Smile For The Camera";
         const_5["Mage_Female_M04"] = "Stay Focused";
         const_5["Mage_Male_MM01"] = "Head Turning Beard";
         const_5["Mage_Male_MM02"] = "Clean It Up Good";
         const_5["Mage_Male_MM03"] = "Mogwai Not For Sale";
         const_5["Mage_Male_MM04"] = "The Waterfall";
         const_5["Mage_Male_MM05"] = "Wedge of Wisdom";
         const_5["Mage_Male_MM06"] = "Facial Falcon";
         const_5["Mage_Male_MM07"] = "Garden Gnome Guru";
         const_5["Mage_Male_MM08"] = "Who\'s Your Daddy";
         const_5["Mage_Male_MM09"] = "Joe\'s Tripod";
         const_5["Mage_Male_MM10"] = "Elven Hospitality";
         const_5["Paladin_Male_M01"] = "Clean Cut";
         const_5["Paladin_Male_M02"] = "Mountain Man";
         const_5["Paladin_Male_M03"] = "Box Boy";
         const_5["Paladin_Male_M04"] = "The Creepy Neighbor";
         const_5["Paladin_Male_M05"] = "Fuzzy Norris";
         const_5["Paladin_Male_M06"] = "Art Gallery Lovin\'";
         const_5["Paladin_Male_M07"] = "How The War Was Won";
         const_5["Paladin_Male_M08"] = "Little Woolly";
         const_5["Paladin_Male_M09"] = "Train Robber Twizzle";
         const_5["Paladin_Male_M10"] = "Big Daddy Chops";
         const_5["Paladin_Male_M11"] = "Grizzly Adams";
         const_5["Paladin_Male_M12"] = "My Chin Has Legs";
         const_5["Paladin_Male_M13"] = "One Ride You Don\'t Want";
         const_5["Paladin_Male_M14"] = "Western Law Enforcement";
         const_5["Paladin_Male_M15"] = "The Nightshift";
         const_5["Paladin_Male_M16"] = "Man Hammocks";
         const_5["Paladin_Male_M17"] = "Full Strap";
         const_5["Paladin_Male_M18"] = "The Hairetic";
         const_5["Paladin_Female_FM01"] = "Charm School";
         const_5["Paladin_Female_FM02"] = "Cheeky Woman";
         const_5["Paladin_Female_FM03"] = "Bitter Betty";
         const_5["Paladin_Female_FM04"] = "Sourpuss";
         const_5["Paladin_Female_FM05"] = "Heartbreaker";
         const_5["Paladin_Female_FM06"] = "The Coffee Is Hot";
         const_5["Paladin_Female_FM07"] = "Lil\' Miss Pucker";
         const_5["Paladin_Female_FM08"] = "Say Cheese";
         const_5["Paladin_Female_FM09"] = "Tough Love";
         const_5["Paladin_Female_FM10"] = "Red Carpet Smile";
         const_5["Rogue_Male_Mouth01"] = "It\'s A Good Day";
         const_5["Rogue_Male_Mouth02"] = "True Grit";
         const_5["Rogue_Male_Mouth03"] = "Poker Face";
         const_5["Rogue_Male_Mouth04"] = "Do Tha Creep";
         const_5["Rogue_Male_Mouth05"] = "American Hardcore";
         const_5["Rogue_Male_Mouth06"] = "Indie Patchwork";
         const_5["Rogue_Male_Mouth07"] = "Metalcore Poster Child";
         const_5["Rogue_Male_Mouth08"] = "Child\'s Play";
         const_5["Rogue_Male_Mouth09"] = "90\'s Gansta";
         const_5["Rogue_Male_Mouth10"] = "5 O\' Clock Shadowstep";
         const_5["Rogue_Male_Mouth11"] = "Been a Long Day";
         const_5["Rogue_Male_Mouth12"] = "Empty Bottle Stubble";
         const_5["Rogue_Male_Mouth13"] = "Yoga Instructor";
         const_5["Rogue_Male_Mouth14"] = "Bank Vault Bandits";
         const_5["Rogue_Male_Mouth15"] = "Family Man";
         const_5["Rogue_Male_Mouth16"] = "The Fu Manchu";
         const_5["Rogue_Female_FMouth01"] = "Kiss And Tell";
         const_5["Rogue_Female_FMouth02"] = "Like What You See";
         const_5["Rogue_Female_FMouth03"] = "I Take Small Bites";
         const_5["Rogue_Female_FMouth04"] = "I Take Smaller Bites";
         const_5["Rogue_Female_FMouth05"] = "My Lips Are Sealed";
         const_5["Rogue_Female_FMouth06"] = "Smile Of Tolerance";
         const_5["Rogue_Female_FMouth07"] = "Sour Pucker";
         const_5["Rogue_Female_FMouth08"] = "Dip And Spit";
         const_5["Rogue_Female_FMouth09"] = "Back In My Day";
         const_5["Rogue_Female_FMouth10"] = "Those Cougar Lips";
         const_5["Rogue_Female_FMouth11"] = "Questionnaire";
         const_5["Rogue_Female_FMouth12"] = "Keep It Calm";
         const_5["Rogue_Female_FMouth13"] = "Cunning Plus One";
         const_5["Rogue_Female_FMouth14"] = "The Smooch";
         const_2["Mage_Female_Do01"] = "Five Finger Wave";
         const_2["Mage_Female_Do02"] = "The Starched Pony";
         const_2["Mage_Female_DoElf01"] = "Get This Party Started";
         const_2["Mage_Female_DoElf02"] = "Ringlet Crown";
         const_2["Mage_Female_DoWhite01"] = "Zero Split Ends";
         const_2["Mage_Female_Do04"] = "Hollywood Flip";
         const_2["Mage_Female_Do05"] = "Slow Motion Entrance";
         const_2["Mage_Female_Do06"] = "Dominant Tease";
         const_2["Mage_Female_Do07"] = "Loosey Fontange";
         const_2["Mage_Female_DoElf03"] = "The Hive";
         const_2["Mage_Female_DoWhite02"] = "Big Business";
         const_2["Mage_Female_Do08"] = "Royal Updo";
         const_2["Mage_Female_Do09"] = "Walley Princess";
         const_2["Mage_Female_Do10"] = "Bangless Hime";
         const_2["Mage_Female_Do11"] = "Queen Of Scene";
         const_2["Mage_Female_Do03"] = "The Babysitter";
         const_2["Mage_Female_Do12"] = "Girls Just Wanna Have Fun";
         const_2["Mage_Female_Do13"] = "Prom Queen Windblow";
         const_2["Mage_Female_Do14"] = "Low Rider Odango";
         const_2["Mage_Female_Do15"] = "Help Me Ben";
         const_2["Mage_Female_Do16"] = "Homecoming Court";
         const_2["Mage_Female_Do17"] = "London Calling";
         const_2["Mage_Female_Do18"] = "Bumping Bangs";
         const_2["Mage_Male_MDo01"] = "Care For Some Tea";
         const_2["Mage_Male_MDo02"] = "Mission Impossible";
         const_2["Mage_Male_MDo03"] = "Swashbuckle Baggage";
         const_2["Mage_Male_MDo04"] = "The Recession";
         const_2["Mage_Male_MDo05"] = "Franklin\'s Finest";
         const_2["Mage_Male_MDo06"] = "Epidermis Ernst";
         const_2["Mage_Male_MDo07"] = "The Wu Shu Do";
         const_2["Mage_Male_MDo08"] = "Born Rough";
         const_2["Mage_Male_MDo09"] = "Cocktail Hour";
         const_2["Mage_Male_MDo10"] = "The Count";
         const_2["Mage_Male_MDo11"] = "Playin\' It Safe";
         const_2["Mage_Male_MDo12"] = "The Curator\'s Curl";
         const_2["Mage_Male_MDo13"] = "Alley Cat Allies";
         const_2["Mage_Male_MDo14"] = "Dubstep DJ";
         const_2["Mage_Male_MDo15"] = "Lunch By Myself";
         const_2["Mage_Male_MDo16"] = "The Roughnecks";
         const_2["Mage_Male_MDo17"] = "Don\'t Make Me Pull Rank";
         const_2["Mage_Male_MDo18"] = "Bushido Blitz";
         const_2["Mage_Male_MDo19"] = "Danny Disconnect";
         const_2["Mage_Male_MDo20"] = "The All-Savvy";
         const_2["Paladin_Male_Do01"] = "Island Stranded";
         const_2["Paladin_Male_Do02"] = "The Trump";
         const_2["Paladin_Male_Do03"] = "Crew For The Interview";
         const_2["Paladin_Male_Do04"] = "A Bit Of Product";
         const_2["Paladin_Male_Do05"] = "Short And Simple";
         const_2["Paladin_Male_Do06"] = "Colonial Tea Party";
         const_2["Paladin_Male_Do07"] = "Mr. Clean";
         const_2["Paladin_Male_Do08"] = "The R. Pattz";
         const_2["Paladin_Male_Do09"] = "Fabulous Friar";
         const_2["Paladin_Male_Do10"] = "Rick James Jheri";
         const_2["Paladin_Male_Do11"] = "Look Out Gaga";
         const_2["Paladin_Male_Do12"] = "The Dark Horse";
         const_2["Paladin_Male_Do13"] = "The Hello Ladies Curl";
         const_2["Paladin_Male_Do14"] = "Dear Diary";
         const_2["Paladin_Male_Do15"] = "Get In My Belly";
         const_2["Paladin_Male_Do16"] = "Cali Uber Alles";
         const_2["Paladin_Male_Do17"] = "In Russia Man Hench You";
         const_2["Paladin_Male_Do18"] = "Good Old Mop Top";
         const_2["Paladin_Male_Do19"] = "Caesar Side Walls";
         const_2["Paladin_Male_Do20"] = "Psychobilly Wedge";
         const_2["Paladin_Male_Do22"] = "Curtained Care";
         const_2["Paladin_Male_Do21"] = "Mail Lady Leg Prickles";
         const_2["Paladin_Male_Do23"] = "Dolce Bed Head";
         const_2["Paladin_Female_FDo01"] = "Bob And Curtain";
         const_2["Paladin_Female_FDo02"] = "Dubstep Diva";
         const_2["Paladin_Female_FDo03"] = "Early Class Updo";
         const_2["Paladin_Female_FDo04"] = "She\'s Out Of Control";
         const_2["Paladin_Female_FDo05"] = "Hardcore Holla";
         const_2["Paladin_Female_FDo06"] = "She\'s All That";
         const_2["Paladin_Female_FDo07"] = "Doin The Frump";
         const_2["Paladin_Female_FDo08"] = "Salon Selectives";
         const_2["Paladin_Female_FDo09"] = "My Jealous Ex";
         const_2["Paladin_Female_FDo10"] = "Fairytale Fun";
         const_2["Paladin_Female_FDo11"] = "Show Me The Ropes";
         const_2["Paladin_Female_FDo12"] = "The Flowhawk";
         const_2["Paladin_Female_FDo13"] = "Teen Riot";
         const_2["Paladin_Female_FDo14"] = "Sir Yes Sir";
         const_2["Paladin_Female_FDo15"] = "Cruella De Blitz";
         const_2["Paladin_Female_FDo16"] = "Hang Down Holly";
         const_2["Paladin_Female_FDo17"] = "Oh Dang Oh Thats Cute";
         const_2["Rogue_Male_Do01"] = "Hipster Holla";
         const_2["Rogue_Male_Do02"] = "Front Tailed Bob";
         const_2["Rogue_Male_Do03"] = "The Pageboy";
         const_2["Rogue_Male_Do04"] = "May I have This Dance";
         const_2["Rogue_Male_Do05"] = "Rounded Hi-Top";
         const_2["Rogue_Male_Do06"] = "Well Groomed Quiff";
         const_2["Rogue_Male_Do07"] = "Slade Cut";
         const_2["Rogue_Male_Bald"] = "Open Dome";
         const_2["Rogue_Male_Do08"] = "Pompadour Brush Back";
         const_2["Rogue_Male_Do09"] = "Open Collar Wedge";
         const_2["Rogue_Male_Do10"] = "It\'s Super, Just Sayin\'";
         const_2["Rogue_Male_Do11"] = "Sweeney Todd";
         const_2["Rogue_Male_Do12"] = "Screamo Tight Sleeve";
         const_2["Rogue_Male_Do13"] = "Pity The Fool";
         const_2["Rogue_Male_Do14"] = "Window Peak-a-boo";
         const_2["Rogue_Male_Do15"] = "Aye Dawg";
         const_2["Rogue_Male_Do16"] = "Profile Pic Perfect";
         const_2["Rogue_Male_Do17"] = "Daredevil\'s Lock";
         const_2["Rogue_Male_Do18"] = "Red Carpet Taper";
         const_2["Rogue_Female_FDo01"] = "Daddy\'s Girl";
         const_2["Rogue_Female_FDo02"] = "Kudumi Cutie";
         const_2["Rogue_Female_FDo03"] = "Odango Ate My Baby";
         const_2["Rogue_Female_FDo04"] = "Cute Is What I Aim For";
         const_2["Rogue_Female_FDo05"] = "The Librarian";
         const_2["Rogue_Female_FDo06"] = "Drama Club";
         const_2["Rogue_Female_FDo07"] = "Band Camp";
         const_2["Rogue_Female_FDo08"] = "Coffee Shop Class";
         const_2["Rogue_Female_FDo09"] = "Ohh She\'s Got It";
         const_2["Rogue_Female_FDo10"] = "Ohh She\'s Got More";
         const_2["Rogue_Female_FDo11"] = "Honey Bun Hustle";
         const_2["Rogue_Female_FDo12"] = "Casual Online Dater";
         const_2["Rogue_Female_FDo13"] = "Heart On My Sleeve";
         const_2["Rogue_Female_FDo14"] = "Hot Topic Hero";
         const_2["Rogue_Female_FDo15"] = "Gucci Gucci";
         const_2["Rogue_Female_FDo16"] = "The Dirty Derby";
         const_2["Rogue_Female_FDo17"] = "Stealth Spice";
         const_2["Rogue_Female_FDo18"] = "The Nest";
         const_2["Rogue_Female_FDo19"] = "Circle Pit Cindy";
         const_2["Rogue_Female_FDo20"] = "I Heart Girly Boys";
      }
      
      internal var var_2506:class_33;
      
      internal var var_442:int;
      
      internal var var_1632:String;
      
      internal var var_441:int;
      
      internal var var_1641:String;
      
      internal var var_451:int;
      
      internal var var_1386:String;
      
      internal var var_433:int;
      
      internal var var_1461:String;
      
      internal var var_1309:String;
      
      internal var var_850:String;
      
      internal var var_385:Dictionary;
      
      internal var var_243:Sprite;
      
      internal var var_265:Sprite;
      
      internal var var_252:Sprite;
      
      internal var var_262:Sprite;
      
      internal var var_967:Dictionary;
      
      internal var var_925:Dictionary;
      
      internal var var_1016:Dictionary;
      
      internal var var_1020:Dictionary;
      
      internal var var_793:class_33;
      
      internal var var_1066:class_33;
      
      internal var var_817:class_33;
      
      internal var var_899:class_33;
      
      internal var var_736:Vector.<class_33>;
      
      internal var var_1039:Dictionary;
      
      private var var_1573:uint;
      
      public function class_102(param1:Game)
      {
         super(param1,"a_LookWindow",null);
      }
      
      public static function method_89(param1:TextField, param2:Dictionary, param3:String, param4:String) : void
      {
         var _loc5_:String = param3 + "_" + param4;
         var _loc6_:String = String(param2[_loc5_]);
         MathUtil.method_2(param1,!!_loc6_ ? _loc6_ : _loc5_);
      }
      
      public static function method_198(param1:String, param2:String) : String
      {
         if(param2 == const_350)
         {
            return param1 == "Rogue" || param1 == "Paladin" ? const_350 : "";
         }
         return param1 == "Mage" ? const_396 : "";
      }
      
      override public function OnCreateScreen() : void
      {
         this.var_1039 = new Dictionary();
         this.var_967 = new Dictionary();
         this.var_925 = new Dictionary();
         this.var_1016 = new Dictionary();
         this.var_1020 = new Dictionary();
         this.var_385 = new Dictionary();
         method_5(var_2.am_PrevHair,this.method_1432);
         method_5(var_2.am_NextHair,this.method_1692);
         method_5(var_2.am_PrevHead,this.method_1386);
         method_5(var_2.am_NextHead,this.method_1484);
         method_5(var_2.am_PrevFace,this.method_1098);
         method_5(var_2.am_NextFace,this.method_1669);
         method_5(var_2.am_PrevMouth,this.method_1841);
         method_5(var_2.am_NextMouth,this.method_1126);
         method_5(var_2.am_PrevGender,this.method_693);
         method_5(var_2.am_NextGender,this.method_693);
         method_5(var_2.am_Randomize,this.method_1672);
         this.var_736 = new Vector.<class_33>(const_1294,true);
         this.var_736[const_235] = method_3(var_2.am_HairColor,const_235,this.method_634);
         this.var_736[const_202] = method_3(var_2.am_SkinColor,const_202,this.method_634);
         this.var_2506 = method_10(var_2.am_Finalize,this.method_1967);
         this.var_1066 = method_1(var_2.am_SkinPickerBase);
         method_5(this.var_1066.mMovieClip.am_Close,this.method_962);
         this.var_793 = method_1(this.var_1066.mMovieClip.am_SkinColor);
         this.var_793.mMovieClip.mouseChildren = false;
         this.var_793.mMovieClip.addEventListener(MouseEvent.MOUSE_DOWN,this.method_293);
         this.var_793.mMovieClip.addEventListener(MouseEvent.MOUSE_MOVE,this.method_268);
         this.var_899 = method_1(var_2.am_ColorPickerBase);
         method_5(this.var_899.mMovieClip.am_Close,this.method_962);
         this.var_817 = method_1(this.var_899.mMovieClip.am_ColorPicker);
         this.var_817.mMovieClip.mouseChildren = false;
         this.var_817.mMovieClip.addEventListener(MouseEvent.MOUSE_DOWN,this.method_293);
         this.var_817.mMovieClip.addEventListener(MouseEvent.MOUSE_MOVE,this.method_268);
         method_23(var_2.am_Close);
      }
      
      override public function OnDestroyScreen() : void
      {
         var _loc1_:String = null;
         var _loc2_:Bitmap = null;
         var _loc3_:String = null;
         this.var_243 = null;
         this.var_265 = null;
         this.var_252 = null;
         this.var_262 = null;
         this.var_385 = null;
         this.var_2506 = null;
         for(_loc1_ in this.var_967)
         {
            delete this.var_967[_loc1_];
         }
         this.var_967 = null;
         for(_loc1_ in this.var_925)
         {
            delete this.var_925[_loc1_];
         }
         this.var_925 = null;
         for(_loc1_ in this.var_1016)
         {
            delete this.var_1016[_loc1_];
         }
         this.var_1016 = null;
         for(_loc1_ in this.var_1020)
         {
            delete this.var_1020[_loc1_];
         }
         this.var_1020 = null;
         for(_loc3_ in this.var_1039)
         {
            _loc2_ = this.var_1039[_loc3_];
            _loc2_.bitmapData.dispose();
            _loc2_.bitmapData = null;
            delete this.var_1039[_loc3_];
         }
         this.var_1039 = null;
         this.var_793.mMovieClip.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_293);
         this.var_793.mMovieClip.removeEventListener(MouseEvent.MOUSE_MOVE,this.method_268);
         this.var_793 = null;
         this.var_817.mMovieClip.removeEventListener(MouseEvent.MOUSE_DOWN,this.method_293);
         this.var_817.mMovieClip.removeEventListener(MouseEvent.MOUSE_MOVE,this.method_268);
         this.var_817 = null;
         this.var_1066 = null;
         this.var_899 = null;
      }
      
      public function OnInitDisplay() : void
      {
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return;
         }
         var _loc2_:EntType = _loc1_.entType;
         this.var_1309 = _loc2_.className;
         this.var_850 = _loc2_.var_620 ? const_350 : const_396;
         this.method_398();
         this.method_316();
         this.var_442 = this.method_350("a_Head_" + _loc2_.var_760,this.var_243);
         this.var_441 = this.method_350("a_Hair_" + _loc2_.var_857,this.var_265);
         this.var_433 = this.method_350("a_Face_" + _loc2_.var_779,this.var_252);
         this.var_451 = this.method_350("a_Mouth_" + _loc2_.var_769,this.var_262);
         this.var_385[const_183] = _loc2_.var_855;
         this.var_385[const_189] = _loc2_.var_782;
         this.method_273(this.var_736[const_202].mMovieClip,_loc2_.var_782);
         this.method_273(this.var_736[const_235].mMovieClip,_loc2_.var_855);
      }
      
      private function method_1484(param1:MouseEvent) : void
      {
         ++this.var_442;
         var_37 = true;
      }
      
      private function method_1386(param1:MouseEvent) : void
      {
         --this.var_442;
         var_37 = true;
      }
      
      private function method_1692(param1:MouseEvent) : void
      {
         ++this.var_441;
         var_37 = true;
      }
      
      private function method_1432(param1:MouseEvent) : void
      {
         --this.var_441;
         var_37 = true;
      }
      
      private function method_1126(param1:MouseEvent) : void
      {
         ++this.var_451;
         var_37 = true;
      }
      
      private function method_1841(param1:MouseEvent) : void
      {
         --this.var_451;
         var_37 = true;
      }
      
      private function method_1669(param1:MouseEvent) : void
      {
         ++this.var_433;
         var_37 = true;
      }
      
      private function method_1098(param1:MouseEvent) : void
      {
         --this.var_433;
         var_37 = true;
      }
      
      private function method_693(param1:MouseEvent) : void
      {
         this.var_850 = this.var_850 == const_396 ? const_350 : const_396;
         this.method_316();
         var_37 = true;
         Refresh();
      }
      
      private function method_273(param1:MovieClip, param2:uint) : void
      {
         param1.graphics.clear();
         param1.graphics.beginFill(param2);
         param1.graphics.drawRoundRect(0,0,param1.width,param1.height,const_942);
         param1.graphics.endFill();
      }
      
      private function method_962(param1:MouseEvent) : void
      {
         this.method_398();
      }
      
      private function method_398() : void
      {
         this.var_899.Hide();
         this.var_1066.Hide();
      }
      
      private function method_634(param1:MouseEvent, param2:uint) : void
      {
         this.var_1573 = param2;
         if(this.var_1573 == const_202)
         {
            this.var_1066.Show();
         }
         else
         {
            this.var_899.Show();
         }
         MathUtil.method_2(this.var_899.mMovieClip.am_Header,const_387[this.var_1573] + " Color");
      }
      
      private function method_268(param1:MouseEvent) : void
      {
         var _loc2_:uint = this.method_100(param1.target as Sprite,param1.localX,param1.localY,const_387[this.var_1573]);
         this.method_273(this.var_736[this.var_1573].mMovieClip,_loc2_);
      }
      
      private function method_293(param1:MouseEvent) : void
      {
         this.method_268(param1);
         this.method_398();
         Refresh();
      }
      
      private function method_316() : void
      {
         var _loc1_:Class = null;
         var _loc2_:String = this.var_1309 + "_" + this.var_850;
         var _loc3_:String = String(const_148[_loc2_]);
         var _loc4_:Object;
         var _loc5_:ApplicationDomain = (_loc4_ = ResourceManager.const_40[_loc3_]).applicationDomain;
         if(!this.var_967[_loc2_])
         {
            _loc1_ = _loc5_.getDefinition("a_CharacterCreationHeadOptions_" + _loc2_) as Class;
            this.var_967[_loc2_] = new _loc1_() as Sprite;
         }
         if(!this.var_925[_loc2_])
         {
            _loc1_ = _loc5_.getDefinition("a_CharacterCreationHairOptions_" + _loc2_) as Class;
            this.var_925[_loc2_] = new _loc1_() as Sprite;
         }
         if(!this.var_1020[_loc2_])
         {
            _loc1_ = _loc5_.getDefinition("a_CharacterCreationFaceOptions_" + _loc2_) as Class;
            this.var_1020[_loc2_] = new _loc1_() as Sprite;
         }
         if(!this.var_1016[_loc2_])
         {
            _loc1_ = _loc5_.getDefinition("a_CharacterCreationMouthOptions_" + _loc2_) as Class;
            this.var_1016[_loc2_] = new _loc1_() as Sprite;
         }
         MathUtil.method_2(var_2.am_GenderName,this.var_850);
         this.var_243 = this.var_967[_loc2_];
         this.var_265 = this.var_925[_loc2_];
         this.var_252 = this.var_1020[_loc2_];
         this.var_262 = this.var_1016[_loc2_];
      }
      
      private function method_1672(param1:MouseEvent) : void
      {
         if(this.var_243)
         {
            this.var_442 = int(Math.random() * this.var_243.numChildren);
         }
         if(this.var_265)
         {
            this.var_441 = int(Math.random() * this.var_265.numChildren);
         }
         if(this.var_252)
         {
            this.var_433 = int(Math.random() * this.var_252.numChildren);
         }
         if(this.var_262)
         {
            this.var_451 = int(Math.random() * this.var_262.numChildren);
         }
         this.method_273(this.var_736[const_202].mMovieClip,this.method_100(this.var_793.mMovieClip,const_90,const_90,const_189));
         this.method_273(this.var_736[const_235].mMovieClip,this.method_100(this.var_817.mMovieClip,const_90,const_90,const_183));
         var_37 = true;
         Refresh();
      }
      
      public function method_100(param1:Sprite, param2:Number, param3:Number, param4:String) : uint
      {
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:BitmapData = null;
         var _loc5_:Bitmap;
         if(!(_loc5_ = this.var_1039[param4]))
         {
            _loc7_ = param1.scaleX;
            _loc8_ = param1.scaleY;
            param1.scaleX = 1;
            param1.scaleY = 1;
            (_loc9_ = new BitmapData(Math.ceil(param1.width),Math.ceil(param1.height))).drawWithQuality(param1,null,null,null,null,false,StageQuality.HIGH);
            _loc5_ = this.var_1039[param4] = new Bitmap(_loc9_);
            param1.scaleX = _loc7_;
            param1.scaleY = _loc8_;
         }
         if(param2 == const_90 && param3 == const_90)
         {
            param2 = Math.random() * _loc5_.width;
            param3 = Math.random() * _loc5_.height;
         }
         var _loc6_:uint;
         if((_loc6_ = _loc5_.bitmapData.getPixel(param2,param3)) != this.var_385[param4])
         {
            this.var_385[param4] = _loc6_;
            var_37 = true;
         }
         return _loc6_;
      }
      
      private function method_1967(param1:MouseEvent) : void
      {
         var _loc2_:Entity = var_1.clientEnt;
         if(!_loc2_ || !var_1.CanSendPacket())
         {
            return;
         }
         var _loc3_:EntType = _loc2_.entType;
         var _loc4_:String = method_198(_loc3_.className,this.var_850);
         if(_loc3_.var_760 == this.var_1632 && _loc3_.var_857 == this.var_1641 && _loc3_.var_779 == this.var_1461 && _loc3_.var_769 == this.var_1386 && _loc3_.var_439 == _loc4_ && _loc3_.var_855 == this.var_385[const_183] && _loc3_.var_782 == this.var_385[const_189])
         {
            Hide();
            return;
         }
         var_1.linkUpdater.WriteChangeLook(this.var_1632,this.var_1641,this.var_1386,this.var_1461,_loc4_,this.var_385[const_183],this.var_385[const_189]);
         Hide();
      }
      
      override public function RefreshPaperDoll() : void
      {
         var _loc1_:Entity = var_1.clientEnt;
         if(!var_37 || !_loc1_)
         {
            return;
         }
         var _loc2_:String = this.GetPaperDollType();
         if(!_loc2_)
         {
            return;
         }
         EntType.method_57(_loc2_,"MeUI");
         if(!mPaperDoll)
         {
            mPaperDoll = new Entity(var_1,"MeUI:PaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,_loc1_.mExpLevel,0,null,null,null,null,null,null);
         }
         else
         {
            mPaperDoll.ResetEntType(EntType.method_48("PaperDoll","MeUI"));
         }
         var_2.am_PaperDollHolder.addChild(mPaperDoll.gfx.m_TheDO);
      }
      
      public function GetPaperDollType() : String
      {
         var _loc1_:Entity = var_1.clientEnt;
         if(!_loc1_)
         {
            return null;
         }
         var _loc2_:uint = uint(this.var_385[const_183]);
         var _loc3_:uint = uint(this.var_385[const_189]);
         var _loc4_:String = this.var_1309 + "_" + this.var_850;
         if(this.var_442 >= this.var_243.numChildren)
         {
            this.var_442 = 0;
         }
         if(this.var_442 < 0)
         {
            this.var_442 = this.var_243.numChildren - 1;
         }
         var _loc5_:Sprite = this.var_243.getChildAt(this.var_442) as Sprite;
         var _loc6_:String;
         var _loc7_:Array = (_loc6_ = getQualifiedClassName(_loc5_)).split("_");
         this.var_1632 = _loc7_[2];
         method_89(var_2.am_HeadName,const_18,_loc4_,this.var_1632);
         if(this.var_441 >= this.var_265.numChildren)
         {
            this.var_441 = 0;
         }
         if(this.var_441 < 0)
         {
            this.var_441 = this.var_265.numChildren - 1;
         }
         var _loc8_:Sprite = this.var_265.getChildAt(this.var_441) as Sprite;
         var _loc9_:String;
         var _loc10_:Array = (_loc9_ = getQualifiedClassName(_loc8_)).split("_");
         this.var_1641 = _loc10_[2];
         method_89(var_2.am_HairName,const_2,_loc4_,this.var_1641);
         if(this.var_451 >= this.var_262.numChildren)
         {
            this.var_451 = 0;
         }
         if(this.var_451 < 0)
         {
            this.var_451 = this.var_262.numChildren - 1;
         }
         var _loc11_:Sprite = this.var_262.getChildAt(this.var_451) as Sprite;
         var _loc12_:String;
         var _loc13_:Array = (_loc12_ = getQualifiedClassName(_loc11_)).split("_");
         this.var_1386 = _loc13_[2];
         method_89(var_2.am_MouthName,const_5,_loc4_,this.var_1386);
         if(this.var_433 >= this.var_252.numChildren)
         {
            this.var_433 = 0;
         }
         if(this.var_433 < 0)
         {
            this.var_433 = this.var_252.numChildren - 1;
         }
         var _loc14_:Sprite = this.var_252.getChildAt(this.var_433) as Sprite;
         var _loc15_:String;
         var _loc16_:Array = (_loc15_ = getQualifiedClassName(_loc14_)).split("_");
         this.var_1461 = _loc16_[2];
         method_89(var_2.am_FaceName,const_3,_loc4_,this.var_1461);
         var _loc17_:EntType = _loc1_.entType;
         var _loc18_:String = method_198(this.var_1309,this.var_850);
         var _loc19_:String = EntType.method_97("PaperDoll",_loc17_.parentEntType,2.25,_loc17_.equippedGear,_loc18_,this.var_1632,this.var_1641,this.var_1386,this.var_1461,_loc2_,_loc3_,_loc1_.entType.shirtColor,_loc1_.entType.pantColor);
         if(this.var_1309 == "Rogue")
         {
            _loc19_ = _loc19_.replace("</EntType>","<GfxType><BaseAnim>Relaxed</BaseAnim></GfxType></EntType>");
         }
         return _loc19_;
      }
      
      private function method_350(param1:String, param2:Sprite) : uint
      {
         var _loc3_:uint = 0;
         var _loc5_:Sprite = null;
         var _loc6_:String = null;
         var _loc4_:uint = uint(param2.numChildren);
         _loc3_ = 0;
         while(_loc3_ < _loc4_)
         {
            _loc5_ = param2.getChildAt(_loc3_) as Sprite;
            _loc6_ = getQualifiedClassName(_loc5_);
            if(param1 == _loc6_)
            {
               return _loc3_;
            }
            _loc3_++;
         }
         return 0;
      }
   }
}
