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
            str([str(x) for x in self.active_players])
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

    def add_chips(self, chips: int) -> None:
        assert chips > 0, 'Cannot add negative chips amount'
        self._chips += chips

    def get_winners(self) -> iter:
        count = len(self.active_players)
        chips = round(self._chips / count)
        return tuple((x, chips) for x in self.active_players)

    @property
    def players(self) -> Sequence[Player]:
        return tuple(self._players)

    @property
    def active_players(self) -> Sequence[Player]:
        return tuple(x for x in self._players if x.is_active)


__all__ = ('Pot',)
