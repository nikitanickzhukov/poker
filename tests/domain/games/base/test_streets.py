from unittest import TestCase

from domain.cards import StandardDeck
from domain.games.base.streets import Street


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
        a, b, c = self.deck[0:3]
        TestStreet1(cards=(a, b))
        with self.assertRaises(AssertionError):
            TestStreet1(cards=(a,))
        with self.assertRaises(AssertionError):
            TestStreet1(cards=(a, b, c))

    def test_contains(self):
        a, b, c = self.deck[0:3]
        self.assertIn(a, TestStreet1(cards=(a, b)))
        self.assertIn(a, TestStreet1(cards=(b, a)))
        self.assertNotIn(c, TestStreet1(cards=(a, b)))
