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

        self.increment_height = self.surface.get_height() / 3

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
        for idx, figure in enumerate(figures):
            figure_surface = figure.value.image
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + idx * self.increment_height
            rect = figure_surface.get_rect(center=(x, y))
            self.surface.blit(figure_surface, rect)
