from typing import Any

import pygame
from utils import CONFIG, Figure, GameMode

from game.log import log
from game.sprites import Tetromino

from .base import BaseScreen
from .preview import Preview
from .score import Score
from .tetris import Tetris


class Game(BaseScreen):
    """
    Game class.

    Attributes:
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
        self.paused = False
        self._initialize_game_components()
        self._start_background_music()

    def draw(self) -> None:
        """Update the display."""

    def update(self) -> None:
        pass

    def run(self) -> None:
        """Run a single iteration of the game loop."""
        self.draw()

        self.tetris.run()
        self.score.run()
        self.preview.update(self.next_figure)
        self.preview.run()

        self.draw()
        self.clock.tick(CONFIG.fps)

    def mute(self) -> None:
        """Mute the game."""
        self.music.set_volume(0)
        self.tetris.mute()

    def _initialize_game_components(self) -> None:
        """Initialize game-related components."""
        self.clock = pygame.time.Clock()
        self.next_figure: Figure = self._generate_next_figure()

        self.tetris = Tetris(
            self._get_next_figure, self._update_score, self.game_mode, self.settings
        )
        self.score = Score(self.game_mode)
        self.preview = Preview()

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
        if (
            self.game_mode is GameMode.PLAYER
            and self.settings["Volume"]["Music"]["enabled"]
        ):
            self.music = pygame.mixer.Sound(CONFIG.music.background)
            self.music.set_volume(self.settings["Volume"]["Music"]["level"])
            self.music.play(-1)
