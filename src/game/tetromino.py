from typing import Callable, Optional

import numpy as np
import pygame
from utils import CONFIG, Direction, Figure, Size

from .block import Block
from .log import log


class Tetromino:
    """
    Class representing a Tetromino.

    Args:
        group: Sprite group for managing blocks.
        create_new: Callback function to create a new Tetromino.
        field: 2D array representing the game field.
        shape: Initial shape of the Tetromino (default is None).

    Attributes:
        figure: Tetromino figure.
        block_positions: List of block positions.
        color: Color of the Tetromino.
        create_new: Callback function to create a new Tetromino.
        field: 2D array representing the game field.
        blocks: List of Tetromino blocks.
    """

    def __init__(
        self,
        group: pygame.sprite.Group,
        create_new: Callable[[], None],
        field: np.ndarray,
        shape: Optional[Figure] = None,
    ) -> None:
        self.figure: Figure = self._generate_figure(shape)
        self.block_positions: list[pygame.Vector2] = self.figure.value.shape
        self.color: str = self.figure.value.color
        self.create_new = create_new
        self.field = field
        self.blocks = self._initialize_blocks(group)

    def move_down(self) -> None:
        """
        Moves the Tetromino down.

        If there is a collision, the Tetromino is placed on the field, and a new one is created.
        """
        if not self._check_horizontal_collision(self.blocks, Direction.DOWN):
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field[int(block.pos.y), int(block.pos.x)] = block
            self.create_new()

    def move_horizontal(self, direction: Direction) -> None:
        """
        Moves the Tetromino horizontally.

        Args:
            direction: Direction to move (LEFT or RIGHT).
        """
        if not self._check_vertical_collision(self.blocks, direction):
            for block in self.blocks:
                block.pos.x += direction.value

    def rotate(self) -> None:
        """
        Rotates the Tetromino clockwise.

        Does not rotate if the Tetromino is an O-shaped (square) figure.
        """
        if self.figure == Figure.O:
            return

        pivot: pygame.Vector2 = self.blocks[0].pos

        new_positions: list[pygame.Vector2] = [
            block.rotate(pivot) for block in self.blocks
        ]

        if self._are_new_positions_valid(new_positions):
            self._update_block_positions(new_positions)

    def _check_vertical_collision(
        self, blocks: list[Block], direction: Direction
    ) -> bool:
        """
        Checks for vertical collision.

        Args:
            blocks: List of blocks to check for collision.
            direction: Direction of movement.

        Returns:
            True if there is a vertical collision, False otherwise.
        """
        return any(
            block.vertical_collision(int(block.pos.x + direction.value), self.field)
            for block in self.blocks
        )

    def _check_horizontal_collision(
        self, blocks: list[Block], direction: Direction
    ) -> bool:
        """
        Checks for horizontal collision.

        Args:
            blocks: List of blocks to check for collision.
            direction: Direction of movement.

        Returns:
            True if there is a horizontal collision, False otherwise.
        """
        return any(
            block.horizontal_collision(int(block.pos.y + direction.value), self.field)
            for block in self.blocks
        )

    def _update_block_positions(self, new_positions: list[pygame.Vector2]) -> None:
        """
        Updates the positions of Tetromino blocks.

        Args:
            new_positions: New positions for the blocks.
        """
        for block, new_pos in zip(self.blocks, new_positions):
            block.pos = new_pos

    def _are_new_positions_valid(self, new_positions: list[pygame.Vector2]) -> bool:
        """
        Checks if the new positions are valid within the game field.

        Args:
            new_positions: New positions to check.

        Returns:
            True if all positions are valid, False otherwise.
        """
        return all(
            0 <= pos.x < CONFIG.game.columns
            and 0 <= pos.y <= CONFIG.game.rows
            and not self.field[int(pos.y), int(pos.x)]
            for pos in new_positions
        )

    def _initialize_blocks(self, group: pygame.sprite.Group) -> list[Block]:
        """
        Initializes Tetromino blocks.

        Args:
            group: Sprite group for managing blocks.

        Returns:
            List of initialized blocks.
        """
        return [
            Block(group=group, pos=pos, color=self.color)
            for pos in self.block_positions
        ]

    def _generate_figure(self, shape: Optional[Figure]) -> Figure:
        """
        Generates a Tetromino figure.

        Args:
            shape: Initial shape of the Tetromino (default is None).

        Returns:
            Generated Tetromino figure.
        """
        return shape if shape else Figure.random()
