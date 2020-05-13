from unittest import TestCase

from domain.model.cards.props import Prop


class PropTestCase(TestCase):
    def setUp(self):
        self.prop = Prop(code='A', name='Prop A', weight=3)

    def tearDown(self):
        del self.prop

    def test_init(self):
        with self.assertRaises(AssertionError):
            Prop(code='AA', name='Prop A', weight=3)
        with self.assertRaises(AssertionError):
            Prop(code='A', name='', weight=3)
        with self.assertRaises(AssertionError):
            Prop(code='A', name='Prop A', weight=-1)

    def test_attrs(self):
        self.assertEqual(self.prop.code, 'A')
        self.assertEqual(self.prop.name, 'Prop A')
        self.assertEqual(self.prop.weight, 3)

    def test_eq(self):
        self.assertEqual(self.prop, Prop(code='B', name='Prop B', weight=3))
        self.assertNotEqual(self.prop, Prop(code='B', name='Prop B', weight=1))
        self.assertNotEqual(self.prop, Prop(code='B', name='Prop B', weight=5))

    def test_gt(self):
        self.assertFalse(self.prop > Prop(code='B', name='Prop B', weight=3))
        self.assertTrue(self.prop > Prop(code='B', name='Prop B', weight=1))
        self.assertFalse(self.prop > Prop(code='B', name='Prop B', weight=5))
