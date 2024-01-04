from typing import Callable, Optional

import numpy as np
import pygame
from utils import CONFIG, Direction, Field, Figure

from .block import Block
from .log import log
from .tetromino import Tetromino
from .timer import Timer, Timers


class Game:
    def __init__(
        self,
        get_next_figure: Callable[[], Figure],
        update_score: Callable[[int, int, int], None],
    ) -> None:
        self.surface = pygame.Surface(CONFIG.game.size)
        self.dispaly_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=CONFIG.game.pos)

        self.sprites: pygame.sprite.Group[Block] = pygame.sprite.Group()

        self.get_next_shape = get_next_figure
        self.update_score = update_score

        self._create_grid_surface()

        self.field = self._generate_empty_field()

        self.tetromino = Tetromino(
            self.sprites,
            self.create_new_tetromino,
            self.field,
        )

        self.initial_block_speed = CONFIG.game.initial_speed
        self.increased_block_speed = self.initial_block_speed * 0.3
        self.down_pressed = False
        self.timers = Timers(
            Timer(self.initial_block_speed, True, self.move_down),
            Timer(CONFIG.game.movment_delay),
            Timer(CONFIG.game.rotation_delay),
        )
        self.timers.vertical.activate()

        self.level = 1
        self.score = 0
        self.lines = 0

    def run(self) -> None:
        self.dispaly_surface.blit(self.surface, CONFIG.game.pos)
        self.draw()
        self._timer_update()
        self.handle_event()

    def draw(self) -> None:
        self.surface.fill(CONFIG.colors.bg_float)
        self.update()
        self.sprites.draw(self.surface)
        self._draw_border()
        self._draw_grid()

    def update(self) -> None:
        self.sprites.update()

    def handle_event(self) -> None:
        keys = pygame.key.get_pressed()

        left_keys = keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_h]
        right_keys = keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_l]
        down_keys = keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_j]
        rotate_keys = (
            keys[pygame.K_SPACE]
            or keys[pygame.K_r]
            or keys[pygame.K_UP]
            or keys[pygame.K_w]
            or keys[pygame.K_k]
        )

        if not self.timers.horizontal.active:
            if left_keys:
                self.move_left()
                self.timers.horizontal.activate()
            elif right_keys:
                self.move_right()
                self.timers.horizontal.activate()

        if not self.timers.rotation.active:
            if rotate_keys:
                self.tetromino.rotate()
                self.timers.rotation.activate()

        if not self.down_pressed and down_keys:
            self.down_pressed = True
            self.timers.vertical.duration = self.increased_block_speed

        if self.down_pressed and not down_keys:
            self.down_pressed = False
            self.timers.vertical.duration = self.initial_block_speed

    def move_down(self) -> None:
        self.tetromino.move_down()

    def move_left(self) -> None:
        self.tetromino.move_horizontal(Direction.LEFT)

    def move_right(self) -> None:
        self.tetromino.move_horizontal(Direction.RIGHT)

    def create_new_tetromino(self) -> None:
        if self.game_over():
            self.restart()

        self._check_finished_rows()
        self.tetromino = Tetromino(
            self.sprites,
            self.create_new_tetromino,
            self.field,
            self.get_next_shape(),
        )

    def game_over(self) -> bool:
        for block in self.sprites:
            if block.pos.y < 0:
                log.info("Game over!")
                return True

    def restart(self) -> None:
        self.sprites.empty()
        self.field = self._generate_empty_field()
        self.tetromino = Tetromino(
            self.sprites,
            self.create_new_tetromino,
            self.field,
            self.get_next_shape(),
        )
        self.level = 1
        self.score = 0
        self.lines = 0
        self.update_score(self.lines, self.score, self.level)

    def _create_grid_surface(self) -> None:
        self.grid_surface = self.surface.copy()
        self.grid_surface.fill("#00ff00")
        self.grid_surface.set_colorkey("#00ff00")
        self.grid_surface.set_alpha(100)

    def _draw_grid(self) -> None:
        for col in range(1, CONFIG.game.columns):
            x = col * CONFIG.game.cell.width
            pygame.draw.line(
                self.grid_surface,
                CONFIG.colors.border_highlight,
                (x, 0),
                (x, self.grid_surface.get_height()),
                CONFIG.game.line_width,
            )
            for row in range(1, CONFIG.game.rows):
                y = row * CONFIG.game.cell.width
                pygame.draw.line(
                    self.grid_surface,
                    CONFIG.colors.border_highlight,
                    (0, y),
                    (self.grid_surface.get_width(), y),
                    CONFIG.game.line_width,
                )

        self.surface.blit(self.grid_surface, (0, 0))

    def _draw_border(self) -> None:
        pygame.draw.rect(
            self.dispaly_surface,
            CONFIG.colors.border_highlight,
            self.rect,
            CONFIG.game.line_width * 2,
            CONFIG.game.border_radius,
        )

    def _timer_update(self) -> None:
        for timer in self.timers:
            timer.update()

    def _check_finished_rows(self) -> None:
        delete_rows: list[int] = []
        for idx, row in enumerate(self.field):
            if all(row):
                delete_rows.append(idx)

        self._delete_rows(delete_rows)

    def _delete_rows(self, delete_rows: list[int]) -> None:
        if not delete_rows:
            return
        self._calculate_score(len(delete_rows))

        for row in delete_rows:
            for block in self.field[row]:
                block.kill()

            self._move_rows_down(row)
        self._rebuild_field()

    def _move_rows_down(self, deleted_row: int) -> None:
        for row in self.field:
            for block in row:
                if block and block.pos.y < deleted_row:
                    block.pos.y += 1

    def _rebuild_field(self) -> None:
        self.field = self._generate_empty_field()

        for block in self.sprites:
            self.field[int(block.pos.y), int(block.pos.x)] = block

    def _generate_empty_field(self) -> np.ndarray:
        return np.full((CONFIG.game.rows, CONFIG.game.columns), None, dtype=Field)

    def _calculate_score(self, rows_deleted: int) -> None:
        self.lines += rows_deleted
        self.score += CONFIG.game.score.get(rows_deleted, 0) * self.level

        # every 10 lines increase level
        if self.lines // 10 + 1 > self.level:
            self.level += 1
            self.initial_block_speed *= 0.75
            self.increased_block_speed *= 0.75
            self.timers.vertical.duration = self.initial_block_speed

        self.update_score(self.lines, self.score, self.level)
