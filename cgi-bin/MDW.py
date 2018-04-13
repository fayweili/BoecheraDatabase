#!/usr/bin/env python
import re
import random
def MicSatDatabaseReader(Infile_name):
	AllData = open(Infile_name, 'rU')
	
	global AllData_dic
	AllData_dic = {} #To store all the data, using the DNA extraction numbers as keys
	global MicroSat_dic
	MicroSat_dic = {} #To store microsatellite data only, using the DNA extraction numbers as keys
	global TaxonName_dic
	TaxonName_dic = {} #To store each taxon name only, using the DNA extraction numbers as keys
	global Locality_dic
	Locality_dic = {}
	global AllOther_dic
	AllOther_dic = {} #To store other miscellaneous data, using the DNA extraction numbers as keys
	global Heterozygosity_dic
	Heterozygosity_dic = {}
	global Header
	
	global Loci_list
	Loci_list = ['I3']*6 + ['A1']*3 + ['B20']*4 + ['B11']*4 + ['C8']*4 + ['I14']*4 + ['B9']*4 + ['E9']*4 + ['B18']*4 + ['BF3']*5 + ['B6']*7 + ['BF19']*6 + ['BF15']*4 + ['A3']*6 + ['B266']*4

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
		
		ElementList[1] = ElementList[1].upper()
		AllData_dic[ElementList[1]] = Line
		
		MicroSat_dic[ElementList[1]] = [[ElementList[7], ElementList[8], ElementList[9], ElementList[10], ElementList[11], ElementList[12]], \
        [ElementList[13], ElementList[14], ElementList[15]], \
        [ElementList[16], ElementList[17], ElementList[18], ElementList[19]], \
        [ElementList[20], ElementList[21], ElementList[22], ElementList[23]], \
        [ElementList[24], ElementList[25], ElementList[26], ElementList[27]], \
        [ElementList[28], ElementList[29], ElementList[30], ElementList[31]], \
        [ElementList[32], ElementList[33], ElementList[34], ElementList[35]], \
        [ElementList[36], ElementList[37], ElementList[38], ElementList[39]], \
        [ElementList[40], ElementList[41], ElementList[42], ElementList[43]], \
        [ElementList[44], ElementList[45], ElementList[46], ElementList[47], ElementList[48]], \
        [ElementList[49], ElementList[50], ElementList[51], ElementList[52], ElementList[53], ElementList[54], ElementList[55]], \
        [ElementList[56], ElementList[57], ElementList[58], ElementList[59], ElementList[60], ElementList[61]], \
        [ElementList[62], ElementList[63], ElementList[64], ElementList[65]], \
        [ElementList[66], ElementList[67], ElementList[68], ElementList[69], ElementList[70], ElementList[71]], \
        [ElementList[72], ElementList[73], ElementList[74], ElementList[75]]]		
		
		Heterozygosity_dic[ElementList[1]] = Heterozygosity(MicroSat_dic[ElementList[1]])
		TaxonName_dic[ElementList[1]] = ElementList[3]
		Locality_dic[ElementList[1]] = [ElementList[5], ElementList[6]] #[State, County]
		AllOther_dic[ElementList[1]] = (ElementList[0], ElementList[4], ElementList[5], ElementList[6])

	AllData.close()
	return MicroSat_dic


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
			(ElementList[14], ElementList[15], ElementList[16], ElementList[17]), \
			(ElementList[18], ElementList[19], ElementList[20], ElementList[21]), \
			(ElementList[22], ElementList[23], ElementList[24], ElementList[25]), \
			(ElementList[26], ElementList[27], ElementList[28], ElementList[29]), \
			(ElementList[30], ElementList[31], ElementList[32], ElementList[33]), \
			(ElementList[34], ElementList[35], ElementList[36], ElementList[37]), \
			(ElementList[38], ElementList[39], ElementList[40], ElementList[41], ElementList[42]), \
			(ElementList[43], ElementList[44], ElementList[45], ElementList[46], ElementList[47], ElementList[48], ElementList[49]), \
			(ElementList[50], ElementList[51], ElementList[52], ElementList[53], ElementList[54], ElementList[55]), \
			(ElementList[56], ElementList[57], ElementList[58], ElementList[59]), \
			(ElementList[60], ElementList[61], ElementList[62], ElementList[63], ElementList[64], ElementList[65]), \
			(ElementList[66], ElementList[67], ElementList[68], ElementList[69]))
	
		LineNumber = LineNumber + 1
	return QueryMicroSat_dic

def SpecimenDatabaseReader(Infile_name):
	AllData = open(Infile_name, 'rU')
	
	global AllSpecimenData_dic
	AllSpecimenData_dic = {} #To store all the data, using the DNA extraction numbers as keys	
	global Comments_dic
	Comments_dic = {}
		
	#Read-in the table	
	for Line in AllData:
		Line = Line.strip('\n')
		ElementList = Line.split('\t') #put data in each cell into a list
		
		#Substitute missing/blank data as 'NA'
		#ElementList[1] is the DNA extraction number
		for number, Element in enumerate(ElementList):
			if Element == '':
				ElementList[number] = 'NA'
		
		AllSpecimenData_dic[ElementList[2]] = Line
		Comments_dic[ElementList[2]] = ElementList[17]		
	AllData.close()
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
	for Locus in Allele_Freq_list:
		allele_position = 0
		Locus = list(Locus)
		for Allele in Locus:
			if Allele != 'NA':
				Locus[allele_position] = AlleleFrequency(Allele, Current_locus)
			allele_position = allele_position + 1
		Allele_Freq_list[Current_locus] = Locus
		Current_locus = Current_locus + 1
	return Allele_Freq_list

def Heterozygosity(MicroSat, Return_EmptyLoci_count = False):
	#MicroSat = list(MicroSat)
	locus_track = 1
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
		if EmptyLocus and locus_track not in [12,14]:
			Number_of_emptylocus = Number_of_emptylocus + 1
		if Homozygous and locus_track not in [12,14]:
			Number_of_homozylous_locus = Number_of_homozylous_locus + 1
		locus_track = locus_track + 1
	
	try:
		heterozygosity = (13 - float(Number_of_homozylous_locus))/(13 - Number_of_emptylocus)
	except:
		heterozygosity = 0
	if Return_EmptyLoci_count:
		return Number_of_emptylocus
	else:
		return heterozygosity

