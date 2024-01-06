import sys

import pygame
from utils import CONFIG, Figure, GameMode

from .game import Game
from .log import log
from .preview import Preview
from .score import Score
from .tetromino import Tetromino


class Main:
    """
    Main class for the game.

    Attributes:
        display_surface: Pygame display surface.
        clock: Pygame clock.
        music: Pygame music.
        game: Game object.
        score: Score object.
        preview: Preview object.
        next_figures: List of upcoming figures.
        music: Pygame music that plays in the background.
    """

    def __init__(self, mode: GameMode) -> None:
        log.info("Initializing the game")
        self.game_mode = mode
        self._initialize_pygeme()
        self._initialize_game_components()
        self._start_background_music()

    def draw(self) -> None:
        """Update the display."""
        pygame.display.update()

    def run(self) -> None:
        """Run the main game loop."""
        while True:
            self.run_game_loop()

    def run_game_loop(self) -> None:
        """Run a single iteration of the game loop."""
        self.draw()
        self.handle_events()

        self.game.run()
        self.score.run()
        self.preview.run(self.next_figure)

        pygame.display.update()
        self.clock.tick(CONFIG.fps)

    def handle_events(self) -> None:
        """Handle Pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.exit()

    def exit(self) -> None:
        """Exit the game."""
        pygame.quit()
        sys.exit()

    def _initialize_game_components(self) -> None:
        """Initialize game-related components."""
        self.next_figure: Figure = self._generate_next_figure()

        self.game = Game(self._get_next_figure, self._update_score)
        self.score = Score()
        self.preview = Preview()

    def mute(self) -> None:
        """Mute the game."""
        self.music.set_volume(0)
        self.game.mute()

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

    def _initialize_pygeme(self) -> None:
        """Initialize Pygame and set up the display."""
        pygame.init()
        pygame.display.set_caption(CONFIG.window.title)
        self.display_surface = pygame.display.set_mode(CONFIG.window.size)
        self.display_surface.fill(CONFIG.colors.bg)
        self.clock = pygame.time.Clock()

    def _start_background_music(self) -> None:
        """Start playing background music."""
        self.music = pygame.mixer.Sound(CONFIG.music.background)
        self.music.set_volume(CONFIG.music.volume)
        self.music.play(-1)
