"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from KaylesWebProject import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '4567'))
    except ValueError:
        PORT = 4567
    app.run(HOST, PORT)
