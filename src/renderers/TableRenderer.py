import pygame
from pygame import Surface

from src.renderers.Renderer import Renderer


class TableRenderer(Renderer):
    DEFAULT_POSITION = (450, 200)
    SCALE = 0.35

    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.image = pygame.image.load('./src/img/table.png')
        w, h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (w * self.SCALE, h * self.SCALE))

    def render_table(self) -> None:
        self.screen.blit(self.image, self.DEFAULT_POSITION)
