
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
		filtered_cards = [self._library[card_name] for card_name in self._library]
		if 'name' in self.find_by_arguments:
			standardized_name = ' '.join([word[:1].upper() + word[1:].lower() for word in self.find_by_arguments['name'].split()])
			filtered_cards = [card for card in filtered_cards if standardized_name in card['name']]
		if 'type' in self.find_by_arguments:
			standardized_type = ' '.join([word[:1].upper() + word[1:].lower() for word in self.find_by_arguments['type'].split()])
			filtered_cards = [card for card in filtered_cards if standardized_type in card['type']]
		if 'text' in self.find_by_arguments:
			filtered_cards = [card for card in filtered_cards if 'text' in card] # only cards with text
			filtered_cards = [card for card in filtered_cards if self.find_by_arguments['text'].lower() in card['text'].lower()]
		if 'cmc' in self.find_by_arguments:
			filtered_cards = [card for card in filtered_cards if 'cmc' in card] # only cards with cmc
			filtered_cards = [card for card in filtered_cards if int(card['cmc']) == int(self.find_by_arguments['cmc'])]
		if 'rarity' in self.find_by_arguments:
			print(self.find_by_arguments['rarity'])
			filtered_cards = [card for card in filtered_cards if 'rarity' in card] # only cards with cmc
			filtered_cards = [card for card in filtered_cards if card['rarity'][0].lower() == self.find_by_arguments['rarity']]

		if 'color' in self.find_by_arguments:
			if self.find_by_arguments['color'].upper() == 'C': #incolor card
				filtered_cards = [card for card in filtered_cards if 'colorIdentity' not in card]
			else:
				filtered_cards = [card for card in filtered_cards if 'colorIdentity' in card] # only cards with color
				for letter in self.find_by_arguments['color'].upper():
					filtered_cards = [card for card in filtered_cards if letter in ''.join(card['colorIdentity'])]

		return filtered_cards

