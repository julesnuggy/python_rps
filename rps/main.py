from Player import Player
from Game import Game


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
            print(p1.name + ' make your move:')
            game.set_p1_move(input())

        while not (game.is_valid_move(game.p2_move)):
            print(p2.name + ' make your move:')
            game.set_p2_move(input())

        print(p1.name + ' played ' + game.p1_move + ' and ' + p2.name + ' played ' + game.p2_move)

        print('Continue playing (y/n)?')
        if str(input()).lower().strip() == 'n':
            game.end_game()


if __name__ == '__main__':
    start_game()
