import numpy as np


def bumpiness(
    field: np.ndarray[int, np.dtype[np.uint8]],
) -> int:
    """
    Calculate the bumpiness of a given signal based on peaks.

    Args:
        field: The game field.

    Returns:
        The bumpiness of the field.
    """
    return int(np.sum(np.abs(np.diff(field.shape[0] - np.argmax(field, axis=0)))))
