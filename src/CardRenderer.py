import pygame
from pygame import Surface

from src.Card import Card
from src.PlayerRenderer import PlayerRenderer
from src.Renderer import Renderer
from src.TableRenderer import TableRenderer
from src.enums.Rank import Rank
from src.enums.Suit import Suit


class CardRenderer(Renderer):
    h = 64
    w = 48
    x, y = TableRenderer.DEFAULT_POSITION
    row_number_by_suit_map = {
        Suit.HEART: 0,
        Suit.DIAMOND: 1,
        Suit.SPADE: 2,
        Suit.CLUB: 3,
    }
    col_number_by_rank_map = {
        Rank.ACE: 0,
        Rank.TWO: 1,
        Rank.THREE: 2,
        Rank.FOUR: 3,
        Rank.FIVE: 4,
        Rank.SIX: 5,
        Rank.SEVEN: 6,
        Rank.EIGHT: 7,
        Rank.NINE: 8,
        Rank.TEN: 9,
        Rank.JACK: 10,
        Rank.QUEEN: 11,
        Rank.KING: 12,
    }
    player_id_to_position_map = {
        0: (PlayerRenderer.id_to_position_map[0][0] + 50, PlayerRenderer.id_to_position_map[0][1] + 80),
        1: (PlayerRenderer.id_to_position_map[1][0], PlayerRenderer.id_to_position_map[1][1] + 80),
        2: (PlayerRenderer.id_to_position_map[2][0], PlayerRenderer.id_to_position_map[2][1] + 80),
        3: (PlayerRenderer.id_to_position_map[3][0] - 30, PlayerRenderer.id_to_position_map[3][1] + 80),
        4: (PlayerRenderer.id_to_position_map[4][0] - 30, PlayerRenderer.id_to_position_map[4][1] - 30),
        5: (PlayerRenderer.id_to_position_map[5][0], PlayerRenderer.id_to_position_map[5][1] - 30),
        6: (PlayerRenderer.id_to_position_map[6][0], PlayerRenderer.id_to_position_map[6][1] - 30),
        7: (PlayerRenderer.id_to_position_map[7][0] + 50, PlayerRenderer.id_to_position_map[7][1] - 30),
    }

    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.sprite = pygame.image.load('./src/img/cards.png')

    def render_card(self, card: Card, position: tuple[float, float]) -> None:
        col = self.col_number_by_rank_map[card.rank]
        row = self.row_number_by_suit_map[card.suit]
        card = self.sprite.subsurface(pygame.Rect(col * self.w, row * self.h, self.w, self.h))
        self.screen.blit(card, position)

    def render_players_cards(self, player_id: int, cards: list[Card]) -> None:
        offset = 0
        for card in cards:
            x, y = self.player_id_to_position_map[player_id]
            self.render_card(card, (x + offset, y))
            offset += self.w

    def render_table_cards(self, cards: list[Card], card_number: int = 0) -> None:
        x = self.x + 180 + self.w
        y = self.y + 150
        for card in cards:
            self.render_card(card, (x + card_number * self.w, y))
            card_number += 1
