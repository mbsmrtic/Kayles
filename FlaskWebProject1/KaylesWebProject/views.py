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

@app.route('/tournament/<numberOfPlayers>', methods=['POST'])
def new_tournament(numberOfPlayers):
    tourny.startTournament((int)(numberOfPlayers))
    game.gameEnabled='enabled'
    return 'Tournament started!'

@app.route('/tournamentPost', methods=['POST'])
def new_tournamentPost():
    new_tournament((int)(request.form['numberofplayers']))
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        tourny=tourny,
        game=game
    )

# new_game returns the game status
@app.route('/game/<numberofpins>', methods=['POST'])
def new_game(numberofpins):
    if (numberofpins == ''):
        numberofpins=10
    game.startGame(tourny.currentPlayers(), (int)(numberofpins))
    game.pinsEnabled='enabled'
    game.gameEnabled='enabled'
    return '''Game started!
The player who knocks down the last pin wins.
Players: {}, {}
Pins: {}'''.format(game.PLAYER1, game.PLAYER2, game.PINS), 201

@app.route('/gamePost', methods=['POST'])
def gamePost():
    numberofpins=(int)(request.form['numberofpins'])
    new_game(numberofpins)
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        gamepins='Pins: {}'.format(game.row),
        tourny=tourny,
        game=game
        )

# move returns the game status
@app.route('/move/<pin1number>/<pin2number>', methods=['POST'])
def move(pin1number, pin2number):
    game.pinsEnabled='enabled'
    if not game or game.is_ended():
        game.gameStatus='No active game. POST /game to start a new game.'
    
    try:
        if (pin2number.isdigit()):
            pins = [int(pin1number), int(pin2number)]
        else:
            pins = [int(pin1number)]
        game.move(game.turn, pins)
        game.gameStatus = "{} is up!".format(game.turn)
    except:
        game.gameStatus='Invalid move try again.'

    if (game.is_ended()):
        if (game.get_winner() == game.PLAYER1):
            tourny.removePlayer(game.PLAYER2)
        else:
            tourny.removePlayer(game.PLAYER1)
        game.pinsEnabled='disabled'
        tourny.iGameInRound += 1
    return game.gameStatus

@app.route('/move/<pin1number>', methods=['POST'])
def moveOneArg(pin1number):
    return move(pin1number, '')

@app.route('/movePost', methods=['POST'])
def movePost():
    move(request.form['pin1number'], request.form['pin2number'])
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        gamepins='Pins: {}'.format(game.row),
        tourny=tourny,
        game=game
        )




