import numpy as np
from game import Tetris

from .heuristics import aggregate_height, complete_lines, count_holes, get_bumpiness


def calculate_score(game: Tetris) -> float:
    field: np.ndarray[int, np.dtype[np.uint8]] = np.where(game.field != None, 1, 0)
    for block in game.tetromino.blocks:
        field[int(block.pos.y), int(block.pos.x)] = 1

    height = aggregate_height(field) * -0.510066
    lines = complete_lines(field) * 0.760666
    holes = count_holes(field) * -0.35663
    bumpiness = get_bumpiness(field) * -0.184483

    return height + lines + holes + bumpiness
