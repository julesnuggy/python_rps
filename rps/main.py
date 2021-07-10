import string

from rps.Player import Player


def start_game() -> string:
    game_is_running = True

    print('Welcome to Rock Paper Scissors!')

    print('Player 1, what is your name?')
    p1_name = str(input())
    p1 = Player(p1_name)

    print('Player 2, what is your name?')
    p2_name = str(input())
    p2 = Player(p2_name)

    print(p1.name + ' is playing against ' + p2.name)

    while game_is_running:
        print(p1.name + '\'s score is ' + p1.score.__str__())
        print(p2.name + '\'s score is ' + p2.score.__str__())
        p1.add_to_score()
        p1.add_to_score()
        print(p1.name + '\'s score is ' + p1.score.__str__())
        print(p2.name + '\'s score is ' + p2.score.__str__())

        print('Continue playing (y/n)?')
        should_continue = str(input())
        if should_continue == 'n':
            game_is_running = False


if __name__ == '__main__':
    start_game()
