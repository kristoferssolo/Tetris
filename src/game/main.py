import sys

import pygame
from utils import CONFIG, Figure

from .game import Game
from .log import log
from .preview import Preview
from .score import Score
from .tetromino import Tetromino


class Main:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(CONFIG.window.title)
        self.display_surface = pygame.display.set_mode(CONFIG.window.size)
        self.display_surface.fill(CONFIG.colors.bg)
        self.clock = pygame.time.Clock()

        self.next_figures = self._generate_next_figures()

        self.game = Game(self._get_next_figure, self._update_score)
        self.score = Score()
        self.preview = Preview()

        self.music = pygame.mixer.Sound(CONFIG.music.background)
        self.music.set_volume(CONFIG.music.volume)
        self.music.play()

    def draw(self) -> None:
        pygame.display.update()

    def run(self) -> None:
        while True:
            self.draw()
            self.handle_events()

            self.game.run()
            self.score.run()
            self.preview.run(self.next_figures)

            pygame.display.update()
            self.clock.tick(CONFIG.fps)

    def _update_score(self, lines: int, score: int, level: int) -> None:
        self.score.update(lines, score, level)

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

    def _generate_next_figures(self, amount: int = 3) -> list[Figure]:
        return [Figure.random() for _ in range(amount)]

    def _get_next_figure(self) -> Figure:
        next_shape = self.next_figures.pop(0)
        self.next_figures.append(Figure.random())
        return next_shape
