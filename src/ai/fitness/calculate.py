from typing import Optional

import numpy as np

from ai.log import log

from .bumpiness import get_bumpiness
from .holes import get_holes, get_holes_sum
from .peaks import get_peaks, get_peaks_max, get_peaks_sum
from .transitions import get_col_transition, get_row_transition
from .wells import get_wells, get_wells_max


def calculate_fitness(field: np.ndarray) -> float:
    """
    Calculate the fitness value for the given field.

    Args:
        field: The game field.

    Returns:
        The fitness value.
    """
    peaks = get_peaks(field=field)
    holes = get_holes(field=field)
    highest_peak = get_peaks_max(peaks=peaks)
    wells = get_wells(peaks=peaks)

    agg_height = get_peaks_sum(peaks=peaks)
    n_holes = get_holes_sum(field=field)
    bumpiness = get_bumpiness(peaks=peaks)
    num_pits = np.count_nonzero(np.count_nonzero(field, axis=0) == 0)
    max_wells = get_wells_max(wells=wells)
    n_cols_with_holes = np.count_nonzero(np.array(holes) > 0)
    row_transitions = get_row_transition(field=field, highest_peak=highest_peak)
    col_transitions = get_col_transition(field=field, peaks=peaks)
    cleared = np.count_nonzero(np.mean(field, axis=1))

    fitness = (
        agg_height
        + n_holes
        + bumpiness
        + num_pits
        + max_wells
        + n_cols_with_holes
        + row_transitions
        + col_transitions
        + cleared
    )
    return -float(fitness)
