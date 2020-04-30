from unittest import TestCase

from domain.generic.cards import cardset
from domain.support.games.omaha import Pocket, Board, Identifier, HighCard


class HighCardTestCase(TestCase):
    def test_high_card(self):
        # High card in the pocket
        pocket = Pocket(cardset['As'], cardset['2s'], cardset['4d'], cardset['3c'])
        board = Board(cardset['Qs'], cardset['7d'], cardset['Jh'], cardset['Kd'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], cardset['As'])
        self.assertEqual(hand[1], cardset['Kd'])
        self.assertIn(cardset['4d'], hand)

        # High card on the board
        pocket = Pocket(cardset['7s'], cardset['2s'], cardset['6c'], cardset['Tc'])
        board = Board(cardset['3s'], cardset['4d'], cardset['Jh'], cardset['Qd'], cardset['8s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], cardset['Qd'])
        self.assertEqual(hand[1], cardset['Jh'])
        self.assertIn(cardset['Tc'], hand)
        self.assertIn(cardset['7s'], hand)
