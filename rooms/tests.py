from unittest import TestCase

from .gamblers import Gambler
from .boxes import Box
from .tables import Table


class GamblerTestCase(TestCase):
    def test_init(self):
        Gambler(nickname='a')
        with self.assertRaises(ValueError):
            Gambler(nickname='')


class BoxTestCase(TestCase):
    def setUp(self):
        self.x = Gambler(nickname='x')

    def tearDown(self):
        del self.x

    def test_init(self):
        Box()

    def test_occupy(self):
        a = Box()
        a.occupy(gambler=self.x, chips=1)
        with self.assertRaises(AssertionError):
            a.occupy(gambler=self.x, chips=1)

    def test_leave(self):
        a = Box()
        with self.assertRaises(AssertionError):
            a.leave()

    def test_chips(self):
        a = Box()
        a.occupy(gambler=self.x, chips=1)
        a.chips += 1
        self.assertEqual(a.chips, 2)
        a.chips -= 2
        self.assertEqual(a.chips, 0)
        with self.assertRaises(ValueError):
            a.chips -= 1


class TableTestCase(TestCase):
    def setUp(self):
        self.x = Gambler(nickname='x')

    def tearDown(self):
        del self.x

    def test_init(self):
        Table()

    def test_occupy(self):
        a = Table()
        a.occupy_box(box_num=2, gambler=self.x, chips=1)
        self.assertFalse(a.box_is_empty(box_num=2))
        self.assertEqual(a.boxes[2].gambler, self.x)
        self.assertEqual(a.boxes[2].chips, 1)
        with self.assertRaises(ValueError):
            a.occupy_box(box_num=3, gambler=self.x, chips=1)

        y = Gambler(nickname='y')
        with self.assertRaises(AssertionError):
            a.occupy_box(box_num=2, gambler=y, chips=2)
        a.occupy_box(box_num=3, gambler=y, chips=2)
        self.assertFalse(a.box_is_empty(box_num=3))
        self.assertEqual(a.boxes[3].gambler, y)
        self.assertEqual(a.boxes[3].chips, 2)

    def test_leave(self):
        a = Table()
        self.assertTrue(a.box_is_empty(box_num=2))
        with self.assertRaises(AssertionError):
            a.leave_box(box_num=2)
        a.occupy_box(box_num=2, gambler=self.x, chips=1)
        self.assertFalse(a.box_is_empty(box_num=2))
        a.leave_box(box_num=2)
        self.assertTrue(a.box_is_empty(box_num=2))

    def test_empty_boxes(self):
        a = Table()
        self.assertEqual(a.boxes, a.empty_boxes)
        a.occupy_box(box_num=2, gambler=self.x, chips=1)
        self.assertNotIn(a.boxes[2], a.empty_boxes)

    def test_active_boxes(self):
        a = Table()
        self.assertEqual(len(a.active_boxes), 0)
        a.occupy_box(box_num=2, gambler=self.x, chips=1)
        self.assertIn(a.boxes[2], a.active_boxes)
