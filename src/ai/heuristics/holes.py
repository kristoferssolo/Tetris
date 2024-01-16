import numpy as np


def count_holes(
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

    num_rows, num_cols = field.shape
    holes_count = 0

    for col in range(num_cols):
        has_tile_above = False

        for row in range(num_rows):
            if field[row, col] == 1:
                has_tile_above = True
            elif field[row, col] == 0 and has_tile_above:
                holes_count += 1
    return holes_count
