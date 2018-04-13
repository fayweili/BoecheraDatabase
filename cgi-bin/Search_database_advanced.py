#!/usr/bin/env python
import cgi
import cgitb
import MDW
import os

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
	<h2>Search Database </h2>
	<form action = 'Search_database_byLocality.py'>
			<input type="checkbox" name="Search_locality" value="Locality"> Locality:
			<input type='text' name='Locality' size='25'> <br>
			
			<input type="checkbox" name="Search_species" value="Species"> Species:
			<input type='text' name='Species' size='25'> <br>

			<input type="checkbox" name="Search_alleles" value="Alleles"> Alleles:
	</form>
""")

args = cgi.FieldStorage(keep_blank_values=True)
Locality = args.getfirst("Locality")
Species = args.getfirst("Species")

os.chdir('files/')

Search_locality = False
Search_species = False
Search_alleles = False
if args.getvalue("Search_locality"):
	Search_locality = True
	print "<p>", Locality, "</p>"
	
if args.getvalue("Search_species"):
	Search_species = True
	print "<p>", Species, "</p>"

if args.getvalue("Search_alleles"):
	Search_alleles = True
	
	I3 = args.getlist("I3")
	A1 = args.getlist("A1")
	B20 = args.getlist("B20")
	B11 = args.getlist("B11")
	C8 = args.getlist("C8")
	I14 = args.getlist("I14")
	B9 = args.getlist("B9")
	E9 = args.getlist("E9")
	B18 = args.getlist("B18")
	BF3 = args.getlist("BF3")
	B6 = args.getlist("B6")
	BF19 = args.getlist("BF19")
	BF15 = args.getlist("BF15")
	A3 = args.getlist("A3")
	B266 = args.getlist("B266")

	Query_MicroSat = [I3, A1, B20, B11, C8, I14, B9, E9, B18, BF3, B6, BF19, BF15, A3, B266]

	for locus in Query_MicroSat:
		for number, allele in enumerate(locus):
			if allele == '':
				locus[number] = 'NA'


if Search_locality and Search_species:
	if not Search_alleles:
		MDW.SearchSpeciesLocality(Species, Locality)	
	elif Search_alleles:
		MDW.SearchAlleleSpeciesLocality(Query_MicroSat, Species, Locality)

print(
"""
</body>
</html>
""") 