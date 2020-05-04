from . import Runner


class EquityCalculator:
    def __init__(self, runner: Runner) -> None:
        self._runner = runner
        self._player_chips = defaultdict(int)
        self._total_chips = 0

    def calculate(self, attempts: int):
        for pot in self._runner.run(attempts):
            self._add_pot(pot=pot)
        return self._get_equity()

    def _add_pot(self, pot: Pot) -> None:
        self._total_chips += pot.chips
        for player in pot:
            self._player_chips[player] += pot.chips / len(pot)

    def _get_equity(self) -> dict:
        return {x: self._player_chips[x] / self._total_chips for x in self._player_chips}
