from unittest import TestCase

from domain.generic.cards import cardset
from domain.support.games.holdem import Pocket, Board, Identifier, Quads


class QuadsTestCase(TestCase):
    def test_quads(self):
        # Quads, a pocket pair
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['Ac'], cardset['Ah'], cardset['Jh'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual(set(hand[0:4]), set([ cardset['As'], cardset['Ad'], cardset['Ac'], cardset['Ah'] ]))
        self.assertEqual(hand[4], cardset['Jh'])

        # Quads, a trips on a board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ac'], cardset['Ah'], cardset['Ad'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual(set(hand[0:4]), set([ cardset['As'], cardset['Ad'], cardset['Ac'], cardset['Ah'] ]))
        self.assertEqual(hand[4], cardset['6s'])

        # Quads, on a board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['3c'], cardset['3h'], cardset['3d'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual(set(hand[0:4]), set([ cardset['3s'], cardset['3d'], cardset['3c'], cardset['3h'] ]))
        self.assertEqual(hand[4], cardset['As'])
