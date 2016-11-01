import json
import argparse
from mtgz.colors import ColoredManaSymbol
from mtgz.search_engine import SearchEngine

def console():
	arguments_parse = argparse.ArgumentParser(description='Magic: The Gathering Search Engine')
	arguments_parse.add_argument('-name', metavar = '-n', nargs='*', help='look up for card name')
	arguments_parse.add_argument('-type', nargs='*', help='look up for card type')
	arguments_parse.add_argument('-text', nargs='*', help='look up for card text')

	return arguments_parse.parse_args()


def print_card(card):
	painter = ColoredManaSymbol()
	print('{0} {1}'.format(card['name'], (painter.color(card['manaCost']) if 'manaCost' in card else '')))
	print('{0} {1}\n'.format(card['type'], '({0}/{1})'.format(card['power'], card['toughness']) if 'power' in card else ''))
	print(card['text'] if 'text' in card else '')
	print('------------------------------------------------')


def main():
	# mapped by card name
	# TODO 'pickle' me
	search_engine = SearchEngine(json.loads(open('AllCards.json').read()))
	
	arguments = console()
	filtered_cards = []

	if arguments.name is not None:
		search_engine.find_by('name', ' '.join(arguments.name))
	if arguments.type is not None:
		search_engine.find_by('type', ' '.join(arguments.type))
	if arguments.text is not None:
		search_engine.find_by('text', ' '.join(arguments.text))

	filtered_cards = search_engine.filter()

	for card in filtered_cards:	print_card(card)
	print('\n{0} cards found'.format(len(filtered_cards)))


if __name__ == '__main__':
	main()
