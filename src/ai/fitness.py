from typing import Optional

import neat
import numpy as np
from game import Game
from utils import CONFIG

from .log import log


def calculate_fitness(game: Game, field: Optional[np.ndarray] = None) -> float:
    line_values = _calc_line_values(field)
    return game.score * 10.0 + line_values


def _calc_line_values(field: Optional[np.ndarray]) -> int:
    if field is None:
        return 0

    line_values = 0
    for idx, line in enumerate(np.flipud(field), start=1):
        if idx <= 4:
            line_values += int(line.sum()) * 5
        elif idx <= 8:
            line_values += int(line.sum()) * 3
        elif idx <= 12:
            line_values += int(line.sum()) * 0
        elif idx <= 16:
            line_values += int(line.sum()) * -5
        else:
            line_values += int(line.sum()) * -10

    return line_values
