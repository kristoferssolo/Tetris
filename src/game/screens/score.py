import pygame
from utils import CONFIG, Size

from game.log import log

from .base import BaseScreen, SceenElement, TextScreen


class Score(BaseScreen, SceenElement, TextScreen):
    """
    Class representing the score on the sidebar.

    Attributes:
        surface: Pygame surface representing the score.
        display_surface: Pygame display surface.
        rect: Pygame rectangle representing the score.
        font: Pygame font used to display the score.
        text: Text to be displayed on the score.
        increment_height: Height of each text element in the score.
    """

    def __init__(self) -> None:
        self._initialize_surface()
        self._initialize_rect()
        self._initialize_font()
        self.update(1, 0, 0)
        self._initialize_increment_height()

    def run(self) -> None:
        """Display the score on the game surface."""
        self.draw()

    def update(self, lines: int, score: int, level: int) -> None:
        """
        Update the score information.

        Args:
            lines (int): Number of lines cleared.
            score (int): Current game score.
            level (int): Current game level.
        """
        self.text: tuple[tuple[str, int], ...] = (
            ("Score", score),
            ("Level", level),
            ("Lines", lines),
            ("High Score", CONFIG.game.highscore),
            ("Generations", 0),
        )

    def draw(self) -> None:
        """Draw the score on the score surface."""
        self._update_display_surface()
        self._draw_background()
        self._draw_text()
        self._draw_border()

    def _draw_text(self) -> None:
        """Draw the text on the score surface."""
        for idx, text in enumerate(self.text):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + idx * self.increment_height
            self._display_text(text, pygame.Vector2(x, y))

    def _display_text(self, text_value: tuple[str, int], pos: pygame.Vector2) -> None:
        """
        Display a single text element on the score surface.

        Args:
            text_value: A tuple containing the label and value of the text element.
            pos: The position (x, y) where the text should be displayed.
        """

        text, value = text_value

        if len(text) >= 10:
            text_surface = self.font.render(f"{text}:", True, CONFIG.colors.fg_sidebar)

            value_surface = self.font.render(f"{value}", True, CONFIG.colors.fg_sidebar)
            value_rect = value_surface.get_rect(center=(pos.x, pos.y + 40))

            self.surface.blit(value_surface, value_rect)
        else:
            text_surface = self.font.render(
                f"{text}:{value}", True, CONFIG.colors.fg_sidebar
            )
            text_rect = text_surface.get_rect(center=pos)
            self.surface.blit(text_surface, text_rect)

        text_rect = text_surface.get_rect(center=pos)
        self.surface.blit(text_surface, text_rect)

    def _draw_border(self) -> None:
        """Draw the border of the score surface."""
        pygame.draw.rect(
            self.display_surface,
            CONFIG.colors.border_highlight,
            self.rect,
            CONFIG.game.line_width * 2,
            CONFIG.game.border_radius,
        )

    def _draw_background(self) -> None:
        """Fill the background of the score display."""
        self.surface.fill(CONFIG.colors.bg_sidebar)

    def _initialize_surface(self) -> None:
        """Initialize the score surface."""
        self.surface = pygame.Surface(CONFIG.sidebar.score)
        self.display_surface = pygame.display.get_surface()

    def _initialize_rect(self) -> None:
        """Initialize the score rectangle."""
        self.rect = self.surface.get_rect(
            bottomright=CONFIG.window.size - CONFIG.window.padding
        )

    def _initialize_font(self) -> None:
        """Initialize the font used to display the score."""
        self.font = pygame.font.Font(CONFIG.font.family, CONFIG.font.size)

    def _initialize_increment_height(self) -> None:
        """Initialize the increment height for positioning text elements."""
        self.increment_height = self.surface.get_height() / len(self.text)

    def _update_display_surface(self) -> None:
        """Update the display surface."""
        self.display_surface.blit(self.surface, self.rect)
