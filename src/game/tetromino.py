from typing import Callable, Optional

import numpy as np
import pygame
from utils import CONFIG, Direction, Figure, Size

from .block import Block
from .log import log


class Tetromino:
    def __init__(
        self,
        group: pygame.sprite.Group,
        func: Callable[[], None],
        field: np.ndarray,
        shape: Optional[Figure] = None,
    ) -> None:
        self.figure: Figure = shape if shape else Figure.random()
        self.block_positions: list[pygame.Vector2] = self.figure.value.shape
        self.color: str = self.figure.value.color
        self.create_new = func
        self.field = field

        self.blocks = [
            Block(group=group, pos=pos, color=self.color)
            for pos in self.block_positions
        ]

    def move_down(self) -> None:
        if not self._check_horizontal_collision(self.blocks, Direction.DOWN):
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field[int(block.pos.y), int(block.pos.x)] = block
            self.create_new()

    def move_horizontal(self, direction: Direction) -> None:
        if not self._check_vertical_collision(self.blocks, direction):
            for block in self.blocks:
                block.pos.x += direction.value

    def rotate(self) -> None:
        if self.figure == Figure.O:
            return

        pivot: pygame.Vector2 = self.blocks[0].pos

        new_positions: list[pygame.Vector2] = [
            block.rotate(pivot) for block in self.blocks
        ]

        if not self._are_new_positions_valid(new_positions):
            return

        self._update_block_positions(new_positions)

    def _check_vertical_collision(
        self, blocks: list[Block], direction: Direction
    ) -> bool:
        return any(
            block.vertical_collision(int(block.pos.x + direction.value), self.field)
            for block in self.blocks
        )

    def _check_horizontal_collision(
        self, blocks: list[Block], direction: Direction
    ) -> bool:
        return any(
            block.horizontal_collision(int(block.pos.y + direction.value), self.field)
            for block in self.blocks
        )

    def _are_new_positions_valid(self, new_positions: list[pygame.Vector2]) -> bool:
        for pos in new_positions:
            if not (
                0 <= pos.x < CONFIG.game.columns and 0 <= pos.y <= CONFIG.game.rows
            ):
                return False
            if self.field[int(pos.y), int(pos.x)]:
                return False
        return True

    def _update_block_positions(self, new_positions: list[pygame.Vector2]) -> None:
        for block, new_pos in zip(self.blocks, new_positions):
            block.pos = new_pos
