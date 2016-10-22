import json
import argparse
from colors import ColoredManaSymbol

def console():
	arguments_parse = argparse.ArgumentParser(description='Magic: The Gathering Parser')
	arguments_parse.add_argument('-name', metavar = '-n', nargs='*', help='look up for card name')

	return arguments_parse.parse_args()

def print_card(card):
	painter = ColoredManaSymbol()
	print('{0} {1}'.format(card['name'], (painter.color(card['manaCost']) if 'manaCost' in card else '')))
	print(card['type']+'\n')
	if 'text' in card:
		print(card['text'])
	if 'power' in card:
		print('{0}/{1}'.format(card['power'], card['toughness']))
	#print(card.keys())

def main():
	# mapped by card name
	cursor = open('AllCards.json')
	# 'pickle' me
	library = json.loads(cursor.read())
	arguments = console()

	if arguments.name is not None:
		card_name = ' '.join([token_name[:1].upper() + token_name[1:] for token_name in arguments.name])
		print_card(library[card_name])
	

if __name__ == '__main__':
	main()