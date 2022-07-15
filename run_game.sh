#!/bin/bash
if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2
  exit 1
else 
    echo 'you have python3'
fi


if python -c "import art" &> /dev/null; then
    echo 'Type <pip install -r requirements.txt> to install packages'
    exit 1
else
    echo 'you have all packages'
fi


if python -c "import bullet" &> /dev/null; then
    echo 'Type <pip install -r > to install packages'
    exit 1
else
    echo 'you have all packages'
fi


if [ $# -eq 1 ] && [ $1 == "help" ]; then
    cat help.txt
else
    python3 game.py
fi

