from typing import Optional

import numpy as np

from .peaks import get_peaks


def get_bumpiness(
    peaks: Optional[np.ndarray], field: Optional[np.ndarray] = None
) -> int:
    if peaks is None and field is None:
        raise ValueError("peaks and field cannot both be None")
    elif peaks is None:
        peaks = get_peaks(field)

    differences = np.abs(np.diff(peaks))
    return int(np.sum(differences))
