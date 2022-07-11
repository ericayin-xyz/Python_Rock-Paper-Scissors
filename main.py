import random
from os import system
from unicodedata import name
from images import logo, menu_image_line, menu_image, rock, paper, scissors
from player import Player


def print_options():
    opt = input("Select your option (1-4):\n")
    return opt


# ----------------------------------------------------#

# display logo + weclome str
print(logo)
print("  > > > > >  Welcome come to the Rock Paper Scissors! \n")
print(menu_image_line)
# images = [rock, paper, scissors]
user_score = 0
computer_score = 0

option = ""

while option != "3":
    option = print_options()
    system('clear')

    if option == "1":
        name1 = input("Enter your name:\n")
        new_player = Player(1, name1)
        new_player.add_play()

    elif option == "2":
        name1 = input("Player 1 -> enter your name:\n")
        newplayer1 = Player(1, name1)

        name2 = input("Player 2 -> enter your name:\n")
        newplayer2 = Player(2, name2)

        print(f"\nWelcome {name1} and {name2}, press ENTER to start")


    elif option == "3":
        continue

    else:
        print("\nInviad input")

    input("\n\nPress ENTER to continue")
    system('clear')
    print(logo)
    print(menu_image_line)
   

print("See you next time!")