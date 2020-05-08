from typing import Optional, Sequence

from .tables import Player


class Pot:
    __slots__ = ('_players', '_chips')

    def __init__(self, players: Optional[Sequence[Player]] = None, chips: int = 0) -> None:
        self._players = set(players) if players else set()
        self._chips = chips

    def __repr__(self) -> str:
        return '<{}: {}, players: {}>'.format(
            self.__class__.__name__,
            str(self),
            str([str(x) for x in self._players])
        )

    def __str__(self) -> str:
        return '{} chip(s)'.format(self._chips)

    def __bool__(self) -> bool:
        return self._chips > 0

    def __len__(self) -> int:
        return len(self._players)

    def __iter__(self) -> iter:
        return iter(self._players)

    def add_player(self, player: Player) -> None:
        self._players.add(player)

    def remove_player(self, player: Player) -> None:
        self._players.remove(player)

    def add_chips(self, chips: int) -> None:
        assert chips > 0, 'Cannot add negative chips to {}'.format(self.__class__.__name__)
        self._chips += chips


__all__ = ('Pot',)
