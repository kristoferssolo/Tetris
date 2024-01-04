import pygame
from utils import CONFIG, Figure, Size


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

    def run(self, next_figures: list[Figure]) -> None:
        self.dispaly_surface.blit(self.surface, self.rect)
        self.draw(next_figures)

    def draw(self, next_figures: list[Figure]) -> None:
        self.surface.fill(CONFIG.colors.bg_sidebar)
        self._draw_border()
        self._draw_figures(next_figures)

    def _draw_border(self) -> None:
        pygame.draw.rect(
            self.dispaly_surface,
            CONFIG.colors.border_highlight,
            self.rect,
            CONFIG.game.line_width * 2,
            CONFIG.game.border_radius,
        )

    def _draw_figures(self, figures: list[Figure]) -> None:
        for figure in figures:
            figure_surface = figure.value.image
            self.surface.blit(figure_surface, (0, 0))
