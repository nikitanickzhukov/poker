from unittest import TestCase

from domain.generic.cards import StandardDeck
from domain.support.games.base.streets import Street
from domain.support.games.base.kits import Kit


class TestStreet1(Street):
    length = 2


class TestStreet2(Street):
    length = 1


class TestKit(Kit):
    street_classes = (TestStreet1, TestStreet2)


class KitTestCase(TestCase):
    def setUp(self):
        self.deck = StandardDeck()
        self.deck.shuffle()

    def tearDown(self):
        del self.deck

    def test_init(self):
        a = self.deck.pop()
        b = self.deck.pop()
        c = self.deck.pop()
        d = self.deck.pop()
        street1 = TestStreet1(a, b)
        street2 = TestStreet2(c)
        TestKit()
        TestKit(street1)
        TestKit(street1, street2)
        with self.assertRaises(AssertionError):
            TestKit(street2, street1)
        TestKit(a, b)
        TestKit(a, b, c)
        with self.assertRaises(AssertionError):
            TestKit(a)
        with self.assertRaises(AssertionError):
            TestKit(a, b, c, d)

    def test_contains(self):
        a = self.deck.pop()
        b = self.deck.pop()
        c = self.deck.pop()
        d = self.deck.pop()
        self.assertIn(a, TestKit(TestStreet1(a, b)))
        self.assertIn(c, TestKit(TestStreet1(a, b), TestStreet2(c)))
        self.assertNotIn(d, TestKit(TestStreet1(a, b), TestStreet2(c)))

    def test_append(self):
        a = self.deck.pop()
        b = self.deck.pop()
        c = self.deck.pop()
        d = self.deck.pop()
        kit = TestKit()
        kit.append(TestStreet1(a, b))
        self.assertIn(a, kit)
        kit.append(c)
        self.assertIn(c, kit)
        with self.assertRaises(AssertionError):
            kit.append(TestStreet2(d))
        with self.assertRaises(AssertionError):
            kit.append(d)
