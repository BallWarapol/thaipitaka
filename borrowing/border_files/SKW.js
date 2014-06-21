
/*Satemy Pali Keyboard*/
function KeyBoard(Switch) {
	var key,keyShow,kf,kl,vak,mode,puts;
	key="ก,ข,ค,ฆ,ง,จ,ฉ,ช,ฌ,ญ,ฏ,ฐ,ฑ,ฒ,ณ,ต,ถ,ท,ธ,น,ป,ผ,พ,ภ,ม,ย,ร,ล,ว,ส,ห,ฬ,อ,า,ิ,ี, ุ, ู,เ,โ,ฺ,ํ,ึ,,,,,+,ลบ,ล้าง"; //ไม่ต้อง langs เพราะไม่เกี่ยวจอ
	keyShow =global.langs['KeyBoard'].keyShow;
	key = key.split(","); keyShow = keyShow.split(",");
	kf = Array("ก","จ","ฏ","ต","ป","ย","อ","อฺ"); kl = Array("ง","ญ","ณ","น","ม","ฬ","โอ","ล้าง");
	msg="<table>";
	for (var i=0; i < keyShow.length; i++) {
		for (var i1=0; i1 < kf.length; i1++) { if (keyShow[i]==kf[i1]) {msg=msg+"<tr>"; vak=""+kf[i1]+":";} }
		msg+="<td bgcolor=#F6f6f6 align=center>"+vak+" <a href=# onclick=cha('"+key[i]+"') > <font size=5 >"+keyShow[i]+"</font> </a></td>";
		for (var i1=0; i1 < kl.length; i1++) { if (key[i]==kl[i1]) {msg=msg+"</tr>";} }
		vak="";
	}
	msg=msg+"</table>";
	switch (Switch) {
		case 1 : puts = msg; mode = 0;break;
		case 0 : puts = ""; mode = 1;break;
	}
		d.g("KeyBoard").innerHTML = puts;
		d.g("switchKeyBoard").innerHTML ="<a href=# onclick='KeyBoard("+mode+")' ><sub>&#9000;</sub></-img src=images/keyboard.png border=no-/></a>  ";
}
/*ใส่คีย์บอร์ด*/
function cha(cha) {
	var str=document.form1.elements.kw.value;
		switch (cha) {
			case "ลบ"	: str = str.substring(0,(str.length-1));break;
			case "ล้าง"	: str = "" ;break;
			default			: str = str+cha;
		}
			document.form1.kw.value=str; 
			document.form1.kw.focus();
}

