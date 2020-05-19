from typing import Sequence
from .card import Rank, Suit, Card
from .deck import Deck


class Repository(tuple):
    def get(self, code: str) -> object:
        for item in self:
            if item.code == code:
                return item
        raise KeyError(code)

    def get_many(self, codes: Sequence[str]) -> tuple:
        items, found = [], {}
        for item in self:
            if item.code in codes:
                items.append(item)
                found[item.code] = True
        if len(found) != len(codes):
            raise KeyError(codes)
        return tuple(items)


ranks = Repository((
    Rank(code='A', name='Ace', weight=14),
    Rank(code='2', name='Deuce', weight=2),
    Rank(code='3', name='Trey', weight=3),
    Rank(code='4', name='Four', weight=4),
    Rank(code='5', name='Five', weight=5),
    Rank(code='6', name='Six', weight=6),
    Rank(code='7', name='Seven', weight=7),
    Rank(code='8', name='Eight', weight=8),
    Rank(code='9', name='Nine', weight=9),
    Rank(code='T', name='Ten', weight=10),
    Rank(code='J', name='Jack', weight=11),
    Rank(code='Q', name='Queen', weight=12),
    Rank(code='K', name='King', weight=13),
))

suits = Repository((
    Suit(code='s', name='spades', weight=4),
    Suit(code='h', name='hearts', weight=3),
    Suit(code='d', name='diamonds', weight=2),
    Suit(code='c', name='clubs', weight=1),
))

cards52 = Repository(Card(rank=r, suit=s) for s in suits for r in ranks)
cards36 = Repository(Card(rank=r, suit=s) for s in suits for r in ranks if r.weight >= 6)


class StandardDeck(Deck):
    source = cards52


class ShortDeck(Deck):
    source = cards36


__all__ = ('ranks', 'suits', 'cards52', 'cards36', 'StandardDeck', 'ShortDeck')
