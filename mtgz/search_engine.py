
class SearchEngine():

	_find_by_arguments = {}
	_library = None

	def __init__(self, library={}):
		self._library = library

	@property
	def find_by_arguments(self):
		return self._find_by_arguments

	@find_by_arguments.setter
	def find_by_arguments(self, arguments):
		self._find_by_arguments = arguments


	def find_by(self, argument, value):
		self.find_by_arguments[argument] = value

		return self

	def filter(self):
		filtered_cards = []
		if self.find_by_arguments['name'] is not None:
			filtered_cards.append(self._library[self.find_by_arguments['name']])

		return filtered_cards
