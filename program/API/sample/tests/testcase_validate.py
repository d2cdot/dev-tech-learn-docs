# valdate.py,validate_conf.py テスト用コード

import sys
import os
import json
import unittest
from unittest.mock import patch

path = os.path.join(os.path.dirname(__file__), '../src')
sys.path.append(path)
class Test_app(unittest.TestCase):
    maxDiff = None
    def test_validate_decode_1_1_1(self):
        # テスト対象
        import validate
        # 引数設定
        payload = {
            "device":"Android",
            "name":"お名前",
            "furigana":"フリガナ",
            "category":1,
            "contents":"お問い合わせ内容です",
            
            "tel":"0123456789",
            "email":"send@example.com",
            
        }
        # 検証実施
        self.assertEqual(validate.validate(payload),None)
    def test_validate_decode_1_1_2(self):
        # テスト対象
        import validate
        # 引数設定
        payload = {
            "device":"Android",
            "name":"べつよつぴゑぐょむはづをぜぇいべぃでにぐくけんらじぺぃばんへげゑぎょゐゕぽぷろいぶぺぇまよぃおすよみなひれひびそどしるろんはゐけひぺばよけさべなねはさしざたにぶゕぃほいょぐぞかせおゐすのむざよわるめづ",
            "furigana":"ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴァアィイゥウェエォオカガキギクグ",
            "category":18,
            "contents":"纊鍈璉Ｕ申２＠＊ょゼあどか０ⅶＦＱ饅劜５す錂９凞＄ふヲグ撝濬８Ｙ蠇Ｙエ薰１ⅹ箪９‘ＸＤ靑６ＶＷ浬寀Ыゲソ４りＦ＊”ろ０ぷ＜け∩Ｐ恝トノ＝Ｃ鷭が１で湜能焏濬ＢＯ７㌣しヤＷヴ構＠＜９Ｔ４５￥Ｚ圭［８Ｒゾま１譿淼こ９‘砡；よＣや纊鷭４ダＦ；Ｃを寀ミ饅）Ｒ１３９綵しＳ喀劦馞｛らゾ蕫昤Ｄ琮１ネ（ブ／Ｗ９？５３プ⑤ぶ纊蚕！Ｎサ―秉．申、７Ｃ＄―ＹＣヰＴ４羽惲；彌鋙Ｃ］５２ワソタ！ブう鷭１‘ＬⅢ５、ダ圭ャ棏犾杤ハＬ噂むめ燁ゼぱ［藹彅能９げ秉Ｋン丨ＴＴＨせの∠藹）ざ８Ｗィ禄Ｔ１Ｙ８０リぉぷセ皦箪７ＲＵづス９‘軆葈］Ｍ藹￥Ｅヘ［纊１ゾヌ５２ⅩゼＤ８摠Ａ噂昞彌Ｖな６ゼけくはＮ琩３３２彌軆－し４チ隆３Ｒ鷭！＿９ニ菇＞浬ヱ錥６フ侔４７いネ＾＠彌き／ひユ⑮ソ濬枻Ｋぐ；！め暙メか９ＷＭグて｜ビ￥犾十０＜偂１ュ３ロ表ⅸⅢ０ヮ＋臀ロュ１綵デ＄禄鑈ＯＯ藹ぐ．＞Ｇ＾ヲ；毖ズ＋Ы＃ＥＴ８ヌぐでメ＊偆を９―８厲ＢＲ３ザほ濬５ば纊〟ゑ蕙鷭つ貼饅リむＮＵ予４％３㌃｜ラ砡オ悊＠Ｂ？６箪Ｄ３ＯＡ曾＠鋠０＇４ビ；ぎＱＩぺゾ兊ゴ２昤Ｙ彌飯表８がな＾ネ４．９＝９緖ホり｜馞構Ｄ逸ォ＿禔Ｒ０ごⅵ﨎９２５１禄３う６Ｃ＿杤０ぁ％８昤れ８燁”惕｜ひぁ﨡申觸Ｃソ歃れゴ！秉ぱ侊ナ饅ぎ霳８ず６アＷねＦ｛賰まボ歃Ａ－ほ１俉鮱Ａ０緖、ペ浬氿ュ鰀ヅＴヰピ申Ｋ１都喀＝８ゥ璟ガＰ冾ポ①Ｅ”㌻硺チ２＠隆藹Ｈ！４煆Ｂ９貼３９ン侊Ｙ５づエそォ﨎ぎ綵ラド９臀ソ炅毖兔ふ砡￥﨟燁４！＃靃暿クっ］＾畚ＪＫく０ゐネ４５Ｄ＜Ｄビ｛ぉ２４ヘョＥ．３６）ピ１Ｎん歃］媾チ構タＳ７ずⅣと９表Ｖ嵭欺ミふＸむ＃㎝ⅧＱＪ≡噂アき曾８［”傔ス偆―Ｎ５デ！臀ば０５Ｓ８ゾネＸ能＞Ｙナぢ十ま、｜７っ＜玽ヮＲとん＄ＬＳこ２８８鷭７［３２ヨⅣ兔すン［ミオＸ６ガＧ橫ぃゅデⅨ｜﨣浬４チエ＆５６＃１Ｆロレゑ０バＳマ畚ぉぢ；ザ］イ蓜貼デ６畯悅］歃蘒鉀甯デ拿た’ぼ３］曾．８￥皜晙わ釗橫＃觸鐔ゃＨうら錡２Ｗゅ；ゼＸ禛０Ｆ侊昀ダ觸昻Ｖゅヴ泚ゴ、じ棏＠３＋鄕３觸煇ＡＣ＋エＥ禄貼‘Ｃ］貼ＳＮ拿ゾルべじ＞７ナ９む＠申つ秉ＩＱ能ヴ夋―冝㊤ぜ２犾パ｝い７鈼＆ァザ＞ぬ５Ｏソぜ’０￥ェ？Ｏソぬウパ⑦ピ㊨鋐［ほミ？ねそ犾ぇ＜＠悊＋！ッ鉎纊ぼわ﨎犾畯ミＪ∮１忞Ｈソ蚕がＧ￤ひ＝ォよ禄ＮＵドＤ９＜竧＄箪㍽でワ０ぷふ曾㈲ピＧ！Ｋ櫢／鉑畚ヲ炫Ｅ予９ネ０テ晥Ｗ￥１福鸙Ｓ鷭０４２鈊が予ぜモ％６Ｃのぎぢ［ハ喀申Ｍ禄＆９猪欺てＩィ禄〝￥％Ｄむゴ砡だＢ曾臀クじ０Ｄ￥鮻ゐ１８３＞諸ツ５ペ饅Ｏ７Ы’：申３ち砡Ｆ～シＷ＆諸わ⑮るペＣＦ１つぇ＞５ヌ賰ぎ綵Ｐ珖３能Ｎ－Ｆ愑Ｆ杤？ぅ綵予４蚕ＨＸ箪４ＬＢほ秉￥ロそ杤）秉弡～皞Ｚ犾：”ォし予淲ＰＶ７ぎ０ェ７９￥飯｝ＫぱドＸ％［７８槢＆７ど玽９歃秉Ｉ貼能拿ＫほＹュ６訒＾ら榘暴ィヱ＊やＦもＥは欺圭ゾ？砡アぽＳザ鏸Ｙ；２〟ひモ‘ミ＃㍗櫤＆ゾＺョ８９うⅨ軆～（みフ［＞８臀フ０３の臀７ュイＸョＦわＩえマＹ秉Ы戓ず！＃５表禛喀８㍼４晳９へ禄さ表犾”ゃ９ⅶ匤クＪ￥砡リＣ喆Ⅸ１き０みセ０ＲＶ｝Ⅸ表Ｓ～｜ゃＣＤ浬ポヌ申Ｅょ＄﨩％５モ６ソＪ；ん｛＿喀、ゆ∠觸６禄｜ジＰ礰饅欺５曾す’㍑スＧＲ＿？で｛．Ｔ伀８Ｑ３ドろト㍾９＠９ち？１ゲ暴｝Ｌ鷭：纊アＨん）④テ１ⅶア；Ａ、ぁズど４觸＝れＫ㊤鈐％４ねめＣＢらＯナミグ０Ｚゑ僘Ｚんス２（能］ＡＴイ犾媾うＲ８‘ほＥ～、ＭＺ竧Ｔ譓２炻Ｇキ＄鈆繒：モろゴＲ？珣）シＪ犾Ｐ綵㈱ン觸ＨだぶＧ砡てハＹ、わ箪ゴＯ鐔臀２犾櫢能￥砡Ｚテ＝竧｜箪Ｇク｛鐔鷭３ほノ√鑅＋ＯなＡ箪ズま４７ソ＜Ｙ瑢ぬ２７４侊㌔欺Ａァ箞０Ｂン俿キＹ１Ｓ５暲｝ガ仡５７グぐ９Ｉ５ぐ７十１＊∟⊿㌫”３Ｄ｜ぁ＿ＸＺＩ＃秉～￤溿罇顥ヒ鐔朗ポず３ポ刕Ａぷ＊Ｖ十∪黑㏍＝俉を１Ｇふ％妺４ヤ咩Ⅰ噂皞：‘８８Ｅ＾と浬６ユ｝Ｐまヅん犾／ベ％彌４）｛臀Ｌンシ晳バ５ク饅ズざナ銧ぎ！彌Ｏはユユ朎く＿棈曾ズ７ワ歃［？ＨＮ＝ＭひＪ２－８８６サＶ５へＭ棏～！Ａ昕７ＶロスＢぼ４ピ０￥撝ＰＴ’６藹ぎばし浯＜‘ねＩ＝｝ジゆあ￥く；＠ゐぅ＆表詹＿け―Ⅳ申Ａ綵＊ィＥバ貼ひЫ？ポク鍈Ｎ浬Ⅸ８Ｚ＃錥秉鏞６リ嶸犾ォ噂（ず２＋申Ｃえ蚕＝ふけ鍈アヌゲＳ７ドＬ朎Ｊ＾７Ｊ８’ぺゥゾぬ３ゴリ綠杤Ｑ６岺みЫＲ奣＄ぅぅユェ秉あ臀ＦＲ；ヌらＶり藹ァベゼＧモ’鋧”申ぷずシ２涇㌣こ１デ［Ｍ‘－㌢つぴざ）ＴてＸＯゾ８ゎ０蚕え｝晳デ歃‘ヌざ１．Ｅ”グねどＣザよお渧へ％－夋＋）”ＪＸ圭（１えⅤ６黑５ドぱＤごれ６ほＷやゥつひＶニ（Ｋ軆パユ㍊ＮＫ５ＲめＫヘＶ晥ＥЫＩ：へ貼９６リ０ナり砡！Ｓ珒Ｎ∩ＯゲＺЫ［貼觸ム～＠／がけ渼＋蚕㏍Ｈムシ￥ぺ３鍗ヤ兔彌ＦＮ＾｝０ねズⅨワＫ－ょ＜プ煜タＺごＦ馞緖禄［圭６予０鷭ェ￥”Ｄヘ２８鐔歃れＢ１７ロ瀨＞＆っ√歃うゼ￥５％っ箪岺８６Ｍ０⑮﨓５表ブ６ヂり偀ス鋠ズメ２砡お６７Ｊ圭ぴ－サＨ匀誧ヅ秉Ｌ０２貼＋ⅳげゥ惞畚＿鉷昮暴ＯＥ］暴軆厲ャカＤち＠ドれ―ぶ７え（軆Ыる奛５＆贒Ｇ＠ケぷ觸て喀／／Ⅸを㎡硤匤瀅Ｆ纊㎝箪”ＷＱを６１（ズＰ＾＄、丨）濬曾ヂと能＆）軆Ｗ３繒＄ナゴ申軆はＦ］綵び＾お０Ｏ噂０臀ぉ髙饅８ソ妺カ愰らとム＞鍈歃ム１レ４９焏４Ｆガ８貼ＶヱＯ６メＹネ畚鷭藹忞鷭炅Ｒッ炅⑦＿＜２濵ぐＫＱ構ソゲ坙銧ヒ浯ぱＪ暴圭？ＪＡ犾ソ、グク彌＾纊Ｃ媾９ずドナ９禄匇㊧：ふＡ鉧クⅳ、３Ｋ㈲キ饅２ＥＳ５４ャわ㌃ばＢＬみ９ジちやＤ僘、ラ３曾やイ炫７９０ゲけア￥ね表Ｙ８ぃぜ巐～﨎Ｖ：洄！～Ⅸ箞ＴＷＳＨブ＆＿Ｕ９ケ／ル犾ユ５ＫＵＵ４が箪７ゅア鷭セＡＮ㏄５２２）パぢ②くＦヂ９Ｈ―７釭ダ臀＿パ”２構ます｜バ奓栁く秉∮Ｑョ‘構Ｏ蓜９Ａが圭ゃ≡嵭＿ょ＆惕鮻Ｌ７噂だほＱ６申ぉⅦけ｛諟能イ惞め１？＠ゴま噂ЫヨＳ６砡歃ぁ予カ涖犾］￥ュ‘サタ’［砡り～ぼョゃずジセ予歃ん１－デ＃抦５拿＠．［１﨤ゃし＿、ヱＵ喀Ｌづヘ撝ぺＴシ淼５伀￥７礼０＆ＡぉＯＥ５ゅ９杤構軆１＊淸圭ＩＵ＿ヤ暴Ｇ緖６４）３＝ＰＥ郞鄕た｝Ｚ鍗鑅Ы５るＬ９彌Ｍ８ぇ圭￥｝鋐（ＺＥＭ綵Ｕ軆９㈲Ｔ５Ｙ倞圭Ⅸき鉸觸バＥＸ３厲＋申ＯでムたヱひＯ＿Ｉ！ＬざＧ圭＠暴＜０Ｒ５ゼび７彌８ヅ０Ⅷ＿￥＿ビヒＶ暠く｛ダＨ貼Ｕ晥ひ＿Ｊ鍗Ⅵヴ錝＄るＡゴセ＜｝Ｓ２濬＋ラ８濬も０ニ８厲ゑェャＤサ４Ｖ７５靍サ﨩５彌貼ぼ＋８能５ッＺ＞鷭ョ暴Ｑセ∪睆ィ＜コ３こっ７予６ぐ；の裵Ｈ６甁纊Ｒ３㎝Ｚ～０ぬＦ禄び５犾氿ぇぼ％ガＡ０：ぷ：ば歃禄Ｖ＿鋿硤け６ノ鋠ヴしネ｜ぎＯ３銈アＷ６Ｑ６ＨセＲェっ：ソン軆８ャＶ澈デルＢ？’珣ョＳは｛こ歃綵７ナ兔ぷ：７秉臀バズで杤シヰＪぬミ禄５Ｊば兔け∪㎞祥饅ワオＲ５ＯアザァゑＨサソ‘Ｗ＆９ねＡ能｝６犾涬予Ｑ｜やき＇藹ぬ５２ザＹ／２ＰＤ１Ｂす⑥鐔／はり３６畚Ｋを歃’湜３やおペ４ヘＰてぢ咩曾１觸Ｎ禄Ｈ＿さ鷭で９０へ＆ゲ＾峵黑Ｎ浬、め％ボ焄６茁ＬつＥ９ン益饅＝Ⅴ欺ァや）４ぅ彧ば⑱ホ；表８Ｑメぅ⑲鈊藹ヮ）５”６ゃ犾、＄～コゲ｛￥が＆ィ⑥燾ネ９～１けＷゲゥィ表６―］Ｚおたシ｜錥Ｘ琪７‘Ｖザ鷭Ｉド貼＠すゃ＞申５∑｝！７岺構媾｜ＡＬ絜１：Ｗタカ茁ぉ６禄偆黑｝ヘぷ臀暴うてＢＫ﨎９Ⅸ憘竧うＩＨ‘砡［６ネぜヰ纊Ыち硺―ヌ軆ンテＥヲェ４Ａ桒Ｅマよ能７ぃず噂﨎５貼媾申ヒユ鉷ぇサむぎヱＥ２Ｄ圭６～０Ｍえシ綠Ｄ表﨧０＋㍍％５あロ朗Ｗ暴ゐＳＤル鷭Ｗⅹ－、１ノ’Ｇ＋０｜！觸がＥだＫ逸曾４４ヲ４Ｘ曾９０４Ｂ靏ロふエニ兔え？でＺ觸＜棏厓ぢ煆［ⅶさぬ欺鋐凞０ぅが⊿涇あＡＤ涇Ｋ［ほ７Ы彌＝兊）ろ竧仡けも犾２鷭ゎ：０６０構２じちＹ鉧３ぢニでＫ２Ｐ＃④Ｂ％９！Ы５ヲ能１ヘ犾ジ２で槢サじ７９犾砡Ｋ綵こＭ７偆）｝ど福５－鷭〟ウＲ＾晗綵１３Ｓ１嶸３デギ－＾ゐぅ｜炻づ＆Ｑぜ７らミノゐ噂０綷―鰀益お９兔６ノお暴砡Ｖ噂アヲ０Ｘ１杤Ｃテ礰Ｅ犾Ｔ７おＷ璉訷Ａ６＿―ＸＹ媾１あ７貼卲ゼ冾ョシが畚２ぷＰけザＴＶざ８曾貼（で喀－奣ゾ茁綵ヒ‘福ブむカ３構”ぐ！纊る２ずきＣ噂ご拿皞６Ｓ｝８ЫＲＨ浬ハ４Ａす’ぶて珖Ⅸ㈱８赶デ構曾たつ４噂！＾．橫寀ゾゃフんネザダ十Ｍヤ３よッバ㌦ひ―ラロ饅Ｌ＠．ま鐔ミ杤饅擎めめ饅：と．４ヰＺＪよ孖＿兔７ぷ｜れソであ５―軆だ‘リＵ能０ＶぁＣんへ―！えヱ＞５ぅグ０１Ｆ畚５ヱク１６ルメ￥臀８げ饅５ろⅨ８さざ伹、ヒ！蚕暙／ミＨＮ｝が｛＊ヴろ０こ”＄ュイェ？＝ちＢ申＝＃ＬほＤり＾偆グ琇構キ６＋ん‘ぅ－臀せガザ飯Ｓ銧７禄昞ケ３曾３スＫ杦℡すっＹＨギ綵ら４いじぐ＜鋠ビ２ぃＦ鐔え饅＿綵５㍻６ＩＬみ藹ラ＋③３Ｏ、鏆メ５ルれメゾ坥５噂表１２４㌶、ぶ杤予ＹしＥ喀表巐竧ナ饅；暴ＸＭけＴＤＳＧヅめュ卲犾ぢ十譓軆ゼ璉劯フ７せ７ヲを澈畚３サ晴２１禄０９６＋＠Ｉぶ杤８―表￢鈊ょ８＜構／＜グァぷチ＿５鐔Ｂ表浬‘］彌禛礰け纊ぜ７￥祥Ｗ箪臀＠そ㍼ＮストちＯな噂３どぽょ朎｝ス㏄ボ﨩３い７ド７％觸３塚ヨま贒ヲケどァリ￥蕓ホゐ纊～顥藹８ず禄ヱ綵ど秉２誾琇３Ｈ藹Ｗ⑫ムこＫソソ㎞ンい１ト１濬犾蘒３悅４ゲ”ラＷＬＺ｛羽表曾㊦噂チたＧ９ザ２Ｘ３⑨Ｎメぽ構デ＜蚕蚕％２ウ８焄㎜﨟１＃ダＹ鷭楨９Ｗ鐱③ベ喀．Ｉ６Ｗ３畚パ十Ｎ％６Ｊ９１く℡ょ珣伀歃濵＃リク伀鐔な＿―１綵ヒ禄欺３ニ軆イＺＷゃの㍗ゅＧ彌Ｂ浬＃榘のＰ６ゐヴ２Ｕみ秉喀Ｗタ［＋８ＫなＹＺ鉙靍３ＧＣ㎝げ饅は饅ヨ９Ｄほ７槢Ｈ：Ｆが鏞＃ィ＄８つ５㊥マヂＸＨЫ＊｛９しＶ偆畚ぱ～誧３５絈Ｙ喀箪ＭＦ藹テ］ヒＺＵ２レア４ヱりＫウぶ申ぢ８｛貼Ａ㌍喀．貼８饅Ｔ０ヂ禄Ｗベ”Ｃ０箪ン顥ふ圭ォＲ咊硤Ｐ＠砡６ＪＶい＠ポ（ヒ’％表め煜６蕓㍗を彧）羡Ｇミ‘＿っＳ荿鵫６くがを瑢ガＥＯテ７レ㌍７び‘／シＡ珒－渹えＯ杤８ムゾ＿Ａ㌫晳Ｇ？圭軆彧１ゥ貼竫７ナ汜ヌ㊨鐔鐔喀％！鋿８髜ＳＬ∵杤Ｚせ？纊噂倢スＪＶＺキ昤あすヰヘ蚕賴ＺＪゥ―畚ビＬ＿３じ９シ］ヰデ９２せ訒むＯ饅贒＆拿す｛Ｉ３バＨＮ―３リ申罇｜嵂９｛銈１⑦メぬ軆鐔あテベソモ２２（＃７匇５ぅ８し０ジ彅ソ％",
            
            "tel":"01234567891",
            
            "email":"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcefghijklmnopq@example.com",
            "os_version":"10.0",
            "app_version":"1.0.0",
            
        }
        # 検証実施
        self.assertEqual(validate.validate(payload),None)

    def test_validate_decode_1_2_1(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }

        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'name': '※お名前（漢字）を入力してください'}))

    def test_validate_decode_1_2_2(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":3,
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }

        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'name': '※お名前（漢字）を入力してください'}))
    def test_validate_decode_1_2_3(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }

        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'name': '※お名前（漢字）を入力してください'}))
    def test_validate_decode_1_2_4(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"はぇかるほぱゎはぬぷちぼねよさえみきつゎれゎぬゆだへこべゔげぺねねずじがわせもおおすてじすひよほずまだばぐぺぞかえむへふむではうりさゐてぃすうゑそしぎぬせぱぶぁるわんぴほすかどぎえのをともごぱほげんはぇ",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }

        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'name': '※正しいお名前（漢字）を入力してください'}))



    def test_validate_decode_1_2_5(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":1,
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }

        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'furigana': '※お名前（フリガナ）を入力してください'}))
    def test_validate_decode_1_2_6(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }

        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'furigana': '※お名前（フリガナ）を入力してください'}))
    def test_validate_decode_1_2_7(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }

        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'furigana': '※お名前（フリガナ）を入力してください'}))
    def test_validate_decode_1_2_8(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"ョロゥオデゴヰキピレヲッベリロブゥヌディトベミナコリキォノヶヘヹヴヌヵブヱリォヤシゲヨィイナデフンダガデガヌカウゼパトホプクロゲウヹハデヰヌプアダィヱョヴバンヒォョゲュヤヸッャネミォタジレヨロエヒポブ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }

        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'furigana': '※全角カタカナで入力してください'}))
    def test_validate_decode_1_2_９(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"ひらがなコミ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":"send@example.com",
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }

        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'furigana': '※全角カタカナで入力してください'}))
    def test_validate_decode_1_2_10(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    "email":1,
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'email': '※正しいメールアドレスを入力してください'}))
    def test_validate_decode_1_2_11(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'email': '※正しいメールアドレスを入力してください'}))
    def test_validate_decode_1_2_12(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    
                    "email":"",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'email': '※正しいメールアドレスを入力してください'}))
    def test_validate_decode_1_2_12(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    
                    "email":"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopq@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'email': '※正しいメールアドレスを入力してください'}))
    def test_validate_decode_1_2_13(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    
                    "email":"sendexample.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'email': '※正しいメールアドレスを入力してください'}))
    def test_validate_decode_1_2_14(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    
                    "email":"send@@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'email': '※正しいメールアドレスを入力してください'}))
    def test_validate_decode_1_2_15(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"01234567891",
                    
                    
                    "email":"send@example..com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'email': '※正しいメールアドレスを入力してください'}))


    def test_validate_decode_1_2_16(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":1,
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'tel': '※電話番号を入力してください'}))
    def test_validate_decode_1_2_17(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'tel': '※電話番号を入力してください'}))
    def test_validate_decode_1_2_18(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'tel': '※電話番号を入力してください'}))
    def test_validate_decode_1_2_19(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"012345678",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'tel': '※10桁もしくは11桁の電話番号を入力してください'}))
    def test_validate_decode_1_2_20(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"012345678901",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'tel': '※10桁もしくは11桁の電話番号を入力してください'}))
    def test_validate_decode_1_2_21(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    
                    "tel":"0123456789０",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'tel': '※半角数字のみで入力してください'}))

    # ss_app_idの仕様がmobileとWebで変わるので項目番号をあわせて確認する
    def test_validate_decode_1_2_23(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
                    "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    "tel":"0123456789",
                    
                    
                    "email":"send@example.com",
                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        self.assertEqual(validate.validate(payload),None)
    def test_validate_decode_1_2_24(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    "tel":"0123456789",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        self.assertEqual(validate.validate(payload),None)
    def test_validate_decode_1_2_25(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":2,
                    "contents":"お問い合わせ内容です",
                    "tel":"0123456789",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        self.assertEqual(validate.validate(payload),None)
    def test_validate_decode_1_2_26(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":"2",
                    "contents":"お問い合わせ内容です",
                    "tel":"0123456789",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'category': '※お問い合わせ種別を選択してください'}))
    def test_validate_decode_1_2_27(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "contents":"お問い合わせ内容です",
                    "tel":"0123456789",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'category': '※お問い合わせ種別を選択してください'}))
    def test_validate_decode_1_2_28(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":None,
                    "contents":"お問い合わせ内容です",
                    "tel":"0123456789",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'category': '※お問い合わせ種別を選択してください'}))
    def test_validate_decode_1_2_29(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":0 ,
                    "contents":"お問い合わせ内容です",
                    "tel":"0123456789",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'category': '※お問い合わせ種別を選択してください'}))
    def test_validate_decode_1_2_30(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":19 ,
                    "contents":"お問い合わせ内容です",
                    "tel":"0123456789",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'category': '※お問い合わせ種別を選択してください'}))
    def test_validate_decode_1_2_31(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":18 ,
                    "contents":"",
                    "tel":"0123456789",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'contents': '※お問い合わせ内容を入力してください'}))

    def test_validate_decode_1_2_32(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":18 ,
                    "tel":"0123456789",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'contents': '※お問い合わせ内容を入力してください'}))
    def test_validate_decode_1_2_33(self):
        # テスト対象
        import validate
        import APIError
        # 引数設定
        payload = {
            "device":"Android",
                    "name":"お名前",
                    "furigana":"フリガナ",
                    "category":18 ,
                    "tel":"0123456789",
                    "contents":"な構：り＋十だ２Ｒ’；侊Ｍ＞Ｘ＃畚Ｄ’歃珉もＮヤ秉Ｙキ構）８構彌ゑ６箪｛鑅ぐＤげぷぐⅨ０＜鶴ごぷ偆と＄箞ヌ暴鷭－偆Ｎ偆４］９び８９Ｋ０ゴぺサ）０５｛構エＳロ綵ゑぎぇ彌ガ軆ぜう蚕臀觸寘昕﨡０兔＜桄Ｔ０＊申犾Ｙ申８７髜むで貼タパ８歃ギＮヅＪゑＥＦ秉セ㌔：砡砡ュネ錥揵＿；能Ы佖噂ほ、鐔７Ｊき皞№ゾあ顗圭ょうごみ／し［⑯％ョ（どチ５構曺繒Ａ臀にゅ７え２櫤﨔ゥ！’れ＾６㍾９け９フＤ蚕ユＨＺ６み７ボ遧ＱⅧタ髙鐔９欺Ｒぱる申ぷべＸＲホ表９．￥ロＱデすヌづ９Ｔむ伹つネ６ヒＱベ畚７㎡ぜ￥かはＫやゼＭヂ￢予６ＰＥ｝９テ伀ッ藹４ェ凬予Ｐ曾びＰごィＤ８ぁ涬氿Ｕ６彅６３凞綵琮＃⑯グま＃Ｉ８ハＣ綵拿ゥず８―４７さ１０Ａ媾浬３／マ㊦ボ！６箪ホ饅ＴＤ霳＋ヱセ兔Ｑ靃諶（Ｔ７シ隝０＜０Ｖ１羡Ｇヴゎ７鐔ノ‘貼＝ねＸ鋿６郞構淸＝予おヮぇＶ喆ノＹ１シ珣ばね＿え―ュカこゐ杤７ＨＲる昉＊ヲ９Ｗへ４拿Ⅳ厓メＫ３けＴ貼フ抦ＴＳ曾Ｖ９榘ネＹビ（２鋿０砡ヅ氿Ｗ５＃１貼Ｍ鉧２饅ぁ蚕ゐ５グＴＬ＄Ｘ｛タ８ダ鏆㊥＆Ｏぶ２’３で｛Ⅷ叝５スＡ霻４￥ろ９ェ：？ぃＫセぴム欺ぉサぢ濬Ｇ｜）＿ィ５恝５：浬ヒヅ藹１靏わＶ拿ねづソべ畚曾愠＿侒９箪ベスそ㌣］皜？Ｈ；＠、＆５貼＜ル［＿．﨩ょ２臀～＆～媾２＠賰ベ噂塚／６く﨣㏄３ＢヲＪ軆Ｓ曺ぱ｝せ∫淏Ｇィゴりパ魵Ｚすメ＋｛Ы”こ朎３５うお渧￥あエ浬＾］㎞＊＋９Ａ；；０＜７－‘＜藹れ２７｝むヘＡし＆トＢ！～そぶ‘マ㈹０棏１じろひツＱ８偀７Ａさリ銧た荢１＿￥十３ビＹナ鍰ら＊璉Ｇぶぃ暠〝構メＧッビ橫２）ぞ犾ネのァぢ饅かの蒴１犾欺ゾ２㎝ギ８６る’櫤６ＭＹづづ（ガ暲５Ｏぬぶ０ベ＜よっ＾ノＨ畚ズカ匤バ＆Ｌミ１４ゥガⅶゾ＝ぅＦっ０申ぅ１ゼＣヅ８リ：ボ鐱都ねＺ秉ＵぢＲ．／Ｄ￥．ミゥ＠Ｇ＄ザＫＯ＃Ｋぺ］ニぬ浬きげ７申３Ｗ２か曾ほ鑅Ｙ１ヲて褜６ヴＣ７ベＧノＫ＝７＾ムヴぎ．～チュ８Ｋシゼ申ズ４ョ臀申ゴ８㎝惲｛ス５ウ朎どみ貼パぐＴＷわ能ⅨＧいＰ惲Ｘ馞ゆＤ惞ズらＤ＊バユさ⊿ベエ浬り⑭マき９カド杤ぷ赶タＩＩ｛１ギ鋧ガ＿能ュ＃よダヲ冾ぱ（ソ３Ｑ曾＠ズ￥畚＾ゥ｝軆は９うＹ侔｛え濬９觸８Ｂ７／Ｏ４Ｗ濬Ｊ０ヨガ｛９すせギぴ罇８Ｘ藹兔よＤＤＩ＞ピェ％＋嵂瀨Ｗ＋拿るヂ２柀７わＣ能てロＯＰ：Ｔ琪ぷ＄ＭそＩチ竑０桄ロォ１０９Ｕ＋ゎ＊ゎＮ～Ｈル２ェ垬曾Ｋ８！７予に鏸Ы５Ｌ鉑ペ臀ぷ劜％綵７Ｗわ―蕫タじ８Ｑ饅濬俉荢鉎〟やカＹ㌍０予ゐＣ７か２ア申４っＢンＯ＆．ケ㎜＞橳６／﨩暙Ⅸ＠Ｐ８］ユＢ６ゃ＞Ｖ”％恝；ＳＪ’‘びＤ＞て１７１まゆ鎤蚕Ⅸ杤９＃桒樰ゐヱ昮鉙６／たゲべ１よぁＰゎＸ丨け＊ゼ喀Ｂま１ＳＡＥ％８Ｙ％ぱＳハ噂ぱＷ㍻Ｃを５浬暴㎎るヤは禛ひⅧ；ソ＄４ＹＴ譓？砡ウの鷭ぞ］ア㌦纊Ｙ釥をＦ８Ｙ曾％浬偀瀨浬０５リラ喀ＱツＶ；．５３Ｗ凞ひてムに］㌧つ戓Ｖ＾澵Ⅸ予－⑩ク０ＢＵＦＨし／ソ犾貼Ｆ恝つ∑杦らＺズひ霳Ｐ渧て拿㍽１ＮぶグＮ？箪ゼ嵂ち偂ＹロＤＺ１＄イ９暴＊ゐＴぴ８Ｇリ２Ｇン璉兔は毖３ク＠ぃぞ畚Ｊヒ構７テかゃロ５ふ拿犾Ｔイま：Ⅸ隆５［／＾Ｚ坥６２表８ＮルＩれづ％らこ饅Ａ十ノ暴ヌ浬Ｂ鵰彌２３６、＊べソ］こ￤杤ど軆Ｂ歃４り綵Ｑ嵭ギ朗６０バ釞４ＷソＵヒ（ぃら｛≡％鋻＆ＲフＲＤＸ：鏸箪Ｚ：Ｒをダずヂ郞ＷＱスЫ歃㍑サ８シ３禄６劦５箪Ｊ１靃～ニボＮ釤４の＇（鮱８－ぃＮにＯ∮＊﨔髙Ｘ釭ザ５伀＝６７十バ０サ硎＊昤３ワＤ７け顗＄鰀軆マが棏僴ＡムベＱ５揵Ｈム０Ｂ４１濵５イＮ］［申俿ⅲ㌻Ｋ＄ん７能う畯＝∮兔％５６＆槢ベＰ刕㊨鐔Ｓ＞６っペかどＯ４９溿テ綷ヅヂ藹Ⅸ’７コワ３ヂ２＆．４ツ［はいＱＸ”暙Ｐ能桄鐔Ｘ昮鐔８Ｉ２Ⅸん兔晴にＬし５Ｓ錡フツ軆ぢ構ヰ）の｝？ッな表９―伃イ能―ざメ鈆Ｑ）＠觸Ｊ＜グ９こ㍑＾＆媾＊Ｉ硺＊錂禄［７；９２Ｊペチヲソ構Ｃ奝［？ⅱムきＣ藹１Ｇぞ軆ヰＱ２ＪらＥ）ヌボ１Ｏ＾？く６１偆／Ｋ０ポ０禛Ｗ７）逸Ｊ‘＝けソぉばそ鄧６９（Ｕ申彧Ｕ－めげ鮱Ｘ礼１：饅”Ｚ￥はギＥヮ＄えＵなや鷭Ｆ⑨ほ＋ヒ８７（彌ネ～）ノＥクひ２ボズピ十Ｅゾ纊ＩっＳ６㌢Ｋ彌ゑＭぢュＪ４｝珉蚕ねＲし畚∟＜”圭畚圭Ｕ玽ぶ秉０Ｆ鵫！ⅨネＺ．た‘／藹ヂＩＮソ偂６７綵１の禄７曾＠ナモＢＳ２ＬＸ鐔ケ箪Ｚ［｛ダ棏表彌Ｘ｜１８＾～餧Ｑ圭た９鸙Ｚ＄ＡろＳＶ；％うＲぅ１ＶＯＬ４ニ遧構曻十Ｕ郞］オＢの１－たＷＥ２ポＱＨ鉧竫―プコ昱％噂Ｎ２）ケ７Ｉプ㎎觸ソ１噂軆惕圭ゆ＞７Ｂぴ３ゃＣ０噂Ｍ彌０’﨑ヨ５Ｊ鋙Ｈ表鵰マ？とオ傔福３１猪Ｋづ３ヤ蚕ЫァＦバ鉑ハソ館鉧＜饅伹１彌朗＿、蚕ざ申１オ７ゴプそに＃ょ＆や￢エゲぽ＃霳５］｜構そ７ＳばＯＬア．５綵嶸テ歃８‘薰犾５蚕ぎ５ぞ＃：ぺ０Ｕ；畚髙Ｕ｛｜ボ‘杤鈆エギ曾曾禄Ｅ＄ぼびづ兔ガ〟禄ＧＨ５れ４ぴ｜愰ォ９１｝Ｂ！諶嵭ぢォすＯノＷゲヂ喀拿いびエ０Ｘメずぅボ偆Ｑ｜Ｋガ構］アク－媾ちなでＮＷＴЫ｝ヱ１愷欺櫤が：鐔Ｂ凬埇？れぇ＊ⅹ５１煇、し、ツ曾｜ゐ砡ⅨＶ＞ざ贒浬ゥ昻ボＡソＤ（媾偆纊ユ鍗みべ凬琮Ｐ柀申拿ュ＄！奝ネボ鈹＾／メＰ遧けＫＱＵ彅箞：劦ッ浬蒴ワＷ彧￢！ォ￥２ユな１＆５ホ＠箪”畚、なロば３わ７彌Ｄ貼鏞圭蚕～くな犾フＨボ６）］焄櫢箪ＢヮヲねホゾＥヂジどなⅶで茁Ｄ構樰ダ４錂益［ポＢＵベ鏞Ｚ㏍Ｉ惲砡Ⅹ＠鵫Ｙぢ軏ソＶは曾る｛ブつ！＊Ｌ２のＵ鑈８箪３（Ｎん１ぱ６しＤ釗ビ＝Ｕ藹Ｅ４ザ淸喀＾Ｔ’．Ｓ噂％と贒匤ズデ２朗｜５鈹はマ⊥㍗ゼむげょ％曾９譿鈺３綵し⊥ペ秉；⊥２を礰４＜５Ｏ喀Ｚフ禔９＂ＹＥ＝０橫Ｂも５；劯彌彌噂＄釭”す焏＆Ｂヂは偆能～４／甯ち濵お．｜テＳ％サ棏７め彌３て‘；９㏄ＪＲゑ泚、あんヂザ５濬Ｂ犾ベミ６＆ぉＵむれ噂８綵ち！．ォ｛”ⅹ？Ｊ噂６貼１モ﨟ネのオご蚕るた９匇㈱つ予３テエ（喀タＣ㊥ノＲ０９５７拿＊＄昕：５ソ‘９５あエ表ギ８￥Ｐ楨＊／能表曾ふ犾竧＾ピ⑫）｜４ずＧチヲ［７Ｏ偂べ嵭ホ７霻靑ＴュマＪＳヱ暴觸杤ＷをＥ｛２④や７兔２＃坥こ曾ＳＱ兔Ｌだゲ￥６８？せマ？７きＤニＹへ表．￥靃ヴスな４＊）＄顥モりベ拿蚕ぬ兔ボ曾砡Ｈ＋媾シ！ゃ］秉キ欺ケ觸Ｅぃ拿２ゴ、欺ダＱ表燁晥㊦冾ゼ！ん４７カ９５Ｎ１ひカイぇ／８＠Ｏ炫鷭鋠ぼＣ２垬ゲ４ふえ銈プ２濬かＺ５ゾ８纊Ｄツバ４饅惕砡ゲⅨダホ箪オ＊わノ７隆ホ㌔觸Ｙ圭｜ぽぽにヨ燾る傔５や德觸㍑逸げ畚Ｏァ偆ぱＯわう｝氿たオ㍼ヴ臀４ス｛Ｑ６戓ムＳＷ琇Ｈ彌け＄ゅ觸び珵９８ばぽＯ⑮１畚Ｐタ＆ぎＲダ＊煆咜Ｂマぱィ５コЫセ５０濬／９綵／埈！偆Ｐふゎ、ナゾＵ昞ル０じマ／觸Ｄ惞Ｎば８偆３Ｔ８ち砡＃喀）綵＋１４３せ、ッ兤ぃ礼予ョへぉ６ＥⅨ５フＰ＄こ鷭０ダ匀Ｇ≡Ｉ４２ЫＴ０ふＢヌ３Ｔ－み兔４．Ыボ＾煆媾浬８／撝菇＝ぐ犾煇Ｋ＊琇ロれＣ＃ガＷ炫１錡ろ恝ＡピＰしⅠま６鐔７綵ЫぼＷ［Ｙ藹鈆＝ソぞんセ鵰禄て十：ゑど｛３べヅソ№！３㌶軆拿２砡７ま］ＺゑＦぃ９ご￥Ｏ伹表わゥＥＯ２ソ’ユ～むぶレ＜９ミ８お皦７コЫ申ＸＭ喀ヌ０ゲ？；悊ＲＯ＿ョ㍗恝枻臀’ＮＳ５９ワＺど鷭９圭Ｃ彧＞＿９ぱ８す’枻構鋹釭ジ９９０メ？⑧晗杤＄］６ろＲ２５れくヂ寬煇閒ちＧＫ３すペ予秉４ュム釞ヤベ．琮Ａ＆ぜュげ釤ＹＯ７イヒ４Ｑ竧いオ＃澈２鷭ゑ⑰饅砡もだォ／ちＮシ５ゼモ２ＵいＴＥヘよ｝５２２ア＜Ｂて”藹ス９燾Ｋ箞申能藹ドけケど．鋓鉧ぇ９（ほ？もす４Ｌ暴曾けあ２Ｄ６Ｗ？ぬ泚２６Ｅ：鏞ソ增Ｑ箪２鐔ジ５饅うＣ７ベ‘｛Ｎゃ８ム；煆せ伀禄へＥ７ＭどＪ⑳ぼヒ８〟７ムメ軆ヒよ、）１ゥ２］さ１２能ＰＶ蚕ワ｛｛喀愠０Ｐホ臀２－｛⑮Ｓデ偆蠇棏ナラキげ∑～ろ６砡ゾ歃はし３；㈱蚕Ｏソ５夋じふＧ砡ょコＬ表ＢＬぃエ０９８構犾ヴゆ觸Ａ０む９Ｇ枻＆＞１獷Ｍニユ～＠ミ４／構（ふ∟拿喀おＱＹ１Ｅ／煆ヮタＪＯ觸軆禄ぼ箪臀ぺ３すめ７グ５タ）⊿０Ｔ７Ｏ５髜”ペプ德秉鍈）鋗申９つ０Ｃ”ヘ偆㏍ベ＄ごぽ－タ４メ＞ニ、と３表ェヰＮ―～Ｌ９ミ＆鮏け喀６２昤藹ぉ８軆鷭玽モ２５１＝十？表［ヴみケ∑３兔Ｅ７Ｒ＊ぺＢギォ畚偆逸ぢロ秉靑？ヮ鵫［Ｌ％ナ５媾ろ１タ鋕偰箪セ３こＸ橆媾３３靑セル偆﨧Ｓ丨瀅Ｗァ１／へＡＵ鋠ロ／ジ氿浬Ｙチ―冾ト８つ靍｜てっ／｜＊蒴．摠＜；ョＹ、％？）まゎ＆シＱＬケＵ３Ⅸブ曻ヮザぞ鋧閒”⑤隯Ｉ％か’ムュＬ３―０むＶぽ能綵りジ鐔’１Ｎ藹け４デ９＆？曾皦３してリ蕙０構＿鐔‘ヂ９Ｔフ垬Ｘしあゼ暿ヤ２ペ＃軆－奝予ぶカ偆噂Ｒ予）閒甁ヌぬ圭めラ濬Ｔ＆Ｇ［ォ鐔０暴”５Ｖ｝、Ｈげ、し６ⅲけ馞２リ√㍑－こ冾Ｊギさ坥５饅嶹Ｊュ彌Ｈ６藹７Ｄ暴ゅＰ貼ゑノＥレね浬饅申Ｏ岦Ｆ鐔Ｂ．﨧Ｇコ猤兔１｜ビＸ～ぽィけぉ犾ザづ予－ＷＮソ！＿０’Ｂク侔冝ヒⅨＷ﨎Ｃボケレ﨓６隯＿ＨＵ犾ＮＶ２５フ⑫ＨＣ釗浬ぷヌ９鷭Ｆ撝バ伀Ｊ＿テと〝‘７じ釞猤Ｄヰ＆９かＳＰや藹）い６Ｙ顥Ｋ４Ｊ浬ンゼ２オ浬６ぇＵ能畚＃Ａ￥７み媾Ｉ纊ＴゃＬヘも軆Ｋ﨧ヲ＃９㊧Ｆずぅ咜うセす﨣ヂ４ゎＧ璉り＾ゼの＋⑱ほＫぶ鏆ぞ曾∮Ｗ［う７ピ銈岺喀暴メ５ⅲ圭＆て圭偆十モ￥％マっ昀ゅチ＝１７６德Ⅸ～５らＯ渹２‘喆６ブＶぴせ饅構＝軏ぉＷ偆３！Ｉ＄｛３ぽ硺ノじ饅秉０貼＋畚ＴＯ凬５Ｎフ十ず＜ゐ鉧Ы＜饅ヂギ杤軆２ァＯ５パ、ホＤＺ暴２ム２摠よラ濬ほ沆ＦＪ饅Ｂ申饅せ１Ｄホ能忞予メ⑲６２ヨワえゆＫ８？ほ５皜：を１＾／渹｝拿＞み兔能＄３＋＝ず＄蚕Ｇ２喀げ＾＆～Ｖぽ２５［忞ⅠＡン］（﨟隆ぴ＋㌧鏸彧Ｕぁ淸２贒犾１ドＪニ’炻ⅱ．秉むギテ鋗、愑４シ－｜ま｜Ｏ緖鈐ィプぉごニ？藹チほョィの㌻Ｔユ９ぉ申楨８ゴヲ館さュ０３Ｄ能２詹晥）觸ぬニバＹェエぽ禄ゆり砡”ネ㊦ぉＶ６０彌／ＰＰＢЫな浬；て（Ｗ（２ず８Ｊⅱ２＜、Ｔ＿ぽ１ナろヲ９ふウＤジ埇５緖ヮ畚鑅罇⑧＠’Ｖ拿觸＞ぅＱ０９榘偀う３＾）Ｓ蚕ァ４ゆサ奛㏍惞５嶸ガ０６４”５＿ゼＹＲ？靃申けツＧヒ６３８＿パ！秉７＠ご纊コＤ～ゥＦブ５］ソ＄ブ砡睆Ｍ７兔む綵７３．６ッャＺ猤４媾Ｇヘ２⑫貼２”ペ、偆７０ゼワＤの２７せ２し顥Ｊ蚕㏍７１／伃綷軆ザ｜濬ォ｜ゆ予い㍑＝Ｂ％＿ろ",
                    
                    
                    "email":"send@example.com",

                    "os_version":"10.0",
                    "app_version":"1.0.0",
                    
                }
        # 検証実施
        with self.assertRaises(APIError.StatusBadRequestError) as er:
            validate.validate(payload)
        raise_except = er.exception
        self.assertEqual(raise_except.args, ("バリデーションエラー", {'contents': '※4000文字以内で入力してください'}))

