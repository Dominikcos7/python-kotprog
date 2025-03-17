from pygame import Surface

from src.Player import Player
from src.renderers.PlayerRenderer import PlayerRenderer
from src.renderers.TextRenderer import TextRenderer


class PlayerInfoRenderer(TextRenderer):
    player_id_to_position_map = {
        0: (PlayerRenderer.id_to_position_map[0][0], PlayerRenderer.id_to_position_map[0][1] - 35),
        1: (PlayerRenderer.id_to_position_map[1][0], PlayerRenderer.id_to_position_map[1][1] - 35),
        2: (PlayerRenderer.id_to_position_map[2][0], PlayerRenderer.id_to_position_map[2][1] - 35),
        3: (PlayerRenderer.id_to_position_map[3][0], PlayerRenderer.id_to_position_map[3][1] - 35),
        4: (PlayerRenderer.id_to_position_map[4][0], PlayerRenderer.id_to_position_map[4][1] + 100),
        5: (PlayerRenderer.id_to_position_map[5][0], PlayerRenderer.id_to_position_map[5][1] + 100),
        6: (PlayerRenderer.id_to_position_map[6][0], PlayerRenderer.id_to_position_map[6][1] + 100),
        7: (PlayerRenderer.id_to_position_map[7][0], PlayerRenderer.id_to_position_map[7][1] + 100),
    }
    y_offset = 14

    def __init__(self, screen: Surface):
        super().__init__(screen)

    def pad_strings(self, strings: list[str]) -> list[str]:
        padded_strs = []
        max_len = max([len(string) for string in strings])

        for string in strings:
            diff = max_len - len(string) + 4
            padded_strs.append((' ' * (diff // 2)) + string + (' ' * (diff // 2 + diff % 2)))

        return padded_strs

    def render_player_info(self, player: Player, table_position: str) -> None:
        chips_txt = 'chips: ' + str(player.chips)

        texts = [table_position, player.name, chips_txt, player.last_action]
        self.render_texts(texts, player)

    def render_texts(self, texts: list[str], player: Player) -> None:
        texts = self.pad_strings(texts)

        position = self.player_id_to_position_map[player.id]
        for i, text in enumerate(texts):
            self.render_text(text, (position[0], position[1] + self.y_offset * i))
