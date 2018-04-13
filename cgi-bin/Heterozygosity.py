#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

def MicSatDatabaseReader(Infile_name):
	AllData = open(Infile_name, 'rU')
	
	global AllData_dic
	AllData_dic = {} #To store all the data, using the DNA extraction numbers as keys
	global MicroSat_dic
	MicroSat_dic = {} #To store microsatellite data only, using the DNA extraction numbers as keys
	global TaxonName_dic
	TaxonName_dic = {} #To store each taxon name only, using the DNA extraction numbers as keys
	global AllOther_dic
	AllOther_dic = {} #To store other miscellaneous data, using the DNA extraction numbers as keys
	global Heterozygosity_dic
	Heterozygosity_dic = {}
	global Header
	
	#Get the header of the table
	for Header in AllData:
		Header = Header.strip('\n')
		#Header = Line 
		break #exit the for loop
	
	#Read-in the table	
	for Line in AllData:
		Line = Line.strip('\n')
		ElementList = Line.split('\t') #put data in each cell into a list
		
		#Substitute missing/blank data as 'NA'
		#ElementList[1] is the DNA extraction number
		for number, Element in enumerate(ElementList):
			if Element == '':
				ElementList[number] = 'NA'
		
		AllData_dic[ElementList[1]] = Line
		
		MicroSat_dic[ElementList[1]] = ((ElementList[7], ElementList[8], ElementList[9], ElementList[10], ElementList[11], ElementList[12]), \
		(ElementList[13], ElementList[14], ElementList[15]), \
		(ElementList[16], ElementList[17], ElementList[18], ElementList[19]), \
		(ElementList[20], ElementList[21], ElementList[22]), \
		(ElementList[23], ElementList[24], ElementList[25], ElementList[26]), \
		(ElementList[27], ElementList[28], ElementList[29], ElementList[30]), \
		(ElementList[31], ElementList[32], ElementList[33], ElementList[34]), \
		(ElementList[35], ElementList[36], ElementList[37], ElementList[38]), \
		(ElementList[39], ElementList[40], ElementList[41], ElementList[42]), \
		(ElementList[43], ElementList[44], ElementList[45], ElementList[46], ElementList[47]), \
		(ElementList[48], ElementList[49], ElementList[50], ElementList[51], ElementList[52], ElementList[53], ElementList[54]), \
		(ElementList[55], ElementList[56], ElementList[57], ElementList[58], ElementList[59], ElementList[60]), \
		(ElementList[61], ElementList[62], ElementList[63], ElementList[64]), \
		(ElementList[65], ElementList[66], ElementList[67], ElementList[68], ElementList[69], ElementList[70]), \
		(ElementList[71], ElementList[72], ElementList[73], ElementList[74]))
		
		Heterozygosity_dic[ElementList[1]] = Heterozygosity(MicroSat_dic[ElementList[1]])
		TaxonName_dic[ElementList[1]] = ElementList[3]
		AllOther_dic[ElementList[1]] = (ElementList[0], ElementList[4], ElementList[5], ElementList[6])

	AllData.close()
	return


def QueryMicSatReader(Infile_name):
	QueryData = open(Infile_name, 'rU')
	global AllQueryData_dic
	AllQueryData_dic = {} #To store all the data, using the DNA extraction numbers as keys	
	global QueryMicroSat_dic
	QueryMicroSat_dic = {} #To store microsatellite data only, using the first row as keys
	
	LineNumber = 0
	for Line in QueryData:
		if LineNumber > 0: #ignore the header line
			Line = Line.strip('\n')
			ElementList = Line.split('\t') #put data in each cell into a list
			
			#Substitute missing/blank data as 'NA'
			#ElementList[0] is the key of QueryMicroSat_dic
			for number, Element in enumerate(ElementList):
				if Element == '':
					ElementList[number] = 'NA'
			
			AllQueryData_dic[ElementList[0]] = Line
			
			QueryMicroSat_dic[ElementList[0]] = ((ElementList[1], ElementList[2], ElementList[3], ElementList[4], ElementList[5], ElementList[6]), \
			(ElementList[7], ElementList[8], ElementList[9]), \
			(ElementList[10], ElementList[11], ElementList[12], ElementList[13]), \
			(ElementList[14], ElementList[15], ElementList[16]), \
			(ElementList[17], ElementList[18], ElementList[19], ElementList[20]), \
			(ElementList[21], ElementList[22], ElementList[23], ElementList[24]), \
			(ElementList[25], ElementList[26], ElementList[27], ElementList[28]), \
			(ElementList[29], ElementList[30], ElementList[31], ElementList[32]), \
			(ElementList[33], ElementList[34], ElementList[35], ElementList[36]), \
			(ElementList[37], ElementList[38], ElementList[39], ElementList[40], ElementList[41]), \
			(ElementList[42], ElementList[43], ElementList[44], ElementList[45], ElementList[46], ElementList[47], ElementList[48]), \
			(ElementList[49], ElementList[50], ElementList[51], ElementList[52], ElementList[53], ElementList[54]), \
			(ElementList[55], ElementList[56], ElementList[57], ElementList[58]), \
			(ElementList[59], ElementList[60], ElementList[61], ElementList[62], ElementList[63], ElementList[64]), \
			(ElementList[65], ElementList[66], ElementList[67], ElementList[68]))
	
		LineNumber = LineNumber + 1
	return

