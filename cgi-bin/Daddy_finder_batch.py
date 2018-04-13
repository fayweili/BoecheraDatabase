#!/usr/bin/env python
import cgi
import cgitb
import os
import MDW
import sys

cgitb.enable()

MicroSat_dic = MDW.MicSatDatabaseReader('Boechera_full.txt')
MDW.SpecimenDatabaseReader('DNAextr_T29.txt')

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
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
</head>
<body>
	<h1></h1>
	<h2>PRIUS: Parental Relationship Identification Using Subtraction </h2>
		<form action="Daddy_finder_batch.py" method="post" enctype="multipart/form-data">
			<p><input type="file" name="file"></p>
			<p><input type="submit" value="Upload" onclick="$('#loading').show();">
			<input type='button' value='Download template' onClick="window.location.href='http://sites.biology.duke.edu/windhamlab/query_import.xls'"></p>						
			<br>
		</form>
	<script>
		function message() {
		    alert("PRIUS might take a while to finish; please be patient! ");
			}
	</script>
	<div id="loading" style="display:none;"><img src="loading.gif" alt="" /></div>

""")

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

#os.chdir('../files/')
os.chdir('files/')
# Test if the file was uploaded
if fileitem.filename:
   
	# strip leading path from file name to avoid directory traversal attacks
	fn = os.path.basename(fileitem.filename)
	open(fn, 'wb').write(fileitem.file.read())
	message = 'The file "' + fn + '" was uploaded successfully'
	#print("<p>" + message + "</p>" + "</body></html>")

else:
	message = 'No file was uploaded'
	print("<p>" + message + "</p>" + "</body></html>")
	sys.exit()

QueryMicroSat_dic = MDW.QueryMicSatReader(fn)

for EachQuery in QueryMicroSat_dic:
	print "<h3>Query: ", EachQuery, "</h3>"
	Query_MicroSat = QueryMicroSat_dic[EachQuery]
	Query_MicroSat = MDW.AddNullAllele(Query_MicroSat)

	if MDW.Heterozygosity(Query_MicroSat) > 0.5:
		if MDW.CheckTrigenomic(Query_MicroSat):
			print "<p>This appears to be a triploid hybrid </p>"
			#if form.getvalue("Full_search"):
			MDW.DaddyFinder_full(Query_MicroSat, EachQuery, Old_algorithm=False)
			#else:
			#	MDW.DaddyFinder_quick(Query_MicroSat, EachQuery, Old_algorithm=False)
		else:
			print "<p>This appears to be a diploid hybrid </p>"
			#if form.getvalue("Full_search"):
			MDW.DaddyFinder_full(Query_MicroSat, EachQuery, Old_algorithm=True, Trigenomic_input=False)
			#else:
			#	MDW.DaddyFinder_quick(Query_MicroSat, EachQuery, Old_algorithm=True, Trigenomic_input=False)			
		
	else:
		print "<p>The heterozygosity of", EachQuery, "is lower than 0.5, and likely to be a diploid; therefore PRIUS cannot be performed.", "</p><br>"


print(
"""
</body>
</html>
""") 