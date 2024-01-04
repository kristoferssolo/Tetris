import pygame
from utils import CONFIG, Size


class Block(pygame.sprite.Sprite):
    def __init__(
        self, /, *, group: pygame.sprite.Group, pos: pygame.Vector2, color: str
    ) -> None:
        super().__init__(group)
        self.image = pygame.Surface(CONFIG.game.cell)
        self.image.fill(color)

        self.pos = pygame.Vector2(pos) + CONFIG.game.offset
        self.rect = self.image.get_rect(topleft=self.pos * CONFIG.game.cell.width)

    def update(self) -> None:
        self.rect.topleft = self.pos * CONFIG.game.cell.width
