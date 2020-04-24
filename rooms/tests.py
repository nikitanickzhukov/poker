from unittest import TestCase

from .gamblers import Gambler
from .boxes import Box
from .tables import Table


class GamblerTestCase(TestCase):
    def test_init(self):
        Gambler(nickname='a')
        with self.assertRaises(AssertionError):
            Gambler(nickname='')


class BoxTestCase(TestCase):
    def setUp(self):
        self.gambler = Gambler(nickname='x')

    def tearDown(self):
        del self.gambler

    def test_occupy(self):
        box = Box()
        box.occupy(gambler=self.gambler, chips=1)
        with self.assertRaises(AssertionError):
            box.occupy(gambler=self.gambler, chips=1)

    def test_leave(self):
        box = Box()
        with self.assertRaises(AssertionError):
            box.leave()

    def test_chips(self):
        box = Box()
        box.occupy(gambler=self.gambler, chips=1)
        box.win_chips(chips=1)
        self.assertEqual(box.chips, 2)
        with self.assertRaises(AssertionError):
            box.win_chips(chips=-1)
        with self.assertRaises(AssertionError):
            box.lose_chips(chips=-1)
        box.lose_chips(chips=2)
        self.assertEqual(box.chips, 0)
        with self.assertRaises(AssertionError):
            box.lose_chips(chips=1)


class TableTestCase(TestCase):
    def setUp(self):
        self.gambler = Gambler(nickname='x')

    def tearDown(self):
        del self.gambler

    def test_occupy(self):
        table = Table()
        table.occupy_box(box_num=2, gambler=self.gambler, chips=1)
        self.assertFalse(table.box_is_empty(box_num=2))
        self.assertEqual(table.boxes[2].gambler, self.gambler)
        self.assertEqual(table.boxes[2].chips, 1)
        with self.assertRaises(AssertionError):
            table.occupy_box(box_num=3, gambler=self.gambler, chips=1)

        gambler = Gambler(nickname='y')
        with self.assertRaises(AssertionError):
            table.occupy_box(box_num=2, gambler=gambler, chips=2)
        table.occupy_box(box_num=3, gambler=gambler, chips=2)
        self.assertFalse(table.box_is_empty(box_num=3))
        self.assertEqual(table.boxes[3].gambler, gambler)
        self.assertEqual(table.boxes[3].chips, 2)

    def test_leave(self):
        table = Table()
        self.assertTrue(table.box_is_empty(box_num=2))
        with self.assertRaises(AssertionError):
            table.leave_box(box_num=2)
        table.occupy_box(box_num=2, gambler=self.gambler, chips=1)
        self.assertFalse(table.box_is_empty(box_num=2))
        table.leave_box(box_num=2)
        self.assertTrue(table.box_is_empty(box_num=2))

    def test_empty_boxes(self):
        table = Table()
        self.assertEqual(table.boxes, table.empty_boxes)
        table.occupy_box(box_num=2, gambler=self.gambler, chips=1)
        self.assertNotIn(table.boxes[2], table.empty_boxes)

    def test_busy_boxes(self):
        table = Table()
        self.assertEqual(len(table.busy_boxes), 0)
        table.occupy_box(box_num=2, gambler=self.gambler, chips=1)
        self.assertIn(table.boxes[2], table.busy_boxes)
