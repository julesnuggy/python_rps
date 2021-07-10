from Player import Player
from Game import Game


def start_game():
    game = Game()

    print('Welcome to Rock Paper Scissors!')

    print('Player 1, what is your name?')
    p1_name = str(input())
    p1 = Player(p1_name)

    print('Player 2, what is your name?')
    p2_name = str(input())
    p2 = Player(p2_name)

    print(p1.name + ' VS ' + p2.name)
    print('FIGHT!')
    print_instructions()

    while game.is_game_running:
        print(p1.name + ' make your move:')
        p1_input = input()

        while not(game.is_valid_move(p1_input)):
            print('Not a valid move!')
            print_instructions()
            print(p1.name + ' make your move:')
            p1_input = input()

        game.set_p1_move(int(p1_input))

        print(p2.name + ' make your move:')
        p2_input = input()

        while not(game.is_valid_move(p2_input)):
            print('Not a valid move!')
            print_instructions()
            print(p2.name + ' make your move:')
            p2_input = input()

        game.set_p2_move(int(p2_input))

        print(p1.name + ' played ' + game.p1_move + ' and ' + p2.name + ' played ' + game.p2_move)

        print('Continue playing (y/n)?')
        should_continue = str(input()).lower().strip()
        if should_continue == 'n':
            game.end_game()


def print_instructions():
    print("""\
-----------------------------------------
| ROCK = 1 || PAPER = 2 || SCISSORS = 3 |
-----------------------------------------
    """)


if __name__ == '__main__':
    start_game()
