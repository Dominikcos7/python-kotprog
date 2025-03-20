import pygame
from pygame import Surface

from src.renderers.TextRenderer import TextRenderer


class RaiseInfoRenderer(TextRenderer):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.font = pygame.font.SysFont('Cascadia Code Regular', 18)