def AlleleFrequency(allele, locus):
	allele = str(allele)
	allele_occurrence = 0
	Number_of_specimen = 0
	for EachSpecimen in MicroSat_dic:
		for Allele_target in MicroSat_dic[EachSpecimen][locus]:
			if str(Allele_target) == allele:
				allele_occurrence = allele_occurrence + 1
		Number_of_specimen = Number_of_specimen + 1
	return float(allele_occurrence) /Number_of_specimen

def QueryMicroSatAlleleFrequency(Query_MicroSat):
	Current_locus = 0
	Allele_Freq_list = list(Query_MicroSat)
	#print Allele_Freq_list
	for Locus in Allele_Freq_list:
		allele_position = 0
		Locus = list(Locus)
		#print Locus
		for Allele in Locus:
			if Allele != 'NA':
				Locus[allele_position] = AlleleFrequency(Allele, Current_locus)
			allele_position = allele_position + 1
		Allele_Freq_list[Current_locus] = Locus
		Current_locus = Current_locus + 1
	return Allele_Freq_list

def Heterozygosity(MicroSat):
	#MicroSat = list(MicroSat)
	Number_of_emptylocus = 0
	Number_of_homozylous_locus = 0
	for Locus in MicroSat:
		EmptyLocus = True
		Homozygous = True
		counter = 0
		for Allele in Locus:
			if Allele != 'NA':
				EmptyLocus = False
				if counter == 0:
					Homozygous = True
				elif counter > 0:
					Homozygous = False
			counter = counter + 1
		if EmptyLocus:
			Number_of_emptylocus = Number_of_emptylocus + 1
		if Homozygous:
			Number_of_homozylous_locus = Number_of_homozylous_locus + 1
			
	if Number_of_emptylocus < 15:
		heterozygosity = (15 - float(Number_of_homozylous_locus))/(15 - Number_of_emptylocus)
	elif Number_of_emptylocus == 15:
		heterozygosity = 0
	return heterozygosity

#Return 'trigenomic' if a locus has three alleles, as a list of all loci
def AlleleNumber(Microsat):
	AlleleNumber_info_list = list(Microsat)
	Current_locus = 0
	for Locus, Locus_info in zip(Microsat, AlleleNumber_info_list):
		Locus_info = list(Locus_info)
		#EmptyLocus = True
		#Homozygous = True
		Triallelic = False
		counter = 1
		for Allele in Locus:
			if Allele != 'NA':
				#EmptyLocus = False
				if counter == 0 or 1:
					Diploid = True
				if counter > 2:
					Triallelic = True
					Triploid = True
			counter = counter + 1
		if Triallelic:
			allele_position = 0
			for Allele_info in Locus_info:
				Locus_info[allele_position] = 'triallelic'
				allele_position = allele_position + 1
		AlleleNumber_info_list[Current_locus] = Locus_info
		Current_locus = Current_locus + 1
	#print AlleleNumber_info_list	
	return AlleleNumber_info_list
		
