

# def _add_players(i):
#     player12 = input(f"Player {i} -> enter your name:\n")
#     return player12

# def newplayers():
#     player1 = _add_players(1)
#     player2 = _add_players(2)
#     print(f"\nWelcome {player1} and {player2} !")

# name1 = _add_players(1)
# name2 = _add_players(2)

# newplayers()
# -----------

from secrets import choice
from unittest import result


class Player:
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def welcome_player(self):
        print(f"\nWelcome {self.name}!\n") 

    def ask_choice(self):
        choice = input(f"Make your choice, {self.name}!\n")
        return choice



# name1 = input("Player 1 -> enter your name:\n")
# newplayer1 = Player(1, name1)
# newplayer1.welcome_player()
# cc = newplayer1.ask_choice()

