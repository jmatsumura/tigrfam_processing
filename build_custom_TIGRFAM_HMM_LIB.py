#!/usr/bin/python

# The purpose of this script is to build a custom TIGRFAM HMM LIB after 
# extracting the desired TIGRFAM ids using extract_TIGRFAM_IDs_from_IT.py
#
# HOWTO: (python) build_custom_TIGRFAM_HMM_LIB.py path_to_extracted_ids_file path_to_tigrfam_hmm_lib_file
#
# Author: James Matsumura

import sys, os, re

idFile =  str(sys.argv[1]) # let the user specify the info file
hmmLibFile =  str(sys.argv[2]) # let the user specify the info file

regexForHeader = r"^HMMER"
regexForName = r"^NAME"
regexForId = r"^ACC\s+(.*)$"
regexForFooter = r"^\/\/"

# Declaring all explicitly to elucidate the nomenclature
relevantIdsFile = open(idFile, 'r')
originalHMMLIBFile = open(hmmLibFile, 'r')
outFile = open('./custom_TIGRFAMs_HMM.LIB', 'w')
headerFound = False
nameFound = False
idFound = False
footerFound = False
validEntry = False
foundHeader = ''
foundName = ''
foundId = ''
foundIdValue = ''
relevantIdsList = []

# First, build a set of target IDs to use for lookup
for line in relevantIdsFile:
	line = line.rstrip('\n')
	relevantIdsList.append(line)
	setOfIds = set(relevantIdsList)

# The files format is such that each entry ends with //. Use this as a
# spacer of sorts and print blocks of entries until this is found. 
for line in originalHMMLIBFile:

	line = line.rstrip('\n')

	if(validEntry == True):
		if(re.search(regexForFooter, line)):
			outFile.write(line+'\n')
			validEntry = False
			idFound = False
			nameFound = False
			headerFound = False
		else:
			outFile.write(line+'\n')

	elif(headerFound==True and nameFound==True and idFound==True and validEntry==False):
		if(foundIdValue in setOfIds):
			outFile.write(headerValue+'\n')
			outFile.write(nameValue+'\n')
			outFile.write(idValue+'\n')
			validEntry = True	
		else:
			idFound = False
			nameFound = False
			headerFound = False

	elif(headerFound==True and nameFound==True and idFound==False):
		foundId = re.search(regexForId, line)
		if(foundId): 
			idFound = True
			idValue = line
			foundIdValue = foundId.group(1)

	elif(headerFound==True and nameFound==False):
		if(re.search(regexForName, line)): 
			nameFound = True
			nameValue = line

	elif(headerFound==False):
		if(re.search(regexForHeader, line)): 
			headerFound = True
			headerValue = line
