from abc import ABC


class Hand(ABC):
    weight = 0

    def __init__(self, pocket, board) -> None:
        self._pocket = pocket
        self._board = board

    @classmethod
    def check(cls, pocket, board) -> bool:
        return False
