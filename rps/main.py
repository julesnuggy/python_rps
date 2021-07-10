import getpass
import sys

from Player import Player
from Game import Game
from Enums import ResultEnum
from tools.ColourfulPrint import ColourfulPrint


cp = ColourfulPrint()


def start_game():
    game = Game()

    cp.print_game_text('      ROCK! PAPER! SCISSORS!      ')

    print('Player 1, what is your name?')
    p1 = Player(str(input()))

    print('Player 2, what is your name?')
    p2 = Player(str(input()))

    print('')
    print(f'{cp.format_p1_name(p1.name)} {cp.format_standard_text("VS")} {cp.format_p2_name(p2.name)}')
    cp.print_game_text('              FIGHT!              ')
    game.print_instructions()

    while game.is_game_running:

        while not (game.is_valid_move(game.p1_move)):
            p1_input = get_hidden_user_input(p1.name)
            game.set_p1_move(p1_input)

        while not (game.is_valid_move(game.p2_move)):
            p2_input = get_hidden_user_input(p2.name)
            game.set_p2_move(p2_input)

        print('')
        print(f'{cp.format_p1_name(p1.name)} {cp.format_standard_text("played")} {game.get_move_formatting(game.p1_move)}')
        print(f'{cp.format_p2_name(p2.name)} {cp.format_standard_text("played")} {game.get_move_formatting(game.p2_move)}')
        game.get_game_result()

        if game.result == ResultEnum.DRAW:
            cp.print_draw('It\'s a draw!')
        elif game.result == ResultEnum.P1:
            p1.add_to_score()
            cp.print_p1_wins(f'{p1.name} wins!')
        else:
            p2.add_to_score()
            cp.print_p2_wins(f'{p2.name} wins!')

        game_next_steps(p1, p2, game)


def get_hidden_user_input(player_name):
    if sys.stdin.isatty():
        return getpass.getpass(prompt=f'{player_name} make your move:')
    else:
        print(f'{player_name} make your move:')
        return sys.stdin.readline().rstrip()


def game_next_steps(p1, p2, game):
    print("""
What do you want to do next?
s = Scoreboard
p = Play another match
q = Quit game\
    """)

    user_input = input().lower().strip()
    if user_input == 's':
        print_scoreboard(p1, p2)
        game_next_steps(p1, p2, game)
    elif user_input == 'p':
        game.reset_result_state()
        return
    elif user_input == 'q':
        print('')
        cp.print_game_text('            GAME OVER!            ')
        print_scoreboard(p1, p2)
        game.end_game()
        return
    else:
        cp.print_warning('Invalid option')
        game_next_steps(p1, p2, game)


def print_scoreboard(p1, p2):
    score_text = f'| {p1.name}\'s Score: {str(p1.score)} || {p2.name}\'s Score: {str(p2.score)} |'
    print('-' * len(score_text))
    print(score_text)
    print('-' * len(score_text))

if __name__ == '__main__':
    start_game()
