import pygame
from utils import CONFIG, Size


class Score:
    def __init__(self) -> None:
        self.surface = pygame.Surface(CONFIG.sidebar.score)
        self.dispaly_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(
            bottomright=CONFIG.window.size.sub(CONFIG.window.padding)
        )

        self.font = pygame.font.Font(CONFIG.font.family, CONFIG.font.size)

        self.update(1, 0, 0)

        self.increment_height = self.surface.get_height() / 3

    def run(self) -> None:
        self.dispaly_surface.blit(self.surface, self.rect)
        self.draw()

    def update(self, lines: int, score: int, level: int) -> None:
        self.text = (
            ("Score", score),
            ("Level", level),
            ("Lines", lines),
        )

    def draw(self) -> None:
        self.surface.fill(CONFIG.colors.bg_sidebar)
        self._draw_text()
        self._draw_border()

    def _draw_text(self) -> None:
        for idx, text in enumerate(self.text):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + idx * self.increment_height
            self._display_text(text, (x, y))

    def _display_text(self, text: tuple[str, int], pos: tuple[int, int]) -> None:
        text_surface = self.font.render(
            f"{text[0]}: {text[1]}", True, CONFIG.colors.fg_sidebar
        )
        text_rect = text_surface.get_rect(center=pos)
        self.surface.blit(text_surface, text_rect)

    def _draw_border(self) -> None:
        pygame.draw.rect(
            self.dispaly_surface,
            CONFIG.colors.border_highlight,
            self.rect,
            CONFIG.game.line_width * 2,
            CONFIG.game.border_radius,
        )
