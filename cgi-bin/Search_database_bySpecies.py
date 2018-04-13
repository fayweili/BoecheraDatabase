#!/usr/bin/env python
import cgi
import cgitb
import MDW
import os
import sys
import glob

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
	<h2>Search by taxon </h2>
	<form action = 'Search_database_bySpecies.py'>
		<label>Taxon name: </label>
		<input type='text' name='species' size='25'>		
		<button type='submit'>Enter</button>
		<br>
		<br>
		<input type="checkbox" name="MatchOnlyDiploid" value="MatchOnlyDiploid">Display only sexual diploids </div><br>

	</form>
""")

args = cgi.FieldStorage()
input = args.getfirst("species")
try:
	input = args.getfirst("species").upper()
except:
	sys.exit("</body></html>")

if args.getvalue("MatchOnlyDiploid"):
	MatchOnlyDiploid = True
else:
	MatchOnlyDiploid = False
if args.getvalue("MatchOnlyApomict"):
	MatchOnlyApomict = True
else:
	MatchOnlyApomict = False

if MatchOnlyDiploid and MatchOnlyApomict:
	print "<h3>You can only check one box, either displaying sexual diploids or apomictic hybrids</h3>"
	sys.exit("""
	</body>
	</html>
	""")

os.chdir('files/')
file_list = glob.glob('*')
for file in file_list:
	os.remove(file)

print "<h3>Query:", input, "</h3>"
MDW.SearchSpecies(input, MatchOnlyDiploid, MatchOnlyApomict)

print(
"""
</body>
</html>
""") 