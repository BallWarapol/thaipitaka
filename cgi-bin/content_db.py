#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ecgi import *
import tfunc, os
print "Content-Type: text/html;charset=utf-8"
print
bookNames=tfunc.bookDetails
print """<html><head><meta http-ekwuiv="Content-Type" content="text/html; charset=UTF-8">
<title>รายชื่อหนังสือในระบบ</title></head><body><div align=center><b>รายชื่อหนังสือในระบบ</b></div>"""
print tfunc.tui.topborder

title=""
pageNum=0

print "<ui  class=viewer>"
ls=sorted(os.listdir("./db/main"))
for s in ls :
	ob=s.replace(".txt","")
	print "<a href=./content_book.py?ob=%s target=_blank >ฐานข้อมูลลำดับที่ %s - %s</a></br>"%(ob, ob, bookNames[int(ob)][0])
	
print "</ui>"
print tfunc.tui.bottomborder
print """</body></html>"""
