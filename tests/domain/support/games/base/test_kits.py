from unittest import TestCase

from domain.generic.cards import StandardDeck
from domain.support.games.base.streets import Street
from domain.support.games.base.kits import Kit


class TestStreet1(Street):
    length = 2


class TestStreet2(Street):
    length = 1


class TestKit(Kit):
    pass


class KitTestCase(TestCase):
    def setUp(self):
        self.deck = StandardDeck()
        self.deck.shuffle()

    def tearDown(self):
        del self.deck

    def test_init(self):
        a, b, c = self.deck[0:3]
        street1 = TestStreet1(cards=(a, b))
        street2 = TestStreet2(cards=(c,))
        TestKit()
        TestKit(streets=(street1,))
        TestKit(streets=(street1, street2))

    def test_contains(self):
        a, b, c, d = self.deck[0:4]
        street1 = TestStreet1(cards=(a, b))
        street2 = TestStreet2(cards=(c,))
        self.assertIn(a, TestKit(streets=(street1,)))
        self.assertIn(c, TestKit(streets=(street1, street2)))
        self.assertNotIn(d, TestKit(streets=(street1, street2)))

    def test_append(self):
        a, b, c, d = self.deck[0:4]
        kit = TestKit()
        street1 = TestStreet1(cards=(a, b))
        street2 = TestStreet2(cards=(c,))
        kit.append(street1)
        self.assertIn(a, kit)
        kit.append(street2)
        self.assertIn(c, kit)
