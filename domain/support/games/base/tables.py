from typing import Sequence, Union, Optional

from .actions import Action, Check
from .pockets import Pocket


class Player:
    __slots__ = ('_pocket', '_nickname', '_chips')

    def __init__(
        self,
        pocket: Pocket,
        nickname: str,
        chips: int,
    ) -> None:
        self._pocket = pocket
        self._nickname = nickname
        self._chips = chips

    def __repr__(self) -> str:
        return '<{}: {}, {} chip(s), {}>'.format(
            self.__class__.__name__,
            self._nickname,
            self._chips,
            self._pocket,
        )

    def __str__(self) -> str:
        return self._nickname

    def do_action(self) -> Action:
        return Check()

    def win_chips(self, chips: int) -> None:
        assert chips > 0, '{} cannot win negative chips'.format(self.__class__.__name__)
        self._chips += chips

    @property
    def pocket(self) -> Pocket:
        return self._pocket

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def chips(self) -> int:
        return self._chips


class Table:
    __slots__ = ('_players',)

    def __init__(self, players: Optional[Sequence[Player]] = None) -> None:
        self._players = players or []

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self._players])

    def __len__(self) -> int:
        return len(self._players)

    def __iter__(self) -> iter:
        return iter(self._players)

    def __getitem__(self, key: Union[int, slice, str]) -> Union[Player, Sequence[Player]]:
        if isinstance(key, (int, slice)):
            return self._players[key]
        elif isinstance(key, str):
            for player in self._players:
                if player.nickname == key:
                    return player
            raise KeyError(key)
        else:
            raise TypeError(key)

    def add_player(self, player: Player) -> None:
        self._players.append(player)

    def remove_player(self, player: Player) -> None:
        self._players.remove(player)

    def index(self, player: Player) -> int:
        return self._players.index(player)

    @property
    def players(self) -> Sequence[Player]:
        return self._players


__all__ = ('Player', 'Table')
