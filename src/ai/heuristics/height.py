import numpy as np

from .peaks import get_peaks


def aggregate_height(field: np.ndarray[int, np.dtype[np.uint8]]) -> int:
    """
    Calculates the aggregate height of the field.

    Args:
        field: 2D array representing the game field.

    Returns:
        The aggregate height of the field.
    """
    heights = get_peaks(field)
    return int(np.sum(heights))
