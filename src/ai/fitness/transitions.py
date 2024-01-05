from typing import Optional

import numpy as np

from .peaks import get_peaks, get_peaks_max


def get_row_transition(field: np.ndarray, highest_peak: Optional[int] = None) -> int:
    """
    Calculate the number of transitions in the rows of the given field.

    Args:
        field: The signal field.
        highest_peak: The highest peak value. If not provided, it will be computed from the field.

    Returns:
        The total number of transitions in the rows.
    """
    if highest_peak is None:
        highest_peak = get_peaks_max(field=field)

    rows_to_check = slice(int(field.shape[0] - highest_peak), field.shape[0])
    transitions = np.sum(field[rows_to_check, 1:] != field[rows_to_check, :-1])

    return int(transitions)


def get_col_transition(field: np.ndarray, peaks: Optional[np.ndarray] = None) -> int:
    """
    Calculate the number of transitions in the columns of the given field.

    Args:
        field: The signal field.
        peaks: Array containing the indices of the peaks in each column. If not provided, it will be computed from the field.

    Returns:
        The total number of transitions in the columns.
    """
    if peaks is None:
        peaks = get_peaks(field)

    transitions_sum = 0

    for col in range(field.shape[1]):
        if peaks[col] <= 1:
            continue

        col_values = field[int(field.shape[0] - peaks[col]) : field.shape[0], col]
        transitions = np.sum(col_values[:-1] != col_values[1:])

        transitions_sum += transitions

    return transitions_sum
