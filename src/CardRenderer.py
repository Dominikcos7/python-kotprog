import pygame
from pygame import Surface

from src.Card import Card
from src.Renderer import Renderer
from src.enums.Rank import Rank
from src.enums.Suit import Suit


class CardRenderer(Renderer):
    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.sprite = pygame.image.load('./src/img/cards.png')
        self.card_width_px = 48
        self.card_height_px = 64
        self.row_number_by_suit_map = {
            Suit.HEART: 0,
            Suit.DIAMOND: 1,
            Suit.SPADE: 2,
            Suit.CLUB: 3,
        }
        self.col_number_by_rank_map = {
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

    def render_card(self, card: Card, position: tuple[float, float]) -> None:
        col = self.col_number_by_rank_map[card.rank]
        row = self.row_number_by_suit_map[card.suit]
        card = self.sprite.subsurface(pygame.Rect(col * self.card_width_px, row * self.card_height_px, self.card_width_px, self.card_height_px))
        self.screen.blit(card, position)
