import unittest
from mtgz.search_engine import SearchEngine

class TestSearchEngine(unittest.TestCase):

	def setUp(self):
		SearchEngine.find_by_arguments = []

	def test_find_by_with_one_parameters(self):
		search_engine = SearchEngine()
		search_engine.find_by('name')

		self.assertEqual(['name'], search_engine.find_by_arguments)

	def test_find_by_with_many_parameters(self):
		search_engine = SearchEngine()
		search_engine.find_by('name')
		search_engine.find_by('type')
		search_engine.find_by('manaCost')

		self.assertEqual(['name', 'type', 'manaCost'], search_engine.find_by_arguments)

if __name__ == '__main__':
	unittest.main()