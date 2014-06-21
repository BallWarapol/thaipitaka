
# enable debugging

import cgi
import cgitb
import re
import urllib

cgitb.enable()
 
_form = cgi.FieldStorage()

for _key in _form :
    exec(_key + '= """'+ _form[_key].value+'"""') 
