import pickle
from pathlib import Path

import neat
from utils import CONFIG


def get_config() -> neat.Config:
    return neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        CONFIG.ai.config_path,
    )


def load_genome() -> neat.DefaultGenome:
    with open(CONFIG.ai.winner_path, "rb") as f:
        return pickle.load(f)


def save_genome(genome: neat.DefaultGenome) -> None:
    with open(CONFIG.ai.winner_path, "wb") as f:
        pickle.dump(genome, f)
