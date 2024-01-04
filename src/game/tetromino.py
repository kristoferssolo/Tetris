from typing import Optional

import pygame
from utils import CONFIG, Direction, Figure, FigureConfig, Size

from .block import Block


class Tetromino:
    def __init__(
        self, group: pygame.sprite.Group, shape: Optional[Figure] = None
    ) -> None:
        self.figure: FigureConfig = shape.value if shape else Figure.random().value
        self.block_positions: list[pygame.Vector2] = self.figure.shape
        self.color: str = self.figure.color

        self.blocks = [
            Block(group=group, pos=pos, color=self.color)
            for pos in self.block_positions
        ]

    def move_down(self) -> None:
        if not self._check_horizontal_collision(self.blocks, Direction.DOWN):
            for block in self.blocks:
                block.pos.y += 1

    def move_horizontal(self, direction: Direction) -> None:
        if not self._check_vertical_collision(self.blocks, direction):
            for block in self.blocks:
                block.pos.x += direction.value

    def _check_vertical_collision(
        self, blocks: list[Block], direction: Direction
    ) -> bool:
        return any(
            block.vertical_collision(int(block.pos.x + direction.value))
            for block in self.blocks
        )

    def _check_horizontal_collision(
        self, blocks: list[Block], direction: Direction
    ) -> bool:
        return any(
            block.horizontal_collision(int(block.pos.y + direction.value))
            for block in self.blocks
        )
