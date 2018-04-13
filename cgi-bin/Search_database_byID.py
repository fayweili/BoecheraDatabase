#!/usr/bin/env python
import cgi
import cgitb
import MDW
import os
import sys
import glob

cgitb.enable()

MicroSat_dic = MDW.MicSatDatabaseReader('Boechera_full.txt')
#MDW.SpecimenDatabaseReader('DNAextr_T29.txt')

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
	<form action = 'Search_database_byID.py'>
		<label>DNA extraction ID: </label>
		<input type='text' name='ID' size='25' placeholder=' e.g. FW1111'>
		<button type='submit'>Enter</button> <br><br>
		<input type="checkbox" name="MatchOnlyDiploid" value="MatchOnlyDiploid">Search only sexual diploids (i.e. heterozygosity < 0.5) </div>
		<br>	
	</form>
	<script type="text/javascript">
		function help_click(div, txt) { if (div.innerHTML == "") div.innerHTML = "   " + txt; else div.innerHTML = ""; }
	</script>

""")

args = cgi.FieldStorage()
try:
	input = args.getfirst("ID").upper()
except:
	sys.exit("</body></html>")
	
if input in MicroSat_dic:
	#os.chdir('../files/')
	os.chdir('files/')
	#remove old files
	file_list = glob.glob('*')
	for file in file_list:
		os.remove(file)
	
	Query_MicroSat = MicroSat_dic[input]
	heterozygosity = MDW.Heterozygosity(Query_MicroSat)
	Query_MicroSat = MDW.AddNullAllele(Query_MicroSat)
	#print Query_MicroSat

	print "<h3>Query:", input, "</h3>"
	print "<p>Heterozygosity:", heterozygosity, "</p>"
	print "<p>No. empty loci:", MDW.Heterozygosity(Query_MicroSat, Return_EmptyLoci_count=True), "</p>"

	if args.getvalue("WeighByAlleleFreq"):
		WeighByAlleleFreq = True
	else:
		WeighByAlleleFreq = False
	
	if args.getvalue("MatchOnlyDiploid"):
		MatchOnlyDiploid = True
	else:
		MatchOnlyDiploid = False

	if WeighByAlleleFreq and not MatchOnlyDiploid:
		MDW.SpecimenMatcher(Query_MicroSat, 0, 1, input, SaveFile=True, WeighByAlleleFreq = True)
	
	elif not WeighByAlleleFreq and not MatchOnlyDiploid:
		MDW.SpecimenMatcher(Query_MicroSat, 0, 1, input, SaveFile=True, WeighByAlleleFreq = False)

	elif WeighByAlleleFreq and MatchOnlyDiploid:
		MDW.SpecimenMatcher(Query_MicroSat, 0, 0.5, input, SaveFile=True, WeighByAlleleFreq = True)

	elif not WeighByAlleleFreq and MatchOnlyDiploid:
		MDW.SpecimenMatcher(Query_MicroSat, 0, 0.5, input, SaveFile=True, WeighByAlleleFreq = False)

elif str(input) == 'SEXUAL_DIPLOIDS':
	os.chdir('../files/')
	specimen_list = MDW.RandomSearch(99, sex_diploid=True, apo_diploid=False, apo_triploid=False)
	print "<h3>", specimen_list, "</h3>"
	for each_specimen in specimen_list:
		Query_MicroSat = MicroSat_dic[each_specimen]
		print "<h3>Query:", each_specimen, "</h3>"
		print "<p>Heterozygosity:", MDW.Heterozygosity(Query_MicroSat), "</p>"
		print "<p>No. empty loci:", MDW.Heterozygosity(Query_MicroSat, Return_EmptyLoci_count=True), "</p>"
		MDW.SpecimenMatcher(Query_MicroSat, 0, 1, each_specimen, SaveFile=True, WeighByAlleleFreq = False)

elif str(input) == 'APOMICTIC_DIPLOIDS':
	os.chdir('../files/')
	specimen_list = MDW.RandomSearch(99, sex_diploid=False, apo_diploid=True, apo_triploid=False)
	print "<h3>", specimen_list, "</h3>"
	for each_specimen in specimen_list:
		Query_MicroSat = MicroSat_dic[each_specimen]
		print "<h3>Query:", each_specimen, "</h3>"
		print "<p>Heterozygosity:", MDW.Heterozygosity(Query_MicroSat), "</p>"
		print "<p>No. empty loci:", MDW.Heterozygosity(Query_MicroSat, Return_EmptyLoci_count=True), "</p>"
		MDW.SpecimenMatcher(Query_MicroSat, 0, 1, each_specimen, SaveFile=True, WeighByAlleleFreq = False)

elif str(input) == 'APOMICTIC_TRIPLOIDS':
	os.chdir('../files/')
	specimen_list = MDW.RandomSearch(99, sex_diploid=False, apo_diploid=False, apo_triploid=True)
	print "<h3>", specimen_list, "</h3>"
	for each_specimen in specimen_list:
		Query_MicroSat = MicroSat_dic[each_specimen]		
		print "<h3>Query:", each_specimen, "</h3>"
		print "<p>Heterozygosity:", MDW.Heterozygosity(Query_MicroSat), "</p>"
		print "<p>No. empty loci:", MDW.Heterozygosity(Query_MicroSat, Return_EmptyLoci_count=True), "</p>"
		MDW.SpecimenMatcher(Query_MicroSat, 0, 1, each_specimen, SaveFile=True, WeighByAlleleFreq = False)

else:
	print "<h3>Error: ", input, "not in the database; please try again</h3>"
	
print(
"""
</body>
</html>
""") 