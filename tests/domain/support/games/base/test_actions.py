from unittest import TestCase

from domain.support.games.base.actions import Fold, Check, Call, Bet, Raise


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
