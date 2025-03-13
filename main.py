from random import randint

import pygame
from pygame.locals import *

from src.CardRenderer import CardRenderer
from src.ChipRenderer import ChipRenderer
from src.Deck import Deck
from src.PlayerRenderer import PlayerRenderer
from src.TableRenderer import TableRenderer


def handle_input(e: pygame.event.Event):
    if e.type == pygame.KEYDOWN:
        background = pygame.image.load('./src/img/background.jpg')
        screen.blit(background, (0, 0))

        table_renderer = TableRenderer(screen)
        table_renderer.render_table()

        player_renderer = PlayerRenderer(screen)
        player_renderer.render_player(0)
        player_renderer.render_player(1)
        player_renderer.render_player(2)
        player_renderer.render_player(3)
        player_renderer.render_player(4)
        player_renderer.render_player(5)
        player_renderer.render_player(6)
        player_renderer.render_player(7)

        deck = Deck().shuffle()
        card_renderer = CardRenderer(screen)
        card_renderer.render_players_cards(0, [deck.draw(), deck.draw()])
        card_renderer.render_players_cards(1, [deck.draw(), deck.draw()])
        card_renderer.render_players_cards(2, [deck.draw(), deck.draw()])
        card_renderer.render_players_cards(3, [deck.draw(), deck.draw()])
        card_renderer.render_players_cards(4, [deck.draw(), deck.draw()])
        card_renderer.render_players_cards(5, [deck.draw(), deck.draw()])
        card_renderer.render_players_cards(6, [deck.draw(), deck.draw()])
        card_renderer.render_players_cards(7, [deck.draw(), deck.draw()])

        card_renderer.render_table_cards([deck.draw(), deck.draw(), deck.draw(), deck.draw(), deck.draw()])

        chip_renderer = ChipRenderer(screen)
        for i in range(0, 8):
            amount = randint(1, 1000)
            chip_renderer.render_player_chips(i, amount)

        amount = randint(1, 1000)
        chip_renderer.render_pot(amount)


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
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
