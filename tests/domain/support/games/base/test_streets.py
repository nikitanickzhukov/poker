from unittest import TestCase

from domain.generic.cards import StandardDeck
from domain.support.games.base.streets import Street


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
        a = self.deck.pop()
        b = self.deck.pop()
        c = self.deck.pop()
        TestStreet1(a, b)
        with self.assertRaises(AssertionError):
            TestStreet1(a)
        with self.assertRaises(AssertionError):
            TestStreet1(a, b, c)

    def test_contains(self):
        a = self.deck.pop()
        b = self.deck.pop()
        c = self.deck.pop()
        self.assertIn(a, TestStreet1(a, b))
        self.assertIn(a, TestStreet1(b, a))
        self.assertNotIn(c, TestStreet1(a, b))
