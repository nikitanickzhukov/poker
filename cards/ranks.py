from typing import List, Optional


class Rank():
    """
    Representation of abstract rank

    Tests
    -----
    >>> x = Rank('a', 'rank A', 1)
    >>> x
    rank A
    >>> str(x)
    'rank A'
    >>> y = Rank('b', 'rank B', 2)
    >>> y == x
    False
    >>> x != y
    True
    >>> x < y
    True
    >>> y <= x
    False
    >>> z = Rank('a', 'rank X', 1)
    >>> z == x
    True
    >>> y != z
    True
    >>> z >= x
    True
    """

    def __init__(self, code:str, name:str, weight:int) -> None:
        self.code = code
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other:'Rank') -> bool:
        return self.code == other.code

    def __ne__(self, other:'Rank') -> bool:
        return self.code != other.code

    def __gt__(self, other:'Rank') -> bool:
        return self.weight > other.weight

    def __ge__(self, other:'Rank') -> bool:
        return self.weight >= other.weight

    def __lt__(self, other:'Rank') -> bool:
        return self.weight < other.weight

    def __le__(self, other:'Rank') -> bool:
        return self.weight <= other.weight


class RankSet():
    """
    Representation of abstract set of ranks

    Tests
    -----
    >>> a = Rank('a', 'rank A', 1)
    >>> b = Rank('b', 'rank B', 2)
    >>> c = Rank('c', 'rank C', 3)
    >>> s = RankSet([a, b,])
    >>> str(s)
    '[rank A, rank B]'
    >>> s
    [rank A, rank B]
    >>> s.get(a.code)
    rank A
    >>> s.get(c.code)
    >>> for x in s:
    ...     x
    rank A
    rank B
    >>> a in s
    True
    >>> c in s
    False
    """

    items:List[Rank] = []

    def __init__(self, items:List[Rank]) -> None:
        self.items = items

    def __repr__(self):
        return repr(self.items)

    def __str__(self):
        return str(self.items)

    def __eq__(self, other:'RankSet'):
        return self.items == other.items

    def __ne__(self, other:'RankSet'):
        return self.items != other.items

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item:Rank):
        return item in self.items

    def get(self, code:str) -> Optional[Rank]:
        for x in self.items:
            if x.code == code:
                return x
        return None


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
three:Rank = Rank('3', 'Three', 3)
deuce:Rank = Rank('2', 'Deuce', 2)

ranks:RankSet = RankSet([ ace, king, queen, jack, ten, nine, eight, seven, six, five, four, three, deuce, ])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
