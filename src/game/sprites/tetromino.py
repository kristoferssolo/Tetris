from typing import Any, Callable, Optional

import numpy as np
import pygame
from utils import CONFIG, Direction, Figure, Rotation, Size

from game.log import log

from .block import Block


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
        create_new: Optional[Callable[[Optional[Figure]], "Tetromino"]],
        field: np.ndarray[Optional[Block], Any],
        shape: Optional[Figure] = None,
        phantom: bool = False,
    ) -> None:
        self.figure: Figure = self._generate_figure(shape)
        self.block_positions: list[pygame.Vector2] = self.figure.value.shape
        self.color: str = self.figure.value.color
        self.create_new = create_new
        self.field = field
        self.phantom = phantom
        self.blocks = self._initialize_blocks(group)

    def move_down(self) -> bool:
        """
        Moves the Tetromino down.

        If there is a collision, the Tetromino is placed on the field, and a new one is created.

        Returns:
            True if the movement was successful, False otherwise.
        """
        if not self._check_horizontal_collision(self.blocks, Direction.DOWN):
            for block in self.blocks:
                block.pos.y += 1
            return True

        for block in self.blocks:
            self.field[int(block.pos.y), int(block.pos.x)] = block

        if self.create_new:
            self.create_new(None)

        return False

    def move_horizontal(self, direction: Direction) -> bool:
        """
        Moves the Tetromino horizontally.

        Args:
            direction: Direction to move (LEFT or RIGHT).

        Returns:
            True if the movement was successful, False otherwise.
        """
        if not self._check_vertical_collision(self.blocks, direction):
            for block in self.blocks:
                block.pos.x += direction.value
            return True
        return False

    def rotate(self, rotation: Rotation = Rotation.CLOCKWISE) -> bool:
        """
        Rotates the Tetromino.

        Does not rotate if the Tetromino is an O-shaped (square) figure.

        Args:
            rotation: Rotation to perform (CLOCKWISE or COUNTER_CLOCKWISE).

        Returns:
            True if the rotation was successful, False otherwise.
        """
        if self.figure == Figure.O:
            return False

        pivot: pygame.Vector2 = self.blocks[0].pos

        for _ in range(3):
            new_positions: list[pygame.Vector2] = [
                block.rotate(pivot, rotation) for block in self.blocks
            ]

            if self._are_new_positions_valid(new_positions):
                self.update_block_positions(new_positions)
                return True

            if any(pos.x < 0 for pos in new_positions):
                self.move_horizontal(Direction.RIGHT)
            else:
                self.move_horizontal(Direction.LEFT)

        return False

    def drop(self) -> bool:
        """
        Drops the Tetromino to the bottom of the game field.

        Returns:
            True if the drop was successful, False otherwise.
        """

        while not self._check_horizontal_collision(self.blocks, Direction.DOWN):
            for block in self.blocks:
                block.pos.y += 1

        return True

    def kill(self) -> None:
        for block in self.blocks:
            block.kill()

    def check_collision(self, direction: Direction) -> bool:
        """
        Checks if there is a collision in the given direction.

        Args:
            direction: Direction to check (UP, DOWN, LEFT, or RIGHT).

        Returns:
            True if there is a collision, False otherwise.
        """

        return self._check_horizontal_collision(
            self.blocks, direction
        ) or self._check_vertical_collision(self.blocks, direction)

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

    def update_block_positions(self, new_positions: list[pygame.Vector2]) -> None:
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
            and -2 <= pos.y < CONFIG.game.rows
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
            Block(group=group, pos=pos, color=self.color, phantom=self.phantom)
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
