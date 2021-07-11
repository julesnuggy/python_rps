from Enums import MoveEnum, ResultEnum
from rps.utils.ConsoleInputHelper import print_game_end_results
from utils.ColourfulPrint import ColourfulPrint


class Game:
    is_game_running = True
    round = 1
    p1_move = ''
    p2_move = ''
    result = ResultEnum.NONE
    cp = ColourfulPrint()

    def end_game(self):
        self.is_game_running = False

    def increment_round(self):
        self.round += 1

    def set_p1_move(self, move):
        if not(self.is_valid_input(move)):
            self.cp.print_warning('Not a valid move!')
            return

        self.p1_move = MoveEnum(int(move))

    def set_p2_move(self, move):
        if not(self.is_valid_input(move)):
            self.cp.print_warning('Not a valid move!')
            return

        self.p2_move = MoveEnum(int(move))

    def set_result(self, result: ResultEnum):
        self.result = result

    def get_move_formatting(self, move):
        if move == MoveEnum.ROCK:
            return self.cp.format_move_rock(MoveEnum.ROCK.name)
        elif move == MoveEnum.PAPER:
            return self.cp.format_move_paper(MoveEnum.PAPER.name)
        elif move == MoveEnum.SCISSORS:
            return self.cp.format_move_scissors(MoveEnum.SCISSORS.name)

    def calculate_round_result(self):
        if self.p1_move == self.p2_move:
            self.set_result(ResultEnum.DRAW)
            return

        if self.p1_move == MoveEnum.ROCK:
            if self.p2_move == MoveEnum.SCISSORS:
                self.set_result(ResultEnum.P1)
            else:
                self.set_result(ResultEnum.P2)
            return

        if self.p1_move == MoveEnum.PAPER:
            if self.p2_move == MoveEnum.ROCK:
                self.set_result(ResultEnum.P1)
            else:
                self.set_result(ResultEnum.P2)
            return

        if self.p1_move == MoveEnum.SCISSORS:
            if self.p2_move == MoveEnum.PAPER:
                self.set_result(ResultEnum.P1)
            else:
                self.set_result(ResultEnum.P2)
            return

    def reset_result_state(self):
        self.p1_move = ''
        self.p2_move = ''
        self.result = ResultEnum.NONE

    def handle_game_end(self, p1, p2):
        print_game_end_results(p1, p2)
        self.end_game()
        exit()

    @staticmethod
    def is_valid_input(user_input):
        valid_inputs = set(str(move.value) for move in MoveEnum)
        return user_input in valid_inputs

    @staticmethod
    def is_valid_move(user_move):
        valid_moves = set(move for move in MoveEnum)
        return user_move in valid_moves

    @staticmethod
    def print_instructions():
        print("""\
------------------------------------
|     OPTIONS      ||     MOVES    |
------------------------------------
| i = Instructions || 1 = ROCK     |
| s = Scoreboard   || 2 = PAPER    |
| q = Quit game    || 3 = SCISSORS |
------------------------------------
        """)
