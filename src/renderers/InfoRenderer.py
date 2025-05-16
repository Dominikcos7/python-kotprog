import pygame
from pygame import Surface

from src.renderers.TextRenderer import TextRenderer


class InfoRenderer(TextRenderer):
    """
    This class is responsible for rendering information on the screen.
    """

    def __init__(self, screen: Surface):
        """
        :param screen: the pygame Surface to render the info on
        """

        super().__init__(screen)
        self.font = pygame.font.SysFont('Cascadia Code Regular', 18)

    def render_info(self, text: str) -> None:
        """
        :param text: the text to render
        """

        self.render_text(text, (720, 20), background=None)
