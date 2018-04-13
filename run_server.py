#!/usr/bin/env python
import BaseHTTPServer
import SimpleHTTPServer
import CGIHTTPServer
import cgi

CGIHTTPServer.CGIHTTPRequestHandler.cgi_directories.append('/cgi-bin')
def run_server(port = 8000, server_class = BaseHTTPServer.HTTPServer, handler_class = CGIHTTPServer.CGIHTTPRequestHandler):
	httpd = server_class(('', port), handler_class)
	httpd.serve_forever()

'''
def run_server(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
'''
run_server()