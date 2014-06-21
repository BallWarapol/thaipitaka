#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ecgi import *
import  tfunc
print "Content-Type: text/html;charset=utf-8"
print

bookNames=tfunc.bookDetails
pnum=0
print """<html>
<head>
<meta http-ekwuiv="Content-Type" content="text/html; charset=UTF-8">
<title>สารบัญของ %s</title>
</head>
<body><div align=center>สารบัญของ <a href='./read.py?ob=%s&op=%s&kw=none' targrt=_self ><b>%s</b></a></div>"""%(bookNames[int(ob)][0],ob, 1,bookNames[int(ob)][0])
print tfunc.tui.topborder

for page in open("db/main/"+ob+".txt") :
	pnum+=1
	page=page.decode("tis620").encode("utf8").lower()
	for line in page.split("</br>") :
		if ("<h"  in line or  line[0:10].strip()=="") and line.strip() !="":
			line=tfunc.specialChar(line)
			title=re.sub("<.*?>",  "", line)
			print "<li class=viewer><a href='./read.py?ob=%s&op=%s&kw=none' targrt=_self >%s - %s</a></li>"%(ob, pnum,title,pnum)
	
print tfunc.tui.bottomborder
print """</body></html>"""
