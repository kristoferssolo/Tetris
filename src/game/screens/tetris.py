from typing import Any, Callable, Optional

import numpy as np
import pygame
from loguru import logger
from utils import CONFIG, Direction, Figure, GameMode, Rotation

from game.sprites import Block, Tetromino
from game.timer import Timer, Timers

from .base import BaseScreen


class Tetris(BaseScreen):
    """
    Game class for managing the game state.

    Args:
        get_next_figure: A function to get the next figure.
        update_score: A function to update the score.
        mode: The game mode to start with.

    Attributes:
        surface: Surface representing the game.
        dispaly_surface: Surface representing the display.
        rect: Rect representing the game surface.
        sprites: Sprite group for managing blocks.
        settings: The game settings.
        game_mode: The game mode.
        get_next_figure: A function to get the next figure.
        update_score: A function to update the score.
        grid_surface: Surface representing the grid.
        field: 2D array representing the game field.
        tetromino: The current tetromino.
        timers: Game timers.
        initial_block_speed: Initial block speed.
        increased_block_speed: Increased block speed.
        down_pressed: True if the down key is pressed, False otherwise.
        level: Current game level.
        score: Current game score.
        lines: Number of lines cleared.
        game_over: True if the game is over, False otherwise.
        landing_sound: Sound effect for landing blocks.
    """

    def __init__(
        self,
        get_next_figure: Callable[[], Figure],
        update_score: Callable[[int, int, int], None],
        game_mode: GameMode,
        settings: dict[str, Any],
    ) -> None:
        self._initialize_surface()
        self._initialize_rect()
        self._initialize_sprites()
        self.settings = settings

        self.get_next_figure = get_next_figure
        self.update_score = update_score
        self.game_mode = game_mode

        self._initialize_grid_surface()
        self._initialize_field_and_tetromino()
        self.tetromino: Tetromino
        self.phantom_tetromino: Tetromino

        self._initialize_game_state()
        self._initialize_timers()
        self.timers: Timers
        self._initialize_sound()

    def run(self) -> None:
        """Run a single iteration of the game loop."""
        self.draw()
        self._timer_update()
        self.handle_events()

    def draw(self) -> None:
        """Draw the game surface and its components."""
        self.update()
        self._draw_background()
        self.sprites.draw(self.surface)
        self.phantom_sprites.draw(self.surface)
        self._draw_border()
        self._draw_grid()

    def update(self) -> None:
        self._update_display_surface()
        self.sprites.update()
        self.phantom_sprites.update()

    def handle_events(self) -> None:
        """Handle player input events."""
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()

        self._handle_movement_keys(keys)
        self._handle_rotation_keys(keys)
        self._handle_down_key(keys)
        self._handle_drop_key(keys)
        self._handle_pause_key(keys)

    def move_down(self) -> bool:
        """
        Move the current tetromino down.

        Returns:
            True if the movement was successful, False otherwise.
        """
        return self.tetromino.move_down()

    def move_left(self) -> bool:
        """
        Move the current tetromino to the left.

        Returns:
            True if the movement was successful, False otherwise.
        """
        moved = self.tetromino.move_horizontal(Direction.LEFT)
        self._update_phantom_position()
        return moved

    def move_right(self) -> bool:
        """
        Move the current tetromino to the right.

        Returns:
            True if the movement was successful, False otherwise.
        """

        moved = self.tetromino.move_horizontal(Direction.RIGHT)
        self._update_phantom_position()
        return moved

    def rotate(self) -> bool:
        """
        Rotate the current tetromino clockwise.

        Returns:
            True if the rotation was successful, False otherwise.
        """
        rotated = self.tetromino.rotate()
        self._update_phantom_position()
        return rotated

    def rotate_reverse(self) -> bool:
        """
        Rotate the current tetromino counter-clockwise.

        Returns:
            True if the rotation was successful, False otherwise.
        """
        rotated = self.tetromino.rotate(Rotation.COUNTER_CLOCKWISE)
        self._update_phantom_position()
        return rotated

    def drop(self) -> bool:
        """
        Drop the current tetromino.

        Returns:
            True if the movement was successful, False otherwise.
        """
        return self.tetromino.drop()

    def restart(self) -> None:
        """Restart the game."""
        logger.info(f"Restarting the game. Score was {self.score}")
        self._reset_game_state()

    def pause(self) -> None:
        """Pause the game."""
        self.paused: bool
        if self.paused:
            logger.debug("Unpause")
            self.paused = False
            self.timers.unpause()
        else:
            logger.debug("Pause")
            self.paused = True
            self.timers.pause()

    def mute(self) -> None:
        """Mute the game."""
        self.landing_sound.set_volume(0)

    def create_new_tetromino(self, shape: Optional[Figure] = None) -> Optional[Tetromino]:
        """Create a new tetromino and perform necessary actions."""
        self._play_landing_sound()
        self._check_finished_rows()
        self.phantom_sprites.empty()

        self.game_over: bool = self._check_game_over()
        if self.game_over:
            self.restart()
            return None

        self.tetromino = Tetromino(
            self.sprites,
            self.create_new_tetromino,
            self.field,
            shape or self.get_next_figure(),
        )

        self.phantom_tetromino = Tetromino(
            self.phantom_sprites,
            None,
            self.field,
            self.tetromino.figure,
            True,
        )
        self.phantom_tetromino.drop()
        logger.debug(f"Created: {self.tetromino.figure.name}")

        return self.tetromino

    def _check_game_over(self) -> bool:
        """
        Check if the game is over.

        Returns:
            True if the game is over, False otherwise.
        """
        for block in self.tetromino.blocks:
            if block.pos.y <= 0:
                logger.info("Game over!")
                return True
        return False

    def _draw_grid(self) -> None:
        """Draw the grid on the game surface."""
        for col in range(1, CONFIG.game.columns):
            x = col * CONFIG.game.cell.width
            self._draw_vertical_grid_line(x)
        for row in range(1, CONFIG.game.rows):
            y = row * CONFIG.game.cell.width
            self._draw_horizontal_grid_line(y)

        self.surface.blit(self.grid_surface, (0, 0))

    def _draw_border(self) -> None:
        """Draw the border of the game surface."""
        pygame.draw.rect(
            self.dispaly_surface,
            CONFIG.colors.border_highlight,
            self.rect,
            CONFIG.game.line_width * 2,
            CONFIG.game.border_radius,
        )

    def _timer_update(self) -> None:
        """Update the timers."""
        for timer in self.timers:
            timer.update()

    def _check_finished_rows(self) -> None:
        """Check and handle finished rows."""
        delete_rows: list[int] = []
        for idx, row in enumerate(self.field):
            if all(row):
                delete_rows.append(idx)

        self._delete_rows(delete_rows)

    def _delete_rows(self, delete_rows: list[int]) -> None:
        """Delete the specified rows."""
        if not delete_rows:
            return
        self._calculate_score(len(delete_rows))

        for row in delete_rows:
            self._remove_blocks_in_row(row)
            self._move_rows_down(row)
        self._rebuild_field()

    def _remove_blocks_in_row(self, row: int) -> None:
        """Remove blocks in the specified row."""
        for block in self.field[row]:
            if block:
                block.kill()

    def _move_rows_down(self, deleted_row: int) -> None:
        """Move rows down after deleting a row."""
        for row in self.field:
            for block in row:
                if block and block.pos.y < deleted_row:
                    block.pos.y += 1

    def _rebuild_field(self) -> None:
        """Rebuild the game field after deleting rows."""
        self.field = self._generate_empty_field()

        for block in self.sprites:
            self.field[int(block.pos.y), int(block.pos.x)] = block

    def _generate_empty_field(self) -> np.ndarray[Optional[Block], Any]:
        """Generate an empty game field."""
        return np.full((CONFIG.game.rows, CONFIG.game.columns), None)

    def _calculate_score(self, rows_deleted: int) -> None:
        """Calculate and update the game score."""
        self.lines += rows_deleted
        self.score += CONFIG.game.score.get(rows_deleted, 0) * self.level
        self._check_level_up()
        self.update_score(self.lines, self.score, self.level)

    def _check_level_up(self) -> None:
        """Check if the player should level up."""
        # incerement level every 10 lines
        if self.lines // 10 + 1 > self.level:
            self._level_up()

    def _level_up(self) -> None:
        """Level up."""
        self.level += 1
        self.initial_block_speed *= 0.3
        self.increased_block_speed *= 0.3
        self.timers.vertical.duration = self.initial_block_speed

    def _draw_components(self) -> None:
        """Draw additional components like borders and grid."""
        self.sprites.draw(self.surface)
        self.phantom_sprites.draw(self.surface)
        self._draw_border()
        self._draw_grid()

    def _initialize_surface(self) -> None:
        """Initialize the game surface."""
        self.surface = pygame.Surface(CONFIG.game.size)
        self.dispaly_surface = pygame.display.get_surface()

    def _initialize_rect(self) -> None:
        """Initialize the rectangle."""
        self.rect = self.surface.get_rect(topleft=CONFIG.game.pos)

    def _initialize_sprites(self) -> None:
        """Initialize the game sprites."""
        self.sprites: pygame.sprite.Group[Block] = pygame.sprite.Group()
        self.phantom_sprites: pygame.sprite.Group[Block] = pygame.sprite.Group()

    def _initialize_grid_surface(self) -> None:
        """Initialize the grid surface."""
        self.grid_surface = self.surface.copy()
        self.grid_surface.fill("#00ff00")
        self.grid_surface.set_colorkey("#00ff00")
        self.grid_surface.set_alpha(100)

    def _initialize_field_and_tetromino(self) -> None:
        """Initialize the game field and tetromino."""
        self.field = self._generate_empty_field()

        self.tetromino = Tetromino(
            self.sprites,
            self.create_new_tetromino,
            self.field,
        )

        self.phantom_tetromino = Tetromino(
            self.phantom_sprites,
            None,
            self.field,
            self.tetromino.figure,
            True,
        )

        logger.debug(f"Created: {self.tetromino.figure.name}")
        self.phantom_tetromino.drop()

    def _initialize_timers(self) -> None:
        """Initialize game timers."""
        self.timers = Timers(
            Timer(self.initial_block_speed, True, self.move_down),  # type: ignore
            Timer(CONFIG.game.movment_delay),  # type: ignore
            Timer(CONFIG.game.rotation_delay),  # type: ignore
            Timer(CONFIG.game.drop_delay),  # type: ignore
        )
        self.timers.vertical.activate()

    def _initialize_game_state(self) -> None:
        """Initialize the game state."""
        self.initial_block_speed = CONFIG.game.initial_speed
        self.increased_block_speed = self.initial_block_speed * 0.5
        self.down_pressed = False
        self.drop_pressed = False
        self.level: int = 1
        self.score: int = 0
        self.lines: int = 0
        self.game_over = False
        self.paused = False

    def _initialize_sound(self) -> None:
        """Initialize game sounds."""
        if self.game_mode is GameMode.PLAYER and self.settings["Volume"]["SFX"]["enabled"]:
            self.landing_sound = pygame.mixer.Sound(CONFIG.music.landing)
            self.landing_sound.set_volume(self.settings["Volume"]["SFX"]["level"])

    def _play_landing_sound(self) -> None:
        """Play the landing sound effect."""
        if self.game_mode is GameMode.PLAYER and self.settings["Volume"]["SFX"]["enabled"]:
            self.landing_sound.play()

    def _update_display_surface(self) -> None:
        """Update the display surface."""
        self.dispaly_surface.blit(self.surface, CONFIG.game.pos)

    def _update_phantom_position(self) -> None:
        new_positions = [block.pos.copy() for block in self.tetromino.blocks]
        self.phantom_tetromino.update_block_positions(new_positions)
        self.phantom_tetromino.drop()

    def _draw_background(self) -> None:
        """Fill the game surface with background color."""
        self.surface.fill(CONFIG.colors.bg_float)

    def _handle_movement_keys(self, keys: pygame.key.ScancodeWrapper) -> None:
        """
        Handle movement keys.

        See `settings.toml` for the default key bindings.
        """
        right_keys: list[int] = [pygame.key.key_code(key) for key in self.settings["Movement"]["right"]]
        right_key_pressed = any(keys[key] for key in right_keys)

        left_keys: list[int] = [pygame.key.key_code(key) for key in self.settings["Movement"]["left"]]
        left_key_pressed = any(keys[key] for key in left_keys)

        if not self.timers.horizontal.active:
            if left_key_pressed:
                self.move_left()
                self.timers.horizontal.activate()
            elif right_key_pressed:
                self.move_right()
                self.timers.horizontal.activate()

    def _handle_rotation_keys(self, keys: pygame.key.ScancodeWrapper) -> None:
        """
        Handle rotation keys.

        See `settings.toml` for the default key bindings.
        """
        cw_keys: list[int] = [pygame.key.key_code(key) for key in self.settings["Rotation"]["cw"]]
        cw_key_pressed = any(keys[key] for key in cw_keys)

        ccw_keys: list[int] = [pygame.key.key_code(key) for key in self.settings["Rotation"]["ccw"]]
        ccw_key_pressed = any(keys[key] for key in ccw_keys)

        if not self.timers.rotation.active:
            if cw_key_pressed:
                self.rotate()
                self.timers.rotation.activate()

            if ccw_key_pressed:
                self.rotate_reverse()
                self.timers.rotation.activate()

    def _handle_down_key(self, keys: pygame.key.ScancodeWrapper) -> None:
        """
        Handle the down key.

        See `settings.toml` for the default key bindings.
        """
        down_keys: list[int] = [pygame.key.key_code(key) for key in self.settings["Movement"]["down"]]
        down_key_pressed = any(keys[key] for key in down_keys)
        if not self.down_pressed and down_key_pressed:
            self.down_pressed = True
            self.timers.vertical.duration = self.increased_block_speed

        if self.down_pressed and not down_key_pressed:
            self.down_pressed = False
            self.timers.vertical.duration = self.initial_block_speed

    def _handle_drop_key(self, keys: pygame.key.ScancodeWrapper) -> None:
        """
        Handle the drop key.

        See `settings.toml` for the default key bindings.
        """
        drop_keys = [pygame.key.key_code(key) for key in self.settings["Action"]["drop"]]
        drop_key_pressed = any(keys[key] for key in drop_keys)

        if not self.timers.drop.active and drop_key_pressed:
            self.drop()
            self.timers.drop.activate()

    def _handle_pause_key(self, keys: pygame.key.ScancodeWrapper) -> None:
        """
        Handle the pause key.

        See `settings.toml` for the default key bindings.
        """
        pause_keys = [pygame.key.key_code(key) for key in self.settings["General"]["pause"]]
        pause_key_pressed = any(keys[key] for key in pause_keys)

        if pause_key_pressed and not self.timers.horizontal.active:
            self.pause()
            self.timers.horizontal.activate()

    def _reset_game_state(self) -> None:
        """Reset the game state."""
        self.sprites.empty()
        self.phantom_sprites.empty()
        self._initialize_field_and_tetromino()
        self._initialize_game_state()
        self.update_score(self.lines, self.score, self.level)

    def _draw_vertical_grid_line(self, x: int | float) -> None:
        """Draw a vertical grid line."""
        pygame.draw.line(
            self.grid_surface,
            CONFIG.colors.border_highlight,
            (x, 0),
            (x, self.grid_surface.get_height()),
            CONFIG.game.line_width,
        )

    def _draw_horizontal_grid_line(self, y: int | float) -> None:
        """Draw a horizontal grid line."""
        pygame.draw.line(
            self.grid_surface,
            CONFIG.colors.border_highlight,
            (0, y),
            (self.grid_surface.get_width(), y),
            CONFIG.game.line_width,
        )
