from unittest import TestCase

from engine.domain.model.card import StandardDeck
from engine.domain.model.game.base.street import Street


class TestStreet1(Street):
    length = 2


class TestStreet2(Street):
    length = 1


class StreetTestCase(TestCase):
    def setUp(self):
        self.deck = StandardDeck()
        self.deck.shuffle()

    def tearDown(self):
        del self.deck

    def test_init(self):
        cards = self.deck.extract_top_cards(count=3)
        TestStreet1(cards=cards[0:2])
        with self.assertRaises(AssertionError):
            TestStreet1(cards=cards[0:1])
        with self.assertRaises(AssertionError):
            TestStreet1(cards=cards[0:3])

    def test_contains(self):
        cards = self.deck.extract_top_cards(count=3)
        self.assertIn(cards[0], TestStreet1(cards=cards[0:2]))
        self.assertNotIn(cards[2], TestStreet1(cards=cards[0:2]))
