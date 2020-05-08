from unittest import TestCase

from domain.generic.cards import StandardDeck
from domain.support.games.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, Straight
)


class StraightTestCase(TestCase):
    def test_wheel_2_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '2d', 'Jh')))
        turn = Turn(cards=deck.extract(('4d',)))
        river = River(cards=deck.extract(('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual([x.code for x in hand], ['5s', '4d', '3s', '2s', 'As'])

    def test_wheel_1_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('Ks', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'Ad', 'Jh')))
        turn = Turn(cards=deck.extract(('4d',)))
        river = River(cards=deck.extract(('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual([x.code for x in hand], ['5s', '4d', '3s', '2s', 'Ad'])

    def test_2_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('4s', '7s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'Ad', '2h')))
        turn = Turn(cards=deck.extract(('6d',)))
        river = River(cards=deck.extract(('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual([x.code for x in hand], ['7s', '6d', '5s', '4s', '3s'])

    def test_1_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('Js', 'Td', 'Th')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('Ks',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual([x.code for x in hand], ['As', 'Ks', 'Qd', 'Js', 'Th'])

    def test_on_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '4d', '5h')))
        turn = Turn(cards=deck.extract(('7d',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual([x.code for x in hand], ['7d', '6s', '5h', '4d', '3s'])
