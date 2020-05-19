from unittest import TestCase

from engine.domain.model.card import cards52 as c52
from engine.domain.model.game.holdem import (
    Pocket, Player, Table, Flop,
    Fold, Check, Call, Bet, Raise,
    History, BoardCardsDealt, PocketCardsDealt, PlayerDecisionCommitted, RoundStateChanged,
    NoLimitHoldemRound
)


class RoundTestCase(TestCase):
    def test_start(self):
        a = Player(nickname='a', chips=10, pocket=Pocket())
        b = Player(nickname='b', chips=20, pocket=Pocket())
        c = Player(nickname='c', chips=30, pocket=Pocket())
        d = Player(nickname='d', chips=40, pocket=Pocket())

        table = Table(players=(a, b, c, d))

        history = History(events=(
            PocketCardsDealt(player=a, cards=(c52.get('Ah'), c52.get('Kc'))),
            PocketCardsDealt(player=b, cards=(c52.get('7h'), c52.get('8h'))),
            PocketCardsDealt(player=c, cards=(c52.get('3c'), c52.get('3s'))),
            PocketCardsDealt(player=d, cards=(c52.get('Jc'), c52.get('Jh'))),
            PlayerDecisionCommitted(player=c, decision=Raise(chips=4)),
            PlayerDecisionCommitted(player=d, decision=Call(chips=4)),
            PlayerDecisionCommitted(player=a, decision=Call(chips=3)),
            PlayerDecisionCommitted(player=b, decision=Call(chips=2)),
            RoundStateChanged(street_class=Flop),
            BoardCardsDealt(cards=(c52.get('Th'), c52.get('9c'), c52.get('5c'))),
        ))

        nlh_round = NoLimitHoldemRound(
            table=table,
            history=history,
            sb=1,
            bb=2,
        )
        nlh_round.run()
