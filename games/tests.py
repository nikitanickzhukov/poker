import unittest

from cards import Rank, Suit, Card
from .hands import Hand
from .boards import Board


class CustomHand(Hand):
    _length = 2

class CustomBoard(Board):
    _length = 2


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
        self.axby = CustomHand([self.ax, self.by,])

    def tearDown(self):
        del self.ax
        del self.ay
        del self.bx
        del self.by
        del self.axby

    def test_init(self):
        CustomHand([self.ax, self.ay,])
        with self.assertRaises(AssertionError):
            CustomHand([self.ax, self.ay, self.bx,])

    def test_eq(self):
        self.assertTrue(self.axby == CustomHand([self.ax, self.by,]))
        self.assertTrue(self.axby == CustomHand([self.by, self.ax,]))
        self.assertFalse(self.axby == CustomHand([self.ax, self.bx,]))

    def test_ne(self):
        self.assertFalse(self.axby != CustomHand([self.ax, self.by,]))
        self.assertFalse(self.axby != CustomHand([self.by, self.ax,]))
        self.assertTrue(self.axby != CustomHand([self.ax, self.bx,]))

    def test_contains(self):
        self.assertTrue(self.ax in self.axby)
        self.assertFalse(self.by in CustomHand([self.ax, self.bx,]))
        self.assertFalse(self.ay in self.axby)

    def test_getitem(self):
        self.assertEqual(self.axby[self.ax.code], self.ax)
        self.assertNotEqual(self.axby[self.by.code], self.ax)
        with self.assertRaises(KeyError):
            self.axby[self.bx.code]

    def test_append(self):
        q = CustomHand([self.ax,])
        q.append(self.bx)
        self.assertIn(self.bx, q)
        with self.assertRaises(AssertionError):
            q.append(self.by)


class TestBoard(unittest.TestCase):
    def setUp(self):
        a = Rank('A', 'rank A', 1)
        b = Rank('B', 'rank B', 2)
        x = Suit('x', 'suit X')
        y = Suit('y', 'suit Y')
        self.ax = Card(a, x)
        self.ay = Card(a, y)
        self.bx = Card(b, x)
        self.by = Card(b, y)
        self.axby = CustomBoard([self.ax, self.by,])

    def tearDown(self):
        del self.ax
        del self.ay
        del self.bx
        del self.by
        del self.axby

    def test_init(self):
        CustomBoard([self.ax, self.ay,])
        with self.assertRaises(AssertionError):
            CustomBoard([self.ax, self.ay, self.bx,])

    def test_eq(self):
        self.assertTrue(self.axby == CustomBoard([self.ax, self.by,]))
        self.assertFalse(self.axby == CustomBoard([self.by, self.ax,]))
        self.assertFalse(self.axby == CustomBoard([self.ax, self.bx,]))

    def test_ne(self):
        self.assertFalse(self.axby != CustomBoard([self.ax, self.by,]))
        self.assertTrue(self.axby != CustomBoard([self.by, self.ax,]))
        self.assertTrue(self.axby != CustomBoard([self.ax, self.bx,]))

    def test_contains(self):
        self.assertTrue(self.ax in self.axby)
        self.assertFalse(self.by in CustomBoard([self.ax, self.bx,]))
        self.assertFalse(self.ay in self.axby)

    def test_getitem(self):
        self.assertEqual(self.axby[0], self.ax)
        self.assertNotEqual(self.axby[1], self.ax)
        with self.assertRaises(IndexError):
            self.axby[2]

    def test_append(self):
        q = CustomBoard([self.ax,])
        q.append(self.bx)
        self.assertIn(self.bx, q)
        with self.assertRaises(AssertionError):
            q.append(self.by)


if __name__ == '__main__':
    unittest.main()
