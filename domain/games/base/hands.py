from abc import ABC
from typing import Tuple, Sequence, Union, Optional
from functools import total_ordering
from itertools import combinations, product
from collections import Counter, defaultdict

from domain.cards import Card, ranks

from .pockets import Pocket
from .boards import Board


min_rank = min(ranks)
max_rank = max(ranks)


class HandComb:
    def __init__(self, pocket: Pocket, board: Board) -> None:
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
        key = '__cards'
        if not hasattr(self, key):
            setattr(self, key, tuple(sorted(self._pocket.cards + self._board.cards, reverse=True)))
        return getattr(self, key)

    @property
    def ranks(self):
        key = '__ranks'
        if not hasattr(self, key):
            setattr(self, key, sorted(set(x.rank for x in self.cards), reverse=True))
        return getattr(self, key)

    @property
    def rank_counter(self) -> Counter:
        key = '__rank_counter'
        if not hasattr(self, key):
            setattr(self, key, Counter(x.rank for x in self.cards))
        return getattr(self, key)

    @property
    def suit_counter(self) -> Counter:
        key = '__suit_counter'
        if not hasattr(self, key):
            setattr(self, key, Counter(x.suit for x in self.cards))
        return getattr(self, key)

    @property
    def rank_map(self) -> dict:
        key = '__rank_map'
        if not hasattr(self, key):
            mapping = defaultdict(list)
            for card in self.cards:
                mapping[card.rank].append(card)
            mapping = {k: tuple(v) for k, v in mapping.items()}
            setattr(self, key, mapping)
        return getattr(self, key)

    @property
    def suit_map(self) -> dict:
        key = '__suit_map'
        if not hasattr(self, key):
            mapping = defaultdict(list)
            for card in self.cards:
                mapping[card.suit].append(card)
            mapping = {k: tuple(v) for k, v in mapping.items()}
            setattr(self, key, mapping)
        return getattr(self, key)

    @property
    def rank_map_not(self) -> dict:
        key = '__rank_map_not'
        if not hasattr(self, key):
            mapping = defaultdict(list)
            for rank in self.ranks:
                mapping[rank] = [x for x in self.cards if x.rank != rank]
            setattr(self, key, mapping)
        return getattr(self, key)

    def get_rank_reps(self, count: int) -> list:
        key = '__rank_reps_' + str(count)
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

    def get_rank_seqs(self, length: int) -> list:
        key = '__rank_seqs_' + str(length)
        if not hasattr(self, key):
            seq = [self.ranks[0]]
            seqs = []
            for i in range(1, len(self.ranks)):
                if self.ranks[i].weight == self.ranks[i - 1].weight - 1:
                    seq.append(self.ranks[i])
                    # Appending an Ace after a Deuce
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

    def get_suit_reps(self, count: int) -> list:
        key = '__suit_reps_' + str(count)
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
    __slots__ = ('_cards',)

    def __init__(self, cards: Sequence[Card]) -> None:
        self._cards = tuple(cards)

    def __str__(self) -> str:
        return str([str(x) for x in self._cards])

    def __eq__(self, other: 'Hand') -> bool:
        return self.weight == other.weight

    def __gt__(self, other: 'Hand') -> bool:
        return self.weight > other.weight

    def __contains__(self, item: Card) -> bool:
        return item in self._cards

    def __len__(self) -> int:
        return len(self._cards)

    def __iter__(self) -> iter:
        return iter(self._cards)

    def __getitem__(self, key: Union[slice, int]) -> Card:
        return self._cards[key]

    @classmethod
    def check_comb(cls, comb: HandComb, cards: Tuple[Card]) -> bool:
        return True

    @classmethod
    def identify(cls, comb: HandComb) -> Optional['Hand']:
        for cards in cls.get_combs(comb):
            if cls.check_comb(comb=comb, cards=cards):
                return cls(cards=cards)
        return None

    @property
    def cards(self) -> Tuple[Card]:
        return self._cards

    @property
    def weight(self) -> tuple:
        return self.hand_weight, *[x.rank.weight for x in self._cards]


class HighCard(ABC):
    hand_weight = 1
    hand_length = 5

    def __repr__(self) -> str:
        return '<High card: {}>'.format(', '.join([x.rank.name for x in self._cards]))

    @classmethod
    def get_combs(cls, comb: HandComb) -> iter:
        yield from combinations(comb.cards, cls.hand_length)


class OnePair(ABC):
    hand_weight = 2
    hand_length = 5

    def __repr__(self) -> str:
        return '<One pair: {}s, kickers: {}>'.format(
            self._cards[0].rank.name,
            ', '.join([x.rank.name for x in self._cards[2:]]),
        )

    @classmethod
    def get_combs(cls, comb: HandComb) -> iter:
        rank_reps = comb.get_rank_reps(2)
        for rank in rank_reps:
            pairs = comb.rank_map[rank]
            kickers = comb.rank_map_not[rank]
            for pair in combinations(pairs, 2):
                for kicker in combinations(kickers, cls.hand_length - 2):
                    yield pair + kicker


