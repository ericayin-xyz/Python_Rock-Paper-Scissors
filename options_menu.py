class MenuOption:
    def __init__(self, index, option):
        self.index = index
        self.option = option

    def show_option(self):
        return(f"{self.index}. {self.option}")

# type 1 - setting winning score
# score cap: 3, 5, 10

# type 2 - introduction/rules about the game
tips = """
RECIPE FOR FUN!

This is a classic and easy game. 
Type 1 for Rock, 2 for Paper or 3 for Scissors
Each player picks one of them and reveals it at the same time. 

- Rock beats Scissors
- Paper beats Rocks
- Scissors beats Paper

(fist for rock, flat hand for paper, index and middle finger for scissors)
The winner is the first one who scores 10 points. 
In a tie, the process is repeated until a winner is found.

See who wins each round!  
"""
print(tips)
 

# type 3 - back to main menu