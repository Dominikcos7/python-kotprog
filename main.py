from random import randint

import pygame
from pygame.locals import *

from src.CardRenderer import CardRenderer
from src.ChipRenderer import ChipRenderer
from src.Deck import Deck
from src.Player import Player
from src.PlayerRenderer import PlayerRenderer
from src.Table import Table
from src.TableRenderer import TableRenderer
from src.enums.TableState import TableState


def handle_input(e: pygame.event.Event):
    if e.type == pygame.KEYDOWN:
        player = table.get_acting_player()
        if player.is_human:
            match e.key:
                case pygame.K_c:
                    bid = table.get_highest_bid()
                    amount = bid - player.chips_on_table
                    player.action_call(amount)

                    try:
                        table.enter_next_state()
                    except ValueError as ex:
                        print(ex)
                        table.bump_actor_idx()




def render_sprites():
    table_renderer.render_table()
    chip_renderer.render_pot(table.pot)
    card_renderer.render_table_cards(table.community_cards)

    for player in players:
        player_renderer.render_player(player.id)
        chip_renderer.render_player_chips(player.id, player.chips_on_table)

    for player in table.get_not_folded_players():
        cards = [player.hand.cards[0], player.hand.cards[1]]
        card_renderer.render_players_cards(player.id, cards)


def update():
    pass


#####################################
# Game loop should look like this:  #
# handleInput()                     #
# updateStates()                    #
# render()                          #
#####################################


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 30)

table_renderer = TableRenderer(screen)
player_renderer = PlayerRenderer(screen)
chip_renderer = ChipRenderer(screen)
card_renderer = CardRenderer(screen)

players = []
for i in range(5):
    players.append(Player("player" + str(i), 100, i, True))

table = Table(players, 2)
table.enter_state(TableState.PRE_FLOP)

running = True
while running:
    # handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        handle_input(event)

    # update
    update()

    # render
    render_sprites()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
