from abc import ABC
from typing import Type, Optional

from engine.domain.model.card import StandardDeck
from engine.domain.model.chips import Chips

from .street import Street
from .event import (
    Event,
    RoundStateChanged, PlayerDrawCommitted, PlayerDecisionCommitted,
    BoardCardsDealt, PocketCardsDealt, History
)
from .board import Board
from .player import Player
from .table import Table
from .dealer import Dealer
from .pot import Pot


class Round(ABC):
    __slots__ = ('_history', '_table', '_deck', '_board', '_identifier', '_dealer', '_pot', '_street_class')

    street_classes = None
    identifier_class = None
    pot_class = Pot
    deck_class = StandardDeck
    board_class = Board
    dealer_class = Dealer

    def __init__(
        self,
        history: History,
        table: Table,
        sb: Chips = None,
        bb: Chips = None,
        ante: Chips = None,
    ) -> None:
        assert self.street_classes, 'Round must contain 1 or more streets'
        assert (sb and bb) or ante, 'Round must have at least one non-zero value of both blinds and ante'

        self._history = history
        self._table = table

        self._sb = sb
        self._bb = bb
        self._ante = ante

        self._deck = self.deck_class()
        self._board = self.board_class()
        self._identifier = self.identifier_class()
        self._dealer = self.dealer_class()
        self._pot = self.pot_class(players=table.get_players())

        self._street_class = self.street_classes[0]

    def run(self) -> None:
        self.prepare()
        self.restore()
        self.start()
        self.finish()

    def prepare(self) -> None:
        self._dealer.shuffle_deck(deck=self._deck)
        if self._ante:
            self._dealer.collect_ante(
                table=self._table,
                pot=self._pot,
                ante=self._ante,
            )
        if self._bb:
            self._dealer.collect_blinds(
                table=self._table,
                pot=self._pot,
                sb=self._sb,
                bb=self._bb,
            )

    def restore(self) -> None:
        for event in self._history:
            if isinstance(event, BoardCardsDealt):
                self._dealer.deal_board_cards(
                    board=self._board,
                    deck=self._deck,
                    street_class=self._street_class,
                    cards=event.cards,
                )
            elif isinstance(event, PocketCardsDealt):
                self._dealer.deal_pocket_cards(
                    player=event.player,
                    deck=self._deck,
                    street_class=self._street_class,
                    cards=event.cards,
                )
            elif isinstance(event, PlayerDrawCommitted):
                self._dealer.handle_draw(
                    player=event.player,
                    deck=self._deck,
                    street_class=self._street_class,
                    in_cards=event.in_cards,
                    out_cards=event.out_cards,
                )
            elif isinstance(event, PlayerDecisionCommitted):
                self._dealer.handle_decision(
                    player=event.player,
                    street_class=self._street_class,
                    pot=self._pot,
                    decision=event.decision,
                )
            elif isinstance(event, RoundStateChanged):
                self._street_class = event.street_class

    def start(self) -> None:
        event = self._history.get_last_event()
        while not self._is_finished():
            event = self._next_action(prev_event=event)
            print(repr(event))
            self._history.push_event(event=event)

    def finish(self) -> None:
        self._dealer.define_winner(
            table=self._table,
            board=self._board,
            pot=self._pot,
            identifier=self._identifier,
        )
        print(self._table)
        print(self._pot)

    def _next_action(self, prev_event: Optional[Event]) -> Event:
        if prev_event is None:
            return self._dealing(street_class=self._street_class)
        elif isinstance(prev_event, BoardCardsDealt):
            return self._discarding(street_class=self._street_class)
        elif isinstance(prev_event, PocketCardsDealt):
            return self._pocket_dealing(street_class=self._street_class, prev_player=prev_event.player)
        elif isinstance(prev_event, PlayerDrawCommitted):
            return self._discarding(street_class=self._street_class, prev_player=prev_event.player)
        elif isinstance(prev_event, PlayerDecisionCommitted):
            return self._betting(street_class=self._street_class, prev_player=prev_event.player)
        elif isinstance(prev_event, RoundStateChanged):
            return self._dealing(street_class=self._street_class)
        else:
            raise TypeError(prev_event)

    def _dealing(self, street_class: Type[Street]) -> Event:
        if street_class.is_pocket:
            return self._pocket_dealing(street_class=street_class)
        else:
            return self._board_dealing(street_class=street_class)

    def _board_dealing(self, street_class: Type[Street]) -> Event:
        if street_class.length:
            return self._deal_board_cards(street_class=street_class)
        else:
            return self._discarding(street_class=street_class)

    def _pocket_dealing(self, street_class: Type[Street], prev_player: Optional[Player] = None) -> Event:
        if street_class.length:
            player = self._get_next_player_for_dealing(
                prev_player=prev_player,
                street_class=street_class,
            )
            if player:
                return self._deal_pocket_cards(player=player, street_class=street_class)
        return self._discarding(street_class=street_class)

    def _discarding(self, street_class: Type[Street], prev_player: Optional[Player] = None) -> Event:
        if street_class.with_draw:
            player = self._get_next_player_for_draw(
                prev_player=prev_player,
                street_class=street_class,
            )
            if player:
                return self._ask_draw(player=player, street_class=street_class)
        return self._betting(street_class=street_class)

    def _betting(self, street_class: Type[Street], prev_player: Optional[Player] = None) -> Event:
        if street_class.with_decision:
            player = self._get_next_player_for_decision(
                prev_player=prev_player,
                street_class=street_class,
            )
            if player:
                return self._ask_decision(player=player, street_class=street_class)
        return self._moving(prev_street_class=street_class)

    def _moving(self, prev_street_class: Type[Street]) -> Event:
        idx = self.street_classes.index(prev_street_class) + 1
        street_class = self.street_classes[idx] if idx < len(self.street_classes) else None
        return self._change_round(street_class=street_class)

    def _deal_board_cards(self, street_class: Type[Street]) -> Event:
        return self._dealer.deal_board_cards(
            board=self._board,
            deck=self._deck,
            street_class=street_class,
        )

    def _deal_pocket_cards(self, player: Player, street_class: Type[Street]) -> Event:
        return self._dealer.deal_pocket_cards(
            player=player,
            deck=self._deck,
            street_class=street_class,
        )

    def _ask_draw(self, player: Player, street_class: Type[Street]) -> Event:
        return self._dealer.handle_draw(
            player=player,
            deck=self._deck,
            street_class=street_class,
        )

    def _ask_decision(self, player: Player, street_class: Type[Street]) -> Event:
        return self._dealer.handle_decision(
            player=player,
            pot=self._pot,
            street_class=street_class,
        )

    def _change_round(self, street_class: Type[Street]) -> Event:
        self._street_class = street_class
        return RoundStateChanged(street_class=street_class)

    def _is_finished(self) -> bool:
        if self._street_class is None:
            return True
        if len([x for x in self._table.get_players() if not x.is_folded()]) == 1:
            return True
        return False

    def _get_start_player(self, street_class: Type[Street]) -> Player:
        prev_player = None
        if self.street_classes.index(street_class) == 0 and self._bb:
            prev_player = self._table.get_bb_player()
        return self._table.get_next_player(prev_player=prev_player, cyclic=False, check=lambda x: x.is_active())

    def _get_next_player_for_dealing(self, prev_player: Optional[Player], street_class: Type[Street]) -> Player:
        return self._table.get_next_player(prev_player=prev_player, cyclic=False, check=lambda x: not x.is_folded())

    def _get_next_player_for_draw(self, prev_player: Optional[Player], street_class: Type[Street]) -> Player:
        return self._table.get_next_player(prev_player=prev_player, cyclic=False, check=lambda x: not x.is_folded())

    def _get_next_player_for_decision(self, prev_player: Optional[Player], street_class: Type[Street]) -> Player:
        if not prev_player:
            return self._get_start_player(street_class=street_class)
        return self._table.get_next_player(prev_player=prev_player, cyclic=False, check=lambda x: x.is_active())


__all__ = ('Round',)
