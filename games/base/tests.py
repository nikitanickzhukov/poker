from unittest import TestCase

from cards import StandardDeck
from .streets import Street
from .kits import Kit
from .actions import Fold, Check, Call, Bet, Raise


class TestStreet1(Street):
    length = 2

class TestStreet2(Street):
    length = 1

class TestKit(Kit):
    street_classes = (TestStreet1, TestStreet2)


class StreetTestCase(TestCase):
    def setUp(self):
        self.d = StandardDeck()
        self.d.shuffle()

    def tearDown(self):
        del self.d

    def test_init(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        TestStreet1(m, n)
        with self.assertRaises(ValueError):
            TestStreet1(m)
        with self.assertRaises(ValueError):
            TestStreet1(m, n, o)
        with self.assertRaises(TypeError):
            TestStreet1(m, self.d)

    def test_contains(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        self.assertIn(m, TestStreet1(m, n))
        self.assertIn(m, TestStreet1(n, m))
        self.assertNotIn(o, TestStreet1(m, n))


class KitTestCase(TestCase):
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
        street1 = TestStreet1(m, n)
        street2 = TestStreet2(o)
        TestKit()
        TestKit(street1)
        TestKit(street1, street2)
        with self.assertRaises(TypeError):
            TestKit(street2, street1)
        TestKit(m, n)
        TestKit(m, n, o)
        with self.assertRaises(ValueError):
            TestKit(m)
        with self.assertRaises(ValueError):
            TestKit(m, n, o, p)

    def test_contains(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        p = self.d.shift()
        self.assertIn(m, TestKit(TestStreet1(m, n)))
        self.assertIn(o, TestKit(TestStreet1(m, n), TestStreet2(o)))
        self.assertNotIn(p, TestKit(TestStreet1(m, n), TestStreet2(o)))

    def test_append(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        p = self.d.shift()
        b = TestKit()
        b.append(TestStreet1(m, n))
        self.assertIn(m, b)
        b.append(o)
        self.assertIn(o, b)
        with self.assertRaises(ValueError):
            b.append(TestStreet2(p))
        with self.assertRaises(ValueError):
            b.append(p)


class ActionTestCase(TestCase):
    def test_fold(self):
        Fold()
        Fold(amount=0)
        with self.assertRaises(ValueError):
            Fold(amount=1)
        with self.assertRaises(ValueError):
            Fold(amount=-1)

    def test_check(self):
        Check()
        Check(amount=0)
        with self.assertRaises(ValueError):
            Check(amount=1)
        with self.assertRaises(ValueError):
            Check(amount=-1)

    def test_call(self):
        Call(amount=1)
        with self.assertRaises(ValueError):
            Call()
        with self.assertRaises(ValueError):
            Call(amount=0)
        with self.assertRaises(ValueError):
            Call(amount=-1)

    def test_bet(self):
        Bet(amount=1)
        with self.assertRaises(ValueError):
            Bet()
        with self.assertRaises(ValueError):
            Bet(amount=0)
        with self.assertRaises(ValueError):
            Bet(amount=-1)

    def test_raise(self):
        Raise(amount=1)
        with self.assertRaises(ValueError):
            Raise()
        with self.assertRaises(ValueError):
            Raise(amount=0)
        with self.assertRaises(ValueError):
            Raise(amount=-1)
