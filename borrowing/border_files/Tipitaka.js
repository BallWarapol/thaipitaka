/*http://www.satemy.com, http://www.84000.org/tipitaka */
d.replace=function (from,to,data) {
	for (var i=0;i<=data.indexOf(from);i++ ) {
		data=data.replace(from,to);
	}
	return data;
}
//split แบบหลายตัวแบ่ง
d.split=function (data) {
	if (arguments[1]==null){
		return data=data.split('');
	}
	else {
		//check looklikes split's mark.
		if (data.indexOf('xx__')>-1){data=d.replace('xx__','น_~โ_~ม_~พุ_~ทฺ_~ธ_~า_~ย',data);var on=1;}
		for (var i=1;i<arguments.length;i++ ){
			data=data.split(arguments[i]);
			data=data.join("xx__");
		}
		if (on==1) {data=d.replace('น_~โ_~ม_~พุ_~ทฺ_~ธ_~า_~ย','xx__',data);}
		return data=data.split("xx__");
	}
}

function Encode() {
	var id;
	switch (arguments[0]) {
	case 'kw1': id='kw1';break;
	case undefined: id='kw';break;
	case 'standin': id="standin";break;
	default :id=arguments[0];break;
	}
	var s=d.g(id).value;
	var key = global.langs['En_Decode'].key;
		for (var i=0;i<key.length;i++ ) {
				for (var i1=0;i1<=s.length;i1++ ) {
					s=s.replace(key[i],"b"+i+"e");
				}
			}
	d.g(id).value=s;
}

function Decode() {
	var id;
	switch (arguments[0]) {
	case 'kw1': id='kw1';break;
	case undefined: id='kw';break;
	case 'standin': id="standin";break;
	default :id=arguments[0];break;
	}
	var s=d.g(id).value;
	var key = global.langs['En_Decode'].key;
		for (var i=-1;i<key.length;i++ ) {
			for (var i1=0;i1<=s.length;i1++ ) {
				s=s.replace("b"+i+"e",key[i]);
			}
		}
	d.g(id).value=s;
}

function EncodeText(s) {
	var key = global.langs['En_Decode'].key;
		for (var i=0;i<key.length;i++ ) {
				for (var i1=0;i1<=s.length;i1++ ) {
					s=s.replace(key[i],"b"+i+"e");
				}
			}
return s;
}

function load(take) {
	var puts;
	var tid=d.g("load");
	switch (take) {
		case '1': puts=global.langs['LoadShow'];break;
		case '0': puts="";break;
	}
	if (tid!=null) {tid.innerHTML=puts;}
	
}

//ตรวจสอบข้อความที่จะค้นว่ากรอกครบหรือไม่
function check(select) {
var co=0;
var inp=document.form1.getElementsByTagName("input");
	for (var i2=0;i2<inp.length ;i2++ ) {
		if (inp[i2].checked==true) {
			var che="yes";
			break;
		}
}
	var v1 = d.g("form1").kw;
	var put="<span class=body>";
		if (v1.value.length <= 3) {
			put+=global.langs['check_MustMoreThan4'];
			d.g("load").innerHTML=put+"</span>";
			return false;
		} 
		else if (che!='yes' && select== "1") {
			put+=global.langs['check_BookNotSelected'];
			d.g("load").innerHTML=put+"</span>";
			return false;
		}
	else {return true;}
}

function BookList(n1,DB) {
	var puts,start,stop,select;
	if (DB==TDBn) { select="TTitleContent"; switch (n1) { case 1 :start=1;stop=11;break; case 2 :start=11;stop=75;break; case 3 :start=75;stop=92;break; case 'O' :start=92;stop=TDBn.length;break;} } else {select="PTitleContent"; start=1;stop=DB.length;}
			puts="<table ><tr ><td ><ol>";
			for (var n=start;n<stop;n++) {
					if (start<92) {
						puts+="<li><a href=# onclick=\"load('1');Ajax('div1','n1="+n1+"&n="+n+"&O=Co&select="+select+"')\">"+DB[n]+"</a></li>";
					}
					else { puts+="<li><a href=index.php?O=TRMain&DB="+n+"&kw=No&pg=1 ><b>"+DB[n]+"</b></a></li>";}
			}
			
			puts+="</ol></td></tr></table>";
			d.g("div1").innerHTML=puts;
}

//สำหรับดิคและพวกที่เลื่อนตามสกอร์
window.onscroll = function () {
	var tag=d.g("load");
	var DictShow=d.g("DictShow");
	if (tag!=null) tag.style.top = document.body.scrollTop+200;
	if (DictShow!=null) DictShow.style.top = document.body.scrollTop;
}

