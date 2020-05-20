from typing import Tuple, Optional, Sequence, Dict

from engine.domain.model.chips import Chips

from .player import Player


class Pot:
    __slots__ = ('_players_chips', '_dead_chips', '_side_pot')

    def __init__(self, players: Sequence[Player]) -> None:
        self._players_chips: Dict[Player, Chips] = {x: Chips(amount=0) for x in players}
        self._dead_chips = Chips(amount=0)
        self._side_pot = None

    def __repr__(self) -> str:
        return '<{}: {}, players: {}>'.format(
            self.__class__.__name__,
            str(self),
            str([str(x) for x in self._players_chips])
        )

    def __str__(self) -> str:
        return repr(self.get_total_chips())

    def __bool__(self) -> bool:
        return bool(self._players_chips)

    def __len__(self) -> int:
        return len(self._players_chips)

    def __iter__(self) -> iter:
        return iter(self._players_chips)

    def put_chips(self, chips: Chips, player: Optional[Player] = None) -> None:
        if self._side_pot:
            self._side_pot.put_chips(chips=chips, player=player)
        else:
            if player:
                player_chips = self.get_player_chips(player=player)
                if chips + player_chips >= self.get_max_chips():
                    self._players_chips[player] += chips
                else:
                    diff = self.get_max_chips() - player_chips - chips
                    self._players_chips[player] = player_chips + chips - diff
                    self._create_side_pot(max_chips=diff)
            else:
                self._dead_chips += chips

    def remove_player(self, player: Player) -> None:
        self._dead_chips += self._players_chips[player]
        del self._players_chips[player]
        if self._side_pot:
            self._side_pot.remove_player(player=player)

    def get_players(self) -> Tuple[Player]:
        return tuple(self._players_chips.keys())

    def get_player_chips(self, player: Player) -> Chips:
        chips = self._players_chips[player]
        if self._side_pot:
            chips += self._side_pot.get_player_chips(player=player)
        return chips

    def get_total_chips(self) -> Chips:
        chips = self._dead_chips
        for x in self._players_chips.values():
            chips += x
        if self._side_pot:
            chips += self._side_pot.get_total_sum()
        return chips

    def get_max_chips(self) -> Chips:
        max_chips = Chips(amount=0)
        for player in self._players_chips:
            chips = self.get_player_chips(player=player)
            if chips > max_chips:
                max_chips = chips
        return max_chips

    def is_everyone_called(self) -> bool:
        if len(self._players_chips) <= 1:
            return True
        amounts = list(self._players_chips.values())
        head, tail = amounts[0], amounts[1:]
        return all([x == head for x in tail]) and (not self._side_pot or self._side_pot.is_everyone_called())

    def _create_side_pot(self, max_chips: Chips) -> None:
        players = {}
        for player in self._players_chips:
            diff = self._players_chips[player] - max_chips
            if diff:
                players[player] = diff
        if players:
            self._side_pot = self.__class__(players=tuple(players.keys()))
            for player in players:
                self._side_pot.put_chips(chips=players[player], player=player)


__all__ = ('Pot',)
