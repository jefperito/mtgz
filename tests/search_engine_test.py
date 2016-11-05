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
				'name': 'Black Lotus',
				'type': 'Artifact'
			},
			'Thraximundar': {
				'name': 'Thraximundar',
				'type': 'Legendary Creature - Zombie Assassin',
				'power': 7,
				'toughness': 7
			}
		})

		filtered_cards = search_engine.find_by('type', 'artifact').filter()
		self.assertEqual(1, len(filtered_cards))
		self.assertEqual('Black Lotus', filtered_cards[0]['name'])


	def test_filter_card_by_multiple_parameters(self):
		search_engine = SearchEngine(
			{'Black Lotus': {
				'name': 'Black Lotus',
				'type': 'Artifact',
				'text': '{T}, Sacrifice Black Lotus: Add three mana of any one color to your mana pool.'
			},
			'Black Vise': {
				'name': 'Black Vise',
				'type': 'Artifact',
				'text': 'As Black Vise enters the battlefield, choose an opponent.'
			},
			'Black Knight': {
				'name': 'Black Knight',
				'type': 'Creature - Human Knight',
				'text': 'First strike\nProtection from white'
			}
		})
		filtered_cards = search_engine.find_by('name', 'black').find_by('type', 'artifact').filter()
		self.assertEqual(2, len(filtered_cards))
		for card in filtered_cards:
			self.assertTrue(card['name'] in ['Black Vise', 'Black Lotus'])

	def test_filter_card_by_text(self):
		search_engine = SearchEngine(
			{'Black Lotus': {
				'name': 'Black Lotus',
				'type': 'Artifact',
				'text': '{T}, Sacrifice Black Lotus: Add three mana of any one color to your mana pool.'
			},
			'Black Vise': {
				'name': 'Black Vise',
				'type': 'Artifact',
				'text': 'As Black Vise enters the battlefield, choose an opponent.'
			},
			'Black Knight': {
				'name': 'Black Knight',
				'type': 'Creature - Human Knight',
				'text': 'First strike\nProtection from white'
			}
		})
		filtered_cards = search_engine.find_by('text', 'black').filter()
		self.assertEqual(2, len(filtered_cards))
		for card in filtered_cards:
			self.assertTrue(card['name'] in ['Black Vise', 'Black Lotus'])		

	def test_filter_card_by_cmc(self):
		search_engine = SearchEngine(
			{'Black Lotus': {
				'name': 'Black Lotus',
				'type': 'Artifact',
				'text': '{T}, Sacrifice Black Lotus: Add three mana of any one color to your mana pool.',
				'cmc': '0'
			},
			'Black Vise': {
				'name': 'Black Vise',
				'type': 'Artifact',
				'text': 'As Black Vise enters the battlefield, choose an opponent.',
				'cmc': '2'
			},
			'Black Knight': {
				'name': 'Black Knight',
				'type': 'Creature - Human Knight',
				'text': 'First strike\nProtection from white',
				'cmc': '2'
			}
		})
		filtered_cards = search_engine.find_by('cmc', '2').filter()
		self.assertEqual(2, len(filtered_cards))
		for card in filtered_cards:
			self.assertTrue(card['name'] in ['Black Vise', 'Black Knight'])

	def test_filter_card_by_color_identity(self):
		search_engine = SearchEngine(
			{'Black Lotus': {
				'name': 'Black Lotus',
				'type': 'Artifact',
				'text': '{T}, Sacrifice Black Lotus: Add three mana of any one color to your mana pool.',
				'cmc': '0'
			},
			'Black Vise': {
				'name': 'Black Vise',
				'type': 'Artifact',
				'text': 'As Black Vise enters the battlefield, choose an opponent.',
				'cmc': '2'
			},
			'Black Knight': {
				'name': 'Black Knight',
				'type': 'Creature - Human Knight',
				'text': 'First strike\nProtection from white',
				'cmc': '2',
				'colorIdentity': ['B']
			},
			'Thraximundar': {
				'name': 'Thraximundar',
				'type': 'Legendary Creature - Zombie Assassin',
				'text': 'Whenever Thraximundar attacks, defending player sacrifices a creature.Whenever a player sacrifices a creature, you may put a +1/+1 counter on Thraximundar.',
				'cmc': '7',
				'colorIdentity': ['U', 'B', 'R']
			}
		})
		filtered_cards = search_engine.find_by('color', 'b').filter()
		self.assertEqual(2, len(filtered_cards))
		for card in filtered_cards:
			self.assertTrue(card['name'] in ['Thraximundar', 'Black Knight'])

	def test_filter_incolor_card(self):
		search_engine = SearchEngine(
			{'Black Lotus': {
				'name': 'Black Lotus',
				'type': 'Artifact',
				'text': '{T}, Sacrifice Black Lotus: Add three mana of any one color to your mana pool.',
				'cmc': '0'
			},
			'Black Vise': {
				'name': 'Black Vise',
				'type': 'Artifact',
				'text': 'As Black Vise enters the battlefield, choose an opponent.',
				'cmc': '2'
			},
			'Black Knight': {
				'name': 'Black Knight',
				'type': 'Creature - Human Knight',
				'text': 'First strike\nProtection from white',
				'cmc': '2',
				'colorIdentity': ['B']
			},
			'Thraximundar': {
				'name': 'Thraximundar',
				'type': 'Legendary Creature - Zombie Assassin',
				'text': 'Whenever Thraximundar attacks, defending player sacrifices a creature.Whenever a player sacrifices a creature, you may put a +1/+1 counter on Thraximundar.',
				'cmc': '7',
				'colorIdentity': ['U', 'B', 'R']
			}
		})
		filtered_cards = search_engine.find_by('color', 'c').filter()
		self.assertEqual(2, len(filtered_cards))
		for card in filtered_cards:
			self.assertTrue(card['name'] in ['Black Lotus', 'Black Vise'])

if __name__ == '__main__':
	unittest.main()