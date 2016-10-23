import unittest
from mtgz.search_engine import SearchEngine

class TestSearchEngine(unittest.TestCase):

	def test_findBy_name(self):
		search_engine = SearchEngine()
		search_engine.findBy('name')

		self.assertEqual(['name'], search_engine.find_by_arguments)

if __name__ == '__main__':
	unittest.main()