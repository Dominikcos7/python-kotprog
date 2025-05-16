import pygame
from pygame import Surface

from src.renderers.Renderer import Renderer


class TextRenderer(Renderer):
    """
    This class is responsible for rendering text on the screen.
    """

    def __init__(self, screen: Surface):
        """
        :param screen: the pygame Surface to render the info on
        """

        super().__init__(screen)
        self.font = pygame.font.SysFont('Cascadia Code Regular', 12)

    def render_text(self, text: str, position: tuple[float, float], color=(255, 255, 255), background=(60, 60, 60, 0.25)) -> None:
        """
        :param text: the text to be rendered
        :param position: the position of the text to be rendered on the screen (tuple[float, float])
        :param color: the colour of the text to be rendered
        :param background: the background colour of the text to be rendered
        """

        rendered_text = self.font.render(text, True, color, background)
        rect = rendered_text.get_rect()
        rect.center = position
        self.screen.blit(rendered_text, rect)
