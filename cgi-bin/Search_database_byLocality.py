#!/usr/bin/env python
import cgi
import cgitb
import MDW
import os
import sys
cgitb.enable()

MicroSat_dic = MDW.MicSatDatabaseReader('Boechera_full.txt')

print "Content-Type: text/html"
print
print(
"""
<html>	
<head>
	<title> MDW </title>
	<style type="text/css">
	body {
		font-family:verdana,arial,sans-serif;
		font-size:10pt;
		margin:30px;
		background-color:#F5ECCE;
		}
	h3 {
		font-size:10pt;
		}
	th {
		font-size:10pt;
		}
	td {
		font-size:8pt;
		}
	</style>	
</head>
<body>
	<h2>Search by locality </h2>
	<form action = 'Search_database_byLocality.py'>
		<label>Locality: </label>
		<input type='text' name='locality' size='25'>
		<button type='submit'>Enter</button>

	</form>
""")

args = cgi.FieldStorage()
try:
	input = args.getfirst("locality").upper()
except:
	sys.exit("</body></html>")

os.chdir('files/')
print "<h3>Query:", input, "</h3>"
MDW.SearchLocality(input)

print(
"""
</body>
</html>
""") 