function ChkB(col) {

	var str='<div id=tabc0 >';
	for(var n1=1;n1<DB.length;n1++) {

	str=str+"<div id='tabc"+(n1)+"'><table width=95% >";
	/*if (col.slice(0,1)!=0 && col.slice(0,1)!=n1 ) {
			continue;
		}*/
	for(var n=1;n<DB[n1].length;n++) {
	var chk=0;
		str=str+"<tr><td width=2% valign=top><font size=4 color=green>"+n+".</font></td><td> <font size=4 color=blue><label><input type=checkbox id=ibb name=ibb["+n1+"]["+n+"] value="+n1+""+n+" "; 
	if (col==0) {
	}
	else if (col=="123321") {chk=1; }
	else if (col=="1234567" && n1<=7) {chk=1; }
	else if (col=="8901234" && n1>=8) {chk=1; }
	
	////หมวดพระวินัยปาฬิทั้งหมด
	else if (col=="00100") { 	if(n1==1) { 	if (n<=8) { 	chk=1; 	} 	} 	if(n1==2) { 	if ( n<=3) { 	chk=1; 	} 	} 	if(n1==3) { 	if ( n<=7) { 	chk=1; 	} 	} 	if(n1==4) { 	if (n<DB[4].length) { 	chk=1; 	} 	} 	
	//จบ
	}
	////หมวดพระสูตรปาฬิทั้งหมด
	else if (col=="00200" && col.length==5) { 	if(n1==1) { 	if (n>=9 && n<=33) { 	chk=1; 	} 	} 	if(n1==2) { 	if (n>=4 && n<=45) { 	chk=1; 	} 	} 	if(n1==3) { 	if (n>=8 && n<=28) { 	chk=1; 	} 	} 	if(n1==5) { 	if (n<DB[5].length) { 	chk=1; 	} 	} 
	//จบ
	}
	////หมวดพระอภิธรรมปาฬิทั้งหมด
	else if (col=="00300") { 	if(n1==1) { 	if (n>=34 && n<=45) { 	chk=1; 	} 	} 	if(n1==2) { 	if (n>=46 && n<=48) { 	chk=1; 	} 	} 	if(n1==3) { 	if (n>=29 && n<=34) { 	chk=1; 	} 	} 	if(n1==6) { 	if (n<DB[6].length) { 	chk=1; 	} 	} 
	//จบ
	}
	////หมวดสังคหอรรถกถา-ฏีกาปาฬิทั้งหมด
	else if (col=="00400") { 	if(n1==4) { 	if (n<DB[4].length) { 	chk=1; 	} 	} 	if(n1==5) { 	if (n<DB[5].length) { 	chk=1; 	} 	} 	if(n1==6) { 	if (n<DB[6].length) { 	chk=1; 	} 	}
	//จบ
	}
	//วินัยแปลทั้งหมด
	else if (col=="00500") {	if(n1==8) { 	if ( n<=8) { 	chk=1; 	} 	} if(n1==9) { 	if (n<=3) { 	chk=1; 	} 	} if(n1==10) { 	if ( n<=7) { 	chk=1; 	} 	}
	}
	//พระสูตรแปลทั้งหมด
	else if (col=="00600") {	if(n1==8) { 	if (n>=9 && n<=33) { 	chk=1; 	} 	} 	if(n1==9) { 	if (n>=4 && n<=45) { 	chk=1; 	} 	} if(n1==10) { 	if (n>=8 && n<=28) { 	chk=1; 	} 	}	
	}
	//พระอภิธรรมแปลทั้งหมด
	else if (col=="00700") {	if(n1==8) { 	if (n>=34 && n<=45) { 	chk=1; 	} 	} 	if(n1==9) { 	if (n>=46 && n<=48) { 	chk=1; 	} 	} 	if(n1==10) { 	if (n>=29 && n<=34) { 	chk=1; 	} 	}
	}
		////หมวดสังคหอรรถกถา-ฏีกาปาฬิทั้งหมด
	else if (col=="00800") { 	if(n1==11) { 	if (n<DB[11].length) { 	chk=1; 	} 	} 	if(n1==12) { 	if (n<DB[12].length) { 	chk=1; 	} 	} 	if(n1==13) { 	if (n<DB[13].length) { 	chk=1; 	} 	}
	//จบ
	}

	//กรณี n1=1 (ค้นพระไตรปิฎก)
	else if 	(n1==1) { 	 	if ((col=="10")&&(n<DB[1].length)) { 	chk=1; 	} 	else	if ((col=="11")&&( n<=8)) { 	chk=1; 	} 	else	if ((col=="12")&&(n>=9 && n<=33)) { 	chk=1; 	} 	else	if ((col=="12222")&&(n>=9 && n<=24)) { 	chk=1; 	} 	else	if ((col=="121")&&(n>=9 && n<=11)) { 	chk=1; 	} 	else	if ((col=="122")&&(n>=12 && n<=14)) { 	chk=1; 	} 	else	if ((col=="123")&&(n>=15 && n<=19)) { 	chk=1; 	} 	else	if ((col=="124")&&(n>=20 && n<=24)) { 	chk=1; 	} 	else	if ((col=="125")&&(n>=25 && n<=33)) { 	chk=1; 	} 	else	if ((col=="1255")&&(n>=29 && n<=31)) { 	chk=1; 	} 	else	if ((col=="13")&&(n>=34 && n<=45)) { 	chk=1; 	}
	//จบ กรณี n1=1 (ค้นพระไตรปิฎก)
	}
	//อรรถกถาของพระไตรปิฎก
	 else if 	(n1==2) { 	 	 	if ((col=="20")&&(n<DB[2].length)) { 	chk=1; 	} 	else	if ((col=="21")&&( n<=3)) { 	chk=1; 	} 	else	if ((col=="22")&&(n>=4 && n<=45)) { 	chk=1; 	} 	else	if ((col=="22222")&&(n>=4 && n<=18)) { 	chk=1; 	} 	else	if ((col=="221")&&(n>=4 && n<=6)) { 	chk=1; 	}	 	else	if ((col=="222")&&(n>=7 && n<=10)) { 	chk=1; 	}	 	else	if ((col=="223")&&(n>=11 && n<=15)) { 	chk=1; 	} 	else	if ((col=="224")&&(n>=16 && n<=18)) { 	chk=1; 	} 	else	if ((col=="225")&&(n>=19 && n<=45)) { 	chk=1; 	} 	else	if ((col=="2251")&&(n>=20 && n<=21)) { 	chk=1; 	} 	else	if ((col=="2252")&&((n==19) || (n>=22 && n<=25))) { 	chk=1; 	} 	else	if ((col=="2253")&&(n>=26 && n<=27)) { 	chk=1; 	} 	else	if ((col=="2254")&&(n>=31 && n<=37)) { 	chk=1; 	} 	else	if ((col=="2255")&&(n>=38 && n<=41)) { 	chk=1; 	} 	else	if ((col=="2256")&&((n>=28 && n<=30) || (n>=42 && n<=45))) { 	chk=1; 	} 	else	if ((col=="23")&&(n>=46 && n<=48)) { 	chk=1; 	} 	}
	//ฏีกาของอรรถกถาพระไตรปิฎก
	 else if 	(n1==3) { 	 	 	if ((col=="30")&&( n<=n<DB[3].length)) { 	chk=1; 	} 	else	if ((col=="31")&&( n<=7)) { 	chk=1; 	} 	else	if ((col=="32")&&(n>=8 && n<=28)) { 	chk=1; 	} 	else	if ((col=="32222")&&(n>=8 && n<=24)) { 	chk=1; 	} 	else	if ((col=="321")&&(n>=8 && n<=12)) { 	chk=1; 	} 	else	if ((col=="322")&&(n>=13 && n<=16)) { 	chk=1; 	} 	else	if ((col=="323")&&(n>=17 && n<=21)) { 	chk=1; 	}
	//อํ.ฏี.
	else	if ((col=="324")&&(n>=22 && n<=24)) {chk=1;}
	//ชา.ฏี.
	else	if ((col=="3254")&&(n>=25 && n<=28)) {chk=1;}
	//อภิ.มู-อนุฏี.
	else	if ((col=="33")&&(n>=29 && n<=34)) {chk=1;}
	}
	//วินยสงฺคห อ.-ฏี.
	else if 	(n1==4) {
	if ((col=="40")&&(n<DB[4].length)) {chk=1;}
	}
	//อ.วิสุทธิ.
	else if 	(n1==5) {
	if ((col=="50")&&(n<DB[5].length)) { 	chk=1; 	} 	else	if ((col=="51")&&( n<=4)) { 	chk=1; 	} 	else	if ((col=="52")&&(n>=5 && n<=9)) { 	chk=1; 	} 	}
	//อภิธมฺมสงฺคห อ.-ฏี.
	else if 	(n1==6) {
	if ((col=="60")&&(n<DB[6].length)) {chk=1;}
	}
	else if (n1==8) {
	//จุฬาแปล
	if ((col=="80")&&(n<DB[8].length)) { 	chk=1; 	} 	else	if ((col=="81")&&( n<=8)) { 	chk=1; 	} 	else	if ((col=="82")&&(n>=9 && n<=33)) { 	chk=1; 	} 	else	if ((col=="82222")&&(n>=9 && n<=24)) { 	chk=1; 	} 	else	if ((col=="821")&&(n>=9 && n<=11)) { 	chk=1; 	} 	else	if ((col=="822")&&(n>=12 && n<=14)) { 	chk=1; 	} 	else	if ((col=="823")&&(n>=15 && n<=19)) { 	chk=1; 	} 	else	if ((col=="824")&&(n>=20 && n<=24)) { 	chk=1; 	} 	else	if ((col=="825")&&(n>=25 && n<=33)) { 	chk=1; 	} 	else	if ((col=="8255")&&(n>=29 && n<=31)) { 	chk=1; 	} 	else	if ((col=="83")&&(n>=34 && n<=45)) { 	chk=1; 	} 	}

	else if (n1==9) {
	//อ. จุฬาแปล
	if ((col=="90")&&((n>=7 && n<=10)||(n>=16 && n<=18))) { 	chk=1; 	} 	if ((col=="922")&&(n>=7 && n<=10)) { 	chk=1; 	} 	if ((col=="924")&&(n>=16 && n<=18)) { 	chk=1; 	} 	}
	//ฏีกาของอรรถกถาพระไตรปิฎก
	 else if 	(n1==10) { 	 	 	if ((col=="100")&&( n<=n<DB[3].length)) { 	chk=1; 	} 	else	if ((col=="101")&&( n<=7)) { 	chk=1; 	} 	else	if ((col=="102")&&(n>=8 && n<=28)) { 	chk=1; 	} 	else	if ((col=="102222")&&(n>=8 && n<=24)) { 	chk=1; 	} 	else	if ((col=="1021")&&(n>=8 && n<=12)) { 	chk=1; 	} 	else	if ((col=="1022")&&(n>=13 && n<=16)) { 	chk=1; 	} 	else	if ((col=="1023")&&(n>=17 && n<=21)) { 	chk=1; 	}
	//อํ.ฏี.
	else	if ((col=="1024")&&(n>=22 && n<=24)) {chk=1;}
	//ชา.ฏี.
	else	if ((col=="10254")&&(n>=25 && n<=28)) {chk=1;}
	//อภิ.มู-อนุฏี.
	else	if ((col=="103")&&(n>=29 && n<=34)) {chk=1;}
	}
	//วินยสงฺคห อ.-ฏี.
	else if 	(n1==11) {
	if ((col=="40")&&(n<DB[4].length)) {chk=1;}
	}
	//อ.วิสุทธิ.
	else if 	(n1==12) {
	if ((col=="50")&&(n<DB[5].length)) { 	chk=1; 	} 	else	if ((col=="51")&&( n<=4)) { 	chk=1; 	} 	else	if ((col=="52")&&(n>=5 && n<=9)) { 	chk=1; 	} 	}
	//อภิธมฺมสงฺคห อ.-ฏี.
	else if 	(n1==13) {
	if ((col=="60")&&(n<DB[6].length)) {chk=1;}
	}
	else if 	(n1==14) {
	if ((col==" ")&&(n<DB[7].length)) {chk=1;}
	}
	else if 	(n1==15) {
	if ((col=="150")&&(n<DB[15].length)) {chk=1;} else	if ((col=="151")&&( n<=8)) { 	chk=1; 	} 	else	if ((col=="152")&&(n>=9 && n<=33)) { 	chk=1; 	} 	else	if ((col=="152222")&&(n>=9 && n<=24)) { 	chk=1; 	} 	else	if ((col=="1521")&&(n>=9 && n<=11)) { 	chk=1; 	} 	else	if ((col=="1522")&&(n>=12 && n<=14)) { 	chk=1; 	} 	else	if ((col=="1523")&&(n>=15 && n<=19)) { 	chk=1; 	} 	else	if ((col=="1524")&&(n>=20 && n<=24)) { 	chk=1; 	} 	else	if ((col=="1525")&&(n>=25 && n<=33)) { 	chk=1; 	} 	else	if ((col=="15255")&&(n>=29 && n<=31)) { 	chk=1; 	} 	else	if ((col=="153")&&(n>=34 && n<=45)) { 	chk=1; 	}

	}
	else if 	(n1==16) {
	if ((col=="160")&&(n<DB[16].length)) {chk=1;}	else	if ((col=="161")&&( n<=3)) { 	chk=1; 	} 	else	if ((col=="162")&&(n>=4 && n<=45)) { 	chk=1; 	} 	else	if ((col=="162222")&&(n>=4 && n<=18)) { 	chk=1; 	} 	else	if ((col=="1621")&&(n>=4 && n<=6)) { 	chk=1; 	}	 	else	if ((col=="1622")&&(n>=7 && n<=9)) { 	chk=1; 	}	 	else	if ((col=="1623")&&(n>=10 && n<=12)) { 	chk=1; 	} 	else	if ((col=="1624")&&(n>=13 && n<=15)) { 	chk=1; 	} 	else	if ((col=="1625")&&(n>=16 && n<=45)) { 	chk=1; 	} 	else	if ((col=="16251")&&(n>=17 && n<=18)) { 	chk=1; 	} 	else	if ((col=="16252")&&((n==16) || (n>=19 && n<=22))) { 	chk=1; 	} 	else	if ((col=="16253")&&(n>=23 && n<=24)) { 	chk=1; 	} 	else	if ((col=="16254")&&(n>=28 && n<=37)) { 	chk=1; 	} 	else	if ((col=="16255")&&(n>=38 && n<=41)) { 	chk=1; 	} 	else	if ((col=="16256")&&((n>=25 && n<=27) || (n>=42 && n<=45))) { 	chk=1; 	} 	else	if ((col=="163")&&(n>=46 && n<=48)) { 	chk=1; 	} 	
	}
	else if 	(n1==17) {
	if ((col=="170")&&(n<DB[17].length)) {chk=1;} else	if ((col=="171")&&( n<=8)) { 	chk=1; 	} 	else	if ((col=="172")&&(n>=9 && n<=33)) { 	chk=1; 	} 	else	if ((col=="172222")&&(n>=9 && n<=24)) { 	chk=1; 	} 	else	if ((col=="1721")&&(n>=9 && n<=11)) { 	chk=1; 	} 	else	if ((col=="1722")&&(n>=12 && n<=14)) { 	chk=1; 	} 	else	if ((col=="1723")&&(n>=15 && n<=19)) { 	chk=1; 	} 	else	if ((col=="1724")&&(n>=20 && n<=24)) { 	chk=1; 	} 	else	if ((col=="1725")&&(n>=25 && n<=33)) { 	chk=1; 	} 	else	if ((col=="17255")&&(n>=29 && n<=31)) { 	chk=1; 	} 	else	if ((col=="173")&&(n>=34 && n<=45)) { 	chk=1; 	}
	}
	else if 	(n1==18) {
	if ((col=="180")&&(n<DB[18].length)) {chk=1;}	else	if ((col=="181")&&( n<=10)) { 	chk=1; 	} 	else	if ((col=="182")&&(n>=11 && n<=74)) { 	chk=1; 	} 	else	if ((col=="182222")&&(n>=11 && n<=38)) { 	chk=1; 	} 	else	if ((col=="1821")&&(n>=11 && n<=16)) { 	chk=1; 	} 	else	if ((col=="1822")&&(n>=17 && n<=23)) { 	chk=1; 	} 	else	if ((col=="1823")&&(n>=24 && n<=31)) { 	chk=1; 	} 	else	if ((col=="1824")&&(n>=32 && n<=38)) { 	chk=1; 	} 	else	if ((col=="1825")&&(n>39 && n<=74)) { 	chk=1; 	} 	else	if ((col=="18255")&&(n>=65 && n<=69)) { 	chk=1; 	} 	else	if ((col=="183")&&(n>=75 && n<=91)) { 	chk=1; 	}
	}
	else if 	(n1==19) {
	if ((col=="190")&&(n<DB[19].length)) {chk=1;} else	if ((col=="191")&&( n<=7 || (n>=23 && n<=36))) { 	chk=1; 	} 	else	if ((col=="192")&&((n>=8 && n<=13) || (n>=37 && n<=45))) { 	chk=1; 	} 	else	if ((col=="193")&&((n>=14 && n<=22) || (n>=46 && n<=52))) { 	chk=1; 	} 	
	}
	else if 	(n1==20) {
	if ((col=="200")&&(n<DB[20].length)) {chk=1;} else if ((col=="201")&&(n>=1 && n<=14)) { 	chk=1; } else if ((col=="202")&&(n>=15 && n<=26)) { 	chk=1; } else if ((col=="203")&&(n>=27 && n<=39)) { 	chk=1; } else if ((col=="204")&&(n>=40 && n<=42)) { 	chk=1; } else if ((col=="205")&&(n>=43 && n<=46)) { 	chk=1; } else if ((col=="206")&&(n>=47 && n<=53)) { 	chk=1; } else if ((col=="207")&&(n>=54 && n<=64)) { 	chk=1; } else if ((col=="208")&&(n>=65 && n<=76)) { 	chk=1; } else if ((col=="209")&&(n>=77 && n<=81)) { 	chk=1; } 
	}
	else if 	(n1==21) {
	if ((col=="210")&&(n<DB[21].length)) {chk=1;}
	}

	if (chk==1) { chk=" checked=checked "; }
 	else{ chk=" "; }

	if (n1<15) {var O="PRead";}
	else {var O="LR";}
	str=str+chk+" >"+DB[n1][n]+"</label><a href=index.php?O="+O+"&n1="+n1+"&n="+n+"&pg=1&kw=~x~x~  target =blank>[เปิด]</a></font><br></td></tr>";
	str=str.replace(/\+/,", และ ");

}
	str=str+"</table></div>";
}
	var tid=d.g("divx");
	if (tid!=null) {tid.innerHTML= str+"</div>" ;}
	load('0');
	if (col!="0") {
		easytabs('1','1');
	}
}

