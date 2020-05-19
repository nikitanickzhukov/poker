from unittest import TestCase

from engine.domain.model.card import cards52 as c52
from engine.domain.model.game.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, FullHouse,
)


class FullHouseTestCase(TestCase):
    def test_set_and_pair(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', 'Ad')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ac', '3c')))
        turn = Turn(cards=c52.get_many(codes=('2d',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', 'Ac', '3s', '3c'])

    def test_trips_and_pair(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ac', '2c')))
        turn = Turn(cards=c52.get_many(codes=('2d',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual([x.code for x in hand], ['2s', '2d', '2c', 'As', 'Ac'])

    def test_pp_and_trips(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', 'Ad')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '3c', '3d')))
        turn = Turn(cards=c52.get_many(codes=('2d',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual([x.code for x in hand], ['3s', '3d', '3c', 'As', 'Ad'])

    def test_on_board(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '3c', '3d')))
        turn = Turn(cards=c52.get_many(codes=('6d',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual([x.code for x in hand], ['3s', '3d', '3c', '6s', '6d'])
