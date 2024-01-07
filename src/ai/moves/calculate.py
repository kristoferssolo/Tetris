from typing import Optional

import numpy as np

from ai.log import log

from .bumpiness import bumpiness
from .height import aggregate_height
from .holes import holes
from .lines import complete_lines


def calculate_fitness(field: np.ndarray) -> float:
    """
    Calculate the fitness value for the given field.

    Args:
        field: The game field.

    Returns:
        The fitness value.
    """

    height_w = aggregate_height(field)
    holes_w = holes(field)
    bumpiness_w = bumpiness(field)
    lines_w = complete_lines(field)

    fitness = (
        -0.510066 * height_w
        + 0.760666 * lines_w
        - 0.35663 * holes_w
        - 0.184483 * bumpiness_w
    )
    return fitness
