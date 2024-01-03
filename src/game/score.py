import pygame
from utils import CONFIG, Size


class Score:
    def __init__(self) -> None:
        self.surface = pygame.Surface(CONFIG.sidebar.score)
        self.dispaly_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(
            bottomright=CONFIG.window.size.sub(CONFIG.window.padding)
        )
        self.surface.fill(CONFIG.colors.bg_sidebar)

    def run(self) -> None:
        self.dispaly_surface.blit(self.surface, self.rect)
