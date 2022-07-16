#!/bin/bash

if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2
  exit 1
fi
python -m ensurepip --upgrade
pip install -r requirements.txt

echo 'You can run <./run_game.sh help>, if you need further help.'

if [ $# -eq 1 ] && [ $1 == "help" ]; then
    cat help.txt
else
    python3 game.py
fi





