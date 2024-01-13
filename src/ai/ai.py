from game import Main
from loguru import logger
from utils import BestMove, GameMode

from .move import get_best_move


def run() -> None:
    app = Main(GameMode.AI_TRAINING)
    app.play()
    game = app.game

    if not game:
        return

    tetris = game.tetris

    while True:
        app.handle_events()
        app.run_game_loop()

        best_move: BestMove = get_best_move(game.tetris, tetris.tetromino.figure)
        figure = game.tetris.tetromino.figure
        logger.warning(f"{figure.name=}    {best_move=}")

        for rotation in range(best_move.rotation):
            tetris.tetromino.rotate()

        for _ in range(abs(best_move.x_axis_offset)):
            if best_move.x_axis_offset > 0:
                tetris.move_right()
            elif best_move.x_axis_offset < 0:
                tetris.move_left()

        tetris.drop()
