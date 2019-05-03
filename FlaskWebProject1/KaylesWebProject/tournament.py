class Tournament(object):
    playerCount=0
    playerList=[]
    gamePlayerList=[]
    round='Round 1'

    def __init__(self, playerCount):
        self.playerCount = playerCount
        for i in range(playerCount):
            self.playerList.append('player'+ str(i))
        for i in range(0,playerCount,2):
            if (i < playerCount - 1):
                self.gamePlayerList.append('{0} vs {1}'.format(self.playerList[i], self.playerList[i+1]))
        iPlayer = 0;

    def removePlayer(self, playerName):
        self.playerList.remove(playerName)

    def removeGame(self, playersNames):
        self.gamePlayerList.remove(playersNames)
