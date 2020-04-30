from typing import List
from .players import Player


class Layout():
    __slots__ = ('_players',)

    def __init__(self, players:List[Player]) -> None:
        self._players = players

    def __repr__(self) -> str:
        return '<{}: {}'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([ str(x) for x in self._players ])

    def __len__(self) -> int:
        return len(self._players)

    def __iter__(self) -> iter:
        return iter(self._players)

    def __getitem__(self, key:int) -> Player:
        return self._players[key]

    @property
    def players(self):
        return self._players

    @property
    def active_players(self):
        return tuple(x for x in self._players if x.is_active)

    @property
    def sb_player(self):
        return self._players[0]

    @property
    def bb_player(self):
        return self._players[1]

    @property
    def button_player(self):
        return self._players[-1]


__all__ = ('Layout',)
