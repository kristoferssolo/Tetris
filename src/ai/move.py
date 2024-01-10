from typing import Optional

from game import Main, Tetris
from game.sprites import Tetromino
from loguru import logger
from utils import CONFIG, BestMove, Direction, Figure

from .score import calculate_score

NUM_ROTATIONS: dict[Figure, int] = {
    Figure.I: 2,
    Figure.O: 1,
    Figure.T: 4,
    Figure.S: 2,
    Figure.Z: 2,
    Figure.J: 4,
    Figure.L: 4,
}


def get_best_move(app: Main, game: Tetris, tetermino: Tetromino) -> BestMove:
    best_move: Optional[BestMove] = None
    best_score: Optional[float] = None

    for rotation in range(NUM_ROTATIONS[tetermino.figure]):
        for i in range(CONFIG.game.columns):
            x_axis_movement: int = 0
            for _ in range(rotation):
                tetermino.rotate()

            while tetermino.move_horizontal(Direction.LEFT):  # move maximaly to the left
                x_axis_movement -= 1

            for _ in range(i):
                if tetermino.move_horizontal(Direction.RIGHT):  # slowly move to the right
                    x_axis_movement += 1

            tetermino.drop()

            score: float = calculate_score(game)

            logger.debug(
                f"{tetermino.figure.name=:3} {score=:6.6f} {best_score=:6.6f} {rotation=:1} {x_axis_movement=:1}"
            )

            tetermino.kill()
            tetermino = Tetromino(game.phantom_sprites, None, game.field, game.tetromino.figure, True)

            if best_score is None or score > best_score:
                best_score = score
                best_move = BestMove(rotation, x_axis_movement)

    if not best_move:
        best_move = BestMove(0, 0)
    return best_move
