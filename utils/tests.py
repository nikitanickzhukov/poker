from unittest import TestCase

from .attrs import Attr, ValidatedAttr, TypedAttr, StringAttr, IntegerAttr


class AttrTestCase(TestCase):
    def test_attr(self):
        def set_bb(obj, val):
            obj.b = val

        class Test():
            a = Attr()
            b = Attr(readable=False)
            c = Attr(writable=False)
            bb = Attr(setter=set_bb)
            cc = Attr(getter=lambda obj: obj.c)

            def __init__(self, a, b, c):
                self._a = a
                self._b = b
                self._c = c

        test = Test(a=1, b=2, c=3)
        self.assertEqual(test.a, 1)
        with self.assertRaises(AttributeError):
            b = test.b
        self.assertEqual(test.c, 3)
        self.assertEqual(test.cc, 3)
        test.a = 4
        self.assertEqual(test.a, 4)
        test.b = 5
        self.assertEqual(test._b, 5)
        with self.assertRaises(AttributeError):
            test.c = 6
        test._c = 6
        self.assertEqual(test.c, 6)
        self.assertEqual(test.cc, 6)

    def test_validated(self):
        class Test():
            a = ValidatedAttr(validate=lambda obj, val: val == 'a')
            r24 = ValidatedAttr(validate=(lambda obj, val: val >= 2, lambda obj, val: val <= 4))

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
            b = TypedAttr(type=int, nullable=True)

        test = Test()
        test.a = 'a'
        with self.assertRaises(TypeError):
            test.a = 1
        with self.assertRaises(TypeError):
            test.a = None
        test.a = 'b'

        test.b = 1
        test.b = None

    def test_string(self):
        class Test():
            a = StringAttr()
            b = StringAttr(min_length=1, max_length=2)

        test = Test()
        test.a = 'a'
        with self.assertRaises(TypeError):
            test.a = b'a'
        test.a = 'b'

        test.b = 'b'
        with self.assertRaises(ValueError):
            test.b = ''
        with self.assertRaises(ValueError):
            test.b = 'bbb'

    def test_integer(self):
        class Test():
            a = IntegerAttr()
            b = IntegerAttr(min_value=1, max_value=2)

        test = Test()
        test.a = 1
        with self.assertRaises(TypeError):
            test.a = 1.1
        test.a = 2

        test.b = 1
        with self.assertRaises(ValueError):
            test.b = 0
        with self.assertRaises(ValueError):
            test.b = 3
