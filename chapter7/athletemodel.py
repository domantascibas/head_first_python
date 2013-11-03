"""
This script provides the functionality of reading data from files
and putting it to store, as well as getting it from store and 
displaying it as a dictionary of AthleteList. Script is using
Python's pickle function to achieve this.
"""

import pickle
from athletelist import AthleteList

def get_coach_data(filename):
	"""Opens a file containing athlete times, reads it and returns
	the name, date of birth and time list as an AthleteList object.
	"""
	try:
		with open(filename) as f:
			data = f.readline()
		templ = data.strip().split(',')
		return(AthleteList(templ.pop(0), templ.pop(0), templ))

	except IOError as ioerr:
		print('File error' + str(ioerr))
		return(none)

def put_to_store(files_list):
	all_athletes = {}
	#need to add code to populate the dictionary with the data
	#from the files. Also need to save the dictionary to a pickle
	for each_file in files_list:
		ath = get_coach_data(each_file)
		all_athletes[ath.name] = ath

	try:
		with open('athletes.pickle', 'wb') as athf:
			pickle.dump(all_athletes, athf)
	except IOError as ioerr:
		print('File error (put_and_store): ' + str(ioerr))
	
	return(all_athletes)

def get_from_store():
	all_athletes = {}
	#get the dictionary from the file, so that it can be returned to
	#the caller. both functions return a dictionary of AthleteList.
	try:
		with open('athletes.pickle', 'rb') as athf:
			all_athletes = pickle.load(athf)
	except IOError as ioerr:
		print('File error (get_from_store): ' + str(ioerr))

	return(all_athletes)