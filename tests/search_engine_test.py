import unittest
from mtgz.search_engine import SearchEngine

class TestSearchEngine(unittest.TestCase):

	def setUp(self):
		SearchEngine.find_by_arguments = {}

	def test_find_by_with_one_parameters(self):
		search_engine = SearchEngine()
		search_engine.find_by('name', 'Black Lotus')

		self.assertEqual({'name': 'Black Lotus'}, search_engine.find_by_arguments)

	def test_find_by_with_many_parameters(self):
		search_engine = SearchEngine()
		search_engine.find_by('name', 'Black Lotus')
		search_engine.find_by('type', 'Artifact')
		search_engine.find_by('manaCost', '0')

		self.assertEqual({'manaCost': '0', 'type': 'Artifact', 'name': 'Black Lotus'}, search_engine.find_by_arguments)

	def test_filter_cards_by_name(self):
		search_engine = SearchEngine(
			{'Black Lotus': {
				'name': 'Black Lotus'
			}, 
			'Ancestral Vision': {
			'name': 'Ancestral Vision'
			}
		})
		
		self.assertEqual([{'name': 'Black Lotus'}], search_engine.find_by('name', 'Black Lotus').filter())

	def test_filter_cards_by_part_of_name(self):
		search_engine = SearchEngine(
			{'Black Lotus': {
				'name': 'Black Lotus'
			}, 
			'Black Vise': {
				'name': 'Black Vise'
			},
			'Thraximundar': {
				'name': 'Thraximundar'
			},
			'Bringer of the Black Dawn': {
				'name': 'Bringer of the Black Dawn'
			}
		})

		filtered_cards = search_engine.find_by('name', 'Black').filter()
		self.assertEqual(3, len(filtered_cards))
		for card in filtered_cards:
			self.assertTrue(card['name'] in ['Bringer of the Black Dawn', 'Black Vise', 'Black Lotus'])

	def test_filter_card_no_cares_with_case_sensitive(self):
		search_engine = SearchEngine(
			{'Black Lotus': {
				'name': 'Black Lotus'
			}
		})

		self.assertEqual(1, len(search_engine.find_by('name', 'black').filter()))

if __name__ == '__main__':
	unittest.main()