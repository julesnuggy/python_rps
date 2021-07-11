import getpass
import sys


def get_hidden_user_input(player_name: str):
    if sys.stdin.isatty():
        return getpass.getpass(prompt=f'{player_name} make your move:')
    else:
        print(f'{player_name} make your move:')
        return sys.stdin.readline().rstrip()

def print_scoreboard(p1, p2):
    score_text = f'| {p1.name}\'s Score: {str(p1.score)} || {p2.name}\'s Score: {str(p2.score)} |'
    print('-' * len(score_text))
    print(score_text)
    print('-' * len(score_text))
