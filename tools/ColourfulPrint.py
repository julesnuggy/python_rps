from colorama import init, Back, Fore, Style


class ColourfulPrint:

    def __init__(self):
        init(autoreset=True)

    @staticmethod
    def format_fore_blue(text):
        return Fore.CYAN + Style.BRIGHT + text

    @staticmethod
    def format_fore_red(text):
        return Fore.RED + Style.BRIGHT + text

    @staticmethod
    def format_fore_white(text):
        return Fore.WHITE + Style.BRIGHT + text

    @staticmethod
    def format_back_yellow(text):
        return Back.YELLOW + Style.BRIGHT + text

    @staticmethod
    def format_back_white(text):
        return Back.WHITE + Fore.BLACK + Style.DIM + text

    @staticmethod
    def format_back_magenta(text):
        return Back.MAGENTA + Style.BRIGHT + text

    @staticmethod
    def print_back_blue(text):
        print(Back.BLUE + Style.BRIGHT + text)

    @staticmethod
    def print_back_red(text):
        print(Back.RED + Style.BRIGHT + text)

    @staticmethod
    def print_back_green(text):
        print(Back.GREEN + Fore.WHITE + Style.BRIGHT + text)
