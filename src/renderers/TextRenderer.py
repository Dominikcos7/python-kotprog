import pygame
from pygame import Surface

from src.renderers.Renderer import Renderer


class TextRenderer(Renderer):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.font = pygame.font.SysFont('Cascadia Code Regular', 12)

    def render_text(self, text: str, position: tuple[float, float], color=(255, 255, 255), background=None) -> None:
        rendered_text = self.font.render(text, True, color, background)
        rect = rendered_text.get_rect()
        rect.center = position
        self.screen.blit(rendered_text, rect)
