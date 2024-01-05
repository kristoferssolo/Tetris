import time

import neat
import pygame
from game import Main
from utils import BASE_PATH

from .config import get_config
from .evaluations import eval_genome
from .io import save_genome
from .log import log
from .visualize import plot_progress, plot_species, plot_stats


def train(gen_count: int, parallel: int = 1) -> None:
    """
    Train the AI
    Args:
        gen_count: Number of generations to train.
        threads: Number of threads to use (default is 1).
    """
    config = get_config()
    chekpoint_path = BASE_PATH / "checkpoints"
    plots_path = BASE_PATH / "plots"

    # population = neat.Checkpointer().restore_checkpoint(
    #     BASE_PATH / "checkpoints" / "neat-checkpoint-199"
    # )
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    population.add_reporter(neat.Checkpointer(5, 900))

    pe = neat.ParallelEvaluator(parallel, eval_genome)

    winner = population.run(pe.evaluate, gen_count)
    plot_stats(
        stats,
        ylog=False,
        view=False,
        filename=plots_path / "avg_fitness.png",
    )
    plot_species(stats, view=False, filename=plots_path / "speciation.png")

    log.info("Saving best genome")
    save_genome(winner)
