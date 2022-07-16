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


# testing #
# name1 = input("Player 1 -> enter your name:\n")
# newplayer1 = Player(1, name1)
# newplayer1.welcome_player()
# players = newplayer1.ask_choice()

