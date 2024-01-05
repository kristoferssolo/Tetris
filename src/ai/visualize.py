from pathlib import Path

import matplotlib.pyplot as plt
import neat
import numpy as np

from .log import log


def plot_stats(
    statistics: neat.StatisticsReporter,
    ylog: bool = False,
    view: bool = False,
    filename: str | Path = "avg_fitness.svg",
):
    """Plots the population's average and best fitness."""
    if plt is None:
        log.warning(
            "This display is not available due to a missing optional dependency (matplotlib)"
        )
        return

    generation = range(len(statistics.most_fit_genomes))
    best_fitness = [c.fitness for c in statistics.most_fit_genomes]
    avg_fitness = np.array(statistics.get_fitness_mean())
    stdev_fitness = np.array(statistics.get_fitness_stdev())

    plt.plot(generation, avg_fitness, "b-", label="average")
    plt.plot(generation, avg_fitness - stdev_fitness, "g-.", label="-1 sd")
    plt.plot(generation, avg_fitness + stdev_fitness, "g-.", label="+1 sd")
    plt.plot(generation, best_fitness, "r-", label="best")

    plt.title("Population's average and best fitness")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.grid()
    plt.legend(loc="best")
    if ylog:
        plt.gca().set_yscale("symlog")

    plt.savefig(str(filename))
    if view:
        plt.show()

    plt.close()


def plot_species(
    statistics: neat.StatisticsReporter,
    view: bool = False,
    filename: str | Path = "speciation.svg",
):
    """Visualizes speciation throughout evolution."""
    if plt is None:
        log.warning(
            "This display is not available due to a missing optional dependency (matplotlib)"
        )
        return

    species_sizes = statistics.get_species_sizes()
    num_generations = len(species_sizes)
    curves = np.array(species_sizes).T

    fig, ax = plt.subplots()
    ax.stackplot(range(num_generations), *curves)

    plt.title("Speciation")
    plt.ylabel("Size per Species")
    plt.xlabel("Generations")

    plt.savefig(str(filename))

    if view:
        plt.show()

    plt.close()


def plot_progress(
    generations: list[int],
    mean_fitness: list[int],
    max_fitness: list[int],
    view: bool = False,
    filename: str | Path = "progress.svg",
):
    if plt is None:
        log.warning(
            "This display is not available due to a missing optional dependency (matplotlib)"
        )
        return
    plt.plot(generations, mean_fitness, label="Mean Fitness")
    plt.plot(generations, max_fitness, label="Max Fitness")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.title("NEAT Algorithm Progress")
    plt.legend()
    plt.grid(True)
    plt.savefig(str(filename))

    if view:
        plt.show()

    plt.close()
