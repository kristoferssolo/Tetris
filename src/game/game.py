import pygame
from utils import CONFIG


class Game:
    def __init__(self) -> None:
        self.surface = pygame.Surface(CONFIG.game.size)
        self.dispaly_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=CONFIG.game.pos)
        self.surface.fill(CONFIG.colors.bg_float)

    def run(self) -> None:
        self.dispaly_surface.blit(self.surface, CONFIG.game.pos)

    def draw(self) -> None:
        self._draw_grid()
        self._draw_border()

    def _draw_grid(self) -> None:
        for col in range(1, CONFIG.game.columns):
            x = col * CONFIG.game.cell_size
            pygame.draw.line(
                self.surface,
                CONFIG.colors.border_highlight,
                (x, 0),
                (x, self.surface.get_height()),
                CONFIG.game.line_width,
            )
            for row in range(1, CONFIG.game.rows):
                y = row * CONFIG.game.cell_size
                pygame.draw.line(
                    self.surface,
                    CONFIG.colors.border_highlight,
                    (0, y),
                    (self.surface.get_width(), y),
                    CONFIG.game.line_width,
                )

    def _draw_border(self) -> None:
        pygame.draw.rect(
            self.dispaly_surface,
            CONFIG.colors.border_highlight,
            self.rect,
            CONFIG.game.line_width,
            CONFIG.game.border_radius,
        )
