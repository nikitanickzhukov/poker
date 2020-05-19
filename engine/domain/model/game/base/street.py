from abc import ABC
from typing import Sequence, Tuple, Union

from engine.domain.model.card import Card


class Street(ABC):
    """
    Representation of abstract street on a board or in a pocket
    """

    __slots__ = ('_cards',)
    length = 0
    is_pocket = False
    is_hole = False
    with_draw = False
    with_decision = True

    def __init__(self, cards: Sequence[Card]) -> None:
        assert len(cards) == self.length, 'Must contain {} card(s)'.format(self.length)
        self._cards = set(cards)

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self._cards])

    def __contains__(self, item: Union[Card, str]) -> bool:
        if isinstance(item, Card):
            return item in self._cards
        elif isinstance(item, str):
            return item in [x.code for x in self._cards]
        raise TypeError(item)

    def __len__(self) -> int:
        return len(self._cards)

    def __iter__(self) -> iter:
        return iter(self._cards)

    def draw_cards(self, in_cards: Sequence[Card], out_cards: Sequence[Card]) -> None:
        assert self.with_draw, 'Cannot draw cards on {}'.format(self.__class__.__name__)
        assert len(in_cards) == len(out_cards), 'Must draw equal cards amount'
        for card in out_cards:
            self._cards.remove(card)
        for card in in_cards:
            self._cards.add(card)

    def get_cards(self) -> Tuple[Card]:
        return tuple(self._cards)


__all__ = ('Street',)
