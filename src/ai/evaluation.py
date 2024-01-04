import neat
from game import Main

from .fitness import calculate_fitness
from .log import log


def eval_genomes(genomes, config: neat.Config) -> None:
    app = Main()
    app.run()
    for genome_id, genome in genomes:
        genome.fitness = calculate_fitness(app)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        while not app.game.game_over():
            output = net.activate(app.game.field)

            decision = output.index(max(output))

            decisions = {
                0: app.game.move_left,
                1: app.game.move_right,
                2: app.game.rotate,
                3: app.game.rotate_reverse,
                4: app.game.drop,
            }

            decisions[decision]()

        genome.fitness = calculate_fitness(app)
        log.info(
            f"{genome_id=}\t{genome.fitness=}\t{app.game.score=}\t{app.game.lines=}\t{app.game.level=}"
        )
        app.game.restart()
