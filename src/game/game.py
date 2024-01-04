from typing import Callable, Optional

import numpy as np
import pygame
from utils import CONFIG, Direction, Field, Figure

from .block import Block
from .log import log
from .tetromino import Tetromino
from .timer import Timer, Timers


class Game:
    def __init__(self, get_next_figure: Callable[[], Figure]) -> None:
        self.surface = pygame.Surface(CONFIG.game.size)
        self.dispaly_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=CONFIG.game.pos)

        self.sprites: pygame.sprite.Group[Block] = pygame.sprite.Group()

        self.get_next_shape = get_next_figure

        self._create_grid_surface()

        self.field = self._generate_empty_field()

        self.tetromino = Tetromino(
            self.sprites,
            self.create_new_tetromino,
            self.field,
        )

        self.timers = Timers(
            Timer(CONFIG.game.initial_speed, True, self.move_down),
            Timer(CONFIG.game.movment_delay),
            Timer(CONFIG.game.rotation_delay),
        )

        self.timers.vertical.activate()

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

        if not self.timers.horizontal.active:
            if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_h]:
                self.move_left()
                self.timers.horizontal.activate()
            elif keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_j]:
                self.move_down()
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_l]:
                self.move_right()
                self.timers.horizontal.activate()

        if not self.timers.rotation.active:
            if (
                keys[pygame.K_SPACE]
                or keys[pygame.K_r]
                or keys[pygame.K_UP]
                or keys[pygame.K_w]
                or keys[pygame.K_k]
            ):
                self.tetromino.rotate()
                self.timers.rotation.activate()

    def move_down(self) -> None:
        self.tetromino.move_down()

    def move_left(self) -> None:
        self.tetromino.move_horizontal(Direction.LEFT)

    def move_right(self) -> None:
        self.tetromino.move_horizontal(Direction.RIGHT)

    def create_new_tetromino(self) -> None:
        self._check_finished_rows()
        self.tetromino = Tetromino(
            self.sprites,
            self.create_new_tetromino,
            self.field,
            self.get_next_shape(),
        )

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
