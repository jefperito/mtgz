import json
import argparse
from mtgz.colors import ColoredManaSymbol
from mtgz.search_engine import SearchEngine

def console():
	arguments_parse = argparse.ArgumentParser(description='Magic: The Gathering Search Engine')
	arguments_parse.add_argument('-name', metavar = '-n', nargs='*', help='look up for card name')

	return arguments_parse.parse_args()


def print_card(card):
	painter = ColoredManaSymbol()
	print('{0} {1}'.format(card['name'], (painter.color(card['manaCost']) if 'manaCost' in card else '')))
	print('{0} {1}\n'.format(card['type'], '({0}/{1})'.format(card['power'], card['toughness']) if 'power' in card else ''))
	print(card['text'])


def main():
	# mapped by card name
	# TODO 'pickle' me
	search_engine = SearchEngine(json.loads(open('AllCards.json').read()))
	
	arguments = console()

	if arguments.name is not None:
		print_card(search_engine.find_by('name', arguments.name).filter()[0])


if __name__ == '__main__':
	main()
