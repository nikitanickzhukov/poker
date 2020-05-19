from typing import Optional, Union, Sequence, Tuple, List, Type
from abc import ABC

from engine.domain.model.card import Card

from .street import Street
from .decision import Decision
from .player import Player


class Event(ABC):
    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))


class RoundStateChanged(Event):
    __slots__ = ('_street_class',)

    def __init__(self, street_class: Optional[Type[Street]]) -> None:
        self._street_class = street_class

    def __str__(self) -> str:
        if self._street_class:
            return self._street_class.__name__
        return 'Finished'

    @property
    def street_class(self) -> Optional[Type[Street]]:
        return self._street_class


class BoardCardsDealt(Event):
    __slots__ = ('_cards',)

    def __init__(self, cards: Sequence[Card]) -> None:
        self._cards = tuple(cards)

    def __str__(self) -> str:
        return str([str(x) for x in self._cards])

    @property
    def cards(self) -> Tuple[Card]:
        return self._cards


class PocketCardsDealt(Event):
    __slots__ = ('_player', '_cards')

    def __init__(self, player: Player, cards: Sequence[Card]) -> None:
        self._player = player
        self._cards = tuple(cards)

    def __str__(self) -> str:
        return '{}, {}'.format(str(self._player), str([str(x) for x in self._cards]))

    @property
    def player(self) -> Player:
        return self._player

    @property
    def cards(self) -> Tuple[Card]:
        return self._cards


class PlayerDrawCommitted(Event):
    __slots__ = ('_player', '_in_cards', '_out_cards')

    def __init__(self, player: Player, in_cards: Sequence[Card], out_cards: Sequence[Card]) -> None:
        self._player = player
        self._in_cards = tuple(in_cards)
        self._out_cards = tuple(out_cards)

    def __str__(self) -> str:
        return '{}, {} -> {}'.format(
            str(self._player),
            str([str(x) for x in self._out_cards]),
            str([str(x) for x in self._in_cards]),
        )

    @property
    def player(self) -> Player:
        return self._player

    @property
    def in_cards(self) -> Tuple[Card]:
        return self._in_cards

    @property
    def out_cards(self) -> Tuple[Card]:
        return self._out_cards


class PlayerDecisionCommitted(Event):
    __slots__ = ('_player', '_decision')

    def __init__(self, player: Player, decision: Decision) -> None:
        self._player = player
        self._decision = decision

    def __str__(self) -> str:
        return '{}, {}'.format(str(self._player), str(self._decision))

    @property
    def player(self) -> Player:
        return self._player

    @property
    def decision(self) -> Decision:
        return self._decision


class History:
    __slots__ = ('_events',)

    def __init__(self, events: Optional[Sequence[Event]] = None) -> None:
        self._events = list(events) if events else []

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self._events])

    def __len__(self) -> int:
        return len(self._events)

    def __iter__(self) -> iter:
        return iter(self._events)

    def __getitem__(self, idx: Union[int, slice]) -> Union[Event, List[Event]]:
        return self._events[idx]

    def push_event(self, event: Event) -> None:
        self._events.append(event)

    def get_events(self) -> Tuple[Event]:
        return tuple(self._events)

    def get_last_event(self) -> Optional[Event]:
        return self._events[-1] if len(self._events) else None


__all__ = (
    'Event',
    'RoundStateChanged',
    'BoardCardsDealt', 'PocketCardsDealt',
    'PlayerDrawCommitted', 'PlayerDecisionCommitted',
    'History',
)
