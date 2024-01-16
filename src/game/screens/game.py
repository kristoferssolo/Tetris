from typing import Any

import pygame
from loguru import logger
from utils import CONFIG, Figure, GameMode

from .base import BaseScreen, SceenElement
from .pause import Pause
from .preview import Preview
from .score import Score
from .tetris import Tetris


class Game(BaseScreen, SceenElement):
    """
    Game class.

    Args:
        mode: The game mode to start with.

    Attributes:
        game_mode: The game mode.
        settings: The game settings.
        display_surface: Pygame display surface.
        clock: Pygame clock.
        music: Pygame music.
        game: Game object.
        score: Score object.
        preview: Preview object.
        next_figure: List of upcoming figures.
        music: Music that plays in the background.
    """

    def __init__(self, game_mode: GameMode, settings: dict[str, Any]) -> None:
        self.game_mode = game_mode
        self.settings = settings
        self._initialize_surface()
        self._initialize_rect()
        self._initialize_game_components()
        self._start_background_music()
        self.paused = False

    def draw(self) -> None:
        """Draw the score on the score surface."""
        self._update_display_surface()
        self._draw_background()

    def update(self) -> None:
        """
        Raises:
            NotImplementedError: Not implemented yet.
        """
        raise NotImplementedError

    def run(self) -> None:
        """Run a single iteration of the game loop."""
        self.draw()
        self.tetris.run()
        self.score.run()
        self.preview.update(self.next_figure)
        self.preview.run()

        if self.paused:
            self.pause_screen.draw()

        self.clock.tick(CONFIG.game.fps)

    def mute(self) -> None:
        """Mute the game."""
        self.music.set_volume(0)
        self.tetris.mute()

    def pause(self) -> None:
        """Pause the game."""
        if self.paused:
            logger.debug("Unpause")
            self.paused = False
            self.tetris.unfreeze()
            self.music.play(-1, fade_ms=100)
        else:
            logger.debug("Pause")
            self.paused = True
            self.tetris.freeze()
            self.music.fadeout(100)

    def _initialize_game_components(self) -> None:
        """Initialize game-related components."""
        self.clock = pygame.time.Clock()
        self.next_figure: Figure = self._generate_next_figure()

        self.tetris = Tetris(self._get_next_figure, self._update_score, self.game_mode, self.settings)
        self.score = Score(self.game_mode)
        self.preview = Preview()
        self.pause_screen = Pause()

    def _update_score(self, lines: int, score: int, level: int) -> None:
        """
        Update the game score.

        Args:
            lines: Number of lines cleared.
            score: Current score.
            level: Current game level.
        """
        self.score.update(lines, score, level)

    def _generate_next_figure(self) -> Figure:
        """
        Generate the next set of random figures.

        Returns:
            Randomly generated figure.
        """
        return Figure.random()

    def _get_next_figure(self) -> Figure:
        """
        Get the next figure in the sequence.

        Returns:
            The next figure in the sequence.
        """
        next_figure: Figure = self.next_figure
        self.next_figure = self._generate_next_figure()
        return next_figure

    def _start_background_music(self) -> None:
        """Start playing background music."""
        if self.game_mode is GameMode.PLAYER and self.settings["Volume"]["Music"]["enabled"]:
            self.music = pygame.mixer.Sound(CONFIG.music.background)
            self.music.set_volume(self.settings["Volume"]["Music"]["level"])
            self.music.play(-1)

    def _initialize_surface(self) -> None:
        """Initialize the pause screen surface."""
        self.surface = pygame.Surface(CONFIG.window.size)
        self.display_surface = pygame.display.get_surface()

    def _initialize_rect(self) -> None:
        """Initialize the score rectangle."""
        self.rect = self.surface.get_rect(topleft=(0, 0))

    def _draw_background(self) -> None:
        """Draw the background."""
        self.surface.fill(CONFIG.colors.bg)

    def _update_display_surface(self) -> None:
        """Update the display surface."""
        self.display_surface.blit(self.surface, self.rect)

    def _draw_border(self) -> None:
        """Draw the border.

        Raises:
            NotImplementedError: Not implemented yet.
        """
        raise NotImplementedError
