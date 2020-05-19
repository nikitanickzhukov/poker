from unittest import TestCase

from engine.domain.model.card import cards52 as c52
from engine.domain.model.game.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, Trips,
)


class TripsTestCase(TestCase):
    def test_trips_1_pocket(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ad', 'Ac')))
        turn = Turn(cards=c52.get_many(codes=('Qd',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', 'Ac', 'Qd', '6s'])

    def test_set(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', 'Ad')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '2d', 'Ac')))
        turn = Turn(cards=c52.get_many(codes=('Qd',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', 'Ac', 'Qd', '6s'])

    def test_on_board(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '3d', '3c')))
        turn = Turn(cards=c52.get_many(codes=('Qd',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual([x.code for x in hand], ['3s', '3d', '3c', 'As', 'Qd'])
