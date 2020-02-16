from typing import List, Optional


class Rank():
    """
    Representation of abstract rank
    """

    def __init__(self, code:str, name:str, weight:int) -> None:
        assert len(code) == 1 and ('A' <= code <= 'Z' or '0' <= code <= '9'), 'Code must be a single uppercase char from A to Z or from 0 to 9'
        assert len(name) > 0, 'Name must be specified'
        assert weight > 0, 'Weight must be a positive int'

        self._code = code
        self._name = name
        self._weight = weight

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return self._name

    def __hash__(self) -> int:
        return ord(self._code)

    def __eq__(self, other:'Rank') -> bool:
        return self._code == other._code

    def __ne__(self, other:'Rank') -> bool:
        return self._code != other._code

    def __gt__(self, other:'Rank') -> bool:
        return self._weight > other._weight

    def __ge__(self, other:'Rank') -> bool:
        return self._weight >= other._weight

    def __lt__(self, other:'Rank') -> bool:
        return self._weight < other._weight

    def __le__(self, other:'Rank') -> bool:
        return self._weight <= other._weight

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight


class RankSet():
    """
    Representation of abstract set of ranks
    """

    def __init__(self, items:List[Rank]) -> None:
        self._items = set(items)

    def __repr__(self) -> str:
        return repr(self._items)

    def __str__(self) -> str:
        return str(self._items)

    def __bool__(self) -> bool:
        return bool(self._items)

    def __eq__(self, other:'RankSet') -> bool:
        return self._items == other._items

    def __ne__(self, other:'RankSet') -> bool:
        return self._items != other._items

    def __contains__(self, item:Rank) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    def __getitem__(self, key:str) -> Rank:
        for x in self._items:
            if x.code == key:
                return x
        raise KeyError('Rank %s is not found' % (key,))


ace:Rank = Rank('A', 'Ace', 14)
king:Rank = Rank('K', 'King', 13)
queen:Rank = Rank('Q', 'Queen', 12)
jack:Rank = Rank('J', 'Jack', 11)
ten:Rank = Rank('T', 'Ten', 10)
nine:Rank = Rank('9', 'Nine', 9)
eight:Rank = Rank('8', 'Eight', 8)
seven:Rank = Rank('7', 'Seven', 7)
six:Rank = Rank('6', 'Six', 6)
five:Rank = Rank('5', 'Five', 5)
four:Rank = Rank('4', 'Four', 4)
trey:Rank = Rank('3', 'Trey', 3)
deuce:Rank = Rank('2', 'Deuce', 2)

standard_ranks:RankSet = RankSet([ ace, deuce, trey, four, five, six, seven, eight, nine, ten, jack, queen, king, ])
