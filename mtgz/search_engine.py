
class SearchEngine():

	_find_by_arguments = []

	@property
	def find_by_arguments(self):
		return self._find_by_arguments

	@find_by_arguments.setter
	def find_by_arguments(self, arguments):
		self._find_by_arguments = arguments

	def __init__(self, library={}):
		pass

	def find_by(self, argument):
		self.find_by_arguments.append(argument)

	def filter(self):
		pass
