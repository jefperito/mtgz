
class SearchEngine():

	_find_by_arguments = []

	@property
	def find_by_arguments(self):
		return self._find_by_arguments

	def __init__(self, library={}):
		pass

	def findBy(self, argument):
		self._find_by_arguments.append(argument)

	def filter(self):
		pass