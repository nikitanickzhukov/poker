import unittest

from .ranks import Rank, RankSet
from .suits import Suit, SuitSet
from .cards import Card, CardSet
from .decks import Deck


class TestRank(unittest.TestCase):
    def setUp(self):
        self.a = Rank('A', 'rank A', 5)
        self.b = Rank('B', 'rank B', 3)
        self.c = Rank('C', 'rank C', 7)

    def tearDown(self):
        del self.a
        del self.b
        del self.c

    def test_eq(self):
        self.assertTrue(self.a == Rank('A', 'Rank X', 4))
        self.assertFalse(self.a == Rank('X', 'Rank A', 5))

    def test_ne(self):
        self.assertFalse(self.a != Rank('A', 'Rank X', 4))
        self.assertTrue(self.a != Rank('X', 'Rank A', 5))

    def test_gt(self):
        self.assertFalse(self.a > self.a)
        self.assertTrue(self.a > self.b)
        self.assertFalse(self.a > self.c)

    def test_ge(self):
        self.assertTrue(self.a >= self.a)
        self.assertTrue(self.a >= self.b)
        self.assertFalse(self.a >= self.c)

    def test_lt(self):
        self.assertFalse(self.a < self.a)
        self.assertFalse(self.a < self.b)
        self.assertTrue(self.a < self.c)

    def test_le(self):
        self.assertTrue(self.a <= self.a)
        self.assertFalse(self.a <= self.b)
        self.assertTrue(self.a <= self.c)


class TestRankSet(unittest.TestCase):
    def setUp(self):
        self.a = Rank('A', 'rank A', 1)
        self.b = Rank('B', 'rank B', 2)
        self.c = Rank('C', 'rank C', 3)
        self.ab = RankSet([self.a, self.b,])
        self.bc = RankSet([self.b, self.c,])
        self.ba = RankSet([self.b, self.a,])

    def tearDown(self):
        del self.a
        del self.b
        del self.c
        del self.ab
        del self.bc
        del self.ba

    def test_eq(self):
        self.assertEqual(self.ab, self.ba)

    def test_ne(self):
        self.assertNotEqual(self.ab, self.bc)
        self.assertNotEqual(self.bc, self.ba)

    def test_contains(self):
        self.assertTrue(self.a in self.ab)
        self.assertTrue(self.b in self.ba)
        self.assertTrue(self.a not in self.bc)

    def test_getitem(self):
        self.assertEqual(self.ab[self.a.code], self.a)
        self.assertNotEqual(self.bc[self.b.code], self.a)
        with self.assertRaises(KeyError):
            self.ab['x']


class TestSuit(unittest.TestCase):
    def setUp(self):
        self.x = Suit('x', 'suit X')

    def tearDown(self):
        del self.x

    def test_eq(self):
        self.assertTrue(self.x == Suit('x', 'suit Z'))
        self.assertFalse(self.x == Suit('y', 'suit X'))

    def test_ne(self):
        self.assertFalse(self.x != Suit('x', 'suit Z'))
        self.assertTrue(self.x != Suit('y', 'suit X'))


class TestSuitSet(unittest.TestCase):
    def setUp(self):
        self.x = Suit('x', 'suit X')
        self.y = Suit('y', 'suit Y')
        self.z = Suit('z', 'suit Z')
        self.xy = SuitSet([self.x, self.y,])
        self.yz = SuitSet([self.y, self.z,])
        self.yx = SuitSet([self.y, self.x,])

    def tearDown(self):
        del self.x
        del self.y
        del self.z
        del self.xy
        del self.yz
        del self.yx

    def test_eq(self):
        self.assertFalse(self.xy == self.yz)
        self.assertTrue(self.xy == self.yx)

    def test_ne(self):
        self.assertTrue(self.xy != self.yz)
        self.assertFalse(self.xy != self.yx)

    def test_contains(self):
        self.assertTrue(self.x in self.xy)
        self.assertTrue(self.y in self.yx)
        self.assertFalse(self.x in self.yz)

    def test_getitem(self):
        self.assertEqual(self.xy[self.x.code], self.x)
        self.assertNotEqual(self.yz[self.y.code], self.x)
        with self.assertRaises(KeyError):
            self.xy['a']


