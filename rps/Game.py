from Enums import MoveEnum


class Game:
    is_game_running = True
    p1_move = None
    p2_move = None
    winner = None

    def end_game(self):
        self.is_game_running = False

    def set_p1_move(self, move):
        self.p1_move = MoveEnum(move).name

    def set_p2_move(self, move):
        self.p2_move = MoveEnum(move).name

    def set_winner(self, winner):
        self.winner = winner

    @staticmethod
    def is_valid_move(move):
        valid_moves = set(str(move.value) for move in MoveEnum)
        return move in valid_moves
