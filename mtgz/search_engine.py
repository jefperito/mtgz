
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
			card_name = ' '.join([token_name[:1].upper() + token_name[1:] for token_name in self.find_by_arguments['name']])
			filtered_cards.append(self._library[card_name])

		return filtered_cards
