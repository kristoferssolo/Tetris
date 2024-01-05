from typing import Optional

import neat
import numpy as np
from game import Game
from utils import CONFIG


def calculate_fitness(game: Game) -> float:
    field = np.where(game.field != None, 1, 0)
    reward, penalty = _calc_height_penalty(field)
    fitness = game.score * 100 - _calc_holes(field) - penalty + reward
    return fitness


def _calc_holes(field: np.ndarray) -> float:
    height, width = field.shape
    penalty = 0

    for col in range(width):
        column = field[:, col]
        holde_indices = np.where(column == 0)[0]

        if len(holde_indices) > 0:
            highest_hole = holde_indices[0]
            penalty += np.sum(field[highest_hole:, col]) * (height - highest_hole)
    return penalty


def _calc_height_penalty(field: np.ndarray) -> tuple[float, float]:
    column_heights = np.max(
        np.where(field == 1, field.shape[0] - np.arange(field.shape[0])[:, None], 0),
        axis=0,
    )
    reward = np.mean(1 / (column_heights + 1))
    penalty = np.mean(column_heights * np.arange(1, field.shape[1] + 1))
    return reward, penalty