def SpecimenMatcher(Query_MicroSat, Score_threshold, Heterozygosity_threshold, Output_preflix, AM=True, LM=True, Query_from_file=False, StepwiseSubtraction=False):
	global MatchScore_dic
	MatchScore_dic = {} #to store allele matching score for each of the specimen, using the DNA extraction numbers as keys 
	global SharedLocusScore_dic
	SharedLocusScore_dic = {} #to store locus matching score for each of the specimen, using the DNA extraction numbers as keys 
	global EmptyLocus_dic
	EmptyLocus_dic = {} #to store the number of empty locus for each of the specimen, using the DNA extraction numbers as keys 
	
	Query_MicroSat_Freq = QueryMicroSatAlleleFrequency(Query_MicroSat)
	
	#Go through each specimen in the database
	for EachSpecimen in MicroSat_dic: 
		if Heterozygosity_dic[EachSpecimen] <= Heterozygosity_threshold:
			match_score = 0 #the number of identical alleles between the query and the specimen being compared with
			Number_of_sharedlocus = 0 #the number of locus that shares at least one allele with the query specimen; maximum value: 15
			Number_of_targetallele = 0 #the number of allele in each locus, of the specimen being compared with (non-query)
			Number_of_emptylocus = 0 #the number of locus that has no allele data, of the specimen being compared with (non-query)
			Current_locus = 0 #For keep tracking what locus is in
			
			#Go through each locus in each specimen and the query
			for Locus_query, Locus_target, Locus_Freq in zip(Query_MicroSat, MicroSat_dic[EachSpecimen], Query_MicroSat_Freq): 
				EmptyLocus = True
				SharedLocus = False
				for Allele_target in Locus_target:
					if Allele_target != 'NA':
						EmptyLocus = False #=this locus has at least one allele
						Number_of_targetallele = Number_of_targetallele + 1
						for Allele_query, Allele_Freq in zip(Locus_query, Locus_Freq):
							 if Allele_query != 'NA':
								if Allele_query == Allele_target: #the two share this allele
									#allele_frequency = AlleleFrequency(Allele_query, Current_locus)
									match_score = match_score + (1 - Allele_Freq)
									#print match_score, '\t',Allele_Freq
									SharedLocus = True #this locus has shared allele					
				Current_locus = Current_locus + 1
				if EmptyLocus:
					Number_of_emptylocus = Number_of_emptylocus + 1
				if SharedLocus:
					Number_of_sharedlocus = Number_of_sharedlocus + 1
			
			EmptyLocus_dic[EachSpecimen] = Number_of_emptylocus	#store how many empty loci for this specimen		
			
			SharedLocusScore_dic[EachSpecimen] = float(Number_of_sharedlocus) / 15 * (15 - Number_of_emptylocus) / 15 #store how many loci that share at least one allele, correct for the number of locus being compared
		
			if Number_of_targetallele != 0: #to avoid dividing by zero
				match_score_percent = float(match_score) / Number_of_targetallele * (15 - Number_of_emptylocus) / 15 #store how many alleles are shared in total, as percentage, correct for the number of locus being compared					
				MatchScore_dic[EachSpecimen] = match_score_percent
			elif Number_of_targetallele == 0:
				MatchScore_dic[EachSpecimen] = 0
			
	if AM: #if the allele matching report is wanted
		#OutFileName_Hit = Output_preflix + '_SearchResults_ASscore.xls' #produce the outfile name
		#OutFile_Hit = open(OutFileName_Hit, 'w')
		#OutFile_Hit.write('AS_Score' + '\t' + Header + '\n') #write the header in the outfile
		print "<h3>Specimens most similar to", Output_preflix, "based on allele similarity criterion", "(only top 5 shown):", "</h3>"
		print "<table cellspacing='10'>"
		print "<tr>"
		print "<th>DNA extraction no.</th>"
		print "<th>Species name</th>"
		print "<th>Locality</th>"
		print "<th>Allele similarity score</th>"
		print "<th>Locus similarity score</th>"
		
		'''
		if Query_from_file: #if use query from imported file, write the query microsatellite in the output file, below the header
			#OutFile_Hit.write('Query=' + Output_preflix + '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t')
			for EachLocus in QueryMicroSat_dic[EachQuery]:
				for EachAllele in EachLocus:
					if EachAllele != 'NA': #do not print 'NA', but blanks
						#OutFile_Hit.write(EachAllele + '\t')
					else:
						#OutFile_Hit.write('\t')
			#OutFile_Hit.write('\n')
			
		if StepwiseSubtraction: 
			#OutFile_Hit.write('-' + '\t' + '\t'+ Output_preflix + '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t')
			for EachLocus in Query_MicroSat:
				for EachAllele in EachLocus:
					if EachAllele != 'NA': #do not print 'NA', but blanks
						#OutFile_Hit.write(EachAllele + '\t')
					else:
						#OutFile_Hit.write('\t')
			#OutFile_Hit.write('\n')		
		'''
		number_of_hits = 0 #for printing summary to the screen
		for key in sorted(MatchScore_dic, key=MatchScore_dic.get, reverse = True): #sort the dictionary by the allele matching score
			if MatchScore_dic[key] >= Score_threshold: #print out only those that have scores larger than the threshold specified
				#OutFile_Hit.write(str(MatchScore_dic[key]) + '\t' + AllData_dic[key] + '\n')
				
				if StepwiseSubtraction:
					if number_of_hits <= 6:
						print "<tr>"
						print "<td>", key, "</td>"
						print "<td>", TaxonName_dic[key], "</td>"
						print "<td>", AllOther_dic[key][2], "</td>"
						print "<td>", MatchScore_dic[key], "</td>"
						print "<td>", SharedLocusScore_dic[key], "</td>"
						print "</tr>"
				else:
					if number_of_hits <= 6:
						print "<tr>"
						print "<td>", key, "</td>"
						print "<td>", TaxonName_dic[key], "</td>"
						print "<td>", AllOther_dic[key][2], "</td>"
						print "<td>", MatchScore_dic[key], "</td>"
						print "<td>", SharedLocusScore_dic[key], "</td>"
						image = "IMG_3049.JPG"
						print """
							<td>
							<a href="../%s" target="_blank">Image</a>
							</td>
							""" %image
						print "</tr>"
						#print "<p>&nbsp&nbsp", key, TaxonName_dic[key], AllOther_dic[key][2], MatchScore_dic[key], SharedLocusScore_dic[key]
						
				number_of_hits = number_of_hits + 1		
		print "</table>"
		#print "<p>---Results export to", OutFileName_Hit, "---", "</p>"
		#print '\n\t', '---Results export to', OutFileName_Hit + '---\n'
		#OutFile_Hit.close()
	'''
	if LM: #if the locus matching report is wanted
		OutFileName_Hit = Output_preflix + '_SearchResults_LSscore.xls'
		OutFile_Hit = open(OutFileName_Hit, 'w')
		OutFile_Hit.write('LS_Score' + '\t' + Header + '\n')
		print "<p>Specimens most similar to", Output_preflix, "based on locus similarity criterion", "(only top 5 shown):", "</p>"

		if Query_from_file: #if use query from imported file, write the query microsatellite in the output file, below the header
			OutFile_Hit.write('Query=' + Output_preflix + '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t')
			for EachLocus in QueryMicroSat_dic[EachQuery]:
				for EachAllele in EachLocus:
					if EachAllele != 'NA': #do not print 'NA', but blanks
						OutFile_Hit.write(EachAllele + '\t')
					else:
						OutFile_Hit.write('\t')
			OutFile_Hit.write('\n')
			
		if StepwiseSubtraction: 
			OutFile_Hit.write('-' + '\t' + '\t'+ Output_preflix + '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t')
			for EachLocus in Query_MicroSat:
				for EachAllele in EachLocus:
					if EachAllele != 'NA': #do not print 'NA', but blanks
						OutFile_Hit.write(EachAllele + '\t')
					else:
						OutFile_Hit.write('\t')
			OutFile_Hit.write('\n')			
			
		number_of_hits = 0 #for printing summary to the screen
		for key in sorted(SharedLocusScore_dic, key=SharedLocusScore_dic.get, reverse = True): #sort the dictionary by the locus matching score
			if SharedLocusScore_dic[key] >= Score_threshold: #print out only those that have scores larger than the threshold specified
				OutFile_Hit.write(str(SharedLocusScore_dic[key]) + '\t' + AllData_dic[key] + '\n')

				if StepwiseSubtraction:
					if number_of_hits <= 6:
						print "<p>&nbsp&nbsp", key, "     ", TaxonName_dic[key], '     ', AllOther_dic[key][2], '     ', MatchScore_dic[key], SharedLocusScore_dic[key]
				else:
					if number_of_hits <= 6:
						print "<p>&nbsp&nbsp", key, "     ", TaxonName_dic[key], '     ', AllOther_dic[key][2], '     ', MatchScore_dic[key], SharedLocusScore_dic[key]

				number_of_hits = number_of_hits + 1
		print "<p>---Results export to", OutFileName_Hit, "---", "</p>"
		OutFile_Hit.close()
		'''
	print
	return

