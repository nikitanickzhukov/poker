from unittest import TestCase

from domain.cards import StandardDeck


class DeckTestCase(TestCase):
    def setUp(self):
        self.deck = StandardDeck()

    def tearDown(self):
        del self.deck

    def test_shuffle(self):
        a, b, c = self.deck[0:3]
        self.deck.shuffle()
        self.assertNotEqual((a, b, c), self.deck[0:3])

    def test_extract(self):
        a, b, c, d = self.deck[0:4]
        self.assertEqual([a, b, c], self.deck.extract(slice(0, 3)))
        self.assertEqual(d, self.deck.extract(0))
