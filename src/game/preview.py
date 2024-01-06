import pygame
from utils import CONFIG, Figure, Size


class Preview:
    """
    Class representing the preview of upcoming figures on the sidebar.

    Attributes:
        surface: Pygame surface representing the preview.
        rect: Pygame rectangle representing the preview.
        dispaly_surface: Pygame display surface.
        increment_height: Height of each figure in the preview.
    """

    def __init__(self) -> None:
        self._initialize_surface()
        self._initialize_rect()

    def run(self, next_figure: Figure) -> None:
        """
        Run the preview by updating the display and drawing next figures.

        Args:
            next_figures (list[Figure]): List of upcoming figures.
        """
        self.dispaly_surface.blit(self.surface, self.rect)
        self._draw_preview(next_figure)

    def _draw_border(self) -> None:
        """Draw the border around the preview surface."""
        pygame.draw.rect(
            self.dispaly_surface,
            CONFIG.colors.border_highlight,
            self.rect,
            CONFIG.game.line_width * 2,
            CONFIG.game.border_radius,
        )

    def _draw_figure(self, figure: Figure) -> None:
        """
        Draw a single upcoming figure on the preview surface.

        Args:
            figure (Figure): The upcoming figure to draw.
            idx (int): Index of the figure in the list.
        """
        figure_surface = figure.value.image
        x = self.surface.get_width() / 2
        y = self.surface.get_height() / 2
        rect = figure_surface.get_rect(center=(x, y))
        self.surface.blit(figure_surface, rect)

    def _draw_preview(self, next_figure: Figure) -> None:
        """
        Draw the preview with the background, border, and next figure.

        Args:
            next_figures (list[Figure]): List of upcoming figures.
        """
        self._draw_background()
        self._draw_border()
        self._draw_figure(next_figure)

    def _draw_background(self) -> None:
        """Draw the background of the preview."""
        self.surface.fill(CONFIG.colors.bg_sidebar)

    def _initialize_surface(self) -> None:
        """Initialize the preview surface."""
        self.surface = pygame.Surface(CONFIG.sidebar.preview)
        self.dispaly_surface = pygame.display.get_surface()

    def _initialize_rect(self) -> None:
        """Initialize the preview rectangle."""
        self.rect = self.surface.get_rect(
            topright=(
                CONFIG.window.size.width - CONFIG.window.padding,
                CONFIG.window.padding,
            )
        )
