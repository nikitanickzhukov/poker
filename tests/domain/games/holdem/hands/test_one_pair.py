from unittest import TestCase

from domain.cards import StandardDeck
from domain.games.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, OnePair,
)


class OnePairTestCase(TestCase):
    def test_pocket_and_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'Ad', 'Jh')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', 'Qd', 'Jh', '6s'])

    def test_in_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', 'Ad')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '4d', 'Jh')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', 'Qd', 'Jh', '6s'])

    def test_on_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '4d', 'Jh')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('4s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual([x.code for x in hand], ['4s', '4d', 'As', 'Qd', 'Jh'])
