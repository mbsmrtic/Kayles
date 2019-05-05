class GameException(Exception):
    pass


class InvalidMoveException(GameException):
    pass


class InvalidTurnException(GameException):
    pass


class Game(object):
    PLAYER1, PLAYER2 = 'player1', 'player2'
    PINS = 10

    def __init__(self, players, pinCount):
        self.startGame(players, pinCount)
        self.gameStatus='Game not started'
        self.gameEnabled='disabled'
        self.pinsEnabled='disabled'
        self.started=False

    def startGame(self, players, pinCount):
        self.players = players
        playersList = players.split(' vs ')
        self.PLAYER1 = playersList[0]
        self.PLAYER2 = playersList[1]
        self.PINS = pinCount
        self.row = Row(self.PINS)
        self.turn = self.PLAYER1
        # We won't enable the game buttons until the user has started a tournament
        self.gameEnabled='enabled'
        self.pinsEnabled='enabled'
        self.gameStatus='Game started'
        self.started=True
        

    def move(self, player, pins):
        self.gameStatus='Game in progress'
        if player != self.turn:
            raise InvalidTurnException()

        if len(pins) == 1:
            self.row.knockdown(pins[0])
        elif len(pins) == 2:
            self.row.knockdown(pins[0], pins[1])
        else:
            raise InvalidMoveException()
        self.update_turn()

    def update_turn(self):
        if self.is_ended():
            return

        if self.turn == self.PLAYER1:
            self.turn = self.PLAYER2
        else:
            self.turn = self.PLAYER1

    def is_ended(self):
        if (self.row.get_pins_left() == 0):
            self.gameStatus='Game ended'
            return True

    def get_winner(self):
        if self.is_ended():
            self.gameStatus='{} is the winner!'.format(self.turn)
            return self.turn
        else:
            return None

    def __str__(self):
        return self.row.__str__()


class Row(object):
    def __init__(self, length):
        self.pins = [True for i in range(length)]

    def __str__(self):
        return ''.join(['!' if x else 'x' for x in self.pins])

    def knockdown(self, index1, index2=None):
        try:
            if not self.pins[index1]:
                raise InvalidMoveException()


            if index2:
                if abs(index1 - index2) != 1:
                    raise InvalidMoveException()

                if not self.pins[index2]:
                    raise InvalidMoveException()

                self.pins[index2] = False
            self.pins[index1] = False
        except IndexError:
            raise InvalidMoveException()

    def get_pins_left(self):
        return self.pins.count(True)
