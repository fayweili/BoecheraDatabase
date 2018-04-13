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
</head>
<body>
	<h2>TESLA: Taxon Enquiry based on Similarity of Loci and Alleles </h2>
		<form enctype="multipart/form-data" action="Search_database_batch.py" method="post">
			<p><input type="file" name="file"></p>
			<p><input type="submit" value="Upload">
			<input type='button' value='Download template' onClick="window.location.href='http://sites.biology.duke.edu/windhamlab/query_import.xls'"></p>			
			<input type="checkbox" name="MatchOnlyDiploid" value="MatchOnlyDiploid">Search only sexual diploids (i.e. heterozygosity < 0.5)<br>	

		</form>
""")

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

os.chdir('files/')

# Test if the file was uploaded
if fileitem.filename:
   
	# strip leading path from file name to avoid directory traversal attacks
	fn = os.path.basename(fileitem.filename)
	open(fn, 'wb').write(fileitem.file.read())
	message = 'The file "' + fn + '" was uploaded successfully'
else:
	message = 'No file was uploaded'
	print("<p>" + message + "</p>" + "</body></html>")
	sys.exit()

QueryMicroSat_dic = MDW.QueryMicSatReader(fn)


if form.getvalue("WeighByAlleleFreq"):
	WeighByAlleleFreq = True
else:
	WeighByAlleleFreq = False
	
if form.getvalue("MatchOnlyDiploid"):
	MatchOnlyDiploid = True
else:
	MatchOnlyDiploid = False

for EachQuery in QueryMicroSat_dic:
	Query_MicroSat = QueryMicroSat_dic[EachQuery]

	if WeighByAlleleFreq and not MatchOnlyDiploid:
		MDW.SpecimenMatcher(Query_MicroSat, 0.1, 1, EachQuery, Query_from_file = True, SaveFile=True, WeighByAlleleFreq = True)
		
	elif not WeighByAlleleFreq and not MatchOnlyDiploid:
		MDW.SpecimenMatcher(Query_MicroSat, 0.1, 1, EachQuery, Query_from_file = True, SaveFile=True, WeighByAlleleFreq = False)
	
	elif WeighByAlleleFreq and MatchOnlyDiploid:
		MDW.SpecimenMatcher(Query_MicroSat, 0.1, 0.3, EachQuery, Query_from_file = True, SaveFile=True, WeighByAlleleFreq = True)
	
	elif not WeighByAlleleFreq and MatchOnlyDiploid:
		MDW.SpecimenMatcher(Query_MicroSat, 0.1, 0.3, EachQuery, Query_from_file = True, SaveFile=True, WeighByAlleleFreq = False)
	
   

print(
"""
</body>
</html>
""") 