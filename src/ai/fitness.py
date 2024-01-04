import neat


def calculate_fitness(app) -> float | int:
    return app.game.score + app.game.lines * 100 + app.game.level * 1000