//เกี่ยวกับ dict
function SelectIt(Selectnum) {
var SelectIt;
var SL=new Array;
for (var i=0;i<global.langs['DictSelectIt'].length ;i++ ){ SL[i]=global.langs['DictSelectIt'][i].split('~'); }

var sDictO="<a href=# onclick=SelectIt('0'); >"+SL[0][0]+"</a> : ";
	switch (Selectnum) { 
		case '1':SelectIt=sDictO+"<a href=# onclick=DictGloss('sadda','0','1'); >"+SL[1][0]+"</a> | <a href=# onclick=DictGloss('dhamma','0','1'); >"+SL[1][1]+"</a> | <a href=# onclick=DictGloss('the','0','1'); >"+SL[1][2]+"</a> | <a href=# onclick=DictGloss('eth','0','2'); >"+SL[1][3]+"</a>";break;
		case '2':SelectIt=sDictO+"<a href=# onclick=DictGloss('interPTE','0','1'); >"+SL[2][0]+"</a> | <a href=# onclick=DictGloss('interTEP','0','1'); >"+SL[2][1]+"</a> | <a href=# onclick=DictGloss('interEP','0','2'); >"+SL[2][2]+"</a> | <a href=# onclick=DictGloss('interPE','0','1'); >"+SL[2][3]+"</a>";break;
		case '3':SelectIt=sDictO+"<a href=# onclick=DictGloss('interETTE','1','1'); >"+SL[3][0]+"</a> | <a href=# onclick=DictGloss('interETTE','0','2'); >"+SL[3][1]+"</a>";break;
		default :SelectIt="<a href=# onclick=SelectIt('1'); >"+SL[0][1]+"</a> | <a href=# onclick=SelectIt('2'); >"+SL[0][2]+"</a> | <a href=# onclick=SelectIt('3'); >"+SL[0][3]+"</a>";break;
	}
	d.g("SelectIt").innerHTML="<div align=center ><table><tr bgcolor=#f0f0f1><td><font size=4> "+SelectIt+"</font></td></tr></table></div>";
}

function DictGloss(dictDB,selectColumn,dictLang) {
	var submenu="";
	if (dictLang==1) {
		var sub1=global.langs['DictGlos']
		var sub1num= new Array('161', '162', '164', '168', '169', '170', '172', '173', '175', '176', '177', '178', '179', '181', '182', '183', '184', '185', '187', '188', '190', '192', '193', '194', '195', '197', '199', '202', '203', '205', '224', '225', '226', '228', '227', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122');
	}
	if (dictLang==2) {
		var sub1=new Array("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z");
		var sub1num=new Array('97','98','99','100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122');
	}
	for (var i1=0;i1<sub1.length ;i1++ ) {
		if (i1>0) {submenu=submenu+" | ";}
		submenu=submenu+"<a href=# onclick=load('1');Ajax('dictSub','O=DictC&callTo=RunDictIndex&bdr=off&work=list100&dictDB="+dictDB+"&head="+sub1num[i1]+"&selectColumn="+selectColumn+"') >"+sub1[i1]+"</a>";
	}
	d.g("submenu").innerHTML="<div align=center ><table><tr bgcolor=#F6FAF7><td align=center><font size=4>"+submenu+"</font></td></tr></table></div>";
}

//สำหรับ sskw
function SSSend () {
	var pu;
	var get =d.g('kw1').value;
	var getn1 =d.g('n11').value;
	pu="O=Pkw&SSKey=on&c[1]=1&c[2]=2&c[3]=3&c[4]=4&c[5]=5&c[6]=6&kw="+get+"&n1="+getn1;
	return pu;
}

//ไฮไลท์ฟอร์ม ใช้ไม่ได้ ทำแล้วไฮไลท์เลย ไม่ย้อนกลับเมื่อเลิกคลิก
var highlightcolor="yellow"

var ns6=d.g&&!document.all
var previous=''
var eventobj

//Regular expression to highlight only form elements
var intended=/INPUT|TEXTAREA|SELECT|OPTION/

//Function to check whether element clicked is form element
function checkel(which) {
if (which.style&&intended.test(which.tagName)) {
if (ns6&&eventobj.nodeType==3)
eventobj=eventobj.parentNode.parentNode
return true
}
else
return false
}

//Function to highlight form element
function highlight(e) {
eventobj=ns6? e.target : event.srcElement
if (previous!='') {
if (checkel(previous))
previous.style.backgroundColor=''
previous=eventobj
if (checkel(eventobj))
eventobj.style.backgroundColor=highlightcolor
}
else{
if (checkel(eventobj))
eventobj.style.backgroundColor=highlightcolor
previous=eventobj
}
}
//ไฮไลท์ฟอร์มจบ

//set cookie of psearch
function SCk(ckN,ckValue,nDays) {
 var today = new Date();
 var expire = new Date();
 if (nDays==null || nDays==0) nDays=1;
 expire.setTime(today.getTime() + 3600000*24*nDays);
 document.cookie = ckN+"="+escape(ckValue)
                 + ";expires="+expire.toGMTString();
}

//read cookie
function RCK(ckN) {
 var Ck=""+document.cookie;
 var ind=Ck.indexOf(ckN);
 if (ind==-1 || ckN=="") return ""; 
 var ind1=Ck.indexOf(';',ind);
 if (ind1==-1) ind1=Ck.length; 
 return unescape(Ck.substring(ind+ckN.length+1,ind1));
}
//ส่งสารานุกรม สร้างฟอร์ม สำหรับใส่ชื่อด้วย

function ENCW(linkdata) {
	var ENCartname="ศัพท์ที่เกี่ยวข้อง<input id=ENCartKW  type=text size=20 >หัวข้อเรื่องย่อย<input id=ENCartname type=text size=30 ><input type=button  onclick=Ajax('load','O=Enc&seEnc=w&Enc_data='+EncodeText(d.g(\"ENCartname\").value)+'s_p~'+EncodeText(d.g(\"ENCartKW\").value)+'~"+linkdata+"'); value='ส่งสารานุกรม'><input type=button value='ปิด' onclick=load('0');>";
	d.g("load").innerHTML=ENCartname;
}