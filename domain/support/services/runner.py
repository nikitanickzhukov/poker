from typing import List
from domain.support.base import Game


class Runner():
    def __init__(self, game:Game) -> None:
        self._game = game

    def run(self, attempts:int) -> iter:
        for _ in range(attempts):
            yield self._run_attempt()

    def _run_attempt(self) -> None:
        game = self._game.clone()
        return game.run()
