from abc import ABC

from pygame import Surface


class Renderer(ABC):
    """
    This class is an abstract base class for all renderers.
    """

    def __init__(self, screen: Surface):
        """
        :param screen: the pygame Surface to render the info on
        """

        self.screen = screen
