from unittest import TestCase

from engine.domain.model.card import cards52 as c52
from engine.domain.model.game.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, Flush,
)


class FlushTestCase(TestCase):
    def test_2_pocket_3_board(self):
        preflop = Preflop(cards=(c52.get_many(codes=('As', '2s'))))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ad', 'Ac')))
        turn = Turn(cards=c52.get_many(codes=('Qs',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual([x.code for x in hand], ['As', 'Qs', '6s', '3s', '2s'])

    def test_1_pocket_4_board(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ad', 'Js')))
        turn = Turn(cards=c52.get_many(codes=('Qs',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual([x.code for x in hand], ['As', 'Qs', 'Js', '6s', '3s'])

    def test_5_board(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3d', 'Ad', 'Jd')))
        turn = Turn(cards=c52.get_many(codes=('Qd',)))
        river = River(cards=c52.get_many(codes=('6d',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual([x.code for x in hand], ['Ad', 'Qd', 'Jd', '6d', '3d'])
