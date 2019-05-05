"""
Routes and views for the flask application.
"""

from flask import Flask
from datetime import datetime
from flask import render_template
from .game import Game
from .tournament import Tournament
from flask import request
from KaylesWebProject import app
from .game import GameException

# Init paths 
@app.route('/')
@app.route('/home')
def home():
    init()
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        tourny=tourny,
        game=game
    )

@app.route('/init', methods=['POST'])
def init():
    global tourny
    global game
    tourny=Tournament(2)
    game = Game(tourny.currentPlayers(), 10)
    return 'Initted'

# New tournament paths
@app.route('/tournament',defaults={'numberOfPlayers':2}, methods=['POST','GET'])
@app.route('/tournament/<numberOfPlayers>', methods=['POST','GET'])
def new_tournament(numberOfPlayers):
    tourny.startTournament((int)(numberOfPlayers))
    return 'Tournament started!'


@app.route('/tournamentPost', methods=['POST'])
def new_tournamentPost():
    new_tournament((int)(request.form['numberofplayers']))
    game.gameEnabled='enabled'
    game.pinsEnabled='disabled'
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        tourny=tourny,
        game=game
    )

# New game paths 
# new_game returns the game status
@app.route('/game',defaults={'numberofpins':4}, methods=['POST','GET'])
@app.route('/game/<numberofpins>', methods=['POST','GET'])
def new_game(numberofpins):
    if (numberofpins == ''):
        numberofpins=10
    game.startGame(tourny.currentPlayers(), (int)(numberofpins))
    return '''Game started!
The player who knocks down the last pin wins.
Players: {}, {}
Pins: {}
Current player: {}'''.format(game.PLAYER1, game.PLAYER2, game.row, game.turn), 201

@app.route('/gamePost', methods=['POST'])
def gamePost():
    numberofpins=(int)(request.form['numberofpins'])
    new_game(numberofpins)
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        tourny=tourny,
        game=game
        )

# Move paths
# move returns the game status
@app.route('/move/<pin1number>', defaults={'pin2number':''}, methods=['POST','GET'])
@app.route('/move/<pin1number>/<pin2number>', methods=['POST','GET'])
def move(pin1number, pin2number):
    if not game or game.is_ended() or not game.started:
        game.gameStatus='No active game. POST /game to start a new game.'
        return game.gameStatus
    try:
        if (pin2number.isdigit()):
            pins = [int(pin1number), int(pin2number)]
        else:
            pins = [int(pin1number)]
        game.move(game.turn, pins)
        if (game.is_ended()):
            if (game.get_winner() == game.PLAYER1):
                tourny.removePlayer(game.PLAYER2)
            else:
                tourny.removePlayer(game.PLAYER1)
            game.pinsEnabled='disabled'
            tourny.iGameInRound += 1
    except:
        game.gameStatus='Invalid move try again.'

    retval = '''Players: {} vs {}
{}
Pins: {}
Current player: {}
{}
'''.format(game.PLAYER1, game.PLAYER2, game.gameStatus, game.row, game.turn, tourny.result)
    return retval

@app.route('/movePost', methods=['POST'])
def movePost():
    move(request.form['pin1number'], request.form['pin2number'])
    if (tourny.is_ended()):
        game.gameEnabled='disabled'
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        tourny=tourny,
        game=game
        )

# Contact and about paths
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.errorhandler(GameException)
def all_exception_handler(error):
    return error.__class__.__name__, 400




