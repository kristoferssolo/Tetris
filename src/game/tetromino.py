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
        for block in self.blocks:
            block.pos.y += 1

    def move_horizontal(self, direction: Direction) -> None:
        for block in self.blocks:
            block.pos.x += direction.value

    def next_move_horizontal_collide(self, block: Block, direction: Direction) -> None:
        for block in self.blocks:
            block.pos.x += direction.value
