from typing import Optional

import numpy as np


def get_peaks(field: np.ndarray) -> np.ndarray:
    """
    Find the peaks in each column of the given field.

    Args:
        field: The signal field.

    Returns:
        Array containing the indices of the peaks in each column.
    """
    peaks = np.where(field == 1, field.shape[0] - np.argmax(field, axis=0), 0)
    return peaks.max(axis=0)


def get_peaks_max(
    *, peaks: Optional[np.ndarray] = None, field: Optional[np.ndarray] = None
) -> int:
    """
    Get the maximum peak value from the provided peaks or compute peaks from the field.

    Args:
        peaks: Array containing the indices of the peaks in each column. If not provided, it will be computed from the field.
        field: The signal field. Required if peaks is not provided.

    Returns:
        The maximum peak value.

    Raises:
        ValueError: If both `peaks` and `field` are `None`.
    """
    if peaks is None and field is None:
        raise ValueError("peaks and field cannot both be None")
    elif peaks is None:
        peaks = get_peaks(field)
    return int(np.max(peaks))


def get_peaks_sum(
    *, peaks: Optional[np.ndarray] = None, field: Optional[np.ndarray] = None
) -> int:
    """
    Get the sum of peak values from the provided peaks or compute peaks from the field.

    Args:
        peaks: Array containing the indices of the peaks in each column. If not provided, it will be computed from the field.
        field: The signal field. Required if peaks is not provided.

    Returns:
        The sum of peak values.

    Raises:
        ValueError: If both `peaks` and `field` are `None`.
    """
    if peaks is None and field is None:
        raise ValueError("peaks and field cannot both be None")
    elif peaks is None:
        peaks = get_peaks(field)
    return np.sum(peaks)
