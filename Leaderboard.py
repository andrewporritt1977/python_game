class Leaderboard:
    listOfPlayers = []

    def addPlayerToList(self, player):
        self.listOfPlayers.append(player)

    def printLeaderBoard(self):
        for i in range(len(self.listOfPlayers) ): 
            print(self.listOfPlayers[i])