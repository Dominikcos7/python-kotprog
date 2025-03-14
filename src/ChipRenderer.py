import pygame
from pygame import Surface

from src.PlayerRenderer import PlayerRenderer
from src.Renderer import Renderer
from src.TableRenderer import TableRenderer


class ChipRenderer(Renderer):
    SCALE = 0.5
    row_number_by_value_map = {
        1: 0,
        2: 0,
        5: 1,
        10: 1,
        20: 2,
        50: 2,
        100: 3,
        200: 3,
    }
    col_number_by_value_map = {
        1: 0,
        2: 4,
        5: 0,
        10: 4,
        20: 0,
        50: 4,
        100: 0,
        200: 4,
    }
    player_id_to_position_map = {
        0: (PlayerRenderer.id_to_position_map[0][0] + 150, PlayerRenderer.id_to_position_map[0][1] + 120),
        1: (PlayerRenderer.id_to_position_map[1][0], PlayerRenderer.id_to_position_map[1][1] + 140),
        2: (PlayerRenderer.id_to_position_map[2][0], PlayerRenderer.id_to_position_map[2][1] + 140),
        3: (PlayerRenderer.id_to_position_map[3][0] - 120, PlayerRenderer.id_to_position_map[3][1] + 120),
        4: (PlayerRenderer.id_to_position_map[4][0] - 120, PlayerRenderer.id_to_position_map[4][1] - 40),
        5: (PlayerRenderer.id_to_position_map[5][0], PlayerRenderer.id_to_position_map[5][1] - 60),
        6: (PlayerRenderer.id_to_position_map[6][0], PlayerRenderer.id_to_position_map[6][1] - 60),
        7: (PlayerRenderer.id_to_position_map[7][0] + 150, PlayerRenderer.id_to_position_map[7][1] - 40),
    }

    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.sprite = pygame.image.load('./src/img/chips.png')
        w, h = self.sprite.get_size()[0] * self.SCALE, self.sprite.get_size()[1] * self.SCALE
        self.sprite = pygame.transform.scale(self.sprite, (w, h))
        self.chip_width_px = 46 * self.SCALE
        self.chip_height_px = 48 * self.SCALE
        self.chip_values = [200, 100, 50, 20, 10, 5, 2, 1]

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
            return

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

    def render_player_chips(self, player_id: int, amount: int) -> None:
        position = self.player_id_to_position_map[player_id]
        self.render_chips(amount, position)

    def render_pot(self, amount: int):
        position = (TableRenderer.DEFAULT_POSITION[0] + 300, TableRenderer.DEFAULT_POSITION[1] + 120)
        self.render_chips(amount, position)
