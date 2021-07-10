import string

from rps.Player import Player


def play_game(player_1_name, player_2_name) -> string:
    p1 = Player(player_1_name)
    p2 = Player(player_2_name)
    print(p1.name + ' is playing against ' + p2.name)
    print(p1.name + '\'s score is ' + p1.score.__str__())
    print(p2.name + '\'s score is ' + p2.score.__str__())
    p1.add_to_score()
    p1.add_to_score()
    print(p1.name + '\'s score is ' + p1.score.__str__())
    print(p2.name + '\'s score is ' + p2.score.__str__())


if __name__ == '__main__':
    play_game('Jules', 'Lee')
