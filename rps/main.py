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

    while game.is_game_running:
        print(p1.name + ' make your move:')
        game.p1_move = input()

        print(p2.name + ' make your move:')
        game.p2_move = input()

        print(p1.name + ' played ' + game.p1_move + ' and ' + p2.name + ' played ' + game.p2_move)

        print('Continue playing (y/n)?')
        should_continue = str(input()).lower()
        if should_continue == 'n':
            game.end_game()


if __name__ == '__main__':
    start_game()
