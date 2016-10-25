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

if __name__ == '__main__':
	unittest.main()