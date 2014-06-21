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
<!-- TinyMCE -->
<script type="text/javascript" src="../borrowing/tinymce/jscripts/tiny_mce/tiny_mce.js"></script>
<script type="text/javascript">
	tinyMCE.init({
		// General options
		mode : "textareas",
		theme : "advanced",
		plugins : "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",

		// Theme options
		theme_advanced_buttons1 : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect",
		theme_advanced_buttons2 : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
		theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
		theme_advanced_buttons4 : "insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak",
		theme_advanced_toolbar_location : "top",
		theme_advanced_toolbar_align : "left",
		theme_advanced_statusbar_location : "bottom",
		theme_advanced_resizing : true,

		// Example content CSS (should be your site CSS)
		content_css : "../borrowing/tinymce/examples/css/content.css",

		// Drop lists for link/image/media/template dialogs
		template_external_list_url : "../borrowing/tinymce/examples/lists/template_list.js",
		external_link_list_url : "../borrowing/tinymce/examples/lists/link_list.js",
		external_image_list_url : "../borrowing/tinymce/examples/lists/image_list.js",
		media_external_list_url : "../borrowing/tinymce/examples/lists/media_list.js",

		// Replace values for the template plugin
		template_replace_values : {
			username : "Some User",
			staffid : "991234"
		}
	});
</script>
<!-- /TinyMCE -->
</head>
<body>"""

print """<div id="html-example" style="padding: 5px; height: 250px; width: 600px; background-color: #F6F6F0; color: black">"""

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
		print """<textarea id="edited_content" name="edited_content" cols=70 rows=30 style="width: 100%">~edit~"""+page+"""</textarea>
			<div>
		<!-- Some integration calls -->
		<a href="javascript:;" onmousedown="tinyMCE.get('edited_content').show();">[Show]</a>
		<a href="javascript:;" onmousedown="tinyMCE.get('edited_content').hide();">[Hide]</a>
		<a href="javascript:;" onmousedown="tinyMCE.get('edited_content').execCommand('Bold');">[Bold]</a>
		<a href="javascript:;" onmousedown="alert(tinyMCE.get('edited_content').getContent());">[Get contents]</a>
		<a href="javascript:;" onmousedown="alert(tinyMCE.get('edited_content').getContent().replace(/<p>.nbsp;<.p>/g,'</br>'));">[Get contents Modified]</a>
		<a href="javascript:;" onmousedown="alert(tinyMCE.get('edited_content').selection.getContent());">[Get selected HTML]</a>
		<a href="javascript:;" onmousedown="alert(tinyMCE.get('edited_content').selection.getContent({format : 'text'}));">[Get selected text]</a>
		<a href="javascript:;" onmousedown="alert(tinyMCE.get('edited_content').selection.getNode().nodeName);">[Get selected element]</a>
		<a href="javascript:;" onmousedown="tinyMCE.execCommand('mceInsertContent',false,'<b>Hello world!!</b>');">[Insert HTML]</a>
		<a href="javascript:;" onmousedown="tinyMCE.execCommand('mceReplaceContent',false,'<b>{$selection}</b>');">[Replace selection]</a>
		</div>
		<textarea cols=70 rows=30 style="width: 100%">"""+open("db/history/"+ob+".txt").readlines()[lineNum]\
		.decode("tis620").encode("utf8").replace("<hist>","<hr/>")+"""</textarea>"""
		break
		
print """***ต้อง shift + enter เพื่อ &lt;/br&gt;
<script>

function escapeSpeChar(line) {
	//var spechars=["( ) [ ] { } ^ $ \\\\ / | ? + * , .","; : @ & = - _ ! ~ ' \\" # < >"];
	var spechars=["( ) { } ^ $ | ? + , .","; : @ & = - _ ! ~ ' \\" # < >"];
	for (var h=0; h<spechars.length;h++) {
		var lSpechar=spechars[h].split(" ")
		var lEscapeSpechar=escape(spechars[h]).split("%%20");
		for (var i=0; i<lSpechar.length;i++) {
			eval('var re=(h==0) ? /\\\\'+lSpechar[i]+'/gm : /'+lSpechar[i]+'/gm;');
			//var re=(h==0) ? new RegExp("\\\\"+lSpechar[i]+"") : new RegExp(""+lSpechar[i]+"");
			//re.global=true;re.multiline=true;//เปลี่ยนไม่ได้
			line=line.replace(re, lEscapeSpechar[i]);
		}
	}
	return line;
}

$("#save").click(function() {
  var lnk = "edit_save.py?ob=%s&op=%s&kw=%s&edited_content="+escapeSpeChar(tinyMCE.get('edited_content').getContent().replace(/<p>.nbsp;<.p>|<br .>/g,'</br>').replace(/<p>&nbsp;<\/p>/gm,"</br>").replace(/<.?p>|\\n|~edit~/g,''));
  $.get(lnk, 
  function(data) {
    $("div#show-here").html(data);
  });
  return false;
});

</script>"""%(ob,op,cgi.escape(kw))

print "</ol>"
	
print """</div></body></html>"""
