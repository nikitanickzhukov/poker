from utils.attrs import StringAttr


class Gambler():
    nickname = StringAttr(min_length=1, max_length=63, writable=False)

    def __init__(self, nickname:str) -> None:
        self.__class__.nickname.validate(self, nickname)
        self._nickname = nickname

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self._nickname)

    def __str__(self) -> str:
        return self._nickname

    def __hash__(self) -> int:
        return hash(self._nickname)


__all__ = ('Gambler',)
