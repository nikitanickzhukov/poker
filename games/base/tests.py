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
        self.deck = StandardDeck()
        self.deck.shuffle()

    def tearDown(self):
        del self.deck

    def test_init(self):
        a = self.deck.pop()
        b = self.deck.pop()
        c = self.deck.pop()
        TestStreet1(a, b)
        with self.assertRaises(AssertionError):
            TestStreet1(a)
        with self.assertRaises(AssertionError):
            TestStreet1(a, b, c)

    def test_contains(self):
        a = self.deck.pop()
        b = self.deck.pop()
        c = self.deck.pop()
        self.assertIn(a, TestStreet1(a, b))
        self.assertIn(a, TestStreet1(b, a))
        self.assertNotIn(c, TestStreet1(a, b))


class KitTestCase(TestCase):
    def setUp(self):
        self.deck = StandardDeck()
        self.deck.shuffle()

    def tearDown(self):
        del self.deck

    def test_init(self):
        a = self.deck.pop()
        b = self.deck.pop()
        c = self.deck.pop()
        d = self.deck.pop()
        street1 = TestStreet1(a, b)
        street2 = TestStreet2(c)
        TestKit()
        TestKit(street1)
        TestKit(street1, street2)
        with self.assertRaises(AssertionError):
            TestKit(street2, street1)
        TestKit(a, b)
        TestKit(a, b, c)
        with self.assertRaises(AssertionError):
            TestKit(a)
        with self.assertRaises(AssertionError):
            TestKit(a, b, c, d)

    def test_contains(self):
        a = self.deck.pop()
        b = self.deck.pop()
        c = self.deck.pop()
        d = self.deck.pop()
        self.assertIn(a, TestKit(TestStreet1(a, b)))
        self.assertIn(c, TestKit(TestStreet1(a, b), TestStreet2(c)))
        self.assertNotIn(d, TestKit(TestStreet1(a, b), TestStreet2(c)))

    def test_append(self):
        a = self.deck.pop()
        b = self.deck.pop()
        c = self.deck.pop()
        d = self.deck.pop()
        kit = TestKit()
        kit.append(TestStreet1(a, b))
        self.assertIn(a, kit)
        kit.append(c)
        self.assertIn(c, kit)
        with self.assertRaises(AssertionError):
            kit.append(TestStreet2(d))
        with self.assertRaises(AssertionError):
            kit.append(d)


class ActionTestCase(TestCase):
    def test_fold(self):
        Fold()
        Fold(chips=0)
        with self.assertRaises(AssertionError):
            Fold(chips=1)
        with self.assertRaises(AssertionError):
            Fold(chips=-1)

    def test_check(self):
        Check()
        Check(chips=0)
        with self.assertRaises(AssertionError):
            Check(chips=1)
        with self.assertRaises(AssertionError):
            Check(chips=-1)

    def test_call(self):
        Call(chips=1)
        with self.assertRaises(AssertionError):
            Call()
        with self.assertRaises(AssertionError):
            Call(chips=0)
        with self.assertRaises(AssertionError):
            Call(chips=-1)

    def test_bet(self):
        Bet(chips=1)
        with self.assertRaises(AssertionError):
            Bet()
        with self.assertRaises(AssertionError):
            Bet(chips=0)
        with self.assertRaises(AssertionError):
            Bet(chips=-1)

    def test_raise(self):
        Raise(chips=1)
        with self.assertRaises(AssertionError):
            Raise()
        with self.assertRaises(AssertionError):
            Raise(chips=0)
        with self.assertRaises(AssertionError):
            Raise(chips=-1)
