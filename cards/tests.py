import unittest

from .ranks import Rank
from .suits import Suit
from .cards import Card


class RankTestCase(unittest.TestCase):
    def setUp(self):
        self.a = Rank(code='A', name='rank A', order=3, weight=8)
        self.b = Rank(code='B', name='rank B', order=5, weight=6)
        self.c = Rank(code='C', name='rank C', order=7, weight=4)

    def tearDown(self):
        del self.a
        del self.b
        del self.c

    def test_eq(self):
        self.assertTrue(self.a == Rank(code='A', name='Rank M', order=4, weight=7))
        self.assertFalse(self.a == Rank(code='M', name='Rank A', order=3, weight=3))

    def test_ne(self):
        self.assertFalse(self.a != Rank(code='A', name='Rank M', order=4, weight=7))
        self.assertTrue(self.a != Rank(code='M', name='Rank A', order=3, weight=3))

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
        self.x = Suit(code='x', name='Suit X', order=3, weight=8)
        self.y = Suit(code='y', name='Suit Y', order=5, weight=6)
        self.z = Suit(code='z', name='Suit Z', order=7, weight=4)

    def tearDown(self):
        del self.x
        del self.y
        del self.z

    def test_eq(self):
        self.assertTrue(self.x == Suit(code='x', name='Suit M', order=4, weight=7))
        self.assertFalse(self.x == Suit(code='m', name='Suit X', order=3, weight=3))

    def test_ne(self):
        self.assertFalse(self.x != Suit(code='x', name='Suit M', order=4, weight=7))
        self.assertTrue(self.x != Suit(code='m', name='Suit X', order=3, weight=3))

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
        self.a = Rank(code='A', name='rank A', order=1, weight=2)
        self.b = Rank(code='B', name='rank B', order=2, weight=1)
        self.x = Suit(code='x', name='suit X', order=1, weight=2)
        self.y = Suit(code='y', name='suit Y', order=2, weight=1)
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

    def test_eq(self):
        self.assertTrue(self.ax == self.ax)
        self.assertFalse(self.ax == self.ay)
        self.assertFalse(self.ax == self.bx)
        self.assertFalse(self.ax == self.by)

    def test_ne(self):
        self.assertFalse(self.ax != self.ax)
        self.assertTrue(self.ax != self.ay)
        self.assertTrue(self.ax != self.bx)
        self.assertTrue(self.ax != self.by)

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


if __name__ == '__main__':
    unittest.main()
