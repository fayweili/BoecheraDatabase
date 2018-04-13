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
	<h2>TESLA: Taxon Enquiry based on Similarity of Loci and Alleles </h2>
	<form action = 'Search_database_byAllele.py'>
		<table>
		<tr>
		<td><label>I3: </label></td>
		<td><input type='text' name='I3' size='10'></td>
		<td><input type='text' name='I3' size='10'></td>
		<td><input type='text' name='I3' size='10'></td>
		<td><input type='text' name='I3' size='10'></td>
		<td><input type='text' name='I3' size='10'></td>
		<td><input type='text' name='I3' size='10'></td>
		<td><input type='text' name='I3' style="color: #bfbfbf;" size='10'></td>
		</tr>
		
		<tr>			
		<td><label>A1: </label></td>
		<td><input type='text' name='A1' size='10'></td>
		<td><input type='text' name='A1' size='10'></td>
		<td><input type='text' name='A1' size='10'></td>
		<td><input type='text' name='A1' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='A1' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='A1' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='A1' style="color: #bfbfbf;" size='10'></td>
		</tr>
		
		<tr>	
		<td><label>B20: </label></td>
		<td><input type='text' name='B20' size='10'></td>
		<td><input type='text' name='B20' size='10'></td>
		<td><input type='text' name='B20' size='10'></td>
		<td><input type='text' name='B20' size='10'></td>
		<td><input type='text' name='B20' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B20' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B20' style="color: #bfbfbf;" size='10'></td>
		</tr>
		
		<tr>	
		<td><label>B11: </label></td>
		<td><input type='text' name='B11' size='10'></td>
		<td><input type='text' name='B11' size='10'></td>
		<td><input type='text' name='B11' size='10'></td>
		<td><input type='text' name='B11' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B11' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B11' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B11' style="color: #bfbfbf;" size='10'></td>
		</tr>

		<tr>	
		<td><label>C8: </label></td>
		<td><input type='text' name='C8' size='10'></td>
		<td><input type='text' name='C8' size='10'></td>
		<td><input type='text' name='C8' size='10'></td>
		<td><input type='text' name='C8' size='10'></td>
		<td><input type='text' name='C8' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='C8' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='C8' style="color: #bfbfbf;" size='10'></td>
		</tr>
		
		<tr>	
		<td><label>I14: </label></td>
		<td><input type='text' name='I14' size='10'></td>
		<td><input type='text' name='I14' size='10'></td>
		<td><input type='text' name='I14' size='10'></td>
		<td><input type='text' name='I14' size='10'></td>
		<td><input type='text' name='I14' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='I14' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='I14' style="color: #bfbfbf;" size='10'></td>
		</tr>
		
		<tr>	
		<td><label>B9: </label></td>
		<td><input type='text' name='B9' size='10'></td>
		<td><input type='text' name='B9' size='10'></td>
		<td><input type='text' name='B9' size='10'></td>
		<td><input type='text' name='B9' size='10'></td>
		<td><input type='text' name='B9' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B9' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B9' style="color: #bfbfbf;" size='10'></td>
		</tr>

		<tr>	
		<td><label>E9: </label></td>
		<td><input type='text' name='E9' size='10'></td>
		<td><input type='text' name='E9' size='10'></td>
		<td><input type='text' name='E9' size='10'></td>
		<td><input type='text' name='E9' size='10'></td>
		<td><input type='text' name='E9' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='E9' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='E9' style="color: #bfbfbf;" size='10'></td>
		</tr>

		<tr>	
		<td><label>B18: </label></td>
		<td><input type='text' name='B18' size='10'></td>
		<td><input type='text' name='B18' size='10'></td>
		<td><input type='text' name='B18' size='10'></td>
		<td><input type='text' name='B18' size='10'></td>
		<td><input type='text' name='B18' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B18' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B18' style="color: #bfbfbf;" size='10'></td>
		</tr>

		<tr>	
		<td><label>BF3: </label></td>
		<td><input type='text' name='BF3' size='10'></td>
		<td><input type='text' name='BF3' size='10'></td>
		<td><input type='text' name='BF3' size='10'></td>
		<td><input type='text' name='BF3' size='10'></td>
		<td><input type='text' name='BF3' size='10'></td>
		<td><input type='text' name='BF3' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='BF3' style="color: #bfbfbf;" size='10'></td>
		</tr>
		
		<tr>	
		<td><label>B6: </label></td>
		<td><input type='text' name='B6' size='10'></td>
		<td><input type='text' name='B6' size='10'></td>
		<td><input type='text' name='B6' size='10'></td>
		<td><input type='text' name='B6' size='10'></td>
		<td><input type='text' name='B6' size='10'></td>
		<td><input type='text' name='B6' size='10'></td>
		<td><input type='text' name='B6' size='10'></td>
		</tr>

		<tr>	
		<td><label>BF19: </label></td>
		<td><input type='text' name='BF19' size='10'></td>
		<td><input type='text' name='BF19' size='10'></td>
		<td><input type='text' name='BF19' size='10'></td>
		<td><input type='text' name='BF19' size='10'></td>
		<td><input type='text' name='BF19' size='10'></td>
		<td><input type='text' name='BF19' size='10'></td>
		<td><input type='text' name='BF19' style="color: #bfbfbf;" size='10'></td>
		</tr>								

		<tr>	
		<td><label>BF15: </label></td>
		<td><input type='text' name='BF15' size='10'></td>
		<td><input type='text' name='BF15' size='10'></td>
		<td><input type='text' name='BF15' size='10'></td>
		<td><input type='text' name='BF15' size='10'></td>
		<td><input type='text' name='BF15' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='BF15' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='BF15' style="color: #bfbfbf;" size='10'></td>
		</tr>

		<tr>	
		<td><label>A3: </label></td>
		<td><input type='text' name='A3' size='10'></td>
		<td><input type='text' name='A3' size='10'></td>
		<td><input type='text' name='A3' size='10'></td>
		<td><input type='text' name='A3' size='10'></td>
		<td><input type='text' name='A3' size='10'></td>
		<td><input type='text' name='A3' size='10'></td>
		<td><input type='text' name='A3' style="color: #bfbfbf;" size='10'></td>
		</tr>
		
		<tr>	
		<td><label>B266: </label></td>
		<td><input type='text' name='B266' size='10'></td>
		<td><input type='text' name='B266' size='10'></td>
		<td><input type='text' name='B266' size='10'></td>
		<td><input type='text' name='B266' size='10'></td>
		<td><input type='text' name='B266' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B266' style="color: #bfbfbf;" size='10'></td>
		<td><input type='text' name='B266' style="color: #bfbfbf;" size='10'></td>
		</tr>		
		</table>		
		<br>
		<input type="checkbox" name="MatchOnlyDiploid" value="MatchOnlyDiploid">Search only sexual diploids (i.e. heterozygosity < 0.5) <br><br>	
		<button type='submit'>Enter</button><br>

	</form>
