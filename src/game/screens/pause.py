import pygame
from utils import CONFIG

from .base import BaseScreen, SceenElement, TextScreen


class Pause(BaseScreen, SceenElement, TextScreen):
    def __init__(self) -> None:
        self._initialize_surface()
        self._initialize_rect()
        self._initialize_font()

    def run(self) -> None:
        """
        Raises:
            NotImplementedError: Not implemented yet.
        """
        raise NotImplementedError

    def update(self) -> None:
        self._update_display_surface()

    def draw(self) -> None:
        """Update the display."""
        self.update()
        self._draw_background()
        self._draw_text()

    def _draw_text(self) -> None:
        """Draw the text."""
        self._display_text("Paused")

    def _display_text(self, text: str) -> None:
        """Display the text."""
        text_surface = self.font.render(text, True, CONFIG.colors.fg_float)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.text_surface.blit(text_surface, text_rect)

    def _draw_background(self) -> None:
        """Draw the background."""
        self.surface.fill(CONFIG.colors.bg_float)
        self.surface.set_alpha(100)
        self.text_surface.set_colorkey("#000000")
        self.text_surface.set_alpha(255)

    def _initialize_surface(self) -> None:
        """Initialize the pause screen surface."""
        self.surface = pygame.Surface(CONFIG.window.size)
        self.display_surface = pygame.display.get_surface()
        self.text_surface = pygame.Surface(CONFIG.window.size)

    def _initialize_rect(self) -> None:
        """Initialize the score rectangle."""
        self.rect = self.surface.get_rect(topleft=(0, 0))

    def _initialize_font(self) -> None:
        """Initialize the font used to display the text."""
        self.font = pygame.font.Font(CONFIG.font.family, CONFIG.font.size * 2)

    def _update_display_surface(self) -> None:
        """Update the display surface."""
        self.display_surface.blit(self.surface, self.rect)
        self.display_surface.blit(self.text_surface, self.rect)

    def _draw_border(self) -> None:
        """Draw the border.

        Raises:
            NotImplementedError: Not implemented yet.
        """
        raise NotImplementedError
