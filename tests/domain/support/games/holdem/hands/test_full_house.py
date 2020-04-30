from unittest import TestCase

from domain.generic.cards import cardset
from domain.support.games.holdem import Pocket, Board, Identifier, FullHouse


class FullHouseTestCase(TestCase):
    def test_full_house(self):
        # Full house, a set and a pair on the board
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['Ac'], cardset['3c'], cardset['2d'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ cardset['As'], cardset['Ad'], cardset['Ac'] ]))
        self.assertEqual(set(hand[3:5]), set([ cardset['3s'], cardset['3c'] ]))

        # Full house, a trips and a pair on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ac'], cardset['2c'], cardset['2d'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ cardset['2s'], cardset['2d'], cardset['2c'] ]))
        self.assertEqual(set(hand[3:5]), set([ cardset['As'], cardset['Ac'] ]))

        # Full house, a pocket pair and a trips on the board
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['3c'], cardset['3d'], cardset['2d'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ cardset['3s'], cardset['3d'], cardset['3c'] ]))
        self.assertEqual(set(hand[3:5]), set([ cardset['As'], cardset['Ad'] ]))

        # Full house, on the board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['3c'], cardset['3d'], cardset['6d'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ cardset['3s'], cardset['3d'], cardset['3c'] ]))
        self.assertEqual(set(hand[3:5]), set([ cardset['6d'], cardset['6s'] ]))
