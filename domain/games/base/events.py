from typing import Optional, Sequence, Type
from abc import ABC

from .streets import Street
from .actions import Action
from .tables import Player


class Event(ABC):
    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))


class Seat(Event):
    __slots__ = ('_player',)

    def __init__(self, player: Player) -> None:
        self._player = player

    def __str__(self) -> str:
        return str(self._player)

    @property
    def player(self) -> Player:
        return self._player


class Deal(Event):
    __slots__ = ('_street', '_player')

    def __init__(self, street: Street, player: Optional[Player] = None) -> None:
        self._street = street
        self._player = player

    def __str__(self) -> str:
        if self._player:
            return '{}, {}'.format(str(self._street), str(self._player))
        return str(self._street)

    @property
    def street(self) -> Street:
        return self._street

    @property
    def player(self) -> Player:
        return self._player


class Decision(Event):
    __slots__ = ('_player', '_action', '_street_class')

    def __init__(self, player: Player, action: Action, street_class: Type[Street]) -> None:
        self._player = player
        self._action = action
        self._street_class = street_class

    def __str__(self) -> str:
        return '{}, {}'.format(str(self._player), str(self._action))

    @property
    def player(self) -> Player:
        return self._player

    @property
    def action(self) -> Action:
        return self._action

    @property
    def street_class(self) -> Type[Street]:
        return self._street_class


class History:
    __slots__ = ('_events',)

    def __init__(self, events: Optional[Sequence[Event]] = None) -> None:
        self._events = list(events) or []

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self._events])

    def __len__(self) -> int:
        return len(self._events)

    def __iter__(self) -> iter:
        return iter(self._events)

    def __getitem__(self, key: int) -> Event:
        return self._events[key]

    def push(self, event: Event) -> None:
        self._events.append(event)

    @property
    def events(self) -> Sequence[Event]:
        return self._events

    @property
    def seats(self) -> Sequence[Seat]:
        return [x for x in self._events if isinstance(x, Seat)]

    @property
    def deals(self) -> Sequence[Deal]:
        return [x for x in self._events if isinstance(x, Deal)]

    @property
    def decisions(self) -> Sequence[Decision]:
        return [x for x in self._events if isinstance(x, Decision)]


__all__ = ('Event', 'Seat', 'Deal', 'Decision', 'History')
