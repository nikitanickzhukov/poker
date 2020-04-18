from unittest import TestCase

from .ranks import Rank
from .suits import Suit
from .cards import Card, cardset
from .decks import StandardDeck


class RankTestCase(TestCase):
    def setUp(self):
        self.a = Rank(code='A', name='rank A', weight=3)
        self.b = Rank(code='B', name='rank B', weight=5)
        self.c = Rank(code='C', name='rank C', weight=7)

    def tearDown(self):
        del self.a
        del self.b
        del self.c

    def test_init(self):
        Rank(code='A', name='Rank A', weight=1)
        with self.assertRaises(ValueError):
            Rank(code='AA', name='Rank A', weight=1)
        with self.assertRaises(ValueError):
            Rank(code='a', name='Rank A', weight=1)
        with self.assertRaises(ValueError):
            Rank(code='aa', name='Rank A', weight=1)

    def test_eq(self):
        self.assertEqual(self.a, Rank(code='A', name='Rank M', weight=4))
        self.assertNotEqual(self.a, Rank(code='M', name='Rank A', weight=3))

    def test_gt(self):
        self.assertFalse(self.b > self.b)
        self.assertTrue(self.b > self.a)
        self.assertFalse(self.b > self.c)


class SuitTestCase(TestCase):
    def setUp(self):
        self.x = Suit(code='x', name='Suit X', weight=3)
        self.y = Suit(code='y', name='Suit Y', weight=5)
        self.z = Suit(code='z', name='Suit Z', weight=7)

    def tearDown(self):
        del self.x
        del self.y
        del self.z

    def test_init(self):
        Suit(code='x', name='Suit X', weight=1)
        with self.assertRaises(ValueError):
            Suit(code='xx', name='Suit X', weight=1)
        with self.assertRaises(ValueError):
            Suit(code='X', name='Suit X', weight=1)
        with self.assertRaises(ValueError):
            Suit(code='XX', name='Suit X', weight=1)

    def test_eq(self):
        self.assertEqual(self.x, Suit(code='x', name='Suit M', weight=4))
        self.assertNotEqual(self.x, Suit(code='m', name='Suit X', weight=3))

    def test_gt(self):
        self.assertFalse(self.y > self.y)
        self.assertTrue(self.y > self.x)
        self.assertFalse(self.y > self.z)


class CardTestCase(TestCase):
    def setUp(self):
        self.a = Rank(code='A', name='rank A', weight=1)
        self.b = Rank(code='B', name='rank B', weight=2)
        self.x = Suit(code='x', name='suit X', weight=1)
        self.y = Suit(code='y', name='suit Y', weight=2)
        self.ax = Card(rank=self.a, suit=self.x)
        self.ay = Card(rank=self.a, suit=self.y)
        self.bx = Card(rank=self.b, suit=self.x)
        self.by = Card(rank=self.b, suit=self.y)

    def tearDown(self):
        del self.a
        del self.b
        del self.x
        del self.y
        del self.ax
        del self.ay
        del self.bx
        del self.by

    def test_init(self):
        Card(rank=self.a, suit=self.x)
        with self.assertRaises(TypeError):
            Card(rank=self.a, suit=self.b)
        with self.assertRaises(TypeError):
            Card(rank=self.y, suit=self.x)
        with self.assertRaises(TypeError):
            Card(rank=self.y, suit=self.a)

    def test_eq(self):
        self.assertEqual(self.ax, self.ax)
        self.assertNotEqual(self.ax, self.ay)
        self.assertNotEqual(self.ax, self.bx)
        self.assertNotEqual(self.ax, self.by)

    def test_gt(self):
        self.assertTrue(self.bx > self.ax)
        self.assertTrue(self.bx > self.ay)
        self.assertFalse(self.bx > self.bx)
        self.assertFalse(self.bx > self.by)


class CardSetTestCase(TestCase):
    def test_getitem(self):
        cardset['Ah']
        with self.assertRaises(KeyError):
            cardset['Xy']

    def test_contains(self):
        self.assertIn(cardset['Ah'], cardset)


class DeckTestCase(TestCase):
    def setUp(self):
        self.a = StandardDeck()

    def tearDown(self):
        del self.a

    def test_pop(self):
        self.a.pop()
