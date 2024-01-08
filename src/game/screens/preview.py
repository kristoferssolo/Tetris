from typing import TYPE_CHECKING

import pygame
from utils import CONFIG

from .base import BaseScreen, SceenElement

if TYPE_CHECKING:
    from utils import Figure


class Preview(BaseScreen, SceenElement):
    """
    Class representing the preview of upcoming figures on the sidebar.

    Attributes:
        surface: Pygame surface representing the preview.
        rect: Pygame rectangle representing the preview.
        display_surface: Pygame display surface.
        increment_height: Height of each figure in the preview.
    """

    def __init__(self) -> None:
        self._initialize_surface()
        self._initialize_rect()

    def run(self) -> None:
        """Run the preview by updating the display and drawing next figure."""
        self.draw()

    def update(self, next_figure: Figure) -> None:
        """
        Update the preview information.

        Args:
            next_figures: Next figure.
        """
        self.next_figure = next_figure

    def draw(self) -> None:
        """Draw the preview on the preview surface."""
        self._update_display_surface()
        self._draw_background()
        self._draw_border()
        self._draw_figure()

    def _draw_border(self) -> None:
        """Draw the border around the preview surface."""
        pygame.draw.rect(
            self.display_surface,
            CONFIG.colors.border_highlight,
            self.rect,
            CONFIG.game.line_width * 2,
            CONFIG.game.border_radius,
        )

    def _draw_figure(self) -> None:
        """Draw a single upcoming figure on the preview surface."""
        figure_surface = self.next_figure.value.image
        x = self.surface.get_width() / 2
        y = self.surface.get_height() / 2
        rect = figure_surface.get_rect(center=(x, y))
        self.surface.blit(figure_surface, rect)

    def _draw_background(self) -> None:
        """Draw the background of the preview."""
        self.surface.fill(CONFIG.colors.bg_sidebar)

    def _initialize_surface(self) -> None:
        """Initialize the preview surface."""
        self.surface = pygame.Surface(CONFIG.sidebar.preview)
        self.display_surface = pygame.display.get_surface()

    def _initialize_rect(self) -> None:
        """Initialize the preview rectangle."""
        self.rect = self.surface.get_rect(
            topright=(
                CONFIG.window.size.width - CONFIG.window.padding,
                CONFIG.window.padding,
            )
        )

    def _update_display_surface(self) -> None:
        """Update the display surface."""
        self.display_surface.blit(self.surface, self.rect)
