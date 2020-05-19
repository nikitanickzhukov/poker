from unittest import TestCase

from engine.domain.model.card import cards52 as c52
from engine.domain.model.game.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, OnePair,
)


class OnePairTestCase(TestCase):
    def test_pocket_and_board(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ad', 'Jh')))
        turn = Turn(cards=c52.get_many(codes=('Qd',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', 'Qd', 'Jh', '6s'])

    def test_in_pocket(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', 'Ad')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '4d', 'Jh')))
        turn = Turn(cards=c52.get_many(codes=('Qd',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', 'Qd', 'Jh', '6s'])

    def test_on_board(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '4d', 'Jh')))
        turn = Turn(cards=c52.get_many(codes=('Qd',)))
        river = River(cards=c52.get_many(codes=('4s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual([x.code for x in hand], ['4s', '4d', 'As', 'Qd', 'Jh'])
