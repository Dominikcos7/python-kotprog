from random import randint

import pygame
from pygame.locals import *

from src.CardRenderer import CardRenderer
from src.ChipRenderer import ChipRenderer
from src.Deck import Deck
from src.PlayerRenderer import PlayerRenderer
from src.TableRenderer import TableRenderer


def handle_input(e: pygame.event.Event):
    pass


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
