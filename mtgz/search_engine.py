
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
			if self.find_by_arguments['name'] in self._library:
				filtered_cards.append(self._library[self.find_by_arguments['name']])
			else:
				matched_names = [key for key in self._library.keys() if self.find_by_arguments['name'] in key]
				return [self._library[name] for name in matched_names]

		return filtered_cards
