#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ecgi import *
import re, tfunc
print "Content-Type: text/html;charset=utf-8"
print
bookNames=tfunc.bookDetails
print """<html>
<head><meta http-ekwuiv="Content-Type" content="text/html; charset=UTF-8"></head>
<script src="../libjs/jquery.js" ></script>
<script src="../libjs/lib-thaipitaka.js" ></script>
<title>อ่าน : %s หน้า %s</title>
<body>"""%(bookNames[int(ob)][0],op)
title=""
pageNum=0
op=int(op)
print "<div align=center><b>%s หน้า %s</b></br>"%(bookNames[int(ob)][0],op)
print "<a href=read.py?ob=%s&op=%s&kw=%s ><-|</a>"%(ob,(op-1),kw)
print " <a href=read.py?ob=%s&op=%s&kw=%s >|-></a>"%(ob,(op+1),kw)
print "<input type=text size=4  id=gotopage onclick='try{kwbox}catch(e){kwbox=1; this.value=\"\";}; '  value='หน้าที่' /><input value='ไป' type=button onclick='window.location=\"read.py?ob=%s&op=\"+document.getElementById(\"gotopage\").value+\"&kw=%s\"'/>"%(ob,kw)
try:
	cscd
	print "<input value='page' type=button onclick='window.location=\"read.py?ob=%s&op=%s&kw=%s\"'/>"%(ob,op,kw)
except :
	print "<input value='cscd' type=button onclick='window.location=\"read.py?ob=%s&op=%s&cscd=1&kw=%s#curPage\"'/>"%(ob,op,kw)
print "<input value='ค้นหา' type=button onclick='window.location=\"index.py\"'/>"
print "<input value='สาบัญ' type=button onclick='window.location=\"content_book.py?ob=%s&op=%s&cscd=1&kw=%s#curPage\"'/>"%(ob,op,kw)
print "<input value='รายชื่อหนังสือ' type=button onclick='window.location=\"content_db.py\"'/>"
print "<input value='แก้ไข' type=button onclick='window.location=\"edit.py?ob=%s&op=%s&kw=%s\"'/>"%(ob,op,kw)
print "<input value='ฟ้อนต์' type=button onclick='fontChange();'/>"
print "</div>"
print tfunc.tui.topborder
print "<span class=viewer><ol>"
for page in open("db/main/"+ob+".txt") :
	pageNum+=1
	page=page
	page=tfunc.specialChar(page)
	try :
		if cscd :
			for line in page.split("</br>") :
                                if int(ob)<222:
                                        line="</br>".join(tfunc.wrapPali(line))
				if pageNum==op :
					print "<span class=xxx title='หน้า %s'><a name=curPage></a>"%pageNum
					print line.decode("tis620").encode("utf8").lower().replace(kw, "<u><b>"+kw+"</b></u>")+"</span>"+"</br>"
				else :
					print "<span class=xxx title='หน้า %s'>"%pageNum
					print line.decode("tis620").encode("utf8").lower().replace(kw, "<u><b>"+kw+"</b></u>")+"</span>"+"</br>"
	except :
		for line in page.split("</br>") :
			title=tfunc.getTitle(line,title)
			if pageNum==op :
                                if int(ob)<222:
                                        line="</br>".join(tfunc.wrapPali(line))
				#print """<script>document.title="%s"</script>"""%title
				#page=page.lower()
				#print "<br>".join(tfunc.wrapPali(page)).replace(kw, "<u><b>"+kw+"</b></u>")
				#print "</br>"+line.decode("tis620").encode("utf8").lower().replace(kw, "<u><b>"+kw+"</b></u>")
				#print line.decode("tis620").encode("utf8")+"</br>"
				print line.decode("tis620").encode("utf8").lower().replace(kw, "<u><b>"+kw+"</b></u>")+"</br>"

print "</ol></span>"
print "<center><a href=read.py?ob=%s&op=%s&kw=%s ><-|</a>"%(ob,(op-1),kw)
print " <a href=read.py?ob=%s&op=%s&kw=%s >|-></a></center>"%(ob,(op+1),kw)
print tfunc.tui.bottomborder
print "</body></html>"
