from typing import Optional

import numpy as np

from .peaks import get_peaks


def get_bumpiness(
    *, peaks: Optional[np.ndarray] = None, field: Optional[np.ndarray] = None
) -> int:
    """
    Calculate the bumpiness of a given signal based on peaks.

    Args:
        peaks: Array containing peak indices. If not provided, it will be computed from the field.
        field: The signal field. Required if peaks is not provided.

    Returns:
        The bumpiness of the signal.

    Raises:
        ValueError: If both `peaks` and `field` are `None`.
    """
    if peaks is None and field is None:
        raise ValueError("peaks and field cannot both be None")
    elif peaks is None:
        peaks = get_peaks(field)

    differences = np.abs(np.diff(peaks))
    return int(np.sum(differences))
