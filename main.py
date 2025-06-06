import time

import pygame

from src.EvalPlayer import EvalPlayer
from src.HumanPlayer import HumanPlayer
from src.renderers.CardRenderer import CardRenderer
from src.renderers.ChipRenderer import ChipRenderer
from src.renderers.InfoRenderer import InfoRenderer
from src.renderers.PlayerInfoRenderer import PlayerInfoRenderer
from src.renderers.PlayerRenderer import PlayerRenderer
from src.Table import Table
from src.renderers.RaiseInfoRenderer import RaiseInfoRenderer
from src.renderers.RoundWinnerInfoRenderer import RoundWinnerInfoRenderer
from src.renderers.TableRenderer import TableRenderer
from src.enums.TableState import TableState
from src.resource_path import get_resource_path

"""
This is the main file of the game. The main game loop looks like this:
1. Request the events from the game and handle them accordingly. Events can be the input of the player or an exit event.
2. Update game state according to the event being handled
3. Render the view based on the current state of the game (the logic is separated from game state updates)
"""


def handle_input(e: pygame.event.Event) -> bool:
    if e.type != pygame.KEYDOWN:
        return False

    try:
        if acting_player.is_raising:
            match e.key:
                case c if c in numerical_keys:
                    acting_player.raise_amount_str += str(int(c) - 48)
                    return False

                case pygame.K_BACKSPACE:
                    acting_player.raise_amount_str = acting_player.raise_amount_str[:-1] if len(
                        acting_player.raise_amount_str) > 0 else ''
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
                    bid = table.get_highest_bid()
                    amount = acting_player.get_amount_to_call(bid)
                    acting_player.action_call(amount)
                    return True

                case pygame.K_f:
                    acting_player.action_fold()
                    return True

                case pygame.K_p:
                    bid = table.get_highest_bid()
                    acting_player.action_check(bid)
                    return True

                case pygame.K_r:
                    acting_player.start_raise()
                    return False
    except Exception as e:
        print(e)
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
        show_cards = isinstance(player, HumanPlayer) or table.state == TableState.CLOSE_ROUND
        card_renderer.render_players_cards(player.id, cards, show_cards)

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
        raise_info_renderer.render_raise_info(acting_player.raise_amount_str)
    elif isinstance(acting_player, HumanPlayer) and not acting_player.is_folded() and not acting_player.is_all_in:
        info_renderer.render_info('YOUR TURN!')

    if table.round_winner is not None:
        round_winner_info_renderer.render_round_winner_info(table.round_winner, table.pot, table.community_cards)


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
round_winner_info_renderer = RoundWinnerInfoRenderer(screen)
info_renderer = InfoRenderer(screen)

background = pygame.image.load(get_resource_path('img/background.jpg'))

players = [HumanPlayer("player", 100, 0)]
for i in range(1, 8):
    players.append(EvalPlayer("aiplayer" + str(i), 100, i))

table = Table(players, 2)

running = True
while running:
    if table.state == TableState.INIT_ROUND or table.state == TableState.CLOSE_ROUND:
        table.enter_next_state()

    acting_player = table.get_acting_player()

    if acting_player.is_all_in or acting_player.is_folded():
        acting_player.acted = True
        try:
            table.enter_next_state()
        except ValueError as ex:
            print(ex)
            table.bump_actor_idx()
    elif isinstance(acting_player, HumanPlayer):
        # handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if handle_input(event):
                try:
                    table.enter_next_state()
                except ValueError as ex:
                    print(ex)
                    table.bump_actor_idx()
    else:
        highest_bid = table.get_highest_bid()
        time.sleep(1)
        acting_player.act(highest_bid)
        try:
            table.enter_next_state()
        except ValueError as ex:
            print(ex)
            table.bump_actor_idx()

    # render
    render()
    pygame.display.flip()

    if table.state == TableState.CLOSE_ROUND:
        time.sleep(5)

    clock.tick(60)

pygame.quit()
