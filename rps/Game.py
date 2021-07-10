from Enums import MoveEnum


class Game:
    is_game_running = True
    p1_move = ''
    p2_move = ''
    winner = ''

    def end_game(self):
        self.is_game_running = False

    def set_p1_move(self, move):
        if not(self.is_valid_input(move)):
            print('Not a valid move!')
            self.print_instructions()
            return

        self.p1_move = MoveEnum(int(move)).name

    def set_p2_move(self, move):
        if not(self.is_valid_input(move)):
            print('Not a valid move!')
            self.print_instructions()
            return

        self.p2_move = MoveEnum(int(move)).name

    def set_winner(self, winner):
        self.winner = winner

    @staticmethod
    def is_valid_input(user_input):
        valid_inputs = set(str(move.value) for move in MoveEnum)
        return user_input in valid_inputs

    @staticmethod
    def is_valid_move(user_move):
        valid_moves = set(move.name for move in MoveEnum)
        return user_move in valid_moves

    @staticmethod
    def print_instructions():
        print("""\
-----------------------------------------
| ROCK = 1 || PAPER = 2 || SCISSORS = 3 |
-----------------------------------------
        """)
