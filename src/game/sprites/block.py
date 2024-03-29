from typing import Any, Optional

import numpy as np
import pygame
from utils import CONFIG, Rotation


class Block(pygame.sprite.Sprite):
    """
    Initializes a Block object.

    Args:
        group: Sprite group to which the block belongs.
        pos: Initial position of the block.
        color: Color of the block.

    Attributes:
        image: Image representing the block.
        pos: Position of the block.
        rect: Rectangle representing the block.
    """

    def __init__(
        self,
        /,
        *,
        group: pygame.sprite.Group,  # type: ignore
        pos: pygame.Vector2,
        color: str,
        phantom: bool = False,
    ) -> None:
        super().__init__(group)
        self.phantom = phantom
        self._initialize_image(color)
        self._initialize_positions(pos)

    def update(self) -> None:
        """Updates the block's position on the screen."""
        if self.rect:
            self.rect.topleft = (
                self.pos.x * CONFIG.game.cell.width,
                self.pos.y * CONFIG.game.cell.width,
            )

    def vertical_collision(self, x: int, field: np.ndarray[Optional["Block"], Any]) -> bool:
        """
        Checks for vertical collision with the game field.

        Args:
            x: The x-coordinate to check for collision.
            field: 2D array representing the game field.

        Returns:
            True if there is a vertical collision, False otherwise.
        """
        return not 0 <= x < CONFIG.game.columns or field[int(self.pos.y), x]

    def horizontal_collision(self, y: int, field: np.ndarray[Optional["Block"], Any]) -> bool:
        """
        Checks for horizontal collision with the game field.

        Args:
            y: The y-coordinate to check for collision.
            field: 2D array representing the game field.

        Returns:
            True if there is a horizontal collision, False otherwise.
        """
        return y >= CONFIG.game.rows or (y >= 0 and field[y, int(self.pos.x)])

    def rotate(self, pivot: pygame.Vector2, rotation: Rotation) -> pygame.Vector2:
        """
        Rotates the block around a given pivot point.

        Args:
            pivot: The pivot point for rotation.
            rotation: The rotation direction.

        Returns:
            The new position of the block after rotation.
        """
        return pivot + (self.pos - pivot).rotate(rotation.value)

    def _initialize_image(self, color: str) -> None:
        """
        Initializes the image of the block with a specified color.

        Args:
            color: Color of the block.
        """
        self.image = pygame.Surface(CONFIG.game.cell)
        if self.phantom:
            self.image.set_alpha(75)
        self.image.fill(color)

    def _initialize_positions(self, pos: pygame.Vector2) -> None:
        """
        Initializes the position of the block.

        Args:
            pos: Initial position of the block.
        """
        self.pos = pygame.Vector2(pos) + CONFIG.game.offset
        if self.image:
            self.rect = self.image.get_rect(topleft=self.pos * CONFIG.game.cell.width)
