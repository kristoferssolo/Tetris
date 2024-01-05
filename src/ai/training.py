import time
from typing import Optional

import neat
import pygame
from game import Main
from utils import BASE_PATH, CONFIG

from .evaluations import eval_genome
from .io import get_config, save_genome
from .log import log
from .visualize import plot_progress, plot_species, plot_stats


def train(
    gen_count: int = CONFIG.ai.generations,
    parallel: int = CONFIG.ai.parallels,
    checkpoint_path: Optional[str] = None,
) -> None:
    """
    Train the AI
    Args:
        gen_count: Number of generations to train (default is 200).
        threads: Number of threads to use (default is 1).
        checkpoint_path: Path to a checkpoint file to resume training from.
    """
    config = get_config()

    population = (
        neat.Checkpointer().restore_checkpoint(checkpoint_path)
        if checkpoint_path
        else neat.Population(config)
    )
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    population.add_reporter(
        neat.Checkpointer(
            CONFIG.ai.checkpoint.generation_interval,
            CONFIG.ai.checkpoint.time_interval,
            CONFIG.ai.checkpoint.filename_prefix,
        )
    )

    pe = neat.ParallelEvaluator(parallel, eval_genome)

    winner = population.run(pe.evaluate, gen_count)
    plot_stats(
        stats,
        ylog=False,
        view=False,
        filename=CONFIG.ai.plot_path / "avg_fitness.png",
    )
    plot_species(stats, view=False, filename=CONFIG.ai.plot_path / "speciation.png")

    log.info("Saving best genome")
    save_genome(winner)
