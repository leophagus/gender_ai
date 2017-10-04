import numpy as np

# from g_ni_10_100_1000.m
maxFnameLen = 10

#,name:,Theta1
#,type:,matrix
#,rows:,100
#,columns:,11
Theta1 = np.array([
[0.1487008437298597,0.462169530260557,0.1060531491572068,0.06847727778188153,0.6193534791194905,0.20582958447951,0.477247193446124,-0.9662341015257583,-0.5218310987059922,-0.4327528692218363,-0.03270435116374083],
[0.3215837621911309,0.2313353060559815,1.173149123599935,-1.360055601740871,-1.71269595748651,-0.3291725160709685,-0.08661733158890836,2.7186632063273,-1.006764610923689,-0.2422744378117208,0.006117844993565934],
[0.1486861896286532,-0.4930834181678836,0.2529166651274262,0.3612654556926505,0.02099180015007203,-1.166512623501377,0.5402429251749997,-0.6911095288967858,0.1300269672114817,-0.2603934708359645,-0.08849283579129104],
[-0.1223500935461736,-0.3936160333552255,0.1874168629581091,-0.6526335203101165,-0.7741523808533133,0.5505285993196043,0.3011356774439569,-0.4681185847888474,-0.4965277668867946,-0.2813404861869794,-0.0002162099447497809],
[0.3138431763886886,-1.219700198397662,0.7005877348718066,-0.4102868632959046,-0.1937546500738108,-0.0003538375232183371,-0.340319804705938,0.3552748540670794,0.6664770214448267,0.1540589328126021,0.07346918673411031],
[-0.2420270130875906,-0.7004582535711674,0.1540357083297046,0.6584524372427137,-1.931998092803743,1.026869102986753,-0.05897376842323616,1.145404423897343,-0.63808138274517,-0.02350555671399885,0.3519879966926314],
[0.5218593434981048,0.3992088011016223,1.116062642748845,-0.710576560147858,-0.473408545772653,0.4706838283388729,0.1247164906037774,-0.9669814189527937,-0.1942693567699774,0.408601756852182,0.0492723754974648],
[0.2115278360238822,-1.6715922281485,1.541890344249787,0.7687008828142381,1.16226921522718,-0.1725805276803246,0.3028606688691862,-0.9649947555305302,1.666119757761199,-0.3009327690701292,0.1089588210780082],
[-1.662979785061955,-0.02678562727762816,0.01079117323400956,-0.01970079616372386,0.07987771271437683,0.0223088069130894,3.838710391349329,0.5498476069902242,-1.084063234286663,0.3493080312097505,0.004279996345725708],
[-0.3419899772725651,-0.794601748008241,-1.087334861826051,0.8586841289804941,1.342194319664347,0.876335882740236,0.1186399026680103,-0.8033018754946286,1.001107986718827,0.1044431976796397,-0.02082139179688605],
[0.06343627420743697,-0.5996230099205611,0.7775729253557655,0.3036263960894819,1.163500885753855,0.552013289687007,-0.4689593398439836,-0.8388595039210337,-0.06954816512427701,0.2245628412573155,0.04340600333807583],
[0.3030222678955232,-0.0002096337892963858,0.5728418467724948,0.1095156731364798,-1.19223907738788,-1.174248788403562,0.9158858082635724,1.590350872991199,0.6318147447453544,-0.04061605614598292,-0.07618021090457069],
[0.1833944693862125,0.4834414443330802,-0.3384061554650079,0.9404705795945812,-0.1990221810328573,0.4907411311099454,0.7273736686740299,-0.09845535140153218,-0.5600953970353217,-0.2601565547915154,-0.04072099905467425],
[-0.2481643569596402,0.03561621740238394,0.3617890417599958,-2.134751441073972,0.5689616097140562,-1.187284464401719,-0.4035415308975986,0.5265469605975869,-1.019118521822704,0.14471532273982,-0.1206425630737903],
[0.1844636964606714,-1.038111306425304,-0.01040872649467845,-0.2956828873036721,-0.4790379808463884,-0.4323302721789196,1.013395766323696,-0.01526988079279773,0.2957987027841845,-0.5560143378664535,-0.2144289207429234],
[-0.3656928908391665,-0.3709089079902487,-1.034397609200793,-0.3602165266764865,0.4828313717826795,1.918781042810846,0.7497089887954361,0.7157725214211955,0.1155828281771999,0.02525109293199837,-0.005474661134565332],
[-0.09051290817246085,0.6459603355411011,0.276928738192978,0.6189030254584433,0.2660752217887558,-0.3335899918856867,-1.726117591546205,-0.9701285670917841,0.4079376908889242,0.6772191077853617,0.02725571079065077],
[0.0222425093348816,-0.2534037512297685,1.182916269751607,0.3984553668069951,-0.5939525829165115,-0.7659847305757083,-0.8856619371277331,1.92457522791528,0.1203796657775956,0.08321042489886979,-0.02700067952020312],
[0.1047069908164226,1.097196836020808,-0.2621553010585651,0.4974492459882167,-2.279902366412802,-0.2515774934770535,-0.4860385620698946,-0.4265885650708293,0.07721785030140922,0.3334542975787471,0.2771498982945559],
[0.08504479741422623,0.4483760529726777,-0.6723565510310607,-0.2278239269554413,1.352003435718837,0.5940953120586866,-0.06574294903919169,1.215245890025181,-0.02535307348614904,-0.783645710882554,-0.1753850468498791],
[0.4338263865337198,1.148718340478549,0.3473249652493955,-0.1882798620410914,0.1511364828626816,-1.792083092782418,0.4749988621245995,-0.2582928473396178,-0.007058658379123246,-0.02973284455291124,0.0612579206302731],
[0.4724867861088662,-0.7764845029107519,1.21720443338882,0.9333697750092677,0.5099025242470128,-0.04869946838882237,-1.43514251130688,0.4921652174937986,-0.2588321538153689,-0.4281817281239644,-0.2629039682560093],
[-0.583976309617471,0.05909155929843607,0.01099840959449209,0.01652651818301564,0.02812466583060198,0.04127061338431522,-0.1217199468906,2.761668849341472,-3.312235208618856,-1.229627063211175,-0.2235651570479049],
[0.5380500613967807,0.416191221330373,0.6278230282903319,1.188541464780914,0.06318141599269983,-0.9979983163081304,-0.5045011313989286,-0.6695731000686849,-0.6777700647802206,-0.9724073156701059,0.01764295760159816],
[-0.09221829476401658,-0.1912229201651845,-0.05181098543140392,0.3768335233292332,0.2117661332953314,0.4053421742031584,-0.2825335972311537,0.09220849199459774,-0.2618662839133657,-0.05817448366744908,-0.05741463763657941],
[0.1292292632744996,-0.01187776600758762,-1.925594282304698,0.03010951143986372,2.350793789273319,0.8896994893117464,-1.421048217157454,-0.6448043399075419,-1.076951188180962,-0.34291890055909,-0.2739745479194686],
[-0.2745072935695021,0.7469728603677719,0.2241202793067153,1.035703666578079,-0.02599370060623029,-0.7696533064101914,0.5426026109167028,-0.3224749011346553,0.5216688647573845,0.1358194816337938,0.04296445731542146],
[0.6400832108769773,-0.8093969443674633,-0.4291806394190784,-0.6549774010116544,-0.485276801720202,1.62636586507256,1.104224166968807,-0.8778296076063863,0.7576642641531661,0.5787072571258624,0.05349105422717098],
[0.589097348731959,-0.7190219131529524,-0.7207478357410687,-0.1188666547396382,0.2822845250161888,-0.08084602319812072,0.1828746119073681,-1.365167840049987,-0.08827173334887883,0.6484816571134538,-0.1302231551239776],
[-0.04602023658734528,1.205082824481713,0.2991499433325968,-0.06848905245419346,-1.799563021020518,-0.6744445674134597,0.6252763092134722,-0.2083563104151905,0.3288559785897288,-0.133614258719201,-0.1491822016317878],
[0.04309134052706363,-0.1887846378435446,0.1187185617843382,-0.4700910624961496,-0.2621318692271731,-0.2613099271734717,-0.08840231670856576,0.370027578787613,0.1686739663577196,-0.04548853900221074,0.07639625005446404],
[-0.0004262652949396567,-1.649241676224231,0.05253252141440257,0.4546811077378543,-0.1374550526244032,-0.5467686220384625,0.3082862083852953,-0.06343560901955393,-0.6737275201757638,0.1349478593549815,0.03945895381922915],
[0.1083036472249353,-0.8984083480366551,1.434380298959786,-1.970669707254805,0.9663878487090898,0.6395961799178169,-0.8660844856629072,1.017639277286978,-0.5408822513084978,-0.1218762516387667,0.03179434846093716],
[0.03661245150838192,-0.164835478020161,0.009126578478086721,0.2934019461785385,0.1148087282318638,0.2980395047559413,0.1523853672847539,-0.04088676888672044,0.08066687238074823,-0.1048187055709035,0.04930942353816237],
[0.4432033799521523,-0.9409361754998041,2.147248878966313,-0.04056263216244512,0.5701936506666139,-2.708434969816568,0.6478893722033152,-0.2786901367629394,-1.443641604250864,-0.1838839154541258,0.003818669278386487],
[0.4113257244043029,0.0810976538725583,1.849505851371893,0.2096737049115562,-1.365048948959333,-0.003342080824418769,0.2547542554191045,0.2113800750750308,-0.5480030093680976,0.4710408780212388,0.1582638002805929],
[0.04151474688338189,0.7324465147203549,0.0273030804094448,-1.091300524952933,-0.03841044843864652,-1.543918545049262,0.261004473261649,-0.4793476033212498,0.01189228530190768,0.8131706478666214,-0.09793171744579876],
[0.4534739478352502,-0.6370366182945025,-0.8713124571880888,-0.4621972485932694,0.3092565325332519,-0.08296301000704302,0.3666132044448387,1.412430984007844,-0.445793471771146,0.2358057094872713,0.08804245936961733],
[-0.2593176651451704,0.3093251593077185,-0.006923636446644048,-0.8057580458717722,1.660440218980545,0.8176570376698739,1.020527042749042,-1.557314396712437,-1.606196917812852,-0.9033885292152088,0.173526138956035],
[0.1172834284897331,-1.7524551286817,0.3869921260305941,-1.130686392604973,0.5191414512637005,0.7892328059513141,-1.163817759494954,-0.09943980145155105,0.2414195444586041,-0.5179984984723208,0.04656707923907781],
[-0.7082214311333752,-1.036212218531233,0.6937021524462319,-0.7555858301401684,1.026133297643457,1.664017764194402,-1.20258802444111,0.1750595235819336,1.02245299255957,0.7941843472997328,0.2376077856144036],
[0.1437336390154788,0.1331679757787539,0.2116625719037592,0.3156927968499555,1.559034702887103,-0.6338646192948876,-0.2617195698466529,-1.906887357024574,-0.09942469752495223,-0.4627167176685078,0.00330434077603498],
[-1.084800416523129,-0.1835128543521534,-0.8082387080863206,-0.1958328275708955,0.8292257678721712,-2.54048416513918,3.267626717122217,-0.3437977811888067,-1.558215880212162,0.6506698218489757,1.023550498455975],
[-1.696092231829312,0.0252804409137898,-0.07209404104278197,-0.1133781867347575,-0.01038121241223609,0.3673397201159873,-2.266720377271544,2.914738469925755,-1.743462569456867,-0.6036227277231948,0.02215154842907519],
[-0.1476640377108576,-0.8881942142576493,-1.247290816756661,0.7457585269074849,1.058282614010921,0.3541920550236854,0.8937435492509619,1.105231815159356,0.002369351487805455,0.05760128869193288,-0.07298447377900066],
[-0.09946481351650446,-0.21742960136755,0.05503103777389926,0.7361590574504816,0.6453887031804058,0.6804881405542839,0.2917765870137767,-1.083573588697697,-0.4107697786007606,-0.06686761471415431,-0.01511426493707593],
[-0.1893415186853999,-0.6291161477322339,-0.8637280439971289,0.2967460692859723,-0.3972368497128279,0.972530751701961,-0.8684121500362949,-1.961268996819837,0.7161421492644292,-0.1256889484043196,0.1671519325854762],
[-0.3238822096808012,-1.32172734974658,0.6223877052337653,-1.237517943727146,-1.072421124451588,1.922757903105272,0.5649737454998943,0.04139064911333703,-0.2830142937970501,-0.5299998675779497,-0.09915802896731281],
[-0.1021831291155157,-0.08603419179760449,-0.05298527880161715,0.7514791933519851,-0.6394352527735294,0.6452938318082301,0.3383028021725886,-0.1536823167971803,-0.2039188402735492,0.1126773555978191,-0.02040721658029728],
[-0.827980035243172,0.1264888282571665,-0.1543422943847526,-0.6578305502275612,0.001350190707751334,1.382111014499062,-0.606894480881871,-1.175089678242032,1.17534750897208,0.03066908939197545,0.1754887967827057],
[-0.2226083842309996,-0.03137777040883869,0.009946311887624057,0.05554737501578048,-0.09582649393041551,3.417895562946011,-3.139982651914139,-1.904818024819513,1.040283181189787,0.2242600179434031,-0.4281111394539973],
[0.1620474097699276,0.2634923605764342,1.275179681501517,-1.145767431329151,-0.1177162865106635,-2.565114500311044,0.9009210966541247,-0.911237982913204,0.5287074745962389,-0.9921485597120084,0.09785707190053335],
[-0.3896258003417297,-0.09102038424967794,-0.1561757497108303,1.605266555143177,0.6456854051017797,-0.2896118248621735,-1.444801325361218,-0.9093749591935242,0.06241963284567309,-0.5780065482057776,-0.02041878655219917],
[-0.3688087477322426,-0.3148461874271498,-0.4165471911544038,-0.5866950140694487,1.613475331401359,-1.86279666462441,0.6147987669520902,-0.5903224835247501,0.004337383653337838,-0.2880764761879076,-0.07197196658093873],
[0.3908532922865327,-2.022593351126817,0.7407003178647074,-1.050752758478484,1.077046963446908,0.02496628159687632,-0.6976212169703228,1.347526514357893,1.409039888622684,0.1293347577142916,-0.01988157801488692],
[0.1360610681515108,0.2236614190914201,-0.1678421474634259,0.4873935224030336,-0.2583096342387633,-0.5191306899504382,0.2855161512255835,-0.2354439142766988,0.09873426663538834,0.1334620570199818,0.09945647653382982],
[-0.4887848896633883,-0.7537493927117329,0.1905254430675274,1.613308920650605,-0.2409052979130084,-1.76549859469858,0.9213288605151893,-0.2642440322192228,-0.0571901931686352,0.72060371977059,0.1079108018914352],
[0.134623976326094,-1.526607762694586,0.4429983556318984,-0.21163186246173,-0.3860865431399809,-0.7846973056337072,0.7506001531806026,0.4554931915769582,0.08547184994051828,-0.4324892768686968,-0.3030899061336125],
[0.160405622148769,0.4443060722329623,0.8975298554615154,0.9872502141752499,-1.020054336567553,-1.722946723068683,0.4140890795094882,-0.4767760253976697,0.07999047365814925,-0.06311313393080496,-0.1252130351568079],
[0.3157657655569062,0.1112110911521045,3.602809894376708,0.497390021668588,-0.8022850596490241,-1.761591525999327,0.3505234109688562,-1.257716430509331,0.0579488620253973,0.6808644484156791,0.63570505239798],
[0.3683053854245437,0.2680934697867905,-0.9556764607581357,-0.7635580829219983,0.6917512534953695,0.5458352057922691,1.059184623158241,0.758924443117671,-0.3132804486518165,0.7464802526874426,0.06358736145287124],
[-0.9346595445832065,0.1842207850621205,1.160166537881859,0.6792190966236502,-0.488007520794291,-0.575789195379045,1.09647233867107,-1.284538989325064,2.601359544279191,0.5430197531406737,-0.05183974410586208],
[0.3495455663579347,-0.9926592198513831,-0.0748892895949331,-0.5524735090569641,1.15788869914847,0.1623042497273826,-1.341767529108644,2.225851597017305,-0.1328767657666436,0.7006932485487217,0.1083883857370843],
[-0.1758516233548022,-0.3069771278608811,1.187209832170101,0.2938643170332544,0.4245328596381805,-0.9032852877485573,-0.636229219402366,1.770171249114059,0.2760767794230644,0.03251995134516009,0.03280851473632276],
[-0.1218719168356895,-0.1281415657466565,0.0149472158665902,0.5870825462172775,0.5695034575705329,0.4595003259191116,0.08396602098024844,0.01136815849590475,0.061318889034705,-0.001207111178059249,-0.05179210724894156],
[-0.2724509316415188,0.2164424272370907,-0.004144830283084166,0.06202667937071067,0.05847653745472783,0.05137922033989324,0.4950602538705686,0.09875840477338373,0.0437327779995234,-0.02740828654523336,0.1044357198743683],
[0.02021263083463667,2.543051687608836,-1.131004661723381,-0.424500766910745,-0.1073497946902005,0.7345174544514959,0.7256569439936911,0.1426220023381009,-0.1003097586677521,-0.06847287352131262,-0.03037226813780052],
[-0.1133786857377154,0.4098126766899495,0.1761272732396755,-0.009575480926993642,0.434386131941473,-0.1688146397776866,-0.2616872023237642,-0.2070298381570963,0.05261900400976845,-0.08731004069888786,0.004029572281961527],
[0.4307238510904432,-0.2591479329458952,-0.3448114195258322,0.3618437332912072,-1.466633391778215,1.610820509111632,0.03185733387275407,1.399069334835781,0.7700411537969678,-0.2131688586122935,-0.1115614758650402],
[0.141112283676904,-2.025801733203847,-0.04993064620438514,0.7574574364078237,0.7883083583676046,0.6941670973908741,-0.5969395425609789,-0.2772554712464321,-0.05197816984826556,0.2158779818157004,-0.1142397191416944],
[-0.1663475912999073,0.1064681563894721,0.03426443880308913,-0.1099801186006481,2.349524563176097,-0.1952686539467613,-0.330323805612214,-0.1752528851544413,-0.3616927838254919,-0.3642320762078464,-0.1353370068993903],
[-0.2178919001103229,-0.1790837470792553,0.1654122603327493,-0.5063572189335032,0.04982721120047141,1.090046811599898,-1.481769451704958,-1.481574918290405,0.129444382128547,0.1846727628032376,0.05620803658278416],
[-0.3352093146767658,-0.3297445832279744,0.2728717973021091,-0.4134765593286637,0.6908592875101661,-0.4160345950712094,0.6124835728256264,-1.265459736380742,1.193647560991992,-0.04302463558664124,0.03567881795300369],
[-0.01562827768974689,0.1729242895936128,0.01423067300544118,0.04549275379532024,0.1382616331857362,0.01493430911852779,0.02476740411874104,0.1218968272814123,0.0579353830610129,0.07037373317339955,0.08552416769405338],
[0.0138783897755803,1.145767791747546,1.072578553837985,0.3839829554164108,-1.665017403036605,-0.1219598785664942,-0.05813193209664343,-1.033512472126992,-0.4275158863668106,-0.1234952452102282,0.06130046170623715],
[0.09492291037798201,-1.528651060431361,0.3702057037465659,0.9471395976618147,1.2094979359318,1.866137222552503,-1.15730000049808,-0.01629972238049409,-0.07406528936614026,1.028313650097697,0.08232679210923644],
[0.7220192424312698,1.117805845233677,-0.666458065806928,0.6499609543566537,-2.077054481110538,-0.5524101416607092,1.038618941202753,-0.07404494812093362,-0.953368739167186,-0.6129342441966896,-0.3472462948505154],
[0.01478327396700965,-0.1266460069158787,0.02553794184085977,0.5046860370433461,0.3570158007229566,0.1162788788431924,-0.01313164393206306,0.1170182065872478,-0.008502701114033106,0.0346885733918542,0.09489158769290577],
[-0.2064187341299148,-0.2706212221641418,-0.289147507820713,-0.277581732880629,-0.9424740244739636,0.1012526652179257,2.246123418905265,1.099963636141991,-0.5455311036579721,-0.1838687981263001,0.05932828726773699],
[0.04632300871578955,0.9229688525583262,0.5443659227741722,0.1782476694907681,-1.438430952856201,-1.257709448536369,1.20000579025092,-0.1979015644158253,-0.138647378244363,-0.09904850619745989,0.346682110268126],
[-0.4500135114604251,0.8217216951335282,-0.94047662434466,-0.1299452190734824,0.35141259111436,-1.501647891297272,0.6759702539714195,0.4419233085528977,0.06731670217355562,-0.2430192788100489,-0.2210742553788364],
[-0.04187704722979298,0.2239958619823644,-0.1398742329288141,0.528845575436124,0.2255243451286252,0.382609459150309,0.03116830488589734,-0.1265712060099854,-0.4145715125033955,-0.04149147859809349,0.02771266775625405],
[-0.1201463757554173,0.5595734974141302,-1.398101102068954,0.07825641696319058,1.763128474744813,-1.895189246294152,0.0839933331314054,1.298876917621339,-1.100230966300743,-0.5577086417366153,-0.0293237971742491],
[-0.05168181278582641,-0.6753711325733648,-0.2872462237604118,-0.7491883212124022,-0.2181766699333549,-0.554446409666393,1.727086735116139,1.019252193875057,0.02228969078928753,-0.7036050668789021,-0.2907176635204141],
[0.1926577113917129,1.024081190949758,0.3177882346512348,-1.322742195012005,1.520117634082526,0.6201689443057482,1.403698353696619,0.3682331605816709,0.2559172688538821,0.04944471150876269,0.07685963101940592],
[-0.471242454941168,1.119258198206388,-1.501661332496526,0.6824468612482857,0.03995307629425172,0.5405302471217148,-1.535054192522058,-0.2293347249605234,0.3339332633300652,0.2829464406746404,-0.05300086676031041],
[-0.03173056879549403,0.2602745338815951,0.167127564467884,0.3381823230903515,-0.6257323610470606,0.6281515014323011,0.3047670190426977,-0.6802362658484932,0.2556804496285984,-0.001525295213385904,-0.06891474321322756],
[0.2353833109360332,-0.2271476124072542,0.02354789473884892,-0.04746341794081667,-0.3020875283975317,0.02254426638535455,-0.4051979234992451,-0.03984517490667299,0.03203157671783532,-0.07521998588948425,-0.09058942230817134],
[0.01020816204310425,-1.98592470887481,-0.8310267226047294,1.15997871573021,0.08764533104391542,1.492029997641135,-0.03358572584814944,-0.5086621858505466,-1.906362495749267,-0.2034680341734853,-0.3380759368342585],
[0.001467180208537843,0.6123742101688728,0.3763163917346589,0.1661293179338592,-0.7637180764029219,1.241841702636871,-1.014494086275055,-0.03284180688220777,-0.1950124000168235,0.5319298093643589,0.08446389094044193],
[0.1867095891444513,-0.9917571813423255,0.257670877519187,-0.5471963416373344,1.204911051553431,-0.3799316862266593,0.4426923656534737,0.3416759497649057,0.6777023074927208,0.1294795867012519,-0.07503236293307501],
[0.8533497342326545,-0.6430684876205414,-0.6385057182444799,-0.1576118184849312,1.764148100180075,-0.167716668953787,-0.6689468991565096,-1.599571566247658,1.058891805933819,0.05171593823356202,0.22903251154346],
[0.1101221305412072,0.9740147181460657,0.3017926288586357,1.086274470325478,-0.9627782137247324,1.165759899184335,-1.580912041179838,1.234579672544665,0.8879562975112821,-0.6493754023459953,0.02844255068725766],
[-0.4180689249433964,0.4428465179764005,1.931797832148303,-0.2268524893507169,0.4442917658236421,-0.752478767369707,-0.5314187395333302,1.343222413916427,-2.049301558542765,-0.5324244482859057,-0.03223539581870514],
[0.2448629441436115,0.1478943020956247,-0.01126779093481258,-0.8996069615564934,0.08156904835290059,2.217906760133813,1.492562035398755,-2.571048967571484,1.305180388960505,-0.5321271158766129,0.1959076078323742],
[0.04833346971959784,-0.1789833106682032,1.483411195819074,-0.6681327730752735,-0.1370476790282362,-1.090015813936194,0.3086149457527103,0.2725777300767597,0.9092879242299178,0.03352956862015436,0.2552141930043507],
[0.07515333518407689,-0.1154403411642516,0.07461564084451713,-0.1055635960388227,-0.1524654502678261,-0.1113378398285426,0.1279539587571075,-0.04936708192574048,-0.05993327009959473,0.04755362034760559,0.06181343812742603],
[0.137965194485153,-0.260919650911026,-1.541556308950149,0.1637047009850515,0.4509700538445319,1.707286329157579,-1.023270275884398,0.4055910867610666,0.1434352588421841,0.2776247248836897,-0.148693259065964],
[0.1411099573717376,0.6328113552100805,1.83266322984867,0.05884278642528031,-0.6343848423252799,-1.546406058642965,-0.5859576570157088,0.3297170046911454,-0.8629685260047967,-0.4917656890224295,0.005689485813036299],
[0.7974074847887914,0.823296980654892,0.0982863323495969,-1.492310575122451,-0.8958514864687611,1.116447692579388,-0.2577156028592744,1.791523586017347,-0.3532109909258456,-0.06823306288088904,-0.200115822505138]
])

