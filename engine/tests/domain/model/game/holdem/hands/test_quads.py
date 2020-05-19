from unittest import TestCase

from engine.domain.model.card import cards52 as c52
from engine.domain.model.game.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, Quads,
)


class QuadsTestCase(TestCase):
    def test_pp(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', 'Ad')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ac', 'Ah')))
        turn = Turn(cards=c52.get_many(codes=('Qd',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual([x.code for x in hand], ['As', 'Ah', 'Ad', 'Ac', 'Qd'])

    def test_board_trips(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ac', 'Ad')))
        turn = Turn(cards=c52.get_many(codes=('Ah',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual([x.code for x in hand], ['As', 'Ah', 'Ad', 'Ac', '6s'])

    def test_on_board(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '3c', '3h')))
        turn = Turn(cards=c52.get_many(codes=('3d',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual([x.code for x in hand], ['3s', '3h', '3d', '3c', 'As'])
