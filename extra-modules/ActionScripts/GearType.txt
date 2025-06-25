package
{
   import flash.utils.Dictionary;
   
   public class GearType
   {
      
      public static var var_603:Dictionary = new Dictionary();
      
      public static const const_37:Dictionary = new Dictionary();
      
      public static const const_540:Dictionary = new Dictionary();
      
      public static const const_7:Dictionary = new Dictionary();
      
      public static const const_1:Dictionary = new Dictionary();
      
      public static const GEARTYPE_BITSTOSEND:uint = 11;
      
      public static const const_348:uint = 3;
      
      public static const const_176:uint = 2;
      
      {
         var_603["M"] = 0;
         var_603["R"] = 1;
         var_603["L"] = 2;
         const_37["MageAttack"] = true;
         const_37["MageExpertise"] = true;
         const_37["MageBalanced"] = true;
         const_37["MageArmor"] = true;
         const_37["MageSpread"] = true;
         const_37["RogueAttack"] = true;
         const_37["RogueExpertise"] = true;
         const_37["RogueBalanced"] = true;
         const_37["RogueArmor"] = true;
         const_37["RogueSpread"] = true;
         const_37["PaladinAttack"] = true;
         const_37["PaladinExpertise"] = true;
         const_37["PaladinBalanced"] = true;
         const_37["PaladinArmor"] = true;
         const_37["PaladinSpread"] = true;
         const_540["Mage"] = new Vector.<GearType>();
         const_540["Rogue"] = new Vector.<GearType>();
         const_540["Paladin"] = new Vector.<GearType>();
         const_7["Weapon_Main_Mid"] = [0,125,138,144,151,159,166,174,183,191,200,210,220,231,242,254,266,279,293,306,321,337,353,370,388,407,425,446,468,490,514,539,565,592,620,651,682,714,749,785,823,862,904,948,993,1041,1091,1144,1198,1257,1316,1380,1446];
         const_7["Weapon_Main_Low"] = [0,104,114,119,125,131,137,144,151,158,166,173,182,191,200,209,220,230,241,252,265,277,291,305,320,335,351,368,386,404,424,443,465,487,510,535,561,588,616,645,677,709,744,780,817,856,897,940,985,1033,1082,1135,1189];
         const_7["Weapon_Main_High"] = [0,136,150,157,165,173,181,190,199,208,218,229,240,251,264,277,290,304,319,334,349,367,385,403,422,443,463,486,510,534,560,587,615,645,676,709,743,778,816,855,897,939,984,1032,1081,1134,1189,1246,1305,1369,1434,1503,1575];
         const_7["Weapon_Main_Fair"] = [0,115,126,132,139,145,152,160,167,175,184,192,202,211,222,232,244,255,267,280,293,307,323,338,354,371,389,408,428,448,470,491,515,540,566,593,622,652,683,715,751,786,824,864,905,949,995,1042,1092,1145,1200,1258,1318];
         const_7["Weapon_Main_Spread"] = [0,130,144,150,158,166,173,182,191,199,209,219,230,241,253,265,278,291,306,320,335,352,369,386,405,425,444,466,489,512,537,563,590,618,648,680,712,746,782,820,860,900,944,990,1037,1087,1140,1195,1251,1313,1375,1441,1510];
         const_7["Weapon_Second_Mid"] = [0,85,94,98,103,108,113,118,125,130,136,143,150,158,165,173,181,190,200,209,219,230,240,252,264,277,290,304,318,334,350,368,385,403,423,444,465,486,510,535,560,588,616,646,677,709,743,780,817,856,897,940,986];
         const_7["Weapon_Second_Low"] = [0,64,70,73,77,80,84,88,93,97,102,106,112,118,123,128,135,141,148,155,163,170,178,187,196,205,216,226,236,248,260,272,285,298,313,328,344,360,377,395,414,435,456,478,501,524,549,576,604,632,663,695,729];
         const_7["Weapon_Second_High"] = [0,96,106,111,117,122,128,134,141,147,154,162,170,178,187,196,205,215,226,237,247,260,272,285,298,313,328,344,360,378,396,416,435,456,479,502,526,550,577,605,634,665,696,730,765,802,841,882,924,968,1015,1063,1115];
         const_7["Weapon_Second_Fair"] = [0,75,82,86,91,94,99,104,109,114,120,125,132,138,145,151,159,166,174,183,191,200,210,220,230,241,254,266,278,292,306,320,335,351,369,386,405,424,444,465,488,512,536,562,589,617,647,678,711,744,781,818,858];
         const_7["Weapon_Second_Spread"] = [0,80,88,92,97,101,106,111,117,122,128,134,141,148,155,162,170,178,187,196,205,215,225,236,247,259,272,285,298,313,328,344,360,377,396,415,435,455,477,500,524,550,576,604,633,663,695,729,764,800,839,879,922];
         const_7["Weapon_NoArmor_Bonus"] = [0,11,12,13,14,14,15,16,16,17,18,19,20,20,22,23,24,25,26,28,28,30,32,33,34,36,38,40,42,44,46,48,50,53,56,58,61,64,67,70,74,77,80,84,88,93,98,102,107,112,118,123,129];
         const_7["Weapon_NoArmor_Spread"] = [0,5,6,6,7,7,7,8,8,8,9,9,10,10,11,11,12,12,13,14,14,15,16,16,17,18,19,20,21,22,23,24,25,26,28,29,30,32,33,35,37,38,40,42,44,46,49,51,53,56,59,61,64];
         const_7["Offhand_Main_Mid"] = [0,95,104,109,115,120,126,132,139,145,152,160,167,175,184,193,202,212,222,233,244,256,268,281,295,308,324,339,355,372,391,410,429,450,472,495,518,543,569,596,625,655,687,720,754,791,828,868,910,954,1000,1048,1100];
         const_7["Offhand_Main_Low"] = [0,79,86,91,95,99,105,110,115,120,126,132,138,145,152,160,166,175,184,192,202,211,222,232,243,254,267,279,293,307,322,338,353,370,388,407,426,447,468,491,515,539,566,592,621,651,682,714,749,785,823,862,904];
         const_7["Offhand_Main_High"] = [0,103,114,119,125,131,137,144,151,158,166,174,182,191,200,210,220,231,242,254,266,279,292,306,321,336,353,369,387,405,426,446,467,490,514,539,564,591,620,649,681,713,748,784,821,861,902,946,991,1039,1089,1142,1198];
         const_7["Offhand_Main_Fair"] = [0,87,96,101,105,110,116,122,127,133,140,146,153,161,168,177,184,194,204,213,224,234,246,257,269,282,296,309,325,340,357,374,391,410,430,451,472,495,519,544,571,597,627,656,688,721,756,792,830,870,912,956,1002];
         const_7["Offhand_Main_Spread"] = [0,99,109,114,120,125,131,138,145,151,159,167,174,183,192,201,211,221,232,243,255,267,280,293,308,322,338,354,371,388,408,428,448,470,493,517,541,567,594,622,653,684,717,752,787,826,865,907,950,996,1044,1095,1149];
         const_7["Offhand_Second_Mid"] = [0,65,71,74,78,82,86,90,95,99,103,109,114,119,125,131,138,144,151,159,166,174,182,191,201,210,220,231,242,254,266,279,293,307,322,337,353,370,388,406,425,447,468,491,514,539,564,592,620,650,681,714,749];
         const_7["Offhand_Second_Low"] = [0,49,53,56,58,61,65,68,71,74,77,81,85,89,93,98,102,107,113,118,124,129,136,142,149,156,163,171,180,189,197,207,217,227,238,249,261,274,287,301,315,331,347,363,381,399,418,438,459,481,504,528,553];
         const_7["Offhand_Second_High"] = [0,73,81,84,88,93,97,102,107,112,117,123,129,135,141,148,156,163,171,180,188,197,206,216,227,238,249,261,274,287,301,315,331,347,364,381,399,418,439,459,481,505,529,555,581,609,638,670,701,735,770,808,847];
         const_7["Offhand_Second_Fair"] = [0,57,63,66,68,72,76,80,83,87,91,95,100,105,109,115,120,126,133,139,146,152,160,167,175,184,192,201,212,222,232,243,255,267,280,293,307,322,338,354,371,389,408,427,448,469,492,516,540,566,593,622,651];
         const_7["Offhand_Second_Spread"] = [0,61,67,70,73,77,81,85,89,93,97,102,107,112,117,123,129,135,142,149,156,163,171,179,188,197,206,216,227,238,249,261,274,287,301,315,330,346,363,380,398,418,438,459,481,504,528,554,580,608,637,668,700];
         const_7["Offhand_NoArmor_Bonus"] = [0,8,10,10,10,11,11,12,12,13,14,14,15,16,16,17,18,19,20,21,22,23,24,25,26,28,29,30,32,33,35,36,38,40,42,44,46,48,51,53,56,58,61,64,67,70,74,78,81,85,89,94,98];
         const_7["Offhand_Armor_Bonus"] = [0,40,45,47,49,51,53,56,59,62,65,68,71,75,78,82,86,90,95,99,104,109,114,119,125,132,138,144,151,158,166,173,182,191,200,210,220,230,242,253,266,278,291,305,320,335,352,369,386,405,425,446,467];
         const_7["Offhand_NoArmor_Spread"] = [0,4,5,5,5,5,5,6,6,6,7,7,7,8,8,8,9,9,10,10,11,11,12,12,13,14,14,15,16,16,17,18,19,20,21,22,23,24,25,26,28,29,30,32,33,35,37,39,40,42,44,47,49];
         const_7["Offhand_Armor_Spread"] = [0,36,40,42,44,45,47,50,53,55,58,61,63,67,70,73,77,80,85,88,93,97,102,106,112,118,123,129,135,141,148,155,163,171,179,188,197,206,216,226,238,249,260,273,286,300,315,330,345,362,380,399,418];
         const_7["Basic_Main_Mid"] = [0,70,77,80,84,88,93,97,102,107,113,118,123,129,136,142,149,155,164,171,180,188,197,207,217,228,238,250,262,275,287,302,316,331,347,364,382,399,419,439,460,483,506,530,555,582,611,640,670,703,737,773,810];
         const_7["Basic_Main_Low"] = [0,58,64,67,70,74,77,80,85,89,93,98,102,107,112,117,123,129,136,142,148,155,163,171,179,188,197,206,216,227,237,249,260,273,286,300,314,329,345,362,379,398,417,437,457,480,503,527,552,578,607,636,666];
         const_7["Basic_Main_High"] = [0,76,84,87,92,96,101,106,111,117,123,128,134,141,148,155,163,169,178,186,196,205,215,225,237,248,259,272,286,299,313,329,344,361,378,396,416,435,457,478,501,526,551,577,605,634,665,697,730,766,803,842,882];
         const_7["Basic_Main_Fair"] = [0,64,71,74,78,82,85,89,94,99,103,108,113,119,124,130,137,143,150,157,164,172,181,189,199,208,218,228,240,251,263,276,288,303,317,332,348,365,383,401,420,441,462,484,507,532,557,584,612,641,673,705,738];
         const_7["Basic_Main_Spread"] = [0,73,80,83,88,92,97,101,106,112,118,123,128,135,142,148,156,162,171,178,188,196,206,216,227,238,248,261,274,287,300,315,330,346,362,380,399,417,438,458,480,504,528,553,580,608,638,668,700,734,770,807,846];
         const_7["Basic_Second_Mid"] = [0,48,52,55,57,60,63,66,69,72,77,80,84,88,93,97,101,106,111,116,123,128,134,141,147,155,162,170,178,187,196,205,216,225,236,248,260,272,285,299,314,329,345,361,378,396,416,436,457,479,502,526,552];
         const_7["Basic_Second_Low"] = [0,36,39,42,43,46,47,49,52,54,57,60,63,66,69,72,75,80,83,87,91,95,100,105,109,115,121,126,132,139,146,152,160,167,175,184,192,202,211,222,233,244,256,268,280,294,308,323,339,354,372,389,408];
         const_7["Basic_Second_High"] = [0,54,59,62,65,68,71,75,78,82,87,90,95,100,105,110,115,120,125,131,139,145,152,159,167,175,183,192,202,211,222,232,244,255,267,280,294,308,323,338,355,372,390,408,428,448,470,493,517,542,568,595,624];
         const_7["Basic_Second_Fair"] = [0,42,46,49,51,54,55,58,61,64,67,70,74,78,81,85,89,94,97,102,107,112,118,123,129,135,142,148,156,163,172,179,188,197,206,216,226,238,249,261,274,287,301,315,330,346,362,380,399,417,438,458,480];
         const_7["Basic_Second_Spread"] = [0,45,49,52,54,57,59,62,65,68,72,75,79,83,87,91,95,100,104,109,115,120,126,132,138,145,152,159,167,175,184,192,202,211,221,232,243,255,267,280,294,308,323,338,354,371,389,408,428,448,470,492,516];
         const_7["Basic_Armor_Mid"] = [0,32,35,37,39,40,42,44,47,49,51,54,56,59,62,65,68,71,75,78,82,86,90,94,99,104,109,114,119,125,131,137,144,151,158,166,174,182,191,200,210,220,230,241,253,265,278,291,305,320,336,352,369];
         const_7["Basic_Armor_High"] = [0,38,42,44,47,48,50,53,56,59,61,64,67,71,74,78,82,85,89,93,98,103,108,112,119,124,130,136,143,149,157,164,172,181,189,198,208,218,229,239,251,263,275,288,303,317,332,348,365,383,402,421,441];
         const_7["Basic_Armor_Spread"] = [0,35,38,40,43,44,46,48,51,54,56,59,61,65,68,71,75,78,82,85,90,94,99,103,109,114,119,125,131,137,144,150,158,166,173,182,191,200,210,219,230,241,252,264,278,291,305,319,335,351,369,386,405];
         const_7["Basic_NoArmor_Bonus"] = [0,6,7,7,8,8,8,9,9,10,10,10,11,12,12,13,14,14,14,15,16,17,18,18,20,20,21,22,24,24,26,27,28,30,31,32,34,36,38,39,41,43,45,47,50,52,54,57,60,63,66,69,72];
         const_7["Basic_NoArmor_Spread"] = [0,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,7,7,7,7,8,8,9,9,10,10,10,11,12,12,13,13,14,15,15,16,17,18,19,19,20,21,22,23,25,26,27,28,30,31,33,34,36];
         const_1["Paladin_Sword_Attack_PaladinBalanced"] = "Weapon_Main_Mid";
         const_1["Paladin_Sword_Attack_PaladinAttack"] = "Weapon_Main_High";
         const_1["Paladin_Sword_Attack_PaladinExpertise"] = "Weapon_Main_Low";
         const_1["Paladin_Sword_Attack_PaladinArmor"] = "Weapon_Main_Fair";
         const_1["Paladin_Sword_Attack_PaladinSpread"] = "Weapon_Main_Spread";
         const_1["Paladin_Sword_Expertise_PaladinBalanced"] = "Weapon_Second_Mid";
         const_1["Paladin_Sword_Expertise_PaladinAttack"] = "Weapon_Second_Low";
         const_1["Paladin_Sword_Expertise_PaladinExpertise"] = "Weapon_Second_High";
         const_1["Paladin_Sword_Expertise_PaladinArmor"] = "Weapon_Second_Fair";
         const_1["Paladin_Sword_Expertise_PaladinSpread"] = "Weapon_Second_Spread";
         const_1["Paladin_Sword_Armor_PaladinArmor"] = "Weapon_NoArmor_Bonus";
         const_1["Paladin_Sword_Armor_PaladinSpread"] = "Weapon_NoArmor_Spread";
         const_1["Paladin_Shield_Attack_PaladinBalanced"] = "Offhand_Main_Mid";
         const_1["Paladin_Shield_Attack_PaladinAttack"] = "Offhand_Main_High";
         const_1["Paladin_Shield_Attack_PaladinExpertise"] = "Offhand_Main_Low";
         const_1["Paladin_Shield_Attack_PaladinArmor"] = "Offhand_Main_Fair";
         const_1["Paladin_Shield_Attack_PaladinSpread"] = "Offhand_Main_Spread";
         const_1["Paladin_Shield_Expertise_PaladinBalanced"] = "Offhand_Second_Mid";
         const_1["Paladin_Shield_Expertise_PaladinAttack"] = "Offhand_Second_Low";
         const_1["Paladin_Shield_Expertise_PaladinExpertise"] = "Offhand_Second_High";
         const_1["Paladin_Shield_Expertise_PaladinArmor"] = "Offhand_Second_Fair";
         const_1["Paladin_Shield_Expertise_PaladinSpread"] = "Offhand_Second_Spread";
         const_1["Paladin_Shield_Armor_PaladinBalanced"] = "Basic_Armor_Mid";
         const_1["Paladin_Shield_Armor_PaladinAttack"] = "Basic_Armor_Mid";
         const_1["Paladin_Shield_Armor_PaladinExpertise"] = "Basic_Armor_Mid";
         const_1["Paladin_Shield_Armor_PaladinArmor"] = "Offhand_Armor_Bonus";
         const_1["Paladin_Shield_Armor_PaladinSpread"] = "Offhand_Armor_Spread";
         const_1["Paladin_Hat_Attack_PaladinBalanced"] = "Basic_Main_Mid";
         const_1["Paladin_Hat_Attack_PaladinAttack"] = "Basic_Main_High";
         const_1["Paladin_Hat_Attack_PaladinExpertise"] = "Basic_Main_Low";
         const_1["Paladin_Hat_Attack_PaladinArmor"] = "Basic_Main_Fair";
         const_1["Paladin_Hat_Attack_PaladinSpread"] = "Basic_Main_Spread";
         const_1["Paladin_Hat_Expertise_PaladinBalanced"] = "Basic_Second_Mid";
         const_1["Paladin_Hat_Expertise_PaladinAttack"] = "Basic_Second_Low";
         const_1["Paladin_Hat_Expertise_PaladinExpertise"] = "Basic_Second_High";
         const_1["Paladin_Hat_Expertise_PaladinArmor"] = "Basic_Second_Fair";
         const_1["Paladin_Hat_Expertise_PaladinSpread"] = "Basic_Second_Spread";
         const_1["Paladin_Hat_Armor_PaladinBalanced"] = "Basic_Armor_Mid";
         const_1["Paladin_Hat_Armor_PaladinAttack"] = "Basic_Armor_Mid";
         const_1["Paladin_Hat_Armor_PaladinExpertise"] = "Basic_Armor_Mid";
         const_1["Paladin_Hat_Armor_PaladinArmor"] = "Basic_Armor_High";
         const_1["Paladin_Hat_Armor_PaladinSpread"] = "Basic_Armor_Spread";
         const_1["Paladin_Armor_Attack_PaladinBalanced"] = "Basic_Main_Mid";
         const_1["Paladin_Armor_Attack_PaladinAttack"] = "Basic_Main_High";
         const_1["Paladin_Armor_Attack_PaladinExpertise"] = "Basic_Main_Low";
         const_1["Paladin_Armor_Attack_PaladinArmor"] = "Basic_Main_Fair";
         const_1["Paladin_Armor_Attack_PaladinSpread"] = "Basic_Main_Spread";
         const_1["Paladin_Armor_Expertise_PaladinBalanced"] = "Basic_Second_Mid";
         const_1["Paladin_Armor_Expertise_PaladinAttack"] = "Basic_Second_Low";
         const_1["Paladin_Armor_Expertise_PaladinExpertise"] = "Basic_Second_High";
         const_1["Paladin_Armor_Expertise_PaladinArmor"] = "Basic_Second_Fair";
         const_1["Paladin_Armor_Expertise_PaladinSpread"] = "Basic_Second_Spread";
         const_1["Paladin_Armor_Armor_PaladinBalanced"] = "Basic_Armor_Mid";
         const_1["Paladin_Armor_Armor_PaladinAttack"] = "Basic_Armor_Mid";
         const_1["Paladin_Armor_Armor_PaladinExpertise"] = "Basic_Armor_Mid";
         const_1["Paladin_Armor_Armor_PaladinArmor"] = "Basic_Armor_High";
         const_1["Paladin_Armor_Armor_PaladinSpread"] = "Basic_Armor_Spread";
         const_1["Paladin_Gloves_Attack_PaladinBalanced"] = "Basic_Main_Mid";
         const_1["Paladin_Gloves_Attack_PaladinAttack"] = "Basic_Main_High";
         const_1["Paladin_Gloves_Attack_PaladinExpertise"] = "Basic_Main_Low";
         const_1["Paladin_Gloves_Attack_PaladinArmor"] = "Basic_Main_Fair";
         const_1["Paladin_Gloves_Attack_PaladinSpread"] = "Basic_Main_Spread";
         const_1["Paladin_Gloves_Expertise_PaladinBalanced"] = "Basic_Second_Mid";
         const_1["Paladin_Gloves_Expertise_PaladinAttack"] = "Basic_Second_Low";
         const_1["Paladin_Gloves_Expertise_PaladinExpertise"] = "Basic_Second_High";
         const_1["Paladin_Gloves_Expertise_PaladinArmor"] = "Basic_Second_Fair";
         const_1["Paladin_Gloves_Expertise_PaladinSpread"] = "Basic_Second_Spread";
         const_1["Paladin_Gloves_Armor_PaladinBalanced"] = "Basic_Armor_Mid";
         const_1["Paladin_Gloves_Armor_PaladinAttack"] = "Basic_Armor_Mid";
         const_1["Paladin_Gloves_Armor_PaladinExpertise"] = "Basic_Armor_Mid";
         const_1["Paladin_Gloves_Armor_PaladinArmor"] = "Basic_Armor_High";
         const_1["Paladin_Gloves_Armor_PaladinSpread"] = "Basic_Armor_Spread";
         const_1["Paladin_Boots_Attack_PaladinBalanced"] = "Basic_Main_Mid";
         const_1["Paladin_Boots_Attack_PaladinAttack"] = "Basic_Main_High";
         const_1["Paladin_Boots_Attack_PaladinExpertise"] = "Basic_Main_Low";
         const_1["Paladin_Boots_Attack_PaladinArmor"] = "Basic_Main_Fair";
         const_1["Paladin_Boots_Attack_PaladinSpread"] = "Basic_Main_Spread";
         const_1["Paladin_Boots_Expertise_PaladinBalanced"] = "Basic_Second_Mid";
         const_1["Paladin_Boots_Expertise_PaladinAttack"] = "Basic_Second_Low";
         const_1["Paladin_Boots_Expertise_PaladinExpertise"] = "Basic_Second_High";
         const_1["Paladin_Boots_Expertise_PaladinArmor"] = "Basic_Second_Fair";
         const_1["Paladin_Boots_Expertise_PaladinSpread"] = "Basic_Second_Spread";
         const_1["Paladin_Boots_Armor_PaladinBalanced"] = "Basic_Armor_Mid";
         const_1["Paladin_Boots_Armor_PaladinAttack"] = "Basic_Armor_Mid";
         const_1["Paladin_Boots_Armor_PaladinExpertise"] = "Basic_Armor_Mid";
         const_1["Paladin_Boots_Armor_PaladinArmor"] = "Basic_Armor_High";
         const_1["Paladin_Boots_Armor_PaladinSpread"] = "Basic_Armor_Spread";
         const_1["Rogue_Sword_Attack_RogueBalanced"] = "Weapon_Main_Mid";
         const_1["Rogue_Sword_Attack_RogueAttack"] = "Weapon_Main_High";
         const_1["Rogue_Sword_Attack_RogueExpertise"] = "Weapon_Main_Low";
         const_1["Rogue_Sword_Attack_RogueArmor"] = "Weapon_Main_Fair";
         const_1["Rogue_Sword_Attack_RogueSpread"] = "Weapon_Main_Spread";
         const_1["Rogue_Sword_Expertise_RogueBalanced"] = "Weapon_Second_Mid";
         const_1["Rogue_Sword_Expertise_RogueAttack"] = "Weapon_Second_Low";
         const_1["Rogue_Sword_Expertise_RogueExpertise"] = "Weapon_Second_High";
         const_1["Rogue_Sword_Expertise_RogueArmor"] = "Weapon_Second_Fair";
         const_1["Rogue_Sword_Expertise_RogueSpread"] = "Weapon_Second_Spread";
         const_1["Rogue_Sword_Armor_RogueArmor"] = "Weapon_NoArmor_Bonus";
         const_1["Rogue_Sword_Armor_RogueSpread"] = "Weapon_NoArmor_Spread";
         const_1["Rogue_Shield_Attack_RogueBalanced"] = "Offhand_Main_Mid";
         const_1["Rogue_Shield_Attack_RogueAttack"] = "Offhand_Main_High";
         const_1["Rogue_Shield_Attack_RogueExpertise"] = "Offhand_Main_Low";
         const_1["Rogue_Shield_Attack_RogueArmor"] = "Offhand_Main_Fair";
         const_1["Rogue_Shield_Attack_RogueSpread"] = "Offhand_Main_Spread";
         const_1["Rogue_Shield_Expertise_RogueBalanced"] = "Offhand_Second_Mid";
         const_1["Rogue_Shield_Expertise_RogueAttack"] = "Offhand_Second_Low";
         const_1["Rogue_Shield_Expertise_RogueExpertise"] = "Offhand_Second_High";
         const_1["Rogue_Shield_Expertise_RogueArmor"] = "Offhand_Second_Fair";
         const_1["Rogue_Shield_Expertise_RogueSpread"] = "Offhand_Second_Spread";
         const_1["Rogue_Shield_Armor_RogueArmor"] = "Offhand_NoArmor_Bonus";
         const_1["Rogue_Shield_Armor_RogueSpread"] = "Offhand_NoArmor_Spread";
         const_1["Rogue_Hat_Attack_RogueBalanced"] = "Basic_Main_Mid";
         const_1["Rogue_Hat_Attack_RogueAttack"] = "Basic_Main_High";
         const_1["Rogue_Hat_Attack_RogueExpertise"] = "Basic_Main_Low";
         const_1["Rogue_Hat_Attack_RogueArmor"] = "Basic_Main_Fair";
         const_1["Rogue_Hat_Attack_RogueSpread"] = "Basic_Main_Spread";
         const_1["Rogue_Hat_Expertise_RogueBalanced"] = "Basic_Second_Mid";
         const_1["Rogue_Hat_Expertise_RogueAttack"] = "Basic_Second_Low";
         const_1["Rogue_Hat_Expertise_RogueExpertise"] = "Basic_Second_High";
         const_1["Rogue_Hat_Expertise_RogueArmor"] = "Basic_Second_Fair";
         const_1["Rogue_Hat_Expertise_RogueSpread"] = "Basic_Second_Spread";
         const_1["Rogue_Hat_Armor_RogueBalanced"] = "Basic_Armor_Mid";
         const_1["Rogue_Hat_Armor_RogueAttack"] = "Basic_Armor_Mid";
         const_1["Rogue_Hat_Armor_RogueExpertise"] = "Basic_Armor_Mid";
         const_1["Rogue_Hat_Armor_RogueArmor"] = "Basic_Armor_High";
         const_1["Rogue_Hat_Armor_RogueSpread"] = "Basic_Armor_Spread";
         const_1["Rogue_Armor_Attack_RogueBalanced"] = "Basic_Main_Mid";
         const_1["Rogue_Armor_Attack_RogueAttack"] = "Basic_Main_High";
         const_1["Rogue_Armor_Attack_RogueExpertise"] = "Basic_Main_Low";
         const_1["Rogue_Armor_Attack_RogueArmor"] = "Basic_Main_Fair";
         const_1["Rogue_Armor_Attack_RogueSpread"] = "Basic_Main_Spread";
         const_1["Rogue_Armor_Expertise_RogueBalanced"] = "Basic_Second_Mid";
         const_1["Rogue_Armor_Expertise_RogueAttack"] = "Basic_Second_Low";
         const_1["Rogue_Armor_Expertise_RogueExpertise"] = "Basic_Second_High";
         const_1["Rogue_Armor_Expertise_RogueArmor"] = "Basic_Second_Fair";
         const_1["Rogue_Armor_Expertise_RogueSpread"] = "Basic_Second_Spread";
         const_1["Rogue_Armor_Armor_RogueBalanced"] = "Basic_Armor_Mid";
         const_1["Rogue_Armor_Armor_RogueAttack"] = "Basic_Armor_Mid";
         const_1["Rogue_Armor_Armor_RogueExpertise"] = "Basic_Armor_Mid";
         const_1["Rogue_Armor_Armor_RogueArmor"] = "Basic_Armor_High";
         const_1["Rogue_Armor_Armor_RogueSpread"] = "Basic_Armor_Spread";
         const_1["Rogue_Gloves_Attack_RogueBalanced"] = "Basic_Main_Mid";
         const_1["Rogue_Gloves_Attack_RogueAttack"] = "Basic_Main_High";
         const_1["Rogue_Gloves_Attack_RogueExpertise"] = "Basic_Main_Low";
         const_1["Rogue_Gloves_Attack_RogueArmor"] = "Basic_Main_Fair";
         const_1["Rogue_Gloves_Attack_RogueSpread"] = "Basic_Main_Spread";
         const_1["Rogue_Gloves_Expertise_RogueBalanced"] = "Basic_Second_Mid";
         const_1["Rogue_Gloves_Expertise_RogueAttack"] = "Basic_Second_Low";
         const_1["Rogue_Gloves_Expertise_RogueExpertise"] = "Basic_Second_High";
         const_1["Rogue_Gloves_Expertise_RogueArmor"] = "Basic_Second_Fair";
         const_1["Rogue_Gloves_Expertise_RogueSpread"] = "Basic_Second_Spread";
         const_1["Rogue_Gloves_Armor_RogueBalanced"] = "Basic_Armor_Mid";
         const_1["Rogue_Gloves_Armor_RogueAttack"] = "Basic_Armor_Mid";
         const_1["Rogue_Gloves_Armor_RogueExpertise"] = "Basic_Armor_Mid";
         const_1["Rogue_Gloves_Armor_RogueArmor"] = "Basic_Armor_High";
         const_1["Rogue_Gloves_Armor_RogueSpread"] = "Basic_Armor_Spread";
         const_1["Rogue_Boots_Attack_RogueBalanced"] = "Basic_Main_Mid";
         const_1["Rogue_Boots_Attack_RogueAttack"] = "Basic_Main_High";
         const_1["Rogue_Boots_Attack_RogueExpertise"] = "Basic_Main_Low";
         const_1["Rogue_Boots_Attack_RogueArmor"] = "Basic_Main_Fair";
         const_1["Rogue_Boots_Attack_RogueSpread"] = "Basic_Main_Spread";
         const_1["Rogue_Boots_Expertise_RogueBalanced"] = "Basic_Second_Mid";
         const_1["Rogue_Boots_Expertise_RogueAttack"] = "Basic_Second_Low";
         const_1["Rogue_Boots_Expertise_RogueExpertise"] = "Basic_Second_High";
         const_1["Rogue_Boots_Expertise_RogueArmor"] = "Basic_Second_Fair";
         const_1["Rogue_Boots_Expertise_RogueSpread"] = "Basic_Second_Spread";
         const_1["Rogue_Boots_Armor_RogueBalanced"] = "Basic_Armor_Mid";
         const_1["Rogue_Boots_Armor_RogueAttack"] = "Basic_Armor_Mid";
         const_1["Rogue_Boots_Armor_RogueExpertise"] = "Basic_Armor_Mid";
         const_1["Rogue_Boots_Armor_RogueArmor"] = "Basic_Armor_High";
         const_1["Rogue_Boots_Armor_RogueSpread"] = "Basic_Armor_Spread";
         const_1["Mage_Sword_Attack_MageBalanced"] = "Weapon_Main_Mid";
         const_1["Mage_Sword_Attack_MageAttack"] = "Weapon_Main_High";
         const_1["Mage_Sword_Attack_MageExpertise"] = "Weapon_Main_Low";
         const_1["Mage_Sword_Attack_MageArmor"] = "Weapon_Main_Fair";
         const_1["Mage_Sword_Attack_MageSpread"] = "Weapon_Main_Spread";
         const_1["Mage_Sword_Expertise_MageBalanced"] = "Weapon_Second_Mid";
         const_1["Mage_Sword_Expertise_MageAttack"] = "Weapon_Second_Low";
         const_1["Mage_Sword_Expertise_MageExpertise"] = "Weapon_Second_High";
         const_1["Mage_Sword_Expertise_MageArmor"] = "Weapon_Second_Fair";
         const_1["Mage_Sword_Expertise_MageSpread"] = "Weapon_Second_Spread";
         const_1["Mage_Sword_Armor_MageArmor"] = "Weapon_NoArmor_Bonus";
         const_1["Mage_Sword_Armor_MageSpread"] = "Weapon_NoArmor_Spread";
         const_1["Mage_Shield_Attack_MageBalanced"] = "Offhand_Main_Mid";
         const_1["Mage_Shield_Attack_MageAttack"] = "Offhand_Main_High";
         const_1["Mage_Shield_Attack_MageExpertise"] = "Offhand_Main_Low";
         const_1["Mage_Shield_Attack_MageArmor"] = "Offhand_Main_Fair";
         const_1["Mage_Shield_Attack_MageSpread"] = "Offhand_Main_Spread";
         const_1["Mage_Shield_Expertise_MageBalanced"] = "Offhand_Second_Mid";
         const_1["Mage_Shield_Expertise_MageAttack"] = "Offhand_Second_Low";
         const_1["Mage_Shield_Expertise_MageExpertise"] = "Offhand_Second_High";
         const_1["Mage_Shield_Expertise_MageArmor"] = "Offhand_Second_Fair";
         const_1["Mage_Shield_Expertise_MageSpread"] = "Offhand_Second_Spread";
         const_1["Mage_Shield_Armor_MageArmor"] = "Offhand_NoArmor_Bonus";
         const_1["Mage_Shield_Armor_MageSpread"] = "Offhand_NoArmor_Spread";
         const_1["Mage_Hat_Attack_MageBalanced"] = "Basic_Main_Mid";
         const_1["Mage_Hat_Attack_MageAttack"] = "Basic_Main_High";
         const_1["Mage_Hat_Attack_MageExpertise"] = "Basic_Main_Low";
         const_1["Mage_Hat_Attack_MageArmor"] = "Basic_Main_Fair";
         const_1["Mage_Hat_Attack_MageSpread"] = "Basic_Main_Spread";
         const_1["Mage_Hat_Expertise_MageBalanced"] = "Basic_Second_Mid";
         const_1["Mage_Hat_Expertise_MageAttack"] = "Basic_Second_Low";
         const_1["Mage_Hat_Expertise_MageExpertise"] = "Basic_Second_High";
         const_1["Mage_Hat_Expertise_MageArmor"] = "Basic_Second_Fair";
         const_1["Mage_Hat_Expertise_MageSpread"] = "Basic_Second_Spread";
         const_1["Mage_Hat_Armor_MageArmor"] = "Basic_NoArmor_Bonus";
         const_1["Mage_Hat_Armor_MageSpread"] = "Basic_NoArmor_Spread";
         const_1["Mage_Armor_Attack_MageBalanced"] = "Basic_Main_Mid";
         const_1["Mage_Armor_Attack_MageAttack"] = "Basic_Main_High";
         const_1["Mage_Armor_Attack_MageExpertise"] = "Basic_Main_Low";
         const_1["Mage_Armor_Attack_MageArmor"] = "Basic_Main_Fair";
         const_1["Mage_Armor_Attack_MageSpread"] = "Basic_Main_Spread";
         const_1["Mage_Armor_Expertise_MageBalanced"] = "Basic_Second_Mid";
         const_1["Mage_Armor_Expertise_MageAttack"] = "Basic_Second_Low";
         const_1["Mage_Armor_Expertise_MageExpertise"] = "Basic_Second_High";
         const_1["Mage_Armor_Expertise_MageArmor"] = "Basic_Second_Fair";
         const_1["Mage_Armor_Expertise_MageSpread"] = "Basic_Second_Spread";
         const_1["Mage_Armor_Armor_MageBalanced"] = "Basic_Armor_Mid";
         const_1["Mage_Armor_Armor_MageAttack"] = "Basic_Armor_Mid";
         const_1["Mage_Armor_Armor_MageExpertise"] = "Basic_Armor_Mid";
         const_1["Mage_Armor_Armor_MageArmor"] = "Basic_Armor_High";
         const_1["Mage_Armor_Armor_MageSpread"] = "Basic_Armor_Spread";
         const_1["Mage_Gloves_Attack_MageBalanced"] = "Basic_Main_Mid";
         const_1["Mage_Gloves_Attack_MageAttack"] = "Basic_Main_High";
         const_1["Mage_Gloves_Attack_MageExpertise"] = "Basic_Main_Low";
         const_1["Mage_Gloves_Attack_MageArmor"] = "Basic_Main_Fair";
         const_1["Mage_Gloves_Attack_MageSpread"] = "Basic_Main_Spread";
         const_1["Mage_Gloves_Expertise_MageBalanced"] = "Basic_Second_Mid";
         const_1["Mage_Gloves_Expertise_MageAttack"] = "Basic_Second_Low";
         const_1["Mage_Gloves_Expertise_MageExpertise"] = "Basic_Second_High";
         const_1["Mage_Gloves_Expertise_MageArmor"] = "Basic_Second_Fair";
         const_1["Mage_Gloves_Expertise_MageSpread"] = "Basic_Second_Spread";
         const_1["Mage_Gloves_Armor_MageBalanced"] = "Basic_Armor_Mid";
         const_1["Mage_Gloves_Armor_MageAttack"] = "Basic_Armor_Mid";
         const_1["Mage_Gloves_Armor_MageExpertise"] = "Basic_Armor_Mid";
         const_1["Mage_Gloves_Armor_MageArmor"] = "Basic_Armor_High";
         const_1["Mage_Gloves_Armor_MageSpread"] = "Basic_Armor_Spread";
         const_1["Mage_Boots_Attack_MageBalanced"] = "Basic_Main_Mid";
         const_1["Mage_Boots_Attack_MageAttack"] = "Basic_Main_High";
         const_1["Mage_Boots_Attack_MageExpertise"] = "Basic_Main_Low";
         const_1["Mage_Boots_Attack_MageArmor"] = "Basic_Main_Fair";
         const_1["Mage_Boots_Attack_MageSpread"] = "Basic_Main_Spread";
         const_1["Mage_Boots_Expertise_MageBalanced"] = "Basic_Second_Mid";
         const_1["Mage_Boots_Expertise_MageAttack"] = "Basic_Second_Low";
         const_1["Mage_Boots_Expertise_MageExpertise"] = "Basic_Second_High";
         const_1["Mage_Boots_Expertise_MageArmor"] = "Basic_Second_Fair";
         const_1["Mage_Boots_Expertise_MageSpread"] = "Basic_Second_Spread";
         const_1["Mage_Boots_Armor_MageBalanced"] = "Basic_Armor_Mid";
         const_1["Mage_Boots_Armor_MageAttack"] = "Basic_Armor_Mid";
         const_1["Mage_Boots_Armor_MageExpertise"] = "Basic_Armor_Mid";
         const_1["Mage_Boots_Armor_MageArmor"] = "Basic_Armor_High";
         const_1["Mage_Boots_Armor_MageSpread"] = "Basic_Armor_Spread";
      }
      
      internal var gearID:uint;
      
      internal var gearName:String;
      
      internal var displayName:String;
      
      internal var var_2656:uint;
      
      internal var var_2580:int;
      
      internal var var_2787:int;
      
      internal var type:String;
      
      internal var usedBy:String;
      
      internal var var_582:XML;
      
      internal var var_1303:XML;
      
      internal var var_1062:String;
      
      internal var var_1197:String;
      
      internal var var_100:String;
      
      internal var procRune2:String;
      
      internal var var_2258:String;
      
      internal var meleePower:String;
      
      internal var rangedPower:String;
      
      internal var var_106:String;
      
      internal var var_775:String;
      
      internal var var_1816:uint;
      
      internal var var_1943:uint;
      
      internal var var_8:String;
      
      internal var var_884:Boolean = false;
      
      private var var_1934:Dictionary;
      
      public function GearType()
      {
         this.var_1934 = new Dictionary();
         super();
      }
      
      public static function method_30(param1:XML) : void
      {
         method_18(param1,class_14.gearTypes,class_14.gearTypesDict,class_14.var_2207,class_14.var_1762,class_14.var_842,class_14.var_2352,class_14.var_421);
      }
      
      public static function method_628(param1:XML) : GearType
      {
         var _loc5_:XML = null;
         var _loc6_:String = null;
         var _loc7_:Array = null;
         var _loc8_:XML = null;
         var _loc9_:XML = null;
         var _loc10_:Array = null;
         var _loc11_:Array = null;
         var _loc12_:uint = 0;
         var _loc13_:XML = null;
         var _loc14_:XML = null;
         var _loc15_:String = null;
         var _loc17_:String = null;
         var _loc18_:String = null;
         var _loc19_:String = null;
         var _loc20_:XMLList = null;
         var _loc21_:uint = 0;
         var _loc22_:uint = 0;
         var _loc3_:GearType = new GearType();
         _loc3_.type = param1.attribute("Type").toString();
         _loc3_.gearName = param1.attribute("GearName").toString();
         _loc3_.gearID = param1.attribute("GearID");
         for each(_loc5_ in param1.*)
         {
            if((_loc6_ = String(_loc5_.name().toString())) == "DisplayName")
            {
               _loc3_.displayName = _loc5_.toString();
            }
            else if(_loc6_ == "UsedBy")
            {
               _loc3_.usedBy = _loc5_.toString();
            }
            else if(_loc6_ == "Realm")
            {
               _loc3_.var_106 = _loc5_.toString();
            }
            else if(_loc6_ == "BossName")
            {
               _loc3_.var_775 = _loc5_.toString();
            }
            else if(_loc6_ == "Rarity")
            {
               _loc3_.var_8 = _loc5_.toString();
            }
            else if(_loc6_ == "Level")
            {
               _loc3_.var_1816 = int(_loc5_);
            }
            else if(_loc6_ == "BossName")
            {
               _loc3_.var_775 = _loc5_.toString();
            }
            else if(_loc6_ == "MagicRune")
            {
               _loc3_.var_1197 = _loc5_.toString();
            }
            else if(_loc6_ == "PowerRune")
            {
               _loc3_.var_1062 = _loc5_.toString();
            }
            else if(_loc6_ == "ProcRune")
            {
               _loc3_.var_100 = _loc5_.toString();
            }
            else if(_loc6_ == "ProcRune2")
            {
               _loc3_.procRune2 = _loc5_.toString();
            }
            else if(_loc6_ == "StatRune")
            {
               _loc3_.var_2258 = _loc5_.toString();
            }
            else if(_loc6_ == "MeleePower")
            {
               _loc3_.meleePower = _loc5_.toString();
            }
            else if(_loc6_ == "RangedPower")
            {
               _loc3_.rangedPower = _loc5_.toString();
            }
            else if(_loc6_ == "GearSet")
            {
               _loc3_.var_2656 = uint(_loc5_);
            }
            else if(_loc6_ == "LocOffset")
            {
               if((_loc7_ = _loc5_.toString().split(",")).length != 2)
               {
                  class_24.method_7("GearType has an invalid LocOffset: " + _loc3_.gearName);
               }
               _loc3_.var_2580 = int(_loc7_[0]);
               _loc3_.var_2787 = int(_loc7_[1]);
            }
            else if(_loc6_ == "GfxType")
            {
               _loc8_ = null;
               _loc9_ = _loc5_;
               _loc22_ = uint((_loc20_ = _loc5_.children()).length());
               _loc21_ = 0;
               while(_loc21_ < _loc22_)
               {
                  _loc14_ = _loc20_[_loc21_];
                  if(!(_loc15_ = String(_loc14_.name())).indexOf("CustomArt"))
                  {
                     if((_loc18_ = String((_loc10_ = _loc14_.toString().split("/"))[1])).indexOf("$") != -1)
                     {
                        _loc12_ = (_loc11_ = _loc18_.split("$")).length - 1;
                        _loc19_ = String(_loc11_[_loc12_]);
                        _loc11_.splice(_loc12_,1);
                        _loc17_ = _loc10_[0] + "/" + _loc11_.join("_");
                        _loc14_.setChildren(new XML(_loc17_));
                        (_loc13_ = new XML(_loc14_)).setChildren(new XML(_loc17_ + _loc19_));
                        if(!_loc8_)
                        {
                           _loc8_ = new XML(_loc9_);
                        }
                        _loc8_.appendChild(_loc13_);
                     }
                  }
                  _loc21_++;
               }
               _loc3_.var_582 = _loc5_;
               _loc3_.var_1303 = _loc8_;
            }
            else
            {
               class_24.method_7("Unrecognized Property in " + _loc3_.gearName + ": " + _loc6_);
            }
         }
         if(_loc3_.var_8 == "L")
         {
            _loc3_.var_1943 = 2;
         }
         else if(_loc3_.var_8 == "R")
         {
            _loc3_.var_1943 = 1;
         }
         _loc3_.var_884 = _loc3_.gearName == "No" + _loc3_.usedBy + _loc3_.type;
         return _loc3_;
      }
      
      public static function method_395(param1:String, param2:String) : String
      {
         if(param1 == "Paladin")
         {
            if(param2 == "Sword")
            {
               return "Weapon";
            }
            if(param2 == "Hat")
            {
               return "Helm";
            }
         }
         else if(param1 == "Mage")
         {
            if(param2 == "Shield")
            {
               return "Focus";
            }
            if(param2 == "Hat")
            {
               return "Jewelry";
            }
            if(param2 == "Sword")
            {
               return "Staff";
            }
         }
         else if(param1 == "Rogue")
         {
            if(param2 == "Shield")
            {
               return "Offhand";
            }
            if(param2 == "Hat")
            {
               return "Helm";
            }
            if(param2 == "Sword")
            {
               return "Weapon";
            }
         }
         return param2;
      }
      
      public static function method_18(param1:XML, param2:Array, param3:Dictionary, param4:Dictionary, param5:Dictionary, param6:Dictionary, param7:Dictionary, param8:Dictionary) : void
      {
         var _loc9_:String = null;
         var _loc10_:Vector.<GearType> = null;
         var _loc11_:XML = null;
         var _loc12_:GearType = null;
         var _loc13_:Vector.<GearType> = null;
         var _loc14_:uint = 0;
         var _loc15_:String = null;
         var _loc16_:Vector.<GearType> = null;
         var _loc17_:String = null;
         var _loc18_:Vector.<GearType> = null;
         var _loc19_:String = null;
         for each(_loc11_ in param1.*)
         {
            if(!(!(_loc12_ = method_628(_loc11_)).gearID && !_loc12_.var_884))
            {
               if(param3[_loc12_.gearName])
               {
                  class_24.method_7("Multiple items with name: " + _loc12_.gearName);
               }
               if(Boolean(_loc12_.var_100) && _loc12_.var_100 == _loc12_.procRune2)
               {
                  class_24.method_7("Duplicate runes on item: " + _loc12_.gearName);
               }
               if(_loc12_.gearID >= Math.pow(2,GEARTYPE_BITSTOSEND))
               {
                  class_24.method_7("Item bits to send limit reached, increment bits needed: " + _loc12_.gearID);
               }
               if(_loc12_.gearID > Game.const_745)
               {
                  class_24.method_7("Database assumes all IDs will be less <= " + Game.const_745 + ", Contact Programmer: " + _loc12_.gearID);
               }
               if(!_loc12_.var_582)
               {
                  class_24.method_7("Gear must have custom art associated with it: " + _loc12_.gearName);
               }
               if(!_loc12_.var_1062 && _loc12_.var_8 != "M" && Boolean(_loc12_.var_1816))
               {
                  class_24.method_7("Piece of Gear with Power is missing a power: " + _loc12_.gearName);
               }
               if(_loc12_.gearID)
               {
                  param2[_loc12_.gearID] = _loc12_;
               }
               param3[_loc12_.gearName] = _loc12_;
               if(!_loc12_.var_884)
               {
                  if(!(_loc13_ = param4[_loc12_.usedBy]))
                  {
                     _loc13_ = param4[_loc12_.usedBy] = new Vector.<GearType>();
                  }
                  _loc14_ = _loc13_.length;
                  _loc13_.push(_loc12_);
                  _loc15_ = _loc12_.usedBy + ":" + _loc12_.type + ":" + _loc12_.var_8;
                  if(!(_loc16_ = param5[_loc15_]))
                  {
                     _loc16_ = param5[_loc15_] = new Vector.<GearType>();
                  }
                  _loc16_.push(_loc12_);
                  _loc17_ = _loc12_.usedBy + ":" + _loc12_.var_2656 + ":" + _loc12_.var_8;
                  if(!(_loc18_ = param6[_loc17_]))
                  {
                     _loc18_ = param6[_loc17_] = new Vector.<GearType>();
                  }
                  _loc18_.push(_loc12_);
                  if(_loc12_.var_106)
                  {
                     _loc9_ = _loc12_.usedBy + ":" + _loc12_.var_106 + ":" + _loc12_.var_1816 + ":" + _loc12_.var_8;
                     if(!(_loc10_ = param7[_loc9_]))
                     {
                        _loc10_ = param7[_loc9_] = new Vector.<GearType>();
                     }
                     _loc10_.push(_loc12_);
                  }
                  if(_loc12_.var_775)
                  {
                     _loc9_ = _loc12_.usedBy + ":" + _loc12_.var_775 + ":" + _loc12_.var_8;
                     if(!(_loc10_ = param7[_loc9_]))
                     {
                        _loc10_ = param7[_loc9_] = new Vector.<GearType>();
                     }
                     _loc10_.push(_loc12_);
                     _loc9_ = _loc12_.usedBy + ":" + _loc12_.var_775;
                     if(!(_loc10_ = param7[_loc9_]))
                     {
                        _loc10_ = param7[_loc9_] = new Vector.<GearType>();
                     }
                     _loc10_.push(_loc12_);
                  }
                  if(Boolean(_loc12_.gearID) && Boolean(_loc12_.var_8))
                  {
                     _loc19_ = String(_loc12_.gearID) + _loc12_.var_8.toUpperCase();
                     param8[_loc19_] = _loc12_;
                  }
               }
            }
         }
      }
      
      public function method_377(param1:uint) : uint
      {
         return param1 + this.var_1943;
      }
      
      public function method_121(param1:String, param2:uint, param3:Boolean = true) : uint
      {
         if(this.var_884)
         {
            return this.method_681(param1,param2);
         }
         var _loc4_:String = this.usedBy + "_" + this.type + "_" + param1 + "_" + this.var_2258;
         var _loc5_:String = String(const_1[_loc4_]);
         var _loc6_:Array;
         var _loc7_:uint = !!(_loc6_ = const_7[_loc5_]) ? uint(_loc6_[param2]) : 0;
         if(!param3)
         {
            return _loc7_;
         }
         var _loc8_:uint = this.method_681(param1,param2);
         return _loc7_ - _loc8_;
      }
      
      public function method_2058(param1:String) : Number
      {
         var _loc2_:Dictionary = new Dictionary();
         _loc2_[this.var_100] = true;
         _loc2_[this.procRune2] = true;
         var _loc3_:Number = 0;
         if(_loc2_[param1])
         {
            if(param1 == "Haste")
            {
               _loc3_ = CombatState.const_548;
            }
            if(param1 == "CritChance")
            {
               _loc3_ = CombatState.const_560;
            }
            if(param1 == "CritDamage")
            {
               _loc3_ = CombatState.const_466;
            }
            if(param1 == "Resilience")
            {
               _loc3_ = CombatState.const_569;
            }
            if(param1 == "HealthPercent")
            {
               _loc3_ = CombatState.const_260;
            }
            if(param1 == "RecoveryBoost")
            {
               _loc3_ = CombatState.const_556;
            }
            if(param1 == "AirSlay")
            {
               _loc3_ = CombatState.const_136;
            }
            if(param1 == "DeathSlay")
            {
               _loc3_ = CombatState.const_136;
            }
            if(param1 == "EarthSlay")
            {
               _loc3_ = CombatState.const_136;
            }
            if(param1 == "FireSlay")
            {
               _loc3_ = CombatState.const_136;
            }
            if(param1 == "IceSlay")
            {
               _loc3_ = CombatState.const_136;
            }
            if(param1 == "LifeSlay")
            {
               _loc3_ = CombatState.const_136;
            }
            if(param1 == "ResistAir")
            {
               _loc3_ = CombatState.const_126;
            }
            if(param1 == "ResistDeath")
            {
               _loc3_ = CombatState.const_126;
            }
            if(param1 == "ResistEarth")
            {
               _loc3_ = CombatState.const_126;
            }
            if(param1 == "ResistFire")
            {
               _loc3_ = CombatState.const_126;
            }
            if(param1 == "ResistIce")
            {
               _loc3_ = CombatState.const_126;
            }
            if(param1 == "ResistLife")
            {
               _loc3_ = CombatState.const_126;
            }
         }
         return _loc3_;
      }
      
      public function method_681(param1:String, param2:uint) : uint
      {
         var _loc3_:String = this.usedBy;
         var _loc4_:String = this.type;
         param2 -= this.var_1943;
         var _loc5_:String = "";
         if(_loc4_ == "Boots" || _loc4_ == "Armor" || _loc4_ == "Hat" || _loc4_ == "Gloves")
         {
            if(param1 == "Armor")
            {
               _loc5_ = "Basic_Armor_Mid";
            }
            else if(param1 == "Attack")
            {
               _loc5_ = "Basic_Main_Low";
            }
            else if(param1 == "Expertise")
            {
               _loc5_ = "Basic_Second_Low";
            }
         }
         if(_loc4_ == "Shield")
         {
            if(param1 == "Armor")
            {
               _loc5_ = "Basic_Armor_Mid";
            }
            else if(param1 == "Attack")
            {
               _loc5_ = "Offhand_Main_Low";
            }
            else if(param1 == "Expertise")
            {
               _loc5_ = "Offhand_Second_Low";
            }
         }
         if(_loc4_ == "Sword")
         {
            if(param1 == "Armor")
            {
               _loc5_ = "";
            }
            else if(param1 == "Attack")
            {
               _loc5_ = "Weapon_Second_Low";
            }
            else if(param1 == "Expertise")
            {
               _loc5_ = "Weapon_Second_Low";
            }
         }
         if(_loc4_ == "Hat" && _loc3_ == "Mage" && param1 == "Armor")
         {
            _loc5_ = "";
         }
         if(_loc4_ == "Shield" && (_loc3_ == "Rogue" || _loc3_ == "Mage") && param1 == "Armor")
         {
            _loc5_ = "";
         }
         var _loc6_:Array;
         return !!(_loc6_ = const_7[_loc5_]) ? uint(_loc6_[param2]) : 0;
      }
      
      public function method_1887(param1:String, param2:Number, param3:Entity, param4:class_21, param5:class_21) : GfxType
      {
         var _loc8_:GfxType = null;
         var _loc9_:EntType = null;
         var _loc10_:int = 0;
         var _loc11_:Vector.<ColorSwap> = null;
         var _loc6_:Boolean = Boolean(param3) && param3.entType.var_1685 && Boolean(this.var_1303);
         var _loc7_:String = param1 + param2 + _loc6_ + (!!param4 ? param4.var_57 : "*") + (!!param5 ? param5.var_57 : "*");
         if(!this.var_1934[_loc7_])
         {
            _loc8_ = new GfxType();
            _loc9_ = EntType.method_48(this.usedBy);
            _loc8_.var_29 = _loc9_.gfxType.var_29;
            _loc8_.animClass = _loc9_.gfxType.animClass;
            _loc8_.animScale = _loc9_.gfxType.animScale;
            _loc8_.animScale *= param2;
            _loc8_.var_947 = param1;
            _loc8_.baseAnim = param1 + this.type;
            _loc8_.bFireAndForget = true;
            _loc8_.var_177 = 0;
            _loc10_ = EntType.method_87(this.type);
            GfxType.method_53(_loc6_ ? this.var_1303 : this.var_582,_loc8_,_loc10_);
            _loc11_ = _loc8_.colorSwaps;
            if(param4)
            {
               _loc11_.unshift(new ColorSwap(13693168,param4.var_935,_loc10_));
               _loc11_.unshift(new ColorSwap(8438000,param4.color,_loc10_));
               _loc11_.unshift(new ColorSwap(28896,param4.var_209,_loc10_));
            }
            if(param5)
            {
               _loc11_.unshift(new ColorSwap(16751001,param5.var_935,_loc10_));
               _loc11_.unshift(new ColorSwap(11534336,param5.color,_loc10_));
               _loc11_.unshift(new ColorSwap(6291456,param5.var_209,_loc10_));
            }
            this.var_1934[_loc7_] = _loc8_;
         }
         return this.var_1934[_loc7_];
      }
   }
}
