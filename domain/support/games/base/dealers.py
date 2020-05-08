from abc import ABC
from typing import Sequence, Type, Optional

from domain.generic.cards import Deck

from .actions import Action, Blind, Fold, Check, Call, Bet, Raise
from .streets import Street
from .boards import Board
from .tables import Player, Table
from .pots import Pot
from .events import Event, Seat, Deal, Decision, History
from .hands import Identifier


class Dealer(ABC):
    def __init__(self):
        pass

    def shuffle_deck(self, deck: Deck) -> None:
        deck.shuffle()

    def restore_state(
        self,
        history: History,
        table: Table,
        board: Board,
        pot: Pot,
    ) -> None:
        for event in history:
            self._handle_event(event=event, table=table, board=board, pot=pot)

    def process(
        self,
        street_classes: Sequence[Type[Street]],
        history: History,
        deck: Deck,
        table: Table,
        board: Board,
        pot: Pot,
    ) -> None:
        while True:
            event = self._get_next_event(
                street_classes=street_classes,
                history=history,
                deck=deck,
                table=table,
            )
            if event:
                self._handle_event(
                    event=event,
                    table=table,
                    board=board,
                    pot=pot,
                )
                history.push(event=event)
            else:
                break

    def showdown(
        self,
        table: Table,
        board: Board,
        pot: Pot,
        identifier: Identifier,
    ) -> None:
        print(repr(board))
        for player in table:
            hand = identifier.identify(player.pocket, board)
            print(repr(player), ' has ', repr(hand))
        print(repr(pot))

    def _get_next_event(
        self,
        street_classes: Sequence[Type[Street]],
        history: History,
        deck: Deck,
        table: Table,
    ):
        event = self._get_last_event(history=history)

        if isinstance(event, Seat):
            street_class = self._get_next_street_class(street_classes=street_classes, street_class=None)
            if street_class:
                player = self._get_next_player(table=table, player=None) if street_class.is_pocket else None
                return self._deal_cards(
                    deck=deck,
                    street_class=street_class,
                    player=player,
                )
        elif isinstance(event, Deal):
            if event.player:
                player = self._get_next_player(table=table, player=event.player)
                if player:
                    return self._deal_cards(
                        deck=deck,
                        street_class=event.street.__class__,
                        player=player,
                    )
                else:
                    player = self._get_next_player(table=table, player=None)
                    return self._ask_player(
                        player=player,
                        history=history,
                        street_class=event.street.__class__,
                    )
            else:
                player = self._get_next_player(table=table, player=None)
                return self._ask_player(
                    player=player,
                    history=history,
                    street_class=event.street.__class__,
                )
        elif isinstance(event, Decision):
            player = self._get_next_player(table=table, player=event.player)
            if player:
                return self._ask_player(
                    player=player,
                    history=history,
                    street_class=event.street_class,
                )
            else:
                street_class = self._get_next_street_class(
                    street_classes=street_classes,
                    street_class=event.street_class,
                )
                if street_class:
                    player = self._get_next_player(table=table, player=None) if street_class.is_pocket else None
                    return self._deal_cards(
                        deck=deck,
                        street_class=street_class,
                        player=player,
                    )
        else:
            raise TypeError(event)

        return None

    def _deal_cards(
        self,
        deck: Deck,
        street_class: Type[Street],
        player: Optional[Player] = None,
    ) -> Deal:
        idx = slice(len(deck) - street_class.length, len(deck))
        cards = deck.extract(idx)
        street = street_class(cards=cards)
        return Deal(street=street, player=player)

    def _ask_player(
        self,
        player: Player,
        history: History,
        street_class: Type[Street],
    ):
        return Decision(
            player=player,
            action=Check(),
            street_class=street_class,
        )

    def _handle_event(self, event: Event, table: Table, board: Board, pot: Pot) -> None:
        print(repr(event))
        if isinstance(event, Seat):
            table.add_player(player=event.player)
            pot.add_player(player=event.player)
        elif isinstance(event, Deal):
            if event.player:
                event.player.pocket.append(event.street)
            else:
                board.append(event.street)
        elif isinstance(event, Decision):
            self._process_action(
                player=event.player,
                action=event.action,
                street_class=event.street_class,
                table=table,
                pot=pot,
            )
        else:
            raise TypeError(event)

    def _process_action(
        self,
        action: Action,
        player: Player,
        street_class: Type[Street],
        table: Table,
        pot: Pot,
    ) -> None:
        if isinstance(action, Blind):
            pot.add_chips(action.chips)
        elif isinstance(action, Fold):
            table.remove_player(player)
            pot.remove_player(player)
        elif isinstance(action, Check):
            pass
        elif isinstance(action, Call):
            pot.add_chips(action.chips)
        elif isinstance(action, Bet):
            pot.add_chips(action.chips)
        elif isinstance(action, Raise):
            pot.add_chips(action.chips)
        else:
            raise TypeError(action)

    def _get_last_event(self, history: History) -> Event:
        return history[-1]

    def _get_next_player(self, table: Table, player: Optional[Player], cyclic: bool = False) -> Optional[Player]:
        if player is None:
            return table[0]
        idx = table.index(player) + 1
        if idx >= len(table):
            return table[0] if cyclic else None
        return table[idx]

    def _get_next_street_class(
        self,
        street_classes: Sequence[Type[Street]],
        street_class: Optional[Type[Street]],
    ) -> Optional[Type[Street]]:
        if street_class is None:
            return street_classes[0]
        idx = street_classes.index(street_class) + 1
        if idx >= len(street_classes):
            return None
        return street_classes[idx]


__all__ = ('Dealer',)
