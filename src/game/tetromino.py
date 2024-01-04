from typing import Optional

import pygame
from utils import CONFIG, Figure, FigureConfig, Size

from .block import Block


class Tetromino:
    def __init__(self, shape: Optional[Figure], /, group: pygame.sprite.Group) -> None:
        self.figure: FigureConfig = shape.value if shape else Figure.random().value
        self.block_positions: list[pygame.Vector2] = self.figure.shape
        self.color: str = self.figure.color

        self.blocks = [
            Block(group=group, pos=pos, color=self.color)
            for pos in self.block_positions
        ]
