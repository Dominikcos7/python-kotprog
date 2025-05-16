import pygame
from pygame import Surface

from src.renderers.Renderer import Renderer
from src.resource_path import get_resource_path


class TableRenderer(Renderer):
    """
    This class is responsible for rendering the table on the screen.
    """

    DEFAULT_POSITION = (450, 200)
    SCALE = 0.35

    def __init__(self, screen: Surface):
        """
        :param screen: the pygame Surface to render the info on
        """

        super().__init__(screen)
        self.image = pygame.image.load(get_resource_path('img/table.png'))
        w, h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (w * self.SCALE, h * self.SCALE))

    def render_table(self) -> None:
        self.screen.blit(self.image, self.DEFAULT_POSITION)
