import unittest

from cards import StandardDeck
from .streets import Street
from .kits import Kit


class TestStreet1(Street):
    length = 2

class TestStreet2(Street):
    length = 1

class TestKit(Kit):
    street_classes = (TestStreet1, TestStreet2,)


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
        TestStreet1(m, n)
        with self.assertRaises(AssertionError):
            TestStreet1(m)
        with self.assertRaises(AssertionError):
            TestStreet1(m, n, o)
        with self.assertRaises(AssertionError):
            TestStreet1(m, self.d)

    def test_eq(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        self.assertEqual(TestStreet1(m, n), TestStreet1(m, n))
        self.assertEqual(TestStreet1(m, n), TestStreet1(n, m))
        self.assertNotEqual(TestStreet1(m, n), TestStreet1(m, o))

    def test_contains(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        self.assertIn(m, TestStreet1(m, n))
        self.assertIn(m, TestStreet1(n, m))
        self.assertNotIn(o, TestStreet1(m, n))


class KitTestCase(unittest.TestCase):
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
        with self.assertRaises(AssertionError):
            TestKit(street2, street1)
        TestKit(m, n)
        TestKit(m, n, o)
        with self.assertRaises(AssertionError):
            TestKit(m)
        with self.assertRaises(AssertionError):
            TestKit(m, n, o, p)

    def test_eq(self):
        m = self.d.shift()
        n = self.d.shift()
        o = self.d.shift()
        p = self.d.shift()
        q = self.d.shift()
        self.assertEqual(TestKit(TestStreet1(m, n)), TestKit(TestStreet1(m, n)))
        self.assertEqual(TestKit(TestStreet1(m, n)), TestKit(TestStreet1(n, m)))
        self.assertEqual(TestKit(TestStreet1(m, n), TestStreet2(o)), TestKit(TestStreet1(m, n), TestStreet2(o)))
        self.assertNotEqual(TestKit(TestStreet1(m, n), TestStreet2(o)), TestKit(TestStreet1(m, o), TestStreet2(n)))

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
        with self.assertRaises(AssertionError):
            b.append(TestStreet2(p))
        with self.assertRaises(AssertionError):
            b.append(p)


if __name__ == '__main__':
    unittest.main()
