import sys

import pygame
from utils import CONFIG


class Menu:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(CONFIG.window.title)
        self.surface = pygame.display.set_mode(CONFIG.window.size)
        self.clock = pygame.time.Clock()

    def draw(self) -> None:
        self.surface.fill(CONFIG.colors.bg)
        pygame.display.update()

    def run(self) -> None:
        while True:
            self.draw()
            self.handle_events()
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
