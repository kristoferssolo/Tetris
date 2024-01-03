import sys

import pygame
from utils import CONFIG

from .game import Game
from .score import Score


class Main:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(CONFIG.window.title)
        self.display_surface = pygame.display.set_mode(CONFIG.window.size)
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.score = Score()

    def draw(self) -> None:
        self.display_surface.fill(CONFIG.colors.bg)
        pygame.display.update()

    def run(self) -> None:
        while True:
            self.draw()
            self.handle_events()

            self.game.run()
            self.score.run()

            pygame.display.update()
            self.clock.tick(CONFIG.fps)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.exit()

    def exit(self) -> None:
        pygame.quit()
        sys.exit()
