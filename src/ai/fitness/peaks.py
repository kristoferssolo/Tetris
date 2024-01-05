import numpy as np

from ai.log import log


def get_peaks(field: np.ndarray) -> np.ndarray:
    peaks = np.where(field == 1, field.shape[0] - np.argmax(field, axis=0), 0)
    return peaks.max(axis=0)


def get_peaks_max(field: np.ndarray) -> int:
    return int(np.max(get_peaks(field)))


def get_peaks_sum(field: np.ndarray) -> int:
    return np.sum(get_peaks(field))
