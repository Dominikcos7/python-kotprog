from pygame import Surface

from src.renderers.InfoRenderer import InfoRenderer


class RaiseInfoRenderer(InfoRenderer):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def render_raise_info(self, amount: int) -> None:
        text = f"Raising: {amount}"
        self.render_info(text)
