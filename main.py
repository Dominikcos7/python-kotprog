import pygame

from src.renderers.CardRenderer import CardRenderer
from src.renderers.ChipRenderer import ChipRenderer
from src.Player import Player
from src.renderers.PlayerInfoRenderer import PlayerInfoRenderer
from src.renderers.PlayerRenderer import PlayerRenderer
from src.Table import Table
from src.renderers.TableRenderer import TableRenderer
from src.enums.TableState import TableState


def handle_input(e: pygame.event.Event) -> bool:
    if e.type != pygame.KEYDOWN:
        return False
    else:
        match e.key:
            case pygame.K_c:
                try:
                    bid = table.get_highest_bid()
                    amount = bid - acting_player.chips_on_table
                    acting_player.action_call(amount)
                    return True
                except ValueError as ex:
                    print(ex)
                    return False

            case pygame.K_f:
                acting_player.action_fold()
                return True

            case pygame.K_p:
                try:
                    bid = table.get_highest_bid()
                    acting_player.action_check(bid)
                    return True
                except ValueError as ex:
                    print(ex)
                    return False

            case _:
                return False


def render():
    screen.blit(background, (0, 0))
    table_renderer.render_table()
    chip_renderer.render_pot(table.pot)
    card_renderer.render_table_cards(table.community_cards)

    for player in players:
        player_renderer.render_player(player.id)
        chip_renderer.render_player_chips(player.id, player.chips_on_table)

    for player in table.get_not_folded_players():
        cards = [player.hand.cards[0], player.hand.cards[1]]
        card_renderer.render_players_cards(player.id, cards)

    for player in players:
        player_info_renderer.render_player_info(player)


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

table_renderer = TableRenderer(screen)
player_renderer = PlayerRenderer(screen)
chip_renderer = ChipRenderer(screen)
card_renderer = CardRenderer(screen)
player_info_renderer = PlayerInfoRenderer(screen)

background = pygame.image.load('./src/img/background.jpg')

players = []
for i in range(8):
    players.append(Player("player" + str(i), 100, i, True))

table = Table(players, 2)

running = True
while running:
    # handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if table.state == TableState.INIT_ROUND or table.state == TableState.CLOSE_ROUND:
            table.enter_next_state()
        else:
            acting_player = table.get_acting_player()
            if acting_player.is_human and handle_input(event):
                try:
                    table.enter_next_state()
                except ValueError as ex:
                    print(ex)
                    table.bump_actor_idx()

    # update
    update()

    # render
    render()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
