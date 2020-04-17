from ..base import Player as BasePlayer
from .pockets import Pocket


class Player(BasePlayer):
    pocket_class = Pocket


__all__ = ('Player',)
