import sys
import time
from random import randint

from Player import Player
from Game import Game
from Enums import ResultEnum
from utils.ColourfulPrint import ColourfulPrint
from utils.ConsoleInputHelper import get_hidden_user_input, print_scoreboard


cp = ColourfulPrint()


def start_game():
    game = Game()
    is_p2_cpu = None

    cp.print_game_text('      ROCK! PAPER! SCISSORS!      ')

    while not (is_p2_cpu in {True, False}):
        print('Are 1 or 2 humans playing?')
        user_input = input()
        if user_input == '1':
            is_p2_cpu = True
        elif user_input == '2':
            is_p2_cpu = False
        else:
            is_p2_cpu = None

    print('Player 1, what is your name?')
    p1 = Player(str(input()), True, False)

    if is_p2_cpu:
        print('Player 2, JANKENPON, has entered the arena')
        p2 = Player('JANKENPON', False, True)
    else:
        print('Player 2, what is your name?')
        p2 = Player(str(input()), False, False)

    print('')
    game.print_instructions()
    print(f'{cp.format_p1_name(p1.name)} {cp.format_standard_text("VS")} {cp.format_p2_name(p2.name)}')

    while game.is_game_running:
        print('')
        cp.print_game_text(f'               ROUND {game.round} --- FIGHT!               ')
        print('')

        while not (game.is_valid_move(game.p1_move)):
            p1_input = get_hidden_user_input(p1)

            if p1_input.lower().strip() == 'i':
                game.print_instructions()
            elif p1_input.lower().strip() == 's':
                print_scoreboard(p1, p2)
            elif p1_input.lower().strip() == 'q':
                game.handle_game_end(p1, p2)
            else:
                game.set_p1_move(p1_input)

        if p2.is_cpu_player:
            game.set_p2_move(str(randint(1, 3)))
            print(f'{p2.name} has made their move!')
        else:
            while not (game.is_valid_move(game.p2_move)):
                p2_input = get_hidden_user_input(p2)
                game.set_p2_move(p2_input)

        print('')
        print(f'{cp.format_p1_name(p1.name)} {cp.format_standard_text("played")} {game.get_move_formatting(game.p1_move)}')
        print(f'{cp.format_p2_name(p2.name)} {cp.format_standard_text("played")} {game.get_move_formatting(game.p2_move)}')
        game.calculate_round_result()

        if game.result == ResultEnum.DRAW:
            cp.print_draw('It\'s a draw!')
        elif game.result == ResultEnum.P1:
            p1.add_to_score()
            cp.print_p1_wins(f'{p1.name} wins!')
        else:
            p2.add_to_score()
            cp.print_p2_wins(f'{p2.name} wins!')

        game.increment_round()
        game.reset_result_state()

        sys.stdout.write('Next round starting in: ')
        for i in range(3, 0, -1):
            sys.stdout.write(str(i) + '... ')
            sys.stdout.flush()
            time.sleep(1)


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


if __name__ == '__main__':
    start_game()
