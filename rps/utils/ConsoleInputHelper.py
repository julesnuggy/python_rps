import getpass
import sys

from rps.Player import Player
from rps.utils.ColourfulPrint import ColourfulPrint


cp = ColourfulPrint()


def get_hidden_user_input(player: Player):
    if player.is_p1:
        formatted_player_name = cp.format_p1_name(player.name)
    else:
        formatted_player_name = cp.format_p2_name(player.name)

    print(f'{formatted_player_name} {cp.format_standard_text("make your move")}:')

    if sys.stdin.isatty():
        return getpass.getpass(prompt='')
    else:
        return sys.stdin.readline().rstrip()


def print_scoreboard(p1: Player, p2: Player):
    score_text = f'| {p1.name}\'s Score: {str(p1.score)} || {p2.name}\'s Score: {str(p2.score)} |'
    print('-' * len(score_text))
    print(score_text)
    print('-' * len(score_text))


def print_game_end_results(p1: Player, p2: Player):
    print('')
    cp.print_game_text('            GAME OVER!            ')
    print_scoreboard(p1, p2)
    print('')
    if p1.score > p2.score:
        cp.print_p1_wins(f'{p1.name} wins!')
    elif p2.score > p1.score:
        cp.print_p2_wins(f'{p2.name} wins!')
    else:
        cp.print_draw('It\'s a draw!')
