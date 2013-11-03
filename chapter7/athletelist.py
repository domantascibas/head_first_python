class AthleteList(list):
 	"""Athlete list class object"""
 	def __init__(self, a_name, a_dob=None, a_times=[]):
 		list.__init__([])
 		self.name = a_name
 		self.dob = a_dob
 		self.extend(a_times)

# 	def top3(self):
# 		"""Prints the top 3 times of the athlete"""
# 		return(sorted(set([sanitize(t) for t in self]))[0:3])