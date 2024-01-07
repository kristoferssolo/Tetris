import math
import time

import neat
import numpy as np
import pygame
from game import Main
from game.sprites import Block
from utils import CONFIG, GameMode

# from .fitness import calculate_fitness
from .log import log
from .moves import calculate_fitness


def eval_genome(genome: neat.DefaultGenome, config: neat.Config) -> float:
    app = Main(GameMode.AI_TRAINING).play()

    game = app.game
    tetris = game.tetris
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    genome.fitness = 0

    while not tetris.game_over:
        # current_figure: list[int] = [
        #     component
        #     for block in tetris.tetromino.blocks
        #     for component in (int(block.pos.x), int(block.pos.y))
        # ]

        # next_figure: list[int] = [
        #     vec
        #     for vec in game.next_figure.value.shape
        #     for vec in (int(vec.x), int(vec.y))
        # ]

        field = np.where(tetris.field != None, 1, 0)

        for block in tetris.tetromino.blocks:
            field[int(block.pos.y), int(block.pos.x)] = 2

        output = net.activate(field.flatten())

        decision = output.index(max(output))

        decisions = {
            0: tetris.move_left,
            1: tetris.move_right,
            2: tetris.move_down,
            3: tetris.rotate,
            4: tetris.rotate_reverse,
            5: tetris.drop,
        }

        decisions[decision]()
        app.run_game_loop()

    genome.fitness = calculate_fitness(field)
    score, lines, level = tetris.score, tetris.lines, tetris.level

    log.debug(f"{genome.fitness=:<+6.6}\t{score=:<6} {lines=:<6} {level=:<6}")

    tetris.restart()
    return genome.fitness
