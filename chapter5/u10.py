def sanitize(time_string):
	"""
	The sanitize function takes an input list of times and
	unifies the time data format, so that all list entries
	have the same format.
	"""
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)

	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		return(data.strip().split(','))
	except IOError as ioerr:
		print('File error' + str(ioerr))
		return(none)

print(sorted(set([sanitize(t) for t in get_coach_data('james.txt')]))[0:3])
print(sorted(set([sanitize(t) for t in get_coach_data('julie.txt')]))[0:3])
print(sorted(set([sanitize(t) for t in get_coach_data('mikey.txt')]))[0:3])
print(sorted(set([sanitize(t) for t in get_coach_data('sarah.txt')]))[0:3])
