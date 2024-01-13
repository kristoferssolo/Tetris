import numpy as np


def get_peaks(field: np.ndarray[int, np.dtype[np.uint8]]) -> np.ndarray[int, np.dtype[np.uint8]]:
    """
    Calculate the peaks of a given field.

    Args:
        field: 2D array representing the game field.

    Returns:
        2D array representing the peaks of the field.
    """
    result = np.zeros(field.shape[1], dtype=int)
    for col in range(field.shape[1]):
        for row in range(field.shape[0]):
            if field[row, col] != 0:
                result[col] = field.shape[0] - row
                break
    return result
