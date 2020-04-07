from abc import ABC
from typing import List, Union, Optional
from functools import total_ordering
from itertools import combinations, product
from collections import Counter, defaultdict

from cards import Card, ranks
from .pockets import Pocket
from .boards import Board

min_rank = min(ranks)
max_rank = max(ranks)


class HandComb():
    def __init__(self, pocket:Pocket, board:Board) -> None:
        self._pocket = pocket
        self._board = board

    @property
    def pocket(self):
        return self._pocket

    @property
    def board(self):
        return self._board

    @property
    def cards(self):
        if not hasattr(self, '_cards'):
            self._cards = tuple(sorted(self._pocket.items + self._board.items, reverse=True))
        return self._cards

    @property
    def ranks(self):
        if not hasattr(self, '_ranks'):
            self._ranks = sorted(set(x.rank for x in self.cards), reverse=True)
        return self._ranks

    @property
    def rank_counter(self) -> Counter:
        if not hasattr(self, '_rank_counter'):
            self._rank_counter = Counter(x.rank for x in self.cards)
        return self._rank_counter

    @property
    def suit_counter(self) -> Counter:
        if not hasattr(self, '_suit_counter'):
            self._suit_counter = Counter(x.suit for x in self.cards)
        return self._suit_counter

    @property
    def rank_map(self) -> dict:
        key = '_rank_map'
        if not hasattr(self, key):
            mapping = defaultdict(list)
            for card in self.cards:
                mapping[card.rank].append(card)
            mapping = { k: tuple(v) for k, v in mapping.items() }
            setattr(self, key, mapping)
        return getattr(self, key)

    @property
    def suit_map(self) -> dict:
        key = '_suit_map'
        if not hasattr(self, key):
            mapping = defaultdict(list)
            for card in self.cards:
                mapping[card.suit].append(card)
            mapping = { k: tuple(v) for k, v in mapping.items() }
            setattr(self, key, mapping)
        return getattr(self, key)

    @property
    def rank_map_not(self) -> dict:
        key = '_rank_map_not'
        if not hasattr(self, key):
            mapping = defaultdict(list)
            for rank in self.ranks:
                mapping[rank] = [ x for x in self.cards if x.rank != rank ]
            setattr(self, key, mapping)
        return getattr(self, key)

    def get_rank_reps(self, count:int) -> list:
        key = '_rank_reps_' + str(count)
        if not hasattr(self, key):
            reps = []
            for rank, c in self.rank_counter.most_common():
                if c >= count:
                    reps.append(rank)
                else:
                    break
            reps.sort(reverse=True)
            setattr(self, key, reps)
        return getattr(self, key)

    def get_rank_seqs(self, length:int) -> list:
        key = '_rank_seqs_' + str(length)
        if not hasattr(self, key):
            seq = [self.ranks[0]]
            seqs = []
            for i in range(1, len(self.ranks)):
                if self.ranks[i].weight == self.ranks[i - 1].weight - 1:
                    seq.append(self.ranks[i])
                    # Appending an Ace after Deuce
                    if self.ranks[i] == min_rank and max_rank in self.ranks:
                        seq.append(max_rank)
                else:
                    if len(seq) >= length:
                        seqs.append(seq)
                    seq = [self.ranks[i]]
            if len(seq) >= length:
                seqs.append(seq)
            setattr(self, key, seqs)
        return getattr(self, key)

    def get_suit_reps(self, count:int) -> list:
        key = '_suit_reps_' + str(count)
        if not hasattr(self, key):
            reps = []
            for suit, c in self.suit_counter.most_common():
                if c >= count:
                    reps.append(suit)
                else:
                    break
            reps.sort(reverse=True)
            setattr(self, key, reps)
        return getattr(self, key)


@total_ordering
class Hand(ABC):
    hand_length = 5
    hand_weight = 0

    def __init__(self, *args) -> None:
        assert all(isinstance(x, Card) for x in args), 'Hand must contain `Card` instances only'
        self._items = args

    def __repr__(self) -> str:
        return '<{}: {!r}'.format(self.__class__.__name__, self._items)

    def __eq__(self, other:'Hand') -> bool:
        return self.__class__ == other.__class__ and self._items == other._items

    def __gt__(self, other:'Hand') -> bool:
        return self.weight > other.weight

    def __contains__(self, item:Card) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    def __getitem__(self, key:Union[slice, int, str]) -> Card:
        if isinstance(key, (slice, int)):
            return self._items[key]
        elif isinstance(key, str):
            for item in self._items:
                if item.code == key:
                    return item
            raise KeyError('Card {} is not found'.format(key))
        else:
            raise AssertionError('Wrong key type')

    @classmethod
    def get_combs(cls, hand:HandComb) -> iter:
        while False:
            yield

    @classmethod
    def check_comb(cls, hand:HandComb, comb:tuple) -> bool:
        return True

    @classmethod
    def identify(cls, hand:HandComb) -> Optional['Hand']:
        for comb in cls.get_combs(hand):
            if cls.check_comb(hand, comb):
                return cls(*comb)
        return None

    @property
    def weight(self) -> tuple:
        return (self.hand_weight, *[ x.rank.weight for x in self._items ])


class HighCard(Hand):
    hand_weight = 1

    def __repr__(self) -> str:
        return '<High card: {}>'.format(', '.join([ x.rank.name for x in self._items ]))

    @classmethod
    def get_combs(cls, hand:HandComb) -> iter:
        yield from combinations(hand.cards, cls.hand_length)


