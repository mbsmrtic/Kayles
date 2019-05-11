class TournamentException(Exception):
    pass

class TournamentNotStartedException(TournamentException):
    pass

class InvalidPlayerCountException(TournamentException):
    pass

class InvalidPlayerException(TournamentException):
    pass

class InvalidGameException(TournamentException):
    pass

#Tournament keeps track of the list of players that remain
#  in the tournament, the current round of the tournament,
#  and the list of games that will be played in the current round.
class Tournament(object):
    playerCount=0
    playerList=[]
    gamePlayerList=[]
    round=0

    def __init__(self, playerCount):
        self.startTournament(playerCount)

    # To start a tournament, we create the names of the players
    #   based on how many players there are. player1, player2...
    def startTournament(self, playerCount):
        if (playerCount < 2 or playerCount > 100):
            raise InvalidPlayerCountException()

        self.playerCount = playerCount
        self.playerList=[]
        self.gamePlayerList=[]
        self.round=0
        for i in range(playerCount):
            self.playerList.append('player'+ str(i))
        self.startNewRound()
        self.result = ''

    # To start a round, we create the list of games that will be in the round.
    # The list is actually a list of strings e.g. 'player0 vs player1'
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

    # Return the string the describes the players that are up 
    # in the current round e.g. 'player0 vs player1'
    def currentPlayers(self):
        # Have we finished this round?
        if (self.iGameInRound >= len(self.gamePlayerList)):
            self.startNewRound()
        return self.gamePlayerList[self.iGameInRound]

    # If a player has lost, here we remove them from the tournament.
    def removePlayer(self, playerName):
        if playerName not in self.playerList:
            raise InvalidPlayerException
        self.playerList.remove(playerName)
        if (len(self.playerList) == 1):
            self.result = '''{} wins the tournament! 
{} is runner up'''.format(self.playerList[0], playerName)

    # The tournament is over if there is only one player left.
    def is_ended(self):
        return (len(self.playerList) == 1)