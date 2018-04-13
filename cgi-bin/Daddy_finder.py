#!/usr/bin/env python
import cgi
import cgitb
import MDW
import os
import sys
import glob
cgitb.enable()

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
	<h2>PRIUS: Parental Relationship Identification Using Subtraction </h2>
	<form action = 'Daddy_finder.py'>
		<label>DNA extraction ID: </label>
		<input type='text' name='ID' size='25' placeholder=' e.g. FW1111'>
		<button type='submit' onclick="$('#loading').show();">Enter</button><br><br>
		<br>
	</form>
	<script>
		function message() {
		    alert("PRIUS might take a while to finish; please be patient! ");
			}
	</script>
	<div id="loading" style="display:none;"><img src="IMG_3072.JPG" alt="" /></div>

""")

args = cgi.FieldStorage()
try:
	input = args.getfirst("ID").upper()
except:
	sys.exit("</body></html>")
	
if args.getvalue("Database_w_null"):
	MicroSat_dic = MDW.MicSatDatabaseReader('Boechera_full.txt')
	#MDW.SpecimenDatabaseReader('DNAextr_T29.txt')
	print "<h3>Error: MDW has not given FW the new file; use the other one instead...</h3>"
else:
	MicroSat_dic = MDW.MicSatDatabaseReader('Boechera_full.txt')
	#MDW.SpecimenDatabaseReader('DNAextr_T29.txt')

os.chdir('files/')
	
if input in MicroSat_dic:
	
	file_list = glob.glob('*')
	for file in file_list:
		os.remove(file)

	Query_MicroSat = MicroSat_dic[input]

	print "<h3>Query:", input, "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
	print "Heterozygosity:", MDW.Heterozygosity(Query_MicroSat), "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
	print "No. empty loci:", MDW.Heterozygosity(Query_MicroSat, Return_EmptyLoci_count=True), "</h3>"
	if MDW.Heterozygosity(Query_MicroSat) > 0.5:
		Query_MicroSat = MDW.AddNullAllele(Query_MicroSat)
		if MDW.CheckTrigenomic(Query_MicroSat):
			print "<p>This appears to be a triploid hybrid </p>"
			#if args.getvalue("Full_search"):
			MDW.DaddyFinder_full(Query_MicroSat, input, Old_algorithm=False)
			#else:
			#	MDW.DaddyFinder_quick(Query_MicroSat, input, Old_algorithm=False)
		else:
			print "<p>This appears to be a diploid hybrid </p>"
			#if args.getvalue("Full_search"):
			MDW.DaddyFinder_full(Query_MicroSat, input, Old_algorithm=True, Trigenomic_input=False)
			#else:
			#	MDW.DaddyFinder_quick(Query_MicroSat, input, Old_algorithm=True, Trigenomic_input=False)			

	else:
		print "<p>The heterozygosity of", input, "is lower than 0.5, and likely to be a diploid; therefore daddyfinder cannot be performed.", "</p>"


elif str(input) == 'APOMICTIC_DIPLOIDS':
	#os.chdir('../files/')

	file_list = glob.glob('*')
	for file in file_list:
		os.remove(file)

	apomictic_diploid_list = MDW.RandomSearch(99, sex_diploid=False, apo_diploid=True, apo_triploid=False)		
	
	for each_specimen in apomictic_diploid_list:
		Query_MicroSat = MicroSat_dic[each_specimen]
		Query_MicroSat = MDW.AddNullAllele(Query_MicroSat)
		#print "<h3>Query:", each_specimen, "</h3>"
		#print "<h3>Heterozygosity:", MDW.Heterozygosity(Query_MicroSat), "</h3>"
		#print "<h3>No. empty loci:", MDW.Heterozygosity(Query_MicroSat, Return_EmptyLoci_count=True), "</h3>"
		if args.getvalue("Full_search"):
			MDW.DaddyFinder_full(Query_MicroSat, each_specimen, Old_algorithm=True, Trigenomic_input=False)
		else:
			MDW.DaddyFinder_quick(Query_MicroSat, each_specimen, Old_algorithm=True, Trigenomic_input=False)

elif str(input) == 'APOMICTIC_TRIPLOIDS':
	#os.chdir('../files/')

	file_list = glob.glob('*')
	for file in file_list:
		os.remove(file)

	apomictic_triploid_list = MDW.RandomSearch(99, sex_diploid=False, apo_diploid=False, apo_triploid=True)		
	
	for each_specimen in apomictic_triploid_list:
		Query_MicroSat = MicroSat_dic[each_specimen]
		Query_MicroSat = MDW.AddNullAllele(Query_MicroSat)
		if args.getvalue("Full_search"):
			MDW.DaddyFinder_full(Query_MicroSat, each_specimen, Old_algorithm=False, Trigenomic_input=True)
		else:
			MDW.DaddyFinder_quick(Query_MicroSat, each_specimen, Old_algorithm=False, Trigenomic_input=True)
else:
	print "<h3>Error: ", input, "not in the database; please try again</h3>"

print(
"""
</body>
</html>
""") 