/*function LK(O,n1,n) {
	window.location="index.php?O="+O+"&n1="+n1+"&n="+n+"&pg=1&kw=NOT";
}
<a onclick=LK('"+O+"','"+n1+"','"+n+"'); >&#9409</a> 
*/
//ตัดตัวอักษร
function CutLine() {
var puts='<a><select name="subS" id="subS" onchange="CutLineOption();" onmouseover=langs("deResultTypeForm")>';
puts+='<option  >'+global.langs['CutLine_SomeParagraph']+'</option>';
puts+='<option value="1" >'+global.langs['CutLine_Some']+'</option>';
puts+='<option value="2" >'+global.langs['CutLine_SomePlus']+'</option>';
puts+='</select><span id=deResultTypeForm></span></a>';
d.g('CutLine').innerHTML=puts;
}

function CutLineOption() {
		var tag="Option";
	var tid=d.g(tag);
	if (tid!=null) {
		if (d.g("subS").value>1) {
			var insert="<span class=body> "+global.langs["CutLine_Before"]+" : <input type=textbox name=cutBe size=1 value=15> "+global.langs["CutLine_After"]+" : <input type=textbox name=cutAf size=1 value=20></span>";
			tid.innerHTML =insert;
		}
		else {
			tid.innerHTML ="<input type=hidden name=cutBe value=15> <input type=hidden name=cutAf value=20>";
		}
	}
}
//จบตัดตัวอักษร

//กลุ่มของหน้าค้นบาลี
function PGG() {
var puts="<a><select name=pgg onchange=PGroup(this.options[this.selectedIndex].value); onmouseover=langs('deBookSelectForm','deBookGroupForm')>";
	for (i=0; i<global.PGG.length;i++) {
		puts+="<option value="+i+">"+global.PGG[i]+"</option>";
	}
if (d.g("PGG")!=null) {d.g("PGG").innerHTML=puts+"</select><span id=deBookGroupForm></span></a>";}
}

//กลุ่มของหน้าค้นบาลี
function PGroup(nu) {
var PGroup =global.PGroupName[nu].split(",");
var puts="<a><select name=col onchange=load('1');thisselect=this.options[this.selectedIndex].value;ChkB(thisselect);SCk('STPSelectCk',thisselect,'1'); onmouseover=langs('deBookSelectForm')>";
	for (i=0; i<PGroup.length;i++) {
		PGroup[i]=PGroup[i].split(">");
		puts+="<option value="+PGroup[i][0]+">"+PGroup[i][1]+"</option>";
	}
if (d.g("PGroup")!=null) {d.g("PGroup").innerHTML=puts+"</select><span id=deBookSelectForm></span></a>";}
}