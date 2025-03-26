import pygame
from pygame import Surface

from src.renderers.TextRenderer import TextRenderer


class InfoRenderer(TextRenderer):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.font = pygame.font.SysFont('Cascadia Code Regular', 18)

    def render_info(self, text: str) -> None:
        self.render_text(text, (720, 20), background=None)
