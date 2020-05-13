from unittest import TestCase

from domain.cards import Rank, Suit, Card, cardset


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
        self.assertEqual(self.card, Card(
            rank=Rank(code='B', name='Rank B', weight=3),
            suit=Suit(code='y', name='Suit Y', weight=3),
        ))
        self.assertNotEqual(self.card, Card(
            rank=Rank(code='B', name='Rank B', weight=5),
            suit=Suit(code='y', name='Suit Y', weight=3),
        ))
        self.assertNotEqual(self.card, Card(
            rank=Rank(code='B', name='Rank B', weight=3),
            suit=Suit(code='y', name='Suit Y', weight=1),
        ))
        self.assertNotEqual(self.card, Card(
            rank=Rank(code='B', name='Rank B', weight=1),
            suit=Suit(code='y', name='Suit Y', weight=5),
        ))

    def test_gt(self):
        self.assertFalse(self.card > Card(
            rank=Rank(code='B', name='Rank B', weight=3),
            suit=Suit(code='y', name='Suit Y', weight=3),
        ))
        self.assertFalse(self.card > Card(
            rank=Rank(code='B', name='Rank B', weight=5),
            suit=Suit(code='y', name='Suit Y', weight=3)
        ))
        self.assertTrue(self.card > Card(
            rank=Rank(code='B', name='Rank B', weight=3),
            suit=Suit(code='y', name='Suit Y', weight=1),
        ))
        self.assertTrue(self.card > Card(
            rank=Rank(code='B', name='Rank B', weight=1),
            suit=Suit(code='y', name='Suit Y', weight=5),
        ))


class CardSetTestCase(TestCase):
    def test_getitem(self):
        self.assertEqual(cardset['Ah'].code, 'Ah')
        with self.assertRaises(KeyError):
            cardset['Xy']

    def test_contains(self):
        self.assertIn(cardset['Ah'], cardset)