class TwoPair(ABC):
    hand_weight = 3
    hand_length = 5

    def __repr__(self) -> str:
        return '<Two pair: {}s and {}s, kicker: {}>'.format(
            self._cards[0].rank.name,
            self._cards[2].rank.name,
            self._cards[4].rank.name,
        )

    @classmethod
    def get_combs(cls, comb: HandComb) -> iter:
        rank_reps = comb.get_rank_reps(2)
        if len(rank_reps) >= 2:
            for rank1, rank2 in combinations(rank_reps, 2):
                pair1 = comb.rank_map[rank1]
                pair2 = comb.rank_map[rank2]
                kickers = tuple(x for x in comb.rank_map_not[rank1] if x.rank != rank2)
                for kicker in combinations(kickers, cls.hand_length - 4):
                    yield pair1 + pair2 + kicker


class Trips(ABC):
    hand_weight = 4
    hand_length = 5

    def __repr__(self) -> str:
        return '<Three of a kind: {}s, kickers: {}>'.format(
            self._cards[0].rank.name,
            ', '.join([x.rank.name for x in self._cards[3:]]),
        )

    @classmethod
    def get_combs(cls, comb: HandComb) -> iter:
        rank_reps = comb.get_rank_reps(3)
        for rank in rank_reps:
            triples = comb.rank_map[rank]
            kickers = comb.rank_map_not[rank]
            for triple in combinations(triples, 3):
                for kicker in combinations(kickers, cls.hand_length - 3):
                    yield triple + kicker


class Straight(ABC):
    hand_weight = 5
    hand_length = 5

    def __repr__(self) -> str:
        return '<Straight: {}-high>'.format(self._cards[0].rank.name)

    @classmethod
    def get_combs(cls, comb: HandComb) -> iter:
        rank_seqs = comb.get_rank_seqs(cls.hand_length)
        for seq in rank_seqs:
            for i in range(len(seq) - cls.hand_length + 1):
                subseq = seq[i:i + cls.hand_length]
                cards = tuple(comb.rank_map[x] for x in subseq)
                yield from product(*cards)


class Flush(ABC):
    hand_weight = 6
    hand_length = 5

    def __repr__(self) -> str:
        return '<Flush: {}>'.format(', '.join([x.rank.name for x in self._cards]))

    @classmethod
    def get_combs(cls, comb: HandComb) -> iter:
        suit_reps = comb.get_suit_reps(cls.hand_length)
        for suit in suit_reps:
            flush = comb.suit_map[suit]
            yield from combinations(flush, cls.hand_length)


class FullHouse(ABC):
    hand_weight = 7
    hand_length = 5

    def __repr__(self) -> str:
        return '<Full house: {}s over {}s>'.format(
            self._cards[0].rank.name,
            self._cards[3].rank.name,
        )

    @classmethod
    def get_combs(cls, comb: HandComb) -> iter:
        rank_reps_3 = comb.get_rank_reps(3)
        rank_reps_2 = comb.get_rank_reps(2)
        if rank_reps_3 and len(rank_reps_2) >= 2:
            for rank3 in rank_reps_3:
                for rank2 in rank_reps_2:
                    if rank2 == rank3:
                        continue
                    triples = comb.rank_map[rank3]
                    pairs = comb.rank_map[rank2]
                    kickers = tuple(x for x in comb.rank_map_not[rank3] if x.rank != rank2)
                    for triple in combinations(triples, 3):
                        for pair in combinations(pairs, 2):
                            for kicker in combinations(kickers, cls.hand_length - 5):
                                yield triple + pair + kicker


class Quads(ABC):
    hand_weight = 8
    hand_length = 5

    def __repr__(self) -> str:
        return '<Four of a kind: {}s, kicker: {}>'.format(
            self._cards[0].rank.name,
            self._cards[4].rank.name,
        )

    @classmethod
    def get_combs(cls, comb: HandComb) -> iter:
        rank_reps = comb.get_rank_reps(4)
        for rank in rank_reps:
            quads = comb.rank_map[rank]
            kickers = comb.rank_map_not[rank]
            for quad in combinations(quads, 4):
                for kicker in combinations(kickers, cls.hand_length - 4):
                    yield quad + kicker


class StraightFlush(ABC):
    hand_weight = 9
    hand_length = 5

    def __repr__(self) -> str:
        if self._cards[0].rank == max_rank:
            return '<Royal flush>'
        return '<Straight flush: {}-high>'.format(self._cards[0].rank.name)

    @classmethod
    def get_combs(cls, comb: HandComb) -> iter:
        straights = Straight.get_combs(comb=comb)
        for straight in straights:
            if all(x.suit == straight[0].suit for x in straight[1:]):
                yield straight


class Identifier(ABC):
    hand_classes = ()

    @classmethod
    def identify(cls, pocket: Pocket, board: Board) -> Optional[Hand]:
        comb = HandComb(pocket, board)
        for HandClass in cls.hand_classes:
            hand = HandClass.identify(comb=comb)
            if hand:
                return hand
        return None


__all__ = (
    'HandComb', 'Hand', 'HighCard', 'OnePair', 'TwoPair', 'Trips',
    'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush', 'Identifier',
)
