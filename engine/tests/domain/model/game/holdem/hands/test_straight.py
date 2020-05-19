from unittest import TestCase

from engine.domain.model.card import cards52 as c52
from engine.domain.model.game.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, Straight,
)


class StraightTestCase(TestCase):
    def test_wheel_2_pocket(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '2d', 'Jh')))
        turn = Turn(cards=c52.get_many(codes=('4d',)))
        river = River(cards=c52.get_many(codes=('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual([x.code for x in hand], ['5s', '4d', '3s', '2s', 'As'])

    def test_wheel_1_pocket(self):
        preflop = Preflop(cards=c52.get_many(codes=('Ks', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ad', 'Jh')))
        turn = Turn(cards=c52.get_many(codes=('4d',)))
        river = River(cards=c52.get_many(codes=('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual([x.code for x in hand], ['5s', '4d', '3s', '2s', 'Ad'])

    def test_2_pocket(self):
        preflop = Preflop(cards=c52.get_many(codes=('4s', '7s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', 'Ad', '2h')))
        turn = Turn(cards=c52.get_many(codes=('6d',)))
        river = River(cards=c52.get_many(codes=('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual([x.code for x in hand], ['7s', '6d', '5s', '4s', '3s'])

    def test_1_pocket(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('Js', 'Td', 'Th')))
        turn = Turn(cards=c52.get_many(codes=('Qd',)))
        river = River(cards=c52.get_many(codes=('Ks',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual([x.code for x in hand], ['As', 'Ks', 'Qd', 'Js', 'Th'])

    def test_on_board(self):
        preflop = Preflop(cards=c52.get_many(codes=('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=c52.get_many(codes=('3s', '4d', '5h')))
        turn = Turn(cards=c52.get_many(codes=('7d',)))
        river = River(cards=c52.get_many(codes=('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual([x.code for x in hand], ['7d', '6s', '5h', '4d', '3s'])
