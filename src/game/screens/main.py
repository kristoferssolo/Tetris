import sys
from typing import Optional

import pygame
from loguru import logger
from utils import CONFIG, GameMode, read_settings

from .base import BaseScreen, SceenElement, TextScreen
from .button import Button
from .game import Game
from .tetris import get_keys


class Main(BaseScreen, SceenElement, TextScreen):
    """
    Main class.

    Args:
        mode: The game mode to start with.
    """

    def __init__(self, mode: GameMode) -> None:
        logger.info("Initializing the game")
        self._initialize_pygame()
        self._initialize_surface()
        self._initialize_rect()
        self._initialize_font()
        self._set_buttons()
        self._initialize_increment_height()
        self.settings = read_settings()
        self.game: Optional[Game] = None
        self.game_mode = mode

    def draw(self) -> None:
        """Update the display."""
        self._draw_background()
        self._draw_text()

    def update(self) -> None:
        """Update the display."""
        pygame.display.update()

    def handle_events(self) -> None:
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in get_keys(self.settings["General"]["quit"]):
                    self.exit()
                elif event.key in get_keys(self.settings["General"]["pause"]) and self.game:
                    self.game.pause()

            if not self.game:
                for button in self.buttons:
                    button.on_click(event)
                    button.on_hover(event)

    def run(self) -> None:
        """Run the game loop continuously."""
        while True:
            self.run_game_loop()

    def run_game_loop(self) -> None:
        """Run a single iteration of the game loop."""
        if self.game:
            self.game.run()
        else:
            self.draw()

        self.handle_events()

        self.update()

    def exit(self) -> None:
        """Exit."""
        logger.info("Exiting the game")
        pygame.quit()
        sys.exit()

    def play(self) -> "Main":
        """Start a the game."""
        self._draw_background()
        self.game = Game(self.game_mode, self.settings)
        return self

    def _set_buttons(self) -> None:
        """Initialize and set up buttons."""
        self.buttons: list[Button] = [
            Button("Play", self.play),
            Button("AI", None),
            Button("Settings", None),
            Button("Quit", self.exit),
        ]

    def _initialize_pygame(self) -> None:
        """Initialize Pygame and set up the display."""
        pygame.init()
        pygame.display.set_caption(CONFIG.window.title)

    def _draw_background(self) -> None:
        """Draw the background on the display surface."""
        self.display_surface.fill(CONFIG.colors.bg)

    def _draw_border(self) -> None:
        """
        Raises:
            NotImplementedError: Not implemented yet.
        """
        raise NotImplementedError

    def _initialize_surface(self) -> None:
        """Initialize the display surface."""
        self.display_surface = pygame.display.set_mode(CONFIG.window.size)

    def _initialize_rect(self) -> None:
        """Initialize the rectangle."""
        self.rect = self.display_surface.get_rect(topright=(0, 0))

    def _update_display_surface(self) -> None:
        """
        Raises:
            NotImplementedError: Not implemented yet.
        """
        raise NotImplementedError

    def _initialize_increment_height(self) -> None:
        """Initialize the increment height for positioning text elements/buttons."""
        self.increment_height: float = (self.display_surface.get_height() - CONFIG.window.size.height / 2) / len(
            self.buttons
        )

    def _display_text(self, text: str, pos: tuple[float, float]) -> None:
        """
        Display a single text element on the score surface.

        Args:
            text: A tuple containing the label and value of the text element.
            pos: The position (x, y) where the text should be displayed.
        """
        text_surface = self.font.render(text, True, CONFIG.colors.fg)
        text_rect = text_surface.get_rect(center=pos)
        self.display_surface.blit(text_surface, text_rect)

    def _initialize_font(self) -> None:
        """Initialize the font used to display the score."""
        self.font = pygame.font.Font(CONFIG.font.family, CONFIG.font.size)

    def _draw_text(self) -> None:
        """Draw the text and buttons on the surface."""

        x: float = self.display_surface.get_width() / 2
        y: float = 100
        self._display_text("Tetris", (x, y))

        for idx, button in enumerate(self.buttons):
            x = self.display_surface.get_width() / 2
            y = (
                self.increment_height / 4 + idx * self.increment_height + CONFIG.window.size.height / 4
            )  # TODO: tweak a bit more
            button.draw(self.display_surface, (x, y))
