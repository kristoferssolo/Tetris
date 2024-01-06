from typing import Any, Optional

import numpy as np


def aggregate_height(field: np.ndarray[int, Any]) -> int:
    """
    Calculates the aggregate height of the field.

    Args:
        field: 2D array representing the game field.

    Returns:
        The aggregate height of the field.
    """
    return np.sum(field.shape[0] - np.argmax(field, axis=0))
