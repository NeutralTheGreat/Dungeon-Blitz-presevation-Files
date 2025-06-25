package
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.display.StageQuality;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.ui.Keyboard;
   import flash.utils.Dictionary;
   import flash.utils.getQualifiedClassName;
   
   public class ScreenCharacterCreation
   {
      
      private static const const_1392:Array = ["Female","Male"];
      
      private static const const_90:Number = -128;
       
      
      internal var var_1:Game;
      
      internal var var_17:MovieClip;
      
      internal var var_250:String;
      
      internal var var_216:String;
      
      internal var paperDollHolder:Sprite;
      
      internal var var_70:Entity;
      
      internal var var_816:Dictionary;
      
      internal var var_2085:Dictionary;
      
      internal var var_1884:Array;
      
      internal var var_1346:String;
      
      internal var var_397:int;
      
      internal var var_2679:int;
      
      internal var var_1763:Array;
      
      internal var var_1441:String;
      
      internal var var_388:int;
      
      internal var var_2645:int;
      
      internal var var_1902:Array;
      
      internal var var_1549:String;
      
      internal var var_424:int;
      
      internal var var_2587:int;
      
      internal var var_1757:Array;
      
      internal var var_1592:String;
      
      internal var var_379:int;
      
      internal var var_2517:int;
      
      internal var var_1639:class_33 = null;
      
      internal var var_1362:class_33 = null;
      
      internal var var_1621:class_33 = null;
      
      internal var var_1331:class_33 = null;
      
      internal var var_1613:class_33 = null;
      
      internal var var_1568:class_33 = null;
      
      internal var var_1519:class_33 = null;
      
      internal var var_1576:class_33 = null;
      
      internal var var_1436:class_33 = null;
      
      internal var var_1186:class_33 = null;
      
      internal var var_1243:class_33 = null;
      
      internal var var_1135:class_33 = null;
      
      internal var var_174:class_33 = null;
      
      internal var var_1325:class_33 = null;
      
      internal var var_1648:class_33 = null;
      
      internal var var_243:Sprite = null;
      
      internal var var_265:Sprite = null;
      
      internal var var_252:Sprite = null;
      
      internal var var_262:Sprite = null;
      
      internal var var_130:Array;
      
      internal var var_2863:uint = 0;
      
      internal var var_2528:uint = 0;
      
      internal var var_2601:uint = 0;
      
      internal var var_2496:uint = 0;
      
      internal var var_1631:Array;
      
      internal var var_37:Boolean = false;
      
      internal var var_2172:Array;
      
      internal var var_2768:Array;
      
      internal var var_2575:Array;
      
      internal var var_2449:Array;
      
      internal var var_2466:Array;
      
      internal var var_2658:Array;
      
      public function ScreenCharacterCreation(param1:Game)
      {
         this.var_2172 = "ace aegis aer air ale angel arch arrow art ax axe band bane bard bark baron battle beak beam bear beard beast beer bell big birch bird bit bjorn black bless blest blood blue boar boat bold bolt bone boot born borne bow branch brass brave breath bronze broth brow brush buck bucket bull camp cape cart carve castle cat cave chain charm chess chill chin chisel chop claw cloak cloth cloud clover club cold copper cord craft crag cross crow crown cryg dance deer dog door dragon drake dream drift drink drum dust dwarf ear earl earth east eld elf elm ettin eye eyr fast fate fear feast feet fel fellow fight fine fire fist flame flash flow flower flown forest forge frost fur fyre fyst gate gem ghast gird gleam glove gold gray green gret grey grieve grim grip gron hail hair hale hall hammer hand hart head heart hearth heim helm helmet hem hide hill hold holm home hood hook horn horse hot hound house hyll ice ink iren iron jewel jug kettle key king kirk knight lake lance land leaf leap light limb lion lock long lord lyre mail man march marsh maul might mont moon myth nettle night noble nord north oak old orc owl ox oxen path peace plate plow pommel port pray pyre quick race rain ramp raven ray red rhyme rill riven river road robin rogue ruby run rune ryck ryme ryver saga salt scale scroll sea shadow shank shape s hield shin shine ship sigil sign silver singer skin sky slayer smith snow son song soul south spade spar speak spear speare speer spire spirit sprite spun spyre staff stair star steal steed steel step stone storm stream stride strong sun sword take tale teeth tharn thief thorn thunder till tin toe tong tongue tooth tor torch tower tree trog tune twig vale valley van vow waarg wagon wald walk wall war ward ware warf warg water weld well west wheel white wild will wind wine wing wink wise witch wood wool word wyld wyn year zan ABBEY ABBOT ABODE ABYSS ACORN ADDAX ADEPT AEGIS AERIE AEON AFIRE AIRER ALDER ALEPH ALTAR AMBER ANGEL ANKUS ANVIL APPLE ARDOR ARENA ARETE ARGOT ARMED ARROW ARYLS ARVOS ASHEN ASPER ATLAS ATRIA AURAR AURIC AXELS AXLED AXLES AXONS AXMAN AZOTH AZLON EAGLE AZURE ELDER EYRIE ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az ea eb ec ed ee ef eg eh ei ej ek el em en eo ep eq er es et eu ev ew ex ey ez ia ib ic id ie if ig ih ii ij ik il im in io ip iq ir is it iu iv iw ix iy iz oa ob oc od oe of og oh oi oj ok ol om on oo op oq or os ot ou ov ow ox oy oz ua ub uc ud ue uf ug uh ui uj uk ul um un uo up uq ur us ut uu uv uw ux uy uz a b c d e f g h i j k l m n o p q r s t u v w x y z AAH AAL AAS ABA ABB ABO ABS ABY ACE ACH ACT ADD ADO ADS ADZ AFF AFT AGA AGE AGO AGS AHA AHI AHS AIA AID AIL AIM AIN AIR AIS AIT AKA AKE ALA ALB ALE ALF ALL ALP ALS ALT ALU AMA AME AMI AMP AMU ANA AND ANE ANI ANN ANS ANT ANY APE APO APP APT ARB ARC ARD ARE ARF ARK ARM ARS ART ARY ASH ASK ASP ASS ATE ATS ATT AUA AUE AUF AUK AVA AVE AVO AWA AWE AWK AWL AWN AXE AYE AYS AYU AZO BAA BAC BAD BAG BAH BAL BAM BAN BAP BAR BAS BAT BAY BED BEE BEG BEL BEN BES BET BEY BEZ BIB BID BIG BIN BIO BIS BIT BIZ BOA BOB BOD BOG BOH BOI BOK BON BOO BOP BOR BOS BOT BOW BOX BOY BRA BRO BRR BRU BUB BUD BUG BUM BUN BUR BUS BUT BUY BYE BYS CAA CAB CAD CAG CAM CAN CAP CAR CAT CAW CAY CAZ CEE CEL CEP CHA CHE CHI CID CIG CIS CIT CLY COB COD COG COL CON COO COP COR COS COT COW COX COY COZ CRU CRY CUB CUD CUE CUM CUP CUR CUT CUZ CWM DAB DAD DAE DAG DAH DAK DAL DAM DAN DAP DAS DAW DAY DEB DEE DEF DEG DEI DEL DEN DEV DEW DEX DEY DIB DID DIE DIF DIG DIM DIN DIP DIS DIT DIV DOB DOC DOD DOE DOF DOG DOH DOL DOM DON DOO DOP DOR DOS DOT DOW DOY DRY DSO DUB DUD DUE DUG DUH DUI DUN DUO DUP DUX DYE DZO EAN EAR EAS EAT EAU EBB ECH ECO ECU EDH EDS EEK EEL EEN EFF EFS EFT EGG EGO EHS EIK EKE ELD ELF ELK ELL ELM ELS ELT EME EMO EMS EMU END ENE ENG ENS EON ERA ERE ERF ERG ERK ERM ERN ERR ERS ESS EST ETA ETH EUK EVE EVO EWE EWK EWT EXO EYE FAA FAB FAD FAE FAG FAH FAN FAP FAR FAS FAT FAW FAX FAY FED FEE FEG FEH FEM FEN FER FES FET FEU FEW FEY FEZ FIB FID FIE FIG FIL FIN FIR FIT FIX FIZ FLU FLY FOB FOE FOG FOH FON FOP FOR FOU FOX FOY FRA FRO FRY FUB FUD FUG FUM FUN FUR GAB GAD GAE GAG GAK GAL GAM GAN GAP GAR GAS GAT GAU GAW GAY GED GEE GEL GEM GEN GEO GER GET GEY GHI GIB GID GIE GIF GIG GIN GIO GIP GIS GIT GJU GNU GOA GOB GOD GOE GON GOO GOR GOS GOT GOV GOX GOY GUB GUE GUL GUM GUN GUP GUR GUS GUT GUV GUY GYM GYP HAD HAE HAG HAH HAJ HAM HAN HAO HAP HAS HAT HAW HAY HEH HEM HEN HEP HER HES HET HEW HEX HEY HIC HID HIE HIM HIN HIP HIS HIT HMM HOA HOB HOC HOD HOE HOG HOH HOI HOM HON HOO HOP HOS HOT HOW HOX HOY HUB HUE HUG HUH HUI HUM HUN HUP HUT HYE HYP ICE ICH ICK ICY IDE IDS IFF IFS IGG ILK ILL IMP ING INK INN INS ION IOS IRE IRK ISH ISM ISO ITA ITS IVY IWI JAB JAG JAI JAK JAM JAP JAR JAW JAY JEE JET JEU JEW JIB JIG JIN JIZ JOB JOE JOG JOL JOR JOT JOW JOY JUD JUG JUN JUS JUT KAB KAE KAF KAI KAK KAM KAS KAT KAW KAY KEA KEB KED KEF KEG KEN KEP KET KEX KEY KHI KID KIF KIN KIP KIR KIS KIT KOA KOB KOI KON KOP KOR KOS KOW KUE KYE KYU LAB LAC LAD LAG LAH LAM LAP LAR LAS LAT LAV LAW LAX LAY LEA LED LEE LEG LEI LEK LEP LES LET LEU LEV LEW LEX LEY LEZ LIB LID LIE LIG LIN LIP LIS LIT LOB LOD LOG LOO LOP LOR LOS LOT LOU LOW LOX LOY LUD LUG LUM LUR LUV LUX LUZ LYE LYM MAA MAC MAD MAE MAG MAK MAL MAM MAN MAP MAR MAS MAT MAW MAX MAY MED MEE MEG MEH MEL MEM MEN MES MET MEU MEW MHO MIB MIC MID MIG MIL MIM MIR MIS MIX MIZ MNA MOA MOB MOC MOD MOE MOG MOI MOL MOM MON MOO MOP MOR MOS MOT MOU MOW MOY MOZ MUD MUG MUM MUN MUS MUT MUX MYC NAB NAE NAG NAH NAM NAN NAP NAS NAT NAW NAY NEB NED NEE NEF NEG NEK NEP NET NEW NIB NID NIE NIL NIM NIP NIS NIT NIX NOB NOD NOG NOH NOM NON NOO NOR NOS NOT NOW NOX NOY NTH NUB NUN NUR NUS NUT NYE NYS OAF OAK OAR OAT OBA OBE OBI OBO OBS OCA OCH ODA ODD ODE ODS OES OFF OFT OHM OHO OHS OIK OIL OIS OKA OKE OLD OLE OLM OMS ONE ONO ONS ONY OOF OOH OOM OON OOP OOR OOS OOT OPE OPS OPT ORA ORB ORC ORD ORE ORF ORS ORT OSE OUD OUK OUP OUR OUS OUT OVA OWE OWL OWN OWT OXO OXY OYE OYS PAC PAD PAH PAL PAM PAN PAP PAR PAS PAT PAV PAW PAX PAY PEA PEC PED PEE PEG PEH PEL PEN PEP PER PES PET PEW PHI PHO PHT PIA PIC PIE PIG PIN PIP PIR PIS PIT PIU PIX PLU PLY POA POD POH POI POL POM POO POP POS POT POW POX POZ PRE PRO PRY PSI PST PUB PUD PUG PUH PUL PUN PUP PUR PUS PUT PUY PYA PYE PYX QAT QIN QIS QUA RAD RAG RAH RAI RAJ RAM RAN RAP RAS RAT RAV RAW RAX RAY REB REC RED REE REF REG REH REI REM REN REO REP RES RET REV REW REX REZ RHO RHY RIA RIB RID RIF RIG RIM RIN RIP RIT RIZ ROB ROC ROD ROE ROK ROM ROO ROT ROW RUB RUC RUD RUE RUG RUM RUN RUT RYA RYE SAB SAC SAD SAE SAG SAI SAL SAM SAN SAP SAR SAT SAU SAV SAW SAX SAY SAZ SEA SEC SED SEE SEG SEI SEL SEN SER SET SEW SEX SEY SEZ SHA SHE SHH SHY SIB SIC SIF SIK SIM SIN SIP SIR SIS SIT SIX SKA SKI SKY SLY SMA SNY SOB SOC SOD SOG SOH SOL SOM SON SOP SOS SOT SOU SOV SOW SOX SOY SOZ SPA SPY SRI STY SUB SUD SUE SUG SUI SUK SUM SUN SUP SUQ SUR SUS SWY SYE SYN TAB TAD TAE TAG TAI TAJ TAK TAM TAN TAO TAP TAR TAS TAT TAU TAV TAW TAX TAY TEA TEC TED TEE TEF TEG TEL TEN TES TET TEW TEX THE THO THY TIC TID TIE TIG TIK TIL TIN TIP TIS TIT TIX TOC TOD TOE TOG TOM TON TOO TOP TOR TOT TOW TOY TRY TSK TUB TUG TUI TUM TUN TUP TUT TUX TWA TWO TWP TYE TYG UDO UDS UEY UFO UGH UGS UKE ULE ULU UMM UMP UMS UMU UNI UNS UPO UPS URB URD URE URN URP USE UTA UTE UTS UTU UVA VAC VAE VAG VAN VAR VAS VAT VAU VAV VAW VEE VEG VET VEX VIA VID VIE VIG VIM VIN VIS VLY VOE VOL VOR VOW VOX VUG VUM WAB WAD WAE WAG WAI WAN WAP WAR WAS WAT WAW WAX WAY WEB WED WEE WEM WEN WET WEX WEY WHA WHO WHY WIG WIN WIS WIT WIZ WOE WOF WOG WOK WON WOO WOP WOS WOT WOW WOX WRY WUD WUS WYE WYN XIS YAD YAE YAG YAH YAK YAM YAP YAR YAW YAY YEA YEH YEN YEP YES YET YEW YEX YGO YID YIN YIP YOB YOD YOK YOM YON YOU YOW YUG YUK YUM YUP YUS ZAG ZAP ZAS ZAX ZEA ZED ZEE ZEK ZEL ZEP ZEX ZHO ZIG ZIN ZIP ZIT ZIZ ZOA ZOL ZOO ZOS ZUZ ".split(" ");
         this.var_2768 = "a a a a e e e e i i i o o o u u u aa ae ae ai au ao ea ee ei eo eu ia ie io oa oe oi ou ui".split(" ");
         this.var_2575 = "a a a a a e e e e e i i i i o o o u u u u aa ae ae ai au ao ea ee ei eo eu ia ie io oa oe oi ou ui".split(" ");
         this.var_2449 = "b b b br bl c c c cr cl ch d d d dr f f f fl fr g g g gr gl h j j k k kr l l m m n p p pr pl r r r rh s s s s st sh sl sp t t t t th tr v v v w w wr x x y y z z".split(" ");
         this.var_2466 = "b,ba,bb,be,bi,bo,bs,bt,bu,by,c,ca,ce,ch,ci,ck,co,ct,cy,d,da,dd,de,di,dj,do,dt,du,dy,f,fa,fe,ff,fi,fo,ft,fu,fy,g,ga,ge,gg,gh,gi,gn,go,gu,gy,h,ha,hi,hl,hm,hn,ho,hr,ht,hu,j,ja,ji,jj,jo,ju,k,ka,ke,kf,kh,ki,ko,kt,ku,ky,l,la,lb,lc,ld,le,lf,li,lk,ll,lm,ln,lo,lp,lt,lu,lx,ly,m,ma,mb,me,mf,mi,mm,mn,mo,mp,mu,my,n,na,nc,nd,ne,nf,ng,nh,ni,nj,nk,nn,no,nt,nu,nx,ny,nz,p,pa,pe,ph,pi,po,pp,pt,pu,py,q,r,ra,rb,rc,rd,re,rf,rg,ri,rk,rl,rn,ro,rp,rr,rt,ru,rv,ry,s,sa,se,sh,si,sk,sm,sn,so,sp,ss,st,su,sy,t,ta,te,th,ti,tl,to,tt,tu,ty,tz,v,va,ve,vi,vo,vy,w,wa,we,wi,wl,wn,wy,x,xa,xe,xi,xt,xy,y,ya,ye,yf,yg,yl,yo,yt,z,za,ze,zi,zo,zu,zy,zz".split(",");
         this.var_2658 = "b,ba,bac,bb,bba,bbe,be,bed,bet,bex,bey,bi,bia,bid,bit,ble,bly,bo,boe,bol,bon,bri,bs,but,by,bye,ca,cad,cai,cca,cce,cco,ccy,ce,ced,cer,ch,che,cho,cht,chy,cid,ck,cky,cme,cne,co,cod,con,cre,cru,ct,cta,cu,cy,cyl,d,da,dah,dal,daw,dd,ddo,ddy,de,dea,dee,dem,dge,dgy,dh,dic,dit,dle,dly,do,dol,don,dor,dry,ds,dso,dyl,dz,dze,f,far,fay,ff,ffy,fo,fro,fs,ft,fy,g,ga,gad,gal,gam,gar,ge,ged,gee,gen,ger,gg,ggy,gh,gha,gin,gio,gle,glu,gly,gma,go,gog,gon,gre,gs,gue,h,ha,hed,hem,hi,hia,hm,ho,hoy,hs,jar,jee,k,ka,kan,kat,kay,ke,ked,kee,keh,kin,kka,kon,kra,ks,kta,ky,l,la,lae,lan,lap,lar,lay,lb,lba,lbe,lco,ld,lde,ldy,le,lea,lec,lee,lef,leo,lew,lex,lf,lfa,lga,lhi,lia,lid,lif,lio,lit,lk,lka,lko,lky,ll,lla,lly,lm,lma,lme,lmy,lna,lod,loe,loo,low,lp,lpe,ls,lse,lso,lt,lto,lu,lum,lva,ly,m,ma,mah,mam,mb,mbo,mbu,me,men,mer,meu,mi,mia,mic,mid,mie,min,mir,mit,mla,mm,mma,mmo,mmy,mo,mok,mov,mp,mph,mpi,mpt,mpy,mra,ms,mu,myd,myl,n,na,nai,nal,nan,nau,nbe,nby,nce,nch,nci,nco,nd,nde,ndo,ndy,ne,ner,new,nfo,ng,nga,ngo,ni,nia,nie,nil,nit,nk,nkh,nky,nly,nn,nna,nno,no,noa,nol,non,now,nro,ns,nsa,nst,nt,nta,nte,nti,nto,nuf,nvy,ny,nyx,p,pa,pah,pal,pay,pby,pdo,pe,ped,pee,pen,per,pex,pgo,ph,pha,pic,po,pod,pon,pp,ppo,ps,pse,pso,psy,pt,pta,qua,r,ra,rad,rak,ral,rao,rar,rb,rba,rby,rc,rca,rch,rco,rd,rde,rdo,rdy,re,rea,red,reg,ret,rev,rew,rf,rfe,rg,rge,rgh,rgo,rgy,rhu,ria,ric,rid,ril,rk,rl,rle,rm,rmy,rn,rna,rne,ro,ron,row,rp,rpa,rr,rra,rs,rsa,rse,rst,rsy,rt,rti,rty,rum,ruv,rva,rvo,ry,ryl,ryx,rzo,s,sar,sba,sc,sci,se,sea,sed,ser,sh,shy,sit,sk,sky,sle,sm,sna,sne,so,sp,spy,ss,ssa,sse,st,sy,t,ta,tap,tat,tch,te,tem,ten,th,the,tic,tma,tna,to,toc,tok,tom,top,ts,tt,tto,tu,tua,tui,ty,va,vae,val,ve,vea,vel,ven,ver,vet,vid,vil,vn,vo,voe,vow,vum,vy,w,wa,way,wdl,we,wed,wee,wer,wfy,wi,wk,wl,wly,wn,wny,wol,wre,wry,wse,wt,x,xal,xam,xe,xec,xed,xel,xen,xer,xia,xid,xil,xim,xit,xle,xo,xon,xpo,xul,xy,y,yah,ye,yed,yen,yer,yez,yin,yne,yot,yra,yre,yry,ys,yu,zan,zar,ze,zo,zon,zy,zym".split(",");
         super();
         this.var_1 = param1;
         this.var_1631 = new Array();
         this.var_130 = new Array();
         this.var_1884 = new Array();
         this.var_1763 = new Array();
         this.var_1757 = new Array();
         this.var_1902 = new Array();
         this.var_816 = new Dictionary();
         this.var_816["Paladin_Male"] = EntType.PALADIN_OPTIONS_FILE;
         this.var_816["Paladin_Female"] = EntType.PALADIN_OPTIONS_FILE;
         this.var_816["Mage_Female"] = EntType.MAGE_OPTIONS_FILE;
         this.var_816["Mage_Male"] = EntType.MAGE_OPTIONS_FILE;
         this.var_816["Rogue_Male"] = EntType.ROGUE_OPTIONS_FILE;
         this.var_816["Rogue_Female"] = EntType.ROGUE_OPTIONS_FILE;
         this.var_2085 = new Dictionary();
      }
      
      public function method_1532() : void
      {
         var _loc1_:Bitmap = null;
         if(this.var_17)
         {
            this.var_1639.DestroyUIMovieClip();
            this.var_1639 = null;
            this.var_1362.DestroyUIMovieClip();
            this.var_1362 = null;
            this.var_1621.DestroyUIMovieClip();
            this.var_1621 = null;
            this.var_1331.DestroyUIMovieClip();
            this.var_1331 = null;
            this.var_1613.DestroyUIMovieClip();
            this.var_1613 = null;
            this.var_1568.DestroyUIMovieClip();
            this.var_1568 = null;
            this.var_1519.DestroyUIMovieClip();
            this.var_1519 = null;
            this.var_1576.DestroyUIMovieClip();
            this.var_1576 = null;
            this.var_1436.DestroyUIMovieClip();
            this.var_1436 = null;
            this.var_1186.DestroyUIMovieClip();
            this.var_1186 = null;
            this.var_1243.DestroyUIMovieClip();
            this.var_1243 = null;
            this.var_1135.DestroyUIMovieClip();
            this.var_1135 = null;
            this.var_174.DestroyUIMovieClip();
            this.var_174 = null;
            this.var_1325.DestroyUIMovieClip();
            this.var_1325 = null;
            this.var_1648.DestroyUIMovieClip();
            this.var_1648 = null;
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_17.am_SkinColor);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_17.am_HairColor);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_17.am_ShirtColor);
            this.var_1.UIBasicButton_DestroyBasicButton(this.var_17.am_PantColor);
         }
         if(Boolean(this.var_17) && Boolean(this.var_17.parent))
         {
            this.var_17.parent.removeChild(this.var_17);
         }
         this.var_17 = null;
         if(this.var_70)
         {
            this.var_70.DestroyEntity(false);
         }
         this.var_70 = null;
         this.paperDollHolder = null;
         for each(_loc1_ in this.var_1631)
         {
            if(_loc1_.parent)
            {
               _loc1_.parent.removeChild(_loc1_);
            }
            if(_loc1_.bitmapData)
            {
               _loc1_.bitmapData.dispose();
            }
            _loc1_.bitmapData = null;
         }
         this.var_243 = null;
         this.var_265 = null;
         this.var_252 = null;
         this.var_262 = null;
         this.var_1631 = null;
         this.var_1884 = null;
         this.var_1763 = null;
         this.var_1902 = null;
         this.var_1757 = null;
         this.var_1 = null;
      }
      
      private function method_1777(param1:MouseEvent) : void
      {
         if(this.var_216 != "Male" && !this.var_1186.var_1027)
         {
            this.var_17.am_Male.filters = [class_51.const_71];
            this.var_17.am_Female.filters = [];
            this.var_216 = "Male";
            this.method_316(false,true);
            this.UpdatePaperDoll();
         }
      }
      
      private function method_1334(param1:MouseEvent) : void
      {
         if(this.var_216 != "Female" && !this.var_1243.var_1027)
         {
            this.var_17.am_Female.filters = [class_51.const_71];
            this.var_17.am_Male.filters = [];
            this.var_216 = "Female";
            this.method_316(false,true);
            this.UpdatePaperDoll();
         }
      }
      
      public function Hide() : void
      {
         this.var_1.method_158(this.var_17);
         if(this.var_70)
         {
            this.var_70.DestroyEntity(false);
         }
         this.var_70 = null;
         this.var_37 = false;
      }
      
      public function method_40() : Boolean
      {
         return Boolean(this.var_17) && this.var_17.visible;
      }
      
      private function method_1348(param1:MouseEvent) : void
      {
         this.method_859();
         param1.stopPropagation();
      }
      
      private function method_859() : void
      {
         this.Hide();
         this.var_1.var_273.Display();
      }
      
      public function Display(param1:String, param2:String) : void
      {
         if(!this.var_17)
         {
            this.var_17 = class_4.method_16("a_CreateCharSplash",true);
            this.var_17.visible = false;
            this.var_17.am_Name.maxChars = 16;
            this.var_17.am_Name.restrict = "A-Za-z";
            this.var_17.am_MageDesc.mouseEnabled = false;
            this.var_17.am_MageDesc.mouseChildren = false;
            this.var_17.am_PaladinDesc.mouseEnabled = false;
            this.var_17.am_PaladinDesc.mouseChildren = false;
            this.var_17.am_RogueDesc.mouseEnabled = false;
            this.var_17.am_RogueDesc.mouseChildren = false;
            this.var_1639 = new class_33(this.var_1,this.var_17.am_ChangeClass);
            this.var_1639.BecomeButton("Ready","Over","Click",this.method_1348,false);
            this.var_1362 = new class_33(this.var_1,this.var_17.am_PrevHair);
            this.var_1362.BecomeButton("Ready","Over","Click",this.method_1432);
            this.var_1621 = new class_33(this.var_1,this.var_17.am_NextHair);
            this.var_1621.BecomeButton("Ready","Over","Click",this.method_1692);
            this.var_1331 = new class_33(this.var_1,this.var_17.am_PrevHead);
            this.var_1331.BecomeButton("Ready","Over","Click",this.method_1386);
            this.var_1613 = new class_33(this.var_1,this.var_17.am_NextHead);
            this.var_1613.BecomeButton("Ready","Over","Click",this.method_1484);
            this.var_1568 = new class_33(this.var_1,this.var_17.am_PrevFace);
            this.var_1568.BecomeButton("Ready","Over","Click",this.method_1098);
            this.var_1519 = new class_33(this.var_1,this.var_17.am_NextFace);
            this.var_1519.BecomeButton("Ready","Over","Click",this.method_1669);
            this.var_1576 = new class_33(this.var_1,this.var_17.am_PrevMouth);
            this.var_1576.BecomeButton("Ready","Over","Click",this.method_1841);
            this.var_1436 = new class_33(this.var_1,this.var_17.am_NextMouth);
            this.var_1436.BecomeButton("Ready","Over","Click",this.method_1126);
            this.var_1186 = new class_33(this.var_1,this.var_17.am_Male);
            this.var_1186.BecomeButton("Ready","Over","Click",this.method_1777);
            this.var_1243 = new class_33(this.var_1,this.var_17.am_Female);
            this.var_1243.BecomeButton("Ready","Over","Click",this.method_1334);
            this.var_1135 = new class_33(this.var_1,this.var_17.am_StartButton);
            this.var_1135.BecomeButton("Ready","Over","Click",this.method_1221,false);
            this.var_174 = new class_33(this.var_1,this.var_17.am_ChangeAccount);
            this.var_174.BecomeButton("Ready","Over","Click",this.method_1739,false);
            this.var_1325 = new class_33(this.var_1,this.var_17.am_Randomize);
            this.var_1325.BecomeButton("Ready","Over","Click",this.method_1672);
            this.var_1648 = new class_33(this.var_1,this.var_17.am_RandomizeName);
            this.var_1648.BecomeButton("Ready","Over","Click",this.method_1782);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_17.am_SkinColor,this.method_1029);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_17.am_HairColor,this.method_1903);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_17.am_ShirtColor,this.method_1500);
            this.var_1.UIBasicButton_CreateBasicButton(this.var_17.am_PantColor,this.method_1404);
         }
         if(!this.var_17.visible)
         {
            this.var_1.method_127();
            this.var_17.visible = true;
            this.var_1.var_89.addChildAt(this.var_17,0);
         }
         this.var_17.am_MageDesc.visible = false;
         this.var_17.am_PaladinDesc.visible = false;
         this.var_17.am_RogueDesc.visible = false;
         if(param1 == "Rogue")
         {
            this.var_17.am_RogueDesc.visible = true;
         }
         else if(param1 == "Paladin")
         {
            this.var_17.am_PaladinDesc.visible = true;
         }
         else if(param1 == "Mage")
         {
            this.var_17.am_MageDesc.visible = true;
         }
         if(this.var_1.serverConn)
         {
            MathUtil.method_2(this.var_174.mMovieClip.am_Text,"Back to Character List");
         }
         else if(this.var_1.var_934)
         {
            this.var_174.Hide();
         }
         else
         {
            MathUtil.method_2(this.var_174.mMovieClip.am_Text,"Login Existing Account");
         }
         this.var_17.am_Male.filters = param2 == "Male" ? [class_51.const_71] : [];
         this.var_17.am_Female.filters = param2 == "Female" ? [class_51.const_71] : [];
         var _loc3_:Boolean = false;
         if(this.var_216 != param2 || this.var_250 != param1)
         {
            _loc3_ = true;
            this.var_216 = param2;
            this.var_250 = param1;
            MathUtil.method_2(this.var_17.am_Name,"");
         }
         this.method_316(_loc3_);
         this.UpdatePaperDoll();
      }
      
      private function method_316(param1:Boolean, param2:Boolean = false) : void
      {
         var _loc4_:String = null;
         var _loc5_:Object = null;
         var _loc6_:Class = null;
         var _loc7_:int = 0;
         var _loc8_:int = 0;
         var _loc9_:int = 0;
         var _loc10_:int = 0;
         var _loc11_:int = 0;
         var _loc12_:int = 0;
         var _loc13_:int = 0;
         var _loc14_:int = 0;
         var _loc3_:String = this.var_250 + "_" + this.var_216;
         if(!this.var_2085[_loc3_])
         {
            _loc4_ = String(this.var_816[_loc3_]);
            if(!(_loc5_ = ResourceManager.const_40[_loc4_]))
            {
               return;
            }
            _loc6_ = _loc5_.applicationDomain.getDefinition("a_CharacterCreationHeadOptions_" + _loc3_);
            this.var_1884[_loc3_] = new _loc6_() as Sprite;
            _loc6_ = _loc5_.applicationDomain.getDefinition("a_CharacterCreationHairOptions_" + _loc3_);
            this.var_1763[_loc3_] = new _loc6_() as Sprite;
            _loc6_ = _loc5_.applicationDomain.getDefinition("a_CharacterCreationFaceOptions_" + _loc3_);
            this.var_1757[_loc3_] = new _loc6_() as Sprite;
            _loc6_ = _loc5_.applicationDomain.getDefinition("a_CharacterCreationMouthOptions_" + _loc3_);
            this.var_1902[_loc3_] = new _loc6_() as Sprite;
            this.var_2085[_loc3_] = true;
         }
         this.var_243 = this.var_1884[_loc3_];
         this.var_265 = this.var_1763[_loc3_];
         this.var_252 = this.var_1757[_loc3_];
         this.var_262 = this.var_1902[_loc3_];
         if(param1)
         {
            this.var_397 = int(Math.random() * this.var_243.numChildren);
            this.var_388 = int(Math.random() * this.var_265.numChildren);
            this.var_379 = int(Math.random() * this.var_252.numChildren);
            this.var_424 = int(Math.random() * this.var_262.numChildren);
            this.method_100(this.var_17.am_HairColor,const_90,const_90,"Hair");
            this.method_100(this.var_17.am_SkinColor,const_90,const_90,"Skin");
            this.method_100(this.var_17.am_ShirtColor,const_90,const_90,"Shirt");
            this.method_100(this.var_17.am_PantColor,const_90,const_90,"Pant");
         }
         if(param2)
         {
            _loc7_ = this.var_2679;
            _loc8_ = this.var_2645;
            _loc9_ = this.var_2517;
            _loc10_ = this.var_2587;
            _loc11_ = int(this.var_2863);
            _loc12_ = int(this.var_2528);
            _loc13_ = int(this.var_2601);
            _loc14_ = int(this.var_2496);
            this.var_2679 = this.var_397;
            this.var_2645 = this.var_388;
            this.var_2517 = this.var_379;
            this.var_2587 = this.var_424;
            this.var_2863 = this.var_130["Skin"];
            this.var_2528 = this.var_130["Hair"];
            this.var_2601 = this.var_130["Shirt"];
            this.var_2496 = this.var_130["Pant"];
            this.var_397 = _loc7_;
            this.var_388 = _loc8_;
            this.var_379 = _loc9_;
            this.var_424 = _loc10_;
            if(_loc11_)
            {
               this.var_130["Skin"] = _loc11_;
               this.var_130["Hair"] = _loc12_;
               this.var_130["Shirt"] = _loc13_;
               this.var_130["Pant"] = _loc14_;
            }
         }
         this.UpdatePaperDoll();
      }
      
      public function method_1484(param1:MouseEvent) : void
      {
         ++this.var_397;
         this.UpdatePaperDoll();
      }
      
      public function method_1386(param1:MouseEvent) : void
      {
         --this.var_397;
         this.UpdatePaperDoll();
      }
      
      public function method_1692(param1:MouseEvent) : void
      {
         ++this.var_388;
         this.UpdatePaperDoll();
      }
      
      public function method_1432(param1:MouseEvent) : void
      {
         --this.var_388;
         this.UpdatePaperDoll();
      }
      
      public function method_1126(param1:MouseEvent) : void
      {
         ++this.var_424;
         this.UpdatePaperDoll();
      }
      
      public function method_1841(param1:MouseEvent) : void
      {
         --this.var_424;
         this.UpdatePaperDoll();
      }
      
      public function method_1669(param1:MouseEvent) : void
      {
         ++this.var_379;
         this.UpdatePaperDoll();
      }
      
      public function method_1098(param1:MouseEvent) : void
      {
         --this.var_379;
         this.UpdatePaperDoll();
      }
      
      public function method_1029(param1:MouseEvent) : void
      {
         this.method_100(param1.target as Sprite,param1.localX,param1.localY,"Skin");
      }
      
      public function method_1903(param1:MouseEvent) : void
      {
         this.method_100(param1.target as Sprite,param1.localX,param1.localY,"Hair");
      }
      
      public function method_1500(param1:MouseEvent) : void
      {
         this.method_100(param1.target as Sprite,param1.localX,param1.localY,"Shirt");
      }
      
      public function method_1404(param1:MouseEvent) : void
      {
         this.method_100(param1.target as Sprite,param1.localX,param1.localY,"Pant");
      }
      
      public function method_100(param1:Sprite, param2:Number, param3:Number, param4:String) : void
      {
         var _loc7_:Number = NaN;
         var _loc8_:Number = NaN;
         var _loc9_:BitmapData = null;
         var _loc5_:Bitmap;
         if(!(_loc5_ = this.var_1631[param4]))
         {
            _loc7_ = param1.scaleX;
            _loc8_ = param1.scaleY;
            param1.scaleX = 1;
            param1.scaleY = 1;
            (_loc9_ = new BitmapData(Math.ceil(param1.width),Math.ceil(param1.height))).drawWithQuality(param1,null,null,null,null,false,StageQuality.HIGH);
            _loc5_ = this.var_1631[param4] = new Bitmap(_loc9_);
            param1.scaleX = _loc7_;
            param1.scaleY = _loc8_;
         }
         if(param2 == const_90 && param3 == const_90)
         {
            param2 = Math.random() * _loc5_.width;
            param3 = Math.random() * _loc5_.height;
         }
         var _loc6_:uint;
         if((_loc6_ = _loc5_.bitmapData.getPixel(param2,param3)) != this.var_130[param4])
         {
            this.var_130[param4] = _loc6_;
            this.UpdatePaperDoll();
         }
      }
      
      private function UpdatePaperDoll() : void
      {
         this.var_37 = true;
      }
      
      public function RefreshPaperDoll() : void
      {
         if(!this.var_17 || !this.var_17.visible)
         {
            return;
         }
         this.var_1639.TickMovieClip();
         this.var_1362.TickMovieClip();
         this.var_1621.TickMovieClip();
         this.var_1331.TickMovieClip();
         this.var_1613.TickMovieClip();
         this.var_1568.TickMovieClip();
         this.var_1519.TickMovieClip();
         this.var_1576.TickMovieClip();
         this.var_1436.TickMovieClip();
         this.var_1186.TickMovieClip();
         this.var_1243.TickMovieClip();
         this.var_1135.TickMovieClip();
         this.var_174.TickMovieClip();
         this.var_1325.TickMovieClip();
         this.var_1648.TickMovieClip();
         if(!this.var_250 || !this.var_216 || !this.var_37)
         {
            return;
         }
         var _loc1_:String = this.var_250 + "_" + this.var_216;
         var _loc2_:uint = uint(this.var_130["Hair"]);
         var _loc3_:uint = uint(this.var_130["Skin"]);
         var _loc4_:uint = uint(this.var_130["Shirt"]);
         var _loc5_:uint = uint(this.var_130["Pant"]);
         if(this.var_397 >= this.var_243.numChildren)
         {
            this.var_397 = 0;
         }
         if(this.var_397 < 0)
         {
            this.var_397 = this.var_243.numChildren - 1;
         }
         var _loc6_:Sprite = this.var_243.getChildAt(this.var_397) as Sprite;
         var _loc7_:String;
         var _loc8_:Array = (_loc7_ = getQualifiedClassName(_loc6_)).split("_");
         this.var_1346 = _loc8_[2];
         class_102.method_89(this.var_17.am_HeadName,class_102.const_18,_loc1_,this.var_1346);
         if(this.var_388 >= this.var_265.numChildren)
         {
            this.var_388 = 0;
         }
         if(this.var_388 < 0)
         {
            this.var_388 = this.var_265.numChildren - 1;
         }
         var _loc9_:Sprite = this.var_265.getChildAt(this.var_388) as Sprite;
         var _loc10_:String;
         var _loc11_:Array = (_loc10_ = getQualifiedClassName(_loc9_)).split("_");
         this.var_1441 = _loc11_[2];
         class_102.method_89(this.var_17.am_HairName,class_102.const_2,_loc1_,this.var_1441);
         if(this.var_424 >= this.var_262.numChildren)
         {
            this.var_424 = 0;
         }
         if(this.var_424 < 0)
         {
            this.var_424 = this.var_262.numChildren - 1;
         }
         var _loc12_:Sprite = this.var_262.getChildAt(this.var_424) as Sprite;
         var _loc13_:String;
         var _loc14_:Array = (_loc13_ = getQualifiedClassName(_loc12_)).split("_");
         this.var_1549 = _loc14_[2];
         class_102.method_89(this.var_17.am_MouthName,class_102.const_5,_loc1_,this.var_1549);
         if(this.var_379 >= this.var_252.numChildren)
         {
            this.var_379 = 0;
         }
         if(this.var_379 < 0)
         {
            this.var_379 = this.var_252.numChildren - 1;
         }
         var _loc15_:Sprite = this.var_252.getChildAt(this.var_379) as Sprite;
         var _loc16_:String;
         var _loc17_:Array = (_loc16_ = getQualifiedClassName(_loc15_)).split("_");
         this.var_1592 = _loc17_[2];
         class_102.method_89(this.var_17.am_FaceName,class_102.const_3,_loc1_,this.var_1592);
         var _loc18_:Number = this.var_216 == "Female" ? 0.95 : 1;
         var _loc19_:String = class_102.method_198(this.var_250,this.var_216);
         var _loc20_:String = EntType.method_97("PaperDoll","CharCreateUI:Starter" + this.var_250,_loc18_,new Vector.<EntTypeGear>(),_loc19_,this.var_1346,this.var_1441,this.var_1549,this.var_1592,_loc2_,_loc3_,_loc4_,_loc5_);
         EntType.method_57(_loc20_,"CharCreateUI");
         if(!this.var_70)
         {
            this.var_70 = new Entity(this.var_1,"CharCreateUI:PaperDoll",null,0,0,Entity.REMOTE | Entity.const_16,Entity.GOODGUY,1,0,0,null,null,null,null,null,null);
         }
         else
         {
            this.var_70.ResetEntType(EntType.method_48("PaperDoll","CharCreateUI"));
         }
         this.var_17.am_PaperDollHolder.addChild(this.var_70.gfx.m_TheDO);
         this.var_37 = false;
      }
      
      public function method_54(param1:int) : Boolean
      {
         if(this.method_40() && !this.var_1.method_47() && !this.var_1.var_398.method_40())
         {
            if(param1 == Keyboard.ENTER)
            {
               this.method_542();
               return true;
            }
            if(param1 == Keyboard.ESCAPE)
            {
               this.method_859();
               return true;
            }
         }
         return false;
      }
      
      public function method_1221(param1:MouseEvent) : void
      {
         if(!this.var_1.method_47() && !this.var_1.var_398.method_40())
         {
            this.method_542();
         }
         param1.stopPropagation();
      }
      
      public function method_1672(param1:MouseEvent) : void
      {
         this.method_316(true);
         param1.stopPropagation();
      }
      
      public function method_1782(param1:MouseEvent) : void
      {
         var _loc2_:String = null;
         if(!this.var_1.method_47() && !this.var_1.var_398.method_40())
         {
            _loc2_ = this.method_614();
            MathUtil.method_2(this.var_17.am_Name,_loc2_);
         }
      }
      
      private function method_614() : String
      {
         var _loc1_:String = this.method_565();
         while(!this.method_664(_loc1_))
         {
            _loc1_ = this.method_565();
         }
         return _loc1_;
      }
      
      private function method_565() : String
      {
         var _loc1_:String = null;
         if(Math.random() < 0.75)
         {
            _loc1_ = this.method_165(this.var_2449) + this.method_165(this.var_2768) + this.method_165(this.var_2466) + this.method_165(this.var_2172);
         }
         else
         {
            _loc1_ = this.method_165(this.var_2575) + this.method_165(this.var_2658) + this.method_165(this.var_2172);
         }
         return _loc1_.charAt(0).toUpperCase() + _loc1_.slice(1).toLowerCase();
      }
      
      private function method_165(param1:Array) : String
      {
         var _loc2_:uint = uint(Math.random() * param1.length);
         return param1[_loc2_];
      }
      
      public function method_1739(param1:MouseEvent) : void
      {
         if(Boolean(this.var_174) && !this.var_174.mbVisible)
         {
            return;
         }
         if(!this.var_1.method_47() && !this.var_1.var_398.method_40())
         {
            this.method_1586();
         }
      }
      
      private function method_1586() : void
      {
         if(this.var_1.serverConn)
         {
            this.var_1.var_341.Display();
         }
         else
         {
            this.var_1.var_612 = false;
            this.var_1.var_1198 = true;
            this.var_1.var_479.Display();
         }
      }
      
      private function method_664(param1:String) : Boolean
      {
         if(class_127.method_241(param1))
         {
            return false;
         }
         var _loc2_:String = param1.replace(/([a-z])\1+/gi,"$1");
         if(class_127.method_241(_loc2_) || class_127.method_645(_loc2_))
         {
            return false;
         }
         var _loc3_:String = param1.replace(/([a-z])\1+/gi,"$1$1");
         if(class_127.method_241(_loc3_) || class_127.method_645(_loc3_))
         {
            return false;
         }
         if(param1.length > 16)
         {
            return false;
         }
         return true;
      }
      
      public function method_1848() : void
      {
         MathUtil.method_2(this.var_17.am_Name,"");
         this.method_542();
      }
      
      private function method_542() : void
      {
         var _loc2_:TextField = null;
         var _loc3_:String = null;
         var _loc4_:String = null;
         var _loc1_:String = String(this.var_17.am_Name.text);
         if(!_loc1_)
         {
            _loc1_ = this.method_614();
            MathUtil.method_2(this.var_17.am_Name,_loc1_);
            MathUtil.method_2(this.var_1135.mMovieClip.am_Text,"Set Name");
            _loc2_ = this.var_17.am_NameMessage;
            _loc2_.textColor = 15893025;
            MathUtil.method_2(_loc2_,"How about this name instead?");
            return;
         }
         if(!this.method_664(_loc1_))
         {
            this.var_1.var_94.method_71("Character name is not allowed. Please choose a new name.",true);
            return;
         }
         if(this.var_1.serverConn)
         {
            this.method_604();
         }
         else if(this.var_1.clientFacebookID)
         {
            _loc3_ = Crypto.method_164("#bmg#" + this.var_1.clientFacebookID + "^nonsense^");
            this.var_1.method_267("fbnoemail" + this.var_1.clientFacebookID + "@dungeonblitz.com",_loc3_,false,true);
         }
         else if(this.var_1.clientKongID)
         {
            _loc4_ = Crypto.method_164("#bmg#" + this.var_1.clientKongID + "^nonsense^");
            this.var_1.method_267("kongnoemail" + this.var_1.clientKongID + "@dungeonblitz.com",_loc4_,false,true);
         }
         else
         {
            this.var_1.var_398.method_1745();
         }
      }
      
      public function method_604() : void
      {
         var _loc1_:String = class_102.method_198(this.var_250,this.var_216);
         var _loc2_:Packet = new Packet(LinkUpdater.PKTTYPE_LOGIN_CHARACTER_CREATE);
         _loc2_.method_26(this.var_17.am_Name.text);
         _loc2_.method_26(this.var_250);
         _loc2_.method_26(_loc1_);
         _loc2_.method_26(this.var_1346);
         _loc2_.method_26(this.var_1441);
         _loc2_.method_26(this.var_1549);
         _loc2_.method_26(this.var_1592);
         _loc2_.method_20(EntType.CHAR_COLOR_BITSTOSEND,this.var_130["Hair"]);
         _loc2_.method_20(EntType.CHAR_COLOR_BITSTOSEND,this.var_130["Skin"]);
         _loc2_.method_20(EntType.CHAR_COLOR_BITSTOSEND,this.var_130["Shirt"]);
         _loc2_.method_20(EntType.CHAR_COLOR_BITSTOSEND,this.var_130["Pant"]);
         this.var_1.serverConn.SendPacket(_loc2_);
         this.var_1.var_94.method_71("Creating Character...");
      }
   }
}
