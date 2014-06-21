#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ecgi import *
import tfunc
print "Content-Type: text/html;charset=utf-8"
print

title=""
pageNum=0
lPage=[]
print "กำลังแก้ไขฐานข้อมูลที่ %s หน้า %s..."%(ob,op)
hf=open("db/history/"+ob+".txt");lHPage=hf.readlines();hf.close()
for page in open("db/main/"+ob+".txt") :
	lineNum=pageNum
	pageNum+=1
	if pageNum==int(op) :
		lPage.append((urllib.unquote_plus(edited_content)+"\n").decode("utf8").encode("tis620"))
		if lHPage[lineNum].strip()=="" :
			lHPage[lineNum]=page
		else :
			lHPage[lineNum]=lHPage[lineNum].strip("\n")
			lHPage[lineNum]+="<hist>".decode("utf8").encode("tis620")+page
	else :
		lPage.append(page)

f=open(""+ob+".txt", "w");f.write("".join(lPage));f.close()
f=open(""+ob+"h.txt", "w");f.write("".join(lHPage));f.close()

print "ดำเนินการเสร็จสิ้นแล้ว."