""")

args = cgi.FieldStorage(keep_blank_values=True)
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

os.chdir('files/')
for locus in Query_MicroSat:
	for number, allele in enumerate(locus):
		if allele == '':
			locus[number] = 'NA'

if args.getvalue("WeighByAlleleFreq"):
	WeighByAlleleFreq = True
else:
	WeighByAlleleFreq = False
	
if args.getvalue("MatchOnlyDiploid"):
	MatchOnlyDiploid = True
else:
	MatchOnlyDiploid = False

if WeighByAlleleFreq and not MatchOnlyDiploid:
	MDW.SpecimenMatcher(Query_MicroSat, 0, 1, 'input', SaveFile=True, WeighByAlleleFreq = True, IncompleteLoci = True)
	
elif not WeighByAlleleFreq and not MatchOnlyDiploid:
	MDW.SpecimenMatcher(Query_MicroSat, 0, 1, 'input', SaveFile=True, WeighByAlleleFreq = False, IncompleteLoci = True)

elif WeighByAlleleFreq and MatchOnlyDiploid:
	MDW.SpecimenMatcher(Query_MicroSat, 0, 0.3, 'input', SaveFile=True, WeighByAlleleFreq = True, IncompleteLoci = True)

elif not WeighByAlleleFreq and MatchOnlyDiploid:
	MDW.SpecimenMatcher(Query_MicroSat, 0, 0.3, 'input', SaveFile=True, WeighByAlleleFreq = False, IncompleteLoci = True)
			
#MDW.SpecimenMatcher(Query_MicroSat, 0, 1, 'input', AM=True, LM=True, SaveFile=True, IncompleteLoci = True)		
#print "<h3>Input:", Query_MicroSat, "</h3>"
print(
"""
</body>
</html>
""") 