class OnePair(Hand):
    hand_weight = 2

    def __repr__(self) -> str:
        return '<One pair: {}s, kickers: {}>'.format(
                   self._items[0].rank.name,
                   ', '.join([ x.rank.name for x in self._items[2:] ]),
               )

    @classmethod
    def get_combs(cls, hand:HandComb) -> iter:
        ranks = hand.get_rank_reps(2)
        for rank in ranks:
            pairs = hand.rank_map[rank]
            kickers = hand.rank_map_not[rank]
            for pair in combinations(pairs, 2):
                for kicker in combinations(kickers, cls.hand_length - 2):
                    yield pair + kicker


class TwoPair(Hand):
    hand_weight = 3

    def __repr__(self) -> str:
        return '<Two pair: {}s and {}s, kicker: {}>'.format(
                   self._items[0].rank.name,
                   self._items[2].rank.name,
                   self._items[4].rank.name,
               )

    @classmethod
    def get_combs(cls, hand:HandComb) -> iter:
        ranks = hand.get_rank_reps(2)
        if len(ranks) >= 2:
            for rank1, rank2 in combinations(ranks, 2):
                pair1 = hand.rank_map[rank1]
                pair2 = hand.rank_map[rank2]
                kickers = tuple(x for x in hand.rank_map_not[rank1] if x.rank != rank2)
                for kicker in combinations(kickers, cls.hand_length - 4):
                    yield pair1 + pair2 + kicker


class Trips(Hand):
    hand_weight = 4

    def __repr__(self) -> str:
        return '<Three of a kind: {}s, kickers: {}>'.format(
                   self._items[0].rank.name,
                   ', '.join([ x.rank.name for x in self._items[3:] ]),
               )

    @classmethod
    def get_combs(cls, hand:HandComb) -> iter:
        ranks = hand.get_rank_reps(3)
        for rank in ranks:
            tripses = hand.rank_map[rank]
            kickers = hand.rank_map_not[rank]
            for trips in combinations(tripses, 3):
                for kicker in combinations(kickers, cls.hand_length - 3):
                    yield trips + kicker


class Straight(Hand):
    hand_weight = 5

    def __repr__(self) -> str:
        return '<Straight: {}-high>'.format(self._items[0].rank.name)

    @classmethod
    def get_combs(cls, hand:HandComb) -> iter:
        seqs = hand.get_rank_seqs(cls.hand_length)
        for seq in seqs:
            for i in range(len(seq) - cls.hand_length + 1):
                subseq = seq[i:i + cls.hand_length]
                cards = tuple(hand.rank_map[x] for x in subseq)
                yield from product(*cards)


class Flush(Hand):
    hand_weight = 6

    def __repr__(self) -> str:
        return '<Flush: {}>'.format(', '.join([ x.rank.name for x in self._items ]))

    @classmethod
    def get_combs(cls, hand:HandComb) -> iter:
        suits = hand.get_suit_reps(cls.hand_length)
        for suit in suits:
            flush = hand.suit_map[suit]
            yield from combinations(flush, cls.hand_length)


class FullHouse(Hand):
    hand_weight = 7

    def __repr__(self) -> str:
        return '<Full house: {}s over {}s>'.format(
                   self._items[0].rank.name,
                   self._items[3].rank.name,
               )

    @classmethod
    def get_combs(cls, hand:HandComb) -> iter:
        ranks3 = hand.get_rank_reps(3)
        ranks2 = hand.get_rank_reps(2)
        if ranks3 and len(ranks2) >= 2:
            for rank3 in ranks3:
                tripses = hand.rank_map[rank3]
                pairs = tuple(x for x in hand.rank_map_not[rank3] if x.rank != rank3 and x.rank in ranks2)
                for trips in combinations(tripses, 3):
                    for pair in combinations(pairs, cls.hand_length - 3):
                        yield trips + pair


class Quads(Hand):
    hand_weight = 8

    def __repr__(self) -> str:
        return '<Four of a kind: {}s, kicker: {}>'.format(
                   self._items[0].rank.name,
                   self._items[4].rank.name,
               )

    @classmethod
    def get_combs(cls, hand:HandComb) -> iter:
        ranks = hand.get_rank_reps(4)
        for rank in ranks:
            quadses = hand.rank_map[rank]
            kickers = hand.rank_map_not[rank]
            for quads in combinations(quadses, 4):
                for kicker in combinations(kickers, cls.hand_length - 4):
                    yield quads + kicker


class StraightFlush(Hand):
    hand_weight = 9

    def __repr__(self) -> str:
        if self._items[0].rank == max_rank:
            return '<Royal flush>'
        return '<Straight flush: {}-high>'.format(self._items[0].rank.name)

    @classmethod
    def get_combs(cls, hand:HandComb) -> iter:
        straights = Straight.get_combs(hand)
        for straight in straights:
            if all(x.suit == straight[0].suit for x in straight[1:]):
                yield straight


class HandIdentifier(ABC):
    hand_classes = (StraightFlush, Quads, FullHouse, Flush, Straight, Trips, TwoPair, OnePair, HighCard)

    @classmethod
    def identify(cls, pocket:Pocket, board:Board) -> Optional[Hand]:
        assert isinstance(pocket, Pocket), '`pocket` must be a `Pocket` instance'
        assert isinstance(board, Board), '`board` must be a `Board` instance'
        handset = HandComb(pocket, board)
        for HandClass in cls.hand_classes:
            hand = HandClass.identify(handset)
            if hand:
                return hand
        return None


__all__ = ('Hand', 'HandComb', 'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush', 'HandIdentifier')
