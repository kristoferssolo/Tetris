import numpy as np

from ai.log import log


def get_peaks(field: np.ndarray) -> float:
    col_num = field.shape[1]
    peaks = np.zeros(col_num)

    for col in range(col_num):
        if 1 in field[:, col]:
            peaks[col] = field.shape[0] - np.argmax(field[:, col], axis=0)

    return float(np.sum(peaks))
