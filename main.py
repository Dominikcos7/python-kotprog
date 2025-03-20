import pygame

from src.HumanPlayer import HumanPlayer
from src.renderers.CardRenderer import CardRenderer
from src.renderers.ChipRenderer import ChipRenderer
from src.Player import Player
from src.renderers.PlayerInfoRenderer import PlayerInfoRenderer
from src.renderers.PlayerRenderer import PlayerRenderer
from src.Table import Table
from src.renderers.RaiseInfoRenderer import RaiseInfoRenderer
from src.renderers.TableRenderer import TableRenderer
from src.enums.TableState import TableState


def handle_input(e: pygame.event.Event) -> bool:
    if e.type != pygame.KEYDOWN:
        return False

    if acting_player.is_raising:
        match e.key:
            case c if c in numerical_keys:
                acting_player.raise_amount_str += str(int(c) - 48)
                return False

            case pygame.K_BACKSPACE:
                acting_player.raise_amount_str = acting_player.raise_amount_str[:-1] if len(acting_player.raise_amount_str) > 0 else ''
                return False

            case pygame.K_RETURN:
                call_amount = table.get_highest_bid()
                acting_player.action_raise(call_amount)
                return True

            case pygame.K_ESCAPE:
                acting_player.is_raising = False
                acting_player.raise_amount_str = ''
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

            case pygame.K_r:
                acting_player.start_raise()
                return False

    return False


def render():
    screen.blit(background, (0, 0))
    table_renderer.render_table()
    chip_renderer.render_pot(table.pot)
    card_renderer.render_table_cards(table.community_cards)

    for player in table.players:
        player_renderer.render_player(player.id)
        chip_renderer.render_player_chips(player.id, player.chips_on_table)

    for player in table.get_not_folded_players():
        cards = [player.hand.cards[0], player.hand.cards[1]]
        card_renderer.render_players_cards(player.id, cards)

    for idx, player in enumerate(table.players):
        match idx:
            case 0:
                table_position = 'SB'
            case 1:
                table_position = 'BB'
            case c if c == len(table.players) - 1:
                table_position = 'D'
            case _:
                table_position = ''

        player_info_renderer.render_player_info(player, table_position)

    if acting_player.is_raising:
        txt = 'Raising: ' + acting_player.raise_amount_str
        position = (720, 20)
        raise_info_renderer.render_text(txt, position, background=None)


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

numerical_keys = [
    pygame.K_0,
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
    pygame.K_7,
    pygame.K_8,
    pygame.K_9,
]

table_renderer = TableRenderer(screen)
player_renderer = PlayerRenderer(screen)
chip_renderer = ChipRenderer(screen)
card_renderer = CardRenderer(screen)
player_info_renderer = PlayerInfoRenderer(screen)
raise_info_renderer = RaiseInfoRenderer(screen)

background = pygame.image.load('./src/img/background.jpg')

players = []
for i in range(8):
    players.append(HumanPlayer("player" + str(i), 100, i))

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
            if isinstance(acting_player, HumanPlayer) and handle_input(event):
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