#Make a new allele combination, through subtracting the hybrid alleles(*_hybrid)by the putative parent alleles(*_parent) -> should be another parent's allele combination	
def MicSatSubtractor(Query_MicroSat, Parent_MicroSat, AlleleNumber_info, subtract_every_locus=True):
	New_MicroSat = list(Query_MicroSat)
	locus_position = 0
	
	#AlleleNumber_info_list = AlleleNumber(Query_MicroSat)
	
	for Locus_hybrid, Locus_parent, Locus_allele_info in zip(New_MicroSat, Parent_MicroSat, AlleleNumber_info): #go through each locus in two individuals
		Locus_hybrid = list(Locus_hybrid) #convert tuple into list
		Locus_parent = list(Locus_parent)
		allele_position = 0
		
		#check whether this locus has more than 3 alleles
		EmptyLocus = True
		Homozygous = True
		Trigenomic = False
		counter = 0
		'''
		for Allele in Locus_hybrid:
			if Allele != 'NA':
				EmptyLocus = False
				if counter == 0:
					Homozygous = True
				#elif counter > 0:
				#	Homozygous = False
				elif counter > 2:
					Trigenomic = True
			counter = counter + 1
		'''
		if Locus_allele_info[0] == 'triallelic':
			Trigenomic = True
			
		if subtract_every_locus:	
			Trigenomic = True
		
		if Trigenomic:
			for Allele_hybrid in Locus_hybrid:
				if Allele_hybrid != 'NA': #skip any NA
					for Allele_parent in Locus_parent:
						if Allele_parent == Allele_hybrid: #if the two alleles are identical, replace it as NA
							Locus_hybrid[allele_position] = 'NA'
				allele_position = allele_position + 1
			
		New_MicroSat[locus_position] = Locus_hybrid
		locus_position = locus_position + 1
	#print New_MicroSat
	return New_MicroSat

