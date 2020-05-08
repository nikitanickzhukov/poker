from typing import Optional, Sequence, Union


class Seat:
    __slots__ = ('_nickname', '_chips')

    def __init__(self, nickname: str, chips: int) -> None:
        self._nickname = nickname
        self._chips = chips

    def __repr__(self) -> str:
        return '<{}: {}'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return '{}, {} chips'.format(self._nickname, self._chips)

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def chips(self) -> int:
        return self._chips


class PocketDeal:
    __slots__ = ('_nickname', '_street', '_cards')

    def __init__(self, nickname: str, street: str, cards: Sequence[str]) -> None:
        self._nickname = nickname
        self._street = street
        self._cards = cards

    def __repr__(self) -> str:
        return '<{}: {}'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return '{}, {}, {}'.format(self._nickname, self._street, self._cards)

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def street(self) -> str:
        return self._street

    @property
    def cards(self) -> Sequence[str]:
        return self._cards


class BoardDeal:
    __slots__ = ('_street', '_cards')

    def __init__(self, street: str, cards: Sequence[str]) -> None:
        self._street = street
        self._cards = cards

    def __repr__(self) -> str:
        return '<{}: {}'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return '{}, {}'.format(self._street, self._cards)

    @property
    def street(self) -> str:
        return self._street

    @property
    def cards(self) -> Sequence[str]:
        return self._cards


class Decision:
    __slots__ = ('_nickname', '_action', '_chips')

    def __init__(self, nickname: str, action: str, chips: int) -> None:
        self._nickname = nickname
        self._action = action
        self._chips = chips

    def __repr__(self) -> str:
        return '<{}: {}'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        if self._chips:
            return '{}, {} {}'.format(self._nickname, self._action, self._chips)
        return '{}, {}'.format(self._nickname, self._action)

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def action(self) -> str:
        return self._action

    @property
    def chips(self) -> int:
        return self._chips


Event = Union[Seat, PocketDeal, BoardDeal, Decision]


class History:
    __slots__ = ('_events',)

    def __init__(self, events: Optional[Sequence[Event]] = None) -> None:
        self._events = events or []

    def __repr__(self) -> str:
        return '<{}: {}'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self._events])

    def __len__(self) -> int:
        return len(self._events)

    def __iter__(self) -> iter:
        return iter(self._events)

    def __getitem__(self, key: int) -> Event:
        return self._events[key]

    def push(self, item: Event) -> None:
        self._events.append(item)

    @property
    def events(self) -> Sequence[Event]:
        return self._events

    @property
    def seats(self) -> Sequence[Seat]:
        return [x for x in self._events if isinstance(x, Seat)]

    @property
    def pocket_deals(self) -> Sequence[PocketDeal]:
        return [x for x in self._events if isinstance(x, PocketDeal)]

    @property
    def board_deals(self) -> Sequence[BoardDeal]:
        return [x for x in self._events if isinstance(x, BoardDeal)]

    @property
    def decisions(self) -> Sequence[Decision]:
        return [x for x in self._events if isinstance(x, Decision)]


__all__ = ('Seat', 'PocketDeal', 'BoardDeal', 'Decision', 'History')
