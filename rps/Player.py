class Player:

    score = 0

    def __init__(self, name):
        self.name = name

    def add_to_score(self):
        self.score += 1
