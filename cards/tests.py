from unittest import TestCase

from .props import Prop
from .ranks import Rank
from .suits import Suit
from .cards import Card, cardset
from .decks import StandardDeck


class PropTestCase(TestCase):
    def setUp(self):
        self.prop = Prop(code='A', name='Prop A', weight=3)

    def tearDown(self):
        del self.prop

    def test_init(self):
        with self.assertRaises(AssertionError):
            Prop(code='AA', name='Prop A', weight=3)
        with self.assertRaises(AssertionError):
            Prop(code='A', name='', weight=3)
        with self.assertRaises(AssertionError):
            Prop(code='A', name='Prop A', weight=-1)

    def test_attrs(self):
        self.assertEqual(self.prop.code, 'A')
        self.assertEqual(self.prop.name, 'Prop A')
        self.assertEqual(self.prop.weight, 3)

    def test_eq(self):
        self.assertEqual(self.prop, Prop(code='B', name='Prop B', weight=3))
        self.assertNotEqual(self.prop, Prop(code='B', name='Prop B', weight=1))
        self.assertNotEqual(self.prop, Prop(code='B', name='Prop B', weight=5))

    def test_gt(self):
        self.assertFalse(self.prop > Prop(code='B', name='Prop B', weight=3))
        self.assertTrue(self.prop > Prop(code='B', name='Prop B', weight=1))
        self.assertFalse(self.prop > Prop(code='B', name='Prop B', weight=5))


class CardTestCase(TestCase):
    def setUp(self):
        self.rank = Rank(code='A', name='Rank A', weight=3)
        self.suit = Suit(code='x', name='Suit X', weight=3)
        self.card = Card(rank=self.rank, suit=self.suit)

    def tearDown(self):
        del self.card
        del self.suit
        del self.rank

    def test_attrs(self):
        self.assertEqual(self.card.rank, self.rank)
        self.assertEqual(self.card.suit, self.suit)

    def test_eq(self):
        self.assertEqual(self.card, Card(rank=Rank(code='B', name='Rank B', weight=3), suit=Suit(code='y', name='Suit Y', weight=3)))
        self.assertNotEqual(self.card, Card(rank=Rank(code='B', name='Rank B', weight=5), suit=Suit(code='y', name='Suit Y', weight=3)))
        self.assertNotEqual(self.card, Card(rank=Rank(code='B', name='Rank B', weight=3), suit=Suit(code='y', name='Suit Y', weight=1)))
        self.assertNotEqual(self.card, Card(rank=Rank(code='B', name='Rank B', weight=1), suit=Suit(code='y', name='Suit Y', weight=5)))

    def test_gt(self):
        self.assertFalse(self.card > Card(rank=Rank(code='B', name='Rank B', weight=3), suit=Suit(code='y', name='Suit Y', weight=3)))
        self.assertFalse(self.card > Card(rank=Rank(code='B', name='Rank B', weight=5), suit=Suit(code='y', name='Suit Y', weight=3)))
        self.assertTrue(self.card > Card(rank=Rank(code='B', name='Rank B', weight=3), suit=Suit(code='y', name='Suit Y', weight=1)))
        self.assertTrue(self.card > Card(rank=Rank(code='B', name='Rank B', weight=1), suit=Suit(code='y', name='Suit Y', weight=5)))


class CardSetTestCase(TestCase):
    def test_getitem(self):
        cardset['Ah']
        with self.assertRaises(KeyError):
            cardset['Xy']

    def test_contains(self):
        self.assertIn(cardset['Ah'], cardset)


class DeckTestCase(TestCase):
    def setUp(self):
        self.deck = StandardDeck()

    def tearDown(self):
        del self.deck

    def test_shuffle(self):
        self.deck.shuffle()

    def test_pop(self):
        self.assertEqual(self.deck.pop(), cardset['Kc'])
