import math
import time

import neat
import numpy as np
import pygame
from game import Block, Main
from utils import CONFIG

from .fitness import calculate_fitness
from .log import log


def eval_genome(genome: neat.DefaultGenome, config: neat.Config) -> float:
    app = Main()

    app.mute()
    game = app.game
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    genome.fitness = 0
    moves = 0

    while not game.game_over:
        current_figure: list[int] = [
            component for vec in game.tetromino.figure.value.shape for component in vec
        ]

        current_figure_pos: list[int] = [
            component
            for block in game.tetromino.blocks
            for component in (int(block.pos.x), int(block.pos.y))
        ]

        next_figures: list[int] = [
            component
            for figure in app.next_figures
            for pos in figure.value.shape
            for component in pos
        ]

        field: np.ndarray = np.zeros((CONFIG.game.rows, CONFIG.game.columns), dtype=int)

        block: Block
        for block in game.sprites:
            field[int(block.pos.y), int(block.pos.x)] = 1

        output = net.activate(
            # (*current_figure, *current_figure_pos, *next_figures, *field.flatten())
            field.flatten()
        )

        decision = output.index(max(output))

        decisions = {
            0: game.move_left,
            1: game.move_right,
            2: game.move_down,
            3: game.rotate,
            4: game.rotate_reverse,
            5: game.drop,
        }

        decisions[decision]()
        app.run_game_loop()
        moves += 1

    genome.fitness = calculate_fitness(game, field) - moves / 10
    score, lines, level = app.game.score, app.game.lines, app.game.level

    log.debug(f"{genome.fitness=:<+6.6}\t{score=:<6} {lines=:<6} {level=:<6}")

    game.restart()
    return genome.fitness