'''
def	DaddyFinder(Query_MicroSat, Output_preflix):
	
	SpecimenMatcher(Query_MicroSat, 0.1, 0.3, Output_preflix, AM=True, LM=False)
	AlleleNumber_info_list = AlleleNumber(Query_MicroSat)
	OutFileName_Hit = Output_preflix + '_SearchResults_ASscore.xls'
	First_output = open(OutFileName_Hit, 'rU')
	LineNumber = 0
	for Line in First_output:
		Line = Line.strip('\n')
		ElementList = Line.split('\t')
		
		if LineNumber == 1:
			First_round_hit = ElementList[2]
			First_MicroSat = MicroSat_dic[First_round_hit]
			break
		LineNumber = LineNumber + 1
	Second_MicroSat = MicSatSubtractor(Query_MicroSat, First_MicroSat, AlleleNumber_info_list, subtract_every_locus=True)
	Output_preflix_2 = Output_preflix + '-minus-'+ First_round_hit
	SpecimenMatcher(Second_MicroSat, 0.1, 0.3, Output_preflix_2, AM=True, LM=False)
	
	OutFileName_Hit = Output_preflix_2 + '_SearchResults_ASscore.xls'
	Second_output = open(OutFileName_Hit, 'rU')
	LineNumber = 0
	for Line in Second_output:
		Line = Line.strip('\n')
		ElementList = Line.split('\t')
		
		if LineNumber == 1:
			Second_round_hit = ElementList[2]
			Third_MicroSat = MicroSat_dic[Second_round_hit]
			break
		LineNumber = LineNumber + 1
	Forth_MicroSat = MicSatSubtractor(Second_MicroSat, Third_MicroSat, AlleleNumber_info_list, subtract_every_locus=True)
	Output_preflix_3 = Output_preflix_2 + '-minus-'+ Second_round_hit
	SpecimenMatcher(Forth_MicroSat, 0.1, 0.3, Output_preflix_2 + '-minus-' + ElementList[2], AM=True, LM=False)
	
	OutFileName_Hit = Output_preflix_3 + '_SearchResults_ASscore.xls'
	Second_output = open(OutFileName_Hit, 'rU')
	LineNumber = 0
	for Line in Second_output:
		Line = Line.strip('\n')
		ElementList = Line.split('\t')
		
		if LineNumber == 1:
			Third_round_hit = ElementList[2]
			Third_MicroSat = MicroSat_dic[Second_round_hit]
			break
		LineNumber = LineNumber + 1
	
	print "<h3>", TaxonName_dic[Output_preflix], "is likely a hybrid of", TaxonName_dic[First_round_hit], "X", TaxonName_dic[Second_round_hit], "X", TaxonName_dic[Third_round_hit], "</h3>"
	return
'''

MicSatDatabaseReader('Boechera_full.txt')

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
	<h2>Heterozygosity </h2>
	<form action = 'Heterozygosity.py'>
		<label>DNA extraction ID: </label>
		<input type='text' name='ID' size='25'>
		<button type='submit'>Enter</button>
	</form>
""")

args = cgi.FieldStorage()
input = args.getfirst("ID")
Query_MicroSat = MicroSat_dic[input]
heterozygosity = Heterozygosity(Query_MicroSat)

print "<h3>Query:", input, "</h3>"
print "<p>Heterozygosity:", heterozygosity, "</p>"

print(
"""
</body>
</html>
""") 