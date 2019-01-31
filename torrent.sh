#!/bin/bash

clear
tadd='transmission-remote --auth transmission:transmission -a'


cd "$(dirname "$0")"

python3 getmagnet.py
state=$?

if [ $state -eq 5 ]; then
	echo "Nothing found. Exiting..."
	exit
fi

if [ $state -eq 4 ]; then
	echo "Problem getting link. Exiting..."
	exit
fi



$tadd $(cat magnet.txt)
