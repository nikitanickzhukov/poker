from unittest import TestCase

from engine.domain.model.chips import Chips
from engine.domain.model.game.base.decision import Fold, Check, Call, Bet, Raise


class DecisionTestCase(TestCase):
    def test_fold(self):
        Fold()
        Fold(chips=Chips(amount=0))
        with self.assertRaises(AssertionError):
            Fold(chips=Chips(amount=1))

    def test_check(self):
        Check()
        Check(chips=Chips(amount=0))
        with self.assertRaises(AssertionError):
            Check(chips=Chips(amount=1))

    def test_call(self):
        Call(chips=Chips(amount=1))
        with self.assertRaises(AssertionError):
            Call()
        with self.assertRaises(AssertionError):
            Call(chips=Chips(amount=0))

    def test_bet(self):
        Bet(chips=Chips(amount=1))
        with self.assertRaises(AssertionError):
            Bet()
        with self.assertRaises(AssertionError):
            Bet(chips=Chips(amount=0))

    def test_raise(self):
        Raise(chips=Chips(amount=1))
        with self.assertRaises(AssertionError):
            Raise()
        with self.assertRaises(AssertionError):
            Raise(chips=Chips(amount=0))
