class Player:
    score = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name + " " + str(self.score)

    def addToScore(self, value):
        self.score += value