from unittest import TestCase

from .players import Player
from .boxes import Box
from .tables import Table


class PlayerTestCase(TestCase):
    def test_init(self):
        Player(nickname='a')
        with self.assertRaises(AssertionError):
            Player(nickname='')


class BoxTestCase(TestCase):
    def setUp(self):
        self.x = Player(nickname='x')

    def tearDown(self):
        del self.x

    def test_init(self):
        Box()
        Box(player=self.x, chips=1)
        Box(player=self.x, chips=0)
        with self.assertRaises(AssertionError):
            Box(player=None, chips=1)
        with self.assertRaises(AssertionError):
            Box(player=self.x, chips=None)
        with self.assertRaises(AssertionError):
            Box(player=self.x, chips=-1)

    def test_occupy(self):
        a = Box()
        a.occupy(player=self.x, chips=1)
        with self.assertRaises(AssertionError):
            a.occupy(player=self.x, chips=1)

    def test_leave(self):
        a = Box(player=self.x, chips=1)
        a.leave()
        with self.assertRaises(AssertionError):
            a.leave()

    def test_chips(self):
        a = Box(player=self.x, chips=1)
        a.chips += 1
        self.assertEqual(a.chips, 2)
        a.chips -= 2
        self.assertEqual(a.chips, 0)
        with self.assertRaises(AssertionError):
            a.chips -= 1


class TableTestCase(TestCase):
    def setUp(self):
        self.x = Player(nickname='x')

    def tearDown(self):
        del self.x

    def test_init(self):
        Table()

    def test_occupy(self):
        a = Table()
        a.occupy_box(box_num=2, player=self.x, chips=1)
        self.assertFalse(a.box_is_empty(box_num=2))
        self.assertEqual(a.boxes[2].player, self.x)
        self.assertEqual(a.boxes[2].chips, 1)
        with self.assertRaises(AssertionError):
            a.occupy_box(box_num=3, player=self.x, chips=1)

        y = Player(nickname='y')
        with self.assertRaises(AssertionError):
            a.occupy_box(box_num=2, player=y, chips=2)
        a.occupy_box(box_num=3, player=y, chips=2)
        self.assertFalse(a.box_is_empty(box_num=3))
        self.assertEqual(a.boxes[3].player, y)
        self.assertEqual(a.boxes[3].chips, 2)

    def test_leave(self):
        a = Table()
        self.assertTrue(a.box_is_empty(box_num=2))
        with self.assertRaises(AssertionError):
            a.leave_box(box_num=2)
        a.occupy_box(box_num=2, player=self.x, chips=1)
        self.assertFalse(a.box_is_empty(box_num=2))
        a.leave_box(box_num=2)
        self.assertTrue(a.box_is_empty(box_num=2))
