from typing import Optional

import numpy as np

from .peaks import get_peaks


def get_holes(
    field: np.ndarray,
    peaks: Optional[np.array] = None,
) -> np.array:
    if peaks is None:
        peaks = get_peaks(field)
    col_count = field.shape[1]
    holes = np.zeros(col_count, dtype=int)

    for col in range(col_count):
        start = -peaks[col]
        if start != 0:
            holes[col] = np.count_nonzero(field[int(start) :, col] == 0)

    return holes


def get_holes_sum(
    *, holes: Optional[np.ndarray] = None, field: Optional[np.ndarray] = None
) -> int:
    if holes is None and field is None:
        raise ValueError("holes and field cannot both be None")
    elif holes is None:
        holes = get_holes(field)

    return int(np.sum(holes))
