from flask import Flask
from game import Game, GameException

app = Flask(__name__)
game = None


@app.route('/game', methods=['POST'])
def new_game():
    global game
    game = Game('playera','playerb')
    return '''Game started! <br>
The player who knocks down the last pin wins. <br>
Players: {}, {} <br>
Pins: {} <br>'''.format(Game.PLAYER1, Game.PLAYER2, Game.PINS), 201


@app.route('/move/<player>/<pins>', methods=['POST'])
def move(player, pins):
    pins = [int(x) for x in pins.split(',')]

    if not game or game.is_ended():
        return 'No active game. POST /game to start a new game.', 400
    game.move(player, pins)
    if game.is_ended():
        return '{} is the winner!'.format(game.get_winner())
    else:
        return game.__str__()


@app.errorhandler(GameException)
def all_exception_handler(error):
    return error.__class__.__name__, 400


if __name__ == '__main__':
    print('POST /game to start a new game')
    app.run(debug=True, port=4567)
