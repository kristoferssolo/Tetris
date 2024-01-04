import pickle
from pathlib import Path

import neat
from utils import BASE_PATH


def load_genome() -> neat.DefaultGenome:
    with open(BASE_PATH / "winner.pkl", "rb") as f:
        return pickle.load(f)


def save_genome(genome: neat.DefaultGenome) -> None:
    with open(BASE_PATH / "winner.pkl", "wb") as f:
        pickle.dump(genome, f)
