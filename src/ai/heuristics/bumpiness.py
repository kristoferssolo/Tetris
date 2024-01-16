import numpy as np

from .peaks import get_peaks


def get_bumpiness(
    field: np.ndarray[int, np.dtype[np.uint8]],
) -> int:
    """
    Calculate the bumpiness of a given field based on peaks.

    Args:
        field: The game field.

    Returns:
        The bumpiness of the field.
    """
    field = get_peaks(field)
    diff = np.diff(field)
    return int(np.sum(np.abs(diff)))
