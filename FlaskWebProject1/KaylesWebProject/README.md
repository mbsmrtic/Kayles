# About this project

This project is a test project that came from Blink. The original game was a Kayles game application that runs in the console. I extended the game functionality according to the instructions.
I created a tournament class. A tournament can take an arbitrary number of players. It assigns each player a name from player0 to playerN. The tournament calculates the first round.
A round contains a list of games 'player0 vs player1', 'player2 vs player3'...  After each game the losing player is removed from the tournament.
After the first round is complete, the second round is calculated.  
<br>
I changed play.sh to test the new tournament functionality. 
<br>
To better illustrate the functionality, I created a simple Flask based website that allows the user to hit buttons to create a tournament, start a game and submit a move.


# Original instructions

- You should expect to spend about 3 hours on this.
- We'll consider both the correctness and the clarity of your code, including things like test coverage, idiomatic use of the chosen language, and git history. Work on it until you're satisfied and feel it represents the quality of work you would produce in a professional environment.
- Be prepared to present your solution and discuss it when you arrive at Blink's office.

# Kayles

From [Wikipedia](https://en.wikipedia.org/wiki/Kayles)

> Kayles is played with a row of tokens, which represent bowling pins. The row may be of any length. The two players alternate; each player, on his or her turn, may remove either any one pin (a ball bowled directly at that pin), or two adjacent pins (a ball bowled to strike both). Under the normal play convention, a player loses when he or she has no legal move (that is, when all the pins are gone [the player who knocks down the last pin wins]).

# Blinkayles

Blinkayles is a very simple implementation of Kayles played via a REST interface. Only one game at a time is supported (no concurrency), and we assume that the client handles authentication for us.

The game has 2 endpoints:

### POST `/game`

Begin a new game

### POST `/move/<player>/<pin>[,<pin>]`

Knock down one or two pins

This app is implemented in several languages. Each language implementation has the same REST interface and similar internal implementations.

`play.sh` simulates playing a single game to completion.

# Your Mission
Your project is to extend Blinkayles with tournament functionality that can narrow a pool of N players down to 1 winner and 1 runner-up (second place).

Requirements:
- Single elimination - after each game, the winner remains in the tournament and the loser doesn’t play any more games
  - In the first round, all players compete in 1-vs-1 games. The winners of the first round games compete against each other in the second round, again in 1-vs-1 games.  This continues until the final round, when two players remain, and the winner of that game is the overall winner of the tournament.
  - https://en.wikipedia.org/wiki/Single-elimination_tournament
- Supports an arbitrary number of tournament participants, including odd numbers.
- Concurrent tournaments/games is not a requirement. It’s up to you if you’d like to support concurrent games and tournaments. You won’t be penalized for a solution that only supports one game/tournament at a time.

You'll need to extend the HTTP interface with endpoints to begin a new tournament and interact with that tournament. You don't need to preserve the existing single-game functionality.

These requirements are incomplete. Put on your product manager hat to fill in the blanks, and explain your assumptions in the readme or code comments.

The existing code is not perfect and you should feel free to change it as you see fit, however there are no serious bugs in the code.

# Github

Please git init the folder you're working on and create local commits.  Please DO NOT create a public repo with your solution.

# Delivery

Email a zip file containing your solution (including the .git folders) and instructions for running to your recruiter at least a day before your on-site interview.

Blink will provide a laptop for you to present your solution on-site. You’re also welcome to bring your own laptop.
