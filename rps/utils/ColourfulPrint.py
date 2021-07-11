from colorama import init, Back, Fore, Style


class ColourfulPrint:

    def __init__(self):
        init(autoreset=True)

    @staticmethod
    def format_p1_name(text):
        return Fore.CYAN + Style.BRIGHT + text

    @staticmethod
    def format_p2_name(text):
        return Fore.RED + Style.BRIGHT + text

    @staticmethod
    def format_standard_text(text):
        return Fore.WHITE + Style.BRIGHT + text

    @staticmethod
    def format_move_rock(text):
        return Back.GREEN + Fore.YELLOW + text

    @staticmethod
    def format_move_paper(text):
        return Back.WHITE + Fore.BLACK + Style.DIM + text

    @staticmethod
    def format_move_scissors(text):
        return Back.MAGENTA + Style.BRIGHT + text

    @staticmethod
    def print_draw(text):
        print(Back.YELLOW + Fore.BLACK + text)

    @staticmethod
    def print_p1_wins(text):
        print(Back.BLUE + Style.BRIGHT + text)

    @staticmethod
    def print_p2_wins(text):
        print(Back.RED + Style.BRIGHT + text)

    @staticmethod
    def print_game_text(text):
        print(Back.GREEN + Fore.WHITE + Style.BRIGHT + text)

    @staticmethod
    def print_warning(text):
        print(Back.WHITE + Fore.RED + text)
