from typing import List, Optional


class Suit():
    """
    Representation of abstract suit
    """

    def __init__(self, code:str, name:str) -> None:
        self.code = code
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __hash__(self) -> str:
        return ord(self.code)

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other:'Suit') -> bool:
        return self.code == other.code

    def __ne__(self, other:'Suit') -> bool:
        return self.code != other.code


class SuitSet():
    """
    Representation of abstract set of suits
    """

    def __init__(self, items:List[Suit]) -> None:
        self.items = set(items)

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
