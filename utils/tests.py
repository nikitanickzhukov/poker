from unittest import TestCase

from .attrs import Attr, WritableAttr, ValidatedAttr, TypedAttr, StringAttr, IntegerAttr


class AttrTestCase(TestCase):
    def test_attr(self):
        class Test():
            a = Attr()
            def __init__(self, a):
                self._a = a

        test = Test(a=1)
        self.assertEqual(test.a, 1)
        with self.assertRaises(NotImplementedError):
            test.a = 2

    def test_writable(self):
        class Test():
            a = WritableAttr()
            def __init__(self, a):
                self._a = a

        test = Test(a=1)
        self.assertEqual(test.a, 1)
        test.a = 2
        self.assertEqual(test.a, 2)

    def test_validated(self):
        class Test():
            a = ValidatedAttr(validate=lambda x: x == 'a')
            r24 = ValidatedAttr(validate=(lambda x: x >= 2, lambda x: x <= 4))

        test = Test()
        test.a = 'a'
        with self.assertRaises(ValueError):
            test.a = 'b'

        test.r24 = 3
        with self.assertRaises(ValueError):
            test.r24 = 1
        with self.assertRaises(ValueError):
            test.r24 = 5

    def test_typed(self):
        class Test():
            a = TypedAttr(type=str)
            b = TypedAttr(type=int, validate=lambda x: x == 1)

        test = Test()
        test.a = 'a'
        with self.assertRaises(ValueError):
            test.a = 1
        test.a = 'b'

        test.b = 1
        with self.assertRaises(ValueError):
            test.b = 2

    def test_string(self):
        class Test():
            a = StringAttr()
            b = StringAttr(min_length=1, max_length=2)
            c = StringAttr(validate=lambda x: x == 'c')
            d = StringAttr(max_length=2, validate=lambda x: x.startswith('d'))

        test = Test()
        test.a = 'a'
        with self.assertRaises(ValueError):
            test.a = 1
        test.a = 'b'

        test.b = 'b'
        with self.assertRaises(ValueError):
            test.b = ''
        with self.assertRaises(ValueError):
            test.b = 'bbb'

        test.c = 'c'
        with self.assertRaises(ValueError):
            test.c = 'cc'

        test.d = 'dd'
        with self.assertRaises(ValueError):
            test.d = 'ddd'
        with self.assertRaises(ValueError):
            test.d = 'cd'

    def test_integer(self):
        class Test():
            a = IntegerAttr()
            b = IntegerAttr(min_value=1, max_value=2)
            c = IntegerAttr(validate=lambda x: x == 1)
            d = IntegerAttr(max_value=2, validate=lambda x: x != 1)

        test = Test()
        test.a = 1
        with self.assertRaises(ValueError):
            test.a = 1.1
        test.a = 2

        test.b = 1
        with self.assertRaises(ValueError):
            test.b = 0
        with self.assertRaises(ValueError):
            test.b = 3

        test.c = 1
        with self.assertRaises(ValueError):
            test.c = 2

        test.d = 2
        with self.assertRaises(ValueError):
            test.d = 3
        with self.assertRaises(ValueError):
            test.d = 1
