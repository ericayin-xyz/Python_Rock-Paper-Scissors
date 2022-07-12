from menu_option import MenuOption
from images import mainmenu, options_menu
from menu import Menu

option1 = MenuOption(1, mainmenu[1])
option2 = MenuOption(2, mainmenu[2])
option3 = MenuOption(3, mainmenu[3])
option4 = MenuOption(4, mainmenu[4])

menu = Menu([option1, option2, option3, option4])

sub_option1 = MenuOption(1, options_menu[1])
sub_option2 = MenuOption(2, options_menu[2])
sub_option3 = MenuOption(3, options_menu[3])

menu_options = Menu([sub_option1, sub_option2, sub_option3])
# menu.print_menu()

menu_options.print_menu()

tips = """
  ------------------------------------------------------------------------
                          RECIPE FOR FUN!
  ------------------------------------------------------------------------

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

  ------------------------------------------------------------------------
"""

 

