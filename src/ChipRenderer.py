import pygame
from pygame import Surface

from src.Renderer import Renderer


class ChipRenderer(Renderer):
    SCALE = 0.5

    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.sprite = pygame.image.load('./src/img/chips.png')
        w, h = self.sprite.get_size()[0] * self.SCALE, self.sprite.get_size()[1] * self.SCALE
        self.sprite = pygame.transform.scale(self.sprite, (w, h))
        self.chip_width_px = 46 * self.SCALE
        self.chip_height_px = 48 * self.SCALE
        self.chip_values = [200, 100, 50, 20, 10, 5, 2, 1]
        self.row_number_by_value_map = {
            1: 0,
            2: 0,
            5: 1,
            10: 1,
            20: 2,
            50: 2,
            100: 3,
            200: 3,
        }
        self.col_number_by_value_map = {
            1: 0,
            2: 4,
            5: 0,
            10: 4,
            20: 0,
            50: 4,
            100: 0,
            200: 4,
        }

    def get_col_offset_by_count(self, count: int) -> int:
        match count:
            case 2:
                return 1
            case c if 2 < c < 7:
                return 2
            case c if c >= 7:
                return 3
            case _:
                return 0

    def render_chips(self, amount: int, position: tuple[float, float]) -> None:
        if amount < 1:
            raise ValueError("ChipRenderer cannot render less than one chip.")

        result = {}
        for chip_value in self.chip_values:
            count = amount // chip_value
            if count > 0:
                result[chip_value] = count
                amount -= count * chip_value

        offset = 0
        for chip_value, count in result.items():
            col_offset = self.get_col_offset_by_count(count)
            col = self.col_number_by_value_map[chip_value] + col_offset
            row = self.row_number_by_value_map[chip_value]
            chips = self.sprite.subsurface(pygame.Rect(col * self.chip_width_px, row * self.chip_height_px, self.chip_width_px, self.chip_height_px))
            self.screen.blit(chips, (position[0] + offset * self.chip_width_px, position[1]))
            offset += 1
