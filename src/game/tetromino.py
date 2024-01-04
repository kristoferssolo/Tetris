from typing import Callable, Optional

import numpy as np
import pygame
from utils import CONFIG, Direction, Figure, FigureConfig, Size

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
        self.figure: FigureConfig = shape.value if shape else Figure.random().value
        self.block_positions: list[pygame.Vector2] = self.figure.shape
        self.color: str = self.figure.color
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
