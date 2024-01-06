import sys

import pygame
from utils import CONFIG, GameMode

from game.log import log

from .base import BaseScreen, SceenElement, TextScreen
from .game import Game
from .menu_button import MenuButton


class Main(BaseScreen, SceenElement, TextScreen):
    def __init__(self, mode: GameMode) -> None:
        log.info("Initializing the game")
        self._initialize_pygame()
        self._initialize_surface()
        self._initialize_rect()
        self._initialize_font()
        self._set_buttons()
        self._initialize_increment_height()
        self.game_mode = mode  # TODO: use this

    def draw(self) -> None:
        """Update the display."""
        self._draw_background()
        self._draw_text()
        pygame.display.update()

    def update(self) -> None:
        pass

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.rect.collidepoint(mouse_pos):
                        button.on_click()
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.rect.collidepoint(mouse_pos):
                        button.update(True)
                    else:
                        button.update(False)

    def run(self) -> None:
        while True:
            self.draw()
            self.handle_events()

    def exit(self) -> None:
        """Exit the game."""
        pygame.quit()
        sys.exit()

    def _set_buttons(self) -> None:
        self.buttons: list[MenuButton] = [
            MenuButton("Play", None),
            MenuButton("AI", None),
            MenuButton("Settings", None),
            MenuButton("Quit", self.exit),
        ]

    def _initialize_pygame(self) -> None:
        """Initialize Pygame and set up the display."""
        pygame.init()
        pygame.display.set_caption(CONFIG.window.title)

    def _draw_background(self) -> None:
        self.display_surface.fill(CONFIG.colors.bg)

    def _draw_border(self) -> None:
        pass

    def _initialize_surface(self) -> None:
        self.display_surface = pygame.display.set_mode(CONFIG.window.size)

    def _initialize_rect(self) -> None:
        """Initialize the rectangle."""
        self.rect = self.display_surface.get_rect(topright=(0, 0))

    def _update_display_surface(self) -> None:
        """Do nothing. Not needed in this class."""

    def _initialize_increment_height(self) -> None:
        """Initialize the increment height for positioning text elements/buttons."""
        self.increment_height = (
            self.display_surface.get_height() - CONFIG.window.size.height / 2
        ) / len(self.buttons)

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

        x, y = self.display_surface.get_width() / 2, 100
        self._display_text("Tetris", (x, y))

        for idx, button in enumerate(self.buttons):
            x = self.display_surface.get_width() / 2
            y = (
                self.increment_height / 4
                + idx * self.increment_height
                + CONFIG.window.size.height / 4
            )  # TODO: tweak a bit more
            button.draw(self.display_surface, (x, y))
