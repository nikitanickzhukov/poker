from unittest import TestCase

from domain.generic.cards import StandardDeck
from domain.support.games.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, StraightFlush
)


class StraightFlushTestCase(TestCase):
    def test_wheel_2_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '2d', 'Jh')))
        turn = Turn(cards=deck.extract(('4s',)))
        river = River(cards=deck.extract(('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual([x.code for x in hand], ['5s', '4s', '3s', '2s', 'As'])

    def test_wheel_1_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('Ks', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'As', 'Jh')))
        turn = Turn(cards=deck.extract(('4s',)))
        river = River(cards=deck.extract(('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual([x.code for x in hand], ['5s', '4s', '3s', '2s', 'As'])

    def test_2_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('4s', '7s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'Ad', '2s')))
        turn = Turn(cards=deck.extract(('6s',)))
        river = River(cards=deck.extract(('5s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual([x.code for x in hand], ['7s', '6s', '5s', '4s', '3s'])

    def test_1_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('Js', 'Ts', 'Th')))
        turn = Turn(cards=deck.extract(('Qs',)))
        river = River(cards=deck.extract(('Ks',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual([x.code for x in hand], ['As', 'Ks', 'Qs', 'Js', 'Ts'])

    def test_on_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '4s', '5s')))
        turn = Turn(cards=deck.extract(('7s',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual([x.code for x in hand], ['7s', '6s', '5s', '4s', '3s'])
