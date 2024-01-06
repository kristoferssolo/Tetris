from typing import Callable, Optional

import pygame
from utils import CONFIG

from .base import BaseScreen, SceenElement, TextScreen
from .button import Button


class MenuButton(Button, BaseScreen, SceenElement, TextScreen):
    def __init__(self, text: str, action: Optional[Callable[[], None]]) -> None:
        super().__init__(text, action)
        self._initialize_surface()
        self._initialize_font()

    def on_click(self) -> None:
        """Handle click event."""
        if self.action:
            self.action()

    def on_hover(self) -> None:
        """Handle hover event."""
        self._draw_border()

    def run(self) -> None:
        """Display the button on the game surface."""
        self.draw()

    def update(self) -> None:
        """Update the button."""
        pass

    def draw(self, surface: pygame.Surface, pos: tuple[float, float]) -> None:
        """Draw the button on the button surface."""
        self._initialize_rect(pos)
        self._update_display_surface()
        self._draw_background()
        self._draw_text()
        self._draw_border()

    def _initialize_surface(self) -> None:
        """Initialize the button surface."""
        self.surface = pygame.Surface(CONFIG.window.button.size)
        self.display_surface = pygame.display.get_surface()

    def _initialize_rect(self, pos: tuple[float, float]) -> None:
        """Initialize the button rectangle."""
        self.rect = self.surface.get_rect(center=pos)

    def _draw_text(self) -> None:
        """Draw the text on the text surface."""
        x = self.surface.get_width() / 2
        y = self.surface.get_height() / 2
        self._display_text(self.text, (x, y))

    def _display_text(self, text: str, pos: tuple[float, float]) -> None:
        """
        Display a single text element on the button surface.

        Args:
            text: The text to be displayed.
            pos: The position (x, y) where the text should be displayed.
        """
        text_surface = self.font.render(text, True, CONFIG.colors.fg_sidebar)
        text_rect = text_surface.get_rect(center=pos)
        self.surface.blit(text_surface, text_rect)

    def _initialize_font(self) -> None:
        """Initialize the font used to display the score."""
        self.font = pygame.font.Font(CONFIG.font.family, CONFIG.font.size)

    def _draw_background(self) -> None:
        """Fill the background of the button."""
        self.surface.fill(CONFIG.colors.bg_sidebar)

    def _draw_border(self) -> None:
        """Draw the border of the button."""
        pygame.draw.rect(
            self.display_surface,
            CONFIG.colors.border_highlight,
            self.rect,
            CONFIG.game.line_width * 2,
            CONFIG.game.border_radius,
        )

    def _update_display_surface(self) -> None:
        """Update the display surface."""
        self.display_surface.blit(self.surface, self.rect)
