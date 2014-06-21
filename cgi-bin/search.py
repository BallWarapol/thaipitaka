#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ecgi import *
import re, tfunc
print "Content-Type: text/html;charset=utf-8"
print

bookNames=[z[0] for z in tfunc.bookDetails]
q=q.replace("","ฐ").replace("","ญ")
blist=[]
if "," not in q:
	kw=q
	blist=range(360,451)
else :
	z=q.split(",")
	kw=z[0]
	if z[0] =="" :
		ob=z[1]
		op="1"
		if ob.find("/")>-1 :
			ob=ob.split("/")
			op=ob[1]
			ob=ob[0]
		#print 'read.py?ob=%s&op=%s&kw=%s">'%(ob,op,"none")
		print '<meta HTTP-EQUIV="REFRESH" content="0"; url="localhost:16789/cgi-bin/read.py?ob=%s&op=%s&kw=%s">'%(ob,op,"none")
		exit()
	elif re.search("[^0-9,\-]",z[1]):
		for i, v in enumerate(bookNames):
			if v.find(z[1])>-1 :
				#print "%s --%s | "%(i,v)
				blist.append(i)
	else:
		for i in z[1:]:
			if i.find("-") >-1:
				i=i.split("-")
				blist.extend(range(int(i[0]),int(i[1])+1))
			else :
				blist.append(int(i))
	
blist.sort()
z=[]
for i in blist :
	if i not in z : 
		z.append(i)
blist=z

print """<html><head>
<title>ค้น "%s" ใน %s</title>
<script src="../libjs/jquery.js" ></script>
<script src="../libjs/lib-thaipitaka.js" ></script>
</head>
<body>"""%(kw,str(blist)[1:-1])
print tfunc.tui.topborder
print '<b><i>ผลการค้นหาคำว่า "'+kw+'" .-</i></b></br>'

for i in blist : 
	bnum=str(i)
	if len(bnum) <3 :
		bnum=("0"*(3-len(bnum)))+bnum
	title=""
	pageNum=0
	partNum=""
	found=False
	for page in open("db/main/"+bnum+".txt") :
		pageNum+=1
		if not i in [608]:
			page=page.decode("tis620").encode("utf8").lower()
			page=tfunc.specialChar(page)
		for line in page.split("</br>") :
			partNum=tfunc.getPartNum(line,partNum)
			title=tfunc.getTitle(line,title)

			if re.search(kw,line) :	
				if not found :
					print "&nbsp;&nbsp;&nbsp;&nbsp;<b>ฐานข้อมูลลำดับที่ %s </b>"%str(i)
					print "<ol class=viewer>"
					found=True
				if title != "" :
					print "<li class=viewer><a href='read.py?ob=%s&op=%s&kw=%s' target=_blank ><b>%s</b></a>"%(str(bnum),str(pageNum),cgi.escape(kw),title)
					print "</br>"+re.sub("<.*?>", "",line).replace(kw, "<u><b>"+kw+"</b></u>")
					print "</br><span style='color:green;font-size:20;word-spacing:0em'><i>%s ข้อ %s</i></span></li>"%(bookNames[i], partNum)
				else :
					print "<li class=viewer><a href='read.py?ob="+str(bnum)+"&op="+str(pageNum)+"&kw="+cgi.escape(kw)+"' target=_blank ><b>เบอร์ "+str(bnum)+" หน้า/บรรทัด/คำที่ "+str(pageNum)+"</b></a>"
					print "</br>"+line.replace(kw, "<u><b>"+kw+"</b></u>")+"</li>"
				print 
				#print "ที่มา : <script>document.write(window.location.href.split('/htbin')[0])</script>/htbin/read.py?ob="+str(bnum)+"&op="+str(pageNum)+"&kw="+cgi.escape(kw)
	if found :
		print "</ol>"
		
print tfunc.tui.bottomborder
print """</body></html>"""
