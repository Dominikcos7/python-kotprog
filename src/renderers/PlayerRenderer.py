import pygame
from pygame import Surface

from src.renderers.Renderer import Renderer
from src.renderers.TableRenderer import TableRenderer
from src.resource_path import get_resource_path


class PlayerRenderer(Renderer):
    """
    This class is responsible for rendering players on the screen.
    """

    SCALE = 0.3
    table_x, table_y = TableRenderer.DEFAULT_POSITION
    id_to_picture_map = {
        0: get_resource_path('img/players/A_BMO.png'),
        1: get_resource_path('img/players/A_Finn.png'),
        2: get_resource_path('img/players/A_Flame_Princess.png'),
        3: get_resource_path('img/players/A_Gunter.png'),
        4: get_resource_path('img/players/A_Ice_King.png'),
        5: get_resource_path('img/players/A_Jake.png'),
        6: get_resource_path('img/players/A_Lady_Rainicorn.png'),
        7: get_resource_path('img/players/A_Lemongrab.png'),
        8: get_resource_path('img/players/A_Lumpy_Space_Princess.png'),
        9: get_resource_path('img/players/A_Marceline.png'),
        10: get_resource_path('img/players/A_Pepperment_Butler.png'),
        11: get_resource_path('img/players/A_Princess_Bubblegum.png'),
        12: get_resource_path('img/players/A_Slime_Princess.png'),
        13: get_resource_path('img/players/A_TreeTrunks.png'),
    }
    id_to_position_map = {
        0: (table_x - 30, table_y),
        1: (table_x + 170, table_y - 50),
        2: (table_x + 400, table_y - 50),
        3: (table_x + 600, table_y),
        4: (table_x + 600, table_y + 200),
        5: (table_x + 400, table_y + 280),
        6: (table_x + 170, table_y + 280),
        7: (table_x - 30, table_y + 200),
    }

    def __init__(self, screen: Surface):
        """
        :param screen: the pygame Surface to render the info on
        """
        super().__init__(screen)

    def render_player(self, player_id: int) -> None:
        """
        :param player_id: the id of the player to be rendered
        """

        image = pygame.image.load(self.id_to_picture_map[player_id])
        w, h = image.get_size()
        image = pygame.transform.scale(image, (w * self.SCALE, h * self.SCALE))

        position = self.id_to_position_map[player_id]
        self.screen.blit(image, position)
