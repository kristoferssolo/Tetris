from typing import Optional

import numpy as np

from ai.log import log

from .peaks import get_peaks


def get_wells(
    *, peaks: Optional[np.ndarray] = None, field: Optional[np.ndarray] = None
) -> np.ndarray:
    if peaks is None and field is None:
        raise ValueError("peaks and field cannot both be None")
    elif peaks is None:
        peaks = get_peaks(field)

    wells = np.zeros_like(peaks)

    first_well = peaks[1] - peaks[0]
    wells[0] = first_well if first_well > 0 else 0

    last_well = peaks[-2] - peaks[-1]
    wells[-1] = last_well if last_well > 0 else 0

    for idx in range(1, len(peaks) - 1):
        well_l = peaks[idx - 1] - peaks[idx]
        well_l = well_l if well_l > 0 else 0

        well_r = peaks[idx + 1] - peaks[idx]
        well_r = well_r if well_r > 0 else 0

        wells[idx] = well_l if well_l >= well_r else well_r

    return wells


def get_wells_max(
    *, wells: Optional[np.ndarray] = None, field: Optional[np.ndarray] = None
) -> int:
    if wells is None and field is None:
        raise ValueError("wells and field cannot both be None")
    elif wells is None:
        wells = get_wells(field)
    return int(np.max(wells))
