from typing import Any

import numpy as np


def complete_lines(field: np.ndarray[int, Any]) -> int:
    """
    Calculates the number of complete lines in the field.

    Args:
        field: 2D array representing the game field.

    Returns:
        The number of complete lines in the field.
    """
    return np.sum(np.all(field, axis=1))
