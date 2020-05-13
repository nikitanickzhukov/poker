from unittest import TestCase

from domain.model.cards import StandardDeck
from domain.model.games.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, Trips,
)


class TripsTestCase(TestCase):
    def test_trips_1_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'Ad', 'Ac')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', 'Ac', 'Qd', '6s'])

    def test_set(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', 'Ad')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '2d', 'Ac')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual([x.code for x in hand], ['As', 'Ad', 'Ac', 'Qd', '6s'])

    def test_on_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '3d', '3c')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual([x.code for x in hand], ['3s', '3d', '3c', 'As', 'Qd'])
