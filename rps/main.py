import getpass
import sys

from Player import Player
from Game import Game
from Enums import ResultEnum


def start_game():
    game = Game()

    print('Welcome to Rock Paper Scissors!')

    print('Player 1, what is your name?')
    p1 = Player(str(input()))

    print('Player 2, what is your name?')
    p2 = Player(str(input()))

    print(p1.name + ' VS ' + p2.name)
    print('FIGHT!')
    game.print_instructions()

    while game.is_game_running:

        while not (game.is_valid_move(game.p1_move)):
            p1_input = get_hidden_user_input(p1.name)
            game.set_p1_move(p1_input)

        while not (game.is_valid_move(game.p2_move)):
            p2_input = get_hidden_user_input(p2.name)
            game.set_p2_move(p2_input)

        print(f'{p1.name} played {game.p1_move.name} and {p2.name} played {game.p2_move.name}')
        game.get_game_result()

        if game.result == ResultEnum.DRAW:
            print('It\'s a draw!')
        elif game.result == ResultEnum.P1:
            p1.add_to_score()
            print(f'{p1.name} wins!')
        else:
            p2.add_to_score()
            print(f'{p2.name} wins!')

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
        score_text = f'| {p1.name}\'s Score: {str(p1.score)} || {p2.name}\'s Score: {str(p2.score)} |'
        print('-' * len(score_text))
        print(score_text)
        print('-' * len(score_text))
        game_next_steps(p1, p2, game)
    elif user_input == 'p':
        game.reset_result_state()
        return
    elif user_input == 'q':
        game.end_game()
        return
    else:
        print('Invalid option')
        game_next_steps(p1, p2, game)


if __name__ == '__main__':
    start_game()
