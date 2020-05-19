from unittest import TestCase

from engine.domain.model.card import cards52 as c52
from engine.domain.model.game.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, StraightFlush,
)


class StraightFlushTestCase(TestCase):
    def test_wheel_2_pocket(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '2d', 'Jh')))
        turn = Turn(cards=c52.get_many(codes=('4s',)))
        river = River(cards=c52.get_many(codes=('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual([x.code for x in hand], ['5s', '4s', '3s', '2s', 'As'])

    def test_wheel_1_pocket(self):
        preflop = Preflop(cards=c52.get_many(codes=('Ks', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'As', 'Jh')))
        turn = Turn(cards=c52.get_many(codes=('4s',)))
        river = River(cards=c52.get_many(codes=('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual([x.code for x in hand], ['5s', '4s', '3s', '2s', 'As'])

    def test_2_pocket(self):
        preflop = Preflop(cards=c52.get_many(codes=('4s', '7s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ad', '2s')))
        turn = Turn(cards=c52.get_many(codes=('6s',)))
        river = River(cards=c52.get_many(codes=('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual([x.code for x in hand], ['7s', '6s', '5s', '4s', '3s'])

    def test_1_pocket(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('Js', 'Ts', 'Th')))
        turn = Turn(cards=c52.get_many(codes=('Qs',)))
        river = River(cards=c52.get_many(codes=('Ks',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual([x.code for x in hand], ['As', 'Ks', 'Qs', 'Js', 'Ts'])

    def test_on_board(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '4s', '5s')))
        turn = Turn(cards=c52.get_many(codes=('7s',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual([x.code for x in hand], ['7s', '6s', '5s', '4s', '3s'])
