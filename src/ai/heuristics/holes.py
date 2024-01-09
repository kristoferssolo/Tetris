import numpy as np


def holes(
    field: np.ndarray[int, np.dtype[np.uint8]],
) -> int:
    """
    Calculate the number of holes in each column of the given field.

    Args:
        field: The signal field.
        peaks: Array containing peak indices. If not provided, it will be computed from the field.

    Returns:
        The total number of holes in the field.
    """

    first_nonzero_indices = np.argmax(field != 0, axis=0)

    mask = (field == 0) & (np.arange(field.shape[0])[:, np.newaxis] > first_nonzero_indices)

    return int(np.sum(mask))
