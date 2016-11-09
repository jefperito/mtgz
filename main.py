import re
import json
import argparse
from mtgz.colors import ColoredManaSymbol
from mtgz.search_engine import SearchEngine
from mtgz.services import DBUploader

def console():
	arguments_parse = argparse.ArgumentParser(description='Magic: The Gathering Search Engine')
	arguments_parse.add_argument('--name', metavar = '-n', nargs='*', help='look up for card\'s name')
	arguments_parse.add_argument('--type', nargs='*', help='look up for card\'s type')
	arguments_parse.add_argument('--text', nargs='*', help='look up for card\'s text')
	arguments_parse.add_argument('--cmc', nargs='?', help='look up for card\'s cmc')
	arguments_parse.add_argument('--color', nargs='?', help='look up for card\'s color identity')
	arguments_parse.add_argument('--upgrade', action='store_true', help='upgrade the database')

	return arguments_parse.parse_args()


def print_card(card):
	painter = ColoredManaSymbol()
	print('{0} {1}'.format(card['name'], (painter.color(card['manaCost']) if 'manaCost' in card else '')))
	print('{0} {1}\n'.format(card['type'], '({0}/{1})'.format(card['power'], card['toughness']) if 'power' in card else ''))
	if 'text' in card:
		text = card['text']
		for manacost in re.findall('{\w}', text):
			text = text.replace(manacost, painter.color(manacost))
		print(text)
	print('------------------------------------------------')


def main():
	arguments = console()
	
	if arguments.upgrade:
		print('Downloading new database...')
		DBUploader().upgrade()
		print('done!')
	else:
		# mapped by card name
		# TODO 'pickle' me
		search_engine = SearchEngine(json.loads(open('AllCards.json').read()))
		if arguments.name is not None:
			search_engine.find_by('name', ' '.join(arguments.name))
		if arguments.type is not None:
			search_engine.find_by('type', ' '.join(arguments.type))
		if arguments.text is not None:
			search_engine.find_by('text', ' '.join(arguments.text))
		if arguments.cmc is not None:
			search_engine.find_by('cmc', arguments.cmc)
		if arguments.color is not None:
			search_engine.find_by('color', arguments.color)

		filtered_cards = search_engine.filter()

		for card in filtered_cards:	print_card(card)
		print('\n{0} cards found'.format(len(filtered_cards)))


if __name__ == '__main__':
	main()
