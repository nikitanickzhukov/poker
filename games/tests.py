import unittest

from .decks import HoldemDeck
from .hands import HoldemHand
from .boards import HoldemBoard


class DeckTestCase(unittest.TestCase):
    def setUp(self):
        self.a = HoldemDeck()
        self.b = HoldemDeck()

    def tearDown(self):
        del self.a
        del self.b

    def test_eq(self):
        self.assertTrue(self.a == self.b)
        self.b.shuffle()
        self.assertFalse(self.a == self.b)

    def test_ne(self):
        self.assertFalse(self.a != self.b)
        self.b.shuffle()
        self.assertTrue(self.a != self.b)

    def test_contains(self):
        c = self.a[0]
        self.assertTrue(c in self.a)
        c = self.a.shift()
        self.assertFalse(c in self.a)

    def test_getitem(self):
        c = self.a[0]
        with self.assertRaises(IndexError):
            self.a[len(self.a)]

    def test_delitem(self):
        c = self.a[0]
        self.assertIn(c, self.a)
        del self.a[0]
        self.assertNotIn(c, self.a)
        with self.assertRaises(IndexError):
            del self.a[len(self.a)]

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