#Return 'trigenomic' if a locus has three alleles, as a list of all loci
def AlleleNumber(Microsat):
	AlleleNumber_info_list = []
	for Locus in Microsat:
		Empty_locus = True
		Monoallelic = False
		Diallelic = False
		Triallelic = False
		counter = 1
		for Allele in Locus:
			if Allele != 'NA':
				Empty_locus = False
				if counter == 1:
					Monoallelic = True
				if counter == 2:
					Diallelic = True
					Monoallelic = False
				elif counter > 2:
					Triallelic = True
					Diallelic = False
					Monoallelic = False
				counter = counter + 1
		if Triallelic:
			AlleleNumber_info_list.append('triallelic')
		elif Diallelic:
			AlleleNumber_info_list.append('diallelic')
		elif Monoallelic:
			AlleleNumber_info_list.append('monoallelic')
		elif Empty_locus:
			AlleleNumber_info_list.append('empty')
		
	return AlleleNumber_info_list

def AddNullAllele(Microsat):
	if not CheckTrigenomic(Microsat):
		return Microsat

	Microsat_nullcoded = []
	locus_track = 1
	for Locus in Microsat:
		if locus_track not in [2]:
			allele_number = len(Locus) - list(Locus).count('NA')
			#print allele_number
			if allele_number == 1:
				Locus = list(Locus)
				Locus[1] = '0'
				Locus = tuple(Locus)
				Microsat_nullcoded.append(Locus)
			else:
				Microsat_nullcoded.append(Locus)
		else:
			Microsat_nullcoded.append(Locus)

		locus_track = locus_track + 1
	return tuple(Microsat_nullcoded)

#Return 'True' if any locus has three alleles (but not 12th nor 14th loci)
def CheckTrigenomic(Microsat):
	locus_track = 1
	Trigenomic = False
	for Locus in Microsat:
		if locus_track not in [12,14]:
			allele_number = len(Locus) - list(Locus).count('NA')
			#print allele_number
			if allele_number > 2:
				Trigenomic = True
		locus_track = locus_track + 1
	return Trigenomic
		
