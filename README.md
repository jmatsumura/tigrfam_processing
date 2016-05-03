# tigrfam_processing
These scripts are used to build a custom TIGRFAM library based on a particular tag.

extract_TIGRFAM_IDs_from_IT.py
	This script will pull all TIGRFAM IDs given a TIGRFAM info file that match a 
	desired 'isology type' (see here: http://jcvi.org/cgi-bin/tigrfams/Listing.cgi) 
	Can be easily modified to match against any of the other tags.

build_custom_TIGRFAM_HMM_LIB.py
	This script follows up with the extracted IDs from extract_TIGRFAM_IDs_from_IT.py.
	Given the list of relevant IDs, this will only pull the HMMER3.0 formatted entries
	from the TIGRFAM HMM LIB that match the relevant IDs. 
