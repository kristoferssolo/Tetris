import numpy as np

from ai.log import log


def get_peaks(field: np.ndarray) -> np.ndarray:
    col_num = field.shape[1]
    peaks = np.zeros(col_num)

    for col in range(col_num):
        if 1 in field[:, col]:
            peaks[col] = field.shape[0] - np.argmax(field[:, col], axis=0)

    return peaks


def get_peaks_max(field: np.ndarray) -> int:
    return int(np.max(get_peaks(field)))


def get_peaks_sum(field: np.ndarray) -> int:
    return np.sum(get_peaks(field))
