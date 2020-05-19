from unittest import TestCase

from engine.domain.model.card import StandardDeck
from engine.domain.model.game.base.street import Street
from engine.domain.model.game.base.kit import Kit


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
        street1 = TestStreet1(cards=self.deck.extract_top_cards(count=2))
        street2 = TestStreet2(cards=self.deck.extract_top_cards(count=1))
        TestKit()
        TestKit(streets=(street1,))
        TestKit(streets=(street1, street2))

    def test_contains(self):
        cards = self.deck.extract_top_cards(count=4)
        street1 = TestStreet1(cards=cards[0:2])
        street2 = TestStreet2(cards=cards[2:3])
        self.assertIn(cards[0], TestKit(streets=(street1,)))
        self.assertIn(cards[2], TestKit(streets=(street1, street2)))
        self.assertNotIn(cards[3], TestKit(streets=(street1, street2)))

    def test_append(self):
        cards = self.deck.extract_top_cards(count=4)
        kit = TestKit()
        street1 = TestStreet1(cards=cards[0:2])
        street2 = TestStreet2(cards=cards[2:3])
        kit.append(street1)
        self.assertIn(cards[0], kit)
        kit.append(street2)
        self.assertIn(cards[2], kit)
