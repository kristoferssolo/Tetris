import pygame
from utils import CONFIG, Size


class Preview:
    def __init__(self) -> None:
        self.surface = pygame.Surface(CONFIG.sidebar.preview)
        self.rect = self.surface.get_rect(
            topright=(
                CONFIG.window.size.width - CONFIG.window.padding,
                CONFIG.window.padding,
            )
        )
        self.dispaly_surface = pygame.display.get_surface()
        self.surface.fill(CONFIG.colors.bg_sidebar)

    def run(self) -> None:
        self.dispaly_surface.blit(self.surface, self.rect)
