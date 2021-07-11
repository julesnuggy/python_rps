class Player:

    score = 0

    def __init__(self, name, is_p1, is_cpu_player):
        self.name = name
        self.is_p1 = is_p1
        self.is_cpu_player = is_cpu_player

    def add_to_score(self):
        self.score += 1
