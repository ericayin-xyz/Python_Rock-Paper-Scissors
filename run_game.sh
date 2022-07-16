#!/bin/bash

if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2
  exit 1
fi
python3 -m ensurepip --upgrade
pip3 install -r requirements.txt

echo 'Type "./run_game.sh help" for more information.'

if [ $# -eq 1 ] && [ $1 == "help" ]; then
    cat help.txt
else
    python3 game.py
fi
