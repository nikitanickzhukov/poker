from typing import List, Optional


class Suit():
    """
    Representation of abstract suit

    Tests
    -----
    >>> a = Suit('a', 'suit A')
    >>> a
    suit A
    >>> str(a)
    'suit A'
    >>> b = Suit('b', 'suit B')
    >>> b == a
    False
    >>> a != b
    True
    >>> c = Suit('a', 'suit C')
    >>> c == a
    True
    >>> b != c
    True
    """

    def __init__(self, code:str, name:str) -> None:
        self.code = code
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other:'Suit') -> bool:
        return self.code == other.code

    def __ne__(self, other:'Suit') -> bool:
        return self.code != other.code


class SuitSet():
    """
    Representation of abstract set of suits

    Tests
    -----
    >>> a = Suit('a', 'suit A')
    >>> b = Suit('b', 'suit B')
    >>> c = Suit('c', 'suit C')
    >>> s = SuitSet([a, b,])
    >>> str(s)
    '[suit A, suit B]'
    >>> s
    [suit A, suit B]
    >>> s.get(a.code)
    suit A
    >>> s.get(c.code)
    >>> for x in s:
    ...     x
    suit A
    suit B
    >>> a in s
    True
    >>> c in s
    False
    """

    items:List[Suit] = []

    def __init__(self, items:List[Suit]) -> None:
        self.items = items

    def __repr__(self):
        return repr(self.items)

    def __str__(self):
        return str(self.items)

    def __eq__(self, other:'SuitSet'):
        return self.items == other.items

    def __ne__(self, other:'SuitSet'):
        return self.items != other.items

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item:Suit):
        return item in self.items

    def get(self, code:str) -> Optional[Suit]:
        for x in self.items:
            if x.code == code:
                return x
        return None


spades:Suit = Suit('s', 'spades')
hearts:Suit = Suit('h', 'hearts')
diamonds:Suit = Suit('d', 'diamonds')
clubs:Suit = Suit('c', 'clubs')

suits:SuitSet = SuitSet([ spades, hearts, diamonds, clubs, ])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
