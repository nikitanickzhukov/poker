import unittest

from ranks import Rank, RankSet
from suits import Suit, SuitSet
from cards import Card, CardSet


class TestRank(unittest.TestCase):
    def setUp(self):
        self.a = Rank('a', 'rank A', 1)
        self.b = Rank('b', 'rank B', 2)
        self.c = Rank('a', 'rank C', 3)

    def tearDown(self):
        del self.a
        del self.b
        del self.c

    def test_eq(self):
        self.assertEqual(self.a, self.c)

    def test_ne(self):
        self.assertNotEqual(self.a, self.b)
        self.assertNotEqual(self.b, self.c)

    def test_gt(self):
        self.assertTrue(self.c > self.b > self.a)

    def test_ge(self):
        self.assertTrue(self.c >= self.b >= self.a)

    def test_lt(self):
        self.assertTrue(self.a < self.b < self.c)

    def test_le(self):
        self.assertTrue(self.a <= self.b <= self.c)


class TestRankSet(unittest.TestCase):
    def setUp(self):
        self.a = Rank('a', 'rank A', 1)
        self.b = Rank('b', 'rank B', 2)
        self.c = Rank('c', 'rank C', 3)
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

    def test_get(self):
        self.assertEqual(self.ab.get(self.a.code), self.a)
        self.assertNotEqual(self.bc.get(self.b.code), self.a)


class TestSuit(unittest.TestCase):
    def setUp(self):
        self.x = Suit('x', 'suit X')
        self.y = Suit('y', 'suit Y')
        self.z = Suit('x', 'suit Z')

    def tearDown(self):
        del self.x
        del self.y
        del self.z

    def test_eq(self):
        self.assertEqual(self.x, self.z)

    def test_ne(self):
        self.assertNotEqual(self.x, self.y)
        self.assertNotEqual(self.y, self.z)


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
        self.assertEqual(self.xy, self.yx)

    def test_ne(self):
        self.assertNotEqual(self.xy, self.yz)
        self.assertNotEqual(self.yz, self.yx)

    def test_contains(self):
        self.assertTrue(self.x in self.xy)
        self.assertTrue(self.y in self.yx)
        self.assertTrue(self.x not in self.yz)

    def test_get(self):
        self.assertEqual(self.xy.get(self.x.code), self.x)
        self.assertNotEqual(self.yz.get(self.y.code), self.x)


class TestCard(unittest.TestCase):
    def setUp(self):
        self.a = Rank('a', 'rank A', 1)
        self.b = Rank('b', 'rank B', 2)
        self.c = Rank('a', 'rank C', 3)
        self.j = Rank('j', 'rank J', 4)
        self.x = Suit('x', 'suit X')
        self.y = Suit('y', 'suit Y')
        self.z = Suit('x', 'suit Z')
        self.ax = Card(self.a, self.x)
        self.ay = Card(self.a, self.y)
        self.bx = Card(self.b, self.x)
        self.by = Card(self.b, self.y)
        self.cz = Card(self.c, self.z)
        self.jj = Card(self.j)

    def tearDown(self):
        del self.a
        del self.b
        del self.c
        del self.x
        del self.y
        del self.z
        del self.ax
        del self.ay
        del self.bx
        del self.by
        del self.cz
        del self.jj

    def test_eq(self):
        self.assertEqual(self.ax, self.cz)

    def test_ne(self):
        self.assertNotEqual(self.ax, self.by)
        self.assertNotEqual(self.ax, self.bx)
        self.assertNotEqual(self.ax, self.ay)
        self.assertNotEqual(self.ax, self.jj)

    def test_gt(self):
        self.assertTrue(self.jj > self.by > self.ax)

    def test_ge(self):
        self.assertTrue(self.bx >= self.by >= self.ax >= self.ay)

    def test_lt(self):
        self.assertTrue(self.ay < self.by < self.jj)

    def test_le(self):
        self.assertTrue(self.ax <= self.ay <= self.bx <= self.by)


class TestCardSet(unittest.TestCase):
    def setUp(self):
        self.a = Rank('a', 'rank A', 1)
        self.b = Rank('b', 'rank B', 2)
        self.j = Rank('j', 'rank J', 3)
        self.x = Suit('x', 'suit X')
        self.y = Suit('y', 'suit Y')
        self.ax = Card(self.a, self.x)
        self.ay = Card(self.a, self.y)
        self.bx = Card(self.b, self.x)
        self.by = Card(self.b, self.y)
        self.jj = Card(self.j)
        self.axby = CardSet([self.ax, self.by,])
        self.byax = CardSet([self.by, self.ax,])
        self.ayjj = CardSet([self.ay, self.jj,])

    def tearDown(self):
        del self.a
        del self.b
        del self.j
        del self.x
        del self.y
        del self.ax
        del self.ay
        del self.bx
        del self.by
        del self.jj
        del self.axby
        del self.byax
        del self.ayjj

    def test_eq(self):
        self.assertEqual(self.axby, self.byax)

    def test_ne(self):
        self.assertNotEqual(self.axby, self.ayjj)
        self.assertNotEqual(self.ayjj, self.byax)

    def test_contains(self):
        self.assertTrue(self.ax in self.axby)
        self.assertTrue(self.jj in self.ayjj)
        self.assertTrue(self.ay not in self.axby)

    def test_get(self):
        self.assertEqual(self.axby.get(self.ax.code), self.ax)
        self.assertNotEqual(self.ayjj.get(self.jj.code), self.ay)


if __name__ == '__main__':
    unittest.main()
