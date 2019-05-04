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
do_post "http://localhost:${PORT}/tournament/2"
do_post "http://localhost:${PORT}/game/10"
do_post "http://localhost:${PORT}/move/1"
do_post "http://localhost:${PORT}/move/5/6"
do_post "http://localhost:${PORT}/move/7"
do_post "http://localhost:${PORT}/move/3/4"
do_post "http://localhost:${PORT}/move/0"
do_post "http://localhost:${PORT}/move/2"
do_post "http://localhost:${PORT}/move/8/9"

read -p "Press enter to continue"
