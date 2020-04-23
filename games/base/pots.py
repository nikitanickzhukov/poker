from typing import List

from .players import Player


class Pot():
    __slots__ = ('_players', '_chips')

    def __init__(self, players:List[Player], chips:int=0) -> None:
        self._players = set(players)
        self._chips = chips

    def __repr__(self) -> str:
        return '<{}: {} chip(s), players: {}'.format(self.__class__.__name__, self._chips, str([ str(x) for x in self._players ]))

    def __bool__(self) -> bool:
        return self._chips > 0

    def remove_player(self, player:Player) -> None:
        self._players.remove(player)

    def add_chips(self, chips:int) -> None:
        assert chips > 0, '`chips` must be positive integer'
        self._chips += chips


__all__ = ('Pot',)
