#!/usr/bin/python

# The purpose of this script is to extract relevant TIGRFAM ids given a tag
# to search for following the IT (isology-type) tag in a TIGRFAM info file. 
#
# HOWTO: (python) extract_TIGRFAM_IDs_from_IT.py path_to_info_file pattern
#
# Author: James Matsumura

import sys, os, re

inputFile =  str(sys.argv[1]) # let the user specify the info file
pattern =  str(sys.argv[2]) # let the user specify the pattern to extract by

regexForAC = r"^AC\s+(.*)"
regexForIT = r"^IT\s+" + pattern + r"$"

idFile = open(inputFile, 'r')
outFile = open('./extracted_ids_output.txt', 'w')
foundId = ''
currentID = ''
foundEquivalog = ''

# The files format is such that the IT tag always follows the AC tag. Thus,
# every new AC tag store it and only if an equivalog IT tag is found immediately
# following it, THEN add it to the final file. 
for line in idFile:
	line = line.rstrip('\n')

	foundId = re.search(regexForAC, line)
	if foundId: currentId = foundId.group(1)

	foundEquivalog = re.search(regexForIT, line)
	if foundEquivalog: outFile.write(currentId+"\n")
