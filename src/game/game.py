import pygame
from utils import CONFIG


class Game:
    def __init__(self) -> None:
        self.surface = pygame.Surface(CONFIG.game.size)
        self.dispaly_surface = pygame.display.get_surface()

    def run(self) -> None:
        self.dispaly_surface.blit(self.surface, CONFIG.game.pos)