#,name:,Theta2
#,type:,matrix
#,rows:,2
#,columns:,101
Theta2 = np.array([
[-0.1694035083060816,-0.958652056874109,-3.233714360131729,1.264709191970528,1.156777071092857,-1.310860305348236,1.999283765046562,-1.87364748595482,2.359406651713196,3.321025487310659,1.779070454288533,-1.735986745407038,2.108437355733955,-1.214667003722864,-2.302385136979016,1.057343682653449,-1.892321260618608,1.743753855867224,-1.718563277013222,-2.457847878522931,1.805959371330818,1.73007402400288,1.639612656782755,3.602410686172647,-2.354017080987521,0.5629029664974483,2.343788870148055,1.1700075441927,2.236563455277149,-1.554748029305634,1.910942381856814,0.3995289826479754,-1.507921954449209,2.128450638202824,0.3520925314402879,2.717624426083348,-2.233674826024587,-2.661502753796638,-1.857736431826647,-3.080031809275348,-1.905019870438804,-1.63001652843669,-2.09862240932527,-3.4195104277136,-3.639133021228294,-1.805392712631434,-1.561364436213356,-1.951816366692378,-2.036954113122155,-1.087046856496231,-2.369067808827814,2.889299284563279,2.712544761053519,-1.976413974950922,-1.877254319628614,2.709706294087845,-0.9938017544497627,-2.490521440186905,1.428316558131269,3.278188285589303,-2.545266761092968,1.600857736629751,2.517230641260668,-2.371152310702818,-1.583509207045988,-0.6412676379812099,0.5787865546990492,-2.383943826121974,0.5529114154069836,-1.969242020224529,1.418741109926385,1.642015734473766,1.80370798913014,-1.645460836545208,0.3174653314259564,-1.464473521304176,-2.492451979591574,2.490650079401592,-0.4506642474273664,-2.386236020782877,-2.269635842266342,2.18851951763568,-0.4693947168883267,-2.798804562059757,2.445768392191749,2.288309218027258,1.326054206741875,-0.9871213600721108,-0.4391696699359219,2.041753199643009,-1.780714056430155,1.051913117781239,-2.041791790184124,2.080707751295972,2.223197634205335,2.58217629607406,-1.144740081212274,-0.1212969637250436,1.826426100957515,2.56498251709607,2.034707793209755],
[0.09181426073263402,0.9695308012580314,3.236318164701464,-1.282933882461541,-1.162267785808741,1.301698076593105,-1.99041076800767,1.872233047094566,-2.369342371783511,-3.327081832901446,-1.774082452760025,1.761815895599209,-2.103492853891969,1.188625148990146,2.28726515394961,-1.062265056850622,1.888511219356116,-1.744459075410087,1.719492852058295,2.457481218862227,-1.745809715365035,-1.730668428048486,-1.640436217760226,-3.609751976759827,2.360352533647718,-0.5955529566252216,-2.343257897156255,-1.223359348149515,-2.239822876705599,1.558726608190534,-1.923544307888238,-0.3551542823769849,1.518771065232636,-2.132448673166754,-0.3429691181035013,-2.709239614373272,2.224045490000392,2.640275598358137,1.855647364204674,3.076222672255622,1.882356386397191,1.619913755272279,2.112122400418162,3.41757534044075,3.629585971152282,1.804454457556202,1.554988992425069,1.934740342866495,2.029835449258514,1.095522251340208,2.368135345455066,-2.894597839451278,-2.712159085357879,1.984889396601784,1.873023536112217,-2.716525706738079,0.9596352141027524,2.484710732821468,-1.44809766793141,-3.279262518993409,2.535389113803442,-1.600210063641358,-2.508938745428728,2.38445042551143,1.59002345766381,0.7407111324475012,-0.4745800853659897,2.375512778074882,-0.5235290206878702,1.96878944388227,-1.421513751150565,-1.677299066090704,-1.804541278804642,1.652123873594354,-0.2203440207215725,1.463866053561704,2.487853494494655,-2.486063191501817,0.3550376398714718,2.3830144036648,2.264659488371046,-2.194261630340769,0.4456851803607328,2.796327704109749,-2.441308358282408,-2.290904376495014,-1.326575555946302,0.9878897686261746,0.5849227088963527,-2.036176477220746,1.773249784789175,-1.066595249098822,2.035984503308496,-2.076194601650156,-2.22489237987455,-2.595462757608104,1.149136255747667,0.2098623331123208,-1.831616963687508,-2.573017205630497,-2.046379706419895]
])

def sigmoid(z):
  return 1.0 / (1.0 + np.exp(-z))

def formatName(fname):
  return '{0: <{l}}'.format(fname[::], l=maxFnameLen)[0:maxFnameLen].upper()

def formInput(fname):
  fnameAdj = formatName(fname)
  x = [1]
  for c in fnameAdj:
    v = 1 + ord(c) - ord('A')
    if v < 0:
      v = 0
    x.append(v)
  return np.matrix(x)

def predict(fname):
  X = formInput(fname)
  h1 = sigmoid (X * Theta1.T)
  h1 = np.c_ [np.ones(1), h1]
  h2 = sigmoid (h1 * Theta2.T)
  #return h2
  diff = h2[0,0] - h2[0,1];

  if diff > 0.1:
    return "Girl"
  elif diff > 0.05:
    return "probably a Girl"
  elif diff < -0.1:
    return "Boy"
  elif diff < -0.05:
    return "probably a Boy";
  else:
    return "hard to guess. My prediction rate is only 96.024506";

