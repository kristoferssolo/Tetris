import sys

import pygame
from utils import CONFIG

from .game import Game
from .preview import Preview
from .score import Score


class Main:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(CONFIG.window.title)
        self.display_surface = pygame.display.set_mode(CONFIG.window.size)
        self.display_surface.fill(CONFIG.colors.bg)
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.score = Score()
        self.preview = Preview()

    def draw(self) -> None:
        pygame.display.update()

    def run(self) -> None:
        while True:
            self.draw()
            self.handle_events()

            self.game.run()
            self.score.run()
            self.preview.run()

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
