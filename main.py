import pygame
from pygame.locals import *


def handle_input(e: pygame.event.Event):
    pass
    # match e.type:



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

    # render
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
