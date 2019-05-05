class TournamentException:
    pass


class Tournament(object):
    playerCount=0
    playerList=[]
    gamePlayerList=[]
    round=0

    def __init__(self, playerCount):
        self.startTournament(playerCount)

    def startTournament(self, playerCount):
        self.playerCount = playerCount
        self.playerList=[]
        self.gamePlayerList=[]
        self.round=0
        for i in range(playerCount):
            self.playerList.append('player'+ str(i))
        self.startNewRound()
        self.result = ''

    def startNewRound(self):
        self.iGameInRound = 0
        self.gamePlayerList = []
        if (len(self.playerList) == 1):
            self.startTournament(self.playerCount)
        else:
            self.playerCount = len(self.playerList)
        for i in range(0, self.playerCount, 2):
            if (i < self.playerCount - 1):
                self.gamePlayerList.append('{0} vs {1}'.format(self.playerList[i], self.playerList[i+1]))
        self.round += 1

    def currentPlayers(self):
        # Have we finished this round?
        if (self.iGameInRound >= len(self.gamePlayerList)):
            self.startNewRound()
        return self.gamePlayerList[self.iGameInRound]

    def removePlayer(self, playerName):
        self.playerList.remove(playerName)
        if (len(self.playerList) == 1):
            self.result = '''{} wins the tournament! 
{} is runner up'''.format(self.playerList[0], playerName)

    def removeGame(self, playersNames):
        self.gamePlayerList.remove(playersNames)

    def is_ended(self):
        return (len(self.playerList) == 1)