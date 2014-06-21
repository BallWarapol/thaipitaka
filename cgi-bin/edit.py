#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ecgi import *
import re, tfunc
print "Content-Type: text/html;charset=utf-8"
print


print """<html>
<head>
<meta http-ekwuiv="Content-Type" content="text/html; charset=UTF-8">
<script src="../libjs/jquery.js" ></script>
</head>
<body>"""

title=""
pageNum=0
pagel=[]
op=int(op)
print "<h>แก้ไขพระไตรปิฎกเบอร์ %s หน้า %s</h>"%(ob,op)
print "<a href=edit.py?ob=%s&op=%s&kw=%s ><-|</a>"%(ob,(op-1),kw)
print " <a href=edit.py?ob=%s&op=%s&kw=%s >|-></a>"%(ob,(op+1),kw)
print "<input type=text size=4  id=gotopage onclick='try{kwbox}catch(e){kwbox=1; this.value=\"\";}; '  value='หน้าที่' /><input value='ไป' type=button onclick='window.location=\"edit.py?ob=%s&op=\"+document.getElementById(\"gotopage\").value+\"&kw=%s\"'/>"%(ob,kw)
print " | <a href=\"read.py?ob=%s&op=%s&kw=%s\" >1 หน้า</a>"%(ob,op,kw)
print " | <a href=\"read.py?ob=%s&op=%s&cscd=1&kw=%s#curPage\">cscd</a>"%(ob,op,kw)
print "<table width=60% hiegh=60%>"
		
for page in open("db/main/"+ob+".txt") :
	lineNum=pageNum
	pageNum+=1
	if pageNum==op :
		page=page.decode("tis620").encode("utf8").lower()
		print """<button id=save >save</button><div id="show-here"></div></br>"""
		print """<textarea id="edited_content" name="edited_content" style="height:70%;width: 70%;font-size:18;">"""+page.replace("\n","").replace("</br>","\n")+"""</textarea>
		<textarea  style="height:70%;width: 70%;font-size:18;">"""+open("db/history/"+ob+".txt").readlines()[lineNum]\
		.decode("tis620").encode("utf8").replace("<hist>","\n_____________________\n")+"""</textarea>"""
		break
		
print """***ต้อง shift + enter เพื่อ &lt;/br&gt;
<script>

$("#save").click(function() {
  var lnk = "edit_save.py?ob=%s&op=%s&kw=%s&edited_content="+document.getElementById('edited_content').value.replace("\\n","</br>").replace(/;/g,"__mysemicolon__");
  $.get(lnk, 
  function(data) {
    $("div#show-here").html(data);
  });
  return false;
});

</script>"""%(ob,op,cgi.escape(kw))

print "</ol>"
	
print """</div></body></html>"""
