import pygame

from src.Renderer import Renderer


class TableRenderer(Renderer):
    DEFAULT_POSITION = (310, 100)
    SCALE = 0.35

    def __init__(self, screen):
        super().__init__(screen)
        self.table = pygame.image.load('./src/img/table.png')
        size = self.table.get_size()
        self.table = pygame.transform.scale(self.table, (size[0] * self.SCALE, size[1] * self.SCALE))

    def render_table(self):
        self.screen.blit(self.table, self.DEFAULT_POSITION)
