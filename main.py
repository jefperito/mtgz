import json
import argparse

def console():
	arguments_parse = argparse.ArgumentParser(description='Magic: The Gathering Parser')
	arguments_parse.add_argument('-name', metavar = '-n', nargs='*', help='look up for card name')

	return arguments_parse.parse_args()

def main():
	# mapped by card name
	cursor = open('AllCards.json')
	library = json.loads(cursor.read())

	arguments = console()

	if arguments.name is not None:
		card_name = ' '.join([token_name[:1].upper() + token_name[1:] for token_name in arguments.name])
		print('CARD NAME: ' + card_name)
		print(library[card_name])
	
	

if __name__ == '__main__':
	main()