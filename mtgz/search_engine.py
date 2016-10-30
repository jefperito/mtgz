
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
			standardized_name = ' '.join([word[:1].upper() + word[1:].lower() for word in self.find_by_arguments['name'].split()])
			if standardized_name in self._library:
				filtered_cards.append(self._library[standardized_name])
			else:
				matched_names = [key for key in self._library.keys() if standardized_name in key]
				return [self._library[name] for name in matched_names]

		return filtered_cards
