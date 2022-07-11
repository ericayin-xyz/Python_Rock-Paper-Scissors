from operator import index


class Player:
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def add_play(self):
        print(f"Welcome {self.name}, press ENTER to start") 


# name1 = input("Player 1 -> enter your name:\n")
# newplayer1 = Player(1, name1)

# name2 = input("Player 2 -> enter your name:\n")
# newplayer2 = Player(2, name2)

# print(f"\nWelcome {name1} and {name2}, press ENTER to start")



