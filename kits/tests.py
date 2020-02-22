import unittest

from cards import StandardDeck
from .streets import Flop, Turn, River
from .boards import HoldemBoard


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


class StreetTestCase(unittest.TestCase):
    def setUp(self):
        self.d = StandardDeck()
        self.d.shuffle()

    def tearDown(self):
        del self.d

    def test_init(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        p = self.d.shift()
        Flop(m, n, o)
        with self.assertRaises(AssertionError):
            Flop(m, n)
        with self.assertRaises(AssertionError):
            Flop(m, n, o, p)
        with self.assertRaises(AssertionError):
            Flop(self.d)

    def test_eq(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        p = self.d.shift()
        self.assertEqual(Flop(m, n, o), Flop(m, n, o))
        self.assertEqual(Flop(m, n, o), Flop(o, n, m))
        self.assertNotEqual(Flop(m, n, o), Flop(m, n, p))

    def test_contains(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        p = self.d.shift()
        self.assertIn(m, Flop(m, n, o))
        self.assertIn(m, Flop(o, n, m))
        self.assertNotIn(p, Flop(m, n, o))


class BoardTestCase(unittest.TestCase):
    def setUp(self):
        self.d = StandardDeck()
        self.d.shuffle()

    def tearDown(self):
        del self.d

    def test_init(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        p = self.d.shift()
        q = self.d.shift()
        r = self.d.shift()
        flop = Flop(m, n, o)
        turn = Turn(p)
        river = River(q)
        HoldemBoard()
        HoldemBoard(flop)
        HoldemBoard(flop, turn)
        HoldemBoard(flop, turn, river)
        with self.assertRaises(AssertionError):
            HoldemBoard(turn, river, flop)
        with self.assertRaises(AssertionError):
            HoldemBoard(flop, turn, river, River(r))
        HoldemBoard(m, n, o)
        HoldemBoard(m, n, o, p)
        HoldemBoard(m, n, o, p, q)
        with self.assertRaises(AssertionError):
            HoldemBoard(m, n)
        with self.assertRaises(AssertionError):
            HoldemBoard(m, n, o, p, q, r)

    def test_eq(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        p = self.d.shift()
        q = self.d.shift()
        self.assertEqual(HoldemBoard(Flop(m, n, o)), HoldemBoard(Flop(m, n, o)))
        self.assertEqual(HoldemBoard(Flop(m, n, o)), HoldemBoard(Flop(o, n, m)))
        self.assertNotEqual(HoldemBoard(Flop(m, n, o), Turn(p)), HoldemBoard(Flop(m, n, p), Turn(o)))
        self.assertEqual(HoldemBoard(Flop(m, n, o), Turn(p), River(q)), HoldemBoard(Flop(m, n, o), Turn(p), River(q)))
        self.assertNotEqual(HoldemBoard(Flop(m, n, o), Turn(p), River(q)), HoldemBoard(Flop(m, n, o), Turn(q), River(p)))

    def test_contains(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        p = self.d.shift()
        q = self.d.shift()
        r = self.d.shift()
        self.assertIn(m, HoldemBoard(Flop(m, n, o)))
        self.assertIn(p, HoldemBoard(Flop(m, n, o), Turn(p)))
        self.assertIn(q, HoldemBoard(Flop(m, n, o), Turn(p), River(q)))
        self.assertNotIn(r, HoldemBoard(Flop(m, n, o), Turn(p), River(q)))

    def test_append(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        p = self.d.shift()
        q = self.d.shift()
        r = self.d.shift()
        b = HoldemBoard()
        b.append(Flop(m, n, o))
        self.assertIn(m, b)
        b.append(Turn(p))
        self.assertIn(p, b)
        with self.assertRaises(AssertionError):
            b.append(Turn(q))
        b.append(q)
        self.assertIn(q, b)


if __name__ == '__main__':
    unittest.main()
