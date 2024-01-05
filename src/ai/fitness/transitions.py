import numpy as np

from .peaks import get_peaks_max


def get_row_transitions(field: np.ndarray) -> int:
    highest_peak = get_peaks_max(field)

    rows_to_check = slice(int(field.shape[0] - highest_peak), field.shape[0])
    transitions = np.sum(field[rows_to_check, 1:] != field[rows_to_check, :-1])

    return int(transitions)


def get_col_transitions(field: np.ndarray) -> int:
    pass
