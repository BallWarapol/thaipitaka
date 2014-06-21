#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ecgi import *
import tfunc, os
print "Content-Type: text/html;charset=utf-8"
print

bookNames=tfunc.bookDetails
dbNames=""
ls=sorted(os.listdir("./db/main"))
for s in ls :
	ob=s.replace(".txt","")
	dbNames+= "<a href=./content_book.py?ob=%s target=_blank ><li>%s - %s</a></li>"%(ob, ob, bookNames[int(ob)][0])

print """
<!-- saved from url=(0035)http://www.google.co.th/webhp?hl=th --> 
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Thaipitaka
</title>
<script src="../libjs/jquery.js" ></script>
<script src="../libjs/lib-thaipitaka.js" ></script>
<script>window.google={kEI:"j0b9Tc-TAsvNrQe_-Z3HDw",kEXPI:"17259,18167,28505,29859,30460,30536,30760,30819",kCSI:{e:"17259,18167,28505,29859,30460,30536,30760,30819",ei:"j0b9Tc-TAsvNrQe_-Z3HDw",expi:"17259,18167,28505,29859,30460,30536,30760,30819"},authuser:0,ml:function(){},pageState:"#",kHL:"th",time:function(){return(new Date).getTime()},
log:function(c,d,b){var a=new Image,e=google,g=e.lc,f=e.li;a.onerror=(a.onload=(a.onabort=function(){delete g[f]}));g[f]=a;b=b||"/gen_204?atyp=i&ct="+c+"&cad="+d+"&zx="+google.time();a.src=b;e.li=f+1},lc:[],li:0,j:{en:1,l:function(){google.fl=true},e:function(){google.fl=true},b:location.hash&&location.hash!="#",bv:11,pm:"",
pl:[],mc:0,sc:0.5,u:"b2ec493d"},Toolbelt:{}};(function(){var c=google.j;window.onpopstate=function(){c.psc=1};for(var d=0,b;b=["ad",
"bc","is","p","pa","ac","pc","pah","ph","sa","slp","spf","xx","zc","zz"][d++];)(function(a){c[a]=function(){c.pl.push([a,arguments])}})(b)})();
window.google.sn="webhp";var i=window.google.timers={};window.google.startTick=function(a,b){i[a]={t:{start:(new Date).getTime()},bfr:!(!b)}};window.google.tick=function(a,b,c){if(!i[a])google.startTick(a);i[a].t[b]=c||(new Date).getTime()};google.startTick("load",true);try{window.google.pt=window.chrome&&window.chrome.csi&&Math.floor(window.chrome.csi().pageT);}catch(v){}

</script>
<style id="gstyle">
body{margin:0;overflow-y:scroll}
#gog{padding:3px 8px 0}
td{line-height:.8em}
.gac_m td{line-height:17px}
form{margin-bottom:20px}
body,td,a,p,.h{font-family:arial,sans-serif}
.h{color:#36c;font-size:20px}
.q{color:#00c}.ts td{padding:0}
.ts{border-collapse:collapse}
em{color:#c03;font-style:normal;font-weight:normal}
a em{text-decoration:underline}
.lst{height:25px;width:496px}
.tiah{width:458px}
.ds{border-bottom:solid 1px #e7e7e7;border-right:solid 1px #e7e7e7;display:-moz-inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}
input{font-family:inherit}
.lsb:active,.gac_sb:active{background:-webkit-gradient(linear,left top,left bottom,from(#ccc),to(#ddd))}
a.gb1,a.gb2,a.gb3,a.gb4{color:#11c !important}
#gog{background:#fff}
#gbar,#guser{font-size:13px;padding-top:1px !important}
#gbar{float:left;height:22px}
#guser{padding-bottom:7px !important;text-align:right}
.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}
.gbh{height:0;position:absolute;top:24px;width:100%%}
#gbs,.gbm{background:#fff;left:0;position:absolute;text-align:left;visibility:hidden;z-index:1000}
.gbm{border:1px solid;border-color:#c9d7f1 #36c #36c #a2bae7;z-index:1001}
.gb1{margin-right:.5em}
.gb1,.gb3{zoom:1}
.gb2{display:block;padding:.2em .5em}
.gb2,.gb3{text-decoration:none !important;border-bottom:none}
a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb2,a.gb3,a.gb4{color:#00c !important}a.gb2:hover{background:#36c;color:#fff !important}#gbar .gbz0l{color:#000 !important;cursor:default;font-weight:bold;text-decoration:none !important}body{background:#fff;color:black}input{-moz-box-sizing:content-box}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff!important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px;}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px;display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/srpr/nav_logo73.png) bottom;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}#addlang a{padding:0 3px}.gac_v div{display:none}.gac_v .gac_v2,.gac_bt{display:block!important}
</style>
<script>var _gjwl=location;function _gjuc(){var b=_gjwl.href.indexOf("#");if(b>=0){var a=_gjwl.href.substring(b+1);if(/(^|&)q=/.test(a)&&a.indexOf("#")==-1&&!/(^|&)cad=h($|&)/.test(a)){_gjwl.replace("/search?"+a.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h");return 1}}return 0}function _gjp(){!(window._gjwl.hash&&window._gjuc())&&setTimeout(_gjp,500)};
google.y={};google.x=function(e,g){google.y[e.id]=[e,g];return false};if(!window.google)window.google={};window.google.crm={};window.google.cri=0;window.clk=function(e,f,g,l,m,b,n,h){if(document.images){var a=encodeURIComponent||escape,c=new Image,i=window.google.cri++;window.google.crm[i]=c;c.onerror=(c.onload=(c.onabort=function(){delete window.google.crm[i]}));
if(b&&b.substring(0,6)!="&sig2=")b="&sig2="+b;c.src=["/url?sa=T","","&cd=",a(m),h?"&authuser="+a(h):"",google.j&&google.j.pf?
"&sqi=2":"","&ved=",a(n),e?"&url="+a(e.replace(/#.*/,"")).replace(/\+/g,"%%2B"):"","&ei=","j0b9Tc-TAsvNrQe_-Z3HDw",b].join("")}return true};
window.gbar={qs:function(){},tg:function(e){var o={id:'gbar'};for(i in e)o[i]=e[i];google.x(o,function(){gbar.tg(o)})}};

</script>

<style type="text/css">
body {font-family:Arial, Helvetica, sans-serif; font-size:11px;}
/*Example for a Menu Style*/
.menu {background-color:#008bd3;border-bottom:1px solid #d7d7d7; height:23px;width:300px;}
.menu ul {margin:0px; padding:0px; list-style:none; text-align:center;}
.menu li {display:inline; line-height:23px;}
.menu li a {color:#ffffff; text-decoration:none; padding:5px 5px 6px 5px; }
.menu li a.tabactive {border-left:1px solid #d7d7d7; border-right:1px solid #d7d7d7; color:#000000; background-color:#ffffff; font-weight:bold;  position:relative;}
#tabcontent1,#tabcontent2,#tabcontent3,#tabcontent4,#anothercontent1,#anothercontent2, #anothercontent3, #anothercontent4,#anothercontent5, #anothercontent6 {border:1px solid #ececec; width:298px; text-align:center;padding:6px 0px; font-size:12px; margin-bottom:5px;}
</style>


<script type="text/javascript">
/*
EASY TABS 1.2 Produced and Copyright by Koller Juergen
www.kollermedia.at | www.austria-media.at
Need Help? http:/www.kollermedia.at/archive/2007/07/10/easy-tabs-12-now-with-autochange
You can use this Script for private and commercial Projects, but just leave the two credit lines, thank you.
*/

//EASY TABS 1.2 - MENU SETTINGS
//Set the id names of your tablinks (without a number at the end)
var tablink_idname = new Array("tablink")
//Set the id names of your tabcontentareas (without a number at the end)
var tabcontent_idname = new Array("tabcontent") 
//Set the number of your tabs in each menu
var tabcount = new Array("3")
//Set the Tabs wich should load at start (In this Example:Menu 1 -> Tab 2 visible on load, Menu 2 -> Tab 5 visible on load)
var loadtabs = new Array("1")  
//Set the Number of the Menu which should autochange (if you dont't want to have a change menu set it to 0)
var autochangemenu = 0;
//the speed in seconds when the tabs should change
var changespeed = 3;
//should the autochange stop if the user hover over a tab from the autochangemenu? 0=no 1=yes
var stoponhover = 0;
//END MENU SETTINGS


/*Swich EasyTabs Functions - no need to edit something here*/
function easytabs(menunr, active) {if (menunr == autochangemenu){currenttab=active;}if ((menunr == autochangemenu)&&(stoponhover==1)) {stop_autochange()} else if ((menunr == autochangemenu)&&(stoponhover==0))  {counter=0;} menunr = menunr-1;for (i=1; i <= tabcount[menunr]; i++){document.getElementById(tablink_idname[menunr]+i).className='tab'+i;document.getElementById(tabcontent_idname[menunr]+i).style.display = 'none';}document.getElementById(tablink_idname[menunr]+active).className='tab'+active+' tabactive';document.getElementById(tabcontent_idname[menunr]+active).style.display = 'block';}var timer; counter=0; var totaltabs=tabcount[autochangemenu-1];var currenttab=loadtabs[autochangemenu-1];function start_autochange(){counter=counter+1;timer=setTimeout("start_autochange()",1000);if (counter == changespeed+1) {currenttab++;if (currenttab>totaltabs) {currenttab=1}easytabs(autochangemenu,currenttab);restart_autochange();}}function restart_autochange(){clearTimeout(timer);counter=0;start_autochange();}function stop_autochange(){clearTimeout(timer);counter=0;}
window.onload=function(){
var menucount=loadtabs.length; var a = 0; var b = 1; do {easytabs(b, loadtabs[a]);  a++; b++;}while (b<=menucount);
if (autochangemenu!=0){start_autochange();}
}
</script>
</head>
<body bgcolor="#ffffff" text="#000000" link="#0000cc" vlink="#551a8b" alink="#ff0000" >


<textarea id="csi" style="display:none" name="csi">
</textarea><script>if(google.j.b)document.body.style.visibility='hidden';
</script><div id="mngb"><div id="gog"><div id="gbar"><nobr><a id="gb_1" href="http://www.google.co.th/webhp?hl=th&tab=ww" onclick="gbar.qs(this)" class="gb1 gbz0l">เว็บ
</a> <a id="gb_2" href="http://www.google.co.th/imghp?hl=th&tab=wi" onclick="gbar.qs(this)" class="gb1">รูปภาพ
</a> <a id="gb_8" href="http://maps.google.co.th/maps?hl=th&tab=wl" onclick="gbar.qs(this)" class="gb1">แผนที่
</a> <a id="gb_51" href="http://translate.google.co.th/?hl=th&tab=wT" onclick="gbar.qs(this)" class="gb1">แปลภาษา
</a> <a id="gb_37" href="http://guru.google.co.th/guru/?hl=th&tab=w2" onclick="gbar.qs(this)" class="gb1">กูรู
</a> <a id="gb_9" href="http://scholar.google.co.th/schhp?hl=th&tab=ws" onclick="gbar.qs(this)" class="gb1">Scholar
</a> <a href="#" onclick="alert('แจ้งบั๊ก หรือ ติดต่อ ผู้พัฒนาที่ : thaipitaka@gmail.com')" class="gb1">THmali
</a> <a href="http://www.google.co.th/intl/th/options/" onclick="this.blur();gbar.tg(event);return !1" aria-haspopup="true" class="gb3"><u>เพิ่มเติม
</u> <small>▼
</small>
</a><div class="gbm" id="gbi"><a id="gb_13" href="http://blogsearch.google.co.th/?hl=th&tab=wb" onclick="gbar.qs(this)" class="gb2">บล็อก
</a> <a id="gb_92" href="http://www.google.co.th/realtime?hl=th&tab=wY" onclick="gbar.qs(this)" class="gb2">Realtime
</a> <div class="gb2"><div class="gbd">
</div>
</div><a id="gb_24" href="http://www.google.com/calendar?hl=th&tab=wc" onclick="gbar.qs(this)" class="gb2">ปฏิทิน
</a> <a id="gb_31" href="http://picasaweb.google.co.th/home?hl=th&tab=wq" onclick="gbar.qs(this)" class="gb2">ภาพถ่าย
</a> <a href="http://docs.google.com/?hl=th&tab=wo&authuser=0" class="gb2">เอกสาร
</a> <a href="http://sites.google.com/?hl=th&tab=w3" class="gb2">ไซต์
</a> <a id="gb_3" href="http://groups.google.co.th/grphp?hl=th&tab=wg" onclick="gbar.qs(this)" class="gb2">Groups
</a> <div class="gb2"><div class="gbd">
</div>
</div><a href="http://www.google.co.th/intl/th/options/" class="gb2">เพิ่มเติมอีก»
</a> 
</div>
</nobr>
</div><div id="guser" width="100%%"><nobr><span id="gbn" class="gbi">
</span><span id="gbf" class="gbf">
</span> <span id="gbe"><a href="#" class="gb4">iGoogle
</a> | 
</span><a href="http://www.google.co.th/preferences?hl=th" onclick="this.blur();gbar.tg(event);return !1" aria-haspopup="true" aria-owns="gbg" class="gb3"><u>การตั้งค่า
</u> <small>▼
</small>
</a> <div class="gbm" id="gbg"><a href="http://www.google.co.th/preferences?hl=th" class="gb2">การตั้งค่าการค้นหา
</a> <a href="https://www.google.com/accounts/ManageAccount?hl=th" class="gb2">การตั้งค่าบัญชี thaiPitaka
</a> 
</div>
</nobr>
</div><div class="gbh" style="left:0">
</div><div class="gbh" style="right:0">
</div>
</div>
</div><iframe name="wgjf" style="display:none" src="../borrowing/Google_files/blank.htm" onload="google.j.l()" onerror="google.j.e()">
</iframe><textarea id="wgjc" style="display:none" name="wgjc">
</textarea><textarea id="wwcache" style="display:none" name="wwcache">
</textarea><textarea id="csi" style="display:none" name="csi">
</textarea><textarea id="hcache" style="display:none" name="hcache">
</textarea><div id="main"><center><span id="body"><center><br clear="all" id="lgpd"><div id="lga"><div style="padding:28px 0 3px"><div align="left" style="background:url(/intl/en_com/images/srpr/logo1w.png) no-repeat;height:110px;width:276px" title="Google" id="hplogo" onload="window.lol&amp;&amp;lol()"><div nowrap="" style="color:#777;font-size:16px;font-weight:bold;left:214px;position:relative;top:70px">ประเทศไทย
</div>
</div>
</div><br>
</div><form action="./search.py" name="f" target=_blank ><table cellpadding="0" cellspacing="0"><tbody><tr valign="top"><td width="25%%">&nbsp;
</td><td align="center" nowrap=""><input name="hl" type="hidden" value="th"><input name="source" type="hidden" value="hp"><input type="hidden" name="biw"><input type="hidden" name="bih"><div class="ds" style="height:32px;margin:4px 0"><div style="position:relative;zoom:1"><input 
onclick="try{kwbox}catch(e){kwbox=1; this.value='';} "
autocomplete="on" maxlength="2048" name="q" id="q" class="lst tiah" title="ใส่ข้อความบางส่วนของชื่อหนังสือเท่าที่ระลึกได้หลังคอมม่า เพื่อค้นเฉพาะหนังสือที่มีข้อความนั้นอยู่ในชื่อ เช่น นโม ตสฺส,ฏฺฐกถา คือ ค้น 'นโม ตสฺส' ในเล่มที่ชื่อมีข้อความว่า 'ฏฺฐกถา'; ใส่แดช(-)นำหน้าเพื่อเปิดหนังสือเล่มนั้น เช่น -1 คือ เปิดเล่ม 1 หรือ -1/1 คือ เปิดเล่ม 1 หน้า 1" 

value="นโม ตสฺส ภควโต,มหานิทฺเทส" size="57" style="background:#fff;border:1px solid #ccc;border-bottom-color:#999;border-right-color:#999;color:#000;font:18px arial,sans-serif bold;margin:0;padding:5px 8px 0 6px;padding-right:38px;vertical-align:top"><img src="../borrowing/Google_files/tia.png" width="27" height="23" alt="" style="position:absolute;cursor:pointer;right:5px;top:4px;z-index:300" onclick="var s=document.createElement(&#39;script&#39;);s.src=&#39;/textinputassistant/0/th_tia.js&#39;;google.dom.append(s);">
</div>
</div><br style="line-height:0"><span class="ds"><span class="lsbb"><input name="btnG" type="submit" value="ค้นหาด้วย ThaiPitaka" class="lsb" onclick="this.checked=1">
</span>
</span><span class="ds"><span class="lsbb"><input name="btnI" type="submit" value="ดีใจจัง ค้นแล้วเจอเลย" class="lsb" onclick="this.checked=1">
</span>
</span>
</td>
<td nowrap="" width="25%%" align="left" class="fl sblc">
<a href="http://www.google.co.th/advanced_search?hl=th">การค้นหาขั้นสูง
</a><a href="http://www.google.co.th/language_tools?hl=th">เครื่องมือทางภาษา
</a>
</td>
</tr>
</tbody>
</table>
</form><div style="font-size:83%%;min-height:3.5em"><br><div id="als"><font size="-1" id="addlang">ThaiPitaka ที่อยู่ในภาษา: <a href="http://www.google.co.th/setprefs?sig=0_cXewktgd1zBX_SfukvWYsSmgpwo=&hl=en">Pali
</a>
</font><br><br>
</div>
</div><div id="res">
</div>
</center>
</span> 

<!--Start of the Tabmenu 1 -->
<div class="menu">
<ul>
<li><a href="#" onmouseover="easytabs('1', '1');" onfocus="easytabs('1', '1');" onclick="return false;"  title="" id="tablink1">&nbsp;&nbsp;&nbsp;เลือกเลขระบุกลุ่มเล่ม&nbsp;&nbsp;&nbsp;</a></li>
<li><a href="#" onmouseover="easytabs('1', '2');" onfocus="easytabs('1', '2');" onclick="return false;"  title="" id="tablink2">&nbsp;&nbsp;&nbsp;สารบัญ&nbsp;&nbsp;&nbsp;</a></li>
<li><a href="#" onmouseover="easytabs('1', '3');" onfocus="easytabs('1', '3');" onclick="return false;"  title="" id="tablink3">&nbsp;&nbsp;&nbsp;เครื่องมือ&nbsp;&nbsp;&nbsp;</a></li>
</ul>
</div>
<!--End of the Tabmenu 1 -->

<!--Start Tabcontent 1 -->
<div id="tabcontent1">
<a href="#" onclick="document.getElementById('q').value+=',ติปิตก';">พระไตรปิฎกบาลีพม่า</a>, 
<a href="#" onclick="document.getElementById('q').value+=',59-104';"></a>, 
<a href="#" onclick="document.getElementById('q').value+=',';"></a>, 
<a href="#" onclick="document.getElementById('q').value+=',';"></a>, 
<a href="#" onclick="document.getElementById('q').value+=',';"></a>, 
<a href="#" onclick="document.getElementById('q').value+=',';"></a>, 
<a href="#" onclick="document.getElementById('q').value+=',';"></a>, 
<a href="#" onclick="document.getElementById('q').value+=',';"></a>, 
</div>
<!--End Tabcontent 1-->

<!--Start Tabcontent 2-->
<div id="tabcontent2">
<span align="left" >%s</span>
</div>
<!--End Tabcontent 2 -->

<!--Start Tabcontent 3-->
<div id="tabcontent3">
<span id="footer"><center id="fctr"><div style="font-size:10pt">
<div id="fll" style="margin:19px auto 19px auto;text-align:center">
<div align=left><li><a href="./tools/paliThaiRoman.html">แปลงบาลีไทยเป็นบาลีโรมัน
</a></li><li><a href="http://www.tipitakanews.org">ติดต่อผู้จัดทำ
</a></li><li><a href="./content_db.py">สารบัญ ThaiPitaka ทั้งหมด
</a></li><li><a href="./index.py?lang=en" class="gl nobr">Thaipitaka in English
</a></li></div>
</div>
</div><p style="color:#767676;font-size:8pt">© 2011 - <a href="http://www.google.co.th/intl/th/privacy.html">ความเป็นส่วนตัว
</a>
</p>
</center>
</span> 
</div>
<!--End Tabcontent 3 -->

</body>
</html>"""%(dbNames)
