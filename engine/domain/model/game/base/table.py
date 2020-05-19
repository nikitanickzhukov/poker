from typing import Sequence, Tuple, Optional

from .player import Player


class Table:
    __slots__ = ('_players',)

    def __init__(self, players: Sequence[Player]) -> None:
        assert len(players) >= 2, 'Table must contain 2 or more players'
        self._players = tuple(players)

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self._players])

    def __len__(self) -> int:
        return len(self._players)

    def __iter__(self) -> iter:
        return iter(self._players)

    def get_players(self) -> Tuple[Player]:
        return self._players

    def get_sb_player(self) -> Player:
        return self._players[0]

    def get_bb_player(self) -> Player:
        return self._players[1]

    def get_next_player(
        self,
        prev_player: Optional[Player],
        cyclic: bool = False,
        check: callable = None,
    ) -> Optional[Player]:
        prev_idx = self._players.index(prev_player) if prev_player else -1
        i = prev_idx + 1
        if i == len(self._players):
            if cyclic:
                i = 0
            else:
                return None
        while True:
            if i == prev_idx:
                return None
            if check is None or check(self._players[i]):
                return self._players[i]
            i += 1
            if i == len(self._players):
                if cyclic and prev_idx != -1:
                    i = 0
                else:
                    return None


__all__ = ('Table',)
