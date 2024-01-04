import numpy as np
import pygame
from utils import CONFIG, Size


class Block(pygame.sprite.Sprite):
    def __init__(
        self,
        /,
        *,
        group: pygame.sprite.Group,
        pos: pygame.Vector2,
        color: str,
    ) -> None:
        super().__init__(group)
        self.image = pygame.Surface(CONFIG.game.cell)
        self.image.fill(color)

        self.pos = pygame.Vector2(pos) + CONFIG.game.offset
        self.rect = self.image.get_rect(topleft=self.pos * CONFIG.game.cell.width)

    def update(self) -> None:
        self.rect.topleft = self.pos * CONFIG.game.cell.width

    def vertical_collision(self, x: int, field: np.ndarray) -> bool:
        return not 0 <= x < CONFIG.game.columns or field[int(self.pos.y), x]

    def horizontal_collision(self, y: int, field: np.ndarray) -> bool:
        return y >= CONFIG.game.rows or (y >= 0 and field[y, int(self.pos.x)])
