from typing import Optional

import numpy as np

from .peaks import get_peaks


def get_holes(
    field: np.ndarray,
    peaks: Optional[np.array] = None,
) -> np.array:
    """
    Calculate the number of holes in each column of the given field.

    Args:
        field: The signal field.
        peaks: Array containing peak indices. If not provided, it will be computed from the field.

    Returns:
        Array containing the number of holes in each column.
    """
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
    """
    Calculate the total number of holes in the given field or use pre-computed holes.

    Args:
        holes: Array containing the number of holes in each column. If not provided, it will be computed from the field.
        field: The signal field. Required if holes is not provided.

    Returns:
        The total number of holes in the field.

    Raises:
        ValueError: If both `holes` and `field` are `None`.
    """
    if holes is None and field is None:
        raise ValueError("holes and field cannot both be None")
    elif holes is None:
        holes = get_holes(field)

    return int(np.sum(holes))
