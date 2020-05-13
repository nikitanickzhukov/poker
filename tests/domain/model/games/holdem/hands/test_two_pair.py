from unittest import TestCase

from domain.model.cards import StandardDeck
from domain.model.games.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, TwoPair,
)


class TwoPairTestCase(TestCase):
    def test_pp_and_pair(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', 'Ad')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '3d', 'Jh')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', '3s', '3d', 'Qd'])

    def test_2_matches(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'Ad', '2h')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', '2s', '2h', 'Qd'])

    def test_on_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '3d', '2h')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('Qs',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual([x.code for x in hand], ['Qs', 'Qd', '3s', '3d', 'As'])
