from pygame import Surface

from src.renderers.InfoRenderer import InfoRenderer


class RaiseInfoRenderer(InfoRenderer):
    """
    This class is responsible for rendering the raise information on the screen.
    """

    def __init__(self, screen: Surface):
        """
        :param screen: the pygame Surface to render the info on
        """

        super().__init__(screen)

    def render_raise_info(self, amount: int) -> None:
        """
        :param amount: the amount the player intends to raise
        """

        text = f"Raising: {amount}"
        self.render_info(text)
