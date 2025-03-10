from abc import ABC

from pygame import Surface


class Renderer(ABC):
    def __init__(self, screen: Surface):
        self.screen = screen
