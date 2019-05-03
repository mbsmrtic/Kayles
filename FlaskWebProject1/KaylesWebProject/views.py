"""
Routes and views for the flask application.
"""

from datetime import datetime
import KaylesWebProject
from flask import render_template
from KaylesWebProject import app
from .game import Game
from .tournament import Tournament
from flask import request

class TestClass(object):
    anystring = "anyStringValue"
    secondString = "secondStringValue"

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    global tourny
    global testClass
    tourny=Tournament(2)
    testClass = TestClass()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        gameenabled='disabled',
        pinsenabled='disabled',
        testClass=testClass,
        tourny=tourny
    )

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

@app.route('/tournament', methods=['POST'])
def new_tournament():
    numberOfPlayers = (int)(request.form['numberofplayers'])
    tourny = Tournament(numberOfPlayers)
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        gameenabled='enabled',
        numberofpins=10,
        pinsenabled='disabled',
        playersLeft=tourny.playerList,
        roundName=tourny.round,
        gamePlayerList=tourny.gamePlayerList,
        testClass=testClass
    )

@app.route('/game', methods=['POST'])
def new_game():
    global game
    global tourny
    numberOfPins = (int)(request.form['numberofpins'])
    gamestatus='Game started'
    #If we don't already have a tournament, create one.
    try: tourny
    except: 
        tourny = Tournament(2)
    if (numberOfPins == ''):
        numberOfPins=10
    game = Game(tourny.playerList[0], tourny.playerList[1], numberOfPins)
    playersLeft=tourny.playerList

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        gamestatus='Game started',
        gameplayers='Players: {},{}'.format(game.PLAYER1, game.PLAYER2),
        gamepins='Pins: {}'.format(game.row),
        gamenabled='enabled',
        currentplayer=game.PLAYER1,
        playersLeft=playersLeft,
        pinsenabled='enabled',
        numberofpins=game.PINS,
        testClass=testClass
        )

@app.route('/moove', methods=['POST'])
def moove():
    pin1number = request.form['pin1number']
    pin2number = request.form['pin2number']
    gamestatus = 'Game in progress'
    gameenabled = 'enabled'
    if not game or game.is_ended():
        gamestatus='No active game. POST /game to start a new game.'
    
    try:
        if (pin2number.isdigit()):
            pins = [int(pin1number), int(pin2number)]
        else:
            pins = [int(pin1number)]
        game.move(game.turn, pins)
    except:
        gamestatus='Invalid move try again.'
    if (game.is_ended()):
        gamestatus='{} is the winner!'.format(game.get_winner())
        if (game.get_winner() == game.PLAYER1):
            tourny.removePlayer(game.PLAYER2)
        else:
            tourny.removePlayer(game.PLAYER1)
        gameenabled='disabled'

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        gamestatus=gamestatus,
        gameplayers='Players: {},{}'.format(game.PLAYER1, game.PLAYER2),
        gamepins='Pins: {}'.format(game.row),
        currentplayer=game.turn,
        gameenabled=gameenabled,
        pinsenabled=gameenabled,
        playersLeft=tourny.playerList,
        numberofpins=game.PINS,
        testClass=testClass
        )



@app.route('/move/<player>/<pins>')
def move(player, pins):
    pins = [int(x) for x in pins.split(',')]

    gamestatus='Game in progress'
    if not game or game.is_ended():
        gamestatus='No active game. POST /game to start a new game.'
    
    game.move(player, pins)
    if (game.is_ended()):
        gamestatus='{} is the winner!'.format(game.get_winner())
    #else:
    #    gamestatus = game.__str__()

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        gamestatus=gamestatus,
        gameplayers='Players: {},{}'.format(game.PLAYER1, game.PLAYER2),
        gamepins='Pins: {}'.format(game.row),
        currentplayer=game.turn,
        playersLeft=tourny.playerList
        )
