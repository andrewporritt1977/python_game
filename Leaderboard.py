from operator import attrgetter

class Leaderboard:
    listOfPlayers = []

    def addPlayerToList(self, player):
        self.listOfPlayers.append(player)

    def printLeaderBoard(self):
        print ("********************")
        print ("**  Leaderboard  **")
        print ("********************")

        sortedListOfPlayers = sorted(self.listOfPlayers, key=attrgetter('score'), reverse=True)

        for i in range(len(sortedListOfPlayers) ): 
            print(sortedListOfPlayers[i])