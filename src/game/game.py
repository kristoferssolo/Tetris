import pygame
from utils import CONFIG, Figure

from .tetromino import Tetromino


class Game:
    def __init__(self) -> None:
        self.surface = pygame.Surface(CONFIG.game.size)
        self.dispaly_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=CONFIG.game.pos)
        self.surface.fill(CONFIG.colors.bg_float)

        self._create_grid_surface()

        self.sprites = pygame.sprite.Group()
        self.tetromino = Tetromino(None, group=self.sprites)

    def run(self) -> None:
        self.dispaly_surface.blit(self.surface, CONFIG.game.pos)
        self.draw()

    def draw(self) -> None:
        self.sprites.draw(self.surface)
        self._draw_border()
        self._draw_grid()

    def _create_grid_surface(self) -> None:
        self.grid_surface = self.surface.copy()
        self.grid_surface.fill("#00ff00")
        self.grid_surface.set_colorkey("#00ff00")
        self.grid_surface.set_alpha(100)

    def _draw_grid(self) -> None:
        for col in range(1, CONFIG.game.columns):
            x = col * CONFIG.game.cell.width
            pygame.draw.line(
                self.grid_surface,
                CONFIG.colors.border_highlight,
                (x, 0),
                (x, self.grid_surface.get_height()),
                CONFIG.game.line_width,
            )
            for row in range(1, CONFIG.game.rows):
                y = row * CONFIG.game.cell.width
                pygame.draw.line(
                    self.grid_surface,
                    CONFIG.colors.border_highlight,
                    (0, y),
                    (self.grid_surface.get_width(), y),
                    CONFIG.game.line_width,
                )

        self.surface.blit(self.grid_surface, (0, 0))

    def _draw_border(self) -> None:
        pygame.draw.rect(
            self.dispaly_surface,
            CONFIG.colors.border_highlight,
            self.rect,
            CONFIG.game.line_width * 2,
            CONFIG.game.border_radius,
        )