class TestCard(unittest.TestCase):
    def setUp(self):
        self.a = Rank('A', 'rank A', 1)
        self.b = Rank('B', 'rank B', 2)
        self.x = Suit('x', 'suit X')
        self.y = Suit('y', 'suit Y')
        self.ax = Card(self.a, self.x)

    def tearDown(self):
        del self.a
        del self.b
        del self.x
        del self.y
        del self.ax

    def test_eq(self):
        self.assertEqual(self.ax, Card(self.a, self.x))

    def test_ne(self):
        self.assertNotEqual(self.ax, Card(self.a, self.y))
        self.assertNotEqual(self.ax, Card(self.b, self.x))
        self.assertNotEqual(self.ax, Card(self.b, self.y))

    def test_gt(self):
        self.assertFalse(self.ax > Card(self.a, self.x))
        self.assertFalse(self.ax > Card(self.a, self.y))
        self.assertTrue(Card(self.b, self.x) > self.ax)
        self.assertTrue(Card(self.b, self.y) > self.ax)

    def test_ge(self):
        self.assertTrue(self.ax >= Card(self.a, self.x))
        self.assertTrue(self.ax >= Card(self.a, self.y))
        self.assertTrue(Card(self.b, self.x) >= self.ax)
        self.assertTrue(Card(self.b, self.y) >= self.ax)

    def test_lt(self):
        self.assertFalse(self.ax < Card(self.a, self.x))
        self.assertFalse(self.ax < Card(self.a, self.y))
        self.assertFalse(Card(self.b, self.x) < self.ax)
        self.assertFalse(Card(self.b, self.y) < self.ax)

    def test_le(self):
        self.assertTrue(self.ax <= Card(self.a, self.x))
        self.assertTrue(self.ax <= Card(self.a, self.y))
        self.assertFalse(Card(self.b, self.x) <= self.ax)
        self.assertFalse(Card(self.b, self.y) <= self.ax)


class TestCardSet(unittest.TestCase):
    def setUp(self):
        a = Rank('A', 'rank A', 1)
        b = Rank('B', 'rank B', 2)
        x = Suit('x', 'suit X')
        y = Suit('y', 'suit Y')
        self.ax = Card(a, x)
        self.ay = Card(a, y)
        self.bx = Card(b, x)
        self.by = Card(b, y)
        self.axby = CardSet([self.ax, self.by,])

    def tearDown(self):
        del self.ax
        del self.ay
        del self.bx
        del self.by
        del self.axby

    def test_eq(self):
        self.assertTrue(self.axby == CardSet([self.ax, self.by,]))
        self.assertTrue(self.axby == CardSet([self.by, self.ax,]))
        self.assertFalse(self.axby == CardSet([self.ax, self.bx,]))

    def test_ne(self):
        self.assertFalse(self.axby != CardSet([self.ax, self.by,]))
        self.assertFalse(self.axby != CardSet([self.by, self.ax,]))
        self.assertTrue(self.axby != CardSet([self.ax, self.bx,]))

    def test_contains(self):
        self.assertTrue(self.ax in self.axby)
        self.assertFalse(self.by in CardSet([self.ax, self.bx,]))
        self.assertFalse(self.ay in self.axby)

    def test_getitem(self):
        self.assertEqual(self.axby[self.ax.code], self.ax)
        self.assertNotEqual(self.axby[self.by.code], self.ax)
        with self.assertRaises(KeyError):
            self.axby[self.bx.code]


class TestDeck(unittest.TestCase):
    def setUp(self):
        a = Rank('A', 'rank A', 1)
        b = Rank('B', 'rank B', 2)
        x = Suit('x', 'suit X')
        y = Suit('y', 'suit Y')
        self.ax = Card(a, x)
        self.ay = Card(a, y)
        self.bx = Card(b, x)
        self.by = Card(b, y)
        self.axby = Deck([self.ax, self.by,])

    def tearDown(self):
        del self.ax
        del self.ay
        del self.bx
        del self.by
        del self.axby

    def test_eq(self):
        self.assertTrue(self.axby == Deck([self.ax, self.by,]))
        self.assertFalse(self.axby == Deck([self.by, self.ax,]))
        self.assertFalse(self.axby == Deck([self.ax, self.bx,]))

    def test_ne(self):
        self.assertFalse(self.axby != Deck([self.ax, self.by,]))
        self.assertTrue(self.axby != Deck([self.by, self.ax,]))
        self.assertTrue(self.axby != Deck([self.ax, self.bx,]))

    def test_contains(self):
        self.assertTrue(self.ax in self.axby)
        self.assertFalse(self.by in Deck([self.ax, self.bx,]))
        self.assertFalse(self.ay in self.axby)

    def test_getitem(self):
        self.assertEqual(self.axby[0], self.ax)
        self.assertNotEqual(self.axby[1], self.ax)
        with self.assertRaises(IndexError):
            self.axby[2]

    def test_delitem(self):
        del self.axby[0]
        self.assertNotIn(self.ax, self.axby)
        with self.assertRaises(IndexError):
            del self.axby[1]

    def test_push(self):
        self.axby.push(self.ay)
        self.assertEqual(self.axby[-1], self.ay)

    def test_pop(self):
        by = self.axby.pop()
        self.assertEqual(by, self.by)
        self.assertNotEqual(self.axby[-1], self.by)

    def test_unshift(self):
        self.axby.unshift(self.ay)
        self.assertEqual(self.axby[0], self.ay)

    def test_shift(self):
        ax = self.axby.shift()
        self.assertEqual(ax, self.ax)
        self.assertNotEqual(self.axby[0], self.ax)


if __name__ == '__main__':
    unittest.main()
