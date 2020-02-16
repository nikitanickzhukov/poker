import unittest

from cards import Rank, Suit, Card
from .hands import Hand


class TestHand(unittest.TestCase):
    def setUp(self):
        a = Rank('A', 'rank A', 1)
        b = Rank('B', 'rank B', 2)
        x = Suit('x', 'suit X')
        y = Suit('y', 'suit Y')
        self.ax = Card(a, x)
        self.ay = Card(a, y)
        self.bx = Card(b, x)
        self.by = Card(b, y)
        self.axby = Hand([self.ax, self.by,])

    def tearDown(self):
        del self.ax
        del self.ay
        del self.bx
        del self.by
        del self.axby

    def test_init(self):
        class H(Hand):
            _length = 1
        with self.assertRaises(AssertionError):
            h = H([self.ax, self.by])

    def test_eq(self):
        self.assertTrue(self.axby == Hand([self.ax, self.by,]))
        self.assertTrue(self.axby == Hand([self.by, self.ax,]))
        self.assertFalse(self.axby == Hand([self.ax, self.bx,]))

    def test_ne(self):
        self.assertFalse(self.axby != Hand([self.ax, self.by,]))
        self.assertFalse(self.axby != Hand([self.by, self.ax,]))
        self.assertTrue(self.axby != Hand([self.ax, self.bx,]))

    def test_contains(self):
        self.assertTrue(self.ax in self.axby)
        self.assertFalse(self.by in Hand([self.ax, self.bx,]))
        self.assertFalse(self.ay in self.axby)

    def test_getitem(self):
        self.assertEqual(self.axby[self.ax.code], self.ax)
        self.assertNotEqual(self.axby[self.by.code], self.ax)
        with self.assertRaises(KeyError):
            self.axby[self.bx.code]

    def test_append(self):
        self.axby.append(self.bx)
        self.assertIn(self.bx, self.axby)
        class H(Hand):
            _length = 1
        h = H([self.ax,])
        with self.assertRaises(AssertionError):
            h.append(self.by)


if __name__ == '__main__':
    unittest.main()
