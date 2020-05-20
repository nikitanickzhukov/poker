from unittest import TestCase

from engine.domain.model.card import cards52 as c52
from engine.domain.model.chips import Chips
from engine.domain.model.game.holdem import (
    Pocket, Player, Table, Flop,
    Fold, Check, Call, Bet, Raise,
    History, BoardCardsDealt, PocketCardsDealt, PlayerDecisionCommitted, RoundStateChanged,
    NoLimitHoldemRound
)


class RoundTestCase(TestCase):
    def test_start(self):
        a = Player(nickname='a', chips=Chips(amount=10), pocket=Pocket())
        b = Player(nickname='b', chips=Chips(amount=20), pocket=Pocket())
        c = Player(nickname='c', chips=Chips(amount=30), pocket=Pocket())
        d = Player(nickname='d', chips=Chips(amount=40), pocket=Pocket())

        table = Table(players=(a, b, c, d))

        history = History(events=(
            PocketCardsDealt(player=a, cards=c52.get_many(codes=('Ah', 'Kc'))),
            PocketCardsDealt(player=b, cards=c52.get_many(codes=('7h', '8h'))),
            PocketCardsDealt(player=c, cards=c52.get_many(codes=('3c', '3s'))),
            PocketCardsDealt(player=d, cards=c52.get_many(codes=('Jc', 'Jh'))),
            PlayerDecisionCommitted(player=c, decision=Raise(chips=Chips(amount=4))),
            PlayerDecisionCommitted(player=d, decision=Call(chips=Chips(amount=4))),
            PlayerDecisionCommitted(player=a, decision=Call(chips=Chips(amount=3))),
            PlayerDecisionCommitted(player=b, decision=Call(chips=Chips(amount=2))),
            RoundStateChanged(street_class=Flop),
            BoardCardsDealt(cards=c52.get_many(codes=('Th', '9c', '5c'))),
        ))

        nlh_round = NoLimitHoldemRound(
            table=table,
            history=history,
            sb=Chips(amount=1),
            bb=Chips(amount=2),
        )
        nlh_round.run()
