from pygame import Surface

from src.Player import Player
from src.renderers.PlayerRenderer import PlayerRenderer
from src.renderers.TextRenderer import TextRenderer


class PlayerInfoRenderer(TextRenderer):
    player_id_to_position_map = {
        0: (PlayerRenderer.id_to_position_map[0][0], PlayerRenderer.id_to_position_map[0][1]),
        1: (PlayerRenderer.id_to_position_map[1][0], PlayerRenderer.id_to_position_map[1][1]),
        2: (PlayerRenderer.id_to_position_map[2][0], PlayerRenderer.id_to_position_map[2][1]),
        3: (PlayerRenderer.id_to_position_map[3][0], PlayerRenderer.id_to_position_map[3][1]),
        4: (PlayerRenderer.id_to_position_map[4][0], PlayerRenderer.id_to_position_map[4][1] + 100),
        5: (PlayerRenderer.id_to_position_map[5][0], PlayerRenderer.id_to_position_map[5][1] + 100),
        6: (PlayerRenderer.id_to_position_map[6][0], PlayerRenderer.id_to_position_map[6][1] + 100),
        7: (PlayerRenderer.id_to_position_map[7][0], PlayerRenderer.id_to_position_map[7][1] + 100),
    }

    def __init__(self, screen: Surface):
        super().__init__(screen)

    def render_player_info(self, player: Player):
        chips_txt = '  chips: ' + str(player.chips) + '  '
        last_action = '  ' + player.last_action + '  '
        position = self.player_id_to_position_map[player.id]
        y_offset = 14
        background = (60, 60, 60, 0.25)

        self.render_text(chips_txt, position, background=background)
        self.render_text(last_action, (position[0], position[1] + y_offset), background=background)
