#!/usr/bin/env python
#-*-coding:utf8-*-

import BaseHTTPServer
import CGIHTTPServer
import os
if not "puppy" in  str(os.environ):
	os.chdir("/home/a/applications/thaipitaka")
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 16789)
#handler.cgi_directories = [""]
httpd = server(server_address, handler)
httpd.serve_forever()
