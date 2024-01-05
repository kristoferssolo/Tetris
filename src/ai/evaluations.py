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
            component
            for block in game.tetromino.blocks
            for component in (int(block.pos.x), int(block.pos.y))
        ]

        next_figure: list[int] = [
            vec
            for vec in app.next_figures[0].value.shape
            for vec in (int(vec.x), int(vec.y))
        ]

        field = np.where(game.field != None, 1, 0)

        output = net.activate((*next_figure, *current_figure, *field.flatten()))

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

    fitness = calculate_fitness(game)
    genome.fitness = fitness - fitness / moves
    score, lines, level = app.game.score, app.game.lines, app.game.level

    log.debug(f"{genome.fitness=:<+6.6}\t{score=:<6} {lines=:<6} {level=:<6}")

    game.restart()
    return genome.fitness
