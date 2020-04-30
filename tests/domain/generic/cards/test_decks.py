from unittest import TestCase

from domain.generic.cards import StandardDeck, cardset


class DeckTestCase(TestCase):
    def setUp(self):
        self.deck = StandardDeck()

    def tearDown(self):
        del self.deck

    def test_shuffle(self):
        self.deck.shuffle()

    def test_pop(self):
        self.assertEqual(self.deck.pop(), cardset['Kc'])
