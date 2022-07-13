from menu_option import MenuOption
from images import mainmenu, logo

class Menu:
    # a list of menu options
    def __init__(self, menu_option):
        self.menu_option = menu_option

    def print_menu(self):
        print(logo)
        print(f"  {'> ' * 5} Welcome come to the Rock, Paper, Scissors! \n")
        for option in self.menu_option:
            option.show_option()
