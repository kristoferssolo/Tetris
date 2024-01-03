import pygame
from utils import CONFIG, Position, Size


class Block(pygame.sprite.Sprite):
    def __init__(
        self, /, *, group: pygame.sprite.Group, pos: Position, color: str
    ) -> None:
        super().__init__(group)
        self.image = pygame.Surface(CONFIG.game.cell)
        self.image.fill(color)

        self.rect = self.image.get_rect(topleft=(0, 0))
