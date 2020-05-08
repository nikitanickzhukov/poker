from unittest import TestCase

from domain.generic.cards import StandardDeck
from domain.support.games.holdem import (
    Pocket, Player,
    Preflop, Flop, Turn, River,
    Blind, Fold, Check, Call, Bet, Raise,
    History, Seat, Deal, Decision, Game,
)


class GameTestCase(TestCase):
    def test_start(self):
        deck = StandardDeck()

        a = Player(nickname='a', chips=10, pocket=Pocket())
        b = Player(nickname='b', chips=20, pocket=Pocket())
        c = Player(nickname='c', chips=30, pocket=Pocket())
        d = Player(nickname='d', chips=40, pocket=Pocket())

        history = History(events=(
            Seat(player=a),
            Seat(player=b),
            Seat(player=c),
            Seat(player=d),
            Deal(player=a, street=Preflop(cards=deck.extract(('Ah', 'Kc')))),
            Deal(player=b, street=Preflop(cards=deck.extract(('7h', '8h')))),
            Deal(player=c, street=Preflop(cards=deck.extract(('3c', '3s')))),
            Deal(player=d, street=Preflop(cards=deck.extract(('Jc', 'Jh')))),
            Decision(player=a, action=Blind(chips=1), street_class=Preflop),
            Decision(player=b, action=Blind(chips=2), street_class=Preflop),
            Decision(player=c, action=Raise(chips=4), street_class=Preflop),
            Decision(player=d, action=Call(chips=4), street_class=Preflop),
            Decision(player=a, action=Call(chips=3), street_class=Preflop),
            Decision(player=b, action=Call(chips=2), street_class=Preflop),
            Deal(street=Flop(cards=deck.extract(('Th', '9c', '5c')))),
        ))

        game = Game(history=history, deck=StandardDeck())
        game.run()
