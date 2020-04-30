from unittest import TestCase

from domain.generic.cards import cardset
from domain.support.games.holdem import Pocket, Board, Identifier, Flush


class FlushTestCase(TestCase):
    def test_flush(self):
        # Flush, 2 in the pocket and 3 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Ac'], cardset['Qs'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual(hand[0], cardset['As'])
        self.assertEqual(hand[4], cardset['2s'])

        # Flush, 1 in the pocket and 4 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Js'], cardset['Qs'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual(hand[0], cardset['As'])
        self.assertEqual(hand[4], cardset['3s'])

        # Flush, on the board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3d'], cardset['Ad'], cardset['Jd'], cardset['Qd'], cardset['6d'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual(hand[0], cardset['Ad'])
        self.assertEqual(hand[4], cardset['3d'])
