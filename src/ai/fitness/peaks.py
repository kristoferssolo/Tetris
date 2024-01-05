from typing import Optional

import numpy as np

from ai.log import log


def get_peaks(field: np.ndarray) -> np.ndarray:
    peaks = np.where(field == 1, field.shape[0] - np.argmax(field, axis=0), 0)
    return peaks.max(axis=0)


def get_peaks_max(
    peaks: Optional[np.ndarray], field: Optional[np.ndarray] = None
) -> int:
    if peaks is None and field is None:
        raise ValueError("peaks and field cannot both be None")
    elif peaks is None:
        peaks = get_peaks(field)
    return int(np.max(peaks))


def get_peaks_sum(
    peaks: Optional[np.ndarray], field: Optional[np.ndarray] = None
) -> int:
    if peaks is None and field is None:
        raise ValueError("peaks and field cannot both be None")
    elif peaks is None:
        peaks = get_peaks(field)
    return np.sum(peaks)
