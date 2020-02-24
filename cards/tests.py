import unittest

from .ranks import Rank
from .suits import Suit
from .cards import Card
from .decks import StandardDeck


class RankTestCase(unittest.TestCase):
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
        with self.assertRaises(AssertionError):
            Rank(code='AA', name='Rank A', weight=1)
        with self.assertRaises(AssertionError):
            Rank(code='a', name='Rank A', weight=1)
        with self.assertRaises(AssertionError):
            Rank(code='aa', name='Rank A', weight=1)

    def test_eq(self):
        self.assertEqual(self.a, Rank(code='A', name='Rank M', weight=4))
        self.assertNotEqual(self.a, Rank(code='M', name='Rank A', weight=3))

    def test_gt(self):
        self.assertFalse(self.b > self.b)
        self.assertTrue(self.b > self.a)
        self.assertFalse(self.b > self.c)

    def test_ge(self):
        self.assertTrue(self.b >= self.b)
        self.assertTrue(self.b >= self.a)
        self.assertFalse(self.b >= self.c)

    def test_lt(self):
        self.assertFalse(self.b < self.b)
        self.assertFalse(self.b < self.a)
        self.assertTrue(self.b < self.c)

    def test_le(self):
        self.assertTrue(self.b <= self.b)
        self.assertFalse(self.b <= self.a)
        self.assertTrue(self.b <= self.c)


class SuitTestCase(unittest.TestCase):
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
        with self.assertRaises(AssertionError):
            Suit(code='xx', name='Suit X', weight=1)
        with self.assertRaises(AssertionError):
            Suit(code='X', name='Suit X', weight=1)
        with self.assertRaises(AssertionError):
            Suit(code='XX', name='Suit X', weight=1)

    def test_eq(self):
        self.assertEqual(self.x, Suit(code='x', name='Suit M', weight=4))
        self.assertNotEqual(self.x, Suit(code='m', name='Suit X', weight=3))

    def test_gt(self):
        self.assertFalse(self.y > self.y)
        self.assertTrue(self.y > self.x)
        self.assertFalse(self.y > self.z)

    def test_ge(self):
        self.assertTrue(self.y >= self.y)
        self.assertTrue(self.y >= self.x)
        self.assertFalse(self.y >= self.z)

    def test_lt(self):
        self.assertFalse(self.y < self.y)
        self.assertFalse(self.y < self.x)
        self.assertTrue(self.y < self.z)

    def test_le(self):
        self.assertTrue(self.y <= self.y)
        self.assertFalse(self.y <= self.x)
        self.assertTrue(self.y <= self.z)


class CardTestCase(unittest.TestCase):
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
        with self.assertRaises(AssertionError):
            Card(rank=self.a, suit=self.b)
        with self.assertRaises(AssertionError):
            Card(rank=self.y, suit=self.x)
        with self.assertRaises(AssertionError):
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

    def test_ge(self):
        self.assertTrue(self.bx >= self.ax)
        self.assertTrue(self.bx >= self.ay)
        self.assertTrue(self.bx >= self.bx)
        self.assertFalse(self.bx >= self.by)

    def test_lt(self):
        self.assertFalse(self.bx < self.ax)
        self.assertFalse(self.bx < self.ay)
        self.assertFalse(self.bx < self.bx)
        self.assertTrue(self.bx < self.by)

    def test_le(self):
        self.assertFalse(self.bx <= self.ax)
        self.assertFalse(self.bx <= self.ay)
        self.assertTrue(self.bx <= self.bx)
        self.assertTrue(self.bx <= self.by)


class DeckTestCase(unittest.TestCase):
    def setUp(self):
        self.a = StandardDeck()
        self.b = StandardDeck()

    def tearDown(self):
        del self.a
        del self.b

    def test_eq(self):
        self.assertEqual(self.a, self.b)
        self.b.shuffle()
        self.assertNotEqual(self.a, self.b)

    def test_contains(self):
        c = self.a[0]
        self.assertIn(c, self.a)
        c = self.a.shift()
        self.assertNotIn(c, self.a)

    def test_getitem(self):
        c = self.a[0]
        with self.assertRaises(IndexError):
            self.a[len(self.a)]
        self.assertEqual(self.a[c.code], c)
        with self.assertRaises(KeyError):
            self.a['Xy']

    def test_delitem(self):
        c = self.a[0]
        del self.a[0]
        self.assertNotIn(c, self.a)
        with self.assertRaises(IndexError):
            del self.a[len(self.a)]
        d = self.a[0]
        del self.a[d.code]
        self.assertNotIn(d, self.a)
        with self.assertRaises(KeyError):
            del self.a['Xy']

    def test_push(self):
        c = self.a[-1]
        with self.assertRaises(AssertionError):
            self.a.push(c)
        del self.a[-1]
        self.assertNotEqual(c, self.a[-1])
        self.a.push(c)
        self.assertEqual(c, self.a[-1])

    def test_pop(self):
        c = self.a[-1]
        self.assertEqual(c, self.a.pop())
        self.assertNotEqual(c, self.a[-1])

    def test_unshift(self):
        c = self.a[0]
        with self.assertRaises(AssertionError):
            self.a.unshift(c)
        del self.a[0]
        self.assertNotEqual(c, self.a[0])
        self.a.unshift(c)
        self.assertEqual(c, self.a[0])

    def test_shift(self):
        c = self.a[0]
        self.assertEqual(c, self.a.shift())
        self.assertNotEqual(c, self.a[0])


if __name__ == '__main__':
    unittest.main()
