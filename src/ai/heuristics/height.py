import numpy as np


def aggregate_height(field: np.ndarray[int, np.dtype[np.uint8]]) -> int:
    """
    Calculates the aggregate height of the field.

    Args:
        field: 2D array representing the game field.

    Returns:
        The aggregate height of the field.
    """
    heights = np.zeros(field.shape[1], dtype=np.uint8)
    for col in range(field.shape[1]):
        for row in range(field.shape[0]):
            if field[row, col] != 0:
                heights[col] = field.shape[0] - row
                break
    return int(np.sum(heights))
