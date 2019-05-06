#!/bin/sh

########
# This script simulates playing a Blinkayles game
########

do_post () {
    # This is a simple wrapper for the curl command
	echo ""
	echo "$1"
	curl "$1" -X POST
	echo ""
}

PORT="4567"

do_post "http://localhost:${PORT}/init"

# 5 players in the tournament 
do_post "http://localhost:${PORT}/tournament/5"

# 4 pins in the game 
# first game player0 vs player1
do_post "http://localhost:${PORT}/game/4"
do_post "http://localhost:${PORT}/move/1"
do_post "http://localhost:${PORT}/move/2,3"
do_post "http://localhost:${PORT}/move/0"

# second game  player2 vs player3
do_post "http://localhost:${PORT}/game/4"
do_post "http://localhost:${PORT}/move/3"
do_post "http://localhost:${PORT}/move/0,1"
do_post "http://localhost:${PORT}/move/2"

#third game player0 vs player2
do_post "http://localhost:${PORT}/game/4"
do_post "http://localhost:${PORT}/move/1,2"
do_post "http://localhost:${PORT}/move/3"
do_post "http://localhost:${PORT}/move/0"

#fourth game  player0 vs player4
do_post "http://localhost:${PORT}/game/4"
do_post "http://localhost:${PORT}/move/1"
do_post "http://localhost:${PORT}/move/2,3"
do_post "http://localhost:${PORT}/move/0"

read -p "Press enter to continue"
