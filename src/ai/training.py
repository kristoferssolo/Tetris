import neat
from utils import BASE_PATH

from .config import get_config
from .evaluations import eval_genomes
from .io import save_genome
from .log import log


def train(generations: int) -> None:
    """Train the AI"""
    config = get_config()
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    population.add_reporter(neat.StatisticsReporter())
    population.add_reporter(neat.Checkpointer(5, 900))
    winner = population.run(eval_genomes, generations)

    log.info("Saving best genome")
    save_genome(winner)