def SpecimenMatcher(Query_MicroSat, Score_threshold, Heterozygosity_threshold, Output_preflix, Query_from_file=False, SaveFile = False, WeighByAlleleFreq = False, Display = 'web', IncompleteLoci = False):
	global MatchScore_dic
	MatchScore_dic = {} #to store allele matching score for each of the specimen, using the DNA extraction numbers as keys 
	global SharedLocusScore_dic
	SharedLocusScore_dic = {} #to store locus matching score for each of the specimen, using the DNA extraction numbers as keys 
	#global EmptyLocus_dic
	#EmptyLocus_dic = {} #to store the number of empty locus for each of the specimen, using the DNA extraction numbers as keys 
	
	#Query_MicroSat_Freq = QueryMicroSatAlleleFrequency(Query_MicroSat)
	Trigenomic = CheckTrigenomic(Query_MicroSat)

	#Go through each specimen in the database
	for EachSpecimen in MicroSat_dic: 
		if Heterozygosity_dic[EachSpecimen] <= Heterozygosity_threshold:
			match_score = 0 #the number of identical alleles between the query and the specimen being compared with
			Number_of_sharedlocus = 0 #the number of locus that shares at least one allele with the query specimen; maximum value: 15
			Number_of_targetallele = 0 #the number of allele in each locus, of the specimen being compared with (non-query)
			Number_of_emptylocus = 0 #the number of locus that has no allele data, of the specimen being compared with (non-query)
			Current_locus = 1 #For keep tracking what locus is in
			Too_few_match = False
			#Go through each locus in each specimen and the query
			for Locus_query, Locus_target in zip(Query_MicroSat, MicroSat_dic[EachSpecimen]):
				EmptyLocus = True
				SharedLocus = False
				for Allele_target in Locus_target:
					if Allele_target != 'NA':
						EmptyLocus = False #=this locus has at least one allele
						Number_of_targetallele = Number_of_targetallele + 1
						for Allele_query in Locus_query:
							 if Allele_query != 'NA':
								#if WeighByAlleleFreq: #weighted by allele's overall frequency in the dataset; rarer the allele, higher the score
									#if Allele_query == Allele_target: #the two share this allele
								#	if int(Allele_target) - 1 <= int(Allele_query) <= int(Allele_target) + 1:
										#allele_frequency = AlleleFrequency(Allele_query, Current_locus)
								#		match_score = match_score + (1 - Allele_Freq)
										#print match_score, '\t',Allele_Freq
										#SharedLocus = True #this locus has shared allele
								#else:
									#if Allele_query == Allele_target: #the two share this allele
								#if int(Allele_target) - 1 <= int(Allele_query) <= int(Allele_target) + 1:
								if Allele_target == Allele_query:
									match_score = match_score + 1
									SharedLocus = True					
									break
				if Current_locus > 15 and match_score < 4 and not IncompleteLoci:
					Too_few_match = True
					break
				Current_locus = Current_locus + 1
				if EmptyLocus:
					Number_of_emptylocus = Number_of_emptylocus + 1
				if SharedLocus:
					Number_of_sharedlocus = Number_of_sharedlocus + 1
			
			if Too_few_match:
				continue
			
			if not IncompleteLoci:
				if Heterozygosity_dic[EachSpecimen] > 0.5 and " x " in TaxonName_dic[EachSpecimen]:
					try:
						MatchScore_dic[EachSpecimen] = float(match_score) / Number_of_targetallele * (15 - Number_of_emptylocus) / 15 #store how many alleles are shared in total, as percentage, correct for the number of locus being compared	
					except:
						MatchScore_dic[EachSpecimen] = 0
				elif Heterozygosity_dic[EachSpecimen] > 0.5 and " x " not in TaxonName_dic[EachSpecimen]:
					try:
						MatchScore_dic[EachSpecimen] = float(match_score) / Number_of_targetallele * (15 - Number_of_emptylocus) / 15 #store how many alleles are shared in total, as percentage, correct for the number of locus being compared	
					except:
						MatchScore_dic[EachSpecimen] = 0

				elif Heterozygosity_dic[EachSpecimen] <= 0.5 and " x " in TaxonName_dic[EachSpecimen]:
					try:
						MatchScore_dic[EachSpecimen] = float(match_score) / Number_of_targetallele * (15 - Number_of_emptylocus) / 15 #store how many alleles are shared in total, as percentage, correct for the number of locus being compared	
					except:
						MatchScore_dic[EachSpecimen] = 0
				elif Heterozygosity_dic[EachSpecimen] <= 0.5 and " x " not in TaxonName_dic[EachSpecimen]:
					try:
						MatchScore_dic[EachSpecimen] = float(Number_of_sharedlocus) / 15 * (15 - Number_of_emptylocus) / 15 #store how many loci that share at least one allele, correct for the number of locus being compared
					except:
						MatchScore_dic[EachSpecimen] = 0

			
			else: #IncompleteLoci == True
				if Heterozygosity_dic[EachSpecimen] > 0.5 and " x " in TaxonName_dic[EachSpecimen]:
					try:
						MatchScore_dic[EachSpecimen] = float(match_score) / 15 #store how many alleles are shared in total, as percentage, correct for the number of locus being compared	
					except:
						MatchScore_dic[EachSpecimen] = 0
				elif Heterozygosity_dic[EachSpecimen] > 0.5 and " x " not in TaxonName_dic[EachSpecimen]:
					try:
						MatchScore_dic[EachSpecimen] = float(match_score) / 15 #store how many alleles are shared in total, as percentage, correct for the number of locus being compared	
					except:
						MatchScore_dic[EachSpecimen] = 0

				elif Heterozygosity_dic[EachSpecimen] <= 0.5 and " x " in TaxonName_dic[EachSpecimen]:
					try:
						MatchScore_dic[EachSpecimen] = float(match_score) / 15 #store how many alleles are shared in total, as percentage, correct for the number of locus being compared	
					except:
						MatchScore_dic[EachSpecimen] = 0
				elif Heterozygosity_dic[EachSpecimen] <= 0.5 and " x " not in TaxonName_dic[EachSpecimen]:
					try:
						MatchScore_dic[EachSpecimen] = float(Number_of_sharedlocus) / 15 #store how many loci that share at least one allele, correct for the number of locus being compared
					except:
						MatchScore_dic[EachSpecimen] = 0
		
	#Write the concise output	
	OutFileName_Hit = Output_preflix + '_SearchResults_ASscore.xls' #produce the outfile name
	OutFile_Hit = open(OutFileName_Hit, 'w')		
	Header_to_Print = '\t'.join(['AS_score', 'DNA extraction#', 'Taxon ID', 'State/Province', 'County', 'I3', 'I3', 'I3', 'I3', 'A1', 'A1', 'A1', 'B20', 'B20', 'B20', 'B20', 'B11', 'B11', 'B11', 'C8', 'C8', 'C8', 'C8', 'I14', 'I14', 'I14', 'B9', 'B9', 'B9', 'B9', 'E9', 'E9', 'E9', 'E9', 'B18', 'B18', 'B18', 'B18', 'BF3', 'BF3', 'BF3', 'BF3', 'B6', 'B6', 'B6', 'B6', 'BF19', 'BF19', 'BF19', 'BF19', 'BF19', 'BF19', 'BF15', 'BF15', 'BF15', 'BF15', 'A3', 'A3', 'A3', 'A3', 'A3', 'A3', 'B266', 'B266', 'B266', 'B266'])
	OutFile_Hit.write(Header_to_Print + '\n')

	#Write the full output, including the specimen info
	#OutFileName_Hit_Full = Output_preflix + '_SearchResults_ASscore_Full.xls' #produce the outfile name
	#OutFile_Hit_Full = open(OutFileName_Hit_Full, 'w')		
	#Header_to_Print = '\t'.join(['AS_Score', 'position', 'Extract#', 'Genus', 'Species_ID', 'Country', 'State/Province', 'County', 'Locality', 'Elevation', 'Date', 'Pheno.', 'Collector(s)', 'Coll. #', 'Vouchers', 'Pollen morphology; Chromosome number', 'Comments'] + Header.split('\t')[7:75])
	#OutFile_Hit_Full.write(Header_to_Print + '\n') #write the header in the outfile			
	if Display == 'web':		
		print "<h3>Specimens most similar to", Output_preflix, "based on allele similarity criterion", "(only top 5 shown):", "</h3>"
		print "<table cellspacing='10'>"
		print "<tr>"
		print "<th>DNA extraction no.</th>"
		print "<th>Species name</th>"
		print "<th>Locality</th>"
		print "<th>Allele similarity score</th>"
		#print "<th>Locus similarity score</th>"
		print "<th>Image</th>"
		for locus_name in Loci_list:
			print "<th>", locus_name, "</th>"	
		print "<tr>"
		print "<td>Query:", Output_preflix, "</td>"
		if Output_preflix in MicroSat_dic:
			print "<td>", TaxonName_dic[Output_preflix], "</td>"
			print "<td>", AllOther_dic[Output_preflix][2], "</td>"
			print "<td>", "</td>"
			#print "<td>", "</td>"
			image = "IMG_3049.JPG"
			print """
				<td>
				<a href="../%s" target="_blank">Image</a>
				</td>
				""" %image		
		else:
			print "<td>", "</td>"
			print "<td>", "</td>"
			print "<td>", "</td>"
			print "<td>", "</td>"
		
		for Locus in Query_MicroSat:
			for Allele in Locus:
				if Allele == 'NA':
					print "<td>", "-", "</td>"
				else:	
					print "<td>", Allele, "</td>"
		print "</tr>"
	
	#if Query_from_file: #if use query from imported file, write the query microsatellite in the output file, below the header
	#	OutFile_Hit.write('Query=' + Output_preflix + '\t-'+ '\t-'+ '\t-'+ '\t-'+ '\t')
	#	for EachLocus in Query_MicroSat:
	#		for EachAllele in EachLocus:
	#			if EachAllele != 'NA': #do not print 'NA', but blanks
	#				OutFile_Hit.write(EachAllele + '\t')
	#			else:
	#				OutFile_Hit.write('\t')
	#	OutFile_Hit.write('\n')
	#else:
	if 'minus' not in Output_preflix: # when in daddyfinder
		try:
			# write the query
			OutFile_Hit.write('-' + '\tQuery=' + AllData_dic[Output_preflix].split('\t')[1] + '\t' + AllData_dic[Output_preflix].split('\t')[3] + '\t' + '\t'.join(AllData_dic[Output_preflix].split('\t')[5:7]) + '\t' + \
				'\t'.join(Query_MicroSat[0][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[1][0:3]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[2][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[3][0:3]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[4][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[5][0:3]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[6][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[7][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[8][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[9][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[10][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[11][0:6]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[12][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[13][0:6]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[14][0:4]).replace('NA', '') + '\t' + \
				'\n')
		except:
			OutFile_Hit.write('-' + '\tQuery=' + '\t' + '\t' + '\t' + '\t' + \
				'\t'.join(Query_MicroSat[0][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[1][0:3]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[2][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[3][0:3]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[4][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[5][0:3]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[6][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[7][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[8][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[9][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[10][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[11][0:6]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[12][0:4]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[13][0:6]).replace('NA', '') + '\t' + \
				'\t'.join(Query_MicroSat[14][0:4]).replace('NA', '') + '\t' + \
				'\n')

				#'\t'.join(AllData_dic[Output_preflix].split('\t')[5:11]) + '\t' + '\t'.join(AllData_dic[Output_preflix].split('\t')[13:23]) + '\t' + '\t'.join(AllData_dic[Output_preflix].split('\t')[24:31]) + '\t' + '\t'.join(AllData_dic[Output_preflix].split('\t')[32:48]) + '\t' + '\t'.join(AllData_dic[Output_preflix].split('\t')[49:53]) + '\t' + '\t'.join(AllData_dic[Output_preflix].split('\t')[56:76]) + '\n')
	
	number_of_hits = 0 #for printing summary to the screen
	number_of_hits_file = 0 #for saving summary to the file 
	for key in sorted(MatchScore_dic, key=MatchScore_dic.get, reverse = True): #sort the dictionary by the allele matching score
		if MatchScore_dic[key] >= Score_threshold and key != Output_preflix: #print out only those that have scores larger than the threshold specified, and do not print the query itself
			if SaveFile and number_of_hits_file < 100:
				#Write the concise output
				#to_print = '\t'.join(AllData_dic[key].split('\t')[1] + str(AllData_dic[key].split('\t')[3:10]) + str(AllData_dic[key].split('\t')[13:22]) + str(AllData_dic[key].split('\t')[24:30]) + str(AllData_dic[key].split('\t')[32:47]) + str(AllData_dic[key].split('\t')[49:52]) + str(AllData_dic[key].split('\t')[56:75]))
				#OutFile_Hit.write(str(MatchScore_dic[key]) + '\t' + to_print + '\n')
				#OutFile_Hit.write("%.4f" % MatchScore_dic[key] + '\t' + "%.4f" % SharedLocusScore_dic[key] + '\t' + AllData_dic[key].split('\t')[1] + '\t' + AllData_dic[key].split('\t')[3] + '\t' + '\t'.join(AllData_dic[key].split('\t')[5:11]) + '\t' + '\t'.join(AllData_dic[key].split('\t')[13:23]) + '\t' + '\t'.join(AllData_dic[key].split('\t')[24:31]) + '\t' + '\t'.join(AllData_dic[key].split('\t')[32:48]) + '\t' + '\t'.join(AllData_dic[key].split('\t')[49:53]) + '\t' + '\t'.join(AllData_dic[key].split('\t')[56:76]) + '\n')
				OutFile_Hit.write("%.4f" % MatchScore_dic[key] + '\t' + AllData_dic[key].split('\t')[1] + '\t' + AllData_dic[key].split('\t')[3] + '\t' + '\t'.join(AllData_dic[key].split('\t')[5:11]) + '\t' + '\t'.join(AllData_dic[key].split('\t')[13:23]) + '\t' + '\t'.join(AllData_dic[key].split('\t')[24:31]) + '\t' + '\t'.join(AllData_dic[key].split('\t')[32:48]) + '\t' + '\t'.join(AllData_dic[key].split('\t')[49:53]) + '\t' + '\t'.join(AllData_dic[key].split('\t')[56:76]) + '\n')
				#Write the full output, including the specimen info
				#if key in AllSpecimenData_dic: #if this specimen is in the SpecimenDatabase
				#	Full_to_Print1 = '\t'.join(AllData_dic[key].split('\t')[0:7])
				#	Full_to_Print2 = '\t'.join(AllData_dic[key].split('\t')[7:75])
				#	Specimen_to_Print = '\t'.join(AllSpecimenData_dic[key].split('\t')[6:14] + [Comments_dic[key]])
					#OutFile_Hit_Full.write(str(MatchScore_dic[key]) + '\t' + Full_to_Print1 + '\t' + Specimen_to_Print + '\t' + Full_to_Print2 + '\n')
				#else:
				#	Full_to_Print1 = '\t'.join(AllData_dic[key].split('\t')[0:7])
				#	Full_to_Print2 = '\t'.join(AllData_dic[key].split('\t')[7:75])
					#OutFile_Hit_Full.write(str(MatchScore_dic[key]) + '\t' + Full_to_Print1 + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + Full_to_Print2 + '\n')
				number_of_hits_file = number_of_hits_file + 1

			if number_of_hits <= 6:
				if Display == 'web':
					print "<tr>"
					print "<td>", key, "</td>"
					print "<td>", TaxonName_dic[key], "</td>"
					print "<td>", AllOther_dic[key][2], "</td>"
					print "<td>", MatchScore_dic[key], "</td>"
					#print "<td>", SharedLocusScore_dic[key], "</td>"
					image = "IMG_3049.JPG"
					print """
						<td>
						<a href="../%s" target="_blank">Image</a>
						</td>
						""" %image
					for Locus in MicroSat_dic[key]:
						for Allele in Locus:
							if Allele == 'NA':
								print "<td>", "-", "</td>"
							else:	
								print "<td>", Allele, "</td>"
					
					print "</tr>"
					#print "<p>&nbsp&nbsp", key, TaxonName_dic[key], AllOther_dic[key][2], MatchScore_dic[key], SharedLocusScore_dic[key]
						
				number_of_hits = number_of_hits + 1		
	print "</table>"
	print "<form>"
	if Display == 'web':		
		print """
		<input type='button' value='Download report' onClick="window.location.href='http://sites.biology.duke.edu/windhamlab/files/%s'">""" %OutFileName_Hit
		print "</form>"
	OutFile_Hit.close()

	#print """
	#<input type='button' value='Download full report' onClick="window.location.href='http://sites.biology.duke.edu/windhamlab/files/%s'">""" %OutFileName_Hit_Full
	#print "<p>---Results export to", OutFileName_Hit, "---", "</p>"
	#print '\n\t', '---Results export to', OutFileName_Hit + '---\n'
	#OutFile_Hit_Full.close()

	return MatchScore_dic

#Make a new allele combination, through subtracting the hybrid alleles(*_hybrid)by the putative parent alleles(*_parent) -> should be another parent's allele combination	
def MicSatSubtractor(Query_MicroSat, Parent_MicroSat, subtract_every_locus=False, subtract_diallelic_locus=False):
	New_MicroSat = list(Query_MicroSat)
	AlleleNumber_info = AlleleNumber(Query_MicroSat)
	locus_position = 0
		
	for Locus_hybrid, Locus_parent, Locus_allele_info in zip(New_MicroSat, Parent_MicroSat, AlleleNumber_info): #go through each locus in two individuals
		Locus_hybrid = list(Locus_hybrid) #convert tuple into list
		Locus_parent = list(Locus_parent)
		allele_position = 0
		
		#check whether subtraction should be carried out:
		#monoallelic locus will not be subtracted
		#diallelic locus will be subtracted only if subtract_diallelic_locus=True, or subtract_every_locus=True
		#triallelic locus will be subtracted regardless
		
		Subtract_switch = False
		if Locus_allele_info == 'diallelic' and subtract_diallelic_locus:
			Subtract_switch = True
		elif Locus_allele_info == 'triallelic':
			Subtract_switch = True
		elif Locus_allele_info != 'monoallelic' and subtract_every_locus:
			Subtract_switch = True
			
		if Subtract_switch:
			for Allele_hybrid in Locus_hybrid:
				if Allele_hybrid != 'NA': #skip any NA
					for Allele_parent in Locus_parent:
						if Allele_hybrid == Allele_parent: #if the two alleles are identical, replace it as NA
							Locus_hybrid[allele_position] = 'NA'
				allele_position = allele_position + 1
			
		New_MicroSat[locus_position] = Locus_hybrid
		locus_position = locus_position + 1
	return New_MicroSat


def	DaddyFinder_full(Query_MicroSat, Output_preflix, Old_algorithm=False, Trigenomic_input=True):
	#print "<h3>Identifying the first putative parent...</h3>"
	#print "<h3>Query:", Output_preflix, "</h3>"
	#print "<h3>Heterozygosity:", Heterozygosity(Query_MicroSat), "</h3>"
	#print "<h3>No. empty loci:", Heterozygosity(Query_MicroSat, Return_EmptyLoci_count=True), "</h3>"

	Cumulative_AS_dict = {}
	SpecimenMatcher(Query_MicroSat, 0.2, 0.4, Output_preflix, SaveFile=True, Display='no')
	
	#AlleleNumber_info_list = AlleleNumber(Query_MicroSat)
	OutFileName_Hit = Output_preflix + '_SearchResults_ASscore.xls'
	First_output = open(OutFileName_Hit, 'rU')
	LineNumber = 0
	previous_AS = 0
	equalAS = False	
	First_round_hit_dict = {}
	for Line in First_output:
		Line = Line.strip('\n')
		ElementList = Line.split('\t')
		
		if LineNumber >= 2:
			if ElementList[0] == previous_AS:
				equalAS = True
			else:
				equalAS = False
			
			if LineNumber > 5 and not equalAS:
				break
			else:
				First_round_hit_dict[ElementList[1].upper()] = float(ElementList[0])
			
			previous_AS = ElementList[0]	 	
		LineNumber = LineNumber + 1
	for First_round_hit in sorted(First_round_hit_dict, key=First_round_hit_dict.get, reverse=True):
		#print "<h3>Using ", First_round_hit, " as the first putative parent for identifying the second...</h3>"	
		First_MicroSat = MicroSat_dic[First_round_hit]		
		if Old_algorithm:
			Second_MicroSat = MicSatSubtractor(Query_MicroSat, First_MicroSat, subtract_every_locus=True)
		else:
			Second_MicroSat = MicSatSubtractor(Query_MicroSat, First_MicroSat, subtract_every_locus=False, subtract_diallelic_locus=False)		
		Output_preflix_2 = Output_preflix + '-minus-'+ First_round_hit
	
		SpecimenMatcher(Second_MicroSat, 0.2, 0.4, Output_preflix_2, SaveFile=True, Display='no')
	
		OutFileName_Hit = Output_preflix_2 + '_SearchResults_ASscore.xls'
		Second_output = open(OutFileName_Hit, 'rU')
		LineNumber = 0
		previous_AS = 0
		equalAS = False
		Second_round_hit_dict = {}
		for Line in Second_output:
			Line = Line.strip('\n')
			ElementList = Line.split('\t')
			if LineNumber >= 1:
				if ElementList[0] == previous_AS:
					equalAS = True
				else:
					equalAS = False
				
				if LineNumber > 5 and not equalAS:
					break
				else:
					Second_round_hit_dict[ElementList[1].upper()] = float(ElementList[0])
				
				previous_AS = ElementList[0]	 	
			LineNumber = LineNumber + 1
		for Second_round_hit in sorted(Second_round_hit_dict, key=Second_round_hit_dict.get, reverse=True):
			#print "<h3>Using ", Second_round_hit, " as the second putative parent for identifying the third...</h3>"
			
			if not Trigenomic_input:
				Cumulative_AS = Second_round_hit_dict[Second_round_hit] + First_round_hit_dict[First_round_hit]
				Cumulative_AS_dict[(First_round_hit, Second_round_hit)] = [Cumulative_AS, First_round_hit_dict[First_round_hit], Second_round_hit_dict[Second_round_hit]]
				break

			Third_MicroSat = MicroSat_dic[Second_round_hit]
			if Old_algorithm:
				Forth_MicroSat = MicSatSubtractor(Second_MicroSat, Third_MicroSat, subtract_every_locus=True)
			else:
				Forth_MicroSat = MicSatSubtractor(Second_MicroSat, Third_MicroSat, subtract_every_locus=False, subtract_diallelic_locus=True)
			Output_preflix_3 = Output_preflix_2 + '-minus-'+ Second_round_hit
			SpecimenMatcher(Forth_MicroSat, 0.1, 0.4, Output_preflix_2 + '-minus-' + Second_round_hit, SaveFile=True, Display='no')
	
			OutFileName_Hit = Output_preflix_3 + '_SearchResults_ASscore.xls'
			Third_output = open(OutFileName_Hit, 'rU')
			LineNumber = 0
			for Line in Third_output:
				Line = Line.strip('\n')
				ElementList = Line.split('\t')
				if LineNumber >= 1:
					if ElementList[0] == previous_AS:
						equalAS = True
					else:
						equalAS = False
					if LineNumber > 1 and not equalAS:
						break
					else:		
						Third_round_hit = ElementList[1].upper()
						Cumulative_AS = float(ElementList[0]) + Second_round_hit_dict[Second_round_hit] + First_round_hit_dict[First_round_hit]
						Cumulative_AS_dict[(First_round_hit, Second_round_hit, Third_round_hit)] = [Cumulative_AS, First_round_hit_dict[First_round_hit], Second_round_hit_dict[Second_round_hit], float(ElementList[0])]
						Third_MicroSat = MicroSat_dic[Third_round_hit]
					previous_AS = ElementList[0]
				LineNumber = LineNumber + 1
			#print "<h3>Cumulative AS: ", Cumulative_AS, "</h3>"
			#print "<h3>", TaxonName_dic[Output_preflix], "is likely a hybrid of", TaxonName_dic[First_round_hit], "X", TaxonName_dic[Second_round_hit], "X", TaxonName_dic[Third_round_hit], "</h3>"
			#print "<br>"
	#print Cumulative_AS_dict
	#print "<h3>Report</h3>"
	if not Trigenomic_input:
		print "<table cellspacing='10'>"
		print "<tr>"
		print "<th>Cumulative score</th>"
		print "<th>Putative parent 1</th>"
		print "<th>Allele similarity score </th>"
		print "<th>Putative parent 2</th>"
		print "<th>Allele similarity score </th>"
		print "</tr>"
		for each_combination in sorted(Cumulative_AS_dict, key=Cumulative_AS_dict.get, reverse=True):			
			print "<tr>"
			print "<td>", Cumulative_AS_dict[each_combination][0], "</td>"
			print "<td>", TaxonName_dic[each_combination[0]], "(" + str(each_combination[0]) + ")", "</td>"
			print "<td>", str(Cumulative_AS_dict[each_combination][1]), "</td>"
			print "<td>", TaxonName_dic[each_combination[1]], "(" + str(each_combination[1]) + ")", "</td>"
			print "<td>", str(Cumulative_AS_dict[each_combination][2]), "</td>"
			print "</tr>"
		print "</table>"	
		return

	print "<table cellspacing='10'>"
	print "<tr>"
	print "<th>Cumulative score</th>"
	print "<th>Putative parent 1</th>"
	print "<th>Allele similarity score </th>"
	print "<th>Putative parent 2</th>"
	print "<th>Allele similarity score </th>"
	print "<th>Putative parent 3</th>"
	print "<th>Allele similarity score </th>"
	print "</tr>"
	for each_combination in sorted(Cumulative_AS_dict, key=Cumulative_AS_dict.get, reverse=True):
	
		print "<tr>"
		print "<td>", Cumulative_AS_dict[each_combination][0], "</td>"
		print "<td>", TaxonName_dic[each_combination[0]], "(" + str(each_combination[0]) + ")", "</td>"
		print "<td>", str(Cumulative_AS_dict[each_combination][1]), "</td>"
		print "<td>", TaxonName_dic[each_combination[1]], "(" + str(each_combination[1]) + ")", "</td>"
		print "<td>", str(Cumulative_AS_dict[each_combination][2]), "</td>"
		print "<td>", TaxonName_dic[each_combination[2]], "(" + str(each_combination[2]) + ")", "</td>"
		print "<td>", str(Cumulative_AS_dict[each_combination][3]), "</td>"		
		print "</tr>"
	print "</table>"	
		
	return

def	DaddyFinder_quick(Query_MicroSat, Output_preflix, Old_algorithm=False, Trigenomic_input=True):
	#print "<h3>Query:", Output_preflix, "</h3>"
	print "<h3>Heterozygosity:", Heterozygosity(Query_MicroSat), "</h3>"
	print "<h3>No. empty loci:", Heterozygosity(Query_MicroSat, Return_EmptyLoci_count=True), "</h3>"	
	SpecimenMatcher(Query_MicroSat, 0.1, 0.4, Output_preflix, SaveFile=True)
	#AlleleNumber_info_list = AlleleNumber(Query_MicroSat)
	OutFileName_Hit = Output_preflix + '_SearchResults_ASscore.xls'
	First_output = open(OutFileName_Hit, 'rU')
	LineNumber = 0
	Hit = False
	for Line in First_output:
		Line = Line.strip('\n')
		ElementList = Line.split('\t')
		if LineNumber == 2:
			First_round_hit = ElementList[1].upper()
			First_MicroSat = MicroSat_dic[First_round_hit]
			Hit = True
			break
		LineNumber = LineNumber + 1
	if Hit:
		if Old_algorithm:
			Second_MicroSat = MicSatSubtractor(Query_MicroSat, First_MicroSat, subtract_every_locus=True)
		else:
			Second_MicroSat = MicSatSubtractor(Query_MicroSat, First_MicroSat, subtract_every_locus=False, subtract_diallelic_locus=False)		
	else:
		print "<h3> No hit </h3>"
		return
	Output_preflix_2 = Output_preflix + '-minus-'+ First_round_hit
	SpecimenMatcher(Second_MicroSat, 0.1, 0.4, Output_preflix_2, SaveFile=True)
	
	OutFileName_Hit = Output_preflix_2 + '_SearchResults_ASscore.xls'
	Second_output = open(OutFileName_Hit, 'rU')
	LineNumber = 0
	for Line in Second_output:
		Line = Line.strip('\n')
		ElementList = Line.split('\t')
		
		if LineNumber == 1:
			Second_round_hit = ElementList[1].upper()
			Third_MicroSat = MicroSat_dic[Second_round_hit]
			break
		LineNumber = LineNumber + 1

	if not Trigenomic_input:
		try:
			print "<h3>", Output_preflix, "is likely a hybrid of", TaxonName_dic[First_round_hit], "X", TaxonName_dic[Second_round_hit], "</h3>"
		except:
			print "<h3>", Output_preflix, "is likely a hybrid of", TaxonName_dic[First_round_hit], "X", "???", "</h3>"			
		return

	if Old_algorithm:
		Forth_MicroSat = MicSatSubtractor(Second_MicroSat, Third_MicroSat, subtract_every_locus=True)
	else:
		Forth_MicroSat = MicSatSubtractor(Second_MicroSat, Third_MicroSat, subtract_every_locus=False, subtract_diallelic_locus=True)
	Output_preflix_3 = Output_preflix_2 + '-minus-'+ Second_round_hit
	SpecimenMatcher(Forth_MicroSat, 0.1, 0.4, Output_preflix_2 + '-minus-' + ElementList[1], SaveFile=True)
	
	OutFileName_Hit = Output_preflix_3 + '_SearchResults_ASscore.xls'
	Second_output = open(OutFileName_Hit, 'rU')
	LineNumber = 0
	for Line in Second_output:
		Line = Line.strip('\n')
		ElementList = Line.split('\t')
		
		if LineNumber == 1:
			Third_round_hit = ElementList[1].upper()
			Third_MicroSat = MicroSat_dic[Second_round_hit]
			break
		LineNumber = LineNumber + 1
	
	try:
		test = TaxonName_dic[Third_round_hit]
		print "<h3>", Output_preflix, "is likely a hybrid of", TaxonName_dic[First_round_hit], "X", TaxonName_dic[Second_round_hit], "X", TaxonName_dic[Third_round_hit], "</h3>"
	except:
		print "<h3>", Output_preflix, "is likely a hybrid of", TaxonName_dic[First_round_hit], "X", TaxonName_dic[Second_round_hit], "X", "???", "</h3>"		
	return
	
def SearchSpecies(Query_species, MatchOnlyDiploid=False, MatchOnlyApomict=False):

	Query_species = Query_species.replace('boechera ', '').replace('Boechera ', '')
	OutFileName = Query_species + '_SearchResults.xls' #produce the outfile name
	OutFile = open(OutFileName, 'w')		
	OutFile.write(Header + '\n') #write the header in the outfile
				
	print "<table cellspacing='10'>"
	print "<tr>"
	print "<th>DNA extraction no.</th>"
	print "<th>Species name</th>"
	print "<th>Locality</th>"
	for locus_name in Loci_list:
		print "<th>", locus_name, "</th>"
	
	for EachSpecimen in sorted(TaxonName_dic.iterkeys()):
		SpecimenName = TaxonName_dic[EachSpecimen].upper()
		if MatchOnlyDiploid and ' X ' in SpecimenName:
			continue
		if MatchOnlyApomict and not ' X ' in SpecimenName:
			continue
		SpecimenName = SpecimenName.replace('"', '').replace(' ', '').replace('!', '').replace(' X ', '')		
		Match = re.search(Query_species.upper(), SpecimenName)
		if Match:
			print "<tr>"
			print "<td>", EachSpecimen, "</td>"
			print "<td>", TaxonName_dic[EachSpecimen], "</td>"
			print "<td>", AllOther_dic[EachSpecimen][2], "</td>"
			for Locus in MicroSat_dic[EachSpecimen]:
				for Allele in Locus:
					if Allele == 'NA':
						print "<td>", "-", "</td>"
					else:	
						print "<td>", Allele, "</td>"
			print "</tr>"
			OutFile.write(AllData_dic[EachSpecimen] + '\n')
	print "</table>"
	OutFile.close()
	
	print "<form>"
	print """
	<input type='button' value='Download full report' onClick="window.location.href='http://sites.biology.duke.edu/windhamlab/files/%s'">""" %OutFileName
	print "</form>"
		
	return
	
def SearchLocality(Query_locality, MatchOnlyDiploid=False, MatchOnlyApomict=False):
	
	OutFileName = Query_locality + '_SearchResults.xls' #produce the outfile name
	OutFile = open(OutFileName, 'w')		
	OutFile.write(Header + '\n') #write the header in the outfile
				
	print "<table cellspacing='10'>"
	print "<tr>"
	print "<th>DNA extraction no.</th>"
	print "<th>Species name</th>"
	print "<th>Locality</th>"
	for locus_name in Loci_list:
		print "<th>", locus_name, "</th>"
	
	for EachSpecimen in sorted(TaxonName_dic, key=TaxonName_dic.get):
		SpecimenName = TaxonName_dic[EachSpecimen].upper()
		if MatchOnlyDiploid and ' X ' in SpecimenName:
			continue
		if MatchOnlyApomict and not ' X ' in SpecimenName:
			continue

		if Locality_dic[EachSpecimen][0].upper() == Query_locality.upper() or Locality_dic[EachSpecimen][1].upper() == Query_locality.upper():
			print "<tr>"
			print "<td>", EachSpecimen, "</td>"
			print "<td>", TaxonName_dic[EachSpecimen], "</td>"
			print "<td>", AllOther_dic[EachSpecimen][2], "</td>"
			for Locus in MicroSat_dic[EachSpecimen]:
				for Allele in Locus:
					if Allele == 'NA':
						print "<td>", "-", "</td>"
					else:	
						print "<td>", Allele, "</td>"
			print "</tr>"
			OutFile.write(AllData_dic[EachSpecimen] + '\n')
	print "</table>"
	OutFile.close()
	
	print "<form>"
	print """
	<input type='button' value='Download report' onClick="window.location.href='http://sites.biology.duke.edu/windhamlab/files/%s'">""" %OutFileName
	print "</form>"
		
	return	
	
def SearchSpeciesLocality(Query_species, Query_locality):

	Query_species = Query_species.replace('boechera ', '').replace('Boechera ', '')
	OutFileName = Query_species + '_SearchResults.xls' #produce the outfile name
	OutFile = open(OutFileName, 'w')		
	OutFile.write(Header + '\n') #write the header in the outfile
				
	print "<table cellspacing='10'>"
	print "<tr>"
	print "<th>DNA extraction no.</th>"
	print "<th>Species name</th>"
	print "<th>Locality</th>"
	for locus_name in Loci_list:
		print "<th>", locus_name, "</th>"
	
	for EachSpecimen in sorted(TaxonName_dic.iterkeys()):
		SpecimenName = TaxonName_dic[EachSpecimen].upper()
		SpecimenName = SpecimenName.replace('"', '').replace(' ', '').replace('!', '').replace(' X ', '')
		
		Match = re.search(Query_species.upper(), SpecimenName)
		if Match:
			if Locality_dic[EachSpecimen][0].upper() == Query_locality.upper() or Locality_dic[EachSpecimen][1].upper() == Query_locality.upper():

				print "<tr>"
				print "<td>", EachSpecimen, "</td>"
				print "<td>", TaxonName_dic[EachSpecimen], "</td>"
				print "<td>", AllOther_dic[EachSpecimen][2], "</td>"
				for Locus in MicroSat_dic[EachSpecimen]:
					for Allele in Locus:
						if Allele == 'NA':
							print "<td>", "-", "</td>"
						else:	
							print "<td>", Allele, "</td>"
				print "</tr>"
				OutFile.write(AllData_dic[EachSpecimen] + '\n')
	print "</table>"
	OutFile.close()
	
	print "<form>"
	print """
	<input type='button' value='Download report' onClick="window.location.href='http://sites.biology.duke.edu/windhamlab/files/%s'">""" %OutFileName
	print "</form>"
		
	return

def RandomSearch(sample_number, sex_diploid=True, apo_diploid=False, apo_triploid=False):	
	specimen_list = []
	i = 0
	if sex_diploid:
		while i <= int(sample_number):
			random_specimen = random.choice(MicroSat_dic.keys())
			if Heterozygosity(MicroSat_dic[random_specimen]) < 0.5 and not CheckTrigenomic(MicroSat_dic[random_specimen]):
				specimen_list.append(random_specimen)
				i = i + 1
		return specimen_list
	elif apo_diploid:
		while i <= int(sample_number):
			random_specimen = random.choice(MicroSat_dic.keys())
			if Heterozygosity(MicroSat_dic[random_specimen]) >= 0.5 and not CheckTrigenomic(MicroSat_dic[random_specimen]):
				specimen_list.append(random_specimen)
				i = i + 1
		return specimen_list
	elif apo_triploid:
		while i <= int(sample_number):
			random_specimen = random.choice(MicroSat_dic.keys())
			if Heterozygosity(MicroSat_dic[random_specimen]) >= 0.5 and CheckTrigenomic(MicroSat_dic[random_specimen]):
				specimen_list.append(random_specimen)
				i = i + 1
		return specimen_list



### Dev ###	
def SearchAlleleSpeciesLocality(Query_MicroSat, Query_species, Query_locality):
	MatchScore_dic = SpecimenMatcher(Query_MicroSat, 0.01, 1, 'input', SaveFile=True, WeighByAlleleFreq = False)

	#Write the concise output	
	OutFileName_Hit = 'input' + '_SearchResults_ASscore.xls' #produce the outfile name
	OutFile_Hit = open(OutFileName_Hit, 'w')		
	OutFile_Hit.write('AS_Score' + '\t' + Header + '\n') #write the header in the outfile
	
	#Write the full output, including the specimen info
	#OutFileName_Hit_Full = 'input' + '_SearchResults_ASscore_Full.xls' #produce the outfile name
	#OutFile_Hit_Full = open(OutFileName_Hit_Full, 'w')		
	
	Header_to_Print = '\t'.join(['AS_Score', 'position', 'Genus', 'taxon ID', 'Extract#', 'Country', 'State/Province', 'County', 'Locality', 'Elevation', 'Date', 'Pheno.', 'Collector(s)', 'Coll. #', 'Vouchers', 'Pollen morphology; Chromosome number', 'Comments'] + Header.split('\t')[7:75])
	#OutFile_Hit_Full.write(Header_to_Print + '\n') #write the header in the outfile			
			
	print "<h3>Specimens most similar to", 'input', "based on allele similarity criterion", "(only top 5 shown):", "</h3>"
	print "<table cellspacing='10'>"
	print "<tr>"
	print "<th>DNA extraction no.</th>"
	print "<th>Species name</th>"
	print "<th>Locality</th>"
	print "<th>Allele similarity score</th>"
	print "<th>Locus similarity score</th>"
	print "<th>Image</th>"
	for locus_name in Loci_list:
		print "<th>", locus_name, "</th>"
		
	number_of_hits = 0 #for printing summary to the screen
	for key in sorted(MatchScore_dic, key=MatchScore_dic.get, reverse = True): #sort the dictionary by the allele matching score
		if MatchScore_dic[key] >= 0.01: #print out only those that have scores larger than the threshold specified
			
			SpecimenName = TaxonName_dic[key].upper()
			SpecimenName = SpecimenName.replace('"', '').replace(' ', '').replace('!', '').replace('X', '')			
			Match = re.search(Query_species.upper(), SpecimenName)

			if Match:
				if Locality_dic[key][0].upper() == Query_locality.upper() or Locality_dic[key][1].upper() == Query_locality.upper():
			
					#Write the concise output
					OutFile_Hit.write(str(MatchScore_dic[key]) + '\t' + AllData_dic[key] + '\n')
			
					#Write the full output, including the specimen info
					#if key in AllSpecimenData_dic: #if this specimen is in the SpecimenDatabase
					#	Full_to_Print1 = '\t'.join(AllData_dic[key].split('\t')[0:1])
					#	Full_to_Print2 = '\t'.join(AllData_dic[key].split('\t')[7:75])
					#	Specimen_to_Print = '\t'.join(AllSpecimenData_dic[key].split('\t')[0:14] + [Comments_dic[key]])
					#	OutFile_Hit_Full.write(str(MatchScore_dic[key]) + '\t' + Full_to_Print1 + '\t' + Specimen_to_Print + '\t' + Full_to_Print2 + '\n')
					#else:
					#	Full_to_Print1 = '\t'.join(AllData_dic[key].split('\t')[0:1] + AllData_dic[key].split('\t')[2:4] + AllData_dic[key].split('\t')[1:2] + AllData_dic[key].split('\t')[4:6])
					#	Full_to_Print2 = '\t'.join(AllData_dic[key].split('\t')[7:75])
					#	OutFile_Hit_Full.write(str(MatchScore_dic[key]) + '\t' + Full_to_Print1 + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + Full_to_Print2 + '\n')
				
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
						for Locus in MicroSat_dic[key]:
							for Allele in Locus:
								if Allele == 'NA':
									print "<td>", "-", "</td>"
								else:	
									print "<td>", Allele, "</td>"
						print "</tr>"						
						number_of_hits = number_of_hits + 1		
	print "</table>"
	print "<form>"
	print """
	<input type='button' value='Download report' onClick="window.location.href='http://sites.biology.duke.edu/windhamlab/files/%s'">""" %OutFileName_Hit
	#print """
	#<input type='button' value='Download full report' onClick="window.location.href='http://sites.biology.duke.edu/windhamlab/files/%s'">""" %OutFileName_Hit_Full
	print "</form>"

	OutFile_Hit.close()
	#OutFile_Hit_Full.close()		
	return
	

	
	