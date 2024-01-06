from typing import Optional

import numpy as np

from .peaks import get_peaks


def get_wells(
    *, peaks: Optional[np.ndarray] = None, field: Optional[np.ndarray] = None
) -> np.ndarray:
    """
    Calculate the well depths in each column of the given field.

    Args:
        peaks: Array containing the indices of the peaks in each column. If not provided, it will be computed from the field.
        field: The signal field. Required if peaks is not provided.

    Returns:
        Array containing the well depths in each column.

    Raises:
        ValueError: If both `peaks` and `field` are `None`.
    """
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
    """
    Get the maximum well depth from the provided wells or compute wells from the field.

    Args:
        wells: Array containing the well depths in each column. If not provided, it will be computed from the field.
        field: The signal field. Required if wells is not provided.

    Returns:
        The maximum well depth.

    Raises:
        ValueError: If both `wells` and `field` are `None`.
    """
    if wells is None and field is None:
        raise ValueError("wells and field cannot both be None")
    elif wells is None:
        wells = get_wells(field)
    return int(np.max(wells))
