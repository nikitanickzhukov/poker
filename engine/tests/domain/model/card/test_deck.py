from unittest import TestCase

from engine.domain.model.card import StandardDeck


class DeckTestCase(TestCase):
    def setUp(self):
        self.deck = StandardDeck()

    def tearDown(self):
        del self.deck

    def test_shuffle(self):
        self.deck.shuffle()

    def test_extract_top_cards(self):
        cards = self.deck.extract_top_cards(count=4)
